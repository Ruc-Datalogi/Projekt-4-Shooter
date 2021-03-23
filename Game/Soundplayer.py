import pygame

class Soundplayer:

###Template sound: make the 'pew.wav' sound when our bullets collide with enemies###
    def __init__(self):
        pygame.mixer.init()
        self.enemy_hit = pygame.mixer.Sound('Game/sound/pew.wav')
        self.enemy_hit.set_volume(0.2)

        self.player_damage = pygame.mixer.Sound('Game/sound/hit-01.wav')
        self.player_damage.set_volume(0.2)

    def enemy_hit_sound(self):
        self.enemy_hit.play()

    def player_damage_sound(self):
        self.player_damage.play()

    def load_music(self):
        pygame.mixer.music.load('Game/sound/music.mp3')
        pygame.mixer.music.set_volume(0.2)

    def play_music(self):
        pygame.mixer.music.play(-1)

    def stop_music(self):
        self.music.stop()