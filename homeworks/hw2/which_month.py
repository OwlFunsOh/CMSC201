"""
File: which_month.py
Author: Alfonso Sebastian Martinez
Date: 09/20/2021
Section: 42
E-mail: amartin6@umbc.edu
Description: The user inputs a month and how far they want to 
             go in the future. The program calculate what month 
             it will be then
"""

starting_month = int(input("What month are we starting in? "))
if starting_month > 12 or starting_month < 1:
    print("That is not a month between 1 and 12.")
else:
    into_future = int(input("How many months in the future should we go? "))
    final_month = (starting_month + into_future) % 12
    if final_month == 1:
        print("The month will be January")
    elif final_month == 2:
        print("The month will be February")
    elif final_month == 3:
        print("The month will be March")
    elif final_month == 4:
        print("The month will be April")
    elif final_month == 5:
        print("The month will be May")
    elif final_month == 6:
        print("The month will be June")
    elif final_month == 7:
        print("The month will be July")
    elif final_month == 8:
        print("The month will be August")
    elif final_month == 9:
        print("The month will be September")
    elif final_month == 10:
        print("The month will be October")
    elif final_month == 11:
        print("The month will be November")
    else:
        print("The month will be December")
        
