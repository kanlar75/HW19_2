from django.shortcuts import render

# Create your views here.
from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'catalog/index.html')


def contacts(request):
    return render(request, 'catalog/contacts.html')
