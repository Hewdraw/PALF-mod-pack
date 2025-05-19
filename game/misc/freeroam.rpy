label freeroam:

python:
    location = "campus"
    AddPikachu()
    HealParty() 

label beforemusic:

call silence() from _call_silence_1

$ renpy.music.queue("audio/music/GSCBike_Start.ogg", channel='music', loop=None, fadein=1.0, tight=None)
$ renpy.music.queue("audio/music/GSCBike_Loop.ogg", channel='music', loop=True)
$ freeroaming = True

scene map with splitfade
show blank2 as blackground behind map
show screen currentdate 
call screen map_UI(_with_none=False)
hide blackground
with dissolve

jump skipresetup

label aftersetup:
scene map
show screen currentdate
call screen map_UI(_with_none=False)

label skipresetup:
    
python:
    trainer1 = MakeRed()
    interaction = _return

if (not isinstance(interaction, str)):
    jump aftersetup

if (IsPresent(interaction)):
    $ interactionsprite = GetCharacterSprite(interaction)

if (interaction == "Study"):
    redmind @thinking "Now, which type should I focus on...?"

    show blank2 with dis:
        alpha 0.8

    $ lastclass = ""

    call screen studyfocus
    $ selectedtype = _return 

    hide blank2 with dis

    if (selectedtype == "Back"):
        jump aftersetup

    if (excusesecondelective or excusesecondhomeroom):
        redmind uniform @thinking "Almost everyone else is in class right now, so I'll have to study alone. It won't be as effective as studying with someone."

        menu:
            "That's fine.":
                $ IncreaseProficiency(selectedtype, 0.25)

            "Nevermind":
                jump aftersetup
    else:
        $ willstudy = list(WillStudy(selectedtype))
        if (len(willstudy) > 0):
            $ randomstudent = RandomChoice(list(WillStudy(selectedtype)), True)

            $ pronoun = ("him" if persondex[randomstudent]["Sex"] == Genders.Male else "her")

            label afterlibraryseed:

            redmind @thinking "It looks like [randomstudent] is in the library right now. Should I study with [pronoun]?"

            menu: 
                "Yeah, sure.":
                    show library with Dissolve(1.0)
                    $ imagestring = GetCharacterSprite(randomstudent)
                    $ renpy.show(imagestring, [dissolvein])

                    pause 1.0

                    narrator "You spent some time studying [selectedtype]-type Pokémon with [randomstudent]."

                    python:
                        renpy.show(GetCharacterSprite(randomstudent, 10))
                        if (randomstudent in ["Jasmine", "Grusha"]):
                            ValueChange(randomstudent, 4, 0.5)
                        else:
                            ValueChange(randomstudent, 2, 0.5)

                        IncreaseProficiency(selectedtype, 0.5)

                        renpy.transition(dis)
                        renpy.hide(imagestring)

                "No, contact someone else.":
                    redmind @thinking "Right... let's see if anyone would be interested in studying this with me."
                    redmind @thinking "They'll need to be taking the [selectedtype] Elective as well, of course."

                    show phone_B 
                    show phone_A
                    with fadeinbottom

                    hide blank2 with dis

                    call screen database(calling=True, limittype=selectedtype, _with_none=False) with Dissolve(1.0)
                    with dissolve
                    $ contact = _return

                    if (contact == "Back"):
                        hide phone_B 
                        hide phone_A
                        with fadeoutbottom
                        jump afterlibraryseed
                    elif (contact == randomstudent):
                        redmind @thinking "[randomstudent] is already there[ellipses] not much point in texting, is there?"
                        hide phone_B 
                        hide phone_A
                        with fadeoutbottom
                        jump afterlibraryseed
                    elif (contact != "Sabrina"):
                        $ pronoun = ("he" if persondex[contact]["Sex"] == Genders.Male else "she")
                        redmind @thinking "Alright, I'll text [contact] and see if [pronoun] can show up."
                    else:
                        hide phone_B 
                        hide phone_A
                        with fadeoutbottom
                        redmind @thinking "Alright, I'll think hard at Sabrina and see if she can show up."

                    if (contact.title() not in WillStudy(selectedtype)):
                        pause 3.0

                        narrator "There was no response..."

                        jump aftersetup

                    show library with Dissolve(1.0)

                    hide phone_B 
                    hide phone_A
                    with fadeoutbottom

                    $ renpy.show(GetCharacterSprite(contact, 0), [dissolvein])

                    pause 1.0

                    narrator "You spent some time studying [selectedtype]-type Pokémon with [contact]."

                    $ renpy.transition(dis)
                    $ renpy.show(GetCharacterSprite(contact, 10))
                    $ ValueChange(contact, 1, 0.5)
                    $ IncreaseProficiency(selectedtype, 0.5)

                    $ renpy.transition(dis)
                    $ renpy.hide(contact.lower())
                
                "Nevermind, I don't want to study.":
                    jump aftersetup
        
        else:
            redmind uniform @thinking "It doesn't look like there's anyone in the library willing to study right now, so I'll have to study alone. It won't be as effective as studying with someone."

            menu:
                "That's fine.":
                    $ IncreaseProficiency(selectedtype, 0.25)

                "Nevermind":
                    jump aftersetup

