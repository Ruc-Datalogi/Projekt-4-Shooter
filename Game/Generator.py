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
    def get_spawn_points(self, enemy_amount):
        spawn_list = []
        random_int = 0

        ##Making sure the enemies don't spawn on top of each other
        while len(spawn_list) < enemy_amount:
            random_int = random.randint(1,14)
            if random_int not in spawn_list:
                spawn_list.append(random_int)
        return spawn_list

    def generate_wave_1(self, amount, enemy_ID):
        enemy_list = self.get_spawn_points(amount)
        for i in range(len(enemy_list)):
            self.mediator.all_game_objects.append(Enemy(enemy_list[i]*20, (random.randint(10, 30)), enemy_ID, 'enemy', self.mediator, self.screen))

    def generate_wave_2(self):
        pass

    def generate_wave_3(self):
        pass

    def check_for_enemy(self):
        for enemy in self.mediator.all_game_objects:
            if enemy.get_object_ID() == 'enemy':
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
                
                self.generate_wave_1(10,0)
        
            self.next_level()
                
        
        if self.level == 2:
            if self.next_wave():
                self.generate_wave_1(8,0)
            self.next_level()      
