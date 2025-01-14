from rest_framework.serializers import ModelSerializer
from .models import Perk


class PerkSerializer(ModelSerializer):
    class meta:
        model = "Perk"
        field = "__all__"
