# lazer.py in g_asteroids (folder)


import pygame
from box import Box
from color import Color
from math import radians, cos, sin

class Lazer(Box):

    def __init__(self, X=1, Y=1):
        Box.__init__(self, 10, 10)
        self.setColor(Color.RED)
        self.setPOS(X, Y)
        self.__ANGLE = 0
        self.__FIRED = False

    # MODIFIER METHODS
    def setFired(self, BOOL):
        '''
        determines if the lazer is currently fired
        :param BOOL: bool
        :return: none
        '''
        self.__FIRED = BOOL

    def setAngle(self, ANGLE):
        self.__ANGLE = ANGLE



    # ACCESSOR METHODS

    def getFired(self):
        return self.__FIRED

    def move(self):
        if self.__FIRED:
            self.setX(self.getX() + self._SPD * cos(radians(self.__ANGLE)))
            self.setY(self.getY() + self._SPD * sin(radians(self.__ANGLE)))

if __name__ == "__main__":
    from window import Window
    pygame.init()

    WINDOW = Window("Lazer test", 800, 600, 60)
    LAZER = Lazer(295,295)
    LAZER.setAngle(0)
    LAZER.setFire(True)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        LAZER.move()
        WINDOW.clearScreen()
        WINDOW.getSurface().blit(LAZER.getSurface(),LAZER.getPOS())
        WINDOW.updateFrame()