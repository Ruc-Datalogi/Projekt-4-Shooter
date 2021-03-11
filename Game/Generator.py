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
        for i in range(0,6):
            self.mediator.all_game_objects.append(Enemy(random.randint(10,290), (random.randint(10, 30))*-1, 1, 'enemy', self.mediator, self.screen))

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


