# a_template
'''
title: pygame template file
author: kliment lo
date-created: 2023/25/10
'''

import pygame

class Window:
    '''
    Create the window that will load the game
    '''

    def __init__(self, TITLE, WIDTH, HEIGHT, FPS):
        self.__TITLE = TITLE # text that appears in the title bar
        self.__FPS = FPS  # FRAMES per second (usually stick to 30, but 60 is also okay)
        self.__WIDTH = WIDTH
        self.__HEIGHT = HEIGHT
        self.__SCREEN_DIMENSIONS = (self.__WIDTH, self.__HEIGHT)
        self.__CLOCK = pygame.time.Clock() # load pygame's internal clock
        self.__SURFACE = pygame.display.set_mode(self.__SCREEN_DIMENSIONS) # creates the pygame surface for everything to be placed on
        self.__SURFACE.fill((50, 50, 50)) #color the surface grey
        pygame.display.set_caption(self.__TITLE)# set the dislpay window title the title text

    def updateFrame(self):
        self.__CLOCK.tick(self.__FPS) # waits for the appropriate time to update the screen
        pygame.display.flip()

    def getSurface(self):
        return self.__SURFACE


class Text:
    '''
    Create a text object to put on the screen
    '''

    def __init__(self, TEXT):
        self.__TEXT = pygame.font.SysFont("Arial", 48)
        self.__SURFACE = self.__TEXT.render(TEXT, 1, (255, 255, 255)) # it also knows basic color names "dark blue" "pink" "green" [replaces the tuple]

    def getSurface(self):
        return self.__SURFACE


if __name__ == "__main__":
    pygame.init() # initializes the pygame engine

    WINDOW = Window("My Template", 800, 600, 30)
    TEXT = Text("Hello World")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # checks if the red "X" button is clicked, OR ELSE IT WONT CLOSE BY CLICKING THE X BUTTON :O
                pygame.quit()
                exit()

        WINDOW.getSurface().blit(TEXT.getSurface(), (0,0))
        WINDOW.updateFrame()

