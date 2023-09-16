from django.urls import path
from django.views.decorators.cache import cache_page
from catalog.apps import CatalogConfig
from catalog.views import *
from catalog.views import ContactFormView

app_name = CatalogConfig.name

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('contacts/', ContactFormView.as_view(), name='contacts'),
    path('products/', ProductsListView.as_view(), name='products'),
    path('categories/', show_category_list, name='categories'),
    path('product/<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name='product'),
    path('categories/<int:pk>/', ProductDetailsByCategory.as_view(), name='product_cat'),
    path('create/', ProductCreateView.as_view(), name='create'),
    path('update/<int:pk>/', ProductUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='delete'),
    path('version/', VersionListView.as_view(), name='version'),

    ]
