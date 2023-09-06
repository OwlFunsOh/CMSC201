"""
File:    mad_py_lib.py
Author:  Alfonso Sebastian Martinez
Date:    09/14/2021
Section: Section 42
E-mail:  amartin6@umbc.edu
Description:
  This program asks for words to put into a mad libbed story
"""

#asks for user inputs to put into the story
user_name = input("Tell me your name: ")
subject = input("Tell me a subject/thing (noun): ")
adjective = input("Tell me an adjective: ")
verb = input("Tell me a verb: ")
noun_two = input("Tell me a noun: ")

#prints the story
print("Hello " + user_name + ", we are going to have an amazing semester learning " \
      + subject + ", it's going to be " + adjective + " so don't worry if you need to "\
      + verb + " from a " + noun_two + ".")