"""
File:    pupper_walks.py
Author:  Alfonso Sebastian Martinez
Date:    09/15/2021
Section: Section 42
E-mail:  amartin6@umbc.edu
Description:
  Asks for pupper's name, how far it walks, and how long it takes to walk that far
"""

pupper_name = input("What is pupper's real name? ")
weekly_frequency = int(input("How many times a week do you walk pupper? "))
length_of_walk = int(input("How long is the walk in miles? "))
min_for_a_mile = int(input("How long does it take for you to walk a mile? "))

yearly_miles = float(52 * weekly_frequency * length_of_walk)
yearly_time = float((min_for_a_mile * length_of_walk * weekly_frequency * 52) / 60)

print("Your dog's name is " + pupper_name + ", and you have walked " + str(yearly_miles) + \
      " miles this year, in " + str(yearly_time) + " hours.")