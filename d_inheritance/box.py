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
        MySprite.__init__(self, WIDTH,HEIGHT)
        self._Surface = pygame.Surface(self._DIMENSIONS, pygame.SRCALPHA, 32)

if __name__ == "__main__":
    from window import Window
    pygame.init()
    WINDOW = Window("Box", 800,600,30)
    BOX = Box(100, 100)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
    WINDOW.clearScreen()
    WINDOW.getSurface().blit(BOX.getSurface(), BOX.getPOS())
    WINDOW.updateFrame()