"""
Filename: how_deep.py
Author: Alfonso Sebastian Apelacio Martinez
Date: 12/01/2021
Section: 42
E-mail: amartin6@umbc.edu
Description:
"""


def ab_equal(n,k,current):
    # base case
    if (n + k) % 2 != 0:
        print(current)

    elif n == 0:
        if k == 0:
            print(current)

    # recursive case
    else:
        ab_equal(n - 1, k + 1, current + 'a')
        ab_equal(n - 1, k - 1, current + 'b')

if __name__ == "__main__":
    print(ab_equal(6, 0, ""))
