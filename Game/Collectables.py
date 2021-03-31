from Spritesheet import *
from GameObject import *

import random, json

class Collectables(GameObject):

    def __init__(self, x_pos, y_pos ,screen, mediator, object_ID):
        self.screen = screen
        self.x_pos = x_pos
        self.y_pos = y_pos

        self.x_speed = random.uniform(-0.5,0.5) 
    
        self.y_speed = - 2

        self.mediator = mediator
        self.object_ID = object_ID
        self.ss = Spritesheet(self.resource_path('Game/sprites/coins.png'))
        self.img = self.ss.image_at(pygame.Rect(1,2,1,2))
        
        self.rect = pygame.Rect(x_pos,y_pos,2,2)

        if self.object_ID == 'coin':
            self.img = self.ss.image_at(pygame.Rect(3,2,10,11))
            


    def get_rect(self):
        return self.rect

    def loop(self):
        self.x_pos += self.x_speed
        self.y_pos += self.y_speed

        self.y_speed += 0.1

        if self.y_speed > 3:
            self.y_speed = 3
        
        self.rect = self.img.get_rect(x=self.x_pos, y=self.y_pos)

        if self.collision('player', self.rect):
            self.updateJsonFile('coin')
            self.mediator.to_be_removed.append(self)

        


    def draw(self):
        self.screen.blit(self.img,(self.x_pos,self.y_pos))

    

