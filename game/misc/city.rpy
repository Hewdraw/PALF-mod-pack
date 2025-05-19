label city:

stop music fadeout 2.5

$ location = "city"

queue music "audio/music/Inspira_start.ogg" noloop
queue music "audio/music/Inspira_loop.ogg"

scene city_B with Dissolve(2.0)

show screen currentdate
hide blackground
with dissolve

label citysetup:
$ trainer1 = Trainer("red", TrainerType.Player, playerparty)
if (not trainer1.HasMons()):
    narrator "You quickly sprint back to campus, protecting your hurt and fainted Pokémon from further harm."
    $ location = "school"
else:
    menu:
        "{b}Is that Silver...?{/b}" if (IsDate(3, 6, 2004) and not HasEvent("Silver", "SilverBirthday1")):
            call SilverBirthday1 from _call_SilverBirthday1
            jump city

        "{b}Give Silver a birthday present{/b}" if (IsDate(3, 6, 2004) and not HasEvent("Silver", "SilverBirthday2") and HasEvent("Silver", "SilverBirthday1")):
            call SilverBirthday2 from _call_SilverBirthday2
            jump city

        "{b}Track down Tia at her part-time job{/b}" if (GetRelationshipRank("Tia") == 1 and HasEvent("Tia", "Tia2Part1") and IsWeekday()):
            jump Tia2Part2

        "{b}Seek out the Tough Pokémon at the Seaport{/b}" if not seaportunlocked and not IsBefore(28, 4, 2004) and IsBefore(1, 5, 2004):
            call cramorantscene from _call_cramorantscene
            jump city

        "{b}Seek out Yellow and her Friend at the Café{/b}" if not sawwallyellow and not IsBefore(7, 5, 2004) and IsBefore(10, 5, 2004):
            call wallyellowscene from _call_wallyellowscene
            jump city

        "{b}Seek out Silver's Gang{/b}" if (not beatgrunts):
            $ courage = personalstats["Courage"]
            $ couragebonus = 0
            if (courage >= 10):
                narrator "Due to your [couragecolor]courage{/color}, you can choose to pick a fight with an especially strong Ex-Rocket member."

                menu:
                    ">Pick a fight with a tough grunt" if (courage >= 10):
                        $ couragebonus = 1
                    ">Pick a fight with a very strong grunt" if (courage >= 20):
                        $ couragebonus = 2
                    ">Pick a fight with an elite grunt" if (courage >= 30):
                        $ couragebonus = 3
                    ">Pick a fight with an ex-Squad Head" if (courage >= 40):
                        $ couragebonus = 4
                    ">Pick a fight with an ex-Administrator" if (courage >= 50):
                        $ couragebonus = 5
                    ">Pick a fight with one of Giovanni's personal guard" if (courage >= 60):
                        $ couragebonus = 6
                    ">Don't get {i}too{/i} brave":
                        pass

            show abandonedhouse
            if (HasEvent("Silver", "Overthrown")):
                show roughneck teamrocket
            else:
                show roughneck 
            with dis

            pause 1.0

            python:
                location = "alley"

                randomdialog = ["What, a gamble battle? Hah! Punk, I've been gamble battling since before you were born!",
                    "A gamble battle? Finally! No more instant ramen for me!",
                    "Hey, you looked at me funny! Come on, I'll take you on!",
                    "You. Me. A gamble battle. Ready?",
                    "I'm in a real bad mood, and you look like the perfect person to take it out on, scrub!",
                    "You don't have a chance in a gamble battle against me! My lucky numbers are hella auspicious today!"]

                if (HasEvent("Silver", "Overthrown")):
                    randomdialog = ["You better watch out! The new boss has told us to not be gentle with nosy kids like you no more.",
                    "Hey, join us! What? You're sayin' no? C'mon, I'll make you an offer you can't refuse!",
                    "The old boss was weak! Our new leader's gonna bring us back, and really {i}make{/i} somethin' of us!",
                    "Hey, ain't you the old boss' friend? I don't wanna hurt you, but the new boss told us we can't go easy on ya!",
                    "Team Rocket Forever! We ain't gotta be ashamed, now the new boss is leadin' us!",
                    "Look at this old uniform--it still fits! And you know what that big, red, 'R' means, don'tcha, punk?",
                    "Oh, it's you? ...Tell the old boss I'm sorry, but I can't just sit around and wait to disappear like he wanted us to."]

                dialog = RandomChoice(randomdialog)
            
            roughneck "[dialog]"

            python:
                beatgrunts = True
                numallies = 1
                numfoes = RandInt(1 + math.floor(couragebonus / 2), 3)
                foenums = (1 if numfoes != 1 else RandInt(1 + math.floor(couragebonus / 2), 3))
                allynums = max(foenums, numfoes)
                trainers = []
                numenemymons = 0
    
                trainers.append(Trainer("red", TrainerType.Player, playerparty, allynums))

                checklevel = AimLevel() + couragebonus * 5
                for i in range(numfoes):
                    if (checklevel >= 40):
                        teamnumber = RandInt(4, 6)
                    elif (checklevel >= 35):
                        teamnumber = RandInt(4, 5)
                    elif (checklevel >= 30):
                        teamnumber = RandInt(3, 5)
                    elif (checklevel >= 25):
                        teamnumber = RandInt(3, 4)
                    elif (checklevel >= 20):
                        teamnumber = RandInt(2, 4)
                    elif (checklevel >= 15):
                        teamnumber = RandInt(2, 3)
                    else:
                        teamnumber = RandInt(1, 3)

                    numenemymons += teamnumber
                    newteam = []
                    for i in range(teamnumber):
                        newpokemon = copy.deepcopy(random.choice(GetTrainerTeam("Grunts")))
                        newpokemon.UpdateLevel(newpokemon.GetLevel() + couragebonus)
                        newteam.append(newpokemon)
                    newtrainer = Trainer("roughneck", TrainerType.Enemy, newteam, foenums)
                    trainers.append(newtrainer)

            call Battle(trainers, customexpressions=["red", "red angrybrow happymouth"] + ["roughneck" + (" teamrocket" if HasEvent("Silver", "Overthrown") else ""), "roughneck angry" + (" teamrocket" if HasEvent("Silver", "Overthrown") else "")] * numfoes, reanchor=[False] + [True] * numfoes) from _call_Battle_43
            if (_return):
                if (HasEvent("Silver", "Overthrown")):
                    show roughneck angry teamrocket with dis
                else:
                    show roughneck angry with dis

                $ punkwins += 1

                $ totalwinnings = math.floor((1 + numfoes / 10.0) * (1 + numenemymons / 10.0) * 50 * (AimLevel() + couragebonus))
                $ money += totalwinnings
                narrator "You won $[totalwinnings]!"
                if (couragebonus > 0):
                    narrator "For [couragecolor]courageously{/color} challenging a harder opponent, your winnings were boosted!"

                if (punkwins == 1):
                    narrator "{color=#0048ff}You discovered the alleyway!{/color} In the alleyway, you'll be able to find new Pokémon, and battle for as long as you want."
                    narrator "However, leaving will cause this period of free time to end."
            else:
                if (HasEvent("Silver", "Overthrown")):
                    show roughneck happy teamrocket with dis
                else:
                    show roughneck happy with dis
                
                $ totallosses = math.floor(money / 10.0)
                $ money -= totallosses
                narrator "You lost $[totallosses]..."

            hide roughneck
            hide abandonedhouse
            with dis

            jump city

        "Visit Alleyway" if punkwins > 0:
            $ wildcount = 0
            call wildarea("alley") from _call_wildarea_3

        "Visit Seaport" if seaportunlocked or not IsBefore(1, 5, 2004):
            $ wildcount = 0
            call wildarea("seaport") from _call_wildarea_4

        "Buy Items":
            call screen shopkeep(shopitems)
            $ boughtitem = _return
            if (boughtitem == "Back"):
                jump city
            else:
                $ totalcost = boughtitem[0] * boughtitems
                if (totalcost > money):
                    narrator "You can't afford that!"
                else:
                    $ itemname = GetItemName(boughtitem[1])
                    $ money -= totalcost 
                    if (boughtitems > 1):
                        narrator "You bought [boughtitems] [itemname]s for $[totalcost]!"
                    else:
                        narrator "You bought a [itemname] for $[totalcost]!"
                    $ GetItem(itemname, boughtitems)
                    if (boughtitems >= 10 and ItemHasCategory(boughtitem[1], "Poké Balls")):
                        narrator "You also got a Premier Ball as an added bonus!"
                        $ GetItem("Premier Ball", 1)
                    $ boughtitems = 1

                jump citysetup

        "Heal Party":
            $ HealParty()
            jump citysetup

        "Access Janine's PC":
            $ currentbox = max(0, currentbox)
            show screen partymons
            call screen pokemonswap
            hide screen partymons
            jump citysetup

        "Head Back to Campus":
            narrator "Are you sure you want to head back to campus? Doing so will end this free time."

            menu:
                "Yes, I'm sure.":
                    $ location = "school"
                    pass

                "Never mind.":
                    jump citysetup
return