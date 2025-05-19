init python:
    class ForeveralTypes:
        AddType = 0
        Training = 1
        AddSTAB = 2
        AddProficiency = 3
        Scaling = 4
        TurnStartStatus = 5
        FormSwap = 6
        AddAbility = 7
        Mega = 8
        MoveBoost = 9
        ReplaceType = 10

    class FVLMacros:
        FVLName = 0
        FVLSpecies = 1
        FVLTrainer = 2
        FVLLevel = 3
        FVLType = 4
        FVLTypeData = 5
        FVLMoves = 6
        FVLDescription = 7

    def lookupforeveraldata(name, datatype):
        for entry in foreveraldex:
            if (entry[FVLMacros.FVLName] == name):
                return entry[datatype]

    def GetForeveralSpecies(fvl):
        return lookupforeveraldata(fvl, FVLMacros.FVLSpecies)[0]

    def GetQuickEquip(mon):
        if (inbattle or playercharacter != None):
            return False
        for fvl in foreveralinv:
            species = lookupforeveraldata(fvl, FVLMacros.FVLSpecies)
            if (mon.Id != 25.2 and mon.GetForeverals() == [] and species != None and mon.GetId() in species):
                return fvl
        return False

    def QuickEquipFVL(mon):
        fvl = GetQuickEquip(mon)
        if (fvl):
            mon.Foreverals = [fvl]
            foreveralinv.remove(fvl)
            mon.RecalculateStats()

    def FVLAbbreviation(fvl):
        if ("Everal" in fvl):
            return "EVL"
        elif ("Diveral" in fvl):
            return "DVL"
        elif ("Megaveral" in fvl):
            return "MVL"
        elif ("Gigaveral" in fvl):
            return "GVL"
        else:
            return "FVL"

    def GetAllForeveralNames():
        return [entry[FVLMacros.FVLName] for entry in foreveraldex]     

    def GetPublicForeverals():
        return [entry[FVLMacros.FVLName] for entry in foreveraldex if entry[FVLMacros.FVLLevel] < 11]

    foreveraldex = []
    #Name, species ids, Trainer, Level, Type, typedata, movesimparted, Description, 
    foreveraldex.append(["Clobbopus Foreveral", [852], "Bea", 3, ForeveralTypes.AddType, ["Water"], ["Aqua Jet", "Bulk Up"], "Adds Water-type"])
    foreveraldex.append(["Tyrogue Everal", [236], "Bea", 3, ForeveralTypes.Training, [], ["Power-Up Punch", "Low Kick"], "Using punching moves increases Defense EVs. Using kicking moves increases Attack EVs"])
    foreveraldex.append(["Timburr Foreveral", [532], "Bea", 3, ForeveralTypes.AddSTAB, ["Grass"], ["Branch Poke", "Karate Chop"], "Adds Grass-type STAB"])

    foreveraldex.append(["Shuckle Foreveral", [213], "Bea", 5, ForeveralTypes.AddAbility, ["Solid Rock"], ["Sticky Web", "Shore Up"], "Grants Solid Rock"])
    foreveraldex.append(["Rockruff Everal", [744], "Bea", 5, ForeveralTypes.AddProficiency, ["Normal", "Fighting", "Dark"], ["Bite", "Quick Attack", "Rock Smash"], "Gains Proficiency from Normal, Fighting, and Dark-types or give Pikachu STAB and resistance to the same"])
    foreveraldex.append(["Nacli Everal", [932], "Bea", 5, ForeveralTypes.Scaling, ["Naclstack", 24], ["Rock Throw", "Rock Smash"], "Base stats scale to Naclstack at level 24"])
#
    foreveraldex.append(["Eevee Everal", [133], "Blue", 3, ForeveralTypes.AddProficiency, ["Fire", "Water", "Electric", "Grass", "Fairy", "Dark", "Psychic", "Ice"], ["Tackle"], "Gains Proficiency from Fire, Water, Electric, Dark, Psychic, Grass, Ice, and Fairy-types or give Pikachu STAB and resistance to the same", "You know why Eevee are the best? It's because they can be {i}anything{/i}, if they put the effort in. Any foe can be overcome by an Eevee, if the Eevee just tries. Heck, you could make a team of Eevee evolutions, and that'd be a pretty good team!"])
    foreveraldex.append(["Bagon Everal", [371], "Blue", 3, ForeveralTypes.Scaling, ["Shelgon", 30], ["Aerial Ace", "Headbutt"], "Base stats scale to Shelgon at level 30", "There aren't a ton of dragons that think becoming a dumb cocoon is a good idea before they turn into a badass dragon. Bagon's one of them, though. But you got to admire its tenacity. It'll jump off cliffs, over and over, and over, to get the feeling of flying. It actually {i}works{/i} for its dream! Even if it mostly just hurts itself.."])
    foreveraldex.append(["Charmander Everal", [4], "Blue", 3, ForeveralTypes.AddProficiency, ["Dragon", "Flying"], ["Dragon Rage", "Dragon Dance"], "Gain Proficiency from Dragon and Flying-types, or give Pikachu STAB and resistance to the same"])
