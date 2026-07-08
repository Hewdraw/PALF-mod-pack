init python:
    def donothing(*args, **kwargs):
        pass

    class TempCharacter():
        def __init__(self, name, addquotes=True):
            self.name = name
            self.addquotes = addquotes

        def __call__(self, what, **kwargs):

            formatwhat = what

            if (self.addquotes):
                formatwhat = "\"" + formatwhat + "\""

            return Character(name=self.name, color="#700000", image=None, ctc=(None if InContest else "ctc_blink"), ctc_position="fixed", callback=callbackcontinue, dynamic=False)(formatwhat, **kwargs)

    class CustomCharacter():
        def __init__(self, name, color, image, **kwargs):
            self.image = image
            self.name = name
            self.color = color
            self.do_extend = donothing
            self.empty_window = donothing

        def __call__(self, what, **kwargs):
            formatcallback=callbackcontinue

            if (what == ""):
                _window_hide(None)
                return Character(name="", color=self.color, image=self.image)("{nw}", **kwargs)
            else:
                formatname = self.name
                dynamic = False
                formatcolor = self.color
                
                if ("persondex" in globals() and formatname in persondex.keys() and not IsNamed(formatname) and not self.image == "latias"):
                    formatname = (lambda: "???")
                elif (formatname == "Red"):
                    formatname = (lambda: first_name)
                elif (formatname == "Pikachu"):
                    formatname = (lambda: pika_name)
                    if (self.image == "libpikachu"):
                        formatcolor = GetLiberaColor()
                        if (formatcolor == "#fff"):
                            formatcolor = "#fca600"
                elif (formatname == "Blue" and IsNamed("Blue") and playercharacter != "Blue"):
                    formatname = (lambda: blue_name)
                elif (formatname == "Kris"):
                    formatname = "Professor Cherry"
                elif (formatname == "Your Starter"):
                    formatcolor = GetColor(starter_id)
                    formatname = (lambda: starter_name)
                elif (formatname == "Nate"):
                    if (HasEvent("Nate", "Blake") and not HasEvent("Nate", "NameRevert")):
                        formatname = (lambda: "Blake")
                elif (formatname == "Sidemon"):
                    formatcolor = GetColor(sidemonnum)
                    formatname = (lambda: (pokedexlookup(sidemonnum, DexMacros.Name) if sidemonoverride == None else sidemonoverride))
                elif (formatname == "Sensei Marshal"):
                    if (playercharacter != None):
                        formatname = (lambda: "Marshal")
                    elif (not HasEvent("Sensei Marshal", "EndedRename")):
                        if (HasEvent("Sensei Marshal", "Renamed2")):
                            formatname = (lambda: "{size=8}Sensei Jugemu Jugemu Goko-no Surikire Suigyomatsu Unraimatsu Furaimatsu Kuunerutokoro-ni Sumutokoro Yaburakoji-no Burakoji Paipopaipo Paipo-no Shuringan Shuringan-no Gurindai Gurindai-no Ponpokopii-no Ponpokona-no Chokyumei-no Chosuke{/size}")
                        elif (HasEvent("Sensei Marshal", "Renamed1")):
                            formatname = (lambda: "{size=15}Sensei Jugemu Jugemu Goko-no Surikire Suigyomatsu Unraimatsu Furaimatsu Kuunerutokoro-ni Sumutokoro Yaburakoji-no Burakoji{/size}")
                elif (formatname == "Leaf"):
                    if (HasEvent("Leaf", "IsFael")):
                        formatname = (lambda: "Fael")
                elif (formatname == "Tia"):
                    if (HasEvent("Tia", "RenameBriefly")):
                        formatname = (lambda: "Ancestor")
                elif (formatname == "Professor Rowan"):
                    formatname = (lambda: "Professor Rowan Nanakamado")
                    if (HasEvent("Professor Rowan", "Rename3")):
                        formatname = (lambda: "Rowan")
                    elif (HasEvent("Professor Rowan", "Rename2")):
                        formatname = (lambda: "Oh, okay, just Rowan")
                    elif (HasEvent("Professor Rowan", "Rename1")):
                        formatname = (lambda: "Apparently not Professor Rowan Nanakamado")
                elif (formatname == "Iono"):
                    formatname = (lambda: "{gradient=#EE8FB5-#1d8fc5}Iono{/gradient}")
                elif (formatname == "Bugsy"):
                    if (HasEvent("Bugsy", "RenamedInstructor")):
                        formatname = (lambda: "Instructor Bugsy")
                elif (formatname == "Duplica"):
                    if (duplicacopying != None):
                        if (duplicacopying == "Red"):
                            formatcolor = "#cf0000"
                            formatname = (lambda: first_name + "?")
                            self.image = "copyred"

                        else:
                            formatcolor = GetCharColor(duplicacopying)
                            formatname = (lambda: duplicacopying + "?")
                            self.image = "copy" + GetCharacterSprite(duplicacopying, 0)
                    else:
                        formatname = (lambda: duplica_name)
                        self.image = "duplica"
                elif (formatname == "DungeonNarrator"):
                    formatname = (lambda: "")
                
                dynamic = self.name != formatname

                # DOCUMENTATION
                # Example of how to implement BipBop sounds for a specific character:
                # Let's say you would want to have Fael be given the voice.
                # You would replace Leaf's formatting above with the following lines:
                
                # elif (formatname == "Leaf"):
                #     if (HasEvent("Leaf", "IsFael")):
                #         formatname = (lambda: "Fael")
                #         formatcallback=functools.partial(boopy_voice, boopfile="Audio/pmd_speak.ogg")

                # If beepboop variable is activated, all characters will play beepboops. Otherwise, no sound is made.
                #if formatcallback == callbackcontinue and beepboop: # AND Var for beep boops are ON.
                #    formatcallback=functools.partial(boopy_voice, boopfile="Audio/pmd_speak.ogg")
                #elif not beepboop:
                formatcallback=smalltalkcallback

                # Except the narrator while in battle, they need silencing.
                #if formatname == "" and inbattle: 
                #    formatcallback=callbackcontinue

                formatwhat = what

                if (self.name == "Ethan"):
                    formatwhat = EthanNameFilter(formatwhat)
                elif (self.name in ["Nate", "Blake"]):
                    formatwhat = NateNameFilter(formatwhat)
                elif (self.name == "DungeonNarrator"):
                    formatwhat = FormatText(formatwhat)
                
                if (formatname == "You"):
                    formatwhat = "{{i}}({}){{/i}}".format(formatwhat)
                elif (formatname == "" or self.name == "DungeonNarrator"):
                    formatwhat = ">{{cps=*0.8}}{}".format(formatwhat)
                elif (formatname == "Tia" and self.image != "latias" and autoquote):
                    if (what[-4:] == "{nw}"):#if this sentence ends in a no-wait...
                        if formatcallback == callbackcontinue: # If no beepboops, keep formatcallback None. 
                            formatcallback=None
                        else: # If formatcallback != callbackcontinue, then we know beepboops are activated.
                            formatcallback=functools.partial(formatcallback, no_click=True)
                        formatwhat = "<{}".format(formatwhat)#remove the ending quote
                    else:
                        formatwhat = "<{}>".format(formatwhat)
                elif (what[-4:] == "{nw}"):#if this sentence ends in a no-wait...
                    if formatcallback == callbackcontinue: # If no beepboops, keep formatcallback None. 
                        formatcallback=None
                    else: # If formatcallback != callbackcontinue, then we know beepboops are activated.
                        formatcallback=functools.partial(formatcallback, no_click=True)
                    formatwhat = "\"{}".format(formatwhat)#remove the ending quote
                elif (autoquote):
                    formatwhat = "\"{}\"".format(formatwhat)
                #elif ("{glitch=" in what):

                formatwhat.replace("first_name", first_name)

                if (not profanity):
                    profanitylist = {
                        "fuck", "shit", "crap", "dick", "ass", "asshole", "goddamn", "bullshit", "horseshit", "bullcrap",
                        "dickhead", "dickheads", "bitch", "bastard", "jackass", "douchebag", "pussy", "shitty", "shitting",
                        "fucking", "fucker", "piss", "pissed", "motherfucker", "damn"
                    }

                    # Regex: optional leading punct, word, optional trailing punct
                    pattern = re.compile(
                        r'(?P<pre>\W*)(?P<word>\b(?:' + '|'.join(re.escape(word) for word in profanitylist) + r')\b)(?P<post>\W*)',
                        re.IGNORECASE
                    )

                    def replace(match):
                        word = match.group("word")
                        return f"{match.group('pre')}{'*' * len(word)}{match.group('post')}"
                    
                    formatwhat = pattern.sub(replace, formatwhat)

                return Character(name=formatname, color=formatcolor, image=self.image, ctc=(None if InContest else "ctc_blink"), ctc_position="fixed", callback=formatcallback, dynamic=dynamic)(formatwhat, **kwargs)

