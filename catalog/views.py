# Create your views here.
from django.shortcuts import render

from catalog.models import Product
from django.views.generic import ListView, DetailView


def index(request):
    context = {'title': 'Главная страница'}
    return render(request, 'catalog/index.html', context=context)


def contacts(request):
    context = {'title': 'Контакты'}
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'You have new message from {name} ({email}): {message}')
    return render(request, 'catalog/contacts.html', context=context)


class ProductsListView(ListView):
    model = Product
    template_name = 'catalog/products.html'
    context_object_name = 'products'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Продукты'
        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product.html'
    context_object_name = 'product'
    pk_url_kwarg = 'pk'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Подробнее о продукте'
        return context

