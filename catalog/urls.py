from django.urls import path

from catalog.views import *

urlpatterns = [
    path('', index, name='index'),
    path('contacts/', contacts, name='contacts'),
    path('products/', products, name='products')
    ]
