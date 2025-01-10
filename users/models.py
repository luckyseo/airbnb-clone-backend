from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
# models.Models안함 - why? : 장고 user다 상속받을라고 , 처음부터X
class User(AbstractUser):

    class GenderChoices(models.TextChoices):
        MALE = ("male", "Male")
        """
        blabla = ("db","show up on the website")
        """
        FEMALE = ("female", "Female")

    class LanguageChoices(models.TextChoices):
        KR = ("kr", "Korean")
        EN = ("en", "English")

    class CurrencyChoices(models.TextChoices):
        WON = "won", "Korean Won"
        USD = "usd", "Dollar"

    first_name = models.CharField(max_length=150, editable=False)
    last_name = models.CharField(
        max_length=150, editable=False
    )  # editable - show on admin panel?
    name = models.CharField(max_length=150, default="")
    is_host = models.BooleanField(default=False)  # null=True: existing users :NULL

    avatar = models.URLField(blank=True)  # not required default img
    # cmd poetry add Pillow
    gender = models.CharField(max_length=10, choices=GenderChoices.choices)
    language = models.CharField(max_length=2, choices=LanguageChoices.choices)
    currency = models.CharField(max_length=5, choices=CurrencyChoices.choices)
