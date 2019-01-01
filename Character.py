import random
import json
from Skills import Skills

class Character:
    def __init__(self):
        #self.Name = random.choice(['Kevin', 'Alice', 'Dri', 'J'])
        pass


    def isProficient(self, skill):
            return skill in self.Proficiencies
    
    def isExpert(self, skill):
            return skill in self.Expertise

    

    @classmethod
    def fromJson(cls,json_file):
        '''Takes a JSON object, parses it and returns a character object'''
        
        #json_file='character.json'
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
            #character.Proficiencies = set(k['isProficient'])
            character.Proficiencies = []
            for p in list(k['isProficient']):
                character.Proficiencies.append(Skills[p])
            character.Expertise = []
            for e in list(k['isExpert']):
                character.Expertise.append(Skills[e])
            characterList.append(character)
        return characterList

def getEnum(name):
    for s in Skills:
        if name == s.name:
            return s


if __name__ == '__main__':
    print('You can test things out here.')
    print('Try running \"python Character.py\" from the right location in a cmd prompt')
    #Alice = Character.getCharacter("Alice")
    characterList = Character.fromJson('character.json')
    for c in characterList:
        print(c.Name)
        print('Proficiencies:')
        for s in Skills:
            print(f'\t{s.name} : {c.isProficient(s)}')
        print()
        print(c.Proficiencies)
        print(c.Expertise)

    
    #print(Alice.Name)
    #print(Alice.Expertise)
    #print(Alice.isExpert("Religion"))
    #print(Alice.Proficiencies)