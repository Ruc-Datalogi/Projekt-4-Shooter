import sys, pygame, random

class Enemy:

    def __init__(self, enemyXPos, enemyYPos):
        self.img = pygame.image.load("Game/sprites/enemy1.png")
        self.enemyX = enemyXPos 
        self.enemyY = enemyYPos
        self.enemySpeedX = 1.5
        self.enemySpeedY = 0
        self.enemyRect = self.img.get_rect()
        

    @property
    def getEnemyRect(self):
        self.enemyRect = pygame.Rect((self.enemyX, self.enemyY),(self.enemyX+self.img.get_width(),self.enemyY+self.img.get_height()))
        return self.enemyRect
    
    def enemyDraw(self, screen):
        screen.blit(self.img, (self.enemyX, self.enemyY))

    def enemyMove(self):
        self.enemyX += self.enemySpeedX
        if self.enemyX >= 576 or self.enemyX <= 24:
            self.enemySpeedX *= -1
            self.enemyY += 50
        self.enemyRect = self.img.get_rect()