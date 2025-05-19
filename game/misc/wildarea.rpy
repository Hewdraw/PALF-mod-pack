label wildarea(newloc):

stop music fadeout 2.5

python:
    if (isinstance(newloc, Dungeon)):
        dungeon = newloc
        newloc = newloc.GetName()
    wildcount = 0
    location = newloc
    continualencounters = 0
    inwildarea = True

show screen currentdate with dis
    
label afterwildareasetup:

if (dungeon != None):
    $ dungeon.SetUp()
elif (location == "fields"):
    $ renpy.music.queue("audio/music/Fieldstheme_Start.ogg", channel='music', loop=None, fadein=1.0, tight=None)
    $ renpy.music.queue("audio/music/Fieldstheme_Loop.ogg", channel='music', loop=True)
    scene clouds:
        yalign 0.5
    show fields1 :
        yalign 0.33 xalign 0.95
    with Dissolve(2.0)
elif (location == "alley"):
    queue music "audio/music/alley_start.ogg" noloop
    queue music "audio/music/alley_loop.ogg"
    scene abandonedhouse:
        yalign 0.5
    with Dissolve(2.0)
elif (location == "seaport"):
    queue music "audio/music/seaport_start.ogg" noloop
    queue music "audio/music/seaport_loop.ogg"
    scene seaport with Dissolve(2.0)
elif (location == "mountain"):
    $ renpy.music.queue("audio/arctic.ogg", channel='music', loop=True)
    scene mountain with Dissolve(2.0)
elif (location == "catacombs"):
    queue music "audio/music/potown_start.ogg" noloop
    queue music "audio/music/potown_loop.ogg"
    $ randback = random.random()
    if (randback <= .2):
        scene catacombs1 with Dissolve(2.0) 
    elif (randback <= .4):
        scene catacombs2 with Dissolve(2.0)
    elif (randback <= .6):
        scene catacombs3 with Dissolve(2.0)
    elif (randback <= .8):
        scene catacombs4 with Dissolve(2.0)
    else:
        scene catacombs5 with Dissolve(2.0)

    if (not HasEvent("Professor Oak", "FoundCatacombs")):
        call CatacombsIntro() from _call_CatacombsIntro

