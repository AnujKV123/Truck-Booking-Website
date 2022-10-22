from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,  login, logout
from django.contrib import messages
from A_business.models import Adding_truck_details, ExtendedUser_Abusniess, Adding_truck_with_driver, Adding_Abusiness_profile
from A_driver.models import Adding_Driver_details
from django.core import serializers
# from .form import ImageForm
import random, math


# Create your views here.
def A_businessHome(request):
    allProds=[]
    # news_f_html = serializers.serialize("json",Adding_truck_details.objects.all())
    # 'news_f_html':news_f_html
    
    # django_list = list(Adding_truck_details.objects.all())

    catprods = Adding_truck_details.objects.values('user', 'Si_no')
    cats = {item['user'] for item in catprods}
    for cat in cats:
        prod = Adding_truck_details.objects.filter(user=cat)
        n = len(prod)
        allProds.append([prod, range(1, n), n])
    params={'allProds':allProds}
    return render(request, "A_business/index.html",params)


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
            return redirect("/A_business")

        elif (signup_password != signup_password_again):
            messages.error(request, 'password do not match! please enter correct password')
            return redirect("/A_business")

        else:
            myuser = User.objects.create_user(
                signup_username, signup_email, signup_password,)
            extendedUser = ExtendedUser_Abusniess(user_x=myuser, signup_phone=signup_phone,signup_email=signup_email,signup_username=signup_username)
            extendedUser.save()
            myuser.save()
            messages.success(request, 'congrats! your A-business account created successfully.Try to login')
            return redirect('/A_business')

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
            messages.success(
            request, 'congrats! you successfully loged-in in A-business.')
            return redirect("/A_business")
        else:
            messages.error(request, 'please enter valid username and passwod.')
            return redirect("/A_business")
    else:
        return HttpResponse("404- Not found")

def handel_logout(request):
    # del request.session['uid']
    logout(request)
    messages.success(request, 'you successfully loged-out from A-business.')
    return redirect('/A_business')

def Add_truck(request):
    print(request.user)
    if(request.session.has_key('uid')):
         if (request.method == "POST"):
             user = request.user
             truck_type = request.POST['truck_type']
             vehicle_company = request.POST['vehicle_company']
             vehicle_model = request.POST['vehicle_model']
             chechis_no = request.POST['chechis_no']
             engine_no = request.POST['engine_no']
             registration_no = request.POST['registration_no']
             Abisnuss_P_id = request.POST['Abusiness_profile_ID']
             front_img = request.FILES['front_img']
             pollution_receipt = request.FILES['pollution_receipt']
             insurence = request.FILES['insurence']
             fitness_certificate = request.FILES['fitness_certificate']
             tax_receipts = request.FILES['tax_receipts']
             permit = request.FILES['permit']
             rc_certificate = request.FILES['rc_certificate']
             check_Abisnuss_P_id = Adding_Abusiness_profile.objects.filter(Profile_id=Abisnuss_P_id)
             if(check_Abisnuss_P_id):
                adding_truck_details = Adding_truck_details(user=user, Truck_type=truck_type, Vehicle_company=vehicle_company, Vehicle_model=vehicle_model, Chechis_no=chechis_no, Engine_no=engine_no, Registration_no=registration_no,Abusiness_profile_id=Abisnuss_P_id, Front_img=front_img, Polluton_receipt=pollution_receipt, Insurence=insurence, Fitness_certificare=fitness_certificate, Tax_receipts=tax_receipts, Permit=permit, Rc_certificate=rc_certificate)
                adding_truck_details.save()
                messages.success(request, 'Congrats! Your vehicle added sucessfully, if your all details are true then my team contact with you within 24 working hours')
                return redirect("/A_business")
            
             else:
                messages.error(request, 'this A-business profile ID not exist please enter valid A-business profile ID.')
                return redirect("/A_business")
    else:
        messages.error(request, 'please enter valid username and passwod.')
        return redirect("/A_business")


