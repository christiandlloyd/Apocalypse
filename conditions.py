import random
random.seed
class Conditions:
    def __init__(self, name):
        self.name = name
        self.turns = 0
        self.damage = 0
        self.chance = 0
    def conditionProc(self):
        Proc = False
        if random.randint(1,100) <= self.chance:
            Proc = True
        return Proc

poisoned = Conditions("Poisoned",)
poisoned.turns = 4
poisoned.damage = 6
poisoned.chance = 75
grappled = Conditions("Grappled",)
grappled.turns = 2
grappled.chance = 50
frozen = Conditions("Frozen",)
frozen.turns = 1
frozen.chance = 65
burning = Conditions("Burning",)
burning.turns = 3
burning.damage = 4
burning.chance = 85