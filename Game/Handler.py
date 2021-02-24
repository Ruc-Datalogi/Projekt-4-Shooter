from Player import Player
from EnemyBullet import EnemyBullet
from Enemy import Enemy

class Handler:

    enemy_list = []
    enemy_bullet_list = []

    def __init__(self, screen):
        self.screen = screen
        self.p1 = Player(self.screen)
        self.enemy_list = []
        self.enemy_bullet_list = []
        #for i in range (-4, 4):
            #for j in range (0, 10):
        self.enemy_list.append(Enemy (100,100,2))



    def draw(self):
        self.p1.playerDraw(self.screen)
        for i in range (0, len(self.enemy_list)):
            self.enemy_list[i].enemyDraw(self.screen)




            
            
            

            
    def update(self):
        self.p1.player_input()
        self.p1.playerMove()

        for i in range(len(self.enemy_list)):
                self.enemy_list[i].enemyMove()
                self.p1.bulletCollision(self.enemy_list[i])
            
        for i in range(len(self.enemy_list)):
            if self.enemy_list[i].getEnemyHealth <= 0:
                self.enemy_list.pop(i)
                break