def Add_truck_with_driver(request):
    print(request.user)
    if(request.session.has_key('uid')):
         if (request.method == "POST"):
             user = request.user
             truck_type = request.POST['truck_type']
             vehicle_company = request.POST['vehicle_company']
             vehicle_model = request.POST['vehicle_model']
             chechis_no = request.POST['chechis_no']
             engine_no = request.POST['engine_no']
             registration_no = request.POST['registration_no']
             Abisnuss_P_id = request.POST['Abusiness_profile_ID']
             Adriver_P_id = request.POST['Adriver_profile_ID']
             front_img = request.FILES['front_img']
             pollution_receipt = request.FILES['pollution_receipt']
             insurence = request.FILES['insurence']
             fitness_certificate = request.FILES['fitness_certificate']
             tax_receipts = request.FILES['tax_receipts']
             permit = request.FILES['permit']
             rc_certificate = request.FILES['rc_certificate']
             check_Abisnuss_P_id = Adding_Abusiness_profile.objects.filter(Profile_id=Abisnuss_P_id)
             check_Adriver_P_id = Adding_Driver_details.objects.filter(Adriver_profile_id=Adriver_P_id)
             if(check_Abisnuss_P_id and check_Adriver_P_id):
                adding_truck_with_driver = Adding_truck_with_driver(user=user, Truck_type=truck_type, Vehicle_company=vehicle_company, Vehicle_model=vehicle_model, Chechis_no=chechis_no, Engine_no=engine_no, Registration_no=registration_no,Abusiness_profile_id=Abisnuss_P_id, Adriver_profile_id=Adriver_P_id, Front_img=front_img, Polluton_receipt=pollution_receipt, Insurence=insurence, Fitness_certificare=fitness_certificate, Tax_receipts=tax_receipts, Permit=permit, Rc_certificate=rc_certificate)
                adding_truck_with_driver.save()
                messages.success(request, 'Congrats! Your vehicle added sucessfully')
                return redirect("/A_business")
            
             else:
                messages.error(request, 'may be this A-business profile ID or A-driver profile ID not valid please enter valid A-business profile ID.')
                return redirect("/A_business")
    else:
        messages.error(request, 'please enter valid username and passwod.')
        return redirect("/A_business")

def Create_Profile(request):
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
             IFC_code = request.POST['IFC_code']
             bank_name = request.POST['bank_name']
             acount_holder_name = request.POST['acount_holder_name']
             pan_no = request.POST['pan_no']
             aadhar_no = request.POST['aadhar_no']
             driving_truck_type = request.POST['truck_type']
             license_no = request.POST['driving_license_no']
             user_img = request.FILES['user_image']
             pan_card = request.FILES['pan_card']
             aadhar_card = request.FILES['aadhar_card']
             copy_of_license = request.FILES['driving_license']
             string = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
             slugEnd = ""
             length = len(string)
             for i in range(10) :
                 slugEnd += string[math.floor(random.random() * length)]
             Abusiness_profile_id = slugEnd + aadhar_no
             if(driving_truck_type != " " and license_no != " " and copy_of_license != " "):
                slugEndX = ""
                length = len(string)
                for i in range(10) :
                    slugEndX += string[math.floor(random.random() * length)]
                Adriver_profile_id = slugEndX + aadhar_no

                adding_Abusiness_profile = Adding_Abusiness_profile(user=user,Name=name, Email=email, Phone_1=phone_1, Phone_2=phone_2, Street_no=street_no, Address_1=address_1, Address_2=address_2, Zip_code=zip_code, District=district, State=state, Nationality=nationality, Bank_account=bank_account_no, Ifc_code=IFC_code, Bank_name=bank_name, Acount_holder_name=acount_holder_name, Driving_Truck_type=driving_truck_type, Driving_license_no=license_no, Pan_no=pan_no, Aadhar_no=aadhar_no, copy_of_pan=pan_card, copy_of_aadhar=aadhar_card, user_img=user_img, copy_of_license=copy_of_license, B_Profile_id=Abusiness_profile_id, D_Profile_id=Adriver_profile_id)
                adding_Abusiness_profile.save()
                messages.success(request, 'A-business profile of' + name +'created sucessfully! A-business profile ID is' + Abusiness_profile_id +'and A-driver profile id is' + Adriver_profile_id)
                return redirect("/A_business")
             else:
                adding_Abusiness_profile = Adding_Abusiness_profile(user=user,Name=name, Email=email, Phone_1=phone_1, Phone_2=phone_2, Street_no=street_no, Address_1=address_1, Address_2=address_2, Zip_code=zip_code, District=district, State=state, Nationality=nationality, Bank_account=bank_account_no, Ifc_code=IFC_code, Bank_name=bank_name, Acount_holder_name=acount_holder_name, Driving_Truck_type=driving_truck_type, Driving_license_no=license_no, Pan_no=pan_no, Aadhar_no=aadhar_no, copy_of_pan=pan_card, copy_of_aadhar=aadhar_card, user_img=user_img, copy_of_license=copy_of_license, B_Profile_id=Abusiness_profile_id)
                adding_Abusiness_profile.save()
                messages.success(request, 'A-business profile of' + name +'created sucessfully! A-business profile ID is' + Abusiness_profile_id)
                return redirect("/A_business")
    else:
        messages.error(request, 'some problem is occured please try again')
        return redirect("/A_business")

def Search_Abusniss_result(request):
        if(request.method == "POST"):
            contact = request.POST['query']
            a_business = Adding_Abusiness_profile.objects.filter(Phone_1=contact)
            if( a_business):
                request.session['business_contact'] = contact
                params = {"a_business": a_business}
                # Display_driver_data(params)
                return render(request ,"A_business/search_result.html",params)
            else:
                messages.error(request, "this phone no. is not valid please! enter valid phone no. ")
                return redirect("/A_business")

