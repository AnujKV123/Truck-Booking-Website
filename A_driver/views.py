from django.db import reset_queries
from django.http import response
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,  login, logout
import A_driver
from A_driver.models import ExtendedUser_Adriver,Adding_Driver_details
from django.contrib import messages
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Adding_Driver_details
from django.http import HttpResponseRedirect
import random, math

# Create your views here.


def A_driverHome(request):
    # Allprods = Adding_Driver_details.objects.all()
    # params = {"Allprods":Allprods}

    return render(request,"A_driver/index.html")


def handel_signup(request):
    if request.method == "POST":
        # get the post parameters
        signup_username = request.POST['signup_username']
        signup_email = request.POST['signup_email']
        signup_phone = request.POST['signup_phone']
        signup_password = request.POST['signup_password']
        signup_password_again = request.POST['signup_password_again']

        if (User.objects.filter(username=signup_username).exists() or User.objects.filter(email=signup_email).exists()):
            messages.error(request, 'please choose unique username amd email.')
            return redirect("/A_driver")

        elif (signup_password != signup_password_again):
            messages.error(request, 'password do not match! please enter correct password')
            return redirect("/A_driver")

        else:
            myuser = User.objects.create_user(
                signup_username, signup_email, signup_password)
            extendedUser = ExtendedUser_Adriver(user_driver=myuser, signup_phone=signup_phone,signup_email=signup_email,signup_username=signup_username)
            extendedUser.save()
            myuser.save()
            messages.success(request, 'congrats! your A-driver account created successfully.Try to login')
            return redirect('/A_driver')

    else:
        return HttpResponse(request, "404 not found")


def handel_login(request):
    if request.method == "POST":
        # Get the post parameters
        login_username = request.POST['login_username']
        login_password = request.POST['login_password']

        user = authenticate(username=login_username, password=login_password)
        if user is not None:
            request.session['uid'] = request.POST["login_username"] 
            login(request, user)
            messages.success(request, 'congrats! you successfully loged-in in A-driver.')
            return redirect("/A_driver")
        else:
            messages.error(request, 'please enter valid username and passwod.')
            return redirect("/A_driver")
    else:
        return HttpResponse("404- Not found")


def handel_logout(request):
    logout(request)
    messages.success(request, 'you successfully loged-out from A-driver.')
    return redirect('/A_driver')

def Add_driver_details(request):
    print(request.user)
    if(request.session.has_key('uid')):
         if (request.method == "POST"):
             user = request.user
             name = request.POST['name']
             email = request.POST['email']
             phone_1 = request.POST['phone_1']
             phone_2 = request.POST['phone_2']
             street_no = request.POST['street_no']
             address_1 = request.POST['address_1']
             address_2 = request.POST['address_2']
             zip_code = request.POST['zip_code']
             district = request.POST['district']
             state = request.POST['state']
             nationality = request.POST['nationality']
             bank_account_no = request.POST['bank_account_no']
             IFSC_code = request.POST['IFSC_code']
             bank_name = request.POST['bank_name']
             Account_holder_name = request.POST['account_holder_name']
             pan_no = request.POST['pan_no']
             aadhar_no = request.POST['aadhar_no']
             driving_license_no = request.POST['driving_license_no']
             truck_type = request.POST['truck_type']
             Driver_image = request.FILES['driver_image']
             Driving_licence = request.FILES['driving_licence']
             Pan_card = request.FILES['pan_card']
             Aadhar_card = request.FILES['aadhar_card']
             string = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
             slugEnd = ""
             length = len(string)
             for i in range(10) :
                 slugEnd += string[math.floor(random.random() * length)]
             Adriver_profile_id = slugEnd + aadhar_no

             adding_Driver_details = Adding_Driver_details(user=user,Name=name, Email=email, Phone_1=phone_1, Phone_2=phone_2, Street_no=street_no, Address_1=address_1, Address_2=address_2, Zip_code=zip_code, District=district, State=state, Nationality=nationality, Bank_account=bank_account_no,Bank_account_user_name=Account_holder_name ,Ifsc_code=IFSC_code, Bank_name=bank_name, Pan_no=pan_no, Aadhar_no=aadhar_no,User_picture=Driver_image, DrivingLisence_copy=Driving_licence, Pan_copy=Pan_card, Aadhar_copy=Aadhar_card, Adriver_profile_id=Adriver_profile_id, driving_truck_type=truck_type, DrivingLisence_no=driving_license_no)
             adding_Driver_details.save()
             messages.success(request, 'Congrats! Your vehicle added sucessfully, if your all details are true then my team contact with you within 24 working hours')
             return redirect("/A_driver")
    else:
        messages.error(request, 'please enter valid username and passwod.')
        return redirect("/A_driver")

def Search_driver_details(request):
    if(request.method == "POST"):
        contact = request.POST['query']
        a_driver = Adding_Driver_details.objects.filter(Phone_1=contact)
        if(a_driver):
            request.session['driver_contact'] = contact
            params = {"a_driver":a_driver}
            # Display_driver_data(params)
            return render(request ,"A_driver/search_result.html",params)
        else:
            messages.error(request, "this phone no. is not valid please! enter valid phone no. ")
            return redirect("/A_driver")

