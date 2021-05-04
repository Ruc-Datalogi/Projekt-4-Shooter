import json

class JsonLoader(object):
    print("i construct")
    
    jsonFile = open("Game/save_file.json", "r")
    data = json.load(jsonFile)

    coins = data["coins"]
    total_coins = data["total_coins"]
    total_kills = data["total_kills"]
    music = data["music"]
    sounds = data["sounds"]
    bullet_damage = data["bullet_damage"]
    bullet_amount = data["bullet_amount"]
    fire_speed = data["fire_speed"]
    shield = data["shield"]
    
    def get_coins(self):
        return self.coins

    def get_music(self):
        return self.music

    def get_sounds(self):
        return self.sounds

    def get_bullet_damage(self):
        return self.bullet_damage
    
    def get_bullet_amount(self):
        return self.bullet_amount
    
    def get_fire_speed(self):
        return self.fire_speed
    
    def get_shield(self):
        return self.shield

    @staticmethod
    def updateJsonFile(self , ID):
        print("i use")
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
            JsonLoader.total_coins = data["total_coins"]

        if ID == 'enemy':
            tmp = data['total_kills']
            tmp = int(tmp) + 1
            data['total_kills'] = str(tmp)

        if ID == 'sounds+':
            tmp = data['sounds']
            tmp = int(tmp) + 10

            if tmp > 100: 
                tmp = 100

            data['sounds'] = str(tmp)
            JsonLoader.sounds = data['sounds']
        
        if ID == 'sounds-':
            tmp = data['sounds']
            tmp = int(tmp) - 10
            
            if tmp < 0:
                tmp = 0
            
            data['sounds'] = str(tmp)
            JsonLoader.sounds = data['sounds']

        if ID == 'music+':
            tmp = data['music']
            tmp = int(tmp) + 10

            if tmp > 100: 
                tmp = 100

            data['music'] = str(tmp)
            JsonLoader.music = data['music']
        
        if ID == 'music-':
            tmp = data['music']
            tmp = int(tmp) - 10
            
            if tmp < 0:
                tmp = 0

            data['music'] = str(tmp)
            JsonLoader.music = data['music']

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