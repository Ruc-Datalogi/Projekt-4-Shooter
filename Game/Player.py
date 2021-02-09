class Player:


    def checkCollision(x,y):
        if x <= 0:
            x = 0
        if x >= 584:
            x = 584
        if y <= 0: 
            y = 0
        if y >= 784:
            y = 784