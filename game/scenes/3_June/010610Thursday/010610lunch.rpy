label lunch010610:

show bruno professor with Dissolve(1.0)

narrator "As you walk into the cafeteria, you see, true to his word, Bruno is instructing various students' Pokémon on the usage of Stealth Rock."

bruno @talking2mouth "[ellipses]You there, [first_name]."

if (WonBattle("BeaBruno1")):
    bruno @talking2mouth "I remember when you defeated Bea and I alongside Alder." 
else:
    bruno @talking2mouth "Do you remember when you floundered in combat alongside Alder and I?"

    red uniform @wince talking2mouth "I wouldn't necessarily call it 'floundering'[ellipses]"

    bruno @talking2mouth "Mastery of Stealth Rock would not have aided you in that fight, as both Bea and I had teams entirely resistant to it."
    bruno @closedbrow talkingmouth "However! We have built our teams to counter Stealth Rock {i}specifically{/i} because we are aware of what a potent weapon it is."

bruno @talkingmouth "I encourage you to make use of my training. I believe you could use this technique effectively."

python:
    hassplintershield = False
    hasstealthrock = False
    namedmon = None
    for mon in playerparty:
        if ("Splinter Shield" in mon.GetMoveNames()):
            hassplintershield = True
            namedmon = mon
            break
        elif ("Stealth Rock" in mon.GetMoveNames()):
            hasstealthrock = True
            if (not hassplintershield):
                namedmon = mon
        elif (MonCanLearn(mon, "Stealth Rock")):
            if (not (hassplintershield or hasstealthrock)):
                namedmon = mon

if (hassplintershield):
    red uniform @talking2mouth "I'm not sure, Sir. My [namedmon.GetSpeciesName()] already knows Splinter Shield, which feels like it might just be an upgrade?"

    bruno @talking2mouth "It is a valuable move, and one Instructor Olivia should be rightly proud of creating. However, it relies on your opponent to make contact with a physical move in order to scatter its splintered shards."
    bruno @closedbrow talking2mouth "It is rare that a strategy that requires one's opponent to make mistakes in combat cannot be improved."
    bruno @talking2mouth "There may even be merit in using both... if one considers Splinter Shield as an upgrade to Protect, rather than Stealth Rock."

elif (hasstealthrock):
    red uniform @talking2mouth "Sorry, Sir. My [namedmon.GetSpeciesName()] already knows Stealth Rock."

    bruno @talking2mouth "Understood."
    bruno @closedbrow talking2mouth "There is little lost by utilizing multiple Pokémon capable of using Stealth Rock, but as a newer trainer, perhaps it is best to have every Pokémon in your party maintain their clearly defined roles."
    bruno @talking2mouth "Regardless, I will leave the option open to you."

elif (namedmon == None):
    red uniform @talking2mouth "Sorry, Sir. I don't have any Pokémon capable of learning Stealth Rock with me."

    bruno @talking2mouth "Understood. Perhaps something to consider."
    bruno @talking2mouth "Kobukan as a region is quite fond of their multi-battles, where Stealth Rock's power is lesser, but it still remains, arguably, the most important move in honorable one-on-one confrontations."

    red @happy "Right. I'll keep that in mind!"

    hide bruno with dis

    jump PickTable

narrator "Would you like to have Bruno tutor one of your Pokémon in Stealth Rock?"

menu:
    "Yes":
        pass

    "No":
        hide bruno with dis

        jump PickTable

label brunostealthrock:

call screen SelectMon
$ tutormon = _return

if (tutormon == 'back'):
    bruno @closedbrow talking2mouth "Confirm your intent."

    menu:
        "I don't want any of my Pokémon to learn Stealth Rock.":
            bruno @talking2mouth "Very well."

        "On second thought...":
            jump brunostealthrock

elif (tutormon == pikachuobj):
    bruno @sadbrow talking2mouth "I must admit I am unsure how I would teach your Pikachu. It is altogether dissimilar to the Kantonian variants I am familiar with."

    jump brunostealthrock

else:
    $ tutormon = _return
    $ tutormonname = tutormon.GetSpeciesName()

    bruno @talking2mouth "Your [tutormonname]. Very well."
    
    $ knowsstealthrock = "Stealth Rock" in tutormon.GetMoveNames()
    $ canlearnstealthrock = MonCanLearn(tutormon, "Stealth Rock")

    if (knowsstealthrock):
        bruno @talking2mouth "This Pokémon already knows Stealth Rock. I can enhance the power and efficiency of the move, but not over the course of a single lunch period."

        jump brunostealthrock

    elif (not canlearnstealthrock):
        bruno @talking2mouth "I do not know how to teach this Pokémon Stealth Rock. It may be possible, yet, but I must continue my {i}own{/i} training first, before the method is revealed to me."

        jump brunostealthrock

    else:
        bruno @angrybrow talking2mouth "Let us begin."

        $ tutormon.LearnNewMove("Stealth Rock")

        if ("Stealth Rock" not in tutormon.GetMoveNames()):
            jump brunostealthrock
        else:
            $ AddEvent("Bruno", "StealthRockTutor")
            red uniform @talkingmouth "Thanks, Sir!"

            pause 1.0

            bruno @closedbrow talking2mouth "Such a polite student. I almost feel guilty that I'm doing this to spite Alder, now[ellipses]"

            pause 1.0

            bruno @closedbrow talkingmouth "Almost."

            hide bruno with dis

            pause 2.0

            narrator "As you prepare to go to a lunch table, you can feel something prickling the back of your neck[ellipses]"

            show bea uniform angrybrow frownmouth with Dissolve(1.0):
                xpos 0.05

            pause 1.0

            narrator "Seems Bea might be a bit jealous. It looks like she was too nervous to join the queue."

            red @happy "Hey, you can come up here, too. There's still some of lunch left!"

            show bea lightblush lookupbrow with dis

            bea "[ellipses]"

            hide bea with dis

            redmind @happybrow "Hah. I guess she {i}really{/i} idolizes Bruno, huh?"

            $ ValueChange("Bea", 1, 0.05)

hide bruno with dis

jump PickTable