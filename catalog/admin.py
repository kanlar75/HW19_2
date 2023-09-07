from django.contrib import admin

from catalog.models import Product, Category, Version


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category',)
    list_filter = ('category',)
    search_fields = ('name', 'description',)


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('product', 'number_ver', 'name_ver', 'sign_ver',)
    list_filter = ('number_ver',)
    search_fields = ('name_ver', 'number_ver',)
