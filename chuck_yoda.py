#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 13:22:29 2020

@author: fouad
"""

## THERE IS A PROBLEM WITH YODA ENDPOINT RETUR ##############
### PLEASE RUN THE CODE MULTIPLE TIMES - EXPLANATION BELOW ##

# import libraries
import requests
import json
import urllib.parse

# store both end points in different string variables
yoda_base_url = "http://yoda-api.appspot.com/api/v1/yodish?text="
chuck_norris_url = "https://api.chucknorris.io/jokes/random?category=science"

# get the joke from Chuck Norris endpoint
response = requests.get(chuck_norris_url)

# load the response in a dictionary
data_cn =json.loads(response.content)

# get the joke from the dictionary {key: value} and store it 
# in a variable
cn_joke = data_cn["value"]

# print originral joke
print("Original Chuck Norris Joke:",cn_joke)

# replace word Chuck Norris with I
cn_joke = cn_joke.replace("Chuck Norris", "I")

# transform the string stored to urlencoded
cn_joke = urllib.parse.quote(cn_joke).lower()

# store the original url and the new encoded string in a new 
# string variable 
new_yoda_url = yoda_base_url + cn_joke

# send request to yoda endpoint
response = requests.get(new_yoda_url)


# the below code is an attempt to prevent below error
# JSONDecodeError: Expecting value
# This error appeared when trying to connect to YODA API endpoint
if "json" in response.headers.get("Content-Type"):
    response = response.json()
    print("Yodish:",response["yodish"])
else:
    response = respones.t
    print("Response is not in JSON format")


# ORIGINAL ATTEMPT FOR CODE PRIOR TO ERROR
# JSONDecodeError: Expecting value

# store the response in a new string variable
# data_yoda = json.loads(response.content)


# print the response
# print("Chuck Yoda:",data_yoda["yodish"])






