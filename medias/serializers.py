from rest_framework.serializers import ModelSerializer
from .models import Photo


class PhotoSerializer(ModelSerializer):
    class Meta:
        model = Photo
        fields = (
            "pk",  # Model Serializer config - pk is read_only
            "file",
            "description",
        )
