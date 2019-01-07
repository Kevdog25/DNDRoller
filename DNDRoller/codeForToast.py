from Character import Character
from Skills import Skills

if __name__ == '__main__':
    characterList = Character.fromJson('characters.json')
    for c in characterList:
        print(c.Name)
        print('Proficiencies:')
        for s in Skills:
            print(f'\t{s.name} : {c.isProficient(s)}')
        print()
            