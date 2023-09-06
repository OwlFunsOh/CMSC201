"""
File:    minor_key.py
Author:  Alfonso Sebastian Apelacio Martinez
Date:    T10/20/2021
Section: 42
E-mail:  amartin6@umbc.edu
Description:
  DESCRIPTION OF WHAT THE PROGRAM DOES
"""

# is_flat() makes the word "flat" into the flat sign for your starting note
def is_flat(note):
    note_list = note.split()
    if "flat" in note_list:
        note_list.remove("flat")
        note_list.append("\u266d")
        note_list = "".join(note_list)
        return note_list
    else:
        return note

# starting_note_scale() finds the index of the starting note in the all_notes list
def starting_note_scale(starting_note):
    all_notes = ['C', 'D\u266d', 'D', 'E\u266d', 'E', 'F', 'G\u266d', 'G', 'A\u266d', 'A', 'B\u266d', 'B']
    for i in range(len(all_notes)):
        if starting_note == all_notes[i]:
            index_output = i
            return index_output



if __name__ == '__main__':
    musical_notes = ['C', 'D\u266d', 'D', 'E\u266d', 'E', 'F', 'G\u266d', 'G', 'A\u266d', 'A', 'B\u266d', 'B']

    # asks for the starting note
    starting_note = input("Enter a starting note (C, D flat): ")

    while starting_note != "quit":
        # Below converts the word flat into a flat symbol
        starting_note = is_flat(starting_note)


        if starting_note_scale(starting_note) == None:
            print("There is no " + starting_note + " in the scale")
        else:
            starting_index = starting_note_scale(starting_note)

        # displays the scale based on starting note
            true_scale = []
            for i in range(len(musical_notes[starting_index:])):
                true_scale.append(musical_notes[i + starting_index])
            for j in range(len(musical_notes) - len(true_scale) + 1):
                true_scale.append(musical_notes[j])
        #below prints the scale
            print(true_scale[0], end=" ")
            print(true_scale[2], end=" ")
            print(true_scale[3], end=" ")
            print(true_scale[5], end=" ")
            print(true_scale[7], end=" ")
            print(true_scale[8], end=" ")
            print(true_scale[11], end=" ")
            print(true_scale[12])

        starting_note = input("Enter a starting note (C, D flat): ")
