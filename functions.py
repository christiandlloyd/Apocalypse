import random
from class_and_item_list import *
import sys,time
from enemies import *
def LevelUpCheck(player):
    while player.levelUpXP >= 2^player.level:
            prints("You have leveled up! You have gained ",round(player.health*.125)," health and can increase one of your stats by 1 point! Choose between 'int,''dex,''wis,' and 'str' to upgrade!\n")
            a = input().lower()
            if a == "int":
                player.int += 1
            if a == "dex":
                player.dex += 1
            if a == "str":
                player.str += 1
            if a == "wis":
                player.wis += 1
            else:
                prints(failedInput)
            player.levelUpXP -= 2^player.level
            player.level += 1

def prints(string,str1="",str2="",str3="",str4="",str5="",str6 ="",str7 ="",str8 =""):#Causes text to print slowly
    string = str(string)+ str(str1) + str(str2) + str(str3) + str(str4 )+ str(str5) +str(str6)+str(str7)+str(str8)
    for letter in string:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.01)
failedInput = "No valid input detected.\n"
random.seed()
def d(a): #rolls a dice. a will typically be 2,4,6,8,10,12,20, or 100.
    return random.randint(1,a)
def attack(player,skill, armorclass = 10): #This is how we roll attacks
    skillTypeBonus = {"Magic":player.int,"Dex":player.dex,"Str":player.str,"Holy":player.wis}
    roll = d(20)
    if (roll+skill.bonus -7 + skillTypeBonus[skill.type] >= armorclass): #Critical Hit
        prints("Criticial Hit!\n")
        return 2
    elif (roll+skill.bonus>= armorclass):
        return 1
    else:
        return 0
def damage (player,skill,): #How damage is determined
    skillTypeBonus = {"Magic":player.int,"Dex":player.dex,"Str":player.str,"Holy":player.wis}
    return(d(skill.damage)+ skill.bonus + skillTypeBonus[skill.type])
def healing (skillbonus,player, skillroll = 1):
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
                text = "Welcome, "+playerClassName.title()+", let us begin your journey...\n"
                prints(text)
                Movement(GenerateMap(),playerClass)
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


def MainMenu(): #Opens a main menu function
    while True:
        prints("Would you like to 'Start' a game, or 'Exit' the program?\n")
        command = input().lower()
        if command == "start":
            startGame()
            break
        elif command == "exit":
            exit()
        else:
            prints(failedInput)
            continue
shopFirstVisit = True
def CombatLoop(player,enemy): #Combat Loop
   ACBuff = 0
   global game
   global RitualCount #For the warlock summoning the demon
   RitualCount = 0
   while True:
    if RitualCount == 6:
        break
    itemsAvailable = []
    if player.appliedConditions != []:
        for condition in player.appliedConditions:
                player.appliedConditionsDict[condition.name]-= 1
                if player.appliedConditionsDict[condition.name] == 0:
                    player.remCondition(condition)
                if condition.damage > 0:
                    conditionDamage = d(condition.damage)
                    player.health -= conditionDamage
                    prints("You took ", conditionDamage," damage from being ",condition.name,"!\n")
                if condition == conditions.frozen or conditions.grappled: #Frozen and Grappled cause a turn skip. Yes, this does mean you could stun lock an enemy
                    prints("You are ", condition.name, " and cannot move!")
                    continue
    if player.health <= 0: #Checks if Player is dead before their turn
        prints("You're body collapses, as your wounds overtake you. You have been defeated this day. Would you like to return to the 'Main Menu' or 'Exit' the game?\n")
        game = False
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
                prints("You used ",skillUsed, "!\n")
                action = player.skills[player.skillNames.index(skillUsed)]
                if action.type == "Healing":
                    healing(action.healing,action.bonus,player)
                else:
                   owie = attack(player,action,enemy.armorClass,) * damage(player,action)
                   enemy.health -= owie
                if owie == 0:
                    prints("You Missed!\n")
                else:
                    prints(enemy.name," took ", owie, " damage!\n")
                    if player.skills[player.skillNames.index(skillUsed)].conditions != []:
                        for condition in player.skills[player.skillNames.index(skillUsed)].conditions:
                            if condition.conditionProc():
                                enemy.addCondition(condition)
                                prints(enemy.name," is now ",condition.name,"!\n")
            else:
                prints(failedInput)
        elif a == "item":
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
        if enemy.appliedConditions != []:
            for condition in enemy.appliedConditions:
                enemy.appliedConditionsDict[condition.name]-= 1
                if enemy.appliedConditionsDict[condition.name] == 0:
                    enemy.remCondition(condition)
                if condition.damage > 0:
                    conditionDamage = d(condition.damage)
                    enemy.health -= conditionDamage
                    prints(enemy.name, " took ", str(conditionDamage)," damage from being ",condition.name,"!\n")
                if condition == conditions.frozen or conditions.grappled: #Frozen and Grappled cause a turn skip. Yes, this does mean you could stun lock an enemy
                    prints(enemy.name," is ", condition.name, " and cannot move!\n")
                    exit()
        if enemy.health <= 0:
            prints(enemy.name," has been slain. Victory is yours this day.\n")
            break
        else: #Enemy does an attack
            enemySkillUsed = enemy.skills[random.randint(0,len(enemy.skills)-1)]
            prints(enemy.name," used ",enemySkillUsed.name,"!\n")
            if enemySkillUsed == RitualChant:
                RitualCount += 1
                continue
            playerAttacked = attack(enemy,enemySkillUsed,player.armorClass,) * damage(enemy,enemySkillUsed)
            player.health -= playerAttacked
            if playerAttacked == 0:
                prints(enemy.name, " missed!\n")
            else:
                prints("You took ",playerAttacked," damage!\n")
                if enemySkillUsed.conditions != []:
                    for condition in enemySkillUsed.conditions:
                        if condition.conditionProc():
                            player.appliedConditions.append(condition)
                            prints("You are now ",condition.name,"!\n")
