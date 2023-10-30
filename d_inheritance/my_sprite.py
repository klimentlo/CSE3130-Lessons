# my_sprite.py in d_inheritance(folder)
'''
title: abstract sprite class
author: kliment lo
date-created: 2023/10/30
'''
import pygame

class MySprite:
    '''
    abstract sprite class to build other sprites. they should be generic where both objects should share in attributes
    '''
    # ATTRIBUTES
    def __init__(self, WIDTH=1, HEIGHT=1, X=0, Y=0, SPEED=5, COLOR=(255,255,255)):
        self.__WIDTH = WIDTH
        self.__HEIGHT = HEIGHT
        self._DIMENSIONS = (self.__WIDTH, self.__HEIGHT)
        self._COLOR = COLOR  # White
        self.__X = X
        self.__Y = Y
        self.__POS = (self.__X, self.__Y)
        self.__SPD = SPEED
        self._SURFACE = pygame.Surface
        self.__DIR_X = 1
        self.__DIR_Y = 1


    # MODIFIER
    def setX(self, X):
        self.__X = X
        self.__POS = (self.__X, self.__Y)

    def setY(self, Y):
        self.__Y = Y
        self.__POS = (self.__X, self.__Y)

    def setPOS(self, X, Y):
        self.setX(X)
        self._setY(Y)



    # ACCESSOR
    def getPOS(self):
        return self.__POS

    def getWidth(self):
        return self._SURFACE.get_width()

    def getHeight(self):
        return self._SURFACE.get_height()

    def getSurface(self):
        return self._SURFACE

