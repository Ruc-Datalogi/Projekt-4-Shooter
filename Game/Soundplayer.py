import pygame

class Soundplayer:

    def __init__(self):
        pygame.mixer.init()
        self.enemy_hit = pygame.mixer.Sound('sound/pew.wav')

    def enemy_hit_sound(self):
        self.enemy_hit.play()


