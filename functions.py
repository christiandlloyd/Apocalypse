import random
from class_and_item_list import *
import sys,time
def prints(string,str1="",str2="",str3="",str4="",str5=""):#Causes text to print slowly
    string = str(string)+ str(str1) + str(str2) + str(str3) + str(str4 )+ str(str5)
    for letter in string:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.01)
failedInput = "No valid input detected."
random.seed()
def d(a): #rolls a dice. a will typically be 2,4,6,8,10,12,20, or 100.
    return random.randint(1,a)
def attack(skill, armorclass = 10): #This is how we roll attacks
    roll = d(20)
    if (roll+skill.bonus -7 >= armorclass): #Critical Hit
        prints("Criticial Hit!")
        return 2
    elif (roll+skill.bonus>= armorclass):
        return 1
    else:
        return 0
def damage (skill): #How damage is determined
    return(d(skill.damage)+ skill.bonus)
def startGame(): #Start of game loop where the player selects characters
    while True:
     prints("To begin your journey, select one of the following classes: Cleric, Mage, Thief, Warrior. Or, you may type 'main menu' to return to the main menu.\n")
     playerClassName = input().lower()
     if playerClassName == "main menu":
         MainMenu()
         break
     else:
        for defaultClass in Characters:
           if playerClassName == defaultClass.name.lower():
              playerClass = defaultClass
        while True:
            prints("You have selected ", playerClassName.title()+", is that correct? Y/n\n")
            confirmed = input().lower()
            if confirmed == "y":
                text = "Welcome, "+playerClassName.title()+", let us begin your journey..."
                prints(text)
                break
            elif confirmed == "n":
                prints("Please select another class, then.")
                break
            else:
                prints(failedInput)
                continue
        if confirmed == "y":
            break
        else:
            continue
    return playerClass

def MainMenu(): #Opens a main menu function
    while True:
        prints("Would you like to 'Start' a game, or 'Exit' the program?\n")
        command = input().lower()
        if command == "start":
            return startGame()
        elif command == "exit":
            exit()
        else:
            prints(failedInput)
            continue
def GenerateMap(): #Generates a 11x11 map for the player to navigate. Row 11 column 6 will always have the boss
  map = []
  roomTypes = ["Monster","Treasure","Rest","Shop","Mini-Boss",]
  row = []
  for x in range(11):
    if x == 5:
      row.append("Start Room")
    else:
      row.append(roomTypes[random.randint(0,4)])
  map.append(row)
  for x in range(9):
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
  map[random.randint(1,9)][random.randint(0,10)] = "Mystical Shrine"
  return map
def WarlockNameGen(): #Generates the Name for the warlock.
    warlock1 = ["Zarg", "Vil","Varth","Mor","Gul","Dorn","Hor", "Vorn","Zil","Ork"]
    warlock2 = ["a","e","i","o","u","y","oa","ua","ia","'"]
    warlock3 = ["thrax","vax","vixis", "dan","grol","zal","x","dol","xill","ks","lich"]
    return warlock1[random.randint(0,9)]+warlock2[random.randint(0,9)]+warlock3[random.randint(0,9)]
def demonNameGen():
    demon1 = ["Far", "Kor", "Yixx", "Lak", "Gulk", "Pul", "Gak", "Muck", "Sikk", "Schall"]
    demon2 = ["Virilliath", "Zilliax", "Noctus","Gulffus","Adolphus", "Alnor", "Orrgus", "Gorgus"]
    return demon1[random.randint(0,9)]+"'"+demon2[random.randint(0,7)]
def CombatLoop(player, enemy): #Combat Loop
   while True:
    if player.health <= 0: #Checks if Player is dead before their turn
        prints("You're body collapses, as your wounds overtake you. You have been defeated this day. Would you like to return to the 'Main Menu' or 'Exit' the game?\n")
        a = input().lower
        while True:
            if a == "main menu":
                MainMenu()
                break
            elif a == "exit":
                exit()
            else:
                prints(failedInput)
                continue
        break
    else:
        prints("The " + enemy.name + " stands before you, would you like to use a 'Skill' or an 'Item'?\n")
        a = input().lower()
        if a == "skill":
            prints("Which skill would you like to use?\n")
            for skill in player.skillNames:
               prints(skill,"\n")
            skillUsed = input().title()
            if skillUsed in player.skillNames:
                if player.skills[skillUsed].type == "Healing":
                    player.health += d(player.skills[skillUsed].healing)
                else:
                   owie = attack(player.skills[skillUsed],enemy.armorClass) * damage(player.skills[skillUsed])
                   enemy.health -= owie
                   prints("The ",enemy.name," took ", owie, " damage!\n")
                if player.skills[skillUsed].conditions != []:
                    if player.skills[skillUsed].conditions.conditionProc():
                       enemy.appliedConditions.append(player.skills[skillUsed].conditions)
                       prints("The ",enemy.name," is now ",player.skills[skillUsed].conditions.name,"!\n")

                   
            


