import random
import string
from pprint import pprint


def initialize_screen():
    with open("dictionary", "r") as file:
        terms = file.readlines()
    terms = [term.upper().strip() for term in terms]

    words = random.sample(terms, 6)

    grid_size = 20
    grid = [['_' for _ in range(grid_size)] for _ in range(grid_size)]

    orientations = ['leftright', 'updown', 'diagonalup', 'diagonaldown']

    for word in words:
        word_length = len(word)
        placed = False

        while not placed:
            orientation = random.choice(orientations)
            if orientation == 'leftright':
                step_x = 1
                step_y = 0
            if orientation == 'updown':
                step_x = 0
                step_y = 1
            if orientation == 'diagonalup':
                step_x = 1
                step_y = -1
            if orientation == 'diagonaldown':
                step_x = 1
                step_y = 1

            x_position = random.randint(0, grid_size - 1)
            y_position = random.randint(0, grid_size - 1)

            ending_x = x_position + (word_length * step_x)
            ending_y = y_position + (word_length * step_y)

            if ending_x < 0 or ending_x >= grid_size: continue
            if ending_y < 0 or ending_y >= grid_size: continue

            failed = False

            for i in range(word_length):
                character = word[i]

                new_position_x = x_position + i * step_x
                new_position_y = y_position + i * step_y

                char_new_position = grid[new_position_x][new_position_y]
                if char_new_position != '_':
                    if char_new_position == character:
                        continue
                    else:
                        failed = True
                        break
            if failed:
                continue
            else:
                for i in range(word_length):
                    character = word[i]

                    new_position_x = x_position + i * step_x
                    new_position_y = y_position + i * step_y

                    grid[new_position_x][new_position_y] = character
                placed = True

    for x in range(grid_size):
        for y in range(grid_size):
            if (grid[x][y] == '_'):
                grid[x][y] = random.choice(string.ascii_uppercase)

    print_grid(grid_size, grid, words)

def print_grid(grid_size, grid, words):
    for x in range(grid_size):
        print ('  '.join( grid[x] ))
    print("Words are: ")
    pprint(words)

