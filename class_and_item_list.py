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
        self.count = 0
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
EldritchBlast = Skill("Eldritch Blast", 3, 6)
RitualChant = Skill("Ritual Chant",0,0)
Claw = Skill("Claw", 4,4)
Bite = Skill("Bite",0,2)
Decay = Skill("Decay",2,10,conditions.poisoned)

ItemsList = []
class Items: #Class for Items
    def __init__(self,name,variations,bonus,type):
        self.name = name
        self.bonus = bonus
        self.type = type
        self.varList = []
        self.skillList = []
        ItemsList.append(self.name)
        for x in range(variations+1): #Creates a list of item variations, ie Sword, sword+1, sword+2...
            if x == 0:
                self.varList.append(self.name)
            else:
                self.varList.append(self.name+" +"+str(x))
                ItemsList.append(self.name+" +"+str(x))
    def addSkill(self,skill): #Gives skill to an item, such as a weapon having an attached skill.
        self.skillList.append(skill)
        
sword = Items("Sword",3,0,"Weapon")
sword.addSkill(Slash)
wand = Items("Wand",3,0,"Weapon")
wand.addSkill(Burn)
shield = Items("Shield",3,0,"Off-Hand")
shield.addSkill(ShieldBash)
dagger = Items("Dagger",3,0,"Weapon")
dagger.addSkill(Poke)
holyBook = Items("Holy Book",3,0,"Off-Hand")
holyBook.addSkill(CureWounds)
axe = Items("Axe",3,0,"Weapon")
axe.addSkill(Chop)
mace = Items("Mace",3,0,"Weapon")
mace.addSkill(Slam)
gloryHammer = Items("Hammer of Glory",0,0,"Weapon")
gloryHammer.addSkill(SolarBeam)
ItemsList.pop(ItemsList.index("Hammer of Glory"))
clothes = Items("Clothes",0,0,"Armor")
leatherArmor = Items("Leather Armor",0,1,"Armor")
ironArmor = Items("Iron Armor",0,2,"Armor")
steelArmor = Items("Steel Armor",0,3,"Armor")
apple = Items("Apple",0,4,"Healing",)
appleStrudel = Items("Apple Strudel",0,8,"Healing",)
applePie = Items("Apple Pie",0,16,"Healing",)
watermelon = Items("Watermelon",0,1,"ArmorBuff",)
watermelonSmoothie = Items("Watermelon Smoothie",0,2,"ArmorBuff",)
watermelonSorbet = Items("Watermelon Sorbet",0,3,"ArmorBuff",)

Characters = []
class Character: #Class for a character set up, intakes stats and default Health and Armor
    def __init__(self,name,dex,int,wis,str,health,armorclass,weapon = None,armor = clothes):
        self.name = name
        self.health = health
        self.maxHealth = health
        self.armorClass = armorclass
        self.skills = []
        self.skillNames = []
        self.dex = dex
        self.str = int
        self.int = wis
        self.wis = str
        self.armor = armor
        self.weapon = weapon
        self.appliedConditions = []
        self.appliedConditionsDict = {}
        self.items = []
        self.defaultClass = self
        Characters.append(self)
    def addCondition(self, condition):
        self.appliedConditions.append(condition)
        self.appliedConditionsDict[condition] = condition.turns
    def remCondition(self, condition):
        self.appliedConditions.pop(condition)
        del self.appliedConditionsDict[condition]
    def addSkills(self, skill1):
        self.skills.append(skill1)
        self.skillNames.append(skill1.name)
    def equipArmor(self,newArmor):
        oldArmor = self.armor
        self.armor = newArmor
        self.armorClass -= oldArmor.bonus
        self.armorClass += newArmor.bonus
    def equipWeapon(self,newWeapon):
        oldWeapon = self.weapon
        self.weapon = newWeapon
        for skill in oldWeapon.skillList:
            if skill not in self.defaultClass.skills:
                self.skillNames.pop(skill)
                self.skills.pop(skill)
        for skill in self.weapon.skillList:
            self.skills.append(skill)
            self.skillNames.append(skill.name)
#Below are default classes
Cleric = Character("Cleric",-1,0,2,1,53,16,mace)
Cleric.addSkills(CureWounds);Cleric.addSkills(Slam);Cleric.addSkills(Smite)
Mage = Character("Mage",0,2,1,-1,45,14,wand)
Mage.addSkills(Burn);Mage.addSkills(Chill);Mage.addSkills(Zap)
Thief = Character("Thief",2,1,0,-1,47,15,dagger)
Thief.addSkills(Stab);Thief.addSkills(Slice);Thief.addSkills(Poke)
Warrior = Character("Warrior",1,-1,0,2,59,17,sword)
Warrior.addSkills(ShieldBash);Warrior.addSkills(Chop);Warrior.addSkills(Slash)

print(ItemsList)