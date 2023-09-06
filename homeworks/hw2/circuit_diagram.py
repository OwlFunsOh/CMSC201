"""
FIle: circuit_diagram.py
Author: Alfonso Sebastian Martinez
Date: 02/20/2021
Section: 42
E-mail: amartin6@umbc.edu
Description: models a logic circuit
"""

var_a = int(input("Enter a: "))
var_b = int(input("Enter b: "))
var_c = int(input("Enter c: "))
var_d = int(input("Enetr d: "))
var_e = int(input("Enter e: "))

if var_a and (not var_d or var_e or (var_b and var_c)):
    print("The circuit outputs 1")
else:
    print("The circuit outputs 0")

