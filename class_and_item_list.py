import conditions
skillList=[]
class Skill: #General Skill stuff
    def __init__(self,name,bonus,damage,type = "Attack"):
        self.name = name
        self.bonus = bonus
        self.damage = damage
        self.healing = 0
        self.type = type
        self.conditions = []
        self.gold = 0
        skillList.append(self)
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
CureWounds = Skill("Cure Wounds",0,0, "Healing")
CureWounds.healing = 8
Slash = Skill("Slash",2,10)
SolarBeam = Skill("Solar Beam",9999,1)


Characters = []
class Character: #Class for a character set up, intakes stats and default Health and Armor
    def __init__(self,name,dex,int,wis,str,health,armorclass):
        self.name = name
        self.health = health
        self.armorClass = armorclass
        self.skills = {}
        self.skillNames = []
        self.dex = dex
        self.str = int
        self.int = wis
        self.wis = str
        self.appliedConditions = []
        self.items = []
        Characters.append(self)
    def addCondition(self, condition):
        self.appliedConditions.append(condition)
    def remCondition(self, condition):
        self.appliedConditions.pop(condition)
    def addSkills(self, skill1):
        self.skills[skill1.name] = skill1
        self.skillNames.append(skill1.name)
    def remSkill(self,skill):
        self.skills.pop(skill)
#Below are default classes
Cleric = Character("Cleric",-1,0,2,1,20,16)
Cleric.addSkills(CureWounds);Cleric.addSkills(Slam);Cleric.addSkills(Smite)
Mage = Character("Mage",0,2,1,-1,15,14)
Mage.addSkills(Burn);Mage.addSkills(Chill);Mage.addSkills(Zap)
Thief = Character("Thief",2,1,0,-1,17,15)
Thief.addSkills(Stab);Thief.addSkills(Slice);Thief.addSkills(Poke)
Warrior = Character("Warrior",1,-1,0,2,24,17)
Warrior.addSkills(ShieldBash);Warrior.addSkills(Chop);Warrior.addSkills(Slash)


ItemsList = []
class Items: #Class for Items
    def __init__(self,name,variations,bonus,type,uses):
        self.name = name
        self.bonus = bonus
        self.type = type
        self.uses = uses
        self.varList = []
        self.skillList = []
        ItemsList.append(self)
        for x in range(variations+1): #Creates a list of item variations, ie Sword, sword+1, sword+2...
            if x == 0:
                self.varList.append(self.name)
            else:
                self.varList.append(self.name+" + "+str(x))
    def addSkill(self,skill): #Gives skill to an item, such as a weapon having an attached skill.
        self.skillList.append(skill)
        
sword = Items("Sword",3,0,"Weapon",999)
sword.addSkill(Slash)
wand = Items("Wand",3,0,"Weapon",999)
wand.addSkill(Burn)
shield = Items("Shield",3,0,"Off-Hand",999)
shield.addSkill(ShieldBash)
dagger = Items("Dagger",3,0,"Weapon",999)
dagger.addSkill(Poke)
holyBook = Items("Holy Book",3,0,"Off-Hand",999)
holyBook.addSkill(CureWounds)
axe = Items("Axe",3,0,"Weapon",999)
axe.addSkill(Chop)
gloryHammer = Items("Hammer of Glory",1,0,"Weapon",1)
gloryHammer.addSkill(SolarBeam)
leatherArmor = Items("Leather Armor",1,1,"Armor",999)
ironArmor = Items("Iron Armor",1,2,"Armor",999)
steelArmor = Items("Steel Armor",1,3,"Armor",999)
apple = Items("Apple",1,4,"Healing",1)
appleStrudel = Items("Apple Strudel",1,8,"Healing",1)
applePie = Items("Apple Pie",1,16,"Healing",1)
watermelon = Items("Watermelon",1,1,"ArmorBuff",1)
watermelonSmoothie = Items("Watermelon Smoothie",1,2,"ArmorBuff",1)
watermelonSorbet = Items("Watermelon Sorbet",1,3,"ArmorBuff",1)

