label testcontest:

python:
    coordinators = [
        CoordinatorGroup([
            Coordinator(first_name, condition=0, isprotag=True)
        ]),
        CoordinatorGroup([
            Coordinator("Brendan", condition=30)
        ]),
        CoordinatorGroup([
            Coordinator("May", condition=15)
        ]),
        CoordinatorGroup([
            Coordinator("Jasmine", condition=5)
        ]),
        CoordinatorGroup([
            Coordinator("Dawn", condition=45)
        ])        
    ]

    judges = [
        Judge(wallace, biases={ ContestMoveType.Cute : 20, ContestMoveType.Beautiful : 30, ContestMoveType.Cool : 30, ContestMoveType.Clever : 10, ContestMoveType.Tough : 30 }),
        Judge(fantina, biases={ ContestMoveType.Cute : 10, ContestMoveType.Beautiful : 30, ContestMoveType.Cool : 30, ContestMoveType.Clever : 30, ContestMoveType.Tough : 20 }),
        Judge(phobos, biases={ ContestMoveType.Cute : 30, ContestMoveType.Beautiful : 30, ContestMoveType.Cool : 20, ContestMoveType.Clever : 30, ContestMoveType.Tough : 10 })
    ]

    contestconditions = {
        "Types" : ["Water", "Ghost", "Flying"],
        "Region" : range(252, 387),#Hoenn
        "Traits" : [ContestMoveType.Beautiful, ContestMoveType.Cool]
    }

call Contest("Test Contest", coordinators, judges, contestconditions) from _call_Contest

"reached here"

return






label Contest(contestname, coordinators, judges, contestconditions):

call clearscreens() from _call_clearscreens_233
scene contesttheater

python:
    HealParty()
    renpy.suspend_rollback(True)
    renpy.block_rollback()
    CurrentContest = contestname
    InContest = True
    StrictlyInContest = True
    Turn = 1
    ContestConditions = contestconditions
    Judges = judges
    Coordinators = coordinators
    Coordinators = sorted(Coordinators, key=lambda coord: -coord.EvaluateCondition())
    ProtagCoordinator = None
    for coord in Coordinators:
        if (coord.IsProtag()):
            ProtagCoordinator = coord
            break
    showround = False
    RealignTextbox()

show screen ContestUI

#Animate the coordinators lining up like a boy band, then sending out their Pokémon

#iterate through the judges as each states what they're looking for in the following round

if (contestname == "Dorm 25 Central Suite Grand Open"):
    Character("Announcer") "\"The peasants are revolting, and they're not happy, either! Words and weapons won't work here! Only a stylish and cool Contest Performance can possibly soothe their aggravated hearts.\""

else:
    $ AddEvent("Professor Oak", "LearnedAboutContestColiseum")
    Character("Announcer") "\"It's a hot day in the Contest Coliseum! The judges look like they're in fine form, chatting and gossiping... the atmosphere is right for a showdown of coordinators!\""

Character("Announcer") "\"Let's see... what will the judges want to be seeing today?\""

python:
    for judge in judges:
        judge.SetSeeking()
        renpy.pause(0.3)

Character("Announcer") "\"Great! The judges are ready, and the crowd's raring to go! Let's see the performers!\""

