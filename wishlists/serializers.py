from rest_framework.serializers import ModelSerializer
from rooms.serializers import RoomListSerializer
from .models import Wishlist


class WishListSerializer(ModelSerializer):
    rooms = RoomListSerializer(
        many=True,
        read_only=True,  # don't want user to send room when creating wishlist
    )

    class Meta:
        model = Wishlist
        fields = (
            "name",
            "rooms",
        )
