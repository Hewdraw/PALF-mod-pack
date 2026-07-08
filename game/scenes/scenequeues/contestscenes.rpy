label contestscenequeue:

label Contest1:
    if (HasEvent("Klara", "AcceptCoordinatorClub")):
        $ AddEvent("Game", "Contest1")
    if (not HasEvent("Game", "Contest1")):
        if (IsDate(7, 6, 2004)):
            narrator "Brendan goes back into the dorm, promising he'll change quickly, and get back out. The minutes pass slowly[ellipses]"

            scene relichall_A with splitfade

            redmind @confusedeyebrows frownmouth "Hm... Where are they?"

            $ showredonly = True

            may @talkingmouth "Hey! Sorry we were late--we couldn't find my scrunchie."

            pause 0.2

            $ showredonly = False

            red @talkingmouth "Completely fine! I wasn't here long. I just--"

        else:
            scene relichall_A with splitfade

            narrator "As you leave Relic Hall for the Contest Coliseum, you see a familiar couple walking past the gates[ellipses]"

            redmind @confusedeyebrows frownmouth "Wait, is that Brendan and May?"

            $ showredonly = True

            may @talkingmouth "Oh! [first_name], hi! We didn't see you there."

            pause 0.2

            $ showredonly = False

            red @talkingmouth "Hey, May! Brendan, too? Are you guys heading to--"

        show brendan contest:
            xpos 1.2
            ease 0.5 xpos 0.75

        show may contest:
            xpos -0.2
            ease 0.5 xpos 0.25

        red @surprisedbrow frownmouth lightblush "{w=0.5}.{w=0.5}.{w=0.5}."

        brendan @happy "Hey, you ready to go, bro?"

        may @surprised "[first_name]? Are you alright? Your face is all flushed...?"

        menu:
            "You guys look amazing!":
                $ AddEvent("Brendan", "ComplimentContestOutfit")
                $ AddEvent("May", "ComplimentContestOutfit")
                $ ValueChange("May", 1, 0.25, False)
                $ ValueChange("Brendan", 1, 0.75)
                
                brendan @happy "Hey! Thanks, bro! You too. From one brother who puts in the work to look good to another; respect."

                may @happy "Thanks, [first_name]. Do you like my contest outfit? Brendan sewed it for me himself!"

                brendan @happy sweat "I mean, I just used a pattern. I didn't create the design. May's dress is based on something Lisia wore earlier in her career. But I guess it's pretty good."
                brendan @talkingmouth "Don't require repairs all the time. Most contest outfits are built to be light, so they fall apart pretty often."
                brendan @closedbrow talking2mouth "I try to make outfits that bring out the best in the wearer, {i}and{/i} don't require bucketloads of cash to keep runnin'."

                may @sadbrow talkingmouth "You're so practical, sweetheart."

            "Brendan, you're seriously hot.":
                $ AddEvent("Brendan", "ComplimentContestOutfit")
                $ ValueChange("Brendan", 1, 0.75)

                brendan @happy "Hey! Thanks, bro! You too. From one brother who puts in the work to look good to another; respect."

                may @talkingmouth "Do you like our outfits? Brendan sewed them himself!"

                brendan @happy sweat "I mean, I just used a pattern. I didn't create the designs--this one's based on the outfit of a Kanto Rock Star called Ryuki. But I guess they're pretty good."
                brendan @talkingmouth "Don't require repairs all the time. Most contest outfits are built to be light, so they fall apart pretty often."
                brendan @closedbrow talking2mouth "I try to make outfits that bring out the best in the wearer, {i}and{/i} don't require bucketloads of cash to keep runnin'."

                may @sadbrow talkingmouth "You're so practical, sweetheart."

            "May, you're absolutely adorable.":
                $ AddEvent("May", "ComplimentContestOutfit")
                $ ValueChange("May", 1, 0.25)

                may @happy "Awww! Thanks, [first_name]. Do you like my contest outfit? Brendan sewed it for me himself!"

                brendan @happy sweat "I mean, I just used a pattern. I didn't create the design. May's dress is based on something Lisia wore earlier in her career. But I guess it's pretty good."
                brendan @talkingmouth "Don't require repairs all the time. Most contest outfits are built to be light, so they fall apart pretty often."
                brendan @closedbrow talking2mouth "I try to make outfits that bring out the best in the wearer, {i}and{/i} don't require bucketloads of cash to keep runnin'."

                may @sadbrow talkingmouth "You're so practical, sweetheart."

            ">Just continue sweating in silence":
                brendan @closedbrow talkingmouth "I think I've got a fresh water somewhere here... hold up."

                show brendan contest:
                    xpos 0.75 ypos 1.0 zoom 1.0
                    ease 0.5 xpos 0.66 ypos 1.2 zoom 1.3

                show may contest:
                    xpos 0.25 ypos 1.0 zoom 1.0
                    ease 0.5 xpos 0.33 ypos 1.2 zoom 1.3

                brendan @sadbrow talking2mouth "Don't go passin' out on us, bro. You got to stay hydrated when you're running in [calendar.month_name[calDate.month]]. It's seriously hot out here."

                redmind @mediumblush frownmouth surprisedbrow "You're telling me."

                narrator "The two extremely attractive coordinators look at you with earnest concern. You attempt to hitch an unflustered grin onto your face. May and Brendan exchange a curious look."

                show brendan contest:
                    xpos 0.66 ypos 1.2 zoom 1.3
                    ease 0.5 xpos 0.75 ypos 1.0 zoom 1.0

                show may contest:
                    xpos 0.33 ypos 1.2 zoom 1.3
                    ease 0.5 xpos 0.25 ypos 1.0 zoom 1.0

        brendan @talking2mouth "We're running a bit late, though, and Liz'll tear our heads off if we're not there and in-position in time..."

        may @closedbrow talking2mouth "I swear, the only one who can keep up with her is Dawn."

        brendan @talking2mouth "Well, Liz did specially recruit her. Dawn's the entire reason we've even got Liz."
        brendan @talkingmouth "Well, Dawn and Calem, anyway."

        may @closedbrow talking2mouth "And we're... {i}so{/i} grateful."

        brendan @talking2mouth "I get that, but what Liz said about needing to try harder to be taken seriously than battlers is real true. I see where she's coming from, honestly."

        may @talking2mouth "Yeah. She's not {i}wrong.{/i} Just... intense."

        brendan @talking2mouth "Anyway, that's why we gotta hurry to the Contest Coliseum! C'mon!"

        if (not HasEvent("Professor Oak", "LearnedAboutContestColiseum")):
            red @sad2eyes lightblush talkingmouth "Y-yeah. Sure thing. Just one question."

            show brendan surprisedbrow frownmouth
            show may surprisedbrow frownmouth
            with dis

            red @confused "Where is it?"

            pause 1.0

            brendan @talking2mouth "What?"

            may @talking2mouth "[first_name], it's right behind the Battle Hall."

            red @talking2mouth "That's not on my map."

            may @closedbrow talking2mouth "[first_name], can I see that map?"

            red @talking2mouth "Sure."

            show mapdemo with dis

            pause 0.5

            show may -surprisedbrow -frownmouth:
                rotate 0 xpos 0.25
                ease 1.0 rotate -50

            show brendan -surprisedbrow -frownmouth:
                rotate 0 xpos 0.75
                ease 1.0 rotate 50

            pause 2.0

            may @talkingmouth "Okay... you're right. It's {i}not{/i} on there. But, um..."

            narrator "Brendan points at a big silver building that is, as the Hoennians said, behind the Battle Hall."

            brendan @talking2mouth "It's there, bro."

            pause 0.5

            red @closedbrow sweat talking2mouth "I thought... that was part of the city."

            may @talkingmouth "A little bit! But the campus extends into the city for a few blocks. That map you have is pretty zoomed-in."

            red @unamusedbrow talking2mouth "...I've been here two months, and I'm just now learning this?"
            red @closedbrow talking2mouth "Jeez. {i}Please{/i} don't tell Leaf. I'd never hear the end of it."

            stop music fadeout 1.5

            $ PlaySound("idea.ogg")

            brendan @talking2mouth "Hm?"

            show may surprisedbrow frownmouth with dis

            brendan surprisedbrow frownmouth @surprised "Oh, crap, we gotta go! Like, triple-time!"
            brendan surprisedbrow frownmouth @surprised "Run, babe! Run, bro!"

        queue music "Audio/Music/Show Me Around.ogg"

        scene blank2 with splitfadefaster

        pause 0.5

        scene colosseum with splitfadefaster

        show brendan contest surprised: 
            xpos 1.3
            ease 0.6 xpos -0.2

        show may contest surprised: 
            xpos 1.2
            ease 0.6 xpos -0.2

        if (not HasEvent("Professor Oak", "LearnedAboutContestColiseum")):
            narrator "Brendan and May lead you to a familiar location, first... the outside of the Battle Hall..."

        else:
            narrator "Brendan and May lead you to the outside of the Battle Hall..."

        scene concerthall with splitfadefaster

        show brendan contest surprised: 
            xpos 1.3
            ease 0.6 xpos -0.2

        show may contest sadbrow frownmouth: 
            xpos 1.2
            ease 0.8 xpos -0.2 

        if (not HasEvent("Professor Oak", "LearnedAboutContestColiseum")):
            narrator "Then to a new location, the outside of a shining silver building that you must assume is the Contest Coliseum..."

        else:
            narrator "Then you take a hard turn left to the shining silver walls of the Contest Coliseum, as statuesque and imposing as ever."

        scene concerthallback with splitfadefaster

        show brendan contest surprised: 
            xpos 1.3
            ease 0.4 xpos -0.2

        show may contest sad: 
            xpos 1.2
            ease 1.0 xpos -0.2 

        narrator "Before pulling a sharp turn around the back of the building."

        brendan @talkingmouth "Through the back! It leads directly to the practice room, and Liz might not see us come in this way!"

        scene concerthallhallway with splitfadefaster

        red @surprised "Directly? You didn't mention the hallway!"

        brendan contest @surprised "It's just at the end of this! We're almost there! We're--"

        stop music fadeout 3.0

        scene blank with transeye2

        pause 2.0

        show concerthallpracticeroom
        show serena contest surprisedbrow frownmouth:
            xpos 1.0/8.0
        show misty contest surprised:
            xpos 2.0/8.0 xzoom -1
        show klara neutralcoat surprisedbrow frownmouth behind misty:
            xpos 3.0/8.0 xzoom -1
        show lisia incognito angrybrow frownmouth:
            xpos 4.0/8.0
        show dawn contest surprisedbrow frownmouth behind dawn:
            xpos 5.0/8.0
        show tia contest surprisedbrow frownmouth:
            xpos 6.0/8.0
        show jasmine contest surprisedbrow frownmouth behind tia:
            xpos 7.0/8.0
            
        pause 3.0

        brendan contest @sadbrow talkingmouth "We're... too late."

        queue music "audio/music/littleroot_start.ogg" fadein 1.5 noloop
        queue music "audio/music/littleroot_loop.ogg"

        show screen currentdate with dis

        if (GetRelationshipRank("Tia") > 0):
            $ ValueChange("Tia", 1, 6.0/8.0)
            tia -surprisedbrow -frownmouth @happy "Hi, [first_name]!"

        else:
            tia -surprisedbrow -frownmouth @happy "Hi, [tiafont][first_name]{/font}!"

        if (GetRelationshipRank("Jasmine") > 0):
            jasmine @talking2mouth "You're here...? I didn't know you were going to watch one of our practices, [first_name]!"
            
            $ ValueChange("Jasmine", 1, 7.0/8.0)

            jasmine -surprisedbrow -frownmouth @happy "How lovely."

        if (GetRelationshipRank("Misty") > 0):
            misty @talkingmouth "[first_name]? What are you doing here? This is the Contest Club. Did you get lost on the way to the Battle Hall?"

            $ ValueChange("Misty", 1, 2.0/8.0)

            misty -surprisedbrow -frownmouth -surprised @sadbrow talking2mouth "Uh... I mean, I don't {i}hate{/i} that you're here..."

        if (GetRelationshipRank("Dawn") > 0):
            dawn @happy "Oh, I'm so glad you're here, [first_name]! I thought about inviting you for a while, now, but..."

            $ ValueChange("Dawn", 1, 5.0/8.0)

            dawn -surprisedbrow -frownmouth @sadbrow talkingmouth "Well, I was worried you'd find it boring, I guess..."

        if (GetRelationshipRank("Serena") > 0):
            $ ValueChange("Serena", 1, 1.0/8.0)

            serena -surprisedbrow -frownmouth @happy "So it seems you have an interest in contests, too? Aren't {i}you{/i} the renaissance man. A versatile mind is an attractive quality on its own merits."

        if (HasEvent("Klara", "BrokeBond")):
            klara @angrybrow "[ellipses]"

            narrator "Klara smirks at you, before her face adopts its standard mask of innocent cuteness. It saddens you somewhat that you can see through it, now..."

        else:
            klara sadbrow poutmouth "[ellipses]"

            narrator "Klara seems to be avoiding your gaze[ellipses]"

        lisia @talking2mouth "...[first_name], right?"

        red @talking2mouth "That's me."

        lisia @closedbrow talking2mouth "Why do I know you...?"

        if (IsCoordinator()):
            red @happy "I, uh, participated in the Millennium Drop Tryouts."#FIX THIS: Add more reasons Lisia could know you for future contests

        else:
            red @happy sweat "Uh, I beat Dawn in the Quarter Qlashes..."

        lisia @surprised "Oh, that's right!"
        lisia -angrybrow frownmouth @happy "Right, and there's that Pikachu. I remember now."

        pause 1.0

        lisia @talking2mouth "Well, thank you for bringing my clubmembers here. I'm afraid I'm going to have to ask you to step out of the practice room for now, though."
        lisia @talkingmouth "We're just about to discuss strategies for the upcoming contest, and we don't want to let any secrets spill out."

        red @talking2mouth "Totally fine."

        serena -surprisedbrow -frownmouth @talkingmouth "If you would like to watch our practice performance, you can head out to the open-air stage. It's directly down the hallway."
        serena @talkingmouth "Grusha and Calem are there, I believe. To cheer on Jasmine and I."

        red @sadbrow talkingmouth "Sounds like a plan. Sorry for interrupting, everyone."

        brendan @sadbrow talkingmouth "Totally fine, bro. Thanks for running with us."

        may contest @happy "We'll see you in a bit! And remember, it's a straight line down the hallway!"

        red @happy "I don't think I'm going to get lost just going down the--{nw}"

        scene concerthallmakeuproom2

        red @unamusedbrow unamusedmouth "I don't think I'm going to get lost just going down the--{fast}and I'm lost." 
        red @closedbrow talking2mouth "I swear, the {i}exact{/i} moment I step off the map Leaf gave me..."

        $ PlaySound("Pokemon/pikachu_sad.ogg")
        libpikachu sad "Piiiika."

        red @talking2mouth "Okay. I just need to retrace my steps, right? Let's just..."

        stop music fadeout 1.5

        queue music "audio/music/potown_start.ogg" noloop
        queue music "audio/music/potown_loop.ogg"

        narrator "You turn around to grab the door handle, and leave this 'ready room' you found yourself in, when, strangely..."

        show concerthallmakeuproom2midnight

        pause 0.1

        hide concerthallmakeuproom2midnight

        pause 0.5

        red @closedbrow talking2mouth "Huh? Did... did the lights just flicker?"

        $ PlaySound("Pokemon/pikachu_scared.ogg")
        libpikachu surprisedbrow frownmouth @surprised "Pika?!"

        red @confused "Yeah, let's... get out of here, bud."

        pause 1.0

        TempCharacter("Doorknob", False) "*{i}Clunk.{/i}*"

        red @surprised "Wait, what? Why isn't the door opening?! What's happening? Is it--!"

        narrator "Before you have the time to panic {i}too{/i} much, you twist the doorknob the other direction, and the door easily opens."

        red @sad2eyes lightblush talking2mouth "...No-one saw that. You're cool. You're still cool."

        narrator "You leave the room."

        show concerthallmakeuproom2:
            matrixcolor SaturationMatrix(1.0)
            linear 6.0 matrixcolor SaturationMatrix(0.2)

        show flashback 
        hide screen currentdate
        with Dissolve(6.0)

        Character("???") "\"{glitch=40.00}Zzt?{/glitch}{w=0.5} {glitch=30.00}Zzzt?{/glitch}{w=0.5} {glitch=20.00}is there anyoneanyoneanyoneanyone{/glitch}{w=0.5} {glitch=10.00}there-here-ere-re-e---?{w=0.5}{/glitch}\""
        Character("???") "\"{glitch=5.00}Is there anyone there...?{/glitch}\""

        pause 1.0

        Character("???") "\"{glitch=60.00}WHY NOT?{/glitch}\""

        scene blank2 with splitfade

        pause 1.0

        scene concerthallhallway with splitfade

        stop music fadeout 1.5
        queue music "audio/music/littleroot_start.ogg" fadein 1.5 noloop
        queue music "audio/music/littleroot_loop.ogg"

        red @talkingmouth "Oh, phew! Here we are. Found our way back to the hallway. Should just be at the end of this, May said, right? Let's go."

        scene concerthallstage with splitfade 

        red @confusedeyebrows talking2mouth "...Hm?"

        show may contest happy:
            xpos 1.0/10.0
        show brendan contest angrybrow happymouth behind may:#god i wish that was me
            xpos 2.0/10.0 xzoom -1
        show serena contest:
            xpos 3.0/10.0
        show misty contest closedbrow behind serena:
            xpos 4.0/10.0 xzoom -1
        show lisia:
            xpos 5.0/10.0
        show dawn contest happy behind lisia:
            xpos 6.0/10.0
        show tia contest frownmouth angrybrow:
            xpos 7.0/10.0
        show klara neutralcoat hairpin makeup behind tia:
            xpos 8.0/10.0
        show jasmine contest winkbrow talkingmouth:
            xpos 9.0/10.0
        with dis

        red @talkingmouth "It looks like the coordinators are here already...?"

        if (IsDate(7, 6, 2004)):
            red @closedbrow frownmouth "No sight of Phobos, though. Guess he thought he'd annoyed Lisia enough...?"

        hide may
        hide brendan
        hide serena
        hide misty
        hide lisia
        hide dawn
        hide tia
        hide klara
        hide jasmine
        with dis

        pause 0.5

        show calem with dis:
            xpos 0.5

        calem surprisedbrow @neutralbrow talkingmouth "Yes, they arrived onstage about half an hour ago."

        red @surprised "What! No way! I left the practice room before them, like... five minutes ago!"

        calem @talkingmouth "Oh? Well, I'm not sure what laws of logic would allow that to be a possibility."

        red @sad2eyes sadeyebrows talking2mouth "I mean... yeah, obviously, it's impossible, but..."

        calem -surprisedbrow @talking2mouth "In any case, Serena informed me that you were coming here when the coordinators arrived. We supposed that you had some urgent business that dragged you away."

        red @sadbrow talkingmouth "No. I just... got turned around, and ended up in a ready room, but... I swear it wasn't for more than a couple minutes."

        calem @closedbrow talkingmouth "I fully believe you. Perhaps it's just my own perception of time that's flawed."

        narrator "Calem quickly checks his phone's clock. Whatever he saw did not seem to impress him, and he puts his phone back in his pocket."

        calem @talking2mouth "Well, whatever the case, it's not worth thinking of. Look, Grusha's coming back."

        show grusha:
            xpos 1.2
            ease 0.5 xpos 0.66

        show calem:
            xpos 0.5
            ease 0.5 xpos 0.33

        grusha @talkingmouth "Oh. You showed up."
        grusha @closedbrow talkingmouth "Thought you'd skipped out."

        narrator "In Grusha's hands, he holds a couple of slushies."

        grusha @talkingmouth "Sorry, [first_name]. Only got two. Didn't know you'd be here."

        red @sadbrow talkingmouth "Nah, it's fine. My stomach feels weird, anyway. Not sure I {i}could{/i} drink right now."

        calem @talking2mouth "...Hm? Grusha, where did you get those? Is someone running a store here?"

        grusha @talkingmouth "Only who you'd expect."

        calem @surprisedbrow talking2mouth "Er... I'm not sure..."

        grusha @closedbrow talking2mouth "'Business'."

        show grusha playfulbrow:
            xpos 0.66
            ease 0.3 xpos 0.75
        show calem surprisedbrow:
            xpos 0.33 xzoom 1
            ease 0.3 xpos 0.5 xzoom -1
        show gardenia behind calem:
            xpos 1.2 ypos 1.0
            parallel:
                easein 0.3 ypos 0.7
                easeout 0.3 ypos 1.0
            parallel:
                ease 0.3 xpos 0.25
            parallel:
                pause 0.3
                ease 0.5 xzoom -1
        with dis

        gardenia @angrybrow talkingmouth "Did someone say 'business'?!"

        calem -surprisedbrow -frownmouth @surprised "That's uncanny."

        grusha -playfulbrow @playfulbrow talking2mouth "I've tried that four times ever since the election. Works every time."

        gardenia surprised @surprisedbrow talking2mouth "Uh... I guess no-one did?"

        if (GetRelationshipRank("Gardenia") < 1):
            red @talkingmouth "Seriously, how do you do that? You're like a ghost. You just phase into reality when there's a chance to make a buck."

            gardenia @happy "Hah! No! No, definitely not a ghost. But I appreciate the compliment."
            gardenia -surprisedbrow -frownmouth -surprised @angrybrow happymouth "The only invisible hand {i}I'm{/i} about is the free market's."

            pause 0.5

            show grusha confusedeyebrows
            show calem surprisedbrow 
            show gardenia surprisedbrow frownmouth
            with dis
            
            red @closedbrow talking2mouth "Well, I'm glad {i}you're{/i} mortal. Pretty sure I just ran into a ghost. Or I'm going crazy."

        else:
            red @talkingmouth "Seriously, how do you do that? You're like an Abra. You just teleport into anywhere you hear there's a chance to profit."

            gardenia @flirtbrow talkingmouth "A merchant never reveals her secrets, Partner."

            pause 0.5

            show grusha confusedeyebrows
            show calem surprisedbrow 
            show gardenia surprisedbrow frownmouth
            with dis
            
            red @closedbrow talking2mouth "Well, I'm going to reveal mine. Seems relevant to your interests, anyway. I'm pretty sure I just ran into a ghost--or I'm going crazy."

        pause 0.5

        grusha -confusedeyebrows @closedbrow talking2mouth "Got a family history of psychosis?"

        red @talkingmouth "My grandpa thought Salazzle ran the government."

        grusha @sad2eyes talking2mouth "Not a good sign."

        show calem -surprisedbrow with dis

        gardenia -surprisedbrow @talking2mouth "Wait. What do you mean you're pretty sure you ran into a ghost?"

        red @sadbrow talkingmouth "Oh, nothing, really. I'm just joking. I got lost, and found this empty ready room." 
        red @sadbrow talking2mouth "The lights flickered, and I couldn't figure out how the doorknob worked. It only took a couple minutes, but somehow I ended up staying there for, like, half an hour."

        gardenia angrybrow frownmouth @talking2mouth "...In {i}this{/i} building?"

        red @talkingmouth "Y-yeah...? Just in the hallway out that door."

        if (GetRelationshipRank("Gardenia") < 1):
            redmind @thinking "She seems {i}really{/i} serious about this..."

        else:
            red @talkingmouth "Guess you've got a plan, then. You're going to get the Disciplinary Committee on it?"

            gardenia @talking2mouth "I might[ellipses] I'll need to think."

        gardenia @talking2mouth "Alright. Well, if no-one's in the mood to buy the lint in my pockets right now, I've got another business engagement to handle."
        gardenia @happy "Seeya! Stay thrifty!"

        hide gardenia with dis

        narrator "As Gardenia walks away, she pulls out her phone. You don't hear what she says into it, but you can make out one word..."
        narrator "'Commission.'"

        redmind @confusedeyebrows frownmouth "Hm...? Is she making something for someone?"

        calem @talkingmouth "...How bizarre."

        grusha @talkingmouth "Sinnohans. Think they see spirits, gods, fairies, whatever, around every corner."

        calem @talking2mouth "That's just a stereotype. Instructor Winona's a devout Arceist, and she's not Sinnohan."

        grusha @talkingmouth "Eh. Instructor Winona {i}needs{/i} to believe the universe has some sort of plan to not have a nervous breakdown every ten minutes."

        pause 1.0

        narrator "The conversation trails off as Grusha, Calem, and you all turn your attention to the stage, where the coordinators are performing rigorous drills of segments of their performances."

        pause 2.0

        show yellow neutrallowponytail with dis:
            xpos 0.25 xzoom -1

        yellow @talking2mouth "...Hi, [first_name]."

        red @happy "Oh, hey, Yell'! Shouldn't you be down there on the stage, with all the others?"

        if (IsBefore(13, 7, 2004)):
            yellow @talking2mouth "N-no... I, um, I'm participating in the Millennium Drop, but I'm not a Coordinator Club member. I could never!"
        else:
            yellow @talking2mouth "N-no... I, um, I participated in the Millennium Drop, but I'm not a Coordinator Club member. I could never[ellipses]"

        calem @talkingmouth sadbrow "One rarely gains experience in a field if they dismiss themselves as too inexperienced to learn."
        calem @talkingmouth "Regardless, please, take a seat with us."

        yellow @happy "Thanks."

        pause 1.0

        calem @talkingmouth "I must confess... I said I'd come out here to support Serena, but I'm not quite certain what we're watching."

        grusha @talkingmouth "Same. I don't think Paldea even has a contest league. I've seen Johtonian contests before--Jasmine's done those, and I came to watch them, then..."
        grusha @confusedeyebrows talking2mouth "But Kobukanian contests are different, aren't they?"

        yellow @talkingmouth "Yes. In Kobukan, instead of having five different contest tracks, there's only one kind of contest. Whether you try to appeal through showing off the toughness of your Pokémon, or their beauty, or their coolness..."
        yellow @talking2mouth "That's up to you. You don't even need to stick to doing a specific kind of appeal throughout the entire contest."

        calem @talking2mouth "Interesting... that's not how it works in other regions, is it?"

        grusha @closedbrow talking2mouth "Nope. Kobukan likes to be contrarian like that."

        hide grusha
        hide calem
        hide yellow
        with dis

        pause 1.0

        show may contest happy: 
            xpos 1.2 xzoom 1
            pause 2.0
            parallel:
                linear 3.0 xpos -0.2
            parallel:
                ease 0.5 xzoom -1
                ease 0.5 xzoom 1
                repeat

        show brendan contest closedbrow talkingmouth with dis:
            xpos 0.33 xzoom -1

        show misty contest happy with dis:
            xpos 0.66

        narrator "You gaze at the stage, trying to make out the performers. You can't hear anything that's being said, though it looks like a few of them are singing."

        redmind @thinking "Guess they didn't hook their mics up...?"

        calem @talkingmouth "...Pardon my ignorance, but they all seem to be performing simultaneously. Are these team-based contests, then?"

        yellow neutrallowponytail @closedbrow talking2mouth "Um... no."

        show jasmine contest angrybrow talkingmouth:
            xpos 1.2
            ease 0.5 xpos 0.85

        show klara neutralcoat hairpin makeup ojoubrow talkingmouth:
            xpos -0.2 xzoom -1
            ease 0.5 xpos 0.15 

        hide may
        show may contest happy: 
            xpos -0.2 xzoom 1
            pause 2.0
            parallel:
                linear 3.0 xpos 1.2
            parallel:
                ease 0.5 xzoom -1
                ease 0.5 xzoom 1
                repeat
                
        yellow @talking2mouth "Five performers all perform simultaneously in Kobukanian contests. They all fight for the judges' attention."

        show tia contest happy with gaussdis:
            zoom 0.0
            parallel:
                linear 0.2 xzoom -1
                linear 0.2 xzoom 1
                repeat 10
            parallel:
                ease 1.0 zoom 1.0

        yellow @happy "But... it's not really fighting. Because you can get points for making your rivals' appeals look better."

        calem @talking2mouth "Fascinating. What a wonderful spirit of cooperation."

        grusha @shadow sweat surprised "Are we not going to acknowledge that Venetia just appeared out of thin air?!"

        calem @talkingmouth "It's amazing what they can do with special effects nowadays, isn't it?"

        narrator "You and Yellow share a look."

        redmind @thinking "There really is such a thing as being {i}too{/i} unflappable..."

        show brendan happy with dis:
            xpos 0.33
            ease 0.5 xpos 1.2

        show misty angrybrow happymouth with dis:
            xpos 0.66
            pause 0.5
            ease 0.5 xpos -0.2

        show klara happy with dis:
            xpos 0.15
            pause 1.0
            ease 0.5 xpos 1.2

        show jasmine happy with dis:
            xpos 0.85
            pause 1.5
            ease 0.5 xpos -0.2

        show tia:
            pause 2.0
            ease 1.0 ypos -0.7

        yellow @surprised blush "U-u-um, anyway, I... yes, so, they all perform at the same time."
        yellow @closedbrow talking2mouth "In this region, the performances of the trainers are considered just as important as those of the Pokémon."
        yellow @talking2mouth "So every appeal has two parts to it. The performer's performance, and the Pokémon's move."

        calem @talkingmouth "Curious. Seems there's a sort of science to this. It appears the human performers' appeals fall into three different categories..."

        grusha @talkingmouth "Hm. Audio's one of them. Singing and playing instruments."

        calem @talkingmouth "Physical appeals are important, too. Dancing and acrobatics. Perhaps even feats of strength could be considered."

        yellow @talking2mouth "The third kind of appeals are 'prop-based appeals'. Or just 'Props'. These appeals use external factors, like... um, juggling, pyrotechnics, or magic tricks."

        calem @talkingmouth "Ah. Like those hidden wires that just allowed Tia to fly."

        yellow @scaredeyes "{w=0.5}.{w=0.5}.{w=0.5}."
        yellow @talking2mouth scaredeyes "Yes.{w=0.5} That is correct."

        hide may
        hide serena
        hide jasmine

        show may contest happy: 
            xpos -0.2 xzoom 1
            pause 2.0
            parallel:
                linear 3.0 xpos 1.2
            parallel:
                ease 0.5 xzoom -1
                ease 0.5 xzoom 1
                repeat

        show serena contest closedbrow talkingmouth:
            xpos 0.33
        show jasmine contest closedbrow sweat talking2mouth:
            xpos 0.66
        with dis

        grusha @talkingmouth "...So who's judging this thing?"

        if (IsBefore(13, 7, 2004)):
            yellow @talking2mouth "Oh, Kobukanian contests have three judges. For example, the Millennium Drop had Champion Wallace, Instructrice Fantina, and[ellipses] Baron Phobos."

        else:
            yellow @talking2mouth "Oh, Kobukanian contests have three judges. For example, the Millennium Drop will have Champion Wallace, Instructrice Fantina, and[ellipses] Baron Phobos."

        yellow @happy "It's pretty useful to know who the judges are ahead of time, so you can tailor your performance to them."

        calem @talkingmouth "Sensible. They'll be wanting to see specific kinds of appeals, won't they? Techniques that demonstrate your Pokémon's toughness might not go over well for a judge who's in the mood to see a cute Pokémon display."

        grusha @sad2eyes talking2mouth "...I've been there before. When I still boarded, there'd be some judges you knew weren't in a good mood. Nothing you did would squeeze a point out of them."
        grusha @closedbrow talking2mouth "That's why you needed to keep an eye on which judges seemed most excited. If you managed to push a judge over the edge, they'd award you a ton of points."
        grusha @sad2eyes sadeyebrows "Of course, after they were satisfied, they'd want to see something else, so you couldn't rely on the same trick forever."

        calem @sad "Probably for the best. A contest where one performer does the same thing over and over sounds rather dull."

        grusha @closedbrow talking2mouth "I could have lived with it."

        yellow @talking2mouth "It sounds like it's the same for Pokémon contests as it is in snowboarding, then." 
        yellow @talkingmouth "Once a judge awards a jackpot, they usually start looking for something else... though they become easier to get excited, since they've been 'warmed up.'"

        red @happy "And, for the record, Yellow knew all this stuff {i}before{/i} she started participating."
        if (HasEvent("Yellow", "AcceptPartner")):
            red @talking2mouth "She totally carried me when we performed together."
       
        yellow @blush closedbrow talking2mouth "It's just basic knowledge. I know enough to get by, but to actually perform in a {i}real{/i} contest[ellipses] even if I do it--did it--that's not me."
        yellow @blush sadbrow talkingmouth "The coordinators... everyone up on stage... they're so brave. And beautiful."

        pause 1.0

        grusha @confusedeyebrows talking2mouth "?"
        calem @angrybrow talking2mouth "."
        red @angrybrow talking2mouth "!"

        narrator "A moment passes, as Grusha, Calem, and you all lock eyes and communicate in the universal man-language of eyebrow waggles."
        narrator "You nod, and come to a silent agreement."

        hide serena
        hide jasmine

        show calem talkingmouth:
            xpos 0.25
        show grusha happybrow:
            xpos 0.75
        show yellow neutrallowponytail blush surprised
        show red happy at Transform(xpos=0.08, yanchor=0.35)
        with vpunch

        Character("The Boys") "\"You're beautiful, too, Yellow.\""

        show calem smilemouth
        show grusha -happybrow
        hide red with dis
        with dis

        pause 1.0

        yellow @heavyblush sad2eyes talkingmouth "Th-thanks... but... please don't say that..."

        calem @closedbrow talking2mouth "Of course."

        grusha @closedbrow talking2mouth "{i}Como desees.{/i}"

        red @sadbrow talkingmouth "We meant it, though."

        show yellow:
            parallel:
                ease 0.5 xpos 0.52
                ease 1.0 xpos 0.48
                ease 0.5 xpos 0.5
                repeat 3
            parallel:
                ease 6.0 ypos 1.3

        show calem happy
        show grusha happy 
        with dis

        yellow cryingeyes talking2mouth "{size=30}Dooooooon't...{/size}"

        scene blank2 with splitfade

        narrator "Yellow, you, and the boys watch the contests with passive interest."
        narrator "You start to notice little oddities, though..."

        pause 0.5

        narrator "Perhaps two singers are singing at slightly different rhythms."
        narrator "May's dance steps are not perfectly coordinated, and she stumbles once or twice."
        narrator "After a while, Jasmine has to excuse herself from the stage, and sits down in the front row as she recovers her breath."
        narrator "And... Klara's sportswear clashes somewhat with the other coordinators' formal outfits, even with the addition of her mink coat."
        narrator "Meanwhile, Tia seems to be entirely unaware of the other performers, dancing to a tune only she can hear."
        narrator "Lisia dashes between the performers, providing advice, straightening outfits, providing guiding notes for their vocal performances..."
        narrator "But she's clearly sweating."

        pause 1.0

        narrator "Only Dawn has a performance you could call 'flawless,' but you can't help but feel that her performance is lacking in some originality."
        narrator "Of course, you don't recall ever seeing a Pokémon contest of {i}any{/i} nature before, so you're not sure where this impression is coming from."

        pause 1.0

        scene concerthallstage
        show calem:
            xpos 0.25
        show grusha:
            xpos 0.75
        show yellow neutrallowponytail
        with dis

        pause 1.0

        calem @talkingmouth "Hm."

        pause 0.5

        yellow @sadbrow talking2mouth "Ooh, that looked like it hurt. Should I...? Oh, no, she's okay."

        pause 0.5

        grusha @closedbrow talkingmouth "I'm just going to say it."
        grusha @sad2eyes sadeyebrows "I mean, we're all thinking it."

        pause 1.5

        grusha @closedbrow talking2mouth "They're trying very hard, and we should be proud of them."

        calem @surprised "Oh?"

        grusha @talkingmouth "What, did you think I was going to say something else? Have more faith."

        calem @angrybrow "{w=0.5}.{w=0.5}.{w=0.5}."
        calem @closedbrow talking2mouth "...I suppose Lisia has only had them for less than a month."

        yellow @talking2mouth "There were a lot of coordinators who were part of the club before, who just joined as, um, hobbyists."
        yellow @closedbrow talkingmouth "After you convinced Lisia to take over, most of the club dropped out. There used to be... about forty of them..."

        calem @talkingmouth "And now there's less than a fourth of that number."
        calem sadbrow "{w=0.5}.{w=0.5}.{w=0.5}."
        calem @talkingmouth "Did I... do something wrong by asking Lisia to teach?"

        yellow @closedbrow talking2mouth "You did something you thought was right, that you thought would help people, at the time."
        yellow @sadbrow talkingmouth "That's all anyone can do, really..."

        grusha @closedbrow talking2mouth "{i}No te preocupes.{/i} The only reason they're worrying about making a splash at the {i}Millennium{/i} is because now there's actually a chance they might. Before Lisia? Nah."

        pause 1.0

        red @happy "Making a splash?"

        grusha @talkingmouth "I do more than ice puns."

        red @talkingmouth "Anyway, what Yellow and Grusha say is right. You helped the coordinators--the ones who wanted to work for it--out."
        red @closedbrow sweat talking2mouth "I guess you might've upset a few hobbyists, but..."

        narrator "You gesture vaguely at the large building you're in."

        red @talking2mouth "It seems like a bit of a waste for the school to have spent {i}this much{/i} money on a club that doesn't get stuff done."

        calem @closedbrow talkingmouth "I suppose there's some truth amongst your points. Thank you for your support, you two."

        red @talking2mouth "Anytime."

        pause 1.0

        yellow @talking2mouth "Looks like they're wrapping up. It's getting kinda late, so we should probably head back to the dorm, [first_name]."

        calem @talkingmouth "Yes, let's--" 
        extend @surprised "hm? Grusha, what is it?"

        grusha @angrybrow talking2mouth "...What's she doing here?"

        redmind @thinking "Who?"

        show melody on with dis:
            xpos 0.2

        show calem:
            xpos 0.25 xzoom 1
            ease 0.5 xpos 0.4 xzoom -1

        show yellow:
            xpos 0.5 
            ease 0.5 xpos 0.6

        show grusha:
            xpos 0.75
            ease 0.5 xpos 0.8

        pause 1.0

        redmind @frownmouth "Oh."

        melody @talkingmouth "...Watching the coordinators. Not a crime."
        melody @bubblemouth "{w=0.5}.{w=0.5}.{w=0.5}."
        melody @talkingmouth "What're you doing here?"

        calem @angrybrow talkingmouth "I'm here to support Serena."

        grusha @talkingmouth "Keeping an eye on Jasmine."

        melody @talkingmouth "Got it. Your girlfriends dragged you here."

        calem @surprisedbrow talking2mouth "Hold on, now--!"

        grusha @closedbrow talking2mouth "You kidding? Her and me?"

        calem @talkingmouth "We're friends, nothing more. There is not even the potential for more."

        grusha @confusedeyebrows talking2mouth "Can you see that working? Really? There's so many reasons that's not happening."

        calem @surprised "I mean, the {i}very idea{/i} beggars the imagination, with a {i}multitude{/i} of... of... factors!"

        grusha @closedbrow talking2mouth "Not happening. Ever."

        melody @bubblemouth "{w=0.5}.{w=0.5}.{w=0.5}."
        melody @talkingmouth "This is so effing high school."
        melody @sadbrow talking2mouth "Fine. Your friends, who are girls, but not girlfriends, dragged you here."
        melody @talkingmouth "What about you, Blondie?"

        yellow @sadbrow talking2mouth "{size=30}...I just think they're pretty...{/size}"

        melody @sadbrow talkingmouth "...This is so sad. You're literally going to make me cry."

        pause 1.0

        melody @talkingmouth "Right. I'm going to join the team. Be right back."

        if (melody_name == None):
            $ melody_name = first_name

        melody @talkingmouth "Later, [melody_name]."

        red @surprised "Huh?"

        hide melody with dis

        pause 1.0

        calem @surprisedbrow talking2mouth "...Join the team? What did she mean by that?"

        redmind @thinking "And... why didn't she ask me why I'm here?"

        show studentcouncil at sepia with dis
        show flashback with dis

        $ renpy.pause(1.0, hard=True)

        show cheren upeyes talking2mouth at sepia behind flashback with dis

        cheren @talkingmouth "You've grown far too comfortable being the most interesting person in every room."
        cheren sad2eyes talkingmouth "You're going to have to learn to realize that occasionally people wish to interact with each other {i}without{/i} using you as a medium."

        hide cheren
        hide studentcouncil
        hide flashback
        with Dissolve(1.0)

        redmind @upeyes frownmouth angryeyebrows "If you keep living in my head, I'm going to start charging you rent."

        call clearscreens() from _call_clearscreens_292
        scene blank2 with splitfade

        $ coordinatingknowledge += 50

        narrator "[bluecolor]Your {/color}[contestcolor]Coordinating Knowledge{/color}[bluecolor] increased by 20 from watching the rest of the club meeting!{/color}"

        narrator "Meanwhile, backstage..."

        python:
            playercharacter = "Lisia"
            timeOfDay = "Night"
            oldinventory = copy.copy(inventory)
            oldpersonalstats = copy.copy(personalstats)
            oldparty = copy.copy(playerparty)
            oldpersondex = copy.copy(persondex)
            oldclassstats = copy.copy(classstats)

            inventory = {
                Item.WallaceBrandPokemakeupKit : 1,
                Item.InstantCoffee : 1,
                Item.TwoToneWig : 1,
                Item.MegaTiara : 1,
                Item.RibbonCase : 1,
                Item.KeytoSootopolis : 1,
            }
            personalstats = {
                "Charm" : 334,
                "Knowledge" : 78,
                "Courage" : 64,
                "Wit" : 49,
                "Patience" : 22
            }
            playerparty = GetTrainerTeam("Lisia")
            persondex = copy.deepcopy(defaultpersondex)
            #battle teammates
            persondex["Lisia"] = {"Named" : True, "Value" : 0, "Contact": True, "Sex": Genders.Female, "Relationship": "Self", "RelationshipRank": 0, "Events": [] }
            persondex["Grandad"] = {"Named" : True, "Value" : 125, "Contact": True, "Sex": Genders.Male, "Relationship": "Granddaughter", "RelationshipRank": 0, "Events": [] }
            persondex["Wallace"] = {"Named" : True, "Value" : 247, "Contact": True, "Sex": Genders.Male, "Relationship": "Niece", "RelationshipRank": 0, "Events": [] }
            persondex["Dawn"] = {"Named" : True, "Value" : 98, "Contact": False, "Sex": Genders.Female, "Relationship": "Mentor", "RelationshipRank": 0, "Events": [] }
            persondex["May"] = {"Named" : True, "Value" : 20, "Contact": False, "Sex": Genders.Female, "Relationship": "Mentor", "RelationshipRank": 0, "Events": [] }
            persondex["Brendan"] = {"Named" : True, "Value" : 56, "Contact": False, "Sex": Genders.Male, "Relationship": "Mentor", "RelationshipRank": 0, "Events": [] }
            persondex["Jasmine"] = {"Named" : True, "Value" : 23, "Contact": False, "Sex": Genders.Male, "Relationship": "Mentor", "RelationshipRank": 0, "Events": [] }
            persondex["Serena"] = {"Named" : True, "Value" : 47, "Contact": False, "Sex": Genders.Male, "Relationship": "Mentor", "RelationshipRank": 0, "Events": [] }
            persondex["Tia"] = {"Named" : True, "Value" : 28, "Contact": False, "Sex": Genders.Male, "Relationship": "Mentor", "RelationshipRank": 0, "Events": [] }
            persondex["Klara"] = {"Named" : True, "Value" : 12, "Contact": False, "Sex": Genders.Female, "Relationship": "Mentor", "RelationshipRank": 0, "Events": [] }
            persondex["Misty"] = {"Named" : True, "Value" : 50, "Contact": False, "Sex": Genders.Female, "Relationship": "Mentor", "RelationshipRank": 0, "Events": [] }

            classstats = { 
                "Normal" : 35,
                "Fire" : 23,
                "Water" : 42,
                "Grass" : 13,
                "Electric" : 47,
                "Ice" : 6,
                "Fighting" : 3,
                "Poison" : 2,
                "Ground" : 2,
                "Flying" : 19,
                "Psychic" : 6,
                "Bug" : 1,
                "Rock" : 1,
                "Ghost" : 24,
                "Dark" : 1,
                "Dragon" : 52,
                "Steel" : 6,
                "Fairy" : 50
            }

        narrator "{color=#71BBA2}You{/color} are fretting over a rapidly-approaching contest."

        scene concerthallbackstage
        show may contest closedbrow sadmouth:
            xpos 1.0/9.0
        show brendan contest closedbrow frownmouth sweat behind may:
            xpos 2.0/9.0 xzoom -1
        show serena contest closedbrow sadmouth:
            xpos 3.0/9.0
        show misty contest closedbrow behind serena:
            xpos 4.0/9.0 xzoom -1
        show dawn contest:
            xpos 5.0/9.0
        show tia contest closedbrow sweat frownmouth:
            xpos 6.0/9.0
        show klara winkbrow talking2mouth neutralcoat hairpin behind tia:
            xpos 7.0/9.0
        show jasmine contest sweat closedbrow talking2mouth:
            xpos 8.0/9.0
        show screen currentdate
        with splitfade

        Character("Coordinators") "\"{size=50}...Phew.{/size}\""

        lisia @happy "Great work, everyone! I'm really proud of you. I can definitely see the diamonds that you'll become!"

        dawn @happy "Thanks, Lisia!"

        may @closedbrow talking2mouth "{size=30}...I can't feel my legs.{/size}"

        brendan @sadbrow talking2mouth "{size=30}I can give you a massage when we get back to the dorm.{/size}"

        may @sadbrow talkingmouth "{size=30}Thanks, sweetie...{/size}"

        lisiamind @closedbrow frownmouth "...Hm. That Birch girl. Brendan takes his contests seriously, but it feels like May's just along for the ride..."
        lisiamind @sadbrow frownmouth "I hope I don't have to give him a different training partner. Their rapport's fantastic, but I'm not sure they're effective at training together... too soft on each other."

        misty @sadbrow talkingmouth "I think I... lost my voice. I've never sung that long. Not even at the theater..."

        lisia @talking2mouth "That's not good! Practicing your singing's important, but you don't want to burn yourself out before the actual contest happens! It's bad enough trying to be heard over other people's jamming performances."

        serena -closedbrow -frownmouth @talkingmouth "Ah... yes. You've been focusing on training your voice, haven't you, Misty?"

        misty @talkingmouth "As much as I can. But projecting my voice only works so much. I'll still never be louder than a sound-based move, a move that causes a massive explosion, a move that changes the weather, or a move that uses wind in some way..."

        lisia @angrybrow talking2mouth "All it takes is one guy with a vendetta against you and an Exploud to completely drown out any chance of the judges noticing you."
        lisia @talkingmouth "That's why it's so important to practice routines! Simple physical moves, like biting, kicking, punching, and slicing moves are really easy and fast to execute." 
        lisia @happy "Even if someone tries to throw off your performance, you can stay focused if you're just doing a simple routine like that."

        jasmine -closedbrow -sweat -talking2mouth @talkingmouth "Such simple routines are not likely to be notably impressive, though, no?"

        lisia @talkingmouth "No... but it's better to pull off an unimpressive technique flawlessly than to fall on your face while trying to pull off a trickier one."

        show tia happy with dis

        tia "[tiafont]Thanks, Liz! You're incredibly knowledgeable about contests, you know? I really admire you!{/font}"

        lisia @happy "Hah hah! Same to you, Venetia!"

        pause 1.0

        lisiamind @sadbrow frownmouth "I still have no idea what she's saying."
        lisiamind @thinking "I just don't have time to hire an interpreter for her, but I really don't see her having much success in the contest, anyway... she doesn't pay attention to the other performers at all."

        Character("???") "\"Excuse me.\""

        lisia @talkingmouth "Hm?"

        show may surprisedbrow frownmouth:
            xpos 1.0/9.0
            ease 0.5 xpos -0.5
        show brendan surprisedbrow frownmouth:
            xpos 2.0/9.0
            ease 0.5 xpos -0.5
        show klara surprisedbrow frownmouth:
            xpos 7.0/9.0 xzoom 1
            ease 0.5 xzoom -1
            pause 0.2
            ease 0.3 xzoom -1
            ease 0.5 xpos -0.2
        show tia -angrybrow -sweat confusedeyebrows frownmouth:
            xpos 6.0/9.0
            ease 0.5 xpos 4.0/9.0
        show serena surprisedbrow frownmouth
        show jasmine surprisedbrow frownmouth:
            xpos 8.0/9.0 xzoom 1
            ease 0.5 xzoom -1
            pause 0.2
            ease 0.3 xzoom 1
            ease 1.0 xpos 2.0/9.0
            ease 0.3 xzoom -1
        show dawn surprisedbrow frownmouth:
            xpos 5.0/9.0
            ease 0.5 xpos 1.0/9.0
        show misty angrybrow:
            xpos 4.0/9.0
            ease 0.5 xpos 5.0/9.0
        with dis

        may @talkingmouth "Ah! It's her!"

        pause 1.0

        show melody on at night:
            xpos 1.2 xzoom -1
            ease 0.5 xpos 0.9

        melody @surprisedbrow bubblemouth "{w=0.5}.{w=0.5}.{w=0.5}."
        melody @surprisedbrow talkingmouth "Wow. Guess I made a splash."

        pause 0.5

        melody @talkingmouth "Water pun."

        pause 1.0

        melody @talking2mouth "What, what's the deal? I don't bite."

        lisiamind @closedbrow frownmouth "Hm... I recognize her. She aced her tryout rounds--even I was impressed. But it looks like my pupils are {i}also{/i} familiar with her... and not in a good way."
        lisiamind @angrybrow frownmouth "Alright, Liz. You can get along with everybody. Build that bridge!"

        lisia @happy "Hi! I'm Lisia, the Coordinator Club's advisor!~ We just finished practice, so I'm afraid the other clubmembers need to go back to their dorms now, but is there something I can help you with?"

        show tia surprisedbrow frownmouth
        show misty angry
        show serena surprisedbrow frownmouth
        show jasmine surprisedbrow frownmouth
        show dawn surprisedbrow frownmouth
        with dis

        melody @talkingmouth "Yeah, I'd like to join."

        pause 0.5

        lisiamind @talkingmouth "Okay... this wasn't a part of the script I expected."

        lisia @talkingmouth "O... kay. Um, I'm not sure we're accepting any new members right now."
        lisia @happy "But, if you think you have a strong case, and you're not afraid to work {i}really{/i} hard at it, I'll hear you out."

        melody @talkingmouth "...Okay."

        melody up @talkingmouth "I've spent years mastering my singing technique. My breath control is precise, and my vibrato is consistent at 5-6 oscillations per second. I can sing from G2 to C6 with perfect pitch accuracy." 
        melody @closedbrow talkingmouth "I control dynamics flawlessly, ranging from 30 to 90 decibels, and my melismatic runs can execute 15 notes per second with precise intonation." 
        melody @talking2mouth "With perfect relative pitch, I can harmonize instantly, and my understanding of harmonic overtones adds measurable depth, as confirmed by spectrogram analysis." 
        melody @closedbrow talking2mouth "Finally, I've participated in every contest in the Orange Archipelago, with a seventy-five percent winning rate."
        melody @bubblemouth "{w=0.5}.{w=0.5}.{w=0.5}."
        melody @talkingmouth "That's {i}every{/i} contest. The Tangelo Open, the Pinkan Junior Cute and Beauty Contests, the Kinnow Memorial Festival, the Pummel-Hamlin Unity Concert, the Mandarin Island Orange Archipelago Grand Open..."
        melody @closedbrow talkingmouth "Et cetera."
        melody on @talkingmouth "And I was the Festival Maiden for seven years running in the Shamouti Island Legend Festival. Which is a big thing in Shamouti." 

        lisia @surprisedbrow frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."

        $ BecomeNamed("Melody")

        lisia @happy "Well, that's a {i}very{/i} impressive resume, you must be Melody, then! I remember hearing about a young woman who was clearing the Orange Archipelago's contest league a couple years ago."

        melody surprisedbrow @neutralbrow talkingmouth "I was also a member of the Coordinator Club during the 2003-2004 school year. I never placed anywhere but first."

        misty @talkingmouth "That's a lie! I don't know about all the other stuff you said, but I know that last one's a lie!"

        show tia surprisedbrow frownmouth:
            ease 0.5 xpos -0.2
        show misty angry:
            ease 0.5 xpos 0.33
        show serena surprisedbrow frownmouth:
            ease 0.5 xpos -0.2
        show jasmine surprisedbrow frownmouth:
            ease 0.5 xpos -0.2
        show dawn surprisedbrow frownmouth:
            ease 0.5 xpos -0.2
        with dis

        melody @bubblemouth "{w=0.5}.{w=0.5}.{w=0.5}."
        melody @talkingmouth "...Why do I know you?"

        misty @talkingmouth "We take classes together!"

        melody -surprisedbrow @surprisedbrow talkingmouth "...Bug?"

        misty @talkingmouth "I hate bugs! I'm in a Goldeen-print swimsuit {i}right now!{/i} Water, dumbass!"

        lisia @angry "Language!"

        melody @talkingmouth "It's fine. I get it now."
        melody @angry "Red hair and a hand-me-down contest outfit? You must be Misty."

        misty @talkingmouth "What is {i}that{/i} supposed to mean?!"

        melody @talkingmouth "Apple doesn't fall far from its tree, I guess. You're the spitting image of your sisters."

        show misty surprisedbrow frownmouth with dis

        melody @talkingmouth "Although they were prettier, taller, and apparently smarter."

        misty angry "You shut up!"
        misty @sadbrow talkingmouth "Liz, you can't {i}seriously{/i} be thinking about bringing her into the club?"
        misty @talkingmouth "She's... she's the {i}worst!{/i}"

        melody @talkingmouth "Not the worst at contests."
        melody @talking2mouth "Besides, I'm not the one causing problems here."

        pause 0.5

        melody @talkingmouth "I'm qualified. Practiced. I passed the tryouts without breaking a sweat."
        melody @talkingmouth "I'll win the Millennium Drop for you, Lisia. Phobos will give you a blank check. That means a new round of outfits for everyone, on the school's dime."
        melody @talking2mouth "You'd have the money to hold {i}any{/i} contest you want, right here in Kobukan. Build a new contest hall that isn't haunted to hell and back. Want to make 'World Contest Champion' mean more?" 
        melody @talkingmouth surprisedbrow "Ten billion would go a long way towards that."
        melody @talkingmouth "That's Tamamushi-level money."
        melody @talking2mouth "I know you won't leave it on the table."

        lisiamind @closedbrow frownmouth "It's true that having Phobos' support would make my dreams of expanding the influence and importance of contests {i}much{/i} easier."
        lisiamind @frownmouth "And, truthfully, I think she probably {i}could{/i} win the Millennium Drop Water Festival Contest. Even now. Her resume is legendary, for such a young girl."
        lisiamind @closedbrow frownmouth "But half my pupils are terrified of her, and the other half hate her."
        lisiamind @closedbrow talking2mouth "She makes a good point... but is it worth the drama? Of course, coordinators thrive on drama, but is it worth {i}that much{/i}...?"

        melody @talkingmouth "...Having difficulty deciding. Fine. Expected."

        show melody at night:
            xzoom -1 xpos 0.9
            ease 0.5 xzoom 1

        melody @bubblemouth "{w=0.5}.{w=0.5}.{w=0.5}." 
        melody @talkingmouth "I respect you a lot, Lisia. So I'm not going to let you make a wrong decision."
        melody @talking2mouth "If you can't decide, check your phone. You have a voicemail. Listen to it."
        melody @talkingmouth "That'll make the decision for you."

        pause 0.5

        melody @talkingmouth "{i}Adiós.{/i}"
        melody @talking2mouth "See you in Bug class, Misty."

        hide melody with dis

        pause 1.0

        misty sad "No way... you can't really be...?"

        pause 1.0

        lisia @closedbrow frownmouth "...I think I need to listen to that voicemail."

        call clearscreens() from _call_clearscreens_293
        scene blank2 with splitfade

        python:
            inventory = oldinventory
            personalstats = oldpersonalstats
            playerparty = oldparty
            persondex = oldpersondex
            classstats = oldclassstats
            playercharacter = None

        pause 1.0

        return True

