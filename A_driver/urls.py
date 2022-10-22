from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.A_driverHome, name='A_driverHome'),
    path('signup', views.handel_signup, name='handel_signup'),
    path('login', views.handel_login, name='handel_login'),
    path('logout', views.handel_logout, name='handel_logout'),
    path("password-reset/", auth_views.PasswordResetView.as_view(template_name='A_driver/forgot_password.html'), name="password_reset"),
    path("password-reset/done/", auth_views.PasswordResetDoneView.as_view(template_name='A_driver/password_reset_done.html'), name="password_reset_done"),
    path("password-reset-confirm/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(template_name='A_driver/reset_password.html'), name="password_reset_confirm"),
    path("password-reset-complete/", auth_views.PasswordResetCompleteView.as_view(template_name='A_driver/password_reset_complete.html'), name="password_reset_complete"),
    path('Add_driver_details', views.Add_driver_details, name='Add_driver_details'),
    path('Search_driver_details', views.Search_driver_details, name='Search_driver_details'),
    path('update_driver_img', views.update_driver_img, name='update_driver_img'),
    path('update_driver_aadhar', views.update_driver_aadhar, name='update_driver_aadhar'),
    path('update_driver_pan', views.update_driver_pan, name='update_driver_pan'),
    path('update_driver_license', views.update_driver_license, name='update_driver_license'),
    path('update_driver_presional_Detail', views.update_driver_presional_Detail, name='update_driver_presional_Detail'),
]