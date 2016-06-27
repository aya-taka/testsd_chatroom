from django.db import models
from django.shortcuts import render, get_object_or_404, redirect
from swampdragon.models import SelfPublishModel
from .serializers import CommentListSerializer, RoomListSerializer, RoomResistSerializer


class Room(SelfPublishModel, models.Model):
    serializer_class = RoomListSerializer
    authid = models.IntegerField()
    name = models.CharField(max_length=100)
    des = models.TextField()

    def __str__(self):
        return self.name


class RoomResist(SelfPublishModel, models.Model):
    serializer_class = RoomResistSerializer
    user = models.IntegerField()
    room = models.IntegerField()
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return "{}".format(self.is_read)


class Comment(SelfPublishModel, models.Model):
    serializer_class = CommentListSerializer
    authid = models.IntegerField()
    # room = models.IntegerField()
    room = models.ForeignKey(Room, related_name="comment")
    text = models.TextField()

    def __str__(self):
        return self.text