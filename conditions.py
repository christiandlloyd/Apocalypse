import random
random.seed
class Conditions:
    def __init__(self, name,turns,chance, damage = 0):
        self.name = name
        self.turns = turns
        self.damage = damage
        self.chance = chance
    def conditionProc(self):
        Proc = False
        if random.randint(1,100) <= self.chance:
            Proc = True
        return Proc

poisoned = Conditions("Poisoned",4,75,6)
grappled = Conditions("Grappled",2,50)
frozen = Conditions("Frozen",1,65)
burning = Conditions("Burned",3,8,85)
