from django.contrib import admin
from .models import House
# Register your models here.

@admin.register(House)#아래 클래스가 HouseModel control
class HouseAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'price_per_night',
        'address','pets_allowed',
    )
    list_filter=(
        'price_per_night',
        'pets_allowed'
    )
    search_fields=("address",)  #if onle one element in tuple, put comma in the end
    #address__startswith.contains, ...
