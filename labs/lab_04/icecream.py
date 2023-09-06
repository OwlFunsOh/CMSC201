"""
File: icecream.py
Author: Alfonso Sebastian Martinez
Date: 09/27/2021
Section: 42
E-mail: amartin6@umbc.edu
Description:
"""

ice_cream_flavors = ["vanilla", "strawberry", "chocolate"]
toppings = ["caramel", "marshmallow", "gummi bears"]

for i in range(len(ice_cream_flavors)):
    if ice_cream_flavors[i] == "strawberry":
        print(ice_cream_flavors[i] + " is fine on its own")
    else:
        for j in range(len(toppings)):
            print(ice_cream_flavors[i] + " is tasty with "+ toppings[j])
    
