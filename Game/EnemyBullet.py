import sys, pygame, random



class EnemyBullet:
    
    def __init__(self, xPos, yPos):
        self.img = pygame.image.load("Game/sprites/bullets/enemy_bullets/green_bullet.png")
        self.enemy_bulletX = xPos 
        self.enemy_bulletY = yPos 
        self.enemy_bulletSpeedX = 0
        self.enemy_bulletSpeedY = 12
        self.enemy_bulletRect = self.img.get_rect()
        self.enemy_bulletDamage = 10
    
    ## For collision ##
    @property
    def getBulletRect(self):
        return self.enemy_bulletRect
    
    ## For damaging enemy ##
    @property
    def getBulletDamage(self):
        return self.enemy_bulletDamage

    ## For removing the bullet ##
    @property  
    def getBulletY(self):
        return self.enemy_bulletY

    ## Draw at specific location ##
    def bulletDraw(self , screen):        
        screen.blit(self.img,(self.enemy_bulletX,self.enemy_bulletY))

    ## Update bullet pos and the rect ##
    def bulletMove(self):
        self.enemy_bulletX += self.enemy_bulletSpeedX
        self.enemy_bulletY += self.enemy_bulletSpeedY
        self.enemy_bulletRect = self.img.get_rect(x=self.enemy_bulletX, y=self.enemy_bulletY)
    