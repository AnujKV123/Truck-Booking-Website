from os import remove
from django.http.request import HttpRequest
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render, HttpResponse
from rest_framework import response
from .models import Product, SearchData
from math import ceil
# *************
# for API
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from home.models import Product,SearchData, BookingRate
from API.models import TruckLocation, OTPcontact
from rest_framework import status
from django.contrib import messages
from rest_framework.response import Response
# for analysing truck location data
import csv
import pandas as pd
import googlemaps
from itertools import tee
import json
import random, math

from rest_framework.response import Response
from django.contrib import messages
import os
from twilio.rest import Client
from django.conf import settings


# Create your views here.
def home (request):
    products = Product.objects.all()
    n = len(products)
    params = {'range':range(1, n), 'product':products}
    return render(request, 'home/index.html', params)

def Save_location(request):
    # get the values from input form
    if request.method == "POST":
        string = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        slugEnd = ""
        length = len(string)
        for i in range(6) :
            slugEnd += string[math.floor(random.random() * length)]
        Enter_Pickup_location = request.POST['Enter_Pickup_location'] #origins
        Enter_drop_location = request.POST['Enter_Drop_Location'] #destination1
        Enter_drop_location2 = request.POST['Enter_Drop_Location2'] #destination2
        Enter_drop_location3 = request.POST['Enter_Drop_Location3'] #destination3
        Schedule = request.POST['cars'] #destination3
        if(Schedule == "Schedule for later"):
            Schedule_Day = request.POST['Schedule_Day'] #Schedule_Day
            Schedule_Time = request.POST['Schedule_Time'] #Schedule_Time
        else:
            Schedule_Day = '' #Schedule_Day
            Schedule_Time = '' #Schedule_Time
        SlugX = Enter_Pickup_location+Enter_drop_location+slugEnd
        Slugy = SlugX.replace(" ", "")
        Slug = Slugy.replace(",","+")
        searchData = SearchData(pickupL=Enter_Pickup_location, dropL=Enter_drop_location, drop2L=Enter_drop_location2, drop3L=Enter_drop_location3, bookingTime=Schedule, scheduleDay=Schedule_Day, scheduleTime=Schedule_Time, slug=Slug)
        searchData.save()
        request.session['searchSlug'] = Slug
        return render(request, "home/searching_truck.html")
    else:
        return redirect("/")
    
    
