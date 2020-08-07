"""
pearl.py - main file
author: george kochera
last updated: 8/6/20
"""
# library imports
import pygame
import random

# Constants
WIDTH = 700
HEIGHT = 700
COLS = 7
ROWS = 7
COL_WIDTH = WIDTH // COLS
ROW_HEIGHT = HEIGHT // ROWS
COL_CENTER = COL_WIDTH // 2
ROW_CENTER = ROW_HEIGHT // 2
NORTH = "North"
SOUTH = "South"
EAST = "East"
WEST = "West"
STRAIGHT = "Straight"
ANGLED = "Angled"

# Colors
BLACK = (0, 0, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)


class PearlBox:
    def __init__(self, position, row, col, index, center):
        self.north = False
        self.east = False
        self.south = False
        self.west = False
        self.contents = None
        self.center = center
        self.position = position
        self.color = None
        self.row = row
        self.col = col
        self.index = index
        self.visited = False

    def __repr__(self):
        return "PEARL - Color: {} - Position: {} - Center: {}".format(self.color, self.position, self.center)


def get_quadrant_from_click(position: tuple, pearl: PearlBox):
    x, y = position
    c_x, c_y = pearl.center
    rel_x = x - c_x
    rel_y = y - c_y
    abs_x = abs(rel_x)
    abs_y = abs(rel_y)
    if abs_y >= abs_x:
        if rel_y > 0:
            return SOUTH
        else:
            return NORTH
    else:
        if rel_x < 0:
            return WEST
        else:
            return EAST


class PearlGame:
    def __init__(self):
        self.last_move = None
        self.squares = {}
        self.first_move_made = False
        self.moved_from_pearl = None
        self.moved_to_pearl = None
        self.starting_box = None
        self.game_won = False

    def get_square_from_click(self, position: tuple):
        w, h = position
        row = h // ROW_HEIGHT
        col = w // COL_WIDTH
        square = col + (row * COLS)
        return self.squares[square]

    def is_valid_move(self, pearl: PearlBox, direction):

        # Keep player in bounds
        if direction == WEST and pearl.col == 0:
            return False
        if direction == EAST and pearl.col == COLS - 1:
            return False
        if direction == NORTH and pearl.row == 0:
            return False
        if direction == SOUTH and pearl.row == ROWS - 1:
            return False


        if self.first_move_made:

            # Determine the type of move
            if self.last_move == EAST or self.last_move == WEST:
                if direction == NORTH or direction == SOUTH:
                    type_of_move = ANGLED
                else:
                    type_of_move = STRAIGHT
            else:
                if direction == EAST or direction == WEST:
                    type_of_move = ANGLED
                else:
                    type_of_move = STRAIGHT
            print(type_of_move)

            # Enforce pearl rules, straight for white ones, and right angles for black ones.
            if pearl.color == BLACK and type_of_move != ANGLED:
                return False
            if pearl.color == WHITE and type_of_move != STRAIGHT:
                return False

            print(self.moved_to_pearl, pearl.index)
            # Enforce the line staying continuous
            if self.moved_to_pearl != pearl.index:
                return False


        return True

    def draw_straight_segment(self, surface: pygame.Surface, pearl: PearlBox, direction):
        # Record the pearl that was moved from
        self.moved_from_pearl = pearl.index
        pearl.visited = True

        # Calculate the line dimensions and determine the pearl that was moved to
        d_x, d_y = pearl.center
        if direction == NORTH:
            d_y -= ROW_HEIGHT
            self.moved_to_pearl = pearl.index - COLS
        elif direction == SOUTH:
            d_y += ROW_HEIGHT
            self.moved_to_pearl = pearl.index + COLS
        elif direction == EAST:
            d_x += COL_WIDTH
            self.moved_to_pearl = pearl.index + 1
        elif direction == WEST:
            d_x -= COL_WIDTH
            self.moved_to_pearl = pearl.index - 1

        # Draw the line and set the last move direction
        pygame.draw.line(surface, RED, pearl.center, (d_x, d_y), 3)
        self.last_move = direction
        if not self.first_move_made:
            self.first_move_made = True
            self.starting_box = pearl.index

    def check_for_winning(self):
        if self.moved_to_pearl == self.starting_box:
            self.game_won = True
            return True
        else:
            return False




def new_game(surface: pygame.Surface):
    """Creates a PearlGame instance, draws the lines, popluates the board and returns the game instance."""
    # create a pearl game instance
    p = PearlGame()

    # define the square locations
    index = 0
    for vert in range(0, HEIGHT, ROW_HEIGHT):
        for horz in range(0, WIDTH, COL_WIDTH):
            row = index // ROWS
            col = index % ROWS
            p.squares[index] = PearlBox((horz, vert), row, col, index, (horz + COL_CENTER, vert + ROW_CENTER))
            index += 1

    # color the background white
    surface.fill(WHITE)

    # draw some vertical lines
    for i in range(COL_WIDTH, WIDTH, COL_WIDTH):
        pygame.draw.line(surface, BLACK, (i, 0), (i, HEIGHT), 2)

    # draw some horizontal lines
    for j in range(ROW_HEIGHT, HEIGHT, ROW_HEIGHT):
        pygame.draw.line(surface, BLACK, (0, j), (HEIGHT, j), 2)

    # set some pearls on the board
    for k in range(0, 9):
        position = random.randint(0, len(p.squares) - 1)
        pearl = p.squares[position]
        if k % 2 == 0:
            draw_pearl(surface, pearl, WHITE)
        else:
            draw_pearl(surface, pearl, BLACK)

    return p


def draw_pearl(surface: pygame.Surface, pearl: PearlBox, color):
    w, h = pearl.position
    w += COL_CENTER
    h += ROW_CENTER
    pearl.center = w, h
    if color == BLACK:
        pygame.draw.circle(surface, BLACK, (w, h), 35)
        pearl.color = BLACK
    elif color == WHITE:
        pygame.draw.circle(surface, BLACK, (w, h), 35, 2)
        pearl.color = WHITE
    else:
        pearl.color = None
