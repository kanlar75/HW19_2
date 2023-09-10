from catalog.models import Product, Version
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView, TemplateView
from django.urls import reverse_lazy, reverse
from django.forms import inlineformset_factory
from django.contrib.auth.mixins import LoginRequiredMixin

from catalog.forms import ProductForm, VersionForm


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
        if self.request.method == 'POST':
            name = self.request.POST.get('name')
            phone = self.request.POST.get('phone')
            message = self.request.POST.get('message')
            print(f'You have new message from {name}({phone}): {message}')
        return super().get_context_data(**kwargs)


class ProductsListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'catalog/products.html'
    context_object_name = 'products'
    login_url = '/users'

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


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'catalog/product.html'
    context_object_name = 'product'
    pk_url_kwarg = 'pk'
    login_url = '/users'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Подробнее о продукте'

        return context


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:products')
    login_url = '/users'


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:products')
    login_url = '/users'

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
    login_url = '/users'


class VersionListView(LoginRequiredMixin, ListView):
    model = Version
    context_object_name = 'version'
    login_url = '/users'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(sign_ver='active')

        return queryset
