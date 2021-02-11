import sys, pygame, random


class Bullet:

    def __init__(self):
        self.img = pygame.image.load("Game/sprites/bullet.png")
        self.playerX = 300 
        self.playerY = 600
        self.playerSpeedX = 0
        self.playerSpeedY = 0
        self.generalSpeed = 3.5
        self.moving = False
    
    
    def playerDraw(self , screen):        
        screen.blit(self.img,(self.playerX,self.playerY))

    def playerMove(self):
        self.playerX += self.playerSpeedX
        self.playerY += self.playerSpeedY

        if self.playerX <= 0:
            self.playerX = 0
        if self.playerX >= 584:
            self.playerX = 584
        if self.playerY <= 0: 
            self.playerY = 0
        if self.playerY >= 784:
            self.playerY = 784



    def playerKey(self, event):
            if event.key == pygame.K_SPACE:
                print("pew pew")
                