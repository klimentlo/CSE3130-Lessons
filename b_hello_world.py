#b_hello_world.py
'''
title: working with text
author: kliment lo
date-created: 2024/10/25
'''
import pygame
from random import randrange

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

    def __init__(self, TEXT, X=0, Y=0, SPEED=5):
        self.__TEXT = TEXT
        self.__FONT = pygame.font.SysFont(("Arial", 48), 50)
        self.__SURFACE = self.__FONT.render(self.__TEXT, 1, Color.GREEN)
        self.__X = X
        self.__Y = Y
        self.__POS = (self.__X, self.__Y) # position of sprite (POS)
        self.__DIR_X = 1
        self.__DIR_Y = 1
        self.__SPD = SPEED

    # MODIFIER METHODS
    def setPOS(self, X, Y):
        self.__X = X
        self.__Y = Y
        self.__POS = (self.__X,self.__Y)

    def setSpeed(self, SPEED):
        self.__SPD = SPEED

    def marqueeX(self, MAX_X):
        self.__X = self.__X + self.__SPD
        if self.__X > MAX_X:
            self.__X = - self.getWidth() # if the text is 50 pixels long, it starts 50 pixels off the screen so it smoothly comes back
            choice = randrange(3)
            if choice == 0:
                choice = Color.RED
            elif choice == 1:
                choice = Color.BLUE
            elif choice == 2:
                choice = Color.GREEN
            self.__SURFACE = self.__FONT.render(self.__TEXT, 1, choice)
        self.__POS = (self.__X, self.__Y)

    def bounceX(self, MAX_X, MIN_X=0):

        self.__X += self.__DIR_X * self.__SPD
        if self.__X > MAX_X - self.getWidth():
            self.__DIR_X = -1
            choice = randrange(3)
            if choice == 0:
                choice = Color.RED
            elif choice == 1:
                choice = Color.BLUE
            elif choice == 2:
                choice = Color.GREEN
            self.__SURFACE = self.__FONT.render(self.__TEXT, 1, choice)

        if self.__X < MIN_X:
            self.__DIR_X = 1
            choice = randrange(3)
            if choice == 0:
                choice = Color.RED
            elif choice == 1:
                choice = Color.BLUE
            elif choice == 2:
                choice = Color.GREEN
            self.__SURFACE = self.__FONT.render(self.__TEXT, 1, choice)

        self.__POS = (self.__X, self.__Y)

    def bounceY(self, MAX_Y, MIN_Y=0):
        self.__Y += self.__DIR_Y * self.__SPD
        if self.__Y > MAX_Y - self.getHeight():
            self.__DIR_Y = -1
            choice = randrange(3)
            if choice == 0:
                choice = Color.RED
            elif choice == 1:
                choice = Color.BLUE
            elif choice == 2:
                choice = Color.GREEN
            self.__SURFACE = self.__FONT.render(self.__TEXT, 1, choice)

        if self.__Y < MIN_Y:
            self.__DIR_Y = 1
            choice = randrange(3)
            if choice == 0:
                choice = Color.RED
            elif choice == 1:
                choice = Color.BLUE
            elif choice == 2:
                choice = Color.GREEN
            self.__SURFACE = self.__FONT.render(self.__TEXT, 1, choice)
        self.__POS = (self.__X, self.__Y)



    # ACCESSOR METHODS
    def getSurface(self):
        return self.__SURFACE

    def getPOS(self):
        return self.__POS

    def getWidth(self):
        return self.__SURFACE.get_width()

    def getHeight(self):
        return self.__SURFACE.get_height()




if __name__ == "__main__":
    pygame.init()

    WINDOW = Window("text sprites", 800, 600, 60)
    # TEXT = Text("Hello World", WINDOW.getWidth()//2, WINDOW.getHeight()//2) # puts top left of text pixel right in the middle of the screen
    TEXT = Text("Hello")
    TEXT.setPOS(WINDOW.getWidth() // 2 - TEXT.getWidth() // 2, WINDOW.getHeight() // 2 - TEXT.getHeight() // 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()


        TEXT.bounceX(WINDOW.getWidth())
        TEXT.bounceY(WINDOW.getHeight())
        TEXT.setSpeed(5)
        WINDOW.clearScreen() # clear screen must be before getsurface
        WINDOW.getSurface().blit(TEXT.getSurface(), TEXT.getPOS())
        # TEXT2.marqueeX(WINDOW.getWidth())
        # TEXT2.setSpeed(100)
        # WINDOW.getSurface().blit(TEXT2.getSurface(), TEXT2.getPOS())


        WINDOW.updateFrame()