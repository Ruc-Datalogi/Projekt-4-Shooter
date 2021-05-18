import sys, pygame, random
from Mediator import *
from Enemy import *
from Boss import *
from Player import *

class Generator:

    def __init__ (self, screen):
        self.screen = screen
        
        self.level = 3
        self.max_amount_of_waves = 3
        self.current_wave = 0
        
        self.timer = 0
        self.game_completed = False

    def get_spawn_points(self, enemy_amount):
        spawn_list = []
        random_int = 0

        ##Making sure the enemies don't spawn on top of each other
        while len(spawn_list) < enemy_amount:
            random_int = random.randint(1,14)
            if random_int not in spawn_list:
                spawn_list.append(random_int)
        return spawn_list

    def reset_generator(self):
        self.level = 1
        self.max_amount_of_waves = 3
        self.current_wave = 0
        
        self.timer = 0

    def generate_wave_1(self, amount, enemy_ID):
        enemy_list = self.get_spawn_points(amount)
        for i in range(len(enemy_list)):
            Mediator.all_game_objects.append(Enemy(enemy_list[i]*20, (random.randint(10, 30)), enemy_ID, 'enemy', self.screen))

    def generate_wave_2(self):
        pass

    def generate_wave_3(self):
        pass

        
    def check_for_enemy(self):
        for enemy in Mediator.all_game_objects:
            if enemy.get_object_ID() == 'enemy' or enemy.get_object_ID() == 'boss':
                return True
        
        return False

    def check_for_boss(self):
        for enemy in Mediator.to_be_removed:
            if enemy.get_object_ID() == 'boss':
                return True
        return False

    def get_level(self):
        return self.level

    def next_wave(self):
        if self.timer > 360 and self.current_wave < self.max_amount_of_waves:
            self.current_wave += 1
            self.timer = 0
            return True
        return False

    def skip_level(self):
        self.level += 1
        self.timer = 0
        self.current_wave = 0

    def next_level(self):
        if self.current_wave == self.max_amount_of_waves and not self.check_for_enemy():
            self.current_wave = 0
            self.max_amount_of_waves += 1
            self.level += 1
            self.timer = 0



    def generate(self):
        self.timer += 1
        
        if self.level == 1:
            
            if self.next_wave():
                self.generate_wave_1(6,0)
            

            self.next_level()
                
        
        if self.level == 2:
            if self.next_wave():
                self.generate_wave_1(8,0)

            self.next_level()    

        if self.level == 3:
            if self.next_wave():
                self.generate_wave_1(4,1)
                self.generate_wave_1(4,2)

            self.next_level() 

        if self.level == 4:
 
            if not self.check_for_enemy():
                Mediator.all_game_objects.append(Boss(100,-20,0,'boss',self.screen))
            
            if self.check_for_boss():
                    self.skip_level()

        if self.level == 5:
            if self.next_wave():
                self.generate_wave_1(10,1)
            self.next_level()

        if self.level == 6:
            if self.next_wave():
                self.generate_wave_1(8,0)
                self.generate_wave_1(8,1)
            self.next_level()

        if self.level == 7:
            if self.next_wave():
                self.generate_wave_1(8,0)
                self.generate_wave_1(8,1)
                self.generate_wave_1(8,2)
            self.next_level()

        if self.level == 8:
            if self.next_wave():
                self.generate_wave_1(10,0)
                self.generate_wave_1(10,1)
                self.generate_wave_1(10,2)
            self.next_level()

        if self.level == 9:
            if self.next_wave():
                self.generate_wave_1(4,0)
                self.generate_wave_1(4,1)
                self.generate_wave_1(4,2)

            if not self.check_for_enemy():
                Mediator.all_game_objects.append(Boss(100,-20,0,'boss',self.screen, 2))
                  
            if self.check_for_boss():
                self.skip_level() 

        if self.level == 10:
            self.game_completed = True

    
    
    def get_game_complete(self):
        return self.game_completed
