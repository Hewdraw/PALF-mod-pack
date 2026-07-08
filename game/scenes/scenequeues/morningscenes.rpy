label morningscenequeue:

label FeebasHatch:
    if (IsAfter(6, 6, 2004) and Item.FeebasEgg in inventory):
        scene bedroom with transeye2
        
        if (not HasEvent("Game", "FirstFeebasHatch")):
            $ AddEvent("Game", "FirstFeebasHatch")

            pause 1.0

            narrator "As you open your eyes in the morning, you suddenly realize you're hearing an odd 'clicking' sound coming from the Feebas egg you had stored in the incubator on your nightstand."

            red casual hatless @confused "Huh[ellipses]? Is it[ellipses]"

            pause 1.0

            red @surprisedbrow talking2mouth "Oh, shit! Champion Wallace's egg's about to hatch!"

            show bedroom with vpunch

            narrator "You throw the covers off of you, unceremoniously launching [pika_name] across the room--"

            $ renpy.music.play("Audio/Pokemon/pikachu_angry3.ogg", channel="altcry", loop=None)
            libpikachu @angryeyes angrymouth "Piii... Pika!"

            narrator "--and rush up to the egg."

            pause 1.0

            narrator "[ellipses]It seems still, again. But, perhaps, you could encourage the egg to hatch?"
        
        else:
            narrator "You awake, again, to the sound of the Feebas egg hatching[ellipses]"

        menu:
            ">Help the Feebas hatch":
                narrator "You place your hands on the egg, and it reacts almost immediately, shaking and jumping--it's tearing itself apart!"

                red casual hatless @wince talkingmouth "Feisty little fish, aren't you? Uh, [pika_name], can you get me a bowl of warm water?"

                $ renpy.music.play("Audio/Pokemon/pikachu_confused2.ogg", channel="altcry", loop=None)
                libpikachu @confusedeyes talkingmouth "Piiika?"

                red @closedbrow talking2mouth "Yeah, I don't know, I just know you're supposed to have a bowl of warm water when delivering babies."
                red @sadbrow talkingmouth "Oh, and it's a fish. So... I guess it probably needs to be {i}in{/i} the bowl?"
                red @surprised "Oh, wait, hold that thought! Here it comes!"

                $ del inventory[Item.FeebasEgg]
                $ sidemonnum = 349
                $ PlaySound("pokemon/cries/349.mp3")

                sidemon "{size=30}Fee...{/size} Feefee!"

                red @happy "Hey, welcome to the party, little lady."

                $ AddMon(Pokemon("Feebas", level=1, moves=["Dragon Breath", "Hypnosis", "Tickle", "Healing Spring"], nature=Natures.Bold, gender=Genders.Female, shinylock=False), True)

                red @happy "Sweet. Everyone in homeroom's going to love to see you."

                pause 1.0

                red @sadbrow talkingmouth "Well, everyone except {i}one{/i} person, I guess."

                return

            ">Leave the egg alone":
                narrator "You decide to leave the egg alone. If you decide to give it to someone else, they'd probably appreciate the chance to see the egg hatch themselves."

                scene blank2 with splitfade

                if (IsDate(13, 6, 2004)):
                    return

