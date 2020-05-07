import pygame

import logging

from RPG import Attributes, States, Menus

# Logging Stuff
formatter = logging.Formatter("%(name)s:%(levelname)s: %(message)s")
file_handler = logging.FileHandler("RPG.log", mode='w')
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)


class Game:

    def create_logger(self, logger_name):
        """
        Logging Util Method for creating a logger
        :param logger_name: A String for the loggers name
        :return: logging.getLogger() with modified params
        """
        log = logging.getLogger(__name__+":"+logger_name)
        log.setLevel(logging.DEBUG)
        stream_handler.setLevel(self.log_level)
        log.addHandler(file_handler)
        log.addHandler(stream_handler)
        return log

    def __init__(self, debug=False):
        """
        Really only used for access to functions
        :param debug: Do you want debug? True or False
        """
        # Logging Init
        if debug:
            log_level = logging.DEBUG
        else:
            log_level = logging.ERROR
        stream_handler.setLevel(log_level)
        self.log_level = log_level
        log = self.create_logger("BASE")

        log.debug("Creating Empty Variables")
        self.screen = None
        self.clock = None

        self.state = None

    def init(self):
        """
        Initializes the actual game environment
        :return:
        """
        log = self.create_logger("INIT")

        log.info("Initializing Pygame and it's Variables")
        pygame.init()
        self.clock = pygame.time.Clock()

        log.debug("Creating Pygame Window and Setting Caption")
        self.screen = pygame.display.set_mode(Attributes.Game.Window.size)
        pygame.display.set_caption(Attributes.Game.name)

    def entry_point(self):
        log = self.create_logger("NTRY")

        log.info("Initializing Game Environment")
        self.init()

        log.info("Starting Main Loop")
        self.main()

    def main(self):
        log = self.create_logger("MNLP")

        log.debug("Main Loop Entered")

        log.debug("Check for None state")
        if self.state is None:
            log.info("No State. Changing to Main Menu state")
            self.state = States.Game.MAIN_MENU

        run = True
        while run:
            # Handle Pygame Window Closing
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    log.info("Pygame Window Closed. Quitting")
                    run = False

            # State Tree
            log.debug("Starting State Tree")
            if self.state == States.Game.QUIT:
                log.debug("State: QUIT")
                log.info("Quit State. Quitting")
                run = False
            elif self.state == States.Game.MAIN_MENU:
                log.debug("State: Main Menu")
                log.info("Starting Main Menu Loop")
                menu_choice = Menus.main_menu(self)
                self.state = Menus.handle_menu_choice(self, menu_choice, Menus.MAIN)
        pygame.quit()
