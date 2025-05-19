init python:
    def cp(trigger, word):
        return ConditionalPluralize(trigger, word)

    def ConditionalPluralize(trigger, word):
        if (isinstance(word, tuple)):
            single, plural = word
        else:
            single = word
            if (word == "was"):
                plural = "were"
            elif (word == "its"):
                plural = "their"
            elif (word[-1] == "y"):
                plural = word[:-1] + "ies"
            elif (word == "Pokémon"):
                plural = word
            else:
                plural = word + "s"
        if (trigger != 1):
            return plural
        else:
            return single

    class GoodEvent:
        GainItem = "GainItem"
        GainExperience = "GainExperience"
        FindStairs = "FindStairs"
        FindPitfall = "FindPitfall"
        GetCoins = "GetCoins"
        GetBond = "GetBond"
        HealAllies = "HealAllies"
        CureStatus = "CureStatus"
        BuffAllies = "BuffAllies"
        MaximizePP = "MaximizePP"
        GainGoodAbility = "GainGoodAbility"
        ApplyFoeHazard = "ApplyFoeHazard"

    GoodEvents = [value for key, value in GoodEvent.__dict__.items() if not key.startswith("__")]

    class BadEvent:
        LevelFoes = "LevelFoes"
        BuffFoes = "BuffFoes"
        DebuffAllies = "DebuffAllies"
        ReduceHealth = "ReduceHealth"
        ApplyStatus = "ApplyStatus"
        WindBlows = "WindBlows"
        IncapacitateAlly = "IncapacitateAlly"
        LoseStairs = "LoseStairs"
        MinimizePP = "MinimizePP"
        GainBadAbility = "GainBadAbility"
        ApplyAllyHazard = "ApplyAllyHazard"
        ConsolidateReinforcements = "ConsolidateReinforcements"
        BecomeExploding = "BecomeExploding"

    BadEvents = [value for key, value in BadEvent.__dict__.items() if not key.startswith("__")]

    class NeutralEvent:
        ChangeStats = "ChangeStats"
        ApplyStatus = "ApplyStatus"
        ChangePP = "ChangePP"
        ScrambleAbilities = "ScrambleAbilities"
        ChangeWeather = "ChangeWeather"
        ChangeTerrain = "ChangeTerrain"
        ApplyHazards = "ApplyHazards"
        SwapVibes = "SwapVibes"
        GoNextFloor = "GoNextFloor"
        FluctuateMysteriosity = "FluctuateMysteriosity"
        ChangeVibeChangeMagnitude = "ChangeVibeChangeMagnitude"
        ClearStats = "ClearStats"
        IncreaseEncounterSize = "IncreaseEncounterSize"

    NeutralEvents = [value for key, value in NeutralEvent.__dict__.items() if not key.startswith("__")]

label HandleNeutralEvent(dungeon, good_events, bad_events):
    python:
        outcome, outcomestr = dungeon.RollCoinFlip()

    if (outcome == Outcomes.Good):
        dn "The Mysteriosity flashes! Many changes occur, first against you, then toward you!"
    else:
        dn "The Mysteriosity flashes! A tremendous number of changes occur, first toward you, then against you!"

    python:
        eventqueueindex = 0
        if outcome == Outcomes.Good:
            eventqueue = bad_events + good_events
        else:
            eventqueue = good_events + bad_events

    label iteratingeventqueue:

    call PerformDungeonEvent(dungeon, Outcomes.Neutral, eventqueue[eventqueueindex]) from _call_PerformDungeonEvent

    $ eventqueueindex += 1
    if (eventqueueindex < len(eventqueue)):
        jump iteratingeventqueue

    return

label PerformDungeonEvent(dungeon, eventype=None, event=None):

$ subevent = True

if (event == None):
    $ subevent = False

    if (eventype == None):
        $ eventype = dungeon.RollOutcome()

    if (eventype == Outcomes.Nothing):
        jump afterdungeonevent

    else:
        $ event = dungeon.PickEvent(eventype)
        $ dungeon.RecordLastEvent(event)

$ skippingeventconsequences = True

$ prnt(f"{event} event triggered.")

if event == GoodEvent.GainItem:
    if (dungeon.GetLootList() == None or len(dungeon.GetLootList()) == 0):
        jump aftergenerosityfluctuation

    python:
        itemsfound, itemsfoundstr = dungeon.GoodMagnitude(1, dungeon.NumTrainers())
        for i in range(itemsfound):
            GetItem(WeightedRandomChoice(dungeon.GetLootList()), 1, text="default")
        dungeon.AddFloorEvent(GoodEvent.GainItem, 1)

    dn "You found [itemsfoundstr] [cp(itemsfound, 'item')]!"