#
    foreveraldex.append(["Swablu Everal", [333], "Dawn", 3, ForeveralTypes.AddProficiency, ["Dragon", "Fairy"], ["Fairy Wind", "Dragon Rage"], "Gains Proficiency from Dragon and Fairy-types or give Pikachu STAB and resistance to the same", "U-um... I really like Swablu... because, um, they're... I mean, they're really cute. And the way they hum is so... but, you know? They can become really strong. And they're never afraid to sing. They don't worry about if they sing well, or not well... they just {i}do{/i} it. That's... I want to be like that"])
    foreveraldex.append(["Snover Everal", [459], "Dawn", 3, ForeveralTypes.Scaling, ["Abomasnow", 40], ["Mega Drain", "Razor Leaf"], "Base stats scale to Abomasnow at level 40"])
    foreveraldex.append(["Comfey Foreveral", [764], "Dawn", 3, ForeveralTypes.MoveBoost, ["Floral Healing"], ["Ingrain", "Wish"], "Boosts Floral Healing. Effect: Heals an ally 50% of their health, or 66% on Grassy Terrain. {i}Also heals the user, and clears status conditions on both{/i}"])

    foreveraldex.append(["Frigibax Everal", [996], "Dawn", 5, ForeveralTypes.Scaling, ["Arctibax", 35], ["Icy Wind", "Dragon Rage"], "Base stats scale to Arctibax at level 35"])
    foreveraldex.append(["Ninetales Diveral", [38, 38.1], "Dawn", 5, ForeveralTypes.FormSwap, [38, 38.1], ["Flame Burst", "Icy Wind"], "Swap between Kantonian/Alolan forms"])
    foreveraldex.append(["Cryogonal Foreveral", [615], "Dawn", 5, ForeveralTypes.AddAbility, ["Prism Armor"], ["Barrier", "Amnesia"], "Grants Prism Armor"])
#
    foreveraldex.append(["Darumaka Diveral", [554, 554.1], "Flannery", 3, ForeveralTypes.FormSwap, [554, 554.1], ["Ember", "Powder Snow"], "Swap between Unovan/Galarian forms"])
    foreveraldex.append(["Magby Everal", [240], "Flannery", 3, ForeveralTypes.Scaling, ["Magmar", 30], ["Ember", "Smog"], "Base stats scale to Magmar at level 30"])
    foreveraldex.append(["Cubone Everal", [104], "Flannery", 3, ForeveralTypes.AddProficiency, ["Fire", "Ghost"], ["Shadow Punch", "Flame Charge"], "Gains Proficiency from Ghost and Fire-types or give Pikachu STAB and resistance to the same"])

    foreveraldex.append(["Darmanitan Diveral", [555, 555.2], "Flannery", 5, ForeveralTypes.FormSwap, [555, 555.2], ["Fire Punch", "Ice Punch"], "Swap between Unovan/Galarian forms"])
    foreveraldex.append(["Heatmor Foreveral", [631], "Flannery", 5, ForeveralTypes.MoveBoost, ["Fire Lash"], ["Leech Life", "Giga Drain"], "Boosts Fire Lash. Power: 80 -> 90. Effect: Lowers Defense. {i}Also heals the user, by 50% of the damage dealt{/i}"])
    foreveraldex.append(["Marowak Diveral", [105, 105.1], "Flannery", 5, ForeveralTypes.FormSwap, [105, 105.1], ["Shadow Bone", "Bone Rush", "Bonemerang", "Bone Club"], "Swap between Kantonian/Alolan forms"])
#
    foreveraldex.append(["Snorunt Everal", [361], "Hilbert", 3, ForeveralTypes.AddProficiency, ["Ghost"], ["Hex", "Powder Snow"], "Gains Proficiency from Ghost-type or give Pikachu STAB and resistance to the same. Male Snorunt can become Froslass"])
    foreveraldex.append(["Dhelmise Foreveral", [781], "Hilbert", 3, ForeveralTypes.MoveBoost, ["Anchor Shot"], ["Aqua Jet", "Aqua Cutter"], "Boosts Anchor Shot. Power: 80 -> 90. Effect: Prevents opponent from switching. {i}Also lowers the opponent's Speed by one stage{/i}"])
    foreveraldex.append(["Piplup Everal", [393], "Hilbert", 3, ForeveralTypes.AddProficiency, ["Steel"], ["Bubble", "Mirror Shot"], "Gains Proficiency from Steel-type or give Pikachu STAB and resistance to the same"])

    foreveraldex.append(["Bergmite Everal", [712], "Hilbert", 5, ForeveralTypes.AddProficiency, ["Rock"], ["Rock Throw", "Icy Wind"], "Gains Proficiency from Rock-type or give Pikachu STAB and resistance to the same"])
    foreveraldex.append(["Riolu Everal", [447], "Hilbert", 5, ForeveralTypes.AddProficiency, ["Steel"], ["Metal Claw", "Power-Up Punch"], "Gains Proficiency from Steel-type or give Pikachu STAB and resistance to the same"])
    foreveraldex.append(["Prinplup Everal", [394], "Hilbert", 5, ForeveralTypes.AddProficiency, ["Steel"], ["Bubble Beam", "Metal Claw"], "Gains Proficiency from Steel-type or give Pikachu STAB and resistance to the same"])
#
    foreveraldex.append(["Mareanie Everal", [747], "Hilda", 3, ForeveralTypes.Scaling, ["Toxapex", 38], ["Baneful Bunker", "Spikes"], "Base stats scale to Toxapex at level 38"])
    foreveraldex.append(["Varoom Everal", [965], "Hilda", 3, ForeveralTypes.AddProficiency, ["Fairy", "Dark", "Fighting", "Fire"], ["Low Sweep", "Flame Charge"], "Gains Proficiency from Fairy, Dark, Fighting, and Fire-types or give Pikachu STAB and resistance to the same"])
    foreveraldex.append(["Aron Foreveral", [304], "Hilda", 3, ForeveralTypes.AddAbility, ["Filter"], ["Iron Defense", "Metal Claw"], "Grants Filter"])

    foreveraldex.append(["Geodude Diveral", [74, 74.1], "Hilda", 5, ForeveralTypes.FormSwap, [74, 74.1], ["Spark", "Mud-Slap"], "Swap between Kantonian/Alolan forms"])
    foreveraldex.append(["Graveler Diveral", [75, 75.1], "Hilda", 5, ForeveralTypes.FormSwap, [75, 75.1], ["Thunder Punch", "Magnitude"], "Swap between Kantonian/Alolan forms"])
    foreveraldex.append(["Pawniard Everal", [624], "Hilda", 5, ForeveralTypes.Scaling, ["Bisharp", 52], ["Pursuit", "Metal Claw"], "Base stats scale to Bisharp at level 52"])
