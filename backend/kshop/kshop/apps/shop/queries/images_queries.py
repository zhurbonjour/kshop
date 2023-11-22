from ..models import Image


def get_favorite_images():
    images = Image.objects.filter(is_favorite=True)
    return images


def get_good_images(good_id: str):
    images = Image.objects.filter(good__id=good_id)
    return images
