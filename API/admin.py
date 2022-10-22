from django.contrib import admin
from .models import TruckLocation,UserLocation,OTPcontact

# Register your models here.
admin.site.register(TruckLocation)
admin.site.register(UserLocation)
admin.site.register(OTPcontact)
