# Generated by Django 4.0.4 on 2022-06-06 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0007_alter_urls_alias_alter_urls_long_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='urls',
            name='views',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]