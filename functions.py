import random
import class_and_item_list

failedInput = "No valid input detected."
random.seed()
def d(a): #rolls a dice. a will typically be 2,4,6,8,10,12,20, or 100.
    return random.randint(1,a)
def attack(activeClass,skill, armorclass = 10): #This is how we roll attacks
    if (d(20)+activeClass.skills.skill.bonus -7 >= armorclass): #Critical Hit
        return 2
    elif (d(20)+activeClass["Skills"][skill]["Bonus"] >= armorclass):
        return 1
    else:
        return 0
def damage (activeClass,skill): #How damage is determined
    return(d(activeClass["Skills"][skill]["Damage"]))
def startGame(): #Start of game loop where the player selects characters
    while True:
     playerClassName = input("To begin your journey, select one of the following classes: Cleric, Mage, Thief, Warrior. Or, you may type 'main menu' to return to the main menu.\n").lower()
     if playerClassName == "main menu":
         MainMenu()
         break
     else:
        for defaultClass in class_and_item_list.Characters:
           if playerClassName == defaultClass.name.lower():
              playerClass = defaultClass
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
    return playerClass

def MainMenu(): #Opens a main menu function
    while True:
        command = input("Would you like to 'Start' a game, or 'Exit' the program?\n").lower()
        if command == "start":
            return startGame()
        elif command == "exit":
            exit()
        else:
            print(failedInput)
            continue
def GenerateMap(): #Generates a 11x11 map for the player to navigate. Row 11 column 6 will always have the boss
  map = []
  roomTypes = ["Monster","Treasure","Rest","Shop","Mini-Boss"]
  for x in range(10):
    row = []
    for column in range(11):
      row.append(roomTypes[random.randint(0,4)])
    map.append(row)
  row = []
  for x in range(11):
    if x == 5:
      row.append("Final-Boss")
    else:
      row.append(roomTypes[random.randint(0,4)])
  map.append(row)
  return map
def WarlockNameGen(): #Generates the Name for the warlock.
    warlock1 = ["Zarg", "Vil","Varth","Mor","Gul","Dorn","Hor", "Vorn","Zil","Org"]
    warlock2 = ["a","e","i","o","u","y","oa","ua","ia","'"]
    warlock3 = ["thrax","vax","vixis", "dan","grol","zal","x","dol","xill","ks","lich"]
    return warlock1[random.randint(0,9)]+warlock2[random.randint(0,9)]+warlock3[random.randint(0,9)]
def demonNameGen():
    demon1 = ["Far", "Kor", "Yixx", "Lak", "Gulk", "Pul", "Gak", "Muck", "Sikk", "Schall"]
    demon2 = ["Virilliath", "Zilliax", "Noctus","Gulffus","Adolphus", "Alnor", "Orrgus", "Gorgus"]
    return demon1[random.randint(0,9)]+"'"+demon2[random.randint(0,7)]