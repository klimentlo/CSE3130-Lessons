# player.py in g_asteroids (folder)

'''
title: player class
author: kliment lo
date-created: 2023/11/06
'''

import pygame
from my_sprite import MySprite
from box import Box
from lazer import Lazer

class Player(MySprite):

    def __init__(self):
        MySprite.__init__(self)
        self.__PLAYER_SPRITE = Box(300,50)
        self._SURFACE = self.__PLAYER_SPRITE.getSurface()
        self.__HEALTH = 100
        self.__ANGLE = 0
        self.__LAZERS = [Lazer()]

    # MODIFIER METHODS
    def ADrotate(self, KEY_PRESSED):
        if KEY_PRESSED[pygame.K_a]:
            self.__ANGLE += self._SPD # will eventually make it rotate anti-clockwise
        if KEY_PRESSED[pygame.K_d]:
            self.__ANGLE -= self._SPD # will eventually make it rotate clockwise
        CENTER = self.getCenter()
        self._SURFACE = pygame.transform.rotate(self.__PLAYER_SPRITE.getSurface(), self.__ANGLE)
        self.setX(CENTER[0] - self.getWidth()//2)
        self.setY(CENTER[1] - self.getHeight()//2)


    # ACCESSOR METHODS


if __name__ == "__main__":
    from window import Window
    pygame.init()
    WINDOW = Window("Player test", 800, 600, 30)
    PLAYER = Player()
    PLAYER.setPOS(WINDOW.getWidth()//2 - PLAYER.getWidth()//2, WINDOW.getHeight()//2 - PLAYER.getHeight()//2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        PRESSED_KEYS = pygame.key.get_pressed()

        PLAYER.ADrotate(PRESSED_KEYS)
        WINDOW.clearScreen()
        WINDOW.getSurface().blit(PLAYER.getSurface(), PLAYER.getPOS())
        WINDOW.updateFrame()

