"""
File: circular.py
Author: Alfonso Sebastian Martinez
DAte: 10/18/2021
Section: 42
E-mail: amartin6@umbc.edu
Description:
"""

if __name__ == '__main__':
    user_string = input("Enter a string: ")
    user_string = user_string.lower()
    split_string = user_string.split()

    #part 2C
    joined_list = "".join(split_string)

    repeated_string = ""
    repeat = "nope"
    actual_repeat = ""
    
    for k in range(1, len(joined_list)):
        if joined_list[0] == joined_list[k]:
            repeated_string = joined_list[0:k]
            if joined_list[k: k + len(repeated_string)] == repeated_string and repeat != "found":
                actual_repeat = repeated_string
                repeat = "found"

        if joined_list[k: len(actual_repeat) + k] == actual_repeat and repeat == "found":
            print(joined_list  + " is a rotation with offset " + str(k))

    if repeat == "nope":
        print("There are no rotations of the string")
