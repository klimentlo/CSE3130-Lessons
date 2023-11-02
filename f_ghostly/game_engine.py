# game_engine.py in f_ghostly (folder)
# pygame.surface.get_masks, pygame.surface.set_masks

import pygame
from window import Window
from text import Text
from image_sprite import ImageSprite
from random import randrange

pygame.init()

if __name__ == "__main__":
    from window import Window

    WINDOW = Window("Image Sprites", 800, 600, 30)
    GHOST = ImageSprite("media/ghost_sprite.png")
    GHOST.setScale(1)

    PIKACHU = ImageSprite("media/pikachu.png")
    PIKACHU.setX(WINDOW.getWidth() // 2 - PIKACHU.getWidth() // 2)
    PIKACHU.setY(WINDOW.getHeight() // 2 - PIKACHU.getHeight() // 2)
    PIKACHU.setScale(1/4)
    PIKACHU.setImageDirX(False)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        # Sprite Movements
        KEYS_PRESSED = pygame.key.get_pressed()
        PIKACHU.WASDmove(KEYS_PRESSED)
        PIKACHU.checkBoundaries(WINDOW.getWidth(), WINDOW.getHeight())

        GHOST.bounceX(WINDOW.getWidth())
        GHOST.bounceY(WINDOW.getHeight())

        # Check Collision
        if PIKACHU.isCollision(GHOST.getWidth(), GHOST.getHeight(), GHOST.getPOS()):
            GHOST.setPOS(randrange(WINDOW.getWidth() - GHOST.getWidth()), randrange(WINDOW.getHeight() - GHOST.getHeight()))

        WINDOW.clearScreen()
        WINDOW.getSurface().blit(GHOST.getSurface(), GHOST.getPOS())
        WINDOW.getSurface().blit(PIKACHU.getSurface(), PIKACHU.getPOS())
        WINDOW.updateFrame()