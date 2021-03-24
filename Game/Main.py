import sys, pygame, random
from Player import *
from Enemy import *
from Menu import *
from Mediator import *
from HUD import *
from Generator import *
from Soundplayer import *
pygame.init()

# Constant variables
SCREEN_SIZE = (600,800)
DISPLAY_SIZE = (300,400)
DARK_GREY = (50,50,50)
menu = Menu()
mediator = Mediator()
RUNNING = True
FPS = 60 
timer = 0


fpsClock = pygame.time.Clock ()
#The real screen
screen = pygame.display.set_mode(SCREEN_SIZE)
#To cast to 
display = pygame.Surface((DISPLAY_SIZE))
player = Player(display,mediator,'player')
generator = Generator(display, mediator)


Soundplayer.load_music(Soundplayer())
Soundplayer.play_music(Soundplayer())

hud = HUD(display, player, DISPLAY_SIZE, mediator, generator)

# Title and Icon
pygame.display.set_caption("The Falcon")
icon = pygame.image.load(menu.resource_path('Game/sprites/playerLV1.png'))
pygame.display.set_icon(icon)







while RUNNING:
    
    ## Draw Menu ##
    if menu.get_menu: 
        menu.draw_background(display,(DISPLAY_SIZE))
        menu.draw_menu(display, (DISPLAY_SIZE))
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                RUNNING = False
                pygame.quit()
                sys.exit()
            menu.menu_input(event)
        if not menu.get_menu:
            mediator.all_game_objects.append(player)

        surf = pygame.transform.scale(display, SCREEN_SIZE)             
        screen.blit(surf, (0,0))
        pygame.display.update()
    else:
    ## Game loop ##
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                RUNNING = False
            
            
        menu.draw_background_scrolling(display,DISPLAY_SIZE)
        
        for object in mediator.all_game_objects:
            object.loop()
            object.draw()


        generator.generate()

        mediator.all_game_objects = [i for i in mediator.all_game_objects if i not in mediator.to_be_removed]
        hud.draw_HUD()


        mediator.to_be_removed.clear()

        ## Check if player is dead or game is completed
        if player.player_dead() or generator.get_game_complete():
            generator = Generator(display, mediator)
            hud = HUD(display, player, DISPLAY_SIZE, mediator, generator)
            mediator.all_game_objects.clear()
            menu.player_dead()

        surf = pygame.transform.scale(display, SCREEN_SIZE)
        screen.blit(surf, (0,0))
        pygame.display.update()
        fpsClock.tick(FPS)



pygame.quit()