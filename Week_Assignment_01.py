#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 16:33:50 2020

@author: fouad
"""

Oreo_Kal = 160
Oreo_Sodium = 190
Oreo_Carbs = 25
Oreo_Fat = 7

User_Oreos = int(input("How many Oreo Cookie have you consumed ? "))

if (Oreo_Kal * User_Oreos < 2000): 
    print("You have Consumed",Oreo_Kal * User_Oreos ,"Kcal,", Oreo_Sodium * User_Oreos ,"mg Of Sodium,", Oreo_Carbs * User_Oreos , "g of carbs and", Oreo_Fat * User_Oreos , " g of fat")
    
else:
    print("You have Consumed",Oreo_Kal * User_Oreos ,"Kcal,", Oreo_Sodium * User_Oreos ,"mg Of Sodium,", Oreo_Carbs * User_Oreos , "g of carbs and", Oreo_Fat * User_Oreos , " g of fat")
    print("WARNING!!! you have surpased the maximum allowed cookies per day, STOP EATING COOKIES !!")