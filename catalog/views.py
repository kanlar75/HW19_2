# Create your views here.
from django.shortcuts import render

from catalog.models import Product


# Create your views here.
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
    return render(request, 'catalog/contacts.html', context=context )


def products(request):
    products_l = Product.objects.all()
    context = {'products': products_l, 'title': 'Продукты'}

    return render(request, 'catalog/products.html', context=context)