label Contest2:
    stop music fadeout 1.5
    queue music "audio/music/lawrencetheme_start.ogg" noloop
    queue music "audio/music/lawrencetheme_loop.ogg"

    if (not HasEvent("Game", "Contest2")):
        $ AddEvent("Game", "Contest2")
        if (HasEvent("Yellow", "AcceptPartner")):
            narrator "As soon as you walk through the front doors of the the Contest Hall, you see Yellow, who eagerly joins up with you, and you proceed to the stands together."

            yellow @happy "Hi, [first_name]! I guess we had the same idea. I thought watching the other Coordinators might help us for the Millennium Drop, later."

        elif (HasEvent("Klara", "AcceptPartner") and not HasEvent("Klara", "BrokeBond")):
            narrator "As soon as you walk through the front doors of the the Contest Hall, you see Klara, who seems uncharacteristically quiet, and is staring at her feet."

            klara makeup hairpin neutralcoat @sadbrow talking2mouth "Hiya, [first_name]. You came to watch the Coordinators, too[ellipses]?"

            pause 1.0

            klara @talking2mouth closedbrow "The club meeting's been going for a while. I was just waiting for[ellipses]"

            pause 1.0

            narrator "She trails off."

            pause 1.0

            klara @restrainedbrow talking2mouth "Let's go. I don't want Liz to yell at me again."

        narrator "This time, you manage to make your way to the Contest Coliseum stage without losing half an hour to spectral forces." 
        narrator "However[ellipses]"
        narrator "After arriving, you might prefer the ghosts."

        scene concerthallstage
        show lisia angrybrow frownmouth:
            xpos 0.25 xzoom -1
        show dawn contest sadbrow frownmouth:
            xpos 0.5
        show phobos frownmouth:
            xpos 0.75
        with vpunch

        phobos @talking2mouth "Honestly, Lisia, is this the best you can do with Dawn? Tired rehashing of her mother's routines? Come now, I'd expect more from the World Contest Champion."

        lisia @talking2mouth "Baron Lawrence Phobos, Dawn's in the process of discovering her own unique Coordinator's style. This will take {i}time{/i}. Dawn's performances are--"

        phobos @upeyes angryeyebrows talking2mouth "Oh, do stop going on, and on, and {i}on{/i} about it. I don't know how many times I've had to tell you I don't like when people say the same pointless thing over and over and over."
        phobos @talking2mouth "I simply can't see Dawn up on the stage of the Millennium Drop proper. Certainly, she passed her tryouts, but let's be honest, the calibre of man we allowed into the tryouts left little in the way of decent competition."
        phobos @sad2eyes sadeyebrows talking2mouth "There was one man--portly, rather rounded, fat, in fewer words--who had {i}dirt{/i} on his hands. In a contest. What an embarrassment."

        lisia @talking2mouth "Dawn is a coordinator with an {i}extremely{/i} promising future. She needs {i}experience{/i} in order to develop her own style, which she can't get if we don't let her participate in--"

        phobos @sadbrow talkingmouth "Liz, Liz, Liz. We're not in the business of promising futures--this is a {i}school{/i}. We're here for {i}achievement{/i}. Can you imagine the horror if your own star pupil failed tremendously on the {i}actual{/i} contest stage?"
        phobos @happy "Honestly, Liz, Dawn, I'm doing you girls a favor. A gift. A present, one might say. Why walk into a situation where you know the judges will be biased against you?"

        pause 1.0

        lisia @talking2mouth "There won't be any bias."

        pause 1.0

        phobos @sadbrow talkingmouth "Liz, Liz, Liz. You should really pay more attention to what people around you are saying. I'm a judge, and I've expressed my thoughts on the matter--have I not? I just won't be swept up, by[ellipses]"

        phobos @talkingmouth "Pardon my crude language, but[ellipses] such {i}unoriginal{/i} performances."
        phobos @talking2mouth closedbrow "Fantina, for her part, though only winning {i}regional{/i} contests, is {i}very{/i} familiar with the contest scene of Sinnoh, including the performances of Johanna."
        phobos @sadbrow talkingmouth "Her unladylike fondness for ghosts won't give her ever greater appreciation for a dead performance, I fear."

        pause 1.0

        lisia @angrybrow talking2mouth "Uncle Wallace--"

        phobos @happy "Ah, I'm glad you mentioned him!"
        phobos @sad2eyes angryeyebrows talking2mouth "But, please, refer to him as World Contest Champion Wallace. It's only respectful to use his title."

        lisia @talking2mouth "[ellipses]I {i}am{/i} World Contest Champion Lisabeth Lutia."

        phobos @confusedbrow talking2mouth "Yes...? I know. Which is why I would have thought you would remember to give your uncle his due respect? In any case, a man of such strength and character will doubtlessly see things the same way I do."

        show dawn surprisedbrow with dis

        lisia surprisedbrow frownmouth @angry "The way {i}you{/i} see things, Baron Phobos, is a whole pile of--!"

        dawn @talking2mouth "W-wait!"

        show phobos -frownmouth with dis

        dawn @talkingmouth sad2brow "He's right. All my routines are just what my mother taught me, over a decade ago[ellipses] they're just hers. I don't have any original routines."
        dawn -surprisedbrow @sadbrow talkingmouth "Maybe I could win the Millennium Drop contest, but[ellipses] if I'm just winning using the same routines I always have, without really {i}thinking{/i} about what I'm doing, then[ellipses] maybe I don't deserve to win."

        lisia angrybrow @sadbrow talkingmouth "Dawn, if you want to participate--"

        phobos @talkingmouth closedbrow "Well done, Dawn. This is a very noble thing. Stepping aside for those more deserving shows great character."
        phobos @talking2mouth closedbrow "Why, I'd do the same thing--save that 'stepping aside' is a bit out of my reach, if you'll pardon the pun."

        lisia @sadbrow talking2mouth "[ellipses]Dawn."

        dawn @downcast2eyes talking2mouth "I'm sorry, Liz."

        hide dawn with dis

        pause 1.0

        red @shadow angry "{size=30}That[ellipses] {i}that{/i}[ellipses]{/size}"

        if (HasEvent("Yellow", "AcceptPartner")):
            yellow @angrybrow talking2mouth "{size=30}It's not right. He shouldn't be able to talk to people like that[ellipses]{/size}"

        elif (HasEvent("Klara", "AcceptPartner")):
            klara makeup @angrybrow frownmouth "{size=30}[ellipses]{/size}"

        phobos @happy "Well, ta-ta-ta. Must be off, now. I have many other hopefuls to supervise."

        hide phobos with dis

        pause 1.0

        show lisia sadbrow frownmouth with dis

        lisia @talking2mouth "{size=30}Ten billion, Liz. Keep your eyes on that. After you get the ten billion, you can make it right[ellipses]{/size}"

        hide lisia with dis

        pause 2.0

        red @angrybrow shadow talking2mouth "[ellipses]What an ass. He thinks he can just tell everyone what to do because he's got more money than them? Some 'royal' bloodline...?"

        $ PlaySound("pokemon/pikachu_angry1.ogg")
        libpikachu glowing @angryeyes angrymouth shadow "Pi-ka!"

        if (HasEvent("Yellow", "AcceptPartner")):
            show yellow frownmouth with dis

            yellow @angrybrow talking2mouth "[pika_name][ellipses] calm down. I know you're angry. I am, too. But we can't do anything right now."

        elif (HasEvent("Klara", "AcceptPartner") and not HasEvent("Klara", "BrokeBond")):
            show klara makeup hairpin coat frownmouth with dis

            klara @angrybrow talking2mouth "The way this guy acts reminds me of Chairman Rose[ellipses]"

            pause 1.0

            klara @talking2mouth "Watch out for Melody. The apple doesn't fall far from the tree. She's doing something, too--I don't know what, but I think she's blackmailing Lisia."

            pause 0.5

            klara @angrybrow talking2mouth "That's not just something I 'heard.' It's something I 'saw.' Lisia didn't want to let Melody into the team, but then Melody left her a voicemail, and she changed her mind overnight."

            red @confused "Why're you telling me this?"

            pause 0.5

            klara @talking2mouth "Someone as trusting as you could get {i}really{/i} hurt by a girl like[ellipses] her."

        pause 1.0

        if (HasEvent("Klara", "AcceptPartner") and not HasEvent("Klara", "BrokeBond")):
            klara @angrybrow talking2mouth "I'm going to the stage. Just watch me. During the Millennium Drop, remember what I'm about to do, then make me look better."

            hide klara with dis

            narrator "Klara leaves without waiting for you to respond."

            pause 2.0

        else:
            yellow @talking2mouth "It's so frustrating[ellipses] contests are meant to be performances of beauty, and[ellipses] and[ellipses] self-expression."
            yellow @angrybrow talking2mouth "But all Phobos wants is to have people express whatever {i}he{/i} wants."

            narrator "Watching the Coordinators... it's true. None of them seem to particularly be enjoying themselves, and even Lisia seems like she's feeling the burden of Phobos' looming presence."

            pause 1.0

            yellow @sad2eyes talking2mouth "I don't think we're going to get much more from this, [first_name]."

            red @closedbrow talking2mouth "Maybe not."

            pause 1.0

            narrator "You and Yellow sit in moody silence together for a while."

            yellow @talking2mouth "Okay. I'm going to go back to the dorm and work on a suit. Um, will you come with me?"

            red @talking2mouth "Go ahead. I think I see Brendan waving me over. I'll be over after."

            yellow @talkingmouth "Alright. Um[ellipses] don't lose your temper with Phobos, okay?"

            red @sweat sadeyebrows sad2eyes talkingmouth "I think that's up to him, honestly."

            yellow @sadbrow talking2mouth "{size=30}Oh dear[ellipses]{/size}"

            hide yellow with dis

            pause 2.0

        show brendan contest frownmouth with dis

        brendan @talking2mouth "Hey, bro."

        red -shadow @talking2mouth "It's worse than I thought. It's[ellipses] {i}so{/i} much worse."

        brendan @talking2mouth "Yeah, our last couple meetings have been like this. We can barely even practice anymore, because as soon as we try, he--"

        show brendan surprisedbrow:
            xpos 0.5 xzoom 1
            ease 0.5 xpos 0.33 xzoom -1

        show phobos with vpunch:
            xpos 0.66

        phobos happy "Brendan! Just the one I was looking for."

        show brendan -surprisedbrow with dis

        pause 0.5

        phobos surprisedbrow frownmouth @talking2mouth "Oh, and you're here as well."

        red @shadow frownmouth "[ellipses]"

        if (IsCoordinator()):
            phobos -surprisedbrow -frownmouth @closedbrow talking2mouth "I suppose you were, technically, at the Millennium Drop tryouts. You fancy yourself a Coordinator now, I suppose? Points for spirit, though not many."

        else:
            phobos -surprisedbrow -frownmouth @closedbrow talking2mouth "I don't recall seeing you at the Millennium Drop tryouts. Well, whatever reason you have for finally showing an interest in the nobler art of Coordinating, I applaud you."

        brendan @talking2mouth "La-- Baron Lawrence Phobos the Third? You wanted to talk to me?"

        redmind @thinking "I can practically hear his teeth grinding together from how much he didn't want to say that."
        redmind @angrybrow "But if Phobos thinks he can bully Brendan into quitting like he did with Dawn, then he's got another think coming."#intentional word choice!
        redmind @thinking "I've never seen someone so dedicated to contests. He won't back down."

        phobos @talkingmouth "Yes, yes, yes. I simply wanted to express my {i}admiration{/i} for you. I know all too well how difficult it is to be a man in this woman-dominated field."
        phobos @happy "I believe I sense in you another student of Champion Wallace's iconic Coordination style? One that revels in and celebrates masculinity, as opposed to the traditional diminishing and mockery we so often feel?"

        brendan @talking2mouth "I, uh, think Champion Wallace is an inspiration to all coordinators, yeah."

        redmind @closedbrow sweat frownmouth "Tactfully dodging the crazy part of the question. Well done."

        phobos @talkingmouth "Splendid, I thought I sensed a kindred spirit. Well, I'll be honest with you then, my boy, my friend, my companion."
        phobos @winkbrow talkingmouth "I'm rooting for you, in actuality. Oh, but what of my niece, you must be thinking?"
        phobos @closedbrow talkingmouth "Perhaps our shared fondness for Water-types is thicker than blood? Oh-ho-ho. How droll."

        brendan @annoyedbrow talking2mouth "Thank you. I'll, uh, do my best to win."

        pause 1.0

        phobos @talking2mouth "Splendid. So you'll change your song?"

        pause 0.5

        brendan @talking2mouth "What?"

        phobos @sadbrow talkingmouth "Well, you said you'd do your best to win. It must have occurred to you that the song you have been practicing is... {i}not{/i} fantastic, no?"

        brendan @angrybrow talking2mouth "It's an old Hoennian hymn. It's--"

        phobos @closedbrow sweat talking2mouth "Yes, yes, yes. Don't tell me things I'm already interintimately familiar with, my dear Brendan."
        phobos @talking2mouth "Regardless of its {i}history{/i}, it's just not[ellipses] {i}it{/i}. It doesn't quite have the 'wow' factor that modern performances require, no?" 
        phobos @sadbrow talkingmouth "We don't want your dear Wailmer to be performing its heart out, but be brought down by a subpar vocal performance on the part of the Coordinator, do we? Of course we don't."

        pause 0.5

        phobos @talkingmouth "Luckily, because I'm in your corner, I've already come up with a splendiferous alternative for you."

        brendan surprisedbrow @neutralbrow talking2mouth "A different song?"

        phobos @talkingmouth "Exactly. I imagine you've heard of {i}Dream Energy{/i}?"

        brendan @talking2mouth "You[ellipses] you've gotta be kidding me."

        redmind @thonk "Hm? Does Brendan recognize this song? Doesn't ring a bell for me[ellipses]"

        phobos @talking2mouth "I think perhaps you're confused. I'm certainly not kidding. We're talking of the same song, yes? {i}Dream Energy{/i}, by famous Almian country singer Blake Hall?"

        brendan -surprisedbrow @sadbrow talking2mouth "Baron, that song {i}sucks{/i}. It's literally famous for being awful."

        phobos @closedbrow talking2mouth "Nonsense. The Go-Rock Triplets performed it in Almia for Altru Inc.'s 70th anniversary. Oh, the Go-Rock--"

        brendan @angrybrow talking2mouth "I know who the Go-Rock Quads are! And they hated the song, too! They were strongarmed into singing it, and spoke about how much they hated it in, like, {i}a lot{/i} of interviews."

        pause 1.0

        phobos @talkingmouth "Brendan, Brendan, Brendan. You're not being very gracious to someone who's given so much to help you. I know how important contests are to you, and I feel the same. Why, I paid for the floor you stand on--the roof above us."
        phobos @talking2mouth "{i}Dream Energy{/i} is a {i}favorite{/i} of mine. Surely you can show your gratitude by singing a song that would mean something grand to someone who cares for you greatly?" 
        phobos @closedbrow talkingmouth "Why, your dulcet tones could {i}surely{/i} make even Dream Energy sound[ellipses] fine."

        pause 0.5

        brendan @talking2mouth "My song is a love song to my girlfriend. It already means--"

        phobos @closedbrow talking2mouth "Oh, yes, that May girl. I've been meaning to talk with her." 
        phobos @sadbrow talkingmouth "I notice you've elected not to partner with her on the contest stage--sensibly, I might add. But I'm moreover worried about her lack of {i}commitment{/i} to coordinating."
        phobos @sadbrow talkingmouth "Not to put suspicion in your mind, but I imagine you've noticed it too? She's just a bit behind the curve in terms of her {i}commitment{/i} to contests, wouldn't you say?" 
        phobos surprisedbrow frownmouth @sad2eyes sadeyebrows talkingmouth "And, ah, if she were to appear during the Millennium Drop, while showing that lack of {i}commitment{/i}, then I--"

        brendan angrybrow @talking2mouth "I'll sing your song."

        phobos -surprisedbrow -frownmouth @talking2mouth "Splendid. I suppose I won't have to talk to May about this, then."

        pause 1.0

        brendan @talking2mouth "You won't."

        phobos @closedbrow talkingmouth "Yes, that's what I said. There's really no reason to keep saying the same thing over and over and over, Brendan. There's no {i}chorus{/i} to this."

        hide phobos with dis

        pause 1.5

        stop music fadeout 1.5
        $ renpy.music.queue("Audio/Music/SoaringIllusions_Intro.ogg", channel='music', loop=None, tight=None)
        $ renpy.music.queue("Audio/Music/SoaringIllusions.ogg", channel='music', loop=True, tight=None)

        brendan "[ellipses]"

        show brendan:
            xpos 0.33 xzoom -1
            ease 0.5 xpos 0.5

        brendan annoyedbrow @talking2mouth "That looked weak, didn't it? Like I was just letting him push me around."

        red @talking2mouth "I understand. You were protecting May."

        brendan @talking2mouth "This guy's not a coordinator. I've never been more sure of anything."

        pause 1.0

        brendan -annoyedbrow @talking2mouth "If he was, he'd know that I'm not just going to go along with what he says--I'd rather drop out from the contest than sing that {i}garbage{/i} song." 
        brendan @annoyedbrow talking2mouth "Seriously, there's a line about {i}shareholders{/i} in it." 
        brendan @talking2mouth "But if it gets him off May's and my backs for a while[ellipses]"

        red @talking2mouth "You've got a plan?"

        brendan @talking2mouth "More or less. I'll have a lot more time to work on the outfits for the party now, anyways[ellipses]"
        brendan @talking2mouth "Sorry, man. I gotta go plan."

        hide brendan with dis

        pause 2.0

        show melody sadbrow on with dis:
            xpos 0.5

        pause 0.5

        red @talking2mouth "Yeah?"

        melody @talking2mouth "I'm not with him, you know."

        red @upeyes talking2mouth "What do you mean? You're his niece."

        melody @talking2mouth "You see a family resemblance?"

        pause 1.0

        red @closedbrow talking2mouth "Why are you even telling me this? Do you think I'll think badly of you because of what he's doing?"

        melody @talking2mouth "No. I don't care if you think badly of me."
        melody -sadbrow @talking2mouth "I don't care what anyone thinks. Good. Bad. Whatever. Think what you want."

        pause 1.0

        if (IsCoordinator()):
            melody @talking2mouth "Not long until the Millennium Drop."
            melody @talking2mouth "Will you be ready?"

            if (HasEvent("Yellow", "AcceptPartner")):
                red @talking2mouth "I don't know. We're pretty busy with some other stuff, but Yellow and I are practicing our routine whenever we have a free moment. Which isn't often."

                melody @talking2mouth "You see it in Yellow, too?"

                red @talking2mouth "I think she can do anything she sets her mind to."

            elif (HasEvent("Klara", "AcceptPartner") and not HasEvent("Klara", "BrokeBond")):
                red @talking2mouth "I don't know. We're pretty busy with some other stuff, but Klara and I are practicing our routine whenever we have a free moment. Which isn't often."

                melody @talking2mouth "[ellipses]"
                melody @talking2mouth "You trust Klara?"

                red @talking2mouth "I {i}choose{/i} to trust."

                melody @talking2mouth "Not that easy."

                red @talking2mouth "It is for me."

            else:
                red @talking2mouth "I don't know. I'm pretty busy with some other stuff, but I'm practicing my routine whenever I have a free moment. Which isn't often."

        else:
            melody @talking2mouth "Why are you here? You're not a Coordinator."

            red @talking2mouth "I'm here to support Yellow. And seeing how Coordinators perform with their Pokémon can show me new ways to battle, anyway."

        pause 1.0

        melody @talking2mouth "'Kay."

        pause 1.0

        melody @bubblemouth "[ellipses]"
        melody @talking2mouth "Battle me again?"

        red @confused "Why?"

        melody @talking2mouth "Bored. Don't need to practice my routine. No-one else wants to talk to me."

        pause 0.5

        melody @talking2mouth "Know you like battles."

        menu:
            "Alright.":
                python:
                    trainer1 = MakeRed()
                    trainer2 = MakeTrainer("Melody")
                    customexpressions=["red frownmouth", "red frownmouth angrybrow", "melody on", "melody on"]

                call Battle([trainer1, trainer2], customexpressions=customexpressions) from _call_Battle_202
                $ RecordBattle("Melody2")

                show melody on bubblemouth with dis

                pause 1.0

                melody @talking2mouth "Still confused."

            "No.":
                pause 1.0

                melody sadbrow @bubblemouth "[ellipses]"
                melody @talking2mouth "Fine."

                show melody:
                    xpos 0.5 
                    ease 0.5 xpos 0.9

                pause 0.3

                red @talking2mouth "Wait. Tell me where you got that Foreveral. I {i}need{/i} to know."

                show melody:
                    ease 0.5 xpos 0.5

                red @closedbrow sweat talking2mouth "You're confused about--something, right? Something about this year? Why our Pokémon are so strong?"
        
        red @talking2mouth "I'll answer your questions if you tell me where you got that Foreveral from."

        melody @talking2mouth "You can't."

        pause 1.0

        melody sadbrow @talking2mouth "And I can't."

        hide melody with dis   

        pause 2.0

        $ coordinatingknowledge += 20

        narrator "[bluecolor]Your {/color}[contestcolor]Coordinating Knowledge{/color}[bluecolor] increased by 20 from watching the rest of the club meeting!{/color}"

        return True

