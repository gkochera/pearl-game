"""
pearl.py - main file
author: george kochera
last updated: 8/6/20
"""

import pygame
import pearl_assets

# constants
WIDTH = pearl_assets.WIDTH
HEIGHT = pearl_assets.HEIGHT

""" GAME CODE STARTS HERE"""

# initialize the game
pygame.init()

# load font
font_med = pygame.font.Font('OpenSans-Semibold.ttf', 60)
font_large = pygame.font.Font('OpenSans-Semibold.ttf', 90)

# set the screen size
screen = pygame.display.set_mode([WIDTH, HEIGHT])

# game loop
running = True
game_started = False
while running:

    # detect quits
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # space bar to start the game
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            # create a surface
            background = pygame.Surface(screen.get_size())
            background.fill(pearl_assets.WHITE)

            # call the new game routine which draws the lines
            # setup the game
            p = pearl_assets.new_game(background)

            # draw the frame/screen
            screen.blit(background, (0, 0))

            # set the game started flag
            game_started = True

        # right mouse click to place a piece
        if event.type == pygame.MOUSEBUTTONDOWN and game_started and not p.game_won:
            position = pygame.mouse.get_pos()
            pearl = p.get_square_from_click(position)
            quadrant = pearl_assets.get_quadrant_from_click(position, pearl)

            if p.is_valid_move(pearl, quadrant):
                p.draw_straight_segment(background, pearl, quadrant)
                screen.blit(background, (0, 0))

            # check for a winning condition
            if p.check_for_winning():
                text_surface = font_med.render("YOU WON!", True, pearl_assets.BLACK)
                text_rect = text_surface.get_rect()
                text_rect.center = ((WIDTH // 2), (HEIGHT // 2))
                screen.blit(text_surface, text_rect)

        if not game_started:
            text_surface = font_med.render("Press Space to Begin", True, pearl_assets.WHITE)
            text_rect = text_surface.get_rect()
            text_rect.center = ((WIDTH // 2), (HEIGHT // 2))
            screen.blit(text_surface, text_rect)
    pygame.display.flip()

pygame.quit()
