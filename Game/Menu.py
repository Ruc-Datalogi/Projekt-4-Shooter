import sys, pygame
from pygame.locals import *
import os

class Menu:
    

    #Constructor
    def __init__(self):
        pygame.font.init()
        self.menuOn = True
        self.selected = 0
        self.backGroundImg = pygame.image.load("Game/sprites/background/preview.png")
        self.backGroundImg_1 = pygame.image.load("Game/sprites/background/background_1.png")
        self.backGroundImg_2 = pygame.image.load("Game/sprites/background/background_2.png")
        self.backGroundImg_3 = pygame.image.load("Game/sprites/background/background_3.png")
        self.backGroundImg_4 = pygame.image.load("Game/sprites/background/background_4.png")
        self.scroller = 0
        self.movingBackground = True




    #Getter to escape Menu
    @property
    def get_menu(self):
        return self.menuOn


    def drawBackgroundScrolling(self, display, DISPLAY_SIZE):
        width = self.backGroundImg.get_width()
        height = self.backGroundImg.get_height()
        for i in range(0,2):
            for j in range(-4,8):
                display.blit(self.backGroundImg,(i*width,j*height + self.scroller))
        

        self.scroller += 1
        if self.scroller >= height:
            self.scroller = 0

    def drawBackground(self, display, DISPLAY_SIZE):
        width = self.backGroundImg.get_width()
        height = self.backGroundImg.get_height()
        
        for i in range(-1, int(DISPLAY_SIZE[0]/width)+1):
            for j in range(-1, int(DISPLAY_SIZE[1]/height +1)):
                display.blit(self.backGroundImg,(i*width, j*height))
        width = self.backGroundImg.get_width()
        height = self.backGroundImg.get_height() 
        
        
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