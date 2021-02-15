import sys, pygame, random


class Bullet:

    def __init__(self, xPos, yPos):
        self.img = pygame.image.load("Game/sprites/bullet.png")
        self.bulletX = xPos -8.5
        self.bulletY = yPos -30
        self.bulletSpeedX = 0
        self.bulletSpeedY = 10
        self.bulletRect = self.img.get_rect()

    @property
    def getBulletRect(self):
        self.bulletRect = pygame.Rect((self.bulletX, self.bulletY),(self.bulletX+self.img.get_width(),self.bulletY+self.img.get_height()))
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
    
    