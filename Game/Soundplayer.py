import pygame, os
from JsonLoader import *

## Class for making all the sounds
class Soundplayer:
    pygame.mixer.init()

    ## Static channels
    channel_enemy = pygame.mixer.Channel(0)
    channel_player = pygame.mixer.Channel(1)

    channel_enemy.set_volume(0.2)
    channel_player.set_volume(0.2)

    def __init__(self):
        pygame.mixer.init()

        self.start_volume = 0.2
        
        self.volume_sounds = int(JsonLoader.get_sounds(JsonLoader))
        self.volume_music = int(JsonLoader.get_music(JsonLoader))
        

        self.enemy_hit = pygame.mixer.Sound(self.resource_path('Game/sound/pew.wav'))
        self.enemy_hit.set_volume(0.8)

        self.player_damage = pygame.mixer.Sound(self.resource_path('Game/sound/hit-01.wav'))
        self.player_damage.set_volume(0.8)

    @staticmethod
    def enemy_hit_sound(self):
        if not self.channel_enemy.get_busy:
            self.channel_enemy.play(self.enemy_hit)
        
    @staticmethod
    def player_damage_sound(self):
        self.channel_player.play(self.player_damage)
    
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
        pygame.mixer.music.set_volume((self.start_volume * volume)/100)

    @staticmethod
    def change_volume_sounds(self, volume):
        self.channel_enemy.set_volume((0.2 * volume)/100)
        self.channel_player.set_volume((0.2 * volume)/100)
        self.channel_player.play(self.player_damage)

    def resource_path(self, relative_path):
        try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)