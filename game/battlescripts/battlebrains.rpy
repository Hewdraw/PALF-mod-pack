#battlebrains
init python:#brainaction makes the function return True or False, to determine whether to use the brain or not
    def dawndragonitebrain(pkmn):
        movechosen = ""
        if (pkmn.GetHealthPercentage() <= 0.2):
            return (Item.FullRestore, [pkmn])
        elif (pkmn.GetHealthPercentage() >= 0.66):
            if (pkmn.GetStatChanges(Stats.Defense) < 6):
                movechosen = "Cotton Guard"
            else:
                if (pkmn.GetMovePP("Hyper Voice") > 1):
                    movechosen = "Hyper Voice"
                else:
                    movechosen = "Dragon Pulse"
        else:
            movechosen = "Roost"

        return (movechosen, [FriendlyBattlers()[0]])

    def dawnpikachubrain(pkmn):
        movechosen = ""
        target = None
        usespreadmoves = False
        if ("Liberage" not in pikachuobj.GetMoveNames() and pkmn.GetHealthPercentage() <= 0.5):
            return (Item.FullRestore, [pkmn])
        elif ("Liberage" not in pikachuobj.GetMoveNames() and (pkmn.Moves[0].PP == 0 or pkmn.Moves[1].PP == 0 or pkmn.Moves[2].PP == 0 or pkmn.Moves[3].PP == 0)):
            return (Item.MaxElixir, [pkmn])
        elif (len(FriendlyBattlers()) == 2):
            noswitch = True
            for action in CurrentActions:
                if (action.GetActionType() == ActionTypes.Pokemon and action.GetTargets()[0].GetId() == 25):
                    noswitch = False
                    if (action.GetUser() == FriendlyBattlers()[0]):
                        target = [FriendlyBattlers()[1]]
                    else:
                        target = [FriendlyBattlers()[0]]
            if (target == None):
                if (noswitch and FriendlyBattlers()[0].GetId() == 292):#Shedinja continjancy
                    return ("Ominous Wind", [FriendlyBattlers()[0]])
                elif (noswitch and FriendlyBattlers()[1].GetId() == 292):#Shedinja continjancy part 2: the reckoning
                    return ("Ominous Wind", [FriendlyBattlers()[1]])
                elif (noswitch and FriendlyBattlers()[0].GetId() != 25 and FriendlyBattlers()[1].GetId() != 25):
                    usespreadmoves = True
                    target = [FriendlyBattlers()[0], FriendlyBattlers()[1]]
                elif (FriendlyBattlers()[0].GetId() == 25):
                    target = [FriendlyBattlers()[1]]
                elif (FriendlyBattlers()[1].GetId() == 25):
                    target = [FriendlyBattlers()[0]]
                else:
                    problematicmoves = ["Perish Song", "Metronome", "Leech Seed", "Dragon Rage", "Sand Attack", "Thunder Wave", "Thunder Shock", "Whirlwind", "Roar", "Toxic", "Bad Breath", "Poison Powder", "Poison Sting", "Sludge Bomb", "Ember", "Steady Flame", "Will-O-Wisp"]
                    for move in problematicmoves:
                        if (move in FriendlyBattlers()[0].GetMoveNames()):
                            target = [FriendlyBattlers()[0]]
                    if (target == None):
                        target = [FriendlyBattlers()[1]]
            maxbonus = 0
            maxmove = "Dragon Pulse"
            for move in pkmn.GetMoveNames():
                newbonus = GetTypeBonus(move, GetMove(move).Type, target[0], pkmn) * GetMove(move).Power
                
                if (MoveValid(pkmn, GetMove(move)) and newbonus > maxbonus and (move not in ["Earthquake", "Hyper Voice"] and not usespreadmoves or move in ["Earthquake", "Hyper Voice"] and usespreadmoves)):
                    maxmove = move
                    maxbonus = newbonus

            return (maxmove, target)

        else:
            target = FriendlyBattlers()[0]
            movechosen = None
            if (movesdodged.count("Dragon Pulse") < 5):
                movechosen = "Dragon Pulse"
            elif ("Earthquake" not in movesdodged):
                movechosen = "Earthquake"
            elif ("Ominous Wind" not in movesdodged):
                movechosen = "Ominous Wind"
            else:
                movechosen = "Hyper Voice"

            return (movechosen, [target])

    def jasminebrain1(pkmn):
        if (pkmn.GetNickname() in ["Magnemite", "Magneton", "Magnezone"]):
            if (HasAlly(pkmn, "Steelix") and not pkmn.HasStatus("levitating")):
                return ("Magnet Rise", [pkmn])
        elif (pkmn.GetNickname() in ["Pineco", "Forretress"]):
            if (HasAlly(pkmn, "Steelix") and not pkmn.HasStatus(".protections")):
                return ("Protect", [pkmn])

    def calembrain1(pkmn):
        movechosen = ""
        custom_action = ""
        calem_flabebe_shenanigans_list = ["Flabébé spun around its flower playfully, taunting you!", "Flabébé deliberately looked away from Calem!", "Flabébé acted as if you weren't worth its time.", "Flabébé gave Calem a withering look."]
        movechosen = random.choice(GetValidMoves(pkmn)).Name
        if (pkmn.GetNickname() == "Flabébé"):
            if (renpy.random.random() < 0.75):
                custom_action = "Calem Flabébé's shenanigans"
                movechosen = renpy.random.choice(calem_flabebe_shenanigans_list)
            
        return (movechosen, [FriendlyBattlers()[0]], custom_action)

    def cherenbrain1(pkmn):
        if (pkmn.GetNickname() in ["Purrloin", "Liepard"] and MoveValid(pkmn, pkmn.GetMoveByName("Assist"))):
            return ("Assist", [pkmn])

    def oakkecleontestbrain(pkmn):
        return (pkmn.GetMoveNames()[0], [FriendlyBattlers()[0]])

    def oakkecleontestswitchbrain(trainer):
        for mon in trainer.GetUnfaintedTeam():
            if (mon.GetNickname() == "Tangela"):
                return mon
        return None#this just means it's giving up trying to make a choice, not that you switch in "nothing"

    def combeebrain(pkmn):
        if (pkmn.GetId() == 416):
            if (pkmn.GetHealthPercentage() <= 0.666):
                return ("Heal Order", [pkmn])
            elif (len(EnemyBattlers()) < 3):
                return ("Defend Order", [pkmn])
        return None

    def gardeniafieldswitchbrain(trainer):
        for mon in trainer.GetUnfaintedTeam():
            if ("Phantump" not in mon.GetNickname()):#send out Phantump last
                return mon
        return None#this just means it's giving up trying to make a choice, not that you switch in "nothing"

    def duplicaswitchbrain(trainer):
        for mon in trainer.GetUnfaintedTeam():
            if (mon.Moves[0].Name != "Kasa's Transform"):#send out special ditto last
                return mon
        return None#this just means it's giving up trying to make a choice, not that you switch in "nothing"

    def beaswitchbrain(trainer):
        tyrogueobj = GetTrainerTeam("Bea", "Tyrogue", heal=False)
        falinksobj = GetTrainerTeam("Bea", "Falinks", heal=False)
        if (tyrogueobj not in trainer.GetUnfaintedTeam() and falinksobj in trainer.GetUnfaintedTeam() and falinksobj not in Battlers()):
            return falinksobj#send out falinks only after Hitmontop has fainted
        return None#this just means it's giving up trying to make a choice, not that you switch in "nothing"

    def flannerybattlebrain(pkmn):
        if (pkmn.GetNickname() == "Numel"):
            usemagnitude = True
            uselavaplume = True                
            for allypkmn in GetBattlers(pkmn):
                fireimmune = True
                usingprotectmove = False
                for action in CurrentActions:
                    if (action.GetUser() == allypkmn):
                        if (action.GetActionType() == ActionTypes.Move and action.GetMove() != None and action.GetMove().Name == "Protect"):
                            usingprotectmove = True
                            break
                        if (allypkmn.GetStat(Stats.Speed) > pkmn.GetStat(Stats.Speed)):#if the ally is moving first...
                            if (not (action.GetActionType() == ActionTypes.Move and action.GetMove() != None and action.GetMove().Name == "Dig")):#and is not going to use dig...
                                fireimmune = False#then don't use lava plume
                        elif (allypkmn.GetStat(Stats.Speed) <= pkmn.GetStat(Stats.Speed)):#if numel is moving first, or it's a speed tie...
                            if (not allypkmn.HasStatus("dug in")):# and the ally is not currently dug in...
                                fireimmune = False#don't use lava plume

                if (not (usingprotectmove or allypkmn == pkmn or fireimmune or allypkmn.HasAbility("Flash Fire", False))):
                    uselavaplume = False

                if (not (usingprotectmove or allypkmn == pkmn or allypkmn.HasItem(Item.AirBalloon))):
                    usemagnitude = False

            options = []

            if (usemagnitude):
                options.append("Magnitude")
            if (uselavaplume):
                options.append("Lava Plume")

            if (len(options) > 0):
                return (random.choice(options), GetTargets(pkmn, Range.AllAdjacent))