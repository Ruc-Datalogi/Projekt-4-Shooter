import sys, pygame, random
from Bullet import Bullet
from Enemy import Enemy

class Player:

    ## Constructor for player ## 
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
        self.timer = 0


    
    ## Draw player and bullets at given pos ##
    def playerDraw(self , screen):        
        screen.blit(self.img,(self.playerX,self.playerY))
        

        for i in range(len(self.bulletlist)):
            self.bulletlist[i].bulletMove()
            self.bulletlist[i].bulletDraw(screen)
        
    ## check bullet collision and damage enemy
    def bulletCollision(self, enemy):
        for i in range(len(self.bulletlist)):
            if self.bulletlist[i].getBulletRect.colliderect(enemy.getEnemyRect):
                print(enemy.getEnemyRect)
                enemy.setHealth(-10)
                self.bulletlist.pop(i)
                break

        ## remove bullets
        for i in range(len(self.bulletlist)):
            if self.bulletlist[i].getBulletY < -100:
                self.bulletlist.pop(i)
                break

    ## Character move and game boundaries ##
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

    ## Get keypressed and use it for movement ##
    def update(self):
        self.playerSpeedX = 0
        self.playerSpeedY = 0
        keystate = pygame.key.get_pressed()

        if keystate[pygame.K_LEFT]:
            self.playerSpeedX -= self.generalSpeed

        if keystate[pygame.K_RIGHT]:
            self.playerSpeedX = self.generalSpeed

        if keystate[pygame.K_UP]:
            self.playerSpeedY -= self.generalSpeed

        if keystate[pygame.K_DOWN]:
            self.playerSpeedY = self.generalSpeed
            
        if self.timer > 10 and keystate[pygame.K_SPACE]:
            self.timer = 0
            self.bulletlist.append(Bullet(self.playerX + 2, self.playerY - 10))
            self.bulletlist.append(Bullet(self.playerX + 10, self.playerY - 10))
            self.bulletlist.append(Bullet(self.playerX + -6, self.playerY - 10))

        if keystate[pygame.K_ESCAPE]:
            sys.exit()

        self.timer +=1

                