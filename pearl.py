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


# functions
def splash_screen():

    # black background
    bground = pygame.Surface(screen.get_size())
    bground.fill(pearl_assets.BLACK)

    # press space to begin
    press_space_text = font_med.render("Press Space to Begin", True, pearl_assets.WHITE)
    press_space_rect = press_space_text.get_rect()
    press_space_rect.center = ((WIDTH // 2), (9 * HEIGHT // 10))

    # title
    title_text = font_med.render("Pearl Puzzle", True, pearl_assets.WHITE, pearl_assets.RED)
    title_rect = title_text.get_rect()
    title_rect.center = ((WIDTH // 2), (HEIGHT // 12))

    # instructions
    base_rect_x, base_rect_y = (WIDTH // 2), ( HEIGHT // 5)
    reset_text = font_sm.render("Press [SPACE] to reset the puzzle.", True, pearl_assets.WHITE)
    reset_rect = reset_text.get_rect()
    reset_rect.center = base_rect_x, base_rect_y

    x_to_quit_text = font_sm.render("Press [x] to quit the puzzle and return to title screen.", True, pearl_assets.WHITE)
    x_to_quit_rect = x_to_quit_text.get_rect()
    x_to_quit_rect.center = base_rect_x, base_rect_y + 50

    press_q_to_quit_text = font_sm.render("Press [q] to quit the game.", True, pearl_assets.WHITE)
    press_q_to_quit_rect = press_q_to_quit_text.get_rect()
    press_q_to_quit_rect.center = base_rect_x, base_rect_y + 100

    rules_1_text = font_sm.render("You must go through all pearls.", True, pearl_assets.WHITE)
    rules_1_rect = rules_1_text.get_rect()
    rules_1_rect.center = base_rect_x, base_rect_y + 200

    rules_2_text = font_sm.render("You must turn before or after a WHITE pearl.", True, pearl_assets.WHITE)
    rules_2_rect = rules_2_text.get_rect()
    rules_2_rect.center = base_rect_x, base_rect_y + 230

    rules_3_text = font_sm.render("You must NOT turn before or after a BLACK pearl.", True, pearl_assets.WHITE)
    rules_3_rect = rules_3_text.get_rect()
    rules_3_rect.center = base_rect_x, base_rect_y + 260

    rules_4_text = font_sm.render("You must go STRAIGHT through WHITE pearls.", True, pearl_assets.WHITE)
    rules_4_rect = rules_4_text.get_rect()
    rules_4_rect.center = base_rect_x, base_rect_y + 290

    rules_5_text = font_sm.render("You must TURN on BLACK pearls.", True, pearl_assets.WHITE)
    rules_5_rect = rules_5_text.get_rect()
    rules_5_rect.center = base_rect_x, base_rect_y + 330

    rules_6_text = font_sm.render("Click in the square near the edge you want to place a line.", True, pearl_assets.WHITE)
    rules_6_rect = rules_6_text.get_rect()
    rules_6_rect.center = base_rect_x, base_rect_y + 400

    author_text = font_tiny.render("Developed By: George Kochera", True, pearl_assets.GRAY)
    author_rect = author_text.get_rect()
    author_rect.center = ((WIDTH - 110), (HEIGHT - 12))


    # apply the text to the screen
    screen.blit(bground, (0, 0))
    screen.blit(press_space_text, press_space_rect)
    screen.blit(title_text, title_rect)
    screen.blit(reset_text, reset_rect)
    screen.blit(x_to_quit_text, x_to_quit_rect)
    screen.blit(press_q_to_quit_text, press_q_to_quit_rect)
    screen.blit(rules_1_text, rules_1_rect)
    screen.blit(rules_2_text, rules_2_rect)
    screen.blit(rules_3_text, rules_3_rect)
    screen.blit(rules_4_text, rules_4_rect)
    screen.blit(rules_5_text, rules_5_rect)
    screen.blit(rules_6_text, rules_6_rect)
    screen.blit(author_text, author_rect)

""" GAME CODE STARTS HERE"""

# initialize the game
pygame.init()

# load font
font_tiny = pygame.font.Font('OpenSans-Semibold.ttf', 14)
font_sm = pygame.font.Font('OpenSans-Semibold.ttf', 24)
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

        # x to quit to main screen
        if event.type == pygame.KEYDOWN and event.key == pygame.K_x:
            game_started = False

        if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
            running = False

        # right mouse click to place a piece
        if event.type == pygame.MOUSEBUTTONDOWN and game_started and not p.game_won:
            position = pygame.mouse.get_pos()
            pearl = p.get_square_from_click(position)
            quadrant = pearl_assets.get_quadrant_from_click(position, pearl)
            if p.is_valid_move(pearl, quadrant):
                p.draw_straight_segment(background, pearl, quadrant)
                screen.blit(background, (0, 0))
                p.set_move_constraints()

                # check for a winning condition
                if p.check_for_winning():
                    text_surface = font_large.render("YOU WON!", True, pearl_assets.BLACK)
                    text_rect = text_surface.get_rect()
                    text_rect.center = ((WIDTH // 2), (HEIGHT // 2))
                    screen.blit(text_surface, text_rect)

                if p.check_for_losing():
                    text_surface = font_large.render("YOU LOST!", True, pearl_assets.RED)
                    text_rect = text_surface.get_rect()
                    text_rect.center = ((WIDTH // 2), (HEIGHT // 2))
                    screen.blit(text_surface, text_rect)

        if not game_started:
            splash_screen()
    pygame.display.flip()

pygame.quit()
