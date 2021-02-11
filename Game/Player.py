import sys, pygame, random
from Bullet import Bullet

class Player:

    def __init__(self, screen):
        self.img = pygame.image.load("Game/sprites/playerLV1.png")
        self.playerX = 300 
        self.playerY = 600
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
            print(len(self.bulletlist))
            self.bulletlist[i].bulletMove()
            self.bulletlist[i].bulletDraw(screen)

    def bulletCollision(self, enemy):
        for i in range(len(self.bulletlist)):
            if self.bulletlist[i].getBulletRect.colliderect(enemy.getEnemyRect):
                print("JA TAK")

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
        if event.type == pygame.KEYDOWN:
            self.moving = True
            print('Key down')
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
                self.bulletlist.append(Bullet(self.playerX, self.playerY))
                print("pew pew")
        
        if event.type == pygame.KEYUP:
            print('Key up')
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT: 
                self.playerSpeedX = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                self.playerSpeedY = 0
                