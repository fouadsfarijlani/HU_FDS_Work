#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 12:15:59 2020

@author: fouad
"""

# import libraries
import requests
import json
import urllib.parse

# put api endpoint into a string variable
base_url = "https://api.chucknorris.io/jokes/search?query="

# get user input
user_input = input("what are you searching for? ")

# transform user input into url encoded format
user_input = urllib.parse.quote(user_input)

# combine the endpoint url with user input
response = requests.get(base_url + user_input)

# load the api request into a json object
data = json.loads(response.content)

# print out the results
for item in data["result"]:
    print(item["value"])