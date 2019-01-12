declare var eel : any;

interface TableRolls {
    characters : Array<string>;
    skillChecks : {
        [skillName : string] : {
            [characterName : string] : Array<number>
            }
        }
}

class HomeController {
    SkillGroups : Array<Array<string>> = [
        ['Investigation',
         'Perception',
         'Stealth', 
         'SleightOfHand'],
        ['Insight',
         'Deception',
         'Persuasion',
         'Intimidation',
         'Performance'],
        ['Athletics',
         'Acrobatics'],
        ['Survival',
         'Medicine',
         'AnimalHandling',
         'Nature'],
        ['Arcana',
         'Religion']
    ]

    SkillTable : HTMLElement;

    constructor(){
        this.SkillTable = document.getElementById('skillTable')!;
        document.body.addEventListener('keydown', (event : KeyboardEvent) => {
            console.log(JSON.stringify(event))
            if (event.key.toUpperCase() === 'R'){
                this.skillTableRefresh()
            }
        })
        
        this.skillTableRefresh()
    }

    private skillTableRefresh(){
        eel.rollSkillChecks()((rolls : TableRolls) => this.initSkillTable(rolls));
    }

    private initSkillTable(response : any) {
        let rolls : TableRolls = response.Value;
        while (this.SkillTable.firstChild) {
            this.SkillTable.removeChild(this.SkillTable.firstChild!);
        }

        let headerRow = document.createElement('tr')
        headerRow.appendChild(document.createElement('td'))
        rolls.characters.forEach((char : string) => {
            let header = document.createElement('td')
            header.innerText = char;
            header.style.textAlign = 'center'
            headerRow.appendChild(header)
        });
        this.SkillTable.appendChild(headerRow);

        this.SkillGroups.forEach((skillGroup : Array<string>, i : number)  => {
            let body = document.createElement('tbody')
            skillGroup.forEach((skill : string) => {
                let row = document.createElement('tr');
                let name = document.createElement('td')
                name.innerText = skill
                row.appendChild(name)

                let skillChecks = rolls.skillChecks[skill]
                rolls.characters.forEach((char : string) => {
                    let check = document.createElement('td'),
                        top = document.createElement('span'),
                        bottom = document.createElement('span');
                    check.style.textAlign = 'center'
                    
                    top.innerText = skillChecks[char][1].toString();
                    bottom.innerText = skillChecks[char][0].toString() + '  ' + skillChecks[char][2].toString();
                    check.appendChild(top); check.appendChild(document.createElement('br'));
                    check.appendChild(bottom);
                    row.appendChild(check);
                });
                body.appendChild(row);
            });
            this.SkillTable.appendChild(body);
        });
    }
}

var homeController : HomeController;
eel.onInit(() => {
    homeController = new HomeController()
})