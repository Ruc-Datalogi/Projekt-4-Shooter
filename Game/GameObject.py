
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
                    self.mediator.to_be_removed.append(element)
                    hit_count += 1
                    
        return hit_count
