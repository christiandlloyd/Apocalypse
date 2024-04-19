from functions import *
import random
from class_and_item_list import *
random.seed()
#The below prints out the opening. The Warlock anbd Demon change every launch
prints("Welcome to 'Apocalypse!' An evil sorcerer, ", WarlockNameGen()," threatens to destroy the kingdom of Gorroth, and in the hills of Ghomshief lies a cave where he begins a dark ritual to summon the demon ",demonNameGen()+".")

prints(" It is up to you to stop him, hero, lest the universe fall into the hands of evil once more.\n")

playerClass = MainMenu()


CombatLoop(playerClass,Mage)