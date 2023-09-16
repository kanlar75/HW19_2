from django.core.cache import cache

from catalog.models import Category
from config import settings


def get_categories():
    if settings.CACHE_ENABLED:
        key = 'category_list'
        category_list = cache.get(key)
        if category_list is None:
            category_list = Category.objects.all()
        else:
            category_list = Category.objects.all()

    return category_list
