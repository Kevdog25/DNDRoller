#from Character import Character
from Skills import Skills
import random

class Character:
    Name = 'test'
    def isProficient(self, skill):
        return random.choice([True, False])
    @classmethod
    def fromJson(cls,f):
        return [Character() for _ in range(3)]

if __name__ == '__main__':
    characterList = Character.fromJson('characters.json')
    for c in characterList:
        print(c.Name)
        print('Proficiencies:')
        for s in Skills:
            print(f'{s.name} : {c.isProficient(s)}')
            