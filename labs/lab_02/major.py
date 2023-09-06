"""
File: major.py
Author: Alfonso Martinez
Date: 09/13/2021
Section: 42
E-mail: amartin6@umbc.edu
Description: This program asks the user for their major
             and will print out a required passing grade
             based on what major you are taking
"""

#asks for the user's major
user_major = input("Please enter your major: ")

if user_major == "CMSC" or user_major == "CMPE":
    print("You need to earn at least a B for CMSC 201 to count.")
else:
    print("You need to earn at least a C for CMSC 201 to count.")
