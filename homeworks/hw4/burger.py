"""
File:    burger.py
Author:  Alfonso Sebastian Martinez
Date:    10/08/2021
Section: 42
E-mail:  amartin6@umbc.edu
Description:
  builds a burger based on user input
"""

if __name__ == '__main__':
    burger = []
    while "top bun" not in burger:
        burger_layer = input("What do you want to add? ")
        burger.append(burger_layer)
        while burger[0] != "bottom bun" and burger_layer != "bottom bun":
            burger.remove(burger_layer)
            print("You must start with the bottom bun!")
            burger_layer = input("What do you want to add? ")
            burger.append(burger_layer)


    num_burger_patties = 0

    while "burger" in burger:
        burger.remove("burger")
        num_burger_patties += 1

    if "cheese" in burger:
        print("You have created a " + str(num_burger_patties) + "-cheeseburger with the condiments:")
    else:
        print("You have created a " + str(num_burger_patties) + "-hamburger with the condiments:")

    #next part is for condiments

    condiments = []

    for topping in burger:
        if topping not in condiments and topping != "burger" and topping != "cheese" and topping != "top bun" and topping != "bottom bun":
            condiments.append(topping)
    print(", ".join(condiments))