label DeoxysContest(contestname, coordinators, judges, contestconditions):

call clearscreens() from _call_clearscreens_274
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
    showround = False
    RealignTextbox()

show screen ContestUI

#Animate the coordinators lining up like a boy band, then sending out their Pokémon

#iterate through the judges as each states what they're looking for in the following round

TempCharacter("Announcer") "Watch out! It's not only the coordinators who are bringing the house down today! The alien entity is firing off powerful psychic attacks wildly, and everyone's in mortal peril! Don't let the panic make you pitchy, coordinators!"
TempCharacter("Announcer") "Let's see... what does this weird entity want to see today?"

python:
    for judge in judges:
        judge.SetSeeking()
        renpy.pause(0.3)

TempCharacter("Announcer") "Great! The weird entity--and its two duplicates--are ready, and the crowd's nonexistent! Let's see the performers!"

python:
    Coordinators[0].DisplayIntroStart(0)
    himpronoun = Coordinators[0].GetHimPronoun()
    hepronoun = Coordinators[0].GetHePronoun()
    if (hepronoun == "they"):
        hepronoun = "they're"
    else:
        hepronoun = hepronoun + "'s"
    renpy.say(TempCharacter("Announcer"), "In the first seed, it's [Coordinators[0].GetName()], performing with [Coordinators[0].GetFirstMonName()]! Look at [himpronoun], cool as a cucumber, like [hepronoun] not inches away from becoming a splatter on the floor!")
    Coordinators[0].DisplayIntroEnd()

    Coordinators[1].DisplayIntroStart(1)
    hepronoun = Coordinators[1].GetHePronoun()
    if (hepronoun == "they"):
        hepronoun = "they're"
    else:
        hepronoun = hepronoun + "'s"
    renpy.say(TempCharacter("Announcer"), "In the second seed, it's [Coordinators[1].GetName()], performing with [Coordinators[1].GetFirstMonName()]! You can barely even tell [hepronoun] having a panic attack!")
    Coordinators[1].DisplayIntroEnd()

    Coordinators[2].DisplayIntroStart(2)
    hispronoun = Coordinators[2].GetHisPronoun()
    renpy.say(TempCharacter("Announcer"), "In the third seed, it's [Coordinators[2].GetName()], performing with [Coordinators[2].GetFirstMonName()]! [hispronoun] hands are shaking--not great for coordination, is it?")
    Coordinators[2].DisplayIntroEnd()

    Coordinators[3].DisplayIntroStart(3)
    renpy.say(TempCharacter("Announcer"), "In the fourth seed, it's [Coordinators[3].GetName()], performing with [Coordinators[3].GetFirstMonName()], ready to put on a show to die for!")
    Coordinators[3].DisplayIntroEnd()

    Coordinators[4].DisplayIntroStart(4)
    renpy.say(TempCharacter("Announcer"), "In the final seed, it's [Coordinators[4].GetName()], performing with [Coordinators[4].GetFirstMonName()]! Let's just keep the ambulance on standby!")
    Coordinators[4].DisplayIntroEnd()

    for i, coord in enumerate(Coordinators):
        for j, coordinator in enumerate(coord.GetImage()): 
            renpy.show(coordinator, at_list=[moveincontest((i + 1) / 7.3, j, len(coord.GetImage()), 2.5)])

pause 1.0

TempCharacter("Announcer") "The performers are all ready! The lights are cued! There's no audience to get in the way... so, without any further ado, let's start the music!"

label DeoxysContestRound:

if (Turn == 11):
    $ showround = False
    jump DeoxysContestResults

elif (Turn > 1):
    python:
        for coord in Coordinators:
            coord.ResetCurrentPoints()
        InActiveContestRound = False
        announcer_dialog = {
            2: "Marvelous! Round two awaits--and somehow, against all medical advice, so do we!",
            3: "Splendid! We are now entering round three! The invisible audience remains absolutely silent with terror!",
            4: "How thrilling! Round four is upon us--let's dive in, preferably not in front of any stray psychic blasts!",
            5: "Fantastic! It's time for round five to shine! As always, point values at the end of round five are doubled--just like the odds of an abrupt and messy tragedy!",
            6: "Excellent! Let us embrace the challenge of round six, while the judges stare with eyes unblinking and eldritch!",
            7: "Remarkable! We move on to round seven--prepare yourselves, and any last words you may still have handy!",
            8: "Incredible! Round eight begins--let the spectacle unfold, along with several emergency evacuation plans!",
            9: "Fabulous! We now enter round nine--anticipation mounts, as does the structural damage!",
            10: "Superb! The grand finale of round ten is here--let's make it unforgettable for everyone who survives it! Remember, all point values at the end of round ten are tripled!"
        }

    # Display the correct announcement based on the current Turn
    TempCharacter("Announcer") "[announcer_dialog[Turn]]"

