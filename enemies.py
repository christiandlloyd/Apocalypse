from class_and_item_list import *
import random
#names for bosses and mini-bosses.
def WarlockNameGen(): #Generates the Name for the warlock.
    warlock1 = ["Zarg", "Vil","Varth","Mor","Gul","Dorn","Hor", "Vorn","Zil","Ork"]
    warlock2 = ["a","e","i","o","u","y","oa","ua","ia","'"]
    warlock3 = ["thrax","vax","vixis", "dan","grol","zal","x","dol","xill","ks","lich"]
    return warlock1[random.randint(0,9)]+warlock2[random.randint(0,9)]+warlock3[random.randint(0,9)]
def demonNameGen():
    demon1 = ["Far", "Kor", "Yixx", "Lak", "Gulk", "Pul", "Gak", "Muck", "Sikk", "Schall"]
    demon2 = ["Virilliath", "Zilliax", "Noctus","Gulffus","Adolphus", "Alnor", "Orrgus", "Gorgus"]
    return demon1[random.randint(0,9)]+"'"+demon2[random.randint(0,7)]

warlockName = WarlockNameGen()
demonName = demonNameGen()


enemiesList = []
bossList = []
miniBossList =[]
class Enemy: #Class for enemies, sorts them into enemies and mini-bosses,as well as bosses
    def __init__(self,name,health,armorclass,int,dex,str,wis,text,named = False,mini = False):
        self.health = health
        self.armorClass = armorclass
        self.skills = []
        self.appliedConditions = []
        self.appliedConditionsDict = {}
        self.text = text + "\n"
        self.int = int
        self.dex = dex
        self.str = str
        self.wis = wis
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
        self.appliedConditionsDict[condition.name] = condition.turns
    def remCondition(self, condition):
        self.appliedConditions.pop(self.appliedConditions.index(condition))
        self.appliedConditionsDict.pop(condition.name)
    def addSkills(self, skill1):
        self.skills.append(skill1)

        #Bosses get 5 skills, Mini 4, regular 3/2
warlock = Enemy(warlockName,100,18,3,-3,-3,-3,"The wicked sorcerer stands before you, holding up his evil pact blade, as he begins his dread incantation. You hold your weapons aloft, and he scowls at you. 'Pathetic Mortal,' he hisses,'you are too late. The solar conjunction is at hand, and my master's arrival is inevitable!' he turns to face you, the countdown to universal annihilation has begun!",True)
warlock.addSkills(EldritchBlast);warlock.addSkills(Decay);warlock.addSkills(RitualChant);warlock.addSkills(Burn);warlock.addSkills(Zap)
mainDemon = Enemy(demonName,999,25,4,4,4,4,"The ritual is completed, it all comes down to this. the evil warlock, " +warlockName+" shouts in glee. 'My dark master has returned to slay the universe, behold, you now face the might of "+demonName+"!' As the wicked form of this towering demon enters the battle field, the sorcerer "+warlockName+" is vaporized into liquid dust by the sheer energy of this vile hell beast. You are the final line of defence that will decide the fate of humanity. This is the epic fight to end all fights. Let slaughter commence!",True)
mainDemon.addSkills(EldritchBlast);mainDemon.addSkills(Decay);mainDemon.addSkills(Burn),mainDemon.addSkills(Chop),mainDemon.addSkills(Zap)
goblin = Enemy("Goblin",15,12,0,2,-4,-4,"You enter a small clearing, filled with trash and viscera, and see a wicked, green goblin. It snarls at you, and rushes you with it's dagger. Let battle commence!")
goblin.addSkills(Poke);goblin.addSkills(Claw);goblin.addSkills(Bite)
orc = Enemy("Orc",26,14,-4,0,2,-4,"You enter a large clearing, corpses, armor, weapons, and bones litering the floor, as a large orc smiles. 'FRESH MEAT' he shouts, hoisting his axe, turning to you. Let battle commence!")
orc.addSkills(Slash);orc.addSkills(Bite)
imp = Enemy("Imp",12,11, 2,2,0,0,"The room warms up as you enter, and a distinct scent of the hells pollutes your nose. You turn and see an imp, 'Bah!' it screams,'Nasty humanses in my home again! Kill,kill,kill!' Let battle commence!")
imp.addSkills(EldritchBlast)
skeleton = Enemy("Skeleton", 10,8,0,0,0,0,"As you enter this room, you see a pile of bones on the ground, which suddenly begin to rise and reform into a wicked skeleton. Let battle commence!")
skeleton.addSkills(Bite); skeleton.addSkills(Claw)
troll = Enemy("Troll",25,16,-4,-3,2,0,"The worst stench ever smelled eminates from this room, as a wicked troll stand before you, drooling a green slime as it prepares to fight. Let battle commence!")
troll.addSkills(Slam);troll.addSkills(Claw)
zombie = Enemy("Zombie",11,8,0,0,0,0,"From a pile of corpses, one begins to rise. A zombie groans as it slowly marches toward you. Let battle commence!")
zombie.addSkills(Bite); zombie.addSkills(Claw)


lesserLich = Enemy("sample",30,17,4,0,2,1,"The floor is littered with the corpses of heroes and undead alike. Before you is a wicked reliquary, eminating death and decay, which can only mean it is a phylactery. Rising from the bones of the dead appears to you a lich. 'My master will not fail!' he says, preparing his vile spells. Let battle commence!",True,True) #There will be a name gen in the map generator that gives these guys names.
lesserLich.addSkills(Decay);lesserLich.addSkills(Burn);lesserLich.addSkills(Chill);lesserLich.addSkills(Zap)
lesserDemon = Enemy("sample",45,18,0,2,4,1,"This room burns, reeking of the stench of hell, as a chaos portal opens, and the walls turn red and scream. From the abyss, a demon exits, and snarls.'My dark master will return to this world, and destroy the universe' it bellows. 'He shall not be stopped!' Let battle commence!",True,True)
lesserDemon.addSkills(Chop);lesserDemon.addSkills(Claw);lesserDemon.addSkills(Burn);lesserDemon.addSkills(EldritchBlast)