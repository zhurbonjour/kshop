from .models import Review
from rest_framework import serializers


class ReviewsSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()

    class Meta:
        model = Review
        fields = "__all__"
