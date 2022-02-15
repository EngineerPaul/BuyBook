# Generated by Django 4.0.2 on 2022-02-15 07:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('buybook', '0011_alter_comment_book_alter_comment_estimate_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Marked',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='marked_books', to='buybook.book', verbose_name='Книга')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='marked_user', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Закладки',
                'ordering': ('user_id', 'book_id'),
            },
        ),
        migrations.CreateModel(
            name='Basket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='basket_books', to='buybook.book', verbose_name='Книга')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='basket_user', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Корзина',
                'ordering': ('user_id', 'book_id'),
            },
        ),
    ]