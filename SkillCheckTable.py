from ScreenManager import BoundedBox
from Skills import Skills
import Rolls


class SkillCheckTable(BoundedBox):

    GroupedSkills = [
        [Skills.Investigation,
         Skills.Perception,
         Skills.Stealth, 
         Skills.SleightOfHand],
        [Skills.Insight,
         Skills.Deception,
         Skills.Persuasion,
         Skills.Intimidation,
         Skills.Performance],
        [Skills.Athletics,
         Skills.Acrobatics],
        [Skills.Survival,
         Skills.Medicine,
         Skills.AnimalHandling,
         Skills.Nature],
        [Skills.Arcana,
         Skills.Religion]
    ]

    def __init__(self, characterList, *args, **kwargs):
        BoundedBox.__init__(self, *args, **kwargs)
        nameLength = sum(1 + len(c.Name) for c in characterList)
        self.Characters = characterList
        self.redraw()
        
    def writeLine(self, i, line):
        if i >= self.Height - 1:
            raise ValueError('Cannot write here')
        self.Buffer[1 + i][1 : 1 + min(len(line), self.Width - 2)] = line
        
    def redraw(self):
        colWidths = [max(len(s.name) for s in Skills) + 1] + [max(len(c.Name), 12) for c in self.Characters]
        header = []
        for colWidth, h in zip(colWidths, [''] + [c.Name for c in self.Characters]):
            header.append(h.center(colWidth))
        r = 0
        self.writeLine(r, u'\u2502'.join(header))
        r += 1
        for group in SkillCheckTable.GroupedSkills:
            self.writeLine(r, u'\u2550' * (self.Width - 2))
            r += 1
            for i, skill in enumerate(group):
                if i > 0 :
                    line = u'\u253C'.join(u'\u2500' * (colWidth) for colWidth in colWidths)
                    #line = u'\u2500' * (sum(colWidths))
                    self.writeLine(r, line)
                    r += 1
                rolls = [Rolls.skillCheck(skill, c) for c in self.Characters]
                line = [skill.name.ljust(colWidths[0])] + [f'{roll[1]}'.center(colWidth) for roll,colWidth in zip(rolls, colWidths[1:])]
                self.writeLine(r, u'\u2502'.join(line))
                r += 1
                line = [''.ljust(colWidths[0])] + ['{:2}   {:2}'.format(roll[0], roll[2]).center(colWidth) for roll, colWidth in zip(rolls, colWidths[1:])]
                self.writeLine(r, u'\u2502'.join(line))
                r += 1
        self.dirty()
        
    def onKeyDown(self, event):
        if event.Char is not None and event.Char.upper() == 'R':
            self.redraw()
        return True
        