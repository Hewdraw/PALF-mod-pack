﻿label Battle(trainers, currentWeather=None, customexpressions=[], reanchor=[], uniforms=[], clearstats=True, gainexp=True, healParty=True, specialmusic=None, unrunnable=False, levelscale=None, stopmusic=True, lockbag=False, dialogfunc=None, custombrain=None, lockluck=False, customswitchbrain=None, customoutfits=[], canBeDitto=False, preserveAllStats=False, dungeon=None):
$ renpy.transition(dissolve)
call clearscreens from _call_clearscreens
python:
    if (renpy.in_rollback()):
        renpy.rollback(True)
    renpy.suspend_rollback(True)
    if (not betatesting()):
        _rollback = False
    inbattle = True
    hidebattleui = False
    Trainers = trainers#[Trainer Class]
    ActionLog = []#[Action]
    CurrentActions = []#[Action] - after these are executed, put them in ActionLog
    CurrentWeather = currentWeather#None or (string, int)
    FriendlyEffects = {}#[Effect] - Includes hazards, reflect, whirlpool, etc.
    EnemyEffects = {}#[Effect]
    BattlefieldEffects = {}#[Effect] - Includes stuff like trick room, terrains, and the increasing power of echoed voice
    Turn = 0
    StopMusic = stopmusic
    LockLuck = lockluck#turns off random critical hits and damage variation
    CustomSwitchBrain = customswitchbrain
    UsingMove = False
    MoveUser = None
    ActiveMove = None
    BeginningEffects = False
    GainExp = gainexp
    BattlerIndex = 0
    FaintedMons = []
    Fled = False
    Unrunnable = unrunnable
    terabuttontext = "Terastallize"
    tookdamage = False
    pokemonfainted = False
    switched = False
    IsWinner = False
    if (dialogfunc == None and dungeon != None and dungeon.CutsceneFunc != None):
        dialogfunc = dungeon.CutsceneFunc

    if (levelscale != None):
        Trainers = copy.deepcopy(trainers)
        for trainer in Trainers:
            for mon in trainer.GetTeam():
                mon.Level = levelscale
                mon.RecalculateStats()

    playerteamnames = []
    enemyteamnames = []
    pkmnnames = []
    pkmnids = []
    WildBattle = True
    GimmickCost = 1 
    AutoLose = False
    AutoWin = False

    BattleSetup()# sets a bunch of battle variables of the 'mons
    for trainer in Trainers:
        for mon in trainer.GetTeam():
            if (clearstats and not preserveAllStats):
                mon.ResetStatChanges()
            if (healParty):
                mon.Heal()
            if (mon.GetHealthPercentage() <= 0):
                FaintedMons.append(mon)
            if mon.Id in [570, 570.1, 571, 571.1] and (trainer.GetType() != TrainerType.Enemy): # ally Zorua and Zoroark create a list of moves that the opponents used against them and that failed
                mon.suspiciousmoves = []
        trainer.ReorderTeam()
        if (trainer.GetType() != TrainerType.Enemy):
            playerteamnames.append(trainer.GetName())
        else:
            if (not trainer.GetIsPokemon()):
                WildBattle = False
            enemyteamnames.append(trainer.GetName())
        if (trainer.GetIsPokemon()):
            pkmnnames.append(trainer.GetName())
            pkmnids.append(trainer.GetTeam()[0].GetId())
        if (trainer.Name == "sideportraitfull"):
            pkmnnames.append(pokedexlookup(trainer.GetTeam()[0].Id, DexMacros.Id))
            pkmnids.append(trainer.GetTeam()[0].Id)
    
    if (specialmusic != "Nothing"):
        renpy.music.stop()
        renpy.music.stop(channel="crowd")
        renpy.music.stop(channel="crowd2")
        if (WildBattle):
            renpy.music.queue("Audio/Music/RBY_Pokemon_Start.ogg", channel='music', loop=None, fadein=1.0, tight=None)
            renpy.music.queue("Audio/Music/RBY_Pokemon_Loop.ogg", channel='music', loop=True)
        elif (specialmusic == None):
            region_music_map = {
                "Johto": "Audio/Music/johtotrainer.ogg",
                "Hoenn": "Audio/Music/hoenntrainer.ogg",
                "Sinnoh": "Audio/Music/sinnohtrainer.ogg",
                "Unova": "Audio/Music/unovatrainer.ogg",
                "Kalos": "Audio/Music/kalostrainer.ogg",
                "Alola": "Audio/Music/alolatrainer.ogg",
                "Galar": "Audio/Music/galartrainer.ogg",
                "Paldea": "Audio/Music/paldeatrainer.ogg",
                "Orre": "Audio/Music/orretrainer.ogg",
            }

            regionmusic = GetBattleMusic(Trainers)
            music_file = region_music_map.get(regionmusic)

            if music_file:
                renpy.music.queue(music_file, channel='music', loop=None, fadein=1.0, tight=None)
            else:
                renpy.music.queue("Audio/Music/KantoTrainerStart_Rock.ogg", channel='music', loop=None, fadein=1.0, tight=None)
                renpy.music.queue("Audio/Music/KantoTrainerLoop_Rock.ogg", channel='music', loop=True)
        elif (len(specialmusic) == 2):
            renpy.music.queue(specialmusic[0], channel='music', loop=None, fadein=1.0, tight=None)
            renpy.music.queue(specialmusic[1], channel='music', loop=True)
        else:
            renpy.music.queue(specialmusic, channel='music', loop=True, fadein=1.0, tight=None) 

if (dungeon == None):
    call CreateSplash(playerteamnames, enemyteamnames, customexpressions, reanchor, uniforms, pkmnnames, pkmnids, customoutfits) from _call_CreateSplash

