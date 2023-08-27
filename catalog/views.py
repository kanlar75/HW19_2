# Create your views here.
from django.shortcuts import render

from catalog.models import Product, Article
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView, TemplateView
from django.urls import reverse_lazy
from pytils.translit import slugify


class IndexView(TemplateView):
    template_name = 'catalog/index.html'
    extra_context = {
        'title': 'Главная'
    }


class ContactView(TemplateView):
    template_name = 'catalog/contacts.html'
    extra_context = {
        'title': 'Контакты'
    }

    def get_context_data(self, **kwargs):
        if self.request.method == 'post':
            name = self.request.POST.get('name')
            phone = self.request.POST.get('phone')
            message = self.request.POST.get('message')
            print(f'You have new message from {name}({phone}): {message}')
        return super().get_context_data(**kwargs)


class ProductsListView(ListView):
    model = Product
    template_name = 'catalog/products.html'
    context_object_name = 'products'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Все продукты'
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


class ArticleCreateView(CreateView):
    model = Article
    fields = ('title', 'body', 'preview', 'slug')
    success_url = reverse_lazy('catalog:article_form.html')

    def form_valid(self, form):
        if form.is_valid():
            new_article = form.save()
            new_article.slug = slugify(new_article.title)
            new_article.save()
        return super().form_valid(form)


class ArticleListView(ListView):
    model = Article
    template_name = 'catalog/articles.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(is_published=True)
        return queryset


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'catalog/blog_item.html'
    context_object_name = 'blog_item'
    pk_url_kwarg = 'pk'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset=queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class ArticleUpdateView(UpdateView):
    model = Article

    def form_valid(self, form):
        if form.is_valid():
            new_article = form.save()
            new_article.slug = slugify(new_article.title)
            new_article.save()
        return super().form_valid(form)


class ArticleDeleteView(DeleteView):
    model = Article
