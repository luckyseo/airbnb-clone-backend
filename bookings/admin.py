from django.contrib import admin
from .models import Booking


# Register your models here.
@admin.register(Booking)
class Booking(admin.ModelAdmin):
    pass