import sys, pygame
from pygame.locals import *
import os

class Menu:
    ## Constructor ##
    def __init__(self):
        pygame.font.init()
        self.menu_on = True
        self.selected = 0
        self.options_on = False
        self.select_options = 0 
        self.scroller = 0
        self.moving_background = 0

        self.background_Img = pygame.image.load(self.resource_path("Game/sprites/background/preview.png"))
        self.background_Img1 = pygame.image.load(self.resource_path("Game/sprites/background/background_1.png"))
        self.background_Img2 = pygame.image.load(self.resource_path("Game/sprites/background/background_2.png"))
        self.background_Img3 = pygame.image.load(self.resource_path("Game/sprites/background/background_3.png"))
        self.background_Img4 = pygame.image.load(self.resource_path("Game/sprites/background/background_4.png"))

        
    ## Getter to escape menu ##
    @property
    def get_menu(self):
        return self.menu_on

    ## Scrolling background ##
    def draw_background_scrolling(self, display, DISPLAY_SIZE):
        width = self.background_Img1.get_width()
        height = self.background_Img1.get_height()
        
        for i in range(0,2):
            for j in range(-4,8):
                display.blit(self.background_Img1,(i*width,j*height + self.scroller))
        

        self.scroller += 1
        if self.scroller >= height:
            self.scroller = 0



    ## Normal background ##
    def draw_background(self, display, DISPLAY_SIZE):
        width = self.background_Img1.get_width()
        height = self.background_Img1.get_height()
        
        ## Draw the pictures side by side to fill the screen ##
        for i in range(-1, int(DISPLAY_SIZE[0]/width)+1):
            for j in range(-1, int(DISPLAY_SIZE[1]/height +1)):
                display.blit(self.background_Img1,(i*width, j*height))

        width = self.background_Img1.get_width()
        height = self.background_Img1.get_height() 

    
        
    ## Draw menu, options, or upgrade menu ##
    def draw_menu(self, screen, SCREEN_SIZE):
        screen.fill((0,0,0))
        

        font = pygame.font.Font('Game/font/kongtext.ttf',16)
        font1 = pygame.font.Font('Game/font/kongtext.ttf',16)

        title = font.render('The Falcon', True, (110,110,110))
        ## Drawing Menu
        if self.menu_on == True:
            if self.selected == 0:
                start = font.render('Start', True, (100,100,100))
            else:
                start = font.render('Start', True, (50,50,50))

            if self.selected == 1:
                options = font.render('Options', True, (100,100,100))
            else:
                options = font.render('Options', True, (50,50,50))

            if self.selected == 2:
                upgrades = font1.render('Upgrades', True, (100,100,100))
            else:
                upgrades = font1.render('Upgrades', True, (50,50,50))

            if self.selected == 3:
                quit = font1.render('Quit', True, (100,100,100))
            else: 
                quit = font1.render('Quit', True, (50,50,50))


            screen.blit(title,(SCREEN_SIZE[0]/6, (SCREEN_SIZE[1]/6)))
            screen.blit(start,(SCREEN_SIZE[0]/6, (SCREEN_SIZE[1]/6)*2))
            screen.blit(options, (SCREEN_SIZE[0]/6, (SCREEN_SIZE[1]/6)*3))
            screen.blit(upgrades, (SCREEN_SIZE[0]/6, (SCREEN_SIZE[1]/6)*4))
            screen.blit(quit, (SCREEN_SIZE[0]/6, (SCREEN_SIZE[1]/6)*5))
        
        ### Drawing Options ###
        if self.options_on == True:
            pass
            
            
    
    

    ## Handling input in the menu ##      
    def menu_input(self, event):
        if self.menu_on:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    self.selected += 1 
                if event.key == pygame.K_UP:
                    self.selected -= 1
                if event.key == pygame.K_RETURN:
                    ## Start Game ##
                    if self.selected == 0:
                        self.menu_on = False
                    ##Options ##    
                    if self.selected == 1:
                        pass
                    if self.selected == 2:
                        self.menu_on = False
                        self.options_on = True
                    if self.selected == 3:
                        sys.exit()
            
            ## For scrolling in the menu ## 
            if self.selected > 3:
                self.selected = 0
            
            if self.selected < 0:
                self.selected = 3

        ## Options screen input ##
        elif self.options_on:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    self.select_options += 1 
                if event.key == pygame.K_UP:
                    self.select_options -= 1
                if event.key == pygame.K_RETURN:
                    if self.select_options == 0:
                        self.moving_background += 1
                        
                    if self.select_options == 1:
                        self.options_on = False
                        self.menu_on = True

        if self.moving_background > 1:
            self.moving_background = 0

        ## For scrolling in the options ##
        if self.select_options > 1:
            self.select_options = 0
        
        if self.select_options < 0:
            self.select_options = 1

        
    def player_dead(self):
        self.menu_on = True       
    
    def resource_path(self, relative_path):
        try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)