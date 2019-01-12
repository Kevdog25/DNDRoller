from DNDRoller.Skills import Skills
from DNDRoller.Stats import Stats
import sys
import random

def skillCheck(skill, char):
    a, b = random.randint(1,20), random.randint(1,20)
    return (min(a, b), a, max(a, b))

def save(stat, char):
    a, b = random.randint(1, 20), random.randint(1, 20)
    return (min(a,b), a, max(a, b))
    
    

    