elif (interaction == "Town"):
    if (IsBefore(17, 4, 2004)):
        redmind @thinking "I should probably get a bit more used to the campus before I head out alone."
        jump aftersetup

    elif (trainer1.HasMons()):
        menu:
            "Go to the city.":
                call city from _call_city

            "Nevermind.":
                jump aftersetup
    else:
        redmind @thinking "I shouldn't leave campus with a party this tired-out."
        jump aftersetup

elif (interaction == "Fields"):
    
    if (IsBefore(13, 4, 2004)):
        redmind @thinking "I should probably get a bit more used to the campus before I head out alone."
        jump aftersetup

    elif (trainer1.HasMons()):
        $ wildcount = 0

        if (IsDate(17, 5, 2004)):
            call cyclizarhunt from _call_cyclizarhunt

        elif (HasEvent("Gardenia", "Gardenia1") and not HasEvent("Gardenia", "Gardenia1Part2")):
            if (GetEventDatetime("Gardenia", "Gardenia1") == calDate or IsAbsent("Gardenia")):
                narrator "You text Gardenia, but get no response--perhaps she is busy right now."
            else:
                $ SetLastHangout("Gardenia")
                call Gardenia1Part2 from _call_Gardenia1Part2

        elif (IsAfter(10, 5, 2004) and not (rescuedwill and rescuedsabrina and rescuedtia) and IsBefore(17, 5, 2004)):
            menu:
                "{color=#0f0}[[Easy]{/color} >Rescue Instructor Will from the Unhallowed Holt" if not rescuedwill:
                    jump unhallowedholt

                "{color=#00f}[[Medium]{/color} >Rescue Tia from the Shattered Glades" if not rescuedtia:
                    jump shatteredglades

                "{color=#f00}[[Hard]{/color} >Rescue Sabrina from the Windswept Woods" if not rescuedsabrina:
                    jump windsweptwoods
    
                ">Go to the fields":
                    if (trainer1.HasMons()):
                        $ wildcount = 0
                        call wildarea("fields") from _call_wildarea_1
                    else:
                        redmind @thinking "I shouldn't leave campus with a party this tired-out."
                        jump aftersetup

                ">Leave":
                    jump aftersetup

        if (IsBefore(18, 5, 2004)):
            call wildarea("fields") from _call_wildarea

        else:
            menu:
                ">Go to the fields":
                    call wildarea("fields") from _call_wildarea_5

                ">Go to Argent Mountain":
                    python:
                        rideable = None
                        for mon in playerparty:
                            if (pokedexlookupname("Cyclizar", DexMacros.Id) == mon.Id):
                                rideable = mon
                                break
                    if (rideable == None):
                        narrator "Would you like to pay $200 to rent a Ride Cyclizar?"

                        menu:
                            ">Pay":
                                if (money < 200):
                                    narrator "Embarrassingly, you do not have enough to pay the fee..."
                                
                                    jump aftersetup

                                else:
                                    $ money -= 200

                                    scene blank2 with splitfade

                                    narrator "You ride the rented Cyclizar up to Argent Mountain."

                                    $ sidemonnum = pokedexlookupname("Cyclizar", DexMacros.Id)
                                    $ PlaySound("pokemon/cries/{}.mp3".format(sidemonnum))
                                    sidemon "Cyc! Lizar!"

                            ">Do Not":
                                jump aftersetup

                    else:
                        scene blank2 with splitfade

                        if (GetRelationshipRank("Silver") > 1):
                            narrator "You put on the cold-weather gear that Silver gave you and ride your Cyclizar up Argent Mountain."
                        else:
                            narrator "You ride your Cyclizar up to Argent Mountain."

                        $ sidemonnum = pokedexlookup("Cyclizar", DexMacros.Id)
                        $ cyclizarnickname = rideable.GetNickname()
                        $ PlaySound("pokemon/cries/{}.mp3".format(sidemonnum))
                        $ sidemonoverride = cyclizarnickname
                        sidemon "Cyc! Lizar!"
                        $ sidemonoverride = None

                    call wildarea("mountain") from _call_wildarea_6

                "Nevermind.":
                    jump aftersetup
    else:
        redmind @thinking "I shouldn't leave campus with a party this tired-out."
        jump aftersetup 

