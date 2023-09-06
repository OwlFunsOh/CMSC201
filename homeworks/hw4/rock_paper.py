"""
File:    padovan.py
Author:  Alfonso Sebastian Martinez
Date:    10/05/2021
Section: 42
E-mail:  amartin6@umbc.edu
Description:
  DESCRIPTION OF WHAT THE PROGRAM DOES
"""

import sys
from random import choice, seed

if len(sys.argv) >= 2:
    seed(sys.argv[1])

if __name__ == '__main__':

    user_choice = input("Enter rock, paper, or scissors to play, stop to end. ")

    while user_choice != "stop":
        the_choice = choice(["paper", "rock", "scissors"])
        if user_choice != "rock" and user_choice != "paper" and user_choice != "scissors":
            print("You need to select rock, paper, or scissors")
            user_choice = input("Enter rock, paper, or scissors to play, stop to end. ")
        else:
            print(the_choice)
            if the_choice == user_choice:
                print("Both " + the_choice + ", there is a tie")
            elif the_choice == "rock":
                if user_choice == "paper":
                    print("Paper covers rock, You win")
                elif user_choice == "paper":
                    print("Rock crushes scissors, You lose")
            elif the_choice == "paper":
                if user_choice == "rock":
                    print("Paper covers rock, You lose")
                elif user_choice == "scissors":
                    print("Scissors cuts paper, You win")
            elif the_choice == "scissors":
                if user_choice == "paper":
                    print("Scissors cuts paper, You lose")
                elif user_choice == "rock":
                    print("Rock crushes scissors, You win")


            user_choice = input("Enter rock, paper, or scissors to play, stop to end. ")