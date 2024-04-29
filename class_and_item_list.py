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
Burn = Skill("Burn",2,8,"Magic")
Burn.addCondition(conditions.burning)
Zap = Skill("Zap",1,10,"Magic")
Chill = Skill("Chill",3,6,"Magic")
Chill.addCondition(conditions.frozen)
Stab = Skill("Stab",3,7,"Dex")
Slice = Skill("Slice",2,9,"Dex")
Poke = Skill("Poke",5,5,"Dex")
Slam = Skill("Slam",1,12,"Str")
Chop = Skill("Chop",0,16,"Str")
ShieldBash = Skill("Shield Bash",2,8,"Str")
ShieldBash.addCondition(conditions.grappled)
Smite = Skill("Smite",3,8,"Holy")
CureWounds = Skill("Cure Wounds",0,0, "Healing")
CureWounds.healing = 8
Slash = Skill("Slash",2,10,"Str")
SolarBeam = Skill("Solar Beam",9999,1,"Glory")
EldritchBlast = Skill("Eldritch Blast", 3, 6,"Magic")
RitualChant = Skill("Ritual Chant",0,0,"Curse")
Claw = Skill("Claw", 4,4,"Str")
Bite = Skill("Bite",0,2,"Str")
Decay = Skill("Decay",2,10,"Magic")
Decay.addCondition = conditions.poisoned

ItemsList = []
itemNames = []
class Items: #Class for Items
    def __init__(self,name,bonus,type,cost = 10):
        self.name = name
        self.bonus = bonus
        self.type = type
        self.cost = cost*(self.bonus + 1)
        self.skillList = []
        ItemsList.append(self)
        itemNames.append(self.name)
    def addSkill(self,skill): #Gives skill to an item, such as a weapon having an attached skill.
        self.skillList.append(skill)
        
sword = Items("Sword",0,"Weapon",)
sword.addSkill(Slash)
sword1 = Items("Sword+1",1,"Weapon")
sword1.addSkill(Slash)
sword2 = Items("Sword+2",2,"Weapon")
sword2.addSkill(Slash)
sword3 = Items("Sword+3",3,"Weapon")
sword3.addSkill(Slash)
wand = Items("Wand",0,"Weapon")
wand.addSkill(Burn)
wand1 = Items("Wand+1",1,"Weapon")
wand1.addSkill(Burn)
wand2 = Items("Wand+2",2,"Weapon")
wand2.addSkill(Burn)
wand3 = Items("Wand+3",3,"Weapon")
wand3.addSkill(Burn)
shield = Items("Shield",0,"Off-Hand")
shield.addSkill(ShieldBash)
shield1 = Items("Shield+1",1,"Off-Hand")
shield1.addSkill(ShieldBash)
shield2 = Items("Shield+2",2,"Off-Hand")
shield2.addSkill(ShieldBash)
shield3 = Items("Shield+3",3,"Off-Hand")
shield3.addSkill(ShieldBash)
dagger = Items("Dagger",0,"Weapon")
dagger.addSkill(Poke)
dagger1 = Items("Dagger+1",1,"Weapon")
dagger1.addSkill(Poke)
dagger2 = Items("Dagger+2",2,"Weapon")
dagger2.addSkill(Poke)
dagger3 = Items("Dagger+3",3,"Weapon")
dagger3.addSkill(Poke)
holyBook = Items("Holy Book",0,"Off-Hand")
holyBook.addSkill(CureWounds)
holyBook1 = Items("Holy Book+1",1,"Off-Hand")
holyBook1.addSkill(CureWounds)
holyBook2 = Items("Holy Book+2",2,"Off-Hand")
holyBook2.addSkill(CureWounds)
holyBook3 = Items("Holy Book+3",3,"Off-Hand")
holyBook3.addSkill(CureWounds)
axe = Items("Axe",0,"Weapon")
axe.addSkill(Chop)
axe1 = Items("Axe+1",1,"Weapon")
axe1.addSkill(Chop)
axe2 = Items("Axe+2",2,"Weapon")
axe2.addSkill(Chop)
axe3 = Items("Axe+3",3,"Weapon")
axe3.addSkill(Chop)
mace = Items("Mace",0,"Weapon")
mace.addSkill(Slam)
mace1 = Items("Mace+1",1,"Weapon")
mace1.addSkill(Slam)
mace2 = Items("Mace+2",2,"Weapon")
mace2.addSkill(Slam)
mace3 = Items("Mace+3",3,"Weapon")
mace3.addSkill(Slam)
gloryHammer = Items("Hammer of Glory",0,"Weapon")
gloryHammer.addSkill(SolarBeam)
itemNames.pop(itemNames.index("Hammer of Glory"));ItemsList.pop(ItemsList.index(gloryHammer)) #Makes it so one-shot weapon cannot be bought
clothes = Items("Clothes",0,"Armor",0)
leatherArmor = Items("Leather Armor",1,"Armor",12)
ironArmor = Items("Iron Armor",2,"Armor",12)
steelArmor = Items("Steel Armor",3,"Armor",12)
apple = Items("Apple",4,"Healing",3)
appleStrudel = Items("Apple Strudel",8,"Healing",3)
applePie = Items("Apple Pie",16,"Healing",3)
watermelon = Items("Watermelon",1,"ArmorBuff",5)
watermelonSmoothie = Items("Watermelon Smoothie",2,"ArmorBuff",5)
watermelonSorbet = Items("Watermelon Sorbet",3,"ArmorBuff",5)

Characters = []
class Character: #Class for a character set up, intakes stats and default Health and Armor
    def __init__(self,name,dex,int,wis,str,health,armorclass,weapon = None,offhand = None,armor = clothes):
        self.name = name
        self.health = health
        self.maxHealth = health
        self.armorClass = armorclass
        self.gold = 0
        self.skills = []
        self.skillNames = []
        self.dex = dex
        self.str = int
        self.int = wis
        self.wis = str
        self.armor = armor
        self.weapon = weapon
        self.offhand = offhand
        self.appliedConditions = []
        self.appliedConditionsDict = {}
        self.items = []
        self.backpack = []
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
            self.addSkills(skill)
    def equipOffHand(self,newOffhand):
        oldOffHand = self.offhand
        self.offhand = newOffhand
        self.items.pop(self.items.index(newOffhand))
        self.items.append(oldOffHand)
        for skill in oldOffHand.skillList:
            if skill not in self.defaultClass.skills:
                self.skillNames.pop(skill)
                self.skills.pop(skill)
        for skill in self.offhand.skillList:
            self.addSkills(skill)
    def addItem(self, item):
        if item.type == "Healing" or item.type == "ArmorBuff":
            self.items.append(item)
        else:
            self.backpack.append(item)
#Below are default classes
Cleric = Character("Cleric",-1,0,2,1,53,16,mace,holyBook)
Cleric.addSkills(CureWounds);Cleric.addSkills(Slam);Cleric.addSkills(Smite)
Mage = Character("Mage",0,2,1,-1,45,14,wand)
Mage.addSkills(Burn);Mage.addSkills(Chill);Mage.addSkills(Zap)
Thief = Character("Thief",2,1,0,-1,47,15,dagger)
Thief.addSkills(Stab);Thief.addSkills(Slice);Thief.addSkills(Poke)
Warrior = Character("Warrior",1,-1,0,2,59,17,sword,shield)
Warrior.addSkills(ShieldBash);Warrior.addSkills(Chop);Warrior.addSkills(Slash)
