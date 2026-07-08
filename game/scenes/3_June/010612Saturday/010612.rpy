label day010612:

label PreParty:
    $ timeOfDay = "Morning"
    call clearscreens() from _call_clearscreens_283
    call calendar(1) from _call_calendar_65

    $ calDate = calDate.replace(day=12, month=6, year=2004)

    $ HealParty()
    $ AddEvent("Ethan", "BunnyRecruit")
    $ mallow_present = False

    stop music fadeout 1.5
    show screen songsplash("Pallet Town", "Zame")
    queue music "audio/music/palletpiano.ogg"

    scene suite
    show yellow:
        xpos 0.75
    show blue:
        xpos 0.25
    show ethan:
        xpos 0.5
    with splitfade

    red @talkingmouth "Morning, guys."

    blue @talking2mouth "Well, look who's {i}finally{/i} awake."

    pause 1.0

    show blue surprisedbrow frownmouth with dis

    red @confused "Blue, I left the dorm at 6:00, just after you did. I just came back and took a shower. I ran past you and Yellow while you were training. You yelled at me for breaking your concentration."
    red @closedbrow talking2mouth "Did you seriously forget already? Or do you not care about what actually happened as long as you can yell at me for {i}something{/i}?"

    pause 0.5

    blue -surprisedbrow @talking2mouth sadeyes angryeyebrows lightblush "Look, just[ellipses] we're meant to be discussing the party, right? Don't try to throw us off from realizing you didn't do {i}your{/i} part."

    ethan @talking2mouth closedbrow "{size=30}Oh, yeah, this'll be a great party.{/size}"

    yellow @talking2mouth "I think maybe I should lead this meeting now."

    red @talking2mouth "All in favor?"

    ethan @talking2mouth "Aye."

    blue @closedbrow talking2mouth "Aye."

    red @talking2mouth "Motion passes. Take the stage, Yell'."

    yellow @talking2mouth "Okay. So, um, Ethan, how'd you do this week?"

    show yellow surprisedbrow
    show blue surprisedbrow
    with dis

    ethan @talking2mouth "Pretty alright. I figured out how to make sure Security isn't a problem for us."

    pause 1.0

    red @talking2mouth "Wait, seriously? That's insane. Like, 100%%? Foolproof?"

    ethan @talking2mouth "Yeah. I've done it before."

    show yellow -surprisedbrow
    show blue -surprisedbrow
    with dis

    ethan @talking2mouth sweat closedbrow "Uh, the DC will probably still be a problem, though. Distracted 'em once--they probably won't fall for it again."

    $ bunny_names = ["Nate", "Sonia", "Iono"]
    $ recruited = [name for name in bunny_names if HasEvent(name, "BunnyRecruit")]

    if recruited:
        if len(recruited) == 1:
            $ recruited_str = recruited[0]
        elif len(recruited) == 2:
            $ recruited_str = " and ".join(recruited)
        else:
            $ recruited_str = ", ".join(recruited[:-1]) + ", and " + recruited[-1]
        red @talkingmouth "Hey, that's still great, man. That'll make [recruited_str]'s job way easier."

        if (HasEvent("Iono", "BunnyRecruit") and not HasEvent("Ethan", "EthanIonoReaction")):
            $ AddEvent("Ethan", "IonoSpoiler")

            show ethan surprisedbrow frownmouth with dis

            pause 1.0

            red @talking2mouth "What?"

            ethan @talking2mouth "Iono's here? {i}The{/i} Iono?"

            red @talking2mouth "Oh. Oh, yeah, I guess you[ellipses] uh[ellipses] can we talk about this later?"

            ethan @closedbrow talking2mouth "Fine, but we {i}will{/i} be talking about it."

    else:
        red @happy "Still, good job, man. That's a big thing I was worried about."

    if (HasEvent("Cheren", "BunnyRecruit") and HasEvent("Silver", "BunnyRecruit") and HasEvent("Skyla", "BunnyRecruit")):
        if (HasEvent("Ethan", "IonoSpoiler")):
            red @sweat sadbrow talkingmouth "Promise." 
            red @talkingmouth "Anyway, I talked to the DC, and[ellipses] I'm getting the impression they're not overly excited about the idea of busting us."

        else:
            red @talkingmouth "Besides, I talked to the DC, and[ellipses] I'm getting the impression they're not overly excited about the idea of busting us."

        red @talkingmouth "They might be less of a problem than we thought, as long as we keep our heads down."

        ethan @closedbrow talkingmouth sweat "{size=30}Kinda stealing my thunder there, but[ellipses]{/size} good job."

    yellow @talkingmouth "Yes, good job, Ethan. And what about you, Blue?"

    if (HasEvent("Sonia", "BunnyRecruit") and HasEvent("Gardenia", "BunnyRecruit")):
        blue @talking2mouth "Sonia got me in contact with Gar--Garden--whatsherface, that girl with the football hair."
        blue @talkingmouth "She looped me into a pretty good stash of ingredients, so we'll be good for the party. And I made some stuff already."
    elif (HasEvent("Gardenia", "BunnyRecruit")):
        blue @talkingmouth "Gar--Garden--whatsherface, that girl with the football hair, looped me into a pretty good stash of ingredients, so we'll be good for the party. And I made some stuff already."
    else:
        blue @talking2mouth "I made some stuff."
        
    blue @happy "The {i}one{/i} good thing about that sugary crap Leaf likes is you can make it and it'll still be good a week later."
    blue @closedbrow talking2mouth "'Course, we're still going to have to cook {i}during{/i} the party if we want the food to be fresh."
    blue @talkingmouth "Tell me you got someone to help out, so I don't have to put up with {i}you{/i} in the kitchen, [first_name]."

    red @unamusedbrow unamusedmouth "[ellipses]"
    red @unamusedbrow talking2mouth "I'm just not going to speak to you anymore."

    # Sonia, Hilda, May, Gardenia
    python:
        talked_to = []
        if HasEvent("Sonia", "BunnyRecruit"):
            talked_to.append("Sonia")
        if HasEvent("Hilda", "BunnyRecruit"):
            talked_to.append("Hilda")
        if HasEvent("May", "BunnyRecruit"):
            talked_to.append("May")
        if HasEvent("Gardenia", "BunnyRecruit"):
            talked_to.append("Gardenia")

    if talked_to:
        ethan @talking2mouth "Good idea. Blue, what's with you this morning?"

        show yellow sad2eyes playfulmouth with dis

        blue @angry "Nothing's 'with me!' I'm just the only one taking this seriously, as {i}usual{/i}, and it's pissing me off!"

        pause 1.0

        show blue surprisedbrow frownmouth lightblush with dis

        yellow -playfulmouth -sad2eyes @closedbrow challengingmouth "Blue was so nervous about this party last night he couldn't sleep."

        blue surprisedeyes angryeyebrows angrymouth -lightblush "Wha--"

        if len(talked_to) == 1:
            red @talking2mouth "Yellow, I talked to [talked_to[0]] about the party."
        elif len(talked_to) == 2:
            red @talking2mouth "Yellow, I talked to [talked_to[0]] and [talked_to[1]] about the party."
        elif len(talked_to) == 3:
            red @talking2mouth "Yellow, I talked to [talked_to[0]], [talked_to[1]], and [talked_to[2]] about the party."
        else:
            red @talking2mouth "Yellow, I talked to Sonia, Hilda, May, and Gardenia about the party."

        python:
            party_comments = []

            if "Sonia" in talked_to:
                party_comments.append("Sonia says she can make a, uh, 'rather decent' curry. Her words.")

            if "Hilda" in talked_to:
                party_comments.append("Hilda's probably the reason Hilbert's still alive, so I have to assume she can at least cook something edible.")

            if "May" in talked_to:
                party_comments.append("May cooks for Brendan all the time, so, y'know, easy choice, really.")

            if "Gardenia" in talked_to:
                if HasEvent("Sonia", "BunnyRecruit"):
                    party_comments.append("like Blue said, Gardenia said she'd get some ingredients for us. Looks like she's already started on that part.")
                else:
                    party_comments.append("Gardenia can procure ingredients.")

        if party_comments:
            python:
                joined_comments = ""
                if len(party_comments) == 1:
                    joined_comments = party_comments[0]
                    split_comments = [joined_comments]
                elif len(party_comments) == 2:
                    joined_comments = party_comments[0] + " " + party_comments[1]
                    split_comments = [joined_comments]
                else:
                    # For more than two comments, split into two lines
                    first_line = " ".join(party_comments[:2])
                    second_line = " ".join(party_comments[2:])
                    # Find the first period in the second line
                    period_index = second_line.find(".")
                    if period_index != -1 and period_index < len(second_line) - 1:
                        # Insert " And" after the first period
                        second_line = second_line[:period_index + 1] + " And" + second_line[period_index + 1:]
                    split_comments = [first_line, second_line]

            red @talkingmouth "[split_comments[0]]"

            if (len(split_comments) > 1):
                red @talking2mouth "[split_comments[1]]"
    else:
        red @talking2mouth "Yellow, I couldn't find anyone who could help out on the food front."
        
        blue angrybrow frownmouth @angry "Great! While everyone else is out there enjoying the party, I'm going to be stuck here in the kitchen with {i}you.{/i}"

        ethan @talking2mouth "What's with you this morning? You weren't even going to go out there."

        blue @angry "Nothing's 'with me!' I'm just the only one taking this seriously, as {i}usual{/i}, and it's pissing me off!"

        pause 1.0

        show blue surprisedbrow frownmouth -blush with dis

        yellow @closedbrow talking2mouth "Blue was so nervous about this party last night he couldn't sleep."

        blue surprised "Wha--"

    show blue wistfulbrow frownmouth with dis

    pause 1.0

    blue -wistfulbrow -frownmouth @talking2mouth "Hmph. And what about you, Yellow? How'd you do?"

    if (HasEvent("Sonia", "BunnyRecruit")):
        yellow @talkingmouth "Um, alright. Sonia was a miracle-worker. She matched tailors up with party-goers incredibly well."

    yellow @talkingmouth "There's still some last-minute adjustments to make to the suits, but everyone who wants one should have one."

    if (HasEvent("Whitney", "BunnyRecruit") and not HasEvent("Whitney", "Whitney2Part2")):
        yellow @talkingmouth sadbrow "Whitney was[ellipses] {i}very{/i} motivated to help. She moved through outfits faster than anyone."
        yellow @talking2mouth closedbrow "Though I had to keep her away from the scissors--I think she was trying to manufacture 'wardrobe malfunctions.'"

        ethan @confused "Man, if a {i}guy{/i} tried that, they'd straight-up be arrested."

        red @closedbrow talking2mouth sweat "Let's just double-check all the suits. We don't want anyone having any accidents."

    ethan @talking2mouth "So, hey, just out of curiosity, but[ellipses] is there one for me?"

    yellow @talkingmouth "Of course, Ethan. You're the reason I had this idea."

    ethan @happy "Hell yeah!"
    ethan @confused "Oh, wait, what about this guy?"

    yellow @talkingmouth "Oh, [first_name], did you want one?"

    red @talking2mouth "I[ellipses] truth be told, I didn't really think about that. I just kinda assumed that I'd be too busy running the party to attend."

    yellow @talkingmouth "Hm[ellipses] I think we have enough material to make one more, if we work quickly."
    yellow @sadbrow talkingmouth "Since it's so late, though, I'll probably have to make a pretty basic one. Is that alright?"

    show ethan surprisedbrow frownmouth with dis

    red @sadbrow talkingmouth "I've got no frame of reference. You could give me a loincloth and I'd believe you if you told me that's what men's bunny suits look like."

    ethan -surprisedbrow -frownmouth @talkingmouth "Oh, they do."

    yellow @talking2mouth "Ethan, stop."

    ethan @talking2mouth closedbrow sweat "{size=30}Next time.{/size}"

    pause 1.0

    yellow @talking2mouth "So[ellipses] the last thing to do is to tell Leaf."

    red @surprisedbrow talking2mouth "She's back?"

    blue @angrybrow talkingmouth "You didn't hear her dragging her suitcase up the stairs? Nice that {i}you{/i} got to sleep."

    blue @talkingmouth "Anyway, it's about time. After we've been busting our asses all week for her, she better be grateful."

    ethan @talkingmouth "Would you do the honors, [first_name]?"

    red @talkingmouth sadbrow "Here we go."

    scene door with splitfade

    $ PlaySound("knock.ogg")

    pause 1.5

    if (HasEvent("Leaf", "AcceptedConfession")):
        redmind sadbrow "Why does this feel so familiar?"

    red @sadbrow talkingmouth "Leaf?"

    scene dooropen with dis

    pause 1.0

    show leaf bedhair shadow flirtbrow frownmouth with Dissolve(5.0)

    leaf @talking2mouth "What?"

    yellow @surprisedmouth surprisedbrow lightblush "{size=30}L-Leaf[ellipses]{/size}"

    blue @talking2mouth surprisedbrow "{size=30}[ellipses]What? Did she do something new with her hair?{/size}"

    yellow @blush scaredbrow surprised2mouth "{size=30}L-Leaf, her--{/size}your pants--!"

    blue @talking2mouth closedbrow "I don't know what you're talking about. She's not wearing any."

    leaf @talking2mouth "Yeah, I ran out. I got snot, tears, and makeup on all of them."

    blue @surprised "WHAT?! You should've let me do your laundry! Ignore these other losers, if you want, but at least call me over to clean your gross clothes!"

    ethan @confused "Wait, Blue does the laundry? Is that why those piles of folded clothes keep appearing on my bed?"

    blue @angry "Who the hell did you think it was, your mother?"

    red @wince talking2mouth "Guys, can we please focus?"

    pause 1.0

    leaf @talking2mouth "I repeat. 'What?'"

    menu:
        "[courageoption]>Get to the point.":
            $ TraitChange("Courage")
            red @talkingmouth "I'm glad to see you're up again. Get dressed, we've got something to tell you."

        "[witoption]>Let her talk.":
            $ TraitChange("Wait")
            red @sadbrow talkingmouth "How are you feeling?"

            leaf @talking2mouth "I hate everyone and everything. My favorite color was pink, but I think if I see pink again, I'll vomit."

            python:
                PlaySound("Pokemon/Ball sound.ogg")
                PlaySound("pokemon/cries/39.mp3")
                sidemonnum = 39

            sidemon "Jiggly[ellipses]"

            show leaf sadbrow with dis

            pause 1.0

            leaf cry @talking2mouth "Not you, sweetheart."

            $ PlaySound("pokemon/ball sound.ogg")

    pause 1.0

    leaf @closedbrow talking2mouth "I'm going back to bed."

    red @talking2mouth "Wait. Please. Hear us out."

    pause 0.5

    leaf @talking2mouth "Let me throw some {i}actual{/i} clothes on."

    scene door with dis

    pause 1.0

    scene blank2 with splitfade

    scene suite 
    show blue:
        xpos 0.25
    show yellow:
        xpos 0.5
    show ethan:
        xpos 0.75
    with splitfade

    ethan @talkingmouth "Well, she came to the door. That's a good sign, right?"

    yellow sadbrow @talking2mouth "I hope so. But I'm starting to wonder if throwing a party for her was the right thing to do[ellipses]"

    show blue surprisedbrow frownmouth
    show ethan surprisedbrow frownmouth
    with dis

    ethan @surprisedbrow frownmouth "[ellipses]"

    blue @surprisedbrow frownmouth "[ellipses]"

    red @surprisedbrow frownmouth "[ellipses]"

    ethan -surprisedbrow @surprised "You're wondering that {i}now?!{/i} We spent {i}all week{/i} on this!"

    show blue wistfulbrow with dis

    yellow @sadbrow talking2mouth "I know! And I know I should've said {i}something{/i} already, but you three were working so hard, and--"

    show blue surprisedbrow:
        xpos 0.25
        ease 0.5 xpos 0.2

    show yellow surprisedbrow frownmouth:
        xpos 0.5
        ease 0.5 xpos 0.4

    show ethan surprisedbrow frownmouth:
        xpos 0.75
        ease 0.5 xpos 0.6

    show leaf flirtbrow frownmouth casual with dis:
        xpos 0.8

    leaf @talking2mouth "What were you working hard on? Getting me out of that room?"

    pause 1.0

    leaf @surprisedbrow talking2mouth "Why isn't anyone speaking?" 
    leaf @angrybrow talking2mouth "You might not have noticed, but I'm not in a good mood, so if you have something you want to say, just say it, or let me go back to decomposing in my room."

    red @talkingmouth "Leaf, remember how when Bianca was going through a tough time, you thought a party might cheer her up?"

    leaf @talking2mouth "Yeah. It was only like two weeks ago."

    blue @closedbrow talking2mouth "{size=30}Three.{/size}"

    red @talkingmouth "Well, that's what we did for you."

    pause 1.0

    leaf surprisedbrow @talking2mouth "What?"

    python:
        bunnycount = BunnyAmount()#max 13
        bunnystring = "A few other people are going."

        if (bunnycount == 13):
            bunnystring = "Everyone's going."

        elif (bunnycount >= 10):
            bunnystring = "A ton of people are going."

        elif (bunnycount >= 7):
            bunnystring = "A bunch of people are going."

    red @talkingmouth "You thought you were going to a bunny party, right? Well, we made one. A real one. [bunnystring]"
    red @talking2mouth "It'll be a safe, fun, sexy place to--"

    show leaf:
        xpos 0.8 ypos 1.0 zoom 1.0
        ease 0.5 ypos 1.2 zoom 1.3 

    stop music fadeout 3.5

    narrator "Leaf suddenly puts her finger on your lips."

    leaf cry sadbrow angrysmilemouth @talking2mouth "Shush."

    pause 1.0

    redmind @thinking "Okay."
    redmind @wince frownmouth "How[ellipses] do I interpret this?"
    redmind @sadbrow "Is she mad? She's smiling, but[ellipses]"

    leaf @talking2mouth "You did that for me? Why[ellipses] how did you[ellipses]"

    pause 1.0

    redmind @wince frownmouth "[ellipses]No, still can't tell."

    pause 1.0

    show leaf:
        xpos 0.8 ypos 1.2 zoom 1.3
        ease 0.2 ypos 1.0 zoom 1.0

    show screen songsplash("The Very Best?", "PianoDeuss")
    queue music "audio/music/TheVeryBest_start.ogg" noloop
    queue music "audio/music/TheVeryBest_loop.ogg"
        
    show suite with vpunch

    show ethan winkeyes sadeyebrows sweat frownmouth 
    show blue angrybrow frownmouth 
    show yellow sadbrow frownmouth
    with dis

    leaf angrybrow frownmouth @angrybrow angrymouth "Why the {i}{b}fuck{/b}{/i} did you think I'd ever want to see another stupid bunny suit?! {b}{i}EVER?!{/i}{/b}"

    red @talking2mouth "Uh, we--"

    leaf @angrymouth "After the election, did I shove you back onto a stage and ask you to tell people about your power?! No! Because that'd be a shitty thing to do!"

    red @sadbrow sadmouth "[ellipses]"

    yellow tears @talkingmouth "{size=30}L-Leaf[ellipses]{/size}"

    show blue wistfulbrow frownmouth with dis

    leaf @talking2mouth "And {i}Blue!{/i} What the hell was {i}your{/i} plan here? Are you {i}really{/i} so bad with people you thought pushing me into the situation that {i}just{/i} left me crying and rubbing my face raw for a {i}week{/i} was a good idea?!"

    show ethan angrybrow -sweat with dis

    yellow @talkingmouth "{size=30}L-Leaf, please[ellipses]{/size}"

    leaf shadow @angrymouth "Ethan! What the hell?! {i}This{/i} is what you decide to put effort into?"
    leaf shadow @angrymouth "It was probably your idea, wasn't it?! Because I threw a party that was {i}nothing{/i} like what traumatized Bianca, you came up with the {i}brilliant{/i} and {i}original{/i} idea to just copy exactly what I did--but make it worse!"

    yellow @talkingmouth "{size=30}Leaf, don't[ellipses]{/size}"

    pause 1.0

    ethan @closedbrow talking2mouth "Yeah, you're right, it was all me. Fuck it, we tried to do a nice thing. I'm leaving."

    show suite with vpunch

    show ethan surprisedbrow frownmouth 
    show blue surprisedbrow frownmouth 
    show leaf surprisedbrow cry frownmouth -shadow
    with dis

    yellow closedeyes angryeyebrows -tears @angrymouth "{b}Leaf, STOP!{/b}"

    pause 1.0

    yellow -closedeyes angrybrow tears @talking2mouth "It {i}wasn't{/i} Ethan! It wasn't [first_name], either! It was {i}me!{/i} {i}I{/i} came up with the idea, and {i}I'm{/i} sorry you didn't like it, but that's no reason to be so mean to our friends!"

    leaf @sadbrow talking2mouth "Y-you? I'd expect the boys to be clueless about women, but you[ellipses] I mean, would {i}you{/i} have wanted this?"

    yellow @sadbrow talking2mouth "No. No, of course not. I wouldn't have even gone to the first party. {i}I{/i} would have been terrified."
    yellow @sadbrow sadmouth "But you[ellipses] you're so brave. You're so brave and confident and beautiful. I thought that you'd--I thought you'd be {i}happy{/i} to have another chance. I didn't think you'd let this get you down."

    leaf @sadbrow talking2mouth "Yellow, I spent a week crying in a hotel room. My grades are probably in the toilet now. What else could I have done to make it clearer that I was extremely down?"

    yellow @talking2mouth "Yelling at your friends, who spent all week trying to do something nice for you, would do it."

    show leaf:
        xpos 0.8
        ease 0.9 xpos 0.81
        ease 0.7 xpos 0.78
        ease 0.3 xpos 0.82
        ease 0.5 xpos 0.8
        pause 1.0
        ease 0.7 xpos 0.81 ypos 1.02

    leaf cry @scaredbrow shadow surprisedmouth "I[ellipses] I[ellipses]"
    leaf cry2 @sadbrow sadmouth "I'm sorry.{w=0.5} I'm so sorry.{w=1.0} I'm so, {i}so{/i}, sorry."

    show ethan sad2brow frownmouth 
    show blue closedbrow frownmouth 
    show yellow sadbrow tears frownmouth
    with dis

    leaf sadbrow @closedbrow sadmouth "I--I just--I thought Klara was my friend, and when she--when you guys said you were going to do the exact same thing she did, I was scared--I thought you were[ellipses]"

    if (HasEvent("Klara", "BrokeBond")):
        red @talking2mouth "We're nothing like Klara, Leaf. Klara was just trying to hurt you. I don't get why, but she was. We just want--we just want to see you smile again."

    else:
        red @talking2mouth "Leaf, what happened with Klara was awful. But this isn't the same thing. We all know exactly what's happening--no-one's going to get hurt or embarrassed this time."

    blue @talking2mouth closedbrow "I didn't see anything wrong with Yellow's idea, but even if there {i}was{/i} something[ellipses] we've got your back more than anyone else out there." 
    blue @wistfulbrow talking2mouth "I mean, we're on the Battle Team, right? We have to."

    ethan sad2eyes noshine "[ellipses]"

    yellow @talking2mouth "Ethan?"

    ethan @talking2mouth "I'm going to need more than a slice of a group apology to get over what Leaf just said."

    leaf @talking2mouth "I'm sorry. I'm so sorry, Ethan. I--I didn't mean it. You're not--you don't[ellipses] I'm sorry. I was such an ass."

    ethan "[ellipses]"
    ethan @talking2mouth "No, that's still not good enough. I'm going to need more."

    yellow @talking2mouth angrybrow "Ethan[ellipses]"

    leaf surprisedbrow frownmouth @talking2mouth "{size=30}Okay.{/size} Okay. What? I'll do it."

    ethan @talking2mouth "Two things. Go to the party that we spent all week trying to set up for you."

    leaf surprisedbrow frownmouth cry @sadbrow talkingmouth "Well[ellipses] yeah. Of course. What's the second thing?"

    ethan @talking2mouth "Tell me why you don't like me. If it's something I'm doing, I gotta know."

    leaf @talking2mouth "What? I--I don't, I mean[ellipses] I like you."

    ethan @talking2mouth "Uh-huh. So when you yelled at [first_name] and Blue for five seconds, but then spent double that time screaming at me, calling me a 'worse copy,' you thought that was all proportionate?"

    leaf sadbrow @talking2mouth "That's not what I[ellipses] well, no. I guess I was a bit harsher to you--"

    ethan @talking2mouth "Leaf, even if you don't realize it, you treat me like Blue treats [first_name]."
    ethan @confused "Do you have a crush on me?"

    show ethan upeyes angryeyebrows frownmouth 
    show blue confusedbrow frownmouth 
    show yellow angrybrow frownmouth
    with dis

    leaf @talking2mouth "Ew, no, I--"

    pause 1.0

    leaf @surprisedbrow talking2mouth "Wait, why did I say that? Why 'ew'?"

    ethan @talking2mouth "That's what I'm asking {i}you.{/i}"

    leaf @sadbrow talking2mouth "I[ellipses] don't know. I'm sorry."

    ethan @closedbrow frownmouth "[ellipses]"
    ethan -noshine @talking2mouth "Alright. At least you don't hate me on purpose. For the record, I helped with your party, so if you could work on {i}not{/i} hating me, I'd appreciate that."

    leaf @talking2mouth "I--"

    ethan -upeyes @talking2mouth "I'm done. Anybody else want to put her through the wringer?"

    yellow -angrybrow @closedbrow talking2mouth "Ethan--"

    menu:
        ">Wring 'er":
            $ AddEvent("Leaf", "WrungOut")

            red @talking2mouth "Actually, yeah. Leaf, what you said about the Student Council election wasn't fair."

            leaf @closedbrow sadmouth "No. No, it wasn't. They're not the same thing at all. And I'm sorry. Your--what you went through was so much worse. I'm sorry. I was being selfish and stupid."

            pause 2.0

            redmind @wince frownmouth "Well, shit." 
            redmind @thonk "I was winding up to really lay into her, but[ellipses] I don't think she could get more sorry."

        ">Don't wring 'er":
            pass

    leaf @talking2mouth "You guys, I know an apology isn't enough, so[ellipses] so I'll make it up to you! I'll figure something out. I'll plan the best apology par--"

    blue @scaredbrow talking2mouth "God, no!"
    blue @wistfulbrow talking2mouth "No more parties. Parties are just trouble. If everyone just spent their time training and studying, we wouldn't be in this mess in the first place."

    yellow @talking2mouth "Blue's right. I think we're all pretty partied out. Or will be, after today, anyway."
    yellow @talkingmouth "But I really don't need anything other than an apology. I know you didn't mean it."

    ethan @closedbrow talking2mouth "{size=30}I still do. Get thinking.{/size}"

    blue @talking2mouth "Just show up to class, so [first_name] and I don't have to take notes for you anymore. Such a pain[ellipses]"

    show leaf:
        xpos 0.81 ypos 1.02
        ease 1.0 xpos 0.85 ypos 1.0

    leaf @talking2mouth sadbrow "Y-you[ellipses]"

    call clearscreens() from _call_clearscreens_284

    show blue surprised:
        xpos 0.2
        linear 0.4 rotate -32
        pause 0.5
        ease 0.5 xpos 0.5 ypos 1.5 zoom 1.9

    show yellow surprised:
        xpos 0.4
        pause 0.2
        linear 0.2 xpos 0.2 rotate -16
        pause 0.5
        ease 0.5 xpos 0.5 ypos 1.5 zoom 1.9

    show ethan surprised:
        xpos 0.6
        pause 0.1
        linear 0.3 xpos 0.2 rotate -8
        pause 0.5
        ease 0.5 xpos 0.5 ypos 1.5 zoom 1.9

    show leaf sad:
        xpos 0.85
        linear 0.4 xpos 0.2
        pause 0.5
        ease 0.5 xpos 0.5 ypos 1.5 zoom 1.9

    show blank2:
        alpha 0.0
        pause 1.4
        alpha 1.0

    leaf sad "You {i}guuuuuys!{/i}"

    scene blank2

    pause 0.5

    stop music fadeout 4.5

    narrator "There is significantly more crying before anyone feels ready to start setting up the party[ellipses]"

    pause 1.0

    show noon at vspaz

    pause 3.5

    $ timeOfDay = "Noon"

    queue music "Audio/Music/ViridianB_Start.ogg" noloop
    queue music "Audio/Music/ViridianB_loop.ogg"

    scene kitchen 
    show screen currentdate
    with splitfade

    pause 1.0

    show blue og with dis

    if (FoodBunnies()):
        blue @talking2mouth "Hey, [first_name]. When are my assistants getting here?"

        red @talkingmouth "We're still four hours away from the party, Blue. You don't need to stress out over it yet."

        if BunRecruit("Sonia"):
            if BunRecruit("Gardenia"):
                red @talking2mouth "But Sonia and Gardenia should be here soon."
                red @talking2mouth "Sonia's also helping organize most of the logistics of this party, and Gardenia's dropping off a bunch of ingredients, so they said they'd arrive around noon, and could pitch into the pre-cooking then."

            else:
                red @talking2mouth "But Sonia should be here soon. She's also helping organize most of the logistics of this party, so she said she'd arrive around noon, and could pitch into the pre-cooking then."

            blue @surprised "Really? You're bringing a Galarian into the kitchen? You know what they say about Galarian cooking, right?"

            red @thonk "[ellipses]{nw}"
            extend @confused "Uh. Do you actually have something against Galarian cooking, or are you just trying to find fault in something I did?"

            blue @talking2mouth "God, it was just a joke. Forget it."

            red @upeyes frownmouth "[ellipses]"

        elif BunRecruit("Gardenia"):
            red @talking2mouth "But Gardenia should be here soon. She's dropping off a bunch of ingredients and supplies, so she said she'd arrive around noon, and could pitch into the pre-cooking then."

        blue @talking2mouth "Whatever. Just make sure I get some help in here. I'm not busting my balls to do this whole thing by myself, even if I could."

    else:
        blue @talking2mouth "Hey, [first_name]. Since you bungled getting me any help in the kitchen so hard, why don't you throw on an apron and roll your sleeves up?"

        red @talkingmouth "We're still four hours away from the party, Blue. You don't need to stress out over it yet."
        red @talking2mouth "Besides, I've got to wait for the guests. There's more to this party's logistics than just the food."

        blue @talking2mouth "Whatever. Just make sure you get in here. I'm not busting my balls to do this whole thing by myself, even if I could."

    red @happy "Hey, that's new. Normally you'd be chomping at the bit to do the whole thing yourself."

    blue @angrybrow talkingmouth "Like I said, I {i}could!{/i} But that's a ton of work!"

    red @sweat closedbrow talkingmouth "Still calling it character development."

    show blue sad2eyes with dis

    $ PlaySound("knock.ogg")

    pause 1.5

    if (BunRecruit("Sonia") and BunRecruit("Gardenia")):
        red @talking2mouth "Oh, that must be Sonia or Gardenia."

    elif (BunRecruit("Sonia")):
        red @talking2mouth "Oh, that must be Sonia."

    elif BunRecruit("Gardenia"):
        red @talking2mouth "Oh, that must be Gardenia."

    else:
        red @confused "Huh. Who's knocking this early?"

    show blue closedbrow talking2mouth:
        xpos 0.5 xzoom 1
        ease 0.5 xzoom -1

    blue @talking2mouth "Great. Send them in."

    show blue:
        xpos 0.5
        ease 0.5 xpos -0.2

    scene blank2 with splitfade

    if (BunRecruit("Whitney")):
        pause 0.5

        scene suite with splitfade

        red @happy "Hey! Is it--"

        show whitney bunny with dis

        whitney happybrow @happy "Heya! Queen bunny's finally here--now this par-tay can {i}really{/i} star-tay!"

        red @surprisedbrow frownmouth lightblush "[ellipses]"

        show yellow blush frownmouth surprisedbrow:
            xpos -0.2 xzoom -1
            ease 5.0 xpos 0.1

        show leaf blush frownmouth surprisedbrow casual:
            xpos 1.2
            ease 5.0 xpos 0.9

        red @sweat talking2mouth "Hey, Whitney. You're, uh, early."

        $ whitrecruit = GetEventDatetime("Whitney", "BunnyRecruit")
        $ whitrecruitday = whitrecruit.day
        $ daydelta = whitrecruit.day - calDate.day
        $ dayname = getRWDay(daydelta)
        $ daytime = GetEventMetadata("Whitney", "BunnyRecruit")[3]

        whitney @neutraleyes neutraleyebrows talkingmouth "Li'l bit. I was just {i}so{/i} excited. I haven't been able to think about anything else since [dayname] [daytime]." 
        whitney @talkingmouth "So I thought I could help with any last-minute tailoring!"

        red @sadbrow talkingmouth "Thanks, but I'm not{nw}"

        show whitney sadbrow frownmouth with dis

        extend @sadbrow talkingmouth " {cps=*0.5}sure we,{w=0.5} uh,{w=0.5} actually[ellipses]"

        pause 1.0

        show whitney -frownmouth happybrow with dis

        red @closedbrow talkingmouth "I mean, we're, uh, glad to have you here. Thanks."

        whitney -happybrow @happybrow talking2mouth "So, where do you want me?"

        show ethan behind leaf:
            xpos 1.2
            ease 0.2 xpos 0.75

        ethan @winkbrow talkingmouth "I can think of {i}several{/i} different inappropriate answers to that."

        whitney @playfuleyes unamusedeyebrows talking2mouth "Yeah, well, I'm a lesbian."

        ethan @talking2mouth "And I wouldn't be writing checks if I thought you'd ever cash 'em."

        whitney @confusedeyebrows talkingmouth "So, wait, you're just hitting on me[ellipses]"

        ethan @talkingmouth "For the love of the game, I guess."

        whitney @happy "Ahaha! You're so weird, Ethan!"

        ethan @talking2mouth closedbrow "Damn, that's the {i}second{/i}-most hurtful thing I've heard today."
        ethan @talkingmouth "Anyway, Yellow, do you have anything Whitney can do?"

        yellow @talkingmouth "Oh. Oh, me. I mean, you're talking to me. Yes. Um, if you could just[ellipses] come to my room[ellipses]"

        show whitney:
            xpos 0.5
            ease 0.5 xpos -0.2

        show yellow:
            xpos 0.1 xzoom -1
            pause 0.3
            ease 0.2 xpos 0.3 xzoom 1

        whitney @happy "Sure thing! {w=0.5}{nw}"
        
        $ PlaySound("door_slam.ogg")

        extend "[ellipses]Ooh, it's {i}pink{/i} in here!" 

        whitney @talkingmouth "Hey, is this your--"

        show leaf:
            xpos 0.9
            ease 0.5 xzoom -1
            ease 0.5 xpos 1.2

        yellow @sadbrow talkingmouth "Ah, please don't--"

        show yellow:
            xpos 0.3
            ease 0.5 xpos -0.2

        ethan @confused "Whitney's been here five seconds, and Yellow's already got her in her bedroom. Unexpected rizz?"

        red @talking2mouth "I'm pretty sure Yellow's straight."

        ethan @talking2mouth "So's spaghetti, until it gets wet. Anyway, I gotta go check on something. Be right back."

        show ethan:
            xpos 0.75
            ease 0.5 xpos 1.2

        pause 1.0
        
        red @talkingmouth closedbrow sweat "Oh, yeah, this'll be a fun party."

        pause 1.0

        if (BunRecruit("Sonia") and BunRecruit("Gardenia")):
            redmind @thonk "But seriously, where are Sonia and Gardenia?"

        elif (BunRecruit("Sonia")):
            redmind @thonk "But seriously, where is Sonia?"

        elif (BunRecruit("Gardenia")):
            redmind @thonk "But seriously, where is Gardenia?"

            if (HasEvent("Klara", "AcceptCoordinatorClub") or HasEvent("Game", "Contest1")):
                pause 1.0

                redmind @thinking "Okay. I have a really dumb idea."
                
                red @talking2mouth "'Business.'"

                show gardenia:
                    xpos 1.2 ypos 1.0
                    parallel:
                        easein 0.3 ypos 0.7
                        easeout 0.3 ypos 1.0
                    parallel:
                        ease 0.3 xpos 0.25
                    parallel:
                        pause 0.3
                        ease 0.5 xzoom -1

                show suite with vpunch

                gardenia @happy "And that's my cue!"

                red @surprisedbrow frownmouth "[ellipses]"
                red @talkingmouth confusedeyebrows "Okay, you {i}had{/i} to be hiding behind the door, waiting for that, right?"

                gardenia @flirtbrow talking2mouth "A good merchant never reveals her secrets--for free."

                red @talkingmouth "Then I guess I'll wait for a sale."

                jump gardeniabunnyintroshortcut
        
        scene blank2 with splitfade

        pause 0.5

        $ PlaySound("knock.ogg")

    if (BunRecruit("Sonia")):
        pause 0.5

        scene suite with splitfade

        sonia @talkingmouth "Er, hello? Sorry if I'm intruding, the door is open, so--"

        red @happy "Oh, Sonia! No, that's great. Please, come in."

        show sonia with dis:
            xpos 0.5

        sonia @talking2mouth "Good morning. Everything going smoothly here?"

        red @talkingmouth "Smooth enough, but you'd probably know more than me."

        sonia @happy "No, no. This is still Dorm 25's party."
        sonia @talking2mouth "Now, regardless there are a {i}lot{/i} of moving parts, but I reckon everything's more or less settled."

        $ bunword = IntToWord(10 + 5 * BunRecruitCategory('Bunny'))
        $ bunword = bunword[0].upper() + bunword[1:]

        sonia @closedbrow talking2mouth "Let's see... we have all our RSVPs back. [bunword] in all."

        red @surprisedbrow "That's a lot. Is the room going to be big enough for all of us?"

        sonia @talking2mouth "I think so. Not everyone will be able to be there for the full party, and we've got enough turnover that I don't think the room should ever be too crowded."

        red @talkingmouth "Fantastic. Thank you for helping us with this."

        sonia @talkingmouth "Oh, it's not at all a problem. Actually, having the chance to stretch the old spreadsheeting fingers after so long was quite refreshing."
        sonia @talking2mouth "I do have a bit of a question, though, if it's alright?"

        red @talkingmouth "Yeah, go ahead?"

        sonia @talking2mouth "Is Leaf alright? She hasn't been showing up to our Electric-type elective, she wasn't at the Battle Team meeting yesterday, and[ellipses]"
        sonia @sadbrow talkingmouth "Well, managing the logistics of this party really seems like the sort of thing that she would've done in other circumstances."

        redmind @wince frownmouth "Ah. I guess Nessa didn't tell her what happened last Saturday. Of course, that's a good thing--no reason to publicize this, really."

        red @talkingmouth "Well[ellipses] I could tell ya, but do you want to ask her yourself?"

        sonia @surprised "Oh? Well, if that's an option, rather."

        red @happy "Leaf? Could you come here for a sec?"

        show leaf casual:
            xpos 1.2
            ease 0.5 xpos 0.66

        show sonia:
            xpos 0.5
            ease 0.5 xzoom -1 xpos 0.33

        leaf sadbrow @neutralbrow talkingmouth "Hey, Sonia."

        sonia @talkingmouth "Leaf! Good to see you again. I was worried something had happened. Didn't you get my texts?"

        leaf sadbrow frownmouth "[ellipses]"

        leaf @talking2mouth "Sorry. I've only sent one text in, like[ellipses] exactly a week."

        sonia @talking2mouth "Ah. Say no more. I've had some weeks like those too. I hope you're feeling better, now?"

        leaf -sadbrow -frownmouth @talkingmouth "Yeah. Because I have the best friends ever."

        sonia @angrybrow talkingmouth "Hold off. I'd say {i}I{/i} do, and I'd battle you for that."
        sonia @talkingmouth "Anyway, I'm glad to hear you're pepping up. I'm sure the WRCEE will be happy to have you back, too."

        red @talking2mouth "Sorry to interrupt--WRCEE?"

        leaf @talkingmouth sadbrow "Oh, it's a[ellipses] it's a club some of the girls in Lt. Surge's elective set up."

        sonia @talkingmouth "The Woman's Rant Center for Electrical Education."

        leaf @flirtbrow talking2mouth "We meet up after class to rant about Lt. Surge and go over the material he was too busy being a misogynist to teach properly."

        red @sweat talking2mouth "[ellipses]Ah."

        leaf @winkbrow talkingmouth "Sorry, this is one club you won't be invited to."

        red @sadbrow talkingmouth "Completely fair."

        sonia @talking2mouth "We also have these 'scream sessions,' where we yell at some of our shyer members to toughen them up, so when Surge does it, they don't cry."

        leaf @happy "Sonia's one of our best screamers, actually."

        sonia @sadbrow talkingmouth "Yes, but I still always cry when I'm on the receiving end."

        red @happy sweat "Sorry you have to deal with that, ladies."

        if (HasEvent("Lieutenant Surge", 2.1)):
            leaf @closedbrow talking2mouth "You've taken his class a bunch as well. You have it almost as bad as us."

            red @sadbrow talkingmouth "Don't I? Don't we all. Lt. Surge has a way of bringing us together."

            $ ValueChange("Leaf", 1, 0.66, False)
            $ ValueChange("Sonia", 1, 0.33)

            red @talkingmouth "Anyway, Sonia, Blue's in the kitchen."

        else:
            leaf @sadbrow talkingmouth "That's just the tip of the iceberg, Skippy. Did you know you can literally {i}die{/i} from toxic shock syndrome if you forget to take a tampon out?"

            red @closedbrow sweat talking2mouth "Right, that's my cue to leave. Sonia, Blue's in the kitchen."

        sonia @talkingmouth "Right-o. I'll be there promptly."

        if (BunRecruit("Whitney")):
            scene blank2 with splitfade

            whitney bunny @talking2mouth "{size=30}Wait, did I just hear Sonia?{/size}"

            scene suite 
            show sonia surprisedbrow frownmouth:
                xpos 0.66
            with splitfade

            show whitney bunny:
                xpos -0.2
                ease 0.5 xpos 0.33

            whitney @talkingmouth "Sonia! Heyyyyyyy."

            sonia @talkingmouth "Oh. Hello, Whitney."

            whitney playfulmouth @confusedbrow talkingmouth "You look surprised. Something catch your eye?"

            sonia "[ellipses]"

            show whitney surprisedbrow frownmouth with dis

            sonia -surprisedbrow -frownmouth @talking2mouth "No, not really. I'm just surprised to see you here so early. That wasn't on the schedule. No harm done, though."

            whitney -surprisedbrow @talking2mouth "Oh. So[ellipses] my outfit[ellipses]?"

            sonia @talkingmouth "It's quite nice. Very flattering."

            pause 1.0

            whitney @sad2eyes angryeyebrows talking2mouth "I thought you'd be more flustered."

            sonia @happy "Ah, apologies. Nessa's my best friend, as you know, so I've seen her wear a variety of outfits that would make your suit look[ellipses] ah, chaste."

            whitney @surprised "Oh[ellipses] okay."

            sonia @talkingmouth "But, like I said, very flattering. Don't unfairly compare yourself to an actual model--trust me, madness that way lies."

            show sonia:
                xpos 0.66
                ease 0.5 xpos -0.2

            pause 1.5

            whitney shadow sad2eyes angryeyebrows talking2mouth "You're going {i}down{/i}, Nessa."

        scene blank2 with splitfade

        pause 0.5

        $ PlaySound("knock.ogg")

    if (BunRecruit("Gardenia")):
        scene suite with splitfade

        red @talkingmouth "Yeah? Come in!"

        show gardenia with dis:
            xpos 0.5

        gardenia @talkingmouth "Hey, partner!" 
        
        red @happy "Hey, Gardenia!"

        label gardeniabunnyintroshortcut:
        
        gardenia @sadbrow talkingmouth "Sorry, can't stay here long. Just came to drop off some ingredients."

        show ethan:
            xpos -0.2
            ease 0.5 xpos 0.33

        if (BunRecruit("Sonia")):
            ethan @talkingmouth "Great, I'll lug 'em into the kitchen. Sonia'll know which ones stay here, and which ones go onto the party room."

        else:
            ethan @talkingmouth "Great, I'll lug 'em into the kitchen--Blue'll probably have strong opinions as to which ones stay here, and which ones go onto the party room."

        show ethan:
            xpos 0.33
            ease 0.5 xpos 1.2

        gardenia @talkingmouth "Speaking of the party room, I dropped by. It was looking a bit sparse, so I dropped off some decorations."

        red @happy "Oh, seriously? Thanks! I'll go there and--"

        show ethan:
            xpos 1.2
            ease 0.5 xpos 0.66

        ethan @angryeyebrows talkingmouth "Hey, hey! You'll do {i}nothing{/i}. You need to stay here and handle all the people. I'll set up the decor."
        ethan @closedbrow talking2mouth "Maybe loop Leaf into it, as well. We could do with some time to talk things out."

        show ethan:
            xpos 0.66
            ease 0.5 xpos 1.2

        pause 1.0

        gardenia @talkingmouth "That's a good worker you've got there. A real go-getter. How much are you paying him?"

        red @confused "Uh, friendship?"

        gardenia @flirtbrow talkingmouth "Ah, priceless. A bit too rich for my tastes."
        gardenia @talkingmouth "I'll check in on the tailors, but then I've gotta run--don't worry, more stuff will be coming throughout the day, even if I'm not delivering it."

        if (BunRecruit("Sonia")):
            gardenia @happy "Sonia's got the details and timeline. Seeya!"
        else:
            gardenia @happy "Seeya!"

        red @talkingmouth "Oh, uh, yeah! See ya! Thanks for--uh, everything!"

        scene blank2 with splitfade

        pause 0.5

        $ PlaySound("knock.ogg")
        
    if BunRecruit("May"):
        scene suite with splitfade

        red @talkingmouth "Oh, hey, you two!"

        # Determine if Mallow is present
        $ mallow_present = GetRelationshipRank("May") >= 2

        if mallow_present:
            red @confused "Or[ellipses] three?"

            show brendan:
                xpos 1.2
                ease 0.5 xpos 0.75

            show mallow:
                xpos 1.2 
                ease 0.5 xpos 0.5

            show may:
                xpos 1.2
                ease 0.5 xpos 0.25

            brendan @happy "Hey, dude. Just dropping the girls off. Yellow working on last-minute tailoring?"

            red @talkingmouth "In her bedroom."

            if BunRecruit("Whitney"):
                red @happy "Knock before going in, though. Whitney's in there, and god knows what she's gotten Yellow into--or out of."
                brendan @talkingmouth closedbrow "Eesh, yeah. Thanks for the heads-up."

            mallow @angrybrow talkingmouth "Hey, hey! [first_name], what did you mean by 'you three' like that?"

            red @happy "Nothing! I just wasn't expecting you."
            red @talkingmouth "Glad you're here, though. I wish I'd thought of inviting you here myself."
            red @talkingmouth "Thanks, May."

            may @happy "Of course! The more the merrier, right? And Mallow's a {i}great{/i} chef, anyway."

            red @talkingmouth "Are you here for the party, or just to help out in the kitchens?"

            mallow @surprisedbrow talking2mouth "Oh, I figured I probably wouldn't have time for the actual party."

        else:
            show brendan:
                xpos 1.2
                ease 0.5 xpos 0.66

            show may:
                xpos 1.2
                ease 0.5 xpos 0.33

            brendan @happy "Hey, dude. Just dropping my girl off. Yellow working on last-minute tailoring?"

            red @talkingmouth "In her bedroom."

            if BunRecruit("Whitney"):
                red @happy "Knock before going in, though. Whitney's in there, and god knows what she's gotten Yellow into--or out of."
                brendan @talkingmouth closedbrow "Eesh, yeah. Thanks for the heads-up."

            may @happy "Sounds like a fun time! Have fun, sweetie." 
            may @talkingmouth "[first_name], thanks for throwing this party. Brendan really needed something to take his mind off the Millennium Drop."

            brendan @sweat sadbrow talkingmouth "Man, I {i}really{/i} want to go over my Millennium Drop routine again, but[ellipses] I should definitely take a break. Not much my Pokémon or I can do about it this late."

            red @talkingmouth "Is there something you're worried about, Brendan?"

            brendan @talking2mouth "Nah, I'm just kinda a perfectionist when it comes to my routines. Used to stay up all night, the night before, practicin', before I realized being tired makes your routines way worse."
            brendan @happy "All-nighters never work. Not in tests, and not in contests, either."

            red @talking2mouth "Amen."

            brendan @talkingmouth "Oh, yeah, May, you wanted to ask [first_name] somethin', right?"

            may @talking2mouth "Oh, yeah."
            may @talkingmouth "So, totally fine if it doesn't work out, but will there be time for me to go to the actual party, or will I be needed in the kitchen the full time?"

        # Sonia or Blue handles kitchen logistics
        if BunRecruit("Sonia"):
            show sonia at loff, flip

            $ LineUp()

            sonia @talking2mouth "Pardon, I couldn't but help overhearing."

            if mallow_present:
                sonia @happy "Er, hello, Mallow, yes? I'm a classmate of May's--I'm sort of handling the logistics of this party."

                mallow @talkingmouth "Oh, hi! Yup, I'm Mallow. May and I are in the cooking club together."
                
                sonia @closedbrow talking2mouth "Oh, we have a cooking club? Hm. Rather odd I'd never heard of it."
                
                mallow @sadbrow blush talking2mouth "We have some troubles with recruiting[ellipses]"
            
            else:
                may @talkingmouth "Oh, hi, Sonia! Thanks for helping out with the logistics of the party."
                
                sonia @happy "Of course. You know me--I never turn down the chance to put myself elbow-deep in a good spreadsheet."

            sonia @talking2mouth "Now, about whether you'll be able to leave the kitchen for a bit, let me just check the spreadsheet[ellipses]"

            show sonia:
                xpos 0.2 xzoom -1
                ease 0.5 xzoom 1

            pause 1.0

            $ kitchen_helpers = len(FoodBunnies()) + (2 if mallow_present else 1)
            
            sonia @talking2mouth closedbrow "Ah, it looks like we've got [IntToWord(kitchen_helpers)] people helping in the kitchen, assuming [first_name] can pop in once or twice."

            red @happy "Totally."

            sonia @talking2mouth "At that rate[ellipses] divide by [IntToWord(kitchen_helpers)][ellipses]"

            show sonia:
                xpos 0.2 xzoom 1
                ease 0.5 xzoom -1

            $ enough_helpers = kitchen_helpers > 3
            if enough_helpers:
                if mallow_present:
                    $ AddEvent("Mallow", "BunnyRecruit")
                    show mallow surprisedbrow frownmouth with dis
                    
                    sonia @happy "Yes, it looks like you should have plenty of time to attend the party yourself, if you'd like. Do you have an outfit?"
                    
                    mallow @talking2mouth "Um. Like a bunny suit? I don't[ellipses]"

                    show mallow -surprisedbrow -frownmouth with dis
                    
                    brendan @talkingmouth "You'll be fine. Yellow and I can whip something up."

                    sonia @talkingmouth "We've actually got a most-completed one already. I predicted there'd be some last-minute additions to the party."

                    brendan @surprisedbrow talking2mouth "Seriously? Sonia, that's great. Thanks!" 
                    brendan @talkingmouth "Nessa told me you were super-reliable. Thanks for helpin' these guys with the party."

                    sonia @sadbrow talkingmouth "{size=30}{i}Nessa{/i} said that? About me?{/size} I mean[ellipses] er, thanks."

                else:
                    $ AddEvent("May", "WearBunny")
                    
                    sonia @happy "Yes, it looks like you should have plenty of time to attend the party yourself, if you'd like. Do you have an outfit?"
                    
                    may @talkingmouth "Yep! Although[ellipses]"
                    may @lightblush talkingmouth "Sweetie, is it fine if I[ellipses]"
                    
                    brendan @talkingmouth "Babe, I literally could not be happier. It's a seriously sexy outfit--just let people know I made it."
                    
                    may @flirtbrow talkingmouth "Of course."
                    
                    red @talkingmouth "Alright, lovebirds. Brendan, you're needed in Yellow's room. May, you--"
            else:
                sonia @sadbrow talkingmouth "I'm quite sorry. I think it'll be all hands on deck."

                if mallow_present:
                    mallow @happy "{i}'A'ole pilikia.{/i} Totally fine! Cooking with my friends is fun enough."
                else:
                    may @talkingmouth "Oh, it's alright. Cooking's fun enough."
        else:
            show blue at loff

            $ LineUp()

            blue @talking2mouth "What are you doing asking [first_name] about this stuff? {i}I'm{/i} in charge of the kitchen."

            if mallow_present:
                mallow @surprisedbrow talking2mouth "[ellipses]You are?"
            else:
                may @surprisedbrow talking2mouth "Wait, really?"

            blue @surprisedbrow talking2mouth "Wha--Yeah, of {i}course{/i} I am! What the hell did you mean by that?"

            may poutmouth flirtbrow @talking2mouth "[first_name], can Blue {i}actually{/i} cook?"

            red @talking2mouth sweat "Yeah, he can. And it tastes good, and it's healthy, too. The problem is everything he cooks ends up looking like grey sludge."

            blue @glancebrow talking2mouth "Bull."

            red @unamusedbrow talkingmouth "No, seriously. Salads? Grey sludge. Meat? Grey sludge. Grey ice cream? Weirdly enough, {i}greyer{/i} sludge."

            blue @angry "Screw you."

            $ kitchen_helpers = len(FoodBunnies()) + (2 if mallow_present else 1)
            $ enough_helpers = kitchen_helpers > 3

            if enough_helpers:
                if mallow_present:
                    $ AddEvent("Mallow", "BunnyRecruit")
                    blue @talking2mouth "Generic Alolan girl, you can go to the party once you're done in the kitchen. I could handle the whole thing myself--I only need you for, like, half an hour."
                    
                    show blue:
                        xpos 0.2 
                        ease 0.5 xzoom -1
                        ease 0.5 xpos -0.2

                    mallow @surprisedbrow talking2mouth "Oh. Thank you!"

                else:
                    $ AddEvent("May", "WearBunny")
                    blue @talking2mouth "I'll show you, May. If {i}I{/i} was cooking for Brendan, he never would've told those stupid-ass lies."
                    blue @closedbrow "Anyway, I could handle the whole thing myself--I only need you for, like, half an hour. Then you can go and do your weird bunny suit thing or whatever."
            else:
                if mallow_present:
                    blue @talking2mouth "Generic Alolan girl, because [first_name] sucks at recruiting, I'm going to need you in the kitchen the whole time, so forget about going to the party. The food'll be the only good part, anyway."
                    
                    show blue:
                        xpos 0.2 
                        ease 0.5 xzoom -1
                        ease 0.5 xpos -0.2
                    
                    mallow @happy "{i}'A'ole pilikia.{/i} Totally fine! Cooking with my friends is fun enough."

                else:
                    blue @talking2mouth "I'll show you, May. If {i}I{/i} was cooking for Brendan, he never would've told those stupid-ass lies."
                    blue @closedbrow talking2mouth "Anyway, because [first_name] sucks at recruiting, I'm going to need you in the kitchen the whole time, so forget about going to the party. The food'll be the only good part, anyway."
                    
                    show blue:
                        xpos 0.25 
                        ease 0.5 xzoom -1
                        ease 0.5 xpos -0.2

                    may @surprisedbrow talking2mouth "What?! How'd he know about that?"

                    red @surprisedbrow talking2mouth "I have no idea. I sure as hell didn't tell him."

                    brendan @closedbrow talking2mouth "Wasn't me, either. Guess he's still[ellipses] well, you know."

            pause 1.0

            if mallow_present:
                mallow @angry "Wait, what did he call me?"
                if enough_helpers:
                    red @talking2mouth sweat closedbrow "Ignore him, he's being more of an ass than normal."

                    may @talkingmouth "Yeah, and he's kinda a butt even on a good day. He's in my homeroom."
                    may @happy "Anyway, it's great you'll be able to go to the actual party, Mallow. Do you have an outfit?"
                    
                    mallow @talking2mouth "Um. Like a bunny suit? I don't[ellipses]"
                    
                    brendan @talkingmouth "You'll be fine. Yellow and I can whip something up."

            elif enough_helpers:
                    red @talking2mouth sweat closedbrow "Ignore him, he's being more of an ass than normal."
                    
                    may @talkingmouth "Yeah, and he's kinda a butt even on a good day, sweetie. You're lucky you don't have homeroom with him."
                    
                    red @talkingmouth "Seriously. Anyway, it's great you'll be able to go to the actual party, May. Do you have an outfit?"
                    
                    may @talkingmouth "Yep! Although[ellipses]"
                    may @lightblush talkingmouth "Sweetie, is it fine if I[ellipses]"
                    
                    brendan @talkingmouth "Babe, I literally could not be happier. It's a seriously sexy outfit--just let people know I made it."
                    
                    may @flirtbrow talkingmouth "Of course."
                    
                    red @talkingmouth "Alright, lovebirds. Brendan, you're needed in Yellow's room. May, you--"

        $ GroupExpression("surprisedbrow frownmouth")

        show suite with vpunch

        $ hideside = True

        blue "{size=60}Alright, you idiot sandwiches! Everyone who can cook--and [first_name]--get in the kitchen!{/size}"
        blue "{size=60}C'mon, chop, chop!{/size}"

        pause 1.0

        $ hideside = False

        red @wince talkingmouth "Yeah[ellipses] that's our cue."

    else:
        red @confused "Now, who could {i}that{/i} be[ellipses]?"

    stop music fadeout 1.5
    queue music "audio/music/NewFriends_start.ogg" noloop
    queue music "audio/music/NewFriends_loop.ogg"

    scene blank2 with Dissolve(2.0)

    narrator "Time passes quickly as you work around the clock to set things up for the party[ellipses]"

    if (BunRecruit("Sonia")):
        pause 1.0

        if (BunRecruit("Gardenia")):
            sonia @talkingmouth "[first_name], sorry, I know I'm being a worrywart, but could you go check on the party room? Ethan and Leaf should be finished setting everything up, now."

        else:
            sonia @sadbrow talkingmouth "[first_name], sorry, I know I'm being a worrywart, but could you go check on the party room?"
            sonia @talkingmouth "I asked Ethan and Leaf to set the decorations up, and they should be done by now."

        red @happy "Not a problem. Be right back!"

    else:
        pause 1.0

        yellow @talking2mouth "Oh, [first_name]! Would you mind checking on the party room? Leaf and Ethan should be done setting it up by now."

        red @talking2mouth "On it. Be right back!"

    pause 1.0

    if (BunRecruit("Nate")):
        scene academyhall with splitfade

        pause 1.0

        show nate suit with dis

        nate @happy "Oh, [nate_name]! Just the guy I was looking for."

        red @talkingmouth "Oh, hey. Nice suit. But, uh, aren't you a bit overdressed?"

        nate @winkbrow talkingmouth "Oh, I've got my {i}fun{/i} suit on underneath this. And my birthday suit on under that."
        nate @talkingmouth "I'm just wearing this while I'm acting as bouncer. Had the suit, uh, 'lying around,' so might as well use it, right?"

        if (GetRelationshipRank("Nate") > 0):
            nate @talking2mouth "Most of the time I wear this, no-one remembers what I'm doing in it."

            red @sad2eyes frownmouth "[ellipses]"
            red @talking2mouth "{size=30}Hey, uh, if this is a 'work suit,' is it safe to wear it out here? Like, you won't get in trouble with Anabel, will you?{/size}"

            nate @talking2mouth "I mean, sure, probably. But it's whatever. Are they {i}really{/i} going to tell me I can't wear the clothes they gave me to a college party?"

            red @thonk "[ellipses]"
            red @confused "I genuinely have no idea."

            nate @talking2mouth "Nah, they won't. They've got way more important stuff to worry about."

            red @sweat talking2mouth "I guess that's good--though maybe not? It'd probably be better if they {i}didn't{/i} have anything to worry about, right?"

            nate @unamusedbrow talkingmouth "Yeah, and it'd also be better if my farts cured cancer, and I didn't have to count calories. Y'know, while we're being silly."

            red @closedbrow sweat talkingmouth "Noted."

        else:
            red @talking2mouth "Fair. Looking sharp."

        red @talkingmouth "Anyway, anything I should know about how you're going to bounce?"

        show nate at getcloser

        nate flirtbrow lightblush @talkingmouth "All night, if you let me."

        red @lightblush frownmouth closedbrow sweat "[ellipses]{nw}"
        extend @lightblush talking2mouth closedbrow sweat "I, uh, don't have the mental bandwidth to process that right now."

        show nate at getfurther

        nate -flirtbrow -lightblush @talking2mouth "Fair, pulling it back."
        nate @talking2mouth "I'm guessing you meant 'bounce' as in 'be a bouncer,' then. Leave the details to me, just know that no-one's getting through that door without your say-so."

        if (BunRecruit("Rosa")):
            red @talkingmouth sadbrow "Thanks, man. The guests'll really appreciate it. Especially Rosa."

            if (GetRelationshipRank("Nate") > 0):
                nate @sadbrow talkingmouth "God, I can imagine. I pretend {i}I've{/i} got it hard, whining about no-one ever really being able to know me. I can't imagine dealing with {i}everyone{/i} knowing you."
                nate sad2eyes sadeyebrows @talkingmouth "R's got it way worse than me, and she doesn't even get the perks I do."

                pause 1.0

            else:
                nate sad2eyes sadeyebrows @talkingmouth "God, I can imagine. I can't imagine even one person knowing you, never mind {i}everyone{/i}. Must be exhausting."

                pause 1.0

                red @thonk "[ellipses]"

                redmind @thinking "He says that, but he sounds wistful[ellipses]?"
                redmind @thonk "Wait, what does he mean he can't imagine even {i}one{/i} person knowing him?"

            nate neutraleyes neutraleyebrows neutralmouth @talkingmouth "Ah, ignore me. Here to check on the status of the room? Mostly quiet on the Western Front."

        else:
            red @talkingmouth sadbrow "Thanks, man. The guests'll really appreciate it. Especially Leaf."

            nate neutraleyes neutraleyebrows neutralmouth @talkingmouth "Ah, I do what I can. Here to check on the status of the room? Mostly quiet on the Western Front."

        red @talking2mouth "Yeah, I will. Thanks."

        if (BunRecruit("Iono")):
            pause 0.5

            show nate at getcloser

            nate @talking2mouth closedbrow sweat "Hey, uh, just one more thing, actually."
            nate frownmouth @upeyes angryeyebrows talking2mouth "I didn't want to say it before, because it's kind of embarrassing, frankly, and I don't think it has anything to do with this party."
            nate frownmouth @upeyes angryeyebrows talking2mouth "But after the Student Council elections, I'm not keeping anything from you, no matter how small."
            
            if (GetRelationshipRank("Nate") > 0):
                nate @talking2mouth "Besides stuff for, you know, work."

            red @sadbrow talkingmouth "Appreciated."

            nate @talking2mouth "Anyway, we've got another signal looking through our security cameras."

            red @confused "Huh?"

            nate @talking2mouth "Yeah, someone's spliced themselves into the feed. Normally, backtracing that kind of thing would be a cinch for me, but[ellipses]"

            pause 1.0

            red @confused "But?"

            nate lightblush poutmouth sad2eyes angryeyebrows @talking2mouth "I can't."

            red @surprisedbrow talkingmouth "Sorry, what?"

            if (GetRelationshipRank("Nate") > 0):
                nate @upeyes talking2mouth "I {i}can't.{/i} Their encryption is too strong, and they're using a quadruple-modal switching algorithm. The {i}Bank of Unova{/i} only uses double-modal."
            else:
                nate @upeyes talking2mouth "I {i}can't.{/i} Their encryption is too strong, and they're using a quadruple-modal switching algorithm."
            nate -lightblush frownmouth -sad2eyes -angryeyebrows @sweat flirtbrow talkingmouth "I've never seen such a paranoidly-built piece of software. It's impressive, in a frustrating way."

            red @closedbrow talkingmouth "Hah!"

            nate @upeyes talking2mouth "Yeah, yeah. Laugh it up, [nate_name]."

            if (GetRelationshipRank("Nate") > 0):
                nate @talking2mouth "Anyway, you don't really need to worry about that. Whoever wrote that program isn't a student--it's gotta be another intelligence agency, something non-INTERPOL."
                nate @closedbrow talking2mouth "My money's on the Fiorians, but whoever it is, they're not going to care that we're throwing a bunny-themed party. They're probably trying to spy on Champion Alder, or maybe Champion Wallace."
                nate @talking2mouth "Even so, I took the camera out of the party room, and made sure there weren't any other hidden ones."

            else:
                red @sadbrow talkingmouth "Sorry. But what does this mean for the party?"

                nate @talking2mouth "Nothing, really. Which is why I didn't mention it until now. Technically, it means that whoever's got the splice could be watching or recording the guests, but I've cleared the party room of cameras."

            red @talking2mouth "But the hallways[ellipses]?"

            if (BunRecruit("Sonia")):
                nate @talking2mouth "Didn't Sonia tell you? I worked with her to plan a route from the dorms to the party room that only passes by cameras I capped."

                red @talking2mouth sweat closedbrow "I swear, I turned away for one second, and by the time I turned back, Sonia had made this entire party work."

                nate -frownmouth @happy "Yeah, she's really reliable. I miss classes with her."

                red @talking2mouth "Sorry, follow-up question: what did you mean by 'capped'?"

            else:
                nate @talkingmouth "Don't worry. I've capped every camera from the dorms to the party room--and most guests'll probably change in the room itself, anyway."

                red @talkingmouth "Like you, with your matroyshka suits. Got it. But what do you mean by 'capped?'"

            nate @confusedbrow frownmouth "[ellipses]"
            nate -frownmouth @happy "I mean I put a cap on the lens, [nate_name]. That's not tech slang. The cap was made of rubber."

            red @happy "Whoops. I just assumed."

            nate @talkingmouth sadbrow "That's not uncommon--people forget that we live in a physical world."
            nate @talkingmouth sadbrow "A thousand programs, laws, cameras, walls, schemes, or whatever else you want can be undone by a single pair of hands in the right place."
            nate @happy "{i}People{/i} are powerful, you know? Not just Pokémon."

            if (GetRelationshipRank("Nate") > 0):
                red @unamusedbrow talkingmouth "Isn't your job to make people forget that?"

                nate @talkingmouth "Yeah, but you're kinda a lost cause in that regard."

                red @unamusedbrow talkingmouth "Flatterer."

            else:
                red @talkingmouth "Good advice. I'll remember that."

                nate @sadbrow talkingmouth "{size=30}I wish.{/size} Yeah, you do that."

        nate @happy "Don't let me keep you from kicking off this bunny party any longer. Hop to it!"

        red @unamusedbrow unamusedmouth tired "[ellipses]"

        if (BunRecruit("Iono")):
            scene blank2 with splitfade

            $ PlaySound("vibrate.ogg")

            pause 1.0
            
            show phone_B
            show iono happy:
                xpos 0.525 zoom 0.9 ypos 0.9
            show phone_A 
            with fadeinbottom

            iono @happymouth "Yeah, that was me."

            red @talking2mouth "Cool. Can you not fight Nate over your shared goal of securing the party?"

            show iono:
                xpos 0.5

            iono @angrybrow talking2mouth "It wasn't {i}meant{/i} to be a fight! He just got all up in my bizzay-ness by noticing what I was doing!"
            iono angry @angryeyes annoyedeyebrow talking2mouth "And the whole 'putting rubber caps on the cameras' thing? Way to nerf me, dude. Hacks are cool, but haxx are {i}not!{/i}"

            narrator "A familiar migraine begins to set in[ellipses]"

            red @talking2mouth "Alright. I assume since you heard the conversation we just had, you have some other way of making sure no-one gets into the party?"

            show iono:
                xpos 0.5

            iono @smugbrow talkingmouth "Don't you worry your pretty little hat about it. I've got this area locked down harder than the wiki page of a controversial politician."

            show iono happybrow teeheemouth:
                xpos 0.525

            red @confused "T-topical. I assume. I don't really know."

            pause 1.0

            red @wince talking2mouth "I'm going to hang up, now. And maybe see if Ethan's got some headache meds in his first-aid kit."

            iono @happy "{i}Sayonara! Ciao! Au revoir! And adieu!{/i}"

            pause 1.0

            iono @confusedbrow talking2mouth "Hey, what's the difference between {i}au revoir{/i} and {i}adieu?{/i} They're both Kalosian, right? Is one, like, 'seeya,' and the other is like 'farewell'? Or is it like--"

            hide phone_B
            hide iono
            hide phone_A
            with fadeoutbottom

            red @unamusedbrow unamusedmouth tired "[ellipses]"

    scene blank2 with splitfade

    pause 1.0

    scene bunday with splitfade

    pause 1.0

    red @talking2mouth "Guys?"

    show leaf at loff
    show ethan at roff
    $ LineUp()

    leaf @happy "Hey, [first_name]."

    red @talkingmouth "Room looks nice. It's, uh, evocative."

    leaf @sadbrow talkingmouth "I really only know one way to decorate a party room."

    ethan @closedbrow talking2mouth "Don't look too closely at the banner back there. I just filled in some of the letters with colored markers, and made new ones by cutting up old receipts."

    if (BunRecruit("Gardenia")):
        red @confused "I thought Gardenia dropped off some more decorations?"

        ethan @happy "Yeah, that's why it still looks good, even though I touched it."

    red @talkingmouth "You both did great. This party is going to kick ass."

    leaf sadbrow @talkingmouth "I'm sure."

    pause 1.0

    red @talkingmouth "Will you be okay?"

    leaf @closedbrow sadmouth "I[ellipses] Yes. Yes, I just[ellipses]"

    pause 0.5

    ethan @closedbrow talking2mouth "{i}Sigh.{/i}"
    ethan @talkingmouth "Leaf, we're going with you. You'll be in good company. No-one's going to get embarrassed today, okay? It'll just be friends--yours and [first_name]'s."

    leaf @talkingmouth "Thanks[ellipses]"

    ethan @talking2mouth "Don't mention it. Seriously, if I think about it too much, I'll chicken out, too."

    leaf surprisedbrow frownmouth @talkingmouth "Seriously? But you're always so gung-ho about the idea of crossdressing."

    ethan @talkingmouth "Haven't {i}done{/i} it before. This'll be something new for me. I probably wouldn't have, even now, if I wasn't doing it to support you."

    leaf sadbrow frownmouth "[ellipses]"
    leaf @talkingmouth "I'm sorry I've been such a jerk to you."

    ethan @closedbrow talking2mouth "Whatever. Let's just focus on the party for now."

    show leaf -frownmouth with dis

    ethan @talkingmouth "[first_name], Leaf and I are going to get changed. You coming with?"

    red @talkingmouth "Oh, was Yellow able to make a suit for me?"

    if (BunRecruit("Whitney")):
        ethan @talkingmouth "Yeah, it looked mostly done when I peeked into Yellow's room. Yellow and Whitney were fighting over how much it covered, but--"

        leaf @surprisedbrow talking2mouth "Did Whitney win?"

        ethan @sad2eyes sadeyebrows talking2mouth "Tragically, no."

        leaf @angrybrow angrymouth "{size=30}The {i}one{/i} time Yellow decides to fight for something.{/size}"

        red @sadbrow talkingmouth "Y'know, it's flattering how much everyone seems to want to see me half-naked, but I can't help but feel a little objectified."

        ethan @flirtbrow talkingmouth "Don't worry about it, toots. We'll buy you an energy drink."

        red @angryeyebrows sad2eyes frownmouth "[ellipses]"

    else:
        ethan @talkingmouth "Yeah, looked pretty much like it when I stuck my head in her room, before I left."

    red @closedeyes confusedeyebrows talking2mouth "Guess I gotta make a decision, then."

    show flashback with superslowdis

    narrator "[bluecolor]If you elect not to wear a bunny suit, you will not be able to attend the party with the other guests.{/color}"
    narrator "However, you will still be able to help in the kitchens, and handle any security concerns that may arise."

    pause 0.5

    narrator "What do you wish to do?"

    menu:
        ">Bare your bunny body":
            $ AddEvent("Game", "BunnyRecruit")

            hide flashback with dis

            ethan @talkingmouth "Cool."

        ">Renounce your rabbit robes":
            hide flashback with dis

            ethan @talking2mouth "Alright, man. I'll tell Yellow that we can save that suit for someone else."

            red @sadbrow talkingmouth "Thanks. I don't want to bring down the mood of the party for everyone else by being awkward about my own suit, you know?"

            ethan @talking2mouth "Yeah, I get it. Don't worry about it, man. We've all got our lines in the sand."

    leaf @talkingmouth "Let's head back to the suite, then. We'll grab the outfits, and bring them back here."

    red @talkingmouth "Yeah, so no-one has to walk across campus in a bunny suit, this time."

    if (BunRecruit("Whitney")):
        leaf @flirtbrow talkingmouth "Although Whitney obviously wanted to. Are we going to make her change clothes back before coming here?"

        red @confused "Change into what? She clearly didn't bring a change of clothes."

        leaf @talking2mouth "Maybe something of Yellow's could fit her? Well, not really around the chest, I guess. I was just spitballing."

        red @talkingmouth flirtbrow "Delaying, you mean?"

        leaf @sadbrow talkingmouth "Tamato, patato."

    red @happy "C'mon, you two. Let's go."

    scene blank2 with splitfade

    pause 1.0

    scene suite with splitfade

    if (BunRecruit("Game")):
        pause 0.5

        show yellow surprisedbrow frownmouth with vpunch

        yellow @surprisedbrow talking2mouth "Oh, there you are! Here's your suit!"

        show yellow at getcloser

        narrator "Yellow tosses the costume at you like it's scalding her hands."

        show yellow at getfurther

        pause 0.5

        yellow @talking2mouth "B-bye!"

        show yellow:
            xpos 0.5
            ease 0.7 xpos 0.45
            ease 0.3 xpos 1.2

        red @sadbrow talkingmouth "Still pretty shy, huh?"

        if (BunRecruit("Whitney")):
            show whitney bunny:
                xpos -0.2
                ease 0.5 xpos 0.33

            whitney @talkingmouth "Yeah, she could barely look at the suit while she was making it. Just kept staring directly at my face."
            whitney @talking2mouth "It's like, hello! My boobs are down here!"

            red @talking2mouth "Clearly. Uh, if she wasn't really looking at it, does the suit actually[ellipses]?"

            whitney @closedbrow talking2mouth "Yeah, I think it should probably be fine. It's a simple pattern, and the stitches are solid." 
            whitney @winkbrow talkingmouth "Only one way to find out though, right?"

            red @talking2mouth "Yeah, I guess. Uh, just double-checking--you {i}are{/i} still gay, right?"

            whitney @closedbrow talkingmouth "Yes, but I'm also a big believer in everyone being their sexiest at all times."

            red @confused "Huh."

            whitney @closedbrow talkingmouth "I'm also a big believer in not getting arrested for practicing that belief in most situations, so when I get the chance--"

            red @happy "You really grab the bull by the horns. Got it."

        red @talkingmouth "Well, I'm going to go back to the party room and change."

        hide yellow

        show leaf at roff
        $ LineUp()

        leaf @talkingmouth "Don't change too much! I like you the way you are."

        scene blank2 with splitfade

        pause 1.0

        scene bunday with splitfade

        pause 0.5

        show red closedbrow frownmouth bunny with Dissolve(2.0)

        $ AddEvent("Game", "AutoBunny")

        red @talkingmouth "Alright, buddy. What's the damage? Is anything sticking out where it shouldn't?"

        $ PlaySound("pokemon/pikachu_happy2.ogg")

        libpikachu @happy "Piiiikaaaa.~"

        red confused "Really? Is it[ellipses]"

        pause 0.5

        red surprisedbrow frownmouth @talking2mouth "Oh, wow."

        pause 0.5

        redmind sad2eyes surprisedeyebrows poutmouth "Yeah, I get it now. I definitely get it."

        pause 0.5

        redmind lightblush "Holy shit, my ass looks {i}incredible{/i}."

        pause 0.5

        redmind sadeyebrows -poutmouth "I {i}cannot{/i} tell Mom about this."

    else:
        narrator "Ethan informs Yellow of your choice."
        narrator "Contrary to your fears she'd be upset, she actually seems {i}relieved.{/i}"
        narrator "You decide to go back to the party room and stand by the door to greet the guests."

    scene blank2 with splitfade

    pause 0.5

    if (not BunRecruit("Nate")):
        narrator "While waiting for guests to arrive, you decide to wait by the door to the party room."

    scene academyhall with splitfade

    if (BunRecruit("Nate")):
        show nate suit with splitfade

        if (BunRecruit("Game")):
            nate @surprisedbrow talkingmouth "Hey, you look good, man."

            red bunny @talkingmouth "That's all? Just 'I look good'?"

            nate @confusedbrow talkingmouth "Feeling confident, huh?"

            red @happy "You flirt with me pretty hard even when I'm wearing last night's jeans, and last {i}week's{/i} vest. Figured you'd pounce at all[ellipses] this."

            nate @talkingmouth "Hey, I know when someone's out of their comfort zone. Comes in handy, being able to tell when someone's playing a different part than usual."
            nate @happy "Don't want to make it {i}more{/i} uncomfortable by making a big deal out of it."

            red @sadbrow talkingmouth "You know[ellipses] you're a pretty good guy."

            nate @winkbrow talkingmouth "Now who's pouncing?"
            nate @talkingmouth "Anyway, going to spend some time out here with li'l ol' me?"

        else:
            nate @happy "Hey, you're back!"

        red @talkingmouth "Yeah, I thought I'd hang out with you and greet the bunnies. You know, in case you need some extra muscle bouncing uninvited guests."

        nate @happy "Oh, for sure. Don't know what I'd do without ya."

        $ SmartShift("nate", 0.33)

        if (GetRelationshipRank("Nate") >= 2):
            red @talking2mouth "Yeah, yeah. Joke all you want. Remember how Bea, Hilbert, and I whooped your ass?"

            nate @unamusedbrow talkingmouth "Remember how it took all three of you?"

            red @unamusedbrow talkingmouth "Remember how it totally didn't?"

            nate @happy "Must be a rogue Beheeyem around, because {i}no{/i}, I don't."

            red @upbrow talkingmouth "Convenient."

        else:
            red @talkingmouth "Dunno, but it probably wouldn't be nearly as fun."

        nate @surprisedbrow talking2mouth "Oh, look sharp. We have contact at 3."

        redmind @thonk "[ellipses]It's 4:30?"

    else:
        redmind @talkingmouth "Oh, here comes someone."

    if (BunRecruit("Nessa")):
        $ MoveInRight("Nessa")

        nessa "[ellipses]"

        nessa @talkingmouth "Oh, shit. Am I early?"

        red @talkingmouth "Right on time. But you're the first one here who isn't helping out, yeah."

        nessa @closedbrow frownmouth "[ellipses]{w=0.5}{nw}"
        extend @talkingmouth "Not a word of this to anyone. If anyone asks, I was fashionably late."

        if (BunRecruit("Nate")):
            show nessa surprisedbrow frownmouth with dis

            nate @talkingmouth "It's okay to be enthusiastic about things. I mean, who doesn't like dressing up once in a while? Or dressing down, I guess."

            nessa @talkingmouth "Um, yeah. You're right. {w=0.5}{nw}"
            extend @confused "Sorry, aren't you a bit overdressed?"

            nate @confused "Don't bouncers wear suits?"

            nessa -surprisedbrow -frownmouth @talkingmouth "Maybe in old movies. Most of the time they wear metal band shirts."
            nessa @talking2mouth "Something without sleeves. A strong pair of arms, and a visible set of Poké Balls, is usually the number-one thing bouncers want."

            nate @closedbrow sweat talking2mouth "Hearing you loud and clear. I'll file that away for next time."

            if (BunRecruit("Game")):
                nessa @closedbrow talkingmouth "Still, you're wearing it well. Half of fashion is wearing it with confidence, and you've got it. Less you, [first_name]."

                red @closedbrow talking2mouth "Ow."

                nessa @talking2mouth "You will, though. It's amazing how used to it you can get. By the end of the day, you'll be looking forward to next time."

                red @talkingmouth "You sound confident."

                nessa @talking2mouth "A model knows clothes. Time wears everything away--awkwardness, too."

                red @talkingmouth sadbrow "I'll keep an open mind."

            else:
                nessa @closedbrow talkingmouth "Still, you're wearing it well. Half of fashion is wearing it with confidence, and you've got it."

                nate @talkingmouth "Hey, you too."

        else:
            red @sadbrow talkingmouth "If anyone asks, I'll jump out the nearest window."

        nessa @talkingmouth "Alright, I'm going in. See you in there later, [first_name]?"

        red @talkingmouth "Yeah, seeya."

        show nessa:
            ease 0.5 xpos -0.2

        pause 1.0

        if (BunRecruit("Nate") and GetRelationshipRank("Nate") >= 1):
            nate @talking2mouth "A girl who needs to reinvent herself every time someone points a camera at her[ellipses]"
            nate @talkingmouth sadbrow "Who wears what she has to, looks how she has to, and knows she's fighting a losing battle against people's memories of her past[ellipses]"

            pause 1.0

            nate @talkingmouth "Models and agents have more in common than you'd think, huh?"

            red @closedbrow talkingmouth "Seems like it."

            nate @talkingmouth "'Course, the biggest thing she and I have in common is that we're both gorgeous."

            if (BunRecruit("Game")):
                red @upbrow talkingmouth "I know you're trying to distract me from thinking about my suit. Thanks."

                nate @closedbrow talkingmouth "Maybe I just like discussing philosophy. You don't know."

                red @confused "Do you?"

                nate @sadbrow talkingmouth "You don't know."

            else:
                red @sweat talkingmouth closedbrow "Pat yourself on the butt a bit harder, why don't you."

        pause 1.0

        if (BunRecruit("Nate")):
            nate @talking2mouth "Oh, look alive. We've got incoming."
        else:
            redmind "Oh, here come more."

        hide nessa

    if (BunRecruit("Whitney")):
        $ MoveInRight("Whitney")

        if (BunRecruit("Game")):
            whitney bunny @talkingmouth "[first_name]! Nice suit. It looks like someone very smart and cute made it for you."

            red bunny @confused "You?"

            whitney @closedbrow talking2mouth "It was more like seventy percent Yellow, but yeah, I helped."

        else:
            whitney bunny @talkingmouth "[first_name]!"

        if (BunRecruit("Nate")):
            nate @surprisedbrow frownmouth "[ellipses]"
            nate @talking2mouth "[nate_name], I thought everyone was going to come here and change?"

            whitney @talking2mouth "Yeah, that was the plan, but I don't mind walking around in this."

            nate frownmouth angrybrow @talking2mouth "It's not about if you're comfortable in your suit or not. You could've jeopardized this entire operation, if someone saw you."

            whitney @talking2mouth "'Kay. Well, you're dressed like mafia, so between the two of us--"

            nate @upbrow talking2mouth "I'm the {i}bouncer!{/i}"

            if (BunRecruit("Nessa")):
                show whitney surprisedbrow frownmouth with dis
                
                nate @wince talking2mouth "Seriously[ellipses] between [nate_name], that Galarian model, and you, I feel like {i}nobody{/i} gets what I'm going for with the suit."

                whitney @talkingmouth "{size=30}Galarian model[ellipses]{/size} Nessa? You mean Nessa is here? Already?"

                red @talking2mouth "Well, yes, but--"

            else:
                whitney @talkingmouth "Oh, we have a bouncer? Thanks for bouncing, then! What was your name?"

                nate @talking2mouth "Uh, Nate."

                whitney @talkingmouth "Sorry for jeopardizing the entire operation, then. But I'm sure you can take care of it!"

            show nate surprisedbrow frownmouth with dis

            show whitney:
                ease 0.2 xpos -0.2

            pause 2.0

            nate -surprisedbrow -frownmouth @closedbrow sweat talking2mouth "[ellipses]Let's just hope no-one saw her."

        else:
            red @talking2mouth "Whitney, did you walk all the way here in your suit?"
    
            whitney @talking2mouth "Yeah, but I don't mind walking around in this. It's kinda thrilling, actually."

            red @wince talking2mouth "I'm glad you're having fun, but that's not the problem. If someone saw you, then the whole party could've been busted."

            whitney @talking2mouth "Don't worry, no-one did."

            red @closedbrow talking2mouth "I--okay. Are you {i}sure{/i}?"

            whitney @talking2mouth "Mostly. Now, can I go in, Mr. Bouncer?"

            red @talking2mouth "Yeah, I guess. Just keep your hands to yourself. The party's meant to be fun and sexy, not[ellipses] over-the-top."

            whitney @confusedbrow frownmouth "[ellipses]"
            whitney @talking2mouth "You know, back in Goldenrod, when girls would pass out at house parties, me and my Miltank would be the ones making sure no-one messed with 'em."
            whitney @closedbrow talking2mouth "You could give me a little more benefit of the doubt."

            red @sadbrow talkingmouth "You're right--I'm sorry."

            whitney @happy "All forgiven! No grudges can be held at a pa~a~a~a~arty!"

            show whitney:
                ease 0.2 xpos -0.2

        pause 2.0

        if (BunRecruit("Nate")):
            nate @talking2mouth "Oh, looks like we've got some more on their way."
        else:
            redmind "Looks like there are some more people coming[ellipses]"

        hide whitney

    if (BunRecruit("Rosa")):
        $ MoveInRight("Rosa")

        if (BunRecruit("Game")):
            if (BunRecruit("Sonia")):
                rosa surprisedbrow lightblush frownmouth @talkingmouth "[first_name]! You're already dressed? I thought Sonia said we'd dress here!"
            else:
                rosa surprisedbrow lightblush frownmouth @talkingmouth "[first_name]! You're already dressed? I thought we were going to come here, then change!"

            red bunny @talkingmouth "Don't worry, you're right. I just changed, then thought I'd greet the guests out here."

            rosa -surprisedbrow -frownmouth @talkingmouth "Oh, okay. Um, you look pretty."

            red @sweat happy "Yeah, I've been getting that a lot."

        else:
            rosa @talkingmouth "Hi, [first_name]. Right through here?"

            red @talkingmouth "That's the way. Everything's locked down and secure--don't worry about anyone who might be watching, because it'll only be everyone in the room there with you."

        if (BunRecruit("Nate")):
            rosa @talkingmouth "Oh, hello, Nate!"

            nate @talkingmouth "Hey, there."

            rosa @talkingmouth "Are you the party's bouncer?"

            if (BunRecruit("Nessa") or BunRecruit("Whitney")):
                nate @happy "Finally, {i}someone{/i} gets it. I knew I liked ya for a reason. I'll buy another ten tickets to your next movie, now."

                rosa @happy "That's the power of guerilla marketing."

                nate @closedbrow talkingmouth "Alright, enough monkeying around. Go on in--we've got the party room locked down and secure, but I can't guarantee this hallway."

            else:
                nate @talkingmouth "Sure am. Though don't get me wrong--I'm going to join the party, too."

        rosa @sadbrow talkingmouth "Thank you so much for accommodating me. I {i}really{/i} appreciate it--like, {i}really{/i}, really."

        show rosa lightblush with dis

        red @happy "Hey, you're worth it. Besides, it wasn't that much trouble--we wanted this party to be safe and secure for {i}everyone{/i}, you know?"

        rosa @happy "I'll pay you back by having the night of my life!"

        show rosa:
            ease 0.5 xpos -0.2

        pause 1.0

        hide rosa with dis

        if (BunRecruit("Nate")):
            nate @talkingmouth "Sweet girl. We met once, you know."

            red @talkingmouth "What, outside of Kobukan?"

            nate @sad2brow talkingmouth "Yeah."

            pause 1.0

            if (GetRelationshipRank("Nate") >= 1):
                red @thonk "[ellipses]"
                
                nate @sad2brow talkingmouth "Nah, she doesn't remember."

            pause 1.0

        if (BunRecruit("Nate")):
            nate @surprisedbrow talking2mouth "Woah. Lotta people on the way. That's probably the majority of the guests left, yeah?"

            red @talkingmouth "Probably."
        
        else:
            redmind @surprisedbrow frownmouth "Woah. Lot of people on the way. That's probably most of the guests left[ellipses]"

    $ PutRoff("Ethan")
    $ PutRoff("Leaf")
    $ LineUp()

    if (BunRecruit("Game")):
        show leaf surprisedbrow frownmouth blush

    ethan @talkingmouth "Hey, man."

    if (BunRecruit("Game")):
        leaf @talking2mouth "H-hi."

        pause 1.0

        show leaf angrybrow angrysmilemouth with dis

        ethan @happy "Leaf, did you just {i}stutter?{/i}"

        leaf @talking2mouth "Have you not noticed how good [first_name] looks? A bit of stuttering is in order!"

    else:
        leaf @talkingmouth "Hey, [first_name]. Going to stand guard?"

        red @talkingmouth "Maybe for a bit. I'll probably go help out in the kitchens for a while."

        if (BunRecruit("May") and BunRecruit("Sonia")):
            red @happy "Don't want to leave May and Sonia alone with Blue."
        elif (BunRecruit("May")):
            red @happy "Don't want to leave May alone with Blue."
        elif (BunRecruit("Sonia")):
            red @happy "Don't want to leave Sonia alone with Blue."
        else:
            red @happy "Don't want to leave Blue alone in the kitchen for too long."

    if (BunRecruit("Nate")):
        nate @talkingmouth "Hey, MC². Hey[ellipses]{w=1.5} {nw}"
        extend @closedbrow talking2mouth sweat "Sex."

        leaf -angrybrow -angrysmilemouth @sadbrow talkingmouth "You[ellipses] uh, you don't {i}need{/i} to use that name."

        nate @talking2mouth sweat closedbrow "{size=30}Oh, thank god.{/size}"
        nate @talking2mouth "Alright. What's the substitute? Remember, three characters or less."

        leaf @closedbrow talking2mouth "Hm[ellipses] how about JGL?"

        nate @confused "JGL?"

        $ PokemonSpeak("Jigglypuff", "Jiggalee! Jiggaloo!")

        nate @talking2mouth "JGL. Sure. Logged it."

    leaf -angrybrow -angrysmilemouth @talkingmouth "Well[ellipses] we're going in to change."

    if (BunRecruit("Game")):
        if (BunRecruit("Nate")):
            red @talking2mouth "Sure thing. I'll go with you--Nate, you have the front?"

            nate @talking2mouth "Fully frontal, yeah."

            pause 1.0

            red @confused "Bit of a stretch, that one."

            nate @sweat talkingmouth closedbrow "They can't all be winners."

        elif (BunRecruit("Iono")):
            red @talkingmouth "Alright. Looks like most of the guests are in, so I'll go in now, too."

            ethan @confused "Huh? What if someone just tries to, uh, wander up? We need {i}someone{/i} at the entrance, right?"

            red @happy "Don't worry, it's covered."

            ethan @confused "If you say so, man. If it's any problem, though, I can stay out here--it's fine."

            red @sadbrow talkingmouth "Nah, really, it's covered. We've got someone watching out for us."

            ethan @closedbrow talkingmouth "Alright."

        elif (BunRecruit("Sonia")):
            red @talkingmouth "Alright. I'll go with you." 
            red @talkingmouth "Oh, but we should have {i}someone{/i} out front, so I'll text Sonia, ask if she can come over and stand guard for a bit."

            ethan @talkingmouth "Sure thing."
        
        else:
            $ AddEvent("Game", "EthanLeafChangeSkip")

            red @talkingmouth "Alright. We should have {i}someone{/i} out front, so I'll stay here for a bit longer. Someone inside can take over after a while, maybe."

            ethan @talking2mouth "Oh, yeah, don't worry about it, man. I'll take over for you, soon as I get changed."

            red @happy "Hey, not so fast! Enjoy yourself a bit, first. You spent just as much time on this party as any of us. We should all get to enjoy it."

            ethan @closedbrow sweat talkingmouth "Yellow probably spent more time on it than either of us combined, honestly[ellipses] and she's not here. Feels kinda bad."

            red @sadbrow talkingmouth "We'll have to plan something for her."

            ethan @closedbrow sweat talkingmouth "As long as it's not a party."

            red @talking2mouth sweat closedbrow "Agreed."

    else:
        $ AddEvent("Game", "EthanLeafChangeSkip")

        red @talkingmouth "Alright. Have fun, you two!"

        ethan @talkingmouth "Yeah, we'll miss ya. We'll try not to have any big battles without you."

        red @angrybrow talking2mouth "Make sure you don't. If you guys have {i}any{/i} fun without me being in the center of it, I'll cry."

        ethan @happy "I think we've all had enough crying for today. We'll be careful."

    scene blank2 with splitfade

    pause 1.0

    if (BunRecruit("Game")):
        scene bunday with splitfade

        if (not HasEvent("Game", "EthanLeafChangeSkip")):
            $ MoveInRight("Leaf blush bunny", 2.0)
            $ MoveInLeft("Ethan lightblush bunny", 2.0)

            pause 2.0

            leaf @talkingmouth "{size=30}Heh.{/size}"

            pause 0.5

            ethan @closedbrow talkingmouth "Heh."

            pause 0.5

            red bunny @closedbrow talkingmouth "Hahaha[ellipses]"

            pause 1.0

            show ethan happy
            show leaf happy
            show red happy bunny at Transform(xpos=0.08, yanchor=0.35)
            with dis

            TempCharacter("{gradient=#cf0000-#00b23f}You D{/gradient}{gradient=#00b23f-#c1861e}orks{/gradient}") "Ha {w=0.5}ha {w=0.5}ha {w=0.5}ha {w=0.5}ha!"

            hide red with dis

            leaf @talkingmouth "Oh my god, this is so silly! We all look ridiculous!"

            ethan @talkingmouth winkbrow "Speak for yourself, princess. I look damn good. See this body? This is peak male performance."

            leaf @sadbrow talkingmouth "Why--{i}gasp{/i}--{nw}"
            
            show leaf:
                xpos 0.66 ypos 1.0
                parallel:
                    ease 0.1 ypos 1.01
                    ease 0.1 ypos 0.99
                    ease 0.1 ypos 1.01
                    ease 0.1 ypos 0.99
                    ease 0.1 ypos 1.01
                    ease 0.1 ypos 1.0
                parallel:
                    ease 0.08 xpos 0.67
                    ease 0.08 xpos 0.65
                    ease 0.08 xpos 0.67
                    ease 0.08 xpos 0.65
                    ease 0.08 xpos 0.66
            
            extend @sadbrow talkingmouth "{size=30}ohmigodican'tbreathe{/size}--{i}why{/i} are your pants unbuttoned?!"

            ethan "Ease of access!"

            leaf "{size=30}Oh, god, stop, seriously, stop, I can't breathe.{/size}"

            red bunny @happy "Y'know[ellipses] I think this party might end up working out, after all."

            show leaf sadbrow neutralmouth 
            show ethan neutraleyebrows neutraleyes neutralmouth
            with dis

            leaf @talkingmouth "Thanks, guys. Seriously."

            if (BunRecruit("Whitney")):
                $ MoveInRight("Whitney bunny")

                whitney @happy "Yeah, seriously! Thank you!"

            if (BunRecruit("Nessa")):
                $ MoveInLeft("Nessa bunny")

                if (BunRecruit("Sonia")):
                    nessa @closedbrow talkingmouth "Thanks for giving Sonia something to throw herself into."
                    nessa @blush winkbrow talkingmouth "[ellipses]And giving me an excuse to wear something fun."
                
                else:
                    nessa @talkingmouth "Thanks for giving me an excuse to wear something fun."
            
            if (BunRecruit("Rosa")):
                $ MoveInLeft("rosa bunny")

                pause 0.3

                $ PlaySound("!.ogg")

                show leaf fullblush surprisedbrow frownmouth with dis

                rosa @happy "Thank you for everything you've done to make this happen. I've always wanted to go to a party like this!"

                leaf @talking2mouth "{size=30}Holy shit.{/size}"

        else:
            $ RemoveEvent("Ethan", "BunnyRecruit")

            show likeanhourlater at vspaz 

            pause 1.0

            scene academyhall with splitfade

            $ MoveInRight("ethan bunny")

            ethan @talkingmouth "[first_name]! Sorry, man, I totally lost track of time in there. I'm here to relieve you."

            red @unamusedeyes happyeyebrows talkingmouth "That's a dangerous thing to say when you're dressed like that."

            ethan @talkingmouth "Heh. Thanks, man."

            pause 1.0

            ethan @happy "I know we did this for Leaf, but, honestly[ellipses] this has made me feel really great. This party, I mean."
            ethan @talkingmouth "Thanks for everything you did."

            red @happy "Hey, it was mostly you and Yellow. All I did was follow directions."

            ethan @talkingmouth "I'm talking about letting me go the party first. Being there when it started really meant a lot."
            ethan @sweat talkingmouth closedbrow "I didn't realize it'd mean a lot to me 'til I did it, but[ellipses] yeah, it did. So, thanks."

            red @talkingmouth "Anytime, bud."

            ethan @happy "Now get in there and have some PG-rated but still sexy fun!"

            scene blank2 with splitfade

            pause 1.0

            scene bunday with splitfade

            if (BunRecruit("Rosa")):#pretty sure this should be impossible, but if it is, no harm in including it.
                $ MoveInLeft("rosa bunny")

            if (BunRecruit("Nessa")):
                $ MoveInLeft("Nessa bunny")

            if (BunRecruit("Whitney")):
                $ MoveInRight("Whitney bunny")

            $ MoveInLeft("Leaf bunny")

            leaf @happy "[first_name]! {i}There{/i} you are!"

            red bunny @happy "Hey, all! Sorry I'm late."

            leaf @flirtbrow talkingmouth "Late what? The party can't {i}really{/i} start without you!"

        red @happy "Well, what are we waiting for? Let's get this party started!"

        $ GroupExpression("happy blush")

        scene bunday with Dissolve(2.0)

    narrator "Over the course of the next few hours, several [bluecolor]events{/color} will occur."
    narrator "No events are mutually exclusive, and no events will expire if you do not get to them in time."

    if (BunRecruit("Game")):
        narrator "Don't worry about optimization; just have fun! You've earned this party, so enjoy it."

stop music fadeout 1.5
queue music "audio/music/viridianforest_start.ogg" noloop
queue music "audio/music/viridianforest_loop.ogg"

$ bunnypartybgm = ("audio/music/viridianforest_start.ogg", "audio/music/viridianforest_loop.ogg")

label BunnyPartyStart:

python:
    rabbit_pokemon_ids = [
        29,   # Nidoran Female
        30,   # Nidorina
        32,   # Nidoran Male 
        33,   # Nidorino
        293,  # Whismur
        427,  # Buneary
        428,  # Lopunny
        659,  # Bunnelby
        660,  # Diggersby
        813,  # Scorbunny
        814,  # Raboot
        815,  # Cinderace
        311,  # Plusle
        312,  # Minun
        494,  # Victini
        184,  # Azumarill
        531,  # Audino
        556,  # Maractus
        327,  # Spinda
        172,  # Pichu
        25,   # Pikachu
        26,   # Raichu
        26.1, # Alolan Raichu,
        133,  # Eevee,
        134,  # Vaporeon,
        135,  # Jolteon,
        136,  # Flareon
        196,  # Espeon
        197,  # Umbreon
        470,  # Leafeon
        471,  # Glaceon
        700,  # Sylveon
        778,  # Mimikyu,
        568   # Trubbish
    ]
    mallow_present = GetRelationshipRank("May") >= 2
    kitchen_helpers = len(FoodBunnies()) + (2 if mallow_present else 1)
    enough_helpers = kitchen_helpers > 3
    kitchen_who = ("May and Mallow" if mallow_present else "May")
    kitchen_what = ("Retrieve" if enough_helpers else "Help")
    prime_security = ("Iono" if BunRecruit("Iono") else ("Nate" if BunRecruit("Nate") and not HasEvent("Nate", "JoinBunny") else ("Sonia" if BunRecruit("Sonia") else "Ethan")))
    if (HasEvent("Game", "BunnyRecruit")):
        AddEvent("Game", "AutoBunny")

    #setup for contests
    contestprioritylist = ["Melody", "May", "Mallow", "Whitney", "Rosa", "Nessa", "Ethan", "Nate", "Leaf"]
    contestproficiencydict = {
        "May": 312,
        "Mallow": 22,
        "Whitney": 210,
        "Rosa": 160,
        "Nessa": 130,
        "Ethan": 70,
        "Nate": 90,
        "Leaf": 26
    }
    contestpartnerdict = {
        "May": "Scorbunny", #coded in
        "Mallow": "Maractus",# coded in
        "Whitney": "Lopunny",# coded in
        "Rosa": "Pikachu",# coded in
        "Nessa": ("Feebas" if HasEvent("Nessa", "GaveFeebas") else "Azumarill"),#coded in
        "Ethan": "Pichu",# coded in
        "Nate": "Trubbish",# coded in
        "Leaf": "Diggersby"# coded in
    }
    coordinators = [CoordinatorGroup([Coordinator(first_name, condition=coordinatingknowledge, isprotag=True, contestsprite="bunny", iscontrollable=True)])]
    setascoordinators = []
    for bunny in contestprioritylist:
        if (len(coordinators) < 5):
            if (bunny not in ["Mallow", "Ethan", "May", "Nate", "Melody"] and BunRecruit(bunny) 
                or bunny == "Mallow" and HasEvent("May", "BunnyKitchen") and mallow_present
                or bunny == "May" and HasEvent("May", "BunnyKitchen")
                or bunny == "Nate" and HasEvent("Nate", "JoinBunny")
                or bunny == "Ethan" and not prime_security == "Ethan"):
                setascoordinators.append(bunny)
                coordinator = Coordinator(bunny, condition=contestproficiencydict[bunny], partner=GetTrainerTeam(bunny, contestpartnerdict[bunny]), contestsprite="bunny")
                coordinatorgroup = CoordinatorGroup([coordinator])
                coordinators.append(coordinatorgroup)
        else:
            break

scene blank2 with splitfade 

pause 0.5

if (BunRecruit("Game")):
    scene bunday with splitfade
else:
    scene academyhall with splitfade

menu:
    "{b}>Go [kitchen_what] [kitchen_who]{/b}" if BunRecruit("May") and not HasEvent("May", "BunnyKitchen"):
        jump BunnyKitchen
    
    "{b}>Check on Nate{/b}" if BunRecruit("Nate") and not HasEvent("Nate", "JoinBunny"):
        jump NateBunnyJoin

    "{b}[prime_security]'s got an update for you...{/b}" if not HasEvent("Melody", "BunnyHandled"):
        jump MelodyBunnyJoin

    "Huh? Looks like [prime_security] is calling..." if (BunRecruit("Game") and (prime_security == "Sonia" or prime_security == "Ethan" or prime_security == "Nate" and not HasEvent("Nate", "JoinBunny"))) and not HasEvent("Kris", "BunnyKrisCameo"):
        jump BunnyKrisCameo

    "Huh? [prime_security] looks concerned..." if (not BunRecruit("Game") and (prime_security == "Sonia" or prime_security != "Ethan" or prime_security == "Nate" and HasEvent("Nate", "JoinBunny"))) and not HasEvent("Kris", "BunnyKrisCameo"):
        jump BunnyKrisCameo

    "Huh? I hear footsteps..." if (not BunRecruit("Game") and prime_security == "Ethan") and not HasEvent("Kris", "BunnyKrisCameo"):
        jump BunnyKrisCameo

    "Nessa looks contemplative..." if BunRecruit("Game") and BunRecruit("Nessa") and not HasEvent("Nessa", "Boning"):
        jump NessaBoning

    "Whitney looks like she's drooling. Maybe I should look into that..." if BunRecruit("Game") and BunRecruit("Whitney") and not HasEvent("Whitney", "BunnyTalk") and not HasEvent("Whitney", "Whitney2Part2"):
        jump WhitneyBunnyTalk

    "Whitney looks subdued. Maybe I should look into that..." if BunRecruit("Game") and BunRecruit("Whitney") and not HasEvent("Whitney", "BunnyTalk") and HasEvent("Whitney", "Whitney2Part2"):
        jump WhitneyBunnyTalk

    "Rosa looks fidgety..." if BunRecruit("Game") and BunRecruit("Rosa") and not HasEvent("Rosa", "BunnyTalk"):
        jump RosaBunnyTalk

    "There's a chocolate fondue fountain?! Score!" if (BunRecruit("Game") and not HasEvent("Game", "BunnyFountain")):
        jump ChocolateBunnyFountain

    "Looks like someone's starting a dance-off...?" if (BunRecruit("Game") and not HasEvent("Game", "BunnyContest") and len(coordinators) == 5):
        jump BunnyContest

    "Leaf is ecstatically jumping from guest to guest." if (BunRecruit("Game") and not HasEvent("Game", "LeafBunnyFossils")):
        jump LeafBunnyFossils

    "Looks like someone's starting a battling tournament? Wait, HERE?!" if (BunRecruit("Game") and not HasEvent("Game", "Bunny Tournament")):
        jump BunnyTournament

    ">Watch the game of Cards Against Pokémonity..." if (BunRecruit("Game")):
        jump BunnyCardsAgainstPokemonity
        
    ">Change the party's music" if BunRecruit("Game"):
        jump Jukebox

    ">End the Party":
        jump AfterParty

label BunnyKitchen:
    scene blank2 with splitfade

    pause 0.5

    scene kitchen with splitfade

    $ PutRoff("May cookingclub apron")
    if (BunRecruit("Sonia")):
        $ PutLoff("Sonia nocoat")
    if (BunRecruit("Hilda")):
        $ PutRoff("Hilda")
    if (BunRecruit("Gardenia")):
        $ PutLoff("Gardenia")
    if (mallow_present):
        $ PutRoff("Mallow")
    $ PutLoff("Blue angrybrow frownmouth")
    $ LineUp()
    $ AddEvent("May", "SeenCooking")

    if (BunRecruit("Game")):
        $ GroupExpression("blush surprisedbrow frownmouth", exclude="blue")
        red @happy "Hey, everyb--"

        show blue:
            ease 0.5 xpos 0.5 ypos 1.2 zoom 1.3

        pause 0.5

        $ LineUp(exclude="blue", considerexcludes=True)

        show blue zorder 1000

        blue @angrybrow angrymouth "What the {i}hell{/i} do you think you're doing?"

        show gardenia flirtbrow lipbitemouth with dis

        if (enough_helpers):
            red @confused "Uh, I was going to retrieve [kitchen_who]--"

        else:
            red @confused "Uh, I thought I could help you guys out in the kitchen--"

        blue @talkingmouth "Dressed like {i}that?!{/i}"

        show gardenia happy with dis

        red @thonk "[ellipses]"

        $ SmartMoveOut("gardenia", exclude="blue", considerexcludes=True)

        red @talking2mouth "Okay, so most people would assume you're yelling at me because you have something against a man in a bunny suit, but I'm pretty sure since it's {i}you,{/i} you--"

        blue @talkingmouth "You've got so much goddamn exposed skin! And I {i}know{/i} you didn't wash your hands before coming in here! You don't even have your hat on, so your hair'll get {i}everywhere!{/i}"

        red @unamusedbrow frownmouth "[ellipses]"

        if (BunRecruit("Hilda") and BunRecruit("Sonia")):
            show hilda sadbrow -frownmouth
            show sonia sadbrow -frownmouth 
            with dis

            narrator "Hilda and Sonia look guiltily at each other."

        elif (BunRecruit("Hilda")):
            show hilda sadbrow -frownmouth with dis

            narrator "Hilda shrugs apologetically."

        elif (BunRecruit("Hilda") and BunRecruit("Sonia")):
            show sonia sadbrow -frownmouth with dis

            narrator "Sonia shrugs apologetically."

        red @talking2mouth "{size=30}The hypocrisy of this bunny.{/size}"

        if (enough_helpers):
            if (mallow_present):
                blue @talkingmouth "May, Mallow, get this walking biohazard out of here. I'll finish up your glaze."

                show may surprisedbrow talking2mouth
                show mallow surprisedbrow talking2mouth
                with dis

                TempCharacter("[ColoredTitle('May')] and [ColoredTitle('Mallow')]") "Yes, chef!"

                show may surprisedbrow frownmouth
                show mallow surprisedbrow frownmouth
                with dis                

                $ SmartMoveOut(["may", "mallow"], exclude="blue", considerexcludes=True)

                red @surprisedbrow frownmouth "[ellipses]"

                red @sadbrow talking2mouth "What did you do to those poor girls?"

                blue scaredeyes angryeyebrows furiousmouth "{size=40}{i}OUT!{/i}{/size}" 
            
            elif (mallow_present):
                blue @talking2mouth "May, get this walking biohazard out of here. I'll finish up your glaze."

                may @surprisedbrow talking2mouth "Yes, chef!"            

                $ SmartMoveOut("may")

                red @surprisedbrow frownmouth "[ellipses]"

                red @sadbrow talking2mouth "What did you do to that poor girl?"

                blue scaredeyes angryeyebrows furiousmouth "{size=40}{i}OUT!{/i}{/size}"

    else:
        red @happy "Hey, everyb--"

        $ GroupExpression("surprisedbrow frownmouth", exclude="blue")

        show blue zorder 1000:
            ease 0.5 xpos 0.5 ypos 1.2 zoom 1.3

        blue @angrybrow angrymouth "What the {i}hell{/i} do you think you're doing?"

        if (enough_helpers):
            red @confused "Uh, I was going to retrieve [kitchen_who]--"

        else:
            red @confused "Uh, I thought I could help you guys out in the kitchen--"

        blue @talking2mouth "I don't want to hear your dumbass reasoning! I want you {i}out{/i} of the kitchen!"

        red @confused "Why? I thought you wanted help?"

        blue @angrymouth "{size=30}You don't understand. I'm the {i}god{/i} of this kitchen. I yell at people to do things, and they actually {i}do{/i} them.{/size}"
        blue @closedbrow happymouth "{size=30}I've even had a couple people say my food was good, without your dumbass 'grey sludge' caveat.{/size}"

        red @confused "So[ellipses]?"

        blue @talking2mouth "{size=30}So there's {i}actually{/i} a small chance that I might have a good time during this pervert rabbit rumpus you threw, and I'm not having you mess it up by being here!{/size}"

        redmind @unamusedbrow unamusedmouth tired "If only he'd tell a {i}therapist{/i} that[ellipses]"

        if (enough_helpers):
            if (mallow_present):
                red @sweat talking2mouth closedbrow "Okay. I'll just grab the girls and get out of your hair."
                
                $ SmartMoveOut("mallow")

            else:
                red @sweat talking2mouth closedbrow "Okay. I'll just grab May and get out of your hair."

            $ SmartMoveOut("may")

        else:
            red @sweat talking2mouth closedbrow "Okay. I get you--I'll get out of your hair."

        blue -angrybrow -frownmouth @talking2mouth "Great. Thanks."

        pause 1.0

        show blue desperateeyes scaredeyebrows frownmouth with dis

        red @confused "Sorry, what was that?"

        blue embarrassedeyes embarrassedeyebrows @angrymouth "I didn't say anything."

        red @unamusedbrow talkingmouth "Really? 'Cause it {i}sounded{/i} like you said thanks."

        blue scaredeyes angryeyebrows furiousmouth "{size=40}{i}OUT!{/i}{/size}"

    scene blank2 with splitfadefaster

    narrator "Got away safely!"

    if (enough_helpers):
        
        pause 1.0
        
        if (BunRecruit("Game")):
            scene bunday 
            
            if (mallow_present):
                show may bunny:
                    xpos 0.66
                show mallow bunny:
                    xpos 0.33
                with splitfade

                may @talkingmouth "Thanks for saving us from Blue, [first_name]."

                red @talkingmouth "Hey, don't worry about it. I know how intense he gets."
                red @sweat talkingmouth "About everything."

                red @happy "Anyway, you worked hard to cook for this party. You should get to enjoy it, too."

                mallow @happy "We totally will! {i}Mahalo!{/i}"
                mallow @sadbrow talkingmouth "{size=30}I can't believe I got invited to a party[ellipses]{/size}"

                red @talkingmouth "Alright, you two have fun. I've gotta go take care of some of the other guests."

                mallow @talkingmouth "If you have a chance, try the garlic gougères! May and I made them."

                show may sadbrow blush with dis

                red @confusedbrow talkingmouth "Oh? May, that's not a meat--or a sweet."

                may @happybrow talkingmouth "No, I guess not. I was going to run it by you before trying it on Brendan, but Mallow was right there, so[ellipses]"

                show mallow surprisedbrow frownmouth with dis

                red @closedbrow talking2mouth "Damn Alolans. Taking our jobs."

                pause 1.0

                red @wince talking2mouth "Sorry, inappropriate?"

                mallow angrybrow -frownmouth @happy "Totally fine, as long as you recognize that a kid from {i}Kanto{/i} is complaining about a native Alolan taking {i}his{/i} job."

                red @sweat happy "I'm {i}sure{/i} that's a very cutting, witty, and topical political statement."

                mallow @surprisedbrow talking2mouth "Oh, you haven't heard? The Alolan job market is--"

                $ AddEvent("May", "RecapPromise")

                red @sweat sadbrow talkingmouth "Sorry, {i}really{/i} gotta go. Why don't you explain it to May? She can recap me in homeroom on Monday."

                mallow @talkingmouth "Hm? Sure. May?"

                may @talkingmouth "Yeah, I'd {i}love{/i} to hear! My Dad is actually {i}really{/i} interested in Alola."
                may @sadbrow talkingmouth "Is it alright if [first_name] and I just have a quick chat first, though?"

                mallow @talkingmouth "Huh? Oh, sure!"
                mallow @happy "{i}A hui hou no!{/i}"
                
                $ MoveOutSmart("mallow")

            else:
                show may bunny
                with splitfade

                may @talkingmouth "Thanks for saving me from Blue, [first_name]."

                red @talkingmouth "Hey, don't worry about it. I know how intense he gets."
                red @sweat talkingmouth "About everything."

                red @happy "Anyway, you worked hard to cook for this party. You should get to enjoy it, too."

                may @talkingmouth "I totally will! Thanks a bunch. Or maybe[ellipses]"
                may @flirtbrow talkingmouth "Thanks a bun-ch?"

                red @upeyes talking2mouth "Ugggggh."

                may @happy "No groaning! It's a punday bunday!"

                red @talking2mouth closedbrow "That's not even Japanese anymore. Go on, assault someone else with your puns."

            if (GetRelationshipRank("May") >= 1):
                may @sadbrow "[ellipses]"
                may @talkingmouth sadbrow "Truth be told, I'm kinda nervous."

                red @confused "Huh? Is it your suit?"

                may @sadbrow talkingmouth "No, the suit's great! Brendan made it--it's been a while since we used it, but it still fits like a charm."

                redmind @wince frownmouth "[ellipses]What does she mean by that? She's, like, eighteen-nineteen. 'Fits like a charm'[ellipses]?"

                may @talking2mouth "I'm nervous because I've made a ton of foods I've never tried before, and a bunch of people are going to be eating them[ellipses]"

                red @talkingmouth "Oh, you're worried that the food won't be as good as you're used to?"

                may @sadbrow talkingmouth "Maybe it's silly, but I've only ever run {i}this{/i} food by friends. They might have been sparing my feelings, like Brendan was, you know?"

                red @upeyes frownmouth "Hmm."
                red @happy "Alright, got it. A bunch of different people worked on the food for this party, right? It wasn't just you."

                may @talking2mouth "Um[ellipses] yeah."

                red @talkingmouth "Cool. So, with that said, let's just[ellipses]"

                show may surprisedbrow frownmouth with dis

                show bunday with vpunch

                red @happy "{size=40}Hey, y'all! We loving the food?!{/size}"

                $ PlaySound("crowd_cheer.ogg")

                if (BunRecruit("Nate") and HasEvent("Nate", "JoinBunny")):
                    show may bigblush with dis

                    $ MoveInRight("nate bunny happy")

                    nate @happy "It's buntastic!"

                if (BunRecruit("Nessa")):
                    show may bigblush with dis
                    $ MoveInLeft("nessa bunny closedbrow")

                    nessa @talkingmouth "I don't say this lightly--it's worth the calories."
                
                if (BunRecruit("Whitney")):
                    show may bigblush with dis
                    $ MoveInRight("whitney bunny")

                    whitney @happy "I {i}literally{/i} can't pull my face out of this cake!"
                
                if (BunRecruit("Rosa")):
                    show may bigblush with dis
                    $ MoveInLeft("rosa bunny")

                    rosa @winkbrow star talkingmouth "Everything on this table has the Rosa Whitley seal of approval!"

                $ MoveInRight("leaf")

                show may bigblush with dis

                leaf bunny @happy "I could open-mouth kiss whoever made these gougères."
                leaf @winkbrow talkingmouth "[first_name][ellipses]?"

                red @wince talking2mouth "Wasn't me, sorry."

                pause 1.0

                may @sadbrow talkingmouth "Thanks, [first_name]."

                red @winkbrow talkingmouth "Thanks for the food. Speaking of which--I think I hear some pretzel sticks calling my name."

        else:
            scene academyhall

            if (mallow_present):
                show may:
                    xpos 0.66
                show mallow:
                    xpos 0.33
                with splitfade

                $ LineUp()

                may @talkingmouth "Thanks for saving us from Blue, [first_name]."

                red @talkingmouth "Hey, don't worry about it. I know how intense he gets."
                red @sweat talkingmouth "About everything."

                red @happy "Anyway, you worked hard to cook for this party. You should get to enjoy it, too."

                mallow @happy "We totally will! {i}Mahalo!{/i}"
                mallow @sadbrow talkingmouth "{size=30}I can't believe I got invited to a party[ellipses]{/size}"

                red @talkingmouth "Alright, you two have fun. Changing rooms are inside."

                may @happy "See you!"

            else:
                show may
                with splitfade

                may @talkingmouth "Thanks for saving me from Blue, [first_name]."

                red @talkingmouth "Hey, don't worry about it. I know how intense he gets."
                red @sweat talkingmouth "About everything."

                red @happy "Anyway, you worked hard to cook for this party. You should get to enjoy it, too."

                may @talkingmouth "I totally will! Thanks a bunch. Or maybe[ellipses]"
                may @flirtbrow talkingmouth "Thanks a bun-ch?"

                red @upeyes talking2mouth "Ugggggh."

                may @happy "No groaning! It's a punday bunday!"

                red @talking2mouth closedbrow "That's not even Japanese anymore. Go on, assault someone else with your puns."

    $ AddEvent("May", "BunnyKitchen")

    jump BunnyPartyStart

label BunnyKrisCameo:
    if (BunRecruit("Game")):
        if (prime_security == "Iono"):
            show phone_B
            show iono happy:
                xpos 0.515 zoom 0.85 ypos 0.9
            show phone_A 
            with fadeinbottom

            iono @happy "Well, if it isn't my favorite chatter!"

            red @confused "It--it {i}isn't.{/i}"

            iono @closedbrow talking2mouth "We've got a crystal alert. Bogey moving in, T minus five."

            red @sadbrow talkingmouth "What does that {i}mean?!{/i}"

            iono @angry "It means you gotta get your {glitch=200.00}ass{/glitch} out into the hallway, buckaroo!"
            iono @sadbrow talking2mouth "You need to run interference. I could battle her, try to drive her off, but I make a habit of not getting into battles with people who could flunk me."

            hide phone_B
            hide iono
            hide phone_A
            with fadeoutbottom

            redmind @thonk "My[ellipses] my head hurts."

            $ BecomeContacted("Iono")

        elif (prime_security == "Nate"):
            if (not HasEvent("Nate", "JoinBunny")):
                show phone_B
                show nate suit frownmouth:
                    xpos 0.5
                show phone_A 
                with fadeinbottom

                nate @talking2mouth "Hey. Small update. Professor Cherry is moving towards us. I give her about three minutes until contact."

                red @closedbrow talking2mouth "Okay. You familiar with her?"

                nate @sadbrow talkingmouth "No more than anyone else."

                red @talking2mouth "Alright. I'll come out and see if I can defuse the situation."

                nate @closedbrow sweat talking2mouth "You sure? I could try to redirect her. Maybe convince her to forget about this."

                red @surprised "God, no!"
                red @happy sweat "Look, she's chill. If I explain what's happening--that it's all above-board, safe, and fun, then we should be fine."

                nate -frownmouth @talkingmouth "Alright, [nate_name]. Put that Frienergy to use, right?"

                red @sadbrow talkingmouth "I'd like to think I could do it even without my power[ellipses] but, yeah, Frienergy will probably help out here."

                nate @talking2mouth "I'll keep myself hidden, but I'll keep an eye on you two, in case you need reinforcements. Out."

                hide phone_B
                hide nate
                hide phone_A
                with fadeoutbottom

                pause 0.5

                $ BecomeContacted("Nate")

            else:
                show nate bunny with dis

                nate @talking2mouth "Hey. Small update. Professor Cherry is moving towards us. I give her about three minutes until contact."

                red @closedbrow talking2mouth "Okay. You familiar with her?"

                nate @sadbrow talkingmouth "No more than anyone else."

                red @talking2mouth "Alright. I'll go out there and see if I can defuse the situation."

                nate @closedbrow sweat talking2mouth "You sure? I could try to redirect her. {size=30}Maybe convince her to forget about this.{/size}"

                red @surprised "God, no!"
                red @happy sweat "Look, she's chill. If I explain what's happening--that it's all above-board, safe, and fun, then we should be fine."

                nate -frownmouth @talkingmouth "Alright, [nate_name]. Put that Frienergy to use, right?"

                red @sadbrow talkingmouth "I'd like to think I could do it even without my power[ellipses] but, yeah, Frienergy will probably help out here."

                nate @talking2mouth "I'll keep myself hidden, but I'll keep an eye on you two, in case you need reinforcements."

                red @talkingmouth "Sounds good."

                hide nate with dis

        elif (prime_security == "Sonia"):
            show phone_B
            show sonia frownmouth:
                xpos 0.52 zoom 0.95
            show phone_A 
            with fadeinbottom

            sonia @talking2mouth "Pardon me. I rather thought you should know--Professor Cherry will be here in about two minutes."

            red @closedbrow talking2mouth "Okay. Think you can head her off?"

            sonia @sadbrow talkingmouth "Not particularly, I'm afraid. I'm one of her students, after all, and[ellipses] I'd rather not incur her wrath."
            sonia -frownmouth @talkingmouth "Might your Frienergy be much better suited for this task?"

            red @sadbrow talkingmouth "I'd like to think I could do it even without my power[ellipses] but, yeah, Frienergy will probably help out here."

            sonia @talkingmouth "Splendid. I'll make myself scarce, then, but I'll be nearby if you need me. Just, er, shout, I suppose."

            hide phone_B
            hide sonia
            hide phone_A
            with fadeoutbottom

            $ BecomeContacted("Sonia")

        else:#ethan
            show ethan bunny surprisedbrow talking2mouth with vpunch

            ethan @talking2mouth "Hey, man, you need to get out there, {i}now{/i}!"

            red @surprised "Why? What happened?"

            ethan @talking2mouth "Kris is going to be here in, like, one minute."

            red @confused "Damn. Can't you[ellipses] I dunno, head her off?"

            ethan @angry "Anyone else? Sure! I just {i}look{/i} at people and they want to go the other direction. It doesn't work on Kris!"
            ethan @sadbrow talkingmouth "She was my {i}babysitter{/i}, man. I can't let her see me like this."

            red @closedbrow talking2mouth sweat "I hear you. I'll head out."

            ethan @wince angrymouth "Hurry!"

            scene blank2 with splitfadefast

        if (prime_security != "Ethan"):
            scene blank2 with splitfade
    
    else:
        scene academyhall with splitfade

        if (prime_security == "Iono"):
            show phone_B
            show iono happy:
                xpos 0.515 zoom 0.85 ypos 0.9
            show phone_A 
            with fadeinbottom

            iono @happy "Well, if it isn't my favorite chatter!"

            red @confused "It--it {i}isn't.{/i}"

            iono @closedbrow talking2mouth "We've got a crystal alert. Bogey moving in, T minus five."

            red @sadbrow talkingmouth "What does that {i}mean?!{/i}"

            iono @angry "It means you gotta get your {glitch=200.00}ass{/glitch} in gear, buckaroo!"
            iono @sadbrow talking2mouth "You need to run interference. I could battle her, try to drive her off, but I make a habit of not getting into battles with people who could flunk me."

            hide phone_B
            hide iono
            hide phone_A
            with fadeoutbottom

            redmind @thonk "My[ellipses] my head hurts."

            $ BecomeContacted("Iono")

        elif (prime_security == "Nate"):
            if (not HasEvent("Nate", "JoinBunny")):
                show nate suit frownmouth with dis

                nate @talking2mouth "Hey. Small update. Professor Cherry is moving towards us. I give her about three minutes until contact."

                red @closedbrow talking2mouth "Okay. You familiar with her?"

                nate @sadbrow talkingmouth "No more than anyone else."

                red @talking2mouth "Alright. I'll see if I can defuse the situation."

                nate @closedbrow sweat talking2mouth "You sure? I could try to redirect her. Maybe convince her to forget about this."

                red @surprised "God, no!"
                red @happy sweat "Look, she's chill. If I explain what's happening--that it's all above-board, safe, and fun, then we should be fine."

                nate -frownmouth @talkingmouth "Alright, [nate_name]. Put that Frienergy to use, right?"

                red @sadbrow talkingmouth "I'd like to think I could do it even without my power[ellipses] but, yeah, Frienergy will probably help out here."

                nate @talking2mouth "I'll keep myself hidden, but I'll keep an eye on you two, in case you need reinforcements. Good luck"

                $ MoveOutSmart("nate")

            else:
                show phone_B
                show nate bunny frownmouth:
                    xpos 0.5
                show phone_A 
                with fadeinbottom

                nate @talking2mouth "Hey. Small update. Professor Cherry is moving towards us. I give her about three minutes until contact."

                red @closedbrow talking2mouth "Okay. You familiar with her?"

                nate @sadbrow talkingmouth "No more than anyone else."

                red @talking2mouth "Alright. I'll see if I can defuse the situation."

                nate @closedbrow sweat talking2mouth "You sure? I could try to redirect her. Maybe convince her to forget about this."

                red @surprised "God, no!"
                red @happy sweat "Look, she's chill. If I explain what's happening--that it's all above-board, safe, and fun, then we should be fine."

                nate -frownmouth @talkingmouth "Alright, [nate_name]. Put that Frienergy to use, right?"

                red @sadbrow talkingmouth "I'd like to think I could do it even without my power[ellipses] but, yeah, Frienergy will probably help out here."

                nate @talking2mouth "Given how I'm dressed, you'll probably have more luck than me. Still, let me know if you need reinforcements. Out."

                hide phone_B
                hide nate
                hide phone_A
                with fadeoutbottom

                $ BecomeContacted("Nate")

        elif (prime_security == "Sonia"): 
            show sonia closedbrow frownmouth with dis

            sonia "{size=30}[ellipses]And you're sure? Soon. Right-o. Thanks bunches.{/size}"

            sonia @sadbrow "Pardon me. I rather thought you should know--Professor Cherry will be here in about two minutes."

            red @closedbrow talking2mouth "Okay. Think you can head her off?"

            sonia @sadbrow talkingmouth "Not particularly, I'm afraid. I'm one of her students, after all, and[ellipses] I'd rather not incur her wrath."
            sonia -frownmouth @talkingmouth "Might your Frienergy be much better suited for this task?"

            red @sadbrow talkingmouth "I'd like to think I could do it even without my power[ellipses] but, yeah, Frienergy will probably help out here."

            sonia @talkingmouth "Splendid. I'll make myself scarce, then, but I'll be nearby if you need me. Just, er, shout, I suppose."

            $ SmartMoveOut("sonia")

    scene academyhall with splitfade

    pause 0.5

    $ MoveInRight("kris angrybrow frownmouth")

    kris @talking2mouth "Right. What's going on here?"

    if (BunRecruit("Game")):
        pause 1.0

        kris @surprisedbrow "[ellipses]"
        kris @disappointedbrow talking2mouth "And what are you wearing?"

    menu:
        "Tell the truth.":
            pass

        "Lie out your [('ass' if profanity else '***')].":
            red @talking2mouth "Uh[ellipses]"

            pause 1.0

            narrator "You suddenly remember you are essentially incapable of doing that."

    if (BunRecruit("Game")):
        red @talking2mouth "Okay, I think I can answer your second question with my answer to your first one." 
        
    red @wince talking2mouth "Uh, there's a bunny-suit themed party happening in this classroom."

    pause 1.0

    red @talkingmouth "Nothing inappropriate's happening. Really."

    kris @closedbrow talking2mouth "A party where everyone's dressed up in bunny suits is {i}inherently{/i} inappropriate for a school environment, [first_name]."

    red @sadbrow talkingmouth "We're not breaking any school rules."

    kris @disappointedbrow talking2mouth "Really. So there's no alcohol? No-one's being pressured into anything they aren't ready for? And you're planning on wrapping this whole thing up, and sending everyone home, before curfew?"

    pause 1.0

    red @talking2mouth "There's no alcohol. We seriously did our best to ensure that only people who {i}really{/i} wanted to be there ended up there."
    red @closedbrow sweat talking2mouth "And curfew is[ellipses] not a great rule. I mean, it's a college."

    pause 0.5

    show kris at getcloser

    redmind @wince frownmouth "What is she[ellipses]?"
    
    pause 0.5

    kris noglasses @talking2mouth "Look me in the eyes and swear to me that you, and {i}all{/i} the kids in there, are making safe, {i}sane{/i} choices."

    pause 0.5

    red @sadbrow talkingmouth "Absolutely, Professor Cherry. I swear. One hundred percent."

    pause 0.5

    show kris glasses with dis

    pause 0.5

    show kris at getfurther

    kris @angrybrow frownmouth "[ellipses]"
    kris @talking2mouth "I have half a mind to spin right around and report you all to Dean Drayden."

    pause 1.0

    kris @pissedbrow talking2mouth "But[ellipses] I'll let you off this time with a {i}very{/i} strong warning. You better {i}fully{/i} appreciate just how strong this warning is, [first_name]. If I see you stepping {i}one{/i} toe out of line after this, then you're sunk."

    red @sadbrow talkingmouth "Thank you very much. We really appreciate--"

    kris @talking2mouth "Also, I'm going to come back in ten minutes with a bowl of condoms. Put it in the middle of the room."

    red @wince talking2mouth "Oh, god, please don't. No-one's doing anything like that, and--"

    kris @pissedbrow pissedmouth "Do you know every single person at the party?! Can you swear on {i}someone else's{/i} future academic life and career that {i}no-one's{/i} going to make like a bunny {i}at your bunny party?!{/i}"

    redmind @downeyes noshine frownmouth "This is the most mortifying conversation I've ever been part of."
    red @downeyes noshine talking2mouth "No, Professor. I don't know everyone. And I can't swear that."

    kris @talking2mouth "Exactly. All of you are way too young to be able to afford mistakes like that. There's no re-dos. If something changes your life, it changes your life {i}forever.{/i} Don't let your hormones cut branches off your future."

    red @downeyes noshine talking2mouth "Yes, Professor."

    kris @talking2mouth "I'm serious, [first_name]. If any of my kids have a baby bump when I hand them their diploma, I'm holding you {i}personally{/i} responsible."

    red @downeyes noshine talking2mouth "That won't be necessary, Professor."

    kris "[ellipses]"
    kris @talking2mouth "Don't tell anyone about this. Your party, or that I was here. I could get in a lot of trouble for {i}not{/i} stopping you kids."

    red @downeyes noshine talking2mouth "Yes, Professor."

    kris @talking2mouth "Wait here."

    scene blank2 with splitfade

    narrator "Professor Cherry, mercifully, departs."

    redmind @downeyes frownmouth noshine "[ellipses]"
    redmind @upeyes "Why do I feel like I just got chewed out by Mom[ellipses]?"

    pause 1.0

    narrator "Professor Cherry returns with the promised bowl, the pink and purple wrappers alluding to ecstasies and delights that no longer seem {i}quite{/i} so appealing."

    if (BunRecruit("Game")):
        narrator "You perform the long walk of shame to place the bowl in the center of the room. You can feel everyone's eyes burning on your skin[ellipses]"
        narrator "On the bright side, wearing a bunny suit hardly registers as an embarrassment anymore."

    else:
        narrator "You hand the bowl off to a late arrival to the party, and try to put the whole thing out of your mind."

    if (prime_security == "Sonia"):
        sonia @talking2mouth "Er[ellipses] well done defusing that. She's rather protective of her students."

    elif (prime_security == "Nate"):
        if (HasEvent("Nate", "JoinBunny")):
            nate bunny @talking2mouth "I did some research on her while you were fighting her off."
            nate @talking2mouth "According to her RateMyProfessor page, she's, uh, known to be a bit protective of her students."

        else:
            nate suit @talking2mouth "I did some research on her while you were fighting her off."
            nate @talking2mouth "According to her RateMyProfessor page, she's, uh, known to be a bit protective of her students."

    elif (prime_security == "Iono"):
        show phone_B
        show iono happy:
            xpos 0.525 zoom 0.9 ypos 0.9
        show phone_A 
        with fadeinbottom

        iono @happy "So, maaaaaaaybe I should've warned you that she tends to Mommy her students?"

    else:
        ethan bunny @talking2mouth "Sorry, man. Should've warned you. She's pretty young, so she remembers what it was like to be our age, and making bad decisions all the time."
        ethan @happy "She gets pretty intense about protecting her kids' futures."
       
    red @downeyes noshine talking2mouth "I noticed."

    $ AddEvent("Professor Cherry", "BunnyKrisCameo")

    jump BunnyPartyStart

label NessaBoning:
    show nessa bunny with dis

    nessa @talking2mouth "Hey."

    red bunny @talkingmouth "Hey. Enjoying the party?"

    nessa @talking2mouth "Yeah."

    pause 1.0

    nessa @talkingmouth "Yeah. I haven't had a lot of chances to really unwind and de-stress like this. Wear what I want for a while."

    nessa @talkingmouth closedbrow "Thanks. To you and the others."

    red @talkingmouth "Not a problem."

    pause 0.5

    red @surprisedbrow talkingmouth "Oh! Your suit. Here, let me--"

    show nessa surprisedbrow frownmouth at getcloser with dis

    pause 0.2

    show nessa closedbrow frownmouth at getfurther with dis

    nessa @talking2mouth "Hey. Words, not hands?"

    red @surprisedbrow frownmouth "[ellipses]"
    red @sweat closedbrow talking2mouth "Sorry."

    nessa -closedbrow @talking2mouth "It's fine. What was it?"

    red @talkingmouth "Uh, one of your[ellipses] strap-things is disconnected."

    nessa @closedbrow talkingmouth "Oh, yeah. That's intentional."

    red @confused "Really? Er[ellipses] {i}why{/i}?"

    pause 0.5

    nessa @talking2mouth "Do you watch much TV?"

    red @sadbrow talkingmouth "Mostly just old movies. Brycen stuff."

    nessa @closedbrow talking2mouth "Alright. Anyway, there was a costume designer for an old sci-fi show named Ware Theiss--"

    red @happy "There was a costume designer named 'Ware'?"

    nessa @closedbrow talkingmouth "He makes a strong case for nominative determinism."
    nessa @closedbrow talkingmouth "But he's not the most egregious example. I worked in a Water-type gym, and my name is Nessa. Sunny's got a classmate named Flannery who's--get this--a Fire-type Gym Leader."

    if (BunRecruit("Whitney")):
        $ MoveInRight("whitney bunny")

        whitney @talkingmouth "Did someone say something about Flannery?"

        nessa @talking2mouth "Just in passing."

        whitney @talking2mouth "Oh.{w=0.5} Okay."

        $ MoveOutSmart("Whitney")

    else:
        red @talking2mouth "[ellipses]Huh."

    nessa @talking2mouth "Anyway, Theiss came up with this idea called the Theiss Titillation Theory. Or the Triple-T, in the industry."

    red @talkingmouth "I'm[ellipses] intrigued, but my original question was about the strap on your suit, in case we lost the track."

    nessa @closedbrow talkingmouth "No, I remember. We get there when we get there. Be patient, [first_name]."

    red @happy "Alright, I'll continue to wait with bated breath."

    nessa @talkingmouth "His theory states that the sexiness of an outfit is directly proportional to how likely it is that some vital part of it will fall off."

    pause 1.0

    red @talking2mouth "Huh. So the loose strap is meant to imply[ellipses]"

    nessa @talkingmouth "Yeah. Of course, there's no chance that any outfit I had a hand in would {i}actually{/i} fall apart, but the implication is sexier than anything else could be."
    nessa @sadbrow talkingmouth "It's one of those 'imagination is always better than reality' situations."

    red @talking2mouth "That's[ellipses] huh. I'll be honest, I never really thought about it like that."

    nessa @talking2mouth "No-one does. I'd like to say being a model is a more complicated job than people think it is, but[ellipses]"
    nessa @sadbrow talkingmouth "Being honest, I don't {i}need{/i} to know any of what I just told you. I just find that part of the job interesting."
    nessa sadbrow @closedbrow talkingmouth "Maybe when I'm too old to be a model, I'll get into clothing design."

    red @sadbrow "[ellipses]"

    show nessa -sadbrow with dis

    red @happy "Well, I've got another question. If you've got the time."

    nessa @talkingmouth "Sure."

    red @talkingmouth "If the outfit absolutely {i}won't{/i} fall off--how do you make sure it doesn't fall off without both straps?"

    nessa @happy "Fabric glue, doubled-sided tape, and enough boning that this suit would probably stand up without me in it."

    red @lightblush surprisedbrow talking2mouth "Beg pardon?"

    nessa @flirtbrow talkingmouth "Don't tell me you don't know what boning is, [first_name]?"

    if (len(dateabase["Casual Entanglements"]) + len(dateabase["Romantic Entanglements"]) > 0):
        red @lightblush sad2brow talking2mouth "Uh--no, I, er, I'm aware of the {i}concept{/i}, but, er--"

    else:
        red @lightblush angrybrow talking2mouth "I can assure you I do. But, uh, just so we're on the same page--"

    nessa @talkingmouth "'Boning' is putting rigid plates of some sort of material in the costume to prevent it from bending, and to give it structure that fabric won't have by itself."

    if (BunRecruit("Whitney")):
        $ MoveInRight("whitney bunny")

        whitney @talkingmouth "Are we talking about tailoring now? Did you know it's called 'boning' because the plates used to be made of Wailmer bone?"

        pause 1.0

        nessa @talkingmouth "Yes."

        pause 0.5

        whitney @talking2mouth "Oh. Okay."

        $ MoveOutSmart("Whitney", duration=2.0)

        red @sadbrow talkingmouth "I didn't!"

        red @talking2mouth "Anyway, I getcha now. That's, uh, different from what I was thinking."
    
    else:
        nessa @closedbrow talkingmouth "It's called boning because the plates used to be made of whalebone."

        red @talking2mouth lightblush closedbrow "Ah. That's different from what I--yeah, I getcha now."

    nessa flirtbrow @talkingmouth "Hm. What {i}were{/i} you thinking?"

    red @lightblush upbrow talking2mouth "I think we both know how the average person would interpret the word 'boning,' if they didn't have any other context."

    nessa "[ellipses]"
    nessa -flirtbrow @sadbrow talkingmouth "You're not as easy to tease as most people I talk to. They normally get all flustered and red-faced and insist they are beacons of purity and have never had a sexual thought in their life."
    
    red @sadbrow talkingmouth "I don't think I've ever seen you tease someone before. Is this something you do often?"

    nessa @flirtbrow talkingmouth "Only when I'm having fun."

    red @happy "I'm glad to hear you're having fun now, then."
    red @upeyes confusedeyebrows frownmouth "[ellipses]"
    red @confused "Although the implications of this are[ellipses]"

    nessa @sadbrow talkingmouth "Don't worry about that."

    if (GetRelationshipRank("Nessa") > 0):
        pause 1.0

        show nessa at getcloser
        
        nessa @talking2mouth "{size=30}How's Leaf doing?{/size}"

        red @talking2mouth "{size=30}Rough at first. We didn't think this through super-well. But I think she's doing better now.{/size}"

        nessa @talking2mouth "{size=30}Good.{/size}"

        show nessa at getfurther

        pause 1.0

        show nessa sadbrow -frownmouth with dis

        nessa @talking2mouth "I don't have the context of what happened. I don't want to point fingers."
        nessa @talking2mouth "But, as a model, no-one should ever be ashamed to wear what they want. Leaf was, and it looks like, now, she's not."
        nessa @talkingmouth "Maybe the flimsier an outfit is, the {i}sexier{/i} it is--but I think what makes an outfit beautiful is how much {i}fun{/i} the wearer is having."

        red @happy "You know, I bet Leaf would like to hear that from you personally."

        nessa @talkingmouth "I'm sure she would. Might even do it, if I feel like it."

        red @tiredbrow talkingmouth "Alright. You have fun--I've gotta check in on some of the other guests."

        nessa surprisedbrow frownmouth @talking2mouth closedbrow "Cheerio."

        pause 2.0

        nessa @sadbrow talkingmouth "Ugh, I'm {i}such{/i} a Galarian."

    else:
        nessa @talkingmouth "Thanks for the party."

    hide nessa with dis

    $ AddEvent("Nessa", "Boning")

    jump BunnyPartyStart

label Jukebox:
    narrator "It looks like there are several different partyguests who would enjoy putting on their music[ellipses]"

    menu JukeBoxMenu:
        ">Give Rosa the AUX cord" if BunRecruit("Rosa"):
            stop music fadeout 1.5
            queue music "audio/music/joinavenue_start.ogg" noloop
            queue music "audio/music/joinavenue_loop.ogg"

            $ bunnypartybgm = ("audio/music/joinavenue_start.ogg", "audio/music/joinavenue_loop.ogg")

            show screen songsplash("Join Avenue", "Zame")

            rosa bunny @talkingmouth "Oh? Sure! Here's one of my favorite tunes--it plays at all the Join Avenues all across the world!"

            pause 1.0

            rosa @angrybrow talkingmouth "Yes, it's mall music! What's wrong with that?"

        ">Give Nessa the AUX cord" if BunRecruit("Nessa"):
            stop music fadeout 1.5
            queue music "audio/music/LoFiMaxRaidBattle_start.ogg" noloop
            queue music "audio/music/LoFiMaxRaidBattle_loop.ogg"

            $ bunnypartybgm = ("audio/music/LoFiMaxRaidBattle_start.ogg", "audio/music/LoFiMaxRaidBattle_loop.ogg")

            nessa bunny @talkingmouth "Sure. This might be a little low-tempo for this party's vibe, but try it out anyway."

        ">Give May the AUX cord" if HasEvent("May", "BunnyKitchen"):
            stop music fadeout 1.5
            queue music "Audio/Music/RSE_Rival_start.ogg" noloop
            queue music "Audio/Music/RSE_Rival_loop.ogg"

            $ bunnypartybgm = ("Audio/Music/RSE_Rival_start.ogg", "Audio/Music/RSE_Rival_loop.ogg")

            may bunny @talkingmouth "Alright! Here's a song I like--Brendan composed it!"

        ">Give Mallow the AUX cord" if HasEvent("May", "BunnyKitchen") and mallow_present:
            stop music fadeout 1.5
            queue music "Audio/Music/alolaencounter_intro.ogg" noloop
            queue music "Audio/Music/alolaencounter_loop.ogg"

            $ bunnypartybgm = ("Audio/Music/alolaencounter_intro.ogg", "Audio/Music/alolaencounter_loop.ogg")

            mallow bunny @talkingmouth "{i}Nui!{/i} This is an old, traditional, Alolan song."

            pause 3.0

            red @confused "Played on a[ellipses] synthesized flute?"

            mallow @talkingmouth "Sure. We have more than just ukulele music."

        ">Give Nate the AUX cord" if BunRecruit("Nate") and HasEvent("Nate", "JoinBunny"):
            stop music fadeout 1.5
            show screen songsplash("Sinis Trio", "Zame")
            queue music "audio/music/natetheme_start.ogg" noloop
            queue music "audio/music/natetheme_loop.ogg"

            $ bunnypartybgm = ("audio/music/natetheme_start.ogg", "audio/music/natetheme_loop.ogg")

            nate bunny @talkingmouth "This one's a classic. The Go-Rock Quads did this one!"

            pause 1.5

            nate @unamusedbrow talking2mouth "No recognition, huh?"

        ">Iono just sent you a file...?" if BunRecruit("Iono"):
            play music "audio/music/mybetterworld.ogg"

            $ bunnypartybgm = ("audio/music/mybetterworld.ogg", "audio/music/mybetterworld.ogg")

            narrator "The moment you open Iono's text, it deletes itself, and the music on the speakers changes."
            narrator "Your phone wasn't even connected to them[ellipses]"

        ">Give Leaf the AUX cord":
            stop music fadeout 1.5
            queue music "Audio/Music/Cinnabar_Start.ogg" noloop
            queue music "Audio/Music/Cinnabar_Loop.ogg"
            
            $ bunnypartybgm = ("Audio/Music/Cinnabar_Start.ogg", "Audio/Music/Cinnabar_Loop.ogg")

            leaf bunny @talkingmouth "Hm? Yeah, sure, take my phone! Just don't look in the photo roll."

            red @thonk "[ellipses]I mean, I wasn't going to, but now[ellipses]"

        ">Give Ethan the AUX cord" if prime_security != "Ethan":
            stop music fadeout 1.5
            queue music "Audio/Music/tension_start.ogg" noloop
            queue music "Audio/Music/tension_loop.ogg"
            
            $ bunnypartybgm = ("Audio/Music/tension_start.ogg", "Audio/Music/tension_loop.ogg")

            narrator "Ethan gives you a strange, smirking look."

        ">Put on some edgy club music":
            stop music fadeout 1.5
            queue music "Audio/Music/silphco_intro.ogg" noloop
            queue music "Audio/Music/silphco_loop.ogg"
            
            $ bunnypartybgm = ("Audio/Music/silphco_intro.ogg", "Audio/Music/silphco_loop.ogg")

            narrator "The guests seem surprised, at first, but soon start dancing. The mood gets tenser."
        
        "You hear Sabrina's thoughts..." if GetRelationshipRank("Sabrina") > 0:
            stop music fadeout 1.5

            redmind @thonk "[sabrinacolor][ellipses]Look up {i}this{/i} song on the internet."

            queue music "Audio/Music/lavenderintense_start.ogg" noloop
            queue music "Audio/Music/lavenderintense_loop.ogg"
            
            $ bunnypartybgm = ("Audio/Music/lavenderintense_start.ogg", "Audio/Music/lavenderintense_loop.ogg")

            if (BunRecruit("Rosa") and BunRecruit("Nessa")):
                narrator "Following Sabrina's instruction, you find the song, and hook it up to the speakers. Rosa and Nessa catch your eye and smile knowingly."

            elif (BunRecruit("Rosa")):
                narrator "Following Sabrina's instruction, you find the song, and hook it up to the speakers. Rosa catches your eye and smiles knowingly."
                
            elif (BunRecruit("Nessa")):
                narrator "Following Sabrina's instruction, you find the song, and hook it up to the speakers. Nessa catches your eye and smiles knowingly."

            else:
                narrator "Following Sabrina's instruction, you find the song, and hook it up to the speakers."

        ">Play the original music":
            stop music fadeout 1.5
            queue music "audio/music/viridianforest_start.ogg" noloop
            queue music "audio/music/viridianforest_loop.ogg"

            $ bunnypartybgm = ("audio/music/viridianforest_start.ogg", "audio/music/viridianforest_loop.ogg")

        ">Leave the music as-is":
            jump BunnyPartyStart

    jump JukeBoxMenu

label NateBunnyJoin:
    redmind @thinking "You know[ellipses] Nate said he wanted to join the party, right?"
    redmind @thonk "He doesn't want to be standing outside the whole time, probably. Maybe I should check on him."

    narrator "No sooner has the thought crossed your mind, then you see the door to the party room open, and a black-suited figure enters[ellipses]"

    $ SmartMoveIn("nate suit")

    nate @talkingmouth "Hey, [nate_name]. Decided my shift's over."
    nate flirtbrow @talkingmouth "You good with that?"

    red @talkingmouth "I mean, sure, man. I can take over for you. Just let me--"

    $ SmartMoveIn("leaf bunny blush")

    show bunday with vpunch

    leaf @happy "Nate, oh my god, did you forget about the {i}bunny{/i} part of bunny suit party?"

    ethan bunny @talkingmouth "Yeah, man, they're meant to be bunny suits, not monkey suits."

    nate @happy "First: killer pun acknowledged. Nice."
    nate smirkmouth @talkingmouth "Secondly--I've got a replacement in mind. Let me just get changed first."

    red @talkingmouth "Huh? Sure. There's a bathroom over there. Just one stall, bit of a tight squeeze, but it's private, so[ellipses]"

    pause 1.0

    red @talkingmouth sweat "I don't know what that look is about, but I kinda get the feeling you have a different plan in mind."

    nate @winkbrow talkingmouth "Clear the stage. I'm about to disappoint my Dad."

    red @confused "The stage? What do you[ellipses]"

    show nate:
        ease 0.5 xpos 0.5 ypos 0.95 zoom 0.9

    $ SmartMoveOut("Leaf", exclude="nate")

    pause 0.5

    narrator "Nate struts to the center of the room."
    narrator "[ellipses]The chatter of the party quiets as the partygoers notice Nate standing there."

    show blank2 behind nate with superslowdis:
        alpha 0.4

    show lightbeam1 with slowdis:
        zoom 0.6 alpha 0.5 yalign 0.9 xalign 0.5

    TempCharacter("Buxom Bunny") "Hey, dude, aren't you a bit overdressed?"

    TempCharacter("Regretful Rabbit") "{size=30}Who is that guy? He's cute, but[ellipses]{/size}"
    
    TempCharacter("Leering Lepus") "Wasn't he the bouncer? You know, outside the party? Did something happen?"

    show nate closedbrow with dis

    narrator "Nate puts his hand into his jacket[ellipses]"

    show nate sweat with dis

    narrator "Tenses[ellipses]"

    pause 1.0

    show nate suitnocoat lightblush angrybrow happymouth with dis:
        xpos 0.5 xzoom 1 ypos 0.95 zoom 0.9
        ease 0.4 xpos 0.52 xzoom -1
        pause 0.3
        ease 0.4 xpos 0.48 xzoom 1
        ease 0.2 xpos 0.5

    narrator "And whips the jacket off, sending it flying into a group of startled rabbits."

    redmind @surprisedbrow heavyblush frownmouth "OH.{w=0.5} {i}That's{/i}--that's what he's doing."

    $ PlaySound("crowd_cheer.ogg")

    show nate flirtbrow smirkmouth with dis

    nate @talkingmouth "I was going to ask if you were liking what you see, but I think I got my answer."

    show nate:
        xpos 0.5 ypos 0.95 zoom 0.9 xzoom 1
        ease 0.5 xpos 0.33 ypos 1.0 zoom 1.0 xzoom -1

    nate @closedbrow happymouth "Just you wait. You haven't seen anything yet--I've got a {i}lot{/i} more layers to go through."

    $ PlaySound("crowd_cheer.ogg")

    nate @talkingmouth "Although, who knows[ellipses] maybe I'm feeling shy. I dunno, should I stop?"

    narrator "Nate's eyes scan the crowd with mechanical precision, locking onto one bunny-suit-clad woman who was doing a fairly accurate impression of a wolf from an old cartoon."

    TempCharacter("Buxom Bunny") "Dude, if you do, I will {i}literally{/i} cry."

    show nate:
        xpos 0.33 ypos 1.0 zoom 1.0 xzoom -1
        parallel:
            ease 0.5 xpos 0.5 ypos 0.95 zoom 0.9
        parallel:
            ease 0.25 xzoom 1
            ease 0.25 xzoom -1

    nate @winkbrow talkingmouth "Roger. Don't want that!"

    show nate halfbunny:
        xpos 0.5 ypos 0.95 zoom 0.9 xzoom -1
        ease 0.5 xpos 0.66 ypos 1.0 zoom 1.0 xzoom 1

    nate @winkbrow talkingmouth "Did I say a {i}lot{/i} more layers? I meant one." 
    nate surprisedbrow frownmouth @flirtbrow talkingmouth "Just one more layer, and I'm all yours--the rabbit of your fantasies. Now, do you--"

    show bunday with vpunch

    TempCharacter("Various Rabbits") "{size=40}YEEEEEESSSSSS!{/size}"

    show nate flirtbrow smirkmouth with dis

    show nate:
        xpos 0.66 ypos 1.0 zoom 1.0 xzoom 1
        parallel:
            ease 0.5 xpos 0.5 ypos 0.95 zoom 0.9
        parallel:
            ease 0.25 xzoom -1
            ease 0.25 xzoom 1

    TempCharacter("{size=23}Uncomfortable Hetero Guy Who is Nevertheless Doing His Best to Keep up the Mood{/size}") "{size=30}[ellipses]Yeah, woo. And, uh, if any chicks wanna follow this guy's example[ellipses]{/size}"

    nate @winkbrow talkingmouth "This is it, then. I'm taking it {i}all{/i} off. You ready?"

    $ PlaySound("crowd_cheer.ogg")

    show bunday with vpunch

    TempCharacter("Various Rabbits, Frothing at the Mouth") "{size=50}YEEEEEESSSSSS!{/size}"

    $ autoquote = False

    nate @winkbrow talkingmouth "\"Then here{w=0.5}"

    show blank

    pause 0.05

    hide blank
    show nate:
        xpos 0.25 ypos 1.2 zoom 1.3

    extend @winkbrow talkingmouth " we{w=0.5}"

    show blank

    pause 0.05

    hide blank
    show nate:
        xpos 0.75 ypos 1.2 zoom 1.3 xzoom -1

    extend @winkbrow talkingmouth " go{w=0.5}!\""

    $ autoquote = True

    show blank

    pause 0.05

    hide blank
    show nate:
        xpos 0.5 ypos 1.2 zoom 1.3 xzoom -1

    pause 1.0

    show nate bunny with Dissolve(5.0):
        xpos 0.5 ypos 1.2 zoom 1.3 xzoom -1
        parallel:
            ease 5.0 ypos 0.95 zoom 0.9
        parallel:
            ease 0.333 xpos 0.65
            ease 0.333 xpos 0.5
            ease 0.333 xpos 0.35
            ease 0.333 xpos 0.5
            repeat 4
        parallel:
            ease 0.5 xzoom 1
            ease 0.5 xzoom -1
            repeat 7

    pause 1.0

    red @heavyblush surprisedbrow frownmouth "[ellipses]"

    show nate:
        xzoom -1 zoom 1.0

    nate @talkingmouth "Sick party, right, everybunny?"

    $ PlaySound("crowd_cheer.ogg")

    pause 1.0

    nate @happy "Alright, alright. Now, no touching--not yet, anyway. I've got something to do first."

    pause 0.5

    show nate at getcloser

    pause 0.5

    nate @talkingmouth "[nate_name]."

    red @talkingmouth "I'm not sure where to look."

    nate @winkbrow talkingmouth "Anywhere you want?"

    red @talkingmouth "I, uh, I don't really know how to carry on this conversation."

    nate -flirtbrow -smirkmouth -sweat @happy "That's alright. I'm going to speak to MC² now, anyway."

    red @talkingmouth "Really? What about?"

    nate @talking2mouth closedbrow sweat "Well, I want to apologize for some stuff[ellipses]"
    nate @talkingmouth sad2brow "But I also want to convince him to take guard duty for a while, so I can join the party."

    red @surprisedbrow frownmouth "[ellipses]"
    red @confused "In a bunny suit?"

    nate @unamusedbrow talkingmouth "I'll admit I've never done this before, but I'm pretty sure the bunny suit is only going to make apologizing and convincing {i}easier{/i}."
    if (BunRecruit("Sonia")):
        nate @closedbrow talking2mouth "But if the suit doesn't work, and I've lost my touch, S owes me a favor, so I can check in with her."

    redmind @thonk "[ellipses]Make apologizing and convincing easier[ellipses]?"

    menu:
        "You dog. Get in there!":
            $ AddEvent("Nate", "EthanSupport")
            nate @winkbrow talkingmouth "And here I was trying to make you jealous."
            nate @happy "There's time yet, I guess, and I'm going to make the most of mine."

            jump postnatebunnyconfrontationconfess

        "What do you mean by that?":
            pass

        "I won't ask.":
            nate happy "Then I won't tell."

            jump postnatebunnyconfrontationconfess

    red @sad2brow talking2mouth sweat "Uh, when you say 'apologizing' and 'convincing[ellipses]'"

    nate @talking2mouth "I don't have any plans. But whatever happens, happens."
    nate @surprisedeyebrows poutmouth upeyes "[ellipses]"
    nate @surprisedbrow talking2mouth "Wait, he likes guys, right? I just assumed, because of {i}his{/i} bunny suit."

    red @sigh "Last I checked."

    nate @confused "You've checked?"

    red @upeyes angryeyebrows talking2mouth "Not like {i}that!{/i}"

    nate @confused "Then there's no problem, is there?"

    label NateProblem:

    menu:
        "You're the problem.":
            show nate surprisedbrow frownmouth with dis

            nate @talking2mouth "Wait. You mean[ellipses] you don't want {i}me{/i} to get with someone else?"

            if (GetRelationshipRank("Nate") > 0):
                narrator "Nate's lips are slightly parted in shock. His bare chest rises and falls quickly--not from the exertion of his dance, which barely seemed to tire him, but from something else." 
                narrator "He looks at you with an emotion quite dissimilar to any you've seen him wear before. {i}Fear.{/i}"
                narrator "Fear of what you might say--fear of what you might not say."
                narrator "[bluecolor]You suspect this is a moment of incredible importance for your relationship's future[ellipses]{/color}"

            menu:
                "[bluecolor][[Nate Rank 1]{/color} That's what I mean." if (GetRelationshipRank("Nate") > 0):
                    $ AddEvent("Nate", "Confess")

                    pause 1.0

                    show nate lightblush with Dissolve(1.0)

                    nate @sad2brow talkingmouth "Ah, geez, [first_name[:3]]--[nate_name]. I didn't think I had a sense of embarrassment left. I mean, look at what I'm wearing!"

                    pause 0.5

                    nate @sad2brow talkingmouth "Well, I hear you. Uh, loud and clear. Message received. Over! Hahaha[ellipses]"

                    red @sigh "I'm sorry. I just blurted that out without thinking about it."

                    nate -surprisedbrow -frownmouth @sadbrow talkingmouth "No, that's[ellipses] good. Uh, good to know."

                    pause 1.0

                    nate @sadbrow talkingmouth "Is it because of the suit?"

                    red @sad2brow talkingmouth "I don't think it's the suit. Maybe a little bit?"

                    pause 0.5

                    nate @closedbrow talking2mouth "Well, shit. What's the standard operating procedure here[ellipses]?"

                    pause 0.5

                    nate @sad2brow talkingmouth "{size=30}Well, last time this happened, they made me wipe the poor girl, change my name, my face, and my region.{/size}"
                    nate @sigh "{size=30}That won't work this time, though.{/size}"

                    red @surprisedbrow talking2mouth "{size=30}Um[ellipses] should I be concerned?{/size}"

                    nate @talking2mouth unamusedbrow "{size=30}No more than you should have been before.{/size}"

                    red @sigh "{size=30}Great.{/size}"

                    pause 1.0

                    nate @talking2mouth "Hey, so, making sure we're all above-board here, I like you. I think you've got a great personality, and an awesome body. But[ellipses] you know who I am."
                    nate @sadbrow talkingmouth "{i}What{/i} I am. What I need to do. And where I'll go when I'm done."

                    red @sad2brow frownmouth "[ellipses]"
                    red @talkingmouth sadbrow "Yeah."

                    nate @confused "And[ellipses]"

                    red @talkingmouth sadbrow "I said what I said. You can't make me forget it; I can't make you forget it. So I guess we've both just got to own it."

                    nate @sad2brow talkingmouth "Uh[ellipses] okay. Okay, I think that we need to, uh[ellipses] discuss this. Later. Just[ellipses] give me a chance to process? Sift through the data?"

                    red @sadbrow talkingmouth "Sure."

                    nate @frownmouth "[ellipses]"
                    nate @surprisedbrow talking2mouth "Oh, right, the MC² thing."

                    red @sigh "Right. That thing."

                    nate @talkingmouth "Well, uh, I think I'll still, you know, apologize and ask him to switch places with me[ellipses]"
                    nate sadbrow lightblush neutralmouth @talkingmouth "But maybe whatever happens[ellipses] won't happen."

                    red @talking2mouth "Yeah. Let's just[ellipses] enjoy the rest of the party, and talk about this later. We're cool?"

                    nate @talkingmouth "As ice."

                    hide nate with Dissolve(2.0)

                    narrator "You and Nate part ways, awkwardly[ellipses] unsure of how this conversation will resolve."

                "No, I mean...":
                    jump NateProblem

        "Ethan's the problem.":
            show nate unamusedbrow frownmouth with dis

            nate @talking2mouth "Seriously? You mean you don't want him to bunk with someone else? {i}That's{/i} your major malfunction?"

            menu:
                "Yes, that's what I mean.":
                    $ AddEvent("Nate", "EthanConfess")

                    pause 1.0

                    show nate upeyes frownmouth with dis

                    pause 1.0

                    nate unamusedbrow @talking2mouth "Fine. But that's pretty damn weird, and I know weird. He's {i}eighteen{/i}, a grown-ass man." 
                    nate @talking2mouth "If you don't want someone else to move in on him, {i}do{/i} something about it, don't just put up roadblocks in front of other people."

                    hide nate with dis

                    narrator "You and Nate part ways, awkwardly..."

                "No, I mean...":
                    jump NateProblem

        "I'm the problem.":
            show nate confusedbrow frownmouth with dis

            nate @talking2mouth "Uh[ellipses] what? What are you saying? You don't want me to go show MC² a good time[ellipses] just because?"

            menu:
                "Yes, that's what I mean.":
                    $ AddEvent("Nate", "CentristConfess")

                    pause 1.0

                    show nate upeyes frownmouth with dis

                    pause 1.0

                    nate unamusedbrow @talking2mouth "Fine. I guess I owe you."

                    hide nate with dis

                    narrator "You and Nate part ways, awkwardly..."

                "No, I mean...":
                    jump NateProblem

        "I guess there's no problem.":
            show nate confusedbrow frownmouth with dis

            nate @talking2mouth "Uh, alright."

            hide nate with dis

            narrator "You and Nate part ways, awkwardly..."

    label postnatebunnyconfrontationconfess:

    hide nate with dis

    pause 1.0

    $ AddEvent("Nate", "JoinBunny")

    jump BunnyPartyStart

label MelodyBunnyJoin:
    $ AddEvent("Melody", "BunnyHandled")
    #Melody crashes the party, but security warns you
    #Iono gives you advance warning, and you can have her turn Melody around
    #Nate gives you advance warning, and you can have him turn Melody around
    #Sonia does not give you advance warning
    #Ethan does not give you advance warning

    if (prime_security == "Iono"):
        show phone_B
        show iono happy:
            xpos 0.525 zoom 0.9 ypos 0.9
        show phone_A 
        with fadeinbottom

        iono @happy "Hey! Listen!"
        iono @closedbrow talking2mouth "Thought you might want to know. Hostile moving in, adorned in the colors of our fair nation of Bunlandia."

        red @sigh "Translation."

        iono frownmouth @rolleyes talking2mouth "There's a girl in a bunny suit headed your way."

        red @confused "[ellipses]Okay? A late arrival, sure, but does that really make her a 'hostile?'"

        iono @winkbrow talkingmouth "Depends how you feel about Me-lo-dy!"

        red @surprisedbrow talking2mouth "Melody's coming?!"

        iono @confusedbrow talking2mouth "Y-yeah."

        pause 1.0

        iono @closedbrow talking2mouth "Didn't--{w=0.5}didn't I just say that?"

        red @closedbrow frownmouth "[ellipses]"

        iono @confusedbrow talking2mouth "Want me to turn her around?"

        pause 0.5

        red @closedbrow talking2mouth "Is that something you can do?"

        iono @rolleyes talking2mouth "Oh, no, when you hired me for security purposes, I thought I'd just watch the cameras, and not actually do anything to, you know, {i}secure{/i} the party."

        pause 0.5

        red @unamusedbrow talking2mouth "My Mom says sarcasm is the lowest form of wit."

        iono @rolleyes talking2mouth "Do you want me to stop Melody or what?"

        redmind @thinking "On one hand, she probably isn't here {i}just{/i} to enjoy the party. On the other hand, if she's got a suit, can we really turn her down[ellipses]"
        redmind @upeyes frownmouth "Well, yeah, of course we can. But I'm curious[ellipses] what does she want to do that'd be worth getting the suit and coming here, even if she wasn't invited?"

        menu:
            "Turn her around.":
                $ AddEvent("Melody", "RejectBunny")
                pass

            "I'll talk with her.":
                pass
                
        iono @happy "You're the boss!"

        hide phone_B
        hide iono
        hide phone_A
        with fadeoutbottom

        $ BecomeContacted("Iono")

    elif (prime_security == "Nate"):
        if (BunRecruit("Game")):
            if (not HasEvent("Nate", "JoinBunny")):
                show phone_B
                show nate suit frownmouth:
                    xpos 0.5
                show phone_A 
                with fadeinbottom
            else:
                show nate bunny frownmouth with dis
        else:
            show nate suit frownmouth with dis

        nate @talking2mouth "Hey. Status update:{w=0.5} M's moving towards us. In a bunny suit."

        if (GetSeenClassScenes("Psychic") >= 10):
            red @confused "Morty?"
        elif (GetSeenClassScenes("Water") >= 10):
            red @confused "Misty?"
        elif (GetRelationshipRank("May") >= 2 and HasEvent("May", "BunnyKitchen")):
            red @confused "Mallow? Isn't she already here?"
        elif ( HasEvent("May", "BunnyKitchen")):
            red @confused "May? Isn't she already here?"
        else:
            red @confused "May?"

        nate @talking2mouth "No, uh, Melody."
        nate @closedbrow talking2mouth "{size=30}Yeah, that {i}would{/i} be confusing, wouldn't it[ellipses]?{/size}"

        redmind @surprisedbrow frownmouth "Melody? In a bunny suit? Why would she[ellipses]?"

        pause 0.5

        nate @confusedeyebrows talking2mouth "Want me to bounce her?"

        redmind @thinking "On one hand, she probably isn't here {i}just{/i} to enjoy the party. On the other hand, if she's got a suit, can we really turn her down[ellipses]"
        redmind @upeyes frownmouth "Well, yeah, of course we can. But I'm curious[ellipses] what does she want to do that'd be worth getting the suit and coming here, even if she wasn't invited?"

        menu:
            "Turn her around.":
                $ AddEvent("Melody", "RejectBunny")
                pass

            "I'll talk with her.":
                pass
                
        nate @talking2mouth "Roger."

        if (not HasEvent("Nate", "JoinBunny")):
            hide phone_B
            hide nate
            hide phone_A
            with fadeoutbottom

            pause 0.5

            $ BecomeContacted("Nate")
        else:
            hide nate with dis

    elif (prime_security == "Sonia"):
        if (BunRecruit("Game")):
            show phone_B
            show sonia surprisedbrow frownmouth:
                xpos 0.52 zoom 0.95
            show phone_A 
            with fadeinbottom

            sonia @talking2mouth "Pardon me. I rather thought you should know--you should really get out here rather immediately!"

            red @surprised "What? What's happening? Is it a professor?"

            sonia surprised "It's Melody! And, er, she brought a bunny suit, so I'm not really clear whether she's here to join the party or something else, but she's staring at me, and I should--"

            hide phone_B
            hide sonia
            hide phone_A
            with fadeoutbottom

            $ BecomeContacted("Sonia")

    else:#ethan
        if (BunRecruit("Game")):
            show ethan bunny surprisedbrow talking2mouth with vpunch

            ethan @talking2mouth "Hey, man, gonna need you out there."

            red @surprised "Why?"

            ethan @talking2mouth "It's Melody. But, uh[ellipses] she's got a bunny suit. She wasn't on the invite list, was she?"

            red @confused "Uh. No. She--she has a suit?"

            ethan @talking2mouth "Yeah. {w=0.5}{nw}"
            extend @talkingmouth lightblush sad2eyes "And not much else."

            red @sigh "Alright. I'll handle this."

    scene blank2 with splitfade

    if (HasEvent("Melody", "RejectBunny")):
        pause 1.0

        narrator "You wait for a while[ellipses] but Melody doesn't show up."
        narrator "It seems security did their job."

        jump BunnyPartyStart

    scene academyhall with splitfade

    $ MoveInRight("melody")
    $ _bunned = BunRecruit("Game")

    if HasEvent("Klara", "BrokeBond"):
        show melody bunny on smilemouth with dis

        melody @talkingmouth "Hey, [first_name]."

        if _bunned:
            melody @surprisedbrow talking2mouth "Oh, wow, you're wearing a suit too? You're {i}really{/i} committed to this. She must have hurt you bad."

        pause 0.5
        
        redmind @surprisedbrow frownmouth "Why--why is she {i}smiling?!{/i}"
        
        pause 0.5

        melody @talking2mouth "Took me forever to get here. I hope I'm not late. She here yet?"
        
        red @talking2mouth "Wha--who?"
        
        melody @talkingmouth "Come on. I know this game. It's dirtier than I thought you'd go for, but I'm a fan. I hate her too."
        
        red @angrybrow talking2mouth "I don't know what you're accusing me of, but we're not doing anything dirty here."

    else:
        show melody bunny on angrybrow frownmouth with dis

        if not _bunned:
            melody @talking2mouth "[first_name]. I should have known you were behind this. Another 'Mister Perfect' who's just good at hiding what a dirtbag he is."
            
            pause 0.5
            
            melody @sadbrow talking2mouth "How could you do this? I thought you were her friend."
            
            red @angrybrow talking2mouth "I don't know what you're accusing me of, but you need to back off. I haven't done anything wrong."
        
        else:
            melody @talking2mouth "[first_name]. I should have known you were behind this. Ano[ellipses]{nw}"
            extend @surprised " What are you wearing?"

            red @downeyes frownmouth "[ellipses]"
            
            red @talking2mouth "Uh, a bunny suit? Same as you."
            
            red @talking2mouth "Well, it's not the same {i}design{/i}, but same {i}concept{/i}, I guess."
            
            melody @angrymouth "Yeah, I can tell it's not the same effing design. {i}Why{/i} are you wearing one?"
            
            red @talking2mouth "Because I'm attending a bunny suit-themed party? I mean, that's why you're wearing the suit, right?"
            
            pause 1.0
            
            melody @talking2mouth "There's--{w=0.5}there's no way the party's real."
            
            red @talking2mouth "There's literally a room full of people who can prove you wrong."

    # ===== Shared "prove it" sequence =====
    melody @talking2mouth "Really. So if I go into that room, I'm going to see a bunch of people in bunny suits?"

    red @talking2mouth upeyes "Yes, because it's a bunny suit-themed party. That {i}you{/i} weren't invited to."

    pause 0.5

    if HasEvent("Klara", "BrokeBond"):
        melody @talkingmouth "Yeah, sure. You lie like a rug, [melody_name]."
    else:
        melody pissed @talking2mouth "You lie like a rug."
        
        show melody at getcloser
        
        melody @angrymouth "Move."

    $ MoveOutSmart("Melody")

    pause 1.0

    $ PlaySound("GenericDoorOpen.ogg")

    pause 2.0

    $ PlaySound("GenericDoorClose.ogg")

    pause 1.0

    show melody bunny on intenseblush

    $ MoveInRight("Melody")

    pause 1.0

    red @talking2mouth "Satisfied?"

    pause 0.5

    melody @talking2mouth "I[ellipses] may have miscalculated."

    # ===== Branch-specific follow-up (the "explain yourself" block) =====
    if HasEvent("Klara", "BrokeBond"):
        red @upeyes angryeyebrows talking2mouth "Mind explaining what awful thing you thought we were doing, that we aren't actually doing, which is apparently a bad thing?"
        red @angryeyebrows sad2eyes talking2mouth "Because I've tried {i}really{/i} hard all week to make this party a safe, above-board, fun place for people to express themselves."
        red @angryeyebrows sad2eyes talking2mouth "If there's a story going around it's something else[ellipses] I {i}really{/i} don't need more rumors circling around about me."

    else:
        if not _bunned:
            red @upeyes angryeyebrows talking2mouth "You called me a dirtbag, and said I was doing something to hurt one of my friends. You weren't here for this, but I've taken a bunch of flak for being {i}too good{/i} a friend."
            red @angryeyebrows sad2eyes talking2mouth "If I could avoid being called a {i}bad{/i} friend as well, that'd be {i}great{/i}."
        
        else:
            red @upeyes angryeyebrows talking2mouth "Got something to say? Because I've gotten a lot of grief for telling the truth too much."
            red @angryeyebrows sad2eyes talking2mouth "If I could avoid being called a {i}liar{/i} as well, that'd be {i}great{/i}."

    pause 1.0

    # ===== Shared apology + "what did you think" =====
    melody up disgustedbrow @talking2mouth "I'm[ellipses] sorry."

    melody @closedbrow talking2mouth "I thought--"

    melody @talking2mouth "Guess it doesn't matter. I thought wrong."

    redmind @upeyes frownmouth "[ellipses]Damn my amiable nature."

    red @closedbrow sweat talking2mouth "What {i}did{/i} you think was happening here?"

    # ===== Branch-specific accusation / relationship beat =====
    if HasEvent("Klara", "BrokeBond"):
        melody @talking2mouth "I thought you were working with Leaf to humiliate Klara as revenge for what Klara did."
        
        red @confused "And you cared?"
        
        melody @talking2mouth "Not about Leaf. I just really effing hate Klara."
        
        red @talking2mouth "Great. Well, sorry to disappoint. This wasn't some twisted revenge plot. I just want everyone here to have a good time--and neither you {i}or{/i} Klara were invited."

        melody @talking2mouth "Yeaaaah. I kinda figured you were being a scumbag--which would have been fun."
        melody @talking2mouth "But I guess you're actually a good guy."

        python:
            character = "Melody"
            newrelationship = "Actually a Good Guy"
            renpy.pause(1.0)
            formertitle = "Classmate"
            CurrentPersondex()[character]["Relationship"] = newrelationship
            CurrentPersondex()[character]["RelationshipRank"] = 0
            PlaySound("sav.ogg")
            AddEvent(character, "Became" + newrelationship)
            renpy.say(None, "Your heart shifts as you feel your relationship with {} evolve from '{{color=#0048ff}}{}{{/color}}' to '{{color=#0048ff}}{}{{/color}}'!".format(character, formertitle, newrelationship))
        
        redmind @frownmouth angryeyebrows upeyes "Seriously?"
        
        pause 0.5

        red @talking2mouth "Well, there's nothing to see here at this party. Klara's not coming, there isn't going to be any big revenge plot."
        red @talking2mouth "If that's all you were here for, you can go."

        pause 1.0

        melody disgustedbrow intenseblush "[ellipses]{nw}"
        extend @talking2mouth "Can I join the party? I'm freezing out here, and I don't want to walk across campus in this outfit again until it gets darker."
        melody -disgustedbrow -intenseblush @talking2mouth closedbrow "I swear I won't talk to anyone. Maybe just pick at the snack table."

    else:
        melody @talking2mouth "I thought you were working with Klara to humiliate Leaf again."
        
        red @confused "And you cared?"
        
        melody @talking2mouth "Not about Leaf. I just really effing hate Klara. And if you were {i}actually{/i} doing that, I would hate you, too."
        
        red @unamusedbrow talking2mouth "Great. I guess that means I'm 'not hated.' What a relationship upgrade."

        python:
            character = "Melody"
            newrelationship = "Not Hated"
            renpy.pause(1.0)
            formertitle = "Classmate"
            CurrentPersondex()[character]["Relationship"] = newrelationship
            CurrentPersondex()[character]["RelationshipRank"] = 0
            PlaySound("sav.ogg")
            AddEvent(character, "Became" + newrelationship)
            renpy.say(None, "Your heart shifts as you feel your relationship with {} evolve from '{{color=#0048ff}}{}{{/color}}' to '{{color=#0048ff}}{}{{/color}}'!".format(character, formertitle, newrelationship))
        
        redmind @frownmouth angryeyebrows upeyes "I was {i}joking.{/i}"
        
        pause 0.5

        red @talking2mouth "Well, if you were trying to save Leaf from this party, you would have been {i}way{/i} too late. We've been going for hours now."
        
        melody @pissedbrow intenseblush talking2mouth "I didn't realize how long it would take to get this suit. I ran halfway across campus. Swallowed my gum."
        
        red @closedbrow talkingmouth "Well, in a universe where {i}any{/i} of this was necessary, I'm sure {i}someone{/i} would appreciate it."

        melody @talking2mouth closedbrow "Fine, {i}fine{/i}, I get it. I overreacted. You're not a liar. And I'm sorry, {i}again{/i}."
        melody @talking2mouth "Can I join the party now? I'm freezing out here, and I don't want to run across campus in this outfit again until it gets darker."
        melody @talking2mouth closedbrow "I swear I won't talk to anyone. Maybe just pick at the snack table."

    # ===== Shared join menu =====
    menu:
        "Fine.":
            melody on @talking2mouth "Thanks."

        "You can join, but you need to talk to people.":
            show melody surprisedbrow frownmouth with dis
            
            $ AddEvent("Melody", "BunnyRecruit")
            
            pause 1.0
            
            melody @talking2mouth "Uh. You sure?"
            
            red @talking2mouth "Yes."
            
            pause 1.0
            
            melody "[ellipses]{nw}"
            extend on @talking2mouth "'Kay."

        "No.":
            $ AddEvent("Melody", "RejectBunny2")
            
            melody on @talking2mouth "Yeah, fair."

    jump BunnyPartyStart

label WhitneyBunnyTalk:
    $ AddEvent("Whitney", "BunnyTalk")
    
    if (HasEvent("Whitney", "Whitney2Part2")):
        show whitney bunny sad2eyes poutmouth with dis

        pause 2.0

        show whitney surprisedeyebrows neutraleyes with dis

        red @talking2mouth "Hey."

        whitney sad2eyes poutmouth -surprisedeyebrows @talking2mouth "Hey."

        pause 1.5

        red @talkingmouth "Mind if I sit?"

        whitney upeyes angryeyebrows neutralmouth @sad2eyes neutraleyebrows talking2mouth "You're good."

        red @happy "I mean, I try, but my legs still get tired."

        whitney @talkingmouth "Just sit down, you jock."

        show whitney at getcloser

        pause 1.5

        show whitney sad2eyes -angryeyebrows with dis

        red @sadbrow talkingmouth "You alright? You seem a bit low-energy. Sugar crash?"

        whitney @talking2mouth "Sugar rushes aren't real."

        pause 1.0

        red @confused "Sure, but I was talking about sugar {i}crashes{/i}."

        whitney lightblush @talking2mouth "Oh. Right."
        whitney sweat @talking2mouth "I was distracted."

        red @sadbrow talkingmouth "All the bunny suits?"

        whitney @angryeyebrows talking2mouth "No, and {i}that's{/i} the problem."
        whitney -sad2eyes @sadbrow talkingmouth "I should be able to just relax, and enjoy this, and have the kinds of thoughts that would make me burst into flame if I ever got into the Bell Tower."

        pause 1.0

        red @talkingmouth "Having difficulty?"

        whitney @talking2mouth "I guess. I just feel like something's missing. But we've got the music, the girls, the suits[ellipses] There {i}isn't{/i} anything missing."

        red @sadbrow talkingmouth "Maybe it's not something, but {i}someone?{/i}"

        whitney blush @talking2mouth "No."

        pause 1.0

        whitney @closedbrow talking2mouth "I dunno."

        pause 1.0

        show whitney at getfurther

        whitney @angrybrow talking2mouth "Gah! I hate people who ruin the mood at parties!"
        whitney happy "I'm not going to let that be me. Smiles only, from now on!"

        $ SmartMoveOut("Whitney", duration = 0.2)

        red @thonk "[ellipses]?"

    else:
        show whitney bunny playfuleyes neutraleyebrows smirk2mouth with dis

        pause 2.0

        show whitney lightblush with dis

        red @talkingmouth "Hey."

        pause 1.5

        red @talkingmouth "Mind if I sit?"

        whitney @talkingmouth "Go ahead."

        show whitney at getcloser

        pause 1.5

        show whitney playfuleyes unamusedeyebrows with dis

        red @sadbrow talkingmouth "You look[ellipses] gone. Floating. Sugar high?"

        whitney @closedbrow talkingmouth "Those don't exist. Sugar crashes do, but sugar highs aren't a thing."

        pause 1.0

        red @talkingmouth sweat "So not a sugar high."

        whitney @talkingmouth "Sugar could never get me this high. I want to stay here, at this party, forever. This is like heaven--it's perfect."

        pause 0.5

        whitney -smirk2mouth -unamusedeyebrows -playfuleyes @closedbrow talking2mouth "Almost[ellipses] too perfect. Like a memory of a pillow."
        whitney @upeyes sadeyebrows talking2mouth "I {i}should{/i} be able to just melt into {i}this, but something keeps tugging at me[ellipses]"
        whitney @closedbrow sweat talking2mouth "Like there's some last piece that I need to make this all real."

        pause 1.0

        red @confused "Uh[ellipses] self-actualization, maybe?"

        whitney @sweat closedbrow talking2mouth "I think my self is a bit too actual."

        pause 1.0

        red @talking2mouth "Whitney, I need to confess something."

        whitney @talking2mouth "You have no idea what self-actualization is."

        red @talking2mouth "I have no idea what self-actualization is."

        pause 1.0

        whitney happybrow neutralmouth @happy "Ahahaha! Alright, I'm not going to mope about something that doesn't exist. C'mon, back to the party. Let's go!"

        show whitney at getfurther

        pause 0.5

        $ SmartMoveOut("Whitney", duration = 0.2)

    hide whitney with dis

    jump BunnyPartyStart

label RosaBunnyTalk:
    $ AddEvent("Rosa", "BunnyTalk")
    
    show rosa bunny sad2eyes surprisedeyebrows pout pouthappymouth with dis

    pause 2.0

    show rosa surprisedbrow with dis

    red @talkingmouth "Hey."

    rosa sweat neutralbrow -pout neutralmouth @talkingmouth "Heya, [first_name]!"
    rosa @happy "Great party you've got here! I'm having a ton of fun."

    pause 1.0

    show rosa sad2eyes sadeyebrows lightblush with dis

    red @happy "You're such a good actor, even though I saw you rubbing a hole through the snack table's tablecloth, I almost believe you."

    rosa -sad2eyes @talkingmouth sadbrow "Ah, you got me. I can't help but be worried, though. This situation is[ellipses]"

    if (GetRelationshipRank("Rosa") > 1):
        red @sadbrow talkingmouth "Don't worry. It won't be anything like that battle we had in the Battle Hall. Our security here is airtight, really. Promise."
    else:
        red @sadbrow talkingmouth "You're worried someone might see you? Take a picture?"

        rosa @talkingmouth "Or a video, or even audio, really. I know I'm just being paranoid, but this is the most out of my comfort zone I've ever been[ellipses]"

    pause 1.0

    rosa @happy "It's kinda funny! I bet most people here feel uncomfortable 'cause of the bunny suits."
    rosa @talkingmouth "I'm actually completely fine with the suit. It's the venue that makes me uncomfortable[ellipses]{w=0.5}{nw}"
    extend @talking2mouth " and it's just a normal classroom."

    red @talking2mouth "Well[ellipses] look, if it's really that bad, you don't need to stay. We can both change back into our normal clothes, and I'll walk you back to your dorm."

    rosa @sad2brow talking2mouth "Well, I don't {i}really{/i} want to do that, either[ellipses]"

    if (prime_security == "Iono"):
        $ PlaySound("vibrate.ogg")

        TempCharacter("Phone") "Bzzt! Bzzt! Bzzt!"

        red @talking2mouth "Oh, sorry. Let me get that."
      
        show phone_B
        show iono angry:
            xpos 0.51 zoom 0.8 ypos 0.9
        show phone_A 
        with fadeinbottom

        iono @angrybrow talking2mouth "Hey, hey, hey! Did I hear someone doubting the power of Iono's firewall?"

        show rosa surprisedbrow -lightblush -sweat frownmouth with dis:
            ease 1.5 rotate 30 xpos 0.55

        rosa @talking2mouth "Did I--did I hear Iono? You have her number?"

        red @unamusedbrow talking2mouth "She definitely has mine."

        iono @happy "Numbers are so 2003. Who even answers their phone anymore? It's all about RotoPhotos Handles."

        if (starter_species_name == "Rotom"):
            red @sweat talking2mouth "I--I don't have one of those. I mean, I've got a Rotom, but it doesn't take pictures--or have handles."

        else:
            red @sweat talking2mouth "I--I don't have one of those."

        iono @grinbrow talkingmouth "Anyway, shut up. Hand me over to Rosa-mimosa. I'mma put her mind all at ease. She'll be so easy that--"

        show rosa happybrow sweat neutralmouth with dis

        iono @closedbrow talking2mouth "Actually, no, {i}that one's{/i} too far. Nevermind, nix that bit, scratch it, purge the record, burn the paper."

        pause 1.5

        iono @confusedbrow talkingmouth "Well?"

        red @closedbrow talking2mouth "Uh[ellipses] Rosa? Are you okay, uh, talking with Iono? I know she's a lot[ellipses]"

        iono @angry "Hey, what do you mean by--"

        hide phone_B
        hide iono angry
        hide phone_A
        with fadeoutbottom

        pause 1.0

        show rosa:
            ease 0.5 rotate 0 xpos 0.5

        rosa @talkingmouth "Y-yeah. Um, if she knows something about the security this party has, maybe she can put my mind at ease."

        red @talkingmouth "Alright."

        narrator "You pass your phone over to Rosa."

        $ hideside = True

        iono "{size=30}You did {i}not{/i} just put me in your pocket while I was speaking! It was full of moths and lint! Hey, Rosa, turn me around, I want to give that punk a piece of my mind!{/size}"

        narrator "Rosa turns to the phone, smiling apologetically."

        $ hideside = False

        hide rosa with dis

        narrator "On the bright side, it looks like she's got something to worry about other than possible security breaches, now."
        narrator "[ellipses]You'll have to remember to get your phone back from her later."

    elif (prime_security == "Nate" and HasEvent("Nate", "JoinBunny")):
        $ MoveInLeft("nate bunny")

        nate @talkingmouth "Maybe I can help?"

        pause 1.5

        rosa @sadbrow talkingmouth "I've seen the kinds of videos were a mostly-naked man walks in offering to help with something. I'm not sure that'd work for me."

        nate @winkbrow talkingmouth "Maybe not, but it definitely works for {i}me{/i}."
        nate @talkingmouth "But, seriously, I can walk you through some of the stuff the security team is doing to keep this place safe and fun for all of us. I had a hand in pretty much all of it, so I'm qualified to talk about it."

        rosa @talkingmouth "I'd[ellipses] if that's alright? I don't want to take up too much of your party time."

        nate @happy "Getting to hang out with my favorite movie star and infodump technobabble? This {i}is{/i} the party time, superstar."

        pause 0.5

        nate @talkingmouth "Go ahead and go back to the party, [nate_name]. I've got this mission."

        red @talkingmouth "Thanks, man."

        show nate:
            ease 0.5 xpos 1.2
        $ SmartMoveOut(["Rosa"], exclude=["nate"])

        pause 0.5 

        narrator "The two bunnies walk off together, chatting casually."

    else:
        $ herpronoun = "her" if prime_security == "Sonia" else "him"
        red @happy "Hey, [prime_security]'s watching the door. You trust [herpronoun], right?"

        rosa @sad2brow pout "[ellipses]"
        rosa @sadbrow talkingmouth "You know what, you're right, I'm probably just being silly. I wouldn't even be the most eye-catching person here, anyway, right? So if someone was going to take pictures[ellipses]"
        rosa @talkingmouth sweat "Well, um, thanks for checking on me. But I'm fine, really. I'm just going to[ellipses] um[ellipses] check out the snacks!"

        hide rosa with dis

        pause 1.0

        narrator "You remain unconvinced."

        redmind @thonk "What was up with that long pause when I asked about [prime_security]?"

    jump BunnyPartyStart

label ChocolateBunnyFountain:
    $ AddEvent("Game", "BunnyFountain")
    $ MoveInRight("leaf bunny")

    leaf @surprisedbrow talking2mouth "Oh, shit, is that a chocolate fountain? Like, chocolate fondue?"

    red @happy "Yeah, Yellow knew someone who--"

    pause 1.0

    red @confused "Wait, fondue? I thought fondue was cheese."

    leaf @talking2mouth "I think it can be chocolate {i}or{/i} cheese."

    if (HasEvent("May", "BunnyKitchen")):
        $ MoveInLeft("may bunny")
        
        if (mallow_present):
            $ MoveInLeft("mallow bunny")

        may @talkingmouth "Yeah, fondue just means 'melted.' It's a Kalosian word. So anything you melt could be a fondue, really."

        pause 1.0

        leaf @talkingmouth "May, remember what we said about butting into other people's conversations to clarify the meaning of words?"

        may @sadbrow talkingmouth "I think we said something about {i}not{/i} doing that?"

        leaf @happy "Well, normally, yes, but it's fine today, because I'm in {i}such{/i} a good mood. I mean, the party's one thing, but we've got a {i}fondue{/i} fountain."
        leaf @closedbrow talkingmouth "All that remains is the titanic task of deciding what I might baptise within the chocolescent geyser..."

        may @talking2mouth "Well, you can't go wrong with the classics, like fruit, or marshmallows."

        if (mallow_present):
            $ GroupExpression("surprisedbrow frownmouth", exclude="mallow")

            mallow @talkingmouth "Yes?"

            pause 1.0
            
            $ GroupExpression("happybrow neutralmouth", exclude="mallow")

            mallow @blush sadbrow talkingmouth "Oh. Oops. I thought I heard--nevermind! Ignore me."
            
            $ GroupExpression("neutralbrow neutralmouth")

        leaf @talkingmouth "Well, yeah, you can't go wrong with the classics, but if I wanted the safe answer, I wouldn't be asking the most adventurous foodie from here to Kobukan."

        if (GetRelationshipRank("May") > 0):
            redmind @thonk "Adventurous? She's the opposite of adventurous when it comes to {i}her{/i} cooking[ellipses] but she doesn't mind eating out-there stuff? Huh."

        may @talkingmouth "When mixing flavors together, like with chocolate fondue, the secret is to have contrast between the two flavors."
        may @closedbrow talking2mouth "Melted chocolate is deep, rich, and smooth. So you're going to want something that's the opposite of all those."

        leaf surprisedbrow frownmouth @neutralbrow talkingmouth "Okay, but not like--"

        if (mallow_present):
            show mallow surprisedbrow frownmouth with dis 

        may happybrow @happy "Like Barraskewda fillet!"

        pause 1.0

        leaf -surprisedbrow -frownmouth @sweat sadbrow talkingmouth "I[ellipses] might need a second opinion?"

        if (mallow_present):
            mallow -surprisedbrow @talkingmouth "I'd probably just try it with some Pinap berries. The fruit's got a tangy 'kick' that just slices through the chocolate."
            mallow @happy "It's really good, even if you don't have any Alolan-grown Pinaps."

            leaf @talkingmouth "{i}That{/i} definitely sounds more my speed."

        may @sadbrow talkingmouth "You'll never know if you don't try it!~"

        if (mallow_present):
            $ SmartMoveOut(["May", "Mallow"])
        else:
            $ SmartMoveOut("May")

        pause 1.0

        leaf @surprisedbrow talking2mouth "Okay, I knew May liked some out-there stuff, but {i}fish and chocolate{/i}?"

        menu:
            "You'll never know if you don't try it!~":
                leaf angrysmilemouth flirtbrow @talking2mouth "Oh, you think you're funny, don't you?"

                red @talkingmouth "Hilarious, yeah."

            "Yeah, that's something else.":
                leaf @surprisedbrow talkingmouth "Right?"

    else:
        leaf @talking2mouth "Actually, May once mentioned dipping fish--Arrokuda, I think--in fondue. So she must've been talking about cheese, right?"
        leaf @talkingmouth "I mean, the girl will eat {i}anything{/i} once, but fish and chocolate don't mix, right?"

        red @talkingmouth "Different tastes, I guess? It's probably the cheese thing, though. Like you say, fish and chocolate would be {i}weird.{/i}"

    pause 1.0

    leaf closedbrow frownmouth "Hmmm[ellipses]"

    pause 1.0

    red @talkingmouth confusedbrow "Pokédollar for your thoughts?"

    leaf -frownmouth @flirtbrow talkingmouth "Oh, they're worth {i}way{/i} more than that, Skippy."

    red @talking2mouth "Fine, keep your secrets."

    leaf angrysmilemouth angrybrow @sadbrow talkingmouth "Aw, but I {i}want{/i} to tell you!"

    red @unamusedbrow talking2mouth "Yeah, I know. I knew I just had to wait you out."

    leaf @flirtbrow talking2mouth "Buttface. Look, here's what I'm thinking."
    leaf -angrysmilemouth -angrybrow @talkingmouth "I bet we can go even weirder than fish and chocolate if we try. Like, if we {i}really{/i} dig deep."

    red @confused "What are you proposing?"

    leaf @closedbrow talkingmouth "Not yet, it's only been, like, two months."

    red @unamusedbrow talkingmouth "There was no comma there."

    leaf @happy "Shush. Here's what I'm thinking. You and I have a competition. We ask each bunny at this party what they want to dip in the fondue, if they could dip {i}anything{/i}, and then whoever gets the weirdest ingredient wins."

    red @confused "What are we winning, exactly?"

    leaf @talking2mouth "Honor? Bragging rights? The ability to tease our friends about the weird stuff they'd dip in fondue if they had the chance, and no-one would judge them?"

    red @unamusedbrow unamusedmouth "[ellipses]"

    menu:
        "No, this is dumb.":
            jump SkipFondue

        "It's a challenge.":
            leaf angrybrow @talkingmouth "You're {i}so{/i} going down. Like a fish in a chocolate fondue fountain, after May gets her hands on it."

            $ SmartMoveOut("leaf")

        "Wow, you {i}really{/i} miss battling, huh?":
            leaf @talkingmouth "Duh! I went a full week without battling. Or talking to anyone. I need to catch up on all that lost time!"
            leaf @winkbrow talkingmouth "And if that means asking really weird questons about what you'd dip into chocolate, so be it."

            red @sigh "So be it."

            leaf @talkingmouth happybrow "So you're in?"

            menu:
                "Seems so.":
                    leaf angrybrow @talkingmouth "You're {i}so{/i} going down. Like a fish in a chocolate fondue fountain, after May gets her hands on it."

                    $ SmartMoveOut("leaf")

                "Irrespectfully, I must decline.":
                    jump SkipFondue

    pause 1.0

    redmind @thinking "Alright. Which of my friends is most likely to have really weird tastes in party foods[ellipses]?"
    
    menu FondueChallenge:
        "Ask Nessa" if (BunRecruit("Nessa") and not HasEvent("Nessa", "AskFondue")):
            $ AddEvent("Nessa", "AskFondue")
            show nessa bunny with dis

            red @talkingmouth "Hey, Nessa! What would you dunk in the fondue fountain, if you had access to anything, and no-one would judge you? I want you to be as weird as possible with this."

            nessa @closedbrow talkingmouth "Probably Chairman Rose's face."
            nessa @talkingmouth sad2brow "But if I need to eat it afterward[ellipses] Galarian muffins."

            red @confused "Galarian muffins? Uh[ellipses] aren't they kinda[ellipses]?"

            nessa frownmouth "[ellipses]"
            nessa @talking2mouth "Are you insulting my culture, [first_name]?"

            red @sadbrow talkingmouth "Maybe just a very specific part of it, mostly as a joke?"

            nessa @talking2mouth "That's a hate crime."

            red @closedbrow talkingmouth "I will immediately accept any punishment you see fit as long as you don't tell my mom."

            pause 1.0

            nessa @talkingmouth sad2brow "Relax, [first_name]. I was joking. I know Galarian muffins are disgusting--like chewing cardboard."

            red @talking2mouth sweat closedbrow "{size=30}Oh, thank god.{/size}"
            
            nessa -frownmouth @talkingmouth "I was serious about dipping them in chocolate, though. The tasteless pastry just makes the deep, rich, flavor of the chocolate even richer."

            red @confused "Huh. Okay, I see it."

            nessa @talkingmouth "Whether it's people or food, you can always just cover up something unappealing with something sweet."
            nessa @talking2mouth "For some people it's clothes, for some it's makeup, and for some it's chocolate fondue."
            nessa @talking2mouth "Just cover that Galarian muffin up with so much chocolate it basically stops being a muffin, and now everyone will like it."

            red @talking2mouth winkbrow sweat "That's[ellipses] depressing."

            nessa @sad2brow talkingmouth "But I look good in this suit, right?"

            hide nessa with dis

            jump FondueChallenge

        "Ask Nate" if (BunRecruit("Nate") and not HasEvent("Nate", "AskFondue")):
            $ AddEvent("Nate", "AskFondue") 

            if (HasEvent("Nate", "JoinBunny")):
                show nate bunny with dis
            else:
                show phone_B
                show nate suit
                show phone_A 
                with fadeinbottom

            red @talkingmouth "Hey, Nate. What would you dunk in the fondue fountain, if you had access to anything, and no-one would judge you? I want you to be as weird as possible with this."

            nate @talkingmouth "Oh, that's kinda an easy one. Donuts."
            
            pause 1.0

            red @talkingmouth "Huh. I'm not sure that's {i}weird{/i}, necessarily, but I'm[ellipses] not really sure what to think about that."
            red @talkingmouth "Why donuts?"

            nate @closedbrow talkingmouth "They're sweet, easy to hold, they've got a great texture, and are structurally sound. Not much more to it."
            nate @talkingmouth "I donut need to justify my choices."

            red @unamusedbrow talking2mouth "Okay."

            nate @talking2mouth "And while we're on the subject--bear claws. Bare is right, there's never enough icing. A quick dunk in the chocolate tank will fix it."

            red @closedbrow talking2mouth "I see where this is going."

            nate @talkingmouth "Éclairs are nice, but I should be éclear--they'll taste better slathered in chocolate."

            red @talking2mouth "Stop."

            nate @talking2mouth "Or, you know, we could just keep it simple. A danish would be sweet."

            red @wince "Ugh."

            nate @closedbrow talkingmouth "Of course, I don't want to glaze over my favorite--strudels rock {i}and{/i} roll."

            red @unamusedbrow talking2mouth "{i}How{/i} are you still going?"

            nate @happy "I guess the point I'm trying to make here is you can dunk pretty much any kind of pastry in chocolate and make it better. You know, try out new stuff. Muffin ventured, muffin gained."

            red @talking2mouth "Your lead-ups are getting longer and longer."

            nate @playfuleyes surprisedeyebrows talkingmouth "I'm getting the vibe you're jelly of my pun-proficiency."

            red @talking2mouth "No, I--"

            pause 1.0

            show nate happy with dis

            red @angry "Was that {i}another{/i} goddamn pun?"

            nate @talkingmouth "Alright, I'm done. Final answer: donuts."

            red @talking2mouth "This wasn't worth it."

            if (HasEvent("Nate", "JoinBunny")):
                hide nate with dis
            else:
                hide phone_B
                hide nate suit
                hide phone_A 
                with fadeoutbottom

            jump FondueChallenge

        "Ask Rosa" if (BunRecruit("Rosa") and not HasEvent("Rosa", "AskFondue")):
            $ AddEvent("Rosa", "AskFondue")
            show rosa bunny with dis

            red @talkingmouth "Hey, Rosa! What would you dunk in the fondue fountain, if you had access to anything, and no-one would judge you? I want you to be as weird as possible with this."

            rosa @closedbrow "Hmm[ellipses]"
            rosa @talkingmouth "Define 'dunk.'"

            red @confused "Uh[ellipses] 'put into?'"

            rosa @talkingmouth "Gotcha. Then milk!"

            pause 1.0

            red @talkingmouth "Milk?"

            rosa @talkingmouth "Sure! Just dump the milk in, swirl it around, and now you've got chocolate milk."

            red @sigh "I feel like this isn't in the {i}spirit{/i} of the chocolate fondue fountain."

            rosa closedbrow frownmouth @talking2mouth "Samuel L. Jacksmon was also scorned in his time."

            red @confused "[ellipses]What?"

            show bunday with vpunch

            show rosa angrybrow frownmouth at getcloser with dis

            rosa @angrymouth "What region are you from?"

            red @surprisedbrow talking2mouth sweat "[ellipses]W-what?!"

            rosa bunnyshadow @angrymouth "What ain't no region I ever heard of! They speak Galarian in What!?"

            red @surprisedbrow talking2mouth sweat "[ellipses]What?!"

            rosa bunnyshadow @angrymouth "Galarian, motherf--"
            rosa -bunnyshadow @surprisedbrow talking2mouth "Oh, no, I can't finish that scene."

            show rosa at getfurther

            rosa -angrybrow -frownmouth @sad2brow talkingmouth "There's some words there I {i}really{/i} shouldn't say."

            red @surprisedbrow frownmouth "[ellipses]"

            red @talking2mouth "I[ellipses] okay. I'm just going to accept this[ellipses] and move on."
            red @wince talkingmouth "Final answer: milk?"

            rosa idwineyes idwinmouth idwineyebrows "It's some {i}serious{/i} gourmet sh--{w=0.5}er, stuff."

            $ SmartMoveOut("rosa")

            pause 1.0

            red @sigh "Game references to the left of me, movie references to the right of me, and book references bringing up the rear. And here I am, stuck in the middle with you."

            $ PlaySound("pokemon/pikachu_happy1.ogg")

            libpikachu "Chaaa!"

            jump FondueChallenge

        "Ask Whitney" if (BunRecruit("Whitney") and not HasEvent("Whitney", "AskFondue")):
            $ AddEvent("Whitney", "AskFondue")
            show whitney bunny with dis

            red @talkingmouth "Hey, Whitney! What would you dunk in the fondue fountain, if you had access to anything, and no-one would judge you? I want you to be as weird as possible with this."

            whitney @upeyes frownmouth "Hmm[ellipses]"
            whitney @talkingmouth "Marshmallows."

            pause 1.0

            red @confused "Marshmallows."

            whitney @talkingmouth "Yup."

            pause 1.0

            red @talkingmouth "I mean, that's a fine answer, but the problem with that is that it's[ellipses] not weird at all. Like, that's actually a pretty common thing to dip in chocolate fondue."
            red @sigh "Might be {i}the{/i} most common thing, actually."

            whitney @upeyes talking2mouth "Well[ellipses] do you want me to go weirder? Because I really think my answer would be marshmallows."

            red @sadbrow talkingmouth "If you wouldn't mind. This is kinda for a competition."

            whitney @talkingmouth "Alright. How about cheese?"

            red @talkingmouth "Cheese?"

            whitney @talkingmouth "Yeah. Fondue can be cheese or chocolate, right? But what if we mixed the two together?"

            red @surprisedbrow talkingmouth "Oh, shit, you're talking about {i}melted{/i} cheese?"
            
            redmind @closedbrow frownmouth "Damn, this girl's hardcore."

            whitney @talkingmouth "Judicious application of dairy improves {i}any{/i} meal!"
            whitney @surprisedbrow talkingmouth "Oh, wait--are you lactose intolerant?"
            
            red @talkingmouth "Not outside of a specific running gag Leaf and I do, sometimes."

            whitney @happy "That's {i}great!{/i}"
            whitney @surprised "It's, like, {i}so{/i} weird that just under half of all people back home are lactose intolerant, you know?"
            whitney @sad "And that's just the saddest thing ever!"
            whitney @closedbrow talking2mouth "For most people, it only triggers when consuming raw dairy, so, like, milk[ellipses]"
            whitney @sad "But there's still a lot of people allergic to ice cream, butter, and cheese. It's a tragedy!"
            whitney @angry "Milk is like, the greatest drink ever, and it's used in all the best foods! And I'm not just saying that because I'm a Miltank trainer."
            whitney @closedbrow talking2mouth "I'm a city girl--I'm not trying to {i}sell{/i} the milk or anything, and in fact, I think drinking Milty's milk would be a tiny bit gross."
            whitney @surprisedbrow talking2mouth "But, like, other milk? It's the best! Besides, if you don't drink your milk, then you don't get strong bones and grow tall!"
            whitney @angrybrow talking2mouth "They don't want you to know this, but there's a reason Unovans get so big. Milk!"
            whitney @sad2eyes angryeyebrows shadow talking2mouth "They've probably got some sort of secret genetic mutation, some form of genetic engineering, and they've modified themselves to be able to drink milk. That's their plan for conquering the world! Milk!"
            whitney @angryeyes angryeyebrows shadow angrymouth "That's why we need to push through the stomach cramps, and the nausea, and the light-headedness!"
            whitney @angryeyes angryeyebrows shadow angrymouth "We must drink milk so that we can stand tall against the encroaching threat of the hard-boned giants of the West! For great justice! For Johto! For lactose!"

            pause 1.0

            red @talking2mouth "What about oatmilk?"

            whitney @confusedbrow talking2mouth "Uh[ellipses] sure, but isn't it a bit freaky? Like, how do you even milk an oat?"
            whitney @closedbrow talking2mouth "I'll take my milk straight from the source, thank you, not any weird secondhand {i}oat{/i} nonsense."

            pause 2.0

            red @talking2mouth "I know I shouldn't ask, but[ellipses] how do you feel about Gogoat milk?"

            whitney @poutmouth sad2eyes "[ellipses]"
            whitney @angrybrow talking2mouth "They're on thin ice."

            hide whitney with dis

            jump FondueChallenge

        "Ask Melody" if (BunRecruit("Melody") and not HasEvent("Melody", "AskFondue")):
            $ AddEvent("Melody", "AskFondue")
            show melody on bunny with dis

            red @talkingmouth "Hey, Melody. What would you dunk in the fondue fountain, if you had access to anything, and no-one would judge you? I want you to be as weird as possible with this."

            melody @talking2mouth "Uh[ellipses] you're asking me?"

            red @talking2mouth "Yeah. You said you'd be part of the party, so that means you're getting caught up in this weird game Leaf and I are playing."

            melody @talking2mouth "[ellipses]{nw}"
            extend @talking2mouth "'Kay."

            pause 0.5

            melody @talking2mouth "Oranges."

            pause 0.5

            red @talkingmouth "Huh? Oran berries?"

            melody @talking2mouth "No, oranges. The citrus fruit."

            red @talking2mouth "Sitrus berries?"

            melody angrybrow @talking2mouth "No! Mandarin oranges! {i}Citrus reticulata!{/i}"

            pause 1.0

            red @closedbrow talking2mouth "You're just making up words, aren't you?"

            melody surprisedbrow @talking2mouth "What? No, they're--they're what the Orange Islands are named after!"

            red @talkingmouth "They're just called 'oranges.'"

            melody angrybrow @talking2mouth "Yes."

            red @confused "Like the color."

            melody @talking2mouth "{i}Yes.{/i}"

            red @closedbrow talkingmouth "Sure. And, uh, just out of curiosity, {w=0.5}{i}{size=30}(snrk){/size}{/i}{w=0.5}, what color are these 'oranges?'"

            melody "[ellipses]{nw}"
            extend pissedmouth @talking2mouth "Orange."

            red @happy "Ah, you nearly got me. I'm too gullible."

            melody @angry "They're real! And they're delicious with chocolate!"

            hide melody with dis

            jump FondueChallenge

        "Ask Ethan" if (not HasEvent("Ethan", "AskFondue")):
            $ AddEvent("Ethan", "AskFondue")
            show ethan bunny with dis
            
            red @talkingmouth "Hey, Ethan! What would you dunk in the fondue fountain, if you had access to anything, and no-one would judge you? I want you to be as weird as possible with this."

            ethan @talkingmouth "Corn dogs."

            red @talkingmouth sweat "You said that[ellipses] very immediately, and {i}very{/i} confidently. Corn dogs?"
            
            ethan @talkingmouth "Yeah. Fry them. Then cover them in whipped cream. Dip them in more chocolate. Refry them. Shove them in the fridge for a week."
            ethan @closedbrow talkingmouth "Then flash-boil them until the stick disintegrates and you can taste the regret."
            
            red @talkingmouth sweat sadbrow "Have--have you {i}done{/i} this?"

            ethan @talking2mouth "I've done many things on the path I've walked. Great things[ellipses] but terrible. Greaterrible."

            pause 1.0

            ethan @talking2mouth "Nah, I'm just messing with you. But I {i}might{/i} try it out someday. The idea's actually kind of interesting."
            
            red @wince talking2mouth "It's a good thing you carry a first aid kit around with you everywhere."

            hide ethan with dis

            jump FondueChallenge

        "Go back to Leaf":
            pass

    $ SmartMoveIn("leaf bunny")

    leaf @talkingmouth "Well? What did you get?"

    menu:
        ">Talk about Nessa's Galarian muffins" if (HasEvent("Nessa", "AskFondue")):
            leaf @surprised "Woah, that's a bold choice. Those things are like cardboard."
        
        ">Talk about Nate's donuts" if (HasEvent("Nate", "AskFondue")):
            leaf @surprised "Woah, sugar overload! Dipping something already made of sweet bread and covered in glaze in even more sugar is intense. If he eats like {i}that{/i}, how does he stay so fit?"
        
        ">Talk about Rosa's milk" if (HasEvent("Rosa", "AskFondue")):
            leaf @angrybrow angrymouth "Ignore the milk! You got to play through a scene of Poké Fiction with Rosa?! And you {i}didn't{/i} invite me?!"
        
        ">Talk about Whitney's cheese" if (HasEvent("Whitney", "AskFondue")):
            leaf @sadbrow talkingmouth "Oh, you got her lactose rant? Yeah, I've heard it, too[ellipses]"
        
        ">Talk about Melody's hallucinations" if (HasEvent("Melody", "AskFondue")):
            leaf @sadbrow talkingmouth "'Oranges[ellipses]?' Oh, [first_name], I'm pretty sure she was making fun of you."

        ">Talk about Ethan's folly" if (HasEvent("Ethan", "AskFondue")):
            leaf @sadbrow talkingmouth "I think, um, the less we talk about that, the better."
        
        ">Confess you didn't ask anyone." if (not (HasEvent("Ethan", "AskFondue") or HasEvent("Whitney", "AskFondue") or HasEvent("Rosa", "AskFondue") or HasEvent("Nate", "AskFondue") or HasEvent("Nessa", "AskFondue"))):
            $ AddEvent("Game", "FondueGame")
            leaf @flirtbrow talking2mouth "Seriously? Kinda lame[ellipses]"

    if (HasEvent("Game", "FondueGame")):
        narrator "You and Leaf compare your weirdest found fondue foods, and, by default, you lose."

        leaf talkingmouth closedbrow "Ah, back into it. The undefeatable Leaf Gracidea Green trounces another challenger who literally didn't even try."

        $ SmartMoveOut("leaf")

        $ AnimateValueChange(-1, 0.5, False, 0, "#a00060")

        narrator "You lose one point of {color=#a00060}Party Atmosphere{/color}."

    else:
        leaf talkingmouth closedbrow "Damn, that's good. The weirdest {i}I{/i} got was just someone who thought covering pretzels in chocolate was really daring."

        $ SmartMoveOut("leaf")

        $ PlaySound("07_fanfare.ogg")

        narrator "You and Leaf compare your weirdest found fondue foods, and you win."
        narrator "[ellipses]Though your victory comes with the heavy realization that you have a lot of friends who are willing to put some weird-ass stuff in their bodies[ellipses]"

    jump BunnyPartyStart

    label SkipFondue:
        leaf angrybrow angrysmilemouth @talking2mouth "Boo. You {i}suck.{/i} I'm going to go hang out with Ethan, he's more fun than you."

        $ SmartMoveOut("leaf")

        pause 1.5

        $ MoveInRight("leaf bunny", duration=1.0)

        pause 1.2

        leaf @winkbrow talkingmouth "(Just kidding, I still love ya.)"

        $ SmartMoveOut("leaf")

        pause 0.5

        jump BunnyPartyStart

label BunnyContest:
    python:
        AddEvent("Game", "BunnyContest")
        lastmovein = "Right"
        if (BunRecruit("whitney")):
            MoveInSmart("Whitney bunny")
            
        if (HasEvent("May", "BunnyKitchen")):
            MoveInSmart("may sadbrow bunny")

            if (mallow_present):
                MoveInSmart("mallow bunny", maintain=True)

        if (BunRecruit("nessa")):
            MoveInSmart("nessa bunny")
        
        if (HasEvent("Nate", "JoinBunny")):
            MoveInSmart("nate bunny")
        
        if (BunRecruit("Rosa")):
            MoveInSmart("rosa bunny")

        if (BunRecruit("Melody")):
            MoveInSmart("melody bunny on")

        if (prime_security != "Ethan"):
            MoveInSmart("ethan bunny")
        MoveInSmart("leaf bunny")

    if (BunRecruit("Whitney") and HasEvent("May", "BunnyKitchen")):
        pause 1.0

        narrator "The party guests start to slowly move along to the music[ellipses]"

        show blank2 zorder 100 with dis:
            alpha 0.2

        show whitney zorder 301 with dis:
            ease 0.5 xpos 0.33 ypos 1.1 zoom 1.2

        show may surprisedbrow frownmouth zorder 301 with dis:
            ease 0.5 xpos 0.66 ypos 1.1 zoom 1.2

        whitney @talkingmouth "May, what's up with the long face? C'mon! Dance with us."

        may sadbrow -frownmouth @surprisedbrow talking2mouth "Oh, sorry! I didn't realize--I was staring off, wasn't I?"

        whitney @happy "Little bit! What're you thinking about?"

        may @talkingmouth "The Millennium Drop, what else?"
        may @closedbrow talkingmouth "Brendan and I agreed we wouldn't worry about it today--we'd give ourselves a break from it."
        may @happy "It's a lot easier to say that than to actually {i}do{/i} it, though."

        whitney @talkingmouth "Oh, I know what'll take your mind off things!"

        show may surprisedbrow frownmouth with dis

        whitney @happy "Let's have a dance-off! We'll have the other guests act as judges--and to make it extra-fun, how about we get our Pokémon involved?"

        may @talkingmouth "So[ellipses] like a contest?"

        whitney @talkingmouth "Not at all! It's a dance-off, where our Pokémon compete alongside us, and use moves, and we've got three judges, and it {i}just so happens{/i} to have a lot of rules similar to Pokémon contests!"

        may "[ellipses]"

        may -surprisedbrow -frownmouth @happy "That sounds really fun, actually. Yeah, let's do it."

        may @closedbrow talking2mouth "{size=30}Hm[ellipses] I think I probably shouldn't go {i}all{/i}-out in this contest[ellipses] maybe this would be a good opportunity to train {i}this{/i} little guy?{/size}"

    elif (BunRecruit("Rosa") and BunRecruit("Nessa")):
        pause 1.0

        narrator "The party guests start to slowly move along to the music[ellipses]"

        show blank2 zorder 100 with dis:
            alpha 0.2

        show nessa zorder 301 with dis:
            ease 0.5 xpos 0.66 ypos 1.1 zoom 1.2

        show rosa zorder 301 with dis:
            ease 0.5 xpos 0.33 ypos 1.1 zoom 1.2

        nessa @talkingmouth "You look like you've turning over an idea"

        rosa @talkingmouth "I was just thinking[ellipses] everyone in the school's preparing for the Millennium Drop. What do you know about it?"

        nessa @talkingmouth "More than I need. Or want. Instructor Wallace has been talking about it a lot. Sometimes I feel like the only person in that class who doesn't care much for contests."

        rosa @sad2eyes frownmouth "Hmm[ellipses]"
        rosa @talkingmouth "But you've never {i}actually{/i} competed in a contest, have you?"

        nessa surprisedbrow @neutralbrow talking2mouth "No."

        rosa @talkingmouth "Okay. Well, why don't we set one up now? I think it'd be really fun!"

        nessa @baffledeyes baffledeyebrows baffledmouth "[ellipses]What?"

        rosa @talkingmouth "I've never competed in a contest, either. But it's showbiz, right? Singing, dancing, putting on a show? We're great at that! We should try it out!"

        nessa @sadbrow talkingmouth "I can't do {i}any{/i} of those things. I just look pretty."

        rosa @happy "That's like half the battle, Nessa. C'mon, let's try it out!"

        pause 1.0

        nessa @closedbrow talkingmouth "You would get along {i}so{/i} well with Lee. Alright, let's try this."

    else:
        narrator "A couple partyguests you don't recognize look like they're discussing setting up an impromptu Pokémon contest[ellipses]"

    hide blank2 with dis

    $ LineUp()

    if (HasEvent("May", "BunnyKitchen") and not BunRecruit("Whitney")):
        pause 0.5

        $ HighlightCharacter("May", "bunny")

        may @closedbrow talking2mouth "{size=30}Hm[ellipses] I think I probably shouldn't go {i}all{/i}-out in this contest[ellipses] maybe this would be a good opportunity to train {i}this{/i} little guy?{/size}"

        hide semiblank2 with dis

    if (BunRecruit("Melody")):
        pause 0.5

        $ HighlightCharacter("Melody", "bunny")

        melody up disgustedbrow "[ellipses]"

        narrator "Melody seems wistful, but doesn't say anything[ellipses] seems she's not going to compete."

        hide semiblank2 with dis

    $ LineUp()        

    narrator "The Contest audience will grant extra points to Fire, Normal, and Electric Pokémon. Leporine, or rabbitlike, Pokémon will be most appreciated."
    $ cutecolor = "{color=" + GetContestTypeColor('Cute') + "}Cute{/color}"
    $ coolcolor = "{color=" + GetContestTypeColor('Cool') + "}Cool{/color}"
    narrator "The Contest judges want to see [cutecolor] and [coolcolor] performances."
    narrator "Would you like to join?"

    menu AgreeBunnyContest:
        "Sign me up!":
            pass

        "Wait, what exactly are 'leporine' Pokémon?":
            narrator "The following Pokémon are considered sufficiently rabbitlike for this contest."

            python:
                rabbitstring = []
                for rabbit in rabbit_pokemon_ids:
                    rabbitstring.append(pokedexlookup(rabbit, DexMacros.Forme))
                
                # Display rabbit names in groups of up to 15 per textbox
                for i in range(0, len(rabbitstring), 15):
                    group = rabbitstring[i:i+15]
                    if len(group) == 1:
                        text = group[0] + "."
                    elif len(group) == 2:
                        text = group[0] + " and " + group[1] + "."
                    else:
                        text = ", ".join(group[:-1]) + ", and " + group[-1] + "."
                    renpy.say(None, text)

            menu:
                "There's a lot of Pokémon there that blatantly aren't rabbits.":
                    narrator "'Rabbitlike.' Leporine ears is pretty much the only criteria that matters."

                    menu:
                        "It just feels like a really arbitrary condition, is all.":
                            narrator "Look, I either use a {i}really{/i} loose definition of 'rabbit' for today's events or force you to use Lopunny."

                            if (not HasPokemon('lopunnyobj')):
                                narrator "[ellipses]Which will be difficult for you, since you didn't catch it."

                            menu:
                                "Well, maybe I {i}do{/i} want to use Lopunny! Maybe I want to struggle!":
                                    narrator "If you want to struggle, play {i}Reborn{/i}. Now can I {i}move on{/i}? Thanks."
                                    
                                    $ AddEvent("Game", "BunnyArgument")

                                "Understood.":
                                    pass

                        "Understood.":
                            pass

                "Understood.":
                    pass
                    
            jump AgreeBunnyContest

        "No thanks.":
            jump BunnyPartyStart

    python:
        contestsayerdict = {
            "May": may,
            "Mallow": mallow,
            "Whitney": whitney,
            "Rosa": rosa,
            "Nessa": nessa,
            "Ethan": ethan,
            "Nate": nate,
            "Leaf": leaf,
            "Melody": melody
        }

        judges = []
        for bunny in contestprioritylist:
            if (len(judges) < 3):
                if (bunny not in setascoordinators 
                    and (bunny not in ["Mallow", "Ethan", "May", "Nate", "Melody"] and BunRecruit(bunny)
                    or bunny == "Mallow" and HasEvent("May", "BunnyKitchen") and mallow_present
                    or bunny == "May" and HasEvent("May", "BunnyKitchen")
                    or bunny == "Nate" and HasEvent("Nate", "JoinBunny")
                    or bunny == "Ethan" and not prime_security == "Ethan")):
                    judges.append(Judge(contestsayerdict[bunny], biases={ ContestMoveType.Cute : 40, ContestMoveType.Beautiful : 20, ContestMoveType.Cool : 40, ContestMoveType.Clever : 10, ContestMoveType.Tough : 5 }, customsex=persondex[bunny]["Sex"], imageextras="bunny"))
            else:
                break

        if (len(judges) < 3):
            judges.append(Judge(silhouettebunny, biases={ ContestMoveType.Cute : 40, ContestMoveType.Beautiful : 20, ContestMoveType.Cool : 40, ContestMoveType.Clever : 10, ContestMoveType.Tough : 5 }, customsex=Genders.Female, imageextras="bunny"))
        if (len(judges) < 3):
            judges.append(Judge(silhouettebunny2, biases={ ContestMoveType.Cute : 40, ContestMoveType.Beautiful : 20, ContestMoveType.Cool : 40, ContestMoveType.Clever : 10, ContestMoveType.Tough : 5 }, customsex=Genders.Female, imageextras="bunny"))
        if (len(judges) < 3):
            judges.append(Judge(silhouettebunny3, biases={ ContestMoveType.Cute : 40, ContestMoveType.Beautiful : 20, ContestMoveType.Cool : 40, ContestMoveType.Clever : 10, ContestMoveType.Tough : 5 }, customsex=Genders.Female, imageextras="bunny"))

        contestconditions = {
            "Types" : ["Fire", "Normal", "Electric"],
            "Region" : rabbit_pokemon_ids,
            "Traits" : [ContestMoveType.Cute, ContestMoveType.Cool]
        }

    call Contest("Cute 'n' Sexy Bunny Party Dance-Off Spectacular", coordinators, judges, contestconditions) from _call_Contest

    scene bunday
    show blank2
    with dis
    $ lastmovein = "Right"
    if (BunRecruit("whitney")):
        $ MoveInSmart("Whitney bunny", behind=["blank2"])
        
    if (HasEvent("May", "BunnyKitchen")):
        $ MoveInSmart("may sadbrow bunny", behind=["blank2"])

        if (mallow_present):
            $ MoveInSmart("mallow bunny", maintain=True, behind=["blank2"])

    if (BunRecruit("nessa")):
        $ MoveInSmart("nessa bunny", behind=["blank2"])

    if (HasEvent("Nate", "JoinBunny")):
        $ MoveInSmart("nate bunny", behind=["blank2"])

    if (BunRecruit("rosa")):
        $ MoveInSmart("rosa bunny", behind=["blank2"])
    
    if (prime_security != "Ethan"):
        $ MoveInSmart("ethan bunny")
    $ MoveInSmart("leaf bunny")

    pause 0.5

    hide blank2 with Dissolve(1.0)

    $ winner = contesthistory["Cute 'n' Sexy Bunny Party Dance-Off Spectacular"][0].GetName()

    if (winner == first_name):
        red @happy "Boom! Can't beat the bunny."

        if (HasEvent("May", "BunnyKitchen")):
            $ HighlightCharacter("May", "bunny")

            may @flirtbrow talkingmouth "You want to try again when I take it seriously?"

            red @wince talkingmouth "{size=30}Nothankyou.{/size}"

        else:
            $ HighlightCharacter("Leaf", "bunny")

            leaf @flirtbrow talking2mouth "Yeah, well done, you beat a bunch of people using Pokémon that have {i}never{/i} coordinated before."

            red @sadbrow talkingmouth "Thank you for literally {i}sucking{/i} the wind from my sails, Leaf. You're like some kind of victory vacuum."

            leaf @winkbrow talkingmouth "That's what I'm here for!"

    elif (winner == "Ethan"):
        $ HighlightCharacter("Ethan", "bunny")

        ethan happyeyes @happy "Man, if my Dad could see me now!"

        show ethan sweat with Dissolve(1.0)

        ethan @sad2eyes sadeyebrows talkingmouth "Maybe I'll tell him about winning a contest, just, uh, without the context."

    elif (winner == "Leaf"):
        $ HighlightCharacter("Leaf", "bunny")

        leaf surprisedbrow frownmouth @talking2mouth "This is--this is some kind of prank, right? Where's the camera?"

        red @sadbrow talkingmouth "No prank. You {i}really{/i} did just win the contest. Well done!"

        pause 1.0

        leaf sad "[ellipses]Ugh."

    elif (winner == "Nate"):
        $ HighlightCharacter("Nate", "bunny")

        nate @sadbrow talkingmouth "{size=30}Damn, in another life, I could've gone pro as a coordinator.{/size}" 
        nate @happy "Guess I'll just have to keep {i}this{/i} memory forever. Thanks for the contest, everyone. This was--it was nice. Seriously."

    elif (winner == "Rosa"):
        $ HighlightCharacter("Rosa", "bunny")

        rosa @sadbrow talkingmouth "Sorry, everyone! I guess this was a tiny bit unfair? I've never coordinated before, but it's not {i}that{/i} different from dancing onstage." 

        if (BunRecruit("Nessa")):
            show rosa zorder 301 with dis:
                ease 0.5 xpos 0.66 ypos 1.1 zoom 1.2

            show nessa zorder 301 with dis:
                ease 0.5 xpos 0.33 ypos 1.1 zoom 1.2

            nessa angryeyebrows frownmouth @talking2mouth "You're too good an actress to be so bad at acting falsely modest."

            rosa @lightblush tonguemouth happybrow "Tee hee!"

        elif (GetRelationshipRank("Rosa") > 0):
            redmind @poutmouth sad2eyes "[ellipses]She's way too good an actress to be so bad at acting falsely modest."

    elif (winner == "Mallow"):
        $ HighlightCharacter("Mallow", "bunny")

        show mallow surprisedbrow frownmouth with dis

        pause 1.0

        red @talking2mouth "Uh[ellipses] May? Is she alright?"

        show may zorder 301 with dis:
            ease 0.5 xpos .66 ypos 1.1 zoom 1.2

        show mallow zorder 301 with dis:
            ease 0.5 xpos .33 ypos 1.1 zoom 1.2

        may @blush talkingmouth "She's[ellipses] not used to winning things. I'll look after her, don't worry."

    elif (winner == "Nessa"):
        $ HighlightCharacter("Nessa", "bunny")

        show nessa surprisedbrow frownmouth with dis

        pause 1.0

        nessa @talking2mouth "[ellipses]Huh."
        nessa @closedbrow talkingmouth "Well, that's something new. Maybe I've got more options than I thought"

        pause 1.0

        nessa @sad2brow talkingmouth "Of course, older coordinators don't see a lot of success, either[ellipses]"

    elif (winner == "May"):
        $ HighlightCharacter("May", "bunny")

        may sadbrow @talkingmouth blush "Er[ellipses] sorry, everyone. I {i}really{/i} was trying to go easy on you."

        narrator "The rest of the party doesn't seem particularly receptive to May's apology[ellipses]"

    elif (winner == "Whitney"):
        $ HighlightCharacter("Whitney", "bunny")

        whitney @talkingmouth "Hah! Take that! The incredibly pretty girl is a triple threat--battles, baseball, {i}and{/i} contests!"

        if (BunRecruit("Nessa")):
            show whitney zorder 301 with dis:
                ease 0.5 xpos 0.66 ypos 1.1 zoom 1.2

            show nessa zorder 301 with dis:
                ease 0.5 xpos 0.33 ypos 1.1 zoom 1.2

            nessa @talkingmouth closedbrow "{size=30}And humility, obviously.{/size}"

            whitney @closedbrow talkingmouth "It's alright to be jealous."

            $ SmartMoveOut("Whitney", exclude=["nessa"])

            nessa angrybrow frownmouth "[ellipses]"
            nessa @talking2mouth angrybrow "How did {i}that{/i} get under my skin?"

        else:
            redmind @upbrow "And humility, clearly."

    jump BunnyPartyStart

label BunnyCardsAgainstPokemonity:
    #drop into game
    #select who is "Card King", and see what the different scenes are based on that.

    python:
        if (BunRecruit("whitney")):
            MoveInSmart("Whitney bunny", behind=["blank2"])
            
        if (HasEvent("May", "BunnyKitchen")):
            MoveInSmart("may sadbrow bunny", behind=["blank2"])

            if (mallow_present):
                MoveInSmart("mallow bunny", maintain=True, behind=["blank2"])

        if (BunRecruit("nessa")):
            MoveInSmart("nessa bunny", behind=["blank2"])

        if (HasEvent("Nate", "JoinBunny")):
            MoveInSmart("nate bunny", behind=["blank2"])

        if (BunRecruit("rosa")):
            MoveInSmart("rosa bunny", behind=["blank2"])

        if (BunRecruit("Melody")):
            MoveInSmart("melody bunny on", behind=["blank2"])
        
        if (prime_security != "Ethan"):
            MoveInSmart("ethan bunny")

        MoveInSmart("leaf bunny")

    narrator "A thriving game of Cards Against Pokémonity is in-progress[ellipses] who's the Card King?"

    menu BunnyPokemonityMenu:
        "Rosa" if BunRecruit("Rosa"):
            $ HighlightCharacter("Rosa", "bunny", reset=True)
            $ LineUp(exclude=["Rosa"], prefilled=[0.5], inner_band=0.02, considerexcludes=False)

            rosa @happy "Oh, {i}this one's{/i} not so bad. {i}Ahem!{/i}"
            rosa @talkingmouth "Coming to theaters this Summer: __________, the untold true story of Pokéstar Studios!"

            pause 1.0

            rosa @confused "Did someone stack this deck[ellipses]?"

            narrator "Everyone passes their answers in."

            rosa @happy "Okay, time to read these out!" 
            rosa @sadbrow talkingmouth sweat "Um, please don't tell my managers I said any of these words[ellipses]"

            if (BunRecruit("Nessa")):
                rosa @talkingmouth "Coming to theaters this Summer: {u}Creepy old rich men{/u}, the untold true story of Pokéstar Studios!"

                pause 0.5

                nessa bunny @closedbrow talkingmouth "Heh."

                rosa @sadbrow talkingmouth "Well, some of them are actually quite nice, as long as you're never alone with them[ellipses]?"

            if HasEvent("May", "BunnyKitchen"):
                rosa @talkingmouth "Coming to theaters this Summer: {nw}"
                extend @surprisedbrow talking2mouth "{u}Drug-Fueled Giratina-Worshipping Orgies of{/u}--{nw}"
                extend @angrybrow angrymouth "okay, no, I'm not reading this! Who submitted this one?!"
                
                may bunny @sadbrow poutmouth "[ellipses]"

            if HasEvent("May", "BunnyKitchen") and mallow_present:
                rosa @talkingmouth "Coming to theaters this Summer: {u}Killing the token minority off first{/u}, the untold true story of Pokéstar Studios!"

                pause 1.0

                rosa @sadbrow sweat talking2mouth "In, um, I think a solid {i}third{/i} of my movies, the tok--a minority {i}doesn't{/i} die first."

                pause 1.0

                rosa @happybrow talkingmouth sweat "If that helps[ellipses]?"

                mallow bunny @angrybrow angrymouth "It doesn't!"

            if BunRecruit("Nate") and HasEvent("Nate", "JoinBunny"):
                rosa @talkingmouth "Coming to theaters this Summer: {u}Secret celebrity sex basements{/u}, the untold true story of Pokéstar Studios!"

                pause 0.5

                rosa @surprisedbrow frownmouth "[ellipses]Wait, who told?"

                pause 1.0

                rosa @happy "I'm just kidding! We don't have anything like that, seriously."

                nate bunny @sad2eyes talkingmouth "{size=30}That {i}you{/i} know about[ellipses]{/size}"
            
            if BunRecruit("Melody"):
                rosa @talkingmouth "Coming to theaters this Summer: {u}Autotuning someone who can't sing{/u}, the untold true story of Pokéstar Studios!"
                
                pause 1.0

                rosa @talkingmouth "I'm {i}really{/i} sorry. I keep telling agents that they shouldn't cast me for singing roles, but they care more about the name recognition than[ellipses] well, anything else."

                melody "[ellipses]"

            if prime_security != "Ethan":
                rosa @talkingmouth "Coming to theaters this Summer: {u}Sequels that just aren't quite as good as the originals{/u}, the untold true story of Pokéstar Studios!"

                pause 0.5

                ethan bunny @talking2mouth closedbrow "{size=30}{i}Cough.{/i}{/size}"

                rosa @closedeyes angryeyebrows talking2mouth "Yeah, hah hah, very funny. Let's just move on."

            rosa @talkingmouth "Coming to theaters this Summer: {u}Leaf Gracidea Green, Rosa Whitley's wife{/u}, the untold true story of Pokéstar Studios!"

            pause 1.0

            rosa @smugeyes neutraleyebrows talking2mouth "This is written in pen on a blank card[ellipses]"

            leaf @closedbrow talking2mouth "Huh. Could've been anyone."

            rosa @talkingmouth sadbrow "I'm straight, Leaf."

            leaf @closedbrow talkingmouth "{size=30}Could've been anyone[ellipses]{/size}"

            if BunRecruit("Whitney"):
                rosa @talkingmouth "Coming to theaters this Summer: {u}Sexy eating disorders{/u}, the untold true story of Pokéstar Studios!"

                pause 0.5

                rosa @winkeyes sadeyebrows sweat talking2mouth "[ellipses]Ow. That one hits a bit too close to home."

                pause 0.5

                whitney bunny @happy "That means I win, right?!"

                rosa @sadbrow talkingmouth sweat "I don't think you're supposed to reveal which card was yours until I make a decision[ellipses]"

        "Nessa" if BunRecruit("Nessa"):
            $ HighlightCharacter("Nessa", "bunny", reset=True)
            $ LineUp(exclude=["Nessa"], prefilled=[0.5], inner_band=0.02, considerexcludes=False)

            nessa @closedbrow talking2mouth "Hm. This should be good."
            nessa @talkingmouth "Dating red flag: Your date shows up wearing ___________."

            pause 1.0

            nessa @closedbrow talkingmouth "Bonus points if you actually make me laugh."

            narrator "Everyone passes their answers in."

            nessa @closedbrow talkingmouth "Alright. Let's see what you've got."

            if (BunRecruit("Rosa")):
                nessa @talkingmouth "Dating red flag: Your date shows up wearing {u}leather pants made from the casting couch{/u}."

                pause 0.5

                show rosa surprisedbrow frownmouth lightblush with dis

                nessa bunny @surprisedbrow surprisedmouth "Rosa? What the fuck?"

                rosa @surprisedbrow surprisedmouth sweat "I--I thought it was funny! I didn't think you'd know it was {i}me!{/i}"

                nessa @closedbrow talkingmouth "I didn't, until just now."

                rosa -surprisedbrow -frownmouth -blush @sadbrow talkingmouth sweat "Aw, you got me[ellipses]"

            if HasEvent("May", "BunnyKitchen"):
                nessa @talkingmouth "Dating red flag: Your date shows up wearing {u}an apron and nothing else{/u}."

                pause 1.0

                nessa @closedbrow talkingmouth "Not {i}necessarily{/i} a dealbreaker."
                
                may bunny @sadbrow poutmouth "{size=30}That's what I said! But Brendan[ellipses]{/size}"

            if HasEvent("May", "BunnyKitchen") and mallow_present:
                nessa @talkingmouth "Dating red flag: Your date shows up wearing {u}a lightly-charred grass skirt{/u}."

                pause 0.5

                nessa @talking2mouth surprisedbrow "I feel like this is a very specific reference to something I don't get."

                mallow @talkingmouth "{size=30}Why would you want to date a firedancer who's bad at his job?{/size}"

                may @closedbrow talkingmouth "{size=30}Mallow, she's kinda right[ellipses]{/size}"

            if BunRecruit("Nate") and HasEvent("Nate", "JoinBunny"):
                nessa @talkingmouth "Dating red flag: Your date shows up wearing {u}an orange jumpsuit{/u}."

                pause 0.5

                nessa @closedbrow talkingmouth "I'll say. Orange isn't anyone's color."

                nate @talking2mouth "And being outside of the prison? Just reeks of commitment issues, right?"

                nessa @talkingmouth "Yeah, you get it."

            if BunRecruit("Melody"):
                nessa @talkingmouth "Dating red flag: Your date shows up wearing {u}a cape{/u}."
                
                pause 1.0

                nessa @talkingmouth "There are a very, {i}very{/i} limited number of people who can pull off capes. Most people who try[ellipses] shouldn't."

                melody @talking2mouth "{size=30}Not everyone's Dragon Tamer material.{/size}"

            if prime_security != "Ethan":
                nessa @talkingmouth "Dating red flag: Your date shows up wearing {u}nothing at all{/u}."

                pause 0.5

                ethan bunny @talking2mouth closedbrow "{size=30}{i}Cough.{/i}{/size}"

                nessa @closedeyes angryeyebrows talking2mouth "That was the obvious answer, right? At least we got it out of the way."

            nessa @talkingmouth "Dating red flag: Your date shows up wearing {u}a pair of oversized glasses and a fake moustache{/u}."

            pause 1.0

            nessa @talking2mouth "I don't know. A sense of humor can be sexy."

            if (HasEvent("Leaf", "AcceptedConfession")):
                redmind @sad2eyes "Not {i}necessarily{/i} a dealbreaker."

            if BunRecruit("Whitney"):
                nessa @talkingmouth "Dating red flag: Your date shows up wearing {u}overpriced Fang Gang merch{/u}."

                pause 1.0

                redmind @thonk "What's she[ellipses]"

                nessa @closedbrow "{size=30}Heh.{/size}"

                nessa @angrybrow talking2mouth "Damn it."

                narrator "Whitney looks very pleased with herself[ellipses]"

        "May" if HasEvent("May", "BunnyKitchen"):
            $ HighlightCharacter("May", "bunny", reset=True)
            $ LineUp(exclude=["May"], prefilled=[0.5], inner_band=0.02, considerexcludes=False)

            may @happy "Oh, this one's great! Give me your grossest, rudest, most awful answers!"
            may @flirtbrow blush "Ahem[ellipses]"
            may @flirtbrow blush talkingmouth "During sex, I like to think about _____________."

            pause 1.0

            leaf @sadbrow talkingmouth "{size=30}Oh, yeah, this is going to be a trainwreck.{/size}"

            narrator "Everyone passes their answers in, somewhat unnerved by May's clear enthusiasm."

            if (BunRecruit("Nessa")):
                may @flirtbrow blush talkingmouth "During sex, I like to think about {u}transparent clothing{/u}."

                pause 0.5

                may @happybrow talkingmouth "Ooh, adding {i}that{/i} to the bucket list!"

                nessa @talking2mouth "Get crepeline, plastic makes too much noise."

            if BunRecruit("Rosa"):
                may @flirtbrow blush talkingmouth "During sex, I like to think about {u}leaking my own sex tape{/u}."
                
                pause 1.0

                may @surprisedbrow bigblush frownmouth "{size=30}Oh. That's--{/size}"
                may @happy "No comment! Let's move on!"

            if mallow_present:
                may @flirtbrow blush talkingmouth "During sex, I like to think about {u}environmentally-friendly alternatives to condoms{/u}."
                
                pause 0.5

                may @happy "You know, there's one environmentally-friendly alternative that makes absolutely {i}no{/i} waste at all!"

                redmind @wince frownmouth "Fascinating. Let's not hear it, please."

            if BunRecruit("Nate") and HasEvent("Nate", "JoinBunny"):
                may @flirtbrow blush talkingmouth "During sex, I like to think about {u}Big Brother watching me{/u}."

                pause 0.5

                may @closedbrow talking2mouth "Oh, ew. Now I'm thinking about my little brother. Okay, gross, gross, let's restart and pretend I didn't get this card."

                nate @talkingmouth sweat sadbrow "{size=30}I guess she hasn't read that book.{/size}"

            if BunRecruit("Melody"):
                may @flirtbrow blush talkingmouth "During sex, I like to think about {u}that catchy jingle from the gum commercial{/u}."
                
                pause 1.0

                $ GroupExpression("angrybrow frownmouth", exclude=["melody"])

                narrator "A sour expression settles on everyone's faces, as that goddamn jingle slides in, entirely unbidden."

                melody @talkingmouth "{size=30}TripleDent gum will make you smile[ellipses]{/size}"

                $ GroupExpression("neutralbrow neutralmouth")

            if prime_security != "Ethan":
                may @talkingmouth "During sex, I like to think about {u}my failing marriage{/u}."

                pause 0.5

                ethan bunny @talking2mouth closedbrow "{size=30}{i}Cough.{/i}{/size}"

                may @angrybrow talking2mouth "That one isn't funny."

            may @talkingmouth "During sex, I like to think about {u}the really thin walls my dormmates can totally hear me through{/u}."

            pause 1.0

            may @sadbrow talkingmouth "Um. Sorry[ellipses]"

            leaf @talkingmouth "Hey, I'm not your dormie anymore. Apologize to the new guys."

            if BunRecruit("Whitney"):
                may surprisedbrow frownmouth @talking2mouth "During sex, I like to think about {u}chocolate syrup drizzled all over my body{/u}."

                pause 0.5

                narrator "May's breathing gets notably heavier, and her eyes flick over to the chocolate fondue fountain."

                may @talkingmouth "Um[ellipses] this one. This one wins! For no particular reason[ellipses]"

                whitney @happy "That's another one for me!"

        "Mallow" if HasEvent("May", "BunnyKitchen") and mallow_present:
            $ HighlightCharacter("Mallow", "bunny", reset=True)
            $ LineUp(exclude=["Mallow"], prefilled=[0.5], inner_band=0.02, considerexcludes=False)

            mallow @surprisedbrow talking2mouth "[ellipses]Okay, {i}someone{/i} definitely stacked the deck."
            mallow @closedbrow talking2mouth "As reparations for Unovan imperialism, all Alolan citizens will recieve ___________."

            narrator "Everyone passes their answers in, while May is quickly making a slashing gesture at her throat."

            if (BunRecruit("Nessa")):
                mallow @talkingmouth "As reparations for Unovan imperialism, all Alolan citizens will recieve {u}a pat on the back and{/u}{nw}"
                extend @surprised "{u} an unenthusiastic handjob?!{/u}"

                pause 1.0

                mallow @sadbrow talking2mouth "I'm not sure I want that[ellipses]"

                nessa @talking2mouth "{size=30}Hey, it's more than Raihan's parents got.{/size}"

            if BunRecruit("Rosa"):
                mallow @talkingmouth "As reparations for Unovan imperialism, all Alolan citizens will recieve {u}a passionate defense of the argument it was actually about Regions' Rights{/u}."
                
                pause 0.5

                mallow @angry "A region's right to do {i}what{/i}?! What, exactly?!"

            if BunRecruit("May"):
                mallow @talkingmouth "As reparations for Unovan imperialism, all Alolan citizens will recieve {u}a tray of special brownies{/u}."
    
                pause 0.5

                mallow @closedbrow talking2mouth "Could be worse. Just don't let my Mama know."

            if BunRecruit("Nate") and HasEvent("Nate", "JoinBunny"):
                mallow @talkingmouth "As reparations for Unovan imperialism, all Alolan citizens will recieve {u}police brutality{/u}."

                pause 1.0

                mallow @angrybrow frownmouth "Hmph."
            
            if BunRecruit("Melody"):
                mallow @talkingmouth "As reparations for Unovan imperialism, all Alolan citizens will recieve {u}more relevance than the Orange Islands{/u}."

                pause 0.5

                mallow @happy "Hey, that's right! I guess it could always be worse!"
                
                melody @talkingmouth "{size=30}Always can.{/size}"

            if prime_security != "Ethan":
                mallow @talkingmouth "As reparations for Unovan imperialism, all Alolan citizens will recieve {u}absolutely nothing{/u}."

                pause 0.5

                ethan bunny @talking2mouth closedbrow "{size=30}{i}Cough.{/i}{/size}"

                mallow @angrybrow talking2mouth "Being true doesn't make it funny."

            mallow @talkingmouth "As reparations for Unovan imperialism, all Alolan citizens will recieve {u}cake{/u}."

            pause 0.5

            mallow @sadbrow talking2mouth "I've heard that before. It was a lie. The cake is always a lie."

            if BunRecruit("Whitney"):
                mallow @talkingmouth "As reparations for Unovan imperialism, all Alolan citizens will recieve {u}the beautiful islands of Alola{/u}."

                pause 0.5

                mallow @happy "Yeah! Yeah, I guess we did, didn't we? I like this one! This one's nice and wholesome. Who was it?"

                whitney @winkbrow talkingmouth "That's me, of course!"

        "Nate" if BunRecruit("Nate") and HasEvent("Nate", "JoinBunny"):
            $ HighlightCharacter("Nate", "bunny", reset=True)
            $ LineUp(exclude=["Nate"], prefilled=[0.5], inner_band=0.02, considerexcludes=False)

            nate @happy "Hah, this is great. As a heads-up, anyone who can land a pun here will win."
            nate @talkingmouth "Alright, here's the card."
            nate @happy "The biggest threat facing society? _____________."

            pause 0.5

            narrator "Everyone passes their answers in."

            if (BunRecruit("Nessa")):
                nate @talkingmouth "The biggest threat facing society? {u}RotoPhotos Comments Sections{/u}."

                pause 0.5

                nate @confused "Uh[ellipses] I don't get it?"

                nessa @closedbrow talking2mouth "Take a look at my RotoPhotos page, and you will."

            if BunRecruit("Rosa"):
                nate @talkingmouth "The biggest threat facing society? {u}An endless parade of derivative sequels{/u}."
                
                pause 0.5

                nate @sadbrow talkingmouth "You know, I actually kinda like sequels. The consistency is nice--knowing I get to watch the same movie over and over, with only small iterations on--"
                nate @happy "Ah, nevermind. Let's move on."

            if HasEvent("May", "BunnyKitchen"):
                nate @talkingmouth "The biggest threat facing society? {u}Public indecency laws{/u}."
                
                pause 0.5

                nate @winkbrow talkingmouth "I think we all know who submitted this one."

            if HasEvent("May", "BunnyKitchen") and mallow_present:
                nate @talkingmouth "The biggest threat facing society? {u}The Unovan Champion{/u}."
                
                pause 0.5

                nate @closedbrow talkingmouth sweat "Not sure that's fair to her, she's, like, four."
                nate @happy "'Course, kids can be cruel!"

            if BunRecruit("Melody"):
                nate @talkingmouth "The biggest threat facing society? {u}Rich old men{/u}."

                pause 0.5

                nate @talkingmouth "Tell me about it. If you tracked where the money for our politicians' campaigns is coming from, you'd be horrified. Here's a hint--it's way fewer people than you think."
                
                melody @talking2mouth "I was more concerned about the rich old men who {i}are{/i} the politicians, not the rich old men standing behind them."

                nate @sadbrow talkingmouth "It's rich old men all the way down."

            if prime_security != "Ethan":
                nate @talkingmouth "The biggest threat facing society? {u}The Shadow Government's Mind Control Waves{/u}."

                pause 0.5

                ethan bunny @talking2mouth closedbrow "{size=30}{i}Cough.{/i}{/size}"

                nate @upeyes angryeyebrows talking2mouth "I can't help but think that if this 'Shadow Government' was even a tenth as powerful as people think, it wouldn't need to be a {i}Shadow{/i} Government."

            nate @talkingmouth "The biggest threat facing society? {u}The bisexual curse of finding everyone hot{/u}."

            pause 0.5

            nate @closedbrow talkingmouth "You know, I never 'got' Bisexuals. Pick a side, and jump over the fence whenever you want, like I do. Trying to hog both sides at once is greedy."

            leaf @sadbrow talkingmouth "Sounds like you just can't handle what we can."

            red @confused "Where does the council stand on Pansexuals?"

            nate @happy "Wherever they want us to, as long as they ask nicely."

            if BunRecruit("Whitney"):
                nate @talkingmouth "The biggest threat facing society? {u}Mass surveillance{/u}."

                pause 0.5

                nate @confused "Huh?"

                whitney @happy "It's bad enough that we have to watch our own figures!"

                pause 1.0

                nate @surprisedbrow talking2mouth "Huh[ellipses]"
                nate @talkingmouth happybrow "Hah."
                nate @happy "Hah hah hah hah hah hah! Oh, that one's {i}great!{/i} And you even got a pun in. Maybe that's cheating, but that was {i}really{/i} good. {i}Hah!{/i} A W for W!"

        "Whitney" if BunRecruit("Whitney"):
            $ HighlightCharacter("Whitney", "bunny", reset=True)
            $ LineUp(exclude=["Whitney"], prefilled=[0.5], inner_band=0.02, considerexcludes=False)

            whitney @happy "Okay, okay! My turn!"
            whitney @talkingmouth "Ooh, this is a fun one[ellipses]"
            whitney @blush talkingmouth "It was love at first sight. Why? _____________."

            narrator "Everyone passes their answers in."

            if (BunRecruit("Nessa")):
                whitney @talkingmouth "It was love at first sight. Why? {u}My sexy, sexy, body{/u}."

                pause 0.5

                whitney @talkingmouth "Sure, it usually is. Who submitted this card? Let's talk later."

                if (HasEvent("Whitney", "Whitney2Part2")):
                    whitney @surprisedbrow talking2mouth "Oh, wait[ellipses]"
                    whitney @sad2brow talking2mouth blush "Um, nevermind."

                    nessa @closedbrow talkingmouth "{size=30}I'm heartbroken, truly.{/size}"

                else:
                    nessa @closedbrow talkingmouth "{size=30}Respectfully: pass.{/size}"

            if BunRecruit("Rosa"):
                whitney @talkingmouth "It was love at first sight. Why? {u}A certain director's foot fetish{/u}."
                
                pause 0.5

                whitney @sadbrow talkingmouth "You know, I heard about that, but does he {i}actually{/i}--"

                rosa @closedbrow talking2mouth sweat "Yes, absolutely."

            if HasEvent("May", "BunnyKitchen"):
                whitney @talkingmouth "It was love at first sight. Why? {u}An emotionally-regulated man{/u}."
                
                pause 0.5

                whitney @talking2mouth closedbrow "You find one for me, and {i}then{/i} I'll laugh."

                redmind @upeyes angryeyebrows frownmouth "I'm offended not just for myself, but for all men."

            if HasEvent("May", "BunnyKitchen") and mallow_present:
                whitney @talkingmouth "It was love at first sight. Why? {u}Infodumping on my special interest{/u}."
                
                pause 0.5

                whitney @happy "That's so true, though! No-one's ever cuter than when they're speaking passionately about something."

            if BunRecruit("Nate") and HasEvent("Nate", "JoinBunny"):
                whitney @talkingmouth "It was love at first sight. Why? {u}Changing myself to be more lovable{/u}."

                pause 0.5

                whitney @happy "Boo, no way! I'm already lovable. {i}Everyone else{/i} should change."
                
                if (HasEvent("Whitney", "Whitney2Part2")):
                    pause 1.0

                    whitney @sad2brow talking2mouth blush "Okay, not {i}everyone.{/i} But, like, several people."

            if BunRecruit("Melody"):
                whitney @talkingmouth "It was love at first sight. Why? {u}Mutual disgust toward the same thing{/u}."

                pause 0.5

                whitney @happy "Well[ellipses] that's kinda like a passion! Hating the same things can bring people together, too, I guess."
                
                melody @talking2mouth "{size=30}There's no-one more certain of what they love than a certified hater.{/size}"

            if prime_security != "Ethan":
                whitney @talkingmouth "It was love at first sight. Why? {u}Bees?{/u}"

                pause 0.5

                ethan bunny @talking2mouth closedbrow "{size=30}{i}Cough.{/i}{/size}"

                whitney @closedbrow talking2mouth "This makes no sense, and bees suck."

            whitney @talkingmouth "It was love at first sight. Why? {u}Sexy but off-putting desperation{/u}."

            pause 0.5

            whitney @closedbrow talkingmouth "Well, {i}I{/i} don't know what that's like. I'm {i}never{/i} off-putting."

            pause 1.0

            whitney @happy "Next round, right?"

            leaf @talkingmouth "Sure, but who won your round?"

            whitney @surprised "Oh! Right!"
            whitney @talkingmouth happybrow sweat "I like being a player way more than being Card King, so I kinda forgot that part of the role."
            whitney @talking2mouth "Hm[ellipses] I guess I liked[ellipses]"

        "Melody" if BunRecruit("Melody"):
            $ HighlightCharacter("Melody", "bunny on", reset=True)
            $ LineUp(exclude=["Melody"], prefilled=[0.5], inner_band=0.02, considerexcludes=False)

            melody @talking2mouth "[ellipses]I'm sorry Professor, but I couldn't complete my homework because of _____________."

            pause 1.0

            melody smilemouth @closedbrow talking2mouth "Alright. Roll them out."

            redmind @thonk "I can't tell if she's starting to have fun or just trying to get through this[ellipses]"

            narrator "Everyone passes their answers in."

            melody @talkingmouth "{size=30}Hah.{/size}"
            melody @talking2mouth "You're all sick."

            if (BunRecruit("Whitney")):
                whitney bunny happy "Guilty!"

            if (BunRecruit("Rosa")):
                melody @talkingmouth "I'm sorry Professor, but I couldn't complete my homework because of {u}a ten-hour Lord of the Chain marathon{/u}."

                pause 0.5

                melody "[ellipses]{nw}"
                extend @talking2mouth "You know, those movies were filmed on the Orange Islands."

                rosa surprisedbrow frownmouth @happy "Did you know that when Viggo Montensen kicked that helmet, he broke his--."

                $ GroupExpression("angrybrow talking2mouth", exclude=["rosa"])

                TempCharacter("Literally Everyone") "YES."

                $ GroupExpression("neutralbrow neutralmouth")

            if (BunRecruit("Nessa")):
                melody @talkingmouth "I'm sorry Professor, but I couldn't complete my homework because of {u}a pervasive sense of apathy{/u}."

                pause 0.5

                melody @talking2mouth "It's a power move, for sure. The Professor's gotta respect the honesty."

                nessa @talking2mouth "Most people don't know how to respond when you don't care about something they're trying to make you care about."

            if HasEvent("May", "BunnyKitchen"):
                melody @talkingmouth "I'm sorry Professor, but I couldn't complete my homework because of {u}loudly announcing I'm trying to get pregnant{/u}."

                pause 0.5

                melody @talking2mouth "Real talk, as your senior: Keep that shit out of school. It's literally only one year--if you can't even wait that long, welcome to the bottom twenty."

                may @angrybrow poutmouth "{size=30}It was just a joke[ellipses]{/size}"

            if HasEvent("May", "BunnyKitchen") and mallow_present:
                melody @talkingmouth "I'm sorry Professor, but I couldn't complete my homework because of {u}being arrested for environmental protests{/u}."

                pause 0.5

                melody @sadbrow talking2mouth "Some Professors would forgive that. Not Kobukan's, though. Kobukan's suck."

                if (HasEvent("May", "BunnyKitchen")):
                    may angrybrow frownmouth @talking2mouth "You know my Dad works here."

                melody @talking2mouth "Yeah, I do."

                pause 1.0

                mallow @sadbrow talkingmouth "{size=30}Um[ellipses] my card[ellipses]?{/size}"

            if BunRecruit("Nate") and HasEvent("Nate", "JoinBunny"):
                melody @talkingmouth "I'm sorry Professor, but I couldn't complete my homework because of {u}a top-secret mission I can only frustratingly hint at{/u}."

                pause 0.5

                show nate surprisedbrow frownmouth with dis

                melody @talking2mouth "Sidebar: Who in this group is most likely to be a secret agent?"

                pause 0.5

                if (BunRecruit("Nessa")):
                    melody @talking2mouth "Personally, I'm thinking Nessa. I feel like she could take secrets to the grave."

                    nessa @closedbrow talkingmouth "And beyond."

                else:
                    melody @talking2mouth "Personally, I'm thinking Ethan. Guy never speaks. He has to have secrets."

                    ethan @angrybrow talking2mouth "I speak all the time!"

                    melody @closedbrow talking2mouth "So silent. So mysterious."
                
                show nate -surprisedbrow -frownmouth with dis

            if prime_security != "Ethan":
                melody @talkingmouth "I'm sorry Professor, but I couldn't complete my homework because of {u}our nasty, forbidden love{/u}."

                pause 0.5

                ethan bunny @talking2mouth closedbrow "{size=30}{i}Cough.{/i}{/size}"

                melody @talking2mouth "Gross. Weird. We're moving on."

            melody @talkingmouth "I'm sorry Professor, but I couldn't complete my homework because of {u}goddamn glitter everywhere{/u}."

            pause 0.5

            melody @talking2mouth "I feel like this is a very personal grievance someone here has."

            leaf @angrybrow talking2mouth "{size=30}Nothing about glitter bombs is personal. They're a war crime.{/size}"

            if BunRecruit("Whitney"):
                melody @talkingmouth "I'm sorry Professor, but I couldn't complete my homework because of {u}literally so many better things to do{/u}."

                pause 0.5

                melody @talkingmouth "Wow. Literally the perfect answer. This one gets it."

                pause 0.5

                whitney bunny @happy "And that's another for the pile!"

        "Leaf":
            $ HighlightCharacter("Leaf", "bunny", reset=True)
            $ LineUp(exclude=["Leaf"], prefilled=[0.5], inner_band=0.02, considerexcludes=False)

            narrator "Leaf's head snaps up when you walk near."

            leaf @happy "Hey, [first_name]! C'mon, join the game."

            red @sadbrow talkingmouth "I[ellipses] uh[ellipses] don't really think my Mom would appreciate me saying some of this stuff."

            leaf @flirtbrow talkingmouth "Seriously? That's your excuse for chickening out? You realize that makes you look {i}way{/i} worse than if you joined and did garbage, right?"

            red @talking2mouth "Yeah, but it's also the truth, so[ellipses]"

        "Ethan" if prime_security != "Ethan":
            $ HighlightCharacter("Ethan", "bunny", reset=True)
            $ LineUp(exclude=["Ethan"], prefilled=[0.5], inner_band=0.02, considerexcludes=False)

            narrator "There seems to be a bit of a lull in the game, and not much discussion is happening as cards are being passed in."

        ">Leave the circle":
            if (prime_security != "Ethan"):
                narrator "As you prepare to leave the circle, you notice that Ethan seems to be winning the game by a fair margin[ellipses]"
            elif (BunRecruit("Whitney")):
                narrator "As you prepare to leave the circle, you notice that Whitney seems to be winning the game by a fair margin[ellipses]"

            jump BunnyPartyStart

    narrator "You've heard enough for now[ellipses]"

    $ GroupExpression("neutralbrow neutralmouth bunny", append=False)

    jump BunnyPokemonityMenu

label LeafBunnyFossils:
    python:
        AddEvent("Game", "LeafBunnyFossils")
        MoveInSmart("leaf bunny")
        if (BunRecruit("whitney")):
            MoveInSmart("Whitney bunny")
            
        if (HasEvent("May", "BunnyKitchen")):
            MoveInSmart("may sadbrow bunny")

            if (mallow_present):
                MoveInSmart("mallow bunny", maintain=True)

        if (BunRecruit("nessa")):
            MoveInSmart("nessa bunny")
        
        if (BunRecruit("Nate") and HasEvent("Nate", "JoinBunny")):
            MoveInSmart("nate bunny")
        
        if (BunRecruit("rosa")):
            MoveInSmart("rosa bunny")

        if (BunRecruit("Melody")):
            MoveInSmart("melody bunny on")

        if (prime_security != "Ethan"):
            MoveInSmart("ethan bunny")

    leaf @talking2mouth "{gradualsize=5-36}[ellipses]and as a party favor, everybunny can have a fossil!{/gradualsize}"

    narrator "You notice with quiet horror that Leaf is trying to shove pieces of paper bearing the the text \"IOU ONE FOSSIL\" into the hands of the party guests."
    narrator "Thankfully, it seems most of the guests are politely declining, recognizing Leaf's bunny-induced mania for what it is."

    red @surprisedbrow frownmouth "[ellipses]"
    red @sweat talkingmouth "Oh, boy. I should talk with her about this."

    show leaf at getcloser zorder 10
    $ LineUp(exclude=["Leaf"], prefilled=[0.5], inner_band=0.02, considerexcludes=False)

    leaf @happy "Oh, you! Yes, [first_name]! You also get a party favor!"

    red @sadbrow talkingmouth "Hey, I appreciate that, but[ellipses]"

    leaf @winkbrow talkingmouth "No, wait, I know--you don't want to be dependent on your friends."
    leaf surprisedbrow frownmouth @sadbrow talkingmouth "But this isn't that! I promise. It's a gift, and I'm giving it to {i}everyone{/i}. It's not just a {i}you{/i} thing!"

    red @wince talkingmouth "That[ellipses] isn't actually my concern this time. It's more like, uh[ellipses] this party's got a {i}lot{/i} of people. I genuinely don't think you can afford it. Besides, aren't they your parents' fossils?"

    leaf @sadbrow talkingmouth "Well[ellipses] yes. But they were fine with me giving one away--I've done that already. Revived it and everything."

    red @talkingmouth "Sure. But there's a difference between one and--you know, like, forty."

    pause 0.5

    red @happy "I get you're really happy right now. And I'm happy you're happy, too. But don't, you know, overcommit yourself by giving out billions of Pokédollars in precious rocks in a single evening."

    leaf -surprisedbrow @closedbrow talking2mouth "I[ellipses] I[ellipses] yeah. Yeah, that makes sense."

    red @sadbrow talkingmouth "You said you already gave one out, right?"

    leaf @talking2mouth "Yeah. I got it last week--only gave it to Yellow this morning, though."

    red @happy "Oh! {i}That's{/i} what your mystery mission for Yellow was last Thursday?"

    leaf -frownmouth @talkingmouth "Yup."

    red @talkingmouth "Well, I'm sure she {i}really{/i} appreciated it. But maybe hold off on giving {i}everyone{/i} a fossil."
    red @talkingmouth "If you want my recommendation, I think Yellow was a fantastic first choice--and Ethan would probably appreciate one too. Might help[ellipses] you know, smooth things over."

    leaf @embarrassedbrow embarrassedmouth "Mmm[ellipses]"

    leaf @talkingmouth "Okay. Thanks, [first_name]. Um[ellipses] just out of curiosity, though[ellipses] if you {i}were{/i} getting a fossil[ellipses] which one would you want?"

    red @upeyes frownmouth "Hm[ellipses] well, if you had three, I might pick[ellipses]"

    $ fossilchoice = "Helix"

    menu LeafBunnyFossilsMenu:
        "The Helix Fossil":
            $ fossilchoice = "Helix"

            leaf @talkingmouth "Huh. You're kinda similar, you know."

            red @confused "That was cryptic."

            leaf @happy "Yellow got a Helix Fossil, too. Well, an Omanyte, now."

        "The Dome Fossil":
            $ fossilchoice = "Dome"

            leaf @talkingmouth "A very democratic choice."

            red @talking2mouth "I feel like I'm missing something."

            leaf @talkingmouth "Something Ethan said. I think it's a play on the word 'Dome'? Like, Dome-ocratic? And Kabuto is kinda dome-shaped."

        "The Old Amber":
            $ fossilchoice = "Amber"

            leaf @happy "I think you'll have to fight Blue for that one! He's been talking about how he wants an Aerodactyl for a while."

            red @playfulbrow talkingmouth "When has fighting Blue ever been a problem?"

        "The Root Fossil":
            $ fossilchoice = "Root"

            leaf @angrybrow talkingmouth "Copycat."

            red @talkingmouth "What, do you have a Lileep?"

            leaf @talking2mouth "I will, one day."

        "The Claw Fossil":
            $ fossilchoice = "Claw"

            leaf @happy "I think you'll have to fight May for that one!"

            if (not mayhaslarvesta):
                redmind @wince frownmouth "Wouldn't be the first time."
            
            else:
                red @talkingmouth "Anorith's got two claws, doesn't it?"

        "The Skull Fossil":
            $ fossilchoice = "Skull"

            leaf @talkingmouth "Cool! Cranidos is really cute, and Rampardos is crazy-strong."

        "The Armor Fossil":
            $ fossilchoice = "Armor"

            leaf @talkingmouth "Shieldon are really tough and defensive, and I love how Bastiodon looks like a castle."

        "The Cover Fossil":
            $ fossilchoice = "Cover"

            leaf @talkingmouth "Oh, really? Instructor Lenora would love that. She was super-involved in the resurrection of the first Tirtouga. She even has a Carracosta on her main team."

        "The Plume Fossil":
            $ fossilchoice = "Plume"

            leaf @talkingmouth "Archen's adorable, and really strong, too."
            leaf @happy "Archeops only gets better! Did you know that Archeops' Base Stat Total is the same number as its Pokédex number, which is {i}also{/i} the decimal number for feathered prehistoric Pokémon?"

            if (HasEvent("Leaf", "ArchenInfodump")):
                red @happy "Yes, since you just told me."

            else:
                $ AddEvent("Leaf", "ArchenInfodump")
                red @talking2mouth "Crazy coincidence, huh?"

        "The Jaw Fossil":
            $ fossilchoice = "Jaw"

            leaf @angrybrow talkingmouth "Aw, no way! If my parents ever get a Jaw Fossil, that baby Tyrunt is {i}mine!{/i} Tyrantrum is literally my favorite Pokémon!"

            red @confused "Really? I would've thought you'd like something more[ellipses]"
            red @wince talking2mouth "Uh, never mind."

            show leaf surprisedbrow frownmouth with dis

            red @sweat talkingmouth sadbrow "But you aren't taking Dragon classes anymore, remember."

            leaf -surprisedbrow -frownmouth @closedbrow talking2mouth blush "I'll figure something out."

        "The Sail Fossil":
            $ fossilchoice = "Sail"

            leaf @talkingmouth "Oh, that's really great! Amaura are just {i}so{/i} adorable. And they become so beautiful when they evolve, too."
    
    $ formatfossilchoice = ("The " + fossilchoice + " Fossil") if fossilchoice != "Old Amber" else "The Old Amber"

    menu:
        ">Confirm your choice: [fossilchoice]":
            $ AddEvent("Leaf", "FossilChoice", fossilchoice)

        ">Rethink choice.":
            jump LeafBunnyFossilsMenu

    leaf @winkbrow talkingmouth "Alright, noted!"

    pause 1.0

    red @confused "Uh[ellipses] at the risk of sounding presumptuous, is that it?"

    leaf @flirtbrow talkingmouth "Well, yeah. I said this was purely a hypothetical. Did you not believe me?"

    red @closedbrow talkingmouth "Fair enough."

    jump BunnyPartyStart

label BunnyTournament:
    python:
        AddEvent("Game", "Bunny Tournament")
        MoveInSmart("leaf bunny")
        if (BunRecruit("whitney")):
            MoveInSmart("Whitney bunny")
            
        if (HasEvent("May", "BunnyKitchen")):
            MoveInSmart("may sadbrow bunny")

            if (mallow_present):
                MoveInSmart("mallow bunny", maintain=True)

        if (BunRecruit("nessa")):
            MoveInSmart("nessa bunny")
        
        if (HasEvent("Nate", "JoinBunny")):
            MoveInSmart("nate bunny")
        
        if (BunRecruit("rosa")):
            MoveInSmart("rosa bunny")

        if (prime_security != "Ethan"):
            MoveInSmart("ethan bunny")

    leaf @talkingmouth "{gradualsize=5-36}[ellipses]alright, everyone ready?{/gradualsize} Let's get this tournament underway!"

    $ GroupExpression("surprisedbrow frownmouth")

    red @surprised "Wait, stop!"

    pause 1.0

    $ HighlightCharacter("Leaf", "bunny", reset=True)
    $ LineUp(exclude=["Leaf"], prefilled=[0.5], inner_band=0.02, considerexcludes=False)

    leaf @neutralbrow talking2mouth "[first_name]? Is something wrong?"

    red @sadbrow talkingmouth "Yes, something is {i}very{/i} wrong! We can't battle in here! This classroom is way too small, and we'd be battling on--{i}in{/i}--school property, anyway!"

    leaf -surprisedbrow @talkingmouth "Oh, that's what you're worried about? Don't worry, we've got a plan. It's only going to be a 1v1 tournament, where each of us only use one Pokémon, so things won't be too crazy."

    $ GroupExpression("neutralbrow neutralmouth", exclude=["leaf"])

    red @flirtbrow talking2mouth "A Steelix versus a Gyarados is plenty crazy, even if there's only two Pokémon on the field."

    leaf @winkbrow talkingmouth "Thought of that, too. We're going to be using bunny Pokémon only."

    red @upeyes talking2mouth "Okay, but even a Buneary using Mega Punch--"

    leaf @flirtbrow talkingmouth "And we're going to be strapping pillows to each of our Pokémon so that their moves are a lot softer, and we don't cause any damage to the classroom."

    pause 1.0

    redmind @surprisedbrow frownmouth lightblush "That will be[ellipses] adorable."

    pause 1.0

    red @closedbrow talking2mouth "Sounds like you really thought this through."

    leaf @talkingmouth "We did. Only thing we don't have something for is[ellipses] well, yeah, battling in a classroom isn't exactly allowed."
    leaf @closedbrow talkingmouth "But I'm pretty sure throwing a sexy bunny party isn't exactly allowed, either."

    leaf @happy "C'mon, it'll be fine. I want to show how thankful I am to you, and everyone here, and this was the only thing I could whip up at such short notice."

    if (HasEvent("Game", "LeafBunnyFossils")):
        leaf @closedbrow talking2mouth "{size=30}Besides the 'giving everyone a fossil' plan, which you didn't seem to love.{/size}"

    leaf @happy "Alright, everyone! This'll be a series of 1v1 battles, using the same Pokémon each time. You can heal in-between! I've got enough potions for all of you."

    redmind @smirkmouth unamusedbrow "Yeah, she came prepared[ellipses]"

    show screen currentdate

    python:    
        '''
        if (HasEvent("May", "BunnyKitchen")):
            $ HighlightCharacter("may", "bunny", True)
            may @talking2mouth "[ellipses]How else would we heal?"
        elif (prime_security != "Ethan"):
            $ HighlightCharacter("ethan", "bunny", True)
            ethan @confused "[ellipses]How else would we heal?"
        elif (BunRecruit("Nessa")):
            $ HighlightCharacter("nessa", "bunny", True)
            nessa @confused "[ellipses]How else would we heal?"
        elif (BunRecruit("Rosa")):
            $ HighlightCharacter("rosa", "bunny", True)
            rosa @confused "[ellipses]How else would we heal?"

        if (BunRecruit("Whitney")):
            $ HighlightCharacter("whitney", "bunny", True)
            whitney @closedbrow talking2mouth "Well, you could run out to the Student Center and try to use the healing machine there."
            whitney @happybrow talkingmouth "Of course, most people wouldn't have any idea how to use it. It's a {i}lot{/i} more complicated than just pressing a button, like most people think."

            pause 1.0

            narrator "For some reason, you can imagine Yellow nodding vigorously."
        '''

    if (HasEvent("May", "BunnyKitchen") and mallow_present):
        $ HighlightCharacter("mallow", "bunny", True)
        mallow @sadbrow talkingmouth "Hey, everyone. Maractus is a rabbit, right? I mean, it's got the ears[ellipses]"

        if (HasEvent("Nate", "JoinBunny")):
            $ HighlightCharacter("nate", "bunny", True)
            nate @talkingmouth "If Maractus is a rabbit, then Trubbish is, too."
    elif (HasEvent("Nate", "JoinBunny")):
        nate @talkingmouth sadbrow "So, hey, we're all cool just pretending Trubbish is a rabbit, right? Like, with the little ears and all? Right, guys?"

        pause 1.0

        nate @surprised "Right?"

    $ LineUp()

    narrator "Leaf has invited you to join a tournament for leporine Pokémon. In this tournament, the effects of damaging moves will be {i}significantly{/i} reduced. Would you like to accept?"

    menu AgreeBunnyTournament:
        "Alright, let's do this.":

            narrator "Please pick a leporine Pokémon."

            python:
                hidebattleui = True
                mustswitch = True
                renpy.transition(dissolve)
                newindex = renpy.call_screen("switch", MakeRed())
                hidebattleui = False
                mustswitch = False
                rabbitpkmn = playerparty[newindex]

            if (rabbitpkmn.Id not in rabbit_pokemon_ids and rabbitpkmn != pikachuobj):
                narrator "Apologies, that Pokémon isn't sufficiently rabbitlike for the purposes of this tournament."

                jump rabbitlikepokemonreminder

            narrator "You have chosen to battle alongside [rabbitpkmn.GetNickname()]."

        "Wait, what exactly are 'leporine' Pokémon?":
            label rabbitlikepokemonreminder:
            narrator "The following Pokémon are considered sufficiently rabbitlike for this tournament."

            python:
                rabbitstring = []
                for rabbit in rabbit_pokemon_ids:
                    rabbitstring.append(pokedexlookup(rabbit, DexMacros.Forme))
                
                # Display rabbit names in groups of up to 15 per textbox
                for i in range(0, len(rabbitstring), 15):
                    group = rabbitstring[i:i+15]
                    if len(group) == 1:
                        text = group[0] + "."
                    elif len(group) == 2:
                        text = group[0] + " and " + group[1] + "."
                    else:
                        text = ", ".join(group[:-1]) + ", and " + group[-1] + "."
                    renpy.say(None, text)

            menu:
                "There's a lot of Pokémon there that blatantly aren't rabbits.":
                    narrator "'Rabbitlike.' Leporine ears is pretty much the only criteria that matters."

                    menu:
                        "It just feels like a really arbitrary condition, is all.":
                            narrator "Look, I either use a {i}really{/i} loose definition of 'rabbit' for today's events or force you to use Lopunny."

                            if (not HasPokemon('lopunnyobj')):
                                narrator "[ellipses]Which will be difficult for you, since you didn't catch it."

                            menu:
                                "Well, maybe I {i}do{/i} want to use Lopunny! Maybe I want to struggle!":
                                    narrator "If you want to struggle, play {i}Reborn{/i}. Now can I {i}move on{/i}? Thanks."
                                    
                                    $ AddEvent("Game", "BunnyArgument")

                                "Understood.":
                                    pass

                        "Understood.":
                            pass

                "Understood.":
                    pass
                    
            jump AgreeBunnyTournament

        "No thanks.":
            jump BunnyPartyStart

    python:
        tournamentopponents = {
            "May": "Scorbunny", #coded in
            "Mallow": "Maractus",# coded in
            "Whitney": "Lopunny",# coded in
            "Rosa": "Pikachu",# coded in
            "Nessa": "Azumarill",#coded in
            "Ethan": "Pichu",# coded in
            "Nate": "Trubbish",# coded in
            "Leaf": "Diggersby"# coded in
        }
        unbattledbunnies = ["Leaf"]
        if (BunRecruit("whitney")):
            unbattledbunnies.append("Whitney")
        if (HasEvent("May", "BunnyKitchen")):
            unbattledbunnies.append("May")
            if (mallow_present):
                unbattledbunnies.append("Mallow")
        if (BunRecruit("nessa")):
            unbattledbunnies.append("Nessa")
        if (HasEvent("Nate", "JoinBunny")):
            unbattledbunnies.append("Nate")
        if (BunRecruit("rosa")):
            unbattledbunnies.append("Rosa")
        if (prime_security != "Ethan"):
            unbattledbunnies.append("Ethan")
            
        trainerred = Trainer("red", TrainerType.Player, [rabbitpkmn])
        wonbunnies = []
        lostbunnies = []
        tourneymatch = 0

    narrator "Everyone draws random lots to see who battles first[ellipses]"

    label bunnytournamentstart:
    python:
        selectedtrainer = RandomChoice(unbattledbunnies)
        unbattledbunnies.remove(selectedtrainer)
        tourneymatch += 1

    narrator "You drew [selectedtrainer]."

    if (selectedtrainer == "May"):
        $ HighlightCharacter("May", extras="bunny", reset=True)
        may @happy "Thanks for setting this party up, and making sure I got to actually enjoy it!"
        may angrybrow talkingmouth "To show you how grateful I am, I'm going to kick you all over this classroom with my little Scorbunny!"

        red @confused "Well, see if I ever do something nice for you again."

    elif (selectedtrainer == "Mallow"):
        $ HighlightCharacter("Mallow", extras="bunny", reset=True)
        if (rabbitpkmn == pikachuobj):
            mallow @surprisedbrow frownmouth "[ellipses]"

            red @confused "What's up?"

            mallow @talking2mouth "Well[ellipses] I, an Alolan, am about to beat up a Unovan Pikachu."
            mallow @sadbrow talkingmouth "The optics here aren't great, are they?"

            red @winkbrow talkingmouth "That's just assuming you win. I think [pika_name]'s got another opinion."

            $ PlaySound("Pokemon/pikachu_angry3.ogg")
            libpikachu glowing angry sparks "Pika!"

        else:
            mallow happy "I probably can't defeat a member of the Battle Team--but I'm more than happy to go down swinging, proving my Alolan pride! {i}Chee-hoo!{/i}"

            pause 1.0

            $ PlaySound("Pokemon/pikachu_angry2.ogg")
            libpikachu angryeyes anger poutmouth sparks "Pi!"

            redmind @upeyes frownmouth "Sounds like [pika_name] is pouting that he can't fight Mallow[ellipses] can grudges be carried through a bloodline?"

    elif (selectedtrainer == "Whitney"):
        $ HighlightCharacter("whitney", extras="bunny", reset=True)
        whitney surprisedbrow frownmouth "[ellipses]"

        red @talkingmouth "What's up? Something on my face?"

        whitney @talking2mouth "I just realized I'm going to be battling you without Milty. I don't think I've[ellipses] {i}ever{/i} battled without her."
        whitney @sad2eyes sadeyebrows talking2mouth "{size=30}This feels kinda like cheating on her[ellipses]{/size}"

    elif (selectedtrainer == "Rosa"):
        $ HighlightCharacter("rosa", extras="bunny", reset=True)
        rosa @talkingmouth "Looks like the stage is ours! Ready for some action?"

        red @happy "As long as you bring the lights and camera!"

    elif (selectedtrainer == "Nessa"):
        $ HighlightCharacter("nessa", extras="bunny", reset=True)
        nessa @talkingmouth "No offense, but I'm going to win this one."

        red @talkingmouth "You sound pretty confident?"

        nessa @talking2mouth "As long as we're pulling our punches, you're not getting through my Azumarill."

        if (rabbitpkmn.GetNickname() != pokedexlookup(rabbitpkmn.Id, DexMacros.Name)):
            red @talkingmouth "I could say the same thing about you getting through [rabbitpkmn.GetNickname()]."
        else:
            red @talkingmouth "I could say the same thing about you getting through my [rabbitpkmn.GetNickname()]."

        nessa @talkingmouth "You'll see what I mean. Let's roll."

    elif (selectedtrainer == "Ethan"):
        $ HighlightCharacter("ethan", extras="bunny", reset=True)
        ethan @talking2mouth "We have to stop meeting like this. People are going to talk."

        red @talkingmouth "You make a very cute bunny."

        ethan @happybrow talkingmouth "Same, bro. Now let's tussle."

    elif (selectedtrainer == "Nate"):
        $ HighlightCharacter("nate", extras="bunny", reset=True)
        nate @thinking "{size=30}Hare[ellipses]? No, that's not it. No-bunny? Kinda derivative. Hip[ellipses] hop? Hoppy? Hoppy battles?{/size}"

        red @unamusedbrow unamusedmouth "[ellipses]"
        red @talking2mouth "Skip the pre-battle bunny-themed pun-liner, and let's battle."

        nate @talkingmouth sadbrow "Aw, you know me."

    elif (selectedtrainer == "Leaf"):
        show leaf angry:
            ease 0.7 xpos 0.5 ypos 2.0 zoom 3.0 alpha 0.0

        leaf "{size=40}BUNNY BATTLE!{/size}"

        redmind @surprisedbrow frownmouth "WHOAHSHI--"

    hide semiblank2
    show blank2:
        alpha 0.3

    call Battle([trainerred, Trainer(selectedtrainer, TrainerType.Enemy, [GetTrainerTeam(selectedtrainer, tournamentopponents[selectedtrainer])])], currentWeather=("Bunny Battle!", 999), specialmusic=(("audio/music/swordshieldgym-intro.ogg", "audio/music/swordshieldgym-loop.ogg") if tourneymatch == 1 else "Nothing"), stopmusic=False, customoutfits=["bunny", "bunny"]) from _call_Battle_193
    $ result = _return

    if (result):
        $ wonbunnies.append(selectedtrainer)
    else:
        $ lostbunnies.append(selectedtrainer)

    if (selectedtrainer == "Leaf"):
        $ RecordBattle("Leaf3")

    if (len(unbattledbunnies) > 0):
        if (result):
            narrator "Nicely done! Time to draw for your next opponent[ellipses]"
        else:
            narrator "You gave it a fair shot, so don't feel bad! Time to draw for your next opponent[ellipses]"
        jump bunnytournamentstart

    if (not ('bunnypartybgm' in globals() and bunnypartybgm != None and len(bunnypartybgm))):
        $ bunnypartybgm = ("audio/music/viridianforest_start.ogg", "audio/music/viridianforest_loop.ogg")
    
    stop music fadeout 1.5
    queue music bunnypartybgm[0] noloop
    queue music bunnypartybgm[1]

    if (len(lostbunnies) == 0):
        narrator "[ellipses]You were undefeated? Incredible! Those were some seriously tough rabbits you had to battle through."

        menu:
            "A solid half of those weren't rabbits.":
                pass

            "They weren't, really.":
                pass

            "Th-thanks[ellipses]?":
                pass

    if (len(wonbunnies) > 2):
        narrator "For winning at least three battles in the bunny battle bonanza, you've earned[ellipses] nothing, actually."

        redmind @sideeyes angryeyebrows frownmouth "What? Pfft."

        narrator "However, it occurs to you that the defensive strategies (strapping fluffy pillows to the Pokémon) utilized in this battle bonanza might be able to be used outside of battle[ellipses] at least by Pokémon that can make their own fluff."

        pause 1.0

        red @thonk "[ellipses]It does?"

        narrator "More or less."

        red @closedbrow talking2mouth "Hey, was anyone recording these fights on video?"

        $ MoveInLeft("leaf bunny")

        leaf @talkingmouth "Sure! Want me to send you a TM?"

        red @talkingmouth "Please."

        if (BunRecruit("Rosa")):
            red @talking2mouth "Oh, wait. Rosa isn't in any of these shots, is she? Because her privacy--"

            leaf @talking2mouth flirtbrow "[first_name], you don't need to tell me to respect Rosa's privacy. I'd literally take her secrets to the grave if she asked me to."

            red @sadbrow talkingmouth "So you're not a crazy stalker uberfan?"

            leaf @closedbrow talkingmouth "I'm definitely {i}two{/i} of those."

        python:
            GetItem(Item.TechnicalMachineCase, text="You gained the TM - Cotton Guard!")
            if Item.TechnicalMachineCase in inventorymetadata:
                inventorymetadata[Item.TechnicalMachineCase].append("Cotton Guard")
            else:
                inventorymetadata[Item.TechnicalMachineCase] = ["Cotton Guard"]

    jump BunnyPartyStart

label AfterParty:
    #Klara crashes the party, but security warns you
    #Iono gives you advance warning, and you can have her turn Klara around
    #Nate gives you advance warning, and you can have him turn Klara around
    #Sonia does not give you advance warning
    #Ethan does not give you advance warning

    if (prime_security == "Iono"):
        show phone_B
        show iono happy:
            xpos 0.525 zoom 0.9 ypos 0.9
        show phone_A 
        with fadeinbottom

        iono @happy "Hey! Security update."

        red @sigh "What is it?"

        iono @thinking "Klara's coming."

        red @talking2mouth "Huh. Didn't see that coming."

        iono @winkbrow talkingmouth "And that's why I told ya!"
        iono @closedbrow talking2mouth "I don't think she's here to crash the party, if it matters. She's got casual clothes on, and she's not holding a spare outfit."

        red @talking2mouth "Sure. Thanks for letting me know. Is she definitely walking to the party, or just this way?"

        iono @winkbrow "My cams are a few decades away from being able to read intent. I can give you her vector and status, but you might just have to ask her if she's coming here yourself."

        red @talking2mouth "Alright."
                
        iono @happy "Good luck!"

        hide phone_B
        hide iono
        hide phone_A
        with fadeoutbottom

        $ BecomeContacted("Iono")

    elif (prime_security == "Nate"):
        if (BunRecruit("Game")):
            if (not HasEvent("Nate", "JoinBunny")):
                show phone_B
                show nate suit frownmouth:
                    xpos 0.5
                show phone_A 
                with fadeinbottom
            else:
                show nate bunny frownmouth with dis
        else:
            show nate suit frownmouth with dis

        nate @talking2mouth "Hey. Status update:{w=0.5} K's en route."

        red @confused "Klara?"

        nate @talking2mouth "No suit. Might be a coincidence, and she's just heading in our general direction."
        nate @sadbrow talkingmouth "I don't believe that, though."

        red @confused "Yeah, me neither, really. I'll go see what's up."

        nate @talking2mouth sad2eyes shadow angryeyebrows "{size=30}Bring a raincoat.{/size}"

        if (not HasEvent("Nate", "JoinBunny")):
            hide phone_B
            hide nate
            hide phone_A
            with fadeoutbottom

            pause 0.5

            $ BecomeContacted("Nate")
        else:
            hide nate with dis

    elif (prime_security == "Sonia"):
        if (BunRecruit("Game")):
            show phone_B
            show sonia surprisedbrow frownmouth:
                xpos 0.52 zoom 0.95
            show phone_A 
            with fadeinbottom

            sonia @talking2mouth "Er, hello. I'm here with Klara, and--"

            red @surprised "Klara? Why?"

            sonia @angrybrow talking2mouth "It's rather rude to interrupt. I was just about to say that {i}I{/i} asked her that, and she said she wants to talk to you."

            red @sigh "Sorry. I'll be out in a second."

            hide phone_B
            hide sonia
            hide phone_A
            with fadeoutbottom

            $ BecomeContacted("Sonia")

    else:#ethan
        if (BunRecruit("Game")):
            show ethan bunny angryeyebrows frownmouth with vpunch

            ethan @talking2mouth "Hey, man. Klara's standing outside."

            red @surprised "Klara? Why?"

            ethan @talking2mouth "I don't know, and I'm not going to ask her."

            red @sigh "Alright. I'll see what's going on."

            pause 0.5

            ethan @sad2eyes angryeyebrows talking2mouth "Don't be nice to her, man."

            red @sadbrow talkingmouth "When has {i}not{/i} being nice ever made anyone feel better?"

            ethan @talking2mouth unamusedbrow "I have a list."

            red @sadbrow talkingmouth "I don't."

            ethan @closedbrow talking2mouth "Yeah, well, lucky you."

            hide ethan with dis

    if (BunRecruit("Game")):
        scene blank2 with splitfade

        scene academyhall with splitfade

    stop music fadeout 1.5
    queue music "audio/music/everyonesfavoritegirl_start.ogg" noloop
    queue music "audio/music/everyonesfavoritegirl_loop.ogg"

    $ MoveInSmart("Klara casual")

    if (HasEvent("Klara", "BrokeBond")):
        if (not BunRecruit("Game")):
            klara @talking2mouth "Oh, hello, [first_name]. Fancy seeing you here."

            red @talking2mouth "You weren't invited to the party. Go away."

            klara @happybrow madmouth "Oh, yes, the 'party.' Of course, the {i}very real{/i} party you and your friends are definitely throwing."

        else:
            klara casual @happy "Oh, hello, [first_name]. Fancy seeing y--"
            klara @surprisedbrow frownmouth "[ellipses]"
            klara surprisedbrow @talking2mouth "What are you wearing."

            red @sigh "I'm really getting tired of hearing that[ellipses]"
            red @talking2mouth "I'm wearing a bunny suit, Klara."

            pause 1.0

            klara @talking2mouth "Why."

            red @talking2mouth "Because Dorm 25 is throwing a bunny suit party. You are not invited. Please go away."

            klara @happybrow madmouth "Oh, of course! The 'party.' Of course, the {i}very real{/i} party you and your friends are definitely throwing."

        klara @ojoubrow ojoumouth "Ah[ellipses]{w=0.5} ahah!{w=0.5} {size=40}Ahahahaha!{/size}"
        klara @angrybrow talkingmouth "You're so committed to the act, I {i}almost{/i} believed it!"

        red @upeyes frownmouth "[ellipses]"
        red @angrybrow talkingmouth "Klara, remember when I literally couldn't lie? Remember how that was a huge thing that kinda ruined my life for a week?"

        klara @angrybrow talking2mouth "{i}Everyone{/i} can lie. Everyone {i}does{/i} lie."
        klara @talking2mouth "I know exactly what this is. This is another fake bunny party. You didn't invite me because that would be too obvious. So you just let rumors get to me. And you expected me to crash the party, in a bunny suit, so you could humiliate me."
        klara @angrybrow talking2mouth "God, you're so bad at manipulating people, it's painful. You're just doing what I did, but worse, like there was {i}any{/i} way I wouldn't see through it."

        pause 0.5

        red @angrybrow talking2mouth "Klara. {i}None{/i} of that is true. I didn't want there to be any rumors about this party--we're trying to keep it secret. I didn't want you to hear about it, because all my dormmates hate you right now, and if you showed up, that would ruin {i}our{/i} party."
        red @angrybrow talking2mouth "I didn't want {i}anyone{/i} to crash the party, because we're taking security really seriously. And I didn't want anyone to be hurt or humiliated during the party--I wasn't thinking about {i}you{/i} at all. I just wanted my friend to feel better."

        pause 0.5 

        red @talking2mouth "No-one's manipulating anyone here. We're genuinely just being honest--but it wouldn't surprise me if you just couldn't understand that."

        klara @angrybrow talking2mouth "Oh, shut {i}up.{/i} At least admit that your plan failed. Look, I'll open the door now and prove it."

        red @angrybrow talking2mouth "You shouldn't, but if you do, you'll deserve what happens."

        $ MoveOutSmart("klara")

        pause 1.0

        $ PlaySound("GenericDoorOpen.ogg")

        pause 2.0

        redmind @sadbrow frownmouth "I told you."

        klara casual @frightenedbrow talking2mouth "Wha[ellipses] what[ellipses]?"

        if (HasEvent("Melody", "BunnyHandled") and not (HasEvent("Melody", "RejectBunny") or HasEvent("Melody", "RejectBunny2"))):
            melody bunny on @talking2mouth "Hey. There's a dress code?"
        elif (BunRecruit("Nessa")):
            nessa bunny @talking2mouth "There's a dress code."

        if (BunRecruit("Whitney")):
            whitney bunny @talking2mouth "Uh, pinky? Love the hair, but you're not supposed to be here."
        
        if (BunRecruit("Rosa")):
            rosa bunny @talking2mouth "Um[ellipses] sorry, I really don't want to sound pretentious, but this is sort of an invite-only event."

        leaf bunny @surprisedbrow frownmouth "[ellipses]"
        leaf @closedbrow talkingmouth "Huh."

        ethan bunny @talking2mouth "Hey, Klarice, right? Pretty sure you weren't invited."

        $ PlaySound("GenericDoorClose.ogg")

        $ hideside = True

        pause 0.5

        ethan "{size=30}Also, your album lacked any distinct musical voice, and was distractingly derivative of Piers' {i}Darker Pulse{/i}.{/size}"

        pause 0.5

        $ hideside = False

        pause 0.5

        show klara casual sadbrow frownmouth with dis

        $ MoveInRight("Klara casual")

        pause 0.5

        klara casual @talking2mouth "You were telling the truth."

        pause 1.0

        klara @closedbrow wrathmouth "{gradualsize=36-40}You TRICKED ME!{/gradualsize}"

        red @angrybrow talking2mouth "You tricked yourself. And you got off easy--no-one sprayed you, no-one took any pictures. You're just going to have that memory of walking into a private party without an invite, which is a lot less than Leaf had to carry."
        
        klara @restrainedbrow talking2mouth "You think you're better than me, don't you? You think that because you're good at battling, and rich, and make friends without trying, that I should be ashamed I {i}have to{/i} try."

        red @sadbrow talking2mouth "I don't think that at all, Klara. And I'm not rich. And I don't make friends without trying--I try really hard, actually."
        red @upeyes sadeyebrows talking2mouth "{size=30}[ellipses]I am good at battling, though.{/size}"

        klara @talking2mouth "Battle me. Battle me, now! I'm not like that crybaby Leaf--if you mess with me, I'll mess you back, way, {i}way{/i} harder."

        red @angrybrow talking2mouth "Fine. We'll make this quick."

        show screen songsplash("Your Favorite Girl", "Vetrom")

        python:
            trainer1 = MakeRed()
            trainer2 = MakeTrainer("Klara")

        call Battle([trainer1, trainer2], specialmusic="audio/music/yourfavoritegirl.ogg", customexpressions=["red angrybrow frownmouth", "red angrybrow frownmouth", "klara angrybrow frownmouth", "klara madbrow madmouth"], customoutfits=[("bunny" if BunRecruit("Game") else ""), "casual"]) from _call_Battle_194
        $ RecordBattle("Klara2")

        show klara casual angrybrow frownmouth with dis

        if (WonBattle("Klara2")):
            narrator "Victory feels hollow."
            narrator "But it is still a victory."

        klara @talking2mouth "Do you want to know {i}why{/i} I hate Leaf? And why I hate you?"

        red @talking2mouth "Yes."

        klara @talking2mouth "Well, no matter how hard you try, you'll never get it."
        klara @angrybrow talking2mouth "You hear me?"
        klara @talking2mouth "[ellipses]You'll {i}never{/i} get your 'why!' {i}{color=#f00}Never!{/color}{/i}"

        hide klara with dis

        pause 1.5

        $ PlaySound("GenericDoorOpen.ogg")
        $ MoveInRight("leaf flirtbrow")

        pause 1.0

        leaf @talkingmouth "Hey."

        pause 0.5

        red @sad2eyes talkingmouth "Hi."

        pause 0.5

        leaf @talkingmouth "You feeling alright?"

        red @talking2mouth "[ellipses]I feel like a door closed."

        $ PlaySound("GenericDoorClosed.ogg")

        leaf @talkingmouth "Well, you know what they say about doors."

        red @talking2mouth "When one closes, another opens?"

        leaf @talkingmouth "More or less."
        
        show leaf at getcloser

        leaf @talkingmouth "Just because you {i}can{/i} leave a door open doesn't mean you should. Sometimes[ellipses] it's better for everyone to close the door, and leave it closed."

        red frownmouth "[ellipses]"
        red @talking2mouth "I'll always be curious, though."

        leaf @sadbrow "[ellipses]"
        leaf @talkingmouth "Yeah. So will I."

    else:
        if (not BunRecruit("Game")):
            klara @talking2mouth "Oh, hello, [first_name]. Fancy seeing you here."

            if (GetContestWinner("Millennium Drop Water Festival Contest Tryouts").IsProtag() and HasEvent("Klara", "AcceptPartner")):
                red @talkingmouth "Hey, Klara. Sorry, is this about our routine? Now's not really a good time."

                klara @happy "Oh, really? Why? What's so important you can't practice for the most important contest either of us are ever going to participate in?"

            else:
                klara @talkingmouth "What are you doing?"

            red @talkingmouth "I'm acting as bouncer for a party Dorm 25 is throwing."

        else:
            klara @happy "Oh, hello, [first_name]. Fancy seeing y--"

            klara @surprisedbrow frownmouth "[ellipses]"

            klara surprisedbrow @talking2mouth "What are you wearing."

            red @sigh "I'm really getting tired of hearing that[ellipses]"
            red @talking2mouth "I'm wearing a bunny suit, Klara."

            pause 1.0

            klara @talking2mouth "Why."

            red @confused "Because Dorm 25 is throwing a bunny suit party? I mean, after you had to cancel yours, we thought we should hold one instead."
        
        red @sadbrow talkingmouth "Sorry for not inviting you, Klara. I felt pretty bad about it, actually--but Leaf's still kinda upset, so I thought it might be best if you two gave each other a bit more space."
        red @talking2mouth "For a bit longer, anyway."

        pause 2.0

        red @confused "Klara? You with us?"

        pause 1.0

        klara @ojoubrow ojoumouth "Ah[ellipses]{w=0.5} ahah!{w=0.5} {size=40}Ahahahaha!{/size}"
        klara -surprisedbrow  @angrybrow talkingmouth "You're so committed to the act, I {i}almost{/i} believed it!"

        red @upeyes frownmouth "[ellipses]"
        red @sadbrow talkingmouth "Klara, remember when I literally couldn't lie? Remember how that was a huge thing that kinda ruined my life for a week?"

        klara @angrybrow talking2mouth "{i}Everyone{/i} can lie. Everyone {i}does{/i} lie."
        klara @talking2mouth "I know exactly what this is. This is another fake bunny party. You didn't invite me because that would be too obvious."
        klara @closedbrow talkingmouth "So you just let rumors get to me. And you expected me to crash the party, in a bunny suit, so you could humiliate me."
        klara @angrybrow talking2mouth "God, you're so bad at manipulating people, it's painful. You're just doing what I did, but worse, like there was {i}any{/i} way I wouldn't see through it."

        pause 0.5

        red @sadbrow talking2mouth "Klara. {i}None{/i} of that is true. I didn't want there to be any rumors about this party--we're trying to keep it secret. I didn't want you to hear about it, because I didn't want you to feel left out."
        red @sadbrow talking2mouth "I didn't want {i}anyone{/i} to crash the party, because we're taking security really seriously. And I didn't want anyone to be hurt or humiliated during the party. I just wanted my friend to feel better."

        pause 0.5 

        red @talking2mouth "No-one's manipulating anyone here. We're genuinely just being honest--like you were, right?"

        klara frownmouth @angrybrow talking2mouth "Are you--are you {i}daft?!{/i} I literally just told you I was lying! I was manipulating Leaf, and you, and everyone else who's stupid enough to fall for it."

        red @upeyes frownmouth "[ellipses]"

        show klara surprisedbrow with dis

        red @talking2mouth "I guess I can see why you think you're doing that. But what if I choose to believe you?"

        klara angrybrow @angry "Why would you do that?! I.{w=0.5} WAS.{w=0.5} LYING!"

        red @talking2mouth "I think that comes down to a matter of opinion."

        klara "[ellipses]"
        klara @closedbrow talking2mouth "No. No, no, no. I can't believe this. I {i}refuse{/i} to believe this."
        klara @talking2mouth "You can't be this[ellipses] {i}this{/i}[ellipses] innocent. This is all a trick."

        red @talkingmouth "It's not a trick. And if you can refuse to believe me, I can refuse to doubt you."

        klara @angrybrow talking2mouth "So you're telling me that--{w=0.5}that if I go into that room behind you right now--there's going to be a ton of people in bunny suits?"

        red @talking2mouth upeyes confusedeyebrows "Well, not a ton. A couple handfuls, I think. I've got the exact numbers in this notebook--"

        klara @wrathmouth "Shut up. Shut {i}up!{/i} This isn't real--you aren't real. This whole {i}thing{/i} you're doing is fake. You've realized I'm onto your trick, so you're trying to psych me out! I'm {i}not{/i} falling for it."

        red @sadbrow talking2mouth "You are."

        klara @wrathmouth "{size=40}SHUT UP!{/size}"

        stop music fadeout 5.0

        $ MoveOutSmart("klara")

        pause 1.0

        $ PlaySound("GenericDoorOpen.ogg")

        pause 2.0

        redmind @sadbrow frownmouth "I told you."

        klara casual @frightenedbrow talking2mouth "Wha[ellipses] what[ellipses]?"

        if (HasEvent("Melody", "BunnyHandled") and not (HasEvent("Melody", "RejectBunny") or HasEvent("Melody", "RejectBunny2"))):
            melody bunny on @talking2mouth "Hey. There's a dress code?"
        elif (BunRecruit("Nessa")):
            nessa bunny @talking2mouth "There's a dress code."

        if (BunRecruit("Whitney")):
            whitney bunny @talking2mouth "Uh, pinky? Love the hair, but you're not supposed to be here."
        
        if (BunRecruit("Rosa")):
            rosa bunny @talking2mouth "Um[ellipses] sorry, I really don't want to sound pretentious, but this is sort of an invite-only event."

        leaf bunny @surprisedbrow frownmouth "[ellipses]"
        leaf @closedbrow talkingmouth "Huh."

        ethan bunny @talking2mouth "Hey, Klarice, right? Pretty sure you weren't invited."

        $ PlaySound("GenericDoorClose.ogg")

        $ hideside = True

        pause 0.5

        ethan "{size=30}Also, your album lacked any distinct musical voice, and was distractingly derivative of Piers' {i}Darker Pulse{/i}.{/size}"

        pause 0.5

        $ hideside = False

        pause 0.5

        show klara sadbrow frownmouth with dis

        $ MoveInRight("Klara casual")

        pause 0.5

        klara @talking2mouth "You were telling the truth."

        pause 1.0

        queue music "audio/music/mansion_start.ogg" noloop
        queue music "audio/music/mansion_loop.ogg" 

        klara @closedbrow wrathmouth "{gradualsize=36-40}I don't GET IT!{/gradualsize}"
        klara @frightenedbrow wrathmouth "You were actually telling the truth this whole time?! {i}WHY?!{/i} What's in it for you?!"

        pause 0.5 

        red @sadbrow talkingmouth "A clear conscience."

        pause 0.5

        klara @restrainedbrow talking2mouth "You think you're better than me, don't you? You think that because you're good at battling, and rich, and make friends without trying, that I should be ashamed I {i}have to{/i} try."

        red @sadbrow talking2mouth "I don't think that at all, Klara. And I'm not rich. And I don't make friends without trying--I try really hard, actually."
        red @upeyes sadeyebrows talkingmouth "{size=30}[ellipses]I am good at battling, though.{/size}"

        $ PlaySound("GenericDoorOpen.ogg")
        $ MoveInRight("leaf flirtbrow frownmouth")

        pause 2.0

        leaf @talking2mouth "Hi, Klara. What the fuck?"

        klara @talking2mouth "What do {i}you{/i} want?"

        leaf @talking2mouth "I mean, I just said 'what the fuck,' I feel like that kinda encapsulates everything I'm looking for."
        leaf @talking2mouth closedbrow "If you need more direction, I guess we could say 'why the fuck?'"

        klara @angrybrow talking2mouth "You--{i}you{/i} caused this!"

        leaf @surprisedbrow talking2mouth "I'm willing to entertain the possibility, but I have no idea what 'this' is, so[ellipses]"

        klara @talking2mouth "It's all {i}your{/i} fault!"

        scene blank

        scene garden:
            zoom 0.625
        show clouds behind garden
        show flashback 
        hide screen currentdate
        with Dissolve(2.0)

        pause 0.5

        show whitney behind flashback with dis:
            xpos 0.33

        show face behind flashback with dis:
            xpos 0.66

        whitney @talking2mouth "I don't think there actually {i}is{/i} an Eevee here."

        face @talking2mouth "What a peculiar thing to lie about. But then, this school's rather full of peculiar types, isn't it?"
        face @closedbrow talking2mouth "I recently encountered an incoming student who was at the {i}bottom{/i} of his class at his pass-fail high school."

        whitney @happy "No way! How'd he get in?"

        face @talking2mouth "I still wonder that, myself. I'm assuming some form of nepotism. I very much doubt he can afford to pay for Kobukan, either."

        whitney @talking2mouth "Ah, good ol' nepo-babies. At least they'll fill out that bottom twenty percent for us, right? 'Specially if they can't pay."

        face @talking2mouth "Most assuredly."

        pause 1.0

        whitney @talking2mouth "Hey, we're giving up. What about you, Pinky? Want to come with us?"

        klara @happybrow sweat talkingmouth "What? No! This is a {i}shiny Eevee{/i}. Do you know how much those are worth?"

        whitney frownmouth @confused "Wait, what do you mean, 'worth'? If you found it, you wouldn't sell it, would you? 'Cause, that's, like, a bit illegal without proper licensing."

        klara @happy "Hah, what? Sell it? Noooo. Just[ellipses] you know, there are lots of trainers who would love the chance to adopt a shiny Eevee, right? And if I started talking to them, maybe we could spend some time together and[ellipses]"
        klara @winkbrow talkingmouth "I mean, that would make things easier, you know what I mean?"

        whitney "[ellipses]"
        whitney @talking2mouth "'Kay. Well, like I said, we're going back to the school. We don't want to miss the assembly."

        klara @happy "You go on ahead! I'll find the Eevee."

        pause 0.5

        show whitney poutmouth sad2eyes
        show face poutsadmouth sadeyes sadeyebrows
        with dis

        pause 1.5

        hide whitney
        hide face
        with dis

        klara @angrybrow anger talking2mouth "I won't be filling the bottom twenty for {i}anyone{/i}. I'll figure out how to pay, even if I have to spend all night looking for that Eevee. That girl--she {i}can't{/i} have been lying."
        klara @sadbrow talking2mouth "There'd be no reason to. There was {i}no reason{/i} to. Right?"

        scene blank with dis

        pause 1.0

        scene garden night
        show rowan at night
        show flashback
        with Dissolve(2.0)

        rowan @talking2mouth "Klara Kray. Looking at this roster sheet, you are meant to be one of my students tomorrow morning."
        rowan @talking2mouth "Allow me to introduce myself by telling you I am {i}very{/i} disappointed."

        klara night @frightenedbrow talking2mouth "Wait, wait! Just give me a few more hours--"

        rowan @talking2mouth angrybrow "I will do no such thing, Klara! The bare minimum this school asks of you on your first day is to attend morning assembly!"
        rowan @closedbrow talking2mouth "I do not care one whit why you thought digging around in the garden like a fool was a fine way to spend your scheduled time, but whatever compelled you to do so is best ignored in future!"

        klara @sadbrow talking2mouth "A--a girl said there was a shiny Eevee out here, and I thought if I could sell--"

        rowan surprisedbrow @angrybrow talking2mouth "And you believed her? Your folly, not hers! If someone promises a shortcut to success or prosperity, dismiss it outright! No such thing exists."

        klara @sadbrow talking2mouth "But--but I {i}need{/i} that Eevee to pay for this school!"

        rowan -surprisedbrow @closedbrow talking2mouth "Harrumph. You are unable to pay?"

        klara @talking2mouth "I passed the entrance exam, and got recommendations from people in the Galarian league--I earned my spot here. I just need to figure out how to pay for it!"

        pause 1.0

        rowan @closedbrow "[ellipses]{nw}"
        extend @talking2mouth "Klara."

        show rowan at getcloser, night

        rowan @talking2mouth "You have earned {i}nothing{/i} until it is held in your hands."
        rowan @talking2mouth "You would have been better served chasing scholarships, rather than fancies of a Shiny Eevee in the gardens. I will do you the kindness of claiming my hearing was acting up, and I didn't hear that ugly implication."

        pause 0.5

        klara @surprisedbrow talking2mouth "Scholarships[ellipses]?"

        rowan @talking2mouth "Harrumph. Yes. Though after this shameful display--skipping assembly, not reporting to your dorm, and worrying your dormmates, and security--you shan't be getting a Pokédollar from me."

        klara @talking2mouth surprisedbrow "Wha--what?! But I--I told you my story! I {i}need{/i} it!"

        rowan @talking2mouth "Do you believe you are the only one? I do not deny this school's cost is absurd. Pah, back in my day, I paid my attendance with part-time jobs."
        rowan @closedbrow talking2mouth "Granted, you face greater difficulties than I did. But that is no excuse if you are unwilling to work to earn the scholarships this school grants."
        rowan @angrybrow talking2mouth "Your problem is not one of poverty, but poverty of {i}character.{/i} Handing you everything you wanted on your first day would do you no good."

        scene blank with dis

        pause 1.0

        scene gym
        show leaf uniform
        show flashback
        with Dissolve(2.0)

        leaf @talking2mouth "Oh, hey! I remember you. We met on our first day here, right?"

        klara uniform @shadow surprisedbrow talking2mouth "Oh[ellipses] yes. Hi."

        pause 0.5

        klara @happy "{i}Hiiiii!{/i} Leaf, right? I guess we'll be battling against each other!"

        leaf @happy "Guess so!"

        klara @surprisedbrow talking2mouth "Oh, but before we do--those Battle Team tryouts--what are you thinking?"

        leaf @talkingmouth "What do you mean?"

        klara @talkingmouth "Well, you know. Is all this really just based on whatever this 'Janine' feels like?"

        leaf @surprisedbrow talking2mouth "Um. Yeah, I think so? But, you know, it's Janine. She's kinda legendary."

        klara @happy "Well, {i}I{/i} heard that the Battle Team has access to a bunch of scholarships. So if I can get in--"

        leaf @happy "Oh, no way, you're also trying to get in? Me, too! I bet the battles the Battle Team has access to are the {i}most{/i} fun."

        klara @surprisedbrow frownmouth "[ellipses]"
        klara @restrainedbrow talkingmouth "Hahaha, whaaaaat? Yeah, that's craaaaazy. And you don't even need the scholarships, do you?"

        leaf @talkingmouth "Not really. But I definitely wouldn't turn them down, hah!"
        leaf @talking2mouth "The Battle Team's usually got, like, forty people in it, though. So however many scholarships there are, the competition's probably going to be pretty tight."
        leaf @talkingmouth happybrow "Or maybe the scholarships are just shared equally among the team members. I dunno."

        klara @restrainedbrow madmouth "As it happens, I do. Instructor Koga told me that Janine's planning on having {i}way{/i} fewer Battle Team members this year. So just being a member might pay for a semester--if that's something you need, duh."

        leaf @talkingmouth "Y-yeah, like, if I needed that. Duh."

        pause 0.5

        leaf surprisedbrow frownmouth @happy "So, can we battle now?"

        TempCharacter("{color=#6f4097}???{/color}") "Wait."

        klara @surprisedbrow talking2mouth "Huh?! Who was that?"

        show smoke:
            animation
            alpha 0.0 yalign 3.0 xalign 0.5
            parallel:
                ease 3.0 yalign 0.5
            parallel:
                ease 0.5 alpha 1.0
                pause 0.5
                ease 3.0 alpha 0.0 

        pause 3.0

        show blank behind flashback
        show janine behind blank

        pause 0.1

        $ renpy.transition(None)
        hide smoke
        hide blank

        $ LineUp()

        janine @talking2mouth "'This Janine.' That's what you called me, right? You're Klara?"

        klara @talking2mouth "Uh--uh, yeppers! I--"

        janine @talking2mouth "You, go away."

        leaf @talkingmouth "Um. Okay."

        $ MoveOutSmart("leaf")

        janine @talking2mouth "My Dad mentioned you."

        klara @happy "Really? That's great! So you know how much I really care about--"

        janine @sadbrow talking2mouth "Stop. Just--{w=0.5}stop talking. You're too pink for this early in the morning."

        klara @frightenedbrow "[ellipses]"

        janine @talking2mouth "My Dad mentioned you. He told me you've been asking {i}so{/i} many questions about me. Not about what I want in a battler, but personal stuff, like my hobbies, routines, and favorite perfume."
        janine @sadbrow talkingmouth "I thought maybe you were asking because you had a crush on me. Not the first time I've had to deal with a fangirl during initiation week."
        janine @closedbrow talking2mouth "But obviously it wasn't that. I don't really care why you're so desperate to get onto the team--whether you were telling that brown-haired girl the truth or not."

        pause 0.5

        janine @talking2mouth "You're obviously trying to take a shortcut. I don't accept that. So save us both the time and don't try out for the Battle Team. I've got enough headaches, with that hedgehog banging on the door every five seconds."

        klara @frightenedbrow talking2mouth "Wait. Wait, wait, wait, wait!"
        klara @talking2mouth "That--that girl, Leaf--I was lying to her! I was trying to trick her, because I don't like her, because she made Professor Rowan chew me out on my first day here, and--"

        janine @talking2mouth "I don't care. And it sounds like you're making excuses, anyway. That girl {i}made{/i} Rowan chew you out?"
        janine @closedbrow talkingmouth "Rowan was my homeroom Professor. Show me a first-weeker who can {i}make{/i} him do anything, and you'll show me Cynthia."

        klara @sadbrow talkingmouth "No, no, you don't understand! Leaf--she--she's {i}nothing!{/i} She doesn't have any ambition! She isn't champion material!"
        klara @angrybrow talking2mouth "She just battles {i}for fun!{/i} She's never had to struggle--{i}I{/i} have! If you put her on the team, she--she'll be useless!"

        pause 0.5

        janine @talking2mouth "I had no intention of putting her on the team. Because, yeah, normally I prefer battlers who want victory a bit more aggressively."

        pause 0.5

        janine @closedbrow talking2mouth "But I'm kind of thinking of trying her out, now. She must have something if she got under your skin so hard, without even noticing."
        janine @closedbrow talkingmouth "Thanks for the idea. You can battle her now."

        hide janine with dis

        pause 1.0

        klara @frightenedbrow frownmouth "[ellipses]"

        $ MoveInSmart("leaf uniform happybrow", duration = 2.5)

        pause 0.5

        leaf @talkingmouth "Hey! Everything alright? What did Janine say? Was she as cool as she looked in the battle exhibition? Did she talk about the Battle Team? Is she interested in you? Did she mention me?"

        Character("{color=#6f4097}Janine{/color}") "\"{size=30}Heh.{/size}\""

        scene blank with dis

        pause 1.0

        scene stadium_full
        show leaf
        show lightbeam1 as beam1:
            pause 2.75
            zoom 0.6 alpha 0.0 yalign 0.9 xpos 0 rotate 40
            block:
                ease 0.25 alpha 0.5
            pause 0.3
            block:
                ease 1.0 rotate -40
                pause 0.5
                ease 1.0 rotate 40
                pause 0.5
                repeat
            
        show lightbeam1 as beam2:
            pause 2.75
            zoom 0.6 alpha 0.0 yalign 0.9 xpos -300 rotate -40
            block:
                ease 0.25 alpha 0.5
            pause 0.1
            block:
                ease 1.0 rotate 40
                pause 0.5
                ease 1.0 rotate -40
                pause 0.5
                repeat

        show lightbeam1 as beam3:
            pause 2.75
            alpha 0.0 yalign 0.8 xpos -400 rotate -40
            block:
                ease 0.25 alpha 0.6
            pause 0.2
            block:
                ease 1.0 rotate 40
                pause 0.5
                ease 1.0 rotate -40
                pause 0.5
                repeat
                
        show lightbeam1 as beam4:
            pause 2.75
            alpha 0.0 yalign 0.8 xpos -1400 rotate 40
            block:
                ease 0.25 alpha 0.6
            block:
                ease 1.0 rotate -40
                pause 0.5
                ease 1.0 rotate 40
                pause 0.5
                repeat
        show flashback
        with Dissolve(2.0)

        lisia @talking2mouth "[ellipses]Oh, and it looks like the battles in section five are finished!" 
        lisia @happy "Congratulations to the brown-haired girl in the pink skirt! Don't worry, pink-haired girl, you still fought well!"

        show leaf

        leaf @happy "Yes! Well done, Jigglypuff!" 

        klara @restrainedbrow talking2mouth "I[ellipses] I thought you were a no-show[ellipses]?"

        leaf @sadbrow talkingmouth "Yep, it was close, but I made it back in time!"

        klara @restrainedbrow talkingmouth "The Quarter Qlashes were meant to start {i}two{/i} hours ago. Why weren't you there? Why did Drayden wait so long?"

        leaf @winkbrow talkingmouth "I guess he's just a really nice guy."

        klara @restrainedbrow talking2mouth "I could've passed my first round without battling anyone if you weren't here. I could've[ellipses]"

        leaf @sadbrow talkingmouth "Aw, no! That'd be awful. Your past two opponents were no-shows as well?"

        klara @angrybrow frownmouth "[ellipses]"
        klara @sadbrow talking2mouth "Did you know there are scholarships tied to success in the Quarter Qlashes?"

        leaf @surprisedbrow talking2mouth "Oh, seriously? Like, from the school, or the Kobukan government?"

        pause 1.0

        klara @sadbrow talking2mouth "{size=30}Please. Pretend you lost. I {i}need{/i}--{/size}"

        $ MoveInSmart("Lisia")

        lisia @happy "Alright, battlers! Please evacuate the battlefield, okay? We've got a lot of rounds to get through, and not much time to do it, since we started late!"

        scene blank2 with Dissolve(3.0)

        image klarawoes1 = Text("Scholarships for perfect attendance and conduct.",size=30,color="#fff")
        image klarawoes2 = Text("Scholarships for success in the Battle Team.",size=30,color="#ffc9c9")
        image klarawoes3 = Text("Scholarships for winning in the Quarter Qlashes.",size=30,color="#ff7878")

        show klarawoes1:
            xalign 0.5 ypos 0.2
        
        show klarawoes2:
            xalign 0.5 ypos 0.4

        show klarawoes3:
            xalign 0.5 ypos 0.6

        narrator "Three options."
        narrator "Three chances."
        narrator "All gone."
        narrator "{i}Within the first month.{/i}"

        scene cafe at grayscale 
        with Dissolve(2.0)

        klara @sadbrow frownmouth "{size=30}[ellipses]What am I even doing here? I should just hitchhike home. I'm done. Out of options. I[ellipses]{/size}"

        $ MoveInRight("phobos", 1.5)
        $ MoveInRight("drayden", 1.5)

        phobos @talkingmouth "{gradualsize=20-36}[ellipses]and most obviously, we'll need to apportion a sizeable amount of the medical budget for the Millennium Drop Water Festival Contest.{/gradualsize}"
        phobos @winkbrow happymouth "The crystal trophy for victory does not come cheaply--such things don't just fall out of the sky!"
        phobos @closedbrow talkingmouth "And, naturally, we'll want the scholarships for victory to properly reflect the esteem with which we hold the noble art of coordinating here in Kobukan. They {i}must{/i} be appropriately brobdingantuan."

        $ MoveOutSmart("phobos")
        $ MoveOutSmart("drayden")

        pause 1.5

        scene cafe with slowdis

        klara @angrybrow talking2mouth "{i}That's it.{/i}"

        scene blank2 with dis

        stop music fadeout 15

        narrator "There was only one problem."
        narrator "You had {i}never{/i} coordinated before."
        narrator "You didn't have time to train your skill[ellipses] but luckily you knew someone--{i}everyone{/i} knew someone--who didn't need skill to succeed."
        narrator "And the best part was that it was in a field that Leaf couldn't interfere with, as she had stated quite clearly she didn't like contests."
        narrator "A foolproof plan."
        narrator "Until you met the biggest fool--a man {i}too dumb{/i} to understand the Sword of Damocles you'd positioned over him."
        narrator "A man who couldn't be blackmailed, threatened, or even persuaded to be anything but kind."
        narrator "Even to you."

        scene academyhall
        show leaf bunny frownmouth:
            xpos 0.66
        show klara frownmouth shadow casual:
            xpos 0.33 xzoom -1
        with splitfade

        queue music "audio/music/lament.ogg"

        pause 1.0

        leaf @talking2mouth "So that's why."

        pause 0.5

        leaf @talking2mouth "Wow. I thought maybe I {i}actually{/i} did something wrong, but that was literally all just on you, and what you did in response was completely disproportionate, even if I {i}did{/i} do any of that on purpose."
        leaf @flirtbrow talking2mouth "Also, you could have just {i}told me{/i} I was upsetting you instead of humiliating me and reminding me of when all my friends died."

        klara @surprisedbrow talking2mouth "What?"

        leaf @closedbrow talking2mouth "Oh, you didn't know about that part? Wow, lucky guess."

        pause 1.0

        show leaf:
            xpos 0.66 xzoom 1
            ease 0.5 xzoom -1

        leaf @closedbrow talking2mouth "Anyway, I know why you hate me now, but I don't hate you, so we can chat or whatever if you want to apologize. You'll need to apologize to [first_name], too."
        leaf @sadbrow frownmouth "[ellipses]"
        leaf @closedbrow cry talking2mouth "I liked thinking you were my friend."

        $ MoveOutSmart("leaf")

        pause 1.0

        klara @talking2mouth "Well? Aren't you going to go join her?"

        if (not BunRecruit("Game")):
            red @talking2mouth "Nah, I'm just guarding the door to the party. Bunny suits are a bit much for me, honestly."

        else:
            red frownmouth sadbrow "[ellipses]"

        klara @angrybrow talking2mouth "I want you to know something, [first_name]."

        red @sadbrow talkingmouth "Yeah?"

        klara @talking2mouth "I {i}truly{/i},{w=0.5} madly,{w=0.5} deeply,{w=0.5} hate you."

        red @wince talking2mouth "I saw that going differently in my head."

        klara @talking2mouth "I always do what's necessary to survive. To win. To get as far ahead as I can, and I don't care who I have to use, or who I have to pull down to crawl up."
        klara @angrybrow talking2mouth "Because I know, no matter how many people call me lazy, that I {i}am{/i} working harder than anyone else."

        pause 0.5

        klara @talking2mouth "I've always done this--because I had to."

        pause 0.5 

        klara @angrybrow shadow talking2mouth "And I've {i}never{/i} felt guilty for it."
        
        klara @angrybrow talking2mouth "I've never felt any shame for what I do. Or who I am. Or how I live."
        klara @angrybrow frownmouth "[ellipses]"
        klara @talking2mouth "Until you."
        klara @talking2mouth "Because even as I was using you so obviously a {i}child{/i} would see it coming a mile away, you were always so stupidly nice, and kind, and understanding--even though you didn't understand {i}anything.{/i}"
        klara @angrybrow talking2mouth "I feel guilty, now. For the first time ever. And I hate it so much I can't stand it."

        pause 1.0

        red @sadbrow "[ellipses]{nw}"
        extend @sadbrow talkingmouth "Good."

        show klara surprisedbrow frownmouth with dis

        red @happy "Don't mess with my friends, Klara." 

        pause 1.0

        klara angrybrow @talking2mouth "I {i}need{/i} you to understand how much I hate you right now. I need you to hurt like you hurt me."
        klara @restrainedbrow shadow talking2mouth "Because I know that you knowing there's someone out there who hates you--even me--is going to hurt you."

        red @upeyes sadeyebrows talking2mouth "Well, Cheren's given me some practice with that[ellipses] but, yeah, this is going to be stuck in the back of my mind pretty much forever. Like[ellipses] like a splinter."

        klara @talking2mouth "Good. Get out your Poké Balls--because my Pokémon are going to hammer that splinter down {i}all{/i} the way."

        show screen songsplash("Your Favorite Girl", "Vetrom")

        python:
            trainer1 = MakeRed()
            trainer2 = MakeTrainer("Klara")

        call Battle([trainer1, trainer2], specialmusic="audio/music/yourfavoritegirl.ogg", customexpressions=["red angrybrow frownmouth", "red angrybrow frownmouth", "klara angrybrow frownmouth", "klara madbrow madmouth"], customoutfits=[("bunny" if BunRecruit("Game") else ""), "casual"]) from _call_Battle_195
        $ RecordBattle("Klara2")

        show klara casual angrybrow frownmouth with dis

        if (WonBattle("Klara2")):
            narrator "Victory feels hollow."
            narrator "But it is still a victory."

        narrator "Klara fixes you with a look of such loathing as you've never seen before--true hatred for who you are, not merely what you've done, or what you might do."
        narrator "And, curiously,{w=0.5} this is a relief."
        narrator "You, at least, have an understanding of Klara now."
        narrator "A casual friend is nice to have,{w=0.5} but perhaps true bonds,{w=0.5} even those of hate,{w=0.5} mean more."
        narrator "I suppose that's your prerogative to decide."

        pause 0.5

        narrator "Regardless[ellipses] you now, truly, understand Klara--if only a little bit."

        scene blank2 with splitfade

        python:
            RelationshipRankUp("Klara", "Hated Enemy", 0)
            persondex["Klara"]["Value"] = 1
            persondex["Klara"]["Nature"] = TrainerNature.Special
            persondex["Klara"]["Mood"] = 0
            AddEvent("Klara", "TrueKlara")

call clearscreens() from _call_clearscreens_285
scene blank2 with Dissolve(3.0)

narrator "Eventually, the party comes to an end[ellipses]"
narrator "The many, many guests change back into their casual clothes and flee back to their dorms, aided by cover of night..."
narrator "...and more than a few instructors who decided for no particular reason to avoid looking out the windows this evening."
narrator "Now, let's do a tally of what you accomplished tonight, shall we?"

init python:
    def GetDescriptorFraction(fraction):
        if (fraction >= 1.0):
            return "{gradient=#EE8FB5-#6b0930}PERFECT{/gradient}!"
        elif (fraction >= 0.85):
            return "{color=#c1861e}Superb{/color}!"
        elif (fraction >= 0.7):
            return "{color=#00b23f}Brilliant{/color}!"
        elif (fraction >= 0.55):
            return "{color=#3110dd}Great{/color}!"
        elif (fraction >= 0.4):
            return "{color=#3C468D}Good{/color}."
        else:
            return "{color=#db4039}Passable{/color}."
    
    numattendees = 0
    foodquality = 0
    tailorquality = 0
    techquality = 0
    totaldescription = ""

python:
    # Number of attendees: May, Melody, Leaf, Ethan, Nessa, Rosa, Nate, Whitney, Red, Mallow 
    numattendees = (HasEvent("May", "BunnyKitchen") #may
        + (HasEvent("May", "BunnyKitchen") and mallow_present)#mallow
        + BunRecruit("Melody")
        + 1 # leaf
        + 1 # red
        + 1 # ethan
        + BunRecruit("Nessa")
        + BunRecruit("Rosa")
        + BunRecruit("Nate")
        + BunRecruit("Whitney"))# out of 10

    foodquality = BunRecruitCategory("Food") + (BunRecruit("May") and mallow_present) + 2# out of 7
    tailorquality = BunRecruitCategory("Tailor") + 2#out of 7
    techquality = BunRecruitCategory("Tech") + 1#out of 4

    totalfraction = (numattendees / 10.0 + foodquality / 7.0 + tailorquality / 7.0 + techquality / 4.0) / 4.0
    totaldescription = GetDescriptorFraction(totalfraction)
    globalmoodboost = round(5.0 * totalfraction)

image partyline1 = DynamicDisplayable(lambda x, y: (Text("The guests said that the atmosphere was [GetDescriptorFraction(numattendees / 10.0)]", size=30, color="#fff"), None))
image partyline2 = DynamicDisplayable(lambda x, y: (Text("The guests said that the food was [GetDescriptorFraction(foodquality / 7.0)]", size=30, color="#fff"), None))
image partyline3 = DynamicDisplayable(lambda x, y: (Text("The guests said that the bunny suits were [GetDescriptorFraction(tailorquality / 7.0)]", size=30, color="#fff"), None))
image partyline4 = DynamicDisplayable(lambda x, y: (Text("The guests said that the party's security was [GetDescriptorFraction(techquality / 4.0)]", size=30, color="#fff"), None))
image partyline5 = DynamicDisplayable(lambda x, y: (Text("Overall, the guests said that the party was[ellipses]", size=30, color="#fff"), None))
image partyline6 = DynamicDisplayable(lambda x, y: (Text("[totaldescription]", size=50, color="#fff"), None))

show partyline1 with Dissolve(1.0):
    xcenter 0.5 ypos 1.0/9.0
show partyline2 with Dissolve(3.0):
    xcenter 0.5 ypos 2.0/9.0
show partyline3 with Dissolve(3.0):
    xcenter 0.5 ypos 3.0/9.0
show partyline4 with Dissolve(3.0):
    xcenter 0.5 ypos 4.0/9.0
show partyline5 with Dissolve(3.0):
    xcenter 0.5 ypos 5.0/9.0

pause 1.0

show partyline6 with Dissolve(3.0):
    xcenter 0.5 ypos 6.0/9.0

python:
    for char in persondex:
        if (IsNamed(char) and GetNature(char) != TrainerNature.Special):
            persondex[char]["Mood"] += globalmoodboost

narrator "Such a [totaldescription[:-1]] party raises the mood of the entire school--yes, {i}everyone{/i}--by [IntToWord(globalmoodboost)] points."

narrator "As you tear down the last of the decorations, and prepare to haul your exhausted body to bed, you silently resolve once again to never be involved in any parties, ever."

$ RemoveEvent("Game", "AutoBunny")

jump day010613