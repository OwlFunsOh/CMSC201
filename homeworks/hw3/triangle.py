"""
File: triangle.py
Author: Alfonso Sebastian Martinez
Date: 09/27/2021
Section: 42
E-mail: amartin6@umbc.edu
Description: prints a right angle triangle
"""

if __name__ == '__main__':
    dimensions = int(input("What is the height/width of the triangle? "))
    for i in range(dimensions):
        for j in range(dimensions - i):
            print(" ", end="")
        for k in range(i + 1):
            print("*", end="")
        print()
