import sys, pygame, random


class Bullet:

    def __init__(self, xPos, yPos):
        self.img = pygame.image.load("Game/sprites/bullet.png")
        self.bulletX = xPos -8.5
        self.bulletY = yPos -30
        self.bulletSpeedX = 0
        self.bulletSpeedY = 10
        #self.bulletState = "ready"
    
    
    def bulletDraw(self , screen):        
        screen.blit(self.img,(self.bulletX,self.bulletY))

    def bulletMove(self):
        self.bulletX -= self.bulletSpeedX
        self.bulletY -= self.bulletSpeedY


    # Bullet movement
    # if statements for skudene
    # Når bulletY er mindre end eller lig med 0, så skal bulletY reset, så der kan skydes igen.
    

    
                