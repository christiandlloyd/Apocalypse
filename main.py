from functions import *
import random
import class_and_item_list
random.seed()


string = "Welcome to 'Apocalypse!' An evil sorcerer, ", WarlockNameGen()," threatens to destroy the kingdom of Gorroth, and in the hills of Ghomshief lies a cave where he begins a dark ritual to summon the demon ",demonNameGen()+"."
prints(string)

prints(" It is up to you to stop him, hero, lest the universe fall into the hands of evil once more.\n")

playerClass = MainMenu()
