import sys, pygame, random
from Friendly_Bullet import Friendly_Bullet
from Enemy import Enemy

class Player:

    ## Constructor for player ## 
    def __init__(self, screen):
        self.img = pygame.image.load("Game/sprites/playerLV1.png")
        self.player_x = 100 
        self.player_y = 100
        self.player_speed_x = 0
        self.player_speed_y = 0
        self.general_speed = 3.5
        self.moving = False
        self.screen = screen
        self.bullet_list = []
        self.timer = 0
        #player health
        self.playerHealth = 100
        self.healthBar = 100
        self.maxplayerHealth = 300
        #self.healthRatio = self.maxplayerHealth / self.healthBar

    def get_dmg (self, amount):
        if self.playerHealth > 0:
            self.playerHealth -= amount
        if self.playerHealth <= 0:
            self.playerHealth = 0
    
    def get_health (self, amount):
        if self.playerHealth < self.maxplayerHealth:
            self.playerHealth += amount
        if self.playerHealth >= self.maxplayerHealth:
            self.playerHealth = self.maxplayerHealth

    def healthRect (self, screen):
        pass
        #(screen, (255, 0, 0), (10,10,self.playerHealth / self.healthRatio,25))


    ## Draw player and bullets at given pos ##
    ## Drawing two rectangles, a green and a dark blue bar.
    ## The Green bar represents our health and the dark blue bar has the same value but doesn't change
    ## This makes it easier to see how much health our character has lost and how much it has left
    def playerDraw(self , screen):        
        screen.blit(self.img,(self.player_x,self.player_y))
        pygame.draw.rect(screen,(68,77,85), pygame.Rect(20, 420, 260, 10))
        
    ## Health bar with 3 different colors.
    ## Green healthbar, if self.healthbar is greater than 50: 
    ## Yellow healthbar, if self.healthbar is greater than 25 and less than 50:
    ## Orange healthbar, if self.healthbar is greater than 0 and less than 25:
        if self.playerHealth > 50:
            pygame.draw.rect(screen,(90,186,74), pygame.Rect(20, 420, (self.playerHealth/self.healthBar)*260, 10))
        elif self.playerHealth > 25 and self.playerHealth < 50:
            pygame.draw.rect(screen,(247,204,59), pygame.Rect(20, 420, (self.playerHealth/self.healthBar)*260, 10))
        elif self.playerHealth > 0 and self.playerHealth < 25:
            pygame.draw.rect(screen,(250,115,54), pygame.Rect(20, 420, (self.playerHealth/self.healthBar)*260, 10))


        


        for i in range(len(self.bullet_list)):
            self.bullet_list[i].bulletMove()
            self.bullet_list[i].bulletDraw(screen)
        
    ## check bullet collision and damage enemy
    def bulletCollision(self, enemy):
        for i in range(len(self.bullet_list)):
            if self.bullet_list[i].getBulletRect.colliderect(enemy.getEnemyRect):
                print(enemy.getEnemyRect)
                enemy.setHealth(-10)
                self.bullet_list.pop(i)
                break

        ## remove bullets
        for i in range(len(self.bullet_list)):
            if self.bullet_list[i].getBulletY < -100:
                self.bullet_list.pop(i)
                break

    ## Character move and game boundaries ##
    def playerMove(self):
        self.player_x += self.player_speed_x
        self.player_y += self.player_speed_y

        if self.player_x <= 0:
            self.player_x = 0
        if self.player_x >= 400 - 14:
            self.player_x = 400 - 14
        if self.player_y <= 0: 
            self.player_y = 0
        if self.player_y >= 540:
            self.player_y = 540

        self.playerHealth -= 0.25
        if self.playerHealth <= 1:
            self.playerHealth = 100
            
    ## Get keypressed and use it for movement ##
    def player_input(self):
        self.player_speed_x = 0
        self.player_speed_y = 0
        keystate = pygame.key.get_pressed()

        if keystate[pygame.K_LEFT]:
            self.player_speed_x -= self.general_speed

        if keystate[pygame.K_RIGHT]:
            self.player_speed_x = self.general_speed

        if keystate[pygame.K_UP]:
            self.player_speed_y -= self.general_speed

        if keystate[pygame.K_DOWN]:
            self.player_speed_y = self.general_speed
            
        if self.timer > 10 and keystate[pygame.K_SPACE]:
            self.timer = 0
            self.bullet_list.append(Friendly_Bullet(self.player_x + 2, self.player_y - 10))
            self.bullet_list.append(Friendly_Bullet(self.player_x + 10, self.player_y - 10))
            self.bullet_list.append(Friendly_Bullet(self.player_x + -6, self.player_y - 10))
        
        if keystate[pygame.K_ESCAPE]:
            sys.exit()

        self.timer +=1

                