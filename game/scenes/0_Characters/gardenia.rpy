label Gardenia1:
    $ AddEvent("Gardenia", "Gardenia1")

    scene city_B
    with Dissolve(2.0)
    $ renpy.music.queue("Audio/Music/inspira_Start.ogg", channel='music', loop=None, fadein=0.0, tight=None)
    $ renpy.music.queue("Audio/Music/inspira_Loop.ogg", channel='music', loop=True, tight=None)

    redmind @thonk "[ellipses]Where[ellipses]?"
    redmind @surprisedbrow frownmouth "Oh, there it is! That must be the place, right?"

    narrator "You're looking up at a square building with glass windows. On a sign above the door is the name 'Natane Eternal Yoga.'"
    narrator "Inside, through the large glass windows facing the street, you can see several people in tight clothing stretching, a few large rubber balls on the floor, and brightly-colored mats everywhere."

    redmind "Well, I'm not sure I've ever {i}seen{/i} a yoga class before, but if I had to describe one, it'd probably be something like this."

    pause 1.0

    redmind @surprisedbrow frownmouth "[ellipses]"
    redmind @sad2eyes poutmouth lightblush "Lotsa butts."

    pause 1.0

    red @closedbrow talking2mouth "Alright, you're being weird now. Just go on in."

    stop music fadeout 3.0

    scene blank with splitfade

    pause 1.0

    scene blank2 with splitfade

    scene yogastudio with splitfade

    queue music "audio/music/gardeniabusiness.ogg" fadein 1.0

    $ renpy.music.play("Audio/school_crowd.ogg", channel='crowd', loop=True, fadein=10.0, relative_volume=0.3)

    red @happy "Hey! Is this, like, a walk-in thing, or should I have made an appointment?"

    show brendan casual surprisedbrow frownmouth with dis:
        xzoom -1

    brendan @talking2mouth "Bro?"

    red @surprisedbrow talkingmouth "Brendan? Hey, man. Is this the right place? Gardenia runs this place, right?"

    brendan -frownmouth -surprisedbrow @talkingmouth "Oh, yeah! Yeah, I think she mentioned that she had been trying to get you to sign up."

    red @happy "Wait, do you mean you {i}work{/i} here?"

    brendan @happy "Kinda, yeah! Gardenia noticed me in Grass class and, uh, hired me to teach here."

    red @confusedbrow talkingmouth "No kidding? You've done something like this before?"

    brendan @talking2mouth "Well, you gotta be loose if you don't want to sprain something in a Contest Performance. You're always twisting your arms and waist around in ways you wouldn't normally, so, yeah, yoga's a good way of staying flexible offstage."

    red @talkingmouth "Cool. Sounds like you know what you're doing here."

    brendan @closedbrow talking2mouth sweat "{size=30}Yeah, well...{/size}"

    brendan @happy "Hey, girls, you've done great! Caroline, remember to lift with your upper arms. Jenna, nice form, you've improved a ton since last time. Keep it up!"
    
    if (GetNature("Brendan") == TrainerNature.Moody):
        brendan sadbrow @talkingmouth "Looks like we went overtime a bit, so I should wrap it up now. If you need anything, I'll be chatting with this guy here."
    else:
        brendan sadbrow @talkingmouth "Looks like we went overtime a bit, so I should wrap it up now. If you need anything, I'll be chatting with my friend here."

    $ PlaySound("Complaining.ogg")

    pause 1.5

    brendan @talkingmouth "Yeah, yeah, I know, girls. But Gardenia pays me for ninety minutes. I can't keep going over just 'cause I like you all."
    brendan @happy "I'll see you next week. Same time, right? Remember to work on your {i}bhujangasanas{/i} at home!"

    stop music channel "crowd" fadeout 3.0

    narrator "The yoga class disperses, though you notice several of the classmembers linger behind around Brendan, throwing nasty looks at you, as though you're, somehow, in their way."

    pause 1.0

    brendan -sadbrow @closedbrow sweat talking2mouth "Sheesh. Scary stuff."

    red @confused "Scary? From where I was standing, kinda looked like a man's paradise."

    brendan @surprisedbrow talking2mouth "What? What do you--"
    brendan @happy "Oh, bro, I get it, but you got it wrong. The girls aren't scary. They're great. Great students, really pay attention to everything I'm saying, do the poses fine after I show 'em once or twice."
    brendan @closedbrow sweat talking2mouth "Nah, man, Gardenia is the scary one."
    brendan @talking2mouth closedbrow sweat "She hired me, and she pays great, but it's like she always knows exactly what I'm going to do."
    brendan @talking2mouth "Like, I mentioned the overtime, and how Gardenia doesn't pay me for that, right?"

    red @talking2mouth "Yeah."

    brendan @closedbrow sweat talkingmouth "I keep tryin' not to do it, to pull out when my phone goes off, but there's always one thing or another keepin' me here. And the weird part is, it's like Gardenia already knows."
    brendan @talking2mouth "She schedules her next classes around whenever I {i}actually{/i} end my classes. Even though I don't even know when it is, there's always a new class lined up right after."
    
    $ renpy.music.play("Audio/school_crowd.ogg", channel='crowd', loop=True, fadein=10.0, relative_volume=0.3)

    narrator "You look at the entrance to the studio--true to his words, a new group of spandex-clad students are filing in. This group, you notice, has significantly more men amongst it..."

    brendan @closedbrow talking2mouth "And, like, when she hired me, she didn't even have the students for my class signed up." 
    brendan @surprisedbrow talking2mouth "Then we did one class--just one, where it was her runnin' a class for me--and suddenly the next day, we got, like, twenty-five signups from people all asking for me specifically."

    red @confused "Huh. Was this one one-on-one class held here?"

    brendan @talkingmouth "Yeah."

    narrator "Brendan points at an area in front of the big window, which would be very visible from the street. You suddenly get an idea of how recruitment might have increased so rapidly."

    brendan @closedbrow sweat talking2mouth "I think the AC was broken or something, because it was swelterin' in here. Since it was just the two of us, Gardenia said I could take my shirt off, but I was still sweatin' like a Meditite."
    brendan @talking2mouth "Course, before we could get started on the yoga, I had to move around a bunch of weights that were left around. Gardenia was goin' to do it herself, but I kinda volunteered--and she seemed to be expectin' that, too, so..."

    pause 1.0

    brendan @talkingmouth sadbrow "Man, am I making sense? I don't think I am. I'm havin' a great time here, the students are too, I just always feel like there's somethin' bigger goin' on than Gardenia lets me know."
    brendan @closedbrow talking2mouth "Maybe that's just what it's like, bein' part of a business. Only time I worked before was in a clothing store."

    $ ValueChange("Brendan", 3)

    narrator "Your understanding of Brendan has increased, though it is clear his understanding of his current situation may not be entirely[ellipses] 'comprehensive.'"

    brendan @talkingmouth "But I guess that's enough of me chatting. You wanted to sign up for a class here?"

    red @talkingmouth "Mostly just check it out, honestly. Gardenia's been trying to get me involved for a long time--I thought I should at least give it a shot."

    brendan @talking2mouth "Well, Gardenia's not here, but Lindsay is teaching the class after mine. You could ask her if there's room."

    red @confused "Wait, Gardenia's not here?"

    brendan @talking2mouth "Uh, no. She's the owner of the company. The owner doesn't, like, teach classes."

    red @closedbrow talking2mouth "Huh. I guess that makes sense, but Gardenia's always seemed to have a very hands-on approach to her business--"

    show brendan surprisedbrow frownmouth with dis:
        xpos 0.5 xzoom -1
        ease 0.5 xpos 0.66 xzoom 1

    show gardenia yoga behind brendan:
        xpos 1.2 ypos 1.0
        parallel:
            easein 0.3 ypos 0.7
            easeout 0.3 ypos 1.0
        parallel:
            ease 0.3 xpos 0.25
            ease 0.5 xpos 0.33
        parallel:
            pause 0.3
            ease 0.5 xzoom -1

    gardenia @happy "And that's my cue! Hey, [first_name], Brendan."

    brendan @talkingmouth "Woah, boss! You're going to be teaching today?"

    gardenia @talkingmouth "Lindsay's using up her PTO before it resets. I could get Angela to cover for her, but since I knew [first_name] here was {i}finally{/i} going to take me up on my offer, I figured I might as well run this session myself."

    brendan -surprisedbrow -frownmouth @happy "Awesome!"
    brendan @sadbrow talkingmouth "Man, I really wish I could join, but I'm kinda sore from my class..."

    gardenia @talkingmouth "Oh, yeah, don't worry about it, Brendan. You don't want to strain yourself. That'd ruin the entire point of yoga, right?"

    brendan @talkingmouth "Right."

    gardenia @rollbrow talkingmouth "Besides, you kinda intimidate Lindsay's students."

    brendan @closedbrow talkingmouth "Yeah, not a lot of my body type in these classes. I'll make myself scarce."
    brendan @talkingmouth "Hey, see you in Grass class later, right?"

    gardenia @happy "Yeah, see you then!"

    hide brendan with dis

    pause 1.0

    show gardenia:
        xpos 0.33 
        ease 0.5 xpos 0.5

    gardenia surprisedbrow frownmouth @happy "So, [first_name], how are you--"

    red @unamusedbrow talking2mouth "How could you possibly know I was going to visit your yoga studio today, specifically?"

    gardenia -surprisedbrow -frownmouth @flirtbrow talkingmouth "Advertising, partner!"
    gardenia @talkingmouth "You get out what you put in, and I've put a lot into you."

    red @closedbrow talking2mouth "How do you figure? You've asked me to sell you stuff, give you money, and bank my money with you."

    show gardenia blush lipbitemouth flirtbrow with dis

    red @unamusedbrow talking2mouth "Kinda feels like I'm the one putting stuff into you."

    pause 2.0

    show gardenia happybrow smirkmouth with dis

    red @upeyes angryeyebrows talking2mouth "Oh, come on, you know what I meant!"

    gardenia -happybrow -smirkmouth -blush @talkingmouth "Yeah, I do. But I'm not sure you know what {i}I{/i} meant. Why don't you stick around after the class for a chat?"

    red @sadbrow talkingmouth "Well, I'm not here {i}just{/i} to do some upward orangutans, or whatever they're called. Is Lindsay's class a beginner's class?"

    gardenia @happy "Great for newcomers and veterans alike. Bring your kids! Bring your polycule! Great date night option, too."

    red @sweat talkingmouth "Hey, you don't have to sell me on it! I'm already here."

    gardenia @talkingmouth "True. Oh, but there's one more thing--I'm guessing you don't have any actual yoga clothes on under that outfit?"

    red @talking2mouth "Sorry, no."

    gardenia @talking2mouth sad2brow "Well, I guess you'll just have to take your shirt off, then. I've got some yoga pants in the back you can borrow."

    red @talkingmouth "Sorry. If you want to use me as a billboard, like you did for Brendan, you'll have to pay me. I--"

    gardenia @talking2mouth "Yeah, okay."

    pause 1.0

    if (GetRelationshipRank("Grusha") > 0):
        red @confused "{i}¿Qué?{/i}"
        
    elif (GetRelationshipRank("Serena") > 1 or GetRelationshipRank("Calem") > 0):
        red @confused "{i}Quoi?{/i}"

    elif (GetRelationshipRank("Tia") > 1):
        red @confused "[tiafont]What{/font}?"

    else:
        $ autoquote = False
        red @confused "\"What?\"\n\n{b}TL Note: This was said in English.{/b}"
        $ autoquote = True

    gardenia @surprisedbrow talking2mouth "What?"

    if (GetRelationshipRank("Grusha") > 0):
        red @closedbrow sweat talking2mouth "Sorry, it means 'what.' Something I picked up from Grusha."

        gardenia @happy "Ooh, Mr. Worldwide! I wish I spoke another language--it'd really help when dealing with international clients."

    elif (GetRelationshipRank("Serena") > 1 and GetRelationshipRank("Calem") > 0):
        red @closedbrow sweat talking2mouth "Sorry, it means 'what.' Something I picked up from Serena and Calem."

        gardenia @happy "Ooh, Mr. Worldwide! I wish I spoke another language--it'd really help when dealing with international clients."

    elif (GetRelationshipRank("Serena") > 1):
        red @closedbrow sweat talking2mouth "Sorry, it means 'what.' Something I picked up from Serena."

        gardenia @happy "Ooh, Mr. Worldwide! I wish I spoke another language--it'd really help when dealing with international clients."

    elif (GetRelationshipRank("Calem") > 0):
        red @closedbrow sweat talking2mouth "Sorry, it means 'what.' Something I picked up from Calem."

        gardenia @happy "Ooh, Mr. Worldwide! I wish I spoke another language--it'd really help when dealing with international clients."

    elif (GetRelationshipRank("Tia") > 1):
        red @closedbrow sweat talking2mouth "Sorry, it means 'what.' Something I picked up from Bianca. Uh, Bianca Vongole."

        gardenia @happy "Oh, right, that finger-spelling language she knows, right? I wish I spoke another language--it'd really help when dealing with international clients."
    else:
        red @closedbrow sweat talking2mouth "Sorry, it means 'what.' Something I picked up from my Mom."
        
        gardenia @happy "Ooh, Mr. Worldwide! I wish I spoke another language--it'd really help when dealing with international clients."

    red @talkingmouth "Huh. Kinda surprised you don't, actually. Most people in Kobukan are at least conversational in Japanese and English."

    gardenia @sad2brow talkingmouth "Guess I just dropped the ball on that one."
    gardenia @talking2mouth "Anyway, yeah, I'll pay you. $500 to go shirtless for the class?"

    red @confused lightblush "Why does this feel like selling my body...?"

    gardenia @sadbrow talkingmouth "Partner, we {i}all{/i} sell our bodies in different ways." 
    gardenia @angrybrow talking2mouth "You know how many blue-collar workers cut pieces of themselves off? You know what sitting in a cubicle behind a desk every day for years does to a white-collar worker's heartrate?"
    gardenia @talkingmouth happybrow "After all, there's only three things you can sell in the world. Information, food, and bodies."
    gardenia @flirtbrow talkingmouth "You're a good-looking guy. Think about it. You get money, I get some advertising, you get to show off, I get some eye candy."
    gardenia @talkingmouth "It's a win-win-win."

    pause 1.5

    red @talking2mouth "Huh. So that's how you got Brendan to keep doing overtime for you."

    gardenia @talkingmouth "Go ahead?"

    red @talkingmouth "You set up a situation where he gets to teach a class for longer, which he enjoys, his students get to spend more time with him, which they enjoy, and you get more out of him than you're paying for, which you enjoy."

    gardenia @talkingmouth "Pretty much got it! That's the core of business--find the deal that makes the biggest profit."
    gardenia @sadbrow talking2mouth "But if the only profit you're looking for is money, well... that's just {i}unimaginative{/i}!"
    gardenia @talkingmouth "Profit can be all kinds of things. It can be happiness, it can be memories, it can be trust, it can be the promise of money later on."
    gardenia @talking2mouth sad2brow "Now, don't think I'm some kind of hippy antidisestablishmentarianist. I like money. I'm not going to start seizing the means of production anytime soon."
    gardenia @talkingmouth "But money's an end to {i}true{/i} profit. If the only profit you're pursuing is monetary, then you're picking up pennies--it's a waste of time."
    gardenia @happy "You know how I've succeeded in business? I can {i}always{/i} make an offer with every possible advantage to it. Sure, the other offer exists, but why would you ever pick it?"
    gardenia @talkingmouth "That's how I seem to know what people are going to do. I'm not a mind-reader, or anything. I'm just following the rule: if all the profit is on one option, people are {i}going{/i} to take that option."

    red @talking2mouth "That's an interesting way to think of it."

    gardenia @sad2brow talking2mouth "Some people think you have to be brutal, cutthroat, maybe even cruel, to survive in the marketplace, but..."
    gardenia @happy "Well, I think they're just losers who gave up too fast! Their way might be easier, but who cares how much you're making if you're hurting people?"

    red @talking2mouth "Huh."

    gardenia @talkingmouth "I don't just want my partners to buy what I'm selling. I want them to buy {i}into{/i} it. I want them to keep coming back. And they won't do that if I don't take care of them."
    gardenia @angrybrow talkingmouth "And right now, 'taking care of them' means getting that shirt off!"

    menu:
        "Sorry, pass. I'm not {i}that{/i} confident.":
            $ AddEvent("Gardenia", "ShirtedYoga")

            gardenia @surprisedbrow frownmouth "[ellipses]"
            gardenia @sad2brow talkingmouth "Well, I guess every rule has an exception."
            gardenia @sad2brow talkingmouth "Oh well. It was at least worth a shot. Still, take the best and jeans off. You'll sweat to death otherwise."

        "[courageoption]You're quite the salesman. You've convinced me.":
            $ TraitChange("Courage")

            $ AddEvent("Gardenia", "ShirtlessYoga")
            $ money += 500

            narrator "Gardenia hands you $500!"

            gardenia @happybrow talkingmouth "You know, you are {i}so{/i} fun to work with?"

            red @talkingmouth "Well, like you said. I want you to keep coming back."

            $ ValueChange("Gardenia", 3)

            gardenia @happy blush "I wish all board meetings were this fun!"

    red @talkingmouth "Alright. You mentioned something about yoga pants?"

    gardenia @talking2mouth "Yeah. They're in the changing room back there. Men's pile is on the left, you're probably a... XXL."

    red @confused "Ouch."

    gardenia @happy "It's a compliment, partner! You've got big glutes."

    red @happy "Guess that'd be the running. Alright, be right back."

    stop music channel "crowd" fadeout 3.0

    scene blank2 with splitfade

    narrator "You head to the changing room and change into your 'yoga outfit.'"
    narrator "The changing room, you notice, is decorated with pictures of spiralled white flowers with a golden tint at the center, somewhat hidden by the multiple overlapping layers of white."

    if (HasEvent("Gardenia", "ShirtlessYoga")):
        redmind swimsuithatless @thonk "Hm. White roses, maybe?"
    else:
        redmind hatless casual @thonk "Hm. White roses, maybe?"

    $ showredonly = True

    gardenia "Hey! [first_name], you almost done in there?"

    red @talkingmouth "Yeah, one sec!"
    
    $ renpy.music.play("Audio/school_crowd.ogg", channel='crowd', loop=True, fadein=3.0, relative_volume=0.3)

    scene yogastudio 
    show gardenia yoga
    with splitfade

    $ showredonly = False

    gardenia @talkingmouth "Nice, nice, looking good. Now, go to the back of the group, and we'll get this started."

    if (HasEvent("Gardenia", "ShirtlessYoga")):
        redmind swimsuithatless @thonk "The back of the group? Closest to the window..."
        redmind @sweat closedbrow "Well, she's doing exactly what she said she would."

    show gardenia:
        ypos 1.0 zoom 1.0
        ease 1.0 ypos 0.9 zoom 0.8
        block:
            pause 3.0
            ease 0.5 xpos 0.25
            ease 0.5 xzoom -1
            pause 1.0
            ease 1.0 xpos 0.75
            ease 0.5 xzoom 1
            pause 1.0
            ease 0.5 xpos 0.5 
            repeat

    gardenia @happy "Alright! Hey, everybody. I'm Gardenia, another instructor with this studio. Lindsay's taking some PTO right now, so I'll be taking over her class today."
    gardenia @talking2mouth "Now, let's get started with some gentle stretches, before we move onto the heavier stuff. Who's ready?"
    gardenia @talkingmouth "Lindsay showed you all the {i}balasana{/i}, right? We'll do a couple minutes of those before moving onto our {i}sirsasana{/i}."

    redmind @thonk "...Beginner-friendly, Gardenia?"

    gardenia @happy "[first_name], in the back, just copy what the people in front of you are doing. That's why I put you in the back."

    if (HasEvent("Gardenia", "ShirtlessYoga")):
        redmind @surprisedbrow frownmouth "Wait... she put me in the back so I could see what the other students are doing?"
        redmind @thinking "So it wasn't {i}just{/i} to have me closest to the window--it was also for my benefit."
        redmind @sadbrow "Damn. This girl's {i}really{/i} good at finding the deal that works for everyone."

    gardenia @talkingmouth "Alright, everyone, let's kneel. Close your eyes, and..."

    show blank2 with transeye

    pause 1.0

    narrator "You stretch your limbs in unfamiliar ways for ninety minutes. Though you were expecting to be sore by the end of it, it's actually pretty similar to the warmups you do before your runs."
    narrator "In fact, by the end of the lesson, you have a ton of energy left over."

    scene yogastudio 
    show gardenia yoga
    with splitfade

    stop music fadeout 3.0
    stop music channel "crowd" fadeout 10.0
    queue music "audio/music/gardeniachill.ogg"

    gardenia @talkingmouth "Phew! That's everything we've got time for today."
    gardenia @talking2mouth "Tips are appreciated, but not required. There's a box near the front, if you're interested."
    gardenia @happy "I probably won't see you all again, but Lindsay will--next week! See ya!"

    pause 2.0

    show gardenia sadbrow with dis

    pause 1.0

    if (HasEvent("Gardenia", "ShirtlessYoga")):
        red swimsuithatless @sadbrow talkingmouth "I guess you miss it?"
    else:
        red hatless @sadbrow talkingmouth "I guess you miss it?"

    gardenia @talkingmouth "Running the classes? A little bit. It's true what Brendan said. You can make money by working for it, but you make {i}a lot{/i} of money by making {i}other people{/i} work for it."
    gardenia @talkingmouth "I wish I had the time to handle more parts of my business personally nowadays. The banking/investment thing I'm doing at school takes the edge off, but it's not the same as putting in a hard day's work everyday."

    red @sadbrow talkingmouth "I've never had nearly enough money or responsibilities to begin to understand what you're talking about, but... I think I get it."

    gardenia -sadbrow @talkingmouth "You know, when I was a kid, I thought I might want to be a florist. Someone who gets their hands dirty every day, who gives people pretty things..."

    red @happy "No kidding?"

    gardenia surprisedbrow frownmouth @happy "I know! I don't look it, right?"

    red @talkingmouth "Oh, no, I wasn't surprised by that. I mean, you totally look it. You're wearing a flower-themed outfit right now."

    pause 1.0

    gardenia -surprisedbrow -frownmouth @talkingmouth "Oh. Yeah, I guess I am."

    red @talkingmouth "I was just surprised because it seems really... I dunno, simple, compared to the stuff you have going on."

    gardenia @talkingmouth sadbrow "That was the appeal, partner."

    red @talking2mouth "Well, how'd you go from Gardenia the florist to Gardenia the billionaire?"

    gardenia @frownmouth rollbrow "Hm[ellipses]"
    gardenia @talking2mouth "Well... the biggest thing was that I discovered I'm allergic to flowers."
    
    red @talking2mouth "Oof. Wait, aren't you named after a flower?"

    gardenia @sadbrow talkingmouth "The irony is {i}not{/i} lost on me, nor on my parents."
    gardenia @talking2mouth "Besides that, flower shops have an abysmal success rate. They need a ton of up-front funding to get started, and it takes a long time before they turn a profit. Almost as bad as restaurants, in that regard."
    gardenia @sadbrow talking2mouth "The kicker, though, is that forty-five percent of all flowers that go through flower shops die on the shelf, and have to get thrown away."
    gardenia @sad2brow talkingmouth "Call me softhearted, partner, but I couldn't live with that. I mean, that's such a painful visual metaphor, you know?"

    red @happy "Sounds bad, but you're the CEO of capitalism now, or something. I bet you can make it work."

    gardenia @talkingmouth "Oh, definitely. I've got a couple plans in mind, logistically. With significant startup funding, and plenty of Grass-type Pokémon around, I could pentuple the lifespan of my flowers."
    
    red @talkingmouth "Well, there we go."

    gardenia @sadbrow talkingmouth "Not that easy, partner. My money isn't liquid, and the money that {i}is{/i}, I can't be throwing around on private projects like this. Plus, I'd need a {i}lot{/i} of Grass-types. More than just one person could train."
    gardenia @sad2brow talkingmouth "Don't laugh, but I've kinda got this idea I might run a gym some day." 
    gardenia @talkingmouth "I mean, a Grass Gym would have a ton of Grass-types in it, and having the flower shop stationed in a gym would let me access league funding for expansion and development."
    gardenia @happybrow talkingmouth "{i}Plus{/i}, once the shop gets situated, the gym could actually turn a profit, which no gym {i}ever{/i} does, besides Galarian ones. So even the league would benefit." 
    gardenia @talkingmouth "I'd be able to hire Gym Trainers who are also florists, so I could help other people fulfill their dreams of working in a flower shop, too..."
    
    pause 1.0

    red @confused "I'm confused. What part of this is unreasonable? The way you said 'don't laugh', I thought this was going to be some kind of crazy fantasy, but it sounds really well-thought out. Like something everyone would profit from."
    
    gardenia @happy "I mean, it's {i}totally{/i} logistically sound. The only problem is I'd need to be a good enough trainer to get a Gym placement, which..."
    gardenia @annoyedbrow talking2mouth "Well, that's the problem with it."

    red @happy "C'mon, I'm sure you're a good trainer."

    gardenia @talkingmouth "Good, sure. But 'good' doesn't cut it in the Sinnoh League. I mean, that's Instructrice Fantina's league. That's {i}Cynthia's{/i} league."
    gardenia @sad2brow talkingmouth "I could have all the money in the world, but if I can't battle to impress Cynthia, then I'm not getting a Gym membership."
    gardenia @annoyedbrow talking2mouth "Ironically, ownership of the gym in my hometown is currently being fought over in a bidding war between Rad Rickshaw, the owner of the local cycle shop, and Ms. Jupiter, a representative of the Team Galactic Energy Company."

    pause 1.0

    red @confused "Why's that ironic?"

    gardenia @happy "Because I could easily outbid both of them!"
    gardenia @sadbrow talkingmouth "I just can't... {i}outbattle{/i} them."

    red @talking2mouth "Hm. Okay, I think I know what we can do about this."

    gardenia @surprisedbrow talkingmouth "Yeah?"

    red @happy "Well, I'm a Battle Team member, so[ellipses]"

    show gardenia flirtbrow with dis

    red @frownmouth "[ellipses]"

    pause 1.0

    red @unamusedbrow talking2mouth "This was your plan all along, wasn't it?"

    gardenia -flirtbrow @talkingmouth "Sorry, [first_name]. I love your company, seriously, partner, but I need training, and I need training fast."

    red @closedbrow talking2mouth "Firstly, I'll do it, no conditions. But I gotta ask--you're in Kobukan. Can't your instructors help you?"

    gardenia @sad2brow frownmouth "[ellipses]{nw}"
    extend @sad2brow talking2mouth "Well, yeah, and they do. But {i}everyone{/i} at this school is getting training from their instructors, and not everyone becomes Gym Leader-level."

    red @talking2mouth "I guess."

    gardenia @sad2brow talkingmouth "And, uh... I like Instructrice Fantina a lot, and she's a good teacher, but... I just can't... uh, that class, it's..."
    gardenia @talking2mouth "Well, I'm in that class 'cause I need to be. It's a sort of 'know your enemy' situation. I can get along just fine with my Grass-types."
    gardenia @annoyedbrow talking2mouth "...Though Ms. Jupiter uses a Skuntank, and Rad Rickshaw has a Clefairy that knows Fire Blast, for some reason."

    red @talking2mouth "Sorry, 'know your enemy'? Do you have something against Instructrice Fantina?"

    gardenia @happy "No, no! Nothing against her. It's, um, ghosts... mostly. Kinda."
    gardenia @sadbrow talkingmouth "It's... kinda a long story."

    red @talking2mouth "I've got nowhere to be."

    gardenia @happy "Sorry, but I {i}do{/i}! Gotta talk with Skyla about shipping some stuff in her plane. We'll chat later, okay?"

    red @talking2mouth "Alright. Where do you want to meet up?"

    gardenia @talkingmouth "Hm... how about the fields? It's a nice, easy, open location for training. Just text me whenever you're free, and I'll tell you if I have time to meet you there."

    red @talking2mouth "Alright, sure. Good talking with you."

    gardenia @happy "Same to you, partner!"

    red @talkingmouth "I liked this class. Not sure I'm going to make it a recurring thing--I'm pretty busy--but it was fun to drop in."

    gardenia @talkingmouth "'Course, totally get it. Just don't forget to text me later about the training."

    red @happy "Won't forget, partner. Seeya later."

    scene blank2 with splitfade

    if (money >= 100):
        narrator "You get changed and prepare to leave the studio. As you walk through the door, you notice a small wooden box with a slot in it..."

        menu:
            ">Tip $100":
                $ money -= 100
                $ ValueChange("Gardenia", 1)

            ">Do not tip":
                pass

    else:
        narrator "You get changed and leave the studio, heading back to campus."

    narrator "You have made plans to meet up with Gardenia later! [bluecolor]When you have free time, you should go to the fields for some special training.{/color}"

    return

