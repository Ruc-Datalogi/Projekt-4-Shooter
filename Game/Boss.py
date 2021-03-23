
from EnemyBullet import EnemyBullet
from GameObject import *
from Mediator import *
from Spritesheet import *
import random

class Boss(GameObject):

    ## Choose enemy sprite ##
    def __init__(self, xpos, ypos, ID, object_ID, mediator, screen):
        
        self.ss = Spritesheet('Game/sprites/SpaceShipAsset.png')
        self.ss2 = Spritesheet('Game/sprites/bullets/allTheBullets.png')
        self.img = self.ss.image_at(pygame.Rect(4, 56, 45, 22))
        self.img = pygame.transform.scale(self.img,(90,44))
        self.img_bullet_blue_rect = self.ss2.image_at(pygame.Rect(111, 108, 11, 36))
        self.img_bullet_red = self.ss2.image_at(pygame.Rect(27,106,17,16))

        self.boss_xpos = xpos
        self.boss_ypos = ypos
        self.boss_x_speed = 0.2
        self.boss_y_speed = 0
        
        self.boss_health = 2000
        self.boss_health_max = self.boss_health

        self.boss_rect = pygame.Rect(0,0,0,0)
        
        self.boss_damage_cooldown = 0
        self.bullet_counter = 60
        self.timer = 0

        self.boss_id = ID
        self.object_ID = object_ID
        self.mediator = mediator
        self.screen = screen
        
    
        

    def get_rect(self):
        return self.enemy_rect
    

    ## Damage the enemy

    def get_enemy_health(self):
        return self.enemy_health

    def boss_draw(self):
        self.screen.blit(self.img, (self.boss_xpos, self.boss_ypos))

            
    ##Make sure the enemy stays in the screen
    def boss_move(self):
        self.timer += 1
        self.boss_damage_cooldown += 1

        self.boss_xpos += self.boss_x_speed

        if self.boss_xpos + self.img.get_width() > self.screen.get_width():
            self.boss_x_speed *= -1
        if self.boss_xpos < 0:
            self.boss_x_speed *=-1

        self.boss_rect = pygame.Rect(self.boss_xpos,self.boss_ypos,self.img.get_width(),self.img.get_height())

        if self.boss_health > 1400:
            if self.timer > 10:
                self.timer = 0
                self.boss_bullet_pattern_1()

        elif self.boss_health > 900:
            if self.timer > 40:
                self.timer = 0
                self.boss_bullet_pattern_2()

            

    
    def loop(self):

        self.boss_move()

        if self.collision('f_bullet',self.boss_rect) and self.boss_damage_cooldown > 6:
           
            self.boss_health -= 10
        
        if self.boss_health < 0:

            self.mediator.to_be_removed.append(self)

    def draw(self):
        self.draw_boss_rect()
        self.boss_draw()


    ## Shower of bullets ##
    def boss_bullet_pattern_1(self):

        self.mediator.all_game_objects.append(EnemyBullet(self.boss_xpos + 6, self.boss_ypos + 26, 0,6, False, self.img_bullet_blue_rect, 'e_bullet', self.mediator, self.screen))
        self.mediator.all_game_objects.append(EnemyBullet(self.boss_xpos + 70, self.boss_ypos + 26, 0,6, False, self.img_bullet_blue_rect, 'e_bullet', self.mediator, self.screen))


    ## Burst of bullets ##
    def boss_bullet_pattern_2(self):
        bullet_list = [i for i in range(-8,8)]
        random_number = random.randint(4,len(bullet_list)-6)
        bullet_list[random_number] = -200
        bullet_list[random_number-1] = -200
        bullet_list[random_number+1] = -200

        print(bullet_list)

        for i in bullet_list:
            if i == -200:
                pass
            else:
                self.mediator.all_game_objects.append(EnemyBullet(self.boss_xpos + 45, self.boss_ypos + 26, (i*0.4) , 3.5, True, self.img_bullet_red, 'e_bullet', self.mediator, self.screen))



    def boss_bullet_pattern_3(self, timer):
        pass
            
    def draw_boss_rect(self):
        pygame.draw.rect(self.screen, (90,90,90), (pygame.Rect(40, 30, 240, 8)))
        pygame.draw.rect(self.screen, (220,20,60), (pygame.Rect(40, 30, 240*(self.boss_health/self.boss_health_max), 8)))