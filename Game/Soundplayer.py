import pygame, os

class Soundplayer:

###Template sound: make the 'pew.wav' sound when our bullets collide with enemies###
    def __init__(self):
        pygame.mixer.init()
        self.enemy_hit = pygame.mixer.Sound(self.resource_path('Game/sound/pew.wav'))
        self.enemy_hit.set_volume(0.2)

        self.player_damage = pygame.mixer.Sound(self.resource_path('Game/sound/hit-01.wav'))
        self.player_damage.set_volume(0.2)


    @staticmethod 
    def enemy_hit_sound(self):
        if not pygame.mixer.get_busy():
            self.enemy_hit.play()

    @staticmethod
    def player_damage_sound(self):
        self.player_damage.play()

    @staticmethod
    def load_music(self):
        pygame.mixer.music.load(self.resource_path('Game/sound/music.mp3'))
        pygame.mixer.music.set_volume(0.2)
    
    @staticmethod
    def play_music(self):
        pygame.mixer.music.play(-1)

    @staticmethod
    def stop_music(self):
        self.music.stop()

    def resource_path(self, relative_path):
        try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)