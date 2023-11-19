from rest_framework import serializers
from .models import Good, Category


class GoodsSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    category = CategoriesSerializer()

    class Meta:
        model = Good
        fields = "__all__"


class CategoriesSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()

    class Meta:
        model = Category
        fields = "__all__"
