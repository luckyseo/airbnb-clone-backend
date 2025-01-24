# permissions.py
from rest_framework.authentication import BaseAuthentication
from users.models import User
from rest_framework.exceptions import AuthenticationFailed
import jwt
from django.conf import settings


class TrustMeBroAuthentication(BaseAuthentication):  # config authentication practice!
    def authenticate(self, request):  # u find user if no user -> not logged in
        # print(request.headers)
        username = request.header.get("trust-me")
        if not username:
            return None
        try:
            user = User.objects.get(username=username)
            return (user, None)  # this is rule (usr, None)
        except User.DoesNotExist:
            raise AuthenticationFailed(f"no user {username}")


class JWTAuthentication(BaseAuthentication):  # decode token
    def authentication(self, request):
        # print(request.headers)
        token = request.headers.get("Jwt")
        if not token:
            return None  # user doesn't want authenticate
        decoded = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=["HS256"],
        )

        pk = decoded.get("pk")
        # print(decode)  # shows {pk:""}
        if not pk:
            raise AuthenticationFailed("invalid token")
        try:
            user = User.objects.get(pk=pk)
            return (user, None)  # this goes to request.user
        except User.DoesNotExist:
            raise AuthenticationFailed("User not Found")
