# c_boxes.py
'''
title: boxes
author: mike zhang
date-created: 2023-10-27
'''

import pygame
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

    # Accessor Methods
    def getSurface(self):
        return self.__SURFACE

    def getPOS(self):
        return self.__POS

if __name__ == "__main__":
    from b_hello_world import Window
    WINDOW = Window("Boxes", 800, 600, 30)
    BOX = Box(100,100)
    BOX.setColor(Color.RED)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if event.type == pygame.QUIT:
                    exit()

        WINDOW.clearScreen()
        WINDOW.getSurface().blit(BOX.getSurface(), BOX.getPOS())
        WINDOW.updateFrame()
