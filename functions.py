import random
random.seed()
def d(a): #rolls a dice. a will typically be 2,4,6,8,10,12,20, or 100.
    return random.randint(1,a)
def attack(attackBonus, armorclass = 10): #This is how we roll attacks
    if (d(20)+attackBonus -7 < armorclass): #Critical Hit
        return 2
    elif (d(20)+attackBonus < armorclass):
        return 1
    else:
        return 0
