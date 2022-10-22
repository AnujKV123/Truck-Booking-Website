from django.contrib import admin
from .models import Adding_truck_details, Adding_truck_with_driver, Adding_Abusiness_profile
from .models import ExtendedUser_Abusniess
# Register your models here.

admin.site.register(Adding_truck_details)
admin.site.register(Adding_truck_with_driver)
admin.site.register(Adding_Abusiness_profile)
admin.site.register(ExtendedUser_Abusniess)
