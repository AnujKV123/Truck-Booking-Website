from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('', views.A_businessHome, name='A_businessHome'),
    path('signup', views.handel_signup, name='handel_signup'),
    path('login', views.handel_login, name='handel_login'),
    # path('login', views.index_view, name='index_view'),
    path('logout', views.handel_logout, name='handel_logout'),
    path("password-reset/", auth_views.PasswordResetView.as_view(
        template_name='A_business/forgot_password.html'), name="password_reset"),
    path("password-reset/done/", auth_views.PasswordResetDoneView.as_view(
        template_name='A_business/password_reset_done.html'), name="password_reset_done"),
    path("password-reset-confirm/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(
        template_name='A_business/reset_password.html'), name="password_reset_confirm"),
    path("password-reset-complete/", auth_views.PasswordResetCompleteView.as_view(
        template_name='A_business/password_reset_complete.html'), name="password_reset_complete"),

    path('Add_truck', views.Add_truck, name='Add_truck'),
    path('Add_truck_with_driver', views.Add_truck_with_driver, name='Add_truck_with_driver'),
    path('Create_Profile', views.Create_Profile, name='Create_Profile'),
    path('Search_Abusniss_result', views.Search_Abusniss_result, name='Search_Abusniss_result'),
    path('update_Buser_img', views.update_Buser_img, name='update_Buser_img'),
    path('update_Buser_aadhar', views.update_Buser_aadhar, name='update_Buser_aadhar'),
    path('update_Buser_pan', views.update_Buser_pan, name='update_Buser_pan'),
    path('update_Buser_license', views.update_Buser_license, name='update_Buser_license'),
    path('update_Buser_presional_Detail', views.update_Buser_presional_Detail, name='update_Buser_presional_Detail'),
]
