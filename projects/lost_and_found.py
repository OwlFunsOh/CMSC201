"""
File: lost_and_found.py
Author: Alfonso Sebastian Apelacio Martinez
Date: 11/08/2021
Section: 42
E-mail: amartin6@umbc.edu
Description
"""
"""
    Starter code for Lost and Found Project 2, CMSC 201 Fall 2021
"""

import json


USE = 'e'
EMPTY = ''
FLOOR = '_'
EXIT = 'x'
DOOR = 'd'
SECRET = 's'
WALL = '*'
ITEMS = 'i'
STARTING_LOCATION = 'start'


def load_map(map_file_name):
    """
        When a map file name is passed the file will load the grid and return it.
        Should you modify this function? No you shouldn't.

    :param map_file_name: a string representing the file name.
    :return: a 2D list which contains the current map.
    """
    with open(map_file_name) as map_file:
        the_map = json.loads(map_file.read())

    return the_map


#The code below sets the default spawn point to 0,0 if a start position was not found
def set_spawn(the_game_map):
    spawn = [0, 0]
    for the_row in range(len(the_game_map)):
        for grid_square in range(len(the_game_map[the_row])):
            if the_game_map[the_row][grid_square]["symbol"] == "start":
                #grid_square = x-value, the_row = y-value
                spawn = [grid_square, the_row]
    return spawn

# Turns secret areas into walls. Also saves the fact that it's a secret area
def hide_secret_areas(the_game_map):
    for row in range(len(the_game_map)):
        for column in range(len(the_game_map[row])):
            if the_game_map[row][column]["symbol"] == "s":
                the_game_map[row][column]["symbol"] = WALL
                the_game_map[row][column]["secret"] = True

    return the_game_map


# The code below will be for player movement. It takes the current position
# and moves one space in any direction except diagonals
def player_movement(movement_key, current_position, the_game_map):
    x_position, y_position = current_position

    #going up
    if movement_key.lower() == "w" and y_position > 0:
        if the_game_map[y_position - 1][x_position]["symbol"] == WALL or \
                the_game_map[y_position - 1][x_position]["symbol"] == DOOR:
            print("Can't go there")
        else:
            y_position -= 1

    #going left
    elif movement_key.lower() == "a" and x_position > 0:
        if the_game_map[y_position][x_position - 1]["symbol"] == WALL or \
                the_game_map[y_position][x_position - 1]["symbol"] == DOOR:
            print("Can't go there")
        else:
            x_position -= 1

    #going down
    elif movement_key.lower() == "s" and y_position < len(the_game_map) - 1:
        if the_game_map[y_position + 1][x_position]["symbol"] == WALL or \
                the_game_map[y_position + 1][x_position]["symbol"] == DOOR:
            print("Can't go there")
        else:
            y_position += 1

    #going right
    elif movement_key.lower() == "d" and x_position < len(the_game_map[0]) - 1:
        if the_game_map[y_position][x_position + 1]["symbol"] == WALL or \
                the_game_map[y_position][x_position + 1]["symbol"] == DOOR:
            print("Can't go there")
        else:
            x_position += 1

    else:
        print("Can't go there")

    current_position = x_position, y_position
    return current_position



# The code below makes secret a door once revealed
def is_secret(the_game_map, x_position, y_position):
    if "secret" in the_game_map[y_position][x_position]:
        if the_game_map[y_position][x_position]["secret"] == True:
            the_game_map[y_position][x_position]["symbol"] = DOOR
            print("You discovered a secret!")

