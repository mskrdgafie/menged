from django.contrib import admin
from django.urls import path
from . import views

app_name = 'mengedApp'

urlpatterns = [
    path('receiver', views.receiverHomePage, name='receiver-home-page'),
    path('sender', views.senderHomePage, name='sender-home-page'),
]