define defaultpersondex = {
    "Professor Oak" : {"Role" : "Staff", "Region": "Kanto", "Named" : True, "Value" : 0, "Contact": False, "Sex": Genders.Male, "Relationship": "Student", "RelationshipRank": 0, "Events": [], "Mood": 0, "Nature": TrainerNature.Special, "Color": "#000000", "Image": "oak", "Direction": "Front"},
    "Blue" : {"Role" : "Student", "Region": "Kanto", "Named" : True, "Value" : 0, "Contact": True, "Sex": Genders.Male, "Relationship": "Rival", "RelationshipRank": 0, "Events": [], "Mood": 0, "Nature": TrainerNature.Distant, "Color": "#3110dd", "Image": "blue", "Direction": "Right"},
    "Silver" : {"Role" : "Student", "Region": "Johto", "Named" : False, "Value" : 0, "Contact": False, "Sex": Genders.Male, "Relationship": "Classmate", "RelationshipRank": 0, "Events": [], "Mood": 0, "Nature": TrainerNature.Moody, "Color": "#686080", "Image": "silver", "Direction": "Right"},
    "Brawly" : {"Role" : "Senior Student", "Region": "Hoenn", "Named" : False, "Value" : 0, "Contact": False, "Sex": Genders.Male, "Relationship": "Underclassman", "RelationshipRank": 0, "Events": [], "Mood": 0, "Nature": TrainerNature.Special, "Color": "#467595", "Image": "brawly", "Direction": "Right"},
    "Roxanne" : {"Role" : "Senior Student", "Region": "Hoenn", "Named" : False, "Value" : 0, "Contact": False, "Sex": Genders.Female, "Relationship": "Underclassman", "RelationshipRank": 0, "Events": [], "Mood": 0, "Nature": TrainerNature.Special, "Color": "#a2254b", "Image": "roxanne", "Direction": "Left"},
    "Falkner" : {"Role" : "Senior Student", "Region": "Johto", "Named" : False, "Value" : 0, "Contact": False, "Sex": Genders.Male, "Relationship": "Underclassman", "RelationshipRank": 0, "Events": [], "Mood": 0, "Nature": TrainerNature.Special, "Color": "#1d8fc5", "Image": "falkner", "Direction": "Left"},
    "Leaf" : {"Role" : "Student", "Region": "Kanto", "Named" : False, "Value" : 0, "Contact": False, "Sex": Genders.Female, "Relationship": "Friend", "RelationshipRank": 0, "Events": [], "Mood": 0, "Nature": TrainerNature.Devoted, "Color": "#00b23f", "Image": "leaf", "Direction": "Left"},
    "Ethan" : {"Role" : "Student", "Region": "Johto", "Named" : False, "Value" : 0, "Contact": False, "Sex": Genders.Male, "Relationship": "Friend", "RelationshipRank": 0, "Events": [], "Mood": 0, "Nature": TrainerNature.Distant, "Color": "#c1861e", "Image": "ethan", "Direction": "Front"},
    "Calem" : {"Role" : "Student", "Region": "Kalos", "Named" : False, "Value" : 0, "Contact": False, "Sex": Genders.Male, "Relationship": "Friend", "RelationshipRank": 0, "Events": [], "Mood": 0, "Nature": TrainerNature.Friendly, "Color": "#4d7ac4", "Image": "calem", "Direction": "Right"},
    "Hilbert" : {"Role" : "Student", "Region": "Unova", "Named" : False, "Value" : 0, "Contact": False, "Sex": Genders.Male, "Relationship": "Dormmate", "RelationshipRank": 0, "Events": [], "Mood": 0, "Nature": TrainerNature.Moody, "Color": "#353535", "Image": "hilbert", "Direction": "Left"},
    "Brendan" : {"Role" : "Student", "Region": "Hoenn", "Named" : False, "Value" : 0, "Contact": False, "Sex": Genders.Male, "Relationship": "Friend", "RelationshipRank": 0, "Events": [], "Mood": 0, "Nature": TrainerNature.Friendly, "Color": "#db4039", "Image": "brendan", "Direction": "Left"},
    "May" : {"Role" : "Student", "Region": "Hoenn", "Named" : False, "Value" : 0, "Contact": False, "Sex": Genders.Female, "Relationship": "Friend", "RelationshipRank": 0, "Events": [], "Mood": 0, "Nature": TrainerNature.Neutral, "Color": "#493bff", "Image": "may", "Direction": "Front"},
    "Flannery" : {"Role" : "Student", "Region": "Hoenn", "Named" : False, "Value" : 0, "Contact": False, "Sex": Genders.Female, "Relationship": "Friend", "RelationshipRank": 0, "Events": [], "Mood": 0, "Nature": TrainerNature.Moody, "Color": "#d62e0d", "Image": "flannery", "Direction": "Right"},
    "Whitney" : {"Role" : "Student", "Region": "Johto", "Named" : False, "Value" : 0, "Contact": False, "Sex": Genders.Female, "Relationship": "Friend", "RelationshipRank": 0, "Events": [], "Mood": 0, "Nature": TrainerNature.Friendly, "Color": "#e47282", "Image": "whitney", "Direction": "Front"},
    "Sabrina" : {"Role" : "Student", "Region": "Kanto", "Named" : False, "Value" : 0, "Contact": False, "Sex": Genders.Female, "Relationship": "Classmate", "RelationshipRank": 0, "Events": [], "Mood": 0, "Nature": TrainerNature.Distant, "Color": "#600080", "Image": "sabrina", "Direction": "Left"},
    "Serena" : {"Role" : "Student", "Region": "Kalos", "Named" : False, "Value" : 0, "Contact": False, "Sex": Genders.Female, "Relationship": "Friend", "RelationshipRank": 0, "Events": [], "Mood": 0, "Nature": TrainerNature.Neutral, "Color": "#cb6e8b", "Image": "serena", "Direction": "Right"},
    "Cheren" : {"Role" : "Student", "Region": "Unova", "Named" : False, "Value" : 0, "Contact": False, "Sex": Genders.Male, "Relationship": "Political Rival", "RelationshipRank": 0, "Events": [], "Mood": 0, "Nature": TrainerNature.Distant, "Color": "#1f67df", "Image": "cheren", "Direction": "Right"},
    "Misty" : {"Role" : "Student", "Region": "Kanto", "Named" : False, "Value" : 0, "Contact": False, "Sex": Genders.Female, "Relationship": "Classmate", "RelationshipRank": 0, "Events": [], "Mood": 0, "Nature": TrainerNature.Moody, "Color": "#eb6400", "Image": "misty", "Direction": "Left"},
    "Bianca" : {"Role" : "Student", "Region": "Unova", "Named" : False, "Value" : 0, "Contact": False, "Sex": Genders.Female, "Relationship": "Friend", "RelationshipRank": 0, "Events": [], "Mood": 0, "Nature": TrainerNature.Friendly, "Color": "#55b13c", "Image": "bianca", "Direction": "Front"},
    "Dawn" : {"Role" : "Student", "Region": "Sinnoh", "Named" : False, "Value" : 0, "Contact": False, "Sex": Genders.Female, "Relationship": "Classmate", "RelationshipRank": 0, "Events": [], "Mood": 0, "Nature": TrainerNature.Neutral, "Color": "#cc8fdb", "Image": "dawn", "Direction": "Front"},
    "Nate" : {"Role" : "Student", "Region": "Unova", "Named" : False, "Value" : 0, "Contact": False, "Sex": Genders.Male, "Relationship": "Friend", "RelationshipRank": 0, "Events": [], "Mood": 0, "Nature": TrainerNature.Friendly, "Color": "#36A8CB", "Image": "nate", "Direction": "Right"},
    "Rosa" : {"Role" : "Student", "Region": "Unova", "Named" : False, "Value" : 0, "Contact": False, "Sex": Genders.Female, "Relationship": "Friend", "RelationshipRank": 0, "Events": [], "Mood": 0, "Nature": TrainerNature.Neutral, "Color": "#ff5a73", "Image": "rosa", "Direction": "Left"},
    "Bea" : {"Role" : "Student", "Region": "Galar", "Named" : False, "Value" : 0, "Contact": False, "Sex": Genders.Female, "Relationship": "Training Partner", "RelationshipRank": 0, "Events": [], "Mood": 0, "Nature": TrainerNature.Neutral, "Color": "#F87816", "Image": "bea", "Direction": "Right"},
    "Nessa" : {"Role" : "Student", "Region": "Galar", "Named" : False, "Value" : 0, "Contact": False, "Sex": Genders.Female, "Relationship": "Date", "RelationshipRank": 0, "Events": [], "Mood": 0, "Nature": TrainerNature.Neutral, "Color": "#5B81D9", "Image": "nessa", "Direction": "Left"},
    "Hilda" : {"Role" : "Student", "Region": "Unova", "Named" : False, "Value" : 0, "Contact": False, "Sex": Genders.Female, "Relationship": "Friend", "RelationshipRank": 0, "Events": [], "Mood": 0, "Nature": TrainerNature.Moody, "Color": "#ea5091", "Image": "hilda", "Direction": "Left"},
    "Gardenia" : {"Role" : "Student", "Region": "Sinnoh", "Named" : False, "Value" : 0, "Contact": False, "Sex": Genders.Female, "Relationship": "Friend", "RelationshipRank": 0, "Events": [], "Mood": 0, "Nature": TrainerNature.Friendly, "Color": "#00712b", "Image": "gardenia", "Direction": "Left"},
    "Skyla" : {"Role" : "Student", "Region": "Unova", "Named" : False, "Value" : 0, "Contact": False, "Sex": Genders.Female, "Relationship": "Friend", "RelationshipRank": 0, "Events": [], "Mood": 0, "Nature": TrainerNature.Friendly, "Color": "#5c87b9", "Image": "skyla", "Direction": "Right"},
    "Brock" : {"Role" : "?", "Region": "Kanto", "Named" : False, "Value" : 0, "Contact": False, "Sex": Genders.Male, "Relationship": "Student", "RelationshipRank": 0, "Events": [], "Mood": 0, "Nature": TrainerNature.Special, "Color": "#6D211D", "Image": "brock", "Direction": "Right"},
    "Erika" : {"Role" : "Student", "Region": "Kanto", "Named" : False, "Value" : 0, "Contact": False, "Sex": Genders.Female, "Relationship": "Friend", "RelationshipRank": 0, "Events": [], "Mood": 0, "Nature": TrainerNature.Distant, "Color": "#34a59a", "Image": "erika", "Direction": "Left"},
    "Janine" : {"Role" : "Senior Student", "Region": "Johto", "Named" : False, "Value" : 0, "Contact": False, "Sex": Genders.Female, "Relationship": "Tool", "RelationshipRank": 0, "Events": [], "Mood": 0, "Nature": TrainerNature.Special, "Color": "#6f4097", "Image": "janine", "Direction": "Right"},
    "Tia" : {"Role" : "Student", "Region": "Hoenn", "Named" : False, "Value" : 0, "Contact": False, "Sex": Genders.Female, "Relationship": "Protector", "RelationshipRank": 0, "Events": [], "Mood": 0, "Nature": TrainerNature.Devoted, "Color": "#C96A70", "Image": "tia", "Direction": "Left"},
    "Sonia" : {"Role" : "Student", "Region": "Galar", "Named" : False, "Value" : 0, "Contact": False, "Sex": Genders.Female, "Relationship": "Classmate", "RelationshipRank": 0, "Events": [], "Mood": 0, "Nature": TrainerNature.Neutral, "Color": "#F19272", "Image": "sonia", "Direction": "Left"},
    "Jasmine" : {"Role" : "Student", "Region": "Johto", "Named" : False, "Value" : 0, "Contact": False, "Sex": Genders.Female, "Relationship": "Political Rival", "RelationshipRank": 0, "Events": [], "Mood": 0, "Nature": TrainerNature.Friendly, "Color": "#939393", "Image": "jasmine", "Direction": "Left"},
    "Grusha" : {"Role" : "Student", "Region": "Paldea", "Named" : False, "Value" : 0, "Contact": False, "Sex": Genders.Male, "Relationship": "Political Rival", "RelationshipRank": 0, "Events": [], "Mood": 0, "Nature": TrainerNature.Moody, "Color": "#00b8d0", "Image": "grusha", "Direction": "Left"},
    "Professor Cherry" : {"Role" : "Staff", "Region": "Johto", "Named" : False, "Value" : 0, "Contact": False, "Sex": Genders.Female, "Relationship": "Student", "RelationshipRank": 0, "Events": [], "Mood": 0, "Nature": TrainerNature.Distant, "Color": "#1dcc88", "Image": "kris", "Direction": "Right"},
    "Instructor Lenora" : {"Role" : "Staff", "Region": "Unova", "Named" : False, "Value" : 0, "Contact": False, "Sex": Genders.Female, "Relationship": "Student", "RelationshipRank": 0, "Events": [], "Mood": 0, "Nature": TrainerNature.Special, "Color": "#aa4a1b", "Image": "lenora", "Direction": "Right"},
    "Instructor Blaine" : {"Role" : "Staff", "Region": "Kanto", "Named" : False, "Value" : 0, "Contact": False, "Sex": Genders.Male, "Relationship": "Student", "RelationshipRank": 0, "Events": [], "Mood": 0, "Nature": TrainerNature.Special, "Color": "#cd5733", "Image": "blaine", "Direction": "Right"},
    "Instructor Wallace" : {"Role" : "Staff", "Region": "Hoenn", "Named" : False, "Value" : 0, "Contact": False, "Sex": Genders.Male, "Relationship": "Student", "RelationshipRank": 0, "Events": [], "Mood": 0, "Nature": TrainerNature.Special, "Color": "#46897c", "Image": "wallace", "Direction": "Right"},
    "Instructor Ramos" : {"Role" : "Staff", "Region": "Kalos", "Named" : False, "Value" : 0, "Contact": False, "Sex": Genders.Male, "Relationship": "Student", "RelationshipRank": 0, "Events": [], "Mood": 0, "Nature": TrainerNature.Special, "Color": "#657f61", "Image": "ramos", "Direction": "Right"},
    "Lieutenant Surge" : {"Role" : "Staff", "Region": "Kanto", "Named" : False, "Value" : 0, "Contact": False, "Sex": Genders.Male, "Relationship": "Student", "RelationshipRank": 0, "Events": [], "Mood": 0, "Nature": TrainerNature.Special, "Color": "#545241", "Image": "surge", "Direction": "Front"},
    "Instructor Melony" : {"Role" : "Staff", "Region": "Galar", "Named" : False, "Value" : 0, "Contact": False, "Sex": Genders.Female, "Relationship": "Student", "RelationshipRank": 0, "Events": [], "Mood": 0, "Nature": TrainerNature.Special, "Color": "#288cff", "Image": "melony", "Direction": "Front"},
    "Sensei Marshal" : {"Role" : "Staff", "Region": "Unova", "Named" : False, "Value" : 0, "Contact": False, "Sex": Genders.Male, "Relationship": "Grasshopper", "RelationshipRank": 0, "Events": [], "Mood": 0, "Nature": TrainerNature.Special, "Color": "#6e492d", "Image": "marshal", "Direction": "Right"},
    "Instructor Koga" : {"Role" : "Staff", "Region": "Kanto", "Named" : False, "Value" : 0, "Contact": False, "Sex": Genders.Male, "Relationship": "Student", "RelationshipRank": 0, "Events": [], "Mood": 0, "Nature": TrainerNature.Special, "Color": "#5f3869", "Image": "koga", "Direction": "Right"},
    "Instructor Bertha" : {"Role" : "Staff", "Region": "Sinnoh", "Named" : False, "Value" : 0, "Contact": False, "Sex": Genders.Female, "Relationship": "Student", "RelationshipRank": 0, "Events": [], "Mood": 0, "Nature": TrainerNature.Special, "Color": "#906438", "Image": "bertha", "Direction": "Front"},
    "Instructor Will" : {"Role" : "Staff", "Region": "Johto", "Named" : False, "Value" : 0, "Contact": False, "Sex": Genders.Male, "Relationship": "Student", "RelationshipRank": 0, "Events": [], "Mood": 0, "Nature": TrainerNature.Special, "Color": "#664f79", "Image": "will", "Direction": "Left"},
    "Burgh" : {"Role" : "Staff", "Region": "Unova", "Named" : False, "Value" : 0, "Contact": False, "Sex": Genders.Male, "Relationship": "Student", "RelationshipRank": 0, "Events": [], "Mood": 0, "Nature": TrainerNature.Special, "Color": "#71a230", "Image": "burgh", "Direction": "Right"},
    "Instructor Olivia" : {"Role" : "Staff", "Region": "Alola", "Named" : False, "Value" : 0, "Contact": False, "Sex": Genders.Female, "Relationship": "Student", "RelationshipRank": 0, "Events": [], "Mood": 0, "Nature": TrainerNature.Special, "Color": "#595554", "Image": "olivia", "Direction": "Left"},
    "Instructrice Fantina" : {"Role" : "Staff", "Region": "Sinnoh", "Named" : False, "Value" : 0, "Contact": False, "Sex": Genders.Female, "Relationship": "Student", "RelationshipRank": 0, "Events": [], "Mood": 0, "Nature": TrainerNature.Special, "Color": "#784972", "Image": "fantina", "Direction": "Front"},
    "Instructor Karen" : {"Role" : "Staff", "Region": "Johto", "Named" : False, "Value" : 0, "Contact": False, "Sex": Genders.Female, "Relationship": "Student", "RelationshipRank": 0, "Events": [], "Mood": 0, "Nature": TrainerNature.Special, "Color": "#314876", "Image": "karen", "Direction": "Left"},
    "Instructor Clair" : {"Role" : "Staff", "Region": "Johto", "Named" : False, "Value" : 0, "Contact": False, "Sex": Genders.Female, "Relationship": "Student", "RelationshipRank": 0, "Events": [], "Mood": 0, "Nature": TrainerNature.Special, "Color": "#5a94c6", "Image": "clair", "Direction": "Left"},
    "Instructor Byron" : {"Role" : "Staff", "Region": "Sinnoh", "Named" : False, "Value" : 0, "Contact": False, "Sex": Genders.Male, "Relationship": "Student", "RelationshipRank": 0, "Events": [], "Mood": 0, "Nature": TrainerNature.Special, "Color": "#4a4a5b", "Image": "byron", "Direction": "Left"},
    "Instructor Valerie" : {"Role" : "Staff", "Region": "Kalos", "Named" : False, "Value" : 0, "Contact": False, "Sex": Genders.Female, "Relationship": "Student", "RelationshipRank": 0, "Events": [], "Mood": 0, "Nature": TrainerNature.Special, "Color": "#de5b99", "Image": "valerie", "Direction": "Right"},
    "Instructor Winona" : {"Role" : "Staff", "Region": "Hoenn", "Named" : False, "Value" : 0, "Contact": False, "Sex": Genders.Female, "Relationship": "Student", "RelationshipRank": 0, "Events": [], "Mood": 0, "Nature": TrainerNature.Special, "Color": "#52adbe", "Image": "winona", "Direction": "Left"},
    "Bruno" : {"Role" : "Staff", "Region": "Kanto", "Named" : False, "Value" : 0, "Contact": False, "Sex": Genders.Male, "Relationship": "Student", "RelationshipRank": 0, "Events": [], "Mood": 0, "Nature": TrainerNature.Special, "Color": "#585355", "Image": "bruno", "Direction": "Left"},
    "Alder" : {"Role" : "Staff", "Region": "Unova", "Named" : False, "Value" : 0, "Contact": False, "Sex": Genders.Male, "Relationship": "Student", "RelationshipRank": 0, "Events": [], "Mood": 0, "Nature": TrainerNature.Special, "Color": "#af4c2e", "Image": "alder", "Direction": "Right"},
    "Lance" : {"Role" : "Staff", "Region": "Kanto", "Named" : False, "Value" : 0, "Contact": False, "Sex": Genders.Male, "Relationship": "Student", "RelationshipRank": 0, "Events": [], "Mood": 0, "Nature": TrainerNature.Special, "Color": "#16367a", "Image": "lance", "Direction": "Front"},
    "Iris" : {"Role" : "Champion", "Region": "Unova", "Named" : False, "Value" : 0, "Contact": False, "Sex": Genders.Female, "Relationship": "Mentor", "RelationshipRank": 0, "Events": [], "Mood": 0, "Nature": TrainerNature.Special, "Color": "#82007e", "Image": "iris", "Direction": "Left"},
    "Dean Drayden" : {"Role" : "Staff", "Region": "Unova", "Named" : False, "Value" : 0, "Contact": False, "Sex": Genders.Male, "Relationship": "Mentor", "RelationshipRank": 0, "Events": [], "Mood": 0, "Nature": TrainerNature.Special, "Color": "#583C68", "Image": "drayden", "Direction": "Front"},
    "Yellow" : {"Role" : "Student", "Region": "Kanto", "Named" : False, "Value" : 0, "Contact" : False, "Sex": Genders.Female, "Relationship": "Dormmate", "RelationshipRank": 0, "Events": [], "Mood": 0, "Nature": TrainerNature.Special, "Color": "#f2a634", "Image": "yellow", "Direction": "Left"},
    "Lisia" : {"Role" : "Staff", "Region": "Hoenn", "Named" : False, "Value" : 0, "Contact" : False, "Sex": Genders.Female, "Relationship": "Mentee", "RelationshipRank": 0, "Events": [], "Mood": 0, "Nature": TrainerNature.Special, "Color": "#71BBA2", "Image": "lisia", "Direction": "Left"},
    "Wally" : {"Role" : "Student", "Region": "Hoenn", "Named" : False, "Value" : 0, "Contact" : False, "Sex": Genders.Male, "Relationship": "Classmate", "RelationshipRank": 0, "Events": [], "Mood": 0, "Nature": TrainerNature.Neutral, "Color": "#377227", "Image": "wally", "Direction": "Right"},
    "Nurse Miriam" : {"Role" : "Staff", "Region": "Paldea", "Named" : False, "Value" : 0, "Contact" : False, "Sex": Genders.Female, "Relationship": "Patient", "RelationshipRank": 0, "Events": [], "Mood": 0, "Nature": TrainerNature.Special, "Color": "#966EFF", "Image": "miriam", "Direction": "Left"},
    "Raihan" : {"Role" : "Student", "Region": "Galar", "Named" : False, "Value" : 0, "Contact" : False, "Sex": Genders.Male, "Relationship": "Acquaintance", "RelationshipRank": 0, "Events": [], "Mood": 0, "Nature": TrainerNature.Neutral, "Color": "#EB5334", "Image": "raihan", "Direction": "Front"},
    "Eri" : {"Role" : "Forthcoming", "Region": "Paldea", "Named" : False, "Value" : 0, "Contact" : False, "Sex": Genders.Female, "Relationship": "Mentee", "RelationshipRank": 0, "Events": [], "Mood": 0, "Nature": TrainerNature.Special, "Color": "#3C468D", "Image": "eri", "Direction": "Right"},
    "Anabel" : {"Role" : "Offcampus", "Region": "Hoenn", "Named" : False, "Value" : 0, "Contact" : False, "Sex": Genders.Female, "Relationship": "Liability", "RelationshipRank": 0, "Events": [], "Mood": 0, "Nature": TrainerNature.Special, "Color": "#a367c0", "Image": "anabel", "Direction": "Left"},
    "Mallow" : {"Role" : "Student", "Region": "Alola", "Named" : False, "Value" : 0, "Contact" : False, "Sex": Genders.Female, "Relationship": "Classmate", "RelationshipRank": 0, "Events": [], "Mood": 0, "Nature": TrainerNature.Special, "Color": "#608946", "Image": "mallow", "Direction": "Right"},
    "Allister" : {"Role" : "Offcampus", "Region": "Galar", "Named" : False, "Value" : 0, "Contact" : False, "Sex": Genders.Male, "Relationship": "None", "RelationshipRank": 0, "Events": [], "Mood": 0, "Nature": TrainerNature.Special, "Color": "#9C96C5", "Image": "allister", "Direction": "Left"},
    "Lawrence" : {"Role" : "Offcampus", "Region": "Johto", "Named" : False, "Value" : 0, "Contact" : False, "Sex": Genders.Male, "Relationship": "Benefactee", "RelationshipRank": 0, "Events": [], "Mood": 0, "Nature": TrainerNature.Special, "Color": "#333", "Image": "phobos", "Direction": "Front"},
    "Klara" : {"Role" : "Student", "Region": "Galar", "Named" : False, "Value" : 0, "Contact" : False, "Sex": Genders.Female, "Relationship": "Crush", "RelationshipRank": 0, "Events": [], "Mood": 0, "Nature": TrainerNature.Devoted, "Color": "#EE8FB5", "Image": "klara", "Direction": "Left"},
    "Melody" : {"Role" : "Student", "Region": "Johto", "Named" : False, "Value" : 0, "Contact" : False, "Sex": Genders.Female, "Relationship": "Classmate", "RelationshipRank": 0, "Events": [], "Mood": 0, "Nature": TrainerNature.Special, "Color": "#FF8D6C", "Image": "melody", "Direction": "Right"},
    "Kate" : {"Role" : "Ranger", "Region": "Almia", "Named" : False, "Value" : 0, "Contact" : False, "Sex": Genders.Female, "Relationship": "Citizen", "RelationshipRank": 0, "Events": [], "Mood": 0, "Nature": TrainerNature.Special, "Color": "#59BB83", "Image": "kate", "Direction": "Right"},
    "Summer" : {"Role" : "Ranger", "Region": "Oblivia", "Named" : False, "Value" : 0, "Contact" : False, "Sex": Genders.Female, "Relationship": "Citizen", "RelationshipRank": 0, "Events": [], "Mood": 0, "Nature": TrainerNature.Special, "Color": "#EF2F30", "Image": "summer", "Direction": "Right"},
    "Shauna" : {"Role" : "Student", "Region": "Kalos", "Named" : False, "Value" : 0, "Contact" : False, "Sex": Genders.Female, "Relationship": "Classmate", "RelationshipRank": 0, "Events": [], "Mood": 0, "Nature": TrainerNature.Special, "Color": "#E779AC", "Image": "shauna", "Direction": "Left"},
    "Professor Rowan" : {"Role" : "Staff", "Region": "Sinnoh", "Named" : False, "Value" : 0, "Contact" : False, "Sex": Genders.Male, "Relationship": "Student", "RelationshipRank": 0, "Events": [], "Mood": 0, "Nature": TrainerNature.Special, "Color": "#3A4D7E", "Image": "rowan", "Direction": "Right"},
    "Zinnia" : {"Role" : "Student", "Region": "Hoenn", "Named" : False, "Value" : 0, "Contact" : False, "Sex": Genders.Female, "Relationship": "None", "RelationshipRank": 0, "Events": [], "Mood": 0, "Nature": TrainerNature.Special, "Color": "#50C878", "Image": "zinnia", "Direction": "Front"},
    "Iono" : {"Role" : "Student", "Region": "Paldea", "Named" : False, "Value" : 0, "Contact" : False, "Sex": Genders.Female, "Relationship": "Collaborator", "RelationshipRank": 0, "Events": [], "Mood": 0, "Nature": TrainerNature.Distant, "Color": "#EE8FB5", "Image": "iono", "Direction": "Left"},
    "Duplica" : {"Role" : "Offcampus", "Region": "Kanto", "Named" : False, "Value" : 0, "Contact" : False, "Sex": Genders.Female, "Relationship": "Faker", "RelationshipRank": 0, "Events": [], "Mood": 0, "Nature": TrainerNature.Special, "Color": "#737373", "Image": "duplica", "Direction": "Left"},
    "Wes" : {"Role" : "Offcampus", "Region": "Orre", "Named" : False, "Value" : 0, "Contact" : False, "Sex": Genders.Male, "Relationship": "Hero", "RelationshipRank": 0, "Events": [], "Mood": 0, "Nature": TrainerNature.Special, "Color": "#135C87", "Image": "wes", "Direction": "Right"},
    "Cynthia" : {"Role" : "Champion", "Region": "Sinnoh", "Named" : True, "Value" : 0, "Contact" : False, "Sex": Genders.Female, "Relationship": "Unmet", "RelationshipRank": 0, "Events": [], "Mood": 0, "Nature": TrainerNature.Special, "Color": "#cfb000", "Image": "cynthia", "Direction": "Left"},
    "Shauntal" : {"Role" : "Offcampus", "Region": "Unova", "Named" : False, "Value" : 0, "Contact" : False, "Sex": Genders.Female, "Relationship": "Acquaintance", "RelationshipRank": 0, "Events": [], "Mood": 0, "Nature": TrainerNature.Special, "Color": "#FF9D8F", "Image": "shauntal", "Direction": "Right"},
    "Morty" : {"Role" : "Student", "Region": "Johto", "Named" : False, "Value" : 0, "Contact" : False, "Sex": Genders.Male, "Relationship": "Classmate", "RelationshipRank": 0, "Events": [], "Mood": 0, "Nature": TrainerNature.Special, "Color": "#A0528B", "Image": "morty", "Direction": "Left"},
    "Bugsy" : {"Role" : "Student", "Region": "Johto", "Named" : False, "Value" : 0, "Contact" : False, "Sex": Genders.Unknown, "Relationship": "Classmate", "RelationshipRank": 0, "Events": [], "Mood": 0, "Nature": TrainerNature.Special, "Color": "#00c54b", "Image": "bugsy", "Direction": "Front"},
    "Roark" : {"Role" : "Student", "Region": "Sinnoh", "Named" : False, "Value" : 0, "Contact" : False, "Sex": Genders.Male, "Relationship": "Acquaintance", "RelationshipRank": 0, "Events": [], "Mood": 0, "Nature": TrainerNature.Special, "Color": "#ff5121", "Image": "roark", "Direction": "Right"},
    "Caitlin" : {"Role" : "Offcampus", "Region": "Unova", "Named" : False, "Value" : 0, "Contact" : False, "Sex": Genders.Female, "Relationship": "Unknown", "RelationshipRank": 0, "Events": [], "Mood": 0, "Nature": TrainerNature.Special, "Color": "#ff54e5", "Image": "caitlin", "Direction": "Left"},
    "Professor Sycamore" : {"Role" : "Staff", "Region": "Kalos", "Named" : False, "Value" : 0, "Contact" : False, "Sex": Genders.Male, "Relationship": "Student", "RelationshipRank": 0, "Events": [], "Mood": 0, "Nature": TrainerNature.Special, "Color": "#4B5A9A", "Image": "sycamore", "Direction": "Front"}
}

