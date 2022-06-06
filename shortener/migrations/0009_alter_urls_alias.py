# Generated by Django 4.0.4 on 2022-06-06 08:24

from django.db import migrations, models
import shortener.models.urls_model


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0008_urls_views'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urls',
            name='alias',
            field=models.URLField(default=shortener.models.urls_model.create_alias, editable=False, max_length=6, unique=True),
        ),
    ]
