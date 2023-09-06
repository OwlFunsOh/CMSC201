"""
File: gandalf.py
Author: Alfonso Sebastian Martinez
Date: 09/20/2021
Section: 42
E-mail: amartin6@umbc.edu
Description:
"""

#asks for the user's race
race = input("Which race are you? ")

#asks these follow up questions if race is human
if race == "human":
    king_of_gondor = input("Are you the true and rightful King of Gondor? ")
    if king_of_gondor == "no":
        take_ring_from_frodo = input("Have you tried to take the ring from Frodo? ")
        if take_ring_from_frodo == "yes":
            print("You are Boromir, poor guy...")
        else:
            print("You are probably Theoden.")
    else:
        print("You are Aragorn: the son of Arathorn.")

#asks these follow up questions if race is elf
elif race == "elf":
    in_matrix = input("Were you in the matrix? ")
    if in_matrix == "yes":
        print("You are Agent Smith, I mean... Elrond")
    else:
        print("You are Legolas")

#asks these follow up questions if race is Maiar
elif race == "maiar":
    good_or_evil = input("Do you end up being good or evil? ")
    if good_or_evil == "evil":
        forged_ring = input("Did you forge the one ring? ")
        if forged_ring == "yes":
            print("You are Sauron")
        else:
            print("You are Saruman")
    else:
        print("You are Gandalf.")

#asks these follow up questions if race is hobbit
elif race == "hobbit":
    carry_one_ring = input("Do you carry the one ring? ")
    if carry_one_ring == "no":
        is_gardener = input("Are you a gardener? ")
        if is_gardener == "no":
            print("You are either Merry or Pippin")
        else:
            print("You are Samwise")
    else:
        print("You are Frodo Baggins")

elif race == "dwarf":
    print("You are Gimli son of Gloin")
else:
    print("You are an Orc, sorry about that.")
    
