from django.contrib import admin
from .models import Review

# Register your models here.


@admin.register(Review)  # review is controlled by the class below
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        "__str__",
        "payload",
    )
    list_filter = ("rating",)
