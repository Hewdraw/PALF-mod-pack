init -2 python:
    def GetItemEntry(itemid):
        if itemid not in itemdex.keys():
            return itemdex[-1]
        return itemdex[itemid]
    
    def GetItemEntryFromName(name):
        if name[-7:].lower() == "berries":
            name = name[:-3] + "y"
        if name == "Curious Keystone":
            return itemdex[Item.OddKeystone]
        if name == "Pink Bow":
            return itemdex[Item.FairyFeather]
        for entry in itemdex.values():
            if entry[ItemdexMacros.Name].lower() == name.lower():
                return entry
        return itemdex[-1]

    def GetItemName(itemid):
        return GetItemEntry(itemid)[ItemdexMacros.Name]

    def GetItemScope(itemid):
        return GetItemEntry(itemid)[ItemdexMacros.Scope]
    
    def ItemHasCategory(itemid, category):
        return GetItemEntry(itemid)[ItemdexMacros.Category] == category
    
    def ItemHasTag(itemid, tag):
        itemtags = GetItemEntry(itemid)[ItemdexMacros.Tags]
        if isinstance(tag, str):
            return tag in itemtags
        elif isinstance(tag, tuple):
            return any(itemid in itemtags for itemid in tag)
    
    def ValidateItemUsage(itemid, arg = None):
        entry = GetItemEntry(itemid)
        condition = entry[ItemdexMacros.UsageCondition]

        if entry[ItemdexMacros.Scope] == "None": # items with "None" as a scope require no arguments
            return condition()
        else:
            return condition(arg)
    
    def CanUseMoveItem(itemid, mon):
        if GetItemScope(itemid) == "Move":
            return any(ValidateItemUsage(itemid, move) for move in mon.GetMoves())
        else:
            return False
    
    # ITEM FORMAT: (0: id, int); (1: name, str); (2: description, str); (3: category, str); (4: return after battle, bool); (5: scope, either "Pokemon", "Move", "None"); (6: usage condition, func); (7: default gift reaction, number), (8: tags, list)
    itemdex = {
        -1 : [-1, "Error", "This is an error. If you see this item, please report it on the server.", "Misc.", True, "None", lambda: False, 0, []],
        0 : [0, "Poké Ball", "Used for catching Pokémon. Decent, at best.", "Poké Balls", True, "None", lambda: inbattle, 1, []],
        1 : [1, "Great Ball", "Designed for capturing Pokémon. Decent enough, though suffers from middle-child syndrome.", "Poké Balls", True, "None", lambda: inbattle, 1, []],
        2 : [2, "Ultra Ball", "An excellent Poké Ball, at a premium price. The Poké Ball of Champions.", "Poké Balls", True, "None", lambda: inbattle, 1, ["likedByJanine"]],
        3 : [3, "Premier Ball", "Works like a Poké Ball, but can make an interesting gift.", "Poké Balls", True, "None", lambda: inbattle, 7, ["universalLike"]],
        4 : [4, "Master Ball", "Can catch a wild Pokémon in a battle without fail.", "Poké Balls", True, "None", lambda: inbattle, 5, []],
        5 : [5, "Cheri Berry", "Cures paralysis.", "Medicines", False, "Pokemon", lambda mon: mon.HasStatus("paralyzed"), 1, ["berry"]],
        6 : [6, "Chesto Berry", "Cures sleep.", "Medicines", False, "Pokemon", lambda mon: mon.HasStatus("asleep"), 1, ["berry"]],
        7 : [7, "Pecha Berry", "Cures poison.", "Medicines", False, "Pokemon", lambda mon: mon.HasStatus("poisoned"), 1, ["berry"]],
        8 : [8, "Rawst Berry", "Cures burn.", "Medicines", False, "Pokemon", lambda mon: mon.HasStatus("burned"), 1, ["berry"]],
        9 : [9, "Oran Berry", "Restores 10 HP when health falls under 50%.", "Medicines", False, "Pokemon", lambda mon: mon.GetHealthPercentage() < 1 and mon.GetHealthPercentage() != 0, 1, ["berry"]],
        10 : [10, "Sitrus Berry", "Restores 25% of the max HP when Health falls under 50%.", "Medicines", False, "Pokemon", lambda mon: mon.GetHealthPercentage() < 1 and mon.GetHealthPercentage() != 0, 1, ["berry"]],
        11 : [11, "Potion", "Restores 20 HP to a Pokémon. Scientifically proven to be less useful than water.", "Medicines", True, "Pokemon", lambda mon: mon.GetHealthPercentage() < 1 and mon.GetHealthPercentage() != 0, 1, ["status healing"]],
        12 : [12, "Super Potion", "Restores 60 HP to a Pokémon. Slightly less effective than a glass of lemonade.", "Medicines", True, "Pokemon", lambda mon: mon.GetHealthPercentage() < 1 and mon.GetHealthPercentage() != 0, 1, ["status healing"]],
        13 : [13, "Hyper Potion", "Restores 120 HP to a Pokémon. Knits wounds, heals bruises, and also acts as a powerful degreaser.", "Medicines", True, "Pokemon", lambda mon: mon.GetHealthPercentage() < 1 and mon.GetHealthPercentage() != 0, 1, ["status healing"]],
        14 : [14, "Max Potion", "Restores a Pokémon to full health. The chemicals here are banned in five regions.", "Medicines", True, "Pokemon", lambda mon: mon.GetHealthPercentage() < 1 and mon.GetHealthPercentage() != 0, 2, ["status healing"]],
        15 : [15, "Full Restore", "Restores a Pokémon to full health and purifies most status conditions. Every Champion carries five.", "Medicines", True, "Pokemon", lambda mon: (mon.GetHealthPercentage() < 1 or mon.HasNormalStatus() or mon.HasStatus("confused")) and mon.GetHealthPercentage() != 0, 3, ["status healing", "likedByJanine"]],
        16 : [16, "Revive", "Restores a fainted Pokémon to half health. Useless in Nuzlockes.", "Medicines", True, "Pokemon", lambda mon: mon in FaintedMons or mon.GetHealthPercentage() <= 0, 1, ["status healing"]],
        17 : [17, "Max Revive", "Restores a fainted Pokémon to full health. Absolutely useless in Nuzlockes.", "Medicines", True, "Pokemon", lambda mon: mon in FaintedMons or mon.GetHealthPercentage() <= 0, 3, ["status healing", "likedByJanine"]],
        18 : [18, "Ether", "Restores 10 PP for a Pokémon's move.", "Medicines", True, "Move", lambda move: move.PP < move.MaxPP, 1, ["status healing"]],
        19 : [19, "Max Ether", "Restores all PP for a Pokémon's move.", "Medicines", True, "Move", lambda move: move.PP < move.MaxPP, 2, ["status healing"]],
        20 : [20, "Elixir", "Restores 10 PP to all moves for a Pokémon.", "Medicines", True, "Pokemon", lambda mon: not mon.HasFullPP(), 2, ["status healing"]],
        21 : [21, "Max Elixir", "Restores all PP to all moves for a Pokémon.", "Medicines", True, "Pokemon", lambda mon: not mon.HasFullPP(), 3, ["status healing"]],
        22 : [22, "Antidote", "Purges poison from a Pokémon. May cause violent expulsion of toxins.", "Medicines", True, "Pokemon", lambda mon: mon.HasStatus("poisoned") or mon.HasStatus("badly poisoned"), 1, ["status healing"]],
        23 : [23, "Paralyze Heal", "Cures full-body paralysis in most Pokémon. Contains tiny rubber molecules that ground the charge.", "Medicines", True, "Pokemon", lambda mon: mon.HasStatus("paralyzed"), 1, ["status healing"]],
        24 : [24, "Ice Heal", "Cures frostbitten and frozen Pokémon. It's literally just warm water.", "Medicines", True, "Pokemon", lambda mon: mon.HasStatus("frozen"), 1, ["status healing"]],
        25 : [25, "Awakening", "Wakes up Pokémon. It's an air horn.", "Medicines", True, "Pokemon", lambda mon: mon.HasStatus("asleep"), 1, ["status healing"]],
        26 : [26, "Burn Heal", "Liquidized aloe. Soothes burns and smells like cucumbers.", "Medicines", True, "Pokemon", lambda mon: mon.HasStatus("burned"), 1, ["status healing"]],
        27 : [27, "Full Heal", "A panacea of incredible proportions. Makes all minor medicines purposeless.", "Medicines", True, "Pokemon", lambda mon: mon.HasNormalStatus() or mon.HasStatus("confused"), 1, ["status healing"]],
        28 : [28, "Energy Powder", "Restores 60 HP, but makes Pokémon grumpy, and they'll refuse other bitter medicine.", "Medicines", True, "Pokemon", lambda mon: (mon.GetHealthPercentage() < 1 and mon.GetHealthPercentage() != 0) and not mon.HasStatus("bitter"), 0, ["status healing", "bitter"]],
        29 : [29, "Heal Powder", "Cures non-volatile status conditions and confusion.", "Medicines", True, "Pokemon", lambda mon: mon.HasNormalStatus() or mon.HasStatus("confused"), 1, ["status healing"]],
        30 : [30, "Pomeg Smoothie", "Sets a Pokémon's Health EVs to 0.", "Medicines", True, "Pokemon", lambda mon: mon.CanSetEV(Stats.Health, 0), 1, ["status healing", "ev item"]],
        31 : [31, "Kelpsy Smoothie", "Sets a Pokémon's Attack EVs to 0.", "Medicines", True, "Pokemon", lambda mon: mon.CanSetEV(Stats.Attack, 0), 1, ["status healing", "ev item"]],
        32 : [32, "Hondew Smoothie", "Sets a Pokémon's Special Attack EVs to 0.", "Medicines", True, "Pokemon", lambda mon: mon.CanSetEV(Stats.SpecialAttack, 0), 1, ["status healing", "ev item"]],
        33 : [33, "Qualot Smoothie", "Sets a Pokémon's Defense EVs to 0.", "Medicines", True, "Pokemon", lambda mon: mon.CanSetEV(Stats.Defense, 0), 1, ["status healing", "ev item"]],
        34 : [34, "Grepa Smoothie", "Sets a Pokémon's Special Defense EVs to 0.", "Medicines", True, "Pokemon", lambda mon: mon.CanSetEV(Stats.SpecialDefense, 0), 1, ["status healing", "ev item"]],
        35 : [35, "Tamato Smoothie", "Sets a Pokémon's Speed EVs to 0.", "Medicines", True, "Pokemon", lambda mon: mon.CanSetEV(Stats.Speed, 0), 1, ["status healing", "ev item"]],
        36 : [36, "HP Up Concentrate", "Sets a Pokémon's HP EVs to 252.", "Medicines", True, "Pokemon", lambda mon: mon.CanSetEV(Stats.Health, 252), 2, ["status healing", "ev item"]],
        37 : [37, "Protein Concentrate", "Sets a Pokémon's Attack EVs to 252.", "Medicines", True, "Pokemon", lambda mon: mon.CanSetEV(Stats.Attack, 252), 2, ["status healing", "ev item"]],
        38 : [38, "Calcium Concentrate", "Sets a Pokémon's Special Attack EVs to 252.", "Medicines", True, "Pokemon", lambda mon: mon.CanSetEV(Stats.SpecialAttack, 252), 2, ["status healing", "ev item"]],
        39 : [39, "Iron Concentrate", "Sets a Pokémon's Defense EVs to 252.", "Medicines", True, "Pokemon", lambda mon: mon.CanSetEV(Stats.Defense, 252), 2, ["status healing", "ev item"]],
        40 : [40, "Zinc Concentrate", "Sets a Pokémon's Special Defense EVs to 252.", "Medicines", True, "Pokemon", lambda mon: mon.CanSetEV(Stats.SpecialDefense, 252), 2, ["status healing", "ev item"]],
        41 : [41, "Carbos Concentrate", "Sets a Pokémon's Speed EVs to 252.", "Medicines", True, "Pokemon", lambda mon: mon.CanSetEV(Stats.Speed, 252), 2, ["status healing", "ev item"]],
        42 : [42, "Energy Root", "Restores 120 HP, but makes Pokémon grumpy, and they'll refuse other bitter medicine.", "Medicines", True, "Pokemon", lambda mon: (mon.GetHealthPercentage() < 1 and mon.GetHealthPercentage() != 0) and not mon.HasStatus("bitter"), 0, ["status healing", "bitter"]],
        43 : [43, "Revival Herb", "Revives a fainted Pokémon and restores it to full HP, but makes Pokémon grumpy, and they'll refuse other bitter medicine.", "Medicines", True, "Pokemon", lambda mon: (mon in FaintedMons or mon.GetHealthPercentage() <= 0) and not mon.HasStatus("bitter"), 0, ["status healing", "bitter"]],
        44 : [44, "Microwave", "Changes Rotom's form to Heat Rotom.", "Evo Items", True, "Pokemon", lambda mon: math.floor(mon.Id) == 479, 1, ["rotom catalog", "not consumed"]],
        45 : [45, "Washing Mchn", "Changes Rotom's form to Wash Rotom.", "Evo Items", True, "Pokemon", lambda mon: math.floor(mon.Id) == 479, 1, ["rotom catalog", "not consumed"]],
        46 : [46, "Refrigerator", "Changes Rotom's form to Frost Rotom.", "Evo Items", True, "Pokemon", lambda mon: math.floor(mon.Id) == 479, 1, ["rotom catalog", "not consumed"]],
        47 : [47, "Fan", "Changes Rotom's form to Fan Rotom.", "Evo Items", True, "Pokemon", lambda mon: math.floor(mon.Id) == 479, 1, ["rotom catalog", "not consumed"]],
        48 : [48, "Lawnmower", "Changes Rotom's form to Mow Rotom.", "Evo Items", True, "Pokemon", lambda mon: math.floor(mon.Id) == 479, 1, ["rotom catalog", "not consumed"]],
        49 : [49, "Oval Stone", "Evolves Happiny.", "Evo Items", True, "None", lambda: False, 1, ["Evo Items"]],
        50 : [50, "Unremarkable Teacup", "Evolves Poltchageist's Counterfeit form.", "Evo Items", True, "Pokemon", lambda mon: mon.Id == 1012, 1, ["Evo Items"]],
        51 : [51, "Up-Grade", "Evolves Porygon.", "Evo Items", True, "None", lambda: False, 1, ["Evo Items"]],
        52 : [52, "Deep Sea Tooth", "Evolves Clamperl. It also doubles Clamperl's Special Attack.", "Evo Items", True, "None", lambda: False, 2, ["Evo Items"]],
        53 : [53, "Deep Sea Scale", "Evolves Clamperl. It also doubles Clamperl's Special Defense.", "Evo Items", True, "None", lambda: False, 2, ["Evo Items"]],
        54 : [54, "Protector", "Evolves Rhydon.", "Evo Items", True, "None", lambda: False, 1, ["Evo Items"]],
        55 : [55, "Cracked Pot", "Evolves Sinistea's Phony form.", "Evo Items", True, "Pokemon", lambda mon: mon.Id == 854, 1, ["Evo Items"]],
        56 : [56, "Galarica Cuff", "Evolves Galarian Slowpoke.", "Evo Items", True, "Pokemon", lambda mon: mon.Id == 79.1, 1, ["Evo Items"]],
        57 : [57, "Sachet", "Evolves Spritzee.", "Evo Items", True, "None", lambda: False, 1, ["Evo Items"]],
        58 : [58, "Electirizer", "Evolves Electabuzz.", "Evo Items", True, "None", lambda: False, 2, ["Evo Items"]],
        59 : [59, "Whipped Dream", "Evolves Swirlix.", "Evo Items", True, "None", lambda: False, 1, ["Evo Items"]],
        60 : [60, "Reaper Cloth", "Evolves Dusclops.", "Evo Items", True, "None", lambda: False, 2, ["Evo Items"]],
        61 : [61, "Galarica Wreath", "Evolves Galarian Slowpoke.", "Evo Items", True, "Pokemon", lambda mon: mon.Id == 79.1, 1, ["Evo Items"]],
        62 : [62, "Magmarizer", "Evolves Magmar.", "Evo Items", True, "None", lambda: False, 2, ["Evo Items"]],
        63 : [63, "Auspicious Armor", "Evolves Charcadet.", "Evo Items", True, "Pokemon", lambda mon: mon.Id == 935, 2, ["Evo Items"]],
        64 : [64, "Dragon Scale", "Evolves Seadra.", "Evo Items", True, "None", lambda: False, 2, ["Evo Items"]],
        65 : [65, "Masterpiece Teacup", "Evolves Poltchageist's Artisan form.", "Evo Items", True, "Pokemon", lambda mon: mon.Id == 1012, 4, ["Evo Items"]],
        66 : [66, "Malicious Armor", "Evolves Charcadet.", "Evo Items", True, "Pokemon", lambda mon: mon.Id == 935, 1, ["Evo Items"]],
        67 : [67, "Chipped Pot", "Evolves Sinistea's Antique form.", "Evo Items", True, "Pokemon", lambda mon: mon.Id == 854, 4, ["Evo Items"]],
        68 : [68, "Metal Alloy", "Evolves Duraludon.", "Evo Items", True, "Pokemon", lambda mon: mon.Id == 884, 2, ["Evo Items"]],
        69 : [69, "Razor Claw", "Evolves Sneasel. It also increases an equipped Pokémon's crit ratio. A very nice item.", "Evo Items", True, "Pokemon", lambda mon: True, 2, ["Evo Items"]],
        70 : [70, "Razor Fang", "Evolves Gligar. It also adds a chance of flinching to an equipped Pokémon's moves.", "Evo Items", True, "None", lambda: False, 2, ["Evo Items"]],
        71 : [71, "King's Rock", "Evolves Poliwhirl and Slowpoke. It also adds a chance of flinching to an equipped Pokémon's moves.", "Evo Items", True, "None", lambda: False, 2, ["Evo Items"]],
        72 : [72, "Link Cable", "Allows you to instantly evolve Trade evolutions, without trading.", "Evo Items", True, "Pokemon", lambda mon: HasTradeEvolution(mon), 5, []],
        73 : [73, "Escape Rope", "Warps you back to campus from any wild area without passing time.", "Misc.", True, "None", lambda: inwildarea, 2, []],
        74 : [74, "Poké Doll", "Guarantees escape from wild Pokémon. A grown man carrying it around will get weird looks.", "Misc.", True, "None", lambda: inbattle and WildBattle and not Unrunnable, 0, []],
        75 : [75, "Repel", "Repels weaker Pokémon. The probability of encountering rare Pokémon increases. Guarantees escape.", "Misc.", True, "None", lambda: freeroaming, 1, ["repel"]],
        76 : [76, "Super Repel", "Repels most Pokémon. The probability of encountering rare Pokémon greatly increases. Guarantees escape.", "Misc.", True, "None", lambda: freeroaming, 2, ["repel"]],
        77 : [77, "Max Repel", "Repels all but the strongest Pokémon. Non-rare Pokémon will not appear. Guarantees escape.", "Misc.", True, "None", lambda: freeroaming, 3, ["repel", "likedByJanine"]],
        78 : [78, "Silk Scarf", "Boosts the power of Normal-type moves.", "Battle Items", True, "None", lambda: False, 1, ["move boost item"]],
        79 : [79, "Charcoal", "Boosts the power of Fire-type moves.", "Battle Items", True, "None", lambda: False, 1, ["move boost item"]],
        80 : [80, "Mystic Water", "Boosts the power of Water-type moves.", "Battle Items", True, "None", lambda: False, 1, ["move boost item"]],
        81 : [81, "Miracle Seed", "Boosts the power of Grass-type moves.", "Battle Items", True, "None", lambda: False, 1, ["move boost item"]],
        82 : [82, "Magnet", "Boosts the power of Electric-type moves.", "Battle Items", True, "None", lambda: False, 1, ["move boost item"]],
        83 : [83, "Never-Melt Ice", "Boosts the power of Ice-type moves.", "Battle Items", True, "None", lambda: False, 1, ["move boost item"]],
        84 : [84, "Black Belt", "Boosts the power of Fighting-type moves.", "Battle Items", True, "None", lambda: False, 1, ["move boost item", "likedByJanine"]],
        85 : [85, "Poison Barb", "Boosts the power of Poison-type moves.", "Battle Items", True, "None", lambda: False, 1, ["move boost item", "likedByJanine"]],
        86 : [86, "Soft Sand", "Boosts the power of Ground-type moves.", "Battle Items", True, "None", lambda: False, 1, ["move boost item"]],
        87 : [87, "Sharp Beak", "Boosts the power of Flying-type moves.", "Battle Items", True, "None", lambda: False, 1, ["move boost item"]],
        88 : [88, "Twisted Spoon", "Boosts the power of Psychic-type moves.", "Battle Items", True, "None", lambda: False, 1, ["move boost item"]],
        89 : [89, "Silver Powder", "Boosts the power of Bug-type moves.", "Battle Items", True, "None", lambda: False, 1, ["move boost item"]],
        90 : [90, "Hard Stone", "Boosts the power of Rock-type moves.", "Battle Items", True, "None", lambda: False, 1, ["move boost item"]],
        91 : [91, "Spell Tag", "Boosts the power of Ghost-type moves.", "Battle Items", True, "None", lambda: False, 1, ["move boost item"]],
        92 : [92, "Black Glasses", "Boosts the power of Dark-type moves.", "Battle Items", True, "None", lambda: False, 1, ["move boost item"]],
        93 : [93, "Dragon Fang", "Boosts the power of Dragon-type moves.", "Battle Items", True, "None", lambda: False, 1, ["move boost item"]],
        94 : [94, "Metal Coat", "Evolves Onix and Scyther. Boosts the power of Steel-type moves.", "Battle Items", True, "None", lambda: False, 1, ["move boost item"]],
        95 : [95, "Fairy Feather", "Boosts the power of Fairy-type moves.", "Battle Items", True, "None", lambda: False, 1, ["move boost item"]],
        96 : [96, "Scope Lens", "Increases an equipped Pokémon's crit ratio.", "Battle Items", True, "None", lambda: False, 2, []],
        97 : [97, "Rocky Helmet", "Damages opposing Pokémon that use contact moves on the equipped Pokémon.", "Battle Items", True, "None", lambda: False, 1, []],
        98 : [98, "Sticky Barb", "Damages the Pokémon that holds it each turn, and is transferred to the Pokémon that makes contact.", "Battle Items", True, "None", lambda: False, 0, []],
        99 : [99, "Leftovers", "Heals the equipped Pokémon every turn.", "Battle Items", True, "None", lambda: False, 0, []],
        100 : [100, "Experience Share", "The equipped Pokémon gains a portion of the battle experience earned by allies.", "Misc.", True, "None", lambda: False, 2, []], # effects defined in battle.rpy
        101 : [101, "Lucky Egg", "Increases the experience gained by an equipped Pokémon.", "Misc.", True, "None", lambda: False, 2, []],
        102 : [102, "Soothe Bell", "When rung, evolves Pokémon that have a strong bond with you.", "Misc.", True, "None", lambda: True, 3, ["not consumed"]],
        103 : [103, "Plain Bread", "Attracts Normal-types in the wild. I'm not saying you're boring, but...", "Misc.", True, "None", lambda: freeroaming or inwildarea, 1, ["treat boost"]],
        104 : [104, "Spicy Jerky", "Attracts Fire-types in the wild. Will get stuck in your teeth for weeks.", "Misc.", True, "None", lambda: freeroaming or inwildarea, 1, ["treat boost"]],
        105 : [105, "Water Bottle", "Attracts Water-types in the wild. A core component of a wet T-shirt contest.", "Misc.", True, "None", lambda: freeroaming or inwildarea, 1, ["treat boost"]],
        106 : [106, "Energy Drink", "Attracts Electric-types in the wild. It contains electrolytes. They're what plants crave.", "Misc.", True, "None", lambda: freeroaming or inwildarea, 1, ["treat boost"]],
        107 : [107, "Salad Wrap", "Attracts Grass-types in the wild. The healthy choice for people who hate themselves.", "Misc.", True, "None", lambda: freeroaming or inwildarea, 1, ["treat boost"]],
        108 : [108, "Ice Pop", "Attracts Ice-types in the wild. Brainfreeze is obligatory, but darn it, it's worth it.", "Misc.", True, "None", lambda: freeroaming or inwildarea, 1, ["treat boost"]],
        109 : [109, "Knuckle Sandwich", "Attracts Fighting-types in the wild. A sandwich carved in the shape of a fist.", "Misc.", True, "None", lambda: freeroaming or inwildarea, 1, ["treat boost"]],
        110 : [110, "Fast Food", "{size=32}Attracts Poison-types in the wild. You're pretty sure the Head Chef bought fast food and disguised it as his own cooking. Delightfully devilish.{/size}", "Misc.", True, "None", lambda: freeroaming or inwildarea, 1, ["treat boost"]],
        111 : [111, "Ground Beef", "Attracts Ground-types in the wild. Does not help with grinding.", "Misc.", True, "None", lambda: freeroaming or inwildarea, 1, ["treat boost"]],
        112 : [112, "Bouffalant Wings", "Attracts Flying-types in the wild. Does not come from actual Bouffalant.", "Misc.", True, "None", lambda: freeroaming or inwildarea, 1, ["treat boost"]],
        113 : [113, "Brain Food", "Attracts Psychic-types in the wild. May also attract zombies.", "Misc.", True, "None", lambda: freeroaming or inwildarea, 1, ["treat boost"]],
        114 : [114, "Picnic Basket", "Attracts Bug-types in the wild. Also comes with complimentary red-and-white checked blanket.", "Misc.", True, "None", lambda: freeroaming or inwildarea, 1, ["treat boost"]],
        115 : [115, "Rock Cakes", "Attracts Rock-types in the wild. It looks like a grinning Geodude.", "Misc.", True, "None", lambda: freeroaming or inwildarea, 1, ["treat boost"]],
        116 : [116, "Soul Food", "Attracts Ghost-types in the wild. Just like Momma used to make.", "Misc.", True, "None", lambda: freeroaming or inwildarea, 1, ["treat boost"]],
        117 : [117, "Gummy Wyrms", "Attracts Dragon-types in the wild. Cheap and sugary candy that looks like Dratini.", "Misc.", True, "None", lambda: freeroaming or inwildarea, 1, ["treat boost"]],
        118 : [118, "Dark Chocolate", "Attracts Dark-types in the wild. Pretentious people will claim it's better than milk chocolate.", "Misc.", True, "None", lambda: freeroaming or inwildarea, 1, ["treat boost"]],
        119 : [119, "Steel-cut Oats", "Attracts Steel-types in the wild. Makes a darn good porridge with some brown sugar.", "Misc.", True, "None", lambda: freeroaming or inwildarea, 1, ["treat boost"]],
        120 : [120, "Pixie Sticks", "Attracts Fairy-types in the wild. Immediate inducer of diabetes in anyone who has a bite.", "Misc.", True, "None", lambda: freeroaming or inwildarea, 1, ["treat boost"]],
        121 : [121, "Odd Keystone", "A vital item that is needed to keep a stone tower from collapsing. Voices can be heard from it occasionally.", "Misc.", True, "None", lambda: False, 2, []],
        122 : [122, "Tera Orb", "Allows your Pokémon to Terastallize.", "Misc.", True, "None", lambda: False, 5, []],
        123 : [123, "Minigiga Laprastar", "Allows Lapras to enter its Minigigamax form.", "Misc.", True, "None", lambda: False, 4, ["megastone", "Lapras"]],
        124 : [124, "Minigiga Toxtricistar", "Allows Toxtricity to enter its Minigigamax form.", "Misc.", True, "None", lambda: False, 4, ["megastone", "Toxtricity"]],
        125 : [125, "Heracronite", "Allows Heracross to Mega Evolve.", "Misc.", True, "None", lambda: False, 4, ["megastone", "Heracross"]],
        126 : [126, "Absolite", "Allows Absol to Mega Evolve.", "Misc.", True, "None", lambda: False, 4, ["megastone", "Absol"]],
        127 : [127, "Audinite", "Allows Audino to Mega Evolve.", "Misc.", True, "None", lambda: False, 4, ["megastone", "Audino"]],
        128 : [128, "Fresh Water", "Restores 30 HP to a Pokémon. It's more useful than an actual potion.", "Medicines", True, "Pokemon", lambda mon: mon.GetHealthPercentage() < 1 and mon.GetHealthPercentage() != 0, 1, ["status healing"]],
        129 : [129, "Normal-Type Gem", "Boosts the first Normal-type move used in a battle.", "Battle Items", False, "None", lambda: False, 1, ["type gem"]],
        130 : [130, "Fire-Type Gem", "Boosts the first Fire-type move used in a battle.", "Battle Items", False, "None", lambda: False, 1, ["type gem"]],
        131 : [131, "Water-Type Gem", "Boosts the first Water-type move used in a battle.", "Battle Items", False, "None", lambda: False, 1, ["type gem"]],
        132 : [132, "Electric-Type Gem", "Boosts the first Electric-type move used in a battle.", "Battle Items", False, "None", lambda: False, 1, ["type gem"]],
        133 : [133, "Grass-Type Gem", "Boosts the first Grass-type move used in a battle.", "Battle Items", False, "None", lambda: False, 1, ["type gem"]],
        134 : [134, "Ice-Type Gem", "Boosts the first Ice-type move used in a battle.", "Battle Items", False, "None", lambda: False, 1, ["type gem"]],
        135 : [135, "Fighting-Type Gem", "Boosts the first Fighting-type move used in a battle.", "Battle Items", False, "None", lambda: False, 1, ["type gem"]],
        136 : [136, "Poison-Type Gem", "Boosts the first Poison-type move used in a battle.", "Battle Items", False, "None", lambda: False, 1, ["type gem"]],
        137 : [137, "Ground-Type Gem", "Boosts the first Ground-type move used in a battle.", "Battle Items", False, "None", lambda: False, 1, ["type gem"]],
        138 : [138, "Flying-Type Gem", "Boosts the first Flying-type move used in a battle.", "Battle Items", False, "None", lambda: False, 1, ["type gem"]],
        139 : [139, "Psychic-Type Gem", "Boosts the first Psychic-type move used in a battle.", "Battle Items", False, "None", lambda: False, 1, ["type gem"]],
        140 : [140, "Bug-Type Gem", "Boosts the first Bug-type move used in a battle.", "Battle Items", False, "None", lambda: False, 1, ["type gem"]],
        141 : [141, "Rock-Type Gem", "Boosts the first Rock-type move used in a battle.", "Battle Items", False, "None", lambda: False, 1, ["type gem"]],
        142 : [142, "Ghost-Type Gem", "Boosts the first Ghost-type move used in a battle.", "Battle Items", False, "None", lambda: False, 1, ["type gem"]],
        143 : [143, "Dragon-Type Gem", "Boosts the first Dragon-type move used in a battle.", "Battle Items", False, "None", lambda: False, 1, ["type gem"]],
        144 : [144, "Dark-Type Gem", "Boosts the first Dark-type move used in a battle.", "Battle Items", False, "None", lambda: False, 1, ["type gem"]],
        145 : [145, "Steel-Type Gem", "Boosts the first Steel-type move used in a battle.", "Battle Items", False, "None", lambda: False, 1, ["type gem"]],
        146 : [146, "Fairy-Type Gem", "Boosts the first Fairy-type move used in a battle.", "Battle Items", False, "None", lambda: False, 1, ["type gem"]],
        147 : [147, "Blank Plate", "Boosts the power of Normal-type moves.", "Battle Items", True, "None", lambda: False, 2, ["plate"]],
        148 : [148, "Fist Plate", "Boosts the power of Fighting-type moves.", "Battle Items", True, "None", lambda: False, 2, ["plate"]],
        149 : [149, "Sky Plate", "Boosts the power of Flying-type moves.", "Battle Items", True, "None", lambda: False, 2, ["plate"]],
        150 : [150, "Toxic Plate", "Boosts the power of Poison-type moves.", "Battle Items", True, "None", lambda: False, 2, ["plate"]],
        151 : [151, "Earth Plate", "Boosts the power of Ground-type moves.", "Battle Items", True, "None", lambda: False, 2, ["plate"]],
        152 : [152, "Stone Plate", "Boosts the power of Rock-type moves.", "Battle Items", True, "None", lambda: False, 2, ["plate"]],
        153 : [153, "Insect Plate", "Boosts the power of Bug-type moves.", "Battle Items", True, "None", lambda: False, 2, ["plate"]],
        154 : [154, "Spooky Plate", "Boosts the power of Ghost-type moves.", "Battle Items", True, "None", lambda: False, 2, ["plate"]],
        155 : [155, "Iron Plate", "Boosts the power of Steel-type moves.", "Battle Items", True, "None", lambda: False, 2, ["plate"]],
        156 : [156, "Flame Plate", "Boosts the power of Fire-type moves.", "Battle Items", True, "None", lambda: False, 2, ["plate"]],
        157 : [157, "Splash Plate", "Boosts the power of Water-type moves.", "Battle Items", True, "None", lambda: False, 2, ["plate"]],
        158 : [158, "Meadow Plate", "Boosts the power of Grass-type moves.", "Battle Items", True, "None", lambda: False, 2, ["plate"]],
        159 : [159, "Zap Plate", "Boosts the power of Electric-type moves.", "Battle Items", True, "None", lambda: False, 2, ["plate"]],
        160 : [160, "Mind Plate", "Boosts the power of Psychic-type moves.", "Battle Items", True, "None", lambda: False, 2, ["plate"]],
        161 : [161, "Icicle Plate", "Boosts the power of Ice-type moves.", "Battle Items", True, "None", lambda: False, 2, ["plate"]],
        162 : [162, "Draco Plate", "Boosts the power of Dragon-type moves.", "Battle Items", True, "None", lambda: False, 2, ["plate"]],
        163 : [163, "Dread Plate", "Boosts the power of Dark-type moves.", "Battle Items", True, "None", lambda: False, 2, ["plate"]],
        164 : [164, "Pixie Plate", "Boosts the power of Fairy-type moves.", "Battle Items", True, "None", lambda: False, 2, ["plate"]],
        165 : [165, "Legend Plate", "Changes Arceus' type to the one that is most efficient against the opponent.", "Battle Items", True, "None", lambda: False, 2, ["plate"]],
        166 : [166, "Macho Brace", "Doubles the amount of EV gained by an equipped Pokémon, at the cost of halving its Speed.", "Misc.", True, "None", lambda: False, 2, []],
        167 : [167, "HP Up", "Increases a Pokémon's HP EVs by 10.", "Medicines", True, "Pokemon", lambda mon: mon.CanModifyEV(Stats.Health, 1), 1, ["status healing", "ev item"]],
        168 : [168, "Protein", "Increases a Pokémon's Attack EVs by 10.", "Medicines", True, "Pokemon", lambda mon: mon.CanModifyEV(Stats.Attack, 1), 1, ["status healing", "ev item"]],
        169 : [169, "Calcium", "Increases a Pokémon's Special Attack EVs by 10.", "Medicines", True, "Pokemon", lambda mon: mon.CanModifyEV(Stats.SpecialAttack, 1), 1, ["status healing", "ev item"]],
        170 : [170, "Iron", "Increases a Pokémon's Defense EVs by 10.", "Medicines", True, "Pokemon", lambda mon: mon.CanModifyEV(Stats.Defense, 1), 1, ["status healing", "ev item"]],
        171 : [171, "Zinc", "Increases a Pokémon's Special Defense EVs by 10.", "Medicines", True, "Pokemon", lambda mon: mon.CanModifyEV(Stats.SpecialDefense, 1), 1, ["status healing", "ev item"]],
        172 : [172, "Carbos", "Increases a Pokémon's Speed EVs by 10.", "Medicines", True, "Pokemon", lambda mon: mon.CanModifyEV(Stats.Speed, 1), 1, ["status healing", "ev item"]],
        173 : [173, "Protein (For Humans)", "\"Increases a human's Attack\". At least, that's what it says on the label.", "Misc.", True, "None", lambda: False, 1, ["pov switch", "bea item"]],
        174 : [174, "Unused Journal", "It was supposed to help you make decisions. You couldn't decide when to start using it.", "Misc.", True, "None", lambda: False, 1, ["pov switch", "bea item"]],
        175 : [175, "Cherished Picture", "A young boy and girl, together, waving at the cameraman. There are no masks in sight.", "Misc.", True, "None", lambda: False, 1, ["pov switch", "bea item"]],
        176 : [176, "Red Whistle", "You never go anywhere without it. You got it too late.", "Misc.", True, "None", lambda: False, 1, ["pov switch", "bea item"]],
        177 : [177, "Notepad", "It's relatively well-kept, considering the massive usage it undergoes.", "Misc.", True, "None", lambda: False, 1, ["pov switch", "cheren item"]],
        178 : [178, "Spare Pens", "Each color indicates the priority of what's being written.", "Misc.", True, "None", lambda: False, 1, ["pov switch", "cheren item"]],
        179 : [179, "Broken Glasses", "They broke when you fell. There's nothing more to it.", "Misc.", True, "None", lambda: False, 1, ["pov switch", "cheren item"]],
        180 : [180, "Tape Roll", "Used to repair glasses. You'll get around to it.", "Misc.", True, "None", lambda: False, 1, ["pov switch", "cheren item"]],
        181 : [181, "To-Do List", "Seventy-two items left. This morning, you had sixty-eight.", "Misc.", True, "None", lambda: False, 1, ["pov switch", "cheren item"]],
        182 : [182, "Music Player", "The music you downloaded can be ascribed to different genres. Lately, you've been listening to angry songs.", "Misc.", True, "None", lambda: False, 1, ["pov switch", "cheren item"]],
        183 : [183, "Spare Tie Clip", "It will someday find its use. For now, it can keep your ahoge in place.", "Misc.", True, "None", lambda: False, 1, ["pov switch", "cheren item"]],
        184 : [184, "Paper with [first_name]'s Face", "Torn from a poster. This was beneath you.", "Misc.", True, "None", lambda: False, 1, ["pov switch", "cheren item"]],
        185 : [185, "Bike Keys", "They come with a cute keychain, which helps you find them when they get lost while running.", "Misc.", True, "None", lambda: False, 1, ["pov switch", "hilda item"]],
        186 : [186, "Spare Tennis Shoes", "The bad smell comes from the worn plastic, rather than from the sweat.", "Misc.", True, "None", lambda: False, 1, ["pov switch", "hilda item"]],
        187 : [187, "Personal Planner", "Last year's. You never got around to buying a new one--or writing in this one.", "Misc.", True, "None", lambda: False, 1, ["pov switch", "hilda item"]],
        188 : [188, "Metal Polish", "You bought it for your Pokémon. Polishing them up is one of the few chores you find fun.", "Misc.", True, "None", lambda: False, 1, ["pov switch", "hilda item"]],
        189 : [189, "Hi-Power Flashlight", "The batteries have been recently changed.", "Misc.", True, "None", lambda: False, 1, ["pov switch", "hilda item"]],
        190 : [190, "The Guide to College Dating", "Unread. A gift from Dad. You know better than to take his advice.", "Misc.", True, "None", lambda: False, 1, ["pov switch", "hilda item"]],
        191 : [191, "How to Win Friends and Influence People", "Mint. Should probably get around to reading it before it's too late.", "Misc.", True, "None", lambda: False, 1, ["pov switch", "whitney item"]],
        192 : [192, "Miltank Collar", "Your Miltank finds it quite stylish. You bought it as part of a pair.", "Misc.", True, "None", lambda: False, 1, ["pov switch", "whitney item"]],
        193 : [193, "Collar", "This one's not for Miltank.", "Misc.", True, "None", lambda: False, 1, ["pov switch", "whitney item"]],
        194 : [194, "Nurse Kit", "It contains necessities... and a hand mirror.", "Misc.", True, "None", lambda: False, 1, ["pov switch", "whitney item"]],
        195 : [195, "Lipstick", "It tastes like cherries. She used to like the taste.", "Misc.", True, "None", lambda: False, 1, ["pov switch", "whitney item"]],
        196 : [196, "Socketed Bat", "Has a socket the perfect size for a Key Stone. Unfortunately, you don't have one.", "Misc.", True, "None", lambda: False, 1, ["pov switch", "whitney item"]],
        197 : [197, "Old Picture", "You're doing a gnarly kickflip on your skateboard. But now you can't remember the last time you jumped.", "Misc.", True, "None", lambda: False, 1, ["pov switch", "ethan item"]],
        198 : [198, "First Aid Kit", "Just in case. You can never be too prepared.", "Misc.", True, "None", lambda: False, 1, ["pov switch", "ethan item"]],
        199 : [199, "Pichu", "Your little buddy.", "Misc.", True, "None", lambda: False, 1, ["pov switch", "ethan item"]],
        200 : [200, "GS Ball", "A memory. The initials \"GS\" are carved into its lid.", "Misc.", True, "None", lambda: False, 1, ["pov switch", "ethan item"]],
        201 : [201, "Picture of Daisy", "Your sister. You'll make things right for her.", "Misc.", True, "None", lambda: False, 1, ["pov switch", "blue item"]],
        202 : [202, "Dad's Coin", "Just sentiment.", "Misc.", True, "None", lambda: False, 1, ["pov switch", "blue item"]],
        203 : [203, "Mom's Watch", "Just sentiment.", "Misc.", True, "None", lambda: False, 1, ["pov switch", "blue item"]],
        204 : [204, "Hand Mirror", "Useful for making sure your hair's in-place. Used to be Daisy's.", "Misc.", True, "None", lambda: False, 1, ["pov switch", "blue item"]],
        205 : [205, "Diary", "Nothing that's written inside can be shown to the public--even less can be shown to children.", "Misc.", True, "None", lambda: False, 1, ["pov switch", "leaf item"]],
        206 : [206, "Towel", "You bring it everywhere you go. Useful for hitchhiking.", "Misc.", True, "None", lambda: False, 1, ["pov switch", "leaf item"]],
        207 : [207, "Root Fossil", "You meant to revive it before coming to Kobukan, but forgot it in your suitcase.", "Misc.", True, "None", lambda: False, 1, ["pov switch", "leaf item", "fossil"]],
        208 : [208, "Air Horn", "Carefully manufactured to wake up sleepyheads.", "Misc.", True, "None", lambda: False, 1, ["pov switch", "leaf item"]],
        209 : [209, "Wallace-Brand Pokémakeup Kit", "One of Uncle Wallace's first sponsors. Your Pokémon wear it proudly.", "Misc.", True, "None", lambda: False, 1, ["pov switch", "lisia item"]],
        210 : [210, "Instant Coffee", "For grandad. He's such a grump in the morning.", "Misc.", True, "None", lambda: False, 1, ["pov switch", "lisia item"]],
        211 : [211, "Brown Wig", "It deceives comically well.", "Misc.", True, "None", lambda: False, 1, ["pov switch", "lisia item"]],
        212 : [212, "Mega Tiara", "A gleaming Key Stone is embedded in it. Polished daily.", "Misc.", True, "None", lambda: False, 1, ["pov switch", "lisia item"]],
        213 : [213, "Ribbon Case", "Four Ranks. Five Categories. And your six Pokémon won them all. You are very proud of them.", "Misc.", True, "None", lambda: False, 1, ["pov switch", "lisia item"]],
        214 : [214, "Key to Sootopolis", "Shining silver. They gave it to you after the Super-Ancient Pokémon attacked... all you could do was cheer them up after, though.", "Misc.", True, "None", lambda: False, 1, ["pov switch", "lisia item"]],
        215 : [215, "Larvesta Egg", "Features a hair-like white texture.", "Misc.", True, "None", lambda: False, 1, ["egg hunt"]],
        216 : [216, "Togepi Egg", "Will become part of a Togepi's shell.", "Misc.", True, "None", lambda: False, 1, ["egg hunt"]],
        217 : [217, "Tyrogue Egg", "Its lilac and brown colors blend together perfectly.", "Misc.", True, "None", lambda: False, 1, ["egg hunt"]],
        218 : [218, "Smoochum Egg", "Has a yellow hair tuft poking from the top.", "Misc.", True, "None", lambda: False, 1, ["egg hunt"]],
        219 : [219, "Magby Egg", "It's very hot to the touch.", "Misc.", True, "None", lambda: False, 1, ["egg hunt"]],
        220 : [220, "Wynaut Egg", "It's completely blue.", "Misc.", True, "None", lambda: False, 1, ["egg hunt"]],
        221 : [221, "Bonsly Egg", "If it wasn't slightly rounded, it would be indistinguishable from a log.", "Misc.", True, "None", lambda: False, 1, ["egg hunt"]],
        222 : [222, "Mantyke Egg", "The colored texture makes it look like it's smiling.", "Misc.", True, "None", lambda: False, 1, ["egg hunt"]],
        223 : [223, "Toxel Egg", "Occasionally, the lighter-colored patches emit electricity.", "Misc.", True, "None", lambda: False, 1, ["egg hunt"]],
        224 : [224, "Deino Egg", "Has a dense patch of hair on the top.", "Misc.", True, "None", lambda: False, 1, ["egg hunt"]],
        225 : [225, "Dubious Disc", "Evolves Porygon2.", "Evo Items", True, "None", lambda: False, 2, ["Evo Items"]],
        226 : [226, "Mystery Gift", "The thing everyone craves.", "Misc.", True, "None", lambda: False, 10, []],
        227 : [227, "Rare Candy", "Increases a Pokémon's level.", "Medicines", True, "Pokemon", lambda mon: not (mon.GetLevel() >= 100 and mon.GetEvos() == []), 0, ["exp item"]],
        228 : [228, "Focus Sash", "Enables the equipped Pokémon to survive a move that would cause it to faint, once per battle.", "Battle Items", True, "None", lambda: False, 2, []],
        229 : [229, "Electric Seed", "Boosts the user's Defense in Electric Terrain.", "Battle Items", True, "None", lambda: False, 1, ["terrain seeds"]],
        230 : [230, "Grassy Seed", "Boosts the user's Defense in Grassy Terrain.", "Battle Items", True, "None", lambda: False, 1, ["terrain seeds"]],
        231 : [231, "Misty Seed", "Boosts the user's Special Defense in Misty Terrain.", "Battle Items", True, "None", lambda: False, 1, ["terrain seeds"]],
        232 : [232, "Psychic Seed", "Boosts the user's Special Defense in Psychic Terrain.", "Battle Items", True, "None", lambda: False, 1, ["terrain seeds"]],
        233 : [233, "Damp Rock", "Extends the duration of rain.", "Battle Items", True, "None", lambda: False, 1, ["weather rocks"]],
        234 : [234, "Heat Rock", "Extends the duration of harsh sunlight.", "Battle Items", True, "None", lambda: False, 1, ["weather rocks"]],
        235 : [235, "Icy Rock", "Extends the duration of hail and snow.", "Battle Items", True, "None", lambda: False, 1, ["weather rocks"]],
        236 : [236, "Smooth Rock", "Extends the duration of sandstorm.", "Battle Items", True, "None", lambda: False, 1, ["weather rocks"]],
        237 : [237, "Terrain Extender", "Extends the duration of terrains.", "Battle Items", True, "None", lambda: False, 1, []],
        238 : [238, "Soul Dew", "Boosts Latios and Latias' Special Attack and Special Defense.", "Battle Items", True, "None", lambda: False, 3, []],
        239 : [239, "Choice Band", "Boosts the equipped Pokémon's Attack, but locks it to use one move only.", "Battle Items", True, "None", lambda: False, 2, ["choice item"]],
        240 : [240, "Choice Scarf", "Boosts the equipped Pokémon's Speed, but locks it to use one move only.", "Battle Items", True, "None", lambda: False, 2, ["choice item"]],
        241 : [241, "Choice Specs", "Boosts the equipped Pokémon's Special Attack, but locks it to use one move only.", "Battle Items", True, "None", lambda: False, 2, ["choice item"]],
        242 : [242, "Thick Club", "Boosts Cubone and Marowak's Attack.", "Battle Items", True, "None", lambda: False, 1, []],
        243 : [243, "Air Balloon", "Enables the equipped Pokémon to float until hit by direct damage.", "Battle Items", True, "None", lambda: False, 1, []],
        244 : [244, "Heavy-Duty Boots", "Negates the effect of entry hazards for the equipped Pokémon.", "Battle Items", True, "None", lambda: False, 1, []],
        245 : [245, "Assault Vest", "Boosts the equipped Pokémon's Special Defense, but prevents it from using status moves.", "Battle Items", True, "None", lambda: False, 1, []],
        246 : [246, "Metronome", "Boosts the power of a move used consecutively.", "Battle Items", True, "None", lambda: False, 1, []],
        247 : [247, "Shell Bell", "Heals the equipped Pokémon after attacking.", "Battle Items", True, "None", lambda: False, 1, []],
        248 : [248, "Life Orb", "Boosts the power of all moves, but damages the equipped Pokémon after attacking.", "Battle Items", True, "None", lambda: False, 1, []],
        249 : [249, "Altarianite", "Allows Altaria to Mega Evolve.", "Misc.", True, "None", lambda: False, 4, ["megastone", "Altaria"]],
        250 : [250, "Aspear Berry", "Cures freeze and frostbite.", "Medicines", False, "Pokemon", lambda mon: mon.HasStatus("frozen") or mon.HasStatus("frostbitten"), 1, ["berry"]],
        251 : [251, "Lum Berry", "Cures non-volatile status conditions and confusion.", "Medicines", False, "Pokemon", lambda mon: mon.HasNormalStatus() or mon.HasStatus("confused"), 1, ["berry"]],
        252 : [252, "Muscle Band", "Boosts the power of physical moves.", "Battle Items", True, "None", lambda: False, 1, []],
        253 : [253, "Safety Goggles", "Protects the holder from weather damage and spore moves.", "Battle Items", True, "None", lambda: False, 1, []],
        254 : [254, "Iron Ball", "Grounds the Pokémon and halves its Speed. Only a couple uses for this item.", "Battle Items", True, "None", lambda: False, 1, []],
        255 : [255, "Apple", "These used to exist, but then people stopped being hungry, and they have no use anymore.", "Misc.", True, "None", lambda: False, 1, []],
        256 : [256, "Lopunnite", "Allows Lopunny to Mega Evolve.", "Misc.", True, "None", lambda: False, 4, ["megastone", "Lopunny"]],
        257 : [257, "Celebi Wing", "An appreciation of patience. No longer has a use, but can still be sold or gifted.", "Misc.", True, "None", lambda: False, 5, []],
        258 : [258, "Mirage Research #4", "Wally's Notes on the Unknown Mythical Pokémon hiding in Kobukan.", "Misc.", True, "None", lambda: True, 1, ["book", "not consumed"]],
        259 : [259, "Ghost Journal", "A running log of the information gathered from the Disciplinary Committee's investigation into Kobukan's ghosts.", "Misc.", True, "None", lambda: True, 1, ["book", "not consumed"]],
        260 : [260, "Lava Cookie", "Heals all status conditions. A delicacy from Lavaridge; warm and classically Hoennian. Keep away from Lance...", "Medicines", True, "Pokemon", lambda mon: mon.HasNormalStatus() or mon.HasStatus("confused"), 2, ["status healing"]],
        261 : [261, "Slowpoke Tail", "Humanely harvested, grilled to perfection, has a soft, marshmallowy texture. A very popular gift item.", "Misc.", True, "Pokemon", lambda: False, 10, []],
        262 : [262, "Mawilite", "Allows Mawile to Mega Evolve.", "Misc.", True, "None", lambda: False, 4, ["megastone", "Mawile"]],
        263 : [263, "Custap Berry", "Allows the Pokémon to move first in a pinch.", "Medicines", False, "None", lambda: mon.GetHealthPercentage() <= 0.25 or mon.HasAbility("Gluttony", False) and mon.GetHealthPercentage() <= 0.5, 1, []],
        264 : [264, "Quick Powder", "Doubles the speed of an untransformed Ditto.", "Battle Items", False, "None", lambda: False, 2, []],
        265 : [265, "Banettite", "Allows Banette to Mega Evolve.", "Misc.", True, "None", lambda: False, 4, ["megastone", "Banette"]],
        266 : [266, "Eviolite", "Boosts the defenses of a Pokémon that can still evolve.", "Battle Items", True, "None", lambda: False, 1, []],
        267 : [267, "Feebas Egg", "Laid by Champion Wallace's Milotic, Lucy. An egg of enormous prestige, especially for coordinators.", "Misc.", True, "None", lambda: False, 5, []],
        268 : [268, "Toxic Orb", "Badly Poisons the Pokémon holding it at the end of the turn.", "Battle Items", True, "None", lambda: False, 3, ["likedByJanine"]],
        269 : [269, "Exp. Candy XS", "Increases a Pokémon's experience by 100 points.", "Medicines", True, "Pokemon", lambda mon: mon.GetLevel() < 100 or mon.GetEvos() != [], 1, ["exp item"]],
        270 : [270, "Exp. Candy S", "Increases a Pokémon's experience by 800 points.", "Medicines", True, "Pokemon", lambda mon: mon.GetLevel() < 100 or mon.GetEvos() != [], 2, ["exp item"]],
        271 : [271, "Exp. Candy M", "Increases a Pokémon's experience by 3,000 points.", "Medicines", True, "Pokemon", lambda mon: mon.GetLevel() < 100 or mon.GetEvos() != [], 3, ["exp item"]],
        272 : [272, "Exp. Candy L", "Increases a Pokémon's experience by 10,000 points.", "Medicines", True, "Pokemon", lambda mon: mon.GetLevel() < 100 or mon.GetEvos() != [], 4, ["exp item"]],
        273 : [273, "Exp. Candy XL", "Increases a Pokémon's experience by 30,000 points.", "Medicines", True, "Pokemon", lambda mon: mon.GetLevel() < 100 or mon.GetEvos() != [], 5, ["exp item", "likedByJanine"]],
        274 : [274, "Oran Pot", "Decorates your dorm. Smells like oranges. Grows an Oran Berry once a day.", "Dorm", True, "None", lambda: False, 2, ["berry pot"]],
        275 : [275, "Rawst Pot", "Decorates your dorm. Smells like strawberries. Grows a Rawst Berry once every two days.", "Dorm", True, "None", lambda: False, 2, ["berry pot"]],
        276 : [276, "Cheri Pot", "Decorates your dorm. Smells like cherries. Grows a Cheri Berry once every two days.", "Dorm", True, "None", lambda: False, 2, ["berry pot"]],
        277 : [277, "Chesto Pot", "Decorates your dorm. Smells like water chestnuts. Grows a Chesto Berry once every two days.", "Dorm", True, "None", lambda: False, 2, ["berry pot"]],
        278 : [278, "Aspear Pot", "Decorates your dorm. Smells like pears. Grows an Aspear Berry once every two days.", "Dorm", True, "None", lambda: False, 2, ["berry pot"]],
        279 : [279, "Pecha Pot", "Decorates your dorm. Smells like peaches. Grows a Pecha Berry once every two days.", "Dorm", True, "None", lambda: False, 2, ["berry pot"]],
        280 : [280, "Sitrus Pot", "Decorates your dorm. Smells like citrons. Grows a Sitrus Berry once every three days.", "Dorm", True, "None", lambda: False, 3, ["berry pot"]],
        281 : [281, "Lum Pot", "Decorates your dorm. Smells like Kantonian plums. Grows a Lum Berry once every seven days.", "Dorm", True, "None", lambda: False, 4, ["berry pot", "likedByJanine"]],
        282 : [282, "Research Paper", "Professor Cherry loves these! Can be given to her to change the type of her next tutoring to one of your two highest.", "Misc.", True, "None", lambda: False, 1, []],
        283 : [283, "Experience Condenser", "Can be toggled on and off to store excess experience and convert it into EXP candies.", "Misc.", True, "None", lambda: True, 2, ["not consumed"]],
        284 : [284, "B5", "{size=29}The 'Balloon Bot Battle Bundle Beta.' Can be used in the Battle Hall to start a single, double, or triple battle against six defenseless Balloon Bots that yield no EXP or Liberation Limit.{/size}", "Misc.", True, "None", lambda: False, 2, []],
        285 : [285, "B5 Plus", "{size=29}The 'Better Balloon Bot Battle Bundle.' Can be used in the Battle Hall to start a single, double, or triple battle against six very powerful Balloon Bots with dangerous moves. Use with caution.{/size}", "Misc.", True, "None", lambda: False, 1, ["likedByJanine"]],
        286 : [286, "Secondhand Laptop", "Required to utilize various softwares.", "Dorm", True, "None", lambda: False, 3, []],
        287 : [287, "TM Software 2000", "{size=28}Can be used in conjunction with Blank TRs and Blank TMs to record moves your Pokémon use in battle, and create TRs/TMs out of them. It takes time to record the move data, and the device cannot be jostled, so you need to win the battle in order to successfully record the move data.{/size}", "Dorm", True, "None", lambda: False, 1, ["software"]],
        288 : [288, "TM Software XP", "{size=28}Can be used in conjunction with Blank TRs and Blank TMs to record moves your Pokémon use in battle, and create TRs/TMs out of them. The 'jostling' problem has been solved, and victory is no longer a prerequisite for a successful recording.{/size}", "Dorm", True, "None", lambda: False, 1, ["software"]],
        289 : [289, "TM Software Vista", "{size=28}Can be used in conjunction with Blank TRs and Blank TMs to record moves any Pokémon uses in battle, and create TRs/TMs out of them. The new AI-powered tracking camera allows you to lock onto moves that even opponents are using, and duplicate them perfectly.{/size}", "Dorm", True, "None", lambda: False, 1, ["software"]],
        290 : [290, "TM Software '05", "{size=28}Can be used in conjunction with Blank TRs and Blank TMs to record moves any Pokémon uses in battle, and create TRs/TMs out of them. Taking advantage of the newest advancements in CPU processing power, it no longer takes a turn to record a move, and can be done multiple times per battle.{/size}", "Dorm", True, "None", lambda: False, 1, ["software"]],
        291 : [291, "Blank TR", "Can be used in battle with TM Software to make a TR of a move. Breaks after one use.", "Battle Items", True, "None", (lambda: ValidateBlankTMTRUsage()), 3, ["not consumed"]],
        292 : [292, "Blank TM", "Can be used in battle with TM Software to make a TM of a move. Reusable, and better for the environment than a TR.", "Battle Items", True, "None", (lambda: ValidateBlankTMTRUsage()), 2, ["not consumed"]],
        293 : [293, "Technical Record", "Can be used to teach a Pokémon a move. Breaks after one use.", "Misc.", True, "None", lambda: True, 2, []],
        294 : [294, "Technical Machine Case", "Carries all your TMs, which can be used to teach a Pokémon a move. Reusable, and better for the environment than a TR.", "Misc.", True, "None", lambda: True, 1, ["not consumed"]],
        295 : [295, "Rhyhorn Reins", "Two long straps of leather. The Rhyhorn bites down and pulls--it's a delicate balance of strength and finesse.", "Misc.", True, "None", lambda: False, 1, ["pov switch", "serena item"]],
        296 : [296, "Coordinator Kit", "Contains makeup, masks, mirrors, and other embellishments.", "Misc.", True, "None", lambda: False, 1, ["pov switch", "serena item"]],
        297 : [297, "Tourist's Guide to Kalos", "Vital in the early days. Did you know Lumiose contains 19% of Kalos' population?", "Misc.", True, "None", lambda: False, 1, ["pov switch", "serena item"]],
        298 : [298, "OUTRAGE Magazine", "Classy literature. A gleaming red Gyarados emblazons the cover.", "Misc.", True, "None", lambda: False, 1, ["pov switch", "serena item"]],
        299 : [299, "Love Letters", "Unread, whether you wrote them or received them.", "Misc.", True, "None", lambda: False, 1, ["pov switch", "serena item"]],
        300 : [300, "Blue Handkerchief", "He forgot to ask for it back. It dries {i}your{/i} tears now.", "Misc.", True, "None", lambda: False, 1, ["pov switch", "serena item"]],
        301 : [301, "Ticket Stubs", "From a weekend when Mom was free.", "Misc.", True, "None", lambda: False, 1, ["pov switch", "serena item"]],
        302 : [302, "Cherish Ball", "Precious gifts are kept in this.", "Poké Balls", True, "None", lambda: inbattle, 7, ["universalLike"]],
        303 : [303, "Gimmighoul Coin", "A shiny coin favored by a certain Pokémon. Holding it to your ear, you swear you can hear laughing...", "Dorm", True, "None", lambda: False, 1, []],
        304 : [304, "Everstone", "You got this from Dawn. She seemed to have bad memories of it...", "Misc.", True, "None", lambda: False, 1, ["pov switch", "blue item"]],
        305 : [305, "Black Apricorn", "A curious fruit. Its ebony flesh is incredibly hard.", "Misc.", True, "None", lambda: False, 1, ["apricorn"]],
        306 : [306, "Blue Apricorn", "A curious fruit. Its cerulean flesh is incredibly hard.", "Misc.", True, "None", lambda: False, 1, ["apricorn"]],
        307 : [307, "Green Apricorn", "A curious fruit. Its verdant flesh is incredibly hard.", "Misc.", True, "None", lambda: False, 1, ["apricorn"]],
        308 : [308, "Pink Apricorn", "A curious fruit. Its roseate flesh is incredibly hard..", "Misc.", True, "None", lambda: False, 1, ["apricorn"]],
        309 : [309, "Red Apricorn", "A curious fruit. Its scarlet flesh is incredibly hard.", "Misc.", True, "None", lambda: False, 1, ["apricorn"]],
        310 : [310, "White Apricorn", "A curious fruit. Its alabaster flesh is incredibly hard.", "Misc.", True, "None", lambda: False, 1, ["apricorn"]],
        311 : [311, "Yellow Apricorn", "A curious fruit. Its amber flesh is incredibly hard.", "Misc.", True, "None", lambda: False, 1, ["apricorn"]]
    }