python:
    Coordinators[0].DisplayIntroStart(0)
    renpy.say(Character("Announcer"), "\"In the first seed, it's [Coordinators[0].GetName()], performing with [Coordinators[0].GetFirstMonName()]! We all have high expectations for this one!\"")
    Coordinators[0].DisplayIntroEnd()

    Coordinators[1].DisplayIntroStart(1)
    renpy.say(Character("Announcer"), "\"In the second seed, it's [Coordinators[1].GetName()], performing with [Coordinators[1].GetFirstMonName()]! Can the first seed be taken down?\"")
    Coordinators[1].DisplayIntroEnd()

    Coordinators[2].DisplayIntroStart(2)
    pronouncalc = ("are they" if Coordinators[2].GetSex() == Genders.Unknown else ("is he" if Coordinators[2].GetSex() == Genders.Male else "is she"))
    renpy.say(Character("Announcer"), "\"In the third seed, it's [Coordinators[2].GetName()], performing with [Coordinators[2].GetFirstMonName()]! Beware the quiet ones! What tricks [pronouncalc] hiding?\"")
    Coordinators[2].DisplayIntroEnd()

    Coordinators[3].DisplayIntroStart(3)
    renpy.say(Character("Announcer"), "\"In the fourth seed, it's [Coordinators[3].GetName()], performing with [Coordinators[3].GetFirstMonName()]! Quite a ways to climb--quite a bit to gain!\"")
    Coordinators[3].DisplayIntroEnd()

    Coordinators[4].DisplayIntroStart(4)
    pronouncalc = ("these performers" if Coordinators[4].IsGroup() else "this performer")
    pronouncalc2 = ("them" if Coordinators[4].GetSex() == Genders.Unknown else ("him" if Coordinators[4].GetSex() == Genders.Male else "her"))
    renpy.say(Character("Announcer"), "\"In the final seed, it's [Coordinators[4].GetName()], performing with [Coordinators[4].GetFirstMonName()]! There's no doubt that [pronouncalc] has something to prove! Let's give [pronouncalc2] the chance!\"")
    Coordinators[4].DisplayIntroEnd()

    for i, coord in enumerate(Coordinators):
        for j, coordinator in enumerate(coord.GetImage()): 
            renpy.show(coordinator, at_list=[moveincontest((i + 1) / 7.3, j, len(coord.GetImage()), 2.5)])

pause 1.0

Character("Announcer") "\"The performers are all ready! The lights are queued! The audience is on the edge of their seats... so, without any further ado, let's start the music!"

label ContestRound:

if (Turn == 11):
    $ showround = False
    jump ContestResults

elif (Turn > 1):
    python:
        for coord in Coordinators:
            coord.ResetCurrentPoints()
        InActiveContestRound = False
        announcer_dialog = {
            2: "Marvelous! Round two awaits--let the excitement continue!",
            3: "Splendid! We are now entering round three!",
            4: "How thrilling! Round four is upon us--let's dive in!",
            5: "Fantastic! It's time for round five to shine! As always, point values at the end of round five are doubled!",
            6: "Excellent! Let us embrace the challenge of round six!",
            7: "Remarkable! We move on to round seven--prepare yourselves!",
            8: "Incredible! Round eight begins--let the spectacle unfold!",
            9: "Fabulous! We now enter round nine--anticipation mounts!",
            10: "Superb! The grand finale of round ten is here--let's make it unforgettable! Remember, all point values at the end of round ten are tripled!"
        }

    # Display the correct announcement based on the current Turn
    Character("Announcer") "\"[announcer_dialog[Turn]]\""

python:
    PlannedMoves = []#has planned moves put in in-order. Elements are (coordinatorobj, moveeffect, moveused, predictedpoints, hasswitched)

    for i in range(len(Coordinators)):
        coord = Coordinators[i]
        coord.ResetCurrentPoints()
        if (not coord.IsProtag()):
            movevals = {}
            maxpointsearned = 0
            for move in coord.GetMoves():
                pointsearned = coord.CalculateMove(move)
                if (pointsearned > maxpointsearned):
                    maxpointsearned = pointsearned
                movename = move.Name
                movevals[move] = round(pointsearned)
                #print((movename, "Point value: " + str(pointsearned), "Safe: " + str(IsRoutineMove(move)), "Appeal bonus: " + str(appealstojudges), "Unappeal penalty: " + str(unappealstojudges), "Jackpot: " + str(jackpothit), "Effect: " +  GetmoveincontestEffect(move)))
            moveselected = weighted_random_selection(movevals)
            #print(moveselected.Name + " was selected")
            usingenergy = coord.CalculateEnergySpending(moveselected)
            PlannedMoves.append((coord, GetmoveincontestEffect(moveselected), moveselected, maxpointsearned, False, usingenergy))
        else:
            renpy.say(None, "What will you do in the following round?")
            renpy.show_screen("ContestUIAbove")
            showround = True
            renpy.transition(dis)
            contestaction = None
            actiontype, movemon, hasswitched, usingenergy = renpy.call_screen("ContestChoices", coordinator=coord, startingmon = coord.GetMon())
            PlannedMoves.append((coord, GetmoveincontestEffect(movemon), movemon, actiontype, hasswitched, usingenergy))
            renpy.hide_screen("ContestUIAbove")

