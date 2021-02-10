import sys, pygame, random

class Enemy:

    def __init__(self):
        self.img = pygame.image.load("Game/sprites/enemy1.png")
        self.enemyX = 100 
        self.enemyY = 100
        self.enemySpeedX = 1.5
        self.enemySpeedY = 0
    
    def enemyDraw(self, screen):
        screen.blit(self.img, (self.enemyX, self.enemyY))

    def enemyMove(self):
        self.enemyX += self.enemySpeedX
        if self.enemyX >= 576 or self.enemyX <= 24:
            self.enemySpeedX *= -1
            self.enemyY += 50
