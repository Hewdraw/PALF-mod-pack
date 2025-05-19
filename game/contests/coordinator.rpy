init python:
    class CoordinatorGroup:
        def __init__(self, coordinators):
            self.Coordinators = coordinators
            self.ActionRecord = {}#has a series of entries, where the 'turns' are recorded. Each key is an int with the turn number, and the value is an int of how many points they won at end of turn. Turn zero is the initial condition factor
            self.CurrentPoints = 0
            self.MovesMade = { 0 : None }#has a series of entries, where the 'turns' are recorded. Each key is an int with the turn number, and the value is the name of the move used, or None
            self.ReactionNoted = False
            self.SuitabilityRecord = { 0 : 0 }
            self.PriorityAdjustment = 0
            self.Energy = 0

        def GetPerformanceDialog(self, move, energy):
            element = move.Type
            movename = move.Name
            performancetype = move.Contest

            if (element == "Normal" and move.Category == "Status"):#overwrite normal-type status moves with whatever the Pokémon in question is
                element = self.GetMon().GetTypes()[0]
                if (element == "Normal" and len(self.GetMon().GetTypes()) > 1):#if the Pokémon actually is normal-type, look for their secondary type
                    element = self.GetMon().GetTypes()[1]

            #performancetype can be one of "Cute", "Tough", "Beautiful", "Clever", or "Cool"
            #turn can be any int from 1 to 10. Higher values should have more excited narration.
            #Energy can be any int from 0 to 3. Higher values should have more excited narration.

            performance_dialogues_male = {
                "Cute": "With a dashing smile and a bow to the crowd,",
                "Tough": "Gritting his teeth and flexing at the crowd,",
                "Beautiful": "With an elegant motion that flows like water,",
                "Clever": "With a quick-witted improvised embellishment,",
                "Cool": "With an effortless and stylish flair,"
            }

            performance_dialogues_female = {
                "Cute": "With an adorable twirl and a curtsey to the crowd,",
                "Tough": "Planting her feet firmly and raising a fist to the crowd,",
                "Beautiful": "With a graceful motion like flowing water,",
                "Clever": "Masterfully executing a practiced performance,",
                "Cool": "With an effortless and stylish flair,"
            }

            performance_dialogues_group = {
                "Cute": "Holding hands and winking at the audience,",
                "Tough": "Back-to-back,",
                "Beautiful": "With synchronized, graceful motions that come together like flowing water,",
                "Clever": "Putting their heads together to come up with a genius plan",
                "Cool": "With an effortless and stylish flair,"
            }

            energydialogues = {
                0: " performs",
                1: " gives a rousing performance",
                2: " gives a striking performance",
                3: " gives an absolutely stunning performance"
            }

            performance_dialogues = {
                Genders.Male : performance_dialogues_male,
                Genders.Female : performance_dialogues_female,
                Genders.Unknown : performance_dialogues_group
            }

            movedialogues = {
                "Normal" : {
                    "Cute" : "charming the audience with a playful bounce!",
                    "Tough" : "showing off raw power with an imposing stance!",
                    "Beautiful" : "demonstrating a smooth and flowing routine!",
                    "Clever" : "crafting a perfectly timed move to intrigue the judges!",
                    "Cool" : "executing a confident and stylish flourish!"
                },
                "Fire" : {
                    "Cute" : "sending out little embers that twinkle like fireflies!",
                    "Tough" : "unleashing a fierce blaze that radiates intensity!",
                    "Beautiful" : "creating a mesmerizing spiral of flames!",
                    "Clever" : "crafting a controlled burst of fire that dazzles the judges!",
                    "Cool" : "setting the stage ablaze with a fiery spectacle!"
                },
                "Water" : {
                    "Cute" : "sprinkling tiny bubbles that glisten in the light!",
                    "Tough" : "summoning a crashing wave with force!",
                    "Beautiful" : "weaving water into an elegant, flowing dance!",
                    "Clever" : "manipulating water with precise control!",
                    "Cool" : "launching a jet of water with pinpoint accuracy!"
                },
                "Grass" : {
                    "Cute" : "instantaneously growing a field of flowers wherever the coordinators step!",
                    "Tough" : "as thick vines burst from the ground and interlace into a rigid canopy!",
                    "Beautiful" : "summoning a whirlwind of petals that dance in the air!",
                    "Clever" : "coiling vines in an intricate pattern!",
                    "Cool" : "slicing through the air with sharp-edged foliage!"
                },
                "Electric" : {
                    "Cute" : "sending out tiny sparks that crackle playfully!",
                    "Tough" : "discharging a bolt of lightning that shakes the stage!",
                    "Beautiful" : "illuminating the stage with a dazzling electric glow!",
                    "Clever" : "timing a precise spark to literally steal the spotlight!",
                    "Cool" : "flashing a blinding bolt of electricity with style!"
                },
                "Ice" : {
                    "Cute" : "sending a soft flurry of snowflakes flying around the stage!",
                    "Tough" : "creating a hard mountain of ice, then shattering it with sheer force!",
                    "Beautiful" : "summoning a gorgeous aurora to cover the stage!",
                    "Clever" : "carving an intricate ice sculpture on the spot!",
                    "Cool" : "skating around on the ice-covered floor with quick, sharp movements!"
                },
                "Fighting" : {
                    "Cute" : "throwing a playful feint before striking a bold pose!",
                    "Tough" : "demonstrating its supreme physical prowess!",
                    "Beautiful" : "flowing seamlessly between powerful strikes!",
                    "Clever" : "using a strategic feint to keep the other coordinator's guessing!",
                    "Cool" : "unleashing a precise and disciplined attack!"
                },
                "Poison" : {
                    "Cute" : "blowing a cloud of iridescent bubbles into the air!",
                    "Tough" : "harmlessly inhaling toxic fumes that could lay out a Copperajah!",
                    "Beautiful" : "creating a mesmerizing mist of purple haze!",
                    "Clever" : "coating the stage with a calculated, eerie poison pattern!",
                    "Cool" : "leaving behind a trail of dazzling, toxic energy!"
                },
                "Ground" : {
                    "Cute" : "kicking up a tiny cloud of dust with an energetic stomp!",
                    "Tough" : "shaking the stage with an earth-rattling strike!",
                    "Beautiful" : "sculpting a smooth, flowing sand formation!",
                    "Clever" : "shifting the ground beneath their feet with precision!",
                    "Cool" : "sending cracks through the ground with a stylish stomp!"
                },
                "Flying" : {
                    "Cute" : "fluttering about in a playful aerial dance!",
                    "Tough" : "slicing through the air with powerful wing beats!",
                    "Beautiful" : "performing an elegant mid-air twirl!",
                    "Clever" : "soaring with precise, controlled movements!",
                    "Cool" : "gliding effortlessly with a confident look!"
                },
                "Psychic" : {
                    "Cute" : "creating a floating display of sparkling energy!",
                    "Tough" : "pulsing psychic energy through the air with force!",
                    "Beautiful" : "forming intricate, shimmering patterns midair!",
                    "Clever" : "telekinetically levitating objects in a gravity-defying show!",
                    "Cool" : "radiating a literally visible aura of power and confidence!"
                },
                "Bug" : {
                    "Cute" : "playing up the inherent adorableness of all things tiny, creepy, and crawly!",
                    "Tough" : "lifting weights a hundred times its own!",
                    "Beautiful" : "releasing a wave of shimmering scales in a hypnotic display!",
                    "Clever" : "outmaneuvering the other coordinators with rapid and unpredictable motions!",
                    "Cool" : "slicing with claw, mandible, and other insectoid armaments!"
                },
                "Rock" : {
                    "Cute" : "stacking tiny pebbles into a cute arrangement!",
                    "Tough" : "crashing a massive boulder into the stage!",
                    "Beautiful" : "sculpting a stone masterpiece mid-performance!",
                    "Clever" : "shaping the rock with calculated strikes!",
                    "Cool" : "shattering rock with seemingly effortless ease!"
                },
                "Ghost" : {
                    "Cute" : "creating playful ghostly wisps that dance around!",
                    "Tough" : "sending out an eerie chill through the audience!",
                    "Beautiful" : "floating ethereally, phasing in and out!",
                    "Clever" : "vanishing and reappearing with perfect timing!",
                    "Cool" : "executing a spooky yet thrilling phantom display!"
                },
                "Dark" : {
                    "Cute" : "giving a mischievous yet charming wink!",
                    "Tough" : "mercilessly overshadowing the competition!",
                    "Beautiful" : "moving with an air of mysterious grace!",
                    "Clever" : "crafting an illusion to dazzle and confuse!",
                    "Cool" : "executing a shadowy maneuver with confidence!"
                },
                "Dragon" : {
                    "Cute" : "letting out a tiny but endearing roar!",
                    "Tough" : "unleashing a powerful draconic roar that shakes the stage!",
                    "Beautiful" : "soaring with majestic, draconic energy!",
                    "Clever" : "using an ancient technique with masterful precision!",
                    "Cool" : "dominating the stage with a fiery draconic display!"
                },
                "Steel" : {
                    "Cute" : "clinking metal pieces together in a rhythmic fashion!",
                    "Tough" : "displaying unyielding resilience with a steel-hard stance!",
                    "Beautiful" : "reflecting light beautifully off metallic surfaces!",
                    "Clever" : "forging an intricate steel shape with expert control!",
                    "Cool" : "striking with a sleek, metallic finish!"
                },
                "Fairy" : {
                    "Cute" : "sprinkling shimmering fairy dust into the air!",
                    "Tough" : "releasing an unexpected burst of dazzling force!",
                    "Beautiful" : "dancing gracefully with a radiant glow!",
                    "Clever" : "casting an enchanting spell with playful trickery!",
                    "Cool" : "winking as a cascade of sparkles follows their movement!"
                }
            }

            energyline = energydialogues[energy]
            if (len(self.GetCoordinators()) > 1):
                energyline = energyline.replace("performs", "perform").replace("gives", "give")
            
            return f"{performance_dialogues[self.GetSex()][performancetype]} {self.GetName()}{energyline} as {self.GetFirstMonName()} uses {movename}, {movedialogues[element][performancetype]}"
            
        def GetActions(self):
            return self.ActionRecord

        def GetAction(self, round):
            if (round in self.GetActions().keys()):
                return self.GetActions()[round]
            else:
                return 0

        def EvaluateCondition(self):
            totalcondition = 0
            for trainer in self.Coordinators:
                totalcondition += trainer.GetCondition()
            self.RecordRound(0, totalcondition)
            return self.GetAction(0)

        def GetPriority(self):
            return self.PriorityAdjustment

        def SetPriority(self, priority):
            self.PriorityAdjustment = priority

        def ResetPriority(self):
            self.SetPriority(0)

        def RecordRound(self, turn, points):
            self.ActionRecord[turn] = points

        def RecordMove(self, turn, movename):
            self.MovesMade[turn] = movename

        def RecordSuitability(self, turn, pts):
            self.SuitabilityRecord[turn] = pts

        def SumSuitability(self):
            total = 0
            for key, val in self.SuitabilityRecord.items():
                total += val
            return total

        def GetMoveRecord(self):
            return self.MovesMade

        def GetPointsOnTurn(self, turn):
            if (turn in self.ActionRecord):
                return self.ActionRecord[turn]
            else:
                return 0

        def NotReactionNoted(self):
            return not self.ReactionNoted

        def NoteReaction(self):
            self.ReactionNoted = True

        def UnNoteReaction(self):
            self.ReactionNoted = False

        def GetCoordinators(self):
            return self.Coordinators

        def GroupSize(self):
            return len(self.GetCoordinators())

        def GetHisPronoun(self):
            return ("his" if self.GetSex() == Genders.Male else ("her" if self.GetSex() == Genders.Female else "their"))
        
        def GetHimPronoun(self):
            return ("him" if self.GetSex() == Genders.Male else ("her" if self.GetSex() == Genders.Female else "them"))

        def IsGroup(self):
            return self.GroupSize() > 1

        def IsSolo(self):
            return not self.IsGroup()

        def IsProtag(self):
            for coordinator in self.GetCoordinators():
                if (coordinator.IsProtag()):
                    return True
            return False

        def GetName(self):
            if (not self.IsGroup()):
                return self.GetSoloCoordinator().GetName()
            else:
                names = [coordinator.GetName() for coordinator in self.GetCoordinators()]
                if len(names) == 2:
                    return " and ".join(names)
                else:
                    return ", ".join(names[:-1]) + ", and " + names[-1]

        def GetSoloCoordinator(self):
            if (self.IsGroup()):
                raise ValueError("Can't run 'GetSoloCoordinator' on group.")
            return self.GetCoordinators()[0]

        def GetImage(self, additionals="", overridemood=0):#1964x3316
            if (not self.IsGroup()):
                return [self.GetSoloCoordinator().GetImage(additionals, overridemood)]
            else:
                images = []
                for coordinator in self.GetCoordinators():
                    images.append(coordinator.GetImage(additionals, overridemood))
                return images

        def Reorder(self, mon):#this function puts the monster at the start of the getteam function
            leadercoord = None
            for coord in self.GetCoordinators():
                if (mon in coord.GetTeam()):
                    leadercoord = coord
                    break
            self.Coordinators.remove(leadercoord)
            self.Coordinators.insert(0, leadercoord)
            swapfrom = leadercoord.Trainer.GetTeam().index(mon)
            swapto = 0
            leadercoord.Trainer.ShiftTeam(swapto, swapfrom, force=True, positionswitch=False)

        def GetTeam(self):
            fulllist = []
            for coordinator in self.GetCoordinators():
                fulllist += coordinator.GetTeam()
            return fulllist

        def GetFirstMonName(self):
            return self.GetMon().GetNickname()

        def GetFirstMonSpeciesName(self):
            return pokedexlookup(self.GetMon().Id, DexMacros.Name)

        def GetSex(self):
            if (self.IsGroup()):
                return Genders.Unknown
            else:
                return self.GetSoloCoordinator().GetSex()

        def MultiplyCurrentPoints(self, multiple):
            self.CurrentPoints *= multiple

        def GetMon(self):
            return self.GetTeam()[0]

        def GetMoves(self):
            return self.GetMon().GetMoves()

        def CalculateMove(self, moveobj):
            contesttype = ContestStringToMacro(moveobj.Contest)
            effect = GetmoveincontestEffect(moveobj)
            routine = effect == ContestEffects.Unjammable
            jams = effect == ContestEffects.Jamming
            index = Coordinators.index(self)

            pointevaluation = 6

            if (index < 2 and routine):
                pointevaluation += 3
            elif (routine):
                pointevaluation -= 1

            if (index > 2 and jams):
                pointevaluation += 3
            elif (jams):
                pointevaluation -= 1

            for i, judge in enumerate(Judges):
                if (RepeatedMove(self, Turn, moveobj)):
                    pointevaluation -= 3
                elif (contesttype == judge.GetSeeking()):
                    pointevaluation += 5 * (judge.GetSparks() + 1)
                    if (judge.GetJackpotLimit() - judge.GetSparks() == 1 + index):
                        pointevaluation += (4 - index) * 10
                elif (Jams(judge.GetSeeking(), contesttype)):
                    pointevaluation -= 2 * (judge.GetSparks() + 1)

            pointevaluation = max(0, pointevaluation)

            return pointevaluation

        def AwardedPoints(self, points, judge):
            if (judge != None):
                index = Judges.index(judge)
                AnimateValueChange(points, (0.85, (index+.5)/len(Judges) + 0.035), changemood=False, pausing = (index == 2))
            else:
                index = Coordinators.index(self)
                AnimateValueChange(points, (0.33, 0.5), changemood=False, pausing=True)

            self.CurrentPoints += points

        def JamPoints(self):
            index = Coordinators.index(self)
            losepoints = min(-1, -math.floor(self.CurrentPoints / 3))
            AnimateValueChange(losepoints, (0.33, 0.5), changemood=False, pausing=True)
            self.CurrentPoints += losepoints
            self.ResetEnergy()

        def GetCurrentPoints(self):
            return self.CurrentPoints

        def ResetCurrentPoints(self):
            self.CurrentPoints = 0

        def GainEnergy(self):
            preenergy = self.Energy
            self.Energy = min(3, self.Energy + 1)
            return preenergy != self.Energy

        def GetEnergy(self):
            return self.Energy

        def ResetEnergy(self):
            self.Energy = 0
        
        def GetConditionAverage(self):
            return sum([coord.GetCondition() for coord in self.GetCoordinators()])/len(self.GetCoordinators())

        def DisplayIntroStart(self, placement):
            images = self.GetImage()
            for i, coordinator in enumerate(images):
                renpy.show(coordinator, at_list=[slideincontest(0.3, i, len(images))])
            renpy.pause(1.0)
            DisplayPokemon(self.GetMon(), contestcenter)
            renpy.pause(0.5)
        
        def DisplayIntroEnd(self):
            renpy.pause(0.5)
            renpy.show("sideportraitnew", at_list=[slideoutcontest(0.11)])
            images = self.GetImage()
            for i, coordinator in enumerate(images):
                renpy.show(coordinator, at_list=[slideoutcontest(0)])
            renpy.pause(0.5)
            renpy.hide("sideportraitnew")
        
        def CalculateEnergySpending(self, move):
            energy = self.GetEnergy()
            if energy > 0:
                if Coordinators.index(self) == len(Coordinators) - 1: # Not spend energy if you're late in the round
                    return 0
                if Turn % 5 == 0: # Spend all your energy turn 5 and 10
                    return energy
                if Coordinators.index(self) == 0: # Spend energy if you're early in the round
                    return min(energy, Turn//3) # Will spend more energy the further they are into the contest
                if energy == 3 and move.Contest == self.GetMon().GetContestTrait(): # Spend energy if you have three and are about to use a STAB move
                    return 3
                if any(IsJammingMove(othermove) for othermove in list(Coordinators[Coordinators.index(self) + 1].GetMoveRecord().values())[1:]) and not IsRoutineMove(move): # Spend energy if you know an opposing coordinator moving after you has a jamming move that will affect the move you're about to use
                    return energy if self.GetConditionAverage() / 160 > 0.5 + random.random() / 2 else 0 # Higher condition coordinators groups have a higher chance of spending all energy if they know the next coordinator has a jamming move
            return 0

    class Coordinator:
        def __init__(self, name, condition = 0, isprotag = False, partner=None, contestsprite=None):
            self.Name = name#the coordinator's name, as read in the persondex
            if (not isprotag):
                if (name in defaultpersondex):
                    self.Trainer = MakeTrainer(name)#the trainer object that contains all the expected information for a trainer
                else:#if using generic npcs
                    self.Trainer = Trainer(name, TrainerType.Enemy, [partner])
            else:
                self.Trainer = MakeRed()
            self.Condition = condition#basically their rizz score
            self.IsProtagonist = isprotag
            self.ContestSprite = "contest"
            if (contestsprite != None):
                self.ContestSprite = contestsprite

            if (partner in self.GetTeam()):
                self.GetTeam().remove(partner)
                self.GetTeam().insert(0, partner)


        def GetCondition(self):
            return self.Condition

        def GetName(self):
            return self.Name

        def GetImage(self, additionals="", overridemood=0):
            return GetCharacterSprite(self.GetName(), overridemood, extras=self.ContestSprite + " " + additionals, protag=self.IsProtagonist)

        def GetTeam(self):
            return self.Trainer.GetTeam()

        def GetSex(self):
            if (self.IsProtag() or self.GetName() in ["Old Man", "Roughneck", "Hiker"]):
                return Genders.Male
            elif (self.GetName() in ["Hex Maniac", "Punk Girl"]):
                return Genders.Female
            return persondex[self.GetName()]["Sex"]

        def IsProtag(self):
            return self.IsProtagonist
            

            
