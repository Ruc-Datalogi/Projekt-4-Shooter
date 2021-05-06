import sys, pygame, os
from pygame.locals import *
from Soundplayer import *
from JsonLoader import *
from Upgrades import *

class Menu:
    ## Constructor ##
    def __init__(self , screen, SCREEN_SIZE):
        pygame.font.init()
        self.menu_on = True
        self.front_screen = True
       
        self.selected = 0
        self.options_on = False
        self.select_options = 0 

        self.select_upgrades = 0
        self.upgrades_on = False

        self.select_current_upgrade = 0
        self.bullet_damage_on = False
        self.bullet_amount_on = False
        self.bullet_fire_speed_on = False
        self.shield_on = False



        self.scroller = 0
        self.moving_background = 0
        self.font = pygame.font.Font('Game/font/kongtext.ttf', 16)
        self.font_display = pygame.font.Font('Game/font/kongtext.ttf', 8)
        self.font_upgrades = pygame.font.Font('Game/font/kongtext.ttf', 8)

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
            title = self.font.render('The Falcon', True, (255,129,0))

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

    def draw_upgrades_screen(self):
        upgrades_title = self.font.render('Upgrades', True, (120,120,120))
        #price = self.font_upgrades.render('Price', True, (255,180,40))
        #level = self.font_upgrades.render('Level', True, (120,120,120))
        coins = self.font_upgrades.render('Coins:', True ,(255,180,40))
        current_coins = self.font_upgrades.render(JsonLoader.get_coins(JsonLoader),True,(255,180,40))

        if self.select_upgrades == 0:
            damage_upgrade = self.font_upgrades.render('Bullet damage', True, (120,120,120))
        else:
            damage_upgrade = self.font_upgrades.render('Bullet damage', True, (50,50,50))

        if self.select_upgrades == 1:
            bullet_amount = self.font_upgrades.render('Bullet amount', True, (120,120,120))
        else:
            bullet_amount = self.font_upgrades.render('Bullet amount', True, (50,50,50))


        if self.select_upgrades == 2:
            fire_speed = self.font_upgrades.render('Fire speed', True, (120,120,120))
        else:
            fire_speed = self.font_upgrades.render('Fire speed', True, (50,50,50))


        if self.select_upgrades == 3:
            shield = self.font_upgrades.render('Shield', True ,(120,120,120))
        else:
            shield = self.font_upgrades.render('Shield', True ,(50,50,50))

        if self.select_upgrades == 4:
            back = self.font.render('Back', True, (120,120,120))
        else:
            back = self.font.render('Back', True, (50,50,50))

        #coins_int = self.font_upgrades.render(JsonLoader.get_coins(JsonLoader),True, (255,247,122))

        #damage_int = self.font_upgrades.render(JsonLoader.get_bullet_damage(JsonLoader), True, (50,50,50))
        #amount_int = self.font_upgrades.render(JsonLoader.get_bullet_amount(JsonLoader),True,(50,50,50))
        #fire_int = self.font_upgrades.render(JsonLoader.get_fire_speed(JsonLoader),True,(50,50,50))
        #shield_int = self.font_upgrades.render(JsonLoader.get_shield(JsonLoader),True,(50,50,50))

        #damage_price =  self.font_upgrades.render(Upgrades.get_price_bullet_damage(Upgrades,JsonLoader.get_bullet_damage(JsonLoader)),True, (50,50,50))
        #damage_price =  self.font_upgrades.render(Upgrades.get_price_bullet_damage(Upgrades,JsonLoader.get_bullet_damage(JsonLoader)),True, (50,50,50))
        #damage_price =  self.font_upgrades.render(Upgrades.get_price_bullet_damage(Upgrades,JsonLoader.get_bullet_damage(JsonLoader)),True, (50,50,50))
        #damage_price =  self.font_upgrades.render(Upgrades.get_price_bullet_damage(Upgrades,JsonLoader.get_bullet_damage(JsonLoader)),True, (50,50,50))

    



        self.screen.blit(upgrades_title, (self.SCREEN_SIZE[0]/8, (self.SCREEN_SIZE[1]/8)))
        #self.screen.blit(level,( (self.SCREEN_SIZE[0]/8)* 4.5 ,(self.SCREEN_SIZE[1]/8)*2 ))
        #self.screen.blit(price,( (self.SCREEN_SIZE[0]/8)* 6 ,(self.SCREEN_SIZE[1]/8)*2 ))
        self.screen.blit(coins,(self.SCREEN_SIZE[0]/8*5.2,(self.SCREEN_SIZE[1]/8*1.14) ))


        #self.screen.blit(coins_int,( (self.SCREEN_SIZE[0]/8)*2.7,(self.SCREEN_SIZE[1]/8)*2 ))
        #self.screen.blit(damage_int,( (self.SCREEN_SIZE[0]/8)* 4.5 ,(self.SCREEN_SIZE[1]/8)*3))
        #self.screen.blit(amount_int,( (self.SCREEN_SIZE[0]/8)* 4.5 ,(self.SCREEN_SIZE[1]/8)*4))
        #self.screen.blit(fire_int,( (self.SCREEN_SIZE[0]/8)* 4.5 ,(self.SCREEN_SIZE[1]/8)*5))
        #self.screen.blit(shield_int,( (self.SCREEN_SIZE[0]/8)* 4.5 ,(self.SCREEN_SIZE[1]/8)*6))

        #self.screen.blit(damage_price,((self.SCREEN_SIZE[0]/8)* 6,(self.SCREEN_SIZE[1]/8)*3))


        self.screen.blit(damage_upgrade,(self.SCREEN_SIZE[0]/8,(self.SCREEN_SIZE[1]/8)*2))
        self.screen.blit(bullet_amount,(self.SCREEN_SIZE[0]/8,(self.SCREEN_SIZE[1]/8)*3))
        self.screen.blit(fire_speed,(self.SCREEN_SIZE[0]/8,(self.SCREEN_SIZE[1]/8)*4))
        self.screen.blit(shield,(self.SCREEN_SIZE[0]/8,(self.SCREEN_SIZE[1]/8)*5))
        self.screen.blit(back,(self.SCREEN_SIZE[0]/8,(self.SCREEN_SIZE[1]/8)*6.5))
        self.screen.blit(current_coins,(self.SCREEN_SIZE[0]/8*6.5,(self.SCREEN_SIZE[1]/8*1.14) ))

    def draw_bullet_damage_screen(self):
        upgrades_title = self.font.render('Upgrades', True, (120,120,120))
        current_upgrade = self.font_upgrades.render('Bullet damage', True, (100,100,100))
        coins = self.font_upgrades.render('Coins:', True ,(255,180,40))
        current_bullet_damage = self.font_upgrades.render('Current:', True ,(100,100,100))
        upgraded_bullet_damage = self.font_upgrades.render('Upgrade:', True ,(20,148,20))
        bullet_damage_increment = self.font_upgrades.render('+2', True ,(20,148,20))
        cost = self.font_upgrades.render('Cost:', True ,(255,180,40))
        bullet_damage = self.font_upgrades.render(JsonLoader.get_bullet_damage(JsonLoader),True,(100,100,100))
        price = self.font_upgrades.render(Upgrades.get_price_bullet_damage(Upgrades,JsonLoader.get_bullet_damage(JsonLoader)), True,(255,180,40))
        current_coins = self.font_upgrades.render(JsonLoader.get_coins(JsonLoader),True,(255,180,40))

        if self.select_current_upgrade == 0:
            upgrade = self.font.render('Upgrade', True, (20,148,20))
        else:
            upgrade = self.font.render('Upgrade', True, (50,50,50))

        if self.select_current_upgrade == 1:
            back = self.font.render('Back', True, (120,120,120))
        else:
            back = self.font.render('Back', True, (50,50,50))

        self.screen.blit(upgrades_title, (self.SCREEN_SIZE[0]/8, (self.SCREEN_SIZE[1]/8)))
        self.screen.blit(current_upgrade,(self.SCREEN_SIZE[0]/8, (self.SCREEN_SIZE[1]/8*1.5)))
        self.screen.blit(coins,(self.SCREEN_SIZE[0]/8*5.2,(self.SCREEN_SIZE[1]/8*1.14) ))
        self.screen.blit(current_bullet_damage,(self.SCREEN_SIZE[0]/8,(self.SCREEN_SIZE[1]/8)*2.5 ))
        self.screen.blit(upgraded_bullet_damage,(self.SCREEN_SIZE[0]/8,(self.SCREEN_SIZE[1]/8)*3.25 ))
        self.screen.blit(bullet_damage_increment,(self.SCREEN_SIZE[0]/8*3,(self.SCREEN_SIZE[1]/8)*3.25 ))
        self.screen.blit(cost,(self.SCREEN_SIZE[0]/8,(self.SCREEN_SIZE[1]/8)*4 ))
        self.screen.blit(upgrade,(self.SCREEN_SIZE[0]/8,(self.SCREEN_SIZE[1]/8)*6 ))
        self.screen.blit(back,(self.SCREEN_SIZE[0]/8*5,(self.SCREEN_SIZE[1]/8)*6 ))
        self.screen.blit(bullet_damage,(self.SCREEN_SIZE[0]/8*3,(self.SCREEN_SIZE[1]/8*2.5)))
        self.screen.blit(price,(self.SCREEN_SIZE[0]/8*3,(self.SCREEN_SIZE[1]/8*4)))
        self.screen.blit(current_coins,(self.SCREEN_SIZE[0]/8*6.5,(self.SCREEN_SIZE[1]/8*1.14) ))

    def draw_bullet_amount_screen(self):
        upgrades_title = self.font.render('Upgrades', True, (120,120,120))
        current_upgrade = self.font_upgrades.render('Bullet amount', True, (100,100,100))
        coins = self.font_upgrades.render('Coins:', True ,(255,180,40))
        current_bullet_amount = self.font_upgrades.render('Current:', True ,(120,120,120))
        upgraded_bullet_amount = self.font_upgrades.render('Upgrade:', True ,(20,148,20))
        bullet_amount_increment = self.font_upgrades.render('+1', True ,(20,148,20))
        cost = self.font_upgrades.render('Cost:', True ,(255,180,40))
        bullet_amount = self.font_upgrades.render(JsonLoader.get_bullet_amount(JsonLoader),True,(120,120,120))
        Price = self.font_upgrades.render(Upgrades.get_price_bullet_amount(Upgrades,JsonLoader.get_bullet_amount(JsonLoader)), True,(255,180,40))
        current_coins = self.font_upgrades.render(JsonLoader.get_coins(JsonLoader),True,(255,180,40))

        if self.select_current_upgrade == 0:
            upgrade = self.font.render('Upgrade', True, (20,148,20))
        else:
            upgrade = self.font.render('Upgrade', True, (50,50,50))

        if self.select_current_upgrade == 1:
            back = self.font.render('Back', True, (120,120,120))
        else:
            back = self.font.render('Back', True, (50,50,50))

        self.screen.blit(upgrades_title, (self.SCREEN_SIZE[0]/8, (self.SCREEN_SIZE[1]/8)))
        self.screen.blit(current_upgrade,(self.SCREEN_SIZE[0]/8, (self.SCREEN_SIZE[1]/8*1.5)))
        self.screen.blit(coins,(self.SCREEN_SIZE[0]/8*5.2,(self.SCREEN_SIZE[1]/8*1.14) ))
        self.screen.blit(current_bullet_amount,(self.SCREEN_SIZE[0]/8,(self.SCREEN_SIZE[1]/8)*2.5 ))
        self.screen.blit(upgraded_bullet_amount,(self.SCREEN_SIZE[0]/8,(self.SCREEN_SIZE[1]/8)*3.25 ))
        self.screen.blit(bullet_amount_increment,(self.SCREEN_SIZE[0]/8*3,(self.SCREEN_SIZE[1]/8)*3.25 ))
        self.screen.blit(cost,(self.SCREEN_SIZE[0]/8,(self.SCREEN_SIZE[1]/8)*4 ))
        self.screen.blit(upgrade,(self.SCREEN_SIZE[0]/8,(self.SCREEN_SIZE[1]/8)*6 ))
        self.screen.blit(back,(self.SCREEN_SIZE[0]/8*5,(self.SCREEN_SIZE[1]/8)*6 ))
        self.screen.blit(bullet_amount,(self.SCREEN_SIZE[0]/8*3,(self.SCREEN_SIZE[1]/8*2.5)))
        self.screen.blit(Price,(self.SCREEN_SIZE[0]/8*3,(self.SCREEN_SIZE[1]/8*4)))
        self.screen.blit(current_coins,(self.SCREEN_SIZE[0]/8*6.5,(self.SCREEN_SIZE[1]/8*1.14) ))

    def draw_bullet_fire_speed_screen(self):
        upgrades_title = self.font.render('Upgrades', True, (120,120,120))
        current_upgrade = self.font_upgrades.render('Fire speed', True, (100,100,100))
        coins = self.font_upgrades.render('Coins:', True ,(255,180,40))
        current_bullet_fire_speed = self.font_upgrades.render('Current:', True ,(120,120,120))
        upgraded_bullet_fire_speed = self.font_upgrades.render('Upgrade:', True ,(20,148,20))
        bullet_fire_speed_increment = self.font_upgrades.render('+1', True ,(20,148,20))
        cost = self.font_upgrades.render('Cost:', True ,(255,180,40))
        fire_speed = self.font_upgrades.render(JsonLoader.get_fire_speed(JsonLoader),True,(120,120,120))
        Price = self.font_upgrades.render(Upgrades.get_price_fire_speed(Upgrades,JsonLoader.get_fire_speed(JsonLoader)), True,(255,180,40))
        current_coins = self.font_upgrades.render(JsonLoader.get_coins(JsonLoader),True,(255,180,40))

        if self.select_current_upgrade == 0:
            upgrade = self.font.render('Upgrade', True, (20,148,20))
        else:
            upgrade = self.font.render('Upgrade', True, (50,50,50))

        if self.select_current_upgrade == 1:
            back = self.font.render('Back', True, (120,120,120))
        else:
            back = self.font.render('Back', True, (50,50,50))

        self.screen.blit(upgrades_title, (self.SCREEN_SIZE[0]/8, (self.SCREEN_SIZE[1]/8)))
        self.screen.blit(current_upgrade,(self.SCREEN_SIZE[0]/8, (self.SCREEN_SIZE[1]/8*1.5)))
        self.screen.blit(coins,(self.SCREEN_SIZE[0]/8*5.2,(self.SCREEN_SIZE[1]/8*1.14) ))
        self.screen.blit(current_bullet_fire_speed,(self.SCREEN_SIZE[0]/8,(self.SCREEN_SIZE[1]/8)*2.5 ))
        self.screen.blit(upgraded_bullet_fire_speed,(self.SCREEN_SIZE[0]/8,(self.SCREEN_SIZE[1]/8)*3.25 ))
        self.screen.blit(bullet_fire_speed_increment,(self.SCREEN_SIZE[0]/8*3,(self.SCREEN_SIZE[1]/8)*3.25 ))
        self.screen.blit(cost,(self.SCREEN_SIZE[0]/8,(self.SCREEN_SIZE[1]/8)*4 ))
        self.screen.blit(upgrade,(self.SCREEN_SIZE[0]/8,(self.SCREEN_SIZE[1]/8)*6 ))
        self.screen.blit(back,(self.SCREEN_SIZE[0]/8*5,(self.SCREEN_SIZE[1]/8)*6 ))
        self.screen.blit(fire_speed,(self.SCREEN_SIZE[0]/8*3,(self.SCREEN_SIZE[1]/8*2.5)))
        self.screen.blit(Price,(self.SCREEN_SIZE[0]/8*3,(self.SCREEN_SIZE[1]/8*4)))
        self.screen.blit(current_coins,(self.SCREEN_SIZE[0]/8*6.5,(self.SCREEN_SIZE[1]/8*1.14) ))

    def draw_shield_screen(self):
        upgrades_title = self.font.render('Upgrades', True, (120,120,120))
        current_upgrade = self.font_upgrades.render('Shield', True, (100,100,100))
        coins = self.font_upgrades.render('Coins:', True ,(255,180,40))
        current_shield = self.font_upgrades.render('Current:', True ,(120,120,120))
        upgraded_shield = self.font_upgrades.render('Upgrade:', True ,(20,148,20))
        shield_increment = self.font_upgrades.render('+0.2 s', True ,(20,148,20))
        cost = self.font_upgrades.render('Cost:', True ,(255,180,40))
        shield = self.font_upgrades.render(JsonLoader.get_shield(JsonLoader),True,(120,120,120))
        Price = self.font_upgrades.render(Upgrades.get_price_shield(Upgrades,JsonLoader.get_shield(JsonLoader)), True,(255,180,40))
        current_coins = self.font_upgrades.render(JsonLoader.get_coins(JsonLoader),True,(255,180,40))

        if self.select_current_upgrade == 0:
            upgrade = self.font.render('Upgrade', True, (20,148,20))
        else:
            upgrade = self.font.render('Upgrade', True, (50,50,50))

        if self.select_current_upgrade == 1:
            back = self.font.render('Back', True, (120,120,120))
        else:
            back = self.font.render('Back', True, (50,50,50))

        self.screen.blit(upgrades_title, (self.SCREEN_SIZE[0]/8, (self.SCREEN_SIZE[1]/8)))
        self.screen.blit(current_upgrade,(self.SCREEN_SIZE[0]/8, (self.SCREEN_SIZE[1]/8*1.5)))
        self.screen.blit(coins,(self.SCREEN_SIZE[0]/8*5.2,(self.SCREEN_SIZE[1]/8*1.14) ))
        self.screen.blit(current_shield,(self.SCREEN_SIZE[0]/8,(self.SCREEN_SIZE[1]/8)*2.5 ))
        self.screen.blit(upgraded_shield,(self.SCREEN_SIZE[0]/8,(self.SCREEN_SIZE[1]/8)*3.25 ))
        self.screen.blit(shield_increment,(self.SCREEN_SIZE[0]/8*3,(self.SCREEN_SIZE[1]/8)*3.25 ))
        self.screen.blit(cost,(self.SCREEN_SIZE[0]/8,(self.SCREEN_SIZE[1]/8)*4 ))
        self.screen.blit(upgrade,(self.SCREEN_SIZE[0]/8,(self.SCREEN_SIZE[1]/8)*6 ))
        self.screen.blit(back,(self.SCREEN_SIZE[0]/8*5,(self.SCREEN_SIZE[1]/8)*6 ))
        self.screen.blit(shield,(self.SCREEN_SIZE[0]/8*3,(self.SCREEN_SIZE[1]/8*2.5)))
        self.screen.blit(Price,(self.SCREEN_SIZE[0]/8*3,(self.SCREEN_SIZE[1]/8*4)))
        self.screen.blit(current_coins,(self.SCREEN_SIZE[0]/8*6.5,(self.SCREEN_SIZE[1]/8*1.14) ))



    ## Draw menu, options, or upgrade menu ##
    def draw_menu(self):
        self.screen.fill((0,0,0))
        

        ## Drawing Menu
        if self.front_screen:
            self.draw_front_screen()
            

        
        ### Drawing Options ###
        elif self.options_on:
            self.draw_options_screen()

        ## Drawing Upgrades ##
        elif self.upgrades_on:
            self.draw_upgrades_screen()
        
        ## Drawing Bullet_damage_screen ##
        elif self.bullet_damage_on:
            self.draw_bullet_damage_screen()

        elif self.bullet_amount_on:
            self.draw_bullet_amount_screen()

        elif self.bullet_fire_speed_on:
            self.draw_bullet_fire_speed_screen()

        elif self.shield_on:
            self.draw_shield_screen()
            
            
    
    

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
                        self.front_screen = False
                        self.upgrades_on = True

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




                ## Decrement volume of music and sounds ##
                if event.key == pygame.K_LEFT:

                    ## For controlling the volume of the music
                    if self.select_options == 0:
                        self.volume_music_int -= self.volume_incrementer
                        if self.volume_music_int < 0:
                            self.volume_music_int = 0

                        JsonLoader.updateJsonFile(JsonLoader,'music-')
                        Soundplayer.change_volume_music(Soundplayer(), int(JsonLoader.get_music(JsonLoader)))

                    ## For the sounds
                    if self.select_options == 1:
                        self.volume_sounds_int -= self.volume_incrementer
                        if self.volume_sounds_int < 0:
                            self.volume_sounds_int = 0

                        JsonLoader.updateJsonFile(JsonLoader, 'sounds-')
                        Soundplayer.change_volume_sounds(Soundplayer(), int(JsonLoader.get_sounds(JsonLoader)))


                ## Increment the volume of the music ##
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


                        JsonLoader.updateJsonFile(JsonLoader,'sounds+')
                        Soundplayer.change_volume_sounds(Soundplayer(), int(JsonLoader.get_sounds(JsonLoader)))

        elif self.upgrades_on:

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    self.select_upgrades += 1 
                if event.key == pygame.K_UP:
                    self.select_upgrades -= 1
                
                if self.select_upgrades > 4:
                    self.select_upgrades = 0
                
                if self.select_upgrades < 0:
                    self.select_upgrades = 4
                
                if event.key == pygame.K_RETURN:
                    if self.select_upgrades == 0:
                        
                        self.upgrades_on = False
                        self.bullet_damage_on = True
                    if self.select_upgrades == 1:
                        
                        self.upgrades_on = False
                        self.bullet_amount_on = True
                    if self.select_upgrades == 2:
                        
                        self.upgrades_on = False
                        self.bullet_fire_speed_on = True
                    if self.select_upgrades == 3:
                        
                        self.upgrades_on = False
                        self.shield_on = True
                    if self.select_upgrades == 4:
                        self.upgrades_on = False
                        self.front_screen = True
        
        elif self.bullet_damage_on:
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.select_current_upgrade += 1
                if event.key == pygame.K_LEFT:
                    self.select_current_upgrade -= 1

                if self.select_current_upgrade > 1:
                    self.select_current_upgrade = 0
                
                if self.select_current_upgrade < 0:
                    self.select_current_upgrade = 1
                
                if event.key == pygame.K_RETURN:
                    if self.select_current_upgrade == 0:
                        print('nu plz')
                        Upgrades.check_upgrade_bullet_damage(Upgrades)
                    if self.select_current_upgrade == 1:
                        self.bullet_damage_on = False
                        self.upgrades_on = True
        
        elif self.bullet_amount_on:
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.select_current_upgrade += 1
                if event.key == pygame.K_LEFT:
                    self.select_current_upgrade -= 1

                if self.select_current_upgrade > 1:
                    self.select_current_upgrade = 0
                
                if self.select_current_upgrade < 0:
                    self.select_current_upgrade = 1
                
                if event.key == pygame.K_RETURN:
                    if self.select_current_upgrade == 0:
                        print("i upgrade :)")
                    if self.select_current_upgrade == 1:
                        self.bullet_amount_on = False
                        self.upgrades_on = True
            
        elif self.bullet_fire_speed_on:
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.select_current_upgrade += 1
                if event.key == pygame.K_LEFT:
                    self.select_current_upgrade -= 1

                if self.select_current_upgrade > 1:
                    self.select_current_upgrade = 0
                
                if self.select_current_upgrade < 0:
                    self.select_current_upgrade = 1
                
                if event.key == pygame.K_RETURN:
                    if self.select_current_upgrade == 0:
                        print("i upgrade :)")
                    if self.select_current_upgrade == 1:
                        self.bullet_fire_speed_on = False
                        self.upgrades_on = True

        elif self.shield_on:
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.select_current_upgrade += 1
                if event.key == pygame.K_LEFT:
                    self.select_current_upgrade -= 1

                if self.select_current_upgrade > 1:
                    self.select_current_upgrade = 0
                
                if self.select_current_upgrade < 0:
                    self.select_current_upgrade = 1
                
                if event.key == pygame.K_RETURN:
                    if self.select_current_upgrade == 0:
                        print("i upgrade :)")
                    if self.select_current_upgrade == 1:
                        self.shield_on = False
                        self.upgrades_on = True

        
            


                  

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