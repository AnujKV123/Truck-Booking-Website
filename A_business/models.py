from django.contrib.auth.models import User
from django.utils.timezone import now
from django.db import models

class ExtendedUser_Abusniess(models.Model):
    user_x = models.OneToOneField(User, on_delete=models.CASCADE)
    signup_phone = models.CharField(max_length=15, default='')
    signup_email = models.CharField(max_length=15, default='')
    signup_username = models.CharField(max_length=15, default='')
    def __str__(self):
        return self.signup_username + "-" + self.signup_phone


class Adding_truck_details(models.Model):
    Si_no = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Truck_type = models.CharField(max_length=150, blank=True)
    Vehicle_company = models.CharField(max_length=150, default='')
    Vehicle_model = models.CharField(max_length=150, default='')
    Chechis_no = models.CharField(max_length=150, default='')
    Engine_no = models.CharField(max_length=150, default='')
    Registration_no = models.CharField(max_length=150, default='')
    Abusiness_profile_id = models.CharField(max_length=150, default='')
    Front_img = models.FileField(
        upload_to='static/file/A_business')
    Polluton_receipt = models.FileField(
        upload_to='static/file/A_business')
    Insurence = models.ImageField(
        upload_to='static/file/A_business')
    Fitness_certificare = models.ImageField(
        upload_to='static/file/A_business')
    Tax_receipts = models.FileField(
        upload_to='static/file/A_business')
    Permit = models.FileField(
        upload_to='static/file/A_business')
    Rc_certificate = models.FileField(
        upload_to='static/file/A_business')
    timeStamp = models.DateTimeField(default=now)

    def __str__(self):
        return self.Truck_type + "-" + self.Abusiness_profile_id + "-" + self.Registration_no


class Adding_truck_with_driver(models.Model):
    Si_no = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Truck_type = models.CharField(max_length=150, blank=True)
    Vehicle_company = models.CharField(max_length=150, default='')
    Vehicle_model = models.CharField(max_length=150, default='')
    Chechis_no = models.CharField(max_length=150, default='')
    Engine_no = models.CharField(max_length=150, default='')
    Registration_no = models.CharField(max_length=150, default='')
    Abusiness_profile_id = models.CharField(max_length=150, default='')
    Adriver_profile_id = models.CharField(max_length=150, default='')
    Front_img = models.FileField(
        upload_to='static/file/A_business')
    Polluton_receipt = models.FileField(
        upload_to='static/file/A_business')
    Insurence = models.ImageField(
        upload_to='static/file/A_business')
    Fitness_certificare = models.ImageField(
        upload_to='static/file/A_business')
    Tax_receipts = models.FileField(
        upload_to='static/file/A_business')
    Permit = models.FileField(
        upload_to='static/file/A_business')
    Rc_certificate = models.FileField(
        upload_to='static/file/A_business')
    timeStamp = models.DateTimeField(default=now)

    def __str__(self):
        return self.Truck_type + "-" + self.Abusiness_profile_id + "-" + self.Registration_no


class Adding_Abusiness_profile(models.Model):
    Si_no = models.AutoField(primary_key=True)
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
    Ifc_code = models.CharField(max_length=150, default='')
    Bank_name = models.CharField(max_length=150, default='')
    Acount_holder_name = models.CharField(max_length=150, default='')
    Pan_no = models.CharField(max_length=150, default='')
    Aadhar_no = models.CharField(max_length=150, default='')
    Driving_Truck_type = models.CharField(max_length=150, blank=True)
    Driving_license_no = models.CharField(max_length=150, blank=True)
    B_Profile_id = models.CharField(max_length=250, blank=True)
    D_Profile_id = models.CharField(max_length=250, blank=True)
    user_img = models.FileField(
        upload_to='static/file/A_business')
    copy_of_pan = models.FileField(
        upload_to='static/file/A_business')
    copy_of_aadhar = models.FileField(
        upload_to='static/file/A_business')
    copy_of_license = models.FileField(
        upload_to='static/file/A_business')
    timeStamp = models.DateTimeField(default=now)

    def __str__(self):
        return self.Name + "-" + self.Phone_1


