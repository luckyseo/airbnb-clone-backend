from rest_framework import serializers
from .models import Category


# serializer: what to show & how it is translated
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            "name",
            "kind",
            # "__all__"
        )
        # or exclude =()