label EthanIonoReaction:
    if (EventAvailable(["Ethan", "Iono"], "EthanIonoReaction", [0, 1])):
        scene suite
        show ethan unamusedbrow unamusedmouth uniform 
        with splitfade

        red uniform @talkingmouth "Hey, Ethan. You're up earl[ellipses]"
        red @confused "Hey, uh, why are you squinting at me like that?"

        if (HasEvent("Ethan", "IonoSpoiler")):
            redmind @thonk "Is this about Iono? Ethan {i}did{/i} say we'd be talking about that[ellipses]"

        show ethan:
            ypos 1.0 zoom 1.0
            ease 0.5 ypos 1.2 zoom 1.3

        pause 0.3

        ethan "[ellipses]"

        red @sad2eyes talkingmouth "Hey, did I ever mention how much of a believer in personal space I was?"

        pause 1.0

        ethan @talking2mouth "You've been holding out on me, [first_name] [last_name]."

        red @confused "Uh[ellipses] is this a serious thing?"

        pause 1.0

        show ethan:
            ypos 1.2 zoom 1.3
            ease 0.5 ypos 1.0 zoom 1.0

        ethan -unamusedbrow -unamusedmouth @closedbrow talkingmouth "Nah, it's a bit."

        red @sweat happy "Oh, phew. Was worried I'd actually done something for a moment there."
        red @confused "But, uh, what was this about, then?"

        ethan @talkingmouth "Iono, bro."
        ethan @confused "You were asking me a bunch of questions about her, and then, like, a couple days later, she transfers into Kobukan? Into {i}my{/i} class?"
        ethan @sadbrow talkingmouth "It's a small world, but it ain't {i}that{/i} small."

        red @talkingmouth "Rrrrright. So, uh, are you going to ask me about how that happened?"

        ethan @sad2eyes sadeyebrows talkingmouth "Could you answer?"

        red @wince talking2mouth "Not without being {i}very{/i} vague about some pretty key details."

        ethan @talking2mouth "I figured. Well, I guess if I'm not getting any answers, I'll just say thanks."
        ethan @talkingmouth "I know I don't {i}really{/i} know her, but I've always liked her. As a streamer, I mean."
        ethan @happy "Used to keep her streams on a lot back in High School. When the house was empty, hearing her screaming her catchphrases from out of my crappy laptop speakers made it seem, uh, less empty."
        ethan @confused "And I figured that when I first saw her, she'd be nothing like her streamer persona, but[ellipses] they're basically the exact same person. Which is weird. I was expecting her to be, like, totally fake."

        pause 0.5

        ethan @closedbrow sweat talking2mouth "Weird to think I might've developed a crush on a real person."

        red @confused "Y-yeah. {i}That{/i} sure is the weird part."

        $ ValueChange("Iono", 3, 0.33, False)
        $ ValueChange("Ethan", 3, 0.66)

        narrator "Your understanding of Ethan and Iono increased!"

        ethan @confused "Between Kris, Iono, and I, I think Professor Cherry's class is getting a reputation for becoming a class that you need to have played, like, twenty years of video games to understand."

        red @confused "Uh... {i}you're{/i} not even twenty."

        ethan @closedbrow talking2mouth "Yeah, I was gaming in the womb. Mom swallowed a Tamagotchi."

        red @closedbrow talking2mouth "That can't have been healthy."

        ethan @talking2mouth closedbrow "We were all so busy watching out for microplastics, we didn't notice the macroplastics."

        red @talking2mouth "The surgery to remove it must've been brutal."

        ethan @talkingmouth "Nah, I was a caesarean baby. Came out holding the Tamagotchi. Kept that thing alive 'til the end."

        pause 1.0

        red @closedbrow "Hm."
        red @talkingmouth "You've been talking to Leaf too much."

        ethan @sadbrow talkingmouth "She grows on you. Kinda like[ellipses] moss? A mushroom of some kind?"

        red @upeyes talkingmouth "C'mon, let's get to homeroom. You've got a class of normies to educate."

        ethan @talking2mouth "The work is hard, but by my Tier 3 Sub, I am God's most pathetic soldier."

        red @closedbrow sweat talkingmouth "Amen."

        return

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

        $ ValueChange("Flannery", 1, 0.33, False)
        $ ValueChange("Whitney", 1, 0.66)
        
        hide whitney 
        hide flannery 
        with dis

        narrator "Your understanding of Flannery and Whitney--okay, well, actually, you're still pretty baffled, but that definitely told you {i}something{/i}. You're just not sure what."

        redmind @thonk "[ellipses]?"

        oak "{gradualsize=20-36}...which brings us to Earthquake, the superior move in 85%% of cases.{/gradualsize} I hope you in the back are paying attention! You'll likely encounter Earthquake more often than any other move."
        oak "Moving on, then..."

        return

