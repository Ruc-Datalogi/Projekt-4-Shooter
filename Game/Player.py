import sys, pygame, random
from FriendlyBullet import *
from Enemy import Enemy
from GameObject import *
from Mediator import *
from Soundplayer import *
from JsonLoader import *
from Upgrades import *

class Player(GameObject):

    ## Constructor for player ## 
    def __init__(self, screen, object_ID):
        self.img = pygame.image.load(self.resource_path("Game/sprites/playerLV1.png"))
        self.player_x = 125 
        self.player_y = 300
        self.player_speed_x = 0
        self.player_speed_y = 0
        self.general_speed = 3.5

        self.speed_x = [0,0]
        self.speed_y = [0,0]

        self.moving = False
        self.screen = screen
        self.bullet_list = []
        self.timer = 0
        self.player_health = 100
        self.player_damage_cooldown = 0
        self.shield_on = False
        self.shield_timer = 0
        self.shield_cooldown = 600
        self.shield_rect = pygame.Rect(0,0,0,0)
        self.shield_amount = 10
        




        self.object_ID = object_ID
        self.player_rect = pygame.Rect(0,0,0,0)
        self.alive = True

    def get_dmg (self, amount):
        if self.player_health > 0:
            self.player_health -= amount
        if self.player_health <= 0:
            self.player_health = 0
    
    def get_score(self):
        return self.player_score


    def get_health (self):
        return self.player_health

    def get_energy (self):
        return self.shield_amount

    def get_rect(self):
        return self.player_rect    

    ## Draw player and bullets at given pos.
    def player_draw(self):        
        self.screen.blit(self.img,(self.player_x,self.player_y))

        pygame.draw.rect(self.screen, (20,240,10), (self.player_rect))

        if self.shield_on:
            pygame.draw.circle(self.screen,(115,220,255,0.5),(self.player_x+self.img.get_width()/2,self.player_y+1+self.img.get_height()/2),13,1)


        
            
            
        

       


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
        if self.shield_on:
            self.shield_rect = pygame.Rect(self.player_x-4,self.player_y-2,20,20)
            
    ## Get keypressed and use it for movement ##
    def player_input(self):
        self.player_speed_x = 0
        self.player_speed_y = 0
        keystate = pygame.key.get_pressed()

        if keystate[pygame.K_LEFT]:
            self.speed_x[0] -= 0.4

            if self.speed_x[0] < -3.5:
                self.speed_x[0] = -3.5

            self.player_speed_x = self.speed_x[0]

        else:
            self.speed_x[0] = 0

        if keystate[pygame.K_RIGHT]:
            self.speed_x[1] += 0.4

            if self.speed_x[1] > 3.5:
                self.speed_x[1] = 3.5

            self.player_speed_x = self.speed_x[1]
        else: 
            self.speed_x[1] = 0
        

        if keystate[pygame.K_DOWN]:
            self.speed_y[0] += 0.4

            if self.speed_y[0] > 3.5:
                self.speed_y[0] = 3.5

            self.player_speed_y = self.speed_y[0]
        
        else:
            self.speed_y[0] = 0

        if keystate[pygame.K_UP]:
            self.speed_y[1] -= 0.4

            if self.speed_y[1] < -3.5:
                self.speed_y[1] = -3.5

            self.player_speed_y = self.speed_y[1]
        else:
            self.speed_y[1] = 0
            
        if self.timer > int(Upgrades.get_level_fire_speed(Upgrades,JsonLoader.get_fire_speed(JsonLoader))) and keystate[pygame.K_SPACE]:
            self.timer = 0
            if int(Upgrades.get_level_bullet_amount(Upgrades, JsonLoader.get_bullet_amount(JsonLoader))) == 1:
                Mediator.all_game_objects.append(FriendlyBullet(self.screen, self.player_x + 2, self.player_y - 10,'f_bullet'))
            elif int(Upgrades.get_level_bullet_amount(Upgrades, JsonLoader.get_bullet_amount(JsonLoader))) == 2:
                Mediator.all_game_objects.append(FriendlyBullet(self.screen, self.player_x - 4, self.player_y - 10,'f_bullet'))
                Mediator.all_game_objects.append(FriendlyBullet(self.screen, self.player_x + 8, self.player_y - 10,'f_bullet'))
            elif int(Upgrades.get_level_bullet_amount(Upgrades, JsonLoader.get_bullet_amount(JsonLoader))) == 3:
                Mediator.all_game_objects.append(FriendlyBullet(self.screen, self.player_x - 8, self.player_y - 10,'f_bullet'))
                Mediator.all_game_objects.append(FriendlyBullet(self.screen, self.player_x + 2, self.player_y - 10,'f_bullet'))
                Mediator.all_game_objects.append(FriendlyBullet(self.screen, self.player_x + 12, self.player_y - 10,'f_bullet'))
        
        

        if keystate[pygame.K_s] and self.shield_cooldown < self.shield_timer and self.shield_amount >= 1:
            self.shield_on = True
            self.shield_timer = 0
            self.shield_amount -= 1

        
        if keystate[pygame.K_ESCAPE]:
            sys.exit()

        self.timer +=1

    def loop(self):
        self.player_input()
        self.player_move()
        if self.shield_on:
            self.collision('e_bullet', self.shield_rect)
        hit_count = self.collision('e_bullet', self.player_rect)
        enemy_hit = self.collision('enemy', self.player_rect)
        if  hit_count > 0 and self.player_damage_cooldown > 8:
            Soundplayer.player_damage_sound(Soundplayer())
            self.player_damage_cooldown = 0
            self.player_health += -10*hit_count
        if enemy_hit > 0 and self.player_damage_cooldown > 8:
            Soundplayer.player_damage_sound(Soundplayer())
            self.player_damage_cooldown = 0
            self.player_health = 0
        
        
        self.shield_timer += 1
        
        if self.shield_timer > int(Upgrades.get_level_shield(Upgrades,JsonLoader.get_shield(JsonLoader)))*60:
            self.shield_on = False

        
    
    
    def draw(self):
        self.player_draw()
    

    def player_dead(self):
        if self.player_health <= 0:
            return True 

    def reset_player (self):
        self.player_x = 125
        self.player_y = 300
        self.player_health = 100
        self.shield_amount = 10