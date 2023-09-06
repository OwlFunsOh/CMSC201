"""
File:    factor_me.py
Author:  Alfonso Sebastian Martinez
Date:    10/08/2021
Section: 42
E-mail:  amartin6@umbc.edu
Description:

"""

if __name__ == '__main__':
    num_to_factor = int(input("Enter a number to factor: "))
    prime_factors = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    factors_into = []
    can_factor = "yes"
    while can_factor == "yes":
        for primes in prime_factors:
            can_factor_again = "yes"
            while can_factor_again == "yes":
                if num_to_factor % primes == 0:
                    num_to_factor = num_to_factor // primes
                    factors_into.append(str(primes))
                else:
                    can_factor_again = "no"

        can_factor = "no"
    print("The factors are: " + "*".join(factors_into))
    if num_to_factor > 1:
        print("This part of the number couldn't be factored with primes less than 50:  " \
                + str(num_to_factor))