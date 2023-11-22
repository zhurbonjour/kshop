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
from django.urls import path
from .api import (
    GoodsAPIView,
    ArchiveGoodsAPIView,
    SelectedGoodAPIView,
    CharacteristicsAPIView,
    CategoriesAPIView,
    CollectionsAPIView,
    ImagesAPIView,
    FavoriteImagesAPIView,
)


app_label = "shop"

urlpatterns = [
    path("goods/", GoodsAPIView.as_view()),
    path("archive-goods/", ArchiveGoodsAPIView.as_view()),
    path("good/<int:id>/", SelectedGoodAPIView.as_view()),
    path("characteristics/", CharacteristicsAPIView.as_view()),
    path("categories/", CategoriesAPIView.as_view()),
    path("collections/", CollectionsAPIView.as_view()),
    path("images/", ImagesAPIView.as_view()),
    path("fagorite-images/", FavoriteImagesAPIView.as_view()),
]