Character("Announcer") "\"The performers are ready to rock! Let's see the performances begin!"

python:
    for i, coord in enumerate(Coordinators):
        coord.ResetCurrentPoints()
        for j, coordinator in enumerate(coord.GetImage()): 
            renpy.show(coordinator, at_list=[moveincontest( (i + 1) / 7.3, j, len(coord.GetImage()), 1.35, 2.5 )])

python:
    InActiveContestRound = True
    DulledPerformances = []
    # performancetypes = {}
    for i, plannedmove in enumerate(PlannedMoves):
        dulledimmune = False
        extrapoints = 0
        coord, effect, movemon, predictedpoints, switchingout, investedenergy = plannedmove
        coord.ResetPriority()
        images = coord.GetImage("angrybrow")
        for j, image in enumerate(images):
            renpy.show(image, at_list=[slideincontest(0.33, j, len(images))])
        sidemonnew = coord.GetMon()
        renpy.show("sideportraitnew", at_list=[slideinmoncontest()])
        if (switchingout):
            if not coord.IsProtag():
                coord.Reorder(movemon)
            coord.UnNoteReaction()
            renpy.say(Character("Announcer"), "\"Looks like {} is switching out to {} {}! What will this new Pokémon bring to the table, I wonder?\"".format(coord.GetName(), coord.GetHisPronoun(), coord.GetFirstMonName()))
        if investedenergy:
            coord.ResetEnergy()
        coord.GetMon().PlayCry()
        renpy.pause(1)
        renpy.show("sideportraitnew", at_list=[contestmoveanimation(investedenergy > 0)])
        renpy.pause(0.6)
        renpy.sound.play("normaldamage.ogg")
        repetitive = False
        if (RepeatedMove(coord, Turn, movemon)):
            repetitive = True
            isare = "is" if coord.IsSolo() else "are"
            renpy.say(Character("Announcer"), "\"Oh... it looks like [coord.GetName()] [isare] having [coord.GetFirstMonName()] use [movemon.Name] again... I'm not sure the judges will be excited to see that!\"")
        else:
            renpy.say(Character("Announcer"), "\"" + coord.GetPerformanceDialog(movemon, investedenergy) + "\"")
        if investedenergy and not switchingout:
            coord.AwardedPoints(3*investedenergy, None)

        totalpointsearned = 0
        jackpotjudge = None

        for judge in Judges:
            pointsearned = 2
            if (repetitive):
                pointsearned -= 1
            if (ContestStringToMacro(movemon.Contest) == judge.GetSeeking()):
                pointsearned += 1
                if (not repetitive):
                    judge.IncreaseSparks()
                if (judge.GetSparks() < judge.GetJackpotLimit()):
                    images = coord.GetImage("angrybrow")
                    for image in images:
                        renpy.show(image)
                else:
                    jackpotjudge = judge
                    pointsearned += 10
                
            if (GetmoveincontestEffect(movemon) == ContestEffects.Risky and Jams(judge.GetSeeking(), ContestStringToMacro(movemon.Contest))):
                judge.DecreaseSparks()
            if (pointsearned != 0):
                coord.AwardedPoints(pointsearned, judge)
        
        if (jackpotjudge != None):
            images = coord.GetImage("happy")
            for image in images:
                renpy.show(image)
            renpy.say(None, "The performance went over incredibly well with [jackpotjudge.GetName()]! [jackpotjudge.GetHePronoun().title()]'s clapping and shouting! What a show!")
            jackpotjudge.ResetSparks()

        extrapoints = 0
        if (GetmoveincontestEffect(movemon) == ContestEffects.Jamming):
            for otherplannedmove in PlannedMoves[:i]:
                othercoord, othereffect, othermovemon, otherpredictedpoints, otherswitchingout, otherinvestedenergy = otherplannedmove
                if (not otherswitchingout and Jams(othermovemon.Contest, movemon)): 
                    if (GetmoveincontestEffect(othermovemon) == ContestEffects.Unjammable):
                        renpy.say(Character("Announcer"), "\"Remarkable! Even in the face of a jamming [movemon.Name], [othercoord.GetName()] maintains [othercoord.GetHisPronoun()] routine! Such concentration!\"")
                    else:
                        renpy.say(Character("Announcer"), "\"Oh no! The jamming [movemon.Name] completely threw off [othercoord.GetName()]'s appeal! Can [othercoord.GetHePronoun()] recover from this?!\"")
                        othercoord.JamPoints()
        elif (GetmoveincontestEffect(movemon) == ContestEffects.Unjammable):
            renpy.say(Character("Announcer"), "\"Look at [coord.GetName()] pull off that routine so flawlessly! There's something to be said for simple perfection, folks!\"")
        elif (GetmoveincontestEffect(movemon) == ContestEffects.Dull and movemon.Contest not in DulledPerformances):
            dulledimmune = True
            DulledPerformances.append(movemon.Contest)
            renpy.say(Character("Announcer"), "\"What's this?! The judges are keeping a keen eye on [coord.GetName()] now! I'm not sure that any other [movemon.Contest] performances will stand out, now!\"")
        elif (GetmoveincontestEffect(movemon) == ContestEffects.Showoff):
            renpy.say(Character("Announcer"), "\"What a flashy performance! I'd wager [coord.GetName()] will definitely be going to the first seed of the next round!\"")
            coord.SetPriority(i * 1000)
        elif (GetmoveincontestEffect(movemon) == ContestEffects.Soothe):
            renpy.say(Character("Announcer"), "\"What's [coord.GetName()] hiding up their sleeve? If they're trying to grab the fifth seed of the next round, they've just done it!\"")
            coord.SetPriority(i * -1000)
        elif (GetmoveincontestEffect(movemon) == ContestEffects.Finale and i == 4):
            images = coord.GetImage("angrybrow")
            for image in images:
                renpy.show(image)
            extrapoints += 3
            renpy.say(Character("Announcer"), "\"Wow! What an incredible way to wrap up the round, ladies and gentleman! [coord.GetName()]'s finale absolutely blew out the competition!\"")
        elif (GetmoveincontestEffect(movemon) == ContestEffects.Spark and i == 0):
            images = coord.GetImage("angrybrow")
            for image in images:
                renpy.show(image)
            extrapoints += 3
            renpy.say(Character("Announcer"), "\"That's a {i}very{/i} strong start to the round, ladies and gentleman! [coord.GetName()]'s performance will be a tough act to follow!\"")

        if (not dulledimmune and GetmoveincontestEffect(movemon) != ContestEffects.Unjammable and movemon.Contest in DulledPerformances):
            images = coord.GetImage("sad")
            for image in images:
                renpy.show(image)
            renpy.say(Character("Announcer"), "\"Oh, but what a shame! Did [coord.GetName()] forget? There's already been a very impressive [movemon.Contest] performance this round, and you don't stand out as a follower! It's a jam for [coord.GetHimPronoun()] now!\"")
            coord.JamPoints()

        preposition = ("is" if coord.IsSolo() else "are")
        if (coord.GetEnergy() == 1):
            extrapoints += 1
            renpy.say(Character("Announcer"), "\"[coord.GetName()] [preposition] showing great energy right now!\"")
        elif (coord.GetEnergy() == 2):
            extrapoints += 2
            renpy.say(Character("Announcer"), "\"[coord.GetName()] has seriously found [coord.GetHisPronoun()] flow! Look at that energy!\"")
        elif (coord.GetEnergy() == 3):
            extrapoints += 3
            renpy.say(Character("Announcer"), "\"[coord.GetName()] [preposition] absolutely bursting with energy! It's a runaway train, and we're all onboard!\"")

        if (not (isinstance(predictedpoints, str) or (switchingout and Turn != 1))):
            if (movemon.Type in coord.GetMon().GetTypes(pureraw=True)):
                if (coord.GainEnergy()):
                    if (coord.IsProtag()):
                        renpy.show_screen("energyupleft", coord.GetName())
                    else:
                        renpy.show_screen("energyupright", coord.GetName())

        if (extrapoints > 0):
            coord.AwardedPoints(extrapoints, None)

        if (coord.GetCurrentPoints() < 3):
            images = coord.GetImage("sadbrow")
            for image in images:
                renpy.show(image)
            renpy.say(None, "The judges don't seem impressed...")
        elif (coord.GetCurrentPoints() > 7 and coord.GetCurrentPoints() < 11):
            images = coord.GetImage("happybrow")
            for image in images:
                renpy.show(image)
            renpy.say(None, "The judges seem impressed!")
        elif (coord.GetCurrentPoints() > 10):
            images = coord.GetImage("happy")
            for image in images:
                renpy.show(image)
            renpy.say(None, "The judges are ecstatic!")

        images = coord.GetImage("-sadbrow -happy -angrybrow")
        for j, image in enumerate(images):
            renpy.show(image, at_list=[moveincontest(0.33, 0, 1, 1.0, 2.5)])
        renpy.show("sideportraitnew", at_list=[slideoutmoncontest()])
        renpy.pause(1.0)

    for plannedmove in PlannedMoves:
        coord, stance, movemon, predictedpoints, switchingout, investedenergy = plannedmove
        suitability = EvaluateSuitability(coord.GetMon(), ContestConditions)

        if (coord.IsProtag()):
            if (coord.NotReactionNoted()):
                coord.NoteReaction()
                if (suitability == -1):
                    renpy.say(Character("Announcer"), "\"Oh...? Seems the crowd isn't too enthused at seeing [coord.GetName()]'s [coord.GetFirstMonSpeciesName()]...\"")
                elif (suitability == 1):
                    renpy.say(Character("Announcer"), "\"Oh? Listen to that crowd! It sounds like they like seeing [coord.GetName()]'s [coord.GetFirstMonSpeciesName()]!\"")
                elif (suitability == 3):
                    renpy.say(Character("Announcer"), "\"Wow! The crowd's really excited to see more of [coord.GetName()]'s [coord.GetFirstMonSpeciesName()]!\"")
                elif (suitability == 5):
                    renpy.say(Character("Announcer"), "\"Good golly! Listen to that roaring crowd! And everyone's cheering at the chance to see [coord.GetName()]'s [coord.GetFirstMonSpeciesName()]!\"")

        coord.RecordSuitability(Turn, suitability)

        if isinstance(predictedpoints, str):
            coord.RecordMove(Turn, None)
        else:
            coord.RecordMove(Turn, movemon.Name)

    if (Turn == 5):
        renpy.say(Character("Announcer"), "\"Did you forget? It's round five! And that means everyone's points get doubled! That'll matter at the end!\"")
        for plannedmove in PlannedMoves:
            coord, stance, movemon, predictedpoint, switchingout, investedenergy = plannedmove
            coord.MultiplyCurrentPoints(2)
    if (Turn == 10):
        renpy.say(Character("Announcer"), "\"A remarkable finale, ladies and gentlemen! At the end of round ten, we {i}triple{/i} the contestants' points! Will this make the difference?!\"")
        for plannedmove in PlannedMoves:
            coord, stance, movemon, predictedpoints, switchingout, investedenergy = plannedmove
            coord.MultiplyCurrentPoints(3)

    for plannedmove in PlannedMoves:
        coord, stance, movemon, predictedpoints, switchingout, investedenergy = plannedmove
        coord.RecordRound(Turn, coord.GetCurrentPoints())


