import conditions
class Skill: #General Skill stuff
    def __init__(self,name,bonus,damage):
        self.name = name
        self.bonus = bonus
        self.damage = damage
        self.healing = 0
        self.conditions = []
    def addCondition(self, condition):
        self.conditions.append(condition)
Burn = Skill("Burn",2,8)
Burn.addCondition(conditions.burning)
Zap = Skill("Zap",1,10)
Chill = Skill("Chill",3,6)
Chill.addCondition(conditions.frozen)
Stab = Skill("Stab",3,7)
Slice = Skill("Slice",2,9)
Poke = Skill("Poke",5,5)
Slam = Skill("Slam",1,12)
Chop = Skill("Chop",0,16)
ShieldBash = Skill("Shield Bash",2,8)
ShieldBash.addCondition(conditions.grappled)
Smite = Skill("Smite",3,8)
CureWounds = Skill("Cure Wounds",0,0)
CureWounds.healing = 8
Slash = Skill("Slash",2,10)



class Character: #Class for a character set up, intakes stats and default Health and Armor
    def __init__(self,name,dex,int,wis,str,health,armorclass):
        self.name = name
        self.health = health
        self.armorClass = armorclass
        self.skills = []
        self.dex = dex
        self.str = int
        self.int = wis
        self.wis = str
        self.appliedConditions = []
        self.items = []
    def addCondition(self, condition):
        self.appliedConditions.append(condition)
    def remCondition(self, condition):
        self.appliedConditions.pop(condition)
    def addSkills(self, skill1):
        self.skills.append(skill1)
    def remSkill(self,skill):
        self.skills.pop(skill)
#Below are default classes
Mage = Character("Mage",0,2,1,-1,15,14)
Mage.addSkills(Burn);Mage.addSkills(Chill);Mage.addSkills(Zap)
Thief = Character("Thief",2,1,0,-1,17,15)
Thief.addSkills(Stab);Thief.addSkills(Slice);Thief.addSkills(Poke)
Cleric = Character("Cleric",-1,0,2,1,20,16)
Cleric.addSkills(CureWounds);Cleric.addSkills(Slam);Cleric.addSkills(Smite)
Warrior = Character("Warrior",1,-1,0,2,24,17)
Warrior.addSkills(ShieldBash);Warrior.addSkills(Chop);Warrior.addSkills(Slash)
Characters = [Mage,Thief,Cleric,Warrior]

Sword1 = {"Bonus":1}
Sword2 = {"Bonus":2}
Sword3 = {"Bonus":3}
Wand1= {"Bonus":1,"Skills":Burn}
Wand2= {"Bonus":2,"Skills":Burn}
Wand3= {"Bonus":3,"Skills":Burn}
Shield1 = {"Armor":1,"Skills":ShieldBash}
Shield2 = {"Armor":2,"Skills":ShieldBash}
Shield3 = {"Armor":3,"Skills":ShieldBash}
Dagger1 = {"Bonus":1,"Skills":Poke}
Dagger2 = {"Bonus":2,"Skills":Poke}
Dagger3 = {"Bonus":3,"Skills":Poke}
Book1 = {"Bonus":1,"Skills":CureWounds}
Book2 = {"Bonus":2,"Skills":CureWounds}
Book3 = {"Bonus":3,"Skills":CureWounds}
Axe1 = {"Bonus":1,"Skills":Chop}
Axe2 = {"Bonus":2,"Skills":Chop}
Axe3 = {"Bonus":3,"Skills":Chop}
Leather = {"ArmorClass":1}
Iron = {"ArmorClass":2}
Steel = {"ArmorClass":3}
Apple = {"Healing":4, "Uses" :1}
Apple_strudel = {"Healing":8, "Uses": 1}
Apple_pie = {"Healing":16, "Uses": 1}
Watermelon = {"ArmorClass": 1, "Uses":1}
Watermelon_smoothy = {"ArmorClass":2, "Uses":1}
Watermelon_sorbet = {"ArmorClass":3, "Uses":1}
Weapons = [Sword1,Sword2,Sword3, Wand1,Wand2,Wand3,Dagger1,Dagger2,Dagger3,Book1,Book2,Book3,Axe1,Axe2,Axe3]
Armor =[Leather, Iron, Steel,Shield1,Shield2,Shield3]
Consumables = [Apple,Apple_strudel,Apple_pie,Watermelon,Watermelon_smoothy,Watermelon_sorbet]