elif event == GoodEvent.GainExperience:
    python:
        player = dungeon.GetPlayer()
        returntext = ""
        if (player != None):
            mons, monsstr = dungeon.GoodMagnitude(1, len(player.GetTeam()))
            exptolvl = pow(AimLevel(), 3) / 25
            exp, expstr = dungeon.GoodMagnitude(max(10, exptolvl / 20), exptolvl)
            expstring = []
            for mon in player.GetNumPkmn(mons):
                expstring += mon.GainExperience(exp)
            PrintExp(expstring)
        dungeon.AddFloorEvent(GoodEvent.GainExperience, 1)

    if (player != None):
        dn "[monsstr] of your Pokémon gained [expstr] experience!"
    else:
        jump aftergenerosityfluctuation

elif event == GoodEvent.FindStairs:
    if (not (dungeon.IsBossFight() or dungeon.GetFoundStairs())):
        $ dungeon.AddFloorEvent(GoodEvent.FindStairs, 1)
        dn "You abruptly found the stairs, even sooner than you were expecting!"
        $ dungeon.FindStairs()
    else:
        jump aftergenerosityfluctuation

elif event == GoodEvent.FindPitfall:
    if (dungeon.GetCurrentFloor() > 0 and not dungeon.IsBossFight()):
        dn "You find a pitfall that looks it will lead to the floor below! Want to take it?"

        menu:
            ">Jump on in!":
                $ Fled = True
                $ dungeon.DecreaseCurrentFloor()
                $ dungeon.AddPermEvent(GoodEvent.FindPitfall, 1)
                jump aftergenerosityfluctuation

            ">No thanks, I like having knees":
                pass
    else:
        jump aftergenerosityfluctuation

elif event == GoodEvent.GetCoins:
    python:
        coinsfound, coinsfoundstr = dungeon.GoodMagnitude(3, dungeon.NumTrainers() * 3)
        GetItem(Item.GimmighoulCoin, coinsfound, hidefanfare=True)
    
    dn "You stumbled upon [coinsfoundstr] Gimmighoul Coins!"

elif event == GoodEvent.GetBond:
    python:
        dungeon.AddFloorEvent(GoodEvent.GetBond, 1)
        allies, alliesstr = dungeon.GoodMagnitude(1, dungeon.NumTrainers())
        bondinc, bondincstr = dungeon.GoodMagnitude(1, 3)
        selectedtrainers = dungeon.GetNumTrainers(allies, excludered=True)
        for trainer in selectedtrainers:
            index = dungeon.GetTrainers().index(trainer)
            ValueChange(trainer.GetFormatName(), bondinc, position=((index + 1)/(len(dungeon.GetTrainers()) + 1), 0.8), pausing=False, changemood=False)

    dn "Your understanding of [alliesstr] [cp(allies, 'ally')] has increased by [bondincstr]!"

elif event == GoodEvent.HealAllies:
    python:
        returntext = ""
        allies, alliesstr = dungeon.GoodMagnitude(1, dungeon.NumBattlers())
        healamount, healamountstr = dungeon.GoodMagnitude(30, 300)
        for mon in dungeon.GetNumBattlers(allies):
            if (mon.GetHealthPercentage() < 1):
                mon.AdjustHealth(healamount)
                returntext += mon.GetTrainer().GetFormatName() + "'s " + mon.GetNickname() + " recovered {} HP!".format(healamountstr)
    
    if (returntext != ""):
        dn "[FormatText(returntext)]"
        dn "[alliesstr] [cp(allies, 'ally')] recovered [healamountstr] HP!"
    else:
        jump aftergenerosityfluctuation

elif event == GoodEvent.CureStatus:
    python:
        returntext = ""
        allies, alliesstr = dungeon.GoodMagnitude(1, dungeon.NumBattlers())
        for mon in dungeon.GetNumBattlers(allies):
            returntext += mon.ClearStatus("burned")
            returntext += mon.ClearStatus("badly poisoned")
            returntext += mon.ClearStatus("poisoned")
            returntext += mon.ClearStatus("paralyzed")
            returntext += mon.ClearStatus("asleep")
            returntext += mon.ClearStatus("frozen")
            returntext += mon.ClearStatus("confused")

    if (returntext != ""):
        dn "[FormatText(returntext)]"
        dn "[alliesstr] [cp(allies, 'ally')] [cp(allies, 'was')] cured of [cp(allies, 'its')] status [cp(allies, 'condition')]!"
    else:
        jump aftergenerosityfluctuation

