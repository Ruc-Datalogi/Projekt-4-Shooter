import sys, pygame, random
from Bullet import Bullet
from Enemy import Enemy

class Player:

    def __init__(self, screen):
        self.img = pygame.image.load("Game/sprites/playerLV1.png")
        self.playerX = 100 
        self.playerY = 100

        self.playerSpeedX = 0
        self.playerSpeedY = 0
        self.generalSpeed = 3.5
        self.moving = False
        self.screen = screen
        self.bulletlist = []
        self.increment = 0

    
    
    def playerDraw(self , screen):        
        screen.blit(self.img,(self.playerX,self.playerY))
        for i in range(len(self.bulletlist)):
            if self.bulletlist[i].getBulletY < -100:
                self.bulletlist.pop(i)
                break

        for i in range(len(self.bulletlist)):
            self.bulletlist[i].bulletMove()
            self.bulletlist[i].bulletDraw(screen)
        

    def bulletCollision(self, enemy):
        for i in range(len(self.bulletlist)):
            if self.bulletlist[i].getBulletRect.colliderect(enemy.getEnemyRect):
                print(enemy.getEnemyRect)

    def playerMove(self):
        self.playerX += self.playerSpeedX
        self.playerY += self.playerSpeedY

        if self.playerX <= 0:
            self.playerX = 0
        if self.playerX >= 400 - 14:
            self.playerX = 400 - 14
        if self.playerY <= 0: 
            self.playerY = 0
        if self.playerY >= 540:
            self.playerY = 540



    def playerKey(self, event):
        if event.type == pygame.KEYDOWN:
            self.moving = True
            if event.key == pygame.K_LEFT: 
                self.playerSpeedX = -self.generalSpeed
            if event.key == pygame.K_RIGHT: 
                self.playerSpeedX = self.generalSpeed
            if event.key == pygame.K_UP:
                self.playerSpeedY = -self.generalSpeed
            if event.key == pygame.K_DOWN:
                self.playerSpeedY = self.generalSpeed
            if event.key == pygame.K_ESCAPE:
                sys.exit()
            if event.key == pygame.K_SPACE:
                self.bulletlist.append(Bullet(self.playerX + 2, self.playerY - 10))
                self.bulletlist.append(Bullet(self.playerX + 10, self.playerY - 10))
                self.bulletlist.append(Bullet(self.playerX + -6, self.playerY - 10))

                print("pew pew")
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT: 
                self.playerSpeedX = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                self.playerSpeedY = 0
                