def update_Buser_img(request):
    contactx = request.session['business_contact']
    a_business = Adding_Abusiness_profile.objects.filter(Phone_1=contactx)
    params = {"a_business":a_business}
    if(request.method == "POST"):
        user_update_image = request.FILES['user_update_image']
        updated = Adding_Abusiness_profile.objects.get(Phone_1=contactx)
        updated.user_img = user_update_image
        updated.save()
        messages.success(request, 'user image updeted sucessfully')
        return render(request ,"A_business/search_result.html",params)
    else:
        messages.error(request, 'user image not updated some problem occured')
        return render(request ,"A_business/search_result.html",params)
        
def update_Buser_aadhar(request):
    contactx = request.session['business_contact']
    a_business = Adding_Abusiness_profile.objects.filter(Phone_1=contactx)
    params = {"a_business":a_business}
    if(request.method == "POST"):
        user_update_aadhar = request.FILES['user_update_aadhar']
        updated = Adding_Abusiness_profile.objects.get(Phone_1=contactx)
        updated.copy_of_aadhar = user_update_aadhar
        updated.save()
        messages.success(request, 'copy of aadhar updeted sucessfully')
        return render(request ,"A_business/search_result.html",params)
    else:
        messages.error(request, 'copy of aadhar not updated some problem occured')
        return render(request ,"A_business/search_result.html",params)

def update_Buser_pan(request):
    contactx = request.session['business_contact']
    a_business = Adding_Abusiness_profile.objects.filter(Phone_1=contactx)
    params = {"a_business":a_business}
    if(request.method == "POST"):
        user_update_pan = request.FILES['user_update_pan']
        updated = Adding_Abusiness_profile.objects.get(Phone_1=contactx)
        updated.copy_of_pan = user_update_pan
        updated.save()
        messages.success(request, 'copy of pan updeted sucessfully')
        return render(request ,"A_business/search_result.html",params)
    else:
        messages.error(request, 'copy of pan not updated some problem occured')
        return render(request ,"A_business/search_result.html",params)

def update_Buser_license(request):
    contactx = request.session['business_contact']
    a_business = Adding_Abusiness_profile.objects.filter(Phone_1=contactx)
    params = {"a_business":a_business}
    if(request.method == "POST"):
        driver_update_license = request.FILES['driver_update_license']
        updated = Adding_Abusiness_profile.objects.get(Phone_1=contactx)
        updated.copy_of_license = driver_update_license
        updated.save()
        messages.success(request, 'copy of driving license updeted sucessfully')
        return render(request ,"A_business/search_result.html",params)
    else:
        messages.error(request, 'copy of driving license not updated some problem occured')
        return render(request ,"A_business/search_result.html",params)

def update_Buser_presional_Detail(request):
    contactx = request.session['business_contact']
    a_business = Adding_Abusiness_profile.objects.filter(Phone_1=contactx)
    params = {"a_business":a_business}
    if(request.method == "POST"):
        Buser_update_Name = request.POST['Buser_update_Name']
        Buser_update_Email = request.POST['Buser_update_Email']
        Buser_update_Phone_1 = request.POST['Buser_update_Phone_1']
        Buser_update_Phone_2 = request.POST['Buser_update_Phone_2']
        Buser_update_Street_no = request.POST['Buser_update_Street_no']
        Buser_update_Address_1 = request.POST['Buser_update_Address_1']
        Buser_update_Address_2 = request.POST['Buser_update_Address_2']
        Buser_update_Zip_code = request.POST['Buser_update_Zip_code']
        Buser_update_District = request.POST['Buser_update_District']
        Buser_update_State = request.POST['Buser_update_State']
        Buser_update_Nationalitye = request.POST['Buser_update_Nationality']
        Buser_update_Pan_no = request.POST['Buser_update_Pan_no']
        Buser_update_Aadhar_no = request.POST['Buser_update_Aadhar_no']
        Buser_update_D_t_type = request.POST['Buser_update_D_t_type']
        Buser_update_license_no = request.POST['Buser_update_license_no']
        updated = Adding_Abusiness_profile.objects.get(Phone_1=contactx)
        updated.Name =  Buser_update_Name
        updated.Email =  Buser_update_Email
        updated.Phone_1 =  Buser_update_Phone_1
        updated.Phone_2 =  Buser_update_Phone_2
        updated.Street_no =  Buser_update_Street_no
        updated.Address_1 =  Buser_update_Address_1
        updated.Address_2 =  Buser_update_Address_2
        updated.Zip_code =  Buser_update_Zip_code
        updated.District =  Buser_update_District
        updated.State =  Buser_update_State
        updated.Nationality =  Buser_update_Nationalitye
        updated.Pan_no =  Buser_update_Pan_no
        updated.Aadhar_no =  Buser_update_Aadhar_no
        updated.Driving_Truck_type =  Buser_update_D_t_type
        updated.Driving_license_no =  Buser_update_license_no
        updated.save()
        messages.success(request, 'driver presional details updeted sucessfully')
        return render(request ,"A_business/search_result.html",params)
    else:
        messages.error(request, 'driver presional details not updated some problem occured')
        return render(request ,"A_business/search_result.html",params)