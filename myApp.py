import requests
import json
import csv
import pandas as pd
import random

# URL = "http://127.0.0.1:8000/API/Truck_Location/"
# URL = "http://127.0.0.1:8000/API/Validate_login/"
# URL = "http://127.0.0.1:8000/API/sendTruckLocation/"
# URL = "http://127.0.0.1:8000/API/sendTruckLocation/"
URL = "https://testapitesting.pythonanywhere.com/SaveOTPContact"

data =     {
        "Contact": "1234598763",
        "OTP": "RAT9bH",
        "Name": "raju",
        "Email": "raju@gmail.com"
    }
json_data = json.dumps(data)
r = requests.post(url = URL, data = json_data)
data = r.json()
print(data)

# list1 = []
# list2 = []
# dfY = pd.read_csv('API/filter_trucks.csv', error_bad_lines=False)
# print(dfY)
# for i1, row1 in dfY.iterrows():
#     LatOrigin = row1['Distance']
#     LongOrigin = row1['Time']
#     list1.append(LatOrigin)
#     list2.append(LongOrigin)
# print(list1)
# print(list2)

# for x 
# chosen_row = random.choice(dfY)
# print(chosen_row)
# with open('API/filter_trucks.csv') as f:
#     reader = csv.reader(f)
#     chosen_row = random.choice(list(reader))
#     print(chosen_row)
# AIzaSyDw9aG53ZyGtbL7mBkYHCDuhZwAJB-lBBM