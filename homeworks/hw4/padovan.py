"""
File:    padovan.py
Author:  Alfonso Sebastian Martinez
Date:    10/04/2021
Section: 42
E-mail:  amartin6@umbc.edu
Description:
  DESCRIPTION OF WHAT THE PROGRAM DOES
"""

if __name__ == '__main__':
    value_one = 0
    value_two = 0
    value_three = 1
    current_value = 0
    steps = 0
    goal = int(input("Enter goal to reach in Padovan Sequence: "))
    while current_value < goal:
        current_value = value_two + value_one
        value_one = value_one + (value_two - value_one)
        value_two = value_two + (value_three - value_two)
        value_three = value_three + (current_value - value_three)
        steps = steps + 1
    if steps - 1 == 1:
        print("It takes " + str(steps - 1) + " step to get there or above")
    else:
        print("It takes " + str(steps - 1) + " steps to get there or above")