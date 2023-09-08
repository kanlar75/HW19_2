# Generated by Django 4.2.4 on 2023-09-07 11:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0009_alter_version_number_ver_alter_version_sign_ver'),
    ]

    operations = [
        migrations.AlterField(
            model_name='version',
            name='number_ver',
            field=models.CharField(max_length=100, verbose_name='номер версии'),
        ),
        migrations.AlterField(
            model_name='version',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='number_ver', to='catalog.product', verbose_name='продукт'),
        ),
    ]
