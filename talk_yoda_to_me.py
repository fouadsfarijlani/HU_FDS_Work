#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 13:11:35 2020

@author: fouad
"""

# import libraries
import requests
import json
import urllib.parse

# save api endpoint into a variable
base_url = "http://yoda-api.appspot.com/api/v1/yodish?text="

# get user input
text = input("Normal sentece: ")

# transforme text input to urlencoded string
text = urllib.parse.quote(text)

# concatinate encoded text and base url
yodish_url = base_url + text

# request the new url
response = requests.get(yodish_url)

# load the response into a string 
data = json.loads(response.content)

# print the output
print(data["yodish"])