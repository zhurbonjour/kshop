from django.db import models


class Review(models.Model):
    good = models.ForeignKey("shop.Good", on_delete=models.CASCADE)
    left_at = models.DateField(auto_now_add=True, verbose_name="Время комментария")
    comment = models.TextField(verbose_name="Отзыв")
    is_active = models.BooleanField(verbose_name="Прошло модерацию", default=True)

    def __str__(self):
        return str(self.comment)[:25]

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
