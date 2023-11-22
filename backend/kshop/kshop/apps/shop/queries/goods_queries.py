from ..models import Good


def get_goods_in_stock():
    goods = Good.objects.filter(
        is_active=True,
        archive=False,
    )
    return goods


def get_archive_goods():
    goods = Good.objects.filter(
        is_active=True,
        archive=True,
    )
    return goods


def get_good_by_id(identificator):
    good = Good.objects.get(pk=identificator)
    return good
