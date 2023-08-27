from django.urls import reverse

from django.db import models, connection

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

    def __str__(self):
        return f'{self.name}, {self.category}, {self.price}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'

    @classmethod
    def truncate(cls):
        with connection.cursor() as cursor:
            cursor.execute(f'TRUNCATE TABLE {cls._meta.db_table} RESTART IDENTITY CASCADE')


class Article(models.Model):
    title = models.CharField(max_length=250, verbose_name='Заголовок')
    slug = models.CharField(max_length=250, verbose_name='slug', **NULLABLE)
    body = models.TextField(verbose_name='Содержимое')
    date_create = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    preview = models.ImageField(upload_to='blog/', null=True, blank=True, verbose_name='Изображение')
    is_published = models.BooleanField(default=True, verbose_name='Опубликована или нет')
    views_count = models.IntegerField(default=0, verbose_name='Количество просмотров')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'статья'
        verbose_name_plural = 'статьи'
