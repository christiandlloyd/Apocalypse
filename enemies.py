from class_and_item_list import *
from functions import *
#names for bosses and mini-bosses.

warlockName = WarlockNameGen()
demonName = demonNameGen()


enemiesList = []
bossList = []
miniBossList =[]
class Enemy: #Class for enemies, sorts them into enemies and mini-bosses,as well as bosses
    def __init__(self,name,health,armorclass,named = False,mini = False):
        self.health = health
        self.armorClass = armorclass
        self.skills = {}
        self.skillNames = []
        self.appliedConditions = []
        if named and mini:
            self.name = name
            miniBossList.append(self)
        elif named and not mini:
            self.name = name
            bossList.append(self)
        else:
            self.name = "The " + name
            enemiesList.append(self)
        
    def addCondition(self, condition):
        self.appliedConditions.append(condition)
    def remCondition(self, condition):
        self.appliedConditions.pop(condition)
    def addSkills(self, skill1):
        self.skills[skill1.name] = skill1

        #Bosses get 5 skills, Mini 4, regular 3/2
warlock = Enemy(warlockName,100,18,True)
warlock.addSkills(EldritchBlast);warlock.addSkills(Decay);warlock.addSkills(RitualChant);warlock.addSkills(Burn);warlock.addSkills(Zap)
mainDemon = Enemy(demonName,999,25,True)
mainDemon.addSkills(EldritchBlast);mainDemon.addSkills(Decay);mainDemon.addSkills(Burn),mainDemon.addSkills(Chop),mainDemon.addSkills(Zap)
goblin = Enemy("Goblin",15,12)
goblin.addSkills(Poke);goblin.addSkills(Claw);goblin.addSkills(Bite)
orc = Enemy("Orc",26,14)
orc.addSkills(Slash);orc.addSkills(Bite)
imp = Enemy("Imp",12,11)
imp.addSkills(EldritchBlast)
skeleton = Enemy("Skeleton", 10,8)
skeleton.addSkills(Bite); skeleton.addSkills(Claw)
troll = Enemy("Troll",25,6)
troll.addSkills(Slam);troll.addSkills(Claw)
zombie = Enemy("Zombie",11,8)
zombie.addSkills(Bite); zombie.addSkills(Claw)


lesserLich = Enemy("sample",30,17,True,True) #There will be a name gen in the map generator that gives these guys names.
lesserLich.addSkills(Decay);lesserLich.addSkills(Burn);lesserLich.addSkills(Chill);lesserLich.addSkills(Zap)
lesserDemon = Enemy("sample",45,18,True,True)
lesserDemon.addSkills(Chop);lesserDemon.addSkills(Claw);lesserDemon.addSkills(Burn);lesserDemon.addSkills(EldritchBlast)