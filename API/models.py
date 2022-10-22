from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

import os
from twilio.rest import Client

# Create your models here.
class TruckLocation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Longitude = models.FloatField(default=0)
    Latitude = models.FloatField(default=0)
    RegistrationNo = models.CharField(max_length=300, default=0)
    TruckType = models.CharField(max_length=300, default=0)
    Truck_Desc = models.CharField(max_length=1000, default=0)
    timeStamp = models.DateTimeField(default=now)
    def __str__(self):
        return self.RegistrationNo

class UserLocation(models.Model):
    Longitude_user = models.CharField(max_length=300, default=0)
    Latitude_user = models.CharField(max_length=300, default=0)
    timeStamp = models.DateTimeField(default=now)
    def __str__(self):
        return self. Longitude_user + "-" + self. Latitude_user

class OTPcontact(models.Model):
    Contact = models.CharField(max_length=15)
    OTP = models.CharField(max_length=6)
    Name = models.CharField(max_length=200)
    Email = models.EmailField(max_length=254)
    def __str__(self):
        return self. Contact

    # def save(self,*args, **kwargs):
    #     # Find your Account SID and Auth Token at twilio.com/console
    #     # and set the environment variables. See http://twil.io/secure
    #     account_sid = 'your_account_sid'
    #     auth_token = 'your_auth_token'
    #     client = Client(account_sid, auth_token)

    #     message = client.messages.create(
    #                                 from_='+14784002330',
    #                                 body= self.OTP,
    #                                 to='(your_phone_bo)'
    #                             )

    #     print(message.sid)
    #     return super().save(self,*args, **kwargs)
    
    