label Start:
while (Turn == 0 or not BattleOver()):
    python:
        random.seed()
        MultihitCount = None
        MultihitMax = None
        UsedEchoedVoice = False
        CurrentActions = []
        ItemText = ""
        SwappingInMon = []
    if (not renpy.get_screen("Battle")):
        show screen battle

    python:
        if (not BeginningEffects):
            priority_abilities = ["Illusion"]
            for mon in Battlers(True):
                if mon.GetAbility() in priority_abilities:
                    mon.SetDamagedThisTurn(False)
                    SwitchInEffects(mon, False, True)
            for mon in Battlers(True):
                if not mon.GetAbility() in priority_abilities:
                    mon.SetDamagedThisTurn(False)
                    SwitchInEffects(mon, False, True)
            BeginningEffects = True
        for mon in Battlers(True):
            mon.SetPreTurnAbility()
        if (dialogfunc != None):
            dialogfunc("BeforeBattle")
        if (Turn == 0):
            Turn = 1

    label ChooseStart:
    $ BattlerIndex = len(CurrentActions)
    $ extrarollback = 0
    while BattlerIndex < len(FriendlyBattlers()):
        hide screen battle
        python:
            mon = FriendlyBattlers()[BattlerIndex]

            skipchoices = False
            for status, move_names in movestatuses.items():
                if mon.HasStatus(status):
                    lastmove = GetLastMove(ActionLog, mon, lookformoves=move_names, returnaction=True)
                    if (lastmove != None):
                        skipchoices = True
                        lasttarget = lastmove.GetTargets()[0]
                        if lasttarget not in Battlers():
                            lasttarget = GetTargets(mon, GetMoveRange(lastmove.Move), True)[min(len(GetTargets(mon, GetMoveRange(lastmove.Move), True)) - 1, lastmove.GetTargetSlots()[0])]
                        CurrentActions.append(Action(0, mon.GetStat(Stats.Speed), ActionTypes.Move, mon.GetTrainer(), mon, GetMove(lastmove.Move.Name), [lasttarget.GetTrainer()], [lasttarget], Turn))

        if (not mon.HasStatus("recharging") and not skipchoices):
            show screen battle

            python:
                createmegaitem = None
                
                for fvl in mon.GetForeverals():
                    if (lookupforeveraldata(fvl, FVLMacros.FVLType) == ForeveralTypes.Mega):
                        createmegaitem = lookupforeveraldata(fvl, FVLMacros.FVLTypeData)[0]

                if (createmegaitem != None):
                    itemname = GetItemName(createmegaitem)
                    preposition = ("a" if itemname[0] not in ["A", "E", "I", "O", "U"] else "an")
                    if mon.HasItem(None):
                        mon.GiveItem(createmegaitem)
                        if mon.HasItem(createmegaitem):
                            renpy.say(None, "{}'s wishes coalesced into {} {}!".format(mon.GetNickname(), preposition, itemname))
                    elif not mon.HasItem(createmegaitem):
                        olditem = mon.GetItem()
                        mon.TakeItem()
                        mon.GiveItem(createmegaitem)
                        if mon.HasItem(createmegaitem):
                            renpy.say(None, "The {} was discarded! {}'s wishes coalesced into {} {}!".format(GetItemName(olditem), mon.GetNickname(), preposition, itemname))

                battleCommand = renpy.call_screen("battle", currentMon=mon)

            if (battleCommand == 'devwin'):
                python:
                    AutoWin = True
                jump endbattle
            elif (battleCommand == 'devlose'):
                python:
                    AutoLose = True
                jump endbattle
            elif (battleCommand == 'devko'):
                python:
                    eb().Health = 0
                    BattleCheck()
            elif (battleCommand == 'tera'):
                if (mon.IsTerad()):
                    $ mon.Terastallized = -1
                else:
                    $ mon.Terastallized = Turn
                jump ChooseStart
            elif (battleCommand == 'lib'):
                if (mon.GetId() == 25):
                    call dawnpikachudialog6 from _call_dawnpikachudialog6
                else:
                    label newbanner:
                    narrator "What color will your banner be?"

                    $ renpy.call_screen("liberize")

                    if (len(libtypes) == 0):
                        narrator "You must pick a banner to fly! Liberation has no room for bystanders!"

                        jump newbanner

                    $ types = libtypes[0]
                    if (len(libtypes) == 2):
                        $ types = libtypes[0] + "/" + libtypes[1]

                    narrator "Do you want to raise up the banner of the [types]-type?"

                    menu:
                        "Let me fight for another cause.":
                            jump newbanner

                        "Raise it high!":
                            pass

                jump ChooseStart
            elif (battleCommand == 'div'):
                python:
                    forms = []
                    for fvl in mon.GetForeverals():
                        if (lookupforeveraldata(fvl, FVLMacros.FVLType) == ForeveralTypes.FormSwap):
                            forms = lookupforeveraldata(fvl, FVLMacros.FVLTypeData)
                    numdiv = 0
                    for othermon in PlayerBattlers():
                        if ((othermon.HasStatus("mega evolved") or othermon.HasStatus("diveralized") or othermon.HasStatus("minigigamaxed")) and othermon != mon):
                            numdiv += 1
                    if ((GimmickCost - numdiv) <= 0):
                        renpy.say(None, "The power of the Foreverals has been expended for this battle...")
                    elif (mon.GetId() == forms[0]):
                        mon.ChangeForme(forms[1])
                    elif (mon.GetId() == forms[1]):
                        mon.ChangeForme(forms[0])
                    else:
                        mon.ChangeForme(forms[0])
                    if (mon.HasStatus("diveralized")):
                        mon.ClearStatus("diveralized")
                    else:
                        mon.ApplyStatus("diveralized")
                jump ChooseStart
            elif (battleCommand == 'mega'):
                python:
                    megaid = None
                    for fvl in mon.GetForeverals():
                        if (lookupforeveraldata(fvl, FVLMacros.FVLType) == ForeveralTypes.Mega):
                            megaid = lookupforeveraldata(fvl, FVLMacros.FVLTypeData)[1]
                    numdiv = 0
                    for othermon in PlayerBattlers():
                        if ((othermon.HasStatus("mega evolved") or othermon.HasStatus("diveralized") or othermon.HasStatus("minigigamaxed")) and othermon != mon):
                            numdiv += 1
                    if ((GimmickCost - numdiv) <= 0):
                        renpy.say(None, "The power of the Foreverals has been expended for this battle...")
                    elif (mon.GetId() != megaid):
                        mon.ChangeForme(megaid)
                        mon.ApplyStatus("mega evolved")
                    else:
                        mon.ClearStatus("mega evolved")
                        mon.ChangeForme(None, revert=True)
                jump ChooseStart
            elif (battleCommand == 'giga'):
                python:
                    megaid = None
                    for fvl in mon.GetForeverals():
                        if (lookupforeveraldata(fvl, FVLMacros.FVLType) == ForeveralTypes.Mega):
                            megaid = lookupforeveraldata(fvl, FVLMacros.FVLTypeData)[1]
                    numdiv = 0
                    for othermon in PlayerBattlers():
                        if ((othermon.HasStatus("mega evolved") or othermon.HasStatus("diveralized") or othermon.HasStatus("minigigamaxed")) and othermon != mon):
                            numdiv += 1
                    if ((GimmickCost - numdiv) <= 0):
                        renpy.say(None, "The power of the Foreverals has been expended for this battle...")
                    elif (mon.GetId() != megaid):
                        mon.ChangeForme(megaid)
                        mon.ApplyStatus("minigigamaxed")
                    else:
                        mon.ClearStatus("minigigamaxed")
                        mon.ChangeForme(None, revert=True)
                jump ChooseStart
            elif (battleCommand == 'fight'):
                $ moveCommand = renpy.call_screen("moves", mon)
                if (moveCommand == 'back'):
                    jump ChooseStart
                elif (moveCommand == 'Struggle'):
                    $ foe = GetRandomAdjacentFoe(mon)
                    $ CurrentActions.append(Action(0, mon.GetStat(Stats.Speed), ActionTypes.Move, mon.GetTrainer(), mon, struggle, [foe.GetTrainer()], [foe], Turn))
                else:
                    $ moveselected = mon.GetMove(moveCommand)
                    if (not MoveValid(mon, moveselected)):
                        $ renpy.say(None, "Can't use that!")
                        jump ChooseStart
                    $ targetFoes = GetTargets(mon, GetMoveRange(moveselected))
                    if (len(GetTargets(mon, GetMoveRange(moveselected))) > 1 and (GetMoveRange(moveselected) == Range.AnyOrSelf or len(Battlers()) > 2)):
                        $ targetFoes = renpy.call_screen("choosetarget", moveselected, mon)
                        if (targetFoes == 'back'):
                            jump ChooseStart
                    $ CurrentActions.append(Action(0, mon.GetStat(Stats.Speed), ActionTypes.Move, mon.GetTrainer(), mon, moveselected, GetTrainers(targetFoes), targetFoes, Turn))    
            elif (battleCommand == 'bag'):
                python:
                    if (not lockbag and not isgame):
                        if (mon.GetTrainerType() == TrainerType.Player):
                            if (len(inventory.keys()) > 0):
                                if (not renpy.get_screen("inventory")):
                                    itemuse = renpy.call_screen("inventory")
                                    targetFoes = []
                                    if (itemuse == "Back"):
                                        renpy.jump("ChooseStart")
                                    elif ItemHasCategory(itemuse, "Poké Balls"):
                                        targetFoes = [EnemyBattlers()[0]]
                                        if (len(EnemyBattlers()) != 1):
                                            targetFoes = renpy.call_screen("choosetarget", Range.Any, mon)
                                        if (targetFoes == "back"):
                                            renpy.jump("ChooseStart")
                                        elif (len(playerparty) == 6 and IsBefore(17, 4, 2004)):
                                            renpy.say(None, "Your party is full, and you don't have anywhere to send your extra Pokémon yet!")
                                            renpy.jump("ChooseStart")
                                        elif (not targetFoes[0].GetTrainer().GetIsPokemon()):
                                            renpy.say(None, "You can't catch an opponent's Pokémon! You don't even have a Snag Machine!")
                                            dialogfunc("FailToCatch")
                                            renpy.jump("ChooseStart")
                                        finalTarget = targetFoes
                                    else:
                                        scope = GetItemScope(itemuse)
                                        if (scope != "None"):
                                            targetFoes = renpy.call_screen("switch", mon.GetTrainer())
                                            if (targetFoes == "back"):
                                                renpy.jump("ChooseStart")
                                            targetFoes = mon.GetTrainer().GetTeam()[targetFoes]
                                            if scope == "Move":
                                                targetMove = renpy.call_screen("moves", targetFoes, ignoreValidity = True)
                                                if targetMove == "back":
                                                    renpy.jump("ChooseStart")
                                        if (scope == "None"):
                                            finalTarget = fb()
                                        else:
                                            finalTarget = targetFoes if scope == "Pokemon" else targetFoes.Moves[targetMove]
                                            if (not ValidateItemUsage(itemuse, finalTarget) or (scope != "None" and targetFoes.HasStatus("embargoed"))):
                                                if (scope == "Pokemon"):
                                                    renpy.say(None, "You can't use that item on that Pokémon!")
                                                elif (scope == "Move"):
                                                    renpy.say(None, "You can't use that item on that move!")
                                                else:
                                                    renpy.say(None, "You can't use that item right now!")
                                                renpy.jump("ChooseStart")
                                            targetFoes = [targetFoes]

                                    CurrentActions.append(Action(6, mon.GetStat(Stats.Speed), ActionTypes.Bag, mon.GetTrainer(), mon, itemuse, GetTrainers(targetFoes), [finalTarget], Turn, targetFoes))

                            else:
                                renpy.say(None, "You have no items in your bag!")
                                renpy.jump("ChooseStart")
                        else:
                            renpy.say(None, "Only you can reach into your bag!")
                            renpy.jump("ChooseStart")
                    else:
                        renpy.say(None, "You can't use your bag right now!")
                        renpy.jump("ChooseStart")
            elif (battleCommand == 'pokemon'):
                $ ShowBattleUI()
                label Switching:
                    python:
                        if (CanSwitch(mon, False)):
                            hideback = False
                            mustswitch = False
                            switchCommand = renpy.call_screen('switch', mon.GetTrainer())
                            if (switchCommand == 'back'):
                                renpy.jump("ChooseStart")
                            newPokemon = mon.GetTrainer().GetTeam()[switchCommand]
                            if (newPokemon.GetHealth() == 0):
                                renpy.say(None, "{} has fainted, and cannot fight!".format(newPokemon.GetNickname()))
                                renpy.jump("Switching")
                            elif (newPokemon in Battlers()):
                                renpy.show_screen("battleui")
                                renpy.say(None, "{} is already in battle!".format(newPokemon.GetNickname()))
                                renpy.jump("Switching")
                            elif (newPokemon in SwappingInMon):
                                renpy.show_screen("battleui")
                                renpy.say(None, "{} is already switching in!".format(newPokemon.GetNickname()))
                                renpy.jump("Switching")
                            SwappingInMon.append(newPokemon)
                            CurrentActions.append(Action(6, mon.GetStat(Stats.Speed), ActionTypes.Pokemon, mon.GetTrainer(), mon, None, [mon.GetTrainer()], [newPokemon], Turn))
                        else:
                            renpy.say(None, "{} cannot switch out!".format(mon.GetNickname()))
                            renpy.jump("ChooseStart")
            elif (battleCommand == 'run'):
                $ ShowBattleUI()
                if (Unrunnable):
                    "You can't run from this battle!"
                elif (WildBattle):
                    if (fb().GetId() == 562.1):
                        $ fail = False
                        if (location != "catacombs"):
                            $ fail = True
                            "[fb().GetNickname()] seems relieved to be given the order to run. It does not seem comfortable in this area."
                        if (not fail):
                            if (eb().GetId() != pokedexlookup("Stonjourner", DexMacros.Id)):
                                $ fail = True
                                "[fb().GetNickname()] seems agitated... it seems to be looking for something in the catacombs, but the wild [eb().GetNickname()] isn't it."
                        if (not fail):
                            if (fb().DamageTaken < 49):
                                $ fail = True
                                "[fb().GetNickname()] is lashing out wildly... it looks like it still has a lot of energy, and wants to battle this Stonjourner longer!"
                        if (fail):
                            $ CurrentActions.append(Action(6, mon.GetStat(Stats.Speed), ActionTypes.Run, mon.GetTrainer(), mon, None, [mon.GetTrainer()], [mon], Turn))
                        else:
                            "You and [fb().GetNickname()] dash through the Stonjourner's legs to get away! However, the moment [fb().GetNickname()] passes through..."
                            $ fb().Evolve(pokedexlookup("Runerigus", DexMacros.Id))
                    else:
                        $ CurrentActions.append(Action(6, mon.GetStat(Stats.Speed), ActionTypes.Run, mon.GetTrainer(), mon, None, [mon.GetTrainer()], [mon], Turn))
                elif (eb() == GetTrainerTeam("Iono", "Mismagius", heal=False) and GetRelationshipRank("Cheren") < 2):
                    "You're not going to run from a battle in front of Cheren. No way."
                elif (HasEvent("Professor Rowan", "RowanBattle") and HasEvent("Professor Rowan", "RunEvents")):
                    "No! There's no running from a trainer battle!\n{w=3.0}Unless you have a {i}really{/i} good reason!"
                    $ Fled = True
                    jump endbattle
                else:
                    "No! There's no running from a trainer battle!"
                hide screen battleui
                jump ChooseStart 
            elif (battleCommand == 'ascend'):
                $ ShowBattleUI()
                $ AutoWin = True
                jump endbattle
            elif (battleCommand == 'back'):
                python:
                    for i in range(min(len(CurrentActions), 1 + extrarollback)):
                        removeditem = CurrentActions.pop()
                        if (removeditem.GetActionType() == ActionTypes.Pokemon):
                            SwappingInMon.remove(removeditem.GetTargets()[0])
                jump ChooseStart

        else:
            $ extrarollback += 1

        $ BattlerIndex += 1

    python:
        for mon in PlayerBattlers():
            if (mon.HasStatus("diveralized") or mon.HasStatus("mega evolved") or mon.HasStatus("minigigamaxed")):
                GimmickCost -= 1

    label enemydecisions:

    python:
        #FIX THIS: this is the opponent's logic. Beef this up.
        for mon in EnemyBattlers():
            #THIS IS WHERE TETRA ELEMENT IS CALCULATED
            if (mon.GetId() == pokedexlookupname("Eevee", DexMacros.Id) and mon.HasAbility("Tetra Element", False)):
                calcs = CalculateTetraElement(mon)
                if (calcs != None):
                    mon.HasAbility("Tetra Element")
                    renpy.say(None, "Energy is gathering around Blue's Eevee! It's changing form!")
                    mon.ChangeForme(calcs)

            validmoves = GetValidMoves(mon)

            skipenemychoices = False
            for status, move_names in movestatuses.items():
                if mon.HasStatus(status):
                    lastmove = GetLastMove(ActionLog, mon, lookformoves=move_names, returnaction=True)
                    if (lastmove != None):
                        skipenemychoices = True
                        lasttarget = lastmove.GetTargets()[0]
                        if lasttarget not in Battlers():
                            lasttarget = GetTargets(mon, GetMoveRange(lastmove.Move), True)[min(len(GetTargets(mon, GetMoveRange(lastmove.Move), True)) - 1, lastmove.GetTargetSlots()[0])]
                        newmove = GetMove(lastmove.Move.Name)
                        if (lastmove.Move.Name in mon.GetMoveNames()):
                            newmove = lastmove.Move

                        CurrentActions.append(Action(0, mon.GetStat(Stats.Speed), ActionTypes.Move, mon.GetTrainer(), mon, newmove, [lasttarget.GetTrainer()], [lasttarget], Turn))

            if (not mon.HasStatus("recharging") and not skipenemychoices):
                if (custombrain == None or custombrain(mon) == None):
                    besttarget = -1
                    if (mon.GetIntelligence() == 0 and not testbattle):
                        movechosen = random.choice(validmoves)
                    else:
                        bestactions = RankTargets(mon)
                        besttarget = bestactions[0][0]
                        movechosen = bestactions[0][1]
                    
                    moverange = GetMoveRange(movechosen)
                    targets = GetTargets(mon, moverange, True)
                    
                    if (not (moverange == Range.AllAdjacentFoes
                        or moverange == Range.AllAdjacent
                        or moverange == Range.AllAllies 
                        or moverange == Range.AllFoes
                        or moverange == Range.All
                        or moverange == Range.AllAlliesAndSelf
                        or len(targets) == 0)):
                            if (besttarget != -1):
                                targets = [besttarget]
                            else:
                                targets = [random.choice(targets)]

                    CurrentActions.append(Action(0, mon.GetStat(Stats.Speed), ActionTypes.Move, mon.GetTrainer(), mon, movechosen, GetTrainers(targets), targets, Turn))

                else:
                    # Generates a tuple with the move's string, and a list of the targets' objects
                    # if custombrain=calembrain1() returns a third element called custom_action on top
                    brainresults = custombrain(mon)
                    custom_action = ""
                    movechosen = mon.GetMoveByName(brainresults[0])
                    targets = brainresults[1]
                    if (len(brainresults) == 3):
                        custom_action = brainresults[2]
                        if (custom_action == "Calem Flabébé's shenanigans"):
                            movechosen = brainresults[0]
                            renpy.say(None, f"{movechosen}")

                    if(custom_action == ""):# Do the regular actions for Moves or Items 
                        if (movechosen == None):# This is an item
                            CurrentActions.append(Action(6, mon.GetStat(Stats.Speed), ActionTypes.Bag, mon.GetTrainer(), mon, brainresults[0], GetTrainers(targets), targets, Turn))
                        elif (movechosen not in GetValidMoves(mon)):
                            movechosen = random.choice(GetValidMoves(mon))
                            moverange = GetMoveRange(movechosen)
                            targets = GetTargets(mon, moverange, True)

                            if (not (moverange == Range.AllAdjacentFoes
                                or moverange == Range.AllAdjacent
                                or moverange == Range.AllAllies 
                                or moverange == Range.AllFoes
                                or moverange == Range.All
                                or moverange == Range.AllAlliesAndSelf
                                or len(targets) == 0)):
                                    targets = [random.choice(targets)]

                        if (movechosen != None):

                            CurrentActions.append(Action(0, mon.GetStat(Stats.Speed), ActionTypes.Move, mon.GetTrainer(), mon, movechosen, GetTrainers(targets), targets, Turn))


        if (eb() != None and eb().HasAbility("Thrice Denied")):
            counted = 0
            for action in CurrentActions:
                if (action.GetUser() == eb()):
                    if (counted == 0):
                        action.SetPriority(1)
                    elif (counted == 2):
                        action.SetPriority(-1)
                    counted += 1
            if (counted < 3):
                renpy.jump("enemydecisions")

        roundsadjusted = False
        quickdrawactivating = False
        for action in CurrentActions:
            if (action.GetActionType() == ActionTypes.Move):
                moveselected = action.GetMove()
                user = action.GetUser()
                moveboosts = []
                for fvl in user.GetForeverals():
                    if (lookupforeveraldata(fvl, FVLMacros.FVLType) == ForeveralTypes.MoveBoost):
                        for newmove in lookupforeveraldata(fvl, FVLMacros.FVLTypeData):
                            moveboosts.append(newmove)
                action.ChangePriority(RunItemFunction("prioritizingMoves", user, []))
                if (moveselected.Name == "Metal Burst"):
                    user.ApplyStatus(".metalbursting", None)
                elif (moveselected.Name == "Shell Trap"):
                    user.ApplyStatus(".shelltrapping", None)

                if (user.HasAbility("Stall", False)):
                    action.ChangePriority(-0.03)
                if (random.random() <= .3 and user.HasAbility("Quick Draw", False) and moveselected.Category != "Status"):
                    quickdrawactivating = True
                    action.ChangePriority(0.05)
                if (moveselected.Category == "Status" and user.HasAbility("Prankster", False)):
                    action.ChangePriority(1)
                    user.ApplyStatus("pranking")
                if (IsHealingMove(moveselected.Name) and user.HasAbility("Triage", False)):
                    action.ChangePriority(3)
                if (moveselected.Type == "Flying" and user.GetHealthPercentage() >= 1.0 and user.HasAbility("Gale Wings", False)):
                    action.ChangePriority(1)
                if (moveselected.Name in ["Magic Room", "Wonder Room", "Trick Room"]):
                    action.ChangePriority(-7)
                elif (moveselected.Name in ["Whirlwind", "Roar", "Teleport", "Dragon Tail", "Circle Throw"]):
                    action.ChangePriority(-6)
                elif (moveselected.Name in ["Counter", "Mirror Coat"]):
                    action.ChangePriority(-5)
                    if (moveselected.Name == "Counter"):
                        user.ApplyStatus(".countering", None)
                    else:
                        user.ApplyStatus(".mirrorcoat", None)
                elif (moveselected.Name == "Shell Smash" and "Shell Smash" in moveboosts):
                    action.ChangePriority(-4)
                elif (moveselected.Name in ["Revenge", "Avalanche"]):
                    action.ChangePriority(-4)
                elif (moveselected.Name in ["Focus Punch", "Shell Trap"]):
                    action.ChangePriority(-3)
                elif (moveselected.Name in ["Slow Freeze", "Vital Throw"]):
                    action.ChangePriority(-1)
                elif (moveselected.Name in ["Bullet Punch", "Quick Attack", "Bide", "Baby-Doll Eyes", "Ice Shard", "Vacuum Wave", "Shadow Sneak", "Water Shuriken", "Legacy", "Mach Punch", "Disabling Poke", "Accelerock", "Sucker Punch", "Aqua Jet", "Ion Deluge"]):
                    action.ChangePriority(1)
                elif (moveselected.Name in ["Rage Powder", "Follow Me", "Feint", "First Impression", "Extreme Speed", "Ally Switch", "Zippy Zap"]):
                    action.ChangePriority(2)
                elif (moveselected.Name in ["Fake Out", "Wide Guard", "Quick Guard"]):
                    action.ChangePriority(3)
                elif (moveselected.Name in ["Snatch", "Endure", "Protect", "Obstruct", "Detect", "Enshroud", "Splinter Shield", "Deathless", "Silk Trap", "Baneful Bunker", "Magic Coat", "Spiky Shield", "Crafty Shield"]):
                    action.ChangePriority(4)
                elif (moveselected.Name in ["Helping Hand"]):
                    action.ChangePriority(5)
                elif (moveselected.Name == "Pursuit"):
                    user.ApplyStatus("pursuing")
                    targetswitching = False
                    for foeaction in CurrentActions:
                        if (foeaction.GetActionType() == ActionTypes.Pokemon and foeaction.GetUser() in action.GetTargets()):
                            action.SetPriority(7)
                        elif (foeaction.GetActionType() == ActionTypes.Move and foeaction.GetMove() != None and not (isinstance(foeaction.GetMove(), str) or isinstance(foeaction.GetMove(), int)) and foeaction.GetMove().Name in ["U-turn", "Flip Turn", "Parting Shot", "Volt Switch"]):
                            action.SetPriority(foeaction.GetPriority())
                            action.SetSpeed(foeaction.GetSpeed() + 1)
                elif (moveselected.Name == "Round" and not roundsadjusted):
                    roundsadjusted = True
                    firstround = -1
                    for action in CurrentActions:
                        if (action.GetActionType() == ActionTypes.Move and action.GetMove().Name == "Round"):
                            if (firstround == -1):
                                action.ChangePriority(0.01)
                                firstround = CurrentActions.index(action)
                            else:
                                action.SetSpeed(CurrentActions[firstround].GetSpeed() + action.GetSpeed() / 1000.0)
                elif (moveselected.Name == "Liberage"):
                    action.ChangePriority(1776)#AMMMMMMMEEEEERICCCCAAAA!

        CurrentActions.sort(key=(lambda entry : (-entry.GetPriority(), (-1 if BattlefieldExists("Trick Room") else 1) * -entry.GetSpeed() + random.random() / 1000)))

    python:
        currentactionindex = 0
        for action in CurrentActions:
            if (action.GetUser().GetAbilityChanged()):
                text = ReactivateAbility(action.GetUser())
                if (text != ""):
                    renpy.show_screen("battleui")
                    renpy.say(None, text)
        if (dialogfunc != None):
            dialogfunc("PreStep")

    label preCurrentActions:

    python:
        currentAction = CurrentActions[currentactionindex]
        actionsuccess = PerformAction(currentAction)
        BattleCheck()
        ActionLog.append(currentAction)

    if (dungeon != None and actionsuccess and currentAction.GetUser().GetTrainerType() != TrainerType.Enemy):
        $ dungeon.DungeonPostTurn()
        $ BattleCheck()
        if (dialogfunc != None):
            $ dialogfunc("PostDungeonEvent")

    if (currentactionindex < len(CurrentActions) - 1):
        $ currentactionindex += 1
        jump preCurrentActions

    python:
        CurrentActions = []
        DoEffects()
        BattleCheck()
        DoBattlefieldEffects()
        BattleCheck()
        Turn += 1
        if (dialogfunc != None):
            dialogfunc("PostTurn")
        if (dungeon != None):
            dungeon.DungeonPostRound()

        
