from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import *

app_name = CatalogConfig.name

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('contacts/', ContactView.as_view(), name='contacts'),
    path('products/', ProductsListView.as_view(), name='products'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product'),
    path('blog/', ArticleListView.as_view(), name='articles'),
    path('blog/<int:pk>/', ArticleDetailView.as_view(), name='articles'),
    path('create/', ArticleCreateView.as_view(), name='create'),

    ]
