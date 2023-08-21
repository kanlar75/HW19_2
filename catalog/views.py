# Create your views here.
from django.shortcuts import render

from catalog.models import Product


# Create your views here.
def index(request):
    return render(request, 'catalog/index.html', {'title': 'Главная страница'})


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'You have new message from {name}({email}): {message}')
    return render(request, 'catalog/contacts.html', {'title': 'Контакты'})


def products(request):
    products_l = Product.objects.all()
    return render(request, 'catalog/products.html', {'products': products_l, 'title': 'Продукты'})
