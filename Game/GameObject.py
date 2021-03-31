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

    
    def updateJsonFile(self , ID):
    
        jsonFile = open("Game/inventory.json", "r") # Open the JSON file for reading
        data = json.load(jsonFile) # Read the JSON into the buffer
        jsonFile.close() # Close the JSON file

        ## Working with buffered content

        if ID == 'coin':
            tmp = data['coins']
            tmp2 = data['total_coins'] 
        
            tmp = int(tmp) + 1 
            tmp2 = int(tmp2) + 1
            print(tmp)
            data['coins'] = str(tmp)
            data['total_coins'] = str(tmp2)
        
        if ID == 'enemy':
            tmp = data['total_kills']
            tmp = int(tmp) + 1
            data['total_kills'] = str(tmp)

        ## Save our changes to JSON file
        jsonFile = open("Game/inventory.json", "w+")
        jsonFile.write(json.dumps(data))
        jsonFile.close()
