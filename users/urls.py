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

urlpatterns = [
    path("", views.Users.as_view()),
    path("me", views.Me.as_view()),  # path order matters!
    path("change-password", views.ChangePassword.as_view()),
    path("log-in", views.LogIn.as_view()),
    path("log-out", views.LogOut.as_view()),
    path("@<str:username>", views.PublicUser.as_view()),
]