elif event == GoodEvent.BuffAllies:
    python:
        returntext = ""
        allies, alliesstr = dungeon.GoodMagnitude(1, dungeon.NumBattlers())
        stages, stagesstr = dungeon.GoodMagnitude(1, 6)
        statchange = RandomChoice([Stats.Attack, Stats.Defense, Stats.SpecialAttack, Stats.SpecialDefense, Stats.Speed, Stats.Evasion, Stats.Accuracy])
        for mon in dungeon.GetNumBattlers(allies):
            returntext += mon.ChangeStats(statchange, stages, mon)

    if (returntext != ""):
        dn "[FormatText(returntext)]"
        dn "[alliesstr] [cp(allies, 'ally')] had a stat increased by [stagesstr] [cp(stages, 'stage')]!"
    else:
        jump aftergenerosityfluctuation

elif event == GoodEvent.MaximizePP:
    python:
        returntext = ""
        allies, alliesstr = dungeon.GoodMagnitude(1, dungeon.NumBattlers())
        moves, movesstr = dungeon.GoodMagnitude(1, 4)
        for mon in dungeon.GetNumBattlers(allies):
            for move in mon.GetNumMoves(moves):
                move.PP = move.MaxPP
                returntext += mon.GetTrainer().GetFormatName() + "'s " + mon.GetNickname() + " " + move.Name + " recovered all its PP!"

    if (returntext != ""):
        dn "[FormatText(returntext)]"
        dn "[alliesstr] [cp(allies, 'ally')] recovered all PP for [movesstr] [cp(moves, 'move')]!"
    else:
        jump aftergenerosityfluctuation

elif event == GoodEvent.GainGoodAbility:
    python:
        returntext = ""
        allies, alliesstr = dungeon.GoodMagnitude(1, dungeon.NumTrainers())
        ability = RandomChoice(["Purifying Salt", "Huge Power", "Moody", "Speed Boost", "Fluffy", "Adaptability", "Serene Grace", "Intimidate", "Magic Guard", "Libero", "Regenerator", "Mold Breaker", "Tinted Lens"])
        for mon in dungeon.GetNumBattlers(allies):
            mon.ApplyStatus(".tracing", ability, mon, True)
            returntext += mon.GetTrainer().GetFormatName() + "'s " + mon.GetNickname() + "'s ability became " + ability + "!"

    if (returntext != ""):
        dn "[FormatText(returntext)]"
        dn "[alliesstr] [cp(allies, 'ally')] gained a powerful ability!"
    else:
        jump aftergenerosityfluctuation

elif event == GoodEvent.ApplyFoeHazard:
    python:
        randchoice = RandInt(1, 4)
        returntext = ""
        if (randchoice == 1):
            returntext += ApplyEffect(fb(), "stealthy rocks", 1, True)
        elif (randchoice == 2):
            returntext += ApplyEffect(fb(), "sticky web", 1, True)
        elif (randchoice == 3):
            returntext += ApplyEffect(fb(), "spikes", 1, True)
        elif (randchoice == 4):
            returntext += ApplyEffect(fb(), "toxic spikes", 1, True)

    if ("But it failed!" not in returntext):
        dn "[FormatText(returntext)]"
        dn "Hazards have been applied to the opponent's side of the field!"
    else:
        jump aftergenerosityfluctuation

elif event == BadEvent.LevelFoes:
    python:
        levels, levelsstr = dungeon.BadMagnitude(1, 3)
        dungeon.AddFloorEvent(BadEvent.LevelFoes, levels + dungeon.GetEventValue(BadEvent.LevelFoes))

    narrator "The wild Pokémon grow more feral! Reinforcements will be [levelsstr] [cp(levels, 'level')] higher!"

elif event == BadEvent.BuffFoes:
    python:
        stat = RandInt(Stats.Attack, Stats.Evasion)
        stages, stagesstr = dungeon.BadMagnitude(1, 6)
        dungeon.AddFloorEvent(stat, stages + dungeon.GetEventValue(stat))

    narrator "The wild Pokémon grow more feral! Reinforcements will have their [StatToString(stat)] increased [stagesstr] [cp(stages, 'stage')]!"

