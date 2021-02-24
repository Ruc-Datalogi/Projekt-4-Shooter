import sys, pygame, random



class EnemyBullet:
    
    def __init__(self, xPos, yPos):
        self.img = pygame.image.load("Game/sprites/bullets/enemy_bullets/green_bullet.png")
        self.bulletX = xPos 
        self.bulletY = yPos 
        self.bulletSpeedX = 0
        self.bulletSpeedY = 12
        self.bulletRect = self.img.get_rect()
        self.bulletDamage = 10
    
    ## For collision ##
    @property
    def getBulletRect(self):
        return self.bulletRect
    
    ## For damaging enemy ##
    @property
    def getBulletDamage(self):
        return self.bulletDamage

    ## For removing the bullet ##
    @property  
    def getBulletY(self):
        return self.bulletY

    ## Draw at specific location ##
    def bulletDraw(self , screen):        
        screen.blit(self.img,(self.bulletX,self.bulletY))

    ## Update bullet pos and the rect ##
    def bulletMove(self):
        self.bulletX -= self.bulletSpeedX
        self.bulletY -= self.bulletSpeedY
        self.bulletRect = self.img.get_rect(x=self.bulletX, y=self.bulletY)
    