if (dungeon == None):
    #when going through the catacombs for the first time with Skyla, heal between every battle
    if (location == "catacombs" and HasEvent("Cheren", "JoinCatacombs") and not HasEvent("Professor Oak", "ClearedCatacombs") and continualencounters < 20):
        $ HealParty()

    if (not MakeRed().HasMons()):
        narrator "You quickly sprint back to campus, protecting your hurt and fainted Pokémon from further harm."
        $ location = "school"
    else:
        $ subtitle = ""
        if (wildcount != 0):
            $ subtitle = " Consecutive battles won: {}".format(wildcount)

        menu:
            "[bluecolor][[Blue Rank 1]{/color} >Talk to Blue" if (IsDate(18, 5, 2004) and location == "mountain" and GetRelationshipRank("Blue") > 0 and not HasEvent("Blue", "MountainTalk")):
                call bluetalkmountainfieldtrip from _call_bluetalkmountainfieldtrip

                jump afterwildareasetup

            "[bluecolor][[Dawn Rank 1]{/color} >Talk to Dawn" if (IsDate(18, 5, 2004) and location == "mountain" and GetRelationshipRank("Dawn") > 0 and not HasEvent("Dawn", "MountainTalk")):
                call dawntalkmountainfieldtrip from _call_dawntalkmountainfieldtrip

                jump afterwildareasetup

            "[bluecolor][[Hilbert Rank 1]{/color} >Talk to Hilbert" if (IsDate(18, 5, 2004) and location == "mountain" and GetRelationshipRank("Hilbert") > 0 and not HasEvent("Hilbert", "MountainTalk")):
                call hilberttalkmountainfieldtrip from _call_hilberttalkmountainfieldtrip

                jump afterwildareasetup

            "Is that Ethan...?" if (IsAfter(17, 5, 2004) and location == "mountain" and not (timeOfDay == "Morning" and IsDate(18, 5, 2004)) and IsPresent("Ethan") and IsPresent("Professor Cherry") and not HasEvent("Ethan", "MountainTalk")):
                call ethantalkmountainfieldtrip from _call_ethantalkmountainfieldtrip

                jump afterwildareasetup

            "Is that a Cramorant...?" if (location == "seaport" and activetreat in ["Water Bottle", "Bouffalant Wings"] and "Cramorant1" not in battlehistory.keys()):
                call cramorantscene2 from _call_cramorantscene2

            "{b}>Go Exploring!{/b}[subtitle]":
                $ continualencounters += 1
                $ GenerateRandomEvent(location)

                if (location == "fields" and IsDate(17, 5, 2004) and continualencounters == 3):
                    call cyclizarhuntpart2 from _call_cyclizarhuntpart2
                elif (location == "catacombs" and HasEvent("Cheren", "JoinCatacombs") and not HasEvent("Professor Oak", "ClearedCatacombs") and continualencounters == 20):
                    call FoundTinkatitaniumLode from _call_FoundTinkatitaniumLode 

                jump afterwildareasetup

            ">Head back to campus":
                if (IsDate(17, 5, 2004) and location == "fields"):
                    python:
                        cyclizarcount = 0
                        for mon in box + playerparty:
                            if (mon.GetId() == pokedexlookupname("Cyclizar", DexMacros.Id)):
                                cyclizarcount += 1

                    narrator "Between your party and your PC Box, you have a total of [cyclizarcount] Cyclizar."
                    narrator "You remember Professor Cherry mentioned she couldn't possibly ask you to catch any more than [bluecolor]five...{/color}"

                elif (location == "catacombs" and HasEvent("Cheren", "JoinCatacombs") and not HasEvent("Professor Oak", "ClearedCatacombs") and continualencounters < 20):
                    skyla night @surprised "Wait, hold on! We can't go back yet, we haven't found the Tinkatitanium yet!"
                    if (continualencounters < 5):
                        skyla @sadbrow talkingmouth "I haven't seen even a trace of it yet. We probably need to keep looking for a while."
                    elif (continualencounters < 10):
                        skyla @talkingmouth "I've been keeping an eye out for any Tinkatitanium, and I think there might be a big pile of it somewhere around here. Let's keep looking!"
                    elif (continualencounters < 15):
                        skyla @angrybrow talkingmouth "I'm pretty sure there's a big pile of Tinkatitanium in the area! All those pinkuns had to get their metal from {i}somewhere{/i}, right?"
                    elif (continualencounters < 20):
                        skyla @happy "I'm absolutely sure of it! There's a massive lode of Tinkatitanium right around the corner! We just have to push a little bit longer!"

                narrator "Are you sure you want to head back to campus? Doing so will end this free time."

                if (wildcount != 0):
                    python:
                        expvalue = 5
                        if (location == "alley"):
                            expvalue = 9
                        elif (location == "seaport"):
                            expvalue = 12
                        elif (location == "mountain"):
                            expvalue = 17
                        elif (location == "catacombs"):
                            expvalue = 22
                        patience = personalstats["Patience"]
                        exptotal = math.floor(pow(expvalue, 3) / 25 * min(3, (1 + wildcount / 10)))
                        exptotalpostpatience = math.floor(pow(expvalue + patience / 10.0, 3) / 25 * min(3, (1 + wildcount / 10)))
                    narrator "You have won [wildcount] consecutive battles, so your party will gain [exptotalpostpatience] experience each, including [exptotalpostpatience - exptotal] bonus experience from [patiencecolor]Patience{/color}. (There are no bonuses after 20 consecutive battles.)"
                    if (GetHighestLevel() > AimLevel() + 3):
                        narrator "{color=#f00}Note:{/color} Pokémon that have significantly more experience than is expected right now may receive less."

                menu:
                    "Yes, I'm sure.":
                        jump leavewildarea

                    "Never mind.":
                        jump afterwildareasetup

