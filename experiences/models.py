from django.db import models
from common.models import CommonModel

# Create your models here.


class Experience(CommonModel):
    country = models.CharField(
        max_length=50,
        default="한국",
    )
    city = models.CharField(
        max_length=80,
        default="서울",
    )
    name = models.CharField(
        max_length=250,
    )
    host = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
    )
    price = models.PositiveIntegerField(
        default="",
    )
    address = models.CharField(
        max_length=250,
        default="",
    )
    start = models.TimeField()
    end = models.TimeField()
    description = models.TextField()
    perks = models.ManyToManyField(
        "experiences.Perk",
    )

    def __str__(self):
        return self.name


class Perk(CommonModel):
    """
    What is included on an Experience
    """

    name = models.CharField(
        max_length=100,
    )
    details = models.CharField(
        max_length=250,
        blank=True,  # not always have description
        default="",  # or null = True
    )
    explanation = models.TextField(
        blank=True,
        default="",
    )

    def __str__(self):
        return self.name
