from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator

from webapp.models import Product, Review


class ProductForm(forms.ModelForm):
    name = forms.CharField(max_length=30, validators=(MinLengthValidator(limit_value=2,
                                                                         message='Кратокое описание должно быть больше 1 символа'),))

    class Meta:
        model = Product
        fields = ('name', 'description', 'category', 'image')
        labels = {
            'name': 'Название',
            'description': 'Описание',
            'category': 'Категория',
            'image': 'Картинка',
        }

    def clean_description(self):
        description = self.cleaned_data.get('description')
        if len(description) < 10:
            raise ValidationError('Описание должено быть длиннее 10 символов')
        elif len(description) > 2999:
            raise ValidationError('Описание должено быть меньше 150 символов')
        return description


class ReviewForm(forms.ModelForm):
    text = forms.CharField(max_length=1000, required=True, label='Текст отзыва')
    grade = forms.IntegerField(label='Оценка')

    class Meta:
        model = Review
        fields = ('text', 'grade')
        labels = {
            'text': 'Отзыв',
            'grade': 'Оценка',
        }