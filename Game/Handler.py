from Player import Player
from EnemyBullet import EnemyBullet
from Enemy import Enemy
from Bullet import Bullet


def handler_draw(self, ):
    


        
        p1.playerDraw(display)
        

        for i in range(len(enemyList)):
            enemyList[i].enemyMove()
            enemyList[i].enemyDraw(display)
            p1.bulletCollision(enemyList[i])
        
        for i in range(len(enemyList)):
            if enemyList[i].getEnemyHealth <= 0:
                enemyList.pop(i)
                break