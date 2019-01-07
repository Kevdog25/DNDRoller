from eel import eel
import time
import numpy as np
from Skills import Skills
import Rolls


Characters = []

@eel.expose
def rollSkillChecks():
    rolls = {}
    for c in Characters:
        c_rolls = {}
        for s in Skills:
            c_rolls[s.name] = Rolls.skillCheck(s, c)
        rolls[c.Name] = c_rolls
    return rolls

@eel.expose
def reloadCharacters():
    return

if __name__=='__main__':
    e = eel('Web')
    eel.start('Home.html')