Character("Announcer") "\"The rankings are in for this round, folks! Let's see what the placings are, then...\""
show screen ContestUIAbove

python:
    positiondic = {}
    for i, coord in enumerate(Coordinators):
        positiondic[coord] = (i+1) / 7

    Coordinators = sorted(Coordinators, key=lambda x:x.GetCurrentPoints() + x.GetPriority(), reverse=True)

    for i, coord in enumerate(Coordinators):
        images = coord.GetImage(overridemood=11-5*i)
        for j, image in enumerate(images):
            renpy.show(image, at_list=[coordposswitch(positiondic[coord], (i+1) / 7.3, j, len(images))])

pause 2.0

$ Turn += 1

jump ContestRound

label ContestResults:

hide screen ContestUIAbove with dis


Character("Announcer") "\"That's a wrap, everyone! The appeals are over! Nothing's left but the crying, now!\""

python:
    for i, coord in enumerate(Coordinators):
        coord.ResetCurrentPoints()
        renpy.transition(dis)
        images = coord.GetImage()
        for j, image in enumerate(images):
            renpy.hide(image)
            renpy.show(image, at_list=[coordposswitch((i+1) / 7.3, (i+1) / 7.3, j, len(images))])

Character("Announcer") "\"The judges are deliberating...\""

Character("Announcer") "\"{w=0.5}.{w=0.5}.{w=0.5}.\""
Character("Announcer") "\"{w=0.5}.{w=0.5}.{w=0.5}.\""
Character("Announcer") "\"{w=0.5}.{w=0.5}.{w=0.5}.\""

