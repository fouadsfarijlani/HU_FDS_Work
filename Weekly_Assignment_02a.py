#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 11:23:53 2020

@author: fouad
"""


# Create a to do list

To_Do_List = []

Program_Run = True
Counter_1 = 1
Counter_2 = 0
User_Command = ""
Delete_Task = False

print("Welcome to the smart to do list, please specify what action you want to take:")
# ask for user input

while Program_Run == True:
    User_Command = input("What option would you like to do next? Add(A)/Remove(R)/print(P)/Exit(E):")
    User_Command = User_Command.upper()
    
    # Ending the program
    if User_Command == "E" or User_Command =="EXIT":
        print("Thank you for using smart to do list !! GO GET THEM !! :)")
        Program_Run = False
    
    # Adding tasks to the TODO list
    elif User_Command == "A" or User_Command == "ADD":
        User_Input = input("What's next on your list? ")
        To_Do_List.append(User_Input)
        
        # Do a check for to do list
        if len(To_Do_List) < 4:
            print("You have less than 4 tasks on your TODO list!! ADD MORE !! ")
        elif len(To_Do_List) > 6:
            print("Sorry, you have 6 tasks already on your TODO list, finish them first then add more")
            To_Do_List.pop(6)
            
     # Printing the TODO list       
    elif User_Command == "P" or User_Command == "PRINT":
        print("Your tasks are as follows: ")
        for tasks in To_Do_List:
            print(Counter_1, "-",tasks)
            Counter_1+=1
        Counter_1 = 1
     
    # Deleting items from the TODO list:
    elif User_Command == "R" or User_Command == "REMOVE":
      
        while Delete_Task == False:
            print("Please specify which one of the tasks you want to remove from your TODO list:")
            for tasks in To_Do_List:
                print(Counter_1, "-",tasks) 
                Counter_1+= 1
            Counter_1 = 1
            User_Delete_Input = input("PLease enter task number or write the task itself: ")
            if User_Delete_Input== "1" or User_Delete_Input == "2" or User_Delete_Input == "3" or User_Delete_Input == "4" or User_Delete_Input == "5" or User_Delete_Input == "6" or User_Delete_Input == "7" or User_Delete_Input == "8" or User_Delete_Input == "9":
                if(int(User_Delete_Input) > len(To_Do_List)):
                    print("Unidentified Number of task, please try again !!!")
                    Delete_Task = True
                else:
                    To_Do_List.pop(int(User_Delete_Input)-1)
                    Delete_Task = True
           
    
    else:
        print("Unkown command, enter a valid command")
    Delete_Task = False
    
                    
                
                
                
                
                
                
                
                
                
                
                
                
