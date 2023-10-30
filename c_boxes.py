# c_boxes.py
'''
title: boxes
author: mike zhang
date-created: 2023-10-27
'''

import pygame
from random import randrange
from b_hello_world import Color


class Box:
    def __init__(self, WIDTH, HEIGHT, X=0, Y=0):
        self.__WIDTH = WIDTH
        self.__HEIGHT = HEIGHT
        self.__DIMENSIONS = (self.__WIDTH, self.__HEIGHT)
        self.__COLOR = Color.WHITE
        self.__SURFACE = pygame.Surface(self.__DIMENSIONS, pygame.SRCALPHA, 32) # 32 is color
        self.__SURFACE.fill(self.__COLOR)
        self.__X = X
        self.__Y = Y
        self.__DIR_X = 1
        self.__DIR_Y = 1
        self.__SPD = 5
        self.__POS = (self.__X, self.__Y)

    # Modifier Method
    def setColor(self, TUPLE):
        '''
        updates the color of the box
        :param: TUPLE: tuple
        :return: none
        '''
        self.__COLOR = TUPLE
        self.__SURFACE.fill(self.__COLOR)

    def bounce(self, MAX_X, MAX_Y):
        self.__X += self.__DIR_X * self.__SPD
        if self.__X > MAX_X - self.__WIDTH:
            self.__DIR_X = - 1
        if self.__X < 0:
            self.__DIR_X = 1

        self.__Y += self.__DIR_Y * self.__SPD
        if self.__Y > MAX_Y - self.__HEIGHT:
            self.__DIR_Y = -1
        if self.__Y < 0:
            self.__DIR_Y = 1

        self.__POS = (self.__X, self.__Y)

    def WASDmove(self, KEYPRESSES):
        '''
        updates the position of the text using the keys wasd
        :param KEYPRESSES: list
        :return: none
        '''
        if KEYPRESSES[pygame.K_d] == 1:
            self.__X += self.__SPD
        if KEYPRESSES[pygame.K_a] == 1:
            self.__X -= self.__SPD
        if KEYPRESSES[pygame.K_w] == 1:
            self.__Y -= self.__SPD
        if KEYPRESSES[pygame.K_s] == 1:
            self.__Y += self.__SPD

        self.__POS= (self.__X, self.__Y)

    def checkBoundaries(self, MAX_X, MAX_Y, MIN_X=0, MIN_Y=0):
        '''
        checking whether the object is going beyond an area
        :param MAX_X: int
        :param MAX_Y: int
        :param MIN_X: int
        :param MIN_Y: int
        :return: none
        '''
        if self.__X > MAX_X - self.getWidth():
            self.__X = MAX_X - self.getWidth()
        if self.__X < MIN_X:
            self.__X = MIN_X

        if self.__Y > MAX_Y - self.getHeight():
            self.__Y = MAX_Y - self.getHeight()
        if self.__Y < MIN_Y:
            self.__Y = MIN_Y

        self.__POS = (self.__X, self.__Y)

    def setPOS(self, X, Y):
        self.__X = X
        self.__Y = Y
        self.__POS = (self.__X, self.__Y)

    # Accessor Methods
    def getSurface(self):
        return self.__SURFACE

    def getPOS(self):
        return self.__POS

    def getWidth(self):
        return self.__WIDTH
    def getHeight(self):
        return self.__HEIGHT

if __name__ == "__main__":
    from b_hello_world import Window
    WINDOW = Window("Boxes", 800, 600, 30)
    # BOX R
    BOXR = Box(100,100)
    BOXR.setColor(Color.RED)
    BOXR.setPOS(WINDOW.getWidth()//2 - BOXR.getWidth()//2, WINDOW.getHeight()//2 - BOXR.getHeight()//2)

    # BOX B
    BOXB = Box(100,100)
    BOXB.setColor(Color.BLUE)
    BOXB.setPOS(randrange(0,WINDOW.getWidth()- BOXB.getWidth()),randrange(1,WINDOW.getHeight()-BOXB.getHeight()))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if event.type == pygame.QUIT:
                    exit()

        BOXB.bounce(WINDOW.getWidth(), WINDOW.getHeight())

        PRESSED_KEYS = pygame.key.get_pressed()
        BOXR.WASDmove(PRESSED_KEYS)
        BOXR.checkBoundaries(WINDOW.getWidth(),WINDOW.getHeight())

        WINDOW.clearScreen()
        WINDOW.getSurface().blit(BOXR.getSurface(), BOXR.getPOS())
        WINDOW.getSurface().blit(BOXB.getSurface(), BOXB.getPOS())
        WINDOW.updateFrame()
