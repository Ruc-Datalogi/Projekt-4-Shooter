import sys, pygame
from pygame.locals import *
from Soundplayer import *
from JsonLoader import *
import os

class Menu:
    ## Constructor ##
    def __init__(self , screen, SCREEN_SIZE):
        pygame.font.init()
        self.menu_on = True
        self.front_screen = True
        self.selected = 0
        self.options_on = False
        self.select_options = 0 
        self.scroller = 0
        self.moving_background = 0
        self.font = pygame.font.Font('Game/font/kongtext.ttf', 16)
        self.font_display = pygame.font.Font('Game/font/kongtext.ttf', 8)
        self.volume_music_int = int(JsonLoader.get_music(JsonLoader))
        self.volume_sounds_int = int(JsonLoader.get_sounds(JsonLoader))
        self.volume_incrementer = 10

        self.screen = screen
        self.SCREEN_SIZE = SCREEN_SIZE

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
    def draw_background(self):
        width = self.background_Img1.get_width()
        height = self.background_Img1.get_height()
        
        ## Draw the pictures side by side to fill the screen ##
        for i in range(-1, int(self.SCREEN_SIZE[0]/width)+1):
            for j in range(-1, int(self.SCREEN_SIZE[1]/height +1)):
                self.screen.blit(self.background_Img1,(i*width, j*height))

        width = self.background_Img1.get_width()
        height = self.background_Img1.get_height() 

    

    def draw_front_screen(self):
            title = self.font.render('The Falcon', True, (120,120,120))

            if self.selected == 0:
                start = self.font.render('Start', True, (100,100,100))
            else:
                start = self.font.render('Start', True, (50,50,50))

            if self.selected == 1:
                options = self.font.render('Options', True, (100,100,100))
            else:
                options = self.font.render('Options', True, (50,50,50))

            if self.selected == 2:
                upgrades = self.font.render('Upgrades', True, (100,100,100))
            else:
                upgrades = self.font.render('Upgrades', True, (50,50,50))

            if self.selected == 3:
                quit = self.font.render('Quit', True, (100,100,100))
            else: 
                quit = self.font.render('Quit', True, (50,50,50))

            self.screen.blit(title,(self.SCREEN_SIZE[0]/6, (self.SCREEN_SIZE[1]/6)))
            self.screen.blit(start,(self.SCREEN_SIZE[0]/6, (self.SCREEN_SIZE[1]/6)*2))
            self.screen.blit(options, (self.SCREEN_SIZE[0]/6, (self.SCREEN_SIZE[1]/6)*3))
            self.screen.blit(upgrades, (self.SCREEN_SIZE[0]/6, (self.SCREEN_SIZE[1]/6)*4))
            self.screen.blit(quit, (self.SCREEN_SIZE[0]/6, (self.SCREEN_SIZE[1]/6)*5))

    def draw_options_screen(self):
        options_title = self.font.render('Options', True, (120,120,120))

        if self.select_options == 0:
            volume_music = self.font.render('Music ', True, (100,100,100))
        else:
            volume_music = self.font.render('Music ', True, (50,50,50))

        if self.select_options == 1:
            volume_sounds = self.font.render('Sounds ', True, (100,100,100))
        else:
            volume_sounds = self.font.render('Sounds ', True, (50,50,50))

        if self.select_options == 2:
            display = self.font.render('Display', True, (100,100,100))
        else:
            display = self.font.render('Display', True, (50,50,50))

        if self.select_options == 3:
            back = self.font.render('Back', True, (100,100,100))
        else:
            back = self.font.render('Back', True, (50,50,50))

        

        volume_music_font = self.font.render(str(self.volume_music_int), False, (80,80,80))
        volume_sounds_font = self.font.render(str(self.volume_sounds_int), False, (80,80,80))
        display_size_font = self.font_display.render(str(self.SCREEN_SIZE[0]) + 'X' + str(self.SCREEN_SIZE[1]),False, (80,80,80))

        self.screen.blit(options_title, (self.SCREEN_SIZE[0]/6, (self.SCREEN_SIZE[1]/6)))
        ## Volume for music
        self.screen.blit(volume_music, (self.SCREEN_SIZE[0]/6, (self.SCREEN_SIZE[1]/6)*2))
        self.screen.blit(volume_music_font,((self.SCREEN_SIZE[0]/6)*4, (self.SCREEN_SIZE[1]/6)*2))

        ## Volume for sounds
        self.screen.blit(volume_sounds, (self.SCREEN_SIZE[0]/6, (self.SCREEN_SIZE[1]/6)*3))
        self.screen.blit(volume_sounds_font, ((self.SCREEN_SIZE[0]/6)*4, (self.SCREEN_SIZE[1]/6)*3))


        ## Display size
        self.screen.blit(display, (self.SCREEN_SIZE[0]/6, (self.SCREEN_SIZE[1]/6)*4))
        self.screen.blit(display_size_font,((self.SCREEN_SIZE[0]/6)*4,(self.SCREEN_SIZE[1]/6)*4 + 6) )


        ## Escpae options
        self.screen.blit(back,(self.SCREEN_SIZE[0]/6, (self.SCREEN_SIZE[1]/6)*5))

    ## Draw menu, options, or upgrade menu ##
    def draw_menu(self):
        self.screen.fill((0,0,0))
        

        ## Drawing Menu
        if self.front_screen == True:
            self.draw_front_screen()
            

        
        ### Drawing Options ###
        elif self.options_on == True:
            self.draw_options_screen()
            
            
    
    

    ## Handling input in the menu ##      
    def menu_input(self, event):
        if self.front_screen:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    self.selected += 1 
                if event.key == pygame.K_UP:
                    self.selected -= 1
                if event.key == pygame.K_RETURN:
                    ## Start Game ##
                    if self.selected == 0:
                        self.menu_on = False
                    
                    ## Options ##    
                    if self.selected == 1:
                        self.front_screen = False
                        self.options_on = True
                    
                    ## Upgrades ## 
                    if self.selected == 2:
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
                    print('fuhdufhs')
                    if self.select_options == 3:
                        self.options_on = False
                        self.front_screen = True




                ## For music ##
                if event.key == pygame.K_LEFT:

                    ## For controlling the volume of the music
                    if self.select_options == 0:
                        self.volume_music_int -= self.volume_incrementer
                        if self.volume_music_int < 0:
                            self.volume_music_int = 0

                        JsonLoader.updateJsonFile(JsonLoader,'music-')
                        Soundplayer.change_volume_music(Soundplayer(), self.volume_music_int)

                    ## For the sounds
                    if self.select_options == 1:
                        self.volume_sounds_int -= self.volume_incrementer
                        if self.volume_sounds_int < 0:
                            self.volume_sounds_int = 0
                    
                        Soundplayer.change_volume_sounds(Soundplayer(), int(JsonLoader.get_music(JsonLoader)))
                        Soundplayer.player_damage_sound(Soundplayer())


                if event.key == pygame.K_RIGHT:
                    ## For controlling the volume of the music
                    if self.select_options == 0:
                        self.volume_music_int += self.volume_incrementer

                        if self.volume_music_int > 100:
                            self.volume_music_int = 100

                        JsonLoader.updateJsonFile(JsonLoader,'music+')

                        Soundplayer.change_volume_music(Soundplayer(), int(JsonLoader.get_music(JsonLoader)))



                    ## Sounds 
                    if self.select_options == 1:
                        self.volume_sounds_int += self.volume_incrementer

                        if self.volume_sounds_int > 100:
                            self.volume_sounds_int = 100

                        Soundplayer.change_volume_sounds(Soundplayer(), self.volume_sounds_int)
                        Soundplayer.player_damage_sound(Soundplayer())

                  

        if self.moving_background > 1:
            self.moving_background = 0

        ## For scrolling in the options ##
        if self.select_options > 3:
            self.select_options = 0
        
        if self.select_options < 0:
            self.select_options = 3

        
    def player_dead(self):
        self.menu_on = True       
    
    # PyInstaller creates a temp folder and stores path in _MEIPASS
    def resource_path(self, relative_path):
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)