init python:
    imageToCharDict = {}
    for key, value in defaultpersondex.items():
        imageToCharDict[value["Image"]] = key

default dateabase = {
    "Kisses": [],
    "Dates": [],
    "Known Locations": [],
    "Romantic Entanglements": [],
    "Casual Entanglements": [],
    "Cross Knowledge": {}#a dictionary with character names, and a list of all the other characters that character knows you're romantically entangled with
}

init python:
    def RecordKiss(character):
        dateabase["Kisses"].append(character)

    def RecordDate(character):
        dateabase["Dates"].append(character)
    
    def RecordKnownLocations(character, location):
        if (not HasLocation(location)):
            dateabase["Known Locations"].append((character, location))

    def HasLocation(location):
        for char, loc in dateabase["Known Locations"]:
            if (loc == location):
                return True
        return False
        
    def RecordRomanticRelationship(character):
        RecordKiss(character)
        dateabase["Romantic Entanglements"].append(character)
    
    def RecordCasualRelationship(character):
        RecordKiss(character)
        dateabase["Casual Entanglements"].append(character)

    def RomanticallyEntangled(character):
        return character in dateabase["Romantic Entanglements"]

    def GetCrossKnown(knower, one = True):
        if knower in dateabase["Cross Knowledge"]:
            if (one):
                return dateabase["Cross Knowledge"][0]
            else:
                return dateabase["Cross Knowledge"]
        return ""

    def HasCrossKnowledge(knower, knowee):
        if (knowee == "Any"):
            return knower in dateabase["Cross Knowledge"] and len(dateabase["Cross Knowledge"][knower]) > 0
        else:
            return knower in dateabase["Cross Knowledge"] and knowee in dateabase["Cross Knowledge"][knower]

    def RecordCrossKnowledge(knower, knowee):
        if (knower not in dateabase["Cross Knowledge"]):
            dateabase["Cross Knowledge"][knower] = []
        dateabase["Cross Knowledge"][knower].append(knowee)

