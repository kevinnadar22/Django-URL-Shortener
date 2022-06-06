from django.contrib import admin
from .models.urls_model import Urls

# Register your models here.


class UrlsAdmin(admin.ModelAdmin):
    model = Urls
    list_display = ['alias', 'long_url',  'date_created', 'is_hidden',]
    list_per_page = 10
    ordering = ('-date_created',)
    

admin.site.register(Urls, UrlsAdmin)