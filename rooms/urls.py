from . import views
from django.urls import path

urlpatterns = [
    path("amenities/", views.Amenities.as_view()),
    path("amenities/<int:pk>", views.AmenitiesDetail.as_view()),
]
