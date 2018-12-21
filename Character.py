import random

class Character:
    def __init__(self):
        self.Name = random.choice(['Kevin', 'Alice', 'Dri', 'J'])
        pass

    @classmethod
    def fromJson(cls, jsonObj):
        '''Takes a JSON object, parses it and returns a character object'''
        character = Character()
        # TODO - Actually do this.

        return character

if __name__ == '__main__':
    print('You can test things out here.')
    print('Try running \"python Character.py\" from the right location in a cmd prompt')