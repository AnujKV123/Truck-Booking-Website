from django.db import models
from django.utils.timezone import now

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50, default='')
    desc = models.CharField(max_length=5000, default='')
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to="static/image/home")
    pub_date = models.DateTimeField(default=now)

    def __str__(self):
        return self.product_name

class SearchData(models.Model):
    pickupL = models.CharField(max_length=1000)
    dropL = models.CharField(max_length=1000)
    drop2L = models.CharField(max_length=1000)
    drop3L = models.CharField(max_length=1000)
    bookingTime = models.CharField(max_length=1000)
    scheduleDay = models.CharField(max_length=100, default="")
    scheduleTime = models.CharField(max_length=100, default="")
    distance = models.CharField(max_length=100, default="")
    booking_status = models.CharField(max_length=100, default="")
    Selected_Truck = models.CharField(max_length=100, default="")
    Trucktype = models.CharField(max_length=100, default="")
    user_contact = models.CharField(max_length=20, default="")
    date = models.DateTimeField(default=now)
    slug = models.SlugField()

    def __str__(self):
        return self.pickupL

class BookingRate(models.Model):
    Truck_Type = models.CharField(max_length=100)
    Rate = models.IntegerField()
    def __str__(self):
        return self.Truck_Type
    