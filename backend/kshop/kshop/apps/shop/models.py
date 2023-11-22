from django.db import models


class Good(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="Название",
    )
    sku = models.CharField(
        max_length=255,
        verbose_name="Артикул",
    )
    price = models.IntegerField(
        verbose_name="Цена",
    )
    description = models.TextField(
        verbose_name="Описание",
    )
    published_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Время публикации",
    )
    is_active = models.BooleanField(
        verbose_name="Продается",
    )
    archive = models.BooleanField(
        verbose_name="Архивный",
    )
    category = models.ForeignKey(
        "Category",
        on_delete=models.CASCADE,
    )
    collection = models.ForeignKey(
        "Collection",
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"


class Image(models.Model):
    good = models.ForeignKey(
        "Good",
        on_delete=models.CASCADE,
    )
    image = models.ImageField(verbose_name="Изображение")
    is_main = models.BooleanField(verbose_name="На обложку")
    is_favorite = models.BooleanField(verbose_name="На главную")

    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"


class Characteristic(models.Model):
    good = models.ForeignKey(
        "Good",
        on_delete=models.CASCADE,
    )
    parameter = models.CharField(
        max_length=255,
        verbose_name="Параметр",
    )
    value = models.CharField(
        max_length=255,
        verbose_name="Значение",
    )

    class Meta:
        verbose_name = "Характеристика"
        verbose_name_plural = "Характеристики"


class Category(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="Название",
    )
    description = models.TextField(
        verbose_name="Описание",
    )
    is_active = models.BooleanField(
        verbose_name="Продается",
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Collection(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="Название",
    )
    description = models.TextField(
        verbose_name="Описание",
    )

    class Meta:
        verbose_name = "Коллекция"
        verbose_name_plural = "Коллекции"
