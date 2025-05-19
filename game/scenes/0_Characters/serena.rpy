label Serena1:
    if (not IsBefore(1, 5, 2004)):
        $ AddEvent("Serena", "Level2SceneVer2")

    scene hall_B 
    show serena
    with Dissolve(2.0)
    $ renpy.music.queue("Audio/Music/Vaniville_Start.ogg", channel='music', loop=None, fadein=0.0, tight=None)
    $ renpy.music.queue("Audio/Music/Vaniville_Loop.ogg", channel='music', loop=True, tight=None)

    narrator "As you turn the corner, you see Serena struggling under the weight of several large books."

    red @talkingmouth "Serena! What're you up to?"

    serena @surprised "Ah? {w=0.5}{nw}"
    extend @happy "Oh, hello. I was just going to the library. I need to catch up on my studying, I'm afraid."

    red @closedbrow talking2mouth "Yeah, that'd explain the stack of books."

    menu:
        "Would you appreciate a study partner?":
            pass

        "Need any help carrying those?":
            pass

    serena @happy "Why, certainly. That would be splendid, thank you."

    red @happy "Cool. Let's head off to the library, then."

    scene library with splitfade

    show serena with dis

    pause 2.0

    red @closedbrow talking2mouth "You've got a pretty wide variety of subjects here. Pokémon breeding, battling, training... looks like a shark cutlery bored."

    serena surprisedbrow frownmouth @surprised "{i}...Qu'est-ce que c'est?{/i}"

    red @surprised "Huh?"

    serena closedbrow talking2mouth "What is... a 'shark cutlery bored'?"

    red @happy "Oh, you know! One of those things where there's all kinds of meats and cheeses, and you eat them down with a bunch of wine."

    serena sad "Are... are you referring to a {i}charcuterie board{/i}?"

    red @surprised "Oh, shit, that's what it's called? That's {i}way{/i} more Kalosian than I was expecting."

    serena -sad "[ellipses]"

    serena @happy "Hee hee hee. You are quite entertaining, [first_name] [last_name]."

    red @closedbrow talking2mouth "Uh, thanks. Kinda feel like I'm the butt of a joke here, but... thanks."

    serena @happy "{i}Non, non!{/i} I'm not laughing at you. I am laughing, ah, {i}with{/i} you. Shark cutlery... hee hee!"

    red @angrybrow happymouth "Yeah, well, I bet a hoity-toity upper-class woman like yourself has her blind spots as well."

    serena angrybrow @happymouth "Oh? Do you challenge me?"

    red @happy "You bet your lavender-scented bedsheets I do."

    serena @happymouth "Then, please, ask me anything you think might be in my blind spot. You may find me surprisingly well-informed."

    red @talkingmouth "Sure. This is something everyone who's ever had to go for a hike on a sweltering forest trail would know. What's in bug juice?"

    serena -angrybrow frownmouth surprisedbrow @surprised "Eh?"

    red @happy "Oh, you don't know? Washing out that early, huh?"

    serena -frownmouth -surprisedbrow @closedbrow talking2mouth "No, I know this. I just thought your questions would be more... agrarian in nature."

    red @confusedeyebrows talking2mouth "Why does everyone think I'm a farmer?"

    serena -thinking @closedbrow talking2mouth "In any case, bug juice is 25 percent purple grape juice, 25 percent raspberry juice, 45 percent lemon-lime soda, and 5 percent vodka, if no-one's watching. With a bit of ice."

    red @surprised "Uh... okay, that is genuinely surprising."

    serena angrybrow @happymouth "Please, keep them coming."

    red @closedbrow talking2mouth "Okay. Uh, what's the best way to catch catfish Pokémon from lakes or ponds?"

    serena @happy "Noodling, of course. Why waste money on bait, when they're just as liable to chow down on your hands?"

    red @surprised "Shit. Okay, your car's battery is dying, it keeps going down, won't charge up even when you drive. What's the problem?"

    serena @happy "Well, it could be any number of things, but the first thing I'd do is check the alternator." 
    serena @closedbrow talking2mouth "If it's broken, then you can just get a new one from pretty much any auto parts store."

    red @surprised "And what if it doesn't fit?"

    serena @happy "Well, that means the bushing is probably a bit too large. So you can just sandpaper the alternator's rear end down."

    red @surprised "...How the hell...?"
    red @closedbrow talking2mouth "Wait. I got it. No, I got it, now. There's absolutely {i}no way{/i} that an upper-class Kalos girl will get this one."
    red @angrybrow happymouth "There's a sport that's pretty popular in Kanto. It's slow, dangerous, and {i}very{/i} dirty."
    red @closedbrow talking2mouth "I don't think even middle-class Kantonians watch it, even though it originated there."
    red @talking2mouth "So--"

    serena @happymouth "Rhyhorn Racing."

    red @surprised "...Uh. A-and... who's the best Rhyhorn Racer...?"

    serena -angrybrow @closedbrow happymouth "That would be Grace Umaoka."

    red @wince talking2mouth "...Damn. I've been completely beaten."

    serena @talkingmouth "Why, thank you. What do I win?"

    pause 2.0

    $ PlaySound("idea.ogg")

    red @angrybrow talking2mouth "Hey. Wait a minute."

    serena surprisedbrow frownmouth @surprised "Oh?"

    red @closedbrow talking2mouth "You're from Kanto."

    serena @talkingmouth "Er... why do you think that?"

    red @talkingmouth "Give me a better reason for you to know Grace Umaoka."

    serena @talkingmouth "Uh... Well, I mean, there are plenty of possible reasons, such as..."

    red @confusedbrow frownmouth "...?"

    serena -surprisedbrow -frownmouth -surprised @sad "I could be related to her?"

    red @closedeyes talking2mouth "Yeah, that doesn't seem likely. Anyway, even if you were, that'd just {i}prove{/i} you're from Kanto."

    serena @surprised "How so?"

    red @happy "Well, I mean, she's Kantonian. She lived there her whole life before she moved...{w=0.5} to...{w=0.5} Kalos...{w=0.5}"

    pause 2.0

    show serena happybrow with dis

    show library with vpunch

    red @surprised "OH MY GOD."

    red @surprised "{i}You're{/i} Serena Umaoka?! Grace's daughter?!"

    serena -happybrow @closedbrow talkingmouth "Shhh. We're in a library."

    red @wince talking2mouth "Sorry."

    serena @sad "But, ah... yes, I am."

    red @talkingmouth "I had a poster of your Mom on my wall at home!"

    serena @talkingmouth "Many did, yes."

    red @talkingmouth "I don't get it, though. Your mom only left Kanto, like, two years ago. What happened?"

    serena @surprised "Could you clarify?"

    red @talkingmouth "Yeah. I mean, I didn't really follow you, no offense, but I sometimes went to your Mom's races, and saw glimpses of you."

    serena @surprised "I'm... not offended that you did not follow me."

    red @closedbrow talking2mouth "But, just, like, two years ago, I remember... you were all... overalls and pigtails. You wore a baseball cap."
    red @closedbrow talking2mouth "You were whooping and hollering at those races. Yelling out like the reddest-necked farmer anywhere in Southwest Kanto."
    red @happy "I mean, I recognize the sunglasses, but everything else... I mean, if you hadn't just told me, I would {i}never{/i} have recognized you."

    serena @sad "Well... a lot can happen in two years."

    red @closedbrow talking2mouth "Yeah, but... {i}that much{/i}? There's gotta be more than just the new environment, right?"

    serena @talkingmouth "As a fan of my mother, I assume you heard about the silicon mine we discovered under our ranch?"

    red @talkingmouth "Yeah, didn't Silph Co. buy it from you for, like, a billion?"

    serena @talkingmouth "Very slightly less. In any case, with that much money... and since we no longer had our ranch... well, we'd always wanted to visit Kalos."

    red @closedbrow talking2mouth "Hm... that explains {i}why{/i}, and {i}how{/i}, you moved... but just moving wouldn't cause such a dramatic change."

    red @sadeyes sadeyebrows happymouth "I mean, I think. I've obviously never moved anywhere before coming to Kobukan."

    serena @sad "...People change for the oddest reasons."

    pause 2.0

    show serena surprisedbrow frownmouth with dis

    red @closedbrow talking2mouth "Does this have anything to do with Calem?"

    show serena sad2brow poutmouth with dis

    pause 2.0

    serena -sad2brow frownmouth @sad2brow talking2mouth "What would make you think that?"

    red @sadeyes sadeyebrows happymouth "Not much. I've just got two dots, and I'm trying to connect them."
    red @talkingmouth "Calem and you knew each other before coming here. Calem didn't know you'd be here, but it seems like you {i}did{/i} know he'd be here."
    if (not IsBefore(1, 5, 2004)):
        red @closedbrow talking2mouth "And now you dorm together."
    red @closedbrow talking2mouth "That's, it just... never made sense to me."

    serena sad "I'm sorry. I don't think... I don't feel comfortable telling you about this. Perhaps one day. But not now."

    pause 1.0

    red @talkingmouth "That's fine. I just want to know something. Are you alright? You're not... forcing yourself to be something you're not, are you?"

    serena @happymouth "If I was, how would I know?"
    serena @sadbrow happymouth "What is the 'true self' beyond the entirety of the memories and thoughts that make up a person?"
    serena @closedbrow talking2mouth "To demonstrate the fullness of the true self at all times sounds exhausting."
    serena @talkingmouth "Though I abhor when one is forced to pretend to be a person they're not..."
    serena -sad @happy "I don't see anything wrong with simply, temporarily, not demonstrating certain parts of yourself. For convenience's sake."

    redmind @sad "That sounds... very much like pretending to be a person you're not."

    red @talkingmouth "Well... I'll leave it there then, Serena Umaoka." 
    red @closedbrow talking2mouth "But if you ever change your mind, and want to tell me about the real Serena, whatever that means, I'll be here."

    serena @talkingmouth "I appreciate it."

    pause 2.0

    serena @closedbrow talkingmouth "I must say, [first_name] [last_name], I am surprised."

    red @surprised "Oh?"

    serena @closedbrow talkingmouth "Yes. I didn't realize you were so perceptive. So intelligent."

    red @happy "C'mon, don't I just give off the vibes of a brainiac?"

    serena @happy "Not particularly, no."

    red @sad "Ouch."

    serena @talkingmouth "But to be able to figure out my background from those few questions... I think, perhaps, you too are hiding your light under a bushel somewhat."

    red @happy "What? Me? No way! I'm a genuine dumbass."

    serena @happy "Hee hee. If you insist."

    pause 2.0

    red @talkingmouth "So, hey, what now? Now that I know your big secret?"

    serena @sadbrow happymouth "I would ask that you please not mention it to anyone else. Calem knows, of course, but it would complicate my plans if he knew there was a third party involved."

    red @talkingmouth "Sure. My lips are sealed."

    red @happy "Uh... what kind of plans are those? Can I know?"

    serena @talkingmouth "Not right now, please."

    red @closedeyes talking2mouth "Ugh, I seriously want to know, though... Oh well. Anything I can do to help with those plans?"

    serena @poutbrow talkingmouth "Um... there is actually, one thing. It might not be possible, but..."

    red @talkingmouth "Sure, name it!"

    if (IsBefore(1, 5, 2004)):
        serena @closedbrow talking2mouth "Would it be possible for you to, ah... make sure Calem stays single?"

        red @surprised "Oh, wow, that's where we're going with this? I mean, I don't know what I can do about that."

        serena poutbrow poutmouth @talking2mouth "...I mean, ah... could you make sure that he stays single, in regards to... ah..."

        redmind @thonk "What's the problem? It looks like she's trying to say something she doesn't know how to say."

        serena frownmouth angrybrow @furybrow angrymouth "Oh, what-{i}ever!{/i} Listen up, [first_name]. You start datin' Calem, and we're going to have {i}big problems{/i}, y'hearin' me?"

    else:
        serena @closedbrow talking2mouth "Would it be possible for you to, ah... perhaps find Calem a... woman?"

        red @surprised "Oh, wow, that's where we're going with this? I mean, I don't know what I can do about that."
        red @confused "Wait, I thought {i}you{/i} wanted to date him?"

        serena @sad "I did! Er... I thought I did? But then I moved in with him, and everything has become so much more difficult, and... I don't know if... that is, to say, I'm unsure if..."

        serena poutbrow poutmouth @talking2mouth "...I mean, ah... it would be easier if he were {i}not{/i} single, since... in regards to... ah..."

        redmind @thonk "What's the problem? It looks like she's trying to say something she doesn't know how to say."

        serena @angry "Oh, what-{i}ever!{/i} Listen up, [first_name]. We'all need to get that boy hitched to some other chick--or man, it don't matter--before I have a nervous breakdown!" 
        serena frownmouth angrybrow @furybrow angrymouth "He's too damn kind, and didn't even {i}mention{/i} the fact I've been lyin' to his face for ages! Y'hearin' me?"

    redmind @surprised "Woah. Her facade completely broke there."

    red @surprised "Uh... yeah, absolutely. I'm hearin' ya."

    pause 2.0

    red @surprised "Wait, he likes men too?"

    serena -angrybrow @closedbrow talking2mouth "That's very clearly not the point."

    redmind @thinking "Huh. I was definitely getting the opposite vibes from him, but, uh... good to know."

    if (IsBefore(1, 5, 2004)):
        red @talkingmouth "Yeah, uh, noted. I'll do my best to avoid dating him. And if I can pull off some wacky hi-jinks to make sure he doesn't date anyone else, I'll see what I can do about that, too."

    else:
        red @talkingmouth "I don't get it, though. {i}You{/i} aren't dating, are you?"

        serena @sad "No."

        red @talkingmouth "Then... why don't you... just tell him you need some space?"

        serena @sadbrow talking2mouth "It is {i}not{/i} that easy. I was chasing after him for so long, and now that he's stopped and turned around to face me, I've run right into him."
        serena @sadbrow talkingmouth "...I have what I wanted. But everything I was chasing after has come too quickly, and... I cannot process my feelings properly when I wake up every morning staring into his gorgeous eyes."

        pause 2.0

        red @playfulbrow talking2mouth "So your plan is to get him a girlfriend--or boyfriend--so that he's no longer an option for yourself?"

        serena @talkingmouth "Rather."

        red @confused "And what if this substitute boyfriend/girlfriend is his {i}one?{/i}"

        serena @sadbrow talkingmouth "Then he will be happy. Consequently, so will I."

        pause 1.0

        red @happy "Well, hell, sign me up."

    serena happybrow neutralmouth "Splendid. I've always wanted to be part of a conspiracy."

    if (not persondex["Serena"]["Contact"]):
        serena "You'll need this, then, to report your success."

        $ BecomeContacted("Serena")

    pause 1.0

    red @talkingmouth "Hey. Uh, I can tell this is really important to you, but... are you sure you have time for this? I mean, Kobukan is really competitive, and everyone's so busy all the time..."

    serena @closedbrow talkingmouth "Hee hee hee."

    serena @talkingmouth "There's always time for true love, my {color=#0048ff}conspirator{/color}."

    $ RelationshipRankUp("Serena", "Conspirator", 1)

    return

