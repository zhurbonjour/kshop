from ..models import Review


def get_reviews_by_good_id(good_id):
    reviews = Review.objects.filter(good__id=good_id, is_active=True)
    return reviews


def get_last_reviews():
    reviews = Review.objects.filter(is_active=True)[:10]
    return reviews
