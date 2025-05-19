init 5 python:
    class Outcomes:
        Neutral = 0,
        Good = 1,
        Bad = 2,
        Nothing = 3

    class Dungeon:
        def __init__(self, 
            name = "Unhallowed Holt",#a string
            endname = "Haunted Depths",#a string
            backgrounds = {"Night" : "midnightforest", "Default": "eveningforest"},#a dictionary of timeofdays to check against. If the current timeofday is not listed, then the "Default" value is picked.
            music = ("audio/music/duskforest.ogg"),#a tuple that contains one or two elements. If it contains two, the first is nolooped, and the second is looped. if it contains one, then it's looped
            encounterpool = {# a dictionary encounterpool, in the same format as the ones for normal wildareas
                pokedexlookupname("Pumpkaboo", DexMacros.Id): 5,
                pokedexlookupname("Phantump", DexMacros.Id): 3,
                pokedexlookupname("Rowlet", DexMacros.Id): 1,
                pokedexlookupname("Shuppet", DexMacros.Id): 7,
                pokedexlookupname("Paras", DexMacros.Id): 10,
            },
            evopool = {},
            difficulty = 16,#an int, 1-100, indicating the dungeon's difficulty. Should be roughly equivalent to AimLevel()
            floors = 5,#the number of battles you need to win to go through the level
            floorlength = 5,#the number of turns a battle will last, at max, before you find the stairs
            levelrange = range(14, 19),#a level range, set up the same way as normal wildarea level ranges
            startingmysteriosity=10,#the base chance that mysteriosity happenings will occur
            startingferocity=10,#the base chance that bad things will happen
            startinggenerosity=50,#the base chance that good things will happen
            trainers=["Cheren", "Skyla", "Silver"],# the trainers you start this dungeon with, not counting red
            cutscenefunc=None,#the function that returns the cutscene labels you should jump to
            godmodder=None,#manually calls events and outcomes if certain conditions are met
            lootlist = {#the dictionary of loot that you should get from this
                Item.GimmighoulCoin : 20, 
                Item.RawstBerry : 10, 
                Item.OranBerry : 10, 
                Item.SitrusBerry : 5,  
                Item.OddKeystone : 1, 
                Item.SpellTag : 5, 
                Item.MiracleSeed : 5 }):
        
            self.Name = name
            self.EndName = endname
            self.Backgrounds = backgrounds
            self.Music = music
            self.EncounterPool = encounterpool
            self.EvoPool = evopool
            self.Difficulty = difficulty
            self.Floors = floors
            self.FloorLength = floorlength
            self.LevelRange = levelrange
            self.StartingMysteriosity = startingmysteriosity
            self.StartingFerocity = startingferocity
            self.StartingGenerosity = startinggenerosity
            self.Mysteriosity = startingmysteriosity
            self.Ferocity = startingferocity
            self.Generosity = startinggenerosity
            self.CutsceneFunc = cutscenefunc
            self.GodModder = godmodder
            self.LootList = lootlist
            self.RedTrainer = MakeRed()
            self.Trainers = [self.RedTrainer] + [MakeTrainer(trainername, TrainerType.Ally) for trainername in trainers]

            self.PermEvents = {}#stays with you for the entire dungeon. Most should only be allowed to trigger once
            self.FloorEvents = {}#reset on every floor
            self.CurrentFloor = 1#increases by one for every floor
            self.FoundStairs = False#reset on every floor
            self.LastOutcome = None#keeps track of the last outcome rolled
            self.LastEvent = None#keeps track of the last event rolled
            self.Progress = 0#keeps track of how much progress the player's made. At the end of every turn, it increments one. There's a progress/FloorLength chance at the end of every turn that the stairs will be found
            self.WindBlows = 0#the wind blowing counter. Starts at 0. When it reaches five, you get an auto-game over. You are eaten by a Grue.
            self.WasSetUp = False#set to true the first time that setup is run.
            self.EventHistory = []#a list used to keep track of conditions met in dungeon cutscenes
            self.Reinforcing = True#whether you should check for reinforcements at the end of the turn. Sometimes, you don't want to.

            self.ItemHistory = {}#keeps track of the items the player has gathered in this dungeon
            self.WealthGained = 0#keeps track of the sell value of all the items the player has gathered, to softly 'cap' it

        def GetCutscene(self, parameters):
            if self.CutsceneFunc != None:
                if (self.CutsceneFunc(parameters)):
                    return True
            return False

        def GetName(self):
            return self.Name

        def GetFloorLength(self):
            return self.FloorLength

        def SetUp(self):
            renpy.call("SetupDungeon", self)

        def GetMusic(self):
            return self.Music

        def GetBackground(self):
            for key, value in self.Backgrounds.items():
                if (timeOfDay == key):
                    return value
            return self.Backgrounds["Default"]

        def GetTrainers(self):
            trainerlist = copy.copy(self.Trainers)
            if (self.GetEventValue(BadEvent.IncapacitateAlly)):
                for trainer in self.GetEventValue(BadEvent.IncapacitateAlly):
                    trainerlist.remove(trainer)
                    if (trainer in Trainers):
                        Trainers.remove(trainer)
            return trainerlist

        def NumTrainers(self):
            return len(self.GetTrainers())

        def GetMysteriosity(self):
            return self.Mysteriosity

        def GetFerocity(self):
            return (self.Ferocity if self.GetEventValue(NeutralEvent.SwapVibes) == 0 else self.Generosity)

        def GetGenerosity(self):
            return (self.Generosity if self.GetEventValue(NeutralEvent.SwapVibes) == 0 else self.Ferocity)

        def GetEventChance(self):
            return str(self.GetMysteriosity()) + "%"

        def RollMystery(self):
            return RandInt(1, self.GetMysteriosity())

        def RollFeral(self):
            return RandInt(1, self.GetFerocity())

        def RollGenerous(self):
            return RandInt(1, self.GetGenerosity())

        def RollCoinFlip(self):
            generous = self.RollGenerous()
            feral = self.RollFeral()
            if (generous > feral):
                return (Outcomes.Good, "{color=#080}♥{b}luck bends toward you!{/b}{/color}")
            else:
                return (Outcomes.Bad, "{color=#800}♠{b}luck bends away from you!{/b}{/color}")

        def RecordLastOutcome(self, outcome):
            self.LastOutcome = outcome
            return self.GetLastOutcome()

        def GetGodmodderResult(self, parameters):
            if (self.GodModder != None and self.GodModder(parameters) != None):
                return self.GodModder(parameters)
            else:
                return None

        def RollOutcome(self):
            if (self.GetGodmodderResult("Outcome") != None):
                return self.GetGodmodderResult("Outcome")

            randint = RandInt(1, 100)
            mystery = self.GetMysteriosity()
            generous = self.GetGenerosity()
            feral = self.GetFerocity()
            
            teststring = "Rand Num: " + str(randint) + ", Mysteriosity: " + str(mystery) + ", Generosity: " + str(generous) + ", Ferocity: " + str(feral)

            if (randint > mystery):
                prnt("no outcome: " + teststring)
                return self.RecordLastOutcome(Outcomes.Nothing)
            else:
                totalval = generous + feral + mystery
                newrandint = RandInt(1, totalval)
                teststring = "rand num 2: " + str(newrandint) + ", " + teststring
                if (newrandint <= generous):
                    prnt("good: " + teststring)
                    return self.RecordLastOutcome(Outcomes.Good)
                elif (newrandint <= generous + feral):
                    prnt("bad: " + teststring)
                    return self.RecordLastOutcome(Outcomes.Bad)
                else:
                    prnt("neutral: " + teststring)
                    return self.RecordLastOutcome(Outcomes.Neutral)

        def GoodOdds(self):
            #if randint <= mystery (Assumed)
            #if randint <= generous
            #min(1.0, self.GetMysteriosity() / 100)#the odds that there's a mysteriosity flux in the first place (Assumed)
            #min(1.0, self.GetGenerosity() / (self.GetGenerosity() + self.GetFerocity() + self.GetMysteriosity()))#the odds that there's a generosity surge in the flux
            return round(100 * min(1.0, self.GetGenerosity() / (self.GetGenerosity() + self.GetFerocity() + self.GetMysteriosity())))

        def BadOdds(self):
            #if randint <= mystery (Assumed)
            #if randint > generous
            #if randint <= feral
            #min(1.0, self.GetMysteriosity() / 100)#the odds that there's a mysteriosity flux in the first place (Assumed)
            #1.0 - min(1.0, self.GetGenerosity() / (self.GetGenerosity() + self.GetFerocity() + self.GetMysteriosity()))#the odds that there's NOT a generosity surge in the flux
            #min(1.0, self.GetFerocity() / (self.GetGenerosity() + self.GetFerocity() + self.GetMysteriosity()))#the odds that there's a ferocity surge in the flux
            return round(100 * (1 - min(1.0, self.GetGenerosity() / (self.GetGenerosity() + self.GetFerocity() + self.GetMysteriosity()))) * min(1.0, self.GetFerocity() / (self.GetGenerosity() + self.GetFerocity() + self.GetMysteriosity())))

        def GetEncounterPool(self):
            return self.EncounterPool

        def GetLevelRange(self):
            return self.LevelRange

        def GetEvoPool(self):
            return self.EvoPool

        def GetLastOutcome(self):
            return self.LastOutcome

        def GetPermEvents(self):
            return self.PermEvents

        def AddPermEvent(self, key, value):
            self.PermEvents[key] = value

        def AddFloorEvent(self, key, value):
            self.FloorEvents[key] = value

        def GetFloorEvents(self):
            return self.FloorEvents

        def GetLastEvent(self):
            return self.LastEvent

        def RecordLastEvent(self, event):
            self.EventHistory.append(event)
            self.LastEvent = event
            return self.GetLastEvent()

        def PickEvent(self, outcome):
            if (self.GetGodmodderResult("Event") != None):
                return self.GetGodmodderResult("Event")

            options = []
            if (outcome == Outcomes.Neutral):
                options = NeutralEvents
            elif (outcome == Outcomes.Good):
                options = GoodEvents
            elif (outcome == Outcomes.Bad):
                options = BadEvents

            removepermkeys = copy.copy(set(self.GetPermEvents().keys()))
            if (BadEvent.LevelFoes in removepermkeys):#this should be repeatable
                removepermkeys.remove(BadEvent.LevelFoes)
            if (NeutralEvent.ChangeVibeChangeMagnitude in removepermkeys):#this should be repeatable
                removepermkeys.remove(NeutralEvent.ChangeVibeChangeMagnitude)
            removefloorkeys = self.GetFloorEvents().keys()

            keys_to_remove = removepermkeys.union(removefloorkeys)
            options = list(set(options) - keys_to_remove)
            return RandomChoice(options)

        def GetEventValue(self, key):
            if (key in self.GetFloorEvents()):
                return self.GetFloorEvents()[key]
            elif (key in self.GetPermEvents()):
                return self.GetPermEvents()[key]
            return 0

        def DungeonPostRound(self):
            if (self.GetEventValue(NeutralEvent.SwapVibes) != 0):
                self.AddPermEvent(NeutralEvent.SwapVibes, self.GetEventValue(NeutralEvent.SwapVibes) - 1)
            self.ChangeMystery(1)
            self.UpdateProgress(1)
            if (not self.IsBossFight() and self.GetProgress() >= self.GetFloorLength() / 2.0 and RandInt(1, self.GetFloorLength()) <= self.GetProgress() and not self.GetFoundStairs()):
                renpy.say(dn, "You have found the stairs!")
                self.FindStairs()
            elif (self.Reinforcing):
                returntext = ""
                reinforcements, reinforcementsstr = self.BadMagnitude(1, len(self.Trainers))
                for i in range(reinforcements):
                    newpokemon = self.AddNewDungeonPokemon()
                    returntext = returntext + " " + SwitchInEffects(newpokemon, True, False, True)
                renpy.say(dn, "{} {} {} appeared for the wild Pokémon! {}".format(reinforcementsstr, cp(reinforcements, "reinforcement"), ("has" if reinforcements == 1 else "have"), returntext))

        def GeneratePokemon(self):
            newpokemonnum = GrabFromEncounterPool(self.GetEncounterPool())
            upperbound = self.GetLevelRange()[-1]
            lowerbound = self.GetLevelRange()[0]
            randlevel, randlevelstr = self.BadMagnitude(lowerbound, upperbound) 
            randlevel += self.GetEventValue(BadEvent.LevelFoes)

            if (newpokemonnum in self.GetEvoPool()):
                evolevel, evoid = evopool[newpokemonnum]
                if (randlevel >= evolevel):#if the pokemon is at, or higher than, the level for evolution
                    newpokemonnum = evoid#change its id

            frenzynerf = None
            if (randlevel >= 3 + AimLevel()):
                frenzynerf = (AimLevel(), None) 

            return Pokemon(newpokemonnum, level = randlevel, shinylock=False, frenzynerf=frenzynerf)

        def AddNewDungeonPokemon(self):
            newpokemon = self.GeneratePokemon()
            for stat in range(Stats.Attack, Stats.Evasion + 1):
                newpokemon.ChangeStats(stat, self.GetEventValue(stat), newpokemon)
            trainerobj = (None if len(EnemyBattlers()) < 6 else RandomChoice(EnemyTrainers(omitdefeated=True)))
            AddNewWildPokemon(newpokemon, randslot = True, useoldtrainer = trainerobj)
            return newpokemon

        def ChangeVibe(self, vibe, valuechange):
            if (vibe in [Outcomes.Good, "Generosity"]):
                self.Generosity += valuechange * max(1, self.GetEventValue(NeutralEvent.ChangeVibeChangeMagnitude))
                self.Generosity = max(1, min(100, self.Generosity))
            elif (vibe in [Outcomes.Bad, "Ferocity"]):
                self.Ferocity += valuechange * max(1, self.GetEventValue(NeutralEvent.ChangeVibeChangeMagnitude))
                self.Ferocity = max(1, min(100, self.Ferocity))
            elif (vibe in [Outcomes.Neutral, "Mysteriosity"]):
                self.Mysteriosity += valuechange
                self.Mysteriosity = max(1, min(100, self.Mysteriosity))

        def ChangeBad(self, valuechange):
            self.ChangeVibe(Outcomes.Bad, valuechange)

        def ChangeGood(self, valuechange):
            self.ChangeVibe(Outcomes.Good, valuechange)

        def ChangeMystery(self, valuechange):
            self.ChangeVibe(Outcomes.Neutral, valuechange)

        def UpdateProgress(self, valuechange=1):
            self.Progress += valuechange

        def ResetProgress(self):
            self.Progress = 0

        def GetProgress(self):
            return self.Progress

        def FindStairs(self):
            self.FoundStairs = True

        def LoseStairs(self):
            self.FoundStairs = False
            self.Progress = -1

        def GetFoundStairs(self):
            return self.FoundStairs

        def ResetFoundStairs(self):
            self.FoundStairs = False

        def IncreaseCurrentFloor(self):
            self.CurrentFloor += 1

        def DecreaseCurrentFloor(self):
            self.CurrentFloor -= 1

        def GetCurrentFloor(self):
            return self.CurrentFloor

        def ChangeFloor(self):
            self.ResetFoundStairs()
            self.ResetProgress()
            self.FloorEvents = {}
            self.ChangeBad(-(self.GetFerocity() / 2.0))
            self.ChangeGood(10)
            self.IncreaseCurrentFloor()

        def StillActive(self):
            for trainer in self.GetTrainers():
                if (len(trainer.GetUnfaintedTeam()) > 0):
                    return True
            return False

        def GetFloors(self):
            return self.Floors

        def RecordItemGet(self, item):
            if (item in self.ItemHistory):
                self.ItemHistory[item] += 1
            else:
                self.ItemHistory[item] = 1
            
            self.WealthGained += GetItemSellValue(item)

        def IsComplete(self):
            return self.GetCurrentFloor() >= self.GetFloors() + 1

        def GoodMagnitude(self, minimum, maximum):
            value = math.floor(minimum) + round((math.ceil(maximum) - math.floor(minimum)) * self.RollGenerous() / 100.0)
            return (value, "{color=#080}♥{b}{size=35}" + IntToWord(value) + "{/size}{/b}{/color}")

        def BadMagnitude(self, minimum, maximum):
            value = math.floor(minimum) + round((math.ceil(maximum) - math.floor(minimum)) * self.RollFeral() / 100.0)
            return (value, "{color=#800}♠{b}{size=35}" + IntToWord(value) + "{/size}{/b}{/color}")

        def GetMagnitude(self, minimum, maximum):
            return self.NeutralMagnitude(minimum, maximum)

        def Magnitude(self, minimum, maximum):
            return self.NeutralMagnitude(minimum, maximum)

        def NeutralMagnitude(self, minimum, maximum):
            value = math.floor(minimum) + round((math.ceil(maximum) - math.floor(minimum)) * self.RollMystery() / 100.0)
            return (value, "{color=#008}♦{b}{size=35}" + IntToWord(value) + "{/size}{/b}{/color}")

        def GetMaxWealthCap(self):
            return self.GetCurrentFloor() * self.Difficulty * 10

        def GetLootList(self, raw=True):
            if (raw):
                return self.LootList
            else:
                newdict = {}
                for key, value in self.LootList.items():
                    if (GetItemSellValue(key) + self.WealthGained < self.GetMaxWealthCap() or key == Item.GimmighoulCoin):
                        newdict[key] = value
                    
                return newdict

        def GetPlayer(self):
            for trainer in self.GetTrainers():
                if (trainer.GetType() == TrainerType.Player):
                    return trainer
            return None

        def GetRedTrainer(self):
            return self.RedTrainer

        def GetNumTrainers(self, numtrainers, excludered=False):
            trainerlist = copy.copy(self.GetTrainers())
            if (excludered):
                if (self.GetRedTrainer() in trainerlist):
                    trainerlist.remove(self.GetRedTrainer())
            while len(trainerlist) > numtrainers:
                trainerlist.remove(RandomChoice(trainerlist))
            return trainerlist

        def GetNumBattlers(self, numbattlers):
            battlerlist = copy.copy(FriendlyBattlers())
            while len(battlerlist) > numbattlers:
                battlerlist.remove(RandomChoice(battlerlist))
            return battlerlist

        def NumBattlers(self):
            return len(FriendlyBattlers())

        def GetNumAllBattlers(self, numallbattlers, excludebosses=False):
            allbattlerlist = copy.copy(Battlers())
            if (excludebosses):
                for battler in allbattlerlist:
                    if battler.HasStatus("tyrannic"):
                        allbattlerlist.remove(battler)
            while len(allbattlerlist) > numallbattlers:
                allbattlerlist.remove(RandomChoice(allbattlerlist))
            return allbattlerlist

        def NumAllBattlers(self):
            return len(Battlers())

        def GetWindBlows(self):
            return self.WindBlows

        def BlowTheWind(self):
            self.WindBlows += 1
            if (self.WindBlows == 1):
                return "The wind blows.\n{cps=*0.7}Something's stirring."
            elif (self.WindBlows == 2):
                return "The wind blows.\n{cps=*0.7}...Something's approaching."
            elif (self.WindBlows == 3):
                return "The wind blows.\n{cps=*0.7}It's getting closer!"
            elif (self.WindBlows == 4):
                return "The wind blows.\n{cps=*0.7}It's right nearby! It's gusting hard!"
            elif (self.WindBlows == 5):
                return "The wind blew.\n{cps=*0.7}It's too late now."

        def DungeonPostTurn(self):
            renpy.call("PerformDungeonEvent", self)

        def IsBossFight(self):
            for mon in EnemyBattlers():
                if (mon.HasStatus("tyrannic")):
                    return True
            return False

