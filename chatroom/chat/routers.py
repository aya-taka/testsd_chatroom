import os
from swampdragon import route_handler
from swampdragon.route_handler import ModelRouter
from django.shortcuts import render, get_object_or_404, redirect
from .models import Comment, Room, RoomResist
from django.contrib.auth.models import User
from .serializers import CommentListSerializer, RoomListSerializer, UserSerializer, RoomResistSerializer


class UserRouter(ModelRouter):
    route_name = 'user-route'
    serializer_class = UserSerializer
    model = 'auth.User'

    def get_object(self, **kwargs):
        return self.connection.user

    def get_query_set(self, **kwargs):
        pass


class RoomRouter(ModelRouter):
    route_name = 'room-route'
    serializer_class = RoomListSerializer
    model = Room

    def get_initial(self, verb, **kwargs):
        kwargs['user'] = self.connection.user
        return kwargs

    def get_subscription_contexts(self, **kwargs):
        kwargs['user'] = self.connection.user
        return kwargs

    def get_object(self, **kwargs):
        #kwargs['room'] = self.model.objects.get(pk=kwargs['id'])
        return self.model.objects.get(pk=kwargs['id'])

    def get_query_set(self, **kwargs):
        # return self.model.objects.filter(room__id=kwargs['room_id'])
        return self.model.objects.all()

    def create(self, **kwargs):
        newroom = Room(name=kwargs["name"], des=kwargs["des"])
        newroom.authid = self.connection.user.id
        newroom.save()

        '''
        allusers = User.objects.count()
        # print(allusers)
        for i in range(1, allusers+1):
            RoomResist(user=i, room=newroom.id).save()
        '''



class CommentRouter(ModelRouter):
    route_name = 'comment-route'
    serializer_class = CommentListSerializer
    model = Comment

    def get_object(self, **kwargs):
        return self.model.objects.get(pk=kwargs['id'])

    def get_query_set(self, **kwargs):
        # print(self.model.objects.filter(room=kwargs['room_id'])[1].text)
        return self.model.objects.filter(room=kwargs['room_id'])
        # return self.model.objects.all()

    def create(self, **kwargs):
        # auth = RoomResist(room=kwargs["room"], user=kwargs["authid"])
        # auth.save()
        # print(kwargs["room"])
        auth, created = RoomResist.objects.get_or_create(user=self.connection.user.id, room=kwargs["room"])
        if auth.is_read:
            # print(auth.is_read)
            pass
        else:
            auth.is_read = True
        auth.save()

        comment = Comment()
        comment.room = get_object_or_404(Room, pk=kwargs["room"])
        comment.authid = self.connection.user.id
        comment.text = kwargs['text']

        comment.save()


class RoomRegistRouter(ModelRouter):
    route_name = 'regist-route'
    serializer_class = RoomResistSerializer
    model = RoomResist

    def get_object(self, **kwargs):
        obj, created = self.model.objects.get_or_create(user=self.connection.user.id, room=kwargs['room_id'])
        return obj

    def get_query_set(self, **kwargs):
        # print(self.model.objects.filter(room=kwargs['room_id'])[1].text)
        return self.model.objects.filter(user=kwargs['user_id'])
        # return self.model.objects.all()

route_handler.register(UserRouter)
route_handler.register(RoomRouter)
route_handler.register(CommentRouter)
route_handler.register(RoomRegistRouter)