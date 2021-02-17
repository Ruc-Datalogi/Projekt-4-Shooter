import sys, pygame, random
from Player import Player
from Enemy import Enemy
from Menu import Menu
pygame.init()

# Constant variables
SCREEN_SIZE = (800,1080)
DISPLAY_SIZE = (400,540)
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
pygame.display.set_caption("Martins Test")
icon = pygame.image.load('Game/sprites/playerLV1.png')
pygame.display.set_icon(icon)

# player
p1 = Player(screen)

# Enemy
enemy1 = Enemy(100, 200)

    

 
# Background
backGroundImg = pygame.image.load("Game/sprites/background/preview.png")
backGroundImg_1 = pygame.image.load("Game/sprites/background/background_1.png")
backGroundImg_2 = pygame.image.load("Game/sprites/background/background_2.png")
backGroundImg_3 = pygame.image.load("Game/sprites/background/background_3.png")
backGroundImg_4 = pygame.image.load("Game/sprites/background/background_4.png")

def drawBackground(): 
    width = backGroundImg.get_width()
    height = backGroundImg.get_height()
    for i in range(0, int(DISPLAY_SIZE[0]/width)+1):
        for j in range(0, int(DISPLAY_SIZE[1]/height +1)):
            display.blit(backGroundImg,(i*width, j*height))

    width = backGroundImg.get_width()
    height = backGroundImg.get_height()            


while RUNNING:
    #Menu
    if menu.get_menu: 
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
        drawBackground()
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                RUNNING = False
            
        
        p1.update()
        p1.playerDraw(display)
        p1.bulletCollision(enemy1)
        p1.playerMove()
        enemy1.enemyDraw(display)
        enemy1.enemyMove()
        surf = pygame.transform.scale(display, SCREEN_SIZE)
        screen.blit(surf, (0,0 ))
        pygame.display.update()
        fpsClock.tick(FPS)



pygame.quit()