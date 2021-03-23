import pygame

class Soundplayer:

    def __init__(self):
        pygame.mixer.init()
        self.enemy_hit = pygame.mixer.Sound('Game/sound/pew.wav')
        self.music = pygame.mixer.Sound('Game/sound/music.mp3')
        self.enemy_hit.set_volume(0.2)


    def enemy_hit_sound(self):
        self.enemy_hit.play()


    def play_music(self):
        self.music.play(-1)

    def stop_music(self):
        self.music.stop()