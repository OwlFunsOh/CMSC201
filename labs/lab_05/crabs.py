"""
File: crabs.py
Author: Alfonso Martinez
Date: 10/04/2021
Section: 42
E-mail: amartin6@umbc.edu
Description:
"""

if __name__ == "__main__":
    weight = ""
    crab_weights = []
    while weight != "STOP":
        weight = input("Enter crab weight, (STOP to end) ")
        if weight != "STOP":
            crab_weights.append(float(weight))
    light_or_heavy = input("Do you want to keep light or heavy crabs? ")
    while light_or_heavy != "light" and light_or_heavy != "heavy":
        print("You must enter light or heavy")
        light_or_heavy = input("Do you want to keep light or heavy crabs? ")

    crabs_kept = []
    crabs_discarded = []

    if light_or_heavy == "light":
        light_weight = float(input("What weight determines whether a crab is light or heavy? "))
        for i in range(len(crab_weights)):
            if crab_weights[i] < light_weight:
                crabs_kept.append(crab_weights[i])
            else:
                crabs_discarded.append(crab_weights[i])
        print("You are keeping the crabs with weights ", crabs_kept)
        print("You are not keeping the crabs with weights ", crabs_discarded)

    elif light_or_heavy == "heavy":
        heavy_weight = float(input("What weight determines whether a crab is light or heavy? "))
        for j in range(len(crab_weights)):
            if crab_weights[j] > heavy_weight:
                crabs_kept.append(crab_weights[j])
            else:
                crabs_discarded.append(crab_weights[j])
        print("You are keeping the crabs with weights ", crabs_kept)
        print("You are not keeping the crabs with weights ", crabs_discarded)
