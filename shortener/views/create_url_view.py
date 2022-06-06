from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import CreateView
from ..models.urls_model import Urls
from ..forms import UrlForm


def create_url_view(request):
    
    if request.method == 'POST':
        form = UrlForm(request.POST)
        if form.is_valid():
            id = form.customSave()
            return HttpResponse(id)
        else:
            return HttpResponse(form.is_valid())