from django.contrib.auth.models import User
from django.db import models


class Review(models.Model):
    author = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='review_products')
    product = models.ForeignKey(to='webapp.Product', on_delete=models.CASCADE, related_name='review_users')
    text = models.TextField(max_length=3000, null=False, blank=False, verbose_name='Текст отзыва')
    grade = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name='Дата и время создания'
                                      )
    updated_at = models.DateTimeField(auto_now=True,
                                      verbose_name='Дата и время обновления'
                                      )

    def __str__(self):
        return f'{self.author} - {self.grade} - {self.text} - {self.product.name}'