import zomatopy
import json
from typing import Any, Dict, Iterator, List, Optional, Text
import ssl
import os
from rasa.constants import DEFAULT_DATA_PATH
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib

config={ "user_key":"9905a5b9828e0ec42e59366409c451a3"}
zomato = zomatopy.initialize_app(config)
loc = tracker.get_slot('location')
cuisine = tracker.get_slot('cuisine').lower()
budget = int(tracker.get_slot("budget"))
location_detail=zomato.get_location(loc, 1)
d1 = json.loads(location_detail)
lat = d1["location_suggestions"][0]["latitude"]
lon = d1["location_suggestions"][0]["longitude"]
cuisines_dict = {'american':1,'chinese':25,'mexican':73,'italian':55,'north indian':50,'south indian':85}
if budget == 701:
    cost_for_2 = 2
elif budget == 299:
    cost_for_2 = 0
else:
    cost_for_2 = 1
results = zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)), cost_for_2)
d = json.loads(results)
response = ""
if d['results_found'] == 0:
    response= "no restaurant found."
    print(response)
else:
    rest_list = []
    for restaurant in d['restaurants']:
        rest_budget = restaurant['restaurant']['average_cost_for_two']
        rest_name = restaurant['restaurant']['name']
        rest_loc = restaurant['restaurant']['location']['address']
        rest_rating = restaurant['restaurant']['user_rating']['aggregate_rating']
        rest_dict = {'name': rest_name, 'loc': rest_loc, 'rating': rest_rating, 'budget': rest_budget}
        rest_list.append(rest_dict)
        if len(rest_list) == 5:
            break

    rest_list = sorted(rest_list, key=lambda i: i['rating'], reverse=True)
    for elem in rest_list:
        response = response + elem['name'] + " in " + elem['loc'] + " has been rated " + elem['rating'] + "\n"

print(response)
# else:
#     for restaurant in d['restaurants']:
#         import pdb; pdb.set_trace()
#         rest_name = restaurant['restaurant']['name']
#         rest_loc = restaurant['restaurant']['location']['address']
#         rest_rating = restaurant['restaurant']['user_rating']['aggregate_rating']
#         rest_dict = {'name': rest_name, 'loc': rest_loc, 'rating': rest_rating}
#         rest_list.append(rest_dict)
#     rest_list = sorted(rest_list, key=lambda i: i['rating'], reverse=True)
#     for elem in rest_list:
#         response = response + elem['name'] + " in " + elem['loc'] + " has been rated " + elem['rating'] + "\n"
#         print(elem['average_cost_for_two'])
# print(response)

# restaurant_details = rest_list
# if restaurant_details:
#     email_content = "<html><body>Hi <br> Please find the restaurant details you were searching: <br>"
#     for restaurant in restaurant_details:
#         email_content = email_content + "<ul>" \
#                         "<li> <b> Restaurant name: " + restaurant['name']  + "</b></li>" \
#                         "<li> Restaurant bocality address: " + restaurant['loc']  + "</li>" \
#                         "<li> Zomato user rating: " + restaurant['rating'] + "</li>" \
#                         "</ul>"
#     email_content = email_content + "<br><br>Regards<br>RestroBOT</body></html>"
#     message = MIMEMultipart("alternative")
#     message["Subject"] = "RestroBOT - Restaurant Details"
#     sender_email = "ankitmhjn13@gmail.com"
#     sender_password = "ankitmsitapril"
#     receiver_email = 'ankitmhjn5@gmail.com'
#     message["From"] = sender_email
#     message["To"] = receiver_email
#     message.attach(MIMEText(email_content, "html"))
#     context = ssl.create_default_context()
#     with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
#         server.login(sender_email, sender_password)
#         server.sendmail(
#             sender_email, receiver_email, message.as_string()
#             )

# import os
# from rasa.constants import DEFAULT_DATA_PATH
#
# def func():
#     cities_name = os.path.join(DEFAULT_DATA_PATH, "cities.json")
#     with open(cities_name) as cities:
#         cities_data = json.load(cities)
#         location = "Delhi"
#         if cities_data is not None:
#             tier1_cities = cities_data["cities"]["tier1"]
#             tier2_cities = cities_data["cities"]["tier2"]
#             tier1_cities = [city.lower() for city in tier1_cities]
#             tier2_cities = [city.lower() for city in tier2_cities]
#             if location and (location.lower() in tier1_cities or location.lower() in tier2_cities):
#                 print("abc")
#                 return "valid"
#             else:
#                 print("def")
#                 return "invalid"
#         print("ghi")
#         return "invalid"
#     print("jkl")
#     return "invalid"
#
# print(func())

# def validate_cuisine():
#     cuisine = "North_Indian"
#     cuisine_file_name = os.path.join(DEFAULT_DATA_PATH, "cuisine.json")
#     with open(cuisine_file_name) as cuisines_list:
#         cuisines = json.load(cuisines_list)
#         cuisines = [cuisine.lower() for cuisine in cuisines['cuisine']]
#         print(cuisines)
#         if cuisine.lower() in cuisines:
#             return "valid"
#         return "invalid"
#
# print(validate_cuisine())