"""
File:         names.py
Author:       Alfonso Sebastian Apelacio Martinez
Date:         10/25/2021
Section:      42
E-mail:       amartin6@umbc.edu
Description:  YOUR DESCRIPTION GOES HERE AND HERE
              YOUR DESCRIPTION CONTINUED SOME MORE
"""


def sum_list(numbers):
    """
    Sums a list of integers
    :param numbers: a list of integers
    :return: the sum of the integers in numbers
    """

    sum = 0
    for i in range(len(numbers)):
        sum += numbers[i]
    return sum


def get_string_lengths(strings):
    """
    Given a list of strings, return a list of integers representing
    the lengths of the input strings
    :param strings: a list of strings
    :return: a list of integers representing the lengths of the input strings
    """

    string_lengths = []
    for i in range(len(strings)):
        string_lengths.append(len(strings[i]))

    return string_lengths


def get_names():
    """
    Asks the user for a list of names
    :return: a list of strings for the names the user entered
    """

    list_of_names = []
    name = input("Enter a name, STOP to stop: ")

    while name != "STOP":
        list_of_names.append(name)
        name = input("Enter a name, STOP to stop: ")
    return list_of_names

if __name__ == '__main__':
    kitties = [
        "Jules",
        "Stubby",
        "Tybalt",
        "Scooter",
        "KC",
        "Garfield",
        "Bucky"
    ]

    # print the sum of the lengths of the strings in kitties

    kitty_name_length = get_string_lengths(kitties)
    print(sum_list(kitty_name_length))

    puppers = [
        "Charlie",
        "Chuck",
        "Chuckadero",
        "Char",
        "Charmander",
        "Charles, Lord of Hearts, King of Snuggles"
    ]

    # prints the sum of the lengths of the strings in puppers
    pupper_name_length = get_string_lengths(puppers)
    print(sum_list(pupper_name_length))

    # gets names from the user and reports how many letters are in all the names
    names_output = get_names()
    names_output_length = get_string_lengths(names_output)
    print("There are " + str(sum_list(names_output_length)) + " letters in the names you entered")
