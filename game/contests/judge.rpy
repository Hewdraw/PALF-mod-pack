init python:
    class Judge:
        def __init__(self, customcharacter, biases=None, customsex=None):
            self.CustomCharacter = customcharacter#the customcharacterobject that holds this character's stuff
            self.Name = customcharacter.name#a string that is the judge's name
            if (customsex == None):
                self.Sex = persondex[self.Name]["Sex"]#A Genders macro
            else:
                self.Sex = customsex

            self.Seeking = None#A ContestMoveType macro
            self.JackpotLimit = 5# goes down to 1
            self.Sparks = 0#goes up to JackpotLimit

            self.Biases = biases

            if (not self.Biases):
                self.Biases = { ContestMoveType.Cute : 10, ContestMoveType.Beautiful : 10, ContestMoveType.Cool : 10, ContestMoveType.Clever : 10, ContestMoveType.Tough : 10 }

            self.LastSeekingDialog = []

        def GetImage(self):
            return self.CustomCharacter.image + " " + self.GetMood()

        def GetMood(self):
            sparkspercentage = self.GetSparks() / self.GetJackpotLimit()

            returnable = ""
            if (sparkspercentage >= 1):
                returnable = "happy"
            elif (sparkspercentage >= .8):
                returnable = "surprisedbrow happymouth"
            elif (sparkspercentage >= .6):
                returnable = "closedbrow happymouth"
            elif (sparkspercentage >= .4):
                returnable = "surprisedbrow"
            elif (sparkspercentage < 0):
                returnable = "closedbrow sadmouth"

            if (self.CustomCharacter == hiker):
                returnable += " hat"
            elif (self.CustomCharacter == hiker2):
                returnable += " knife"
            elif (self.CustomCharacter == hiker3):
                returnable += " backpack"

            return returnable

        def SetSeeking(self):
            biasdict = copy.copy(self.Biases)
            for judge in Judges:
                sought = judge.GetSeeking()
                if (sought != None):
                    biasdict[sought] = 0
            self.Seeking = weighted_random_selection(biasdict)

        def GetSeeking(self):
            return self.Seeking

        def GetSeekingImage(self):
            if (self.GetSeeking() == ContestMoveType.Cool): 
                return "gui/contest/request_cool.webp"
            elif (self.GetSeeking() == ContestMoveType.Cute):
                return "gui/contest/request_cute.webp"
            elif (self.GetSeeking() == ContestMoveType.Clever): 
                return "gui/contest/request_clever.webp"
            elif (self.GetSeeking() == ContestMoveType.Beautiful):
                return "gui/contest/request_beautiful.webp"
            elif (self.GetSeeking() == ContestMoveType.Tough):
                return "gui/contest/request_tough.webp"

        def GetJackpotLimit(self):
            return self.JackpotLimit

        def GetSparks(self):
            return self.Sparks
            
        def GetName(self):
            return self.Name

        def IncreaseSparks(self):
            self.Sparks += 1

        def DecreaseSparks(self):
            self.Sparks -= 1
            if (self.Sparks < 0):
                self.Sparks = 0

        def ResetSparks(self):
            self.Sparks = 0
            self.JackpotLimit = max(1, self.GetJackpotLimit() - 1)
            self.SetSeeking()

        def GetSex(self):
            return self.Sex

        def GetHePronoun(self):
            return ("he" if self.GetSex() == Genders.Male else "she")