label endbattle:

if (StopMusic):
    stop music fadeout 2.0
if (Fled):
    $ IsWinner = False
    $ wildcount = 0
    "You got away safely!"
else:
    $ IsWinner = PlayerWon()

    if (IsWinner):
        if (WildBattle):
            $ wildcount += 1
        
        if (usingliberationlimit and not WildBattle and not isgame and pikachuobj in FriendlyPokemon()):
            $ maxliberationlimit += 1
            "You win! Pikachu's Liberation Limit increased by one!"
        else:
            if (dungeon == None):
                "You win!"
            else:
                "You quickly take the stairs to the next floor!"
    else:
        "You lose!"
        $ wildcount = 0

        if (WildBattle and not isgame):
            $ moneylost = math.floor(money / 10.0)
            $ money -= moneylost
            
            "You lost $[moneylost] in your panicked escape!"
        
        else:
            if (GainExp and not isgame):
                python:
                    skiprewards = False
                    enemytrainer = EnemyTrainers()[0].Name
                    if (enemytrainer in ["lenora", "blaine", "wallace", "ramos", "surge", "melony", "marshal", "koga", "bertha", "will", "burgh", "olivia", "fantina", "karen", "clair", "byron", "valerie", "winona"]):
                        enemylevel = EnemyPokemon()[0].GetLevel()
                        battlecode = enemytrainer + str(enemylevel)
                        if (battlecode in losttestbattles):
                            skiprewards = True
                        else:
                            losttestbattles.append(battlecode)

                if (not skiprewards):
                    "Because of the difficult battle, your team gained extra experience!"

                    if (pikachuobj in FriendlyPokemon() and not WildBattle and not isgame and usingliberationlimit):
                        $ maxliberationlimit += 3
                        "Pikachu's Liberation Limit increased by three!"

                    python:
                        bonusexperience = 0

                        highestlevel = 0
                        highestmon = None
                        for mon in PlayerPokemon():
                            if (mon.GetLevel() > highestlevel):
                                highestmon = mon
                                highestlevel = mon.GetLevel()

                        lowestlevel = 101
                        lowestmon = None
                        for mon in EnemyPokemon():
                            if (mon.GetLevel() < lowestlevel):
                                lowestmon = mon
                                lowestlevel = mon.GetLevel()
                        
                        bonusexperience = math.ceil(lowestmon.CalculateGivingExperience(highestmon) * 3.0)

                        for trainer in Trainers:
                            if (trainer.GetType() == TrainerType.Player):
                                explist = []
                                for mon in trainer.GetTeam():
                                    explist += mon.GainExperience(bonusexperience, True)
                                if (len(explist) > 0):
                                    renpy.say(None, " ".join(explist))
                                

                
                else:
                    "You think you and your Pokémon have learned everything you can from this level of battle..."

