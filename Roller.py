from Character import Character
from Skills import Skills
import random

def loadCharacters(directory):
    # TODO - Actually load characters
    return [Character() for _ in range(3)]

def clearScreen():
    print('\n'*50)

def displayRolls(chars):
    # TODO - actually care about the characters
    colHeaders = [''] + [c.Name for c in chars]
    colWidths = [max(len(s.name) for s in Skills)] + [max(len(c.Name), 8) for c in chars]
    totalWidth = sum(colWidths) + len(colHeaders)

    print('|'.join(header.center(width) for header, width in zip(colHeaders, colWidths)))
    for skill in Skills:
        row = []
        lowerRow = []
        for c, width in zip(chars, colWidths[1:]):
            low, roll, high = skillCheck(skill, c)
            row.append('{:>2}'.format(roll).center(width))
            lowerRow.append('({:2})({:2})'.format(low, high).center(width))

        print(skill.name.ljust(colWidths[0]) + '|' + '|'.join(cell.center(width) for cell, width in zip(row, colWidths[1:])))
        print(''.ljust(colWidths[0]) + '|' + '|'.join(cell.center(width) for cell, width in zip(lowerRow, colWidths[1:])))
    

def skillCheck(skill, char):
    a, b = random.randint(1,20), random.randint(1, 20)
    return min(a, b), a, max(a, b)

if __name__ == '__main__':
    directory = 'characters'
    chars = loadCharacters(directory)

    while True:
        clearScreen()
        displayRolls(chars)

        x = input()
        if x.upper() == 'R':
            chars = loadCharacters(directory)
        elif x.upper() == 'Q':
            break
            

