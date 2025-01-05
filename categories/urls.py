from django.urls import path
from . import views

urlpatterns = [
    path("", views.Categories.as_view()),  # as_view() -> to call class
    path("<int:pk>", views.CategoryDetail.as_view()),
]
