from django.db import models
from common.models import CommonModel


# Create your models here.
class Room(CommonModel):
    class RoomKindChoices(models.TextChoices):
        ENTIRE_PLACE = ("entire_place", "Entire Place")
        PRIVATE_ROOM = ("private_room", "Private Room")
        SHARED_ROOM = ("shared_room", "Shared Room")

    name = models.CharField(
        max_length=150,
    )
    country = models.CharField(
        max_length=50,
        default="한국",
    )
    city = models.CharField(
        max_length=80,
        default="서울",
    )
    price = models.PositiveIntegerField()
    rooms = models.PositiveIntegerField()
    toilets = models.PositiveIntegerField()
    description = models.TextField(
        max_length=150,
    )
    address = models.CharField(
        max_length=250,
    )
    pet_friendly = models.BooleanField(
        default=False,
    )
    kind = models.CharField(
        max_length=20,
        choices=RoomKindChoices.choices,
    )
    owner = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
    )
    amenities = models.ManyToManyField(
        "rooms.Amenity",
    )
    category = models.ForeignKey(
        "categories.Category",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )

    """
    one to many : e.g an owner has many rooms
    many to many : e.g a room has many amenities & a amenity belongs to many rooms
    """

    def __str__(self):  # show name variable of the instance isntead of object addr
        return self.name

    # many to many rel


class Amenity(CommonModel):
    name = models.CharField(
        max_length=150,
    )
    description = models.CharField(
        max_length=150,
        null=True,  # null in db
        blank=True,  # website blank
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Amenities"
        """
         if you already have an app changing the name of the model will not be easy
         since you already have data under a model there. 
         It will also break your code.
        """
