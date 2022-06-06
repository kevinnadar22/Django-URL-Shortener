from django.shortcuts import render
from django.views.generic import CreateView
from ..models.urls_model import Urls
from ..forms import UrlForm


# Home View

class UrlsCreateView(CreateView):
    model = Urls
    template_name = "shortener/home.html"
    form_class = UrlForm




