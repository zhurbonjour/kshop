from rest_framework import serializers
from .models import Good, Category, Collection, Image


class CategoriesSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()

    class Meta:
        model = Category
        fields = "__all__"


class GoodsSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    category = CategoriesSerializer(read_only=True)

    class Meta:
        model = Good
        fields = "__all__"


class CollectionsSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()

    class Meta:
        model = Collection
        fields = "__all__"


class IDRequestSerializer(serializers.Serializer):
    id = serializers.IntegerField()


class ImageSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()

    class Meta:
        model = Image
        fields = "__all__"


class CharacteristicsSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()

    class Meta:
        model = Image
        fields = "__all__"