label EthanYellowCherryUnpopular:
    if (IsAfter(9, 6, 2004) and EventAvailable(["Ethan", "Yellow", "Blue"], "CherryUnpopular")):
        scene suite
        show ethan uniform:
            xpos 0.33
        show yellow uniformhairdown:
            xpos 0.66
        with splitfade

        yellow @talking2mouth "Ethan, do you know where my hair ties went?"

        ethan @talking2mouth "Huh? Why're you asking me?"

        yellow @sadbrow talkingmouth "Well[ellipses] I know you like dressing up in women's clothing sometimes, so[ellipses]"

        ethan @closedbrow talkingmouth "I mean, yeah, but hair ties are basically just rubber bands. That's not women's clothing."
        ethan @talking2mouth "Like, you could put a hair tie around a man-bun, right?"
        ethan @confused "And, actually, you wear the {i}male{/i} uniform, so would your hair ties even {i}be{/i} women's clothing?"
        ethan @unamusedbrow talking2mouth "How femme do you feel when you're tying your hair? I need to know."

        yellow @sadbrow talkingmouth "Does that mean 'no?'"

        $ pidgenick = GetTrainerTeam("Blue", "Pidgeotto").GetNickname()

        ethan @closedbrow talking2mouth "Nah, they're all {i}over{/i} the suite."
        ethan @happy "Couple in the bathroom sink, couple in the kitchen sink, found one in my sock drawer, and Blue's [pidgenick] is making a little nest out of them in the corner of his bedroom."

        yellow @surprised "What?"

        ethan @talkingmouth "Yeah, I was surprised Blue lets his [pidgenick] out of its Poké Ball in the dorm, too. Kinda figured it'd be all work and no play with that guy."

        yellow @closedbrow talking2mouth "Blue trains his Pokémon very well. He's not harsh or cruel toward them. He just pushes them to their limit, then lets them relax."

        ethan @talking2mouth "Yeah? Because Pichu sees how Blue trains his Pokémon and she's terrified."

        if (GetTrainerTeam("Yellow", "Pichu").GetId() == 172):
            yellow @sadbrow talkingmouth "Neither of our Pichu are the {i}bravest{/i} Pokémon out there."

            ethan @talking2mouth sweat closedbrow "Guess they get that from their trainers."

        else:
            yellow @sadbrow talkingmouth "Your Pichu isn't the {i}bravest{/i} Pokémon out there."

            ethan @talking2mouth sweat closedbrow "Guess she gets that from her trainer."

        pause 1.0

        red uniform @talkingmouth "Hey, guys. Mind if I interrupt?"

        ethan @happy "Not at all, mi amigo. 'Sup?"

        yellow @talkingmouth "Good morning."

        red @talkingmouth "You guys are in Professor Cherry's class, right?"

        ethan @talkingmouth "Yeah, Kris'."

        yellow @talking2mouth "{i}Doctor{/i} Cherry, Ethan, but yes."

        ethan @talking2mouth "Dude, she put me in my pajama onesies and blasted {i}Real Housewives of Undella Bay{/i} loud enough that my neighbor could probably hear it, right after she put me down for a nap."
        ethan @unamusedbrow talking2mouth "She did that, like, five times before I finally ripped the wires out of the TV's speakers." 
        ethan @happy "I've {i}earned{/i} the right to call my babysitter 'Kris.' Besides, it'd be weird if I suddenly started calling her Doctor Cherry, at least when we're not around other people."

        yellow @closedbrow talking2mouth "Okay."
        yellow @happy "Sorry, [first_name], what was your question?"

        red @talkingmouth "It's something Sam mentioned--he said something about his reputation at this school being a bit overinflated."

        ethan @sad2brow talkingmouth "I know he's your friend, but based on that one week he taught us... yeah. Yeah, it {i}really{/i} is."

        red @sadbrow talkingmouth "He's gotten better."
        red @talking2mouth "Anyway, I was wondering, what do Professor Cherry's students think of her? I mean, she's barely older than some of them."

        ethan @sadbrow talking2mouth "Dude, she's {i}younger{/i} than some of them."

        yellow @talking2mouth "I think a lot of her students treated her very unfairly when they first joined her class."
        yellow @talkingmouth "I can understand why they might feel disappointed, though. She's the newest Professor, and she has one of the smallest classrooms--nothing like the grand marble arches of Professor Oak's classroom."
        yellow @closedbrow talking2mouth "If students happened to walk by one of the other classrooms, and peeked in those, before they walked into hers[ellipses]"

        pause 1.0

        ethan surprisedbrow frownmouth @neutraleyes neutraleyebrows talking2mouth "I'm sure the school just gives the biggest classrooms to professors with the most seniority."

        yellow @sadbrow talking2mouth "Professor Oak and Professor Cherry both just joined the school this year, though."

        ethan -surprisedbrow -frownmouth @closedbrow talking2mouth sweat "Oh, yeah. Right. Uh[ellipses] I guess they probably just gave her the smaller classroom because no-one knew who she was until, like, a year ago, then."

        yellow @talking2mouth "Most likely."
        yellow @happybrow talkingmouth "Well, regardless of how her students thought of her at the beginning of the year, I think everyone's starting to appreciate her more, now. Her energy is really infectious."
        yellow @talkingmouth "She also teaches us a lot of practical skills--potion-blending, Poké Ball-making... that sort of thing. She often reminds us that being a strong battler isn't the only thing Kobukan can help us do."
        yellow @happy "She has her quirks, too, of course. She'll often get so excited in the middle of a lesson she'll jump on someone's desk, but you get used to it."

        red @happy "Guess she was scared of damaging our furniture--she never did that in our classroom."

        pause 1.0

        red @talking2mouth "Although, come to think of it, she {i}did{/i} break into Sam's grading cabinet."

        ethan @talkingmouth "Sounds like her. When she wants to do something, physical obstacles are never more than a momentary consideration for her."
        ethan @happy "Guess you don't get a PhD at twenty-one by letting things slow you down, though."

        red @happy "Must've been fun to be baby-sat by her."

        ethan @talkingmouth "If {i}someone{/i} was baby-sitting me[ellipses] yeah. Can't think of anyone that could've done it better."
        ethan upeyes frownmouth "[ellipses]"

        pause 0.5

        red @talking2mouth "What are you thinking about?"

        ethan -upeyes -frownmouth @talking2mouth "I dunno, really. Her, I guess. We used to be pretty similar. I also used to jump on tables and stuff. I used to skateboard with her, and I was mad skilled at it."
        ethan @talkingmouth "Maybe I still am. Kinda scared to try it out, now."

        red @happy "You got a board with you?"

        ethan @talking2mouth "Nah, left it back at home. Maybe I'll ask it to be sent over--could be fun. There's this one guy I follow on RotoPhotos who {i}battles{/i} while skating. Pretty insane stuff."

        red @talkingmouth "Seriously? That sounds pretty cool. Send me a link."

        ethan @happy "Will do, man."

        $ ValueChange("Ethan", 3, 0.4, False)
        $ ValueChange("Professor Cherry", 3, 0.6)

        narrator "Your understanding of Ethan and Professor Cherry increased!"

        pause 1.0

        show ethan surprisedbrow frownmouth:
            xpos 0.33
            ease 0.5 xpos 0.5

        show yellow surprisedbrow frownmouth:
            xpos 0.66
            ease 0.5 xpos 0.75

        show blue uniform surprisedbrow surprisedmouth:
            xpos -0.2
            ease 0.5 xpos 0.25

        blue @angry "Hey! Are you guys just going to stand here blabbing about {i}whatever{/i} all morning? You're going to be late to class!"

        red @surprised "Shit, you're right! We've only got, like, three minutes!"

        yellow @talkingmouth "Oh, but, my hairtie--"

        blue @angry "Save it! You look better with your hair down, anyway!"

        show ethan:
            xpos 0.5
            pause 0.3
            ease 0.7 xpos 0.4
            ease 0.2 xpos 1.5

        show blue:
            xpos 0.25
            ease 0.7 xpos 0.15
            ease 0.2 xpos 1.5

        show yellow:
            xpos 0.75 xzoom 1
            pause 0.3
            ease 0.2 xzoom -1

        pause 1.5

        yellow @talking2mouth "I[ellipses] what?"

        pause 0.5

        show yellow:
            xpos 0.75 xzoom -1
            ease 0.5 xzoom 1
            pause 0.3
            ease 0.5 xpos 0.5

        pause 1.5

        yellow @talkingmouth "{size=30}Oh, here's one.{/size}"

        pause 1.0

        yellow smirkmouth sad2eyes "[ellipses]"

        show yellow:
            xpos 0.5 xzoom 1
            ease 0.5 xzoom -1
            pause 0.3
            ease 0.7 xpos 0.4
            ease 0.2 xpos 1.5

        pause 2.0

        return

