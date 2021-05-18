
from EnemyBullet import EnemyBullet
from GameObject import *
from Mediator import *
from Spritesheet import *
from Soundplayer import *
from Upgrades import *
import random

class Boss(GameObject):

    ## Choose enemy sprite ##
    def __init__(self, xpos, ypos, ID, object_ID,screen, level = 1):
        
        self.ss = Spritesheet(self.resource_path('Game/sprites/SpaceShipAsset.png'))
        self.ss2 = Spritesheet(self.resource_path('Game/sprites/bullets/allTheBullets.png'))
        self.soundplayer = Soundplayer()

        self.img = self.ss.image_at(pygame.Rect(4, 56, 45, 22))
        self.img = pygame.transform.scale(self.img,(90,44))
        self.img_bullet_blue_rect = self.ss2.image_at(pygame.Rect(111, 108, 11, 36))
        self.img_bullet_red = self.ss2.image_at(pygame.Rect(27,106,17,16))
        self.img_bullet_blue = self.ss2.image_at(pygame.Rect(8,129,17,16))

        self.boss_xpos = xpos
        self.boss_ypos = ypos
        self.boss_x_speed = 0
        self.boss_y_speed = 0.5
        self.boss_ready = False
        
        self.boss_health = 2000
        self.boss_health_max = self.boss_health

        self.boss_rect = pygame.Rect(0,0,0,0)
        
        self.boss_damage_cooldown = 0
        self.bullet_counter = 60
        self.timer = 0
        
        ##boss bullet pattern 4, random movement
        self.tp_timer = 0

        self.boss_id = ID
        self.object_ID = object_ID
        self.screen = screen

        self.level = level
        self.update_boss()
        print(self.level)
        self.alive = True

        
    
        

    def get_rect(self):
        return self.boss_rect
    

    ## Damage the enemy

    def get_enemy_health(self):
        return self.enemy_health

    def boss_draw(self):
        self.screen.blit(self.img, (self.boss_xpos, self.boss_ypos))

            
    ##Make sure the enemy stays in the screen
    def boss_move(self):
        self.timer += 1
        self.tp_timer += 1
        self.boss_damage_cooldown += 1

        self.boss_xpos += self.boss_x_speed
        self.boss_ypos += self.boss_y_speed

        if self.boss_ypos > 50 and not self.boss_ready:
            self.boss_ready = True
            self.boss_y_speed = 0
            self.boss_x_speed = 0.2
            if self.level == 2:
                self.boss_x_speed = 0.4
        

        if self.boss_xpos + self.img.get_width() + 2 > self.screen.get_width():
            self.boss_x_speed *= -1
        if self.boss_xpos < 2:
            self.boss_x_speed *=-1

        self.boss_rect = pygame.Rect(self.boss_xpos,self.boss_ypos,self.img.get_width(),self.img.get_height())


        if self.boss_ready and self.level == 1:
            if self.boss_health > 1400:
                if self.timer > 10:
                    self.boss_x_speed = 0.4
                    self.timer = 0
                    self.boss_bullet_pattern_1()

            elif self.boss_health > 900:
                if self.timer > 40:
                    self.boss_x_speed = 0.2
                    self.timer = 0
                    self.boss_bullet_pattern_2()
            else:
                if self.timer > 20:
                    self.timer = 0
                    self.boss_bullet_pattern_3()
        
        elif self.boss_ready and self.level == 2:
            if self.boss_health > 3500:
                if self.timer > 10:
                    self.timer = 0
                    self.boss_bullet_pattern_1()

            elif self.boss_health > 2000:
                if self.timer > 40:
                    self.timer = 0
                    self.boss_bullet_pattern_2()
            else:
                
                if self.timer > 30 and self.tp_timer > 10:
                    self.timer = 0
                    self.boss_bullet_pattern_3()
                if self.tp_timer > 60:
                    self.tp_timer = 0
                    self.tp_boss()

    
    def loop(self):

        self.boss_move()


        if self.boss_ready:
            hit_count = self.collision('f_bullet', self.boss_rect)
            if hit_count >= 1:
                Soundplayer.enemy_hit_sound(Soundplayer())
                self.boss_health -= float(Upgrades.get_level_bullet_damage(Upgrades,JsonLoader.get_bullet_damage(JsonLoader)))*hit_count  
        
        if self.boss_health < 0:

            Mediator.to_be_removed.append(self)

    def draw(self):
        self.draw_boss_rect()
        self.boss_draw()


    ## Shower of bullets ##
    def boss_bullet_pattern_1(self):

        Mediator.all_game_objects.append(EnemyBullet(self.boss_xpos + 6, self.boss_ypos + 26, 0,6, False, self.img_bullet_blue_rect, 'e_bullet', self.screen))
        Mediator.all_game_objects.append(EnemyBullet(self.boss_xpos + 70, self.boss_ypos + 26, 0,6, False, self.img_bullet_blue_rect, 'e_bullet', self.screen))


    ## Burst of bullets with space in ##
    def boss_bullet_pattern_2(self):
        bullet_list = [i for i in range(-8,8)]
        random_number = random.randint(5,len(bullet_list)-7)
        bullet_list[random_number] = -200
        bullet_list[random_number-1] = -200
        bullet_list[random_number+1] = -200


        for i in bullet_list:
            if i == -200:
                pass
            else:
                Mediator.all_game_objects.append(EnemyBullet(self.boss_xpos + 45, self.boss_ypos + 26, (i*0.4)
                , 3.5, True, self.img_bullet_red, 'e_bullet',self.screen))


    ## Blue burst of bullets constant ##
    def boss_bullet_pattern_3(self):
        
        for i in range(-6, 9):
            Mediator.all_game_objects.append(EnemyBullet(self.boss_xpos + 45, self.boss_ypos + 26, (i*0.5) , 3, True, self.img_bullet_blue, 'e_bullet', self.screen))


    ## 
    def boss_bullet_pattern_4(self):
        for i in range(-6, 9):
            Mediator.all_game_objects.append(EnemyBullet(self.boss_xpos + 45, self.boss_ypos + 26, (i*0.5) , 3, True, self.img_bullet_blue, 'e_bullet', self.screen))
        
    def tp_boss(self):
        self.boss_xpos = random.randint(20, self.screen.get_width() - self.img.get_width() - 20)    
       
            
    def draw_boss_rect(self):
        if self.boss_ready:
            pygame.draw.rect(self.screen, (112,128,144), (pygame.Rect(40, 30, 220, 8)))
            pygame.draw.rect(self.screen, (220,20,60), (pygame.Rect(40, 30, 220*(self.boss_health/self.boss_health_max), 8)))

    def update_boss(self):
        if self.level == 2:
            self.boss_health = 5000
            self.boss_health_max = 5000
            
            
            