python: # berries and type gems won't be returned
    RecordTMTRMove(Item.BlankTR)
    RecordTMTRMove(Item.BlankTM)
    for trainer in Trainers:
        for mon in trainer.GetTeam():
            if not mon.HasItem(None) and not GetItemEntry(mon.GetItem())[ItemdexMacros.ReturnAfterBattle]:
                mon.TakeItem()

label losebattle:

hide screen battleui
hide screen battle
hide blank2
with Dissolve(0.5)

if (not renpy.get_screen("currentdate")):
    $ renpy.transition(dissolve)
    show screen currentdate

python:
    renpy.hide("rain")
    renpy.hide("snow")
    renpy.hide("blizzard")
    renpy.hide("sand")
    for mon in FriendlyPokemon() + EnemyPokemon():
        if (mon.GetCaught() > 0):
            mon.AdjustHealth(mon.GetCaught(), absolute=True)
            mon.ResetCaught()
        if (mon.GetStartingItem() != None and GetItemEntry(mon.GetStartingItem())[ItemdexMacros.ReturnAfterBattle]):
            mon.Item = mon.GetStartingItem()
        elif (mon.GetStartingItem() == None):
            mon.Item = None
        if (mon.HasStatus("mega evolved") or mon.HasStatus("minigigamaxed")):
            mon.ClearStatus("mega evolved")
            mon.ClearStatus("minigigamaxed")
            mon.ChangeForme(None, revert=True)
        if (mon.HasAbility("Schooling", False)):
            mon.ChangeForme(None, revert=True)
        if (mon.HasAbility("Shields Down", False)):
            mon.ChangeForme(None, revert=True)
        if (mon.HasAbility("Forecast", False)):
            mon.ChangeForme(None, revert=True)
        if (mon.HasAbility("Tetra Element", False)):
            mon.ChangeForme(None, revert=True)
        if (mon.HasAbility("Disguise", False)):
            mon.ClearStatus("busted disguise")
        mon.Untransform()
        if (mon.HasNormalStatus() and mon.HasAbility("Natural Cure")):
            mon.ClearStatus(None, all=True)
        else:
            mon.ClearStatus("volatiles", volatiles=True)
        if (not mon.HasItem(None)) and ItemHasTag(mon.GetItem(), "megastone"):
            mon.Item = None
    Turn = 0
    Trainers = []
    BattlefieldEffects.clear()
    FriendlyEffects.clear()
    EnemyEffects.clear()
    CurrentWeather = None
    inbattle = False
    if (dungeon == None):
        if (not betatesting()):
            renpy.block_rollback()
        renpy.suspend_rollback(False)
        _rollback = True

return IsWinner 

