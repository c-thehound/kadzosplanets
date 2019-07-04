from django.contrib import admin
from django.urls import path,include,re_path
from .views import *

urlpatterns = [
    path('',landing,name="Landing page"),
    path('blog/',blog,name="Blog"),
    re_path(r'^.well-known/acme-challenge/.*$',views.acme_challenge, name='acme-challenge'),
]