# ITEM FORMAT: (0: id, int); (1: name, str); (2: description, str); (3: category, str); (4: return after battle, bool); (5: scope, either "Pokemon", "Move", "None"); (6: usage condition, func); (7: default gift reaction, number), (8: tags, list)
    
    # ##### ITEM FUNCTIONS ##### #
    def RunItemFunction(event, itemtarget, args, item = "", ignoreEmbargo = False, ignoreKlutz = False):
        global activetreat
        global activerepel
        global repelstepsleft
        global Fled
        global bellrung
        global inbattle
        global CritCaptures

        global receivedUse
        global ItemText
        global invoverwrite
        ItemText = ""

        if item == "":
            item = itemtarget.GetItem() if isinstance(itemtarget, Pokemon) else args[0].GetItem()

        if item != None:
            name = GetItemName(item)
            # If the Pokémon is under embargo or has Klutz, the item is set to an unreachable value so that the default value (for the events that return something) is returned correctly
            if not ignoreEmbargo:
                if ((GetItemScope(item) == "Pokemon" and itemtarget.HasStatus("embargoed")) or (GetItemScope(item) == "Move" and args[0].HasStatus("embargoed"))):
                    item = -1
            if not ignoreKlutz and event != "used" and GetItemScope(item) == "Pokemon" and itemtarget.HasAbility("Klutz"):
                item = -1
        else:
            item = -1

        # EVENTS
        # "received" event: Receiving the item in-battle through the usage of Trick, Thief, etc. Relevant because some items are used immediately upon being received, if they pass the criteria, like berries.
        if event == "received":
            if IsBerry(item) and ValidateItemUsage(item, itemtarget) and (True if item not in [Item.OranBerry, Item.SitrusBerry] else itemtarget.GetHealthPercentage() < .5):
                RunItemFunction("used", itemtarget, [])
                ItemText += "{} ate the stolen {}!".format(itemtarget.GetNickname(), name)
                itemtarget.MarkItemUsed()
        
        # "forceReceived" - Receiving the *effect* of the item in-battle through Pluck or Bug Bite.
        elif event == "forceReceived":
            opponent = args[0]
            opponentitem = opponent.GetItem()

            if IsBerry(opponentitem):
                receivedUse = ""
                RunItemFunction("used", itemtarget, [True], opponentitem)
                ItemText += "{} consumed {}'s {}! {}".format(itemtarget.GetNickname(), opponent.GetNickname(), GetItemName(opponentitem), receivedUse)
                opponent.TakeItem()
        
        # "used" event: Using the item from the inventory, whether in or out of battle. PP Ups, Rare Candies, Evolutionary stones, etc.
        elif event == "used":
            posttext = ""

            if ItemHasCategory(item, "Poké Balls"): # Poké Balls
                canBeDitto = args[0]
                itemtarget = itemtarget[0]
                currenthp = itemtarget.Health

                if (itemtarget not in Battlers()):
                    renpy.say(None, "The {} was already captured, so you didn't use the {}!".format(itemtarget.GetNickname(), name))
                else:
                    if (random.random() > GetAverageProficiency() / 200.0 or GetRelationshipRank("Professor Cherry") == 0):
                        maxhp = itemtarget.GetStat(Stats.Health, ignorepositive=True, ignorenegative=True, triggerAbilities=False)
                        statbonus = 1.5 if itemtarget.HasStatus("poisoned") or itemtarget.HasStatus("burned") or itemtarget.HasStatus("paralyzed") or itemtarget.HasStatus("badly poisoned") else 1
                        statbonus = 2.5 if itemtarget.HasStatus("asleep") or itemtarget.HasStatus("frozen") else statbonus
                        ballbonus = 1
                        if (item == 1):
                            ballbonus = 1.5
                        elif (item == 2):
                            ballbonus = 2.0
                        catchratio = ((maxhp * 3 - currenthp * 2) * 4096 * ((700 - pokedexlookup(itemtarget.Id, DexMacros.Total)) / 700) / (3 * maxhp) / 4096) * statbonus * ballbonus

                        randnum = random.random()
                        caught = catchratio / randnum

                        if (item == 4):
                            caught = 1

                        itemtarget.Health = 0

                        if (caught > 0.25):
                            renpy.say(None, "The {} {{w=0.5}}shakes...".format(name))

                        if (caught > 0.5):
                            renpy.say(None, "The {} {{w=0.5}}shakes.".format(name))
                        
                        if (caught > 0.75):
                            renpy.say(None, "The {} {{w=0.5}}shakes!".format(name))

                        if (caught < 1):
                            renpy.say(None, "The {} {{w=0.5}}{{nw}}".format(name))
                            itemtarget.Health = currenthp
                            renpy.say(None, "The {} {{fast}}breaks...".format(name))

                            for mon in FriendlyBattlers():
                                if mon.HasItem(None) and mon.HasAbility("Ball Fetch"):
                                    renpy.say(None, "{} fetched the {}!".format(mon.GetNickname(), name))
                                    mon.GiveItem(item)
                                    break
                        else:
                            renpy.say(None, "The {} {{w=0.5}}clicks!".format(name))
                            if canBeDitto:
                                itemtarget.TryCatchDitto()
                            itemtarget.MakeCaught(currenthp)
                            renpy.hide("ditto")
                            
                    else: # Kris' Kritical Kapture Korner
                        itemtarget.Health = 0
                        CritCaptures += 1
                        renpy.say(None, "The {} {{w=0.5}}shakes...".format(name))

                        renpy.say(None, "The {} {{w=0.5}}clicks!".format(name))

                        renpy.say(None, "{b}A CRITICAL CAPTURE!{/b} You imagine Professor Cherry's proud grin.")

                        if (CritCaptures == 1):
                            ValueChange("Professor Cherry", 3, 0.5)
                        
                        if canBeDitto:
                            itemtarget.TryCatchDitto()
                        itemtarget.MakeCaught(currenthp)
                        renpy.hide("ditto")
                        
                itemtarget.Pokeball = item
            
            elif item in [Item.PechaBerry, Item.Antidote]:
                receivedUse = itemtarget.ClearStatus("poisoned")
                receivedUse = itemtarget.ClearStatus("badly poisoned")
            
            elif item in [Item.CheriBerry, Item.ParalyzeHeal]:
                receivedUse = itemtarget.ClearStatus("paralyzed")
            
            elif item in [Item.ChestoBerry, Item.Awakening]:
                receivedUse = itemtarget.ClearStatus("asleep")
            
            elif item in [Item.RawstBerry, Item.BurnHeal]:
                receivedUse = itemtarget.ClearStatus("burned")
            
            elif item in [Item.AspearBerry, Item.IceHeal]:
                receivedUse = itemtarget.ClearStatus("frozen")
                receivedUse = itemtarget.ClearStatus("frostbitten")
            
            elif item == Item.LumBerry:
                receivedUse = itemtarget.ClearStatus("all", nonvolatilesandconfusion = True)
            
            elif item == Item.OranBerry:
                itemtarget.AdjustHealth(10)
                receivedUse = "{} restored some health!".format(itemtarget.GetNickname())

            elif item == Item.SitrusBerry:
                itemtarget.AdjustHealth(itemtarget.GetStat(Stats.Health) / 4)
                receivedUse = "{} restored some health!".format(itemtarget.GetNickname())

            elif item == Item.Potion:
                itemtarget.AdjustHealth(20)
            
            elif item == Item.SuperPotion:
                itemtarget.AdjustHealth(60)
            
            elif item == Item.HyperPotion:
                itemtarget.AdjustHealth(120)
            
            elif item == Item.MaxPotion:
                itemtarget.AdjustHealth(999)
            
            elif item == Item.FullRestore:
                itemtarget.AdjustHealth(999)
                itemtarget.ClearStatus("all", nonvolatilesandconfusion = True)
            
            elif item == Item.Revive:
                FaintedMons.remove(itemtarget)
                itemtarget.AdjustHealth(itemtarget.GetStat(Stats.Health) / 2.0)
            
            elif item == Item.MaxRevive:
                FaintedMons.remove(itemtarget)
                itemtarget.AdjustHealth(999)
            
            elif item == Item.Ether:
                itemtarget.PP = min(itemtarget.PP + 10, itemtarget.MaxPP)
                posttext = "The PP of {}'s {} have been set to {}.".format(args[0].GetNickname(), itemtarget.Name, itemtarget.PP)
            
            elif item == Item.MaxEther:
                itemtarget.PP = itemtarget.MaxPP
                posttext = "The PP of {}'s {} have been maxed out.".format(args[0].GetNickname(), itemtarget.Name)
            
            elif item == Item.Elixir:
                for move in itemtarget.GetMoves():
                    move.PP = min(move.PP + 10, move.MaxPP)
                posttext = "The PP of {}'s moves have been increased by 10.".format(itemtarget.GetNickname())
            
            elif item == Item.MaxElixir:
                for move in itemtarget.GetMoves():
                    move.PP = move.MaxPP
                posttext = "The PP of {}'s moves have been maxed out.".format(itemtarget.GetNickname())
            
            elif item in [Item.FullHeal, Item.HealPowder, Item.LavaCookie]:
                itemtarget.ClearStatus("all", nonvolatilesandconfusion = True)
            
            elif item == Item.EnergyPowder:
                itemtarget.AdjustHealth(60)
            
            elif item == Item.EnergyRoot:
                itemtarget.AdjustHealth(120)
            
            elif item == Item.RevivalHerb:
                FaintedMons.remove(itemtarget)
                itemtarget.AdjustHealth(999)
            
            elif item == Item.PomegSmoothie:
                itemtarget.SetEV(Stats.Health, 0)
            
            elif item == Item.KelpsySmoothie:
                itemtarget.SetEV(Stats.Attack, 0)
            
            elif item == Item.HondewSmoothie:
                itemtarget.SetEV(Stats.SpecialAttack, 0)
            
            elif item == Item.QualotSmoothie:
                itemtarget.SetEV(Stats.Defense, 0)
            
            elif item == Item.GrepaSmoothie:
                itemtarget.SetEV(Stats.SpecialDefense, 0)
            
            elif item == Item.TamatoSmoothie:
                itemtarget.SetEV(Stats.Speed, 0)
            
            elif item == Item.HPUpConcentrate:
                itemtarget.SetEV(Stats.Health, 252)
            
            elif item == Item.ProteinConcentrate:
                itemtarget.SetEV(Stats.Attack, 252)
            
            elif item == Item.CalciumConcentrate:
                itemtarget.SetEV(Stats.SpecialAttack, 252)
            
            elif item == Item.IronConcentrate:
                itemtarget.SetEV(Stats.Defense, 252)
            
            elif item == Item.ZincConcentrate:
                itemtarget.SetEV(Stats.SpecialDefense, 252)
            
            elif item == Item.CarbosConcentrate:
                itemtarget.SetEV(Stats.Speed, 252)
            
            elif ItemHasTag(item, "rotom catalog"): # Rotom catalog
                newid = "Rotom (Rotom)"
                if (item == Item.Microwave):
                    newid = "Rotom (Heat Rotom)"
                elif (item == Item.WashingMchn):
                    newid = "Rotom (Wash Rotom)"
                elif (item == Item.Refrigerator):
                    newid = "Rotom (Frost Rotom)"
                elif (item == Item.Fan):
                    newid = "Rotom (Fan Rotom)"
                elif (item == Item.Lawnmower):
                    newid = "Rotom (Mow Rotom)"
                if (newid == pokedexlookup(itemtarget.GetId(), DexMacros.Forme)):
                    newid = "Rotom (Rotom)"
                renpy.invoke_in_new_context(itemtarget.ChangeForme, newid)

            elif item == Item.EscapeRope:
                renpy.jump("freeroam")

            elif item == Item.ExperienceCondenser:
                if (item not in inventorymetadata):
                    inventorymetadata[item] = [False, 0]
                renpy.call_in_new_context("useexpcondenser")
            
            elif item == Item.PokeDoll:
                Fled = True
            
            elif item in [Item.Repel, Item.SuperRepel, Item.MaxRepel]:
                activerepel = name
                repelstepsleft = 20
            
            elif ItemHasTag(item, "exp item"):
                if (item == Item.RareCandy and itemtarget in FaintedMons or itemtarget.GetHealthPercentage() <= 0):
                    FaintedMons.remove(itemtarget)
                    itemtarget.AdjustHealth(2 if itemtarget.Id != 292 else 1)
                if itemtarget.GetLevel() < 100:
                    if (item == Item.RareCandy):
                        PrintExp(itemtarget.GainExperience(itemtarget.CalculateAllExperienceNeededForLevel(itemtarget.GetMaxLevel() + 1) - itemtarget.GetExperience() + 1, ignorescaling=True))
                    elif (item == Item.ExpCandyXS):
                        PrintExp(itemtarget.GainExperience(100, ignorescaling=True))
                    elif (item == Item.ExpCandyS):
                        PrintExp(itemtarget.GainExperience(800, ignorescaling=True))
                    elif (item == Item.ExpCandyM):
                        PrintExp(itemtarget.GainExperience(3000, ignorescaling=True))
                    elif (item == Item.ExpCandyL):
                        PrintExp(itemtarget.GainExperience(10000, ignorescaling=True))
                    elif (item == Item.ExpCandyXL):
                        PrintExp(itemtarget.GainExperience(30000, ignorescaling=True))
                else:
                    pass # TODO: add the evolution mechanic once the evolution rework has been done
            
            elif item == Item.SootheBell:
                # TODO: replace after the evolution rework has been done
                if (playercharacter != None):
                    renpy.say(None, "You ring the bell, but you cannot hear it.")
                else:
                    anyinterest = False
                    for mon in playerparty:
                        if len(GetEvos(mon.Id)) > 0:
                            if (mon.Id == 133): # eevee consideration
                                hasfairymove = False
                                for move in mon.GetMoves():
                                    if (move.Type == "Fairy"):
                                        hasfairymove = True
                                        break
                                if (hasfairymove):
                                    evoid = 700 # transprideeon
                                elif (IsLater()):
                                    evoid = 197 # myfirstoceon
                                else: # ["Early Morning", "Morning", "Noon", "Afternoon"]
                                    evoid = 196 # tdpeon
                            else:
                                evoid = GetEvos(mon.Id)[0]

                            if (evoid == mon.Id):
                                continue
                                
                            evocondition = pokedexlookup(evoid, DexMacros.Evolve)
                            if (evocondition != None and "Friendship" in evocondition):
                                anyinterest = True
                                if ("Morn/Day" in evocondition and IsLater()):
                                    renpy.say(None, "{} seems interested in the bell's chime, but is tired due to the late hour, and won't approach.".format(mon.GetNickname()))
                                elif ("Night" in evocondition and IsEarlier()):
                                    renpy.say(None, "{} seems interested in the bell's chime, but shields its eyes from the sunlight, and won't approach.".format(mon.GetNickname()))
                                else:
                                    fv = FriendshipValues(mon, evoid)
                                    renpy.say(None, fv[1])
                                    if (fv[0]):
                                        mon.Evolve(pokedexlookup(evoid, DexMacros.Id))
                                        break
                    if (not anyinterest):
                        if (bellrung):
                            renpy.say(None, "None of your Pokémon seem to have any interest in the Soothe Bell.")
                        else:
                            renpy.say(None, "The bell rings, pure and clear.")
                            renpy.transition(dis)
                            renpy.show("whitney uniform surprised", [Transform(zoom=0.9, ypos=0.9, xpos=0.25)])
                            if (HasEvent("Whitney", "HasHappiny")):
                                renpy.say(whitney, "Huh? Sunnyside? Flan, come look! My Chansey's evolving!")
                            else:
                                renpy.say(whitney, "Huh? Guzzles? Flan, come look! My Munchlax is evolving!")
                            renpy.transition(dis)
                            renpy.hide("whitney")
                    bellrung = True
            
            elif ItemHasTag(item, "treat boost"): # Treat boost items
                activetreat = item
                posttext = "You will attract {}-type Pokémon more frequently.".format(treatboosts[item])
            
            elif item == Item.FreshWater:
                itemtarget.AdjustHealth(30)
            
            elif item == Item.HPUp:
                itemtarget.ModifyEV(Stats.Health, 10)
            
            elif item == Item.Protein:
                itemtarget.ModifyEV(Stats.Attack, 10)
            
            elif item == Item.Calcium:
                itemtarget.ModifyEV(Stats.SpecialAttack, 10)
            
            elif item == Item.Iron:
                itemtarget.ModifyEV(Stats.Defense, 10)
            
            elif item == Item.Zinc:
                itemtarget.ModifyEV(Stats.SpecialDefense, 10)
            
            elif item == Item.Carbos:
                itemtarget.ModifyEV(Stats.Speed, 10)

            elif item == Item.MirageResearch4:
                renpy.show_screen("book_mixed_text", mirageresearch4)

            elif item == Item.GhostJournal:
                renpy.show_screen("book_mixed_text", ghostjournal)

            elif item in [Item.BlankTR, Item.BlankTM]:
                itemname = GetItemName(item)
                softwaretype = Item.TMSoftware2000
                if (Item.TMSoftware05 in inventory):
                    softwaretype = Item.TMSoftware05
                elif (Item.TMSoftwareVista in inventory):
                    softwaretype = Item.TMSoftwareVista
                elif (Item.TMSoftwareXP in inventory):
                    softwaretype = Item.TMSoftwareXP
                copyablemoves = []
                for mon in (Battlers() if (softwaretype in [Item.TMSoftware05, Item.TMSoftwareVista]) else FriendlyBattlers()):
                    lastmove = GetLastMove(ActionLog, mon)
                    if (lastmove != None and not IsCustomMove(lastmove)):
                        copyablemoves.append((mon.GetNickname() + " - " + lastmove.Name, lastmove.Name))
                if (Item.TMSoftware05 in inventory):
                    renpy.say(None, "Which move would you like to record?")
                else:
                    renpy.say(None, "Which move would you like to begin recording?")
                copyablemoves.append(("Nevermind", "abort"))
                recordingmove = renpy.display_menu(copyablemoves)
                if (recordingmove == "abort"):
                    return
                if (softwaretype == Item.TMSoftware05):
                    inventorymetadata[item] = [Item.TMSoftware05, recordingmove]
                    RecordTMTRMove(item)
                    return
                
                if (softwaretype in [Item.TMSoftwareVista, Item.TMSoftwareXP]):
                    renpy.say(None, "You have started to record the move {}! The recording will be complete by the end of the battle.".format(recordingmove))
                else:
                    renpy.say(None, "You have started to record the move {}! The recording will be complete by the end of the battle, as long as you don't lose!".format(recordingmove))
                
                inventorymetadata[item] = [softwaretype, recordingmove]

            elif (item == Item.TechnicalMachineCase):
                renpy.call_in_new_context("usetm")

            elif (item == Item.TechnicalRecord):
                renpy.call_in_new_context("usetr")

            # Side effects
            if ItemHasTag(item, "bitter"):
                itemtarget.ApplyStatus("bitter")
            
            if not (len(args) != 0 and args[0]):
                receivedUse = ""

            if not item in [-1, ""]:
                if ItemHasTag(item, "book"):
                    invoverwrite = "You read {}.".format(name)
                else:
                    invoverwrite = "You used the {}".format(name) + ("." if GetItemScope(item) == "None" else " on {}.".format(itemtarget.GetNickname() if GetItemScope(item) == "Pokemon" else itemtarget.Name)) + ("" if posttext == "" else "\n{}".format(posttext))
        
        # "receivedStatus" event: The event is triggered whenever a Pokémon gains a status condition while holding an item
        elif event == "receivedStatus":
            status = args[0]
            
            if ((item == Item.CheriBerry and status == "paralyzed")
                or (item == Item.ChestoBerry and status == "asleep")
                or (item == Item.PechaBerry and status == "poisoned")
                or (item == Item.RawstBerry and status == "burned") 
                or (item == Item.AspearBerry and status in ["frozen", "frostbitten"])
                or (item == Item.LumBerry and status in normalstatuses + ["confused"])):
                itemtarget.ClearStatus(status)
                itemtarget.MarkItemUsed()
                ItemText = "{} ate the {} and is not {} anymore!".format(itemtarget.GetNickname(), name, status)
        
        # "takingDamage" event
        elif event == "takingDamage":
            if item == Item.OranBerry and itemtarget.GetHealthPercentage() < .5:
                itemtarget.AdjustHealth(10)
                itemtarget.MarkItemUsed()
                ItemText = "{} ate the {} and restored some health!".format(itemtarget.GetNickname(), name)
            elif item == Item.SitrusBerry and itemtarget.GetHealthPercentage() < .5:
                itemtarget.AdjustHealth(itemtarget.GetStat(Stats.Health) / 4)
                itemtarget.MarkItemUsed()
                ItemText = "{} ate the {} and restored some health!".format(itemtarget.GetNickname(), name)
        
        # "takingDirectDamage" event - when a Pokémon takes damage from a damaging move
        elif event == "takingDirectDamage":
            if item == Item.FocusSash and not itemtarget.HasStatus(".used focus sash"):
                itemtarget.AdjustHealth(1, True)
                if (itemtarget.HasStatus("deathless")):
                    itemtarget.AdjustHealth(itemtarget.GetStat(Stats.Health) / 2.0, True)
                itemtarget.ApplyStatus(".used focus sash", 1)
                ItemText += "{} survived thanks to the {}!".format(itemtarget.GetNickname(), name)
            
            if item == Item.AirBalloon:
                itemtarget.MarkItemUsed()
                ItemText = "{}'s {} popped!".format(itemtarget.GetNickname(), name)
        
        # "checkingXStat" events
        elif event == "checkingAttackStat":
            atk = args[0]

            if item == Item.ChoiceBand:
                return atk * 1.5
            elif item == Item.ThickClub and itemtarget.GetId() in [104, 105, 105.1]:
                return atk * 2
            return atk

        elif event == "checkingDefenseStat":
            dfn = args[0]

            if item == Item.Eviolite and len(GetEvos(itemtarget)) > 0:
                return dfn * 1.5

            return dfn

        elif event == "checkingSpeedStat":
            spd = args[0]
            
            if item in [Item.MachoBrace, Item.IronBall]:
                return spd / 2
            elif item == Item.ChoiceScarf:
                return spd * 1.5
            elif item == Item.QuickPowder and ValidateItemUsage(item, itemtarget):
                return spd * 2.0
            elif item == Item.QuickPowder and itemtarget.GetId() == pokedexlookupname("Ditto", DexMacros.Id):
                return spd * 1.5
            return spd

        elif event == "checkingSpAtkStat":
            spatk = args[0]
            
            if item == Item.DeepSeaTooth:
                return spatk * 2
            elif item == Item.ChoiceSpecs:
                return spatk * 1.5
            elif item == Item.SoulDew and itemtarget.GetId() in [380, 380.1, 381, 381.1]:
                return spatk * 1.5
            return spatk
        
        elif event == "checkingSpDefStat":
            spdef = args[0]
            
            if item == Item.DeepSeaScale:
                return spdef * 2
            elif item == Item.SoulDew and itemtarget.GetId() in [380, 380.1, 381, 381.1]:
                return spdef * 1.5
            elif item == Item.AssaultVest:
                return spdef * 1.5
            elif item == Item.Eviolite and len(GetEvos(itemtarget)) > 0:
                return spdef * 1.5

            return spdef
        
        elif event == "checkingCritStat":
            crit = args[0]
            
            if item in [Item.RazorClaw, Item.ScopeLens]:
                ItemText = "The critical chance was boosted by the {}!".format(name)
                return crit + 1
            return crit
        
        elif event == "checkingGroundedStat":
            if args[0] == "ungrounded": # The argument will tell whether we're checking for the Pokémon to be grounded or ungrounded
                if item == Item.AirBalloon:
                    return True
            else:
                if item == Item.IronBall:
                    return True
            return False
        
        # "blockEffect" event
        elif event == "blockEffect":
            cause = args[0]

            if item == Item.SafetyGoggles and cause in ["spore", "weather"]:
                return True
            return False

        # "attackValidation" event
        elif event == "attackValidation":
            move = args[0]

            if item == Item.AssaultVest:
                return move.Category != "Status" or move.Name == "Me First"
            return True
        
        # "afterAttacking" event (triggers only if the attack is successful)
        elif event == "afterAttacking":
            opponent = args[0]

            if item in [Item.RazorFang, Item.KingsRock]:
                return SideEffect(opponent, args, "flinching", chance=0.1)
            elif item == Item.ShellBell:
                itemtarget.AdjustHealth(max(itemtarget.GetStat(Stats.Health) * 1/8.0, 1))
                ItemText = "{} restored some health thanks to the {}!".format(itemtarget.GetNickname(), name)
            elif item == Item.LifeOrb:
                itemtarget.AdjustHealth(-max(itemtarget.GetStat(Stats.Health) * 1/10.0, 1))
                ItemText = "{} lost health due to the {}!".format(itemtarget.GetNickname(), name)
            return
        
        # "usingMove" event
        elif event == "usingMove":
            move = args[0]
            physical = move.Category == "Physical"
            power = args[1]
            
            if ItemHasTag(item, "move boost item"): # move boost items
                if ((item == Item.SilkScarf and move.Type == "Normal")
                    or (item == Item.Charcoal and move.Type == "Fire")
                    or (item == Item.MysticWater and move.Type == "Water")
                    or (item == Item.MiracleSeed and move.Type == "Grass")
                    or (item == Item.Magnet and move.Type == "Electric")
                    or (item == Item.NeverMeltIce and move.Type == "Ice")
                    or (item == Item.BlackBelt and move.Type == "Fighting")
                    or (item == Item.PoisonBarb and move.Type == "Poison")
                    or (item == Item.SoftSand and move.Type == "Ground")
                    or (item == Item.SharpBeak and move.Type == "Flying")
                    or (item == Item.TwistedSpoon and move.Type == "Psychic")
                    or (item == Item.SilverPowder and move.Type == "Bug")
                    or (item == Item.HardStone and move.Type == "Rock")
                    or (item == Item.SpellTag and move.Type == "Ghost")
                    or (item == Item.BlackGlasses and move.Type == "Dark")
                    or (item == Item.DragonFang and move.Type == "Dragon")
                    or (item == Item.MetalCoat and move.Type == "Steel")
                    or (item == Item.FairyFeather and move.Type == "Fairy")):
                    return power * 1.1
            
            if ItemHasTag(item, "type gem"): # type gems
                if ((item == Item.NormalTypeGem and move.Type == "Normal")
                    or (item == Item.FireTypeGem and move.Type == "Fire")
                    or (item == Item.WaterTypeGem and move.Type == "Water")
                    or (item == Item.GrassTypeGem and move.Type == "Grass")
                    or (item == Item.ElectricTypeGem and move.Type == "Electric")
                    or (item == Item.IceTypeGem and move.Type == "Ice")
                    or (item == Item.FightingTypeGem and move.Type == "Fighting")
                    or (item == Item.PoisonTypeGem and move.Type == "Poison")
                    or (item == Item.GroundTypeGem and move.Type == "Ground")
                    or (item == Item.FlyingTypeGem and move.Type == "Flying")
                    or (item == Item.PsychicTypeGem and move.Type == "Psychic")
                    or (item == Item.BugTypeGem and move.Type == "Bug")
                    or (item == Item.RockTypeGem and move.Type == "Rock")
                    or (item == Item.GhostTypeGem and move.Type == "Ghost")
                    or (item == Item.DarkTypeGem and move.Type == "Dark")
                    or (item == Item.DragonTypeGem and move.Type == "Dragon")
                    or (item == Item.SteelTypeGem and move.Type == "Steel")
                    or (item == Item.FairyTypeGem and move.Type == "Fairy")):
                    itemtarget.MarkItemUsed()
                    return power * 1.3
            
            if ItemHasTag(item, "plate"): # plates
                if ((item == Item.BlankPlate and move.Type == "Normal")
                    or (item == Item.FistPlate and move.Type == "Fighting")
                    or (item == Item.SkyPlate and move.Type == "Flying")
                    or (item == Item.ToxicPlate and move.Type == "Poison")
                    or (item == Item.EarthPlate and move.Type == "Ground")
                    or (item == Item.StonePlate and move.Type == "Rock")
                    or (item == Item.InsectPlate and move.Type == "Bug")
                    or (item == Item.SpookyPlate and move.Type == "Ghost")
                    or (item == Item.IronPlate and move.Type == "Steel")
                    or (item == Item.FlamePlate and move.Type == "Fire")
                    or (item == Item.SplashPlate and move.Type == "Water")
                    or (item == Item.MeadowPlate and move.Type == "Grass")
                    or (item == Item.ZapPlate and move.Type == "Electric")
                    or (item == Item.MindPlate and move.Type == "Psychic")
                    or (item == Item.IciclePlate and move.Type == "Ice")
                    or (item == Item.DracoPlate and move.Type == "Dragon")
                    or (item == Item.DreadPlate and move.Type == "Dark")
                    or (item == Item.PixiePlate and move.Type == "Fairy")):
                    return power * 1.2
                
                elif item == Item.LegendPlate:
                    pass # TODO: change Arceus' forme when (if) they're added

            if ItemHasTag(item, "choice item"): # Choice Items
                itemtarget.ApplyStatus(".lock on move", move.Name)

            if item == Item.Metronome:
                global ActionLog
                movelog = reversed([action for action in ActionLog if action.GetActionType() == ActionTypes.Move and action.GetUser() == itemtarget])
                consecutivemoves = 0
                for action in movelog:
                    if (action.GetTurn() >= itemtarget.GetTurnSwitchedIn() and action.GetSuccess() and consecutivemoves < 5):
                        consecutivemoves += 1
                    else:
                        break
                return power + 0.2 * consecutivemoves

            elif item == Item.LifeOrb:
                return power * 1.3

            elif item == Item.MuscleBand and physical:
                return power * 1.1
                
            return power
        
        # "hitByContactMove" event
        elif event == "hitByContactMove":
            attacker = args[0]
            
            if item == Item.RockyHelmet:
                attacker.AdjustHealth(-attacker.GetStat(Stats.Health) * 1/6.0)
                ItemText = "{} was hurt by {}'s {}!".format(attacker.GetNickname(), itemtarget.GetNickname(), name)
            elif item == Item.StickyBarb and attacker.HasItem(None):
                itemtarget.TakeItem()
                attacker.GiveItem(98)
                ItemText = "The {} attached to {}!".format(name, attacker.GetNickname())
        
        # "endOfTurn" event
        elif event == "endOfTurn":
            if item == Item.StickyBarb:
                itemtarget.AdjustHealth(-itemtarget.GetStat(Stats.Health) * 1/8.0)
                ItemText = "{} was hurt by the {}!".format(itemtarget.GetNickname(), name)
            elif item == Item.Leftovers:
                if (itemtarget.GetHealthPercentage() < 1):
                    itemtarget.AdjustHealth(max(itemtarget.GetStat(Stats.Health) * 1/16.0, 1))
                    ItemText = "{} restored some health thanks to the {}!".format(itemtarget.GetNickname(), name)
            elif item == Item.ToxicOrb:
                ItemText = itemtarget.ApplyStatus("badly poisoned")
        
        # "gainExp" event
        elif event == "gainExp":
            gainedExp = args[0]
            
            if item == Item.LuckyEgg and inbattle:
                return gainedExp * 1.5
            return gainedExp

        # "gainEVs" event
        elif event == "gainEVs":
            gainedEVs = args[0]

            if item == Item.MachoBrace:
                return gainedEVs * 2
            return gainedEVs

        # "onSwitch" event: returns False if itemtarget negates entry hazards
        elif event == "onSwitch":
            if ((item == Item.ElectricSeed and BattlefieldExists("Electric Terrain"))
                or (item == Item.GrassySeed and BattlefieldExists("Grassy Terrain"))):
                itemtarget.ChangeStats(Stats.Defense, 1)
            elif ((item == Item.MistySeed and BattlefieldExists("Misty Terrain"))
                or (item == Item.PsychicSeed and BattlefieldExists("Psychic terrain"))):
                itemtarget.ChangeStats(Stats.SpecialDefense, 1)
            elif item == Item.AirBalloon:
                ItemText = "{} floats thanks to the {}!".format(itemtarget.GetNickname(), name)
            elif item == Item.HeavyDutyBoots:
                return False
            return True
        
        # "settingWeatherTerrain" event
        elif event == "settingWeatherTerrain":
            weatherterrain = args[0]
            countdown = args[1]

            if ((item == Item.DampRock and weatherterrain == "rainy")
                or (item == Item.HeatRock and weatherterrain == "sunny")
                or (item == Item.IcyRock and weatherterrain in ["snowy", "hailing"])
                or (item == Item.SmoothRock and weatherterrain == "sandstorm")):
                ItemText = "The {} weather was prolonged by {}'s {}!".format(weatherterrain, itemtarget.GetNickname(), name)
                return 8
            elif (item == Item.TerrainExtender and weatherterrain in ["Electric Terrain", "Grassy Terrain", "Misty Terrain", "Psychic Terrain"]):
                ItemText = "The {} was prolonged by {}'s {}!".format(weatherterrain, itemtarget.GetNickname(), name)
                return 8
            return countdown

        # "removed" event
        elif event == "removed":
            if ItemHasTag(item, "choice item") and not itemtarget.HasAbility("Gorilla Tactics", False):
                itemtarget.ClearStatus(".fixated")

        elif event == "prioritizingMoves":
            if item == Item.CustapBerry:
                if (ValidateItemUsage(item, itemtarget)):
                    itemtarget.MarkItemUsed()
                    ItemText = "{} ate the {} and moved first!".format(itemtarget.GetNickname(), name)
                    return 0.04
            return 0