default first_name = "You"
default last_name = "Sugimori"
default pika_name = "Your Pikachu"
default blue_name = "Blue"

#The Champion
define cynthia = CustomCharacter("Cynthia", "#cfb000", "cynthia")

define oak = CustomCharacter("Professor Oak", "#000000", "oak")
define pikachu = CustomCharacter("Pikachu", "#fca600", "pikachu")
define libpikachu = CustomCharacter("Pikachu", "#fca600", "libpikachu")
define cospikachu = CustomCharacter("Chuchu", "#fca600", "cospikachu")
define starter = CustomCharacter("Your Starter", "#fca600", "starterportrait")
define red = CustomCharacter("Red", "#cf0000", "red")
define redmind = CustomCharacter("You", "#cf0000", "red")
define mom = CustomCharacter("Mom", "#b7669e", "mom")
define dad = CustomCharacter("Dad", "#234099", None)

#students
define blue = CustomCharacter("Blue", "#3110dd", "blue")
define bluemind = CustomCharacter("You", "#3110dd", "blue")
define silver = CustomCharacter("Silver", "#686080", "silver")
define face = CustomCharacter("Ace Student F", "#C89BE3", "face")
define mace = CustomCharacter("Ace Student M", "#665787", "mace")
define leaf = CustomCharacter("Leaf", "#00b23f", "leaf")
define leafmind = CustomCharacter("You", "#00b23f", "leaf")
define leafdate = CustomCharacter("Leaf",  "#00b23f", "leafdate")
define ethan = CustomCharacter("Ethan", "#c1861e", "ethan")
define ethanmind = CustomCharacter("You", "#c1861e", "ethan")
define calem = CustomCharacter("Calem", "#4d7ac4", "calem")
define hilbert = CustomCharacter("Hilbert", "#353535", "hilbert")
define brendan = CustomCharacter("Brendan", "#db4039", "brendan")
define may = CustomCharacter("May", "#493bff", "may")
define flannery = CustomCharacter("Flannery", "#d62e0d", "flannery")
define whitney = CustomCharacter("Whitney", "#e47282", "whitney")
define whitneymind = CustomCharacter("You", "#e47282", "whitney")
define secondwhitney = CustomCharacter("You", "#e47282", "secondwhitney")
define sabrina = CustomCharacter("Sabrina", "#600080", "sabrina")
define serena = CustomCharacter("Serena", "#cb6e8b", "serena")
define cheren = CustomCharacter("Cheren", "#1f67df", "cheren")
define cherenmind = CustomCharacter("You", "#1f67df", "cheren")
define misty = CustomCharacter("Misty", "#eb6400", "misty")
define bianca = CustomCharacter("Bianca", "#55b13c", "bianca")
define dawn = CustomCharacter("Dawn", "#cc8fdb", "dawn")
define nate = CustomCharacter("Nate", "#36A8CB", "nate")
define rosa = CustomCharacter("Rosa", "#ff5a73", "rosa")
define bea = CustomCharacter("Bea", "#F87816", "bea")
define beamind = CustomCharacter("You", "#F87816", "bea")
define nessa = CustomCharacter("Nessa", "#5B81D9", "nessa")
define hilda = CustomCharacter("Hilda", "#ea5091", "hilda")
define hildamind = CustomCharacter("You", "#ea5091", "hilda")
define gardenia = CustomCharacter("Gardenia", "#00712b", "gardenia")
define skyla = CustomCharacter("Skyla", "#5c87b9", "skyla")
define skylatease = CustomCharacter("Skyla", "#5c87b9", "skylatease")
define erika = CustomCharacter("Erika", "#34a59a", "erika")
define tia = CustomCharacter("Tia", "#C96A70", "tia")
define latias = CustomCharacter("Tia", "#C96A70", "latias")
define sonia = CustomCharacter("Sonia", "#F19272", "sonia")
define jasmine = CustomCharacter("Jasmine", "#939393", "jasmine")
define grusha = CustomCharacter("Grusha", "#00b8d0", "grusha")
define yellow = CustomCharacter("Yellow", "#f2a634", "yellow")
define wally = CustomCharacter("Wally", "#377227", "wally")
define raihan = CustomCharacter("Raihan", "#EB5334", "raihan")
define eri = CustomCharacter("Eri", "#3C468D", "eri")
define mallow = CustomCharacter("Mallow", "#608946", "mallow")
define klara = CustomCharacter("Klara", "#EE8FB5", "klara")
define melody = CustomCharacter("Melody", "#FF8D6C", "melody")
define shauna = CustomCharacter("Shauna", "#E779AC", "shauna")
define zinnia = CustomCharacter("Zinnia", "#50C878", "zinnia")
define iono = CustomCharacter("Iono", "#EE8FB5", "iono")
define morty = CustomCharacter("Morty", "#A0528B", "morty")
define bugsy = CustomCharacter("Bugsy", "#00c54b", "bugsy")

