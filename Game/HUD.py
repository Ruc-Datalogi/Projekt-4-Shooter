import sys, pygame, random
from Player import *

class HUD:

    def __init__(self, screen, player, screen_size):
        self.screen = screen
        self.player = player
        self.screen_size = screen_size
        self.font = pygame.font.SysFont('chalkduster.ttf',18)


    def draw_overlay_HUD(self):
        #overlay bottom background
        pygame.draw.rect(self.screen,(93, 100, 117), pygame.Rect(0,self.screen_size[1]*0.9, self.screen_size[0], self.screen_size[1]*0.1))
        #overlay bottom background border
        pygame.draw.rect(self.screen,(52, 61, 82), pygame.Rect(0,self.screen_size[1]*0.9, self.screen_size[0]-1, (self.screen_size[1]-1)*0.1),width=2)
        pygame.draw.rect(self.screen,(52, 61, 82), pygame.Rect(self.screen_size[0]*0.77,self.screen_size[1]*0.9, self.screen_size[0]-1, (self.screen_size[1]-1)*0.1),width=2)
        
        #overlay top background 
        pygame.draw.rect(self.screen,(93, 100, 117), pygame.Rect(0,0, self.screen_size[0], self.screen_size[1]*0.05))
        #overlay top background border
        pygame.draw.rect(self.screen,(52, 61, 82), pygame.Rect(0,0, self.screen_size[0], self.screen_size[1]*0.05), width=2)


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

        
        

        
        

    def draw_energy_HUD(self):
        #Energybar background
        pygame.draw.rect(self.screen,(68,77,85), pygame.Rect(self.screen_size[0]*0.02,self.screen_size[1]*0.955, self.screen_size[0]*0.735, self.screen_size[1]*0.03))
        #Energybar gul
        pygame.draw.rect(self.screen,(255, 213, 0), pygame.Rect(self.screen_size[0]*0.02,self.screen_size[1]*0.955, self.screen_size[0]*0.735, self.screen_size[1]*0.03))
        #Energybar brackets
        for i in range(0,10):
            pygame.draw.rect(self.screen,(52,61,70), pygame.Rect(self.screen_size[0]*0.018+i*self.screen_size[0]*0.0734,self.screen_size[1]*0.955, self.screen_size[0]*0.0734, (self.screen_size[1]-1)*0.03), width=2)
        #Overlay 
        pygame.draw.rect(self.screen,(52,61,70), pygame.Rect(self.screen_size[0]*0.02,self.screen_size[1]*0.955, self.screen_size[0]*0.735, self.screen_size[1]*0.03), width=1)


    def draw_score(self):
        
        text = self.font.render('Score: ',1,(200,200,200))
        self.screen.blit(text, (6, 5))


    def draw_HUD(self):
        self.draw_overlay_HUD()
        self.draw_energy_HUD()
        self.draw_health_HUD()
        self.draw_score()

