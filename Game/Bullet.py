import sys, pygame, random
from Enemy import Enemy


class Bullet:

    def __init__(self, xPos, yPos):
        self.img = pygame.image.load("Game/sprites/bullets/red_bullet.png")
        self.bulletX = xPos 
        self.bulletY = yPos 
        self.bulletSpeedX = 0
        self.bulletSpeedY = 12
        self.bulletRect = self.img.get_rect()
        self.bullet_hit = False

    @property
    def getBulletRect(self):
        
        return self.bulletRect

    @property  
    def getBulletY(self):
        return self.bulletY
    
    def is_collided_with(self, img):
        return self.rect.colliderect(img.rect)

    def bulletDraw(self , screen):        
        screen.blit(self.img,(self.bulletX,self.bulletY))

    def bulletMove(self):
        self.bulletX -= self.bulletSpeedX
        self.bulletY -= self.bulletSpeedY
        self.bulletRect = self.img.get_rect(x=self.bulletX, y=self.bulletY)
    
    