from django.db import models
from django.db.models import TextChoices


class CategoryChoice(TextChoices):
    CAR = 'CAR', 'Машина'
    BOARD_GAME = 'BOARD_GAME', 'Настольные игры'


class Product(models.Model):
    name = models.CharField(max_length=50,
                            verbose_name='Название',
                            null=False,
                            blank=False
                            )
    category = models.TextField(max_length=100,
                                verbose_name='Категория',
                                null=False,
                                blank=False,
                                choices=CategoryChoice.choices,
                                default=CategoryChoice.CAR
                                )
    description = models.TextField(max_length=3000,
                                   verbose_name='Описание',
                                   null=False,
                                   blank=True,
                                   )
    image = models.TextField(max_length=3000,
                             null=False,
                             blank=True,
                             verbose_name='Картинка'
                             )
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name='Дата и время создания'
                                      )
    updated_at = models.DateTimeField(auto_now=True,
                                      verbose_name='Дата и время обновления'
                                      )

    def __str__(self):
        return f'{self.name} - {self.category} - {self.description} - {self.image}'