python:
    PlannedMoves = []#has planned moves put in in-order. Elements are (coordinatorobj, moveeffect, moveused, predictedpoints, hasswitched)

    for i in range(len(Coordinators)):
        coord = Coordinators[i]
        coord.ResetCurrentPoints()
        if (not coord.GetIsControllable()):
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

TempCharacter("Announcer") "The performers are ready to rock! The unblinking alien entity is ready to judge! The empty seats are ready to continue being empty! Let's see the performances begin!"

python:
    for i, coord in enumerate(Coordinators):
        coord.ResetCurrentPoints()
        for j, coordinator in enumerate(coord.GetImage()): 
            renpy.show(coordinator, at_list=[moveincontest((i + 1) / 7.3, j, len(coord.GetImage()), 1.35, 2.5)])

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
            if not coord.GetIsControllable():
                coord.Reorder(movemon)
            coord.UnNoteReaction()
            renpy.say(TempCharacter("Announcer"), "Looks like {} {} switching out to {} {}! A bold decision in these dire and audience-free conditions! What will this new Pokémon bring to the table, besides further risk to life and limb, I wonder?".format(coord.GetName(), coord.GetIsAre(), coord.GetHisPronoun(), coord.GetFirstMonName()))
        if investedenergy:
            coord.ResetEnergy()
        coord.GetMon().PlayCry()
        renpy.pause(1)
        renpy.show("sideportraitnew", at_list=[contestmoveanimation(investedenergy > 0)])
        renpy.pause(0.6)
        renpy.sound.play("normaldamage.ogg")
        repetitive = False
        announcerline = ""
        if (RepeatedMove(coord, Turn, movemon)):
            repetitive = True
            isare = "is" if coord.IsSolo() else "are"
            announcerline = "Oh[ellipses] it looks like [coord.GetName()] [isare] having [coord.GetFirstMonName()] use [movemon.Name] again[ellipses] In a venue with no audience and no margin for error, repetition is a dangerous choice!"
        else:
            announcerline = coord.GetPerformanceDialog(movemon, investedenergy, True)

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
            announcerline += "The performance went over incredibly well with [jackpotjudge.GetName()]! At least--probably? I can't really tell!"
            jackpotjudge.ResetSparks()

        extrapoints = 0
        if (GetmoveincontestEffect(movemon) == ContestEffects.Jamming):
            for otherplannedmove in PlannedMoves[:i]:
                othercoord, othereffect, othermovemon, otherpredictedpoints, otherswitchingout, otherinvestedenergy = otherplannedmove
                if (not otherswitchingout and Jams(movemon.Contest, othermovemon.Contest)): 
                    if (GetmoveincontestEffect(othermovemon) == ContestEffects.Unjammable):
                        announcerline += "Remarkable! Even in the face of a jamming [movemon.Name], [othercoord.GetName()] maintains [othercoord.GetHisPronoun()] routine! Such concentration, especially while death hovers politely nearby!"
                    else:
                        announcerline += "Oh no! The jamming [movemon.Name] completely threw off [othercoord.GetName()]'s appeal! Have you all forgotten you should be working {i}together?{/i}"
                        othercoord.JamPoints(sidebar=True)
        elif (GetmoveincontestEffect(movemon) == ContestEffects.Unjammable):
            announcerline += "Look at [coord.GetName()] pull off that routine so flawlessly! There's something to be said for simple perfection, folks--especially today, when overcomplicating things may get somebody vaporized!"
        elif (GetmoveincontestEffect(movemon) == ContestEffects.Dull and movemon.Contest not in DulledPerformances):
            dulledimmune = True
            DulledPerformances.append(movemon.Contest)
            announcerline += "What's this?! The judges are keeping a keen eye on [coord.GetName()] now! I'm not sure that any other [movemon.Contest] performances will stand out now. What a noble sacrifice, keeping the entity's attention squarely on [coord.GetHimPronoun()]!"
        elif (GetmoveincontestEffect(movemon) == ContestEffects.Showoff):
            announcerline += "What a flashy performance! I'd wager [coord.GetName()] will definitely be going to the first seed of the next round--assuming we all live to the next round!"
            coord.SetPriority(i * 1000)
        elif (GetmoveincontestEffect(movemon) == ContestEffects.Soothe):
            announcerline += "What's [coord.GetName()] hiding up [coord.GetHisPronoun()] sleeve? If it's a ploy to grab the fifth seed of the next round and avoid direct eye contact with the alien entity, brilliantly executed!"
            coord.SetPriority(i * -1000)
        elif (GetmoveincontestEffect(movemon) == ContestEffects.Finale and i == 4):
            images = coord.GetImage("angrybrow")
            for image in images:
                renpy.show(image)
            extrapoints += 3
            announcerline += "Wow! What an incredible way to wrap up the round, ladies and gentlemen! [coord.GetName()]'s finale attracted {i}all{/i} of the entity's attention! Is that a good thing?"
        elif (GetmoveincontestEffect(movemon) == ContestEffects.Spark and i == 0):
            images = coord.GetImage("angrybrow")
            for image in images:
                renpy.show(image)
            extrapoints += 3
            announcerline += "That's a {i}very{/i} strong start to the round, ladies and gentlemen! [coord.GetName()]'s performance will be a tough act to follow, particularly while everyone is busy not dying!"

        if (not dulledimmune and GetmoveincontestEffect(movemon) != ContestEffects.Unjammable and movemon.Contest in DulledPerformances):
            images = coord.GetImage("sad")
            for image in images:
                renpy.show(image)
            announcerline += "Oh, but what a shame! Did [coord.GetName()] forget? There's already been a very impressive [movemon.Contest] performance this round, and the only thing worse than an angry alien is a bored one! It's a jam for [coord.GetHimPronoun()] now!"
            coord.JamPoints()

        preposition = ("is" if coord.IsSolo() else "are")
        announcerline2 = ""
        if (coord.GetEnergy() == 1):
            extrapoints += 1
            announcerline2 += "[coord.GetName()] [preposition] showing great energy right now! That's exactly what you want when morale is low and the psychic bombardment is high!"
        elif (coord.GetEnergy() == 2):
            extrapoints += 2
            announcerline2 += "[coord.GetName()] has seriously found [coord.GetHisPronoun()] flow! Look at that energy! It almost matches the literal energy beams that are tearing up the arena!"
        elif (coord.GetEnergy() == 3):
            extrapoints += 3
            announcerline2 += "[coord.GetName()] [preposition] absolutely bursting with energy! It's a runaway train, the brakes aren't working, and we're all onboard!"

        if (not (isinstance(predictedpoints, str) or (switchingout and Turn != 1))):
            if (movemon.Type in coord.GetMon().GetTypes(pureraw=True)):
                if (coord.GainEnergy()):
                    if (coord.GetIsControllable()):
                        renpy.show_screen("energyupleft", coord.GetName())
                    else:
                        renpy.show_screen("energyupright", coord.GetName())

        if (extrapoints > 0):
            coord.AwardedPoints(extrapoints, None)

        if (announcerline):
            renpy.say(TempCharacter("Announcer"), FormatText(announcerline))
            if (announcerline2):
                renpy.say(TempCharacter("Announcer"), FormatText(announcerline2))

        if (coord.GetCurrentPoints() < 3):
            images = coord.GetImage("sadbrow")
            for image in images:
                renpy.show(image)
        elif (coord.GetCurrentPoints() > 7 and coord.GetCurrentPoints() < 11):
            images = coord.GetImage("happybrow")
            for image in images:
                renpy.show(image)
        elif (coord.GetCurrentPoints() > 10):
            images = coord.GetImage("happy")
            for image in images:
                renpy.show(image)

        #feebas evolution interruption
        prnt(coord.GetName(), Turn, coord.GetIsControllable(), coord.GetFirstMonSpeciesName())
        if (Turn == 10 and coord.GetIsControllable() and coord.GetFirstMonSpeciesName() == "Feebas"):
            AddEvent("Game", "EvolvedFeebas")
            renpy.pause(3.0)

            renpy.say(Character("Announcer"), "\"Wait[ellipses] what's going on with that Feebas? It's not leaving the stage[ellipses]\"")
            renpy.say(Character("Announcer"), "\"[coord.GetName()]! Is something wrong?\"")

            renpy.transition(Dissolve(3.0))
            renpy.show("blank2", [Transform(alpha=0.5)])

            renpy.say(narrator, "[coord.GetFirstMonName()] looks back at you pridefully as she refuses to vacate the stage.")
            renpy.say(narrator, "Such a comely fish[ellipses] this stage is not the place for one such at her. It's {i}far{/i} too small.")
            renpy.say(narrator, "This stage has become a puddle--no longer content to be the big fish of it, [coord.GetFirstMonName()] yearns for the sea.")
            renpy.say(narrator, "What star can endure a crowd of one who cheers for trickles, when they know they are capable of waves?")
            renpy.say(narrator, "{color=#46897c}Let us hear its screams as the ocean embraces it!{/color}")

            coord.GetMon().Evolve(350, force=True)

            renpy.transition(Dissolve(1.5))
            renpy.hide("blank2")

            renpy.pause(3.0)

            PlaySound("crowd_cheer.ogg")
            PlaySound("crowd_cheer.ogg")
            PlaySound("crowd_cheer.ogg")

            renpy.say(Character("Announcer"), "\"Aaaaaabsolutely incredible, ladies and gentlemen! Look at that, the alien entity's beaming with happiness!\"")
            renpy.say(Character("Announcer"), "\"A mid-contest evolution! How incredible! How stellar! How beautiful! The alien seems overjoyed--extra points? Sounds like it!\"")

            for judge in Judges:
                coord.AwardedPoints(10, judge)

            renpy.say(Character("Announcer"), "\"What a show! What a remarkable show!\"")

        for j, image in enumerate(images):
            renpy.show(image, at_list=[moveincontest(0.33, 0, 1, 1.0, 2.5)])
        renpy.show("sideportraitnew", at_list=[slideoutmoncontest()])
        renpy.pause(1.0)

    for plannedmove in PlannedMoves:
        coord, stance, movemon, predictedpoints, switchingout, investedenergy = plannedmove
        suitability = EvaluateSuitability(coord.GetMon(), ContestConditions)

        if (coord.GetIsControllable()):
            if (coord.NotReactionNoted()):
                coord.NoteReaction()
                if (suitability == -1):
                    renpy.say(TempCharacter("Announcer"), "Oh...? I think the entity just narrowed its eyes at [coord.GetName()]'s [coord.GetFirstMonSpeciesName()]! {i}That's{/i} not a good sign!")
                elif (suitability == 1):
                    renpy.say(TempCharacter("Announcer"), "Oh? The entity doesn't seem to be paying much attention to [coord.GetName()]'s [coord.GetFirstMonSpeciesName()]--which is probably a good thing, given the context!")
                elif (suitability == 3):
                    renpy.say(TempCharacter("Announcer"), "Hey! Is it just me, or is the entity almost trying to avoid [coord.GetName()]'s [coord.GetFirstMonSpeciesName()] with its Psychic attacks? That must be a good sign!")
                elif (suitability == 5):
                    renpy.say(TempCharacter("Announcer"), "Check {i}that{/i} out! I'm pretty sure the alien entity is {i}communicating{/i} with [coord.GetName()]'s [coord.GetFirstMonSpeciesName()]! Whatever they're doing, they're doing it right!")

        coord.RecordSuitability(Turn, suitability)

        if isinstance(predictedpoints, str):
            coord.RecordMove(Turn, None)
        else:
            coord.RecordMove(Turn, movemon.Name)

    if (Turn == 5):
        renpy.say(TempCharacter("Announcer"), "Did you forget? It's round five! And that means everyone's points get doubled! A lovely little perk for making it this far alive!")
        for plannedmove in PlannedMoves:
            coord, stance, movemon, predictedpoint, switchingout, investedenergy = plannedmove
            coord.MultiplyCurrentPoints(2)
    if (Turn == 10):
        renpy.say(TempCharacter("Announcer"), "A remarkable finale, ladies and gentlemen! At the end of round ten, we {i}triple{/i} the contestants' points! Will this make the difference between victory and obliteration?!")
        for plannedmove in PlannedMoves:
            coord, stance, movemon, predictedpoints, switchingout, investedenergy = plannedmove
            coord.MultiplyCurrentPoints(3)

    for plannedmove in PlannedMoves:
        coord, stance, movemon, predictedpoints, switchingout, investedenergy = plannedmove
        coord.RecordRound(Turn, coord.GetCurrentPoints())

