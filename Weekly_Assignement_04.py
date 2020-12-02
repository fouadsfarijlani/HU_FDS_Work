#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 11:40:02 2020

@author: fouad
"""

# import pandas

import pandas as pd

# import csv file
df = pd.read_csv("movie_plots.csv")


# create calculate word occurance percentage

def word_occurance(arg):
    
    # get the occurance of the word in a column
    df["Word"] = df["Plot"].str.contains(arg)
    
    # get a subset of the data where the occurance is True 
    df_word_occurance = df[df["Word"] == True]
    
    #group the data by country and calculate the occurance of the word 
    df_word_occurance = df_word_occurance.groupby("Origin/Ethnicity")["Word"].count().reset_index(name = "Occurance")
    
    # get another subset from original df  and calculate the totla number of movies by country
    df_total_movies = df.groupby("Origin/Ethnicity")["Title"].count().reset_index(name = "Total Movies")
    
    # merge the two new subset with a left outer join
    df_output = pd.merge(left = df_total_movies, right = df_word_occurance, how = "left" ,left_on = "Origin/Ethnicity", right_on = "Origin/Ethnicity")
    
    # clean the data for final calculation
    df_output["Occurance"] = df_output["Occurance"].fillna(0)
    df_output["Occurance"] = df_output["Occurance"].astype(int)
    
    #sort the new df subset by Origin
    df_output = df_output.sort_values(by = "Origin/Ethnicity", ascending = True)
    
    # calculate the percentage
    df_output["Percentage"] = round((df_output["Occurance"]/df_output["Total Movies"]) * 100, 2)
    
    
    print(df_output)
 


user_input = input("Search the occurance of the word in Movie Cultures: ")

word_occurance(user_input)



    