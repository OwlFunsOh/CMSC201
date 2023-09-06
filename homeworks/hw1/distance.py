"""
File:    distance.py
Author:  Alfonso Sebastian Martinez
Date:    09/13/2021
Section: Section 42
E-mail:  amartin6@umbc.edu
Description:
    The program asks the users for float values and calculates the distance formula between those points
"""

x_1 = float(input("Enter x_1: "))
y_1 = float(input("Enter y_1: "))
x_2 = float(input("Enter x_2: "))
y_2 = float(input("Enter y_2: "))

distance = ((((x_2 - x_1)**2) + ((y_2 - y_1)**2))**0.5)

print("The distance between (" + str(x_1) + ", " + str(y_1) + ") and (" + str(x_2) + ", " + str(y_2) + ") is " + str(distance))
