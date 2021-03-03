
class GameObject:
    

    def __init__(self, objectID, mediator):
        self.objectID = objectID
        self.mediator = mediator
        

    def loop(self):
        pass


    def draw(self):
        pass
    
    def getObjectID(self):
        return self.objectID

    def get_rect(self):
        pass
    
    ## check bullet collision and damage enemy  
    def collision(self, ID, rect):
        for element in self.mediator.all_game_objects:
            if element.getObjectID() == ID:
                if rect.colliderect(element.get_rect()):
                    self.mediator.to_be_removed.append(element)
                    return True
        return False
