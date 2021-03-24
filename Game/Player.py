import sys, pygame, random
from FriendlyBullet import *
from Enemy import Enemy
from GameObject import *
from Mediator import *
from Soundplayer import *

class Player(GameObject):

    ## Constructor for player ## 
    def __init__(self, screen, mediator, object_ID):
        self.img = pygame.image.load("Game/sprites/playerLV1.png")
        self.player_x = 125 
        self.player_y = 300
        self.player_speed_x = 0
        self.player_speed_y = 0
        self.general_speed = 3.5

        self.moving = False
        self.screen = screen
        self.bullet_list = []
        self.timer = 0
        self.player_health = 100
        self.player_damage_cooldown = 0




        self.mediator = mediator
        self.object_ID = object_ID
        self.player_rect = pygame.Rect(0,0,0,0)
        self.soundplayer = Soundplayer()

    def get_dmg (self, amount):
        if self.player_health > 0:
            self.player_health -= amount
        if self.player_health <= 0:
            self.player_health = 0
    
    def get_score(self):
        return self.player_score


    def get_health (self):
        return self.player_health

    def get_rect(self):
        return self.player_rect    

    ## Draw player and bullets at given pos.
    def player_draw(self):        
        self.screen.blit(self.img,(self.player_x,self.player_y))

        pygame.draw.rect(self.screen, (20,240,10), (self.player_rect))
        

       


    ## Character move and game boundaries ##
    def player_move(self):
        self.player_x += self.player_speed_x
        self.player_y += self.player_speed_y

        if self.player_x <= 0:
            self.player_x = 0
        if self.player_x >= 300 - 14:
            self.player_x = 300 - 14
        if self.player_y <= 16: 
            self.player_y = 16
        if self.player_y >= 400*0.855:
            self.player_y = 400*0.855


        self.player_damage_cooldown += 1

        self.player_rect = pygame.Rect(self.player_x + 5 , self.player_y + 5, 3, 6)
            
    ## Get keypressed and use it for movement ##
    def player_input(self):
        self.player_speed_x = 0
        self.player_speed_y = 0
        keystate = pygame.key.get_pressed()

        if keystate[pygame.K_LEFT]:
            self.player_speed_x -= self.general_speed

        if keystate[pygame.K_RIGHT]:
            self.player_speed_x = self.general_speed

        if keystate[pygame.K_UP]:
            self.player_speed_y -= self.general_speed

        if keystate[pygame.K_DOWN]:
            self.player_speed_y = self.general_speed
            
        if self.timer > 10 and keystate[pygame.K_SPACE]:
            self.timer = 0
            self.mediator.all_game_objects.append(FriendlyBullet(self.screen, self.player_x + 2, self.player_y - 10,'f_bullet',self.mediator))
        
        if keystate[pygame.K_ESCAPE]:
            sys.exit()

        self.timer +=1

    def loop(self):
        self.player_input()
        self.player_move()
        hit_count = self.collision('e_bullet', self.player_rect)
        
        if  hit_count > 0 and self.player_damage_cooldown > 8:
            Soundplayer.player_damage_sound(Soundplayer())
            self.player_damage_cooldown = 0
            self.player_health += -10*hit_count
        

    
    def draw(self):
        self.player_draw()
    

    def player_dead(self):
        if self.player_health <= 0:
            self.player_x = 125
            self.player_y = 300
            self.player_health = 100
            return True 