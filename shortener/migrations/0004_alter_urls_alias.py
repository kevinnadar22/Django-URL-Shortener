# Generated by Django 4.0.4 on 2022-05-31 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0003_alter_urls_options_alter_urls_alias'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urls',
            name='alias',
            field=models.URLField(max_length=6, unique=True),
        ),
    ]