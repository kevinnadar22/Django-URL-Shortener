# Generated by Django 4.0.4 on 2022-06-04 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0005_alter_urls_long_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urls',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
