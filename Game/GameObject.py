
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
