from django.db import models


class Review(models.Model):
    good = models.ForeignKey("shop.Good", on_delete=models.CASCADE)
    left_at = models.DateField(auto_now_add=True, verbose_name="Время комментария")
    comment = models.TextField(verbose_name="Отзыв")

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
