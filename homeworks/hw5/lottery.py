"""
File: lottery.py
Author: Alfonso Sebastian Apelacio Martinez
Date: 10/18/2021
Section: 42
E-mail: amartin6@umbc.edu
Description:
"""

from random import randint, sample

#definitions
def get_ticket():
    white_balls = sample(range(1,70),5)
    white_balls.sort()
    ticket = (white_balls, randint(1,26))
    return ticket

def check_ticket(test_ticket, winning_ticket, grand_prize):
    similarities = 0
    for i in range(5):
        if test_ticket[i] == winning_ticket[i]:
            similarities += 1
    if test_ticket[5] == winning_ticket[5]:
        if similarities < 2:
            print("This ticket wins $4")
        elif similarities == 2:
            print("This ticket wins $7")
        elif similarities == 3:
            print("This ticket wins $100")
        elif similarities == 4:
            print("This ticket wins $50000")
        else:
            print("This ticket wins $" + str(grand_prize))
    else:
        if similarities < 3:
            print("This ticket wins $0")
        elif similarities == 3:
            print("This ticket wins $7")
        elif similarities == 4:
            print("This ticket wins $100")
        else:
            print("This ticket wins $1000000")

if __name__ == '__main__':
    winning_ticket = input("What is the winning ticket? (Put the powerball last) ")
    test_ticket = input("What is the test ticket? (Put the powerball last) ")
    grand_prize = int(input("What is the grand prize? "))
    winning_ticket = winning_ticket.split()
    test_ticket = test_ticket.split()
    
    check_ticket(winning_ticket, test_ticket, grand_prize)
