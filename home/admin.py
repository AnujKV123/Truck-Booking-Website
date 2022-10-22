from django.contrib import admin

# Register your models here.
from .models import Product,SearchData,BookingRate

admin.site.register(Product)
admin.site.register(SearchData)
admin.site.register(BookingRate)