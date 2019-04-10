from django.contrib import admin
from django.urls import path,include
from .views import subscribe_to_mail

urlpatterns = [
    path('subscribe/',subscribe_to_mail,name="Subscribe to mail")
]
