# Generated by Django 4.0.2 on 2022-02-05 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buybook', '0003_alter_book_cover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='cover',
            field=models.ImageField(blank=True, upload_to='media/covers/', verbose_name='Обложка'),
        ),
    ]