#
    foreveraldex.append(["Nidoran-X Diveral", [29, 32], "Janine", 3, ForeveralTypes.FormSwap, [29, 32], ["Swagger", "Flatter"], "Swap between Male/Female forms"])
    foreveraldex.append(["Salandit Everal", [757], "Janine", 3, ForeveralTypes.AddAbility, ["Cute Charm"], ["Attract", "Captivate"], "Grants Cute Charm.\nMale Salandit can become Salazzle"])
    foreveraldex.append(["Mankey Everal", [56], "Janine", 3, ForeveralTypes.AddProficiency, ["Ghost"], ["Low Kick", "Astonish"], "Gain Proficiency from Ghost-type, or give Pikachu STAB and resistance to the same"])

    foreveraldex.append(["Nidorin-X Diveral", [30, 33], "Janine", 5, ForeveralTypes.FormSwap, [30, 33], ["Poison Sting", "Return"], "Swap between Male/Female forms"])
    foreveraldex.append(["Seviper Foreveral", [336], "Janine", 5, ForeveralTypes.MoveBoost, ["Poison Tail"], ["Brick Break", "Poison Tail"], "Boosts Poison Tail. Power: 50 -> 65. Effect: High crit rate. 10% chance to poison. {i}Double power on Normal-types{/i}"])
    foreveraldex.append(["Falinks Foreveral", [870], "Janine", 5, ForeveralTypes.MoveBoost, ["No Retreat"], ["No Retreat", "Power-Up Punch"], "Boosts No Retreat. Effect: Boosts stats, but prevents switching. {i}Grants same effect to allies{/i}"])
#
    foreveraldex.append(["Bidoof Everal", [399], "Professor Cherry", 3, ForeveralTypes.AddProficiency, ["Water"], ["Water Gun", "Super Fang"], "Gain Proficiency from Water-type, or give Pikachu STAB and resistance to the same"])
    foreveraldex.append(["Sunkern Everal", [191], "Professor Cherry", 3, ForeveralTypes.Scaling, ["Arceus", 100], ["Sunny Day", "Mega Drain"], "Base stats scale to Arceus at level 100"])
    foreveraldex.append(["Zigzagoon Diveral", [263, 263.1], "Professor Cherry", 3, ForeveralTypes.FormSwap, [263, 263.1], ["Headbutt", "Bite"], "Switch between Hoennian/Galarian forms"])
#
    foreveraldex.append(["Drampa Foreveral", [780], "Leaf", 3, ForeveralTypes.AddAbility, ["Friend Guard"], ["Dragon Rage", "Return"], "Grants Friend Guard"])
    foreveraldex.append(["Tynamo Everal", [602], "Leaf", 3, ForeveralTypes.Scaling, ["Eelektrik", 39], ["Bounce", "Dive"], "Base stats scale to Eelektrik at level 39"])
    foreveraldex.append(["Mareep Everal", [179], "Leaf", 3, ForeveralTypes.AddProficiency, ["Dragon"], ["Dragon Breath", "Cotton Guard"], "Gain Proficiency from Dragon-type, or give Pikachu STAB and resistance to the same"])
#
    foreveraldex.append(["Makuhita Everal", [296], "May", 3, ForeveralTypes.AddProficiency, ["Electric"], ["Thunder Punch", "Charge"], "Gain Proficiency from Electric-type, or give Pikachu STAB and resistance to the same"])
    foreveraldex.append(["Burmy Everal", [412], "May", 3, ForeveralTypes.AddProficiency, ["Steel", "Grass", "Ground", "Flying"], ["Shore Up", "Camouflage"], "Gains Proficiency from Steel, Grass, Ground, and Flying classes, or gives Pikachu STAB and resistance to the same"])
    foreveraldex.append(["Spidops Foreveral", [918], "May", 3, ForeveralTypes.MoveBoost, ["Silk Trap"], ["Silk Trap", "Sticky Web"], "Boosts Silk Trap. Effect: Blocks damaging moves and lowers speed of foes that make contact. {i}Also blocks status moves{/i}"])

    foreveraldex.append(["Heracross Megaveral", [214], "May", 5, ForeveralTypes.Mega, [Item.Heracronite, 214.1], ["Arm Thrust", "Pin Missile"], "Generates Heracronite at start of turn"])
    foreveraldex.append(["Mothim Foreveral", [414], "May", 5, ForeveralTypes.MoveBoost, ["Bug Bite"], ["Bug Bite", "Leech Life"], "Boosts Bug Bite. Effect: Does damage and eats foe's berry. {i}In first move slot: Its secondary type becomes the type of the food item it is holding on switch-in{/i}"])
    foreveraldex.append(["Wormadam Diveral", [413, 413.1, 413.2], "May", 5, ForeveralTypes.FormSwap, [413, 413.1, 413.2], ["Earth Power", "Energy Ball", "Flash Cannon"], "Swap between Wormadam forms"])
