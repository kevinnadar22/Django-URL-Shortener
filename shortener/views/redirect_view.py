from re import U
from django.shortcuts import get_object_or_404, redirect, render
from ..models.urls_model import Urls

def redirect_view(request, alias):
    long_url = Urls.objects.filter(alias=alias).first()
    long_url.views = long_url.views + 1
    long_url.save()
    return redirect(long_url.long_url)