from .models import Review
from rest_framework import serializers


class IDRequestSerializer(serializers.Serializer):
    id = serializers.IntegerField()


class ReviewsSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()

    class Meta:
        model = Review
        fields = "__all__"
