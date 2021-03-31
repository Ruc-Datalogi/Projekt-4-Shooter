import sys, os, json


class GameObject:
    

    def __init__(self, object_ID, mediator):
        self.object_ID = object_ID
        self.mediator = mediator
        

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
        for element in self.mediator.all_game_objects:
            if element.get_object_ID() == ID:
                if rect.colliderect(element.get_rect()):
                    if element.get_object_ID() != 'player':
                        self.mediator.to_be_removed.append(element)
                    hit_count += 1
                    
        return hit_count
    
    def collision_test(self, rect):
        hit_count = []
        for element in self.mediator.all_game_objects:
            if rect.colliderect(element.get_rect()):
                hit_count.append(element.get_object_ID())

        return hit_count
        
    def resource_path(self, relative_path):
        try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)

    
    
