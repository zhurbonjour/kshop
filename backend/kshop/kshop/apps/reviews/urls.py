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
from .api import LastReviewsAPIView, SelectedGoodReviewsAPIView


app_label = "reviews"

urlpattrns = [
    path("", LastReviewsAPIView.as_view()),
    path("<int:id>/", SelectedGoodReviewsAPIView.as_view()),
]
