# my_sprite.py in f_ghostly

'''
title: abstract sprite class
author: mike zhang
date-created: 2023-10-30
'''
import pygame

class MySprite:
    """
    abstract sprite class to build other sprites
    """

    def __init__(self, WIDTH=1, HEIGHT=1, X=0, Y=0, SPEED=5, COLOR=(255, 255, 255)):
        self.__WIDTH = WIDTH
        self.__HEIGHT = HEIGHT
        self._DIMENSIONS = (self.__WIDTH, self.__HEIGHT)
        self.__X = X
        self.__Y = Y
        self.__POS = (self.__X, self.__Y)
        self._COLOR = COLOR # White
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
        self.setY(Y)

    def setSpeed(self, SPEED):
        self.__SPD = SPEED

    def marqueeX(self, MAX_X, MIN_X=0):
        self.__X += self.__SPD

        if self.__X > MAX_X:
            self.__X = MIN_X - self.getWidth()

        self.__POS = (self.__X, self.__Y)

    def bounceX(self, MAX_X, MIN_X=0):
        self.__X += self.__DIR_X * self.__SPD

        if self.__X > MAX_X - self.getWidth():
            self.__DIR_X = -1
        if self.__X < MIN_X:
            self.__DIR_X = 1

        self.__POS = (self.__X, self.__Y)

    def bounceY(self, MAX_Y, MIN_Y=0):
        self.__Y += self.__DIR_Y * self.__SPD

        if self.__Y > MAX_Y - self.getHeight():
            self.__DIR_Y = -1
        if self.__Y < MIN_Y:
            self.__DIR_Y = 1

        self.__POS = (self.__X, self.__Y)

    def WASDmove(self, PRESSED_KEYS):

        if PRESSED_KEYS[pygame.K_d] == 1:
            self.__X += self.__SPD
        if PRESSED_KEYS[pygame.K_a] == 1:
            self.__X -= self.__SPD
        if PRESSED_KEYS[pygame.K_w] == 1:
            self.__Y -= self.__SPD
        if PRESSED_KEYS[pygame.K_s] == 1:
            self.__Y += self.__SPD

        self.__POS = (self.__X, self.__Y)

    def checkBoundaries(self, MAX_X, MAX_Y, MIN_X=0, MIN_Y=0):

        if self.__X > MAX_X - self.getWidth():
            self.__X = MAX_X - self.getWidth()
        if self.__X < MIN_X:
            self.__X = MIN_X
        if self.__Y > MAX_Y - self.getHeight():
            self.__Y = MAX_Y - self.getHeight()
        if self.__Y < MIN_Y:
            self.__Y = MIN_Y

        self.__POS = (self.__X, self.__Y)


    # ACCESSOR METHODS
    def getPOS(self):
        return self.__POS

    def getWidth(self):
        return self._SURFACE.get_width()

    def getHeight(self):
        return self._SURFACE.get_height()

    def getSurface(self):
        return self._SURFACE

    def isCollision(self, WIDTH, HEIGHT, POS):
        """
        use the Width, Height, and Position of an external sprite to test if it is colliding
        with the given sprite.
        :param WIDTH: int
        :param HEIGHT: int
        :param POS: tuple
        """

        if POS[0] >= self.__X - WIDTH and POS[0] <= self.__X + self.getWidth() and \
            POS[1] >= self.__Y - HEIGHT and POS[1] <= self.__Y + self.getHeight():
            return True
        else:
            return False
