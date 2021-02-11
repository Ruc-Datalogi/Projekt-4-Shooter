import sys, pygame
from pygame.locals import *
import os

class Menu:
    

    #Constructor
    def __init__(self):
        pygame.font.init()
        self.menuOn = True
        self.selected = 0


    #
    @property
    def get_menu(self):
        return self.menuOn



    def drawMenu(self, screen, SCREEN_SIZE):
        screen.fill((0,0,0))

        font = pygame.font.SysFont('chalkduster.ttf',72)
        font1 = pygame.font.SysFont('chalkduster.ttf',72)
        font2 = pygame.font.SysFont('chalkduster.ttf',72)
        if self.selected == 0:
            start = font.render('Start', True, (100,100,100))
        else:
            start = font.render('Start', True, (50,50,50))
        if self.selected == 1:
            options = font.render('Options', True, (100,100,100))
        else:
            options = font.render('Options', True, (50,50,50))
        if self.selected == 2:
            quit = font1.render('Quit', True, (100,100,100))
        else: 
            quit = font1.render('Quit', True, (50,50,50))
    
        screen.blit(start, (150, 200))
        screen.blit(options, (150, 300))
        screen.blit(quit, (150, 400))



    def menuInput(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                self.selected += 1 
            if event.key == pygame.K_UP:
                self.selected -= 1
            if event.key == pygame.K_RETURN:
                self.menuOn = False
                self.menuSelecter(self.selected)            
        
        if self.selected > 2:
            self.selected = 0
        
        if self.selected < 0:
            self.selected = 2

    
    
    def menuSelecter(self, input):
        if input == 0:
            return 'start'
        if input == 1:
            return 'options'
        if input == 2:
            sys.exit()
            