Character("Announcer") "\"While we're waiting on them to reach a decision, let's check in with the audience! Points will be awarded based on how much the Coordinators' Pokémon resonated with the audience--let's find out!\""

show screen ContestUIAbove(False) with dis

python:
    for coord in Coordinators:
        coord.CurrentPoints = coord.SumSuitability()

pause 3.0

Character("Announcer") "\"Popular opinion isn't everything, but it sure helps! Let's reveal the results of the rounds, now, starting from round zero, the seeding round! The Coordinators and their Pokémon were evaluated on their physical condition!\""

show screen ContestUIAbove(False) with dis

python:
    showround = True
    Turn = 0
    renpy.pause(1.0)

    highestval = 0
    for coord in Coordinators:
        conditionpoints = coord.GetPointsOnTurn(0)
        if (conditionpoints > highestval):
            highestval = conditionpoints
    
    for coord in Coordinators:
        coord.CurrentPoints += math.ceil(50 * (coord.GetPointsOnTurn(0) / highestval))

pause 3.0

Character("Announcer") "\"First impressions can be deceiving! Did anyone expect {i}this{/i} outcome from the seeding? Let's see if the performance rounds matched the seeding! It's time for the final countdown!\""

python:
    for i in range(1, 11):
        Turn = i
        for coord in Coordinators:
            coord.CurrentPoints += coord.GetPointsOnTurn(i)
        renpy.pause(1)

