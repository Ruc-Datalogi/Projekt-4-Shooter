import sys, pygame, random
from Player import Player
from Enemy import Enemy
from Menu import Menu
pygame.init()

# Constant variables
SCREEN_SIZE = (600,880)
DISPLAY_SIZE = (300,440)
DARK_GREY = (50,50,50)
menu = Menu()
RUNNING = True
FPS = 60 
fpsClock = pygame.time.Clock()
#The real screen
screen = pygame.display.set_mode(SCREEN_SIZE)
#To cast to 
display = pygame.Surface((DISPLAY_SIZE))

# Title and Icon
pygame.display.set_caption("Space Hero")
icon = pygame.image.load('Game/sprites/playerLV1.png')
pygame.display.set_icon(icon)

# player
p1 = Player(screen)
enemyList = []
enemyList.append(Enemy (10,10,1))
enemyList.append(Enemy (20,10,1))
enemyList.append(Enemy (30,10,0))
enemyList.append(Enemy (40,10,0))
enemyList.append(Enemy (50,10,0))


# Enemy



while RUNNING:
    #Menu
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
    #game loop
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                RUNNING = False
            
        menu.drawBackgroundScrolling(display,DISPLAY_SIZE)

        p1.update()
        p1.playerDraw(display)
        p1.playerMove()

        for i in range(len(enemyList)):
            enemyList[i].enemyMove()
            enemyList[i].enemyDraw(display)
            p1.bulletCollision(enemyList[i])
        
        for i in range(len(enemyList)):
            print(enemyList[i].getEnemyHealth)
            if enemyList[i].getEnemyHealth <= 0:
                enemyList.pop(i)
            break


        

        surf = pygame.transform.scale(display, SCREEN_SIZE)
        screen.blit(surf, (0,0 ))
        pygame.display.update()
        fpsClock.tick(FPS)



pygame.quit()