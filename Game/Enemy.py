import sys, pygame, random

class Enemy:

    ## Choose enemy sprite ##
    def __init__(self, enemyXPos, enemyYPos, enemyID):
        self.img = pygame.image.load("Game/sprites/enemy1.png")
        if enemyID == 0: 
            self.img = pygame.image.load("Game/sprites/enemy1.png")
        if enemyID == 1:
            self.img = pygame.image.load("Game/sprites/enemy2.png")
        if enemyID == 2:
            self.img = pygame.image.load("Game/sprites/enemy3.png")
        self.enemy_bullet_cooldown = random.randint(40,60)
        self.enemy_timer = 0
        
        self.enemyX = enemyXPos 
        self.enemyY = enemyYPos
        self.enemySpeedX = 1.5
        self.enemySpeedY = 0
        self.enemyHealth = 2 
        self.enemy_bullet_list = []
        self.enemyRect = self.img.get_rect()
    
        

    @property
    def getEnemyRect(self):
        return self.enemyRect
    

    ## Damage the enemy
    def setHealth(self, x):
        print(self.enemyHealth)
        self.enemyHealth += x

    @property
    def getEnemyHealth(self):
        return self.enemyHealth

    def enemyDraw(self, screen):
        screen.blit(self.img, (self.enemyX, self.enemyY))



    ##Make sure the enemy stays in the screen
    def enemyMove(self):
        self.enemy_timer += 1
        self.enemyX += self.enemySpeedX
        if self.enemyX >= 300 or self.enemyX <= 0:
            self.enemySpeedX *= -1
            self.enemyY += 20
        self.enemyRect = self.img.get_rect(x=self.enemyX, y=self.enemyY)
        if self.enemy_timer > self.enemy_bullet_cooldown:
            self.enemy_bullet_list(EnemyBullet (self.enemyX,self.enemyY))
            
