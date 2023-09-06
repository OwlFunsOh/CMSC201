"""
File:    rewrite_replace.py
Author:  Alfonso Sebastian Apelacio Martinez
Date:    10/21/2021
Section: 42
E-mail:  amartin6@umbc.edu
Description:
  DESCRIPTION OF WHAT THE PROGRAM DOES
"""

def rewrite_replace(the_string, look_for, replace_with):
    # this first part combines the string with no spaces
    # string = the_string.split()
    # string = "".join(string)
    new_string_list = []

    previous_index = 0

    # This for i loop checks for look_for string in the string list
    for i in range(len(the_string)):
        if the_string[i:i + len(look_for)] == look_for:
            new_string_list.append(the_string[previous_index:i])
            new_string_list.append(replace_with)
            previous_index = i + len(look_for)
        if i == len(the_string) - 1 and the_string[previous_index:i] != look_for:
            new_string_list.append(the_string[previous_index:i + 1])


    return "".join(new_string_list)



if __name__ == '__main__':
    # saves user input into variables for use in rewrite_replace() parameters
    user_string = input("What is the total string? ")
    user_look_for = input("What string should we look for? ")
    user_replace = input("What string should we replace that string with? ")

    print(rewrite_replace(user_string, user_look_for, user_replace))