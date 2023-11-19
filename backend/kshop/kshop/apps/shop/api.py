"""
/shop/category - получение всех категорий
q/shop/good/id - получение товара с id 
q/shop/goods - получение актуальных товаров 
q/shop/archive-goods - получене архивных товаров
/shop/get-favorite-images - получение картинок для слайдера
/reviews/ - получение последних 10 отзывов
/reviews/10 - получение отзывов на товар с id 10
/posts/ - получение последних 3-х постов для отрисовки на главной
"""
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .queries import goods_queries
from .serializers import GoodsSerializer
from drf_yasg.utils import swagger_auto_schema


class GoodsAPIView(ListAPIView):
    queryset = goods_queries.get_goods_in_stock()
    serializer_class = GoodsSerializer()
    permission_classes = [AllowAny]

    @swagger_auto_schema(responses={200: GoodsSerializer(many=True)})
    def get(self, request):
        queryset = self.get_queryset()
        serializer = GoodsSerializer(queryset, many=True)
        return Response(serializer.data)
