"""
File: basel.py
Author: Alfonso Sebastian Martinez
Section: 42
E-mail: amartin6@umbc.edu
Description: The code takes the sum of 1 / n ** 2
"""
if __name__== '__main__':
    approximation = 0
    terms_to_sum = int(input("What is the number of terms you want to sum? "))
    for i in range (terms_to_sum):
        approximation = approximation + (1 / (i + 1) ** 2)
    print("The approximation for " + str(terms_to_sum) + " terms is " + str(approximation))
