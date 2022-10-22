from rest_framework import serializers
from .models import TruckLocation, OTPcontact
from A_business.models import Adding_truck_details
from home.models import SearchData


class TruckLocationSerializers(serializers.Serializer):
    Longitude = serializers.FloatField(default=0)
    Latitude = serializers.FloatField(default=0)
    RegistrationNo = serializers.CharField(max_length=300, default=0)
    def create(self, validate_data):
        return TruckLocation.objects.create(**validate_data)




# class Validate_login(serializers.Serializer):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     Name = models.CharField(max_length=150, default='')
#     Registration_no = models.CharField(max_length=150, default='')
#     Truck_type = models.CharField(max_length=150, blank=True)
#     Vehicle_model = models.CharField(max_length=150, default='')
#     Chechis_no = models.CharField(max_length=150, default='')

#     def create(self, validate_data):
#         return Adding_truck_details.objects.create(**validate_data)

class Validate_login_serializers(serializers.ModelSerializer):
    class Meta:
        model = Adding_truck_details
        fields = ['user', 'Name', 'Registration_no', 'Truck_type', 'Vehicle_model', 'Chechis_no']

class sendTruckLocation_serializers(serializers.ModelSerializer):
    class Meta:
        model = TruckLocation
        fields = ['Longitude', 'Latitude','RegistrationNo', 'user']


class ShowMap_serializers(serializers.ModelSerializer):
    class Meta:
        model = SearchData
        fields = ['pickupL', 'dropL','drop2L', 'drop3L', 'bookingTime', 'scheduleDay', 'scheduleTime']


# class SaveOTPcontact_serializers(serializers.ModelSerializer):
#     class Meta:
#         model = OTPcontact
#         fields = ['Contact']