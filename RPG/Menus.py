import pygame

import RPG

MAIN = 0


class CHOICES:
    class MAIN:
        WINDOW_CLOSE = 0
        QUIT = 1


def handle_menu_choice(game, menu_choice, menu):
    """
    Handler Method for menu selections
    :param game: instance of the game. Most of the time will be self when called
    :param menu_choice: the menu method response, ex. Menus.CHOICES.MAIN.QUIT
    :param menu: the menu method identifier, ex. Menus.MAIN
    :return: Game State from States
    """
    log = game.create_logger("MNHN")

    log.debug("Handling Menu Selection")
    if menu == MAIN:
        if menu_choice == CHOICES.MAIN.WINDOW_CLOSE:
            return RPG.States.Game.QUIT
        if menu_choice == CHOICES.MAIN.QUIT:
            return RPG.States.Game.QUIT


def main_menu(game):
    """
    Displays Main Menu with pygame
    :return: Menu Choice from Menus.CHOICES.MAIN
    """
    log = game.create_logger("M_MN")

    # pygame loop
    run = True
    while run:

        # Pygame Handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # Window Closed
                log.info("Window Closed. Quitting")
                return CHOICES.MAIN.WINDOW_CLOSE
            if event.type == pygame.KEYDOWN:
                # Key Pressed
                log.debug("Key Down Detected")
                if event.key == pygame.K_q:
                    # Quit Selected
                    log.info("Quit Selected. Quitting")
                    return CHOICES.MAIN.QUIT

        game.clock.tick(RPG.Attributes.Game.tick_rate)