from django.db import models
from common.models import CommonModel

# Create your models here.


class Wishlist(CommonModel):
    title = models.CharField(
        max_length=100,
    )
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
    )
    rooms = models.ManyToManyField(
        "rooms.Room",
    )
    experiences = models.ManyToManyField(
        "experiences.Experience",
    )

    def __str__(self):
        return self.title
