# permissions.py
from rest_framework.authentication import BaseAuthentication
from users.models import User
from rest_framework.exceptions import AuthenticationFailed


class TrustMeBroAuthentication(BaseAuthentication):
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
