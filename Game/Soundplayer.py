import pygame

class Soundplayer:

###Template sound: make the 'pew.wav' sound when our bullets collide with enemies###
    def __init__(self):
        pygame.mixer.init()
        self.enemy_hit = pygame.mixer.Sound('Game/sound/pew.wav')
        self.enemy_hit.set_volume(0.2)


    def enemy_hit_sound(self):
        self.enemy_hit.play()


