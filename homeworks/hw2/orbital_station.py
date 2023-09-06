"""
File: orbital_station.py
Author: Alfonso Sebastian Martinez
Date: 09/20/2021
Section: 42
E-mail: amartin6@umbc.edu
Description: Calculates RPM requirement or station radius depending
             on which variable is given
"""

control_variable = input('Would you like to control "rotation speed" or "station radius"? ')

if control_variable == "rotation speed":
    station_radius = float(input("What is the radius of the station? "))
    rpm_total = (60/(2 * 3.14)) * ((9.8 / station_radius) ** 0.5)
    print("The rotation speed is " + str(rpm_total) + " rpm")
else:
    station_rpm = float(input("What speed in rpm do you want the station to rotate? "))
    rpm_total = 9.8 / (((2 * 3.14 * station_rpm) / 60) ** 2)
    print("The station radius is " + str(rpm_total) + " meters")
    