#Not technically students
define brawly = CustomCharacter("Brawly", "#467595", "brawly")
define roxanne = CustomCharacter("Roxanne", "#a2254b", "roxanne")
define falkner = CustomCharacter("Falkner", "#1d8fc5", "falkner")
define janine = CustomCharacter("Janine", "#6f4097", "janine")
define iris = CustomCharacter("Iris", "#82007e", "iris")
define brock = CustomCharacter("Brock", "#6D211D", "brock")
define lisia = CustomCharacter("Lisia", "#71BBA2", "lisia")
define lisiamind = CustomCharacter("You", "#71BBA2", "lisia")
define duplica = CustomCharacter("Duplica", "#737373", "duplica")
define wes = CustomCharacter("Wes", "#135C87", "wes")

#type instructors
define lenora = CustomCharacter("Instructor Lenora", "#aa4a1b", "lenora")
define blaine = CustomCharacter("Instructor Blaine", "#cd5733", "blaine")
define wallace = CustomCharacter("Instructor Wallace", "#46897c", "wallace")
define ramos = CustomCharacter("Instructor Ramos", "#657f61", "ramos")
define surge = CustomCharacter("Lieutenant Surge", "#545241", "surge")
define melony  = CustomCharacter("Instructor Melony", "#288cff", "melony")
define marshal = CustomCharacter("Sensei Marshal", "#6e492d", "marshal")
define koga = CustomCharacter("Instructor Koga", "#5f3869", "koga")
define bertha = CustomCharacter("Instructor Bertha", "#906438", "bertha")
define winona = CustomCharacter("Instructor Winona", "#52adbe", "winona")
define will = CustomCharacter("Instructor Will", "#664f79", "will")
define burgh = CustomCharacter("Burgh", "#71a230", "burgh")
define olivia = CustomCharacter("Instructor Olivia", "#595554", "olivia")
define fantina = CustomCharacter("Instructrice Fantina", "#784972", "fantina")
define karen = CustomCharacter("Instructor Karen", "#314876", "karen")
define clair = CustomCharacter("Instructor Clair", "#5a94c6", "clair")
define byron = CustomCharacter("Instructor Byron", "#4a4a5b", "byron")
define valerie = CustomCharacter("Instructor Valerie", "#de5b99", "valerie")