elif event == BadEvent.DebuffAllies:
    python:
        returntext = ""
        allies, alliesstr = dungeon.BadMagnitude(1, dungeon.NumTrainers())
        stages, stagesstr = dungeon.BadMagnitude(1, 6)
        statchange = RandomChoice([Stats.Attack, Stats.Defense, Stats.SpecialAttack, Stats.SpecialDefense, Stats.Speed, Stats.Evasion, Stats.Accuracy])
        for mon in dungeon.GetNumBattlers(allies):
            returntext += mon.ChangeStats(statchange, -stages, mon)

    if (returntext != ""):
        dn "[FormatText(returntext)]"
        dn "[alliesstr] [cp(allies, 'ally')] had a stat decreased by [stagesstr] [cp(stages, 'stage')]!"
    else:
        jump aftergenerosityfluctuation

elif event == BadEvent.ReduceHealth:
    python:
        returntext = ""
        allies, alliesstr = dungeon.BadMagnitude(1, dungeon.NumTrainers())
        healamount, healamountstr = dungeon.BadMagnitude(30, 300)
        for mon in dungeon.GetNumBattlers(allies):
            if (mon.GetHealthPercentage() < 1):
                mon.AdjustHealth(-healamount)
                if (mon.GetHealthPercentage() <= 0):
                    mon.Health = 1
                    editedhealamountmagnitude, editedhealamountmagnitudestr = dungeon.BadMagnitude(healamount - 1, healamount - 1)
                    returntext += mon.GetTrainer().GetFormatName() + "'s " + mon.GetNickname() + " lost {} HP!".format(editedhealamountmagnitudestr)
                else:
                    returntext += mon.GetTrainer().GetFormatName() + "'s " + mon.GetNickname() + " lost {} HP!".format(healamountstr)
    
    if (returntext != ""):
        dn "[FormatText(returntext)]"
        dn "[alliesstr] [cp(allies, 'ally')] lost HP!"
    else:
        jump aftergenerosityfluctuation

elif event == BadEvent.ApplyStatus:
    python:
        returntext = ""
        allies, alliesstr = dungeon.BadMagnitude(1, dungeon.NumBattlers())
        status = RandomChoice(["burned", "badly poisoned", "poisoned", "paralyzed", "asleep", "frozen"])
        for mon in dungeon.GetNumBattlers(allies):
            statusmessage = mon.ApplyStatus(status, 1, mon, True)
            if (mon.HasStatus(status)):
                returntext += statusmessage

    if (returntext != ""):
        dn "[FormatText(returntext)]"
        dn "[alliesstr] [cp(allies, 'ally')] became [status]!"
    else:
        jump aftergenerosityfluctuation

elif event == BadEvent.WindBlows:
    python:
        returntext = dungeon.BlowTheWind()
    
    dn "[FormatText(returntext)]"

    if (dungeon.GetWindBlows() == 5):
        scene blank2
        call clearscreens() from _call_clearscreens_64
        jump gameover
    
elif event == BadEvent.IncapacitateAlly:
    if (not dungeon.IsBossFight()):
        python:
            returntext = ""
            allies, alliesstr = dungeon.BadMagnitude(1, max(1, math.floor(dungeon.NumTrainers() / 2)))
            incapallies = dungeon.GetNumTrainers(allies)
            dungeon.AddFloorEvent(BadEvent.IncapacitateAlly, incapallies)
            dungeon.GetTrainers()

        dn "[alliesstr] [cp(allies, 'ally')] [cp(allies, 'was')] suddenly whisked away to another floor!"
    else:
        jump aftergenerosityfluctuation

elif event == BadEvent.LoseStairs:
    if (dungeon.GetFoundStairs()):
        $ dungeon.LoseStairs()
        dn "You look away for a moment and suddenly lose track of the stairs..."
    else:
        jump aftergenerosityfluctuation
    
elif event == BadEvent.MinimizePP:
    python:
        returntext = ""
        allies, alliesstr = dungeon.BadMagnitude(1, dungeon.NumTrainers())
        moves, movesstr = dungeon.BadMagnitude(1, 4)
        for mon in dungeon.GetNumBattlers(allies):
            for move in mon.GetNumMoves(moves):
                move.PP = 0
                returntext += mon.GetTrainer().GetFormatName() + "'s " + mon.GetNickname() + "'s " + move.Name + " lost all its PP!"

    if (returntext != ""):
        dn "[FormatText(returntext)]"
        dn "[alliesstr] [cp(allies, 'ally')] lost all PP for [movesstr] [cp(moves, 'move')]!"
    else:
        jump aftergenerosityfluctuation

