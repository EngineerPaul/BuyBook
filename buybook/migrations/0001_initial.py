# Generated by Django 4.0.2 on 2022-02-05 09:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=70, verbose_name='Имя')),
                ('slug', models.SlugField(max_length=70, unique=True, verbose_name='Url')),
            ],
            options={
                'verbose_name': 'Автор',
                'verbose_name_plural': 'Авторы',
                'ordering': ['full_name'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='Жанр')),
                ('slug', models.SlugField(max_length=30, unique=True, verbose_name='Url')),
            ],
            options={
                'verbose_name': 'Жанр',
                'verbose_name_plural': 'Жанры',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Название')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='Url')),
                ('cover', models.ImageField(blank=True, upload_to='photo/covers/', verbose_name='Обложка')),
                ('pages', models.IntegerField(verbose_name='Количество страниц')),
                ('isbn', models.CharField(blank=True, max_length=30, verbose_name='ISBN')),
                ('published_at', models.IntegerField(blank=True, verbose_name='Год издания')),
                ('circulation', models.IntegerField(blank=True, verbose_name='Тираж')),
                ('cover_type', models.CharField(blank=True, max_length=20, verbose_name='Тип обложки')),
                ('book_format', models.CharField(blank=True, max_length=30, verbose_name='Формат')),
                ('weight', models.FloatField(blank=True, max_length=10, verbose_name='Вес')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Добавлено на сайт')),
                ('cost', models.IntegerField(verbose_name='Стоимость')),
                ('discount', models.IntegerField(default=0, verbose_name='Скидка')),
                ('units_in_stock', models.IntegerField(default=0, verbose_name='Кол-во в наличии')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='buybook.author', verbose_name='Автор')),
                ('genre', models.ManyToManyField(blank=True, to='buybook.Genre', verbose_name='Жанр')),
            ],
            options={
                'verbose_name': 'Книга',
                'verbose_name_plural': 'Книги',
                'ordering': ['-created_at', 'title'],
            },
        ),
    ]