label EthanSleepHabits:
    if (EventAvailable(["Ethan", "Leaf", "Yellow"], "SleepHabits")):
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

        narrator "Got away safely!"

        return

"You go to your first homeroom class. Professor Oak's lecture goes on for perhaps a bit long, but it's still a vast improvement over before."

label genericmorningbunnyrecruit:

if (IsAfter(6, 6, 2004) and IsBefore(12, 6, 2004)):
    scene homeroom with splitfade

    show hilbert uniform:
        xpos 1/6
    show whitney uniform:
        xpos 2/6
    show flannery uniform:
        xpos 3/6
    show dawn uniform:
        xpos 4/6
    show may uniform:
        xpos 5/6
    with dis

    python:
        bunnyrecruits = []
        for char in ["Hilbert", "Whitney", "Flannery", "Dawn", "May"]:
            if (CanBunnyRecruit(char)):
                bunnyrecruits.append((char, char))

    if (len(bunnyrecruits) > 0):
        narrator "Now seems like it might be a good time to mention the party on Saturday[ellipses] whom should you approach?"
        python:
            classchar = renpy.display_menu(bunnyrecruits)
            renpy.transition(dis)
            renpy.show(GetCharacterSprite(classchar, None, True))

        "You want to talk to [classchar]?"

        menu:
            "Yes.":
                call BunnyRecruit(classchar, True) from _call_BunnyRecruit_16

            "No.":
                $ renpy.hide(classchar.lower())

                jump genericmorningbunnyrecruit

return