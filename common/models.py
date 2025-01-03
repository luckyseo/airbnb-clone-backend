from django.db import models


# Create your models here.
class CommonModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:  # not upload this model on the database
        abstract = True