label Contest3:
    stop music fadeout 1.5
    queue music "audio/music/lawrencetheme_start.ogg" noloop
    queue music "audio/music/lawrencetheme_loop.ogg"

    if (not HasEvent("Game", "Contest3")):
        $ AddEvent("Game", "Contest3")

        if (HasEvent("Yellow", "AcceptPartner")):
            narrator "As soon as you walk through the front doors of the the Contest Hall, you see Yellow, who grimaces at you, but falls in next to you, nevertheless."

            yellow @sadbrow talking2mouth "I already checked[ellipses] Phobos is here."

            red @closedbrow talking2mouth "[ellipses]Great."

            yellow @sad2brow talking2mouth "I {i}really{/i} try to see the best in everyone, but[ellipses]"

            pause 1.0

            yellow @sadbrow talkingmouth "I might need a new prescription for this one."

            red @sad2brow talkingmouth "Nice one."

            yellow @closedbrow talking2mouth "That's the meanest thing I've said since 1995."

            pause 0.5 

            red @talking2mouth "Oh, yeah? What did you say then?"

            yellow @talking2mouth "I told Blue he was a butthead."

            red @talking2mouth "Brutal. No wonder he turned out the way he did."

            yellow @happymouth happybrow blush "Heehee[ellipses]"

            narrator "You and Yellow walk into the Contest Coliseum's main area, already pre-cringing with anticipation at what might be waiting."

        elif (HasEvent("Klara", "AcceptPartner") and not HasEvent("Klara", "BrokeBond")):
            narrator "As soon as you walk through the front doors of the the Contest Hall, you see Klara, whose head snaps up at the sound of your footsteps."

            klara makeup hairpin neutralcoat @angrybrow talking2mouth "Phobos is still here. You don't need to be here."

            red @sadbrow talkingmouth "I need to watch your performances if I'm going to complement them, right? We won't get those scholarships if I have no idea what you're doing."

            pause 0.5

            klara @restrainedbrow talking2mouth "{i}Fine{/i}. Just[ellipses] don't draw so much attention this time."

            redmind @thonk "[ellipses]?"

            narrator "Klara struts on ahead, refusing to look at you, and you follow behind." 
            
        narrator "Unfortunately, you both get advanced warning of what you're walking into, in the form of shouting, that carries quite a ways[ellipses]"

        scene concerthallstage
        show serena contest angrybrow frownmouth:
            xpos 0.25
        show misty contest angrybrow frownmouth:
            xpos 0.5 xzoom -1
        show phobos:
            xpos 0.75
        with vpunch

        phobos @talking2mouth "Now, now, now, girls. There's really no need to get your hair all in a knot over this. I was simply stating that there's really no reason for Bianca to be on the stage."

        serena @talking2mouth "She has every right to perform alongside us! So what if she does not sing? Neither does May!"

        misty @angrymouth "Singing is just {i}one{/i} type of contest performance! There are dancers, there are people who use props--Bianca's got better special effects than {i}any{/i} of us!"

        phobos @closedbrow talking2mouth "{size=30}Yes, well, May isn't really much of a threat, is she?{/size}"
        phobos @sadbrow talkingmouth "Honestly, truthfully, and moreover, nonfictionally, I am somewhat surprised by your reactions. Surely you can see how you really ought to be more {i}grateful?{/i}"
        phobos @happy "Why, every competitor I remove from contention increases your own odds."
        phobos @sad2eyes angryeyebrows talking2mouth "Perhaps, then, you can find it within yourself to, perhaps--and this is just a suggestion--{nw}"

        show misty surprisedbrow frownmouth 
        show serena surprisedbrow frownmouth 
        with dis

        extend @sad2eyes angryeyebrows talking2mouth "{i}shut up?{/i}"

        pause 1.5

        show misty angrybrow frownmouth 
        show serena angrybrow frownmouth 
        with dis

        pause 0.5

        phobos @sadbrow talkingmouth "Oh, pardon my brusque language. I'm just so terribly tired of ingratitudinity. I don't expect you to understand, but perhaps one day, when you have something of worth you wish to share with others, you will."

        serena @talking2mouth "We will not be {i}grateful{/i} for you depriving our friends and comrades of the joy of competition. This benefits no-one."

        phobos @sad2brow talking2mouth "Sorry, listening? Were you listening? Were you {i}not listening?{/i} It's been decided. I've already told Bianca that she will not participate in the Million Drop. Three hours ago, in fact."
        phobos @closedbrow talking2mouth "I think she understood me--she appeared suitably chastenedized, in any case."

        misty @talkingmouth "So, you told us this just to[ellipses]"

        phobos @talkingmouth closedbrow "Just to let you know what I'm doing for you, my dear girls."
        phobos @upeyes talkingmouth sadeyebrows "Seemed I misjudged your reactions, but, ah well. My intentions were good."

        pause 1.0

        red @shadow angrybrow talking2mouth "Alright, that's it."

        if (HasEvent("Yellow", "AcceptPartner")):
            narrator "You open your mouth to speak, when you suddenly feel a hand on your back. You look back, expecting to see Yellow, but see, instead[ellipses]"

        elif (HasEvent("Klara", "AcceptPartner")):
            narrator "You open your mouth to speak, when you suddenly feel a hand on your back. You look back, expecting to see Klara, but see, instead[ellipses]"

        else:
            narrator "You open your mouth to speak, when you suddenly feel a hand on your back. Startled, you look back, and see[ellipses]"

        melody on @talking2mouth "Wait."

        show phobos surprisedbrow frownmouth 
        show serena surprisedbrow frownmouth
        with dis

        misty @angrybrow talkingmouth "Lawrence, you are an {i}actual{/i} piece of shit."

        serena @talking2mouth "Misty!"

        misty @angrymouth "Fuck you."
        misty @angrymouth"{i}Fuck{/i} you, fuck your ridiculous manicured eyebrows, fuck your made-up words, fuck your nonexistent accomplishments, fuck your stupid floating chair, fuck your 'generosity,' and fuck any contest you ever appear in."
        misty @angrymouth "Contests are worse because you exist."

        pause 1.0

        phobos -surprisedbrow @unamusedeyebrows sad2eyes shadow talking2mouth "You may dismiss yourself."

        misty @talkingmouth "I will fucking not. Call security on me. That's the only way I'm moving one goddamn step."

        pause 1.0

        phobos @closedbrow talkingmouth "Ah[ellipses] the classic 'Kantonian Spirit' at work. Uneducated, uncultured, foul-mouthed, inebriated--more fond of rolling around in muck than anything resembling intelligent conversation."
        
        show serena angrybrow with dis
        
        phobos @sadbrow talkingmouth "As a fellow member of higher society, I apologize that you had to hear that, my dear Serena. But persons of our status must, occasionally, mingle with these sorts."
        phobos surprisedbrow frownmouth @closedbrow talkingmouth "I wager she considers watching a Rhyhorn race to be a 'fine night out on a town.' These provincial hicks are--"

        serena angrybrow @furybrow angrymouth "SHUT {i}UP{/i}, you shithead! Y'all acting like you know a damn ol' thing 'bout Kantonians?! Misty's from Cerulean, y'g'damn {i}maroon{/i}! Girl's {i}way{/i} less of a country girl than I am, y'damn nimrod!"

        pause 2.0

        phobos @closedbrow talking2mouth "I don't believe there's any need for either of you to continue your attempts in the Millennium Drop. Perhaps you can keep Bianca company, since you're supposedly so fond of her."

        show serena angrybrow angrymouth
        show misty angrybrow angrymouth 
        with dis

        TempCharacter("{color=#cb6e8b}Serena{/color} & {color=#eb6400}Misty{/color}") "{size=40}Fuck you.{/size}"

        show serena angrybrow frownmouth
        show misty angrybrow frownmouth 
        with dis

        phobos upeyes angryeyebrows talking2mouth "Clearly, the Battle Team's influence has spread even to my beloved Coordinator Club--I never would have been paid such unconscionairable disrespect before."

        hide phobos with dis

        pause 2.0

        misty smilemouth -angrybrow @happybrow talkingmouth "Honestly, telling billionaires to fuck off in real life is {i}way{/i} more satisfying than it is on the internet."

        serena -frownmouth -angrybrow @talkingmouth happybrow "Yes, we did have a rather delightful little moment there."

        misty @talkingmouth "You ever been involved in a protest before? I'm meeting up with some people to picket a shipping company in the harbor on Saturday. Want to scream at polluters?"

        serena @sadbrow talkingmouth "Well[ellipses] I suppose my preparations for the Millennium Drop have just been rather abruptly cancelled. So, yes, I suppose I'm free."

        misty @talking2mouth "Cool."

        hide misty 
        hide serena
        with dis

        pause 1.0

        if (HasEvent("Yellow", "AcceptPartner")):
            show yellow frownmouth with dis:
                xpos 0.66

            show melody on with dis:
                xpos 0.33

            pause 1.0

            melody @talking2mouth "Scootch, blondie. I want to talk to [first_name]."

            yellow @talking2mouth "Um[ellipses] [first_name]?"

            red @talking2mouth "It's fine. I'll meet up with you after."

            yellow @talking2mouth "Alright."

            hide yellow with dis

            narrator "Yellow leaves, but casts a worried look behind her as she does so, as though afraid Melody would swallow you whole while her back is turned."

            show melody:
                xpos 0.33
                ease 0.5 xpos 0.5

        elif (HasEvent("Klara", "AcceptPartner")):
            show klara hairpin makeup neutralcoat angrybrow frownmouth with dis:
                xpos 0.66

            show melody on with dis:
                xpos 0.33

            klara @talking2mouth "What do {i}you{/i} want?"

            melody @bubblemouth "[ellipses]"
            melody @talking2mouth "Mostly to see how this plays out."

            pause 1.0

            melody @talking2mouth "He surprised you, didn't he?"

            klara @talking2mouth "I don't know what you're talking about."
            
            melody @surprisedbrow talking2mouth "Nah. Surprised me, too. I get it."

            klara @angrybrow angrymouth "I {i}don't{/i} know what you're talking about!"
            klara @angrybrow angrymouth "And don't pretend you're any better than me--sure, you've got an impressive resume, but has anyone even heard you sing a single note? All we have is Liz's word."
            klara @wrathbrow angrymouth "Contests are about {i}charming{/i} people, and you're as charming as a Muk. I bet you didn't actually win any of those trophies or awards you {i}say{/i} you won!"

            melody @talking2mouth "Contests are about skill and originality, and you're as original as a Ditto." 
            melody @sadbrow talkingmouth "{i}Everything{/i} you do is a worse imitation of someone else."

            klara @talking2mouth "Oh, sure! I know what kind of {i}skill{/i} you have. I didn't think Liz swung that way, but that's the only thing that makes sense, after she let {i}you{/i} in."

            melody @talking2mouth "Projection."

            klara @talking2mouth "Come off it. You can barely string three words together, and we're supposed to believe you {i}convinced{/i} Liz to let you join the Coordinator Club? Liar."

            melody @bubblemouth "[ellipses]"
            melody @talking2mouth "If you'd heard that voicemail, you'd be convinced, too. But you'll {i}never{/i} hear it."
            melody @closedbrow talking2mouth "And if you could do what I can[ellipses] you'd leave the same message."

            klara @wrathbrow wrathmouth "I'm done talking with you! [first_name], just keep your eyes on me!"

            hide klara with dis

            narrator "Klara storms off toward the stage, without a look behind."

            melody @bubblemouth "[ellipses]"

            show melody:
                xpos 0.33
                ease 0.5 xpos 0.5

        else:
            show melody on with dis

        red @sad2eyes angryeyebrows talking2mouth "Why'd you stop me?"

        melody @talking2mouth "He doesn't think you're a threat. If you keep your head down, you can still participate in the Millennium Drop."

        red @talking2mouth "I {i}don't{/i} keep my head down."

        melody @bubblemouth "[ellipses]"

        melody @talking2mouth "Fine. I delayed you for thirty seconds."
        melody @talking2mouth "You can still do something stupid and heroic. He's right over there. I won't stop you again."

        pause 0.5

        red @upeyes angryeyebrows talking2mouth "Why are you working with him?"

        pause 1.0

        melody @talking2mouth "I thought we hated the same things."

        pause 0.5

        red @talking2mouth "'Thought.' Past tense?"

        melody @sadbrow talking2mouth "Past tense."

        red @talking2mouth "What do you hate?"

        melody @talking2mouth "This school. Contests. Coordinating. Singing. The sound of waves."

        red @talking2mouth "That's a list of stuff you used to love, isn't it?"

        melody @talking2mouth "Does it matter? I hate it now."
        melody @talking2mouth "Hating it is safer than loving it was."

        pause 1.0

        red @talking2mouth "Coordinators don't perform because it's safe."

        melody @talking2mouth "You think you know anything about Coordinating?"
        
        if (IsCoordinator()):
            melody @closedbrow talking2mouth "You've competed in {i}one{/i} contest."
        else:
            melody @closedbrow talking2mouth "You're not a Coordinator. You've never even competed."

        red @talking2mouth "I don't know Coordinating, I guess. But I know people. And I knew a person who hated what she did--and hated what she didn't do."

        melody @bubblemouth "[ellipses]"

        red @talkingmouth sadbrow "Her name was Dawn. And I ended up breaking her out of that cage she made for herself. It was really public. There was a lot of shouting involved, and a bunch of colorful lights."
        red @sadbrow happymouth "If that's where this is headed, and you like your privacy, we could try to handle it privately?"

        pause 1.0

        melody @talking2mouth "You think {i}I{/i} made this cage?"
        melody @sadbrow talkingmouth "You really {i}don't{/i} know anything, [melody_name]."

        hide melody with dis   

        pause 2.0

        $ coordinatingknowledge += 20

        narrator "[bluecolor]Your {/color}[contestcolor]Coordinating Knowledge{/color}[bluecolor] increased by 20 from watching the rest of the club meeting!{/color}"

        return True

return False