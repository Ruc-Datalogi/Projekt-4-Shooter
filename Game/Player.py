import sys, pygame, random
from Friendly_Bullet import Friendly_Bullet
from Enemy import Enemy
from GameObject import *
from Mediator import *

class Player(GameObject):

    ## Constructor for player ## 
    def __init__(self, screen, mediator, objectID):
        self.img = pygame.image.load("Game/sprites/playerLV1.png")
        self.player_x = 100 
        self.player_y = 100
        self.player_speed_x = 0
        self.player_speed_y = 0
        self.general_speed = 3.5

        self.moving = False
        self.screen = screen
        self.bullet_list = []
        self.timer = 0
        self.playerHealth = 100
        self.player_damage_cooldown = 0
        self.player_score = 0



        self.mediator = mediator
        self.objectID = objectID
        self.player_rect = pygame.Rect(0,0,0,0)

    def get_dmg (self, amount):
        if self.playerHealth > 0:
            self.playerHealth -= amount
        if self.playerHealth <= 0:
            self.playerHealth = 0
    
    def get_score(self):
        return self.player_score


    def get_health (self):
        return self.playerHealth

    def healthRect (self, screen):
        pass
        #(screen, (255, 0, 0), (10,10,self.playerHealth / self.healthRatio,25))
    
    def get_rect(self):
        return self.player_rect    


    ## Draw player and bullets at given pos ##
    ## Drawing two rectangles, a green and a dark blue bar.
    ## The Green bar represents our health and the dark blue bar has the same value but doesn't change
    ## This makes it easier to see how much health our character has lost and how much it has left
    def playerDraw(self , screen):        
        screen.blit(self.img,(self.player_x,self.player_y))
        

       


    ## Character move and game boundaries ##
    def playerMove(self):
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

        
        if self.playerHealth <= 0:
            sys.exit()

        self.player_damage_cooldown += 1

        self.player_rect = pygame.Rect(self.player_x, self.player_y, self.img.get_width(), self.img.get_height())
            
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
            self.mediator.all_game_objects.append(Friendly_Bullet(self.screen, self.player_x + 2, self.player_y - 10,'f_bullet',self.mediator))
        
        if keystate[pygame.K_ESCAPE]:
            sys.exit()

        self.timer +=1

    def loop(self):
        self.player_input()
        self.playerMove()
        hit_count = self.collision('e_bullet', self.player_rect)
        if  hit_count > 0 and self.player_damage_cooldown > 8:
            self.player_damage_cooldown = 0
            self.playerHealth += -10*hit_count
        
        for object in self.mediator.to_be_removed:
            if object.getObjectID() == 'enemy':
                self.player_score += 1

    
    def draw(self):
        self.playerDraw(self.screen)
                