#
    foreveraldex.append(["Wooper Diveral", [194, 194.1], "Misty", 3, ForeveralTypes.FormSwap, [194, 194.1], ["Sludge", "Bubble Beam"], "Switch between Johtonian/Paldean forms"])
    foreveraldex.append(["Seel Everal", [86], "Misty", 3, ForeveralTypes.AddProficiency, ["Ice"], ["Bubble Beam", "Powder Snow"], "Gain Proficiency from Ice-type, or give Pikachu STAB and resistance to the same"])
    foreveraldex.append(["Azurill Everal", [298], "Misty", 3, ForeveralTypes.AddProficiency, ["Water"], ["Aqua Jet", "Bounce"], "Gain Proficiency from Water-type, or give Pikachu STAB and resistance to the same"])

    foreveraldex.append(["Frillish Everal", [592], "Misty", 5, ForeveralTypes.Scaling, ["Jellicent", 40], ["Hex", "Will-O-Wisp"], "Base stats scale to Jellicent at level 40"])
    foreveraldex.append(["X-sire Diveral", [195, 980], "Misty", 5, ForeveralTypes.FormSwap, [195, 980], ["Waterfall", "Poison Jab"], "Swap between Quagsire and Clodsire"])
    foreveraldex.append(["Castform Foreveral", [351], "Misty", 5, ForeveralTypes.MoveBoost, ["Sunny Day", "Rain Dance", "Hail", "Snowscape"], ["Sunny Day", "Rain Dance", "Hail", "Snowscape"], "Boosts Sunny Day, Rain Dance, Hail, and Snowscape. Effect: Sets up weather. {i}In first move slot: activates automatically on switch-in for three PP{/i}"])
#
    foreveraldex.append(["Bonsly Everal", [438], "Nessa", 3, ForeveralTypes.AddType, ["Grass"], ["Branch Poke", "Ingrain"], "Adds Grass-type"])
    foreveraldex.append(["Binacle Foreveral", [688], "Nessa", 3, ForeveralTypes.AddAbility, ["Sap Sipper"], ["Bug Bite", "Sludge"], "Grants Sap Sipper"])
    foreveraldex.append(["Wishiwashi Foreveral", [746], "Nessa", 3, ForeveralTypes.AddAbility, ["Swift Swim"], ["Shore Up", "Fillet Away"], "Grants Swift Swim"])

    foreveraldex.append(["Slowpoke Diveral", [79, 79.1], "Nessa", 5, ForeveralTypes.FormSwap, [79, 79.1], ["Amnesia", "Yawn"], "Switch between Kantonian/Galarian forms"])
    foreveraldex.append(["Veluza Foreveral", [976], "Nessa", 5, ForeveralTypes.MoveBoost, ["Fillet Away"], ["Fillet Away", "Heart Stamp"], "Boosts Fillet Away. Effect: Halves HP to boost stats. {i}Also purifies status conditions{/i}"])
    foreveraldex.append(["Chinchou Foreveral", [170], "Nessa", 5, ForeveralTypes.AddAbility, ["Water Absorb"], ["Charge", "Aqua Ring"], "Grants Water Absorb"])
#
    foreveraldex.append(["Joltik Everal", [595], "Rosa", 3, ForeveralTypes.Scaling, ["Galvantula", 36], ["Bug Bite", "Electroweb"], "Base stats scale to Galvantula at level 36"])
    foreveraldex.append(["Kricketot Foreveral", [401], "Rosa", 3, ForeveralTypes.AddType, ["Normal"], ["Uproar", "Sing"], "Adds Normal-type"])
    foreveraldex.append(["Kricketune Foreveral", [402], "Rosa", 3, ForeveralTypes.AddType, ["Normal"], ["Hyper Voice", "Perish Song"], "Adds Normal-type"])

    foreveraldex.append(["Paras Everal", [46], "Rosa", 5, ForeveralTypes.AddProficiency, ["Ghost"], ["Rain Dance", "Recover"], "Gain Proficiency from Ghost-type, or give Pikachu STAB and resistance to the same"])
    foreveraldex.append(["Parasect Foreveral", [47], "Rosa", 5, ForeveralTypes.ReplaceType, [("Grass", "Ghost")], ["Rain Dance", "Recover"], "Replaces Grass-type with Ghost"])
    foreveraldex.append(["Toxel Everal", [848], "Rosa", 5, ForeveralTypes.AddAbility, ["Moody"], ["Poison Sting", "Thunder Shock"], "Grants Moody. Nature will change randomly at the end of every turn"])

    foreveraldex.append(["Toxtricity Gigaveral", [849], "Rosa", 7, ForeveralTypes.Mega, [Item.MinigigaToxtricistar, 849.2], ["Overdrive", "Sludge Bomb"], "Generates Minigiga Toxtricistar at start of turn"])
    foreveraldex.append(["Galvantula Foreveral", [596], "Rosa", 7, ForeveralTypes.MoveBoost, ["Electroweb"], ["Electroweb", "Zap Cannon"], "Boosts Electroweb. Power: 55 -> 80. Effect: Does damage and lowers speed. {i}Also lowers evasion and traps opponent{/i}"])
    foreveraldex.append(["Leavanny Foreveral", [542], "Rosa", 7, ForeveralTypes.AddAbility, ["Sharpness"], ["Leaf Blade", "X-Scissor"], "Grants Sharpness"])