## Below are event functions
def Shop(player):
    global shopFirstVisit
    nimseyInventory = []
    for x in range(5):
            nimseyInventory.append(itemNames[random.randint(0,len(itemNames)-1)])
    if shopFirstVisit:
        prints("You see before you a rickety looking market stall, with a few items on it. Sleeping in a chair behind the stall lies a small, gnomish woman, with pale white skin and short red hair.You tap your finger on the stall, and she shoots up, dusting herself off. 'Greetings, traveler!' she hoots, wide grin on her face. 'My name is Nimsey, and welcome to Nimsey's Wonderous Emporium! Everything you see is available to buy, and, just like any good merchant, I deal in gold and gold alone.\n")
        shopFirstVisit = False
    prints("'So, what can I get for you? Finest goods this side of the Korgarami River!' Nimsey says, with a wink.\nWould you like to 'view' her wares, or 'leave?'\n")
    while True:
        a = input().lower()
        b = ''
        if a == "view":
            prints("Well, I've got these for sale! Take a look!\n")
            while True:
                prints("Nimsey has the following items for sale:\n")
                for item in nimseyInventory:
                    prints(item,", which costs ",ItemsList[itemNames.index(item)].cost,"\n")
                prints("Select an item to buy, you may also 'leave.'\n")
                b = input().title()
                if b in nimseyInventory and player.gold >= ItemsList[itemNames.index(b)].cost:
                    player.items.append(ItemsList[itemNames.index(b)])
                    player.gold -= ItemsList[itemNames.index(b)].cost
                    nimseyInventory.pop(nimseyInventory.index(b))
                    prints("'Thank you for your purchase!' Nimsey says, with a smile.\n")
                    continue
                elif b in nimseyInventory and player.gold < ItemsList[itemNames.index(b)].cost:
                    prints("'Sorry, bub, but you don't have enough gold to buy that item.' she says \n")
                    continue
                elif b == "Leave":
                    break
                else:
                    prints(failedInput)
                    continue
        if a == "leave" or b == "Leave":
            prints("'See ya later!' Nimsey says, packing up her stall.\n")
            break
        else:
            prints(failedInput)
            continue
def Monster(player):
    enemy = enemiesList[random.randint(0,len(enemiesList)-1)]

    prints(enemy.text,"\n")
    CombatLoop(player,enemy)
    player.levelUpXP += 4
def MiniBoss(player):
    randomGen = random.randint(0,1)
    enemy = miniBossList[randomGen]
    if randomGen == 0:
        enemy.name = WarlockNameGen()
        while enemy.name == warlockName:
            enemy.name = WarlockNameGen()
    else:
        enemy.name = demonNameGen()
        while enemy.name == demonName:
            enemy.name = demonNameGen()
    prints(enemy.text)
    CombatLoop(player, enemy)
    player.levelUpXP += 20
def StartRoom(player):
    prints("The entrance to the cave opens before you, and as you enter, an eerie feeling sets in. Unholy might fills the caverns, as the blood stains on the walls foretell doom. You resolve yourself, with a heart pure as steel, and look at the paths before you.\n")
    player.gold += 10
