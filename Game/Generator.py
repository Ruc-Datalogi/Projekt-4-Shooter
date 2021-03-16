import sys, pygame, random
from Mediator import *
from Enemy import *


class Generator:

    def __init__ (self, screen, mediator):
        self.screen = screen
        self.mediator = mediator
        
        self.level = 1
        self.max_amount_of_waves = 3
        self.current_wave = 0

        self.timer = 0

    def generate_wave_1(self):
        spawn_list = []
        random_int = 0

        ##Making sure the enemies don't spawn on top of each other
        while len(spawn_list) < 6:
            random_int = random.randint(1,14)
            if random_int not in spawn_list:
                spawn_list.append(random_int)
        for i in range(0,6):
            self.mediator.all_game_objects.append(Enemy(spawn_list[i]*20, (random.randint(10, 30)), 1, 'enemy', self.mediator, self.screen))

    def generate_wave_2(self):
        spawn_list = []
        random_int = 0
        
        while len(spawn_list) < 4:
            random_int = random.randint(1,14)
            if random_int not in spawn_list:
                spawn_list.append(random_int)
        
        for i in range (0, 4):
            self.mediator.all_game_objects.append(Enemy(spawn_list[i]*20, (random.randint(10, 30)), 2, 'enemy', self.mediator, self.screen))


    def generate_wave_3(self):
        pass

    def check_for_enemy(self):
        for enemy in self.mediator.all_game_objects:
            if enemy.get_objectID() == 'enemy':
                return True
        
        return False

    def get_level(self):
        return self.level


    def generate(self):
        if self.level == 1:
            self.timer += 1

            if self.timer > 360 and self.current_wave < self.max_amount_of_waves:
                
                self.current_wave += 1
                self.generate_wave_1()
                self.timer = 0
        
            if self.current_wave == self.max_amount_of_waves and not self.check_for_enemy():
                self.current_wave = 0
                self.max_amount_of_waves += 1
                self.level += 1
                self.timer = 0
        
        if self.level == 2:
            self.timer += 1

            if self.timer > 180 and self.current_wave < self.max_amount_of_waves:
                
                self.current_wave += 1
                self.generate_wave_1()
                self.timer = 0
        
            if self.current_wave == self.max_amount_of_waves and not self.check_for_enemy():
                self.level += 1

    

    


