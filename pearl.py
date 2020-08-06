"""
pearl.py - main file
author: george kochera
last updated: 8/6/20
"""

import pygame
import random

# global variables
WIDTH = 700
HEIGHT = 700
black = (0, 0, 0)
red = (255, 0, 0)
white = (255, 255, 255)
squares = {}


# my functions
def draw_black_pearl(surface: pygame.Surface, key: int):
    w, h = squares[key]
    w += (WIDTH // 7) // 2
    h += (HEIGHT // 7) // 2
    pygame.draw.circle(surface, black, (w, h), 35)


def draw_white_pearl(surface: pygame.Surface, key: int):
    w, h = squares[key]
    w += (WIDTH // 7) // 2
    h += (HEIGHT // 7) // 2
    pygame.draw.circle(surface, black, (w, h), 35, 2)


def new_game(surface: pygame.Surface):
    # define the square locations
    index = 0
    for vert in range(0, HEIGHT, HEIGHT // 7):
        for horz in range(0, WIDTH, WIDTH // 7):
            squares[index] = (horz, vert)
            index += 1

    # color the background white
    surface.fill(white)

    # draw some vertical lines
    for i in range(WIDTH // 7, WIDTH, WIDTH // 7):
        pygame.draw.line(surface, black, (i, 0), (i, HEIGHT), 2)

    # draw some horizontal lines
    for j in range(HEIGHT // 7, HEIGHT, HEIGHT // 7):
        pygame.draw.line(surface, black, (0, j), (HEIGHT, j), 2)

    # set some pearls on the board
    for k in range(0, 9):
        position = random.randint(0, len(squares) - 1)
        if k % 2 == 0:
            draw_white_pearl(surface, position)
        else:
            draw_black_pearl(surface, position)


""" GAME CODE STARTS HERE"""

# initialize the game
pygame.init()

# set the screen size
screen = pygame.display.set_mode([WIDTH, HEIGHT])

# game loop
running = True
while running:

    # load the font
    if pygame.font:
        font = pygame.font.Font('OpenSans-Semibold.ttf', 36)

    # detect quits
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            # create a surface
            background = pygame.Surface(screen.get_size())

            # call the new game routine which draws the lines
            new_game(background)

            # draw the frame/screen
            screen.blit(background, (0, 0))

    pygame.display.flip()

pygame.quit()
