from django.db import models, connection

from config import settings
from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование')
    description = models.TextField(blank=True, verbose_name='описание')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

    @classmethod
    def truncate(cls):
        with connection.cursor() as cursor:
            cursor.execute(f'TRUNCATE TABLE {cls._meta.db_table} RESTART IDENTITY CASCADE')


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование')
    description = models.TextField(blank=True, verbose_name='описание')
    image = models.ImageField(upload_to='images/', verbose_name='изображение', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='категория')
    price = models.IntegerField(verbose_name='цена')
    date_create = models.DateField(auto_now_add=True, verbose_name='дата создания')
    date_update = models.DateField(auto_now=True, verbose_name='дата изменения')
    user_owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE, verbose_name='пользователь')

    def __str__(self):
        return f'{self.name}, {self.category}, {self.price}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'

    @classmethod
    def truncate(cls):
        with connection.cursor() as cursor:
            cursor.execute(f'TRUNCATE TABLE {cls._meta.db_table} RESTART IDENTITY CASCADE')


class Version(models.Model):
    SIGN_CHOICES = (('active', 'Активна'), ('no_active', 'Не активна'))
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="get_ver", verbose_name='продукт')
    number_ver = models.CharField(max_length=100, verbose_name='номер версии')
    name_ver = models.CharField(max_length=100, verbose_name='название версии')
    sign_ver = models.CharField(max_length=50, choices=SIGN_CHOICES, verbose_name='признак версии')

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'

    def __str__(self):
        return f'{self.product} - {self.number_ver}/({self.name_ver})'
