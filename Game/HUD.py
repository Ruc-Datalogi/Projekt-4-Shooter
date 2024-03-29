import sys, pygame, random, os
from Player import *
from Spritesheet import *
from JsonLoader import *

class HUD:

    def __init__(self, screen, player, screen_size, generator):
        self.screen = screen
        self.player = player
        self.screen_size = screen_size
        self.generator = generator
        self.font = pygame.font.Font(self.resource_path('Game/font/kongtext.ttf'),8)
        self.score = 0
        self.ss = Spritesheet(self.resource_path('Game/sprites/coins.png'))
        self.coin = self.ss.image_at(pygame.Rect(79,5,5,5))




    def draw_overlay_HUD(self):
        #overlay bottom background
        pygame.draw.rect(self.screen,(93, 100, 117), pygame.Rect(0,self.screen_size[1]*0.9, self.screen_size[0], self.screen_size[1]*0.1))
        #overlay bottom background border
        pygame.draw.rect(self.screen,(52, 61, 82), pygame.Rect(0,self.screen_size[1]*0.9, self.screen_size[0]-1, (self.screen_size[1]-1)*0.1),width=2)
        pygame.draw.rect(self.screen,(52, 61, 82), pygame.Rect(self.screen_size[0]*0.77,self.screen_size[1]*0.9, self.screen_size[0]-1, (self.screen_size[1]-1)*0.1),width=2)
        
        #overlay top background 
        pygame.draw.rect(self.screen,(93, 100, 117), pygame.Rect(0,0, self.screen_size[0], self.screen_size[1]*0.04))
        #overlay top background border
        pygame.draw.rect(self.screen,(52, 61, 82), pygame.Rect(0,0, self.screen_size[0], self.screen_size[1]*0.04), width=2)


        #special ability square
        pygame.draw.rect(self.screen,(68,77,85), pygame.Rect(self.screen_size[0]*0.79,self.screen_size[1]*0.915, self.screen_size[0]*0.09, self.screen_size[1]*0.07))
        pygame.draw.rect(self.screen,(68,77,85), pygame.Rect(self.screen_size[0]*0.89,self.screen_size[1]*0.915, self.screen_size[0]*0.09, self.screen_size[1]*0.07))
        #special ability border
        pygame.draw.rect(self.screen,(52,61,70), pygame.Rect(self.screen_size[0]*0.79,self.screen_size[1]*0.915, self.screen_size[0]*0.09, self.screen_size[1]*0.07),width=2)
        pygame.draw.rect(self.screen,(52,61,70), pygame.Rect(self.screen_size[0]*0.89,self.screen_size[1]*0.915, self.screen_size[0]*0.09, self.screen_size[1]*0.07),width=2)
        
        

    def draw_health_HUD(self):
        #Healthbar background
        pygame.draw.rect(self.screen,(68,77,85), pygame.Rect(self.screen_size[0]*0.02,self.screen_size[1]*0.915, self.screen_size[0]*0.735, self.screen_size[1]*0.03))

        # Update and draw healthbar
        if self.player.get_health() > 30:
            pygame.draw.rect(self.screen,(90,186,74), pygame.Rect(self.screen_size[0]*0.02,self.screen_size[1]*0.915, (self.player.get_health()/100)*self.screen_size[0]*0.735, self.screen_size[1]*0.03))
        else:
            pygame.draw.rect(self.screen,(255,45,12), pygame.Rect(self.screen_size[0]*0.02,self.screen_size[1]*0.915, (self.player.get_health()/100)*self.screen_size[0]*0.735, self.screen_size[1]*0.03))
        
        for i in range(0,10):
                pygame.draw.rect(self.screen,(52,61,70), pygame.Rect(self.screen_size[0] * 0.018 + i * self.screen_size[0]*0.0734, self.screen_size[1]*0.915, self.screen_size[0]*0.0734, (self.screen_size[1]-1)*0.03), width=2)
        
        pygame.draw.rect(self.screen,(52,61,70), pygame.Rect(self.screen_size[0]*0.02,self.screen_size[1]*0.915, self.screen_size[0]*0.735, self.screen_size[1]*0.03), width=1)

        ## The green bar represents our health
        ## When the healthbar turns gray it means that user has been hit and has lost health
        

        
        

    def draw_energy_HUD(self):
        #Energybar background
        pygame.draw.rect(self.screen,(68,77,85), pygame.Rect(self.screen_size[0]*0.02,self.screen_size[1]*0.955, self.screen_size[0]*0.735, self.screen_size[1]*0.03))
        #Energybar gul
        pygame.draw.rect(self.screen,(115,220,255), pygame.Rect(self.screen_size[0]*0.02,self.screen_size[1]*0.955,(self.player.get_energy()/10)*self.screen_size[0]*0.735, self.screen_size[1]*0.03))
        #Energybar brackets
        for i in range(0,10):
            pygame.draw.rect(self.screen,(52,61,70), pygame.Rect(self.screen_size[0]*0.018+i*self.screen_size[0]*0.0734,self.screen_size[1]*0.955, self.screen_size[0]*0.0734, (self.screen_size[1]-1)*0.03), width=2)
        #Overlay 
        pygame.draw.rect(self.screen,(52,61,70), pygame.Rect(self.screen_size[0]*0.02,self.screen_size[1]*0.955, self.screen_size[0]*0.735, self.screen_size[1]*0.03), width=1)


    def draw_score(self):
        
        score = self.font.render('Score ' + str(self.score) ,0,(255,255,255))
        level = self.font.render('Level ' + str(self.generator.get_level()),0,(255,255,255))
        x = self.font.render('x',0,(255,255,255))

        amount_coins = self.font.render(JsonLoader.get_coins(JsonLoader),0,(255,255,255))
        
        self.screen.blit(self.coin,(90, 6))
        self.screen.blit(x,(98, 4))
        self.screen.blit(amount_coins,(108, 4))
        self.screen.blit(score, (6, 4))
        self.screen.blit(level,(self.screen_size[0] - 70 ,4))



    def draw_HUD(self):
        for object in Mediator.to_be_removed:
            if object.get_object_ID() == 'enemy':
                self.score += 1
            

        self.draw_overlay_HUD()
        self.draw_energy_HUD()
        self.draw_health_HUD()
        self.draw_score()

    def resource_path(self, relative_path):
        try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)
    
