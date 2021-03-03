import sys, pygame, random
from Player import *

class HUD:

    def __init__(self, screen, player, screen_size):
        self.screen = screen
        self.player = player
        self.screen_size = screen_size


    def draw_overlay_HUD(self):
        #overlay background
        pygame.draw.rect(self.screen,(93, 100, 117), pygame.Rect(0,self.screen_size[1]*0.9, self.screen_size[0], self.screen_size[1]*0.1))
        #overlay background border
        pygame.draw.rect(self.screen,(52, 61, 82), pygame.Rect(0,self.screen_size[1]*0.9, self.screen_size[0]-1, (self.screen_size[1]-1)*0.1),width=2)
        pygame.draw.rect(self.screen,(52, 61, 82), pygame.Rect(self.screen_size[0]*0.77,self.screen_size[1]*0.9, self.screen_size[0]-1, (self.screen_size[1]-1)*0.1),width=2)
        #special ability border
        pygame.draw.rect(self.screen,(52, 61, 82), pygame.Rect(self.screen_size[0]*0.79,self.screen_size[1]*0.915, self.screen_size[0]*0.09, self.screen_size[1]*0.07),width=2)
        pygame.draw.rect(self.screen,(52, 61, 82), pygame.Rect(self.screen_size[0]*0.89,self.screen_size[1]*0.915, self.screen_size[0]*0.09, self.screen_size[1]*0.07),width=2)
        
        

    def draw_health_HUD(self):
        #Healthbar background
        pygame.draw.rect(self.screen,(68,77,85), pygame.Rect(self.screen_size[0]*0.02,self.screen_size[1]*0.915, self.screen_size[0]*0.735, self.screen_size[1]*0.03))

        if self.player.get_health() > 25:
            pygame.draw.rect(self.screen,(90,186,74), pygame.Rect(self.screen_size[0]*0.02,self.screen_size[1]*0.915, (self.player.get_health()/100)*self.screen_size[0]*0.735, self.screen_size[1]*0.03))
        else:
            pygame.draw.rect(self.screen,(255,45,12), pygame.Rect(self.screen_size[0]*0.02,self.screen_size[1]*0.915, (self.player.get_health()/100)*self.screen_size[0]*0.735, self.screen_size[1]*0.03))
        # Health bar with 3 different colors.
        ## Green healthbar, if self.healthbar is greater than 50: 
        ## Yellow healthbar, if self.healthbar is greater than 25 and less than 50:
        ## Orange healthbar, if self.healthbar is greater than 0 and less than 25:
        
        

    def draw_energy_HUD(self):
        #Energybar background
        pygame.draw.rect(self.screen,(68,77,85), pygame.Rect(self.screen_size[0]*0.02,self.screen_size[1]*0.955, self.screen_size[0]*0.735, self.screen_size[1]*0.03))
        #Energybar pisgul
        pygame.draw.rect(self.screen,(255, 213, 0), pygame.Rect(self.screen_size[0]*0.02,self.screen_size[1]*0.955, self.screen_size[0]*0.735, self.screen_size[1]*0.03))
        #Energybar brackets
        for i in range(0,10):
            pygame.draw.rect(self.screen,(0, 0, 0), pygame.Rect(self.screen_size[0]*0.02+i*self.screen_size[0]*0.0734,self.screen_size[1]*0.955, self.screen_size[0]*0.0734, (self.screen_size[1]-1)*0.03), width=2)
        
    def draw_HUD(self):
        self.draw_overlay_HUD()
        self.draw_energy_HUD()
        self.draw_health_HUD()