# asteroid.py in g_asteroids(folder)

'''
title: asteroid class
author: kliment lo
date-created: 2023/11/07
'''


from box import Box
from my_sprite import MySprite
import pygame
import random
import math

class Asteroid(MySprite):

    def __init__(self):
        MySprite.__init__(self)
        SIZE = random.choice([40, 50, 60, 70, 80, 90, 100])
        self.__ASTEROID_SPRITE = Box(SIZE, SIZE)
        self._SURFACE = self.__ASTEROID_SPRITE.getSurface()
        self.__SPIN_DIR = random.choice([-1,1])
        self.__ANGLE = 0
        self.__X_RATIO = 0.0
        self.__Y_RATIO = 0.0

    # MODIFIER METHODS
    def autoRotate(self):
        CENTER = self.getCenter()
        self.__ANGLE += self._SPD * self.__SPIN_DIR
        self._SURFACE = pygame.transform.rotate(self.__ASTEROID_SPRITE.getSurface(), self.__ANGLE)
        self.setX(CENTER[0] - self.getWidth()//2)
        self.setY(CENTER[1] - self.getHeight()//2)

    def setAngleRatios(self, X, Y):
        '''
        updates the x and y ratios for the position at (x,y)
        :param X: float
        :param Y: float
        :return: none
        '''
        X_DELTA = abs(self.getX() - X)
        Y_DELTA = abs(self.getY() - Y)
        self.__X_RATIO = math.cos(math.atan(Y_DELTA/X_DELTA))
        self.__Y_RATIO = math.sin(math.atan(Y_DELTA/X_DELTA))

    def moveTowardsCenter(self, X, Y):
        if self.getX() < X - self.getWidth()//2:
            self.setX(self.getX() + self._SPD*self.__X_RATIO)
        else:
            self.setX(self.getX()-self._SPD * self.__X_RATIO)
        if self.getY() < Y - self.getHeight()//2:
            self.setY(self.getY() + self._SPD * self.__Y_RATIO)
        else:
            self.setY(self.getY() - self._SPD * self.__Y_RATIO)
    # ACCESSOR METHODS

if __name__ == "__main__":
    from window import Window
    pygame.init()
    WINDOW = Window("Asteroid Test", 800, 600, 30)
    ASTEROIDS = [Asteroid(), Asteroid()]


    for asteroid in ASTEROIDS:
        asteroid.setPOS(random.randrange(WINDOW.getWidth()-asteroid.getWidth()), random.randrange(WINDOW.getHeight() - asteroid.getHeight()))
        asteroid.setAngleRatios(WINDOW.getWidth()//2, WINDOW.getHeight()//2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        for asteroid in ASTEROIDS:
            asteroid.autoRotate()
            asteroid.moveTowardsCenter(WINDOW.getWidth()//2, WINDOW.getHeight()//2)

        WINDOW.clearScreen()
        for asteroid in ASTEROIDS:
            WINDOW.getSurface().blit(asteroid.getSurface(), asteroid.getPOS())
        WINDOW.updateFrame()