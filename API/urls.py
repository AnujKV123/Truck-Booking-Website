from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    # path('', views.A_businessHome, name='A_businessHome'),
    path('Truck_Location/', views.Truck_Location, name='Truck_Location'),
    path('Validate_login/', views.Validate_login, name='Validate_login'),
    path('sendTruckLocation/', views.sendTruckLocation, name='sendTruckLocation'),
    # path('SaveOTPContact/', views.SaveOTPContact, name='SaveOTPContact'),
    path('ShowMap/', views.ShowMap, name='ShowMap'),
    # path('VerifyOTP/', views.VerifyOTP, name='VerifyOTP'),
    # path('<str:post>/', views.ShowMap, name='ShowMap'),
]