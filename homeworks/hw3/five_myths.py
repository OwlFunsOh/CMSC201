"""
File: five_myths.py
Author: Alfonso Sebastian Martinez
Date: 09/27/2021
Section: 42
E-mail: amartin6@umbc.edu
Description: User gets asked for a subject, then says five myths. After that, user states if myth is true
"""

if __name__== '__main__':
    five_myths = []
    real_myths = []
    fake_myths = []
    subject = input("Tell me a subject: ")
    for i in range(5):
        new_myth = input("Tell me a myth about " + subject + ": ")
        five_myths.append(new_myth)
    for j in range(5):
        myth_yes_or_no = input("Is it actually a myth that: " + five_myths[j] + "? ")
        if myth_yes_or_no == "yes":
            real_myths.append(five_myths[j])
        else:
            fake_myths.append(five_myths[j])
    print("")
    print("Here are the myths: ")
    for k in range(len(real_myths)):
        print(real_myths[k])
    print("")
    print("Here are the non-myths which shouldn't have been included:")
    for l in range(len(fake_myths)):
        print(fake_myths[l])