#
    foreveraldex.append(["Misdreavus Everal", [200], "Sabrina", 3, ForeveralTypes.Scaling, ["Mismagius", 50], ["Mean Look", "Perish Song"], "Base stats scale to Mismagius at level 50"])
    foreveraldex.append(["Meditite Everal", [307], "Sabrina", 3, ForeveralTypes.Training, [], ["Karate Chop", "Confusion"], "Using fighting moves increases Attack EVs. Using psychic moves increases Special Defense EVs"])
    foreveraldex.append(["Litwick Everal", [607], "Sabrina", 3, ForeveralTypes.Scaling, ["Lampent", 41], ["Will-O-Wisp", "Hex"], "Base stats scale to Lampent at level 41"])

    foreveraldex.append(["Hypno Foreveral", [97], "Sabrina", 5, ForeveralTypes.AddAbility, ["Bad Dreams"], ["Hypnosis", "Dream Eater"], "Grants Bad Dreams"])
    foreveraldex.append(["Espurr Foreveral", [677], "Sabrina", 5, ForeveralTypes.AddAbility, ["Aftermath"], ["Calm Mind", "Stored Power"], "Grants Aftermath"])
    foreveraldex.append(["Shuppet Foreveral", [353], "Sabrina", 5, ForeveralTypes.MoveBoost, ["Spite"], ["Spite", "Grudge"], "Boosts Spite. Effect: {i}Removes all PP from this move, and the opponent's most-recently used move{/i}"])
#
    foreveraldex.append(["Rhyhorn Foreveral", [111], "Serena", 3, ForeveralTypes.AddAbility, ["Speed Boost"], ["Bulldoze", "Accelerock"], "Grants Speed Boost"])
    foreveraldex.append(["Sandile Everal", [551], "Serena", 3, ForeveralTypes.Scaling, ["Krokorok", 29], ["Fire Fang", "Thunder Fang"], "Base stats scale to Krokorok at level 29"])
    foreveraldex.append(["Litten Everal", [725], "Serena", 3, ForeveralTypes.AddProficiency, ["Dark"], ["Flame Burst", "Bite"], "Gain Proficiency from Dark-type, or give Pikachu STAB and resistance to the same"])

    foreveraldex.append(["Deino Everal", [633], "Serena", 5, ForeveralTypes.Scaling, ["Zweilous", 50], ["Dragon Rage", "Beat Up"], "Base stats scale to Zweilous at level 50"])
    foreveraldex.append(["Krokorok Foreveral", [552], "Serena", 5, ForeveralTypes.AddAbility, ["Strong Jaw"], ["Ice Fang", "Psychic Fangs"], "Grants Strong Jaw"])
    foreveraldex.append(["Torracat Everal", [726], "Serena", 5, ForeveralTypes.AddProficiency, ["Dark"], ["Fire Fang", "Crunch"], "Gain Proficiency from Dark-type, or give Pikachu STAB and resistance to the same"])
#
    foreveraldex.append(["Zubat Foreveral", [41], "Silver", 3, ForeveralTypes.AddAbility, ["Regenerator"], ["Parting Shot", "Baton Pass"], "Grants Regenerator"])
    foreveraldex.append(["Golbat Foreveral", [42], "Silver", 3, ForeveralTypes.AddAbility, ["Regenerator"], ["Volt Switch", "Flip Turn"], "Grants Regenerator"])
    foreveraldex.append(["Nymble Everal", [919], "Silver", 3, ForeveralTypes.AddProficiency, ["Dark"], ["Parting Shot", "U-turn"], "Gain Proficiency from Dark-type, or give Pikachu STAB and resistance to the same"])

    foreveraldex.append(["Crobat Foreveral", [169], "Silver", 5, ForeveralTypes.AddAbility, ["Regenerator"], ["U-turn", "Teleport"], "Grants Regenerator"])
    foreveraldex.append(["Raticate Diveral", [20, 20.1], "Silver", 5, ForeveralTypes.FormSwap, [20, 20.1], ["Crunch", "Hyper Fang"], "Swap between Kantonian/Alolan forms"])
    foreveraldex.append(["Lokix Foreveral", [920], "Silver", 5, ForeveralTypes.AddSTAB, ["Fighting"], ["Beat Up", "Retaliate"], "Adds Fighting-Type STAB"])

    foreveraldex.append(["Absol Megaveral", [359], "Silver", 7, ForeveralTypes.Mega, [Item.Absolite, 359.1], ["Night Slash", "Spirit Break"], "Generates Absolite at start of turn"])
    foreveraldex.append(["Croagunk Everal", [453], "Silver", 7, ForeveralTypes.Scaling, ["Toxicroak", 37], ["Poison Jab", "Karate Chop"], "Base stats scale to Toxicroak at level 37"])
    foreveraldex.append(["Koffing Everal", [109], "Silver", 7, ForeveralTypes.AddProficiency, ["Fairy"], ["Fairy Wind", "Poison Gas"], "Gain Proficiency from Fairy-type, or give Pikachu STAB and resistance to the same"])
#
    foreveraldex.append(["Ducklett Foreveral", [580], "Skyla", 3, ForeveralTypes.AddAbility, ["Regenerator"], ["U-turn", "Flip Turn"], "Grants Regenerator"])
    foreveraldex.append(["Nincada Everal", [290], "Skyla", 3, ForeveralTypes.AddProficiency, ["Flying", "Ghost"], ["Dig", "Fly"], "Gain Proficiency from Flying and Ghost-types, or give Pikachu STAB and resistance to the same"])
    foreveraldex.append(["Cramorant Foreveral", [845], "Skyla", 3, ForeveralTypes.TurnStartStatus, ["gorging"], ["Stockpile", "Swallow", "Spit Up"], "Start in Gorging Form"])

    foreveraldex.append(["Gligar Foreveral", [207], "Skyla", 5, ForeveralTypes.AddAbility, ["Poison Heal"], ["Magnitude", "Wing Attack"], "Grants Poison Heal"])
    foreveraldex.append(["Farfetch'd Diveral", [83, 83.1], "Skyla", 5, ForeveralTypes.FormSwap, [83, 83.1], ["Wing Attack", "Karate Chop"], "Swap between Kantonian/Galarian forms"])
    foreveraldex.append(["Noctowl Foreveral", [164], "Skyla", 5, ForeveralTypes.AddType, ["Psychic"], ["Hypnosis", "Dream Eater"], "Adds Psychic-type"])
