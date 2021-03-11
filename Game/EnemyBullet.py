import sys, pygame, random
from GameObject import *
from Mediator import *
from Spritesheet import *


class EnemyBullet(GameObject):
    
    def __init__(self, xpos, ypos, objectID, mediator, screen):
        self.ss = SpriteSheet('Game/sprites/bullets/allTheBullets.png')
        self.img = self.ss.image_at(pygame.Rect(146, 8, 16, 16))
        self.img = pygame.transform.scale(self.img,(8,8))
        self.enemy_bullet_x = xpos 
        self.enemy_bullet_y = ypos 
        self.enemy_bulletspeed_x = random.uniform(-1,1)
        self.enemy_bulletspeed_y = 1.5
        self.enemy_bullet_Rect = self.img.get_rect()
        self.enemy_bullet_damage = 10
        self.objectID = objectID
        self.mediator = mediator
        self.screen = screen
    
    ## For collision ##
    def get_rect(self):
        return self.enemy_bullet_Rect
    
    ## For damaging enemy ##
    def get_bullet_damage(self):
        return self.enemy_bullet_damage

    ## For removing the bullet ##
    def get_bullet_y(self):
        return self.enemy_bullet_y

    ## Draw at specific location ##
    def bullet_draw(self):        
        self.screen.blit(self.img,(self.enemy_bullet_x,self.enemy_bullet_y))

    ## Update bullet pos and the rect ##
    def bullet_move(self):
        self.enemy_bullet_x += self.enemy_bulletspeed_x
        self.enemy_bullet_y += self.enemy_bulletspeed_y
        self.enemy_bullet_Rect = self.img.get_rect(x=self.enemy_bullet_x, y=self.enemy_bullet_y)
    

    def loop(self):
        self.bullet_move()

    def draw(self):
        self.bullet_draw()