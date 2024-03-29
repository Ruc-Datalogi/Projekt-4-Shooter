import sys, pygame, random
from GameObject import *
from Mediator import *


class EnemyBullet(GameObject):
    
    def __init__(self, xpos, ypos, bullet_speed_x ,bullet_speed_y, bullet_bend , img_bullet, object_ID, screen):
        self.img = img_bullet

        self.enemy_bullet_x = xpos 
        self.enemy_bullet_y = ypos 
        self.enemy_bulletspeed_x = bullet_speed_x
        self.enemy_bulletspeed_y = bullet_speed_y

        
        if self.enemy_bulletspeed_x > 2:
            self.enemy_bulletspeed_x = 2

        if self.enemy_bulletspeed_x < -2:
            self.enemy_bulletspeed_x = -2
        

        self.enemy_bullet_Rect = self.img.get_rect()
        self.enemy_bullet_damage = 10
        self.object_ID = object_ID
        self.screen = screen
        self.alive = True

    
    
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

        if self.enemy_bullet_x > 400:
            Mediator.to_be_removed.append(self)
        if self.enemy_bullet_x < -40:
            Mediator.to_be_removed.append(self)

        if self.enemy_bullet_y < -30:
            Mediator.to_be_removed.append(self)
        
        if self.enemy_bullet_y > 400:
            Mediator.to_be_removed.append(self)
    

    def loop(self):
        self.bullet_move()

    def draw(self):
        self.bullet_draw()