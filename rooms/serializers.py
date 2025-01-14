from rest_framework.serializers import ModelSerializer
from .models import Amenity, Room
from users.serializers import UserSerializer
from categories.serializers import CategorySerializer


class AmenitySerializer(ModelSerializer):
    class Meta:
        model = Amenity
        fields = (
            "name",
            "description",
        )


class RoomListSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = (
            "pk",
            "name",
            "country",
            "city",
            "price",
        )


class RoomDetailSerializer(ModelSerializer):
    # instead of using depth=1, by using serializer, u arrange scope of details it need to be exposed
    owner = UserSerializer(read_only=True)
    amenities = AmenitySerializer(
        read_only=True, many=True
    )  # many=True - show objects in list type
    category = CategorySerializer(read_only=True)
    # because above attributes have relationships, those need manual save or connect

    class Meta:
        model = Room
        fields = "__all__"

    #  depth = 1  # expanding relation easily


"""
    # from serializer.save() 
    def create(self, validated_data): no need to overwrite
        return Room.objects.create(**validated_data)

"""