### Helper Functions ###
init python:
    def ApplyEffect(mon, effect, effectvalue, onfoe):
        effectdict = None
        words = "The opponent's"
        if (not onfoe):
            words = "The allied"

        if (mon.GetTrainerType() == TrainerType.Enemy):
            if (onfoe):
                effectdict = FriendlyEffects
            else:
                effectdict = EnemyEffects
        else:
            if (onfoe):
                effectdict = EnemyEffects
            else:
                effectdict = FriendlyEffects
        if (effect in effectdict):
            return "But it failed!"
        else:
            effectdict[effect] = effectvalue
            return "{} team came under the effect of {}!".format(words, effect)

    def ShowBattleUI():
        if (not renpy.get_screen("battlui")):
            renpy.show_screen("battleui")

    def BattleCheck():
        if (BattleOver()):
            renpy.jump("Start")

    def SwitchInEffects(mon, returntext=False, firstturn=False, preserveStats=False):
        returnmessage = ""
        mon.SetTurnSwitchedIn(Turn)
        if (not (firstturn or preserveStats or preserveAllStats or dungeon != None)):
            mon.ResetStatChanges()

        returnmessage += FormeChanges(mon)

        foreveralstab = False
        for fvl in mon.GetForeverals():
            if (lookupforeveraldata(fvl, FVLMacros.FVLType) == ForeveralTypes.TurnStartStatus):
                returnmessage += mon.GetNickname() + "'s wishes coalesced! The " + fvl + " activated! "
                for effect in lookupforeveraldata(fvl, FVLMacros.FVLTypeData):
                    returnmessage += mon.ApplyStatus(effect)

        returnmessage += ReactivateAbility(mon)

        if (mon.HasAbility("Curious Medicine")):
            for othermon in GetBattlers(mon):
                othermon.ResetStatChanges()

        if (EffectOnOwnField(mon, "healing wish") 
            and GetBattlers(mon).index(mon) == GetFieldEffects(mon)["healing wish"]
            and (mon.GetHealthPercentage() < 1 or mon.HasNormalStatus())):
            del GetFieldEffects(mon)["healing wish"]
            mon.AdjustHealth(mon.GetStat(Stats.Health))
            mon.ClearStatus(None, all=True)

        if (mon.HasStatus("badly poisoned")):
            mon.Status["badly poisoned"] = 1

        if (RunItemFunction("onSwitch", mon, [])):
            if (EffectOnOwnField(mon, "sticky web") and IsGrounded(mon)):
                returnmessage += "{} became tangled in the sticky webs! {}".format(mon.GetNickname(), mon.ChangeStats(Stats.Speed, -1))
            if (EffectOnOwnField(mon, "toxic spikes") and IsGrounded(mon)):
                if (mon.HasType("Poison")):
                    del GetFieldEffects(mon)["toxic spikes"]
                    returnmessage += "{} absorbed the toxic spikes!".format(mon.GetNickname())
                elif (GetFieldEffects(mon)["toxic spikes"] == 1):
                    returnmessage += "{} landed on the toxic spikes! {}" .format(mon.GetNickname(), mon.ApplyStatus("poisoned", 1, mon))
                elif (GetFieldEffects(mon)["toxic spikes"] == 2):
                    returnmessage += "{} landed on the toxic spikes! {}" .format(mon.GetNickname(), mon.ApplyStatus("badly poisoned", 1, mon))
            if (EffectOnOwnField(mon, "spikes") and IsGrounded(mon)):
                if (GetFieldEffects(mon)["spikes"] == 1):
                    mon.AdjustHealth(-mon.GetStat(Stats.Health) * 1/8.0)
                elif (GetFieldEffects(mon)["spikes"] == 2):
                    mon.AdjustHealth(-mon.GetStat(Stats.Health) * 1/6.0)
                elif (GetFieldEffects(mon)["spikes"] == 3):
                    mon.AdjustHealth(-mon.GetStat(Stats.Health) * 1/4.0)
                returnmessage += "{} landed on the spikes!".format(mon.GetNickname())
            if (EffectOnOwnField(mon, "stealthy rocks")):
                typebonus = 1.0
                for type in mon.GetTypes():                
                    typebonus *= GetEffectiveness("Rock", type)
                mon.AdjustHealth(-mon.GetStat(Stats.Health) * 0.125 * typebonus)
                returnmessage += "{} landed on the sharp rocks!".format(mon.GetNickname())
        returnmessage += ItemText

        for othermon in Battlers():
            if (othermon.HasStatus("wrapped") and othermon.GetStatusCount(".wrappedby") not in Battlers()):
                othermon.ClearStatus("wrapped")
            if (othermon.HasStatus("firespun") and othermon.GetStatusCount(".firespunby") not in Battlers()):
                othermon.ClearStatus("firespun")
            if (othermon.HasStatus("whirlpooled") and othermon.GetStatusCount(".whirlpooledby") not in Battlers()):
                othermon.ClearStatus("whirlpooled")
            if (othermon.HasStatus("bound") and othermon.GetStatusCount(".boundby") not in Battlers()):
                othermon.ClearStatus("bound")
            if (othermon.HasStatus("clamped") and othermon.GetStatusCount(".clampedby") not in Battlers()):
                othermon.ClearStatus("clamped")
            if (othermon.HasStatus("infested") and othermon.GetStatusCount(".infestedby") not in Battlers()):
                othermon.ClearStatus("infested")
            if (othermon.HasStatus("entombed") and othermon.GetStatusCount(".entombedby") not in Battlers()):
                othermon.ClearStatus("entombed")
            if (othermon.HasStatus("anchored") and othermon.GetStatusCount("anchored") not in Battlers()):
                othermon.ClearStatus("anchored")
            if (othermon.HasStatus("shackled") and othermon.GetStatusCount("shackled") not in Battlers()):
                othermon.ClearStatus("shackled")
            if (othermon.HasStatus("octolocked") and othermon.GetStatusCount("octolocked") not in Battlers()):
                othermon.ClearStatus("octolocked")

        if (returntext):
            return FormatText(returnmessage)
        elif (returnmessage != ""):
            renpy.say(None, FormatText(returnmessage))
        mon.PlayCry()

    def AdjustPokemon(mon):
        trainer = mon.GetTrainer()
        if (trainer.GetType() != TrainerType.Enemy):
            newstarters = trainer.GetTeam()[:trainer.GetNumber()]
            replacements = [newmon for newmon in trainer.GetUnfaintedTeam() if newmon not in FriendlyBattlers()]
            switched = False
            while (not switched and len(replacements) > 0):
                switchindex = renpy.call_screen("switch", trainer)
                if (switchindex == "back"):
                    renpy.say(None, "You must select a Pokémon!")
                elif (trainer.GetTeam()[switchindex].GetHealthPercentage() <= 0.0):
                    renpy.say(None, "That Pokémon cannot fight!")
                elif (trainer.GetTeam()[switchindex] in Battlers()):
                    renpy.say(None, "That Pokémon is already in battle!")
                else:
                    mon.Untransform()
                    switched = True
                    newmon = trainer.GetTeam()[switchindex]
                    trainer.ShiftTeam(trainer.GetTeam().index(mon), switchindex, True)
                    renpy.say(None, "{} switched out, and {} switched in!".format(mon.GetNickname(), newmon.GetNickname()))
                    if (dialogfunc != None):
                        dialogfunc("AllySwitch")
                    SwitchInEffects(newmon)
                replacements = [newmon for newmon in trainer.GetUnfaintedTeam() if newmon not in FriendlyBattlers()]
        else:
            newstarters = trainer.GetTeam()[:trainer.GetNumber()]
            for i, mon in enumerate(newstarters):
                replacements = [newmon for newmon in trainer.GetUnfaintedTeam() if newmon not in EnemyBattlers()]
                if (mon.GetHealth() <= 0 and len(replacements) > 0):
                    newmon = None
                    if (CustomSwitchBrain != None):
                        newmon = CustomSwitchBrain(trainer)
                    if (newmon == None):
                        newmon = random.choice(replacements)
                    trainer.ShiftTeam(i, trainer.GetTeam().index(newmon), True)
                    if (len(trainer.GetUnfaintedTeam()) >= trainer.GetNumber()):
                        mon.Untransform()
                        renpy.say(None, "{} switched out, and {} switched in!".format(mon.GetNickname(), newmon.GetNickname()))
                        if (dialogfunc != None):
                            dialogfunc("EnemySwitch")
                        SwitchInEffects(newmon)        

    def PerformAction(action):
        global Fled
        actionType = action.GetActionType()
        if (action.GetPerformed() or action.GetUser() != None and (action.GetUser().GetHealth() <= 0 or action.GetUser() not in Battlers())):
            action.ChangeSuccess(False)
            return False
        if (actionType == ActionTypes.Move):
            DoMove(action, action.GetUser(), action.GetMove(), action.GetTargets())

            if (dialogfunc != None):
                dialogfunc(["AfterMove", ("Ally" if action.GetUser().GetTrainerType() != TrainerType.Enemy else "Enemy")])

        elif (actionType == ActionTypes.Pokemon):
            swappingmon = action.GetUser()
            swappingmonslot = action.GetUserTrainer().GetTeam().index(swappingmon)
            partymon = action.GetTargets()[0]
            partymonslot = action.GetUserTrainer().GetTeam().index(partymon)
            if (CanSwitch(swappingmon, False)):
                action.GetUserTrainer().ShiftTeam(swappingmonslot, partymonslot)
                renpy.say(None, "{} switched in! ".format(partymon.GetNickname()) + SwitchInEffects(partymon, True))
                swappingmon.Untransform()
            else:
                renpy.say(None, "{} cannot switch out!".format(swappingmon.GetNickname()))

        elif (actionType == ActionTypes.Bag):
            UseBattleItem(action)

            if (dialogfunc != None):
                dialogfunc(["UseItem", ("Ally" if action.GetUser().GetTrainerType() != TrainerType.Enemy else "Enemy"), action.GetMove()])

        elif (actionType == ActionTypes.Run):
            opponentspeed = 0
            for mon in EnemyBattlers():
                opponentspeed += mon.GetStat(Stats.Speed)

            selfspeed = 0
            for mon in FriendlyBattlers():
                selfspeed += mon.GetStat(Stats.Speed)
            
            odds = selfspeed / opponentspeed * 0.5

            if (action.GetUser().HasAbility("Run Away") or activerepel != None or action.GetUser().HasType("Ghost")):
                odds = 1

            if (random.random() < odds):
                Fled = True
            else:
                renpy.say(None, "You failed to get away!")
        
        action.SetPerformed()

        return True

    def UseBattleItem(action):
        item = action.GetMove()
        if (not renpy.get_screen("battleui")):
            renpy.show_screen("battleui")
        if (action.GetUser().GetTrainerType() == TrainerType.Player):
            if (item in inventory.keys()):
                if not ItemHasCategory(item, "Poké Balls"):
                    if (ValidateItemUsage(item, action.GetTargets()[0])):
                        RunItemFunction("used", action.GetTargets()[0], [action.MoveOwners[0] if GetItemScope(item) == "Move" else None], item)
                        if (GetItemScope(item) == "None"):
                            renpy.say(None, "You used the {}!".format(GetItemName(item)))
                        else:
                            renpy.say(None, "You used the {} on {}!".format(GetItemName(item), action.GetTargets()[0].GetNickname() if GetItemScope(item) == "Pokemon" else action.MoveOwners[0].GetNickname()))
                    else:
                        renpy.say(None, "The {} had no effect!".format(GetItemName(item)))
                else:
                    RunItemFunction("used", action.GetTargets()[0], [canBeDitto], item)
                if (not ItemHasTag(item, "not consumed")):
                    LoseItem(item)

            else:
                preposition = "a"
                if (GetItemName(item)[0].lower() in ["a", "e", "i", "o", "u"]):
                    preposition += "n"
                renpy.say(None, "You don't have {} {} to use!".format(preposition, item))
        
        else:
            preposition = "a"
            if (GetItemName(item)[0].lower() in ["a", "e", "i", "o", "u"]):
                preposition += "n"
            if (ValidateItemUsage(item, action.GetTargets()[0])):
                RunItemFunction("used", action.GetTargets()[0], [action.MoveOwners[0] if GetItemScope(item) == "Move" else None], item)
                if (GetItemScope(item) == "None"):
                    renpy.say(None, "The foe used {} {}!".format(preposition, GetItemName(item)))
                else:
                    renpy.say(None, "The foe used {} {} on {}!".format(preposition, GetItemName(item), action.GetTargets()[0].GetNickname() if GetItemScope(item) == "Pokemon" else action.MoveOwners[0].GetNickname()))

    def DoDamage(user, move, target, overwritetype = None, iscrit=False, overwritepower=0, typebonus=1, fixeddamage=-1, sheerforcebonus=False, recklessbonus=False, atebonus=False, analyticbonus=False, parentalbond=False, contact=False):
        global ItemText
        global tookdamage

        damage = 0
        if (fixeddamage == -1):
            power = math.floor(move.Power if overwritepower == 0 else overwritepower)
            element = move.Type if overwritetype == None else overwritetype
            isSpecial = move.Category == "Special"
            
            atkStat = Stats.SpecialAttack if isSpecial else Stats.Attack
            atkStatVal = user.GetStat(atkStat, ignorenegative=iscrit)
            if (move.Name != "Foul Play"):
                if (user.GetStatChanges(atkStat) != 0 and target.HasAbility("Unaware")):
                    atkStatVal = user.GetStat(atkStat, ignorenegative=True, ignorepositive=True)
            else:
                atkStatVal = target.GetStat(atkStat, ignorenegative=iscrit)

            defStat = Stats.SpecialDefense if isSpecial else Stats.Defense
            if (move.Name in ["Psyshock", "Psystrike"]):
                defStat = Stats.Defense
            defStatVal = target.GetStat(defStat, ignorepositive=iscrit)
            if (target.GetStatChanges(defStat) != 0 and (user.HasAbility("Unaware") or move.Name in ["Chip Away", "Darkest Lariat"])):
                defStatVal = target.GetStat(defStat, ignorenegative=True, ignorepositive=True)

            foreveralstab = False
            for fvl in user.GetForeverals():
                if (element in lookupforeveraldata(fvl, FVLMacros.FVLTypeData)):
                    if (lookupforeveraldata(fvl, FVLMacros.FVLType) == ForeveralTypes.AddSTAB 
                        or user.GetId() == 25.2 and lookupforeveraldata(fvl, FVLMacros.FVLType) == ForeveralTypes.AddProficiency):
                        foreveralstab = True
                        break

            stabbonus = 1.5 if foreveralstab or user.HasType(element) or (user.GetTerastallized() != -1 and element == user.GetTeraType()) else 1.0
            stabbonus = 2.0 if (not user.IsTerad() and stabbonus == 1.5 and user.HasAbility("Adaptability")) or (user.IsTerad() and element == user.GetTeraType() and user.HasAbility("Adaptability")) else stabbonus
            stabbonus = 2.25 if (user.IsTerad() and user.HasAbility("Adaptability") and element == user.GetTeraType() and element in user.GetTypes(ignoreTera=True)) else stabbonus
            burnpenalty = 0.5 if (user.HasStatus("burned") and not isSpecial and not user.HasAbility("Guts")) else 1.0
            pursuitbonus = 2.0 if user.HasStatus("pursuing") else 1.0
            mudsportpenalty = 0.33 if element == "Electric" and BattlefieldExists("Mud Sport") else 1.0
            watersportpenalty = 0.33 if element == "Fire" and BattlefieldExists("Water Sport") else 1.0
            critbonus = 1.5 if iscrit else 1.0
            critbonus = 2.25 if iscrit and user.HasAbility("Sniper") else critbonus
            mistyterrainpenalty = 0.5 if element == "Dragon" and BattlefieldExists("Misty Terrain") and IsGrounded(target) else 1.0
            electricterrainbonus = 1.3 if element == "Electric" and BattlefieldExists("Electric Terrain") and IsGrounded(user) else 1.0
            grassyterrainbonus = 1.3 if element == "Grass" and BattlefieldExists("Grassy Terrain") and IsGrounded(user) else 1.0
            grassyterrainpenalty = 0.5 if move.Name in ["Magnitude", "Earthquake", "Bulldoze"] and BattlefieldExists("Grassy Terrain") and IsGrounded(target) else 1.0
            chargedbonus = 2.0 if element == "Electric" and user.HasStatus("charged") else 1.0
            steelworkerbonus = 1.5 if element == "Steel" and user.HasAbility("Steelworker") else 1.0
            ironfistbonus = 1.2 if IsPunchMove(move.Name) and user.HasAbility("Iron Fist") else 1.0
            sharpnessbonus = 1.5 if IsSliceMove(move.Name) and user.HasAbility("Sharpness") else 1.0
            blazebonus = 1.5 if element == "Fire" and user.GetHealthPercentage() <= 1.0/3.0 and user.HasAbility("Blaze") else 1.0
            torrentbonus = 1.5 if element == "Water" and user.GetHealthPercentage() <= 1.0/3.0 and user.HasAbility("Torrent") else 1.0
            overgrowbonus = 1.5 if element == "Grass" and user.GetHealthPercentage() <= 1.0/3.0 and user.HasAbility("Overgrow") else 1.0
            swarmbonus = 1.5 if element == "Bug" and user.GetHealthPercentage() <= 1.0/3.0 and user.HasAbility("Swarm") else 1.0
            tintedlensbonus = 2.0 if typebonus < 1 and user.HasAbility("Tinted Lens") else 1.0
            sheerforcebonus = 1.3 if sheerforcebonus and user.HasAbility("Sheer Force") else 1.0
            strongjawbonus = 1.5 if IsBiteMove(move.Name) and user.HasAbility("Strong Jaw") else 1.0
            recklessbonus = 1.2 if recklessbonus else 1.0
            flashfirebonus = 1.5 if element == "Fire" and user.HasStatus("aflame") and user.HasAbility("Flash Fire") else 1.0
            sandforcebonus = 1.3 if element in ["Rock", "Ground", "Steel"] and WeatherIs("sandstorm") and user.HasAbility("Sand Force") else 1.0
            thickfatpenalty = 0.5 if element in ["Ice", "Fire"] and target.HasAbility("Thick Fat") else 1.0
            defensecurlcombo = 2.0 if move.Name in ["Rollout", "Ice Ball"] and user.HasStatus(".curling") else 1.0
            technicianbonus = 1.5 if move.Power <= 60 and user.HasAbility("Technician") else 1.0
            stompbonus = 2.0 if move.Name in ["Stomp", "Body Slam", "Dragon Rush", "Steamroller", "Heat Crash", "Heavy Slam", "Flying Press", "Malicious Moonsault"] and target.HasStatus(".minimized") else 1.0
            helpinghandbonus = pow(1.5, user.GetStatusCount("helped"))
            dryskinbonus = 1.25 if element == "Fire" and target.HasAbility("Dry Skin") else 1.0
            screenspenalty = 0.67 if target.GetTrainer().Number >= 2 or (target.GetTrainerType() == TrainerType.Enemy and len(EnemyTrainers()) >= 2) or (target.GetTrainerType() != TrainerType.Enemy and len(FriendlyTrainers()) >= 2) else 0.5
            lightscreenpenalty = screenspenalty if isSpecial and EffectOnOwnField(target, "light screen") else 1.0
            reflectpenalty = screenspenalty if not isSpecial and EffectOnOwnField(target, "reflect") else 1.0
            auroraveilpenalty = screenspenalty if lightscreenpenalty + reflectpenalty == 2 and EffectOnOwnField(target, "aurora veil") else 1.0
            rivalrybonus = 1.25 if user.GetGender() == target.GetGender() and user.GetGender() != Genders.Unknown and user.HasAbility("Rivalry") else 1.0
            rivalrypenalty = 0.75 if user.GetGender() != target.GetGender() and user.GetGender() != Genders.Unknown and target.GetGender() != Genders.Unknown  and user.HasAbility("Rivalry") else 1.0
            sunbonus = 1.5 if WeatherIs("sunny") and element == "Fire" else 1.0
            sunpenalty = 0.5 if WeatherIs("sunny") and element == "Water" else 1.0
            rainbonus = 1.5 if WeatherIs("rainy") and element == "Water" else 1.0
            rainpenalty = 0.5 if WeatherIs("rainy") and element == "Fire" else 1.0
            toughclawsbonus = 1.3 if contact and user.HasAbility("Tough Claws") else 1.0
            atebonus = 1.2 if atebonus and user.HasAbility("Pixilate") else 1.0
            analyticbonus = 1.3 if analyticbonus and user.HasAbility("Analytic") else 1.0
            stakeoutbonus = 2.0 if target.GetTurnSwitchedIn() == Turn and user.HasAbility("Stakeout") else 1.0
            filterpenalty = 0.75 if typebonus > 1 and (target.HasAbility("Filter") or target.HasAbility("Solid Rock") or target.HasAbility("Prism Armor")) else 1.0
            punkrockbonus = 1.3 if IsSoundMove(move.Name) and user.HasAbility("Punk Rock") else 1.0
            punkrockpenalty = 0.5 if IsSoundMove(move.Name) and target.HasAbility("Punk Rock") else 1.0
            friendguardpenalty = 0.75 * GetFriendGuardCount(target)
            parentalbondpenalty = 0.25 if parentalbond else 1.0
            fluffypenalty = 0.5 if contact and target.HasAbility("Fluffy") else 1.0
            fluffybonus = 2.0 if element == "Fire" and target.HasAbility("Fluffy") else 1.0
            purifyingsaltpenalty = 0.5 if element == "Ghost" and target.HasAbility("Purifying Salt") else 1.0
            icescalespenalty = 0.5 if isSpecial and target.HasAbility("Ice Scales") else 1.0
            supremeoverlordbonus = user.GetStatusCount("reigning supreme") if user.GetStatusCount("reigning supreme") != 0 else 1.0
            waterbubblepenalty = 0.5 if element == "Fire" and target.HasAbility("Water Bubble") else 1.0
            waterbubblebonus = 2.0 if element == "Water" and user.HasAbility("Water Bubble") else 1.0
            vulnerablebonus = 2.0 if target.HasStatus("vulnerable") else 1.0
            powerspotbonus = 1.3 if AbilityOnOwnField(user, "Power Spot", True) else 1.0
            batterybonus = 1.3 if isSpecial and AbilityOnOwnField(user, "Battery", True) else 1.0
            steelyspiritbonus = pow(1.5, NumAbilityOnOwnField(user, "Steely Spirit")) if element == "Steel" else 1.0
            thricedeniedpenalty = 0.333 if target.HasAbility("Thrice Denied") else 1.0
            randomvariation = ((100 - random.randint(0,15))/100 if not LockLuck else 1.0)

            basepower = PokeRound(power * pursuitbonus * defensecurlcombo
                * rivalrybonus * rivalrypenalty
                * atebonus * ironfistbonus * recklessbonus
                * sheerforcebonus * sandforcebonus * analyticbonus * toughclawsbonus
                * punkrockbonus * technicianbonus * strongjawbonus * sharpnessbonus
                * dryskinbonus * helpinghandbonus * chargedbonus
                * mistyterrainpenalty * electricterrainbonus * grassyterrainbonus
                * watersportpenalty * mudsportpenalty 
                * supremeoverlordbonus * waterbubblebonus * powerspotbonus * batterybonus
                * steelyspiritbonus)
            
            basepower = RunItemFunction("usingMove", user, [move, basepower])

            atkStatVal = PokeRound(atkStatVal
                * overgrowbonus * blazebonus * torrentbonus * swarmbonus * flashfirebonus * steelworkerbonus
                * stakeoutbonus * thickfatpenalty * purifyingsaltpenalty)

            atkStatVal = 1 if atkStatVal < 1 else atkStatVal

            basedamage = math.floor(math.floor(math.floor(2.0 * user.GetLevel() / 5.0 + 2) * basepower * atkStatVal / defStatVal) / 50.0) + 2
            basedamage = PokeRound(basedamage * parentalbondpenalty)
            basedamage = PokeRound(basedamage * sunbonus * sunpenalty * rainbonus * rainpenalty)
            basedamage = PokeRound(basedamage * critbonus)
            basedamage = math.floor(basedamage * randomvariation)
            basedamage = PokeRound(basedamage * stabbonus)
            basedamage = math.floor(basedamage * typebonus)
            basedamage = PokeRound(basedamage * burnpenalty)
            basedamage = PokeRound(basedamage * waterbubblepenalty)
            basedamage = PokeRound(basedamage * thricedeniedpenalty)

            damage = PokeRound(basedamage
                * reflectpenalty * lightscreenpenalty * auroraveilpenalty
                * tintedlensbonus * fluffypenalty * filterpenalty * fluffybonus 
                * stompbonus * punkrockpenalty * icescalespenalty * vulnerablebonus)

            if (dungeon != None and user.GetTrainerType() == TrainerType.Ally):
                damage = PokeRound(damage * move.PP / move.MaxPP)

            damage = 1 if damage <= 0 else damage
        else:
            damage = fixeddamage

        if (target.HasStatus("substitute") and not IsSoundMove(move.Name) and not user.HasAbility("Infiltrator")):
            damage = min(damage, target.GetStatusCount("substitute"))
            if (target.GetStatusCount("substitute") > damage):
                target.ApplyStatus("substitute", target.GetStatusCount("substitute") - damage, target, True)
            else:
                target.ClearStatus("substitute")
        else:
            damage = min(damage, target.GetHealth())
            if (target in playerparty):
                tookdamage = True
            target.AdjustHealth(-damage, directdamage=True)

        if (dungeon != None and target.HasStatus("tyrannic") and typebonus > 1 and len(target.GetTrainer().GetUnfaintedTeam()) > 1):
            del target.GetTrainer().Team[1]

        #renpy.say(None, "//TESTING:{} used {} on {}, dealing {} damage!".format(user.GetNickname(), move.Name, target.GetNickname(), damage))
        return damage

    def BattleOver():
        global pokemonfainted

        if (Fled or AutoLose or AutoWin):
            return True

        maxnumber = 0
        for trainer in Trainers:
            if (trainer.GetNumber() > maxnumber):
                maxnumber = trainer.GetNumber()

        battletype = max(maxnumber, len(FriendlyTrainers()), len(EnemyTrainers()))
        partyleads = []
        for trainer in Trainers:
            partyleads += trainer.GetTeam()[:battletype]

        for mon in partyleads:
            if (mon.GetHealth() == 0 and not mon in FaintedMons):
                prefixexpgain = ""
                if (mon.GetCaught() > 0):
                    renpy.say(None, "{} was caught!".format(mon.GetNickname()))
                    if (mon != GetTrainerTeam("Brendan", "Sandshrew", False)):
                        renpy.transition(dissolve)
                        renpy.show_screen("mondata", mon)
                        mon.Nickname = renpy.input("Would you like to give it a nickname?", default=pokedexlookup(mon.GetId(), DexMacros.Name), exclude="{}[[]%<>", length=12)
                        renpy.transition(dissolve)
                        renpy.hide_screen("mondata")
                else:
                    mon.PlayCry()
                    if (mon in playerparty):
                        pokemonfainted = True
                    prefixexpgain = f"{mon.GetNickname()} fainted!"
                    if (mon.HasStatus('.keystone')):
                        for othermon in mon.GetTrainer().GetTeam():
                            othermon.Health = 0
                    if (not GainExp):
                        renpy.say(None, prefixexpgain)
                    if (dungeon != None):
                        dungeon.ChangeBad(3)
                        if (dungeon.GetLootList() != None and len(dungeon.GetLootList()) != 0):
                            item = WeightedRandomChoice(dungeon.GetLootList(False))
                            itemname = GetItemName(item)
                            preposition = ("an" if itemname[0].lower() in ["a", "e", "i", "o", "u"] else "a")
                            dungeon.RecordItemGet(item)
                            GetItem(item, count = 1, text = None, audio = False, hidefanfare=True)
                            prefixexpgain += f" It dropped {preposition} {itemname}!"
                    mon.GetTrainer().IncreaseFaintedPokemonCount()
                    mon.ChangeForme(None, revert=True)
                    mon.ClearStatus("", all=True)
                    mon.FaintedOnTurn = Turn
                    for allymon in GetBattlers(mon):
                        if (allymon.HasAbility("Power of Alchemy")):
                            allymon.ApplyStatus("alchemized", mon.GetAbility())
                FaintedMons.append(mon)
                mon.Untransform()
                if (GainExp):
                    if (mon.GetTrainerType() == TrainerType.Enemy):#if opponent faints...
                        splitmons = []
                        for othermon in PlayerPokemon():
                            if (othermon.HasItem(Item.ExperienceShare) and othermon not in PlayerBattlers() and othermon.GetHealthPercentage() > 0):
                                splitmons.append(othermon)
                        
                        exptext = []
                        for playermon in PlayerBattlers() + splitmons:#give experience to all playerbattlers
                            exptext += playermon.GainExperience(mon.CalculateGivingExperience(playermon) / (len(splitmons) + 1) * (playermon.GetTrainer().GetNumber() if playermon.HasItem(Item.ExperienceShare) else 1.0), prefix=([prefixexpgain] if prefixexpgain != "" else None))
                            prefixexpgain = ""
                        PrintExp(exptext)
                
                AdjustPokemon(mon)

        hasOne = False
        for mon in FriendlyPokemon():
            if (mon.GetHealth() > 0):
                hasOne = True
                break

        if (not hasOne):
            return True

        hasOne = False
        for mon in EnemyPokemon():
            if (mon.GetHealth() > 0):
                hasOne = True
                break

        if (not hasOne):
            if (dungeon != None and dungeon.Reinforcing):
                newpokemon = dungeon.AddNewDungeonPokemon()
                newtext = SwitchInEffects(newpokemon, True, False, True)
                renpy.say(None, "A wild {} appeared out of the Mysteriosity! {}".format(newpokemon.GetNickname(), newtext))
            else:
                return True
        
        return False

    def PlayerWon():
        if (AutoLose):
            return False
        if (AutoWin):
            return True
        for mon in FriendlyBattlers():
            if (mon.GetHealth() > 0):
                return True
        return False

    def ApplyWeather(weather, countdown, user=None):
        global CurrentWeather
        if (CurrentWeather != None and WeatherIs(weather) or AbilityOnField("Cloud Nine")):
            return "But it failed!"
        else:
            CurrentWeather = (weather, countdown if user == None else RunItemFunction("settingWeatherTerrain", user, [weather, countdown]))

            for mon in Battlers():
                if (mon.HasAbility("Forecast", triggersplash=False)):
                    FormeChanges(mon)

            renpy.hide("rain")
            renpy.hide("snow")
            renpy.hide("blizzard")
            renpy.hide("sand")
            if (not lowspecs):
                if (WeatherIs("rainy")):
                    renpy.show("rain", [thirtydegrees])
                elif (WeatherIs("snowy")):
                    renpy.show("snow")
                elif (WeatherIs("hailing")):
                    renpy.show("blizzard", [sixtydegrees])
                elif (WeatherIs("sandstorm")):
                    renpy.show("sand", [ninetydegrees])

            if (WeatherIs("sandstorm")):
                returnable = "A sandstorm whipped up!"
            elif (WeatherIs("hailing")):
                returnable = "It started to hail!"
            else:
                returnable = "The sky became {}!".format(weather)
            return returnable + ItemText

    def FormeChanges(user):
        returnable = ""
        if (user.GetId() != 555 and user.GetHealthPercentage() > 0.5 and user.HasAbility("Zen Mode")):
            returnable += user.ChangeForme("Darmanitan (Standard Mode)")
        elif (user.GetId() != 555.1 and user.GetHealthPercentage() <= 0.5 and user.HasAbility("Zen Mode")):
            returnable += user.ChangeForme("Darmanitan (Zen Mode)")
        elif (user.GetId() == 774 and user.GetHealthPercentage() <= 0.5 and user.HasAbility("Shields Down")):
            returnable += user.ChangeForme(user.GetMiniorForme())
        elif (user.GetId() == 774.1 and user.GetHealthPercentage() > 0.5 and user.HasAbility("Shields Down")):
            returnable += user.ChangeForme("Minior (Meteor Form)")
        elif (user.GetId() == 746 and user.Level >= 20 and user.GetHealthPercentage() > 0.25 and user.Image == None and user.HasAbility("Schooling")):
            returnable += user.ChangeForme("Wishiwashi (School Form)")
        elif (user.GetId() == 746 and user.Level >= 20 and user.GetHealthPercentage() <= 0.25 and user.Image != None and user.HasAbility("Schooling")):
            returnable += user.ChangeForme("Wishiwashi (Solo Form)")
        elif (user.GetId() in [351, 351.1, 351.2, 351.3] and user.HasAbility("Forecast", triggersplash=False)):
            if (WeatherIs("rainy") and user.GetId() != 351.2 and user.HasAbility("Forecast")):
                returnable += user.ChangeForme("Castform (Rainy Form)")
            elif (WeatherIs("sunny") and user.GetId() != 351.1 and user.HasAbility("Forecast")):
                returnable += user.ChangeForme("Castform (Sunny Form)")
            elif ((WeatherIs("hailing") or WeatherIs("snowy")) and user.GetId() != 351.3 and user.HasAbility("Forecast")):
                returnable += user.ChangeForme("Castform (Snowy Form)")
            elif (WeatherIs(None) and user.GetId() != 351 and user.HasAbility("Forecast")):
                returnable += user.ChangeForme("Castform (Normal)")
        elif (user.GetId() in [412, 412.1, 412.2]):
            if (GetCamoType() in ["Grass", "Bug"] and user.GetId() != 412):
                returnable += user.ChangeForme("Burmy (Plant Cloak)")
            elif (GetCamoType() in ["Steel", "Poison"] and user.GetId() != 412.2):
                returnable += user.ChangeForme("Burmy (Trash Cloak)")
            elif (GetCamoType() in ["Ground", "Rock"] and user.GetId() != 412.1):
                returnable += user.ChangeForme("Burmy (Sandy Cloak)")

        return returnable

    def DoEffects():# will do effects, and also increment them down, if applicable
        global ItemText
        
        decrementers = ["gasping", "snatching", "thrashing", "outraged", "the standout", "confused", "asleep", "wrapped", "flinching", "pursuing", "bound", 
            "taunted", "encored", "enduring", "deathless", "protected", "mind read", "locked on", ".lockingon", ".mindreading", ".baneful", ".enshrouded", 
            ".splintering", ".spiky", ".silked", "pranking", "disabled", "firespun", "whirlpooled", "uproaring", "drowsy", "entombed", "dug in", "airborne", 
            "ethereal", "electrified", "ionized", "embargoed", "laser focused", "levitating", "roosted", "perishing", "petal dancing", "coated in magic", 
            "clamped", "infested", "diving", "diveralized", "grudging", ".obstructing", "unhealthy", "recharging", "quashed"]            
        
        pickuped = False
        harvested = False
        for user in Battlers(True):
            returnable = ""

            for other in GetBattlers(user):
                for status in normalstatuses:
                    if (user != other and other.HasStatus(status) and abs(GetBattlers(user).index(user) - GetBattlers(user).index(other)) == 1 and random.random() <= 0.3 and user.HasAbility("Healer")):
                        returnable += other.GetNickname() + " was healed by " + user.GetNickname() + "!"
                        other.ClearStatus(status)
            
            if (user.HasStatus("frenzied") and not user.HasStatus("gorging") and user.HasAbility("Gulp Missile")):
                user.ClearStatus("gulping")
                returnable += user.ApplyStatus("gorging")

            if (user.HasAbility("Pickup", False) and user.HasItem(None) and not pickuped and not harvested):
                for othermon in Battlers():
                    if (othermon != user):
                        for action, item, turn in reversed(othermon.GetItemHistory()):
                            if (turn == Turn and action == "Used" and user.HasAbility("Pickup")):
                                pickuped = True
                                returnable += user.GiveItem(item)
                                break

            if (user.HasAbility("Harvest", False) and user.HasItem(None) and not pickuped and not harvested):
                for action, item, turn in reversed(user.GetItemHistory()):
                    if (IsBerry(item) and action == "Used" and (random.random() <= 0.5 or WeatherIs("sunny")) and user.HasAbility("Harvest")):
                        harvested = True
                        returnable += user.GiveItem(item, fromharvest = True)
                        break

            dellist = []
            for status in user.GetStatusKeys():
                if (status in normalstatuses and random.random() <= 1.0/3.0 and user.HasAbility("Shed Skin")):
                    returnable += "{}'s shed skin sloughed off!".format(user.GetNickname())
                    dellist.append(status)
                elif (status in normalstatuses and WeatherIs("rainy") and user.HasAbility("Hydration")):
                    dellist.append(status)

            if (user.HasStatus("asleep") and AbilityOnOpponentField(user, "Bad Dreams")):
                if (user.AdjustHealth(user.GetStat(Stats.Health) * -1.0/8.0)):
                    returnable += "{} is tormented by Bad Dreams!".format(user.GetNickname())

            for status in dellist:
                returnable += user.ClearStatus(status)

            if (user.HasStatus("aqua ring")):
                if (user.AdjustHealth(user.GetStat(Stats.Health) * 1.0/16.0)):
                    returnable += "{} is healed by the aqua ring!".format(user.GetNickname())
            if (user.HasStatus("ingrained")):
                if (user.AdjustHealth(user.GetStat(Stats.Health) * 1.0/16.0)):
                    returnable += "{} is healed by its roots!".format(user.GetNickname())
            if (user.HasStatus("salt cured")):
                if (user.HasType("Water") or user.HasType("Steel")):
                    if (user.AdjustHealth(user.GetStat(Stats.Health) * -1.0/4.0)):
                        returnable += "{} is direly hurt by its salt cure!".format(user.GetNickname())
                else:
                    if (user.AdjustHealth(user.GetStat(Stats.Health) * -1.0/8.0)):
                        returnable += "{} is hurt by its salt cure!".format(user.GetNickname())
            
            if (user.HasStatus(".wrappedby") and not user.HasStatus("wrapped")):
                user.ClearStatus(".wrappedby")
            if (user.HasStatus(".firespunby") and not user.HasStatus("firespun")):
                user.ClearStatus(".firespunby")
            if (user.HasStatus(".whirlpooledby") and not user.HasStatus("whirlpooled")):
                user.ClearStatus(".whirlpooledby")
            if (user.HasStatus(".boundby") and not user.HasStatus("bound")):
                user.ClearStatus(".boundby")
            if (user.HasStatus(".clampedby") and not user.HasStatus("clamped")):
                user.ClearStatus(".clampedby")
            if (user.HasStatus(".infestedby") and not user.HasStatus("infested")):
                user.ClearStatus(".infestedby")
            if (user.HasStatus(".entombedby") and not user.HasStatus("entombed")):
                user.ClearStatus(".entombedby")
            if (user.HasStatus(".octolockedby") and not user.HasStatus("octolocked")):
                user.ClearStatus(".octolockedby")

            if (EffectOnOwnField(user, "future sight")
                and user in GetBattlers(user)
                and GetBattlers(user).index(user) == GetFieldEffects(user)["future sight"][1]
                and Turn >= GetFieldEffects(user)["future sight"][0] + 2):
                moveuser = GetFieldEffects(user)["future sight"][2]
                del GetFieldEffects(user)["future sight"]
                newaction = Action(0, moveuser.GetStat(Stats.Speed, triggerAbilities=False), ActionTypes.Move, moveuser.GetTrainer(), moveuser, GetMove("Future Sight"), [user.GetTrainer()], [user], Turn)
                DoMove(newaction, moveuser, GetMove("Future Sight"), [user], alreadypretext="The vision came true!")

            if (user.GetTurnSwitchedIn() != Turn or JustSwitchedIn(ActionLog, user)):
                if (user.HasStatus("burned")):
                    if (user.AdjustHealth(user.GetStat(Stats.Health) * -1.0/16.0)):
                        returnable += "{} is hurt by its burn!".format(user.GetNickname())
                elif (user.HasStatus("poisoned")):
                    if (user.HasAbility("Poison Heal")):
                        if (user.AdjustHealth(user.GetStat(Stats.Health) * 1.0/8.0)):
                            returnable += "{} is healed by poison!".format(user.GetNickname())
                    else:
                        if (user.AdjustHealth(user.GetStat(Stats.Health) * -1.0/8.0)):
                            returnable += "{} is hurt by poison!".format(user.GetNickname())
                elif (user.HasStatus("badly poisoned")):
                    user.Status["badly poisoned"] = user.GetStatusCount("badly poisoned") + 1
                    if (user.HasAbility("Poison Heal")):
                        if (user.AdjustHealth(user.GetStat(Stats.Health) * 1.0/8.0)):
                            returnable += "{} is healed by its deadly poison!".format(user.GetNickname())
                    else:
                        if (user.AdjustHealth(user.GetStat(Stats.Health) * -user.GetStatusCount("badly poisoned")/16.0)):
                            returnable += "{} is hurt by its deadly poison!".format(user.GetNickname())
                if (user.HasStatus("wrapped")):
                    if (user.AdjustHealth(user.GetStat(Stats.Health) * -1.0/8.0)):
                        returnable += "{} is hurt by Wrap!".format(user.GetNickname())
                if (user.HasStatus("firespun")):
                    if (user.AdjustHealth(user.GetStat(Stats.Health) * -1.0/8.0)):
                        returnable += "{} is hurt by Fire Spin!".format(user.GetNickname())
                if (user.HasStatus("whirlpooled")):
                    if (user.AdjustHealth(user.GetStat(Stats.Health) * -1.0/8.0)):
                        returnable += "{} is hurt by Whirlpool!".format(user.GetNickname())
                if (user.HasStatus("entombed")):
                    if (user.AdjustHealth(user.GetStat(Stats.Health) * -1.0/8.0)):
                        returnable += "{} is hurt by Sand Tomb!".format(user.GetNickname())
                if (user.HasStatus("bound")):
                    if (user.AdjustHealth(user.GetStat(Stats.Health) * -1.0/8.0)):
                        returnable += "{} is hurt by Bind!".format(user.GetNickname())
                if (user.HasStatus("clamped")):
                    if (user.AdjustHealth(user.GetStat(Stats.Health) * -1.0/8.0)):
                        returnable += "{} is hurt by Clamp!".format(user.GetNickname())
                if (user.HasStatus("infested")):
                    if (user.AdjustHealth(user.GetStat(Stats.Health) * -1.0/8.0)):
                        returnable += "{} is hurt by Infestation!".format(user.GetNickname())
                if (user.HasStatus("cursed")):
                    if (user.AdjustHealth(user.GetStat(Stats.Health) * -1.0/4.0)):
                        returnable += "{} is hurt by the curse!".format(user.GetNickname())
                if (user.HasStatus("nightmarish")):
                    if (user.AdjustHealth(user.GetStat(Stats.Health) * -1.0/4.0)):
                        returnable += "{} dreams of cacotopia...".format(user.GetNickname())
                if (user.HasStatus("octolocked")):
                    returnable += "{} is stuck in the Octolock!".format(user.GetNickname())
                    returnable += user.ChangeStats(Stats.Defense, -1, user.GetStatusCount(".octolockedby"))
                    returnable += user.ChangeStats(Stats.SpecialDefense, -1, user.GetStatusCount(".octolockedby"))
                
                RunItemFunction("endOfTurn", user, [])
            
            returnable += ItemText

            ItemText = ""

            if (user.HasStatus("seeded")):# in this case, target is the seeder, and user is the one who is seeded
                target = user.GetStatusCount("seeded")[1]#seeded's count is a tuple, (slotint, obj)
                oldtarget = target
                if (target not in Battlers()):
                    possibletargets = GetTargets(user, Range.Any, target.GetTrainerType() != user.GetTrainerType())
                    numtargets = len(possibletargets)
                    if (numtargets != 0):
                        target = possibletargets[min(user.GetStatusCount("seeded")[0], numtargets - 1)]
                        user.ApplyStatus("seeded", (user.GetStatusCount("seeded")[0], target), applier=oldtarget, overwrite=True)
                    else:
                        target = None
                if (target != None):
                    damage = user.GetStat(Stats.Health) * -1.0/8.0
                    if (user.AdjustHealth(damage)):
                        returnable += "{} is hurt by Leech Seed!".format(user.GetNickname())
                        if (target.AdjustHealth(-damage)):
                            returnable += "{} recovered health!".format(target.GetNickname())
           
            if (user.HasStatus("charged")):
                lastmove = GetLastMove(ActionLog, user, returnnonemoves=["Charge", "Energize"])
                if (lastmove != None and lastmove.Type == "Electric"):
                    user.ClearStatus("charged")
            if (user.HasStatus("rollout") and not user.HasStatus(".usedrollout")):
                user.ClearStatus("rollout")
            if (user.HasStatus("ice ball") and not user.HasStatus(".usediceball")):
                user.ClearStatus("ice ball")
            if (user.HasStatus("biding")):
                user.ApplyStatus("biding", user.GetStatusCount("biding") + 1, overwrite=True)
            else:
                user.ClearStatus(".bidingdamage")

            user.ClearStatus(".usedrollout")
            user.ClearStatus(".usediceball")
            dellist = []
            for status in user.GetStatusKeys():
                if (status in decrementers):
                    returnable += user.DecrementStatus(status)
                    if (user.GetStatusCount(status) <= 0):
                        dellist.append(status)
            for status in dellist:
                if (status not in ["confused", "asleep"]):
                    if (status == "perishing"):
                        user.AdjustHealth(0, absolute=True)
                        returnable += "{} succumbed to the perish song!".format(user.GetNickname())
                    if (status == "petal dancing"):
                        returnable += user.ApplyStatus("confused", random.randint(2, 5))
                    user.ClearStatus(status)

            if (user.HasStatus("helped")):
                user.ClearStatus("helped")

            if ("drowsy" in dellist):
                returnable += user.ApplyStatus("asleep", random.randint(1, 3))

            if (user.HasStatus(".disabling") and not user.HasStatus("disabled")):
                user.ClearStatus(".disabling")

            if (user.GetTurnSwitchedIn() != Turn or JustSwitchedIn(ActionLog, user)):
                if (user.HasAbility("Moody") or user.HasStatus(".moody") or user.HasStatus("winging it")):
                    returnable += ActivateMoody(user)
                if (user.HasAbility("Speed Boost")):
                    returnable += user.ChangeStats(Stats.Speed, 1, user)

            returnable += FormeChanges(user)

            if (returnable != ""):
                renpy.say(None, FormatText(returnable))

    def ApplyBattlefieldEffects(effect, count, overwrite=False, user=None):
        global BattlefieldEffects
        if (not overwrite and BattlefieldExists(effect)):
            return "But it failed!"
        else:
            if ("Terrain" in effect or effect == "Burial Ground"):
                if (BattlefieldExists("Misty Terrain")):
                    del BattlefieldEffects["Misty Terrain"]
                elif (BattlefieldExists("Electric Terrain")):
                    del BattlefieldEffects["Electric Terrain"]
                elif (BattlefieldExists("Grassy Terrain")):
                    del BattlefieldEffects["Grassy Terrain"]
                elif (BattlefieldExists("Burial Ground")):
                    del BattlefieldEffects["Burial Ground"]
                elif (BattlefieldExists("Psychic Terrain")):
                    del BattlefieldEffects["Psychic Terrain"]
            if user != None:
                BattlefieldEffects[effect] = RunItemFunction("settingWeatherTerrain", user, [effect, count])
            else:
                BattlefieldEffects[effect] = count
            return "The battlefield is under the effect of {}!".format(effect)

    def DoBattlefieldEffects():# will do effects, and also increment them down, if applicable
        global UsedEchoedVoice
        global BattlefieldEffects
        global CurrentWeather
        if (UsedEchoedVoice):
            if (BattlefieldExists("Echoed Voice")):
                ApplyBattlefieldEffects("Echoed Voice", min(BattlefieldEffects["Echoed Voice"] + 40, 200), True)
            else:
                ApplyBattlefieldEffects("Echoed Voice", 80)
        else:
            if (BattlefieldExists("Echoed Voice")):
                del BattlefieldEffects["Echoed Voice"]

        decrementers = ["Mud Sport", "Gravity", "Misty Terrain", "Water Sport", "Burial Ground", "Simple World", "Electric Terrain", "Grassy Terrain"]
        becopy = BattlefieldEffects.copy()

        for effect in becopy.keys():
            if (effect in decrementers):
                BattlefieldEffects[effect] -= 1
                if (BattlefieldEffects[effect] <= 0):
                    del BattlefieldEffects[effect]

        decrementers = ["mist", "lucky", "wide guard", "tailwind", "quick guard", "reflect", "aurora veil", "light screen", "safeguard", "crafty shield"]
        fecopy = FriendlyEffects.copy()
        for effect in fecopy.keys():
            if (effect in decrementers):
                FriendlyEffects[effect] -= 1
                if (FriendlyEffects[effect] <= 0):
                    del FriendlyEffects[effect]

        if ("wishing star" in FriendlyEffects.keys()):
            if (FriendlyEffects["wishing star"][0] == 2):
                FriendlyEffects["wishing star"][0] = 1
            else:
                slot = FriendlyEffects["wishing star"][1]
                healamount = FriendlyEffects["wishing star"][2]
                if (len(FriendlyBattlers()) > slot):
                    FriendlyBattlers()[slot].AdjustHealth(healamount)
                    renpy.say(None, "The wish came true!")
                    del FriendlyEffects["wishing star"]

        eecopy = EnemyEffects.copy()
        for effect in eecopy.keys():
            if (effect in decrementers):
                EnemyEffects[effect] -= 1
                if (EnemyEffects[effect] <= 0):
                    del EnemyEffects[effect]

        if ("wishing star" in EnemyEffects.keys()):
            if (EnemyEffects["wishing star"][0] == 2):
                EnemyEffects["wishing star"][0] = 1
            else:
                slot = EnemyEffects["wishing star"][1]
                healamount = EnemyEffects["wishing star"][2]
                if (len(EnemyBattlers()) > slot):
                    EnemyBattlers()[slot].AdjustHealth(healamount)
                    renpy.say(None, "The wish came true!")
                    del EnemyEffects["wishing star"]

        if ("Burial Ground" in BattlefieldEffects.keys()):
            for mon in Battlers(True):
                if (IsGrounded(mon) and not (mon.HasType("Ground") or mon.HasType("Ghost"))):
                    mon.AdjustHealth(mon.GetStat(Stats.Health) * -1.0/16.0)
                    mon.ChangeStats(Stats.Speed, -1)
                    renpy.say(None, "The Burial Ground draws {} in!".format(mon.GetNickname()))
        elif ("Grassy Terrain" in BattlefieldEffects.keys()):
            for mon in Battlers(True):
                if (IsGrounded(mon)):
                    mon.AdjustHealth(mon.GetStat(Stats.Health) * 1.0/16.0)
            renpy.say(None, "The Grassy Terrain heals all!")

        if (CurrentWeather != None):
            weather = CurrentWeather[0]
            weathercount = CurrentWeather[1]

            if (WeatherIs("sandstorm", True)):
                if (weathercount != 0):
                    weathercount -= 1
                    if (WeatherIs("sandstorm")):
                        renpy.say(None, "The sandstorm rages!")
                        for mon in Battlers(True):
                            if (not ("Steel" in mon.GetTypes() or "Rock" in mon.GetTypes() or "Ground" in mon.GetTypes() or mon.HasAbility("Overcoat") or mon.HasAbility("Sand Force") or mon.HasAbility("Sand Rush") or mon.HasAbility("Sand Veil") or RunItemFunction("blockEffect", mon, ["weather"]))):
                                if (mon.AdjustHealth(mon.GetStat(Stats.Health) * -1.0/16.0)):
                                    renpy.say(None, "{} is buffeted by the sandstorm!".format(mon.GetNickname()))
                                BattleCheck()
                    CurrentWeather = (weather, weathercount)

                else:
                    renpy.say(None, "The sandstorm calmed...")
                    CurrentWeather = None
                    renpy.hide("sand")

            elif (WeatherIs("sunny", True)):
                if (weathercount != 0):
                    weathercount -= 1
                    if (WeatherIs("sunny")):
                        for mon in Battlers(True):
                            if (mon.HasAbility("Solar Power") or mon.HasAbility("Dry Skin")):
                                mon.AdjustHealth(-mon.GetStat(Stats.Health) / 8.0)
                    CurrentWeather = (weather, weathercount)

                else:
                    renpy.say(None, "The sunlight faded...")
                    CurrentWeather = None

            elif (WeatherIs("rainy", True)):
                if (weathercount != 0):
                    weathercount -= 1
                    if (WeatherIs("rainy")):
                        for mon in Battlers(True):
                            if (mon.HasAbility("Dry Skin")):
                                mon.AdjustHealth(mon.GetStat(Stats.Health) / 8.0)
                            elif (mon.HasAbility("Rain Dish")):
                                mon.AdjustHealth(mon.GetStat(Stats.Health) / 16.0)
                    CurrentWeather = (weather, weathercount)

                else:
                    renpy.say(None, "The rainclouds dissipated...")
                    CurrentWeather = None
                    renpy.hide("rain")

            elif (WeatherIs("hailing", True)):
                if (weathercount != 0):
                    weathercount -= 1
                    if (WeatherIs("hailing")):
                        renpy.say(None, "The hail falls!")
                        for mon in Battlers(True):
                            if (not ("Ice" in mon.GetTypes() or mon.HasAbility("Overcoat") or mon.HasAbility("Ice Body") or mon.HasAbility("Snow Cloak") or RunItemFunction("blockEffect", mon, ["weather"]))):
                                if (mon.AdjustHealth(mon.GetStat(Stats.Health) / -16.0)):
                                    renpy.say(None, "{} is buffeted by the hail!".format(mon.GetNickname()))
                                BattleCheck()
                            elif (mon.HasAbility("Ice Body")):
                                mon.AdjustHealth(mon.GetStat(Stats.Health) / 16.0)
                    CurrentWeather = (weather, weathercount)

                else:
                    renpy.say(None, "The hail calmed...")
                    CurrentWeather = None
                    renpy.hide("blizzard")

            elif (WeatherIs("snowy", True)):
                if (weathercount != 0):
                    weathercount -= 1
                    if (WeatherIs("snowy")):
                        renpy.say(None, "The snow falls!")
                        for mon in Battlers(True):
                            if (mon.HasAbility("Ice Body")):
                                mon.AdjustHealth(mon.GetStat(Stats.Health) / 16.0)
                    CurrentWeather = (weather, weathercount)

                else:
                    renpy.say(None, "The snow dissipates...")
                    CurrentWeather = None
                    renpy.hide("snow")
