import sys, pygame, random
from Player import Player
from Enemy import Enemy
from Menu import Menu
from Mediator import Mediator

pygame.init()

# Constant variables
SCREEN_SIZE = (300,400)
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

# Title and Icon
pygame.display.set_caption("The Falcon")
icon = pygame.image.load('Game/sprites/playerLV1.png')
pygame.display.set_icon(icon)

mediator.all_game_objects.append(Player (display,mediator,'player'))


# Enemy



while RUNNING:
    ## Draw Menu ##
    if menu.get_menu: 
        menu.drawBackground(display,(DISPLAY_SIZE))
        menu.drawMenu(display, (DISPLAY_SIZE))
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                RUNNING = False
                pygame.quit()
                sys.exit()
            menu.menuInput(event)
        surf = pygame.transform.scale(display, SCREEN_SIZE)
        screen.blit(surf, (0,0))
        pygame.display.update()
    else:
    ## Game loop ##
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                RUNNING = False
            
        menu.drawBackgroundScrolling(display,DISPLAY_SIZE)
        
        for object in mediator.all_game_objects:
            object.loop()
            object.draw()

                   
        mediator.all_game_objects = [i for i in mediator.all_game_objects if i not in mediator.to_be_removed]


        
        surf = pygame.transform.scale(display, SCREEN_SIZE)
        screen.blit(surf, (0,0))
        pygame.display.update()
        fpsClock.tick(FPS)



pygame.quit()