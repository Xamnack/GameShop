# Generated by Django 3.1.7 on 2021-05-08 15:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gameApp', '0003_cart'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cart',
            options={'verbose_name': 'Корзина', 'verbose_name_plural': 'Корзины'},
        ),
        migrations.AlterModelOptions(
            name='reviews',
            options={'verbose_name': 'Отзыв', 'verbose_name_plural': 'Отзывы'},
        ),
    ]