#
    foreveraldex.append(["Yamper Foreveral", [835], "Sonia", 3, ForeveralTypes.AddAbility, ["Fluffy"], ["Bite", "Attract"], "Grants Fluffy"])
    foreveraldex.append(["Togedemaru Foreveral", [777], "Sonia", 3, ForeveralTypes.AddAbility, ["Rough Skin"], ["Spiky Shield", "Wide Guard"], "Grants Rough Skin"])
    foreveraldex.append(["Growlithe Foreveral", [58], "Sonia", 3, ForeveralTypes.AddAbility, ["Strong Jaw"], ["Bite", "Thunder Fang"], "Grants Strong Jaw"])#On evolution, grant Psychic Fangs and Ice Fang 

    foreveraldex.append(["Stunfisk Diveral", [618], "Sonia", 5, ForeveralTypes.FormSwap, [618, 618.1], ["Discharge", "Iron Head"], "Swap between Unovan/Galarian forms"])
    foreveraldex.append(["Boltund Foreveral", [836], "Sonia", 5, ForeveralTypes.AddAbility, ["Speed Boost"], ["Electro Ball", "Baton Pass"], "Grants Speed Boost"])
    foreveraldex.append(["Turtonator Foreveral", [776], "Sonia", 5, ForeveralTypes.AddAbility, ["Aftermath"], ["Mind Blown", "Explosion"], "Grants Aftermath"])
#
    foreveraldex.append(["Noibat Foreveral", [714], "Tia", 3, ForeveralTypes.AddSTAB, ["Normal"], ["Uproar", "Disarming Voice"], "Grants Normal-type STAB"])
    foreveraldex.append(["Mime Jr. Everal", [439], "Tia", 3, ForeveralTypes.AddProficiency, ["Ice"], ["Draining Kiss", "Powder Snow"], "Gain Proficiency from Ice-type, or give Pikachu STAB and resistance to the same"])
    foreveraldex.append(["Trapinch Everal", [328], "Tia", 3, ForeveralTypes.AddProficiency, ["Bug", "Dragon"], ["Bug Bite", "Dragon Breath"], "Gain Proficiency from Dragon and Bug-types, or give Pikachu STAB and resistance to the same"])

    foreveraldex.append(["Baltoy Everal", [343], "Tia", 5, ForeveralTypes.Scaling, ["Claydol", 36], ["Iron Defense", "Amnesia"], "Base stats scale to Claydol at level 36"])
    foreveraldex.append(["Claydol Foreveral", [344], "Tia", 5, ForeveralTypes.AddAbility, ["Solid Rock"], ["Recover", "Rapid Spin"], "Grants Solid Rock"])
    foreveraldex.append(["Mr. Mime Diveral", [122, 122.2], "Tia", 5, ForeveralTypes.FormSwap, [122, 122.1], ["Draining Kiss", "Powder Snow"], "Swap between Kantonian/Galarian forms"])
#
    foreveraldex.append(["Munchlax Foreveral", [446], "Whitney", 3, ForeveralTypes.AddAbility, ["Harvest"], ["Slack Off", "Uproar"], "Grants Harvest"])
    foreveraldex.append(["Ralts Everal", [280], "Whitney", 3, ForeveralTypes.AddProficiency, ["Fighting"], ["Draining Kiss", "Vacuum Wave"], "Gain Proficiency from Fighting-type, or give Pikachu STAB and resistance to the same"])
    foreveraldex.append(["Happiny Everal", [440], "Whitney", 3, ForeveralTypes.AddAbility, ["Regenerator"], ["Seismic Toss", "Soft-Boiled"], "Grants Regenerator"])
#
    foreveraldex.append(["Lopunny Megaveral", [428], "Whitney", 5, ForeveralTypes.Mega, [Item.Lopunnite, 428.1], ["Return", "Power-Up Punch"], "Generates Lopunnite at start of turn"])
    foreveraldex.append(["Chansey Everal", [113], "Whitney", 5, ForeveralTypes.AddAbility, ["Regenerator"], ["Thunder Wave", "Encore"], "Grants Regenerator"])
    foreveraldex.append(["Audino Megaveral", [531], "Whitney", 5, ForeveralTypes.Mega, [Item.Audinite, 531.1], ["Aqua Ring", "Grassy Terrain"], "Generates Audinite at start of turn"])
#
    foreveraldex.append(["Swinub Everal", [220], "Jasmine", 3, ForeveralTypes.Scaling, ["Piloswine", 33], ["Ice Shard", "Bulldoze"], "Base stats scale to Piloswine at level 33"])
    foreveraldex.append(["Bunnelby Everal", [659], "Jasmine", 3, ForeveralTypes.AddProficiency, ["Ground"], ["Dig", "Mud-Slap"], "Gain Proficiency from Ground-type, or give Pikachu STAB and resistance to the same"])
    foreveraldex.append(["Magnemite Everal", [81], "Jasmine", 3, ForeveralTypes.Scaling, ["Magneton", 30], ["Magnet Bomb", "Thunder Shock"], "Base stats scale to Magneton at level 30"])
