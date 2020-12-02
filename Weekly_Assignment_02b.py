#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 13:56:18 2020

@author: fouad
"""

Users_List = {1:{"First Name" : "Fouad", "Last Name" : "Sfarijlani", "Email" : "fouad.sfarijlani@student.hu.nl", "password" : "123#123"},
             2:{"First Name" : "Erik", "Last Name" : "Hekman", "Email" : "erik.hekman@student.hu.nl", "password" : "fds@321"},
             3:{"First Name" : "Dennis", "Last Name" : "Nguyen", "Email" : "dennis.nguyeni@student.hu.nl", "password" : "pds@123"},
             4:{"First Name" : "Sergul", "Last Name" : "Nguyen", "Email" : "sergul.nguyen@student.hu.nl", "password" : "nmp@123"}
             }

User_Found = False

username_input = input("Please enter your email address:")
password_input = input("Password:")

first_name_lookup = ""
last_name_lookup = ""

for key,users in Users_List.items():
    
    if users["Email"] == username_input and users["password"] == password_input:
        first_name_lookup = users["First Name"]
        last_name_lookup = users["Last Name"]
        User_Found = True
        break
    else:
        User_Found = False
        

if User_Found == True:
    print("Hello", first_name_lookup, last_name_lookup, "you have successfully logged in")
else:
    print("Wrong username or password")