#Read CSV file into data frame named 'df'
#change seperator (sep e.g. ',') type if necessary
df = pd.read_csv('API/Truck_Location.csv')

    
#Perform request to use the Google Maps API web service
API_key = 'G_api_key'#enter Google Maps API key
@api_view(['GET'])
def pairwise(request, format=None):
    gmaps = googlemaps.Client(key=API_key)  
    writer = csv.writer(open("API/Truck_Location.csv", "w", newline=''))
    writer.writerow(['user', 'Longitude', 'Latitude', 'RegistrationNo', 'TruckType', 'Truck_Desc'])
    for member in TruckLocation.objects.all().values_list('user', 'Longitude', 'Latitude', 'RegistrationNo', 'TruckType', 'Truck_Desc'):
        writer.writerow(member)
    
    Matching_slug = request.session['searchSlug']
    searchdata = SearchData.objects.filter(slug = Matching_slug)
    Enter_Pickup_location = searchdata[0].pickupL

    list1 = []
    list2 = []
    for i1, row1 in df.iterrows():
        LatOrigin = row1['Latitude']
        LongOrigin = row1['Longitude']
        destination = (LongOrigin,LatOrigin)

        # pass origin and destination variables to distance_matrix function# output in meters
        result = gmaps.distance_matrix(Enter_Pickup_location,  destination, mode='driving')
        distance = result["rows"][0]["elements"][0]["distance"]["text"]
        time = result['rows'][0]['elements'][0]['duration']['text']
        print(type(distance))
        # VarX = distance.remove(" km")
        print(distance, "hahahahaha")
        print(time, "hahahahaha")
        #append result to list
        list1.append(distance)
        list2.append(time)

    #Add column 'Distance' to data frame and assign to list values
    print(list1)
    print(list2)
    # df["Distance"] = pd.Series(list1)
    # df["Time"] = pd.Series(list2)
    df["Time"] = list2
    df["Distance"] = list1
    print(df["Distance"])
    print(df["Time"])

    df.to_csv('API/calculated_distance.csv', index=None, header= ['user','Longitude','Latitude','RegistrationNo', 'TruckType', 'Truck_Desc', 'Time','Distance'])

    dfX = pd.read_csv('API/calculated_distance.csv')
    print(dfX)
    listX=[]
    for i1, row1 in dfX.iterrows():
        Distance = row1["Distance"]
        Time = row1["Time"]
        RegistrationNo = row1["RegistrationNo"]
        TruckType = row1["TruckType"]
        Truck_Desc = row1["Truck_Desc"]
        

        if(Distance.endswith(' m')):
            Distance_in_meter = Distance.replace(" m",'')
            if(len(Distance_in_meter) == 2):
                meter_to_km = float("0.0"+Distance_in_meter)
                listVAr = {
                'Distance':meter_to_km,
                'Time':Time,
                'RegistrationNo':RegistrationNo,
                'TruckType':TruckType,
                'Truck_Desc':Truck_Desc
                }
                listX.append(listVAr) 
            elif(len(Distance_in_meter) == 3):
                meter_to_km = float("0."+Distance_in_meter)
                listVAr = {
                'Distance':meter_to_km,
                'Time':Time,
                'RegistrationNo':RegistrationNo,
                'TruckType':TruckType,
                'Truck_Desc':Truck_Desc
                }
                listX.append(listVAr) 
        else:
            distance_X = Distance.replace(" km",'')
            distance_Xi = float(distance_X)
            listVAr = {
                'Distance':distance_Xi,
                'Time':Time,
                'RegistrationNo':RegistrationNo,
                'TruckType':TruckType,
                'Truck_Desc':Truck_Desc
            }
            listX.append(listVAr)       
    print(listX)
    list_micro = []
    list_mini = []
    list_medium = []
    list_max = []
    list_ultra_Max = []
    for i in listX:
        if(i['TruckType'] == 'micro' and i['Distance']<=150):
            list_micro.append(i)
    list_microx = sorted(list_micro, key = lambda i: i['Distance'])

    for i in listX:
        if(i['TruckType'] == 'mini' and i['Distance']<=150):
            list_mini.append(i)
    list_minix = sorted(list_mini, key = lambda i: i['Distance'])

    for i in listX:
        if(i['TruckType'] == 'medium' and i['Distance']<=150):
            list_medium.append(i)
    list_mediumx = sorted(list_medium, key = lambda i: i['Distance'])

    for i in listX:
        if(i['TruckType'] == 'max' and i['Distance']<=150):
            list_max.append(i)
    list_maxx = sorted(list_max, key = lambda i: i['Distance'])

    for i in listX:
        if(i['TruckType'] == 'ultra-max' and i['Distance']<=150):
            list_ultra_Max.append(i)
    list_ultra_Maxx = sorted(list_ultra_Max, key = lambda i: i['Distance'])

    params={'list_micro':list_microx, 'list_mini':list_minix, 'list_medium':list_mediumx, 'list_max':list_maxx, 'list_ultra_Max':list_ultra_Maxx}
    return Response(params)

