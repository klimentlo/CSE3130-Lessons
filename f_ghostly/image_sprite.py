# image_sprite.py in f_ghostly
'''
title: Image Sprite
author: mike zhang
date-created: 2023-10-31
'''
import pygame
from my_sprite import MySprite


class ImageSprite(MySprite):

    def __init__(self, IMAGE_FILE_LOC):
        MySprite.__init__(self)
        self.__FILE_LOC = IMAGE_FILE_LOC
        self._SURFACE = pygame.image.load(self.__FILE_LOC).convert_alpha()
        self.__IMAGE_DIR_X = True  # True is looking to the right

    # MODIFIER METHODS
    def setScale(self, SCALE_X, SCALE_Y=0):
        """
        Changes the scale of the image, making it bigger or smaller
        :param SCALE_X: float
        :param SCALE_Y: float
        :return: None
        """
        if SCALE_Y == 0:
            SCALE_Y = SCALE_X
        self._SURFACE = pygame.transform.scale(self._SURFACE, (self.getWidth() * SCALE_X, self.getHeight() * SCALE_Y))

    def setImageDirX(self, BOOL):
        """
        sets the Image Direction X Variable. True is right, False is left
        :param BOOL: bool
        :return: None
        """
        self.__IMAGE_DIR_X = BOOL

    def WASDmove(self, PRESSED_KEYS):
        MySprite.WASDmove(self, PRESSED_KEYS)
        if PRESSED_KEYS[pygame.K_d] == 1 and not self.__IMAGE_DIR_X:
            # if d key is pressed and image is looking left
            self._SURFACE = pygame.transform.flip(self._SURFACE, True, False)
            self.__IMAGE_DIR_X = True
        if PRESSED_KEYS[pygame.K_a] == 1 and self.__IMAGE_DIR_X:
            # if a key is pressed and image is looking right
            self._SURFACE = pygame.transform.flip(self._SURFACE, True, False)
            self.__IMAGE_DIR_X = False


if __name__ == "__main__":
    from window import Window

    WINDOW = Window("Image Sprites", 800, 600, 30)
    GHOST = ImageSprite("media/ghost_sprite.png")
    GHOST.setScale(2)
    PIKACHU = ImageSprite("media/pikachu.png")
    PIKACHU.setX(WINDOW.getWidth() // 2 - PIKACHU.getWidth() // 2)
    PIKACHU.setY(WINDOW.getHeight() // 2 - PIKACHU.getHeight() // 2)
    PIKACHU.setImageDirX(False)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        KEYS_PRESSED = pygame.key.get_pressed()

        PIKACHU.WASDmove(KEYS_PRESSED)
        PIKACHU.checkBoundaries(WINDOW.getWidth(), WINDOW.getHeight())

        WINDOW.clearScreen()
        WINDOW.getSurface().blit(GHOST.getSurface(), GHOST.getPOS())
        WINDOW.getSurface().blit(PIKACHU.getSurface(), PIKACHU.getPOS())
        WINDOW.updateFrame()