elif event == BadEvent.GainBadAbility:
    python:
        returntext = ""
        allies, alliesstr = dungeon.BadMagnitude(1, dungeon.NumTrainers())
        ability = RandomChoice(["Normalize", "Stall", "Slow Start", "Truant", "Defeatist", "Wimp Out", "Klutz", "Hustle", "Gorilla Tactics"])
        for mon in dungeon.GetNumBattlers(allies):
            mon.ApplyStatus(".tracing", ability, mon, True)
            returntext += mon.GetTrainer().GetFormatName() + "'s " + mon.GetNickname() + "'s ability became " + ability + "!"

    if (returntext != ""):
        dn "[FormatText(returntext)]"
        dn "[alliesstr] [cp(allies, 'ally')] gained a hindering ability!"
    else:
        jump aftergenerosityfluctuation

elif event == BadEvent.ApplyAllyHazard:
    python:
        randchoice = RandInt(1, 4)
        returntext = ""
        if (randchoice == 1):
            returntext += ApplyEffect(fb(), "stealthy rocks", 1, False)
        elif (randchoice == 2):
            returntext += ApplyEffect(fb(), "sticky web", 1, False)
        elif (randchoice == 3):
            returntext += ApplyEffect(fb(), "spikes", 1, False)
        elif (randchoice == 4):
            returntext += ApplyEffect(fb(), "toxic spikes", 1, False)

    if ("But it failed!" not in returntext):
        dn "[FormatText(returntext)]"
        dn "Hazards have been applied to your side of the field!"
    else:
        jump aftergenerosityfluctuation

elif event == BadEvent.ConsolidateReinforcements:
    python:
        allreinforcements = []
        for enemy in EnemyBattlers():
            if (len(enemy.GetTrainer().GetUnfaintedTeam()) > 1 and not enemy.HasStatus("tyrannic")):
                for reinforcement in enemy.GetTrainer().GetUnfaintedTeam():
                    if (reinforcement != enemy):
                        allreinforcements.append(reinforcement)

        for reinforcement in allreinforcements:
            for trainer in Trainers:
                if (reinforcement in trainer.GetTeam()):
                    trainer.GetTeam().remove(reinforcement)

        if (dungeon.IsBossFight()):
            for enemy in EnemyBattlers():
                if (enemy.HasStatus("tyrannic")):
                    consolidationmon = enemy
                    break
        else:
            consolidationmon = RandomChoice(EnemyBattlers())
        consolidationpoint = consolidationmon.GetTrainer()

        for reinforcement in allreinforcements:
            consolidationpoint.GetTeam().append(reinforcement)

        randchoice = RandInt(1, 4)
        returntext = ""
        if (randchoice == 1):
            returntext += ApplyEffect(fb(), "stealthy rocks", 1, False)
        elif (randchoice == 2):
            returntext += ApplyEffect(fb(), "sticky web", 1, False)
        elif (randchoice == 3):
            returntext += ApplyEffect(fb(), "spikes", 1, False)
        elif (randchoice == 4):
            returntext += ApplyEffect(fb(), "toxic spikes", 1, False)

    if (len(allreinforcements) != 0):
        dn "The wild Pokémon have rallied around the wild [consolidationmon.GetNickname()]!"
    else:
        jump aftergenerosityfluctuation

elif event == BadEvent.BecomeExploding:
    python:
        battlers, battlersstr = dungeon.BadMagnitude(1, dungeon.NumAllBattlers())
        battlemons = dungeon.GetNumAllBattlers(battlers, excludebosses=True)
        for mon in battlemons:
            mon.ApplyStatus("exploding", count=1, applier=None, overwrite=True)

    dn "[battlersstr] Pokémon suddenly started flashing!"

elif event == NeutralEvent.ChangeStats:
    call HandleNeutralEvent(dungeon, [GoodEvent.BuffAllies], [BadEvent.BuffFoes, BadEvent.DebuffAllies]) from _call_HandleNeutralEvent

elif event == NeutralEvent.ApplyStatus:
    call HandleNeutralEvent(dungeon, [GoodEvent.CureStatus], [BadEvent.ApplyStatus]) from _call_HandleNeutralEvent_1

elif event == NeutralEvent.ChangePP:
    call HandleNeutralEvent(dungeon, [GoodEvent.MaximizePP], [BadEvent.MinimizePP]) from _call_HandleNeutralEvent_2

elif event == NeutralEvent.ScrambleAbilities:
    call HandleNeutralEvent(dungeon, [GoodEvent.GainGoodAbility], [BadEvent.GainBadAbility]) from _call_HandleNeutralEvent_3

