from django.urls import path
from materials.apps import MaterialsConfig
from materials.views import *

app_name = MaterialsConfig.name

urlpatterns = [
    path('', ArticleListView.as_view(), name='list'),
    path('view/<int:pk>/', ArticleDetailView.as_view(), name='view'),
    path('create/', ArticleCreateView.as_view(), name='article_create'),
    path('update/<int:pk>/', ArticleUpdateView.as_view(), name='article_update'),
    path('delete/<int:pk>/', ArticleDeleteView.as_view(), name='article_delete'),
    ]
