from django.contrib import admin
from .models import Comment, Room, RoomResist

# Register your models here.
admin.site.register(Comment)
admin.site.register(Room)
admin.site.register(RoomResist)