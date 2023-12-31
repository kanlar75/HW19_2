# Generated by Django 4.2.4 on 2023-08-27 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Заголовок')),
                ('slug', models.CharField(blank=True, max_length=250, null=True, verbose_name='slug')),
                ('body', models.TextField(verbose_name='Содержимое')),
                ('date_create', models.DateField(auto_now_add=True, verbose_name='Дата создания')),
                ('preview', models.ImageField(blank=True, null=True, upload_to='blog/', verbose_name='Изображение')),
                ('is_published', models.BooleanField(default=True, verbose_name='Опубликована или нет')),
                ('views_count', models.IntegerField(default=0, verbose_name='Количество просмотров')),
            ],
            options={
                'verbose_name': 'статья',
                'verbose_name_plural': 'статьи',
            },
        ),
    ]
