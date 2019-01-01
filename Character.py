import random
import json

class Character:
    def __init__(self):
        #self.Name = random.choice(['Kevin', 'Alice', 'Dri', 'J'])
        pass


    def isProficient(self, skill):
            return skill in self.Proficiencies
    
    def isExpert(self, skill):
            return skill in self.Expertise

    

    @classmethod
    def fromJson(cls):
        '''Takes a JSON object, parses it and returns a character object'''
        
        json_file='character.json'
        json_data=open(json_file)
        data = json.load(json_data)
        characterList = []
        for k in data:
            character = Character()
            character.Name = k["Name"]
            character.Strength = k["Stats"]["Strength"]
            character.Dexterity = k["Stats"]["Dexterity"]
            character.Constitution = k["Stats"]["Constitution"]
            character.Wisdom = k["Stats"]["Wisdom"]
            character.Intelligence = k["Stats"]["Intelligence"]
            character.Charisma = k["Stats"]["Charisma"]
            character.Proficiencies = set(k['isProficient'])
            character.Expertise = set(k['isExpert'])
            characterList.append(character)
        return characterList

    def getCharacter(self,name):
        fromJson()
        for k in :
            if k.name == name:
                return k
        return  






if __name__ == '__main__':
    print('You can test things out here.')
    print('Try running \"python Character.py\" from the right location in a cmd prompt')
    Alice = Character.getCharacter("Alice")
    print(Alice.Name)
    print(Alice.Expertise)
    print(Alice.isExpert("Religion"))
    print(Alice.Proficiencies)