import sys, pygame, random
from EnemyBullet import EnemyBullet
from GameObject import *
from Mediator import *
from Spritesheet import *


class Enemy(GameObject):

    ## Choose enemy sprite ##
    def __init__(self, enemy_xpos, enemy_ypos, enemy_ID, object_ID, mediator, screen):
        
        self.ss = Spritesheet('Game/sprites/SpaceShipAsset.png')
        self.ss2 = Spritesheet('Game/sprites/bullets/allTheBullets.png')
        self.img = self.ss.image_at(pygame.Rect(2, 41, 12, 12))
        self.img_bullet = self.ss2.image_at(pygame.Rect(1, 1, 1, 1))
        # Gul enemy
        if enemy_ID == 0:
            self.img = self.ss.image_at(pygame.Rect(2, 41, 12, 12))
            self.img_bullet = self.ss2.image_at(pygame.Rect(166, 8, 16, 16))
            self.bullet_speed = 1
            self.bullet_interval = 60
        # Grøn enemy
        elif enemy_ID == 1:
            self.img = self.ss.image_at(pygame.Rect(19, 44, 14, 9))
            self.img_bullet = self.ss2.image_at(pygame.Rect(225, 8, 16, 16))
            self.bullet_speed = 2
            self.bullet_interval = 75
        #Blå enemy
        elif enemy_ID == 2:
            self.img = self.ss.image_at(pygame.Rect(39, 44, 9, 10))
            self.img_bullet = self.ss2.image_at(pygame.Rect(187, 8, 16, 16))
            self.bullet_speed = 2.5
            self.bullet_interval = 90

        self.enemy_bullet_cooldown = random.randint(0,60)
        self.enemy_timer = 0
        
        self.enemy_x = enemy_xpos
        self.enemy_y = enemy_ypos
        self.enemy_speed_x = 0.6
        self.enemy_speed_y = 0.1
        self.enemy_health = 110 
        
        self.enemy_damage_cooldown = 0

        self.enemy_rect = self.img.get_rect()
        self.object_ID = object_ID
        self.mediator = mediator
        self.screen = screen
        self.showing_image = self.img
    
        

    def get_rect(self):
        return self.enemy_rect
    

    ## Damage the enemy
    def set_health(self, x):
        print(self.enemy_health)
        self.enemy_health += x

    def get_enemy_health(self):
        return self.enemy_health

    def enemy_draw(self):
        self.screen.blit(self.showing_image, (self.enemy_x, self.enemy_y))

            
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

        if self.enemy_timer > self.bullet_interval + self.enemy_bullet_cooldown:
            self.enemy_bullet_cooldown = random.randint(0,60)
            self.enemy_timer = 0
            self.mediator.all_game_objects.append(EnemyBullet (self.enemy_x,self.enemy_y +4, self.bullet_speed, self.img_bullet, 'e_bullet', self.mediator, self.screen))

 
        
        
    
    def loop(self):
        self.enemy_move()
        #self.showing_image = self.img
        if self.collision('f_bullet',self.enemy_rect) and self.enemy_damage_cooldown > 10:
            self.temp_image = self.img.copy()
            self.temp_image.set_alpha(128)
            self.temp_rect = pygame.Rect(self.enemy_x, self.enemy_y, self.img.get_width(), self.img.get_height())
            #virk
            # zero out RGB values
            #self.temp_image.fill((0, 0, 0, 255), None, pygame.BLEND_RGBA_MULT)
            # add in new RGB values
            #self.temp_image.fill((254, 254, 254), None, pygame.BLEND_RGBA_ADD)

            self.enemy_health -= 10
            self.showing_image = self.temp_image
        
        if self.enemy_health < 0:
            self.mediator.to_be_removed.append(self)

    def draw(self):
        self.enemy_draw()
            
