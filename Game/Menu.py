import sys, pygame
from pygame.locals import *
import os

class Menu:
    
    score = 0

    ## Constructor ##
    def __init__(self):
        pygame.font.init()
        self.menuOn = True
        self.selected = 0
        self.optionsOn = False
        self.selectOptions = 0
        self.upgradesOn = False
        self.selectUpgrades = 0 
        self.scroller = 0
        self.movingBackground = 0
        self.score_font = pygame.font.SysFont('comicsans', 30, True)

        self.backGroundImg = pygame.image.load("Game/sprites/background/preview.png")
        self.backGroundImg_1 = pygame.image.load("Game/sprites/background/background_1.png")
        self.backGroundImg_2 = pygame.image.load("Game/sprites/background/background_2.png")
        self.backGroundImg_3 = pygame.image.load("Game/sprites/background/background_3.png")
        self.backGroundImg_4 = pygame.image.load("Game/sprites/background/background_4.png")

        
        




    ## Getter to escape menu ##
    @property
    def get_menu(self):
        return self.menuOn

    ## Scrolling background ##
    def drawBackgroundScrolling(self, display, DISPLAY_SIZE):
        width = self.backGroundImg.get_width()
        height = self.backGroundImg.get_height()
        
        for i in range(0,2):
            for j in range(-4,8):
                display.blit(self.backGroundImg,(i*width,j*height + self.scroller))
        

        self.scroller += 1
        if self.scroller >= height:
            self.scroller = 0



    ## Normal background ##
    def drawBackground(self, display, DISPLAY_SIZE):
        width = self.backGroundImg.get_width()
        height = self.backGroundImg.get_height()
        
        ## Draw the pictures side by side to fill the screen ##
        for i in range(-1, int(DISPLAY_SIZE[0]/width)+1):
            for j in range(-1, int(DISPLAY_SIZE[1]/height +1)):
                display.blit(self.backGroundImg,(i*width, j*height))

        width = self.backGroundImg.get_width()
        height = self.backGroundImg.get_height() 

    
        
    ## Draw menu, options, or upgrade menu ##
    def drawMenu(self, screen, SCREEN_SIZE):
        screen.fill((0,0,0))

        font = pygame.font.SysFont('chalkduster.ttf',48)
        font1 = pygame.font.SysFont('chalkduster.ttf',48)
        fontSmall = pygame.font.SysFont('chalkduster.ttf',24)

        title = font.render('The Falcon', True, (120,120,120))
        ## Drawing Menu
        if self.menuOn == True:
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
        if self.optionsOn == True:
            pass
            
            
    
    

    ## Handling input in the menu ##      
    def menuInput(self, event):
        if self.menuOn:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    self.selected += 1 
                if event.key == pygame.K_UP:
                    self.selected -= 1
                if event.key == pygame.K_RETURN:
                    ## Start Game ##
                    if self.selected == 0:
                        self.menuOn = False
                    ##Options ##    
                    if self.selected == 1:
                        pass
                    if self.selected == 2:
                        self.menuOn = False
                        self.optionsOn = True
                    if self.selected == 3:
                        sys.exit()
            
            ## For scrolling in the menu ## 
            if self.selected > 3:
                self.selected = 0
            
            if self.selected < 0:
                self.selected = 3

        ## Options screen input ##
        elif self.optionsOn:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    self.selectOptions += 1 
                if event.key == pygame.K_UP:
                    self.selectOptions -= 1
                if event.key == pygame.K_RETURN:
                    if self.selectOptions == 0:
                        self.movingBackground += 1
                        
                    if self.selectOptions == 1:
                        self.optionsOn = False
                        self.menuOn = True

        if self.movingBackground > 1:
            self.movingBackground = 0

        ## For scrolling in the options ##
        if self.selectOptions > 1:
            self.selectOptions = 0
        
        if self.selectOptions < 0:
            self.selectOptions = 1

        
    def menuSelecter(self, input):
        if input == 0:
            return 'start'
        if input == 1:
            return 'options'
        if input == 2:
            return 'quit'       

    def set_score(self, x):
        score += x
        