def Treasure(player):
    goldGained = d(4)+d(4)+d(4)+d(4)+d(4)+d(4)
    itemInChest = ItemsList[random.randint(0,len(ItemsList)-1)]
    prints("Before you lies a large, wooden box with a hatch on it. Instinctively, you open it, revealing the treasure inside.\nYou gained ",goldGained," gold and a ",itemInChest.name,"!\n")
    player.gold += goldGained
    player.addItem(itemInChest)
    player.levelUpXP += 2
    
def Rest(player):
    equipdict = {"Off-Hand":player.equipOffHand,"Armor":player.equipArmor,"Weapon":player.equipWeapon}
    prints("At the end of this tunnel, you find a cozy, lit campfire with an empty bedroll set down. After careful inspection, it appears to be fine.\n")
    while True:
        prints("Would you like to 'rest,' or view your 'inventory?' Or, you may also 'leave' this campfire.\n")
        g = input().lower()
        if g == "rest":
            player.health = player.maxHealth
            prints("You awaken feeling well rested. The campfire is snubbed out, and it is time to continue your journey.\n")
            break
        elif g == "inventory":
            while True:
                prints("You have the following items in your backpack:\n") 
                names = []
                for item in player.backpack:
                    prints(item.name,"\n")
                    names.append(item.name)
                    prints("Would you like to equip any items? Or, type 'back' to go back.\n")
                    name = input().title()
                if name in names:
                    prints("You have sucessfully equipped the ",name,"!\n")
                    equipdict[item.type](player.backpack[names.index(name)])
                elif name == "back":
                    break
                else:
                    prints(failedInput)
                    continue
        elif g == "leave":
            break
        else:
            prints(failedInput)
            continue
def Empty(player):
    prints("This room is empty. Seems you've already visited it.\n")

def FinalBoss(player):
    prints(warlock.text)
    CombatLoop(player,warlock)
    if RitualCount == 6:
        prints(mainDemon.text)
        CombatLoop(player,mainDemon)
    if player.health >= 0:
        prints("The stench of dark magics leaves the caverns, and a beam of light shines down from the heavens, as the Gods acknowledge your bravery, and, heart pure as steel, you leave, seeking whatever journey lies ahead.\n")
        exit()
                    

def MysticalShrine(player):
    prints("Before you lies a shrine, with a hilt of a weapon sticking out of it. You recall that this shrine was planteed here by the Gods countless centuries ago, and, only one with a heart pure as steel can weild this ancestral weapon, The Hammer of Glory.\n")
    prints("Would you like to attempt to pull it out? Yes or no?\n")
    while True:
        a = input().lower()
        if a == "yes":
            prints("You heave with all your might, and the Hammer of Glory yields itself to you, destroying the shrine, as the enchanted astral hammer, with magics entwined in a star, is now yours. The power to defeat ",warlockName," is now in your hands, brave hero.\n")
            player.equipWeapon(gloryHammer)
            break
        elif a == "no":
            prints("As you turn away from the shrine, it fades out of this dimension, as it looks for a new hero to weild it's power.\n")
            break
        else:
            prints(failedInput)
def GenerateMap(): # a 11x11 map for the player to navigate. Row 11 column 6 will always have the final boss, and they will trigger whichever function.
  map = {}
  mysticalShrineCoords = (random.randint(1,9),random.randint(0,10))
  roomNames = [Monster,Treasure,Shop,MiniBoss,Rest]
  for x in range(11):
    for y in range(11):
        if (x,y) == (0,5):
            map[(x,y)] = StartRoom
        elif (x,y) ==(10,5):
            map[(x,y)] = FinalBoss
        elif (x,y) == mysticalShrineCoords:
            map[(x,y)] = MysticalShrine
        else:
            map[(x,y)] = roomNames[random.randint(0,4)]
  return map
game = True
def Movement(map,player): #Function for moving around the map
    movesDict = {"North":(1,0),"South":(-1,0),"East":(0,1),"West":(0,-1)}
    global game
    startSquare = (0,5)
    while game:
        map[startSquare](player)
        map[startSquare] = Empty
        if startSquare == (10,5):
            game = False
        movesList = ["North","South","East","West"]
        if startSquare[0] == 0:
            movesList.pop(movesList.index("South"))
        if startSquare[0] == 10:
            movesList.pop(movesList.index("North"))
        if startSquare[1] == 0:
            movesList.pop(movesList.index("West"))
        if startSquare[1] == 10:
            movesList.pop(movesList.index("East"))
        prints("Would you like to move ")
        for direction in movesList:
            if direction == movesList[-1]:
                prints("or ",direction, "?\n")
            else:
                prints(direction, ", ")
        move = input().title()
        startSquare = (startSquare[0]+movesDict[move][0],startSquare[1]+movesDict[move][1])
        LevelUpCheck(player)



            


