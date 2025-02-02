from django.db import models
from common.models import CommonModel

# Create your models here.


class Booking(CommonModel):
    """booking model Definition"""

    class BookingKindChoices(models.TextChoices):
        ROOM = "room", "Room"
        EXPERIENCE = "experience", "Experience"

    kind = models.CharField(
        max_length=15,
        choices=BookingKindChoices.choices,
    )
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
    )
    room = models.ForeignKey(
        "rooms.Room",
        null=True,
        blank=True,  # for django admin form
        on_delete=models.SET_NULL,  # we might need to leave booking history
    )
    experience = models.ForeignKey(
        "experiences.experience",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    
    )
    check_in = models.DateField(null=True, blank=True,)
    check_out = models.DateField(null=True, blank=True,)
    experience_time = models.DateTimeField(null=True, blank=True)
    guests = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.kind.title} for: {self.user}"
