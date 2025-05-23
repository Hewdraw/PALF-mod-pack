﻿init python:
    def FormatText(text):
        # Function to perform formatting on text outside curly braces
        def format_outside_braces(text):
            return text.replace("!", "! ").replace(".", ". ").replace("  ", " ").replace(". . .", "...")
        
        # Pattern to find text within curly braces
        pattern = re.compile(r'{[^{}]*}')
        
        # Find all text within curly braces
        matches = pattern.findall(text)
        
        # Replace text within curly braces with placeholders
        placeholder = "__BRACE_TEXT__"
        text_with_placeholders = pattern.sub(placeholder, text)
        
        # Format the text with placeholders
        formatted_text = format_outside_braces(text_with_placeholders)
        
        # Reinsert the text within curly braces
        for match in matches:
            formatted_text = formatted_text.replace(placeholder, match, 1)
        
        return formatted_text

    def LastResortWorks(actionlog, user):
        movesused = []
        nummovesneeded = max(len(user.GetMoves()) - 1, 1)
        for action in reversed(actionlog):
            if (action.GetActionType() == ActionTypes.Move 
                and not action.GetMove().Name in movesused 
                and action.GetUser() == user 
                and action.GetMove().Name != "Last Resort"):
                movesused.append(action.GetMove().Name)
            elif (action.GetActionType() == ActionTypes.Pokemon and action.GetTargets() == user):#if this 'mon ever switched in at some point, stop counting before here
                return nummovesneeded <= len(movesused)
        return nummovesneeded <= len(movesused)

    def PaybackDoubles(user, target):
        for action in reversed(ActionLog):
            if (action.GetUser() == target and action.GetActionType() in [ActionTypes.Move, ActionTypes.Bag] and action.GetTurn() == Turn):
                return True
        return False

    def RoundDoubles(user):
        for action in reversed(ActionLog):
            if (action.GetActionType() == ActionTypes.Move and action.GetTurn() == Turn and action.GetMove().Name == "Round" and action.GetUser() != user):
                return True
        return False

    def GetLastMove(actionlog, user=None, target=None, ignorepp=False, ignoremoves=[], returnnonemoves=[], lookformoves=[], returnaction=False, ignorefailures=False):
        for action in reversed(actionlog):
            if (action.GetActionType() == ActionTypes.Move 
                and (user == None or (action.GetUser() == user and action.GetTurn() >= user.GetTurnSwitchedIn()))
                and (target == None or target in action.GetTargets())
                and action.GetMove().Name not in ignoremoves
                and action.GetMove().Name not in returnnonemoves
                and (not ignorefailures or action.GetSuccess())
                and (lookformoves == [] or action.GetMove().Name in lookformoves)):
                if (ignorepp):
                    thismove = copy.deepcopy(action.GetMove())
                    thismove.PP = thismove.MaxPP
                    return thismove
                elif (returnaction):
                    return action
                else:
                    return action.GetMove()
            elif (action.GetActionType() == ActionTypes.Move 
                and (user == None or action.GetUser() == user)
                and action.GetMove().Name not in ignoremoves
                and action.GetMove().Name in returnnonemoves):
                return None
        return None

    def JustSwitchedIn(actionlog, pkmn):
        if (Turn == 0):
            return True
        for action in reversed(actionlog):
            if (action.GetActionType() == ActionTypes.Pokemon and pkmn in action.GetTargets() and action.GetTurn() == Turn):
                return True
        return False

    def BattlefieldExists(battlefield):
        try:
            return battlefield in BattlefieldEffects.keys()
        except:
            return False        

    #I know this could be simplified, but I'm doing it like this for legibility
    def IsGrounded(pkmn):
        if (pkmn.HasStatus("smacked down") or BattlefieldExists("Gravity") or pkmn.HasStatus("roosted") or RunItemFunction("checkingGroundedStat", pkmn, ["grounded"])):
            return True
        if ("Flying" in pkmn.GetTypes() or pkmn.HasAbility("Levitate", False) or pkmn.HasStatus("levitating") or RunItemFunction("checkingGroundedStat", pkmn, ["ungrounded"])):
            return False
        return True

    def IsGroundedSimpleWorld(pkmn, flyingcheck):
        if (pkmn.HasStatus("smacked down") or BattlefieldExists("Gravity") or pkmn.HasStatus("roosted") or RunItemFunction("checkingGroundedStat", pkmn, ["grounded"])):
            return True
        if (flyingcheck or pkmn.HasAbility("Levitate", False) or pkmn.HasStatus("levitating") or RunItemFunction("checkingGroundedStat", pkmn, ["ungrounded"])):
            return False
        return True

    def GetImprisonedMoves(mon):
        imprisoningfoe = StatusOnFoes(mon, "imprisoning")
        if (imprisoningfoe != None):
            return imprisoningfoe.GetMoveNames()
        else:
            return []

    def ContinuingMove(user, name):
        for condition, moves in movestatuses.items():
            if (user.HasStatus(condition) and name in moves):
                return True
        return False

    def MoveValid(user, maybemove):
        name = maybemove.Name
        return not (maybemove.PP == 0 and not ContinuingMove(user, name)
            or (user.HasStatus(".lock on move") and user.GetStatusCount(".lock on move") != name)
            or (user.HasStatus("taunted") and maybemove.Category == "Status") 
            or (user.HasStatus("encored") and maybemove != GetLastMove(ActionLog, user, ignorefailures=True))
            or (user.HasStatus("rollout") and name != "Rollout")
            or (user.HasStatus("ice ball") and name != "Ice Ball")
            or (user.HasStatus("biding") and name != "Bide")
            or (user.HasStatus(".disabling") and name == user.GetStatusCount(".disabling"))
            or (user.HasStatus("tormented") and maybemove == GetLastMove(ActionLog, user))
            or (user.HasStatus("dug in") and name != "Dig")
            or (user.HasStatus("diving") and name != "Dive")
            or (user.HasStatus("airborne") and name not in ["Fly", "Bounce"])
            or (user.HasStatus("cloaked in light") and name != "Sky Attack")
            or (user.HasStatus("charging light") and name != "Solar Beam")
            or (user.HasStatus("thrashing") and name != "Thrash")
            or (user.HasStatus("gasping") and IsSoundMove(name))
            or (user.HasStatus("unhealthy") and IsHealingMove(name))
            or (BattlefieldExists("Gravity") and name in ["Bounce", "Fly", "Flying Press", "High Jump Kick", "Jump Kick", "Magnet Rise", "Sky Drop", "Splash", "Telekinesis"])
            or (not RunItemFunction("attackValidation", user, [maybemove]))
            or (name in GetImprisonedMoves(user))
            or (name == "Gigaton Hammer" and maybemove == GetLastMove(ActionLog, user)))

    def HasValidMoves(user):
        for move in user.GetMoves():
            if (MoveValid(user, move)):
                return True
        return False

    def WeatherIs(weather, ignoreairlock=False):
        if (weather == None and CurrentWeather == None):
            return True
        return (CurrentWeather != None and CurrentWeather[0] == weather) and (ignoreairlock or not AbilityOnField("Cloud Nine"))

    def IsExplosion(movename):
        if (not isinstance(movename, str)):
            movename = movename.Name
        return movename in ["Self-Destruct", "Explosion", "Mind Blown", "Misty Explosion"]

    def IsPunchMove(movename):
        if (not isinstance(movename, str)):
            movename = movename.Name
        return "Punch" in movename or movename in ["Meteor Mash", "Headlong Rush", "Plasma Fists", "Rage Fist", "Surging Strikes", "Wicked Blow", "Meteor Mash", "Sky Uppercut", "Ice Hammer", "Hammer Arm", "Double Iron Bash", "Headlong Rush"]

    def IsSliceMove(movename):
        if (not isinstance(movename, str)):
            movename = movename.Name
        return movename in ["Aerial Ace", "Air Cutter", "Air Slash", "Aqua Cutter", "Behemoth Blade", "Bitter Blade", "Ceaseless Edge", "Cross Poison", "Cut", "Fury Cutter", "Kowtow Cleave", "Leaf Blade", "Night Slash", "Population Bomb", "Psyblade", "Psycho Cut", "Razor Leaf", "Razor Shell", "Sacred Sword", "Slash", "Solar Blade", "Stone Axe", "X-Scissor"]

    def IsSoundMove(movename):
        if (not isinstance(movename, str)):
            movename = movename.Name
        return movename in ["Boomburst", "Bug Buzz", "Chatter", "Clanging Scales", "Clangorous Soul", "Clangorous Soulblaze", "Confide", "Disarming Voice", "Echoed Voice", "Eerie Spell", "Grass Whistle", "Growl", "Heal Bell", "Howl", "Hyper Voice", "Metal Sound", "Noble Roar", "Overdrive", "Parting Shot", "Perish Song", "Relic Song", "Roar", "Round", "Screech", "Shadow Panic*", "Sing", "Snarl", "Snore", "Sparkling Aria", "Supersonic", "Torch Song", "Uproar"]

    def IsBiteMove(movename):
        if (not isinstance(movename, str)):
            movename = movename.Name
        return "Fang" in movename or movename in ["Bite", "Crunch", "Fishious Rend", "Jaw Lock"]

    def IsKickMove(movename):
        if (not isinstance(movename, str)):
            movename = movename.Name
        return "Kick" in movename or movename in ["Triple Axel", "Stomp"]

    def IsWeatherMove(movename):
        if (not isinstance(movename, str)):
            movename = movename.Name
        return movename in ["Rain Dance", "Sunny Day", "Snowscape", "Chilly Reception", "Hail", "Sandstorm", "Healing Spring"]

    def IsWindMove(movename):
        if (not isinstance(movename, str)):
            movename = movename.Name
        return movename in ["Aeroblast", "Air Cutter", "Bleakwind Storm", "Blizzard", "Fairy Wind", "Gust", "Heat Wave", "Hurricane", "Icy Wind", "Petal Blizzard", "Sandsear Storm", "Sandstorm", "Springtide Storm", "Tailwind", "Twister", "Whirlwind", "Wildbolt Storm"]

    def IsDanceMove(movename):
        if (not isinstance(movename, str)):
            movename = movename.Name
        return "Dance" in movename or movename in ["Aqua Step", "Clangorous Soul"]

    def IsRecklessMove(movename):
        if (not isinstance(movename, str)):
            movename = movename.Name
        return movename in ["Axe Kick", "High Jump Kick", "Jump Kick", "Supercell Slam", "Brave Bird", "Chloroblast", "Double-Edge", "Flare Blitz", "Head Charge", "Head Smash", "Light of Ruin", "Mind Blown", "Self-Destruct", "Shadow End", "Shadow Rush", "Struggle", "Submission", "Take Down", "Volt Tackle", "Wave Crash", "Wild Charge", "Wood Hammer"]

    def IsSwitchingMove(movename):
        if (not isinstance(movename, str)):
            movename = movename.Name
        return movename in ["Baton Pass", "Chilly Reception", "Flip Turn", "Parting Shot", "Shed Tail", "Teleport", "U-turn", "Volt Switch"]

    def IsPriorityMove(movename):
        if (not isinstance(movename, str)):
            movename = movename.Name
        return movename in ["Accelerock", "Ally Switch", "Aqua Jet", "Baby-Doll Eyes", "Baneful Bunker", "Bide", "Bullet Punch", "Burning Bulwark", "Crafty Shield", "Detect", "Endure", "Extreme Speed", "Fake Out", "Feint", "First Impression", "Follow Me", "Grassy Glide", "Helping Hand", "Ice Shard", "Ion Deluge", "Jet Punch", "King's Shield", "Mach Punch", "Magic Coat", "Obstruct", "Powder", "Protect", "Quick Attack", "Quick Guard", "Rage Powder", "Shadow Sneak", "Silk Trap", "Snatch", "Spiky Shield", "Spotlight", "Sucker Punch", "Thunderclap", "Upper Hand", "Vacuum Wave", "Water Shuriken", "Wide Guard", "Zippy Zap"]

    def IsAuraPulseMove(movename):
        if (not isinstance(movename, str)):
            movename = movename.Name
        return "Pulse" in movename or movename in ["Aura Sphere"]

    def IsBallBombMove(movename):
        if (not isinstance(movename, str)):
            movename = movename.Name
        return movename in ["Acid Spray", "Aura Sphere", "Barrage", "Beak Blast", "Bullet Seed", "Egg Bomb", "Electro Ball", "Energy Ball", "Focus Blast", "Gyro Ball", "Ice Ball", "Magnet Bomb", "Mist Ball", "Mud Bomb", "Octazooka", "Pollen Puff", "Pyro Ball", "Rock Blast", "Rock Wrecker", "Searing Shot", "Seed Bomb", "Shadow Ball", "Sludge Bomb", "Syrup Bomb", "Weather Ball", "Zap Cannon"]

    def IsChargeRechargeMove(movename):
        if (not isinstance(movename, str)):
            movename = movename.Name
        return movename in ["Bounce", "Dig", "Dive", "Electro Shot", "Fly", "Freeze Shock", "Geomancy", "Ice Burn", "Meteor Beam", "Phantom Force", "Razor Wind", "Shadow Force", "Skull Bash", "Sky Attack", "Sky Drop", "Solar Beam", "Solar Blade", "Blast Burn", "Eternabeam", "Frenzy Plant", "Giga Impact", "Hydro Cannon", "Hyper Beam", "Meteor Assault", "Prismatic Laser", "Roar of Time", "Rock Wrecker", "Shadow Half"]

    def IsPowderSporeMove(movename):
        if (not isinstance(movename, str)):
            movename = movename.Name
        return "Spore" in movename or ("Powder" in movename and movename != "Powder Snow")

    def AbilityOnField(abilityname):
        for mon in Battlers():
            if mon.HasAbility(abilityname):
                return True
        return False

    def StatusInBattlers(statusname):
        for mon in Battlers():
            if mon.HasStatus(statusname):
                return True
        return False

    def StatusOnFoes(mon, statusname):
        if (mon in FriendlyBattlers()):
            for othermon in EnemyBattlers():
                if othermon.HasStatus(statusname):
                    return othermon
        else:
            for othermon in FriendlyBattlers():
                if othermon.HasStatus(statusname):
                    return othermon
        return None

    def EffectOnOwnField(mon, effectname):
        if (mon == None):
            return False
        if (mon.GetTrainerType() != TrainerType.Enemy):
            return effectname in FriendlyEffects.keys()
        else:
            return effectname in EnemyEffects.keys()

    def EffectOnOpponentField(mon, effectname):
        if (mon == None):
            return False
        if (mon.GetTrainerType() == TrainerType.Enemy):
            return effectname in FriendlyEffects.keys()
        else:
            return effectname in EnemyEffects.keys()

    def EffectCountOnOpponentField(mon, effectname):
        if (mon.GetTrainerType() == TrainerType.Enemy):
            if (effectname in FriendlyEffects.keys()):
                return FriendlyEffects[effectname] 
        else:
            if (effectname in EnemyEffects.keys()):
                return EnemyEffects[effectname] 
        return 0

    def GetFieldEffects(mon):
        if (mon.GetTrainerType() == TrainerType.Enemy):
            return EnemyEffects
        else:
            return FriendlyEffects

    def GetBattlers(mon, reverse = False):
        if (mon == None):
            return []
        if (mon.GetTrainerType() == TrainerType.Enemy):
            return EnemyBattlers() if not reverse else FriendlyBattlers()
        else:
            return FriendlyBattlers() if not reverse else EnemyBattlers()

    def IsHealingMove(movename):
        if (not isinstance(movename, str)):
            movename = movename.Name
        return movename in ["Life Dew", 'Draining Kiss', 'Floral Healing', 'Giga Drain', 'Rest', 'Synthesis', 'Absorb', 'Drain Punch', 'Dream Eater', 'Heal Order', 'Heal Pulse', 'Healing Wish', 'Horn Leech', 'Leech Life', 'Lunar Dance', 'Mega Drain', 'Milk Drink', 'Moonlight', 'Morning Sun', 'Oblivion Wing', 'Parabolic Charge', 'Purify', 'Recover', 'Roost', 'Shore Up', 'Slack Off', 'Soft-Boiled', 'Strength Sap', 'Swallow', 'Wish']

    def AbilityOnOpponentField(originmon, abilityname, splash=True):
        for mon in GetBattlers(originmon, True):
            if mon.HasAbility(abilityname, splash):
                return True
        return False

    def AbilityOnOwnField(originmon, abilityname, excludeself=False):
        for mon in GetBattlers(originmon):
            if (excludeself or originmon != mon) and mon.HasAbility(abilityname):
                return True
        return False

    def NumAbilityOnOwnField(originmon, abilityname, excludeself=False):
        count = 0
        for mon in GetBattlers(originmon):
            if ((not excludeself or mon != originmon) and mon.HasAbility(abilityname)):
                count += 1
        return count
            
    def MakesContact(move):
        contact = True
        if (move.Category != "Physical"):
            contact = False

        if (move.Name in ["Aqua Cutter", "Attack Order", "Aura Wheel", "Barrage", "Beak Blast", "Beat Up", "Bone Club", "Bone Rush", "Bonemerang", "Bulldoze", "Bullet Seed", "Diamond Storm", "Dragon Darts", "Drum Beating", "Earthquake", "Egg Bomb", "Explosion", "Feint", "Fissure", "Flower Trick", "Freeze Shock", "Fusion Bolt", "Gigaton Hammer", "Grav Apple", "Gunk Shot", "Ice Shard", "Icicle Crash", "Icicle Spear", "Land's Wrath", "Last Respects", "Leafage", "Magnet Bomb", "Magnitude", "Metal Burst", "Meteor Assault", "Natural Gift", "Order Up", "Pay Day", "Petal Blizzard", "Pin Missile", "Poison Sting", "Poltergeist", "Precipice Blades", "Present", "Psycho Cut", "Pyro Ball", "Razor Leaf", "Rock Blast", "Rock Slide", "Rock Throw", "Rock Tomb", "Rock Wrecker", "Sacred Fire", "Salt Cure", "Sand Tomb", "Scale Shot", "Secret Power", "Seed Bomb", "Self-Destruct", "Shadow Bone", "Sky Attack", "Smack Down", "Sinister Arrow Raid", "Spike Cannon", "Spirit Shackle", "Splintered Stormshards", "Stone Edge", "Thousand Arrows", "Thousand Waves", "Twineedle", "Electro Drift", "Infestation", "Draining Kiss", "Grass Knot", "Wring Out", "Trump Card", "Petal Dance"]):
            contact = not contact
        return contact

    def IsIgnorable(ability):
        return ability in ["Battle Armor", "Clear Body", "Damp", "Dry Skin", "Filter", "Flash Fire", "Flower Gift", "Heatproof", "Hyper Cutter", "Immunity", "Inner Focus", "Insomnia", "Keen Eye", "Leaf Guard", "Levitate", "Lightning Rod", "Limber", "Magma Armor", "Marvel Scale", "Motor Drive", "Oblivious", "Own Tempo", "Sand Veil", "Shell Armor", "Shield Dust", "Simple", "Snow Cloak", "Solid Rock", "Soundproof", "Sticky Hold", "Storm Drain", "Sturdy", "Suction Cups", "Tangled Feet", "Thick Fat", "Unaware", "Vital Spirit", "Volt Absorb", "Water Absorb", "Water Veil", "White Smoke", "Wonder Guard", "Big Pecks", "Contrary", "Friend Guard", "Heavy Metal", "Light Metal", "Magic Bounce", "Multiscale", "Sap Sipper", "Telepathy", "Wonder Skin", "Aura Break", "Aroma Veil", "Bulletproof", "Flower Veil", "Fur Coat", "Overcoat", "Sweet Veil", "Dazzling", "Disguise", "Fluffy", "Queenly Majesty", "Water Bubble", "Ice Scales", "Ice Face", "Mirror Armor", "Pastel Veil", "Punk Rock", "Armor Tail", "Earth Eater", "Good as Gold", "Purifying Salt", "Well-Baked Body", "Wind Rider"]

    def ActivateMoody(pkmn):
        canraise = []
        canlower = []
        returnable = ""

        for i in range(Stats.Attack, Stats.Speed + 1):
            statmod = pkmn.GetStatChanges(i)
            if (statmod != -6):
                canlower.append(i)
            if (statmod != 6):
                canraise.append(i)
        
        raising = (None if len(canraise) == 0 else random.choice(canraise))
        if (raising != None):
            returnable += pkmn.ChangeStats(raising, 2, pkmn)
            if (raising in canlower):
                canlower.remove(raising)

        lowering = (None if len(canlower) == 0 else random.choice(canlower))
        if (lowering != None):
            returnable += pkmn.ChangeStats(lowering, -1, pkmn)

        if ("Toxel Everal" in pkmn.GetForeverals()):
            pkmn.Nature = RandInt(0, 24)

        return returnable

    def IsSpecialAbility(ability):
        return ability in ["Prism Armor", "Thrice Denied", "Truant", "Multitype", "Stance Change", "Schooling", "Comatose", "Shields Down", "Disguise", "RKS System", "Battle Bond", "Power Construct", "Ice Face", "Gulp Missile", "Zero to Hero", "Commander", "Trace", "Forecast", "Flower Gift", "Zen Mode", "Illusion", "Imposter", "Power of Alchemy", "Receiver", "Disguise", "Power Construct", "Ice Face", "Hunger Switch", "Gulp Missile", "Neutralizing Gas", "Zero to Hero", "Commander"]

    def CanSwitch(pkmn, forced, selfforced=False):
        if (selfforced or (forced and not pkmn.HasStatus("ingrained")) or pkmn.HasType("Ghost") or pkmn.GetHealthPercentage() <= 0.0):
            return True
        return not (
        pkmn.HasStatus("blocked")
        or pkmn.HasStatus("menaced")
        or pkmn.HasStatus("webbed")
        or pkmn.HasStatus("ingrained") 
        or pkmn.HasStatus("firespun") 
        or pkmn.HasStatus("octolocked") 
        or pkmn.HasStatus("whirlpooled") 
        or pkmn.HasStatus("bound") 
        or pkmn.HasStatus("clamped") 
        or pkmn.HasStatus("infested") 
        or pkmn.HasStatus("wrapped") 
        or pkmn.HasStatus("anchored") 
        or pkmn.HasStatus("shackled")
        or pkmn.HasStatus("entombed")
        or pkmn.HasStatus("no retreat")
        or (IsGrounded(pkmn) and AbilityOnOpponentField(pkmn, "Arena Trap"))
        or (AbilityOnOpponentField(pkmn, "Shadow Tag") and not (pkmn.HasAbility("Shadow Tag"))) 
        or (pkmn.HasType("Steel") and AbilityOnOpponentField(pkmn, "Magnet Pull")))

    def MoveIsIn(move):
        return move in movesin
    
    def AbilityIsIn(ability):
        return ability in abilitiesin
    
    def GetCamoType():
        camotype = "Normal"
        if (BattlefieldExists("Electric Terrain")):
            camotype = "Electric"
        elif (location == "laboratory" or BattlefieldExists("Misty Terrain")):
            camotype = "Fairy"
        elif (location in ["unhallowed holt", "catacombs"] or BattlefieldExists("Burial Ground")):
            camotype = "Ghost"
        elif (location == "fields" or BattlefieldExists("Grassy Terrain")):
            camotype = "Grass"
        elif (location == "alley"):
            camotype = "Poison"
        elif (location == "seaport"):
            camotype = "Water"
        elif (location == "windswept woods"):
            camotype = "Flying"
        elif (location == "shattered glades"):
            camotype = "Fighting"
        elif (location == "city"):
            camotype = "Steel"
        elif (location == "mountain"):
            camotype = "Ice"
        elif (location == "campus"):
            camotype = "Rock"
        elif (location.title() in typenums):
            camotype = location.title()
        return camotype

    def IsGenderless(mon):
        return pokedexlookup(mon.GetId(), DexMacros.Name) in ["Balloon Bot", "Arceus", "Arctovish", "Arctozolt", "Articuno", "Azelf", "Baltoy", "Beldum", "Blacephalon", "Bronzong", "Bronzor", "Brute Bonnet", "Buzzwole", "Calyrex", "Carbink", "Celebi", "Celesteela", "Chi-Yu", "Chien-Pao", "Claydol", "Cobalion", "Cosmoem", "Cosmog", "Cryogonal", "Darkrai", "Deoxys", "Dhelmise", "Dialga", "Diancie", "Ditto", "Dracovish", "Dracozolt", "Electrode", "Entei", "Eternatus", "Falinks", "Fezandipiti", "Flutter Mane", "Genesect", "Gholdengo", "Gimmighoul", "Giratina", "Glastrier", "Golett", "Golurk", "Great Tusk", "Groudon", "Guzzlord", "Ho-Oh", "Hoopa", "Iron Bundle", "Iron Hands", "Iron Jugulis", "Iron Leaves", "Iron Moth", "Iron Thorns", "Iron Treads", "Iron Valiant", "Jirachi", "Kartana", "Keldeo", "Klang", "Klink", "Klinklang", "Koraidon", "Kyogre", "Kyurem", "Lugia", "Lunala", "Lunatone", "Magearna", "Magnemite", "Magneton", "Magnezone", "Manaphy", "Marshadow", "Maushold", "Melmetal", "Meloetta", "Meltan", "Mesprit", "Metagross", "Metang", "Mew", "Mewtwo", "Minior", "Miraidon", "Moltres", "Munkidori", "Naganadel", "Necrozma", "Nihilego", "Ogerpon", "Okidogi", "Palkia", "Pheromosa", "Phione", "Poipole", "Polteageist", "Porygon", "Porygon-Z", "Porygon2", "Raikou", "Rayquaza", "Regice", "Regidrago", "Regieleki", "Regigigas", "Regirock", "Registeel", "Reshiram", "Roaring Moon", "Rotom", "Sandy Shocks", "Scream Tail", "Shaymin", "Shedinja", "Silvally", "Sinistea", "Slither Wing", "Solgaleo", "Solrock", "Spectrier", "Stakataka", "Starmie", "Staryu", "Suicune", "Tandemaus", "Tapu Bulu", "Tapu Fini", "Tapu Koko", "Tapu Lele", "Terapagos", "Terrakion", "Ting-Lu", "Type: Null", "Unown", "Uxie", "Victini", "Virizion", "Volcanion", "Voltorb", "Walking Wake", "Wo-Chien", "Xerneas", "Xurkitree", "Yveltal", "Zacian", "Zamazenta", "Zapdos", "Zarude", "Zekrom", "Zeraora", "Zygarde"]

    def Battlers(speedsort = False):
        battlers = []
        for trainer in Trainers:
            battlers += trainer.GetLead(False)
        if (speedsort):
            battlers.sort(key=(lambda entry : (-entry.GetStat(Stats.Speed, triggerAbilities=False))))
        return battlers

    def IsCustomMove(move):
        if (not isinstance(move, str)):
            move = move.Name
        return move in custommovesin

    def BattleSetup():
        for trainer in Trainers:
            trainer.ResetFaintedPokemonCount()
            for mon in trainer.GetTeam():
                mon.Owner = trainer
                mon.TrainerType = trainer.GetType()
                mon.ItemHistory = [("Started", mon.GetItem(), 0)]
                mon.TimesHit = 0
                mon.CritsLanded = 0
                mon.ResetFaintedTurn()
                if (IsAfter(10, 5, 2004) or (IsDate(9, 5, 2004) and timeOfDay not in ["Noon", "Morning", "Afternoon"])):
                    mon.Trained = []
                    for move in custommovesin:
                        if (move in mon.GetMoveNames()):
                            mon.Trained.append(move)
                mon.ResetCaught()

    def PlayerBattlers():
        players = []
        for mon in Battlers():
            if (mon.GetTrainerType() == TrainerType.Player):
                players.append(mon)
        return players

    def PlayerPokemon():
        for trainer in Trainers:
            if (trainer.GetType() == TrainerType.Player):
                return trainer.GetTeam()
        return []

    def EnemyPokemon():
        enemies = []
        for trainer in Trainers:
            if (trainer.GetType() == TrainerType.Enemy):
                enemies += trainer.GetTeam()
        return enemies
    
    def EnemyUnfainteds():
        unfainteds = []
        for trainer in Trainers:
            if (trainer.GetType() == TrainerType.Enemy):
                unfainteds += trainer.GetUnfaintedTeam()
        return unfainteds

    def FriendlyPokemon():
        enemies = []
        for trainer in Trainers:
            if (trainer.GetType() != TrainerType.Enemy):
                enemies += trainer.GetTeam()
        return enemies

    def FriendlyUnfainteds():
        unfainteds = []
        for trainer in Trainers:
            if (trainer.GetType() != TrainerType.Enemy):
                unfainteds += trainer.GetUnfaintedTeam()
        return unfainteds

    def AllyBattlers():
        allies = []
        for mon in Battlers():
            if (mon.GetTrainerType() == TrainerType.Ally):
                allies.append(mon)
        return allies

    def weighted_random_sort(targets):
        items = list(targets.items())
        
        # Transform weights to be non-negative and increase their effect by multiplying by 2
        min_weight = min(weight for _, weight in items)
        if min_weight < 0:
            items = [(key, (weight - min_weight) * 2) for key, weight in items]
        else:
            items = [(key, weight * 2) for key, weight in items]
        
        sorted_keys = []
        
        while items:
            # Calculate the cumulative weights
            total_weight = sum(weight for _, weight in items)
            if total_weight == 0:
                sorted_keys.extend(key for key, _ in items)  # If all remaining weights are zero, append the remaining keys
                break

            cumulative_weights = []
            current_weight = 0
            for _, weight in items:
                current_weight += weight
                cumulative_weights.append(current_weight / total_weight)
            
            # Choose a random number and find the corresponding item
            rand = random.random()
            for i, cum_weight in enumerate(cumulative_weights):
                if rand < cum_weight:
                    chosen_item = items.pop(i)
                    sorted_keys.append(chosen_item[0])
                    break
        
        return sorted_keys

    def RankTargets(mon):
        targets = {}
        unalteredtargets = {}
        possiblemoves = GetValidMoves(mon)
        for move in possiblemoves:
            movename = move.Name
            subtargets = GetTargets(mon, GetMoveRange(move), GetMoveRange(move) in [Range.Adjacent, Range.Any] and movename not in ["Heal Pulse", "Helping Hand"])
            for target in subtargets:
                perceivedtarget = target if not target.HasStatus("illusion") else target.GetStatusCount("illusion")

                targets[(target, move)] = ((
                    (10 if move.Category != "Status" else 0)#prioritize damaging move 
                    + (5 * mon.GetStatChanges(Stats.Attack) if move.Category == "Physical" and mon.GetStatChanges(Stats.Attack) > 0 else 0)#prioritize move that's been buffed
                    + (5 * mon.GetStatChanges(Stats.SpecialAttack) if move.Category == "Special" and mon.GetStatChanges(Stats.SpecialAttack) > 0 else 0)#prioritize move without debuffs
                    + (5 if mon.HasType(move.Type) and move.Category != "Status" else 0)#prioritize move with STAB
                    + (20 if move.Category == "Status" and not target.HasNormalStatus() and not target.HasStatus("confused") and not FriendlyStatChanges() - EnemyStatChanges() < 0 else 0)#prioritize status move unless foe has nonvolatile status condition or a negative stat change, or you have a positive stat change
                    + (5 * (len(subtargets) - 1) if GetMoveRange(move) in [Range.AllAdjacent, Range.AllAdjacentFoes, Range.AllFoes, Range.AllAllies, Range.All] else 0))# Priorititize multi-target moves if they can hit multiple targets
                    * (pow(GetTypeBonus(move.Name, move.Type, perceivedtarget, mon), 2) if move.Category != "Status" else 1.0))#_heavily_ prioritize damaging moves with higher effectiveness
                unalteredtargets[(target, move)] = targets[(target, move)]

                if ((movename in ["Recover", "Milk Drink", "Moonlight", "Morning Sun", "Synthesis", "Slack Off", "Shore Up", "Roost", "Soft-Boiled", "Life Dew"] and mon.GetHealthPercentage() >= 0.5)
                    or (movename == "Tailwind" and EffectOnOwnField(mon, "tailwind"))
                    or (movename in ["Rain Dance", "Healing Spring"] and WeatherIs("rainy"))
                    or (movename == "Sunny Day" and WeatherIs("sunny"))
                    or (movename == "Sandstorm" and WeatherIs("sandstorm"))
                    or (movename == "Hail" and WeatherIs("hailing"))
                    or (movename == "Snowscape" and WeatherIs("snowy"))
                    or (movename == "Taunt" and target.HasStatus("taunted"))
                    or (movename == "Leech Seed" and target.HasStatus("seeded"))
                    or (movename == "Spikes" and EffectCountOnOpponentField(mon, "spikes") >= 3)
                    or (movename == "Toxic Spikes" and EffectCountOnOpponentField(mon, "toxic spikes") >= 2)
                    or (movename == "Stealth Rock" and EffectOnOpponentField(mon, "stealthy rocks"))
                    or (movename == "Aqua Ring" and mon.HasStatus("aqua ring"))
                    or (movename == "Perish Song" and target.HasStatus("perishing"))
                    or (movename == "Reflect" and (EffectOnOwnField(mon, "reflect") or EffectOnOwnField(mon, "aurora veil")))
                    or (movename == "Light Screen" and (EffectOnOwnField(mon, "light screen") or EffectOnOwnField(mon, "aurora veil")))
                    or (movename == "Safeguard" and EffectOnOwnField(mon, "safeguard"))
                    or (movename == "Aurora Veil" and (EffectOnOwnField(mon, "aurora veil") or not (WeatherIs("hailing") or WeatherIs("snowy"))))
                    or (movename == "Heal Pulse" and (target not in GetBattlers(mon) or target.GetHealthPercentage() >= 0.67))
                    or (movename == "Rage" and mon.HasStatus("raging"))
                    or (BattlefieldExists(movename))
                    or (movename == "Shed Tail" and mon.GetHealthPercentage() < 0.5 and len(mon.GetTrainer().GetUnfaintedTeam()) < 2)
                    or (movename == "Clear Mind" and (not (target.HasNormalStatus() or target.HasStatus("confused") or target.HasStatus("perishing") or mon.GetTotalStatChanges() < -1) or target not in GetBattlers(mon)))
                    or (movename == "Dream Eater" and not target.HasStatus("asleep"))
                    or (movename == "Wish" and (mon.GetHealthPercentage() == 1.0 or EffectOnOwnField(mon, "wishing star")))
                    or (movename == "Healing Wish" and (not (mon.GetHealthPercentage() < 0.75 or mon.HasNormalStatus()) or len(mon.GetTrainer().GetUnfaintedTeam()) <= len(GetBattlers(mon))))
                    or (movename in ["Attract"] and (mon.GetGender() == target.GetGender() or mon.GetGender() == Genders.Unknown or target.GetGender() == Genders.Unknown))
                    or (movename in ["Attract", "Ardent Gaze"] and (target.HasStatus("infatuated") or perceivedtarget.HasAbility("Oblivious", False)))
                    or (movename in ["Mean Look", "Block", "Spider Web"] and mon.HasStatus("perishing"))
                    or (movename in ["Protect", "Detect", "Wide Guard", "Mat Block", "Enshroud", "Crafty Shield", "Spike Shield", "Splinter Shield"] and mon.GetStatusCount(".protections") > 0)
                    or (movename in ["Whirlwind", "Roar"] and target.GetTotalStatChanges() <= 1 and (EffectCountOnOpponentField(mon, "spikes") + EffectCountOnOpponentField(mon, "toxic spikes") + EffectCountOnOpponentField(mon, "stealthy rocks") == 0))
                    or (movename in ["Ingrain", "Bark Up"] and mon.HasStatus("ingrained"))
                    or (movename in ["Disable", "Disabling Poke"] and (target.HasStatus("disabled") or Turn - target.GetTurnSwitchedIn() < 1))
                    or (movename in ["Will-O-Wisp", "Steady Flame"] and (target.HasNormalStatus() or perceivedtarget.HasType("Fire") or perceivedtarget.HasAbility("Flash Fire", False) or perceivedtarget.HasAbility("Thermal Exchange", False)))
                    or (movename in ["Toxic", "Poison Gas"] and (target.HasNormalStatus() or perceivedtarget.HasType("Poison") or perceivedtarget.HasAbility("Immunity", False)))
                    or (movename in ["Thunder Wave"] and (perceivedtarget.HasType("Ground")))
                    or (movename in ["Thunder Wave", "Glare", "Stun Spore"] and (target.HasNormalStatus() or perceivedtarget.HasType("Electric") or perceivedtarget.HasAbility("Limber", False)))
                    or (movename in ["Confuse Ray", "Sweet Kiss", "Supersonic"] and target.HasStatus("confused"))
                    or (movename in ["Legacy", "Fake Out", "First Impression"] and not (Turn == 1 or (Turn - mon.GetTurnSwitchedIn() <= 1)))
                    or (movename in ["Sleep Powder", "Poison Powder", "Spore", "Stun Spore"] and (perceivedtarget.HasType("Grass") or target.HasNormalStatus() or perceivedtarget.HasAbility("Overcoat")))
                    or (move.Category == "Status" and AbilityOnOpponentField(mon, "Magic Bounce", False))
                    or ((movename in target.suspiciousmoves) if hasattr(target, "suspiciousmoves") else False)
                    or (movename == "Fling" and CalculateFling(mon) < 30)):
                    del targets[(target, move)]
                    unalteredtargets[(target, move)] -= 30

                elif ((movename in ["Recover", "Milk Drink", "Moonlight", "Morning Sun", "Slack Off", "Shore Up", "Roost", "Soft-Boiled", "Life Dew", "Synthesis"] and mon.GetHealthPercentage() < 0.5)
                    or (movename == "Tailwind" and not EffectOnOwnField(mon, "tailwind"))
                    or (movename in ["Rain Dance", "Healing Spring"] and not WeatherIs("rainy"))
                    or (movename == "Sunny Day" and not WeatherIs("sunny"))
                    or (movename == "Sandstorm" and not WeatherIs("sandstorm"))
                    or (movename == "Hail" and not WeatherIs("hailing"))
                    or (movename == "Snowscape" and not WeatherIs("snowy"))
                    or (movename == "Taunt" and not target.HasStatus("taunted"))
                    or (movename == "Leech Seed" and target.HasStatus("seeded"))
                    or (movename == "Hex" and target.HasNormalStatus() and not perceivedtarget.HasType("Normal"))
                    or (movename == "Spikes" and EffectCountOnOpponentField(mon, "spikes") < 3)
                    or (movename == "Toxic Spikes" and EffectCountOnOpponentField(mon, "toxic spikes") < 2)
                    or (movename == "Stealth Rock" and not EffectOnOpponentField(mon, "stealthy rocks"))
                    or (movename == "Perish Song" and not CanSwitch(target, False))
                    or (movename == "Reflect" and not EffectOnOwnField(mon, "reflect") and not EffectOnOwnField(mon, "aurora veil"))
                    or (movename == "Light Screen" and not EffectOnOwnField(mon, "light screen") and not EffectOnOwnField(mon, "aurora veil"))
                    or (movename == "Safeguard" and not EffectOnOwnField(mon, "safeguard"))
                    or (movename == "Aurora Veil" and not EffectOnOwnField(mon, "aurora veil") and (WeatherIs("snowy") or WeatherIs("hailing")))
                    or (movename == "Heal Pulse" and target in GetBattlers(mon) and target.GetHealthPercentage() >= 0.67)
                    or (movename == "Rage" and not mon.HasStatus("raging") and not perceivedtarget.HasType("Ghost"))
                    or (not BattlefieldExists(movename))
                    or (movename == "Shed Tail" and mon.GetHealthPercentage() >= 0.5 and len(mon.GetTrainer().GetUnfaintedTeam()) > 1)
                    or (movename == "Clear Mind" and (target.HasNormalStatus() or target.HasStatus("confused") or target.HasStatus("perishing") or mon.GetTotalStatChanges() < -1) and target in GetBattlers(mon))
                    or (movename == "Wish" and (mon.GetHealthPercentage() < 1.0 and not EffectOnOwnField(mon, "wishing star")))
                    or (movename == "Healing Wish" and ((mon.GetHealthPercentage() < 0.75 or mon.HasNormalStatus()) and len(mon.GetTrainer().GetUnfaintedTeam()) > len(GetBattlers(mon))))
                    or (movename in ["Attract"] and (not target.HasStatus("infatuated") and mon.GetGender() != target.GetGender() and mon.GetGender() != Genders.Unknown and target.GetGender() != Genders.Unknown and not perceivedtarget.HasAbility("Oblivious", False)))
                    or (movename in ["Attract", "Ardent Gaze"] and not target.HasStatus("infatuated") and not perceivedtarget.HasAbility("Oblivious", False))
                    or (movename in ["Defog", "Tidy Up", "Mortal Spin", "Rapid Spin"] and (EffectOnOwnField(mon, "spikes") or EffectOnOwnField(mon, "toxic spikes") or EffectOnOwnField(mon, "stealthy rocks")))
                    or (movename in ["Protect", "Detect", "Wide Guard", "Mat Block", "Enshroud", "Crafty Shield", "Spike Shield", "Splinter Shield"] and mon.GetStatusCount(".protections") == 0)
                    or (movename in ["Whirlwind", "Roar"] and (target.GetTotalStatChanges() > 1 or (EffectCountOnOpponentField(mon, "spikes") + EffectCountOnOpponentField(mon, "toxic spikes") + EffectCountOnOpponentField(mon, "stealthy rocks") > 0)))
                    or (movename in ["Ingrain", "Bark Up"] and not mon.HasStatus("ingrained"))
                    or (movename in ["Will-O-Wisp", "Steady Flame"] and not (target.HasNormalStatus() or perceivedtarget.HasType("Fire") or perceivedtarget.HasAbility("Flash Fire", False) or perceivedtarget.HasAbility("Thermal Exchange", False)))
                    or (movename in ["Toxic", "Poison Gas"] and not (target.HasNormalStatus() or perceivedtarget.HasType("Poison") or perceivedtarget.HasAbility("Immunity", False)))
                    or (movename in ["Thunder Wave", "Glare", "Stun Spore"] and not (target.HasNormalStatus() or perceivedtarget.HasType("Electric") or perceivedtarget.HasAbility("Limber", False)))
                    or (movename in ["Thunder Wave"] and not (perceivedtarget.HasType("Ground")))
                    or (movename in ["Confuse Ray", "Sweet Kiss", "Supersonic"] and not target.HasStatus("confused"))
                    or (movename in ["Legacy", "Fake Out", "First Impression"] and (Turn == 1 or (Turn - mon.GetTurnSwitchedIn() <= 1)))
                    or (movename in ["Sleep Powder", "Poison Powder", "Spore", "Stun Spore"] and not (perceivedtarget.HasType("Grass") or target.HasNormalStatus() or perceivedtarget.HasAbility("Overcoat", False)))
                    or (movename == "Fling" and (CalculateFling(mon) > 60 or mon.GetItem() in [Item.KingsRock, Item.RazorFang, Item.PoisonBarb]))):
                    targets[(target, move)] += 20
                    unalteredtargets[(target, move)] += 20

                #if ((target, move) not in targets.keys()):
                #    print(mon.GetNickname() + " will not use " + move.Name + " on " + target.GetNickname())
                #else:
                #    print(mon.GetNickname() + " uses " + move.Name + " on " + target.GetNickname() + " for " + str(targets[(target, move)]) + " points")
            
        #print("\n\n\n")

        if (len(targets) < 1):
            return weighted_random_sort(unalteredtargets)
        else:
            return weighted_random_sort(targets)

    def FriendlyStatChanges():
        totalval = 0
        for mon in FriendlyBattlers():
            totalval += mon.GetTotalStatChanges()
        return totalval

    def EnemyStatChanges():
        totalval = 0
        for mon in EnemyBattlers():
            totalval += mon.GetTotalStatChanges()
        return totalval

    def GetValidMoves(mon):
        validmoves = []
        for enemymove in mon.GetMoves():
            if (MoveValid(mon, enemymove)):
                validmoves.append(enemymove)
        if (len(validmoves) == 0):
            validmoves = [struggle]
        return validmoves

    def FriendlyBattlers():
        players = []
        for mon in Battlers():
            if (mon.GetTrainerType() != TrainerType.Enemy):
                players.append(mon)
        return players

    def EnemyBattlers():
        enemies = []
        for mon in Battlers():
            if (mon.GetTrainerType() == TrainerType.Enemy):
                enemies.append(mon)
        return enemies

    def EnemySpecies():
        enemies = []
        for enemy in EnemyBattlers():
            enemies.append(enemy.GetId())
        return enemies

    def FriendlyTrainers():
        friends = []
        for trainer in Trainers:
            if (trainer.GetType() != TrainerType.Enemy):
                friends.append(trainer)
        return friends

    def EnemyTrainers(omitdefeated=False):
        enemies = []
        for trainer in Trainers:
            if (trainer.GetType() == TrainerType.Enemy and (not omitdefeated or len(trainer.GetUnfaintedTeam()) > 0)):
                enemies.append(trainer)
        return enemies

    def GetGrid():
        pkmngrid = [[], []]
        for trainer in Trainers:
            if (trainer.GetType() == TrainerType.Enemy):
                pkmngrid[1] += trainer.GetLead(False)
            else:
                pkmngrid[0] += trainer.GetLead(False)
        return pkmngrid

    def GetTargets(mon, range = Range.Adjacent, forceenemy = False):
        xcoord = -1
        ycoord = -1
        for i, sublist in enumerate(GetGrid()):
            for j, othermon in enumerate(GetGrid()[i]):
                if (mon == othermon):
                    xcoord = i
                    ycoord = j
        adjacents = []

        for i, sublist in enumerate(GetGrid()):
            for j, othermon in enumerate(GetGrid()[i]):
                if (othermon != None):
                    mygrid = []
                    othergrid = []
                    if (mon in GetGrid()[0]):
                        mygrid = GetGrid()[0]
                        othergrid = GetGrid()[1]
                    elif (mon in GetGrid()[1]):
                        mygrid = GetGrid()[1]
                        othergrid = GetGrid()[0]
                    verticality = j
                    isself = othermon == mon
                    
                    overwriteadjacency = 0
                    if (len(mygrid) + len(othergrid) == 5):
                        if (len(mygrid) == 2 and mygrid.index(mon) == 1 and othermon not in mygrid):
                            j -= 1
                        elif (len(mygrid) == 3 and mygrid.index(mon) != 1 and othermon not in mygrid):
                            if (mygrid.index(mon) == 0 and othergrid.index(othermon) == 1):
                                j += 1
                            elif (mygrid.index(mon) == 2 and othergrid.index(othermon) == 0):
                                j -= 1
                    elif (len(GetGrid()[0]) + len(GetGrid()[1]) <= 4 and mon in mygrid and othermon in othergrid):
                        overwriteadjacency = -99

                    isadjacent = overwriteadjacency + abs(j - ycoord) <= 1 and not isself
                    isenemy = (mon.GetTrainerType() == TrainerType.Enemy and othermon.GetTrainerType() != TrainerType.Enemy) or (mon.GetTrainerType() != TrainerType.Enemy and othermon.GetTrainerType() == TrainerType.Enemy)

                    # Flintlock's special code to try to account for larger battles.
                    # This should support as many per side as you wish.
                    # I've tested it with a side having 15, worked perfectly.
                    # Code is not ever used as long as a side does not have more than 3.
                    # Granted, logic would likely still work fine if you wanted to port it to do so.
                    # This uses some math to allow for targeting, based on step_size, and relative location of
                    # the opponents, assuming that the side with less are centered on the battlefield, in position.
                    # Another potential use: Horde battles.
                    if isenemy and (len(mygrid) > 3 or len(othergrid) > 3):

                        if len(mygrid) < len(othergrid):
                            step_size = (len(othergrid) - 1) / (len(mygrid) + 1)
                            user_relative_location = step_size * (mygrid.index(mon) + 1)
                            isadjacent = abs(othergrid.index(othermon) - user_relative_location) <= step_size + 0.01
                        elif len(mygrid) == len(othergrid):
                            isadjacent = abs(othergrid.index(othermon) - mygrid.index(mon)) <= 1.0
                        elif len(mygrid) > len(othergrid):
                            step_size = (len(mygrid) - 1) / (len(othergrid) + 1)
                            enemy_relative_location = step_size * (othergrid.index(othermon) + 1)
                            isadjacent = abs(enemy_relative_location - mygrid.index(mon)) <= step_size + 0.01

                    if ((range == Range.Adjacent and isadjacent and (not forceenemy or isenemy)
                        or range == Range.AdjacentFoe and isadjacent and isenemy
                        or range == Range.Any and not isself and (not forceenemy or isenemy)
                        or range == Range.AnyOrSelf
                        or range == Range.AdjacentAllyOrSelf and (isadjacent or isself) and not isenemy
                        or range == Range.AllAdjacentFoes and isadjacent and isenemy
                        or range == Range.AllAdjacent and isadjacent
                        or range == Range.AllAllies and not isself and not isenemy
                        or range == Range.AllFoes and isenemy
                        or range == Range.All
                        or range == Range.AdjacentAlly and isadjacent and not isenemy
                        or range == Range.Self and isself
                        or range == Range.AllAlliesAndSelf and not isenemy)
                        or range == Range.AnyAlly and not isenemy):
                            adjacents.append(othermon)
                
        return adjacents

    def GetRandomAdjacentFoe(mon):
        return RandomChoice(GetTargets(mon))

    def GetMoveRange(move):
        ranges = {
            Range.AdjacentFoe : ["Doodle","G-Max Befuddle","G-Max Cannonade","G-Max Centiferno","G-Max Chi Strike","G-Max Cuddle","G-Max Depletion","G-Max Drum Solo","G-Max Finale","G-Max Fireball","G-Max Foam Burst","G-Max Gold Rush","G-Max Gravitas","G-Max Hydrosnipe","G-Max Malodor","G-Max Meltdown","G-Max One Blow","G-Max Rapid Flow","G-Max Replenish","G-Max Resonance","G-Max Sandblast","G-Max Smite","G-Max Steelsurge","G-Max Stonesurge","G-Max Stun Shock","G-Max Sweetness","G-Max Tartness","G-Max Terror","G-Max Vine Lash","G-Max Volcalith","G-Max Volt Crash","G-Max Wildfire","G-Max Wind Rage","Max Airstream","Max Darkness","Max Flare","Max Flutterby","Max Geyser","Max Hailstorm","Max Knuckle","Max Lightning","Max Mindstorm","Max Ooze","Max Overgrowth","Max Phantasm","Max Quake","Max Rockfall","Max Starfall","Max Steelspike","Max Strike","Max Wyrmwind","Me First"],
            Range.Any : ["Struggle","Acrobatics","Aerial Ace","Aeroblast","Air Slash","Aura Sphere","Bounce","Brave Bird","Chatter","Dark Pulse","Dragon Pulse","Drill Peck","Fly","Flying Press","Gust","Heal Pulse","Hurricane","Oblivion Wing","Peck","Pluck","Shadow Blast","Shadow Blitz","Shadow Bolt","Shadow Break","Shadow Chill","Shadow End","Shadow Fire","Shadow Rush","Sky Attack","Sky Drop","Water Pulse","Wing Attack","Fling"],
            Range.AnyOrSelf : ["Clear Mind", "Metallize"],
            Range.AdjacentAllyOrSelf : ["Acupressure"], 
            Range.AllAdjacentFoes : ["Breaking Swipe", "Acid","Air Cutter","Astral Barrage","Bleakwind Storm","Blizzard","Bouncy Bubble","Breaking Swipe","Bubble","Burning Jealousy","Captivate","Clanging Scales","Clangorous Soulblaze","Core Enforcer","Cotton Spore","Dark Void","Dazzling Gleam","Diamond Storm","Disarming Voice","Dragon Energy","Electroweb","Eruption","Fiery Wrath","G-Max Snooze","Glacial Lance","Glaciate","Growl","Heal Block","Heat Wave","Hyper Voice","Icy Wind","Incinerate","Land's Wrath","Leer","Make It Rain","Mortal Spin","Muddy Water","Origin Pulse","Overdrive","Poison Gas","Powder Snow","Precipice Blades","Razor Leaf","Razor Wind","Relic Song","Rock Slide","Sandsear Storm","Shell Trap","Snarl","Splishy Splash","Springtide Storm","String Shot","Struggle Bug","Sweet Scent","Swift","Tail Whip","Thousand Arrows","Thousand Waves","Twister","Venom Drench","Water Spout","Wildbolt Storm"], 
            Range.AllAdjacent : ["Boomburst","Brutal Swing","Bulldoze","Corrosive Gas","Discharge","Earthquake","Explosion","Lava Plume","Magnitude","Mind Blown","Misty Explosion","Parabolic Charge","Petal Blizzard","Searing Shot","Self-Destruct","Sludge Wave","Sparkling Aria","Surf","Synchronoise","Teeter Dance"], 
            Range.AllAllies : ["Coaching"],
            Range.AllFoes : ["Shadow Down","Shadow Hold","Shadow Mist","Shadow Panic","Shadow Rave","Shadow Storm","Shadow Wave","Spikes","Stealth Rock","Sticky Web","Toxic Spikes"],
            Range.All : ["Stone Cold Stunner", "Healing Spring", "Simple World", "Burial Ground", "Chilly Reception","Court Change","Electric Terrain","Fairy Lock","Flower Shield","Grassy Terrain","Gravity","Hail","Haze","Ion Deluge","Magic Room","Misty Terrain","Mud Sport","Perish Song","Psychic Terrain","Rain Dance","Rototiller","Sandstorm","Shadow Half","Shadow Shed","Shadow Sky","Snowscape","Sunny Day","Teatime","Trick Room","Water Sport","Wonder Room"],
            Range.AdjacentAlly : ["Aromatic Mist","Helping Hand","Hold Hands"],
            Range.Self : ["nothing", "Splinter Shield", "Buffet", "Bark Up", "Deathless", "Wing It", "Energize", "Chrysalize", "Enshroud", "Acid Armor","Agility","Ally Switch","Amnesia","Aqua Ring","Assist","Autotomize","Baneful Bunker","Barrier","Baton Pass","Belly Drum","Bide","Bulk Up","Calm Mind","Camouflage","Celebrate","Charge","Clangorous Soul","Coil","Comeuppance","Conversion","Copycat","Cosmic Power","Cotton Guard","Counter","Curse","Defend Order","Defense Curl","Destiny Bond","Detect","Double Team","Dragon Dance","Endure","Extreme Evoboost","Fillet Away","Focus Energy","Follow Me","Geomancy","Growth","Grudge","Harden","Heal Order","Healing Wish","Helping Hand","Hone Claws","Howl","Imprison","Ingrain","Iron Defense","King's Shield","Laser Focus","Lunar Dance","Magic Coat","Magnet Rise","Max Guard","Meditate","Metal Burst","Metronome","Milk Drink","Minimize","Mirror Coat","Moonlight","Morning Sun","Nasty Plot","Nature Power","No Retreat","Obstruct","Outrage","Petal Dance","Power Shift","Power Trick","Protect","Quiver Dance","Rage Powder","Raging Fury","Recover","Recycle","Refresh","Rest","Revival Blessing","Rock Polish","Roost","Sharpen","Shed Tail","Shell Smash","Shelter","Shift Gear","Shore Up","Silk Trap","Slack Off","Sleep Talk","Snatch","Soft-Boiled","Spiky Shield","Splash","Stockpile","Struggle","Stuff Cheeks","Substitute","Swallow","Swords Dance","Synthesis","Tail Glow","Take Heart","Teleport","Thrash","Tidy Up","Uproar","Victory Dance","Wish","Withdraw","Work Up"],
            Range.AllAlliesAndSelf : ["Aromatherapy","Aurora Veil","Crafty Shield","Gear Up","Happy Hour","Heal Bell","Howl","Jungle Healing","Life Dew","Light Screen","Lucky Chant","Lunar Blessing","Magnetic Flux","Mat Block","Mist","Quick Guard","Reflect","Safeguard","Tailwind","Wide Guard"],
            Range.AnyAlly : []
        }

        for key in ranges.keys():
            if move.Name in ranges[key]:
                return key
        return 0

    def GetTrainers(monlist):
        owners = []
        for mon in monlist:
            owners.append(mon.GetTrainer())
        return owners

    def GetSlots(monlist):
        slots = []
        for mon in monlist:
            slots.append(mon.GetTrainer().GetTeam().index(mon))
        return slots

    def HasFaintedLead(trainer):
        hasFaintedLead = False
        for mon in trainer.GetTeam()[:trainer.GetNumber()]:
            if (mon.GetHealth() <= 0):
                hasFaintedLead = True
        return hasFaintedLead

    def AreAllied(mon1, mon2):
        return ((mon1.GetTrainerType() == mon2.GetTrainerType()) 
            or (mon1.GetTrainerType() == TrainerType.Ally and mon2.GetTrainerType() == TrainerType.Player) 
            or (mon1.GetTrainerType() == TrainerType.Player and mon2.GetTrainerType() == TrainerType.Ally))

    def IsSnatchable(movename):
        return movename in ["Acid Armor", "Agility", "Amnesia", "Aqua Ring", "Aromatherapy", "Aurora Veil", "Autotomize", "Barrier", "Belly Drum", "Bulk Up", "Calm Mind", "Camouflage", "Charge", "Coil", "Conversion", "Cosmic Power", "Cotton Guard", "Defend Order", "Defense Curl", "Double Team", "Dragon Dance", "Focus Energy", "Gear Up", "Growth", "Harden", "Heal Bell", "Heal Order", "Healing Wish", "Hone Claws", "Howl", "Imprison", "Ingrain", "Iron Defense", "Laser Focus", "Light Screen", "Lucky Chant", "Lunar Dance", "Magnet Rise", "Magnetic Flux", "Mat Block", "Meditate", "Milk Drink", "Minimize", "Mist", "Moonlight", "Morning Sun", "Nasty Plot", "Power Trick", "Quick Guard", "Quiver Dance", "Recover", "Recycle", "Reflect", "Refresh", "Rest", "Rock Polish", "Roost", "Safeguard", "Sharpen", "Shell Smash", "Shift Gear", "Shore Up", "Slack Off", "Soft-Boiled", "Stockpile", "Substitute", "Swallow", "Swords Dance", "Synthesis", "Tail Glow", "Tailwind", "Wide Guard", "Wish", "Withdraw", "Work Up"]

    def AssistCanCall(movename):
        return movename not in ["Stone Cold Stunner", "Assist", "Baneful Bunker", "Beak Blast", "Belch", "Bestow", "Celebrate", "Chatter", "Circle Throw", "Copycat", "Counter", "Covet", "Destiny Bond", "Detect", "Dragon Tail", "Endure", "Feint", "Focus Punch", "Follow Me", "Helping Hand", "Hold Hands", "King's Shield", "Mat Block", "Me First", "Metronome", "Mimic", "Mirror Coat", "Mirror Move", "Phantom Force", "Protect", "Rage Powder", "Shell Trap", "Sketch", "Sleep Talk", "Snatch", "Spiky Shield", "Spotlight", "Struggle", "Switcheroo", "Thief", "Transform", "Trick", "Kasa's Transform"]

    def GetCalculatedMovePower(move):
        movename = move if isinstance(move, str) else move.Name
        if (movename in movepowerdex.keys()):
            return max(40, movepowerdex[movename])
        else:
            return 80

    def GetMovePower(move):
        if (move.Name in ["Eruption", "Water Spout", "Fissure", "Guillotine", "Horn Drill", "Sheer Cold"]):
            return 150
        elif (move.Name in ["Counter", "Metal Burst", "Mirror Coat"]):
            return 120
        elif (move.Name in ["Crush Grip", "Dragon Rage", "Electro Ball", "Endeavor", "Final Gambit", "Flail", "Frustration", "Grass Knot", "Guardian of Alola", "Gyro Ball", "Heat Crash", "Heavy Slam", "Hidden Power", "Low Kick", "Natural Gift", "Nature's Madness", "Night Shade", "Present", "Psywave", "Punishment", "Return", "Reversal", "Seismic Toss", "Sonic Boom", "Spit Up", "Super Fang", "Trump Card", "Wring Out"]):
            return 80
        elif (move.Name in ["Stored Power", "Power Trip"]):
            return 20
        else:
            return (0 if isinstance(move.Power, str) else move.Power)

    def GetFriendGuardCount(mon):
        count = 0
        for othermon in GetBattlers(mon):
            if (othermon != mon and othermon.HasAbility("Friend Guard")):
                count += 1
        return count

    def NaturalGiftData(berry):
        if (berry == 5): # Cheri Berry
            return ("Fire", 80)
        elif (berry == 6): # Chesto Berry
            return ("Water", 80)
        elif (berry == 7): # Pecha Berry
            return ("Electric", 80)
        elif (berry == 8): # Rawst Berry
            return ("Grass", 80)
        elif (berry == 250): # Aspear Berry
            return ("Ice", 80)
        elif (berry == "Leppa Berry"):
            return ("Fighting", 80)
        elif (berry == 9): # Oran Berry
            return ("Poison", 80)
        elif (berry == "Persim Berry"):
            return ("Ground", 80)
        elif (berry == 251): # Lum Berry
            return ("Flying", 80)
        elif (berry == 10): # Sitrus Berry
            return ("Psychic", 80)
        elif (berry == "Figy Berry"):
            return ("Bug", 80)
        elif (berry == "Wiki Berry"):
            return ("Rock", 80)
        elif (berry == "Mago Berry"):
            return ("Ghost", 80)
        elif (berry == "Aguav Berry"):
            return ("Dragon", 80)
        elif (berry == "Iapapa Berry"):
            return ("Dark", 80)
        elif (berry == "Razz Berry"):
            return ("Steel", 80)
        elif (berry == "Bluk Berry"):
            return ("Fire", 90)
        elif (berry == "Nanab Berry"):
            return ("Water", 90)
        elif (berry == "Wepear Berry"):
            return ("Electric", 90)
        elif (berry == "Pinap Berry"):
            return ("Grass", 90)
        elif (berry == "Pomeg Berry"):
            return ("Ice", 90)
        elif (berry == "Kelpsy Berry"):
            return ("Fighting", 90)
        elif (berry == "Qualot Berry"):
            return ("Poison", 90)
        elif (berry == "Hondew Berry"):
            return ("Ground", 90)
        elif (berry == "Grepa Berry"):
            return ("Flying", 90)
        elif (berry == "Tamato Berry"):
            return ("Psychic", 90)
        elif (berry == "Cornn Berry"):
            return ("Bug", 90)
        elif (berry == "Magost Berry"):
            return ("Rock", 90)
        elif (berry == "Rabuta Berry"):
            return ("Ghost", 90)
        elif (berry == "Nomel Berry"):
            return ("Dragon", 90)
        elif (berry == "Spelon Berry"):
            return ("Dark", 90)
        elif (berry == "Pamtre Berry"):
            return ("Steel", 90)
        elif (berry == "Watmel Berry"):
            return ("Fire", 100)
        elif (berry == "Durin Berry"):
            return ("Water", 100)
        elif (berry == "Belue Berry"):
            return ("Electric", 100)
        elif (berry == "Occa Berry"):
            return ("Fire", 80)
        elif (berry == "Passho Berry"):
            return ("Water", 80)
        elif (berry == "Wacan Berry"):
            return ("Electric", 80)
        elif (berry == "Rindo Berry"):
            return ("Grass", 80)
        elif (berry == "Yache Berry"):
            return ("Ice", 80)
        elif (berry == "Chople Berry"):
            return ("Fighting", 80)
        elif (berry == "Kebia Berry"):
            return ("Poison", 80)
        elif (berry == "Shuca Berry"):
            return ("Ground", 80)
        elif (berry == "Coba Berry"):
            return ("Flying", 80)
        elif (berry == "Payapa Berry"):
            return ("Psychic", 80)
        elif (berry == "Tanga Berry"):
            return ("Bug", 80)
        elif (berry == "Charti Berry"):
            return ("Rock", 80)
        elif (berry == "Kasib Berry"):
            return ("Ghost", 80)
        elif (berry == "Haban Berry"):
            return ("Dragon", 80)
        elif (berry == "Colbur Berry"):
            return ("Dark", 80)
        elif (berry == "Babiri Berry"):
            return ("Steel", 80)
        elif (berry == "Chilan Berry"):
            return ("Normal", 80)
        elif (berry == "Liechi Berry"):
            return ("Grass", 100)
        elif (berry == "Ganlon Berry"):
            return ("Ice", 100)
        elif (berry == "Salac Berry"):
            return ("Fighting", 100)
        elif (berry == "Petaya Berry"):
            return ("Poison", 100)
        elif (berry == "Apicot Berry"):
            return ("Ground", 100)
        elif (berry == "Lansat Berry"):
            return ("Flying", 100)
        elif (berry == "Starf Berry"):
            return ("Psychic", 100)
        elif (berry == "Enigma Berry"):
            return ("Bug", 100)
        elif (berry == "Micle Berry"):
            return ("Rock", 100)
        elif (berry == "Custap Berry"):
            return ("Ghost", 100)
        elif (berry == "Jaboca Berry"):
            return ("Dragon", 100)
        elif (berry == "Rowap Berry"):
            return ("Dark", 100)
        elif (berry == "Roseli Berry"):
            return ("Fairy", 80)
        elif (berry == "Kee Berry"):
            return ("Fairy", 100)
        elif (berry == "Maranga Berry"):
            return ("Dark", 100)

    def IsBerry(item):
        if isinstance(item, str):
            item = GetItemEntry(item)[0]
        return item != None and ItemHasTag(item, "berry")

    def ReactivateAbility(mon, fromTrace = False):
        returnmessage = ""

        for fvl in mon.GetForeverals():
            if (lookupforeveraldata(fvl, FVLMacros.FVLType) == ForeveralTypes.MoveBoost):
                for newmove in lookupforeveraldata(fvl, FVLMacros.FVLTypeData):
                    moveboosts.append(newmove)

        if ("Hail" in moveboosts and mon.Moves[0].Name == "Hail" and mon.Moves[0].PP >= 3):
            mon.Moves[0].PP -= 3
            returnmessage += mon.GetNickname() + "'s wishes coalesced! The sky manifests pounding hail! " + ApplyWeather("hailing", 5, mon)
        elif ("Sunny Day" in moveboosts and mon.Moves[0].Name == "Sunny Day" and mon.Moves[0].PP >= 3):
            mon.Moves[0].PP -= 3
            returnmessage += mon.GetNickname() + "'s wishes coalesced! The sky manifests blazing sun! " + ApplyWeather("sunny", 5, mon)
        elif ("Rain Dance" in moveboosts and mon.Moves[0].Name == "Rain Dance" and mon.Moves[0].PP >= 3):
            mon.Moves[0].PP -= 3
            returnmessage += mon.GetNickname() + "'s wishes coalesced! The sky manifests pouring rain! " + ApplyWeather("rainy", 5, mon)
        elif ("Snowcape" in moveboosts and mon.Moves[0].Name == "Snowscape" and mon.Moves[0].PP >= 3):
            mon.Moves[0].PP -= 3
            returnmessage += mon.GetNickname() + "'s wishes coalesced! The sky manifests a blanket of sleet! " + ApplyWeather("snowy", 5, mon)
        elif ("Bug Bite" in moveboosts and mon.Moves[0].Name == "Bug Bite" and mon.GetItem() in treatboosts):
            pokemontype = treatboosts[mon.GetItem()]
            mon.ApplyStatus("satiated", pokemontype)
            returnmessage += mon.GetNickname() + "'s wishes coalesced! " + mon.GetNickname() + " chowed down on their " + mon.GetItem() + " and is now " + pokemontype + "-type!"

        for ability in mon.GetAbilities():
            if (ability not in ["Intimidate", "Anticipation", "Download", "Drizzle", "Drought", "Snow Warning", "Sand Stream", "Forewarn", "Frisk", "Illusion", "Imposter", "Intimidate", "Schooling", "Shields Down", "Screen Cleaner", "Trace", "Hospitality", "Supreme Overlord", "Grassy Surge", "Misty Surge", "Electric Surge", "Psychic Surge"]):
                continue

            if (not fromTrace):
                if (mon.HasAbility("Trace") and len(GetTargets(mon, Range.AdjacentFoe)) != 0):
                    tracedmon = random.choice(GetTargets(mon, Range.AdjacentFoe))
                    if (not IsSpecialAbility(tracedmon.GetAbility())):
                        mon.ApplyStatus(".tracing", tracedmon.GetAbility())
                        returnmessage += "{} traced the ability {}!".format(mon.GetNickname(), tracedmon.GetAbility())

            if (mon.HasAbility("Grassy Surge")):
                returnmessage += ApplyBattlefieldEffects("Grassy Terrain", 5, False, mon)

            if (mon.HasAbility("Misty Surge")):
                returnmessage += ApplyBattlefieldEffects("Misty Terrain", 5, False, mon)

            if (mon.HasAbility("Psychic Surge")):
                returnmessage += ApplyBattlefieldEffects("Psychic Terrain", 5, False, mon)

            if (mon.HasAbility("Electric Surge")):
                returnmessage += ApplyBattlefieldEffects("Electric Terrain", 5, False, mon)

            if (mon.HasAbility("Supreme Overlord")):
                faintedmons = len(mon.GetTrainer().GetTeam()) - len(mon.GetTrainer().GetUnfaintedTeam())
                if (faintedmons > 0):
                    mon.ApplyStatus("reigning supreme", 1 + 0.1 * faintedmons)
                    returnmessage += mon.GetNickname() + " gained strength from the fallen!"
            
            if (mon.HasAbility("Intimidate")):
                for othermon in GetTargets(mon, Range.AllAdjacentFoes):
                    if (not (othermon.HasAbility("Own Tempo") or othermon.HasAbility("Oblivious") or othermon.HasAbility("Inner Focus") or othermon.HasAbility("Scrappy"))):
                        returnmessage += othermon.ChangeStats(Stats.Attack, -1, mon) + " "
                    if (othermon.HasAbility("Rattled")):
                        returnmessage += othermon.ChangeStats(Stats.Speed, 1, mon) + " "

            if (mon.HasAbility("Screen Cleaner")):
                removeeffects = ["light screen", "reflect", "aurora veil"]
                effectdel = []
                for cleareffect in EnemyEffects.keys():
                    if (cleareffect in removeeffects):
                        effectdel.append(cleareffect)
                for clearingeffect in effectdel:
                    del EnemyEffects[clearingeffect]
                if (len(effectdel) > 0):
                    returnmessage += "Wiped down the foe's screens! "
                effectdel = []
                for cleareffect in FriendlyEffects.keys():
                    if (cleareffect in removeeffects):
                        effectdel.append(cleareffect)
                for clearingeffect in effectdel:
                    del FriendlyEffects[clearingeffect]
                if (len(effectdel) > 0):
                    returnmessage += "Wiped down your own screens! "
            
            if (mon.HasAbility("Frisk")):
                for othermon in GetBattlers(mon, True):
                    if not othermon.HasItem(None):
                        returnmessage += "{} frisked the foe {} and found one {}! ".format(mon.GetNickname(), othermon.GetNickname(), othermon.GetItemName())

            if (mon.HasAbility("Anticipation")):
                for othermon in GetBattlers(mon, True):
                    for move in othermon.GetMoves():
                        typebonus = 1.0
                        for type in mon.GetTypes():                
                            typebonus *= GetEffectiveness(move.Type, type)
                            if (typebonus > 1 and "shuddered" not in returnmessage):
                                returnmessage += "{} shuddered!".format(mon.GetNickname())
            
            if (mon.HasAbility("Forewarn")):
                maxpower = 0
                movelist = []
                for othermon in GetBattlers(mon, True):
                    for move in othermon.GetMoves():
                        movepower = GetMovePower(move)
                        if (movepower > maxpower):
                            maxpower = movepower
                            movelist = [move.Name]
                        elif (movepower == maxpower):
                            movelist.append(move.Name)
                chosenmove = random.choice(movelist)
                returnmessage += "{} was forewarned of {}!".format(mon.GetNickname(), chosenmove)

            if (mon.HasAbility("Sand Stream")):
                returnmessage += ApplyWeather("sandstorm", 5, mon)
            elif (mon.HasAbility("Drizzle")):
                returnmessage += ApplyWeather("rainy", 5, mon)
            elif (mon.HasAbility("Drought")):
                returnmessage += ApplyWeather("sunny", 5, mon)
            elif (mon.HasAbility("Snow Warning")):
                returnmessage += ApplyWeather("snowy", 5, mon)

            if (mon.HasAbility("Hospitality")):
                for othermon in GetBattlers(mon, False):
                    if (othermon != mon and othermon.GetHealthPercentage() < 1):
                        othermon.AdjustHealth(othermon.GetStat(Stats.Health) * 0.25)
                        returnmessage += "{} showed {} some hospitality!".format(mon.GetNickname(), othermon.GetNickname())
                        break
            
            if (mon.HasAbility("Imposter")):
                target = random.choice(GetTargets(mon, Range.AllFoes))
                mon.ApplyStatus("transformed", copy.deepcopy(target))
                mon.ChangeForme("DittoTransform")
                returnmessage += "{} transformed into the opponent {}!".format(mon.GetNickname(), target.GetNickname())
            
            if (mon.HasAbility("Illusion", False)):
                usertrainer = mon.GetTrainer()
                if usertrainer != None and len(usertrainer.GetTeam()) > 1:
                    alivepokemon = []
                    for alivemon in usertrainer.GetTeam():
                        if (alivemon.Health >= 1 and alivemon not in Battlers()):
                            alivepokemon.append(alivemon)
                    if len(alivepokemon) > 0:
                        mon.ApplyStatus("illusion", alivepokemon[-1])
                        mon.ChangeForme("Illusion")

        return returnmessage

    def HasAlly(mon, allymonname):
        if (mon in FriendlyBattlers()):
            for othermon in FriendlyBattlers():
                if (othermon.GetNickname() == allymonname):
                    return True
        elif (mon in EnemyBattlers()):
            for othermon in EnemyBattlers():
                if (othermon.GetNickname() == allymonname):
                    return True
        else:
            return False

    def CalculateTetraElement(eevee):# returns the id of the eevee form to change into
        eeveedict = {
            "Fire": pokedexlookupname("Flareon", DexMacros.Id),
            "Water": pokedexlookupname("Vaporeon", DexMacros.Id),
            "Electric": pokedexlookupname("Jolteon", DexMacros.Id),
            "Psychic": pokedexlookupname("Espeon", DexMacros.Id),
            "Dark": pokedexlookupname("Umbreon", DexMacros.Id),
            "Ice": pokedexlookupname("Glaceon", DexMacros.Id),
            "Grass": pokedexlookupname("Leafeon", DexMacros.Id),
            "Fairy": pokedexlookupname("Sylveon", DexMacros.Id)
        }

        possibletypes = ["Fire", "Water", "Electric", "Psychic", "Dark", "Ice", "Grass", "Fairy"]
        typedict = {}

        for mon in GetTargets(eevee, forceenemy = True):
            for element in possibletypes:
                bonusagainstfoe = 1
                bonusfromfoe = 1
                bonusagainstfoe *= GetAllEffectiveness(element, mon.GetTypes())
                for foeelement in mon.GetTypes():
                    bonusfromfoe += GetEffectiveness(foeelement, element)
                cumulativebonus = bonusagainstfoe / bonusfromfoe
                if (element not in typedict.keys() or typedict[element] < cumulativebonus):
                    typedict[element] = cumulativebonus

        if (len(typedict) != 0):
            return eeveedict[max(typedict, key=typedict.get)]
        else:
            return None

    def CalculateHocusTransform(ditto):# returns the id of the legendary beast to change into
        beastdict = {
            "Fire": pokedexlookupname("Entei", DexMacros.Id),
            "Electric": pokedexlookupname("Raikou", DexMacros.Id),
            "Water": pokedexlookupname("Suicune", DexMacros.Id)
        }

        possibletypes = ["Water", "Fire", "Electric"]
        typedict = {}

        for mon in GetTargets(ditto, forceenemy = True):
            for element in possibletypes:
                bonusagainstfoe = 1
                bonusfromfoe = 1
                bonusagainstfoe *= GetAllEffectiveness(element, mon.GetTypes())
                for foeelement in mon.GetTypes():
                    bonusfromfoe += GetEffectiveness(foeelement, element)
                cumulativebonus = bonusagainstfoe / bonusfromfoe
                if (element not in typedict.keys() or typedict[element] < cumulativebonus):
                    typedict[element] = cumulativebonus

        if (len(typedict) != 0):
            return beastdict[max(typedict, key=typedict.get)]
        else:
            return None

    def AddNewWildPokemon(pkmn, firstslot=False, randslot=False, useoldtrainer=None):
        global Trainers
        if (useoldtrainer != None):
            newtrainer = useoldtrainer
            newtrainer.Team.append(pkmn)
        else:
            newtrainer = Trainer(str(len(Trainers)), TrainerType.Enemy, [pkmn], isPokemon=True)
        pkmn.Owner = newtrainer
        pkmn.TrainerType = newtrainer.GetType()
        pkmn.ItemHistory = [("Started", mon.GetItem(), 0)]
        if (IsAfter(9, 5, 2004) or (IsDate(9, 5, 2004) and timeOfDay not in ["Noon", "Morning", "Afternoon"])):
            pkmn.Trained = []
            for move in custommovesin:
                if (move in pkmn.GetMoveNames()):
                    pkmn.Trained.append(move)        
        pkmn.ResetCaught()
        if (useoldtrainer == None):
            if (randslot):
                candidates = []
                for trainer in EnemyTrainers(omitdefeated=True):
                    candidates.append(trainer)
                if (len(candidates) > 0):
                    candidate = RandomChoice(candidates)
                    newindex = Trainers.index(candidate) + RandomChoice([-1, 1])
                else:
                    newindex = 0
                Trainers.insert(newindex, newtrainer)
            elif (firstslot):
                Trainers = [newtrainer] + Trainers
            else:
                Trainers.append(newtrainer)

    def ClearSemiInvuls(mon):
        clearimmediately = ["airborne", "dug in", "diving", "ethereal"]
        for status in clearimmediately:
            if (mon.GetStatusCount(status) == 1):
                mon.ClearStatus(status)

    def GetBattleMusic(Trainers):
        regiondict = {}
        for trainer in Trainers:
            if (trainer.GetType() == TrainerType.Enemy):
                region = GetMusicRegion(trainer.GetName())
                if region in regiondict:
                    regiondict[region] += 1
                else:
                    regiondict[region] = 1

        topregion = max(regiondict, key=regiondict.get)

        if (topregion != "Default"):
            return topregion

        regiondict = {}
        for trainer in Trainers:
            if (trainer.GetType() == TrainerType.Ally):
                region = GetMusicRegion(trainer.GetName())
                if region in regiondict:
                    regiondict[region] += 1
                else:
                    regiondict[region] = 1

        if (len(regiondict) > 0):
            topregion = max(regiondict, key=regiondict.get)
            if (topregion != "Default"):
                return topregion

        return "Kanto"

define movestatuses = {
    "ice ball": ["Ice Ball"],
    "rollout": ["Rollout"],
    "thrashing": ["Thrash"],
    "uproaring": ["Uproar"],
    "outraged": ["Outrage"],
    "dug in": ["Dig"],
    "diving": ["Dive"],
    "airborne": ["Fly", "Bounce"],
    "ethereal": ["Phantom Force"],
    "cloaked in light": ["Sky Attack"],
    "charging light": ["Solar Beam"],
    "hardheaded": ["Skull Bash"],
    "whipping up winds": ["Razor Wind"],
    "petal dancing": ["Petal Dance"],
    "biding": ["Bide"]
}
