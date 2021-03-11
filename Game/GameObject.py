
class GameObject:
    

    def __init__(self, objectID, mediator):
        self.objectID = objectID
        self.mediator = mediator
        

    def loop(self):
        pass


    def draw(self):
        pass
    
    def get_objectID(self):
        return self.objectID

    def get_rect(self):
        pass
    
    ## check bullet collision and damage enemy  
    def collision(self, ID, rect):
        hit_count = 0
        for element in self.mediator.all_game_objects:
            if element.get_objectID() == ID:
                if rect.colliderect(element.get_rect()):
                    self.mediator.to_be_removed.append(element)
                    hit_count += 1
                    
        return hit_count
