import sys, pygame, random
from GameObject import *
from Mediator import *

class FriendlyBullet(GameObject):
    
    def __init__(self, screen, xpos, ypos, object_ID, mediator):
        self.img = pygame.image.load("Game/sprites/bullets/red_bullet.png")
        self.bullet_x = xpos 
        self.bullet_y = ypos 
        self.screen = screen
        self.bulletspeed_x = 0
        self.bulletspeed_y = 12
        self.bullet_rect = self.img.get_rect()
        self.bullet_damage = 10
        self.object_ID = object_ID
        self.mediator = mediator
    
    ## For collision ##
    
    def get_rect(self):
        return self.bullet_rect
    
    ## For damaging enemy ##
    
    def get_bullet_damage(self):
        return self.bullet_damage

    ## For removing the bullet ##
 
    def get_bullet_y(self):
        return self.bullet_y

    ## Draw at specific location ##
    def bullet_draw(self):        
        self.screen.blit(self.img,(self.bullet_x,self.bullet_y))

    ## Update bullet pos and the rect ##
    def bullet_move(self):
        self.bullet_x -= self.bulletspeed_x
        self.bullet_y -= self.bulletspeed_y
        self.bullet_rect = self.img.get_rect(x=self.bullet_x, y=self.bullet_y)

        if self.bullet_y < -16:
            self.mediator.to_be_removed.append(self)
    
    def loop(self):
        self.bullet_move()

    def draw(self):
        self.bullet_draw()


    