from catalog.models import Product, Version, Category
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView, TemplateView, FormView
from django.urls import reverse_lazy, reverse
from django.forms import inlineformset_factory
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from catalog.forms import ProductForm, VersionForm, ContactForm
from catalog.services import get_categories


class IndexView(TemplateView):
    template_name = 'catalog/index.html'
    extra_context = {
        'title': 'Главная'
    }


# class CategoryListView(LoginRequiredMixin, ListView):
#     model = Category
#     extra_context = {
#         'title': 'Все категории'
#     }
@login_required
def show_category_list(request):
    context = {'object_list': get_categories(),
               'title': 'Все категории продуктов'}
    return render(request, 'catalog/category_list.html', context)


class ProductsListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'catalog/products.html'
    context_object_name = 'products'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        active_version = Version.objects.filter(sign_ver='active')
        context['title'] = 'Все продукты'

        for product in context['object_list']:
            version = active_version.filter(product=product)
            if version:
                product.version = {
                    'name_ver': version[0].name_ver,
                    'number_ver': version[0].number_ver
                }

        return context


class ProductDetailsByCategory(ListView):
    model = Product
    template_name = 'catalog/products_cat.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset.filter(category_id=self.kwargs.get('pk'))
        print(queryset[0].category)
        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        category_item = Category.objects.get(pk=self.kwargs.get('pk'))
        context['object_list'] = Product.objects.filter(category_id=category_item.pk)
        context['title'] = f'Все продукты категории: {category_item.name}'

        return context


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'catalog/product.html'
    context_object_name = 'product'
    pk_url_kwarg = 'pk'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Подробнее о продукте'

        return context


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:products')

    def form_valid(self, form):
        self.object = form.save()
        self.object.user_owner = self.request.user
        self.object.save()
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:products')

    def get_success_url(self):
        return reverse('catalog:update', args=[self.kwargs.get('pk')])

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormSet = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            formset = VersionFormSet(self.request.POST, instance=self.object)
        else:
            formset = VersionFormSet(instance=self.object)
        context_data['formset'] = formset
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        return super().form_valid(form)


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:products')


class VersionListView(LoginRequiredMixin, ListView):
    model = Version
    context_object_name = 'version'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(sign_ver='active')

        return queryset


class ContactFormView(FormView):
    form_class = ContactForm
    template_name = 'catalog/contact.html'
    success_url = reverse_lazy('/')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Контакты'
        return context

    def form_valid(self, form):
        return redirect('/')
