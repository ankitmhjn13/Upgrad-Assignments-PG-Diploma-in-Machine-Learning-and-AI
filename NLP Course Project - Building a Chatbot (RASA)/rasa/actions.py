from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals
from rasa_sdk import Action
from rasa_sdk.events import SlotSet
from rasa.constants import DEFAULT_DATA_PATH
import zomatopy
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import json
import os
from typing import Any, Dict, Iterator, List, Optional, Text
import json
import traceback
import logging
logger = logging.getLogger(__name__)


class ActionSearchRestaurants(Action):
    def name(self):
        return 'action_search_restaurants'

    def run(self, dispatcher, tracker, domain):
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
            dispatcher.utter_message("No restaurant found.")
            return [SlotSet('location', loc)]
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

        dispatcher.utter_message(response)
        return [SlotSet('location',loc)]


class ActionValidateCuisine(Action):
    def name(self):
        return "action_validate_cuisine"

    def run(
        self, dispatcher, tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        cuisine = tracker.get_slot("cuisine")
        cuisine_file_name = os.path.join(DEFAULT_DATA_PATH, "cuisine.json")
        with open(cuisine_file_name) as cuisines_list:
            cuisines = json.load(cuisines_list)
            if cuisines:
                cuisines = [cuisine.lower() for cuisine in cuisines['cuisine']]
            if cuisine.lower() in cuisines:
                return [SlotSet("is_cuisine_valid", "valid")]
        return [SlotSet("is_cuisine_valid", "invalid")]


class ActionValidateLocation(Action):
    def name(self):
        return "action_validate_location"

    def run(
        self, dispatcher, tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        location = tracker.get_slot("location")
        cities_name = os.path.join(DEFAULT_DATA_PATH, "cities.json")
        location_valid = "invalid"
        with open(cities_name) as cities:
            cities_data = json.load(cities)
            if cities_data is not None:
                tier1_cities = cities_data["cities"]["tier1"]
                tier2_cities = cities_data["cities"]["tier2"]
                tier1_cities = [city.lower() for city in tier1_cities]
                tier2_cities = [city.lower() for city in tier2_cities]
                if location and (location.lower() in tier1_cities or location.lower() in tier2_cities):
                    return [SlotSet("location_valid", "valid")]
                else:
                    return [SlotSet("location_valid", "invalid")]
            return [SlotSet("location_valid", "invalid")]
        return [SlotSet("location_valid", location_valid)]


class ActionSendEmail(Action):
    def name(self):
        return "action_send_details"

    def getRestaurant(self, loc, cuisine, budget):
        config = {"user_key": "f4924dc9ad672ee8c4f8c84743301af5"}
        zomato = zomatopy.initialize_app(config)
        location_detail = zomato.get_location(loc, 1)
        d1 = json.loads(location_detail)
        lat = d1["location_suggestions"][0]["latitude"]
        lon = d1["location_suggestions"][0]["longitude"]
        cuisines_dict = {'american': 1, 'chinese': 25, 'mexican': 73, 'italian': 55, 'north indian': 50,
						 'south indian': 85}
        if budget == 701:
            cost_for_2 = 2
        elif budget == 299:
            cost_for_2 = 0
        else:
            cost_for_2 = 1

        results = zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)), cost_for_2)
        d = json.loads(results)
        rest_list = []
        if d['results_found'] == 0:
            return None
        else:
            for restaurant in d['restaurants']:
                rest_budget = restaurant['restaurant']['average_cost_for_two']
                rest_name = restaurant['restaurant']['name']
                rest_loc = restaurant['restaurant']['location']['address']
                rest_rating = restaurant['restaurant']['user_rating']['aggregate_rating']
                rest_dict = {'name': rest_name, 'loc': rest_loc, 'rating': rest_rating, 'budget': rest_budget}
                rest_list.append(rest_dict)
                if len(rest_list) == 10:
                    break

            rest_list = sorted(rest_list, key=lambda i: i['rating'], reverse=True)
            return rest_list

    def run(
        self, dispatcher, tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        email_to = tracker.get_slot("emailid")
        cuisine = tracker.get_slot("cuisine")
        budget = tracker.get_slot("budget")
        loc = tracker.get_slot('location')
        rest_details = self.getRestaurant(loc, cuisine, budget)
        if rest_details:
            email_content = "<html><body>Hi <br> Please find the <b><u>%s</u></b> restaurant details you were searching: <br>" % (cuisine.upper())
            for restaurant in rest_details:
                email_content = email_content + "<ul><b>Restaurant name: " + restaurant['name'] + "</b>" \
                                "<li> Address: " + restaurant['loc'] + "</li>" \
								"<li> Budget for 2 person: " + str(restaurant['budget']) + "</li>" \
								"<li> Zomato user rating: " + str(restaurant['rating']) + "</li></ul>"
            email_content = email_content + "<br><br>Regards<br>RestroBOT</body></html>"
            message = MIMEMultipart("alternative")
            message["Subject"] = "RestroBOT - Restaurant Details"
            sender_email = "ankitmhjn13@gmail.com"
            sender_password = "ankitmsitapril"
            message["From"] = sender_email
            message["To"] = email_to
            message.attach(MIMEText(email_content, "html"))
            context = ssl.create_default_context()
            try:
                with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                    server.login(sender_email, sender_password)
                    server.sendmail(
						sender_email, email_to, message.as_string()
					)
                dispatcher.utter_message("Email sent please check")
                return []
            except Exception as exp:
                print("exception raised while sending the email %s" %(exp))
                traceback.format_exc()
                dispatcher.utter_message("I am getting issue while sending the email. will try it in some time")
                return []
        else:
            dispatcher.utter_message("I am getting issue while sending the email. will try it in some time")
            return []

