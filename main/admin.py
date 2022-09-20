from django.contrib.admin import register, ModelAdmin

# Register your models here.
from main.models import *


@register(Category)
class CategoryAdmin(ModelAdmin):
    list_display = ('name', 'category_author')


@register(Photo)
class PhotoAdmin(ModelAdmin):
    list_display = ('category', 'photo_description', 'photo', 'date')




