from django.db import models
from common.models import CommonModel

# Create your models here.


class Category(CommonModel):
    class CategoryKindChocies(models.TextChoices):
        ROOMS = "rooms", "Rooms"
        EXPERIENCES = "experiences", "Experiences"

    name = models.CharField(
        max_length=50,
    )
    kind = models.CharField(
        max_length=15,
        choices=CategoryKindChocies.choices,
    )

    def __str__(self):
        return f"{self.kind}: {self.name}"

    class Meta:
        verbose_name_plural = "Categories"
