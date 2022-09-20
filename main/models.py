from django.contrib.auth.models import User

from django.db.models import *
from django.urls import reverse


class Category(Model):
    category_author = ForeignKey(User, on_delete=SET_NULL, blank=True, null=True, verbose_name='Автор категории')
    name = CharField(max_length=50, verbose_name='Название категории')
    date = DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

    def get_absolute_url(self):
        return reverse('category', kwargs={
            'category_id': self.pk
        })


class Photo(Model):
    category = ForeignKey(Category, on_delete=CASCADE, null=True, blank=True)
    photo_description = CharField(max_length=255, blank=True, default=None, verbose_name='Описание фото')
    photo = ImageField(verbose_name='Фото')
    date = DateTimeField(auto_now_add=True, verbose_name='Дата добавления')

    def __str__(self):
        return self.photo_description

    class Meta:
        verbose_name = 'фото'
        verbose_name_plural = 'фотографии'
