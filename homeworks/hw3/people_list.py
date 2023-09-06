"""
File: people_list.py
Author: Alfonso Sebastian Martinez
Date: 09/27/2021
Section: 42
E-mail: amartin6@umbc.edu
Description: adds, subtracts, or takes the longest name on a list
"""

if __name__ == '__main__':
    list_of_people = []
    how_many_steps = int(input("How many steps should we run? "))
    for i in range(how_many_steps):
        user_command = input("Enter command: ")
        command_list = user_command.split(" ")
        if command_list[0] == "add":
            list_of_people.append(command_list[1])
            print(command_list[1] + " added.")
        elif command_list[0] == "remove":
            if command_list[1] in list_of_people:
                list_of_people.remove(command_list[1])
                print(command_list[1] + " removed.")
            else:
                print("User is not in the list")
        elif command_list[0] == "max":
            current_max_length_name = list_of_people[0]
            for j in range(len(list_of_people)):
                if len(current_max_length_name) < len(list_of_people[j]):
                    current_max_length_name = list_of_people[j]
                elif len(current_max_length_name) == len(list_of_people[j]):
                    if list_of_people[j] > current_max_length_name:
                        current_max_length_name = list_of_people[j]
            print("The max name is " + current_max_length_name)
