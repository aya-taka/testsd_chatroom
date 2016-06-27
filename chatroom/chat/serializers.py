from swampdragon.serializers.model_serializer import ModelSerializer


class UserSerializer(ModelSerializer):
    class Meta:
        model = 'auth.User'
        publish_fields = ('username',)


class CommentListSerializer(ModelSerializer):
    class Meta:
        model = 'chat.Comment'
        # フロントから参照することのできる情報の定義
        publish_fields = ('text', 'room', 'authid')
        # フロントから更新することのできる情報の定義
        # フロントからcreateなどするときに、最低限渡す必要がある情報
        update_fields = ('text', 'room', 'authid', )


class RoomListSerializer(ModelSerializer):
    class Meta:
        model = 'chat.Room'
        publish_fields = ('name', 'des', 'authid')
        update_fields = ('name', 'des', 'authid', )


class RoomResistSerializer(ModelSerializer):
    class Meta:
        model = 'chat.RoomResist'
        publish_field = ('user', 'room', 'is_read')
        update_fields = ('user', 'room', 'is_read', )
