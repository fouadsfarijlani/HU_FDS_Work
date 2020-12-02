#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 11:41:02 2020

@author: fouad
"""

# import libraries
import requests
import json

# create a string value for CHUCK NORRIS RANDOM endpoint
base_url = "https://api.chucknorris.io/jokes/random"

# get the content and store it in a variable called response
response = requests.get(base_url)

# store the content in a variable called data
data = json.loads(response.content)

# print the output of the data
print("Random Chuck Norris Joke:\n" + data["value"])