elif (interaction == "Catacombs"):
    if (HasEvent("Professor Oak", "FoundCatacombs") or (IsPresent("Silver") and IsPresent("Cheren") and IsPresent("Skyla"))):
        if (trainer1.HasMons()):
            call wildarea("catacombs") from _call_wildarea_8
        else:
            redmind @thinking "I shouldn't go exploring with a party this tired-out."
            jump aftersetup 
    else:
        $ missing_students = [student for student in ["Silver", "Skyla", "Cheren"] if IsAbsent(student)]
        $ formatted_missing = ", ".join(missing_students[:-1]) + (" and " + missing_students[-1] if len(missing_students) > 1 else missing_students[0])
        $ preposition = 'is' if len(missing_students) == 1 else 'are'

        redmind @thinking "I should wait for everyone on the Disciplinary Committee to be free before going in here. It looks like [formatted_missing] [preposition] unavailable right now."
        
        jump aftersetup

elif (interaction == "GatherDC"):
    if (IsPresent("Silver") and IsPresent("Cheren") and IsPresent("Skyla") and IsPresent("Gardenia")):
        call Cheren2Part2 from _call_Cheren2Part2
    else:
        $ missing_students = [student for student in ["Silver", "Skyla", "Cheren", "Gardenia"] if IsAbsent(student)]
        $ formatted_missing = ", ".join(missing_students[:-1]) + (" and " + missing_students[-1] if len(missing_students) > 1 else missing_students[0])
        $ preposition = 'is' if len(missing_students) == 1 else 'are'

        redmind @thinking "I should wait for Gardenia and the Disciplinary Committee to be free before confronting I-Balls. It looks like [formatted_missing] [preposition] unavailable right now."
        
        jump aftersetup

elif (interaction == "Business"):
    jump talkbusiness

elif (interaction == "Bees"):
    call combeefrenzy from _call_combeefrenzy

    if (not HasEvent("Whitney", "FrenzBee")):
        jump aftersetup

elif (interaction == "LevelCheck"):
    show stadium_empty
    show janine 
    with dis
    $ levelaim = AimLevel()
    $ highestlevel = GetHighestLevel()
    janine @surprised "Hm?"
    janine @closedbrow talking2mouth "Oh, you want a check-in, huh? You should have a team of level [levelaim] Pokémon."
    janine @talking2mouth "Your highest-leveled Pokémon is level [highestlevel]. {nw}"
    if (highestlevel >= levelaim):
        extend @happymouth "You're good."
        if (highestlevel > levelaim + 5):
            janine @surprised "Maybe a bit too good. You've been spending a lot of time training, huh? Don't neglect your other responsibilities."
    elif (highestlevel < levelaim):
        extend @sadbrow talking2mouth "Fix that."
        if (highestlevel < levelaim - 5):
            janine @sad "Soon. This is a dangerous situation to be in."

    red @talkingmouth "Thanks for the advice."

    jump aftersetup

