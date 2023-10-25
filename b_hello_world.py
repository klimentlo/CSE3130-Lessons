#b_hello_world.py
'''
title: working with text
author: kliment lo
date-created: 2024/10/25
'''
import pygame

class Color:
    WHITE = (255,255,255)
    GREY = (50,50,50)
    RED = (255,0,0)
    GREEN = (0,255,0)
    BLUE = (0,0,255)

class Window:
    '''
    creates the window that will load pygame
    '''

    def __init__(self, TITLE, WIDTH, HEIGHT, FPS):
        self.__TITLE = TITLE
        self.__FPS = FPS
        self.__WIDTH = WIDTH
        self.__HEIGHT = HEIGHT
        self.__SCREEN_DIMENSIONS = (self.__WIDTH, self.__HEIGHT)
        self.__CLOCK = pygame.time.Clock()
        self.__SURFACE = pygame.display.set_mode(self.__SCREEN_DIMENSIONS)
        self.__SURFACE.fill(Color.GREY) # pulls the color from color class
        pygame.display.set_caption(self.__TITLE)

    def clearScreen(self):
        self.__SURFACE.fill(Color.GREY)

    def updateFrame(self):
        self.__CLOCK.tick(self.__FPS)
        pygame.display.flip()

    def getSurface(self):
        return self.__SURFACE

    def getWidth(self):
        return self.__WIDTH

    def getHeight(self):
        return self.__HEIGHT

class Text:
    '''
    Creates a text object to put on the screen
    '''

    def __init__(self, TEXT, X=0, Y=0):
        self.__TEXT = pygame.font.SysFont(("Arial", 48),50)
        self.__SURFACE = self.__TEXT.render(TEXT,1,Color.GREEN)
        self.__X = X
        self.__Y = Y
        self.__POS = (self.__X,self.__Y) # position of sprite (POS)

    # MODIFIER METHODS
    def marqueenX(self, MAX_X):
        self.__X = self.__X + 5
        if self.__X > MAX_X:
            self.__X = 0
        self.__POS = (self.__X, self.__Y)


    # ACCESSOR METHODS
    def getSurface(self):
        return self.__SURFACE

    def getPOS(self):
        return self.__POS

if __name__ == "__main__":
    pygame.init()

    WINDOW = Window("text sprites", 800, 600, 30)
    TEXT = Text("Hello World", WINDOW.getWidth()//2, WINDOW.getHeight()//2)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()


        TEXT.marqueenX(WINDOW.getWidth())

        WINDOW.clearScreen()
        WINDOW.getSurface().blit(TEXT.getSurface(), TEXT.getPOS())
        WINDOW.updateFrame()