label Serena2:
    scene library 
    show serena
    with Dissolve(2.0)
    $ renpy.music.queue("Audio/Music/Vaniville_Start.ogg", channel='music', loop=None, fadein=0.0, tight=None)
    $ renpy.music.queue("Audio/Music/Vaniville_Loop.ogg", channel='music', loop=True, tight=None)
    
    serena @happy "Ah, wonderful. I was wondering when I might see you again. I rather thought you'd attempted to defect from our grand cause."

    red @happy "Wouldn't dream of it. Our grand cause being... um, trying to get Calem a date, right?"

    serena @angrybrow talkingmouth "Quite right."

    red @sadbrow sweat talkingmouth "Dumb question, I know, but have you asked Calem if he wants us to do this for him?"

    serena @closedbrow talking2mouth "No need. I know he doesn't."

    serena @happy "Which makes it all the more thrilling, do you not think? It's rather like wrapping up a Snowfall present--a lovely surprise for the receiver."

    red @sadbrow talkingmouth "Well... you know him better than I do. But, for the record, this was {i}your{/i} idea, right?"

    serena @closedbrow talkingmouth "Naturally. I get the credit."

    red @sad2brow talkingmouth sweat "{size=30}That's one way to put it.{/size}"

    serena @closedbrow talking2mouth "I believed there was a new member of the Coordinator Club that held promise, at first..."
    serena @sadbrow talkingmouth "Too hasty an estimation, I'm afraid. I simply thought she was Calem's 'type'. Various other attributes have revealed themselves since then, and I'm quite sure it's not the perfect match I envisioned."
    serena @closedbrow talkingmouth "But this minor setback revealed something quite important to me. I cannot simply rely on my eyes to estimate people, much as one's visual estimation of myself might be quite misguided."

    pause 1.0

    show serena angrybrow with dis:
        block:
            xpos 0.49
            pause 0.01
            xpos 0.51
            pause 0.01
            repeat 20
        xpos 0.5

    narrator "Serena vibrates with visible excitement."

    red @sadbrow talkingmouth "You're crazy, you know that?"

    serena -angrybrow @closedbrow talkingmouth "I am naught but flattered, Mr. [last_name]. A dash of insanity is a cornerstone to any excellent conspiracy, is it not?"

    red @closedbrow talking2mouth "{size=30}Hoo boy.{/size}"
    red @talkingmouth "Okay. You said you can't just rely on your eyes. So what are you thinking?"

    serena @talking2mouth "Oh, it's quite simple. We'll simply interview a few notable prospects."

    red @confused "Huh. Okay, that's an idea, sure. I guess it might actually work, even. Who are we starting with?"

    if (not HasCrossKnowledge("Serena", "Jasmine")):
        serena @talkingmouth "Jasmine. Fortunately, she is right here in the library."
        
        serena @talkingmouth "Please, accompany me, if you will."

        red @talkingmouth "Sure."

        show serena:
            xpos 0.5
            ease 0.5 xpos 1.1

        pause 1.0

        show serena sadbrow:
            xpos 1.1
            ease 0.5 xpos 0.5

        pause 1.0

    else:
        serena @talkingmouth "In a moment. One more thing, if you will."

        red @talkingmouth "Sure." 

    serena sadbrow @talkingmouth "Ah... this may come as a bit of a struggle, but might I request you are not entirely truthful about what we are interviewing our prospectives about?"

    red @closedbrow talking2mouth "That's going to make everything much harder, and not just for me."

    serena @closedbrow talking2mouth "I am simply unsure if we will receive candid responses if we do not leverage a bit of occlusion in regards to our overall plan."

    red @talkingmouth sadbrow "I mean, I see where you're coming from. But, uh, not sure I can agree with you."

    serena -sadbrow @talkingmouth "Very well. Perhaps we should make a bet?"

    red @confused "Oh yeah? What kind of bet? Can't really do money..."

    serena @closedbrow talkingmouth "If this plan yields no fruit, then I shall grant you two tickets to a Rhyhorn race, for you and a friend."

    red @happy "Sneaky. You know I'd invite you, anyway."

    serena @winkbrow talkingmouth "I'm sure you can imagine that attending such an event with one with the last name 'Umaoka' is, perhaps, a greater benefit than it appears on the surface."

    red @talkingmouth "I just enjoy your company, but sure, hanging out with Grace's daughter at a Rhyhorn Race is a pretty big benefit, too. It's a date, then."

    serena @closedbrow talkingmouth "Only if it's {i}not{/i} a date. I'll warn you I'm quite confident in my picks."

    if (not HasCrossKnowledge("Serena", "Jasmine")):
        if (RomanticallyEntangled("Jasmine")):
            $ RecordCrossKnowledge("Serena", "Jasmine")
            show serena surprisedbrow frownmouth with dis

            red @talking2mouth "Well... I gotta say that your first pick doesn't fill me with confidence."

            serena @talking2mouth "Oh? Jasmine? She is delightful! Kind, beautiful, unyielding, and Calem and Jasmine are already familiar with each other."
            serena @closedbrow talking2mouth "Unless you have knowledge I do not, I'm not sure I can agree with your assertion."

            red @talking2mouth "Uh... yeah. Yeah, I do have knowledge you do not."
            
            show serena surprisedbrow frownmouth blush with dis

            red @closedbrow talking2mouth "Unless, uh, Jasmine swings both ways."

            pause 1.0

            serena @talking2mouth "Oh my."

            serena @closedbrow talking2mouth "Well, granted, perhaps that was not the best pick. Let's move on."

            show serena -surprisedbrow -frownmouth with dis

            red @sadbrow talkingmouth "Who's next on the list?"

        else:
            red @closedbrow talking2mouth "Alright. Let's go hunt down Jasmine."

            pause 1.0

            show jasmine:
                xpos 1.1
                ease 0.5 xpos 0.66

            show serena:
                xpos 0.5
                ease 0.5 xpos 0.33


            if (GetRelationshipRank("Jasmine") > 0):
                jasmine @talkingmouth "Oh, hello, [first_name]. Serena, you're here too?"

                serena @talkingmouth "Rather so. We were hoping we might have a moment of your time, and perhaps ask you a couple questions?"

            else:
                jasmine @talkingmouth "Oh, hello, Serena. [first_name], you're here too?"

                red @happy "Yep. We've gotta couple questions for you. Got a second?"

            jasmine @talkingmouth "I don't see why not. I was just about to take this book back to my dorm."

            jasmine @happy "Do you mind if we sit?"

            serena @talkingmouth "Not at all."

            show jasmine:
                xpos 0.66 ypos 1.0 zoom 1.0
                ease 0.5 ypos 1.2 zoom 1.3

            show serena:
                xpos 0.33 ypos 1.0 zoom 1.0
                ease 0.5 xpos 0.33 ypos 1.2 zoom 1.3

            serena @talkingmouth "So, you were just about to bring that book back, yes? May I inquire as to its contents?"

            jasmine @surprised "Hm? Certainly."
            jasmine surprisedbrow frownmouth @happybrow talkingmouth "It's called {i}Metal Magic.{/i} It's a book in a series about wizards who burn metals to use, um, magical powers. I simply can't put it down!"

            serena closedbrow frownmouth @talking2mouth "Hm. Fiction?"

            pause 2.0

            jasmine -surprisedbrow -frownmouth @talking2mouth "...One assumes."

            serena @talking2mouth "I see..."

            redmind @thinking "I know what she's thinking. Calem isn't the biggest fan of fiction, preferring to read biographies, or historical texts. His shelf in the old dorm had tons of black-and-white photos of stern-looking dead guys on them."
            redmind @sadbrow "But that's a really small thing to cut Jasmine out of the running for..."

            serena -closedbrow -talking2mouth @talkingmouth "It's no matter. Tell me, what are your thoughts on art? Painting, or other such mediums?"

            jasmine @talkingmouth "I'm not sure I have strong opinions, besides a general appreciation. Um, at the therapy center I attend occasionally, some of the other patients paint--there's one girl who's delightfully good at it, though she uses her feet."
            jasmine @happy "I don't usually engage in that sort of thing, though."

            serena sadbrow frownmouth @talking2mouth "I see."

            pause 1.0

            jasmine sadbrow @talkingmouth "I'm sorry. I feel like I'm disappointing you in some way."

            serena neutralbrow @happybrow talkingmouth "N-no, not at all."

            show jasmine surprisedbrow frownmouth with dis

            serena @talkingmouth "I suppose I've one more question. How many children do you intend on having?"

            pause 1.0

            show jasmine unamusedbrow frownmouth with dis

            show serena surprisedbrow with dis

            jasmine @talking2mouth "Unless massive advances in gene editing technology are invented, approved for use, and made available to the public at an affordable rate within the next two decades, I suspect my answer is unavoidably zero."

            serena -surprisedbrow @sadbrow talking2mouth "...Ah. I apologize, I didn't mean to imply that... er, that is..."

            jasmine -unamusedbrow -frownmouth @talking2mouth "I know you meant no offense. None has been taken."
            jasmine @sadbrow talkingmouth "But it is not exactly a choice for me, nor for many others. The ability to {i}choose{/i} who we are is a wonderful gift."

            serena @talkingmouth "That... it is."
            serena -frownmouth @closedbrow talking2mouth "Apologies. We should let you get back to your {i}Metal Magic{/i}."

            jasmine @happybrow talkingmouth "Thank you. And, really, I am not offended." 
            jasmine @sadbrow talkingmouth "Just... appreciate what you have. Many people wish to change their lives, not because they seek something better, but because they cannot endure what they {i}do{/i} have."

            serena @sadbrow talkingmouth "Of course. I am aware."

            jasmine @closedbrow talkingmouth "Of course you are. I will see you later, in Instructor Bertha's class, then?"

            serena @talkingmouth "Yes, see you then."

            hide jasmine with dis

            pause 0.5

            show serena blush poutmouth angrybrow with dis

            red @talking2mouth "If all our interviews go like that, those Rhyhorn race tickets are as good as mine."

            serena "Hmph!"
            serena @blush talking2mouth "I've never interviewed someone before. Please allow me a grace period as I become accustomed to the role I'm playing!"

            red @happy "Sure, sure. Who's next on the list?"

            show serena -blush -poutmouth -angrybrow with dis

    else:
        red @talkingmouth "Sure. Who's on the list?"

    if (not HasCrossKnowledge("Serena", "Janine")):
        serena @talkingmouth "I've decided on Janine."

        red @surprisedbrow talking2mouth "What?"

        serena @closedbrow talking2mouth "She is ambitious, attractive, strong, and clever. I see no problem, do you?"

        if (RomanticallyEntangled("Janine")):
            $ RecordCrossKnowledge("Serena", "Janine")
            show serena surprisedbrow frownmouth with dis

            red @talking2mouth "Uh, yeah. She's kinda... involved already. With me. And she isn't looking for anything more. Kinda a one-guy woman, y'know?"

            if (HasCrossKnowledge("Serena", "Jasmine")):
                serena -surprisedbrow -frownmouth @talking2mouth "Jasmine {i}and{/i} Janine, hm...? Perhaps I should introduce you to Jaquelyn or Jamala."

                red -surprisedbrow -frownmouth @closedbrow sweat talking2mouth "It's a coincidence, I swear."

            serena @talkingmouth "Well, that's quite surprising. But fear not, we have plenty of other individuals on the list to try our hand at."

        else:
            red @closedbrow talking2mouth "Look, Calem's kind of a gentleman. I'm pretty sure Janine is a bit too forceful for him."

            serena @blush heartbrow talkingmouth "Hm... so you say. But I assure you Calem can be quite forceful when sufficiently motivated."

            serena @closedbrow talking2mouth "Still, I'll keep your warning in mind. Is Janine available now?"

            red @talking2mouth "As far as I know. She's probably at the Battle Hall, if she wants to be found."

            serena @talkingmouth "Then let us not tarry!"

            show serena: 
                xpos 0.33 ypos 1.2 zoom 1.3
                ease 0.6 xpos 0.4 ypos 1.0 zoom 1.0
                ease 0.2 xpos 1.2

            pause 1.0

            redmind @thonk "I'm not sure I know {i}how{/i} to tarry."

            scene blank2 with splitfade

            pause 1.0

            scene stadium_empty
            show janine 
            with dis

            serena @talkingmouth "Hello, Janine."

            janine @talking2mouth "Uh, hi. [first_name]?"

            red @talkingmouth "Sorry, this is Serena Umaoka. She's got a couple questions for you."

            janine @talking2mouth "Sure. This won't take long?"

            serena @talkingmouth "It shouldn't! First question, if I may. What do you like to do in your freetime?"

            janine @surprisedbrow talking2mouth "Oh, wow. Was expecting something about battles, to be honest. Uh, in my freetime, I..."
            janine @closedbrow talking2mouth "Huh. Haven't really had free time in a while. I guess free climbing is pretty fun?"
            janine surprisedbrow @neutralbrow blush talking2mouth "Oh, and working on my knotcraft. You know, ropes. Hooks. Other things."

            serena @talkingmouth "That makes sense. They probably help you with climbing!"

            pause 1.0

            janine smilemouth @talking2mouth "Yeah, sometimes."

            serena @talking2mouth "Okay. {size=30}That can be worked around.{/size} Do you have any interest in having children at some point?"

            janine surprisedbrow -smilemouth @talking2mouth "What?"

            serena @talkingmouth "Um, children. You know, {i}enfants{/i}."

            janine @closedbrow talking2mouth "What kind of quiz is this?"

            serena @sadbrow talkingmouth "I really meant no offense. If you don't wish to answer..."

            janine @closedbrow talking2mouth "No, it's fine, I'm just not used to getting caught so off-guard."
            janine @sadbrow talking2mouth "Uh, not really thinking about children at the moment. Or marriage."
            janine @talking2mouth "Champion's step one. Everything else is step two."

            serena closedbrow talking2mouth "Hm..."

            redmind @thonk "Hm. Serena didn't like that. I guess kids must be pretty important to Calem."
            redmind @sad2brow "On the other hand, she's asking questions that most people don't generally ask until {i}several{/i} dates in. [ellipses]I assume."

            show janine surprisedbrow with dis

            serena @talkingmouth "Okay, I think that's all I need to know. Though, just to ask, would you have any interest in taking your husband's name?"

            pause 1.0

            janine -surprisedbrow @talking2mouth "[ellipses]Seriously, [first_name], where'd you get this girl?"

            serena @talkingmouth "If it's too personal, I--"

            janine @closedbrow talking2mouth "Look. I'm a Koga. I'll always be a Koga. Now, that doesn't mean I'm going to do all the crazy stuff my Dad does, but I'm pretty sure his heart would break if I left this name behind."
            janine @closedbrow talking2mouth "If I marry someone, they're just going to have to be okay with that."

            serena @happy "Splendid. Thank you, Janine. I may ask some follow-up questions later, but I think I've made a good start at the present. I appreciate your time!"

            hide serena with dis

            pause 1.5

            janine angrybrow @talking2mouth "What the fuck was that, [first_name]? She's that student who's always hanging out with that old man, right? Was she hitting on me?"

            red @sadbrow talkingmouth "It's {i}so{/i} much weirder than that."

            janine sadbrow @talking2mouth "...I'm going to be thinking about this for weeks. Damn."

            hide janine with dis

            pause 1.5

            show serena neutralbrow neutralmouth:
                xpos 1.1
                ease 0.5 xpos 0.5

            serena @talkingmouth "A disappointing showing. She was very impressive during that exhibition match at the beginning of the year, but perhaps not the sort of impressive that Calem is looking for."

            red @unamusedbrow talking2mouth "I'm not sure that Calem is looking for {i}anything{/i} right now."

            serena @talkingmouth "Which is why it's up to us to find it for him!"

            red @closedbrow sweat talking2mouth "Sure. Who's next on the list?"

    else:
        red @talkingmouth "Sure. Who's next on the list?"

    if (not HasCrossKnowledge("Serena", "Dawn")):
        serena @talkingmouth "Dawn is, I believe, an excellent pick."

        red @talkingmouth "Are you..."

        pause 1.0

        if (HasEvent("Instructor Valerie", 2.1)):
            red @closedbrow talking2mouth "No, actually, that makes sense. I can even see that. We all share Fairy class, too, so I know we're familiar with each other."
        else:
            red @talking2mouth "No, actually, that makes sense. I can even see that. They share Fairy class, too, so they're familiar with each other."

        if (RomanticallyEntangled("Dawn")):
            $ RecordCrossKnowledge("Serena", "Dawn")
            show serena surprisedbrow frownmouth with dis

            red @talkingmouth "There's just the problem that Dawn and I are kinda, already, a thing."

            if (HasCrossKnowledge("Serena", "Jasmine")):
                if (HasCrossKnowledge("Serena", "Janine")):
                    serena @blush surprisedbrow talkingmouth "Surely not. All three of them?"

                    red @closedbrow lightblush talking2mouth "I swear we all talked it out, and everyone's fine with the arrangement. I'm not being a scumbag."

                    red @talkingmouth "But... yeah, all three of them."

                else:
                    serena @blush surprisedbrow talkingmouth "Surely not. Jasmine {i}and{/i} Dawn?"

                    red @closedbrow lightblush talking2mouth "I swear we all talked it out, and they're both fine with the arrangement. I'm not being a scumbag."

                    red @talkingmouth "But... yeah, both of them."

            elif (HasCrossKnowledge("Serena", "Janine")):
                if (HasCrossKnowledge("Serena", "Jasmine")):
                    serena @blush surprisedbrow talkingmouth "Surely not. All three of them?"

                    red @closedbrow lightblush talking2mouth "I swear we all talked it out, and everyone's fine with the arrangement. I'm not being a scumbag."

                    red @talkingmouth "But... yeah, all three of them."

                else:
                    serena @blush surprisedbrow talkingmouth "Surely not. Janine {i}and{/i} Dawn?"

                    red @closedbrow lightblush talking2mouth "I swear we all talked it out, and they're both fine with the arrangement. I'm not being a scumbag."

                    red @talkingmouth "But... yeah, both of them."

            serena @talkingmouth "Well, that's only a minor hiccup. I was hopeful about this one, but we have other options."

        else:
            serena @talkingmouth "My thoughts exactly. I'm rather familiar with her from our work in the Coordinator club together, and I'm quite certain she's a perfect fit for our Calem."

            red @talkingmouth sweat "All I can do is watch the trainwreck, at this point."

            serena @angrybrow talking2mouth "Nonsense. Dawn will be a perfect match, just you wait and see. I imagine she's probably practicing in the Contest Coliseum at this time. Please, let's make haste--the [timeOfDay.lower()] is drawing long."

            scene blank2 with splitfade

            pause 2.0

            $ AddEvent("Professor Oak", "LearnedAboutContestColiseum")

            scene concerthallstage
            show dawn contest closedbrow frownmouth
            with splitfade

            red @talking2mouth "{size=30}Hm... she seems to be pretty focused on her routine. Should we wait...?{/size}"

            serena @closedbrow talkingmouth "{size=30}How considerate. Yes, let's.{/size}"

            pause 1.0

            show dawn neutralbrow with Dissolve(2.0)

            pause 0.5

            show dawn surprisedbrow frownmouth with vpunch

            if (GetRelationshipRank("Dawn") < 2):
                dawn @surprisedbrow talking2mouth "Hi, welcome to the Contest Coliseum, I'm not scared, nice to meet you again!"

            else:
                dawn @surprisedbrow talking2mouth "Hi! [first_name], Serena--hi! I'm not scared!"

            show dawn:
                xpos 0.5
                ease 0.5 xpos 0.33

            show serena with dis:
                xpos 0.66 xzoom -1

            serena @talkingmouth "Naturally. You look effortlessly graceful, incidentally, Dawn. I do hope someone's told you today."

            dawn -surprisedbrow @sadbrow talkingmouth "{size=30}It actually takes a lot of effort...{/size}"

            serena @talkingmouth "May I trouble you to answer a couple of questions? It's for a personal quiz, of sorts. A compatibility tester, if you will."

            dawn @sadbrow talkingmouth "Um... sure. Who am I testing my compatibility with...?"

            if (GetRelationshipRank("Dawn") > 3):
                show dawn lightblush sad2eyes with dis

                narrator "Dawn's eyes quickly flick over to meet yours..."

                show dawn -lightblush -sad2eyes with dis

                narrator "...Then, just as quickly, flick away."

            serena @talking2mouth "Oh. Well... Calem, actually. Calem Xavier."

            show dawn lightblush surprisedbrow frownmouth with dis

            dawn @talkingmouth "Calem...?"

            serena @talking2mouth "Do you have thoughts on this?"

            dawn -lightblush -surprisedbrow @sadbrow talkingmouth "{size=30}Mostly just wondering why you're testing my compatibility with Calem...{/size}"
            dawn @talkingmouth "N-not really, no."

            serena @talkingmouth "Splendid. Well, before we get into the proper meat and potatoes of the questions, why don't you just tell me a bit about Calem? Or, rather, what you think of him?"

            dawn sad2eyes frownmouth @talking2mouth "Um... he's... cool."

            pause 1.0

            serena @surprisedbrow talkingmouth "Is that all?"

            dawn sad2eyes @talking2mouth "Well, I... I really appreciate everything he did for the Coordinator Club. I feel like him recruiting Lisia put me on a new path for life."
            dawn -sad2eyes @talking2mouth "And he's so earnest and passionate in our Fairy-type class. He doesn't get the fashion stuff Instructor Valerie is always saying, but he works so hard to understand, anyway."
            
            show serena frownmouth with dis
            
            dawn @talkingmouth "And he's great with Wally. Whenever Wally seems confused, or struggles with something, Calem helps him out, and he's so patient and kind with him."
            dawn @happybrow talkingmouth "And he's super smart, but also really sensitive and he actually gets art, and we can talk about Sinnohan painters together, which I can't do with anyone else!"
            dawn surprisedbrow frownmouth @happy "And he shows up all the time to the contests to support you, so he's clearly a great friend, and his silver hair makes him look very distinguished, and he--"

            pause 1.0

            dawn @bamboozledeyes sadeyebrows lightblush talking2mouth "Ahhhh! No, I didn't say any of that! Don't tell him I said that--don't even remember, please!"
            dawn @bamboozled2eyes sadeyebrows lightblush talking2mouth "He'd probably think I was a weirdo, and it kinda sounds like I've been watching him, but I swear I haven't, but I mean, I'm not ignoring him, either, it's just that--"

            serena @talking2mouth "It's fine."

            dawn surprisedbrow @sadbrow talkingmouth "[ellipses]Huh?"

            serena @talking2mouth "I don't think there's any reason to continue asking questions on this theme. It seems pretty clear that the two of you are wholly incompatible."

            dawn @talking2mouth "Oh. Oh, well... okay. That's, um, good. I guess."

            serena @closedbrow talking2mouth "Yes."

            pause 1.0

            dawn @talking2mouth "Okay."
            
            pause 1.0

            serena @talking2mouth "Okay."

            pause 2.0

            dawn @talkingmouth "I'm going to go die now."

            serena @talking2mouth "Okay."

            red @sweat talking2mouth "No, that's not okay. Dawn, you don't need to die."

            show dawn:
                xpos 0.33
                ease 5.0 xpos 0.1 rotate -30 ypos 2.0

            pause 2.0

            dawn @sadbrow talkingmouth "{size=30}Maybe I'll just go back to the vase again... It was nice in there. Dark.{/size}"

            pause 2.0

            red @confused "C'mon. What was that?"

            serena @closedbrow talking2mouth "It's nothing, just... I think we've been going about this the wrong way."

            redmind @sadbrow frownmouth "It sounded to me like you realized that Dawn was getting a bit too close to an actual solution to your problem, and you didn't actually want one..."

            red @sweat closedbrow talking2mouth "Fine. Who's next on the list?"

    else:
        red @talkingmouth "Sure. Who's next on the list?"

    show serena:
        ease 0.5 xpos 0.5

    serena @closedbrow talking2mouth "I think, perhaps, the list is not giving us what we want."

    red @upeyes talking2mouth angryeyebrows "Okay. So what do we {i}want{/i}?"

    serena @sadbrow talkingmouth "...Truthfully? I am not sure I can bear the thought of Calem with another woman after all."

    red @happy "Well, at least we're being honest, now. So--"

    serena @closedbrow talking2mouth "So men it is."

    red @unamusedbrow unamusedmouth "[ellipses]"
    red @sadbrow talking2mouth "Serena, I'm begging you, don't make us go through this, but with men, this time."

    serena @closedbrow talking2mouth "I don't believe that'll be necessary. There is one person who requires no interview to pass muster."
    serena @closedbrow talkingmouth "I speak, of course, of you."

    menu:
        "I would very much rather not.":
            $ HasEvent("Serena", "RejectCalemDate")
            
            red @talking2mouth "I'm not dating Calem so you can convince yourself that {i}you{/i} don't want to date him, Serena."
            red @sadbrow talkingmouth "He's a great guy. Considerate and witty. But this is weird, and I think you know, deep down, it's weird."
            
            serena @talkingmouth "Don't worry about a thing. I'll set everything in motion."

            red @confused "I feel like I'm being ignored."

            serena @closedbrow talkingmouth "I assure you, dear [first_name], this development is mandatorily important for the success of this little caper."
            
            redmind @unamusedbrow unamusedmouth "I am {i}definitely{/i} being ignored."

        "Flattered. Sure.":
            $ HasEvent("Serena", "AcceptCalemDate")

        "This is so stupid.":
            $ HasEvent("Serena", "StupidCalemDate")

            serena @angrybrow talkingmouth "Stupid? Or original?"

            red @unamusedbrow talking2mouth "Definitely stupid."

            show serena angrybrow poutmouth with dis

            $ ValueChange("Serena", -1)

            serena @talking2mouth "I am sure they said the same thing to the man who first proposed a heliocentric galaxy."

            red @talking2mouth "I'm not dating Calem so you can convince yourself that {i}you{/i} don't want to date him, Serena."
            red @sadbrow talkingmouth "He's a great guy. Considerate and witty. But this is weird, and I think you know, deep down, it's weird."
            
            serena -angrybrow -poutmouth @talkingmouth "Don't worry about a thing. I'll set everything in motion."

            red @confused "I feel like I'm being ignored."

            serena @closedbrow talkingmouth "I assure you, dear [first_name], this development is mandatorily important for the success of this little caper."

            redmind @unamusedbrow unamusedmouth "I am {i}definitely{/i} being ignored."
    
    serena @happy "Oh, how funny it is, to look back on these events now. I suspected some sort of great machination was required to resolve this, but the [bluecolor]solution{/color} was right in front of me, the whole time!"

    red @unamusedbrow talking2mouth "Yeah. Great."

    serena @closedbrow talking2mouth "Of course, this will result in {i}both{/i} of you being tied up together. This leaves little but scraps for myself, but I suppose that's the lot I've signed up for."
    serena @sadbrow talkingmouth "And as long as you two are happy, I am certain I will be, too."
    serena surprisedbrow frownmouth @talkingmouth "I'll give you a call, shortly, with further details. Allow me to--"

    $ Pokemon("Zorua").PlayCry()

    pause 2.0

    serena @talkingmouth "Pardon. Was that..."
    serena @happy "Oh, that's a gee-darn Zorua! Those sumbitches are rare as hell, even out here, all cozy-up with Unova. I gotta snag it!"
    $ houndourname = GetTrainerTeam("Serena", "Houndour").GetNickname()
    serena angrybrow happymouth "We'll talk later, [first_name]! Get the lead out, [houndourname], we're goin' fox-huntin'!"

    show serena:
        xpos 0.5
        ease 0.7 xpos 0.4
        ease 0.3 xpos 1.1

    pause 2.0

    red @unamusedbrow unamusedmouth "[ellipses]"

    redmind @closedbrow frownmouth "She better not have forgotten about those Rhyhorn Race tickets she owes me."

    $ RelationshipRankUp("Serena", "Solution")

    return