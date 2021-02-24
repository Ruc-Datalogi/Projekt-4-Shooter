from Player import Player
from EnemyBullet import EnemyBullet
from Enemy import Enemy
from Bullet import Bullet

def __init__(self, screen):
    self.screen = screen
    self.p1 = Player()
    self.enemy_list = []
    self.enemy_bullet_list = []



def handler_draw(self):
    self.p1.playerDraw(self.screen)
    for i in range (len(self.enemy_bullet_list)):
        self.enemy_list[i].enemyDraw(display)




        
        
        

        
def handler_update(self):
    self.p1.player_input()
    self.p1.playerMove()
    for i in range(len(self.enemy_list)):
            self.enemy_list[i].enemyMove()
            self.p1.bulletCollision(self.enemy_list[i])
        
    for i in range(len(self.enemy_list)):
        if self.enemy_list[i].getEnemyHealth <= 0:
            self.enemy_list.pop(i)
            break
