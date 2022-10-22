from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('Save_location/', views.Save_location, name='Save_location'),
    path('export/', views.pairwise, name='pairwise'),
    path('updateLocationRequest/', views.updateLocationRequest, name='updateLocationRequest'),
    path('RedirectTo/', views.RedirectTo, name='RedirectTo'),
    path('SaveOTPContact/', views.SaveOTPContact, name='SaveOTPContact'),
    path('renderVerification/', views.renderVerification, name='renderVerification'),
    path('VerifyOTP/', views.VerifyOTP, name='VerifyOTP'),
    path('updateUX/', views.updateUX, name='updateUX'),
    path('updateTRNO/', views.updateTRNO, name='updateTRNO'),
    path('updateBStatusCancle/', views.updateBStatusCancle, name='updateBStatusCancle'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
