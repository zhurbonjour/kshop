"""
+q/shop/category - получение всех категорий
+q/shop/collections - получение всех коллекций
+q/shop/good/id - получение товара с id 
+q/shop/goods - получение актуальных товаров 
+q/shop/archive-goods - получене архивных товаров
+q/shop/get-favorite-images - получение картинок для слайдера
+q/shop/images - получение картинок по id товара
/posts/ - получение последних 3-х постов для отрисовки на главной
"""
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from .queries import (
    goods_queries,
    categories_queries,
    images_queries,
    characteristic_queries,
)
from .serializers import (
    CollectionsSerializer,
    GoodsSerializer,
    IDRequestSerializer,
    CategoriesSerializer,
    ImageSerializer,
    CharacteristicsSerializer,
)
from drf_yasg.utils import swagger_auto_schema


class GoodsAPIView(ListAPIView):
    """
    Получение всех продаваемых активных товаров
    """

    queryset = goods_queries.get_goods_in_stock()
    serializer_class = GoodsSerializer()
    permission_classes = [AllowAny]

    @swagger_auto_schema(responses={200: GoodsSerializer(many=True)})
    def get(self, request):
        queryset = self.get_queryset()
        serializer = GoodsSerializer(queryset, many=True)
        return Response(serializer.data)


class ArchiveGoodsAPIView(ListAPIView):
    """
    Получение архивных товаров
    """

    queryset = goods_queries.get_archive_goods()
    serializer_class = GoodsSerializer()
    permission_classes = [AllowAny]

    @swagger_auto_schema(responses={200: GoodsSerializer(many=True)})
    def get(self, request):
        queryset = self.get_queryset()
        serializer = GoodsSerializer(queryset, many=True)
        return Response(serializer.data)


class SelectedGoodAPIView(APIView):
    """
    Получение выбранного товара по его id
    """

    permission_classes = [AllowAny]

    @swagger_auto_schema(
        responses={
            200: GoodsSerializer(many=True),
            404: "nothing found",
            422: "bad request params",
        },
    )
    def get(self, request, id):
        data = {"id": id}
        inserializer = IDRequestSerializer(data=data)
        if inserializer.is_valid():
            identifier = inserializer.data["id"]
            try:
                good = goods_queries.get_good_by_id(identifier)
                serializer = GoodsSerializer(instance=good)
                return Response(serializer.data)
            except ObjectDoesNotExist:
                return Response(status=404, data={"error": "nothing found"})
        else:
            return Response(status=422, data={"error": "bad request params"})


class CategoriesAPIView(ListAPIView):
    """
    Получение всех категорий товаров
    """

    queryset = categories_queries.get_all_categories()
    serializer_class = CategoriesSerializer()
    permission_classes = [AllowAny]

    @swagger_auto_schema(responses={200: CategoriesSerializer(many=True)})
    def get(self, request):
        queryset = self.get_queryset()
        serializer = CategoriesSerializer(queryset, many=True)
        return Response(serializer.data)


class CollectionsAPIView(ListAPIView):
    """
    Получение доступных коллекций. Сделано наперед, пока что не используем.
    """

    queryset = categories_queries.get_all_collections()
    serializer_class = CollectionsSerializer()
    permission_classes = [AllowAny]

    @swagger_auto_schema(responses={200: CollectionsSerializer(many=True)})
    def get(self, request):
        queryset = self.get_queryset()
        serializer = CollectionsSerializer(queryset, many=True)
        return Response(serializer.data)


class ImagesAPIView(APIView):
    """
    Получение изображений для товара по его id
    """

    permission_classes = [AllowAny]

    @swagger_auto_schema(
        query_serializer=IDRequestSerializer(),
        responses={
            200: ImageSerializer(many=True),
            404: "nothing found",
            422: "bad request params",
        },
    )
    def get(self, request):
        inserializer = IDRequestSerializer(data=request.query_params)
        if inserializer.is_valid():
            try:
                good_id = inserializer.data["id"]
                images = images_queries.get_good_images(good_id)
                serializer = ImageSerializer(instance=images, many=True)
                return Response(serializer.data)
            except ObjectDoesNotExist:
                return Response(status=404, data={"error": "nothing found"})
        else:
            return Response(status=422, data={"error": "bad request params"})


class CharacteristicsAPIView(APIView):
    """
    Получение характеристик товара по его id
    """

    permission_classes = [AllowAny]

    @swagger_auto_schema(
        query_serializer=IDRequestSerializer(),
        responses={
            200: CharacteristicsSerializer(many=True),
            404: "nothing found",
            422: "bad request params",
        },
    )
    def get(self, request):
        inserializer = IDRequestSerializer(data=request.query_params)
        if inserializer.is_valid():
            try:
                good_id = inserializer.data["id"]
                chars = characteristic_queries.get_characteristics_by_good_id(good_id)
                serializer = CharacteristicsSerializer(instance=chars, many=True)
                return Response(serializer.data)
            except ObjectDoesNotExist:
                return Response(status=404, data={"error": "nothing found"})
        else:
            return Response(status=422, data={"error": "bad request params"})


class FavoriteImagesAPIView(ListAPIView):
    """
    Получение картинок для главной страницы
    """

    queryset = images_queries.get_favorite_images()
    serializer_class = ImageSerializer(many=True)
    permission_classes = [AllowAny]

    @swagger_auto_schema(responses={200: ImageSerializer(many=True)})
    def get(self, request):
        queryset = self.get_queryset()
        serializer = ImageSerializer(queryset, many=True)
        return Response(serializer.data)
