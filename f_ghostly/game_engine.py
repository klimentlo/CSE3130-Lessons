# game_engine.py in f_ghostly

"""
title: Ghostly
author: Mike Zhang
date-created: 2023-10-31
"""

import pygame
from window import Window
from text import Text
from image_sprite import ImageSprite
from random import randrange

pygame.init()

class Game:

    def __init__(self):
        self.__WINDOW = Window("Ghostly", 800, 600, 30)
        self.__PLAYER = ImageSprite("media/pikachu.png")
        self.__PLAYER.setScale(0.2)
        self.__PLAYER.setSpeed(20)
        self.__PLAYER.setPOS(self.__WINDOW.getWidth()//2 - self.__PLAYER.getWidth()//2, self.__WINDOW.getHeight()//2 - self.__PLAYER.getHeight()//2)
        self.__PLAYER.setImageDirX(False)
        self.__ENEMIES = []
        self.__ENEMIES.append(ImageSprite("media/ghost_sprite.png"))
        self.__ENEMIES[-1].setScale(2)
        self.__ENEMIES[-1].setPOS(randrange(self.__WINDOW.getWidth() - self.__ENEMIES[-1].getWidth()), randrange(self.__WINDOW.getHeight() - self.__ENEMIES[-1].getHeight()))
        while self.__PLAYER.isCollision(self.__ENEMIES[-1].getWidth(), self.__ENEMIES[-1].getHeight(), self.__ENEMIES[-1].getPOS()):
            self.__ENEMIES[-1].setPOS(randrange(self.__WINDOW.getWidth() - self.__ENEMIES[-1].getWidth()),
                                      randrange(self.__WINDOW.getHeight() - self.__ENEMIES[-1].getHeight()))
        self.__SCORE = 0
        self.__SCORE_TEXT = Text(f"SCORE: {self.__SCORE}")
        self.__SCORE_TEXT.setPOS(self.__WINDOW.getWidth() - self.__SCORE_TEXT.getWidth() - 10, 15)
        self.__LIVES = 3
        self.__LIVES_TEXT = Text(f"LIVES: {self.__LIVES}")
        self.__LIVES_TEXT.setX(10)
        self.__GAME_OVER = False
        self.__GAME_OVER_TEXT = Text("Game Over!")
        self.__GAME_OVER_TEXT.setPOS(self.__WINDOW.getWidth()//2 - self.__GAME_OVER_TEXT.getWidth()//2, self.__WINDOW.getHeight()//2 - self.__GAME_OVER_TEXT.getHeight()//2)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            PRESSED_KEYS = pygame.key.get_pressed()

            if not self.__GAME_OVER:
                for enemy in self.__ENEMIES:
                    enemy.bounceX(self.__WINDOW.getWidth())
                    enemy.bounceY(self.__WINDOW.getHeight())

                self.__PLAYER.WASDmove(PRESSED_KEYS)
                self.__PLAYER.checkBoundaries(self.__WINDOW.getWidth(), self.__WINDOW.getHeight())

                for i in range(len(self.__ENEMIES)):
                    if self.__PLAYER.isCollision(self.__ENEMIES[i].getWidth(), self.__ENEMIES[i].getHeight(), self.__ENEMIES[i].getPOS()):
                        self.__LIVES -= 1
                        self.__LIVES_TEXT.setText(f"LIVES: {self.__LIVES}")
                        self.__PLAYER.setPOS(self.__WINDOW.getWidth()//2 - self.__PLAYER.getWidth()//2, self.__WINDOW.getHeight()//2 - self.__PLAYER.getHeight()//2)
                        for enemy in self.__ENEMIES:
                            enemy.setPOS(randrange(self.__WINDOW.getWidth()-enemy.getWidth()), randrange(self.__WINDOW.getHeight()-enemy.getHeight()))
                            while self.__PLAYER.isCollision(enemy.getWidth(), enemy.getHeight(), enemy.getPOS()):
                                enemy.setPOS(randrange(self.__WINDOW.getWidth() - enemy.getWidth()),
                                             randrange(self.__WINDOW.getHeight() - enemy.getHeight()))

                self.__SCORE += 1
                self.__SCORE_TEXT.setText(f"SCORE: {self.__SCORE}")
                self.__SCORE_TEXT.setX(self.__WINDOW.getWidth() - self.__SCORE_TEXT.getWidth() - 10)

                if self.__SCORE % 100 == 0:
                    self.__ENEMIES.append(ImageSprite("media/ghost_sprite.png"))
                    self.__ENEMIES[-1].setScale(2)
                    self.__ENEMIES[-1].setPOS(randrange(self.__WINDOW.getWidth() - self.__ENEMIES[-1].getWidth()),
                                              randrange(self.__WINDOW.getHeight() - self.__ENEMIES[-1].getHeight()))
                    while self.__PLAYER.isCollision(self.__ENEMIES[-1].getWidth(), self.__ENEMIES[-1].getHeight(),
                                                    self.__ENEMIES[-1].getPOS()):
                        self.__ENEMIES[-1].setPOS(randrange(self.__WINDOW.getWidth() - self.__ENEMIES[-1].getWidth()),
                                                  randrange(self.__WINDOW.getHeight() - self.__ENEMIES[-1].getHeight()))

                if self.__LIVES < 1:
                    self.__GAME_OVER = True

            self.__WINDOW.clearScreen()
            self.__WINDOW.getSurface().blit(self.__SCORE_TEXT.getSurface(), self.__SCORE_TEXT.getPOS())
            self.__WINDOW.getSurface().blit(self.__LIVES_TEXT.getSurface(), self.__LIVES_TEXT.getPOS())
            if not self.__GAME_OVER:
                for i in range(len(self.__ENEMIES)):
                    self.__WINDOW.getSurface().blit(self.__ENEMIES[i].getSurface(), self.__ENEMIES[i].getPOS())
                self.__WINDOW.getSurface().blit(self.__PLAYER.getSurface(), self.__PLAYER.getPOS())
            else:
                self.__WINDOW.getSurface().blit(self.__GAME_OVER_TEXT.getSurface(), self.__GAME_OVER_TEXT.getPOS())
            self.__WINDOW.updateFrame()

if __name__ == "__main__":
    GAME = Game()
    GAME.run()