"""
File:    escape_velocity.py
Author:  Alfonso Sebastian Martinez
Date:    09/14/2021
Section: Section 42
E-mail:  amartin6@umbc.edu
Description:
  Asks the user for values to put into an escape velocity formula
"""

constant = 6.67 * (10**-11)

launching_body = input("What body are we launching from? ")

mass = float(input("Enter the mass of the planet in scientific notation with the floating number first: "))
mass_power = int(input("What power of 10 is this? "))

body_radius = float(input("Enter the coefficient of the scientific notation of the radius from the center of " + launching_body + "? "))
radius_power = int(input("What power of 10 is this? "))

escape_velocity = (((2 * constant * (mass * (10 ** mass_power))) / (body_radius * (10 ** radius_power))) ** 0.5)

print("The escape velocity required for " + launching_body + " is " + str(round(escape_velocity, 3)) + " m/s")


