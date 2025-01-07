from django.urls import path
from . import views

urlpatterns = [
    path("perks/", views.Perks.as_view()),
    path("perks/<int:pk>", views.PerkDetails.as_view()),
]
