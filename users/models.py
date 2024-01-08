from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
#models.Models안함 : 장고 user다 상속받을라고 , 처음부터X
class User(AbstractUser):
    first_name=models.CharField(max_length=150,editable=False)
    last_name=models.CharField(max_length=150, editable=False)
    name = models.CharField(max_length=150,default="")
    is_host = models.BooleanField(default=False)#null=True: existing users :NULL
