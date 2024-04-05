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
applyPoison = random.randrange(0,1) #Just checks if poison needs to be added to damage
grappled = random.randint(0,1) #Checks if enemy is grappled

failedInput = "Input not recognized." #General failed input message


#Below are default classes
Mage ={"Health" : 15, "ArmorClass" : 14, "Skills":{"Burn":{"Damage":10,"Bonus": 2},"Zap":{"Damage":12,"Bonus": 1},"Chill":{"Damage":8,"Bonus": 3}}, "Stats":{"Dex":0,"Str":-1,"Wis":1,"Int":2}}
Theif ={"Health" : 17, "ArmorClass" : 17, "Skills":{"Stab":{"Damage":10,"Bonus": 3},"Slice":{"Damage":8,"Bonus": 4},"Poisoned Blade":{"Damage":12,"Bonus": 4, "Status": applyPoison}}, "Stats":{"Dex":2,"Str":0,"Wis":-1,"Int":1}}
Cleric = {"Health" : 20, "ArmorClass" : 16, "Skills":{"Hammer Slam":{"Damage":8,"Bonus": 3},"Smite":{"Damage":10,"Bonus": 2},"Cure Wounds":{"Healing": 8}}, "Stats":{"Dex":-1,"Str":1,"Wis":2,"Int":0}}
Warrior = {"Health" : 24, "ArmorClass" : 15, "Skills":{"Wrestle":{"Status": grappled,"Bonus": 2},"Shield Bash":{"Damage":12,"Bonus": 1},"Slash":{"Damage":10,"Bonus": 3}}, "Stats":{"Dex":1,"Str":2,"Wis":0,"Int":-1}}
Characters = {"mage": Mage,"cleric": Cleric,"warrior": Warrior,"theif": Theif}

#Generates name for warlock
warlock1 = ["Zarg", "Vil","Varth","Mor","Gul","Dorn","Hor", "Vorn","Zil","Org"]
warlock2 = ["a","e","i","o","u","y","oa","ua","ia","'"]
warlock3 = ["thrax","vax","vixis", "dan","grol","zal","x","dol","xill","ks","lich"]
warlockName = warlock1[random.randint(0,9)]+warlock2[random.randint(0,9)]+warlock3[random.randint(0,9)]

#Generates Demon Name
demon1 = ["Far", "Kor", "Yixx", "Lak", "Gulk", "Pul", "Gak", "Muck", "Sikk", "Schall"]
demon2 = ["Virilliath", "Zilliax", "Noctus","Gulffus","Adolphus", "Alnor", "Orrgus", "Gorgus"]
demonName = demon1[random.randint(0,9)]+"'"+demon2[random.randint(0,7)]

print("Welcome to 'Apocalypse!' An evil sorcerer,", warlockName,"threatens to destroy the kingdom of Gorroth, and in the hills of Ghomshief lies a cave where he begins a dark ritual to summon the demon",demonName+".")

#Determines player's default class. While loop lets them confirm their class, and select another class if need be.
print("It is up to you to stop him, hero, lest the universe fall into the hands of evil once more.")
while True:
     playerClassName = input("To begin your journey, select one of the following classes: Cleric, Mage, Thief, Warrior.\n").lower()
     if playerClassName not in Characters.keys():
         print("That is not an available class, please try again.")
         continue
     else:
        while True:
            print("You have selected", playerClassName.title()+", is that correct? Y/n")
            confirmed = input().lower()
            if confirmed == "y":
                print("Welcome,",playerClassName.title()+", let us begin your journey...")
                break
            elif confirmed == "n":
                print("Please select another class, then.")
                break
            else:
                print(failedInput)
                continue
        if confirmed == "y":
            break
        else:
            continue
         

