"""
    Come up with a name for the game

    JMPs and HLTs
"""

import random

GRID_WIDTH = 8
GRID_HEIGHT = 3
DICE_SIDES = 6


def generate_random_map(length, the_seed=0):
    """
        :param length - the length of the map
        :param the_seed - the seed of the map
        :return: a randomly generated map based on a specific seed, and length.
    """
    if the_seed:
        random.seed(the_seed)
    map_list = []
    for _ in range(length - 2):
        random_points = random.randint(1, 100)
        random_position = random.randint(0, length - 1)
        map_list.append(random.choices(['nop', f'add {random_points}', f'sub {random_points}', f'mul {random_points}', f'jmp {random_position}', 'hlt'], weights=[5, 2, 2, 2, 3, 1], k=1)[0])

    return ['nop'] + map_list + ['hlt']


def make_grid(table_size):
    """
    :param table_size: this needs to be the length of the map
    :return: returns a display grid that you can then modify with fill_grid_square (it's a 2d-grid of characters)
    """
    floating_square_root = table_size ** (1 / 2)

    int_square_root = int(floating_square_root) + (1 if floating_square_root % 1 else 0)
    table_height = int_square_root
    if int_square_root * (int_square_root - 1) >= table_size:
        table_height -= 1

    the_display_grid = [[' ' if j % GRID_WIDTH else '*' for j in range(GRID_WIDTH * int_square_root + 1)]
                        if i % GRID_HEIGHT else ['*' for j in range(GRID_WIDTH * int_square_root + 1)]
                        for i in range(table_height * GRID_HEIGHT + 1)]
    return the_display_grid


def fill_grid_square(display_grid, size, index, message):
    """
    :param display_grid:  the grid that was made from make_grid
    :param size:  this needs to be the length of the total map, otherwise you may not be able to place things correctly.
    :param index: the index of the position where you want to display the message
    :param message: the message to display in the square at position index, separated by line returns.
    """
    floating_square_root = size ** (1 / 2)
    int_square_root = int(floating_square_root) + (1 if floating_square_root % 1 else 0)
    table_row = index // int_square_root
    table_col = index % int_square_root

    if table_row % 2 == 0:
        column_start = GRID_WIDTH * table_col
    else:
        column_start = GRID_WIDTH * (int_square_root - table_col - 1)

    for r, message_line in enumerate(message.split('\n')):
        for k, c in enumerate(message_line):
            display_grid[GRID_HEIGHT * table_row + 1 + r][column_start + 1 + k] = c

    return display_grid


def roll_dice():
    """
        Call this function once per turn.

        :return: returns the dice roll
    """
    return random.randint(1, DICE_SIDES)



def display_grid(size, seed):
    board_layout = make_grid(int(size))
    board_actions = generate_random_map(int(size), int(seed))

    for i in range(int(size)):
        fill_grid_square(board_layout, int(size), i, str(i) + "\n" + board_actions[i])

    for j in range(len(board_layout)):
        print("".join(board_layout[j]))


#will make a dictionary. Keys will be space number, values will be action
def action_dictionary(size, board_actions):
    #board_actions is a list. They will be values. Space number on board is the key
    action_on_space = {}
    for i in range(size):
        action_on_space[i] = board_actions[i]

    return action_on_space


#The following definition will handle all the math relating to score
def math_for_score(total, command, number):
    if command == "add":
        total = total + int(number)
    elif command == "sub":
        total = total - int(number)
    elif command == "mul":
        total = total * int(number)

    return total


def play_game(game_map):
    game_over = False
    #starting position of the game
    user_position = 0
    score = 0


    #action_on_the_space is a dictionary
    action_on_the_space = action_dictionary(len(game_map), game_map)
    while game_over != True:
    #updates position based on dice roll
        dice_roll = roll_dice()
        user_position += dice_roll

        if user_position > len(game_map) - 1:
            user_position = user_position % len(game_map)
        print()
        print("You rolled a " + str(dice_roll) + ". You are now in position " + str(user_position))


        current_space = action_on_the_space[user_position]

        print("The instruction on that position is " + current_space)

        current_space = current_space.split()

        if current_space[0] != "hlt" and current_space[0] != "nop" and current_space[0]\
           != "jmp":
            score = math_for_score(score, current_space[0], current_space[1])


        elif current_space[0] == "jmp":
            while current_space[0] == "jmp":
                user_position = int(current_space[1])
                current_space = action_on_the_space[user_position]

            if current_space[0] != "hlt" and current_space[0] != "nop" and current_space[0] \
                    != "jmp":
                score = math_for_score(score, current_space[0], current_space[1])

            elif current_space[0] == "hlt":
                game_over = True


        elif current_space[0] == "hlt":
            game_over = True
            

        print("Your score is now " + str(score))

    print()
    print("Final Position: " + str(user_position) + " Final score: " + str(score))

if __name__ == '__main__':
    play_again = "yes"

    while play_again == "yes":
        #asks the user for seed and board size
        size_and_seed = input("Enter board size and seed: ")
        size_and_seed = size_and_seed.split()

        display_grid(size_and_seed[0], size_and_seed[1])

        #sets the score
        board_actions = generate_random_map(int(size_and_seed[0]), int(size_and_seed[1]))
        play_game(board_actions)

        play_again = input("Would you like to play again? Type yes/no ")
    
