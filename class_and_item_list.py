import conditions

#Below are default classes
Mage ={"Health" : 15, "ArmorClass" : 14, "Skills":{"Burn":{"Damage":10,"Bonus": 2},"Zap":{"Damage":12,"Bonus": 1},"Chill":{"Damage":8,"Bonus": 3}}, "Stats":{"Dex":0,"Str":-1,"Wis":1,"Int":2}}
Thief ={"Health" : 17, "ArmorClass" : 15, "Skills":{"Stab":{"Damage":10,"Bonus": 3},"Slice":{"Damage":8,"Bonus": 4},"Poisoned Blade":{"Damage":12,"Bonus": 4, "Status": conditions.applyPoison}}, "Stats":{"Dex":2,"Str":0,"Wis":-1,"Int":1}}
Cleric = {"Health" : 20, "ArmorClass" : 16, "Skills":{"Hammer Slam":{"Damage":8,"Bonus": 3},"Smite":{"Damage":10,"Bonus": 2},"Cure Wounds":{"Healing": 8}}, "Stats":{"Dex":-1,"Str":1,"Wis":2,"Int":0}}
Warrior = {"Health" : 24, "ArmorClass" : 17, "Skills":{"Wrestle":{"Status": conditions.grappled,"Bonus": 2},"Shield Bash":{"Damage":12,"Bonus": 1},"Slash":{"Damage":10,"Bonus": 3}}, "Stats":{"Dex":1,"Str":2,"Wis":0,"Int":-1}}
Characters = {"mage": Mage,"cleric": Cleric,"warrior": Warrior,"thief": Thief}

Sword1 = {"Bonus":1,"Skills":{"Slash":{"Damage":10,"Bonus": 3}}}
Sword2 = {"Bonus":2,"Skills":{"Slash":{"Damage":10,"Bonus": 3}}}
Sword3 = {"Bonus":3,"Skills":{"Slash":{"Damage":10,"Bonus": 3}}}
Wand1= {"Bonus":1,"Skills":{"Burn":{"Damage":10,"Bonus": 2}}}
Wand2= {"Bonus":2,"Skills":{"Burn":{"Damage":10,"Bonus": 2}}}
Wand3= {"Bonus":3,"Skills":{"Burn":{"Damage":10,"Bonus": 2}}}
Shield1 = {"Armor":1,"Skills":{"Shield Bash":{"Damage":12,"Bonus": 1}}}
Shield2 = {"Armor":2,"Skills":{"Shield Bash":{"Damage":12,"Bonus": 1}}}
Shield3 = {"Armor":3,"Skills":{"Shield Bash":{"Damage":12,"Bonus": 1}}}
Dagger1 = {"Bonus":1,"Skills":{"Stab":{"Damage":10,"Bonus": 3}}}
Dagger2 = {"Bonus":2,"Skills":{"Stab":{"Damage":10,"Bonus": 3}}}
Dagger3 = {"Bonus":3,"Skills":{"Stab":{"Damage":10,"Bonus": 3}}}
Book1 = {"Bonus":1,"Skills":{"Cure Wounds":{"Healing": 8}}}
Book2 = {"Bonus":2,"Skills":{"Cure Wounds":{"Healing": 8}}}
Book3 = {"Bonus":3,"Skills":{"Cure Wounds":{"Healing": 8}}}
Axe1 = {"Bonus":1,"Skills":{"Chop":{"Damage":12,"Bonus": 2}}}
Axe2 = {"Bonus":2,"Skills":{"Chop":{"Damage":12,"Bonus": 2}}}
Axe3 = {"Bonus":3,"Skills":{"Chop":{"Damage":12,"Bonus": 2}}}
Leather = {"ArmorClass":1}
Iron = {"ArmorClass":2}
Steel = {"ArmorClass":3}
Apple = {"Healing":4, "Uses" :1}
Apple_strudel = {"Healing":8, "Uses": 1}
Apple_pie = {"Healing":16, "Uses": 1}
Watermelon = {"ArmorClass": 1, "Uses":1}
Watermelon_smoothy = {"ArmorClass":2, "Uses":1}
Watermelon_sorbet = {"ArmorClass":3, "Uses":1}
Weapons = [Sword1,Sword2,Sword3, Wand1,Wand2,Wand3,Dagger1,Dagger2,Dagger3,Book1,Book2,Book3,Axe1,Axe2,Axe3]
Armor =[Leather, Iron, Steel,Shield1,Shield2,Shield3]
Consumables = [Apple,Apple_strudel,Apple_pie,Watermelon,Watermelon_smoothy,Watermelon_sorbet]

