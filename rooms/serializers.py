from rest_framework.serializers import ModelSerializer
from .models import Amenity, Room
from users.serializers import UserSerializer
from categories.serializers import CategorySerializer
from rest_framework import serializers
from medias.serializers import PhotoSerializer


class AmenitySerializer(ModelSerializer):
    class Meta:
        model = Amenity
        fields = (
            "name",
            "description",
        )


class RoomListSerializer(ModelSerializer):
    rating = serializers.SerializerMethodField()
    photos = PhotoSerializer(many=True, read_only=True)

    def get_rating(self, room):
        return room.rating()

    class Meta:
        model = Room
        fields = (
            "pk",
            "name",
            "country",
            "city",
            "price",
            "rating",
            "photos",
        )


class RoomDetailSerializer(ModelSerializer):
    # instead of using depth=1, by using serializer, u arrange scope of details it need to be exposed
    owner = UserSerializer(read_only=True)
    amenities = AmenitySerializer(
        read_only=True, many=True
    )  # many=True - show objects in list type
    category = CategorySerializer(read_only=True)
    # because above attributes have relationships, those need manual save or connect
    rating = serializers.SerializerMethodField()
    is_owner = serializers.SerializerMethodField()
    photos = PhotoSerializer(many=True, read_only=True)

    class Meta:
        model = Room
        fields = "__all__"

    def get_rating(self, room):
        return room.rating()

    def get_is_owner(self, room):
        request = self.context["request"]
        return room.owner == request.user

    #  depth = 1  # expanding relation easily


"""
    # from serializer.save() 
    def create(self, validated_data): no need to overwrite
        return Room.objects.create(**validated_data)

"""