pause 2.0
hide screen ContestUIAbove
$ showround = False
Character("Announcer") "\"And that's everything, ladies and gentlemen! As always, the Coordinator or Coordinators with the most points is the winner, and that means the winner can only be...!\""
pause 1.0

python:
    for i, coord in enumerate(Coordinators):
        for j, coordinator in enumerate(coord.GetImage()): 
            renpy.show(coordinator, at_list=[moveincontest( (i + 1) / 7.3, j, len(coord.GetImage()), 1.35, 2.5 )])
        renpy.pause(0.5)
    StrictlyInContest = False
    RealignTextbox()

    Coordinators = sorted(Coordinators, key=lambda coord: -coord.GetCurrentPoints())
    contesthistory[CurrentContest] = Coordinators
    lastwinner = Coordinators[0]

hide screen ContestUI with dis
scene blank2
show contest_stage with dis:
    xcenter 0.5 ycenter 0.5
    linear 1.0 zoom 1.25
pause 2.0
play sound "audio/Button_Back.ogg"
show contestdark_stage:
    xcenter 0.5 ycenter 0.5 zoom 1.25
show contestdark_curtains as curtains:
    xcenter 0.5 ycenter 0.5 zoom 1.25
python:
    for i, coordinator in enumerate(lastwinner.GetImage()): 
        renpy.show(coordinator, at_list=[contestwinner(i, lastwinner.GroupSize())], behind="curtains")
pause 5.0
Character("Announcer") "\"{cps=*0.4}Here it comes[ellipses]{/cps}\""
pause 2.0
show contest_light:
    xcenter 0.5 ycenter 0.5 zoom 1.25
python:
    for i, coordinator in enumerate(lastwinner.GetImage()): 
        renpy.show(coordinator, at_list=[contestwinnerreveal(i, lastwinner.GroupSize())])
play sound "audio/Button_Back.ogg"
pause 0.5
play sound "audio/Get.ogg"
pause 8
Character("Announcer") "\"[lastwinner.GetName()]!\""
play sound "audio/crowd_cheer.ogg"
python:
    for i, coordinator in enumerate(lastwinner.GetImage("happy")): 
        renpy.show(coordinator, at_list=[contestwinnerreveal(i, lastwinner.GroupSize())])
pause 10

call clearcontestscreens() from _call_clearcontestscreens_1
$ InContest = False
$ renpy.suspend_rollback(False)
$ renpy.block_rollback()

return