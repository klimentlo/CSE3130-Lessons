# game_engine.py in g_asteroids (folder)

'''
title: Game engine
author: kliment lo
date-created: 2023/11/08
'''

import pygame
from player import Player
from asteroid import Asteroid
from window import Window
from box import Box
from text import Text
from color import Color
from random import randrange
pygame.init()

class Game:

    def __init__(self):
        self.__WINDOW = Window("Asteroids", 600, 600, 60)
        self.__PLAYER = Player()
        self.__PLAYER.setPOS(self.__WINDOW.getWidth()//2 - self.__PLAYER.getWidth()//2,
                             self.__WINDOW.getHeight()//2 - self.__PLAYER.getHeight()//2)
        # Title Bar
        self.__TITLE_BAR = Box(self.__WINDOW.getWidth(), self.__WINDOW.getHeight()//10)
        self.__TITLE_BAR.setColor(Color.BLACK)
        self.__TITLE_TEXT = Text("ASTEROIDS")
        self.__TITLE_TEXT.setPOS(self.__WINDOW.getWidth()//2 - self.__TITLE_TEXT.getWidth()//2,
                                 5)
        # Score
        self.__SCORE = 0
        self.__SCORE_TEXT = Text(f"SCORE: {self.__SCORE}")
        self.__SCORE_TEXT.setPOS(self.__WINDOW.getWidth() - self.__SCORE_TEXT.getWidth() - 5,
                                 5)
        # Health Text
        self.__HEALTH_TEXT = Text("HEALTH: ")
        self.__HEALTH_TEXT.setY(5)

        # Health Bar
        self.__HEALTH_BAR = Box(self.__PLAYER.getHealth(), self.__WINDOW.getHeight()//20)
        self.__HEALTH_BAR.setColor(Color.GREEN)
        self.__HEALTH_BAR.setPOS(self.__HEALTH_TEXT.getX() + self.__HEALTH_TEXT.getWidth() + 4,
                                 15)
        # Asteroids
        self.__ASTEROIDS = []
        for i in range(50):
            self.__ASTEROIDS.append(Asteroid())
            # if it ever spawns on the visible screen
            while (0 <= self.__ASTEROIDS[-1].getX() < self.__WINDOW.getWidth()) and (0 <= self.__ASTEROIDS[-1].getY() < self.__WINDOW.getHeight()):
                # spawn it somewhere outside the the screen
                self.__ASTEROIDS[-1].setPOS(randrange(0-self.__ASTEROIDS[-1].getWidth()-300, self.__WINDOW.getWidth() + 300),
                                            randrange(0-self.__ASTEROIDS[-1].getHeight()-300, self.__WINDOW.getHeight() + 300))

            self.__ASTEROIDS[-1].setSpeed(1)
            self.__ASTEROIDS[-1].setAngleRatios(self.__WINDOW.getWidth()//2, self.__WINDOW.getHeight()//2)
            self.__GAME_OVER = False
            self.__GAME_OVER_TEXT = Text("Game Over")
            self.__GAME_OVER_TEXT.setPOS(self.__WINDOW.getWidth()//2 - self.__GAME_OVER_TEXT.getWidth()//2, self.__WINDOW.getHeight()//2 - self.__GAME_OVER_TEXT.getHeight()//2)






    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            KEYS_PRESSED = pygame.key.get_pressed()

            # -- Processing
            self.__PLAYER.ADrotate(KEYS_PRESSED)
            self.__PLAYER.fireLazer(KEYS_PRESSED)
            self.__PLAYER.setSpeed(10)
            self.__PLAYER.moveLazers()
            self.__PLAYER.updateLazerCooldown(self.__WINDOW.getFPS())
            self.__PLAYER.resetLazers(self.__WINDOW.getWidth(), self.__WINDOW.getHeight(), 0, self.__WINDOW.getHeight()//10)

            for asteroid in self.__ASTEROIDS:
                asteroid.moveTowardsCenter(self.__WINDOW.getWidth()//2, self.__WINDOW.getHeight()//2)
                asteroid.autoRotate()
            self.__lazerAsteroidCollision()
            self.__asteroidPlayerCollisions()


            self.__updateWindowFrame()





    def __lazerAsteroidCollision(self):
        for h in range(len(self.__ASTEROIDS)):
            for i in range(self.__PLAYER.getLazerCount()):
                if self.__ASTEROIDS[h].isCollision(self.__PLAYER.getLazerSurface(i).get_width(), self.__PLAYER.getLazerSurface(i).get_height(), self.__PLAYER.getLazerPOS(i)):
                    self.__ASTEROIDS[h] = Asteroid()
                    # --- MOVE ASTEROID
                    while (0 <= self.__ASTEROIDS[h].getX() < self.__WINDOW.getWidth()) and (
                            0 <= self.__ASTEROIDS[h].getY() < self.__WINDOW.getHeight()):
                        # spawn it somewhere outside the the screen
                        self.__ASTEROIDS[h].setPOS(
                            randrange(0 - self.__ASTEROIDS[h].getWidth() - 300, self.__WINDOW.getWidth() + 300),
                            randrange(0 - self.__ASTEROIDS[h].getHeight() - 300, self.__WINDOW.getHeight() + 300))

                    self.__ASTEROIDS[h].setSpeed(2)
                    self.__ASTEROIDS[h].setAngleRatios(self.__WINDOW.getWidth() // 2, self.__WINDOW.getHeight() // 2)
                    # --- Updating the Score
                    self.__SCORE += 10
                    self.__SCORE_TEXT.setText(f"Score: {self.__SCORE}")
                    self.__SCORE_TEXT.setPOS(self.__WINDOW.getWidth() - self.__SCORE_TEXT.getWidth() - 5, 5)

    def __asteroidPlayerCollisions(self):
        for i in range(len(self.__ASTEROIDS)):
            if self.__ASTEROIDS[i].isCollision(self.__PLAYER.getSurface().get_width(),self.__PLAYER.getSurface().get_height(), self.__PLAYER.getPOS()):
                # --- MOVE ASTEROID
                self.__ASTEROIDS[i] = Asteroid()
                while (0 <= self.__ASTEROIDS[i].getX() < self.__WINDOW.getWidth()) and (
                        0 <= self.__ASTEROIDS[i].getY() < self.__WINDOW.getHeight()):
                    # spawn it somewhere outside the the screen
                    self.__ASTEROIDS[i].setPOS(
                        randrange(0 - self.__ASTEROIDS[i].getWidth() - 300, self.__WINDOW.getWidth() + 300),
                        randrange(0 - self.__ASTEROIDS[i].getHeight() - 300, self.__WINDOW.getHeight() + 300))

                self.__ASTEROIDS[i].setSpeed(2)
                self.__ASTEROIDS[i].setAngleRatios(self.__WINDOW.getWidth() // 2, self.__WINDOW.getHeight() // 2)
                # --- UPDATE PLAYER HEALTH
                self.__PLAYER.takeDamage(20)
                self.__HEALTH_BAR = Box(self.__PLAYER.getHealth(), self.__WINDOW.getHeight()//20)
                self.__HEALTH_BAR.setColor(Color.GREEN)
                self.__HEALTH_BAR.setPOS(self.__HEALTH_TEXT.getX() + self.__HEALTH_TEXT.getWidth() + 4, self.__HEALTH_TEXT.getY() + self.__HEALTH_TEXT.getHeight()//2 -
                                         self.__HEALTH_BAR.getHeight()//2)
                if self.__PLAYER.getHealth() > 50:
                    self.__HEALTH_BAR.setColor(Color.GREEN)
                if self.__PLAYER.getHealth() > 20:
                    self.__HEALTH_BAR.setColor(Color.ORANGE)
                else:
                    self.__HEALTH_BAR.setColor(Color.RED)

                # --- CHECK GAME OVER
                if self.__PLAYER.getHealth() <= 0:
                    self.__GAME_OVER = True




    def __updateWindowFrame(self):
        # The order of blitting objects will affect which comes on top
        self.__WINDOW.clearScreen()
        # Asteroid Sprites
        if not self.__GAME_OVER:
            for asteroid in self.__ASTEROIDS:
                self.__WINDOW.getSurface().blit(asteroid.getSurface(), asteroid.getPOS())

        # --- Lay out
        self.__WINDOW.getSurface().blit(self.__TITLE_TEXT.getSurface(), self.__TITLE_TEXT.getPOS())
        self.__WINDOW.getSurface().blit(self.__TITLE_BAR.getSurface(), self.__TITLE_BAR.getPOS())
        self.__WINDOW.getSurface().blit(self.__HEALTH_TEXT.getSurface(), self.__HEALTH_TEXT.getPOS())
        self.__WINDOW.getSurface().blit(self.__HEALTH_BAR.getSurface(), self.__HEALTH_BAR.getPOS())
        self.__WINDOW.getSurface().blit(self.__SCORE_TEXT.getSurface(), self.__SCORE_TEXT.getPOS())


        # --- Sprites
        if not self.__GAME_OVER:
            self.__WINDOW.getSurface().blit(self.__PLAYER.getSurface(), self.__PLAYER.getPOS())
            for i in range(self.__PLAYER.getLazerCount()):
                self.__WINDOW.getSurface().blit(self.__PLAYER.getLazerSurface(i), self.__PLAYER.getLazerPOS(i))

        if self.__GAME_OVER:
            self.__WINDOW.getSurface().blit(self.__GAME_OVER_TEXT.getSurface(), self.__GAME_OVER_TEXT.getPOS())

        self.__WINDOW.updateFrame()

if __name__ == "__main__":
    GAME = Game()
    GAME.run()
