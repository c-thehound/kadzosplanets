from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('story/<int:pk>/',story,name="Story data")
]