#other staff
define bruno = CustomCharacter("Bruno", "#585355", "bruno")
define alder = CustomCharacter("Alder", "#af4c2e", "alder")
define lance = CustomCharacter("Lance", "#16367a", "lance")
define kris = CustomCharacter("Professor Cherry", "#1dcc88", "kris")
define drayden = CustomCharacter("Dean Drayden", "#583C68", "drayden")
define miriam = CustomCharacter("Nurse Miriam", "#966EFF", "miriam")
define rowan = CustomCharacter("Professor Rowan", "#3A4D7E", "rowan")
define sycamore = CustomCharacter("Professor Sycamore", "#4B5A9A", "sycamore")

#others...?
define narrator = CustomCharacter("", "#000", "")
define dungeonnarrator = CustomCharacter("DungeonNarrator", "#000", "")
define dn = dungeonnarrator
define security = CustomCharacter("Security", "#ff4400", "")
define roughneck = CustomCharacter("Roughneck", "#ff4400", "roughneck")
define roughneck2 = CustomCharacter("Toughneck", "#ff4400", "roughneck2")
define roughneck3 = CustomCharacter("Buffneck", "#ff4400", "roughneck3")
define hiker = CustomCharacter("Burly Man", "#ff4400", "hiker")
define hiker2 = CustomCharacter("Brawny Man", "#ff4400", "hiker2")
define hiker3 = CustomCharacter("Boisterous Man", "#ff4400", "hiker3")
define silhouettebunny = CustomCharacter("Buxom Bunny", "#ff4400", "silhouettebunny")
define silhouettebunny2 = CustomCharacter("Ravishing Rabbit", "#ff4400", "silhouettebunny2")
define silhouettebunny3 = CustomCharacter("Languid Lepine", "#ff4400", "silhouettebunny3")
define femthug = CustomCharacter("Punk Girl", "#ff4400", "femthug")
define hexmaniac = CustomCharacter("Hex Maniac", "#ff4400", "hexmaniac")
define sidemon = CustomCharacter("Sidemon", "#000", "sidemonportrait")
define lace = CustomCharacter("Lady Ace Trainer", "#6E7AA8", "lace")
define oldman = CustomCharacter("Old Man", "#C68C28", "oldman")
define anabel = CustomCharacter("Anabel", "#a367c0", "anabel")
define allister = CustomCharacter("Allister", "#9C96C5", "allister")
define phobos = CustomCharacter("Lawrence", "#333", "phobos")#COMPLIMENT ME!!! TELL ME I'M CLEVER!!!
define kate = CustomCharacter("Kate", "#59BB83", "kate")
define summer = CustomCharacter("Summer", "#EF2F30", "summer")
define shauntal = CustomCharacter("Shauntal", "#FF9D8F", "shauntal")
define caitlin = CustomCharacter("Caitlin", "#ff54e5", "caitlin")
define deoxysa = CustomCharacter("Spiky Entity", "#ff4400", "deoxysa")
define deoxysd = CustomCharacter("Sturdy Entity", "#ff4400", "deoxysd")
define deoxyss = CustomCharacter("Swift Entity", "#ff4400", "deoxyss")

