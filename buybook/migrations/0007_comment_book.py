# Generated by Django 4.0.2 on 2022-02-13 10:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('buybook', '0006_alter_comment_options_comment_created_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='book',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='buybook.book', verbose_name='Книга'),
        ),
    ]
