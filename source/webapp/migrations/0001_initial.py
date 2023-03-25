# Generated by Django 4.1.7 on 2023-03-25 05:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
                ('category', models.TextField(choices=[('CAR', 'Машина'), ('BOARD_GAME', 'Настольные игры')], default='CAR', max_length=100, verbose_name='Категория')),
                ('description', models.TextField(blank=True, max_length=3000, verbose_name='Описание')),
                ('image', models.TextField(blank=True, max_length=3000, verbose_name='Картинка')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=3000, verbose_name='Текст отзыва')),
                ('grade', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.product')),
            ],
        ),
    ]
