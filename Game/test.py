import sys, pygame, random  
pygame.init()

# Constant variables
SCREEN_SIZE = (600,800)
DARK_GREY = (50,50,50)
RUNNING = True
FPS = 60 
fpsClock = pygame.time.Clock()
# Init

screen = pygame.display.set_mode(SCREEN_SIZE)

# Title and Icon
pygame.display.set_caption("Martins Test")
icon = pygame.image.load('sprites/playerLV1.png')
pygame.display.set_icon(icon)

# player
playerImg = pygame.image.load("sprites/playerLV1.png")
playerX = 300 
playerY = 600
playerSpeedX = 0
playerSpeedY = 0
generalSpeed = 3.5

# Enemy
enemyImg = pygame.image.load("sprites/enemy1.png")
enemyX = 100 
enemyY = 100
enemySpeedX = 1.5
enemySpeedY = 0


# Background
backGroundImg = pygame.image.load("sprites/background/preview.png")

def drawBackground():   
    width = backGroundImg.get_width()
    height = backGroundImg.get_height()
    for i in range(0, int(600/width)+1):
        for j in range(0, int(800/height +1)):
            screen.blit(backGroundImg, (i*width, j*height))
    width = backGroundImg.get_width()
    height = backGroundImg.get_height()


def player(xPos,yPos):
    screen.blit(playerImg, (xPos, yPos))

def enemy(xPos,yPos):
    screen.blit(enemyImg, (xPos,yPos))
            

while RUNNING:
    drawBackground()
    #game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT: RUNNING = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT: 
                playerSpeedX = -generalSpeed
            if event.key == pygame.K_RIGHT: 
                playerSpeedX = generalSpeed
            if event.key == pygame.K_UP:
                playerSpeedY = -generalSpeed
            if event.key == pygame.K_DOWN:
                playerSpeedY = generalSpeed
            if event.key == pygame.K_ESCAPE:
                sys.exit()
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT: 
                playerSpeedX = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerSpeedY = 0

    
    #Enemy
    enemyX += enemySpeedX

    if enemyX >= 576 or enemyX <= 24:
        enemySpeedX *= -1
        enemyY += 50
    

    #Pos
    playerX += playerSpeedX
    playerY += playerSpeedY
    #Boundraies
    if playerX <= 0:
        playerX = 0
    if playerX >= 584:
        playerX = 584
    if playerY <= 0: 
        playerY = 0
    if playerY >= 784: 
        playerY = 784
    
    player(playerX, playerY)
    enemy(enemyX,enemyY)
    pygame.display.update()
    fpsClock.tick(FPS)


pygame.quit()