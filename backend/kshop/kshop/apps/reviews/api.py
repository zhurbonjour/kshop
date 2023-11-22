"""
/reviews/ - получение последних 10 отзывов
/reviews/10 - получение отзывов на товар с id 10
"""

from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from .serializers import ReviewsSerializer
from .queries import reviews_queries
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema


class LastReviewsAPIView(ListAPIView):
    queryset = reviews_queries.get_last_reviews()
    serializer_class = ReviewsSerializer()
    permission_classes = [AllowAny]

    @swagger_auto_schema(responses={200: ReviewsSerializer(many=True)})
    def get(self, request):
        queryset = self.get_queryset()
        serializer = ReviewsSerializer(queryset, many=True)
        return Response(serializer.data)


class SelectedGoodReviewsAPIView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        responses={
            200: ReviewsSerializer(many=True),
            422: "bad request params",
        }
    )
    def get(self, request, id):
        inserializer = ReviewsSerializer(id)
        if inserializer.is_valid():
            good_id = inserializer.data["id"]
            reviews = reviews_queries.get_reviews_by_good_id(good_id)
            serializer = ReviewsSerializer(instance=reviews)
            return Response(serializer.data)
        else:
            return Response(status=422, data={"error": "bad request params"})