def player_action(the_game_map, position, inventory):
    x_position, y_position = position
    requirements_met = True

    # Checks up
    if y_position > 0:
        if the_game_map[y_position - 1][x_position]["symbol"] == DOOR:
            if "requires" in the_game_map[y_position - 1][x_position]:
                for i in range(len(the_game_map[y_position - 1][x_position]["requires"])):
                    if the_game_map[y_position - 1][x_position]["requires"][i] not in inventory:
                        requirements_met = False
            if requirements_met:
                the_game_map[y_position - 1][x_position]["symbol"] = FLOOR
                print(f"A door has been opened")

        if the_game_map[y_position - 1][x_position]["symbol"] == WALL:
            is_secret(the_game_map, x_position, y_position - 1)

    # Checks left
    if x_position > 0:
        if the_game_map[y_position][x_position - 1]["symbol"] == DOOR:
            if "requires" in the_game_map[y_position][x_position - 1]:
                for i in range(len(the_game_map[y_position][x_position - 1]["requires"])):
                    if the_game_map[y_position][x_position - 1]["requires"][i] not in inventory:
                        requirements_met = False
            if requirements_met:
                the_game_map[y_position][x_position - 1]["symbol"] = FLOOR
                print(f"A door has been opened")

        if the_game_map[y_position][x_position - 1]["symbol"] == WALL:
            is_secret(the_game_map, x_position - 1, y_position)


    # Checks down
    if y_position < len(the_game_map) - 1:
        if the_game_map[y_position + 1][x_position]["symbol"] == DOOR:
            if "requires" in the_game_map[y_position + 1][x_position]:
                for i in range(len(the_game_map[y_position + 1][x_position]["requires"])):
                    if the_game_map[y_position + 1][x_position]["requires"][i] not in inventory:
                        requirements_met = False
            if requirements_met:
                the_game_map[y_position + 1][x_position]["symbol"] = FLOOR
                print(f"A door has been opened")

        if the_game_map[y_position + 1][x_position]["symbol"] == WALL:
            is_secret(the_game_map, x_position, y_position + 1)

    # Checks right
    if x_position < len(the_game_map[0]) - 1:
        if the_game_map[y_position][x_position + 1]["symbol"] == DOOR:
            if "requires" in the_game_map[y_position][x_position + 1]:
                print(the_game_map[y_position][x_position + 1]["requires"])
                for i in range(len(the_game_map[y_position][x_position + 1]["requires"])):
                    if the_game_map[y_position][x_position + 1]["requires"][i] not in inventory:
                        requirements_met = False
            if requirements_met:
                the_game_map[y_position][x_position + 1]["symbol"] = FLOOR
                print(f"A door has been opened")

        if the_game_map[y_position][x_position + 1]["symbol"] == WALL:
            is_secret(the_game_map, x_position + 1, y_position)

def check_for_items(the_game_map, position, inventory):
    x_position, y_position = position
    if "items" in the_game_map[y_position][x_position]:
        for i in range(len(the_game_map[y_position][x_position]["items"])):
            inventory.append(the_game_map[y_position][x_position]["items"][i])
            print(f"You got the {the_game_map[y_position][x_position]['items']}")

    return inventory



def play_game(the_game_map):
    if the_game_map:
        # prints the map
        for the_row in the_game_map:
            for grid_square in the_row:
                print(grid_square["symbol"], end="     ")
            print()

        # prints the spawn location
        position = set_spawn(the_game_map)
        print(f"\nYour spawn location is at {position}!")

        exit_found = False
        player_inventory = []
        action = input("Enter move (wasd) (e to activate doors or secrets) ")


        while not exit_found and action != "quit":
            if action != "e":
                position = player_movement(action, position, the_game_map)
                x_position, y_position = position
                if the_game_map[y_position][x_position]["symbol"] == EXIT:
                    exit_found = True
                    print(f"Congratulations on finding the exit at {position}!")
                else:
                    print(f"Your current position is now {position}")
                    check_for_items(the_game_map, position, player_inventory)
                    action = input("Enter move (wasd) (e to activate doors or secrets) ")
            else:
                player_action(the_game_map, position, player_inventory)
                action = input("Enter move (wasd) (e to activate doors or secrets) ")


if __name__ == "__main__":
    map_file_name = input('What map do you want to load? ')
    the_game_map = load_map(map_file_name)

    # Takes out all of the "s" and turns into WALL.
    game_map = hide_secret_areas(the_game_map)
    play_game(game_map)

