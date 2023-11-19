from kshop.apps.shop.models import Category, Collection


def get_all_categories():
    categories = Category.objects.all()
    return categories


def get_all_categorietions():
    collections = Collection.objects.all()
    return collections
