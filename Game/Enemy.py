import sys, pygame, random
from EnemyBullet import EnemyBullet
from GameObject import *
from Mediator import *


class Enemy(GameObject):

    ## Choose enemy sprite ##
    def __init__(self, enemyXPos, enemyYPos, enemyID, objectID, mediator, screen):
        self.img = pygame.image.load("Game/sprites/enemy1.png")
        if enemyID == 0: 
            self.img = pygame.image.load("Game/sprites/enemy1.png")
        if enemyID == 1:
            self.img = pygame.image.load("Game/sprites/enemy2.png")
        if enemyID == 2:
            self.img = pygame.image.load("Game/sprites/enemy3.png")

        self.img.set_colorkey((255,255,255))
        self.enemy_bullet_cooldown = random.randint(60,180)
        self.enemy_timer = 0
        
        self.enemyX = enemyXPos 
        self.enemyY = enemyYPos
        self.enemySpeedX = 1
        self.enemySpeedY = 0
        self.enemyHealth = 100 
        
        self.enemy_damage_cooldown = 0

        self.enemyRect = self.img.get_rect()
        self.objectID = objectID
        self.mediator = mediator
        self.screen = screen
    
        

    def get_rect(self):
        return self.enemyRect
    

    ## Damage the enemy
    def setHealth(self, x):
        print(self.enemyHealth)
        self.enemyHealth += x

    def getEnemyHealth(self):
        return self.enemyHealth

    def enemyDraw(self):
        self.screen.blit(self.img, (self.enemyX, self.enemyY))

            
    ##Make sure the enemy stays in the screen
    def enemyMove(self):
        self.enemy_timer += 1
        self.enemy_damage_cooldown += 1
        
        self.enemyX += self.enemySpeedX
        if self.enemyX >= 300 - 14 or self.enemyX <= 0:
            self.enemySpeedX *= -1
            self.enemyY += 20

        self.enemyRect = self.img.get_rect(x=self.enemyX, y=self.enemyY)

        if self.enemy_timer > self.enemy_bullet_cooldown:
            self.enemy_timer = 0
            self.enemy_bullet_cooldown = random.randint(60,180)
            self.mediator.all_game_objects.append(EnemyBullet (self.enemyX,self.enemyY +4, 'e_bullet', self.mediator, self.screen))

 
        
        
    
    def loop(self):
        self.enemyMove()

        if self.collision('f_bullet',self.enemyRect) and self.enemy_damage_cooldown > 10:
            self.enemyHealth -= 10
        
        if self.enemyHealth < 0:
            self.mediator.to_be_removed.append(self)

    def draw(self):
        self.enemyDraw()
            
