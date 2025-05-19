init python:
    def MakeRed(number=1, heal=True):
        trainer1 = Trainer("red", TrainerType.Player, playerparty, number=number, heal=heal)
        for mon in playerparty:
            mon.Owner = trainer1
        return trainer1

    def MakeTrainer(trainername, trainertype = TrainerType.Enemy, number=1, order=None, heal=True):
        trainer1 = Trainer(trainername.lower(), trainertype, GetTrainerTeam(trainername.title(), heal=heal, order=order), number=number)
        for mon in trainer1.GetTeam():
            mon.Owner = trainer1
        return trainer1

    class Trainer:
        def __init__(self, name, trainertype, team, number=1, isPokemon=False, heal=True):
            self.Name = name.lower()#string
            self.Team = team#[Pokemon]
            self.Type = trainertype#TrainerType macro
            self.Number = number#1 for single battle, 2 for double, 3 for triple
            self.IsPokemon = isPokemon
            self.FaintedPokemonCount = 0#used for last respects

        def ResetFaintedPokemonCount(self):
            self.FaintedPokemonCount = 0

        def GetFaintedPokemonCount(self):
            if (not hasattr(self, 'FaintedPokemonCount')):
                self.FaintedPokemonCount = 0
            return self.FaintedPokemonCount

        def IncreaseFaintedPokemonCount(self):
            if (not hasattr(self, 'FaintedPokemonCount')):
                self.FaintedPokemonCount = 0
            self.FaintedPokemonCount = self.FaintedPokemonCount + 1

        def GetIsPokemon(self):
            return self.IsPokemon

        def GetFormatName(self):
            if (self.Name == "red"):
                return first_name
            else:
                return self.Name.title()

        def GetName(self):
            return self.Name

        def ReorderTeam(self):
            fainteds = []
            for mon in self.GetTeam():
                if (mon.GetHealthPercentage() <= 0):
                    fainteds.append(mon)
            self.Team = self.GetUnfaintedTeam() + fainteds

        def GetLead(self, addNones=True):
            leads = self.Team[:self.Number]
            if (addNones):
                for i in range(len(leads)):
                    if (leads[i].GetHealth() <= 0):
                        leads[i] = None
            else:
                removelist = []
                for mon in leads:
                    if (mon.GetHealth() <= 0):
                        removelist.append(mon)
                for mon in removelist:
                    leads.remove(mon)
            return leads

        def GetTeam(self, heal=False):
            if (self.Team == None):
                if (self.Name == "red"):
                    self.Team = playerparty
                else:
                    self.Team = GetTrainerTeam(self.Name, None, heal)
            return self.Team

        def GetNumPkmn(self, numpkmn):
            teamlist = copy.copy(self.GetTeam())
            while len(teamlist) > numpkmn:
                teamlist.remove(RandomChoice(teamlist))
            return teamlist

        def GetUnfaintedTeam(self):
            unfainteds = []
            for mon in self.GetTeam():
                if (mon.GetHealth() > 0):
                    unfainteds.append(mon)
            return unfainteds

        def GetType(self):
            return self.Type

        def ShiftTeam(self, swapto, swapfrom, force=False, positionswitch = False):
            global switchedmon
            
            swappingmon = self.GetTeam()[swapto]
            swappingtomon = self.GetTeam()[swapfrom]
            
            if (not positionswitch):
                if (swappingtomon.GetHealth() <= 0):
                    renpy.say(None, "{} is fainted, and can't switch in!".format(swappingtomon.GetNickname()))
                    return False
                elif (not CanSwitch(swappingmon, force)):
                    renpy.say(None, "Can't switch in!")
                    return False

                if (swappingmon.GetHealthPercentage() > 0 and swappingmon.HasAbility("Regenerator")):
                    swappingmon.AdjustHealth(swappingmon.GetStat(Stats.Health) * 0.33)
                if (swappingmon.HasNormalStatus() and swappingmon.HasAbility("Natural Cure")):
                    swappingmon.ClearStatus(None, all=True)    
                    
                swappingmon.ClearStatus(None, volatiles=True)
                swappingtomon.ClearStatus(None, volatiles=True)

            self.GetTeam()[swapto], self.GetTeam()[swapfrom] = self.GetTeam()[swapfrom], self.GetTeam()[swapto]

            if (not positionswitch):
                for mon in Battlers():
                    if (mon.GetStatusCount("infatuated") == swappingmon):
                        mon.ClearStatus("infatuated")
                    if (mon.GetStatusCount("menaced") == swappingmon):
                        mon.ClearStatus("menaced")

            if (self.Name == "red"):
                switchedmon = True

            return True

        def HasMons(self):
            for mon in self.GetTeam():
                if (mon.GetHealth() != 0):
                    return True
            return False

        def GetNumber(self):
            return self.Number