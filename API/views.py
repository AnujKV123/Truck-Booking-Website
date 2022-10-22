

import re
from django.shortcuts import render,redirect
import io
from rest_framework.parsers import JSONParser
from .serializers import TruckLocationSerializers, Validate_login_serializers, sendTruckLocation_serializers, ShowMap_serializers
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework import status
from A_business.models import Adding_truck_details
from .models import TruckLocation,OTPcontact
from home.models import SearchData
from django.contrib import messages

from rest_framework.response import Response
import io
from django_otp.oath import totp
import time
from django.contrib import messages


# for getting OTP
# from datetime import datetime
# from django.core.exceptions import ObjectDoesNotExist
# import pyotp
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from .models import phoneModel
# import base64





# Create your views here.
@csrf_exempt
def Truck_Location(request):
    if request.method == "POST":
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = TruckLocationSerializers(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            res = {"message":"data created"}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type = 'application/json')
    json_data = JSONRenderer().render(serializer.errors)
    return HttpResponse(json_data, content_type = 'application/json')



@api_view(["GET"])
@csrf_exempt
def Validate_login(request):
    user = request.user.id
    Trucks = Adding_truck_details.objects.filter(user=user)
    serializer =  Validate_login_serializers(Trucks, many=True)
    return JsonResponse({'Trucks': serializer.data}, safe=False, status=status.HTTP_200_OK)

@api_view(["GET"])
@csrf_exempt
def sendTruckLocation(request):
    user = request.user.id
    location = TruckLocation.objects.filter(user=user)
    serializer =  sendTruckLocation_serializers(location, many=True)
    return JsonResponse({'location': serializer.data}, safe=False, status=status.HTTP_200_OK)



# @api_view(['POST'])
# def SaveOTPContact(request):
#     if request.method == 'POST':
#         print(request.data)
#         contactX = request.data
#         contact = contactX['Contact']
#         secret_key = b'12345678901234567890'
#         now = int(time.time())
#         otp = 0

#         for delta in range(10,110,20):
#             otp =+ totp(key=secret_key, step=10, digits=6, t0=(now-delta))
#         if(OTPcontact.objects.filter(Contact=contact)):
#             changeOtp = OTPcontact.objects.get(Contact=contact)
#             changeOtp.Contact = contact
#             changeOtp.OTP = otp
#             changeOtp.save()
#             request.session['MatchContact'] = contact
#             request.session['MatchOTP'] = otp
#             return Response(status=status.HTTP_201_CREATED)
#         else:
#             createOTP = OTPcontact(Contact = contact, OTP = otp)
#             createOTP.save()
#             request.session['MatchContact'] = contact
#             request.session['MatchOTP'] = otp
#             return Response(status=status.HTTP_201_CREATED)
#     return Response(status=status.HTTP_400_BAD_REQUEST)

# def VerifyOTP(request):
#     if (request.method == "POST"):
#         fetchOtp = OTPcontact.objects.fillter(Contact=request.session['MatchContact'])
#         OTP = fetchOtp[0]['Contact']
#         enterOTP = request.POST['otp']
#         varX = 0
#         if(OTP == enterOTP):
#             return HttpResponse('hi i am verifird')
#         else:
#             messages.error(request, 'please enter correct otp')


@api_view(['GET'])
@csrf_exempt
def ShowMap(request):
    searchSlug = request.session['searchSlug']
    pickupL = SearchData.objects.filter(slug = searchSlug)
    serializer = ShowMap_serializers(pickupL, many=True)
    return JsonResponse(serializer.data, safe=False)




