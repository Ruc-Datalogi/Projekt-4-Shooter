
from EnemyBullet import EnemyBullet
from GameObject import *
from Mediator import *
from Spritesheet import *


class Boss(GameObject):

    ## Choose enemy sprite ##
    def __init__(self, xpos, ypos, ID, object_ID, mediator, screen):
        
        self.ss = Spritesheet('Game/sprites/SpaceShipAsset.png')
        self.ss2 = Spritesheet('Game/sprites/bullets/allTheBullets.png')
        self.img = self.ss.image_at(pygame.Rect(4, 56, 45, 22))
        self.img = pygame.transform.scale(self.img,(90,44))
        self.img_bullet_blue = self.ss2.image_at(pygame.Rect(111, 108, 11, 36))

        self.boss_xpos = xpos
        self.boss_ypos = ypos
        self.boss_x_speed = 0.2
        self.boss_y_speed = 0
        self.boss_health = 100
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

        if self.timer > 5:
            self.timer = 0
            self.mediator.all_game_objects.append(EnemyBullet(self.boss_xpos + 6, self.boss_ypos + 22, 6, False, self.img_bullet_blue, 'e_bullet', self.mediator, self.screen))
            self.mediator.all_game_objects.append(EnemyBullet(self.boss_xpos + 70, self.boss_ypos + 22, 6, False, self.img_bullet_blue, 'e_bullet', self.mediator, self.screen))

    
    def loop(self):
        self.boss_move()

        if self.collision('f_bullet',self.boss_rect) and self.boss_damage_cooldown > 6:
           
            

            self.boss_health -= 10
        
        if self.boss_health < 0:
            self.mediator.to_be_removed.append(self)

    def draw(self):
        self.boss_draw()
            