label SetupDungeon(dungeon):

$ music = dungeon.GetMusic()
if (isinstance(music, str)):
    queue music music

elif (len(music) == 1):
    queue music music[0]

else:
    queue music music[0] noloop
    queue music music[1]

python:
    renpy.stop_skipping()
    renpy.block_rollback()
    _rollback = False
    renpy.suspend_rollback(True)
    if (dungeon.WasSetUp):
        renpy.transition(dis)
    else:
        renpy.transition(Dissolve(2.0))
    renpy.scene()
    renpy.show(dungeon.GetBackground())
    dungeon.WasSetUp = True

show screen dungeonpartyviewer(dungeon)

return

label DungeonPartyLogistics(dungeon):
label selecttrainerlogistics:

dn "Who do you want to check in on?"

python:
    itemkeys = []
    for trainer in dungeon.GetTrainers():
        itemkeys.append((trainer.GetFormatName(), trainer))
    itemkeys.append(("Nevermind.", "esc"))
    trainer = renpy.display_menu(itemkeys)

if (trainer == "esc"):
    return

label selectedtrainerlogistics:

$ charsex = Genders.Male if trainer.GetName() == "red" else persondex[trainer.GetFormatName()]["Sex"]
$ himpronoun = GetHimPronoun(charsex)
$ hispronoun = GetHisPronoun(charsex)

