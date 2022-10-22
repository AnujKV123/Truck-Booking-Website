from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.A_blogHome, name='A_blogHome'),
    path('search', views.Search, name='Search'),
    path('<str:slug>', views.blogPost, name='blogPost'),
]
