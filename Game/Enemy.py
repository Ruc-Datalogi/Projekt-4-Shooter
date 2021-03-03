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
        self.enemy_bullet_cooldown = random.randint(300,600)
        self.enemy_timer = 0
        
        self.enemyX = enemyXPos 
        self.enemyY = enemyYPos
        self.enemySpeedX = 1.5
        self.enemySpeedY = 0
        self.enemyHealth = 200 
        self.enemy_bullet_list = []
        self.enemyRect = self.img.get_rect()

        self.objectID = objectID
        self.mediator = mediator
        self.screen = screen
    
        

    @property
    def getEnemyRect(self):
        return self.enemyRect
    

    ## Damage the enemy
    def setHealth(self, x):
        print(self.enemyHealth)
        self.enemyHealth += x

    @property
    def getEnemyHealth(self):
        return self.enemyHealth

    def enemyDraw(self):
        self.screen.blit(self.img, (self.enemyX, self.enemyY))

            
    ##Make sure the enemy stays in the screen
    def enemyMove(self):
        self.enemy_timer += 1
        self.enemyX += self.enemySpeedX
        if self.enemyX >= 300 or self.enemyX <= 0:
            self.enemySpeedX *= -1
            self.enemyY += 20
        self.enemyRect = self.img.get_rect(x=self.enemyX, y=self.enemyY)

        if self.enemy_timer > 10:
            self.enemy_timer = 0
            self.enemy_bullet_cooldown = random.randint(500,800)
            self.mediator.all_game_objects.append(EnemyBullet (self.enemyX,self.enemyY +4, 'e_bullet', self.mediator, self.screen))
        
        
    
    def loop(self):
        self.enemyMove()

    def draw(self):
        self.enemyDraw()
            
