import random
import json

class Character:
    def __init__(self):
        #self.Name = random.choice(['Kevin', 'Alice', 'Dri', 'J'])
        pass


    def isProficient(self, skill):
        for k in self.Proficiencies:
            if k == skill:
                return True
        return 
    
    def isExpert(self, skill):
        for k in self.Expertise:
            if k == skill:
                return True
        return

    

    @classmethod
    def fromJson(cls):
        '''Takes a JSON object, parses it and returns a character object'''
        character = Character()
        json_file='character.json'
        json_data=open(json_file)
        data = json.load(json_data)
        character.Name = data["Name"]
        character.Strength = data["stats"]["Strength"]
        character.Dexterity = data["stats"]["Dexterity"]
        character.Constitution = data["stats"]["Constitution"]
        character.Wisdom = data["stats"]["Wisdom"]
        character.Intelligence = data["stats"]["Intelligence"]
        character.Charisma = data["stats"]["Charisma"]
        character.Proficiencies = set(data['isProficient'])
        character.Expertise = set(data['isExpert'])        
        return character






if __name__ == '__main__':
    print('You can test things out here.')
    print('Try running \"python Character.py\" from the right location in a cmd prompt')
    Alice = Character.fromJson()
    print(Alice.Name)
    print(Alice.Expertise)
    print(Alice.isExpert("Religion"))
    print(Alice.Proficiencies)