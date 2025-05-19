label morningscenequeue:

label FlanneryWhitneyMorningAfter:
    if (HasEvent("Whitney", "Whitney2Part2") and EventAvailable(["Flannery", "Whitney"], "FlanneryWhitneyMorningAfter", 2)):
        scene blank2
        
        play music "Audio/Music/Oak Intro.ogg" noloop
        queue music "Audio/Music/Oak Class.ogg"

        show homeroom behind blank2
            
        $ renpy.transition(dissolve)
        show screen currentdate

        show oakbg
        hide blank2 
        with splitfade

        oak @talking2mouth "And, as a result of this, the power of the move 'Magnitude' has never been demonstrated to go under 'Magnitude 4', {gradualsize=36-20}though it tends toward seven, with an uneven distribution towards 70 BP, which is...{/gradualsize}"

        pause 1.0

        redmind uniform @sadbrow "Well[ellipses] not all of his lectures can hit it out of the park. There's always gotta be a bit of the old Sam in there."

        pause 1.0

        redmind @thonk "Hm. What are Whitney and Flannery doing?"

        show whitney uniform lightblush sad2eyes frownmouth:
            xpos 0.66
        show flannery uniform lightblush sad2eyes frownmouth:
            xpos 0.33
        with Dissolve(1.0)

        flannery "[ellipses]"
        
        whitney "[ellipses]"

        flannery @talking2mouth "{size=30}So[ellipses] last night.{/size}"

        whitney @talking2mouth "{size=30}Yep.{/size}"

        flannery @talking2mouth mediumblush "{size=30}It was, uh, different.{/size}"
        flannery @sadeyebrows talkingmouth "{size=30}Not sure I can really say what's, uh, 'normal', since I'm pretty new to this[ellipses] but that was different.{/size}"

        whitney @scaredbrow sweat sadmouth "{size=30}Different {i}bad?!{/i}{/size}"

        flannery @surprisedbrow talking2mouth sweat "{size=30}Huh? No, no! It was great. It, uh, {i}felt{/i}[ellipses] great.{/size}"

        pause 1.0

        show whitney surprisedbrow frownmouth with dis

        flannery @sadbrow talkingmouth "{size=30}I'm just going to put it out there--were you {i}crying?{/i}{/size}"

        pause 1.0

        whitney @talking2mouth "{size=30}N-no.{/size}"

        flannery @talking2mouth "{size=30}Huh. I just thought I heard you sniffling, and your face was wet--{/size}"

        whitney mediumblush @talking2mouth "{size=30}That was something else.{/size}"

        flannery @closedbrow talking2mouth "{size=30}Huh.{w=0.5} Okay.{/size}"

        $ ValueChange("Whitney", 1, 0.33, False)
        $ ValueChange("Whitney", 1, 0.66)
        
        hide whitney 
        hide flannery 
        with dis

        narrator "Your understanding of Flannery and Whitney--okay, well, actually, you're still pretty baffled, but that definitely told you {i}something{/i}. You're just not sure what."

        redmind @thonk "[ellipses]?"

        oak "{gradualsize=20-36}...which brings us to Earthquake, the superior move in 85%% of cases.{/gradualsize} I hope you in the back are paying attention! You'll likely encounter Earthquake more often than any other move."
        oak "Moving on, then..."

        return

label EthanSleepHabits:
    if (EventAvailable("Ethan", "SleepHabits")):
        scene kitchen 
        show ethan casual:
            xpos 0.33
        show leaf hatless:
            xpos 0.66
        with splitfade

        leaf @talkingmouth "Oh, hey, [first_name]!"
        leaf @happy "Sleep well?"

        red uniform @sadbrow talkingmouth "As well as could be expected. Been better. Been a lot worse, too."

        pause 1.0

        ethan playfuleyes angryeyebrows frownmouth "[ellipses]"
        ethan -playfuleyes -angryeyebrows @confused "Hey, man, you look tired. Are you sneaking out at night?"

        red @closedbrow talking2mouth "A bit, yeah. I try not to make a habit of it, but sometimes stuff comes up."

        ethan @closedbrow talking2mouth "Alright. Just take care of yourself, you know? I've pulled all-nighters before, and I don't think I've {i}ever{/i} not regretted it the next morning."

        leaf @talking2mouth "Don't you pull all-nighters pretty much every night?"

        ethan @closedbrow talking2mouth "And I regret it pretty much every morning."

        red @sadbrow sweat talkingmouth "You need help, man?"

        ethan @happy "Nah, just a gallon of melatonin."

        show yellow uniform with dis
        show ethan casual:
            xpos 0.33
            ease 0.5 xpos 0.25
        show leaf hatless:
            xpos 0.66
            ease 0.5 xpos 0.75

        yellow @talking2mouth "You should try {i}natural{/i} remedies to insomnia before drowning the problem in drugs."
        yellow @talkingmouth "It might be that something you're doing every night is preventing you from getting to sleep." 
        yellow @talking2mouth "How soon before you fall asleep do you put your phone away? It can take up to twenty minutes to get out of that blue-light-seeing information-processing zone."

        pause 1.5

        ethan @sadbrow talkingmouth "You don't really need to ask me that one, do you?"

        yellow @sadbrow talkingmouth "Please tell me that you put your phone away at some point. Don't tell me you fall asleep with it in your hand."

        ethan @closedbrow talking2mouth "I cannot tell a lie."

        yellow @sadbrow talking2mouth "Oh, Ethan..."

        show leaf surprisedbrow frownmouth with dis

        ethan @confused "Hey, weren't we chewing out [first_name] for {i}his{/i} sleep issues? Why am {i}I{/i} suddenly on trial?"

        leaf @happy "You know, that's actually a good question! Who said [first_name] can't deceive? He totally just deflected the topic there."
        leaf angrybrow angrysmilemouth "[ellipses]"
        leaf @talking2mouth "And he got away while we were talking about you."

        narrator "You got away safely!"

        return

"You go to your first homeroom class. Professor Oak's lecture goes on for perhaps a bit long, but it's still a vast improvement over before."

return