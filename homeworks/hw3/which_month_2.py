"""
File: which_month_2.py
Author: Alfonso Sebastian Martinez
Date: 09/20/2021
Section: 42
E-mail: amartin6@umbc.edu
Description: The user inputs a month and how far they want to
             go in the future. The program calculates what month
             it will be then
"""

if __name__ == '__main__':
    months = ["December", "January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November"]
    starting_month = int(input("What month are we starting in (enter as an int)? "))
    if starting_month > 12 or starting_month < 1:
        print("That is not a month between 1 and 12.")
    else:
        into_future = int(input("How many months in the future should we go? "))
        final_month = (starting_month + into_future) % 12
        print(months[final_month])
