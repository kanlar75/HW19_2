from django.core.cache import cache

from catalog.models import Category
from config import settings


def get_categories():

    category_list = cache.get('category_list')
    if category_list is None:
        category_list = Category.objects.all()
        cache.set('category_list', category_list, 60)
    return category_list

