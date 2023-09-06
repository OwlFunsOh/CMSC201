"""
File: ab_verify.py
Author: Alfonso Sebastian Apelacio Martinez
Date: 12/03/2021
Section: 42
E-mail: amartin6@umbc.edu
Description:
"""


def ab_verify(string, index):
    # base cases/simple cases
    if len(string) < 1:
        return False

    elif string[index] == "b":
        # False if no a's
        if index == 0:
            return False
        else:
            # return True if index >= num_bs
            # return False if index < num_bs
            num_bs = 0
            for each_letter in string:
                print(f"{num_bs} in first elif")
                if each_letter == "b":
                    num_bs += 1
                    print(f"{num_bs} after change")
                    print(index)
                    if index < num_bs:
                        return False
            return True

    elif "b" not in string:
        return True

    # recursive case
    # below counts number of a's in the beginning
    else:
        if index + 1 <= len(string) - 1:
            index += 1
            index = ab_verify(string, index) + 1
            num_bs = 0
            for each_letter in string:
                print(each_letter)
                if each_letter == "b":
                    num_bs = num_bs + 1
                    print(num_bs)
                elif index < num_bs:
                    return False
                elif index >= num_bs:
                    return True
            return index
        return 1


    # if number of a's >= number of b's, return True
    # if number of b's > number of a's, return False









if __name__ == "__main__":
    s = input('Enter a string to test: ')
    while s != 'quit':
        print(ab_verify(s, 0))
        s = input('Enter a string to test: ')