label Gardenia1Part2:
    narrator "You text Gardenia, and meet up with her in the fields..."

    $ AddEvent("Gardenia", "Gardenia1Part2")
    stop music fadeout 1.5
    $ renpy.music.queue("audio/music/Fieldstheme_Start.ogg", channel='music', loop=None, fadein=1.0, tight=None)
    $ renpy.music.queue("audio/music/Fieldstheme_Loop.ogg", channel='music', loop=True)
    show clouds:
        yalign 0.5
    show fields1 :
        yalign 0.33 xalign 0.95
    with Dissolve(2.0)
    show gardenia with dis:
        xpos 0.5

    red @talkingmouth sweat "[ellipses]And that kinda fills out pretty much everything I can tell you about battling in one sitting. Man, I need some water."
    red @closedbrow talking2mouth "Man, my throat is sore. I don't normally talk this much for so long."

    gardenia @talkingmouth "Thought you might, so I came prepared. Here you go!"

    $ GetItem(Item.FreshWater, text="Gardenia tosses you a bottle of water. It slips through your hands and lands, perfectly, on its cap. You both pop off for a moment before agreeing further acknowledgement of that awesome feat would ruin it.")

    red @talkingmouth "So, the only thing left to do after this is a battle. See if you can put what I've said into practice. Let's make it a single battle."
    red @happy "Ready?"

    gardenia @angrybrow talkingmouth "Sure am! Let's go!"

    python:
        trainer1 = MakeRed()
        trainer2 = MakeTrainer("Gardenia")

    call Battle([trainer1, trainer2], customswitchbrain=gardeniafieldswitchbrain, dialogfunc=gardeniafielddialog) from _call_Battle_170
    $ RecordBattle("Gardenia1")

    show gardenia with dis

    if (not WonBattle("Gardenia1")):
        $ AddEvent("Gardenia", "LostFieldBattle")
        gardenia sadbrow frownmouth @surprisedbrow talkingmouth "...Oh. You know, uh, sometimes, when you make an investment, and, sometimes it doesn't, uh... quite turn out to be the thing you're investing in..."

        red @closedbrow talking2mouth "Geez, spare my feelings, why don't you?"

        gardenia @talkingmouth "I'm sorry, [first_name]. I really want to do this with you, but I don't have a lot of time. I think I need to find someone else for this."

        pause 1.0

        red @sad2eyes angryeyebrows talking2mouth "I tried, alright? I'm sorry it wasn't what you expected."

        gardenia @sadbrow frownmouth "[ellipses]{nw}"
        extend @sadbrow talking2mouth "Yeah. So am I. Sorry, partner."

        hide gardenia with dis

        pause 1.0

        narrator "Gardenia walks away embarrassedly."

        scene blank2 with Dissolve(2.0)

        narrator "Perhaps Gardenia wasn't really as peace-and-love as she purported to be. Perhaps she, like all capitalists, only saw you for the value you could provide."

        pause 1.0

        narrator "Or perhaps you disappointed her beyond recovery."

        $ partysize = IntToWord(len(GetTrainerTeam("Gardenia")) - 1).title()

        narrator "C'mon, man. [partysize] Pokémon. You only had to knock out [partysize.lower()]. She didn't use the Phantump. And she runs {i}mono-Grass{/i}. You {i}really{/i} couldn't make that happen for her?"

        $ PlaySound("sav.ogg")

        narrator "Your heart stagnates as you become certain your relationship with Gardenia '{color=#cf0000}will never change{/color}'."

        pause 1.0 

        narrator "If one can profit from things other than money, so, too, can one go bankrupt..."

        jump endofgardenia1part2

    queue music "audio/music/gardeniachill.ogg"

    $ ValueChange("Gardenia", 3)

    gardenia surprisedbrow frownmouth @happy "You're just too strong! What can I say? Well-battled, partner!"

    red @angryeyebrows talking2mouth "I'm not sure it was."

    gardenia -surprisedbrow @talkingmouth sadbrow "Uh... what do you mean?"

    red @confused "C'mon. You've got a level {i}eight{/i} Phantump. And you didn't even let me knock it out, you just forfeited."

    gardenia @talking2mouth sadbrow "I feel like you {i}wanting{/i} to KO a level eight Phantump is the bigger issue here."

    red @closedbrow talking2mouth "That's not the point."
    red @talking2mouth sadbrow "I've seen your Phantump before, and thought it was weird, but {i}this{/i} was a one-on-one battle, and I really got a good look at it. Even besides its low level, it's..."
    red @talking2mouth "Gardenia, I'm going to ask you straight-out--why aren't you training your Phantump?"

    gardenia @sad2brow talking2mouth "I, uh--"

    red @talking2mouth "I know you aren't. Please don't try to argue {i}that{/i} point. It gained a few levels, but barely any, {i}especially{/i} compared to your other Pokémon." 

    pause 1.0

    gardenia sadbrow @talking2mouth "I'm scared of it."

    red @talking2mouth "Thought so. Why didn't you ask for a new starter from Kobukan?"

    gardenia @rollbrow talking2mouth "Because who would take a girl scared of a Phantump seriously? They're adorable. I mean, creepy, yeah, but cute, too."
    gardenia @sad2brow talkingmouth "Besides, it's not like you can just ask for a new starter. Kobukan's been plopping random starter Pokémon on people for hundreds of years, and that strategy's never failed."
    gardenia @sadbrow talkingmouth "I mean, I signed up for the Grass {i}and{/i} Ghost electives. They gave me a Grass and Ghost-type. That's not a coincidence, right? Even if I picked out the Poké Ball from a random tray, something weird is going on here."

    red @talking2mouth "I... guess. Yeah, come to think of it, a {i}lot{/i} of people got Pokémon that fit the electives they signed up for."

    pause 1.0

    red @confused sweat "...Wait, literally everyone I know except Blue did. Am I missing something?"

    gardenia @sadbrow talkingmouth "Probably, but I'm just as in the dark about it as you are."

    red @closedbrow talking2mouth sweat "Well, whatever. That's not the point right now."
    red @sadbrow talkingmouth "Gardenia, I want to help you here. I want to train you up to be a great Gym Leader, so you can open your flower shop, and get your hands dirty every day giving people pretty things."
    red @talking2mouth "But it's gotta start with this Phantump. Why are you scared of him? You, yourself, said he's adorable, so I know it's not just his appearance."

    pause 1.0

    stop music fadeout 2.0

    gardenia sadbrow frownmouth "[ellipses]"
    gardenia talking2mouth "My uncle."

    call clearscreens() from _call_clearscreens_242
    scene blank2 with splitfade

    queue music "audio/music/Eterna_Start.ogg" noloop
    queue music "audio/music/Eterna_Loop.ogg"

    pause 1.0

    scene gardeniahouse
    show flashback
    with splitfade

    $ hideside = True

    gardeniadad "Here we are, Natane clan!"

    gardeniamom "Oh, how lovely! What a fantastic house! it's so big!"

    gardeniadad "Plenty of wildlife, plenty of trees, grass, plants... close to the Pokémon Gym, too, so when little Gardenia starts her challenge, she can start right next door!"

    gardenia "...I liked Jubilife. This place is so slow and boring..."

    gardeniauncle "Don't say that, kiddo! Slow and boring is the perfect canvas for us to make a killing. Besides, things are already speeding up. Did you hear Cynthia started her Gym Challenge here?"

    gardeniamom "Cynthia? Who's that? Is that one of your business partners?"

    gardeniauncle "Hah, not this one. Not yet, anyway. She's a really popular challenger for the Sinnoh League right now. She beat the local Gym Leader just a couple months ago, and she's already gotten five badges. She's facing Byron next!"

    gardeniadad "Oh, well, no-one's getting through the Iron Wall of Canalave. I'm sure she'll bounce right off of him, like so many others do."

    gardeniauncle "Maybe, but I've got an eye for talent, and this Cynthia girl's overflowing with it.{w=1.0} Just like little Gardenia here!"

    gardenia "..."

    gardeniauncle "C'mon, kiddo. Let's go check out the uptown--see what sorts of businesses are flourishing, and what Eterna Town needs."

    gardeniamom "There you go again, already thinking about how to make money..."

    gardeniauncle "Heh heh heh! I didn't hear you complaining when I helped you buy this house. Riverfront property, Nikki! That's not something that's easy to find, nevermind easy to buy."

    gardeniadad "Give your sister a break. You know we appreciate you entirely. I think what Nikki is trying to say is just that we don't want to live in this big house if it means you have to work so hard we never see you."

    gardeniauncle "Well, you're crap outta luck, then, because I already bought it, and unless you want to squat in that 'haunted' mansion in the forest, you aren't going to find a bigger one in Eterna! Heh heh heh!"

    gardeniamom "Oh, you're too much. Really, though, thank you. Both Nando and I {i}really{/i} appreciate what you've done for us."

    gardeniauncle "Good! 'Cause there's more coming. For now, though, I'm going to take my favorite niece for a ride around town. Maybe we'll check out that gym nearby."

    gardeniadad "Alright. Just make sure to bring her back before dark."

    gardeniauncle "You got it, Nando! {size=30}And, hey, when's dark, exactly...? I mean, that's relative--{/size}"

    scene blank2 with splitfade

    pause 1.0

    show oneyearlater at vspaz

    pause 3.5

    scene gardeniahouse2
    show flashback
    with splitfade
    
    gardeniadad "A new house?! It's even bigger than the last one--but--surely this was extremely expensive?!"

    gardeniauncle "Hey, Gardenia's a growing girl. She should have a growing house, too! Heh heh heh!"
    
    gardeniauncle "Besides, this house? Pocket change compared to the money I'm bringing in after the Galactic Energy deal."
    gardeniamom "You did it again! How much was that deal worth?"

    gardeniauncle "Heh heh heh! The {i}real{/i} value of the deal is in the contacts I made."

    gardeniamom "Isn't the real value of the deal in the happiness you gave people?"

    gardeniauncle "Sure, in a metaphorical sense. But I'm talking stacks on stacks on stacks. Galactic Energy is now the sole supplier of energy for all of Eterna, and I've got plans to spread their web to the surrounding areas, soon, too."
    gardeniauncle "Mark my words: Eterna Town won't be a town in a year. With the green I'm bringing in, we'll attract enough people to push us over the edge to 'city', and you know what that means--more federal funds!"

    gardeniadad "You are, as always, impressive. Though I worry some of the sleepy timelessness of Eterna may be lost in the shuffle..."

    gardeniauncle "Oh, don't worry about that. Honestly, this town could use a little less timelessness! Like that awful 'haunted' mansion in the forest! You know kids play there, and go missing?"

    gardeniamom "I'm sure that's just an urban legend."

    gardeniauncle "Maybe. I've heard about Drifloon south of Eterna Forest, but they shouldn't have gotten so far North..."
    gardeniauncle "Well, whether it's true or not, {i}someone{/i} should do something about it! I'd run for Mayor if I wouldn't have to divest from my businesses."
    gardeniauncle "Actually, hold that thought."

    scene blank2 with splitfade

    pause 1.0

    show oneyearlater at vspaz

    pause 3.5

    scene interviewerplace
    show flashback
    with splitfade

    TempCharacter("Interviewer Roxy") "So, you must be very proud! How do you feel, being the first mayor of Eterna City?"

    gardeniauncle "Like you said, Roxy, very proud."
    
    gardeniauncle "I'd like to thank my amazing sister, Nikki, and my favorite niece, Gardenia, there in the crowd. Couldn't have done this without their support."

    pause 1.0

    gardeniauncle "Heh heh heh! Just kidding ya, Nando. That's my Brother-In-Law, Roxy, yeah, over there, in the funny hat. Couldn't have done this without you, either. Thanks for helping me with the campaign funds. I'll pay you back, promise!"

    TempCharacter("Interviewer Roxy") "It seems family's very important to you."

    gardeniauncle "It's the most important thing, Roxy. And now, as Mayor, every Eterna Citizen is my family, and I'll take care of all of you."
    gardeniauncle "I've got a lot of plans for this city. We're not going to be a little rinky-dink that people pass through to get to Hearthome anymore." 
    gardeniauncle "Timelessness is so yesterday--we've gotta modernize! Build up our industry, our economy, our tourism, and make Eterna a place worth visiting!"
    gardeniauncle "Mark my words, in a year, Champion Cynthia will be visiting this place. In five? She'll probably be living here!"
    gardeniauncle "And the first part of that is tearing down that deathtrap in the forest. Every cent I've got left will go towards turning that place into firewood."
    gardeniauncle "Why haven't we done it yet? 'Nostalgia'? 'Afraid the ghosts will get us'? Hah! Funny how the ghosts all disappear when someone who isn't superstitious shows up!  No more of our kids are going to wander in there and disappear!"

    TempCharacter("Interviewer Roxy") "...Hm? Is that happening? We haven't reported anything about that. Have you heard anything like that, Oli?"

    narrator "The cameraman shakes his head and shrugs."

    gardeniauncle "Well... you know how it is. No-one's reporting it, but we all know it's happening. But no longer, under my watch!"

    gardeniamom "{size=30}Personally, I think he just has such a vendetta against that house because it's the biggest house in Eterna he can't buy...{/size}"

    gardeniauncle "Hey, I heard that! And I, uh[ellipses] well, maybe I have an ulterior motive. But, hey, every deal should accomplish two things, like I always say, right, Gardenia?"

    scene blank2 with splitfade

    pause 1.0

    show oneyearlater at vspaz

    pause 3.5

    scene gardeniahouse3
    show flashback
    with splitfade

    gardeniadad "...How does your brother keep finding bigger and bigger houses? He's not building new ones, is he?"

    gardeniamom "I can't begin to tell. I think we might want to talk with him about downsizing, though. Three moves in four years is a lot for Gardenia, and I'm worried it's putting pressure on her."

    gardeniadad "I must agree, sweetheart. I don't want to seem ungrateful, but we're reaching the point where we have to scream to be heard in any other room in this house." 
    gardeniadad "Gardenia disappears for hours, and when I call her, and she says she's in her bedroom, I have to ask which one, and which floor, too."

    gardeniamom "Well, my brother {i}does{/i} like to spoil us. I just wish he was around this massive house he bought more."

    gardeniadad "Some people are just workaholics. For all his admirable traits, your brother is {i}squarely{/i} in that camp."

    stop music fadeout 10.0

    pause 1.0

    $ PlaySound("knock.ogg")

    pause 1.0

    queue music "audio/music/hauntedchateau.ogg" fadein 30

    gardeniamom "Hm? A knock at the door?"

    gardeniadad "{size=30}Now, the question is {i}which one?{/i}{/size}"

    pause 2.0

    gardeniamom "Oh, hello! Jupiter, right? From city hall?"

    TempCharacter("Ms. Jupiter") "Yes, I'm the Mayor's secretary. We're afraid he's been missing for a couple days, and we were hoping you might know where he is."

    gardeniamom "[ellipses]Missing? Like, {i}gone{/i}, {i}missing{/i}?"

    TempCharacter("Ms. Jupiter") "Unfortunately. As the person in charge of keeping track of his whereabouts, and managing his schedule, I feel this lays squarely on me--but more important than assigning blame is locating him again."

    gardeniamom "O-of course. Well, I'm sure he'll be found soon enough. I'll call him on his mobile. I bet he just, um, perhaps, got distracted brokering a deal, and[ellipses] forgot to go to work[ellipses]"

    TempCharacter("Ms. Jupiter") "The Mayor has publically divested himself of all income besides his salary as Mayor. Unless he is engaged in illicit, hidden, business, I've no idea what sort of deal you may be referring to."

    gardeniamom "{size=30}It was just an idea.{/size}"

    TempCharacter("Ms. Jupiter") "The last time someone in the office saw him, he mentioned he was going to the mansion in Eterna Forest." 
    TempCharacter("Ms. Jupiter") "Naturally, we've already deployed the police force and asked the Gym Leader to scan the area. No signs yet, but we'll stay vigilant."

    gardeniadad "We'll keep an eye out, Ms. Jupiter. Thank you for letting us know."

    TempCharacter("Ms. Jupiter") "Please do. I will, in turn, let you know if any developments occur. Good day."

    scene blank2 with splitfade

    pause 1.0

    show oneyearlater at vspaz

    pause 3.5

    scene gardeniahouse3night
    show flashback
    with splitfade

    gardeniadad "Please, give us a little more time. We'll find the money. I promise we will, somehow."

    TempCharacter("Ms. Jupiter") "Mr. Natane, it is not my lenience to give. The bank wants you out of its house. I came to give you early warning, not to be bargained with."
    
    gardeniamom "But... the money {i}exists{/i}! We know it does, somewhere! My brother had it before he went missing, he knows the account--the codes--"

    TempCharacter("Ms. Jupiter") "The late Mayor--"
    
    gardeniamom "My brother is {i}not{/i} dead!"

    pause 1.0

    TempCharacter("Ms. Jupiter") "The {i}former{/i} Mayor's hypothetical possession of the funds he was using to pay for this house is of no account to the bank. He is no longer paying--and you are living in a house you have neither title to, nor ability to pay for, nor sell."
    TempCharacter("Ms. Jupiter") "You have done so for over a year. From a legal perspective, this is a criminal act."

    gardeniadad "What will we do? Gardenia is--she's just a girl. We have no other family to stay with."

    TempCharacter("Ms. Jupiter") "Perhaps, friends?"

    gardeniamom "[ellipses]Ms. Jupiter, we[ellipses]"
    
    TempCharacter("Ms. Jupiter") "Please."
    TempCharacter("Ms. Jupiter") "Please do not ask."
    TempCharacter("Ms. Jupiter") "I am--{i}was{/i} your brother's secretary, Mrs. Natane. An employee. The bond between he and I severed when he reneged on his contract. There was never a bond between you and I. Please do not make me be cruel."

    pause 1.0

    TempCharacter("Ms. Jupiter") "I believe there is a homeless shelter near the Condominiums."

    gardeniadad "We cannot go there. When my Brother-In-Law departed with our money, he took much of the city's, too." 
    gardeniadad "The homeless shelter is almost full to bursting with people that his act harmed. I fear what may happen to Gardenia if we were to go there."

    pause 2.0

    TempCharacter("Ms. Jupiter") "Then[ellipses] perhaps[ellipses] there is one more option. Just[ellipses] until you can get back on your feet."
    TempCharacter("Ms. Jupiter") "I was attempting on your behalf to see if squatter's rights applied in this case. They do not, but in the process, another possibility occurred to me. A place where they {i}would{/i}."

    gardenia "No."
    
    scene blank2 with splitfade

    pause 1.0

    gardenia "No!"

    scene hauntedmansion2 with Dissolve(1.0)
    
    gardenia "Not here!"

    scene hauntedmansion1 at night

    pause 0.1

    scene hauntedmansion2

    gardenia "Not here, {i}anywhere{/i} but here!" 

    scene hauntedmansion1 at night

    pause 0.1

    scene hauntedmansion2

    pause 1.0

    scene hauntedmansion1 at night

    pause 0.1

    scene hauntedmansion2
    
    gardenia "Not where the ghosts took him!"

    scene hauntedmansion1 at night with slowdis

    gardenia "Please, not here!{w=0.5} Anywhere but here!{w=0.5} I don't want to live here!{w=0.5}{nw}" 
    
    show hauntedmansion1 at night with vpunch

    extend " {i}PLEASE!{/i}"

    scene blank2 with splitfade

    stop music fadeout 1.5

    TempCharacter("???") "{size=30}Gardenia[ellipses]?{/size}"

    pause 0.5
    
    TempCharacter("???") "Gardenia[ellipses]?"

    pause 0.5
    
    $ hideside = False

    scene clouds:
        yalign 0.5
    show fields1 :
        yalign 0.33 xalign 0.95
    show gardenia surprisedbrow frownmouth tears 
    with vpunch

    red @angrybrow talking2mouth "Gardenia!"

    pause 1.0

    queue music "audio/music/gardeniachill.ogg" fadein 5.0

    show gardenia sad2brow with dis

    pause 3.0

    gardenia -sad2brow @sadbrow talking2mouth "[ellipses]I hated that house. I don't care if you don't believe me, because it's true--that house was full of ghosts."
    gardenia @angrybrow talking2mouth "And I don't just mean Ghost Pokémon! Actual, human, physical, ghosts! And they're the ones who took my uncle away!"
    gardenia @sadbrow talking2mouth "They'd show up as red eyes in paintings. Shadows would appear on the TVs. They threw china around the kitchen, then the next day, the china would be in one piece again, and the table was laid."
    gardenia angrybrow @angrybrow talking2mouth "My uncle made it his mission to kick the ghosts out of that house, and they took him for it. {i}That's{/i} what happened."

    narrator "Gardenia glares at you, daring you to contradict her. You have some doubts[ellipses]"
    narrator "But perhaps now's not the time."

    gardenia sadbrow @talking2mouth "I hated being homeless. It was uncomfortable. It was cold. It was scary. And it was {i}so{/i} embarrassing."
    gardenia @talking2mouth "I spent every second I could in the forest. I was more comfortable jumping out my bedroom window into the treetops outside than I was walking down the creaky stairs to the kitchen."
    gardenia @sad2brow talking2mouth "When I went to school, the other kids saw my ragged clothes, and my old shoes, and the dark circles under my eyes, and they whispered that {i}I{/i} was a ghost. That I was some kid who went into the mansion and got lost forever."
    gardenia @sadbrow talking2mouth "I know it's hard to believe. But it's true, I promise. That's why I hate ghosts. That's why I'm trying to get the Disciplinary Committee to clean Kobukan of ghosts."#FIX THIS: Adjust based on LoN storyline progress
    gardenia -tears @sad2brow talking2mouth "That's why I can't train Phantump, because... because every time I look at its empty, unblinking, red eyes... I remember the red eyes that would watch me from the mirrors in that awful mansion."

    pause 1.5

    red @sadbrow talking2mouth "I'm so sorry you had to live with that."

    gardenia @sadbrow talking2mouth "I bet you're probably the only one at Kobukan who can even halfway understand what it's like to be poor. We were only in that house for five years, but... it changed me. It changed my mom, it changed my Dad."
    gardenia @sadbrow talkingmouth "Our thermostats are never a degree hotter than they need to be. We have wallets bulging with coupons. Dinners are planned based on whatever ingredients expire soonest."
    gardenia @talking2mouth "I could outbid a large regional energy company in Sinnoh, and I still patch up my own clothes. My mom cuts my hair. We make bread out of old Nanab berries. This stuff stays with you."

    red @sadbrow talkingmouth "I get it. I really do."

    gardenia @sad2brow talking2mouth "I... I know it's not fair to Phantump that I'm not giving it the training my other Pokémon get. But it's not fair to {i}me{/i} that I got a Phantump in the first place!"

    red @talking2mouth "...I have a question. Just one. Why {i}did{/i} you sign up for the Ghost Elective, if you're so scared of them?"

    gardenia @talking2mouth "Well... like I said, it's a 'know your enemy' kind of thing. Most people attend Kobukan to learn the strengths of their Pokémon, but you can also take a class just to learn their weaknesses."
    gardenia @annoyedbrow talking2mouth "And once I know what the weaknesses of all these damn ghosts are, I'll finish my uncle's work, and... and bust 'em. Bag 'em, tag 'em, send them to the great beyond." 
    gardenia @rollbrow talking2mouth "Maybe even sell my services to other people who are dealing with a ghost problem."

    red @sadbrow talkingmouth "That plan doesn't seem super compatible with the Flower Shop/Gym idea."

    gardenia @sadbrow talking2mouth "I guess not. But this is something I {i}have{/i} to do. If I can clear out Kobukan, that'll be proof it can be done, at least."

    red @closedbrow talking2mouth "Well... I guess I just have to wish you luck."

    if (HasEvent("Cheren", "Cheren2Part2")):
        gardenia -frownmouth @sadbrow talkingmouth "Hey, you contribute, too. It's not {i}just{/i} luck you're giving me."

        red @talkingmouth sadbrow "True, I guess."
        
    red @closedbrow talking2mouth "We're definitely going to have to talk about your Phantump later, but I want to do some more research into Phantump first. I think I remember something about training them."

    gardenia sadbrow -frownmouth @sadbrow talkingmouth "Alright. Um[ellipses] Thanks for being cool while I trauma'd at you."

    red @sadbrow talkingmouth "Hey, you got to get a really unhappy memory off your chest, and I got to understand my friend better. That's profit for everyone."

    gardenia @sadbrow talkingmouth "You got it, partner. You know, you were a {i}great{/i} [bluecolor]investment{/color}."

    red @happy "I promise I've only just {i}started{/i} to pay off."

    hide gardenia with dis

    $ RelationshipRankUp("Gardenia", "Investment", 1)

    label endofgardenia1part2:

    return