# box.py in d_inheritance(folder)
'''
title: box class
author: kliment lo
date-created: 2023/10/30
'''

from my_sprite import MySprite
import pygame

class Box(MySprite):

    def __init__(self, WIDTH=1, HEIGHT=1):
        MySprite.__init__(self, WIDTH, HEIGHT)
        self._SURFACE = pygame.Surface(self._DIMENSIONS, pygame.SRCALPHA, 32)
        self._SURFACE.fill(self._COLOR)

if __name__ == "__main__":
    from window import Window
    from random import randrange
    pygame.init()
    WINDOW = Window("Box", 800, 600, 30)
    #BOX = Box(100, 100)
    BOXES = []
    for i in range(200):
        SIZE = randrange(2,6)
        BOXES.append(Box(SIZE,SIZE))
        BOXES[-1].setX(randrange(WINDOW.getWidth()-SIZE))
        BOXES[-1].setY(randrange(WINDOW.getHeight()-SIZE))
        BOXES[-1].setSpeed(3)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()



        for star in BOXES:
            star.marqueeX(WINDOW.getWidth())
            WINDOW.clearScreen()

        for star in BOXES:
            WINDOW.getSurface().blit(star.getSurface(), star.getPOS())
        #WINDOW.getSurface().blit(BOX.getSurface(), BOX.getPOS())
        WINDOW.updateFrame()