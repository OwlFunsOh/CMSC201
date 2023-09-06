"""
File: list_reverse.py
Author: Alfonso Martinez
Date: 10/04/2021
Section: 42
E-mail: amartin6@umbc.edu
Description:
"""

if __name__ == '__main__':
    user_list = input("Enter a list separated by commas: ")
    user_list = user_list.split(",")
    
    kept_strings = []
    removed_strings = []
    #Separates user_list into one element at a time to count characters in element
    for i in range(len(user_list)):    
        current_string = user_list[i]
        counter = 0
        string_removed = "no"
        
        while counter != len(current_string) and string_removed == "no":
            for number in range(10):
                if current_string[counter] == str(number):
                    string_removed = "yes"
            counter += 1
        if string_removed == "yes":
            removed_strings.append(user_list[i])
        else:
            kept_strings.append(user_list[i])
    kept_strings_backwards = []
    if len(kept_strings) != 0:
         for i in range(len(kept_strings) - 1, -1, -1):
             kept_strings_backwards.append(kept_strings[i])
         print(", ".join(kept_strings_backwards))
    else:
        print("The list is empty")
