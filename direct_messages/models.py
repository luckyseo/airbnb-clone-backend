from django.db import models
from common.models import CommonModel

# Create your models here.


class ChattingRoom(CommonModel):
    """Messageroom for Room model definiton"""

    users = models.ManyToManyField(
        "users.User",
    )

    def __str__(self):
        return "Chatting Room"


"""
Room models error occur-> room.Room and dm.room -> both connected to users model is the real problem
"""


class Message(CommonModel):
    """Message Model Definition"""

    text = models.TextField()
    user = models.ForeignKey(
        "users.User",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )
    room = models.ForeignKey(
        "direct_messages.ChattingRoom",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"{self.user} says {self.text}"
