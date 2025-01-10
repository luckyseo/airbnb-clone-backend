"""
GET PUT/me - allow users to change thier name - private
GET /users/username for public profile when u see another user's profile
POST /users
POST /users/log-in
POST /users/change-password
POST /users/github - after frontend build
"""

from django.urls import path
from . import views

urlpatterns = [path("me", views.Me.as_view())]
