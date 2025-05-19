
label prologue:
    stop music

    scene blank2
    $ RealignTextbox()

    TempCharacter("DISCLAIMER") "This game is a fanwork with no connection to any official Pokémon product." 
    TempCharacter("CONTENT WARNING") "The story contains elements of mature topics such as abuse, assault, murder, and crippling poverty. Adults, children, and animals may suffer the aforementioned. This game contains flashing lights and loud sounds." 
    TempCharacter("DISCLAIMER") "This game is not to be played by individuals underneath the age of majority of their home country. Regardless of age, player discretion is advised."

    menu: 
        ">I understand":
            narrator "Lovely. Enjoy, then."

        ">I am not old enough to play this game":
            narrator "Very well. I hope you return when you are older."

            $ MainMenu(confirm=False)()

    play music "audio/music/Dreams and Adventures.ogg"
    
    show pallet with dis:
        alpha 0.75
        
    show blank with dis:
        alpha 0.85
    
    pause 2.0

    show oak with dis

    oak @talkingmouth "Hello there!{w=0.5} Welcome to the world of Pokémon!"
    oak @happy "My name is Oak. People call me the Pokémon Professor!"
    oak @talkingmouth "This world is inhabited by creatures called Pokémon!{w=0.5} For some people, Pokémon are pets. Others use them for battling."
    oak @closedbrow talkingmouth "As for myself... I study Pokémon as a profession."
    oak @happy "But first, tell me a little about yourself."
    red "[ellipses]"
    oak @confusedbrow talkingmouth "Let's begin with your name.{w=0.5} What is it?"

    label firstname:
        $ first_name = renpy.input("{color=#e70000}What's your FIRST name? (Press Enter for the default){/color}", length=12, exclude="{}[[]%<>",)
        $ first_name = first_name.strip()

        if first_name == "":
            $ first_name = "Red"

        oak @talkingmouth "Right! So your first name is [first_name]."

        menu:
            "That's me.":
                red @happy "That's me."
                pass

            "I stuttered.":
                red @sadeyes sadeyebrows talkingmouth "I stuttered."
                oak @surprised "Oh? Then, what {i}is{/i} your first name?"
                jump firstname

    oak @talkingmouth "Well, then, what's your last name?"

    label lastname:
        $ last_name = renpy.input("{color=#e70000}What's your LAST name? (Press Enter for the default){/color}", length=20, exclude="{}[[]%<>",)
        $ last_name = last_name.strip()

        if last_name == "":
            $ last_name = "Sugimori"

        oak @happy "Right! So your last name is [last_name]."

        menu:
            "Sure is.":
                red @happy "Sure is."
                pass

            "Let me try that again.":
                red @sadeyes sadeyebrows talkingmouth "Let me try that again."
                oak @surprised "Eh? Alright, then."
                jump lastname

    oak @happy "Right! So your name is [first_name] [last_name]."
    oak @surprised sweat "Ah! I remember now. {w=0.5}{nw}" 
    extend @happy sweat "You're the trainer of this Pikachu."

    $ renpy.music.play("Audio/Pokemon/pikachu_norm1.ogg", channel="altcry")

    pikachu neutral_2 "Pi-KA-chu!"

    oak @happy "He's quite fond of you.{w=0.5}{nw}"
    oak @sadeyes sadeyebrows talkingmouth "He's quite fond of you.{fast} Erm, what was his name again?"

    label pikaname:
        $ pika_name = renpy.input("{color=#e70000}What is your Pikachu's nickname?{/color}", length=12, exclude="{}[[]%<>",)
        $ pika_name = pika_name.strip()
        
        if pika_name == "" or pika_name == "pikachu":
            $ pika_name = "Pikachu"

        oak @talkingmouth "You named him [pika_name]?"

        menu:
            "The one and only.":
                red @happybrow talkingmouth "The one and only."
                pass

            "What kind of name is that?":
                red @angrybrow talking2mouth "What kind of name is that?"
                oak @surprised "Eh? Okay, what did you {i}actually{/i} name him, then?"
                jump pikaname

    oak @happy "That's right! I remember now!{w=0.5} His name is [pika_name]!"

    oak @talkingmouth "Now, one more thing. This is a story about many young adults your age. And your age group, well..."
    oak @sadbrow talkingmouth sweat "To be more direct, people will swear. However, you may choose that to be censored."
    oak @closedbrow talkingmouth "You can change this any time you want, incidentally, in the pause menu you access by right-clicking."

    oak @talkingmouth "In any case, would you like expletives to be censored in this story for now? {color=#ff0000}(This feature is not {i}100%%{/i} functional.){/color}"

    menu:
        "**** no.":
            $ profanity = True
            red @angry "Fuck no."

        "Yes, please.":
            red @sadbrow happymouth "Yes, please."

    oak @happy "Very well."
    
    oak @talkingmouth "[first_name]!{w=0.5} Your very own Pokémon legend is about to unfold!"

    oak @angrybrow talkingmouth "A world of dreams and adventures with Pokémon awaits!"
    oak happy "Now it's time to wake up! Wake up!"

    hide oak with dis

    stop music fadeout 2.5
        
    show blank:
        alpha 0.85
        ease 2.0 alpha 1.0
        
    oak "Pikachuuuu~!"
    
    show pallet:
        alpha 0.75
        pause 2.5
        ease 2.5 alpha 1.0
    
    $ renpy.pause(2.5, hard=True)

    hide blank    
    show pallet with vpunch:
        alpha 1.0
    $ PlaySound("Body Roll.ogg")
    
    red casual hatless @surprised "GAH!"

    $ renpy.music.queue("Audio/Music/Pallet Town A.ogg", channel='music', loop=True, fadein=1.0, tight=None)
    $ renpy.pause(1.25, hard=True)

    hide oak
    hide blank2
    hide blank
    
    red sadeyebrows closedeyes talking2mouth "{cps=*0.1}Unghh..."

    red angrybrow happymouth "Phew! Almost slept in!"

    pause 1.5
    
    $ renpy.music.play("Audio/Pokemon/pikachu_question.ogg", channel="altcry", loop=None)
    pikachu neutral_4 "Pi-ka?"

    red -sadeyebrows -closedeyes -talking2mouth "What's up, [pika_name]?"

    $ renpy.music.play("Audio/Pokemon/pikachu_norm2.ogg", channel="altcry", loop=None)
    pikachu neutral_2b "Piiii-ka!"

    red -angrybrow -happymouth @happy "Time to rise and shine!"

    $ renpy.music.play("Audio/Pokemon/pikachu_sad.ogg", channel="altcry", loop=None)
    pikachu bashful "Piiii{w=0.5}{nw}"
    extend bashful_2 "kaaaa."

    red talkingmouth "Hey, that's a good thing, buddy! A future Champion's Pokémon {i}should{/i} get up early in the morning, and go to bed late!"

    red talking2mouth angrybrow "Like they say; Late to bed and early to rise makes you... {w=0.5}uh...{w=0.5} {nw}"
    red -angrybrow happy "Like they say; Late to bed and early to rise makes you... uh...{fast} tired! All the time!"

    $ renpy.music.play("Audio/Pokemon/pikachu_excite4.ogg", channel="altcry", loop=None)
    pikachu neutral_2b "Piii-kaaaa!"

    show mom:
        xpos 1.5

    mom "Did I just hear my darling baby say the word 'tired'?"

    show mom at moveinleft

    pause 1.0

    red frownmouth angryeyes confusedeyebrows @talking2mouth "Oh, hey, Mom! Welcome to my bedroom. Yes, please, come in, make yourself at home!"

    mom @angry "As long as you're living under my roof, I certainly will!"

    red closedeyes -confusedeyebrows happymouth "...Fair."

    mom @happymouth "Anyway, I heard you said the word 'tired!' I didn't know you even knew that word, sweetie!"

    red surprised "Mom! What are you saying?"

    mom @happy "...Well, when you have more energy than your Pikachu, a mother can sometimes be led to think her son doesn't sleep!"

    red -surprisedbrow -frownmouth -surprised @happy sweat "Hey, there's no time to sleep if I want to be a Champion some day."

    mom sadeyebrows sadeyes @talkingmouth "I wonder if [pika_name] agrees with you?"

    pause 1.0

    $ renpy.music.play("Audio/Pokemon/pikachu_sad.ogg", channel="altcry", loop=None)

    pikachu yawn "{cps=*0.1}Pikaaaaaa..."

    pause 1.0

    red @closedeyes talking2mouth "...Well, when I'm Champion, I'll have more Pokémon than just [pika_name]."
    red @angrybrow happymouth "Anyway! We're burning daylight! Come on, [pika_name], let's go for a run before the sun gets too high!"

    mom @surprised "Wait! God, slow down for half a second, won't you?! I have some really, really big news!"

    red -angrybrow -happymouth @talkingmouth "I'm putting on my running shoes right now, but go ahead."

    mom sadeyes sadeyebrows @talkingmouth "...Wouldn't you like to guess?"

    menu:
        "You're going to start charging me rent?":
            show mom -sadeyes -sadeyebrows with dis

            red happy "You're going to start charging me rent?"

            mom @sadeyes sadeyebrows happymouth "Aw, sweetheart, I wouldn't dream of it. You'll always be welcome home, sweetie."

            red -happy @talkingmouth "Oh, I know that, Mom. But, really, I wouldn't mind working to contribute to the household as well."
            
            red @closedeyes sadeyebrows talking2mouth "{size=30}Or at least get a bigger bed...{/size}"
            
            mom @talkingmouth "Sweetheart, you don't need to think about something like that yet. You just graduated high school! You've got plenty of time to work. You should be enjoying your young years."
            
            mom @happy "Besides, this news is going to interfere with any working plans you might have had!"
           
            red @confused "Huh?"

            show mom happy:
                zoom 1.0 ypos 1.0
                ease 0.75 zoom 1.25 ypos 1.25
            
            pause 0.75
            
            mom "Oh, my darling baby boy... I'm so proud...!"

            red @closedeyes lightblush talking2mouth "Pinching my cheeks, Mom? I'm eighteen, you know..."

            show mom -happy sadeyes sadeyebrows:
                zoom 1.25 ypos 1.25
                ease 0.75 zoom 1.0 ypos 1.0
            
            mom @sadbrow talkingmouth "Oh, I know... and it happened far too soon for my heart."
            
            mom @happy "But enough about my happiest memories.{w=0.5} You got into Kobukan Academy!"
            
        "Is it another Skitty video?":
            show mom surprisedbrow frownmouth with dis

            red @playfulbrow sweat talkingmouth "Is it another Skitty video?"

            mom angrybrow frownmouth -surprisedbrow -frownmouth -surprised @surprised "What?{w=0.25} No!{w=0.5} [first_name], this is a much bigger deal than that!"
            
            red -angrybrow happymouth "So what, is it a Lillipup?"
            
            mom @angry "You've got some nerve!{w=0.5} I don't remember raising such a lippy son!"
                      
            mom -angrybrow -frownmouth @happy "But no, that's not it, either. Sweetheart, you got accepted into Kobukan Academy!"
        
        "I'm going for my run.":
            show mom -sadeyes -sadeyebrows with dis

            red @sadeyebrows closedeyes talkingmouth sweat "Hey, it's Friday.{w=0.5} If you don't mind, I'll be taking advantage of my day off and-"
            
            mom @happy "Nice try, honey."

            show mom happy:
                zoom 1.0 ypos 1.0
                ease 0.75 zoom 1.25 ypos 1.25
            
            pause 0.75
            
            mom "Oh, my darling baby boy... I'm so proud...!"

            red @closedeyes lightblush talking2mouth "Pinching my cheeks, Mom? I'm eighteen, you know..."

            show mom -happy sadeyes sadeyebrows:
                zoom 1.25 ypos 1.25
                ease 0.75 zoom 1.0 ypos 1.0
            
            mom @sadbrow talkingmouth "Oh, I know... and it happened far too soon for my heart."
            
            mom @happy "But enough about my happiest memories.{w=0.5} You got into Kobukan Academy!"

    stop music fadeout 2.0    

    pause 2.0

    red angrybrow sadmouth "...No, I didn't."

    $ renpy.music.queue("Audio/Music/Littleroot_Start.ogg", channel='music', loop=False, fadein=1.0, tight=None)
    $ renpy.music.queue("Audio/Music/Littleroot_Loop.ogg", channel='music', loop=True, fadein=0.0, tight=None)

    mom sadeyebrows frownmouth @surprised "...What?"

    red -angrybrow closedeyes sadeyebrows "I couldn't have, Mom. The application fee alone was $10,000."

    red sadeyes "Besides, my grades are in the bottom tenth percentile for Kobukan. And my extracurriculars are nonexistent. What's there to do in Pallet Town besides hang out with Sam?"

    red @talkingmouth "...I couldn't even apply, Mom. I wrote three letters to them asking for a fee waiver. I only got a response on my third letter, and they just said to stop pestering them."

    mom @angry "Sweetheart! We could have afforded the application fee!"

    red sad "Not for my odds. I used one of those online calculators, you know? They said my chance of getting in was too low to be computed."

    red sadeyebrows closedeyes happymouth "Which has to be some kind of record, at least."

    mom @sad "Oh... sweetheart, I'm sorry. I know that getting into Kobukan was always a dream of yours."

    red happy "Hey, that was just the most direct path to becoming Champion. I'll figure out another!"

    pause 1.0

    stop music fadeout 1.0

    red confused "Er... why did you think I got into Kobukan, though?"

    $ renpy.music.queue("Audio/Music/Pallet Town A.ogg", channel='music', loop=True, fadein=1.0, tight=None)

    mom happy "Oh, it's just because we received a letter that says 'Kobukan Academy Acceptance Letter' on the envelope."

    red -confused closedeyes talking2mouth "Huh. That's very misleading.{w=1.0}{nw}"
    red neutraleyes talking2mouth "Huh. That's very misleading. {fast}Can I see it?"

    mom -happy @talkingmouth "Sure thing, sweetie."

    show letter at itemhover

    show mom:
        xcenter 0.5
        ease 1.0 xcenter 0.75
    
    $ PlaySound("item_get.ogg")

    red @confused "Oh, yeah, it says it right there.{w=0.5} Huh.{w=0.5} That's...{w=0.5} weird."
    red @sad2eyes angryeyebrows talking2mouth "Oh, I bet I know what happened. This was probably meant to go to {i}him{/i}, wasn't it?"

    mom sadeyes sadeyebrows @talkingmouth "Maybe. But perhaps you should just read it?"

    red happy "I'm not going to read his mail, Mom. That's, like, a major crime."

    mom @angry "Well, I've already read it. And you don't want me to go to prison alone, do you?"

    red closedeyes @talkingmouth "And that's how the [last_name] crime family got started..."

    show letter at itemhide
    show mom:
        ease 1.0 xcenter 0.5

    red -happy -closedeyes @talkingmouth "Alright, let's see what this thing says."

    red @thinking "[ellipses]"
    show mom -sadeyebrows -sadeyes with dis

    show red:
        xpos -0.5

    show image "CG/Acceptance Letter.webp" with Dissolve(2.0)

    red @surprisedeyes frownmouth "[ellipses]"

    show mom happyeyes happyeyebrows with dis

    red @surprisedeyes frownmouth "[ellipses]"

    show mom happy with dis

    red @surprised "[ellipses]"

    pause 1.0

    red @surprised "Oh my god, Mom."

    mom @talkingmouth "Well, sweetheart? Was this, perhaps, a letter meant for our charming neighbor?"

    mom @playfulbrow talkingmouth blush "Or was it, as I said, proof that good things happen to good people?"

    red @surprisedeyes confusedeyebrows talking2mouth "...How?"

    mom @closedbrow talking2mouth "I...{w=0.5} really don't know, actually. I never doubted that you'd get in, but if you didn't even apply, I'm not sure if my motherly belief was {i}that{/i} powerful."

    red @surprised "[ellipses]"

    $ renpy.music.play("Audio/Pokemon/pikachu_confused.ogg", channel="altcry", loop=None)
    pikachu neutral_4 "Piiika?"

    red @surprised "...I have no idea, [pika_name]. I just have no idea."

    show mom happybrow neutralmouth
    hide image "CG/Acceptance Letter.webp"
    hide red
    with Dissolve(1.0)

    pause 1.0

    red hatless casual @happy "But I'm not going to lead this gift horse to water!"

    mom sadeyes sadeyebrows @talkingmouth "I don't think that's {i}exactly{/i} how the phrase goes..."

    stop music fadeout 2.0
    show blank2 with splitfade
    
    $ renpy.pause(2.0, hard=True)
    
    hide pallet
    hide mom
    
    $ renpy.music.queue("Audio/Music/ViridianB_Start.ogg", channel='music', loop=None, fadein=1.0, tight=None)
    $ renpy.music.queue("Audio/Music/ViridianB_Loop.ogg", channel='music', loop=True, tight=None)
    
    $ renpy.music.play("Audio/bigcrowdloop.ogg", channel='crowd', loop=True, fadein=0.5)
    
    scene airport behind blank2:
        xalign 1.0 yalign 1.0
    hide blank2 with splitfade
    
    pause 1.0

    redmind angrybrow frownmouth "The Kanto Airfield terminal in Viridian City...{w=0.5} and a one-way ticket to the Kobukan region."
    red -angrybrow closedeyes @talkingmouth sweat"I can't believe it's been an entire month, and we still have absolutely no idea how I got into Kobukan."
    red -closedeyes @confused "We definitely emailed the school {i}several{/i} times to make sure this wasn't a mistake, right?"
    
    show mom with dis

    mom @talkingmouth "Of course, sweetie. Both of us did."

    red @closedbrow talking2mouth "So there's two big questions, now. {w=0.5}How did I get in? {w=0.5}{nw}"
    extend @closedbrow sweat talkingmouth "And how are we going to pay for this?"
    
    mom @angry "That should be the last thing you're worrying about, sweetheart. {w=0.5}{nw}"
    extend @happy "We'll figure something out, don't worry!"

    red @thinking "[ellipses]"
    red @sadeyes sadeyebrows talkingmouth "I believe you, Mom.{w=0.5} We'll figure something out."
    red @happy "And, hey, worst-case scenario, I get six months of free tuition before they realize we can't pay, kick me out, and sue us for the tuition!"
    mom @angryeyes angryeyebrows happymouth blush "Don't even joke about that!"
    
    pause 2.0

    mom @sadeyebrows sadeyes talkingmouth "This is as far as I can take you, [first_name]."
    
    red @talkingmouth "I'm eighteen. I'll be fine."
    
    mom @happy "I know you will."
    mom @sadbrow talkingmouth "A goodbye hug from my beloved Champion?"
    
    red @sad2eyes sadeyebrows lightblush talkingmouth "Man... I'm going to have to work really hard to not let all the people at Kobukan realize that I'm such a huge mama's boy."

    show mom happyeyes sadeyebrows -happymouth blush:
        zoom 1.0 ypos 1.0
        ease 0.75 zoom 1.25 ypos 1.25
    
    pause 2.5

    show mom -happy -blush:
        zoom 1.25 ypos 1.25
        ease 0.75 zoom 1.0 ypos 1.0
    
    red @talkingmouth sadbrow "I love you, Mom."
    mom tears sadbrow @talkingmouth "I love you too, sweetheart."
    
    $ renpy.music.play("Audio/Pokemon/pikachu_sad.ogg", channel="altcry", loop=None)
    pikachu sad_2 "Piiiikaaaa."

    mom sadeyes sadeyebrows @talkingmouth "Looks like [pika_name] loves you as well."
    
    red @happy "Hey, buddy, don't look so sad!{w=0.5} I'll send for you as soon as I'm allowed to. I'm just not allowed to bring any of my personal Pokémon with me right away."
    red @talkingmouth "Keep Mom company for me in the meantime, will ya? Here, I'll give you one of [first_name]'s famous headpats to tide you over 'til then."
    
    $ renpy.music.play("Audio/Pokemon/pikachu_sad2.ogg", channel="altcry", loop=None)
    pikachu @sad "Pika... piiiikaaaa."
    
    show mom -sadeyebrows -sad -talkingmouth with dis

    red @talkingmouth "I'm off, Mom."
    
    mom @talkingmouth "Have a safe trip!{w=0.5} Take care now!"

    show mom surprised:
        xpos 0.5
        ease 7.0 xpos 1.2
        
    show airport:
        xalign 1.0 yalign 1.0
        ease 8.0 xalign 0.0
        
    mom "Oh! And make sure you do your laundry!{w=0.5} And go to bed {gradualsize=34-16}earlier so you don't end up falling asleep so much! And eat full meals, not just energy bars...!{/gradualsize}"

    pause 1.0

    redmind sadeyes sadeyebrows "Poor mom. She's already got empty-nest syndrome."

    pause 1.0

    redmind sad "Oh man, [pika_name] looks real sad. He'll just have to be strong until I can get him sent to the academy."

    stop music fadeout 2.0
    pause 2.5
    
    show airport:
        xalign 0.0 yalign 1.0
        ease 4.0 xalign 1.0

    show mom -surprisedbrow -frownmouth -surprised:
        xpos 1.2
        ease 4.0 xpos 0.5
    
    $ renpy.pause(4.5, hard=True)
    
    show airport:
        xalign 1.0
    
    $ renpy.music.play("Audio/Pokemon/pikachu_sad2.ogg", channel="altcry", loop=None)
    pikachu sad_2 "Pika... piiiikaaaa."
        
    mom -tears @talkingmouth "Oh, don't worry [pika_name], you'll be with him before you know it! {w=0.5}{nw}"
    extend angryeyes angryeyebrows @talkingmouth "Though it'd be a lot easier to put you on the plane if you'd just stay in your ball..."
    
    $ renpy.music.play("Audio/Pokemon/pikachu_sad.ogg", channel="altcry", loop=None)
    pikachu sad "Piiiikaaaa."

    mom -angryeyes -angryeyebrows -talkingmouth @happy "Oh, I know how you feel, I really do.{w=0.5} But it's best not to dwell on these sorts of things."
    mom happyeyes talkingmouth -tears @talkingmouth "All boys leave home some day. It said so on TV!"
    mom -happyeyes @talkingmouth "Let's go home."

    hide mom with dis
    
    $ PlaySound("plane_chime.ogg")
    
    TempCharacter("PA Voice") "This is the pre-boarding announcement for the 7:45 a.m. flight to Inspira City. Takeoff will begin in 45 minutes."
    TempCharacter("PA Voice") "We are now requesting passengers with small children and Pokémon to begin boarding at this time. Regular boarding will begin in fifteen minutes. Thank you."
    
    pikachu neutral_3 "[ellipses]"
    
    $ renpy.music.play("Audio/Pokemon/pikachu_angry1.ogg", channel="altcry", loop=None)
    pikachu angry_2 "Pi-ka!"
    $ renpy.music.stop(channel='crowd', fadeout=1.0)
    
    $ renpy.music.queue("Audio/Music/SoaringDreams_Start.ogg", channel='music', loop=None, fadein=1.0, tight=None)
    $ renpy.music.queue("Audio/Music/SoaringDreams_Loop.ogg", channel='music', loop=True, tight=None)
    
    hide mom
    
    show sky:
        alpha 0.0 yalign 1.0 xalign 0.2 zoom 1.25
        parallel:
            ease 1.0 alpha 1.0
        parallel:
            ease 30.0 xalign 1.0
    
    show clouds1 as base1:
        xpos -200 ypos 100 alpha 0.0
        block:
            parallel:
                linear 0.5 alpha 1.0
            parallel:
                linear 12.0 xpos 2000
            parallel:
                pause 11.0
                linear 1.0 alpha 0.0
    show clouds2 as base2:
        xpos -800 ypos 400 alpha 0.0
        block:
            parallel:
                linear 0.5 alpha 1.0
            parallel:
                linear 8.0 xpos 1000
            parallel:
                pause 7.0
                linear 1.0 alpha 0.0
    show clouds3 as base3:
        xpos -400 ypos 0 alpha 0.0
        block:
            parallel:
                linear 0.5 alpha 1.0
            parallel:
                linear 10.0 xpos 2200
            parallel:
                pause 9.0
                linear 1.0 alpha 0.0
    
    show clouds1 as set1:
        xpos -1800 ypos 100 alpha 0.0
        block:
            parallel:
                linear 0.5 alpha 1.0
            parallel:
                linear 15.0 xpos 1800
            parallel:
                pause 14.0
                linear 1.0 alpha 0.0
                pause 1.0
                xpos -1500
            repeat
    show clouds2 as set2:
        xpos -1700 ypos 100 alpha 0.0
        block:
            parallel:
                linear 0.5 alpha 1.0
            parallel:
                linear 12.0 xpos 2200
            parallel:
                pause 11.0
                linear 1.0 alpha 0.0
                pause 1.0
                xpos -1400
            repeat
    show clouds3 as set3:
        xpos -2100 ypos 0 alpha 0.0
        block:
            parallel:
                linear 0.5 alpha 1.0
            parallel:
                linear 17.0 xpos 2200
            parallel:
                pause 16.0
                linear 1.0 alpha 0.0
                pause 1.0
                xpos -1800
            repeat
    show clouds1 as set4:
        xpos -1700 ypos -100 alpha 0.0
        pause 5.0
        block:
            parallel:
                linear 0.5 alpha 1.0
            parallel:
                linear 6.0 xpos 1800
            parallel:
                pause 5.0
                linear 1.0 alpha 0.0
                pause 1.0
                xpos -1400
            repeat
    show clouds2 as set5:
        xpos -1900 ypos 500 alpha 0.0
        pause 6.0
        block:
            parallel:
                linear 0.5 alpha 1.0
            parallel:
                linear 8.0 xpos 2200
            parallel:
                pause 7.0
                linear 1.0 alpha 0.0
                pause 1.0
                xpos -1700
            repeat
    show clouds3 as set6:
        xpos -2100 ypos -50 alpha 0.0
        pause 5.0
        block:
            parallel:
                linear 0.5 alpha 1.0
            parallel:
                linear 20.0 xpos 2200
            parallel:
                pause 19.0
                linear 1.0 alpha 0.0
                pause 1.0
                xpos -1900
            repeat
    show clouds2 as set7:
        xpos -1900 ypos 200 alpha 0.0
        pause 4.0
        block:
            parallel:
                linear 0.5 alpha 1.0
            parallel:
                linear 10.0 xpos 2200
            parallel:
                pause 9.0
                linear 1.0 alpha 0.0
                pause 1.0
                xpos -1700
            repeat
    
    $ renpy.pause(1.5, hard=True)
    
    hide airport
    
    redmind -sadeyebrows closedeyes frownmouth "Phew!"
    redmind "Do city folk really always use airplanes to go places?{w=0.5} This is nothing like flying on a Pokémon.{w=0.5}"
    redmind happymouth "...Not that I've done that yet, either."
    redmind -happymouth -closedeyes -frownmouth "Some of the older guys back in Pallet told me the Kobukan region is just next door to Unova... but pretty far away from Kanto."
    redmind confusedeyebrows frownmouth "If Kobukan is this far away, I can't imagine how far Kalos or Paldea are."
    redmind closedeyes frownmouth "...Ugh. I've been here for ten hours...{w=0.5}{nw}" 
    redmind surprised "...Ugh. I've been here for ten hours... {fast}wait!{w=0.5} What's that out the window?"

    $ PlaySound("plane_chime.ogg")

    "PA Voice" "{color=#e70000}Good afternoon, passengers. We are expecting to land in the Kobukan region in approximately twenty minutes. The weather in Inspira City is clear and sunny.{/color}" 
    "PA Voice" "{color=#e70000}As we start our descent, please make sure your seat belt is securely fastened, your tray table is in the locked and upright position, and all electronic devices are turned off. Thank you.{/color}"
    
    red happy "All right, this is it!{w=0.5} The beginning of the rest of my life!"
    
    show blank2 with Dissolve(1.0)
        
    $ PlaySound("Airplane.ogg")
    
    $ renpy.pause(2.0, hard=True)
    
    hide clouds1 as base1
    hide clouds2 as base2
    hide clouds3 as base3
    hide clouds1 as set1
    hide clouds2 as set2
    hide clouds3 as set3
    hide clouds1 as set4
    hide clouds2 as set5
    hide clouds3 as set6
    hide clouds2 as set7    
    
    stop music fadeout 2.0
    $ renpy.pause(2.5, hard=True)
    
    $ renpy.music.play("Audio/cityambience.ogg", channel='crowd', loop=True, fadein=1.5)
    
    $ renpy.pause(1.5, hard=True)
    
    scene city_A with Dissolve(2.0)
        
    $ renpy.pause(1.5, hard=True)
    
    hide sky
    hide blank2
    
    redmind closedeyes frownmouth "...Except I have no idea where I am, or which direction the school's in."
    redmind happymouth "If I remember correctly from my research, there should be a bus that leads there, right? The Red Line."
    redmind angrybrow frownmouth "The problem is...{w=0.5} I see the Scarlet Line, the Ruby Line, even the Pearl Line. Those are all red...{w=0.5} ish."
    red -angrybrow happy "Well, if I just pick a direction and start running, I'm bound to hit something that points me in the right direction!"

    show pallet at sepia
    show flashback
    with dis

    $ renpy.pause(1.0, hard=True)
    
    show mom angry at sepia, dissolvein behind flashback

    mom "For heaven's sake, slow down and think about your surroundings! If you're lost, just ask someone for directions!"

    show blank with splitfade

    hide mom
    hide pallet
    hide flashback
    hide blank with dis

    red @talkingmouth "Yeah, I suppose I could do that."

    pause 1.5

    red talkingmouth "Hey! Excuse me.{w=0.5} Do you know which bus goes to..."
    
    "{color=#3110dd}Familiar Voice" "\"Huh?\""

    show blue surprisedbrow frownmouth sweat with dis

    red surprised "Wha-"

    show blue -surprisedbrow -frownmouth -surprised closedbrow frownmouth with dis
    
    pause 1.0
    
    blue "[ellipses]"
    
    play music "Audio/Music/RivalTune.ogg" noloop
    blue -sweat -frownmouth @happymouth "...Son of a bitch."

    red -surprisedbrow -frownmouth -surprised angrybrow talking2mouth "...Blue."
    
    queue music "audio/music/Inspira_start.ogg" noloop
    queue music "audio/music/Inspira_loop.ogg"

    blue -happymouth -closedbrow @surprised "What the hell are {i}you{/i} doing here?"
    
    red @closedbrow talking2mouth "Is it too hard to believe I got into Kobukan Academy?"
    
    blue @happy "No, I can totally believe that! Just like I can believe that you're the Queen of Kalos, or that it says gullible on the ceiling!"
    
    red -angrybrow @confused "But we're outdoors...?"
    
    show blue surprisedbrow frownmouth with dis

    pause 1.5

    blue -surprisedbrow -frownmouth -surprised @happy "I almost wish you {i}had{/i} made it into Kobukan. I'll miss my favorite stooge when I'm taking my place among the future Champions of the world."
    
    red -surprisedeyes -surprisedeyebrows -frownmouth @playfulbrow talkingmouth "Then you'll be {i}really{/i} happy when you see me walking down the same hallways as you."
    
    blue -happy @surprised sweat "You...{w=0.5} almost sound serious."
    
    red @happy "There's two things I take seriously, Blue. My dream to be a Pokémon Champion, and my rivalry with you."
    
    blue -surprisedbrow -frownmouth -surprised -sweat @angry "Don't be so cocky! I don't take you seriously at all. You're a dreamer with no direction."
    blue -angry @closedbrow talkingmouth "I know exactly where I'm going, {i}and{/i} how I'm getting there."

    red -happy @frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."

    red @talkingmouth "Hey, Blue. Since I'm obviously not going to Kobukan Academy, and you are, there's no way that anyone at this new school will learn about your nickname, right?"

    blue frownmouth @angrybrow talkingmouth "Don't you dare."

    red @talking2mouth "That nickname that everyone called you? The one I came up with when I was, like, eight, and stuck with you all this time?"

    blue -frownmouth angry "I'm warning you!"

    red -talking2mouth @happy "Remind me what that was, again?"

    label bluename:
        $ blue_name = renpy.input("{color=#e70000}What was Blue's nickname? (Press Enter for the default.){/color}", length=12, exclude="{}[[]%<>",)
        $ blue_name = blue_name.strip()

        if blue_name == "" or blue_name == "blue" or blue_name == "Blue":
            $ blue_name = "Blueberry"

        red @happy "Oh, I think I'm close. Was it...{w=0.5} [blue_name]?"

        menu:
            "Yep, that was it.":
                red happyeyes talkingmouth "Yep, that was it."
                pass

            "Ooh, wait, here's an even better one.":
                red happyeyes talkingmouth "Ooh, wait, here's an even better one."
                jump bluename

    blue @angry "It doesn't make sense! It's not clever, or catchy, or... It was so stupid! Why did everyone call me that?!"

    red -happyeyes -happyeyebrows -talkingmouth @talkingmouth "I guess the humor is just a bit too highbrow for you, [blue_name]."

    blue @closedbrow happymouth "You wouldn't know 'highbrow' if it hit you with a shovel."
    blue @angry "You're a country hick who saw a Champion on TV one day and deluded yourself into thinking you had a chance! Now, I've got {i}way{/i} more important stuff to do than hang around with a clown like you, so I'm out of here."
    blue -angry @surprisedbrow happymouth "Smell ya later!"

    show blue:
        parallel:
            ease 0.5 alpha 0.0
        parallel:
            ease 0.75 xpos 1.3

    pause 1.5

    redmind @thonk "'Country hick?' We come from the same town..."
    
    show city_A:
        zoom 1.0 xalign 0.5 yalign 1.0
        block:
            ease 0.5 zoom 1.1 yalign 1.0 xalign 1.0
            pause 0.5
            ease 0.5 xalign 0.0
            pause 0.5
            ease 0.4 xalign 0.5
            
    redmind -surprisedbrow -frownmouth -surprised "Anyway, I need to find someone that can point me in the direction of the academy."
    redmind closedeyes frownmouth "Maybe someone I {i}don't{/i} know, this time..."
    
    show city_A:
        zoom 1.1 xalign 0.5 yalign 1.0
        ease 0.5 zoom 1.0
    
    pause 0.5
    
    show silver neutral with dis:
        xpos 1.3
        ease 1.0 xpos 0.5
    
    pause 2.0
    
    hide blue
    
    redmind @playfulbrow unamusedmouth "...Hm. I don't think I've ever seen a guy whose face says, more obviously, 'don't talk to me.'"
    redmind happy "Well, I can definitely find someone without such an aura of antisociality if I just-"

    silver @talkingmouth "Hey, red."

    red surprised "Huh? Me?"

    silver angrybrow @talking2mouth "What're you, dense? I'm lookin' {i}straight{/i} at you!"
    
    redmind @winkeyes sadeyebrows sweat frownmouth "Oh, shit, is this guy trying to pick a fight?" 
    redmind @thinking "...I don't have any Pokémon on me. I should probably just get out of here."

    red @sad2eyes talking2mouth "Uh... Okay. I think that's the end of this conversation."
    
    silver sad "W-wait! I, uh... I just meant to..."

    pause 1.5

    silver closedbrow "Forget it. Ignore me."

    redmind @confusedeyebrows frownmouth "Oh. Maybe he's just very awkward?"

    red @happy "Uh, maybe we got off on the wrong foot. Why don't you tell me what's up?"

    pause 1.5

    silver -closedbrow @sad "...Ugh. I just wanted to say, that... uh... I overheard your conversation..."

    red @talking2mouth angrybrow "Not a {i}strong{/i} start, but carry on."

    silver @closedbrow talkingmouth "And I figured that... well, if you really did get into Kobukan... and since you were looking around... you probably were trying to find your way there."

    red @happy "You're pretty perceptive!"

    silver @sadbrow happymouth "Thanks, it's a survival mechanism."
    silver @talkingmouth "Anyway, am I right? {w=0.5}I mean, are you trying to get to Kobukan?"

    red @talkingmouth "Yeah. If you could point me in the right direction, that'd be a big help."

    silver @closedbrow talkingmouth "Good. That's what I want. {w=0.5}{nw}"
    extend @surprisedbrow talkingmouth "To be helpful, I mean."

    pause 1.5

    red @talking2mouth "So-"

    silver @closedbrow talkingmouth "That way."

    red happy "Thanks! Is it running distance?"

    silver @surprisedbrow talkingmouth "I mean...{w=0.5} I wouldn't, but probably."

    red @happy "Cool. Seeya!"

    show silver:
        xpos 0.5
        ease 3.0 xpos 0.0
        
    show city_A:
        ease 3.0 zoom 2.0

    pause 3.0

    silver @surprised "Hey, wait!"

    show city_A:
        linear 1.0 zoom 1.0

    show silver:
        linear 1.0 xpos 0.5

    red @talkingmouth "Yeah? What's up?"

    silver @closedbrow talkingmouth "About earlier...{w=0.5} Sorry. It's, uh,{w=0.25} it's been a pretty rough day so far."
        
    red @confused "But it's barely past noon?"

    silver @surprisedbrow talkingmouth "Er..."
    
    red @happy "Hey, don't worry about it.{w=0.5} We all have those kinds of days."
    
    silver @closedbrow talkingmouth "Hmm... {w=0.5}{nw}"
    extend @happy "Oh, I know!"
    silver @happymouth "Here, take this."
    
    show ragecandy at itemhover

    show silver:
        xcenter 0.5
        ease 1.0 xcenter 0.75
    
    $ renpy.music.set_volume(0.25, delay=0.0, channel="music")
    $ PlaySound("item_get.ogg")
    $ renpy.music.set_volume(1.0, delay=2.0, channel="music")
    
    pause 2.0

    red surprised "A chocolate bar?"
        
    silver sadbrow @talkingmouth "It's a Rage Candy Bar.{w=0.5} ...Yeah. A chocolate bar. They're from Johto."
    
    red @talkingmouth "Huh."

    show ragecandy at itemhide

    show silver:
        xcenter 0.75
        ease 1.0 xcenter 0.5

    pause 1.0

    red happy "Well, my mother told me never to accept candy from strangers. So, the name's [first_name]. What's yours?"

    $ BecomeNamed("Silver")

    silver @talkingmouth "Oh. Uh, it's Silver."

    red -happy @talkingmouth "Cool. See ya, then."

    show silver closedbrow with dis:
        xpos 0.5
        ease 3.0 xpos 0.0
        
    show city_A:
        ease 3.0 zoom 2.0

    pause 3.0

    $ renpy.music.queue("Audio/Bus arrive1.ogg", channel='misc', loop=None, tight=None)
    $ renpy.music.queue("Audio/Bus arrive2.ogg", channel='misc', loop=True, tight=None)
    
    pause 2.0
    
    silver neutralbrow @talkingmouth "...If you care, that bus goes directly there."

    show city_A:
        linear 0.5 zoom 1.0

    show silver:
        linear 0.5 xpos 0.5

    red angryeyebrows angryeyes frownmouth @talkingmouth "Man, I'm never going to get to go on my run, am I?" 
    red happy "Fine, I'll get on the bus. Geez."
    
    silver surprisedbrow @talkingmouth "I feel like I'm missing some context...?"
    
    red @talkingmouth "Life's better without it. Seeya, red!"

    $ renpy.music.set_volume(0.25, delay=0.5, channel="music")
    $ renpy.music.stop(channel='misc', fadeout=1.5)
    
    show blank2 with splitfade
    $ renpy.music.play("Audio/Bus_stop.ogg", channel='misc', loop=None, fadein=0.0)
    
    $ renpy.pause(2.0, hard=True)
    
    show text "{color=#ffffff}.{/color}" as text1:
        alpha 1.0
        pause 0.5
        linear 0.0 alpha 0.0
    show text "{color=#ffffff}..{/color}" as text2:
        alpha 0.0
        pause 0.5
        block:
            linear 0.0 alpha 1.0
            pause 0.5
            linear 0.0 alpha 0.0
    show text "{color=#ffffff}...{/color}" as text3:
        alpha 0.0
        pause 1.0
        block:
            linear 0.0 alpha 1.0
            pause 1.5
            linear 1.0 alpha 0.0
    $ renpy.pause(4.0, hard=True)
    
    hide city_A
    show city_B behind blank2
    
    hide text
    hide text1
    hide text2
    hide text3
    
    $ renpy.music.set_volume(1.0, delay=1.0, channel="music")
    $ renpy.music.play("Audio/bigcrowdloop.ogg", channel='crowd2', loop=True, fadein=0.5)
    
    hide blank2 with splitfade
    
    $ renpy.pause(1.5, hard=True)
    
    red @surprised "Whoa!"

    redmind @thinking "This place is big. Like, really big! I saw Inspira tons of times when I was doing my research on Kobukan, but..."
    redmind @upeyes sweat frownmouth "Eeesh. Just looking up at the skyscrapers gives me vertigo. I have to really crane my neck, too."

    red happy "Oh, hey, I can see the school from here! Alright, now, if I just tighten my laces, then I can finally-"

    show city_B with hpunch
    
    Character("Rude Man") "\"Can you {i}move{/i}, maybe? I'm walking here!\""

    red @surprised "Uh... s-sorry? Sorry!"

    redmind @closedeyes frownmouth "Wait, that was totally on him! Why'd I apologize?"

    show brawly uniform:
        xcenter 1.5
        ease 0.5 xcenter 0.5

    brawly happy @angrybrow happymouth "Brother-man! You can't let jerks like that push you around. You need to stand up to them, and tell dicks like that what's what!"
    brawly @closedbrow talking2mouth -happy "Have some confidence in yourself! You don't need anyone to back you up!"
 
    red surprised "...Uh, hi?"
    red -surprisedbrow -frownmouth -surprised @talking2mouth "I appreciate the support, but who are you...?"

    $ BecomeNamed("Brawly")

    brawly -happy @happy "Brawly!"

    redmind closedeyes frownmouth "Yeah, that checks out."
    red surprised "Hey, that uniform! You're a Kobukan student, right?"
    brawly @surprised "Oh, yeah! Member of the Student Council, actually. Are you a new student?"
    red -surprisedbrow -frownmouth -surprised @talkingmouth "Yeah. My name's [first_name]. I'm actually heading to the academy now."
    brawly @talkingmouth "Well, nice to meet ya, [first_name]! I'm actually running a bit late for this orientation the SC Prez is running, so I gotta dash. Up for a jog?"
    red surprised "{w=0.5}.{w=0.5}.{w=0.5}."
    red happy "Oh, I think we're going to get along fine. Yeah, lead the way, Brawly."

    show blank2:
        alpha 0.0
        ease 2.0 alpha 1.0
    
    $ renpy.music.stop(channel='crowd', fadeout=1.5)
    $ renpy.music.stop(channel='crowd2', fadeout=1.5)
    
    $ renpy.pause(4.0, hard=True)
    
    show relichall_A:
        alpha 0.0
        ease 2.0 alpha 1.0
    
    $ renpy.pause(2.5, hard=True)

    hide brawly
    
    hide blank2

    show brawly uniform:
        xcenter 1.5 xzoom -1
        ease 0.5 xcenter 0.5

    brawly @surprisedbrow happymouth "Hoo boy! You're pretty damn fast! You sure you never trained?"
    red closedeyes @talking2mouth "Just went for the odd run every day. Never had the chance for more. Back at Pallet High, the closest thing to a sports team we had was the old folks' bingo club."
    brawly @happy "Maybe you're just a natural, then. Anyway, we're here!"
    
    hide city_B
    
    show relichall_A:
        subpixel True
        zoom 1.0 xpos 0.0 ypos 0.0 alpha 1.0
        ease 6.0 zoom 1.14 xpos -0.14 ypos -0.04
    
    red surprised "...Damn. It's gorgeous."
     
    red closedeyes happymouth happyeyebrows "Wow, okay. Gotta center myself." 
    red -closedeyes -happymouth -happyeyebrows @talkingmouth "You said there's some sort of orientation thing first, right, Brawly?"
    brawly @happy "Yeah, that's--"

    show relichall_A with vpunch

    roxanne uniform @angry "{size=50}{b}BRAWLY!{/b}{/size}"
    brawly @closedbrow talking2mouth "...Yeah, that's the thing I'm late for."
    
    show roxanne uniform:
        xcenter -0.5 xzoom -1
        ease 1.0 xcenter 0.33

    show brawly:
        xcenter 0.5
        ease 1.0 xcenter 0.66

    roxanne @angrybrow talking2mouth "Brawly, were you running in your uniform again?"
    brawly @sadbrow happymouth "Yep! Sorry, Prez."
    roxanne @happybrow talkingmouth "Oh, sweetheart, you will be. {i}You will be.{/i}"
    brawly @sadbrow happymouth "Eh heh heh... I already am."
    
    show roxanne:
        xcenter 0.33
        ease 0.75 zoom 1.25 xcenter 0.33 ypos 1.1

    roxanne @talkingmouth "Now, who's this?"
    red @talkingmouth "[first_name], Ma'am."

    menu: 
        ">Cover for Brawly":
            show brawly happy with dis
            red @talkingmouth "A new student. I was a bit lost, so Brawly helped me find my way here."
            $ AddEvent("Brawly", "Covered")

            show roxanne:
                zoom 1.25 xcenter 0.33 ypos 1.1
                ease 0.5 xzoom -1 xcenter 0.33 ypos 1.1 

            roxanne @happy "Really? How wonderful it is to hear you're taking your Student Council responsibilities seriously.{w=1.0} For once."

            show roxanne:
                xzoom -1 xcenter 0.33 ypos 1.1 
                ease 0.75 xzoom 1 xcenter 0.33 ypos 1.1

            roxanne @talkingmouth "But where are my manners? Please, allow me to introduce myself."

        ">Leave it be":
            red @talkingmouth "Pleasure to meet you."
            roxanne @talkingmouth "The pleasure's all mine, I'm sure."

    $ BecomeNamed("Roxanne")
    roxanne @closedbrow talkingmouth "My name is Roxanne, Kobukan Academy Student Council President. Please, if you ever need something, know that we, the Student Council, are here to serve you."
    roxanne @happybrow sweat talking2mouth "...Except for right now, as we're very late for the orientation we need to set up. Please excuse us."

    red surprised "Huh? Uh, yeah, sure."

    brawly @happy "See ya, [first_name]! You can just chill 'til we announce orientation over the loudspeaker. Go to the dorms, pick out a suite!"

    show brawly:
        ease 1.0 xcenter -0.5

    show roxanne:
        zoom 1.25 ypos 1.1
        ease 1.0 xcenter -0.5

    red -surprisedbrow -frownmouth -surprised @talkingmouth "...Dorms, huh? Guess I should go looking for wherever those are."

    show relichall_A:
        ease 3.0 zoom 1.3

    pause 3.0

    show mace:
        alpha 0.0 xpos 0
        parallel:
            ease 0.5 alpha 1.0
        parallel:
            ease 1.75 xpos 0.66

    show face:
        alpha 0.0 xpos 0
        pause 0.25
        parallel:
            ease 0.5 alpha 1.0
        parallel:
            ease 1.5 xpos 0.33    
    
    mace @talkingmouth "We beg your pardon. Are you a new student?"
    
    show relichall_A:
        zoom 1.3
        ease 1.0 zoom 1.14 xpos -0.1 ypos -0.1
    
    red @talkingmouth "Uh, yeah. What's up?"

    show face smile2mouth happyeyebrows with dis

    mace smilemouth happybrow @happy "Splendid. Us, too! Pleasure."
    
    face @happy "We were hoping you knew something about the orientation that's coming up? We know there {i}is{/i} one, but don't know where it is."

    show face surprisedbrow frownmouth
    show mace surprisedbrow frownmouth
    with dis

    red @happy "Oh, yeah, I was just chatting with a Student Council member about that. He said to just pick out a dorm, then they'd announce the assembly over the loudspeakers."
    
    show face surprisedbrow with dis
    
    mace surprisedbrow @surprisedbrow talkingmouth "You already have the ear of a Student Council member? Formidable. Pre-existing connections, I suppose?"
    
    red -happy @sweat talkingmouth "Not so much. Just met him in Inspira half an hour ago. Don't know {i}anyone{/i} here except another new student, actually."

    face -surprisedbrow -frownmouth -surprised smile2mouth sadbrow @happy "Really, no connections at all? It's so, so, hard to get in here though... how did you manage it?"
    
    mace @closedbrow talkingmouth "Would it be rude to assume that you come from money?"
    
    show face sad
    show mace sad
    with dis
    
    red @happy "Hah, I wish! Nah, I lived in a one-bedroom house in Pallet Town."
    
    mace @sweat sadbrow sadmouth "...Then, perhaps, you're a legacy?"
    
    red -happy @talkingmouth "First person in my family to go to college, actually."
    
    face @angry "Okay, so your academics had to be stellar! Four point ones across the board! Top of your class, surely?!"
    
    red @closedeyes sadmouth "You're not going to believe this, but my high-school was pass-fail. So, in the sense that there were only a few of us, and we all passed, I was top of the class."
    red @happy sweat "Buuuut...{w=0.5} I was probably at the bottom of that group."
    
    mace angry -sweat "[ellipses]"
    
    face @closedbrow frownmouth "[ellipses]"
    
    show face sad with dis
    
    mace @sad "Apologies. We have to go...{w=0.5} somewhere else."

    show mace sad:
        alpha 1.0 xpos 0.66
        parallel:
            pause 0.25
            ease 0.5 alpha 0.0
        parallel:
            ease 1.0 xpos 1.0

    show face sad:
        alpha 1.0 xpos 0.33
        parallel:
            pause 0.5
            ease 0.5 alpha 0.0
        parallel:
            ease 1.0 xpos 1.0
    
    pause 2.0

    stop music fadeout 3.5
    
    redmind sad "Yeah.{w=0.5} That figures.{w=0.5} I mean, from their perspective, and even from mine, there's no way I should be here."
    red @thinking "[ellipses]"
    redmind angrybrow frownmouth "But I am. And I'll do whatever it takes to prove to everyone, and myself, that I deserve this chance."

    queue music "Audio/Music/Show Me Around.ogg"
    
    show relichall_A:
        subpixel True
        zoom 1.14 xpos -0.1 ypos -0.1
        ease 3.0 zoom 1.25 ypos -200 xpos -320
    
    $ renpy.pause(1.8, hard=True)
    
    $ PlaySound("ExitBuilding.ogg")
    scene blank with dip_white

    jump day010402