elif (interaction in ["B5", "B5Plus"]):
    show stadium_empty with dis

    if (interaction == "B5"):
        "You have activated the Balloon Bot Battle Bundle Beta. What type of battle would you like to start?"
    else:
        "You have activated the Better Balloon Bot Battle Bundle. What type of battle would you like to start?"

    $ battlecount = 1

    menu:
        "Single battle.":
            pass

        "Double battle.":
            $ battlecount = 2

        "Triple battle.":
            $ battlecount = 3

    python:
        trainer1 = MakeRed(battlecount)
        enemyteam = []

        if (interaction == "B5"):
            for i in range(6):
                enemyteam.append(Pokemon(0, 1))
        else:
            for i in range(6):
                moveset = []
                for j in range(4):
                    moveset.append(RandomChoice([
                        "Hyper Beam", "Return", "Baton Pass",
                        "Flamethrower", "Flare Blitz", "Will-O-Wisp",
                        "Liquidation", "Scald", "Shell Smash",
                        "Seed Bomb", "Energy Ball", "Leech Seed",
                        "Wild Charge", "Thunderbolt", "Thunder Wave",
                        "Ice Spinner", "Ice Beam", "Haze",
                        "Close Combat", "Focus Blast", "Detect",
                        "Poison Jab", "Sludge Wave", "Toxic Spikes",
                        "Earthquake", "Earth Power", "Spikes",
                        "Brave Bird", "Air Slash", "Tailwind",
                        "Psycho Cut", "Psychic", "Calm Mind",
                        "Leech Life", "Bug Buzz", "Quiver Dance",
                        "Stone Edge", "Ancient Power", "Stealth Rock",
                        "Phantom Force", "Shadow Ball", "Destiny Bond",
                        "Crunch", "Dark Pulse", "Nasty Plot",
                        "Dragon Claw", "Dragon Pulse", "Dragon Dance",
                        "Iron Head", "Flash Cannon", "Swords Dance",
                        "Play Rough", "Moonblast", "Belly Drum"], True))
                enemyteam.append(Pokemon(0, 50, moves=moveset))

        trainer2 = Trainer("Iono", TrainerType.Enemy, enemyteam, battlecount)

    if (interaction == "B5" and LoseItem(Item.B5) or interaction == "B5Plus" and LoseItem(Item.B5Plus)):
        call Battle([trainer1, trainer2], customexpressions=["red", "red", "iono nobody nomagnemite", "iono nobody nomagnemite"], gainexp=False) from _call_Battle_90
    else:
        "Error: Misusing the Balloon Bot Battle Bundle series of products may void the warranty. Please ensure your Balloon Bot Battle Bundle product is on a flat, level, surface, before initializing."

elif (interaction == "CriticalCheck"):
    show clouds
    show garden:
        zoom 0.625
    show kris
    with dis
    $ critrate = GetAverageProficiency() / 2.0
    kris @happy "Hello, [first_name]."
    kris @talkingmouth "Have you been keeping up on your capturing? [bluecolor]Given your current proficiencies, you should expect to be able to land critical captures [critrate]%% of the time."

    red @talkingmouth "Understood. Thanks, Doctor."

    jump aftersetup

elif (interaction == "AccessPC"):
    $ currentbox = max(0, currentbox)
    show screen partymons
    call screen pokemonswap
    hide screen partymons
    jump aftersetup

elif (interaction == "CookingClub"):
    if (GetRelationshipRank("May") > 1):
        show mallow:
            xpos 0.33 
        show may cookingclub apron:
            xpos 0.66
        with dis

        mallow @happy "Alola, [first_name]! Did you come here to hang with May and I? Or are you just looking to buy something?"

        red @talkingmouth "Just buying something for today, please."

        may @flirtbrow talkingmouth "Sorry, but there's no discount for friends!"

        red @happy "Wouldn't dream of asking for one."

        if (not HasEvent("May", "SeenClassic")):
            $ AddEvent("May", "SeenClassic")

            red @talkingmouth "Hey, is that a new outfit?"

            may @talkingmouth "It's actually an old one. I wore these old clothes until they were almost falling off of me."
            may @happy "But Brendan repaired 'em."
            may @talkingmouth "Anyway, I figured I shouldn't be wearing my nice clothes while I'm cooking."

            mallow @surprisedbrow talking2mouth "Tamato stains are {i}the worst.{/i}"

            may @surprisedbrow talkingmouth "True!"

            pause 1.0

            may @happy "Oh, right! Shopkeeping! What did you want to buy?"

    else:
        show mallow with dis

        mallow @happy blush "[first_name]! Alola! Great to see you again. Are you here to participate in the Cooking Club? Or do you just want to buy some PokéTreats?"

        red @talkingmouth "Just the treats for now, please."

        mallow @happy "Alright!"

    call screen shopkeep(treatitems if GetRelationshipRank("May") < 2 else treatitemspostmay)
    $ boughtitem = _return
    if (boughtitem == "Back"):
        if (GetRelationshipRank("May") > 1):
            mallow @happy "Okay! We'll see you later."
        
        else:
            mallow surprised "O-oh! Okay! I'll see you later, right?"

        jump aftersetup
    else:
        $ totalcost = boughtitem[0] * boughtitems
        if (totalcost > money):
            narrator "You can't afford that!"
        else:
            $ itemname = GetItemName(boughtitem[1])
            $ cookingcredit += totalcost
            $ money -= totalcost 
            if (boughtitems > 1):
                narrator "You bought [boughtitems]x [itemname] for $[totalcost]!"
            else:
                narrator "You bought [itemname] for $[totalcost]!"
            $ GetItem(itemname, boughtitems)
            $ boughtitems = 1

    jump aftersetup