elif (not dungeon.IsComplete()):
    $ dungeon.GetCutscene("DungeonTurn" + str(dungeon.GetCurrentFloor()))

    show screen dungeonpartyviewer(dungeon)
    
    menu:
        "{b}Advance forward!{/b}":
            python:
                continualencounters += 1
                GenerateRandomEvent(location, dungeon)
                dungeon.SetUp()
            
            if (not Fled and dungeon.StillActive()):
                $ dungeon.ChangeFloor()

                if (dungeon.IsComplete()):
                    stop music fadeout 1.5

                    call clearscreens() from _call_clearscreens_154
                    hide screen dungeonbattleui
                    hide screen dungeonbattlefieldstatus
                    hide screen dungeonpartyviewer
                    scene blank2 
                    with Dissolve(2.0)

                    jump leavewildarea

            elif (not dungeon.StillActive()):
                jump gameover

        "Check in on your party":
            call DungeonPartyLogistics(dungeon) from _call_DungeonPartyLogistics

        "Take stock of your environment":
            show screen dungeonbattlefieldstatus(dungeon)

        "Refresh yourself on Dungeons":
            show screen DungeonHelp zorder 100

    jump afterwildareasetup

label leavewildarea:

call clearscreens() from _call_clearscreens_223

if (dungeon == None):
    show screen currentdate with dis

python:
    activetreat = None
    continualencounters = 0
    if (dungeon == None and wildcount != 0):
        expstring = []
        for mon in playerparty:
            expstring += mon.GainExperience(exptotalpostpatience)
        PrintExp(expstring)
    if (wildcount > highestwildcount):
        highestwildcount = wildcount
    wildcount = 0
    location = "school"
    inwildarea = False
    dungeon = None
    _rollback = True
    renpy.suspend_rollback(False)

return