#
    foreveraldex.append(["Drilbur Everal", [529], "Jasmine", 5, ForeveralTypes.AddProficiency, ["Steel"], ["Metal Claw", "Sand Tomb"], "Gain Proficiency from Steel-type, or give Pikachu STAB and resistance to the same"])
    foreveraldex.append(["Diggersby Foreveral", [660], "Jasmine", 5, ForeveralTypes.AddAbility, ["Mold Breaker"], ["Extreme Speed", "Dig"], "Grants Mold Breaker"])
    foreveraldex.append(["Skarmory Foreveral", [227], "Jasmine", 5, ForeveralTypes.MoveBoost, ["Steel Wing"], ["Steel Wing", "Roost"], "Boosts Steel Wing. Power: 70 -> 90. Effect: {i}Has a 30% chance of boosting Defense and Special Defense{/i}"])
#
    foreveraldex.append(["Tyrunt Everal", [696], "Raihan", 3, ForeveralTypes.Scaling, ["Tyrantrum", 39], ["Ice Fang", "Thunder Fang"], "Base stats scale to Tyrantrum at level 39"])
    foreveraldex.append(["Minior Foreveral", [774], "Raihan", 3, ForeveralTypes.MoveBoost, ["Shell Smash"], ["Shell Smash", "Power Gem"], "Boosts Shell Smash. Effect: Decreases defense to increase offense. {i}Will always move last{/i}"])
    foreveraldex.append(["Dreepy Everal", [885], "Raihan", 3, ForeveralTypes.Scaling, ["Drakloak", 50], ["Shadow Sneak", "Dragon Rage"], "Base stats scale to Drakloak at level 50"])
#
    foreveraldex.append(["Sigilyph Foreveral", [561], "Bianca", 3, ForeveralTypes.AddAbility, ["Simple"], ["Stored Power", "Calm Mind"], "Grants Simple"])
    foreveraldex.append(["Stantler Everal", [234], "Bianca", 3, ForeveralTypes.AddProficiency, ["Psychic"], ["Return", "Psybeam"], "Gain Proficiency from Psychic-type, or give Pikachu STAB and resistance to the same"])
    foreveraldex.append(["Glameow Everal", [431], "Bianca", 3, ForeveralTypes.Scaling, ["Purugly", 38], ["Covet", "Fake Out"], "Base stats scale to Purugly at level 38"])
#
    foreveraldex.append(["Cyndaquil Everal", [155], "Ethan", 3, ForeveralTypes.AddProficiency, ["Ghost"], ["Defense Curl", "Rollout"], "Gain Proficiency from Ghost-type, or give Pikachu STAB and resistance to the same"])
    foreveraldex.append(["Quilava Everal", [156], "Ethan", 3, ForeveralTypes.AddProficiency, ["Ghost"], ["Flame Burst", "Flame Charge"], "Gain Proficiency from Ghost-type, or give Pikachu STAB and resistance to the same"])
    foreveraldex.append(["Aipom Foreveral", [190], "Ethan", 3, ForeveralTypes.AddAbility, ["Technician"], ["Covet", "Fake Out"], "Grants Technician"])
#
    foreveraldex.append(["Sandshrew Diveral", [27, 27.1], "Nate", 3, ForeveralTypes.FormSwap, [27, 27.1], ["Rollout", "Ice Ball"], "Swap between Kantonian/Alolan forms"])
    foreveraldex.append(["Skrelp Everal", [690], "Nate", 3, ForeveralTypes.AddProficiency, ["Dragon"], ["Dragon Rage", "Dragon Breath"], "Gain Proficiency from Dragon-type, or give Pikachu STAB and resistance to the same"])
    foreveraldex.append(["Grimer Diveral", [88, 88.1], "Nate", 3, ForeveralTypes.FormSwap, [88, 88.1], ["Sludge", "Bite"], "Swap between Kantonian/Alolan forms"])
#
    foreveraldex.append(["Ferroseed Everal", [597], "Nate", 5, ForeveralTypes.Scaling, ["Ferrothorn", 40], ["Ingrain", "Curse"], "Base stats scale to Ferrothorn at level 40"])
    foreveraldex.append(["Sandslash Diveral", [28, 28.1], "Nate", 5, ForeveralTypes.FormSwap, [28, 28.1], ["Avalanche", "Revenge"], "Swap between Kantonian/Alolan forms"])
    foreveraldex.append(["Trubbish Everal", [568], "Nate", 5, ForeveralTypes.Scaling, ["Garbodor", 36], ["Fling", "Camouflage"], "Base stats scale to Garbodor at level 36"])
#
    foreveraldex.append(["Turtwig Everal", [387], "Erika", 3, ForeveralTypes.AddProficiency, ["Ground"], ["Bite", "Withdraw"], "Gain Proficiency from Ground-type, or give Pikachu STAB and resistance to the same"])
    foreveraldex.append(["Grotle Everal", [388], "Erika", 3, ForeveralTypes.AddProficiency, ["Ground"], ["Crunch", "Iron Defense"], "Gain Proficiency from Ground-type, or give Pikachu STAB and resistance to the same"])
    foreveraldex.append(["Foongus Everal", [590], "Erika", 3, ForeveralTypes.Scaling, ["Amoonguss", 39], ["Rain Dance", "Moonlight"], "Base stats scale to Amoonguss at level 39"])
#
    foreveraldex.append(["Frosmoth Foreveral", [873], "Grusha", 3, ForeveralTypes.AddAbility, ["Fluffy"], ["Snowscape", "Aurora Veil"], "Grants Fluffy"])
    foreveraldex.append(["Archen Everal", [566], "Grusha", 3, ForeveralTypes.Scaling, ["Archeops", 37], ["Wing Attack", "Rock Throw"], "Base stats scale to Archeops at level 37"])
    foreveraldex.append(["Drifloon Foreveral", [425], "Grusha", 3, ForeveralTypes.AddType, ["Fire"], ["Flame Burst", "Will-O-Wisp"], "Adds Fire-type"])