TempCharacter("Announcer") "The rankings are in for this round, folks! Let's see what the placings are, then, before anything else catches fire!"
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

jump DeoxysContestRound

label DeoxysContestResults:

hide screen ContestUIAbove with dis

stop music fadeout 1.5

TempCharacter("Announcer") "That's a wrap, everyone! The appeals are over! Nothing's left but the crying, the tallying, and the lingering dread!"

python:
    for i, coord in enumerate(Coordinators):
        coord.ResetCurrentPoints()
        renpy.transition(dis)
        images = coord.GetImage()
        for j, image in enumerate(images):
            renpy.hide(image)
            renpy.show(image, at_list=[coordposswitch((i+1) / 7.3, (i+1) / 7.3, j, len(images))])

TempCharacter("Announcer") "The entity seems to be deliberating[ellipses]"
TempCharacter("Announcer") "While we're waiting on that thing to reach a decision, let's check in with the room!"
TempCharacter("Announcer") "There is, of course, no audience, but points will still be awarded based on how much the Coordinators' Pokémon soothed or stirred the terrified people present--let's find out!"

show screen ContestUIAbove(False) with dis

python:
    for coord in Coordinators:
        coord.CurrentPoints = coord.SumSuitability()

pause 3.0

TempCharacter("Announcer") "Popular opinion isn't everything, but when the stakes are high, every little bit helps!"
TempCharacter("Announcer") "Let's reveal the results of the rounds, now, starting from round zero, the seeding round! The Coordinators and their Pokémon were evaluated on their physical condition!"

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