dn "You've selected [trainer.GetFormatName()]. What do you want to do with [himpronoun]?" 

menu:
    ">Change [hispronoun] position in the marching order":
        $ index = dungeon.GetTrainers().index(trainer)
        dn "[trainer.GetFormatName()] is in slot [IntToWord(index + 1)]. Where would you like to shift [himpronoun]?"

        menu:
            ">Shift to the far left" if (index not in [0, 1]):
                $ dungeon.Trainers.remove(trainer)
                $ dungeon.Trainers.insert(0, trainer)

            ">Shift left" if (index != 0):
                $ dungeon.Trainers[index], dungeon.Trainers[index - 1] = dungeon.Trainers[index - 1], dungeon.Trainers[index]

            ">Shift right" if (index != dungeon.NumTrainers() - 1):
                $ dungeon.Trainers[index], dungeon.Trainers[index + 1] = dungeon.Trainers[index + 1], dungeon.Trainers[index]

            ">Shift to the far right" if (index not in [dungeon.NumTrainers() - 2, dungeon.NumTrainers() - 1]):
                $ dungeon.Trainers.remove(trainer)
                $ dungeon.Trainers.append(trainer)

            "Nevermind.":
                jump selectedtrainerlogistics

    ">Change [hispronoun] first Pokémon":
        call screen switch(trainer)

        if (isinstance(_return, int)):
            $ trainer.ShiftTeam(0, _return, positionswitch = True)

        jump selectedtrainerlogistics

    "Nevermind.":
        jump selecttrainerlogistics

return
