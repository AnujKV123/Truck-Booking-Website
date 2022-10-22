from django.contrib.auth.models import User
from django.utils.timezone import now
from django.db import models

class ExtendedUser_Adriver(models.Model):
    user_driver = models.OneToOneField(User, on_delete=models.CASCADE)
    signup_phone = models.CharField(max_length=15, default='')
    signup_email = models.CharField(max_length=15, default='')
    signup_username = models.CharField(max_length=15, default='')
    timeStamp = models.DateTimeField(default=now)
    def __str__(self):
        return self.signup_username + "-" + self.signup_phone

class Adding_Driver_details(models.Model):
    D_Si_no = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Name = models.CharField(max_length=150, default='')
    Email = models.CharField(max_length=250, default='')
    Phone_1 = models.CharField(max_length=13, default='')
    Phone_2 = models.CharField(max_length=13, default='')
    Street_no = models.CharField(max_length=100, default='')
    Address_1 = models.CharField(max_length=250, default='')
    Address_2 = models.CharField(max_length=250, default='')
    Zip_code = models.CharField(max_length=150, default='')
    District = models.CharField(max_length=150, blank=True)
    State = models.CharField(max_length=150, blank=True)
    Nationality = models.CharField(max_length=150, blank=True)
    Bank_account = models.CharField(max_length=150, default='')
    Bank_account_user_name = models.CharField(max_length=150, default='')
    Ifsc_code = models.CharField(max_length=150, default='')
    Bank_name = models.CharField(max_length=150, default='')
    Pan_no = models.CharField(max_length=150, default='')
    Aadhar_no = models.CharField(max_length=150, default='')
    Adriver_profile_id = models.CharField(max_length=250)
    driving_truck_type = models.CharField(max_length=150)
    DrivingLisence_no = models.CharField(max_length=150, default='')
    User_picture = models.FileField(upload_to='static/file/A_driver')
    Aadhar_copy = models.FileField(upload_to='static/file/A_driver')
    Pan_copy = models.FileField(upload_to='static/file/A_driver')
    DrivingLisence_copy = models.FileField(upload_to='static/file/A_driver')
    timeStamp = models.DateTimeField(default=now)

    def __str__(self):
        return self.Name + "-" + self.Phone_1

