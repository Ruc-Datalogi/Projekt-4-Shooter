import sys, os, json
from Mediator import *

class GameObject:
    
    def __init__(self, object_ID):
        self.object_ID = object_ID
        self.alive = True
        
    def loop(self):
        pass

    def draw(self):
        pass
    
    def get_object_ID(self):
        return self.object_ID

    def get_rect(self):
        pass
    
    ## check bullet collision and damage enemy  
    def collision(self, ID, rect):
        hit_count = 0
        for element in Mediator.all_game_objects:
            if element.get_object_ID() == ID:
                if rect.colliderect(element.get_rect()):
                    if element.get_object_ID() != 'player':
                        Mediator.to_be_removed.append(element)
                    hit_count += 1
                    
        return hit_count

        
    def resource_path(self, relative_path):
        try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)