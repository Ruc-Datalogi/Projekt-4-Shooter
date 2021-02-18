import sys, pygame, random

class Enemy:

    def __init__(self, enemyXPos, enemyYPos, enemyID):
        self.img = pygame.image.load("Game/sprites/enemy1.png")
        if enemyID == 0: 
            self.img = pygame.image.load("Game/sprites/enemy1.png")
        if enemyID == 1:
            self.img = pygame.image.load("Game/sprites/enemy2.png")
        if enemyID == 2:
            self.img = pygame.image.load("Game/sprites/enemy3.png")
             
        self.enemyX = enemyXPos 
        self.enemyY = enemyYPos
        self.enemySpeedX = 1.5
        self.enemySpeedY = 0
        self.enemyHealth = 1 
        self.enemyRect = self.img.get_rect()
    
        

    @property
    def getEnemyRect(self):
        return self.enemyRect
    

    ## Damage the enemy
    def setHealth(self, x):
        self.enemyHealth += x

    @property
    def getEnemyHealth(self):
        return self.enemyHealth

    def enemyDraw(self, screen):
        screen.blit(self.img, (self.enemyX, self.enemyY))

    def enemyMove(self):
        self.enemyX += self.enemySpeedX
        if self.enemyX >= 300 or self.enemyX <= 12:
            self.enemySpeedX *= -1
            self.enemyY += 50
        self.enemyRect = self.img.get_rect(x=self.enemyX, y=self.enemyY)