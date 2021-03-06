# Generated by Django 3.1.7 on 2021-05-23 06:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('userApp', '0007_chat_friends'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='m_from',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='m_from', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.AlterField(
            model_name='chat',
            name='m_to',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='m_to', to=settings.AUTH_USER_MODEL, verbose_name='Друг'),
        ),
    ]