elif event == NeutralEvent.ChangeWeather:
    python:
        randchoice = RandInt(1, 5)
        duration, durationstr = dungeon.GetMagnitude(3, 20)
        returntext = ""
        if (randchoice == 1):
            returntext += ApplyWeather("sandstorm", duration)
        elif (randchoice == 2):
            returntext += ApplyWeather("hailing", duration)
        elif (randchoice == 3):
            returntext += ApplyWeather("rainy", duration)
        elif (randchoice == 4):
            returntext += ApplyWeather("snowy", duration)
        elif (randchoice == 5):
            returntext += ApplyWeather("sunny", duration)

    if ("But it failed!" not in returntext):
        dn "[FormatText(returntext)]"
        dn "The Mysteriosity changed the weather for [durationstr] turns!"
    else:
        jump aftergenerosityfluctuation

elif event == NeutralEvent.ChangeTerrain:
    python:
        randchoice = RandInt(1, 4)
        duration, durationstr = dungeon.GetMagnitude(3, 20)
        returntext = ""
        if (randchoice == 1):
            returntext += ApplyBattlefieldEffects("Grassy Terrain", duration)
        elif (randchoice == 2):
            returntext += ApplyBattlefieldEffects("Misty Terrain", duration)
        elif (randchoice == 3):
            returntext += ApplyBattlefieldEffects("Psychic Terrain", duration)
        elif (randchoice == 4):
            returntext += ApplyBattlefieldEffects("Electric Terrain", duration)

    if ("But it failed!" not in returntext):
        dn "[FormatText(returntext)]"
        dn "The Mysteriosity changed the terrain for [durationstr] turns!"
    else:
        jump aftergenerosityfluctuation

elif event == NeutralEvent.ApplyHazards:
    call HandleNeutralEvent(dungeon, [GoodEvent.ApplyFoeHazard], [BadEvent.ApplyAllyHazard]) from _call_HandleNeutralEvent_4
    
elif event == NeutralEvent.SwapVibes:
    python:
        turns, turnsstr = dungeon.GetMagnitude(1, 10)
        dungeon.AddPermEvent(NeutralEvent.SwapVibes, turns)
    dn "The Mysteriosity fluctuated wildly! Ferocity became Generosity, and Generosity became Ferocity, for [turnsstr] [cp(turns, 'turn')]!"
    
elif event == NeutralEvent.GoNextFloor:
    if (not dungeon.IsBossFight()):
        python:
            AutoWin = True

        dn "The Mysteriosity fluctuates, and... wait, you're on the next floor already?!"

    else:
        jump aftergenerosityfluctuation
    
elif event == NeutralEvent.FluctuateMysteriosity:
    python:
        flux, fluxstr = dungeon.GetMagnitude(dungeon.GetMysteriosity() / 2, dungeon.GetMysteriosity() * 2)

    dn "The Mysteriosity fluctuates and swells enormously! (A [fluxstr] unit increase!)"

elif event == NeutralEvent.ChangeVibeChangeMagnitude:
    python:
        change, changestr = dungeon.GetMagnitude(100, 300)
        dungeon.AddPermEvent(NeutralEvent.ChangeVibeChangeMagnitude, max(1, change) * dungeon.GetEventValue(NeutralEvent.ChangeVibeChangeMagnitude) / 100)

    dn "The Mysteriosity fluctuates, and the air becomes tense! Both Ferocity and Generosity will increase [changestr] percent faster!"

elif event == NeutralEvent.ClearStats:
    python:
        for mon in Battlers():
            mon.ResetStatChanges()

    dn "The Mysteriosity fluctuates, and every battler's stats are reset!"

elif event == NeutralEvent.IncreaseEncounterSize:
    if (dungeon.Reinforcing):
        python:
            pkmn = dungeon.AddNewDungeonPokemon()

        narrator "A wild [pkmn.GetNickname()] appeared out of the Mysteriosity!"
    else:
        jump aftergenerosityfluctuation

else:# custom events
    $ renpy.call(event)

if (subevent):
    jump aftergenerosityfluctuation

label afterdungeonevent:

python:
    skippingeventconsequences = False
    if (eventype == Outcomes.Good):
        dungeon.ChangeGood(-20)
    elif (eventype == Outcomes.Bad):
        dungeon.ChangeGood(10)

label aftergenerosityfluctuation:

if (not subevent and eventype != Outcomes.Nothing and skippingeventconsequences):
    $ prnt(f"{event} event had no effect.")

return