import sys, pygame, random
from Mediator import *
from Enemy import *


class Generator:

    def __init__ (self, screen, mediator):
        self.screen = screen
        self.mediator = mediator
        self.level = 0
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
        pass

    def generate_wave_3(self):
        pass

    def generate (self):
        if self.level == 0:
            self.timer += 1
            if self.timer > 180:
                self.generate_wave_1()
                self.timer = 0


