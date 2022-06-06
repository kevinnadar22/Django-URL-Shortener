from django.contrib import admin
from django.urls import path, include
from .views import home_view
from .views.redirect_view import redirect_view
from .views.create_url_view import create_url_view
from .views.login_view import login_view
from .views.view_links import URLSListView


urlpatterns = [
    path('', home_view.UrlsCreateView.as_view(), name='home'),
    path('create/url/', create_url_view, name='create'),
    path('login/', login_view, name='login'),
    path('links/', URLSListView.as_view(), name='view_links'),
    path('<str:alias>/', redirect_view, name='redirect'),
]
