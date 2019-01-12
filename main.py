from eel import eel
import time
import numpy as np
from DNDRoller.Skills import Skills
import DNDRoller.Rolls as Rolls
from DNDRoller.Character import Character

Characters = []

@eel.expose
def rollSkillChecks():
    skillChecks = {}
    characters = [c.Name for c in Characters]
    for s in Skills:
        s_rolls = {}
        for c in Characters:
            s_rolls[c.Name] = Rolls.skillCheck(s, c)
        skillChecks[s.name] = s_rolls

    return {
        'characters' : characters,
        'skillChecks' : skillChecks
    }

@eel.expose
def rollSepllsAndWeapons():
    rolls = {}
    for c in Characters:
        c_rolls = {}
    return rolls

@eel.expose
def reloadCharacters():
    global Characters
    Characters = Character.fromJson('characters.json')

if __name__=='__main__':
    reloadCharacters()
    e = eel('Web')
    eel.start('Home.html')