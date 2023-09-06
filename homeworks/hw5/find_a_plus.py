"""
File:    minor_key.py
Author:  Alfonso Sebastian Apelacio Martinez
Date:    10/21/2021
Section: 42
E-mail:  amartin6@umbc.edu
Description:
  DESCRIPTION OF WHAT THE PROGRAM DOES
"""

import random

def generate_grid(m, n, seed=0):
   if seed:
       random.seed(seed)
   return [[random.choice(['.', '*']) for _ in range(n)] for _ in range(m)]

def display_grid(the_grid):
   for row in the_grid:
       print(' '.join(row))

def is_plus_there(my_grid):
    plus_here = False
    for i in range(1, len(my_grid) - 1):
        for j in range(1, len(my_grid[i] ) - 1):
            if my_grid[i][j] == "*" and my_grid[i - 1][j] == "*" and my_grid[i + 1][j] == "*" and \
                    my_grid[i][j - 1] == "*" and my_grid[i][j + 1] == "*":
                plus_here = True
    return plus_here


if __name__ == '__main__':
    numbers = input('Enter the dimensions (and optionally the seed): ').split()
    x = int(numbers[0])
    y = int(numbers[1])
    the_seed = int(numbers[2])
    a_grid = generate_grid(x, y, the_seed)
    display_grid(a_grid)

    print(is_plus_there(a_grid))