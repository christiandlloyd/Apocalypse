import functions
import random
import class_and_item_list

random.seed()

print("Welcome to 'Apocalypse!' An evil sorcerer,", functions.WarlockNameGen(),"threatens to destroy the kingdom of Gorroth," 
"and in the hills of Ghomshief lies a cave where he begins a dark ritual to summon the demon",functions.demonNameGen()+".")

#Determines player's default class. While loop lets them confirm their class, and select another class if need be.
print("It is up to you to stop him, hero, lest the universe fall into the hands of evil once more.")

playerClass = functions.MainMenu()

