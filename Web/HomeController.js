"use strict";
var HomeController = /** @class */ (function () {
    function HomeController() {
        var _this = this;
        this.SkillGroups = [
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
        ];
        this.SkillTable = document.getElementById('skillTable');
        document.body.addEventListener('keydown', function (event) {
            console.log(JSON.stringify(event));
            if (event.key.toUpperCase() === 'R') {
                _this.skillTableRefresh();
            }
        });
        this.skillTableRefresh();
    }
    HomeController.prototype.skillTableRefresh = function () {
        var _this = this;
        eel.rollSkillChecks()(function (rolls) { return _this.initSkillTable(rolls); });
    };
    HomeController.prototype.initSkillTable = function (response) {
        var _this = this;
        var rolls = response.Value;
        while (this.SkillTable.firstChild) {
            this.SkillTable.removeChild(this.SkillTable.firstChild);
        }
        var headerRow = document.createElement('tr');
        headerRow.appendChild(document.createElement('td'));
        rolls.characters.forEach(function (char) {
            var header = document.createElement('td');
            header.innerText = char;
            header.style.textAlign = 'center';
            headerRow.appendChild(header);
        });
        this.SkillTable.appendChild(headerRow);
        this.SkillGroups.forEach(function (skillGroup, i) {
            var body = document.createElement('tbody');
            skillGroup.forEach(function (skill) {
                var row = document.createElement('tr');
                var name = document.createElement('td');
                name.innerText = skill;
                row.appendChild(name);
                var skillChecks = rolls.skillChecks[skill];
                rolls.characters.forEach(function (char) {
                    var check = document.createElement('td'), top = document.createElement('span'), bottom = document.createElement('span');
                    check.style.textAlign = 'center';
                    top.innerText = skillChecks[char][1].toString();
                    bottom.innerText = skillChecks[char][0].toString() + '  ' + skillChecks[char][2].toString();
                    check.appendChild(top);
                    check.appendChild(document.createElement('br'));
                    check.appendChild(bottom);
                    row.appendChild(check);
                });
                body.appendChild(row);
            });
            _this.SkillTable.appendChild(body);
        });
    };
    return HomeController;
}());
var homeController;
eel.onInit(function () {
    homeController = new HomeController();
});