#
    foreveraldex.append(["Budew Everal", [406], "Brendan", 3, ForeveralTypes.Scaling, ["Roselia", 15], ["Mega Drain", "Acid Spray"], "Base stats scale to Roselia at level 15"])
    foreveraldex.append(["Mudkip Everal", [258], "Brendan", 3, ForeveralTypes.AddProficiency, ["Ground"], ["Mud Shot", "Bubble Beam"], "Gain Proficiency from Ground-type, or give Pikachu STAB and resistance to the same"])
    foreveraldex.append(["Buizel Foreveral", [418], "Brendan", 3, ForeveralTypes.AddAbility, ["Strong Jaw"], ["Ice Fang", "Fire Fang"], "Grants Strong Jaw"])
#
    foreveraldex.append(["Crabrawler Everal", [739], "Calem", 3, ForeveralTypes.AddProficiency, ["Ice"], ["Mach Punch", "Ice Shard"], "Gain Proficiency from Ice-type, or give Pikachu STAB and resistance to the same"])
    foreveraldex.append(["Togepi Everal", [175], "Calem", 3, ForeveralTypes.AddProficiency, ["Flying"], ["Shell Smash", "Egg Bomb"], "Gain Proficiency from Flying-type, or give Pikachu STAB and resistance to the same"])
    foreveraldex.append(["Vullaby Everal", [629], "Calem", 3, ForeveralTypes.Scaling, ["Mandibuzz", 54], ["Shell Smash", "Roost"], "Base stats scale to Mandibuzz at level 54"])
#
    foreveraldex.append(["Carbink Everal", [703], "Wally", 3, ForeveralTypes.AddAbility, ["Prism Armor"], ["Trick Room", "Magic Coat"], "Grants Prism Armor"])
    foreveraldex.append(["Mawile Megaveral", [303], "Wally", 3, ForeveralTypes.Mega, [Item.Mawilite, 303.1], ["Vise Grip", "Double Iron Bash"], "Generates Mawilite at start of turn"])
    foreveraldex.append(["Scraggy Everal", [559], "Wally", 3, ForeveralTypes.Scaling, ["Scrafty", 39], ["Bite", "Low Sweep"], "Base stats scale to Scrafty at level 39"])
#
    foreveraldex.append(["Rowlet Everal", [722], "Gardenia", 3, ForeveralTypes.AddProficiency, ["Ghost", "Fighting"], ["Shadow Sneak", "Karate Chop"], "Gain Proficiency from Ghost and Fighting-type, or give Pikachu STAB and resistance to the same"])
    foreveraldex.append(["Dartrix Everal", [723], "Gardenia", 3, ForeveralTypes.AddProficiency, ["Ghost", "Fighting"], ["Shadow Claw", "Double Kick"], "Gain Proficiency from Ghost and Fighting-type, or give Pikachu STAB and resistance to the same"])
    foreveraldex.append(["Tropius Foreveral", [357], "Gardenia", 3, ForeveralTypes.AddAbility, ["Drought"], ["Flamethrower", "Growth"], "Grants Drought"])
#
    foreveraldex.append(["Mimi-X-chu Diveral", [778, 25], "Iono", 3, ForeveralTypes.FormSwap, [778, 25], ["Volt Tackle", "Shadow Sneak"], "Swap between Mimikyu and Pikachu"])
    foreveraldex.append(["X-rigus Diveral", [563, 867], "Iono", 3, ForeveralTypes.FormSwap, [563, 867], ["Shadow Claw", "Bulldoze"], "Swap between Cofagrigus and Runerigus"])
    foreveraldex.append(["Voltorb Everal", [100], "Iono", 3, ForeveralTypes.AddProficiency, ["Grass"], ["Grass Knot", "Synthesis"], "Gain Proficiency from Grass-type, or give Pikachu STAB and resistance to the same"])
#
    foreveraldex.append(["Eevee Diveral", [133], "Blue", 11, ForeveralTypes.AddAbility, ["Tetra Element"], ["Leaf Blade", "Flare Blitz", "Surf", "Thunderbolt", "Ice Beam", "Moonblast", "Foul Play", "Psychic"], "Grants Tetra Element. Its power is imperfect"])
    foreveraldex.append(["Pichu Everal", [172], "Ethan", 11, ForeveralTypes.Scaling, ["Pichu", 100], ["Zippy Zap", "Floaty Fall", "Splishy Splash"], "Base stats scale based on destined defeats by the opponent. Its power is imperfect"])
    foreveraldex.append(["Wimpod Foreveral", [767], "Klara", 5, ForeveralTypes.AddAbility, ["Intimidate"], ["First Impression", "U-turn", "Flip Turn", "Aqua Jet"], "Grants Intimidate. Its power is imperfect"])
    foreveraldex.append(["Vespiquen Uneveral", [416], "Klara", 11, ForeveralTypes.MoveBoost, ["Attack Order", "Defend Order", "Heal Order"], ["Attack Order", "Defend Order", "Heal Order"], "Boosts Attack Order. Effect: High crit rate. \n{i}Also boosts allied Beedrill's offense.{/i}\nBoosts Defense Order. Effect: Raises defenses. \n{i}Also summons allied Beedrill.{/i}\nBoosts Heal Order. Effect: Heals self. \n{i}Also heals allied Beedrill.{/i}\nForces unevolution. Its power is imperfect"])
    foreveraldex.append(["Dodrio Overal", [85], "???", 11, ForeveralTypes.AddAbility, ["Thrice Denied"], ["Frustration", "Drill Peck", "Acupressure", "Tri Attack"], "Grants Thrice Denied.\nPermits attacking three times per turn at different priorities.\nCuts direct damage taken to a third.\nForces evolution. Its power is imperfect"])

