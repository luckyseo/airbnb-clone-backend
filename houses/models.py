from django.db import models

# Create your models here.

class House(models.Model):
    """
    Model definitons for houses
    """
    name = models.CharField(max_length=140)#길이제한할떄
    price_per_night = models.PositiveIntegerField()
    description = models.TextField()#구체적인게 좋음
    address = models.CharField(max_length=140)
    pets_allowed = models.BooleanField(default=True, help_text="Does this house allow pets?")

    def __str__(self):
        return self.name