define gardeniamom = CustomCharacter("Mom", "#8EC300", None)
define gardeniadad = CustomCharacter("Dad", "#4F6552", None)
define gardeniauncle = CustomCharacter("Uncle", "#7D5ED5", None)

define charlist = [
    cynthia,
    
    oak, pikachu, starter, red, mom, blue, silver, brawly, roxanne, 
    face, mace, falkner, leaf, ethan, calem, hilbert, brendan, may, flannery,
    whitney, sabrina, serena, cheren, misty, bianca, dawn, nate, rosa, bea,
    nessa, hilda, gardenia, skyla, brock, erika, janine, tia, latias, sonia, 
    jasmine, grusha, yellow, ethanmind, bluemind, wally, raihan, eri, klara, 
    melody, leafdate, leafmind, zinnia, iono, morty, shauna,

    lenora, blaine, wallace, ramos, surge, melony, marshal, koga, bertha, 
    winona, will, burgh, olivia, fantina, karen, clair, byron, valerie,

    bruno, alder, lance, kris, drayden, iris, miriam, rowan, lisia, lisiamind,

    narrator, security, roughneck, roughneck2, roughneck3, femthug, sidemon, 
    lace, oldman, anabel, allister, phobos, kate, summer, hiker, hiker2, hiker3,
    gardeniamom, gardeniadad, gardeniauncle, duplica, wes, hexmaniac, shauntal]

# change with new characters
define classdex = {
    "Bianca" : { "Normal", "Psychic"},
    "Cheren" : { "Normal", "Dark"},
    "May" : { "Fire", "Fighting", "Bug"},
    "Whitney" : { "Normal", "Fairy"},
    "Hilbert" : { "Ice", "Steel", "Ghost"},
    "Hilda" : { "Poison", "Steel", "Rock"},
    "Calem" : { "Fighting", "Flying", "Fairy"},
    "Sabrina" : { "Psychic", "Ghost"},
    "Nessa" : { "Water", "Rock"},
    "Dawn" : { "Ice", "Dragon", "Fairy"},
    "Nate" : { "Electric", "Steel", "Poison"},
    "Rosa" : { "Electric", "Psychic", "Bug"},
    "Silver" : { "Poison", "Dark"},
    "Brendan" : { "Grass", "Ground", "Water"},
    "Flannery" : { "Fire", "Ground"},
    "Serena" : { "Dark", "Fire", "Ground"},
    "Skyla" : { "Flying", "Bug"},
    "Leaf" : { "Grass", "Electric", "Dragon"},
    "Misty" : { "Water", "Ice"},
    "Bea" : { "Fighting", "Rock"},
    "Blue" : { "Flying", "Dragon"},
    "Gardenia" : { "Grass", "Ghost"},
    "Erika" : { "Grass", "Poison" },
    "Tia" : { "Dragon", "Psychic" },
    "Sonia" : { "Electric", "Fire" },
    "Jasmine" : { "Steel", "Ground" },
    "Grusha" : { "Ice", "Flying" },
    "Wally" : { "Fairy", "Fighting" },
    "Raihan" : { "Rock", "Dragon" },
    "Klara" : { "Water", "Bug" },
    "Iono" : { "Electric", "Ghost" }
}

define classtaught = {
    "Instructor Lenora" : "Normal",
    "Instructor Blaine" : "Fire",
    "Instructor Wallace" : "Water",
    "Instructor Ramos" : "Grass",
    "Lieutenant Surge" : "Electric",
    "Instructor Melony" : "Ice",
    "Sensei Marshal" : "Fighting",
    "Instructor Koga" : "Poison",
    "Instructor Bertha" : "Ground",
    "Instructor Will" : "Psychic",
    "Burgh" : "Bug",
    "Instructor Olivia" : "Rock",
    "Instructrice Fantina" : "Ghost",
    "Instructor Karen" : "Dark",
    "Instructor Clair" : "Dragon",
    "Instructor Byron" : "Steel",
    "Instructor Valerie" : "Fairy",
    "Instructor Winona" : "Flying"
}

define altclasstaught = {
    "Normal": "Instructor Lenora",
    "Fire": "Instructor Blaine",
    "Water": "Instructor Wallace",
    "Grass": "Instructor Ramos",
    "Electric": "Lieutenant Surge",
    "Ice": "Instructor Melony",
    "Fighting": "Sensei Marshal",
    "Poison": "Instructor Koga",
    "Ground": "Instructor Bertha",
    "Psychic": "Instructor Will",
    "Bug": "Burgh",
    "Rock": "Instructor Olivia",
    "Ghost": "Instructrice Fantina",
    "Dark": "Instructor Karen",
    "Dragon": "Instructor Clair",
    "Steel": "Instructor Byron",
    "Fairy": "Instructor Valerie",
    "Flying": "Instructor Winona"
}

