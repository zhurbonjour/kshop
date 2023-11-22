from ..models import Characteristic


def get_characteristics_by_good_id(good_id: int):
    chars = Characteristic.objects.filter(good__id=good_id)
    return chars