elif (interaction == "Back"):
    jump aftersetup

else:
    if (interaction == "Janine" and (len(GetScenes([interaction])) == 0 or not GetScenes([interaction])[0][1])):
        if (HasEvent("Janine", "Domming")):
            narrator "You know better than to bother Janine while she's busy. The possible consequences scare and thrill you... but should be left for another time."
        else:
            narrator "You shouldn't bother Janine while she's busy."
        jump aftersetup
    elif (interaction == "Yellow"):
        narrator "Yellow is hard at work in the infirmary... you shouldn't interrupt her right now."
        jump aftersetup
    else:
        $ renpy.hide(interactionsprite)
        $ renpy.show(interactionsprite, [farleftside, dissolvein])
        narrator "You want to find [interaction]?"

        menu:
            "{b}>Yes, go find [interaction]{/b}" if (len(GetScenes([interaction])) == 1 and GetScenes([interaction])[0][1]):
                $ SetLastHangout(interaction)
                stop music fadeout 2.0
                $ renpy.hide(interactionsprite)
                $ renpy.call(GetScenes([interaction])[0][1])

                jump afterfreetime

            ">Yes, hang out" if not (len(GetScenes([interaction])) == 1 and GetScenes([interaction])[0][1]):
                if (interaction in ["Sabrina", "Blue", "Janine", "Misty", "Dawn", "Hilbert", "Professor Cherry"] and GetRelationshipRank(interaction) == 0):
                    narrator "You suspect that you are not close enough to [interaction] to hang out one-on-one..."
                    jump aftersetup
                elif (interaction in ["Leaf", "Sonia", "Nate", "Rosa"] and GetMood(interaction) >= 0 and GetRelationshipRank("Cheren") == 2 and not HasEvent("Cheren", "AcquiredMagnet")):
                    $ AddEvent("Cheren", "AcquiredMagnet")

                    if (interaction == "Leaf"):
                        call LeafMagnetGet() from _call_LeafMagnetGet
                    elif (interaction == "Sonia"):
                        call SoniaMagnetGet() from _call_SoniaMagnetGet
                    elif (interaction == "Nate"):
                        call NateMagnetGet() from _call_NateMagnetGet
                    elif (interaction == "Rosa"):
                        call RosaMagnetGet() from _call_RosaMagnetGet

                    jump afterfreetime

                python:
                    SetLastHangout(interaction)
                    renpy.transition(dis)
                    renpy.show(GetCharacterSprite(interaction, 10))
                    valuetochange = 3
                    if (interaction in ["Jasmine", "Grusha"]):
                        valuetochange = 6
                    ValueChange(interaction, valuetochange, 0.12)

                narrator "You spend some one-on-one time with [interaction]."
                python:
                    if (GetRelationshipRank(interaction) >= 1):
                        partyset = set()
                        if (interaction in classdex.keys()):
                            for mon in playerparty:
                                for typename in GetCharTypes(interaction):
                                    if mon.HasType(typename):
                                        partyset.add(mon)
                        expstring = []
                        for mon in partyset:
                            expstring += mon.GainExperience(math.floor(pow(AimLevel(), 3) / 25 * (GetCharacterLevel(interaction) / 5)))
                        PrintExp(expstring)

                    renpy.hide(interactionsprite)
                jump afterfreetime

            ">Give a gift" if (interaction not in GiftsGiven and persondex["Gardenia"]["Contact"]):
                python:
                    global invoverwrite
                    global itemdesc
                    invoverwrite = None
                    itemdesc = " "
                    item = renpy.call_screen("fieldinventory", True)
                if (item == "back"):
                    $ renpy.hide(interactionsprite)
                    $ renpy.jump("freeroam")
                else:
                    $ itemname = GetItemName(item)
                    menu:
                        ">Give [interaction] the [itemname]":
                            if (LoseItem(item)):
                                python:
                                    presentvalue = GetGiftValue(interaction, item)
                                    renpy.show(GetCharacterSprite(interaction, presentvalue))
                                    if (presentvalue < 1):
                                        renpy.say(None, "You swear you saw {} cringing as they take the {}...".format(interaction, itemname))
                                    elif (presentvalue == 1):
                                        renpy.say(None, "{} seems confused, but politely accepts the {}.".format(interaction, itemname))
                                    elif (presentvalue == 2):
                                        renpy.say(None, "{} accepts the {}.".format(interaction, itemname))
                                    elif (presentvalue == 3):
                                        renpy.say(None, "{} happily accepts the {}.".format(interaction, itemname))
                                    elif (presentvalue == 4):
                                        renpy.say(None, "{} joyfully accepts the {}.".format(interaction, itemname))
                                    elif (presentvalue >= 5):
                                        renpy.say(None, "{} ecstatically accepts the {}!".format(interaction, itemname))
                                    if (interaction in ["Jasmine", "Grusha"]):
                                        presentvalue *= 2
                                    GiftsGiven.append(interaction)
                                    ValueChange(interaction, presentvalue, 0.12, changemood=False)

                        "Nevermind":
                            pass

                    $ renpy.hide(interactionsprite)
                    $ renpy.jump("freeroam")

            "Nevermind":
                python:
                    renpy.hide(interactionsprite)
                    renpy.jump("freeroam")

