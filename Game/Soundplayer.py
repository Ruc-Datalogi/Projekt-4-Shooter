import pygame, os
from JsonLoader import *


class Soundplayer:

###Template sound: make the 'pew.wav' sound when our bullets collide with enemies###


    def __init__(self):
        pygame.mixer.init()

        self.start_volume = 0.2
        
        self.volume_sounds = int(JsonLoader.get_sounds(JsonLoader))
        self.volume_music = int(JsonLoader.get_music(JsonLoader))
        

        self.enemy_hit = pygame.mixer.Sound(self.resource_path('Game/sound/pew.wav'))
        self.enemy_hit.set_volume(0.2)

        self.player_damage = pygame.mixer.Sound(self.resource_path('Game/sound/hit-01.wav'))
        self.player_damage.set_volume(0.2)
        self.channel = pygame.mixer.Channel(0)









    @staticmethod 
    def enemy_hit_sound(self):
        if not pygame.mixer.get_busy():
            self.channel = self.enemy_hit.play()

    @staticmethod
    def player_damage_sound(self):
            self.channel = self.player_damage.play()

    @staticmethod
    def load_music(self):
        pygame.mixer.music.load(self.resource_path('Game/sound/music.mp3'))
        pygame.mixer.music.set_volume(0.2)
        self.change_volume_music(self, self.volume_music)

    
    @staticmethod
    def play_music(self):
        pygame.mixer.music.play(-1)

    @staticmethod
    def stop_music(self):
        self.music.stop()
    
    @staticmethod
    def change_volume_music(self, volume):
        print(volume)
        pygame.mixer.music.set_volume((self.start_volume * volume)/100)

    @staticmethod
    def change_volume_sounds(self, volume):
        self.channel.set_volume((0.2 * volume)/100)
        #self.player_damage.set_volume((0.2 * volume)/100)
        #self.enemy_hit.set_volume((0.2 * volume)/100)

    def resource_path(self, relative_path):
        try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)