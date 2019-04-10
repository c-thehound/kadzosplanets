from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('',landing,name="Landing page"),
    path('blog/',blog,name="Blog")
]
