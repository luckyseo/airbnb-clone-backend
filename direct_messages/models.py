from django.db import models
from common.models import CommonModel
# Create your models here.

class ChattingRoom(CommonModel):
    """Messageroom for Room model definiton"""
    users = models.ManyToManyField(
        "users.User",
    )
"""
Room models error occur-> room.Room and dm.room -> both connected to users model is the real problem
"""
class Message(CommonModel):
    """Message Model Definition"""
    text= models.TextField()
    user = models.ForeignKey(
        "users.User",
        on_delete=models.SET_NULL,
    )
    room = models.ForeignKey(
        "direct_messages.Room",
        on_delete=models.CASCADE,
    )