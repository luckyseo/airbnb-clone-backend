from django.urls import path
from . import views

"""
    path("", views.Categories.as_view()),  # as_view() -> to call class
    path("<int:pk>", views.CategoryDetail.as_view()),
"""
urlpatterns = [
    path(
        "",
        views.CategoryViewSet.as_view(
            {
                "get": "list",
                "post": "create",
            }
        ),
    ),
    path(
        "<int:pk>",  # name has to be pk
        views.CategoryViewSet.as_view(
            {
                "get": "retrieve",  # pk is required for retrieve method
                "put": "partial_update",
                "delete": "destroy",
            }
        ),
    ),
]
