import json

class JsonLoader(object):

    
    jsonFile = open("Game/save_file.json", "r")
    data = json.load(jsonFile)

    coins = data["coins"]
    total_kills = data["total_kills"]
    music = data["music"]
    sounds = data["sounds"]
    
    
    def get_coins(self):
        return self.coins

    @classmethod
    def get_music(s):
        return s.music

    @staticmethod
    def updateJsonFile(self , ID):
    
        jsonFile = open("Game/save_file.json", "r") # Open the JSON file for reading
        data = json.load(jsonFile) # Read the JSON into the buffer
        jsonFile.close() # Close the JSON file

        ## Working with buffered content

        if ID == 'coin':
            tmp = data['coins']
            tmp2 = data['total_coins'] 
        
            tmp = int(tmp) + 1 
            tmp2 = int(tmp2) + 1
            data['coins'] = str(tmp)
            data['total_coins'] = str(tmp2)
            JsonLoader.coins = data["coins"]

        if ID == 'enemy':
            tmp = data['total_kills']
            tmp = int(tmp) + 1
            data['total_kills'] = str(tmp)

        ## Save our changes to JSON file
        jsonFile = open("Game/save_file.json", "w+")
        jsonFile.write(json.dumps(data))
        jsonFile.close()

    def reload_json_file(self):
        jsonFile = open("Game/save_file.json", "r")
        data = json.load(jsonFile)

        coins = data["coins"]
        total_kills = data["total_kills"]
        music = data["music"]
        sounds = data["sounds"]