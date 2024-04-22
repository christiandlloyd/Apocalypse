import random
from class_and_item_list import *
import sys,time
def prints(string,str1="",str2="",str3="",str4="",str5="",str6 ="",str7 ="",str8 =""):#Causes text to print slowly
    string = str(string)+ str(str1) + str(str2) + str(str3) + str(str4 )+ str(str5) +str(str6)+str(str7)+str(str8)
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
def healing (skillbonus,player, skillroll = 0):
    if skillroll !=0:
        healed = d(skillroll) + skillbonus
    else:
        healed = skillbonus
    player.health += healed
    if player.health > player.maxHealth:
        player.health = player.maxHealth
    prints("You healed ",str(healed),"! You are now at ", str(player.health)," health!")
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
shopFirstVisit = True
def Shop():
    global shopFirstVisit
    if shopFirstVisit:
        prints("You see before you a rickety looking market stall, with a few items on it. Sleeping in a chair behind the stall lies a small, gnomish woman, with pale white skin and short red hair.You tap your finger on the stall, and she shoots up, dusting herself off. 'Greetings, traveler!' she hoots, wide grin on her face. 'My name is Nimsey, and welcome to Nimsey's Wonderous Emporium! Everything you see is available to buy, and, just like any good merchant, I deal in gold and gold alone.\n")
        shopFirstVisit = False
    prints("'So, what can I get for you? Finest goods this side of the Korgarami River!' Nimsey says, with a wink.\nWould you like to 'view' her wares, or 'leave?'")

def GenerateMap(): #Generates a 11x11 map for the player to navigate. Row 11 column 6 will always have the boss
  map = {}
  mysticalShrineCoords = (random.randint(1,9),random.randint(0,10))
  roomTypes = [Monster(),Treasure(),Rest(),Shop(),Mini-Boss(),]
  for x in range(11):
    for y in range(11):
        if (x,y) == (0,5):
            map[(x,y)] = StartRoom()
        elif (x,y) ==(10,5):
            map[(x,y)] == FinalBoss()
        elif (x,y) == mysticalShrineCoords:
            map[(x,y)] == MysticalShrine()
        else:
            map[(x,y)] == roomTypes[random.randint(0,4)]
  return map

def Movement(map,startSquare): #Function for moving around the map
    movesDict = {"North":(1,0),"South":(-1,0),"East":(0,1),"West":(0,-1)}
    while True:
        movesList = ["North","South","East","West"]
        if startSquare[0] == 0:
            movesList.pop("South")
        if startSquare[0] == 10:
            movesList.pop("North")
        if startSquare[1] == 0:
            movesList.pop("West")
        if startSquare[1] == 10:
            movesList.pop("East")
        prints("Would you like to move ")
        for direction in movesList:
            if movesList.index(direction) == movesList.len()-1:
                prints("or ",direction, "?\n")
            else:
                prints(direction, ", ")
        move = input().title()
        startSquare = (startSquare[0]+movesDict[move][0],startSquare[1]+movesDict[move][1])
        map[startSquare]

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
   ACBuff = 0
   while True:
    itemsAvailable = []
    if player.appliedConditions != []:
        for condition in condition:
                player.appliedConditions[condition]-= 1
                if player.aplliedConditions[condition] == 0:
                    player.remCondition(condition)
                if condition.damage > 0:
                    conditionDamage = d(condition.damage)
                    enemy.health -= conditionDamage
                    prints(enemy.name, " took ", str(conditionDamage)," damage from being ",condition.name,"!\n")
                if condition == conditions.frozen or conditions.grappled: #Frozen and Grappled cause a turn skip. Yes, this does mean you could stun lock an enemy
                    prints("You are ", condition.name, " and cannot move!")
                    continue
    if player.health <= 0: #Checks if Player is dead before their turn
        prints("You're body collapses, as your wounds overtake you. You have been defeated this day. Would you like to return to the 'Main Menu' or 'Exit' the game?\n")
        a = input().lower()
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
        prints(enemy.name + " stands before you, would you like to use a 'Skill' or an 'Item'?\n")
        a = input().lower() #Player always goes first
        if a == "skill":
            prints("Which skill would you like to use?\n")
            for skill in player.skillNames:
               prints(skill,"\n")
            skillUsed = input().title()
            if skillUsed in player.skillNames:
                action = player.skills[player.skillNames.index(skillUsed)]
                if action.type == "Healing":
                    healing(action.healing,action.bonus,player)
                else:
                   owie = attack(action,enemy.armorClass) * damage(action)
                   enemy.health -= owie
                if owie == 0:
                    prints("You Missed!")
                else:
                    prints(enemy.name," took ", owie, " damage!\n")
                    if player.skills[skillUsed].conditions != []:
                        for condition in player.skills[skillUsed].conditions:
                            if condition.conditionProc():
                                enemy.appliedConditions.append(condition)
                                prints("The ",enemy.name," is now ",condition.name,"!\n")
        if a == "item":
            while True:
                prints("Which item would you like to use? Or, type 'back' to go back.\n")
                for item in player.items:
                    itemsAvailable.append[item.name]
                    prints(item.name, "\n")
                itemUsed = input().title
                if itemUsed not in itemsAvailable:
                    prints(failedInput)
                if itemUsed == "Back":
                    break
                else:
                    itemConsumed = player.items[itemsAvailable.index(itemUsed)]
                    if itemConsumed.type == "ArmorBuff":
                        ACBuff += itemConsumed.bonus
                        player.items.pop(itemsAvailable.index(itemUsed))
                    if itemConsumed.type == "Healing":
                        healing(0,itemConsumed.bonus,player)
        else:
            prints(failedInput)                
            continue
        #Condition Check on Enemy
        if enemy.conditions != []:
            for condition in condition:
                enemy.appliedConditions[condition]-= 1
                if enemy.aplliedConditions[condition] == 0:
                    enemy.remCondition(condition)
                if condition.damage > 0:
                    conditionDamage = d(condition.damage)
                    enemy.health -= conditionDamage
                    prints(enemy.name, " took ", str(conditionDamage)," damage from being ",condition.name,"!\n")
                if condition == conditions.frozen or conditions.grappled: #Frozen and Grappled cause a turn skip. Yes, this does mean you could stun lock an enemy
                    prints(enemy.name," is ", condition.name, " and cannot move!")
                    continue
        if enemy.health <= 0:
            prints(enemy.name," has been slain. Victory is yours this day.")
            break
        else: #Enemy does an attack
            enemySkillUsed = enemy.skills[enemy.skillNames[random.randint(0,enemy.skillList.len()-1)]]
            playerAttacked = attack(player.skills[skillUsed],player.armorClass) * damage(player.skills[skillUsed])
            player.health -= playerAttacked
            if playerAttacked == 0:
                prints(enemy.name, " missed!")
            else:
                if enemySkillUsed.conditions != []:
                    for condition in enemySkillUsed.conditions:
                        if condition.conditionProc():
                            player.appliedConditions.append(condition)
                            prints("You are now ",condition.name,"!\n")
            


