# collision_test.py in e_collisions(folder)
'''
title: collision testing
author: kliment lo
date-created: 2023/11/1
'''


if __name__ == "__main__":
    import pygame
    from window import Window
    from box import Box
    from color import Color
    from random import randrange

    WINDOW = Window("collision test", 800, 600, 30)
    RED_BOX = Box(200, 200)
    RED_BOX.setColor(Color.RED)
    RED_BOX.setX(WINDOW.getWidth()//2 - RED_BOX.getWidth()//2)
    RED_BOX.setY(WINDOW.getHeight() // 2 - RED_BOX.getHeight()//2)

    BLUE_BOX = Box(100, 100)
    BLUE_BOX.setColor(Color.BLUE)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        PRESSED_KEYS = pygame.key.get_pressed()

        RED_BOX.bounceX(WINDOW.getWidth())
        RED_BOX.bounceY(WINDOW.getHeight())
        BLUE_BOX.WASDmove(PRESSED_KEYS)

        if RED_BOX.isCollision(BLUE_BOX.getWidth(),BLUE_BOX.getHeight(), BLUE_BOX.getPOS()):
            print("Hit! ")
            NEW_WIDTH = RED_BOX.getWidth()*3 //4
            RED_BOX = Box(NEW_WIDTH, NEW_WIDTH)
            RED_BOX.setColor(Color.RED)

            BLUE_BOX.setSpeed(7)

            BLUE_BOX.setPOS(randrange(WINDOW.getWidth() - BLUE_BOX.getWidth()), randrange(WINDOW.getHeight() - BLUE_BOX.getHeight()))

            RED_BOX.setPOS(randrange(WINDOW.getWidth() - RED_BOX.getWidth()), randrange(WINDOW.getHeight() - RED_BOX.getHeight()))

            while RED_BOX.isCollision(BLUE_BOX.getWidth(), BLUE_BOX.getHeight(), BLUE_BOX.getPOS()):
                RED_BOX.setPOS(randrange(WINDOW.getWidth() - RED_BOX.getWidth(), randrange(WINDOW.getHeight() - RED_BOX.getHeight())))



        WINDOW.clearScreen()
        WINDOW.getSurface().blit(RED_BOX.getSurface(), RED_BOX.getPOS())
        WINDOW.getSurface().blit(BLUE_BOX.getSurface(), BLUE_BOX.getPOS())
        WINDOW.updateFrame()