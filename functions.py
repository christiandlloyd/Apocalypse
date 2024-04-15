import random
import class_and_item_list

failedInput = "No valid input detected."
random.seed()
def d(a): #rolls a dice. a will typically be 2,4,6,8,10,12,20, or 100.
    return random.randint(1,a)
def attack(activeClass,skill, armorclass = 10): #This is how we roll attacks
    if (d(20)+activeClass["Skills"][skill]["Bonus"] -7 >= armorclass): #Critical Hit
        return 2
    elif (d(20)+activeClass["Skills"][skill]["Bonus"] >= armorclass):
        return 1
    else:
        return 0
def damage (activeClass,skill): #How damage is determined
    return(d(activeClass["Skills"][skill]["Damage"]))
def startGame(): #Start of game loop where the player selects characters
    while True:
     global playerClassName
     playerClassName = input("To begin your journey, select one of the following classes: Cleric, Mage, Thief, Warrior.\n").lower()
     if playerClassName == "main menu":
         MainMenu()
         break
     if playerClassName not in class_and_item_list.Characters.keys():
         print(failedInput)
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
    return

def MainMenu(): #Opens a main menu function
    while True:
        command = input("Would you like to 'Start' a game, or 'Exit' the program?\n").lower()
        if command == "start":
            startGame()
            break
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