define starters = {
    "Normal":[506,206,531],
    "Fire":[4,554,631],
    "Water":[258,418,746],
    "Grass":[387,548,556],
    "Electric":[179,170,479],
    "Ice":[363,361,615],
    "Fighting":[532,447,214],
    "Poison":[41,747,336],
    "Ground":[328,529,618],
    "Flying":[396,198,357],
    "Psychic":[280,79,561],
    "Bug":[540,290,213],
    "Rock":[246,557,774],
    "Ghost":[607,200,778],
    "Dragon":[371,714,780],
    "Steel":[304,597,227],
    "Fairy":[669,742,303],
    "Dark":[551,215,302]
}

define availablechars = {
    "Battle Hall" : ["Blue", "Janine"],
    "Academy" : ["Sabrina", "Cheren", "Dawn"],
    "Recreation Center" : ["Misty", "Nessa", "Bea"],
    "Aura Hall" : ["Leaf", "May", "Hilda", "Serena"],
    "Research Center" : ["Nate", "Bianca"],
    "Garden" : ["Erika", "Professor Cherry"],
    "Relic Hall" : ["Ethan", "Brendan", "Calem", "Hilbert"],
    "Student Center" : ["Rosa", "Skyla"],
    "Baseball Field" : ["Flannery", "Whitney", "Gardenia"],
    "Pledge Hall" : ["Silver"]
}

define sceneconditions = {
    "Bea1" : {"Level" : 2},
    "Bea2" : {"Level" : 4, "Nate" : 1, "Others" : ["Nate"]},
    "Bianca1" : {"Level" : 2, "Date" : [19, 5, 2004]},
    "Blue1" : {"Level" : 2, "Date" : [24, 4, 2004]},
    "Brendan1" : {"Level" : 2, "Event" : ["Professor Oak", "LearnedAboutContestColiseum", "Find the Contest Coliseum."]},
    "Calem1" : {"Level" : 2, "Serena" : 2},
    "Cheren1" : { "Event" : ["Cheren", "SPECIAL", "The future is cloudy..."] },
    "Cheren2" : { "Event" : ["Cheren", "SPECIAL", "The future is cloudy..."] },
    "Dawn1" : {"Level" : 2},
    "Dawn2" : {"Level" : 4, "Date" : [7, 5, 2004]},
    "Erika1" : {"Level" : 2, "Date" : [11, 5, 2004]},
    "Ethan1" : {"Event" : ["Ethan", "MountainTalk", "Meet on the mountain"], "NotEvent" : ["Ethan", "Forgotten", "The future refuses to change."]},
    "Flannery1" : {"Level" : 2, "Date" : [24, 4, 2004], "Time" : "Evening"},
    "Flannery2" : {"Level" : 4, "Time" : "Evening"},
    "Gardenia1" : {"Level" : 2, "Date" : [7, 5, 2004], "NotEvent2" : ["Gardenia", "LostFieldBattle", "You're in the red."], "NotEvent" : ["Gardenia", "Gardenia1", "Meet in the fields."], "Others": ["Brendan"]},
    "Hilda1" : {"Level" : 2, "Others" : ["Nate", "Bea", "Bianca"]},
    "Hilda2" : {"Level" : 4, "Date" : [7, 5, 2004], "Hilbert" : 1},
    "Hilbert1" : {"Level" : 2, "Date" : [19, 4, 2004]},
    "Hilbert2" : {"Level" : 4, "Hilda" : 1, "Nate" : 1},
    "Iono1" : {"Level" : 2, "Event" : ["Iono", "SkippedClass", "The future is cloudy..."]},
    "Janine1" : {"Level" : 2, "Date" : [25, 4, 2004]},
    "Janine2" : {"Level" : 4, "Date" : [7, 5, 2004]},
    "Jasmine1" : {"Level" : 2, "Date" : [7, 5, 2004]},
    "Jasmine2" : {"Level" : 4, "NotEvent" : ["Jasmine", "Jasmine2Part1", "Attend Steel class with Jasmine."]},
    "Grusha1" : {"Level" : 2, "Date" : [13, 5, 2004], "NotEvent" : ["Grusha", "Scene1Part1", "Sneak out at night."]},
    "Klara1" : {"Level" : 2, "Event" : ["Klara", "SPECIAL", "Text at night"], "Date" : [26, 5, 2004]},
    "Kris1" : {"Level" : 2},
    "Leaf1" : {"Level" : 2},
    "May1" : {"Level" : 2},
    "May2" : {"Level" : 4, "Date": [21, 5, 2004], "Others" : ["Bea"]},
    "Misty1" : {"Level" : 2, "Date" : [22, 4, 2004]},
    "Misty2" : {"Level" : 4, "Date" : [7, 5, 2004], "NotEvent" : ["Misty", "Scene2Part1", "Text Misty at night."]},
    "Nate1" : {"Level" : 2, "Date" : [17, 5, 2004]},
    "Nate2" : {"Level" : 4, "Bea" : 2, "Hilbert" : 2, "Others" : ["Bea", "Hilbert"]},
    "Nessa1" : {"Level" : 2, "Date" : [14, 4, 2004]},
    "Nessa2" : {"Level" : 4, "Raihan" : 1},
    "Raihan1" : {"Level" : 2},
    "Rosa1" : {"Level" : 2, "Date" : [18, 4, 2004]},
    "Rosa2" : {"Level" : 4, "Date" : [7, 5, 2004]},
    "Rosa3" : {"Level" : 6, "Raihan" : 1},
    "Sabrina1" : {"Level" : 2},
    "Serena1" : {"Level" : 2},
    "Serena2" : {"Level" : 4, "Date" : [18, 5, 2004], "Others" : ["Janine", "Jasmine", "Dawn"]},
    "Silver1" : {"Level" : 2, "Date" : [18, 4, 2004]},
    "Silver2" : {"Level" : 4, "Date" : [7, 5, 2004]},
    "Silver3" : {"Level" : 6, "Event" : ["Silver", "Silver2Part2", "The future is cloudy..."]},
    "Skyla1" : {"Level" : 2, "Date" : [18, 4, 2004]},
    "Skyla2" : {"Level" : 4, "Date" : [7, 5, 2004], "Event2" : ["Skyla", "Skyla1Part2", "The future is cloudy..."], "Event" : ["Skyla", "TalkedBothProfessors", "Visit Flying and Bug classes."], "NotEvent" : ["Skyla", "Skyla2", "Sneak out at night."]},
    "Sonia1" : {"Level" : 2, "Nessa" : 1},
    "Sonia2" : {"Level" : 4, "Date" : [7, 5, 2004]},
    "Tia1" : {"Level" : 2},
    "Tia2" : {"Level" : 4, "Date" : [17, 5, 2004], "Others" : ["Professor Cherry"], "NotEvent" : ["Tia", "Tia2Part1", "Go to Inspira on a weekday."]},
    "Wally1" : {"Level" : 2, "Event" : ["Wally", "ClassIntro", "Attend class with Wally."]},
    "Whitney1" : {"Level" : 2, "Date" : [27, 4, 2004]},
    "Whitney2" : {"Level" : 4, "Date" : [7, 5, 2004]}
}

define extrascenes = [
    "Bea2Part2",
    "Misty2Part2",
    "Grusha1Part2",
    "Tia2Part2",
    "Jasmine2Part2",
    "Whitney2Part2",#sorta a whitney/flannery combo scene, but I'm calling it whitney2part2 for standardization purposes
    "Calem1Part2",#sorta a calem/serena combo scene, but I'm calling it Calem1Part2 for standardization purposes
    "Wally1Part2",
    "Cheren2Part2",
    "Gardenia1Part2",
    "Silver2Part2",
    "Skyla1Part2",
    "Skyla1Part3",
    "Skyla1Part4",
    "Skyla2Part2"
]