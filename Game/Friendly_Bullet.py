import sys, pygame, random
from GameObject import *
from Mediator import *

class Friendly_Bullet(GameObject):
    
    def __init__(self, screen, xPos, yPos, objectID, mediator):
        self.img = pygame.image.load("Game/sprites/bullets/red_bullet.png")
        self.bulletX = xPos 
        self.bulletY = yPos 
        self.screen = screen
        self.bulletSpeedX = 0
        self.bulletSpeedY = 12
        self.bulletRect = self.img.get_rect()
        self.bulletDamage = 10
        self.objectID = objectID
        self.mediator = mediator
    
    ## For collision ##
    
    def get_rect(self):
        return self.bulletRect
    
    ## For damaging enemy ##
    
    def getBulletDamage(self):
        return self.bulletDamage

    ## For removing the bullet ##
 
    def getBulletY(self):
        return self.bulletY

    ## Draw at specific location ##
    def bulletDraw(self):        
        self.screen.blit(self.img,(self.bulletX,self.bulletY))

    ## Update bullet pos and the rect ##
    def bulletMove(self):
        self.bulletX -= self.bulletSpeedX
        self.bulletY -= self.bulletSpeedY
        self.bulletRect = self.img.get_rect(x=self.bulletX, y=self.bulletY)

        if self.bulletY < -16:
            self.mediator.to_be_removed.append(self)
    
    def loop(self):
        self.bulletMove()

    def draw(self):
        self.bulletDraw()


    