@api_view(['POST'])
def updateLocationRequest(request):
    if request.method == 'POST':
        LocationX = request.data
        rdx = LocationX["RDX"]
        slug = request.session['searchSlug']
        matchSlugX = SearchData.objects.filter(slug=slug)
        if(matchSlugX):
            if(rdx == "zero"):
                matchSlug = SearchData.objects.get(slug=slug)
                matchSlug.pickupL = LocationX["origin"]
                matchSlug.dropL = LocationX["destination"]
                matchSlug.distance = LocationX["distance"]
                matchSlug.save()
                return response(status=status.HTTP_100_CONTINUE)
            elif(rdx == "one"):
                matchSlug = SearchData.objects.get(slug=slug)
                matchSlug.pickupL = LocationX["origin"]
                matchSlug.dropL = LocationX["destination"]
                matchSlug.drop2L = LocationX["wayapath1"]
                matchSlug.distance = LocationX["distance"]
                matchSlug.save()
                return response(status=status.HTTP_100_CONTINUE)
            elif(rdx == "two"):
                matchSlug = SearchData.objects.get(slug=slug)
                matchSlug.pickupL = LocationX["origin"]
                matchSlug.dropL = LocationX["destination"]
                matchSlug.drop2L = LocationX["wayapath1"]
                matchSlug.drop3L = LocationX["wayapath2"]
                matchSlug.distance = LocationX["distance"]
                matchSlug.save()
                return response(status=status.HTTP_100_CONTINUE)
    else:
        return response(status=status.HTTP_400_BAD_REQUEST)    

def RedirectTo(request):
    return render(request, 'home/send_OTP.html')

@api_view(['POST'])
def SaveOTPContact(request):
    if request.method == 'POST':
        print("hahahahahahaha")
        contactX = request.data
        print(contactX)
        contact = contactX["Contact"]
        print(contact)
        string = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        otp = ""
        length = len(string)
        for i in range(6) :
            otp += string[math.floor(random.random() * length)]
        if(OTPcontact.objects.filter(Contact=contact)):
            OTPcontact.objects.filter(Contact=contact).update(OTP = otp)
            SearchData.objects.filter(slug = request.session['searchSlug']).update(user_contact = contact)
            SearchData.objects.filter(slug = request.session['searchSlug']).update(booking_status = 'booked')
            account_sid = 'your_account_sid'
            auth_token = 'your_auth_token'
            client = Client(account_sid, auth_token)

            # client.messages.create(
            #     from_='+14784002330',
            #     body= otp,
            #     to='your_phone_number'
            #                     )
            return response(status=status.HTTP_100_CONTINUE)
        else:
            createOTP = OTPcontact(Contact = contact, OTP = otp)
            createOTP.save()
            SearchData.objects.filter(slug = request.session['searchSlug']).update(user_contact = contact)
            SearchData.objects.filter(slug = request.session['searchSlug']).update(booking_status = 'booked')
            return response(status=status.HTTP_201_CREATED)
    else:
        return redirect("/")

def renderVerification(request):
    return render(request, 'home/verification.html')