def update_driver_img(request):
    contactx = request.session['driver_contact']
    a_driver = Adding_Driver_details.objects.filter(Phone_1=contactx)
    params = {"a_driver":a_driver}
    if(request.method == "POST"):
        Driver_update_image = request.FILES['driver_update_image']
        updated = Adding_Driver_details.objects.get(Phone_1=contactx)
        updated.User_picture = Driver_update_image
        updated.save()
        messages.success(request, 'driver image updeted sucessfully')
        return render(request ,"A_driver/search_result.html",params)
    else:
        messages.error(request, 'driver image not updated some problem occured')
        return render(request ,"A_driver/search_result.html",params)
        
def update_driver_aadhar(request):
    contactx = request.session['driver_contact']
    a_driver = Adding_Driver_details.objects.filter(Phone_1=contactx)
    params = {"a_driver":a_driver}
    if(request.method == "POST"):
        Driver_update_image = request.FILES['driver_update_aadhar']
        updated = Adding_Driver_details.objects.get(Phone_1=contactx)
        updated.Aadhar_copy = Driver_update_image
        updated.save()
        messages.success(request, 'copy of aadhar updeted sucessfully')
        return render(request ,"A_driver/search_result.html",params)
    else:
        messages.error(request, 'copy of aadhar not updated some problem occured')
        return render(request ,"A_driver/search_result.html",params)

def update_driver_pan(request):
    contactx = request.session['driver_contact']
    a_driver = Adding_Driver_details.objects.filter(Phone_1=contactx)
    params = {"a_driver":a_driver}
    if(request.method == "POST"):
        Driver_update_image = request.FILES['driver_update_pan']
        updated = Adding_Driver_details.objects.get(Phone_1=contactx)
        updated.Pan_copy = Driver_update_image
        updated.save()
        messages.success(request, 'copy of pan updeted sucessfully')
        return render(request ,"A_driver/search_result.html",params)
    else:
        messages.error(request, 'copy of pan not updated some problem occured')
        return render(request ,"A_driver/search_result.html",params)

def update_driver_license(request):
    contactx = request.session['driver_contact']
    a_driver = Adding_Driver_details.objects.filter(Phone_1=contactx)
    params = {"a_driver":a_driver}
    if(request.method == "POST"):
        Driver_update_image = request.FILES['driver_update_license']
        updated = Adding_Driver_details.objects.get(Phone_1=contactx)
        updated.DrivingLisence_copy = Driver_update_image
        updated.save()
        messages.success(request, 'copy of driving license updeted sucessfully')
        return render(request ,"A_driver/search_result.html",params)
    else:
        messages.error(request, 'copy of driving license not updated some problem occured')
        return render(request ,"A_driver/search_result.html",params)

def update_driver_presional_Detail(request):
    contactx = request.session['driver_contact']
    a_driver = Adding_Driver_details.objects.filter(Phone_1=contactx)
    params = {"a_driver":a_driver}
    if(request.method == "POST"):
        driver_update_Name = request.POST['driver_update_Name']
        driver_update_Email = request.POST['driver_update_Email']
        driver_update_Phone_1 = request.POST['driver_update_Phone_1']
        driver_update_Phone_2 = request.POST['driver_update_Phone_2']
        driver_update_Street_no = request.POST['driver_update_Street_no']
        driver_update_Address_1 = request.POST['driver_update_Address_1']
        driver_update_Address_2 = request.POST['driver_update_Address_2']
        driver_update_Zip_code = request.POST['driver_update_Zip_code']
        driver_update_District = request.POST['driver_update_District']
        driver_update_State = request.POST['driver_update_State']
        driver_update_Nationalitye = request.POST['driver_update_Nationality']
        driver_update_Pan_no = request.POST['driver_update_Pan_no']
        driver_update_Aadhar_no = request.POST['driver_update_Aadhar_no']
        updated = Adding_Driver_details.objects.get(Phone_1=contactx)
        updated.Name = driver_update_Name
        updated.Email = driver_update_Email
        updated.Phone_1 = driver_update_Phone_1
        updated.Phone_2 = driver_update_Phone_2
        updated.Street_no = driver_update_Street_no
        updated.Address_1 = driver_update_Address_1
        updated.Address_2 = driver_update_Address_2
        updated.Zip_code = driver_update_Zip_code
        updated.District = driver_update_District
        updated.State = driver_update_State
        updated.Nationality = driver_update_Nationalitye
        updated.Pan_no = driver_update_Pan_no
        updated.Aadhar_no = driver_update_Aadhar_no
        updated.save()
        messages.success(request, 'driver presional details updeted sucessfully')
        return render(request ,"A_driver/search_result.html",params)
    else:
        messages.error(request, 'driver presional details not updated some problem occured')
        return render(request ,"A_driver/search_result.html",params)