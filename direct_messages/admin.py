from django.contrib import admin
from .models import ChattingRoom, Message

# Register your models here.


@admin.register(ChattingRoom)
class ChattingRoomAdmin(admin.ModelAdmin):
    pass


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = (
        "__str__",
        "created_at",
        "updated_at",
    )
    list_filter = (
        "text",
        "user",
        "created_at",
    )
