"""
Filename: how_deep.py
Author: Alfonso Sebastian Apelacio Martinez
Date: 11/29/2021
Section: 42
E-mail: amartin6@umbc.edu
Description: Checks how deep the list is
"""

def how_deep(list_struct):
    current_depth = 0

    # base case
    if len(list_struct) == 0:
        return 1

    # recursive case
    else:
        depth = 1
        for each_list in list_struct:
            if len(each_list) != 0:
                depth = how_deep(each_list)
            if depth > current_depth:
                current_depth = depth
    return current_depth + 1
            
if __name__ == "__main__":
    print(how_deep([[[], [], [], [[[]]]], []]))
    print(how_deep([]))
    print(how_deep([[], []]))
    print(how_deep([[[]], [], [[]], [[[]]]]))
    print(how_deep([[[[], [[]], [[[]]], [[[[]]]]]]]))
    print(how_deep([[[], []], [], [[], []]]))
