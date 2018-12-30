from SkillCheckTable import SkillCheckTable
from ScreenManager.Window import getScreenSize
from ScreenManager import Box, ScreenManager
import os


class character():
    def __init__(self):
        self.Name = 'Name'

if __name__ == '__main__':
    os.system('mode con lines=55 cols=120')
    manager = ScreenManager()
    characters = [character() for i in range(3)]
    skillCheckTable = SkillCheckTable(characters, x = 0, y = 0, width = 56, height = 54)
    manager.addBox(skillCheckTable)
    manager.run()