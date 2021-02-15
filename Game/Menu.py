import sys, pygame
from pygame.locals import *
import os

class Menu:
    

    #Constructor
    def __init__(self):
        pygame.font.init()
        self.menuOn = True
        self.selected = 0


    #Getter to escape Menu
    @property
    def get_menu(self):
        return self.menuOn



    def drawMenu(self, screen, SCREEN_SIZE):
        screen.fill((0,0,0))

        font = pygame.font.SysFont('chalkduster.ttf',48)
        font1 = pygame.font.SysFont('chalkduster.ttf',48)
        font2 = pygame.font.SysFont('chalkduster.ttf',48)
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
    
        screen.blit(start,(SCREEN_SIZE[0]/4, (SCREEN_SIZE[1]/6)*2))
        screen.blit(options, (SCREEN_SIZE[0]/4, (SCREEN_SIZE[1]/6)*3))
        screen.blit(quit, (SCREEN_SIZE[0]/4, (SCREEN_SIZE[1]/6)*4))



    def menuInput(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                self.selected += 1 
            if event.key == pygame.K_UP:
                self.selected -= 1
            if event.key == pygame.K_RETURN:
                #Start Game
                if self.selected == 0:
                    self.menuOn = False
                if self.selected == 1:
                    pass
                if self.selected == 2:
                    sys.exit()
                    
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
            return 'quit'            