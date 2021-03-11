import sys, pygame, random
from EnemyBullet import EnemyBullet
from GameObject import *
from Mediator import *


class Enemy(GameObject):

    ## Choose enemy sprite ##
    def __init__(self, enemy_xpos, enemy_ypos, enemyID, objectID, mediator, screen):
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
        
        self.enemy_x = enemy_xpos
        self.enemy_y = enemy_ypos
        self.enemy_speed_x = 0.6
        self.enemy_speed_y = 0.1
        self.enemy_health = 20 
        
        self.enemy_damage_cooldown = 0

        self.enemy_rect = self.img.get_rect()
        self.objectID = objectID
        self.mediator = mediator
        self.screen = screen
    
        

    def get_rect(self):
        return self.enemy_rect
    

    ## Damage the enemy
    def set_health(self, x):
        print(self.enemy_health)
        self.enemy_health += x

    def get_enemy_health(self):
        return self.enemy_health

    def enemy_draw(self):
        self.screen.blit(self.img, (self.enemy_x, self.enemy_y))

            
    ##Make sure the enemy stays in the screen
    def enemy_move(self):
        self.enemy_timer += 1
        self.enemy_damage_cooldown += 1
        
        self.enemy_x += self.enemy_speed_x
        if self.enemy_x >= 300 - 14 or self.enemy_x <= 0:
            self.enemy_speed_x *= -1
            
        
        self.enemy_y += self.enemy_speed_y
        if self.enemy_y >= 400:
            self.mediator.to_be_removed.append(self)

        self.enemy_rect = self.img.get_rect(x=self.enemy_x, y=self.enemy_y)

        if self.enemy_timer > self.enemy_bullet_cooldown:
            self.enemy_timer = 0
            self.enemy_bullet_cooldown = random.randint(60,180)
            self.mediator.all_game_objects.append(EnemyBullet (self.enemy_x,self.enemy_y +4, 'e_bullet', self.mediator, self.screen))

 
        
        
    
    def loop(self):
        self.enemy_move()

        if self.collision('f_bullet',self.enemy_rect) and self.enemy_damage_cooldown > 10:
            self.enemy_health -= 10
        
        if self.enemy_health < 0:
            self.mediator.to_be_removed.append(self)

    def draw(self):
        self.enemy_draw()
            
