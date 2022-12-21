# Generated by Django 3.2.16 on 2022-12-21 08:12

import django.core.validators
from django.db import migrations, models
import main.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Название')),
                ('description', models.CharField(max_length=250, verbose_name='Описание')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата')),
                ('image', models.ImageField(upload_to=main.models.Service.get_name_file, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg'])], verbose_name='Картинка')),
            ],
        ),
    ]
