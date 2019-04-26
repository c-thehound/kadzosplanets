from django.contrib import admin
from django.urls import path,include
from .views import subscribe_to_mail,message

urlpatterns = [
    path('subscribe/',subscribe_to_mail,name="Subscribe to mail"),
    path('message/',message,name="Leave a message"),
]