def VerifyOTP(request):
    if (request.method == "POST"):
        OTPCobtactxx = SearchData.objects.filter(slug = request.session['searchSlug'])
        OTPContactFX = [item.user_contact for item in OTPCobtactxx]
        OTPContactCX = OTPContactFX[0]

        fetchOtp = OTPcontact.objects.filter(Contact=OTPContactCX)
        OTP = [item.OTP for item in fetchOtp]
        varX = OTP[0]
        request.session['MatchContact'] = varX

        Name = [itemx.Name for itemx in fetchOtp]
        vary = Name[0]
        fetchStatus = SearchData.objects.filter(slug = request.session['searchSlug'])
        booking_status = [itemx.booking_status for itemx in fetchStatus]
        status = booking_status[0]
        
        fetchStatus = SearchData.objects.filter(slug = request.session['searchSlug'])
        wp1 = [itemx.drop2L for itemx in fetchStatus]
        wp1x = wp1[0]
        
        fetchStatus = SearchData.objects.filter(slug = request.session['searchSlug'])
        wp2 = [itemx.drop3L for itemx in fetchStatus]
        wp2x = wp2[0]
        
        distance = [itemx.distance for itemx in fetchStatus]
        distanceX = distance[0]

        truckType = [itemx.Trucktype for itemx in fetchStatus]
        tType = truckType[0]
        if(tType == 'micro'):
            Brate = BookingRate.objects.filter(Truck_Type='micro')
            rate = [itemx.Rate for itemx in Brate]
            ratex = rate[0]
            if(int(float(distanceX)) <=20):
                CRate = 200 + int(float(distanceX))*ratex
                if(wp1x and wp2x):
                    CRateX = CRate + 300
                elif(wp1x or wp2x):
                    CRateX = CRate + 150
                else:
                    CRateX = CRate
            elif(int(float(distanceX))>20 and int(float(distanceX)) <=50):
                CRate = 100 + int(float(distanceX))*ratex
                if(wp1x and wp2x):
                    CRateX = CRate + 300
                elif(wp1x or wp2x):
                    CRateX = CRate + 150
                else:
                    CRateX = CRate
            else:
                CRate = int(float(distanceX))*ratex
                if(wp1x and wp2x):
                    CRateX = CRate + 300
                elif(wp1x or wp2x):
                    CRateX = CRate + 150
                else:
                    CRateX = CRate

        elif(tType == 'mini'):
            Brate = BookingRate.objects.filter(Truck_Type='mini')
            rate = [itemx.Rate for itemx in Brate]
            ratex = rate[0]
            if(int(float(distanceX)) <=20):
                CRate = 350 + int(float(distanceX))*ratex
                if(wp1x and wp2x):
                    CRateX = CRate + 400
                elif(wp1x or wp2x):
                    CRateX = CRate + 200
                else:
                    CRateX = CRate
            elif(int(float(distanceX))>20 and int(float(distanceX)) <=50):
                CRate = 200 + int(float(distanceX))*ratex
                if(wp1x and wp2x):
                    CRateX = CRate + 400
                elif(wp1x or wp2x):
                    CRateX = CRate + 200
                else:
                    CRateX = CRate
            else:
                CRate = int(float(distanceX))*ratex
                if(wp1x and wp2x):
                    CRateX = CRate + 400
                elif(wp1x or wp2x):
                    CRateX = CRate + 200
                else:
                    CRateX = CRate

        elif(tType == 'medium'):
            Brate = BookingRate.objects.filter(Truck_Type='medium')
            rate = [itemx.Rate for itemx in Brate]
            ratex = rate[0]
            if(int(float(distanceX)) <=20):
                CRate = 450 + int(float(distanceX))*ratex
                if(wp1x and wp2x):
                    CRateX = CRate + 500
                elif(wp1x or wp2x):
                    CRateX = CRate + 250
                else:
                    CRateX = CRate
            elif(int(float(distanceX))>20 and int(float(distanceX)) <=50):
                CRate = 300 + int(float(distanceX))*ratex
                if(wp1x and wp2x):
                    CRateX = CRate + 500
                elif(wp1x or wp2x):
                    CRateX = CRate + 250
                else:
                    CRateX = CRate
            else:
                CRate = int(float(distanceX))*ratex
                if(wp1x and wp2x):
                    CRateX = CRate + 500
                elif(wp1x or wp2x):
                    CRateX = CRate + 250
                else:
                    CRateX = CRate

        elif(tType == 'max'):
            Brate = BookingRate.objects.filter(Truck_Type='max')
            rate = [itemx.Rate for itemx in Brate]
            ratex = rate[0]
            if(int(float(distanceX)) <=20):
                CRate = 550 + int(float(distanceX))*ratex
                if(wp1x and wp2x):
                    CRateX = CRate + 600
                elif(wp1x or wp2x):
                    CRateX = CRate + 300
                else:
                    CRateX = CRate
            elif(int(float(distanceX))>20 and int(float(distanceX)) <=50):
                CRate = 400 + int(float(distanceX))*ratex
                if(wp1x and wp2x):
                    CRateX = CRate + 600
                elif(wp1x or wp2x):
                    CRateX = CRate + 300
                else:
                    CRateX = CRate
            else:
                CRate = int(float(distanceX))*ratex
                if(wp1x and wp2x):
                    CRateX = CRate + 600
                elif(wp1x or wp2x):
                    CRateX = CRate + 300
                else:
                    CRateX = CRate

        elif(tType == 'ultramax'):
            Brate = BookingRate.objects.filter(Truck_Type='ultramax')
            rate = [itemx.Rate for itemx in Brate]
            ratex = rate[0]
            if(int(float(distanceX)) <=20):
                CRate = 650 + int(float(distanceX))*ratex
                if(wp1x and wp2x):
                    CRateX = CRate + 800
                elif(wp1x or wp2x):
                    CRateX = CRate + 450
                else:
                    CRateX = CRate
            elif(int(float(distanceX))>20 and int(float(distanceX)) <=50):
                CRate = 500 + int(float(distanceX))*ratex
                if(wp1x and wp2x):
                    CRateX = CRate + 800
                elif(wp1x or wp2x):
                    CRateX = CRate + 450
                else:
                    CRateX = CRate
            else:
                CRate = int(float(distanceX))*ratex
                if(wp1x and wp2x):
                    CRateX = CRate + 800
                elif(wp1x or wp2x):
                    CRateX = CRate + 450
                else:
                    CRateX = CRate
        
        else:
            Brate = BookingRate.objects.filter(Truck_Type='ultramax')
            rate = [itemx.Rate for itemx in Brate]
            ratex = rate[0]
            if(int(float(distanceX)) <=20):
                CRate = 650 + int(float(distanceX))*ratex
                if(wp1x and wp2x):
                    CRateX = CRate + 800
                elif(wp1x or wp2x):
                    CRateX = CRate + 450
                else:
                    CRateX = CRate
            elif(int(float(distanceX))>20 and int(float(distanceX)) <=50):
                CRate = 500 + int(float(distanceX))*ratex
                if(wp1x and wp2x):
                    CRateX = CRate + 800
                elif(wp1x or wp2x):
                    CRateX = CRate + 450
                else:
                    CRateX = CRate
            else:
                CRate = int(float(distanceX))*ratex
                if(wp1x and wp2x):
                    CRateX = CRate + 800
                elif(wp1x or wp2x):
                    CRateX = CRate + 450
                else:
                    CRateX = CRate
        


        if(status == 'booked'):
            statusX = 'ok'
        else:
            statusX = 'notok'
        print(status)
        if not len(vary):
            nameX = 'not_filled'
        else:
            nameX = 'filled'
        params = {'U_name':nameX, 'status':statusX, 'displayData':fetchStatus, 'rate':CRateX}
        enterOTP = request.POST["otp"]
        if(varX == enterOTP):
            return render(request, 'home/user_home_page.html',params)
        else:
            return redirect('/renderVerification')
    else:
        return redirect("/")

@api_view(['POST'])
def updateUX(request):
    if (request.method == "POST"):
        dataUx = request.data
        name = dataUx["Name"]
        email = dataUx["Email"]
        contactUx = OTPcontact.objects.get(Contact=request.session['MatchContact'])
        contactUx.Name = name
        contactUx.Email = email
        contactUx.save()
        return response(status = status.HTTP_200_OK)
    else:
        return response(status = status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def updateTRNO(request):
    if (request.method == "POST"):
        dataTRNO = request.data
        trnox = dataTRNO["TRNO"]
        ttypex = dataTRNO["Truck_type"]
        SearchData.objects.filter(slug = request.session['searchSlug']).update(Selected_Truck = trnox)
        SearchData.objects.filter(slug = request.session['searchSlug']).update(Trucktype = ttypex)
        return response(status = status.HTTP_200_OK)
    else:
        return response(status = status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def updateBStatusCancle(request):
    if (request.method == "POST"):
        dataBC = request.data
        trnox = dataBC["status"]
        SearchData.objects.filter(slug = request.session['searchSlug']).update(booking_status = trnox)
        return response(status = status.HTTP_200_OK)
    else:
        return response(status = status.HTTP_204_NO_CONTENT)