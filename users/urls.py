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
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("", views.Users.as_view()),  # when ppl go to /users and do nothing else
    path("me", views.Me.as_view()),  # path order matters!
    path("change-password", views.ChangePassword.as_view()),
    path("log-in", views.LogIn.as_view()),
    path("log-out", views.LogOut.as_view()),
    path("token-login", obtain_auth_token),  # send username/pw -> gives token
    path("jwt-login", views.JWTLogIn.as_view()),
    path("@<str:username>", views.PublicUser.as_view()),
]