label afterfreetime:
$ freeroaming = False
call clearscreens from _call_clearscreens_18

python:
    if (IsAfter(30, 4, 2004)):
        added = UpdateForeverals()
        if (len(added) > 0 and pikachuobj in playerparty):
            renpy.say(None, "What? [pika_name] started coughing... something's coming out!")
            for key, value in added.items():
                count = len(value)
                if count == 1:
                    reward = value[0]
                    renpy.say(None, f"Your bond with {key} earned you the {reward}!")
                else:
                    rewards = ', '.join(value[:-1])
                    last_reward = value[-1]
                    exclamation_marks = '!' * math.ceil(count / 3)
                    renpy.say(None, f"Your bond with {key} earned you the {rewards}, and {last_reward}{exclamation_marks}")
            
            if (IsAfter(8, 5, 2004) and persondex["Yellow"]["Value"] != 0):
                persondex["Yellow"]["Value"] = len(claimedforeverals)
                renpy.say(None, "Yellow is overjoyed!")

hide blank2
show blank2

pause 1.0

if (IsDate(5, 6, 2004)):
    if (timeOfDay == "Morning"):
        call klarapartyscene1 from _call_klarapartyscene1

    elif (timeOfDay == "Noon"):
        call klarapartyscene2 from _call_klarapartyscene2

    else:
        call klarapartyscene3 from _call_klarapartyscene3

if (timeOfDay == "Morning"):
    $ timeOfDay = "Noon"
elif (timeOfDay == "Noon" or timeOfDay == "Afternoon"):
    $ timeOfDay = "Evening"
elif (timeOfDay == "Evening" or timeOfDay == "After School"):
    if (excusesecondhomeroom):
        $ jumpto = "aftersecondhomeroom"
        $ jumptoyear = "01"
        $ jumptomonth = ("0" if calDate.month < 10 else "") + str(calDate.month)
        $ jumptodate = ("0" if calDate.day < 10 else "") + str(calDate.day)
        $ renpy.jump(jumpto + jumptoyear + jumptomonth + jumptodate)
    else:
        $ timeOfDay = "Night"

hide noon
hide evening
hide night

if (timeOfDay == "Noon"):
    show noon at vspaz
elif (timeOfDay == "Evening"):
    show evening at vspaz
    if (not excusesecondhomeroom and getRWDay(0) not in ["Saturday", "Sunday"]):
        pause 3.0

        $ jumpto = "secondhomeroom"
        $ jumptoyear = "01"
        $ jumptomonth = ("0" if calDate.month < 10 else "") + str(calDate.month)
        $ jumptodate = ("0" if calDate.day < 10 else "") + str(calDate.day)
        $ renpy.jump(jumpto + jumptoyear + jumptomonth + jumptodate)

elif (timeOfDay == "Night"):
    show night at vspaz

    pause 3.0

    show screen currentdate with dis

    if (not skipnightscenes and getRWDay(0) != "Friday"):
        call nightscenequeue from _call_nightscenequeue

    return

pause 3.0

if (IsDate(29, 5, 2004)):
    if (timeOfDay == "Noon"):
        jump nooncontestintermission

    else:
        jump eveningcontestintermission

jump beforemusic