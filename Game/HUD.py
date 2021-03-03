import sys, pygame, random
from Player import *

class HUD:

    def __init__(self, screen, player, screen_size):
        self.screen = screen
        self.player = player
        self.screen_size = screen_size


    def draw_overlay_HUD(self):
        pygame.draw.rect(self.screen,(93, 100, 117), pygame.Rect(0,self.screen_size[1]*0.9, self.screen_size[0], self.screen_size[1]*0.1))
        pygame.draw.rect(self.screen,(52, 61, 82), pygame.Rect(0,self.screen_size[1]*0.9, self.screen_size[0]-1, (self.screen_size[1]-1)*0.1),width=2)
        

    def draw_health_HUD(self):
        pygame.draw.rect(self.screen,(68,77,85), pygame.Rect(20, 420, 260, 10))
        
        # Health bar with 3 different colors.
        ## Green healthbar, if self.healthbar is greater than 50: 
        ## Yellow healthbar, if self.healthbar is greater than 25 and less than 50:
        ## Orange healthbar, if self.healthbar is greater than 0 and less than 25:
        if self.player.get_health() > 50:
            pygame.draw.rect(self.screen,(90,186,74), pygame.Rect(self.screen_size[0], self.screen_size[0], (self.player.get_health/self.healthBar)*260, 10))
        elif self.player.get_health > 25 and self.player.get_health < 50:
            pygame.draw.rect(self.screen,(247,204,59), pygame.Rect(20, 420, (self.player.get_health/self.healthBar)*260, 10))
        elif self.player.get_health > 0 and self.player.get_health < 25:
            pygame.draw.rect(self.screen,(250,115,54), pygame.Rect(20, 420, (self.player.get_health/self.healthBar)*260, 10))