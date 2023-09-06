"""
File: super.py
Authot: Alfonso Martinez
Date: 09/13/2021
Section: 42
E-mail: amartin6@umbc.edu
Description: Asks the user if they are a hero or a villain
             and gives an appropriate response for it
"""

#Asks the user if they are a hero or villain and their name
user_hero_or_villain = input("Are you a hero or a villain? ")

#compares if user is hero or villain and gives appropriate response

if user_hero_or_villain == "villain":
    villain_name = input("What is your name? ")
    print(villain_name + " sounds pretty eveil!")
elif user_hero_or_villain == "hero":
    people_saved = int(input("How many people have you saved? "))
    if people_saved <= 10:
        print("Go on more patrols!")
    elif people_saved > 10 and people_saved < 100:
        print("Sounds like you're making a difference!")
    elif people_saved >= 100:
        print("Wow, great job saving the city!")
    else:
        print("Can't save negative people lmao")
else:
    print("Looks like you're neither a hero or a villain")