init python:
    def GetTreatBoost(monid):
        if (activetreat == None):
            return 1
        elif (treatboosts[activetreat] in [pokedexlookup(monid, DexMacros.Type1), pokedexlookup(monid, DexMacros.Type2)]):
            return wildcount + 1
        return 1

    def GrabFromEncounterPool(encounterpool):
        encounterlist = []
        encountermax = 0
        for entry, odds in encounterpool.items():
            if (activerepel == None
            or activerepel == "Repel" and odds < 10
            or activerepel == "Super Repel" and odds < 7
            or activerepel == "Max Repel" and odds < 5):
                encounterlist.append((encountermax, entry))
                encountermax += (odds * GetTreatBoost(entry))
        encounterlist.append((9999, 0))
        
        randnum = RandInt(0, encountermax)
        for i in range(len(encounterlist)):
            if (randnum <= encounterlist[i + 1][0]):
                return encounterlist[i][1]

    def GenerateRandomEvent(location, dungeon=None):
        global sidemonnum, sidemonnum2, sidemonnum3
        global activerepel
        global repelstepsleft
        #events = []
        #generate more random events through this
        
        goodguys = [MakeRed()]
        badguys = []
        if (dungeon != None):
            goodguys = dungeon.GetTrainers()
        elif (location == "fields" and IsDate(17, 5, 2004)):
            goodguys.append(MakeTrainer("Leaf", TrainerType.Ally))
            goodguys.append(MakeTrainer("Dawn", TrainerType.Ally))
        elif (location == "catacombs" and HasEvent("Cheren", "JoinCatacombs") and not HasEvent("Professor Oak", "ClearedCatacombs")):
            goodguys.append(MakeTrainer("Skyla", TrainerType.Ally))

        numfoes = len(goodguys)
        if (dungeon != None):
            numfoes, numfoesstr = dungeon.BadMagnitude(1, 6)

        for i in range(numfoes):
            if (dungeon != None):
                newpokemon = dungeon.GeneratePokemon()
                newpokemonnum = newpokemon.GetId()

            else:
                encounterpool = {}
                levelrange = range(3, 11)
                evopool = {}

                if (location == "fields"):
                    encounterpool = {
                        263: 10,
                        155: 3,
                        399: 10,
                        191: 10,
                        835: 10,
                        133: 1,
                        919: 10,
                        406: 7,
                        29: 7,
                        32: 7,
                        333: 7,
                        307: 7,
                        401: 10,
                        111: 5,
                        710: 5,
                        659: 10,
                        967: 3,
                        777: 7,
                        764: 7
                    }
                elif (location == "alley"):
                    levelrange = range(6, 13)
                    encounterpool = {
                        431: 10,
                        725: 1,
                        767: 10,
                        412.2: 10,
                        81: 10,
                        351: 1,
                        559: 7,
                        568: 10,
                        104: 7,
                        629: 7,
                        677: 7,
                        917: 10,
                        744: 3,
                        353: 10,
                        88.1: 10,
                        714: 5,
                        965: 5,
                        439: 5
                    }
                elif (location == "seaport"):
                    levelrange = range(9, 16)
                    encounterpool = {
                        190: 10,
                        58: 7,
                        223: 10,
                        781: 1,
                        602: 3,
                        131: 1,
                        852: 7,
                        690: 7,
                        194.1: 10,
                        580: 10,
                        976: 5,
                        595: 7,
                        688: 10,
                        592: 5,
                        592.1: 5,
                        318: 7,
                        885: 3,
                        393: 3,
                        298: 10
                    }
                elif (location == "mountain"):
                    levelrange = range(14, 21)
                    encounterpool = {
                        234: 3,
                        776: 1,
                        86: 10,
                        459: 10,
                        74.1: 10,
                        712: 7,
                        739: 7,
                        757: 7,
                        220: 10,
                        225: 7,
                        337: 5,
                        338: 5,
                        872: 7,
                        932: 10,
                        425: 10,
                        624: 3,
                        996: 1,
                        27.1: 7,
                        703: 5
                    }
                elif (location == "catacombs"):
                    levelrange = range(19, 26)
                    encounterpool = {
                        19.1 : 10,
                        935 : 3,
                        874 : 5,
                        854 : 7,
                        736 : 10,
                        971 : 7,
                        453 : 10,
                        92 : 10,
                        50.1 : 10,
                        83.1 : 7,
                        856 : 5,
                        622 : 7,
                        95 : 7,
                        562.1 : 7,
                        859 : 5,
                        443 : 1,
                        52.2 : 10,
                        957 : 7,
                        109 : 10,
                        207 : 7
                    }
                    evopool = {
                        19.1 : (20, 20.1),
                        736 : (20, 737),
                        92 : (25, 93),
                        443 : (24, 444),
                        957 : (24, 958)
                    }

                newpokemonnum = GrabFromEncounterPool(encounterpool)
                randlevel = RandomChoice(levelrange)

                if (newpokemonnum in evopool):
                    evolevel, evoid = evopool[newpokemonnum]
                    if (randlevel >= evolevel):#if the pokemon is at, or higher than, the level for evolution
                        newpokemonnum = evoid#change its id

                newpokemon = Pokemon(newpokemonnum, level = randlevel, shinylock=False)

            if (i == 0):
                sidemonnum = newpokemonnum
            elif (i == 1):
                sidemonnum2 = newpokemonnum
            elif (i == 2):
                sidemonnum3 = newpokemonnum
            trainer2 = Trainer("sideportraitfull", TrainerType.Enemy, [newpokemon], isPokemon=True)
            badguys.append(trainer2)

        repelstepsleft -= 1
        if (repelstepsleft == 0):
            activerepel = None

        specialuniforms = []
        specialoutfits = []
        if (IsDate(18, 5, 2004) and timeOfDay == "Morning"):
            specialuniforms=[True, False]

        if (specialuniforms == []):
            if (location == "mountain" and GetRelationshipRank("Silver") > 1):
                specialoutfits=["winter", ""]

        
        if (dungeon != None):
            if (dungeon.GetCutscene("DungeonBattle" + str(dungeon.GetCurrentFloor()))):
                return 

        renpy.call("Battle", goodguys + badguys, uniforms=specialuniforms, customoutfits=specialoutfits, healParty=False, specialmusic=("Audio/Music/RBY_Pokemon_Start.ogg", "Audio/Music/RBY_Pokemon_Loop.ogg"), canBeDitto=True, dungeon=dungeon)