TempCharacter("Announcer") "First impressions can be deceiving! Did anyone expect {i}this{/i} outcome from the seeding?"
TempCharacter("Announcer") "It's time for the final countdown, ascribing no particular extra meaning to the word 'final!'"

python:
    for i in range(1, 11):
        Turn = i
        for coord in Coordinators:
            coord.CurrentPoints += coord.GetPointsOnTurn(i)
        renpy.pause(1)

pause 2.0
hide screen ContestUIAbove
$ showround = False
TempCharacter("Announcer") "And that's everything, ladies and gentlemen! Or, more accurately, everything except the giant psychic emergency still unfolding around us!"
TempCharacter("Announcer") "As always, the Coordinator or Coordinators with the most points is the winner, and that means the winner can only be...!"
pause 1.0

python:
    for i, coord in enumerate(Coordinators):
        for j, coordinator in enumerate(coord.GetImage()): 
            renpy.show(coordinator, at_list=[moveincontest((i + 1) / 7.3, j, len(coord.GetImage()), 1.35, 2.5 )])
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
TempCharacter("Announcer") "{cps=*0.4}Here it comes[ellipses]{/cps}"
pause 2.0
show contest_light:
    xcenter 0.5 ycenter 0.5 zoom 1.25
python:
    for i, coordinator in enumerate(lastwinner.GetImage()): 
        renpy.show(coordinator, at_list=[contestwinnerreveal(i, lastwinner.GroupSize())])
play sound "audio/Button_Back.ogg"
pause 0.5
$ PlaySound("Get.ogg")
pause 8
TempCharacter("Announcer") "[lastwinner.GetName()]! A huge metaphorical round of applause from the entity! It looks like it may have {i}actually{/i} calmed down!"
play sound "audio/crowd_cheer.ogg"
python:
    for i, coordinator in enumerate(lastwinner.GetImage("happy")): 
        renpy.show(coordinator, at_list=[contestwinnerreveal(i, lastwinner.GroupSize())])
pause 10

call clearcontestscreens() from _call_clearcontestscreens_2
$ InContest = False
$ renpy.suspend_rollback(False)
$ renpy.block_rollback()

return