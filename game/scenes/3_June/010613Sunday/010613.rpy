label day010613:

$ timeOfDay = "Morning"
call clearscreens() from _call_clearscreens_286
call calendar(1) from _call_calendar_66

python:
    calDate = calDate.replace(day=13, month=6, year=2004)
    HealParty()

    yellowin = False
    protagin = False
    klarain = False
    yellowpartnered = False
    klarapartnered = False
    yellowpath = False
    klarapath = False
    tryoutwinner = GetContestWinner("Millennium Drop Water Festival Contest Tryouts")
    if (tryoutwinner != None):#if false, you didn't participate
        winnername = tryoutwinner.GetName()

        #you are in if:
        # you got first place
        protagin = tryoutwinner.IsProtag()

        #yellow is in if:
        # you won with her as your partner
        # you didn't partner with her
        yellowpartnered = HasEvent("Yellow", "AcceptPartner")
        yellowin = tryoutwinner.IsProtag() and yellowpartnered or not yellowpartnered
        yellowpath = protagin and yellowpartnered

        #klara should be in if:
        # you won with her as your partner
        # you didn't partner with her
        klarapartnered = HasEvent("Klara", "AcceptPartner")
        klarain = tryoutwinner.IsProtag() and klarapartnered or not klarapartnered
        klarapath = protagin and klarapartnered
    else:
        yellowin = klarain = True

stop music fadeout 1.5
show screen songsplash("Pallet Town", "Zame")
queue music "audio/music/palletpiano.ogg"

pause 1.0

if (IsAfter(6, 6, 2004) and Item.FeebasEgg in inventory):
    call FeebasHatch() from _call_FeebasHatch

    scene blank2 with Dissolve(2.0)

    narrator "You attempt to go back to sleep[ellipses]"

red casual hatless @frownmouth closedbrow "[ellipses]Mmmrgh[ellipses]"

pause 0.5

$ PlaySound("pokemon/pikachu_norm3.ogg")

libpikachu talkingmouth "Pika."

red @angryeyebrows talking2mouth closedeyes "Five more minutes, [pika_name]. Just five more minutes."

pause 1.0

redmind @sad2eyes sadeyebrows "When did [pika_name] start being the more energetic one between the two of us?"

if (IsCoordinator()):
    redmind @sweat frownmouth closedbrow "In retrospect, staying up late and throwing a huge party right before the Millennium Drop wasn't my best idea."
    if (not protagin):
        redmind @upeyes frownmouth "Of course, it's not like I'm going to be participating[ellipses]"
        redmind @closedbrow "Ah, well. We gave it a good effort."
    elif (klarapath):
        redmind @upeyes frownmouth "Of course, I'm not sure I'm going to get to compete[ellipses] since Klara and I aren't really a thing anymore."
        redmind @closedbrow sweat "And even if I {i}am{/i} allowed to compete, all my practice was as part of a duo."
        redmind @closedbrow "Ah, well. We gave it a good effort."

    pause 0.5 

    red @talking2mouth closedbrow sweat "Alright, I'm getting up."

    scene bedroom:
        zoom 1.1 rotate 2 yalign 0.5 xalign 0.5
    show screen currentdate
    with transeye2

    pause 1.0

    show bedroom:
        ease 2.0 zoom 1.0 rotate 0

    if (protagin):
        redmind casual hatless @thinking "Let's see[ellipses] I've got some time before the Millennium Drop[ellipses] what should I do?"

    elif (yellowin):
        redmind casual hatless @thinking "Let's see[ellipses] I've got some time before Yellow heads off to the Millennium Drop. I want to be there for her, but I can probably get some stuff done before then. What should I do?"

    $ showredonly = True

    pause 1.0

    show bedroom:
        ease 0.5 zoom 1.5 xanchor 0.99 xpos 1.10

$ showredonly = True

ethan "{size=30}Hey, man! You awake in there?{/size}"

red casual hatless @talking2mouth sweat "As of a couple seconds ago."

ethan "{size=30}Cool. Want to do something?{/size}"

pause 0.5

red @talkingmouth "Do something? Sure. Let me just get dressed first."

ethan "{size=30}I dunno, I feel like that's going to {i}significantly{/i} limit the number of things we can do.{/size}"

show bedroom with vpunch

blue "Oh my {size=40}GOD!{/size} Could at least {i}one{/i} person in this dorm stop flirting with [first_name] for five seconds?!"

pause 0.5

yellow "{size=30}I don't flirt with him.{/size}"

blue "You don't count!"

pause 0.5

yellow "{size=30}{i}Why{/i} don't I count, Blue?{/size}"

blue "Because--like, you--because you {i}don't{/i} flirt! You just don't."

yellow "{size=30}I {i}could{/i}{/size}."

pause 1.0

ethan "{size=30}I'm trying to imagine this, and I'm just[ellipses] I'm just coming up blank.{/size}"

yellow "{size=30}[ellipses]H-Hey.{w=0.5} {cps=5}Big boy{/cps}[ellipses]{/size}"

pause 1.0

ethan "{size=30}Actually, yeah, that would work on me.{/size}"

blue "Ugh. When we were all working together on something, I almost forgot how much being around you three gives me a headache."

scene suite 
show blue og angrybrow frownmouth:
    xpos 0.25
show yellow neutralhairdown frownmouth:
    xzoom -1
show ethan:
    xpos 0.75
with splitfade

$ showredonly = False

red @talkingmouth "Hey, someone called?"

blue @closedbrow talking2mouth "And there's number two. When Leaf wakes up in three hours, the whole migraine gang will be here."

ethan @talkingmouth "Migraine gang? Makes us sound like a quirky miniboss squad in some sort of cyberpunk setting. I dig it."

yellow @talking2mouth "Leaf's actually already awake. She said she was going to Inspira early to pick something up."

red @talkingmouth "Huh. Any idea what it is? She mentioned, like, ten days ago, that she had a secret plan for you. I don't know if that's still on the table, given last week, but[ellipses] maybe?"

blue @talking2mouth "Probably something to thank us for busting our asses throwing that party."

ethan @talking2mouth "Leaf's kinda aggressively thankful. Group agreement to not get into an arms race of appreciation gifts?"

blue @closedbrow talkingmouth "Pfft. Don't need to tell {i}me{/i} twice. I'm never doing {i}anything{/i} for her again. Or {i}any{/i} of you winners, for that matter."

$ SmartMoveOut("Blue")

blue og @angrybrow "Smell ya later!"

pause 1.0

ethan @talkingmouth "You know, he used to call us losers. Now he calls us winners."
ethan @winkbrow talkingmouth "Obviously, he's being sarcastic, but, like, that's {i}something{/i}, right?"

pause 0.5

red @upeyes confusedeyebrows talking2mouth "Guess so."

pause 0.5

ethan @talking2mouth "Anyway. You were down to do something, right?"

red @talkingmouth "Yep."

if (yellowpath):
    red @talking2mouth "Let me just check with Yellow. Do you want to go over our routines one more time?"

    yellow -frownmouth @talkingmouth "I think I should probably just take a break. I haven't really been able to think about anything else but the Millennium Drop--at this point, I think I've done everything I can."

    red @happy "You haven't been able to think about anything else? Didn't you just spend the last week planning a big party?"

    yellow @closedbrow talkingmouth "That was a group effort. And[ellipses] a bit of a distraction."

    red @talkingmouth "Alright, fair enough."

ethan @talkingmouth "Cool. So, want to just get some breakfast? And, like, chat? About normal stuff."
ethan @talkingmouth "Feels like it's been a while since we've had the world slow down."

red @talking2mouth "No kidding."

if (yellowin and not protagin):
    ethan @talkingmouth "Hey, Yell'. Are you going to practice your routine for the contest?"

    yellow -frownmouth @talkingmouth "I think I should probably just take a break. I haven't really been able to think about anything else but the Millennium Drop--at this point, I think I've done everything I can."

    red @happy "You haven't been able to think about anything else? Didn't you just spend the last week planning a big party?"

    yellow @closedbrow talkingmouth "That was a group effort. And[ellipses] a bit of a distraction."

    red @talkingmouth "Alright, fair enough."

    ethan @talking2mouth "If you're not busy, then, want to come with us?"

else:
    ethan @talkingmouth "Yellow, want to come with us?"

$ MoveInSmart("Blue", 0.2)

show ethan surprisedbrow frownmouth with dis

yellow surprisedbrow frownmouth @talking2mouth neutralbrow "I--"

blue @talkingmouth "If she's not training for her contest, she's helping {i}me{/i} train."

pause 1.0

ethan unamusedbrow frownmouth @talking2mouth "Wow, Yellow. You're such a skilled ventriloquist--it sounded like your answer came from Blue's mouth."

yellow -surprisedbrow @sadbrow talkingmouth "I[ellipses] I {i}was{/i} actually planning on going with Blue."

ethan @talking2mouth sadbrow sweat "Alright, don't let me get in the way."
ethan -unamusedbrow -frownmouth @talkingmouth "See you later."

yellow @happy "Bye, Ethan!"

$ SmartMoveOut("Yellow")
$ SmartMoveOut("Blue")

pause 1.0

ethan frownmouth confusedbrow @talking2mouth "Do you think Yellow's, like, {i}into{/i} it?"

pause 0.5

red @confused "What?"

ethan @talking2mouth sweat closedbrow "Yeah, nevermind. Let's get breakfast."

scene blank2 with splitfade

pause 2.0

$ removestudents = ["Blue", "Yellow", "Ethan", "Leaf"]

narrator "You will have three time slots before the Millennium Drop to prepare. Make sure to use your time carefully! [bluecolor]After the third time slot, the Millennium Drop will begin immediately.{/color}"

call freeroam() from _call_freeroam_50

stop music fadeout 1.5
queue music "audio/music/ocean waltz_start.ogg" fadein 3.0 noloop
queue music "audio/music/ocean waltz_loop.ogg"

scene blank2 with splitfade

redmind @thinking "It's finally time[ellipses]"

if (IsCoordinator()):
    if (not protagin):
        redmind @sadeyebrows closedeyes "I might not have won, but I still want to see who {i}does{/i}."
    elif (klarapath):
        redmind @sadeyebrows closedeyes "Time to find out if I can compete in the Millennium Drop without the person I signed up with, that is."

elif (yellowin):
    redmind @happy "Time to see what Yellow can do."

scene concerthallstagemidnight with splitfade

stop music fadeout 3.33

pause 1.0

redmind night @confused "Huh?"

pause 0.5

redmind @thonk "Where {i}is{/i} everybody?"

$ MoveInSmart("leaf surprisedbrow frownmouth", maintain=True, atlist=[night])
$ MoveInSmart("yellow surprisedbrow frownmouth", atlist=[night])

red @talking2mouth "Hey, girls. Uh, do you have any idea what's happening? And where are Ethan and Blue?"

leaf @talking2mouth "The guys are up in the stands, but we're down here trying to figure out what's happening. Wasn't this place supposed to be holding its contest in, like, fifteen minutes? Where's the audience?"

if (yellowin):
    yellow @talking2mouth "We're[ellipses] {i}really{/i} behind schedule[ellipses] and where's Lisia?"

else: 
    yellow @talking2mouth "They're[ellipses] {i}really{/i} behind schedule[ellipses] and where's Lisia?"

$ MoveInSmart("phobos unamusedbrow frownmouth", atlist=[night])

pause 0.5

yellow @talking2mouth "Um, hel--"

show leaf angrybrow with dis

$ ShiftAlign("phobos", 0.5, [night])

stop music fadeout 1.5
queue music "audio/music/lawrencetheme_start.ogg" noloop
queue music "audio/music/lawrencetheme_loop.ogg"

phobos @talking2mouth upeyes unamusedeyebrows "Oh no, weren't you informed? I suppose it falls to me, so hard to find good help, et cetera, et cetera, et cetera."

show phobos:
    matrixcolor IdentityMatrix()

show contest_light:
    xcenter 0.5 ycenter 0.5 zoom 1.25

phobos @upeyes sadeyebrows talking2mouth "There has been[ellipses] an accident. Yes, a dear friend of the Waters family has just called Champion Wallace back to Hoenn, and so he must go. A shame, really, that he couldn't see the performance put on tonight."

pause 0.5

yellow angrybrow @sadbrow talking2mouth "Um. But Lisia--"

show leaf angrysmilemouth with dis

phobos @talking2mouth closedeyes angryeyebrows "You really must learn to stop interrupting me, it's incrediscribably discourteous." 
phobos @upeyes talking2mouth "As I was {i}going to{/i} say, Lisia must accompany her uncle in this matter--she was specifically requested."

hide contest_light 
show phobos at night
with Dissolve (1.333)

leaf @talking2mouth "How do you know this? How do you know {i}any{/i} of this?"

phobos @closedbrow talkingmouth "Ah, well, I'm a close personal friend of Champion Wallace. Men of such taste and elegance are simply drawn together."

if (ClassSceneSeen("Water", 10)):
    redmind @unamusedbrow unamusedmouth "I've been in enough of Instructor Wallace's classes to know that's bullshit."

show phobos surprisedbrow frownmouth with dis

yellow @talking2mouth "So there are only going to be two judges?"

pause 0.333

show leaf shadow with dis

phobos -surprisedbrow @angrybrow talking2mouth "Please think before you open your mouth. Two judges? What a repulsive thought. No, please be sensible, you can't run a contest with {i}two{/i} judges. We aren't going to toss out the rulebook for your convenience."

pause 0.333

show leaf surprisedbrow frownmouth -shadow
show yellow surprisedbrow frownmouth
with dis

phobos @talkingmouth "Fantina is also indisposed.{w=0.333} So we'll be running it with one."

pause 0.333

phobos @talkingmouth "Me, in case the implication wasn't clear."
phobos @closedbrow talking2mouth "Alas, as no audience is here, so many of the performers have dropped out, and I am feeling rather under the weather, I've decided to cancel the show."
phobos @closedbrow talking2mouth "A terrible shame, a crying shame, a shameful shame, surely."

pause 0.333

show yellow sadbrow frownmouth with dis

phobos @talking2mouth closedbrow sweat "Now, kindly conduct yourself out of here, if you please. There's no real need for anyone but me to be here anymore."

show phobos at night:
    ease 0.5 xpos 1.2

pause 0.5

hide phobos

stop music fadeout 1.5
queue music "audio/music/lament.ogg" fadein 3.0

$ LineUp(atlist=[night])

pause 0.5

hide contest_light with Dissolve(2.0)

if (HasEvent("Melody", "PhobosPrettyCool")):
    red @talking2mouth "About three weeks ago, I said I thought Phobos was 'pretty cool.'"
    red @sadbrow talking2mouth "I have never been so wrong about something in my life."

elif (HasEvent("Melody", "PhobosNotSure")):
    red @talking2mouth "About three weeks ago, I said I didn't know how I felt about Phobos."
    red @sadbrow talking2mouth "I know how I feel, now."

elif (HasEvent("Melody", "PhobosDick")):
    red @talking2mouth "About three weeks ago, I said I thought Phobos was 'a bit of a dick.'"
    red @sadbrow talking2mouth "I don't think I have ever understated something more."

else:
    $ ReportRequest()

leaf angrybrow @talking2mouth "See, {i}this{/i} is why I hate contests. You don't get anything like this with battles. It's just about who can hit harder, not about whose friends with whoever's cousin's former roommate."

yellow @sadbrow frownmouth "[ellipses]"

show leaf sadbrow frownmouth with dis

red night @sadeyebrows sad2eyes talking2mouth "Leaf, I know you're trying to help, but[ellipses]"

pause 1.0

if (protagin and yellowin):
    leaf @talking2mouth "I'm sorry, you guys. I know you were really looking forward to this."

elif (protagin):
    leaf @talking2mouth "I'm sorry, [first_name]. I know you were really looking forward to this."

elif (yellowin):
    leaf @talking2mouth "I'm sorry, Yellow. I know you were really looking forward to this."

else:
    leaf @talking2mouth "I'm sorry, you guys. I know you were really looking forward to this."

if (HasEvent("Game", "Contest3")):
    red @talking2mouth "After watching what Phobos has been doing all week--trying to push people out of the contest--I probably should've expected he'd pull something like this."
    red @sadbrow talkingmouth "But, man, pushing the {i}judges{/i} out? How low can you go? I thought he was just going to try and rig it for Melody to win."

elif (HasEvent("Game", "Contest2")):
    red @talking2mouth "I saw him trying to push other coordinators out earlier this week, but[ellipses] I didn't think he'd go this far."
    red @sadbrow talkingmouth "Man, pushing the {i}judges{/i} out? How low can you go? I thought he was just going to try and rig it for Melody to win."

else:
    red @angrybrow talking2mouth "I can't believe he'd go so far as to push the judges out. When they realize what he did, they'll be furious, but I guess he doesn't care about that."
    red @closedbrow talking2mouth "I thought he was just going to try and rig it for Melody to win."

pause 1.0

$ MoveInSmart("melody on sadbrow sadmouth", atlist=[night])

pause 1.0

leaf angrybrow frownmouth @talking2mouth "Speak of the devil."

pause 0.5

melody @talking2mouth "I didn't want this."

pause 0.5

melody @angrybrow talking2mouth "I didn't {i}need{/i} this."

yellow @talkingmouth sadbrow "But you benefit, right?"

pause 0.5

melody "[ellipses]"
melody -sadbrow @talking2mouth "Yeah."
melody @talking2mouth "I get my deepest wish."

pause 0.5

melody @sadbrow talkingmouth "So[ellipses] you have to understand, that I--I {i}need{/i} to do anything I can to--to get it."

pause 1.0

melody @talking2mouth "Sorry."

$ SmartMoveOut("melody", atlist=[night])

pause 2.0

if (yellowin and protagin):
    red @sweat talking2mouth "Well[ellipses] if the contest isn't happening anymore, do you want to just[ellipses] go back to the dorm?"

elif (yellowin):
    red @sweat talking2mouth "Well[ellipses] if the contest isn't happening anymore, do you want to just[ellipses] go back to the dorm, Yellow?"

else:
    red @sweat talking2mouth "Well[ellipses] if the contest isn't happening, and there's nothing for us to watch, do you want to just[ellipses] go back to the dorm, Yellow?"

pause 0.5

redmind @closedbrow sweat frownmouth "No, she {i}really{/i} doesn't. Man, after pushing herself out of her comfort zone to do this, to have it all just fall flat is[ellipses]"

show leaf sadbrow -frownmouth with dis

if (protagin and yellowin):
    red @talkingmouth "Want to go backstage and[ellipses] put on a show anyway? Even if it's just for our dormies?"

    pause 0.5

    yellow @smilemouth "[ellipses]"
    yellow happybrow @talkingmouth "Yes. I do."

elif (yellowin or not protagin):
    red @talkingmouth sadbrow "What do you think about going backstage, and putting on a show anyway? I'd watch it."
    
    pause 0.5

    yellow @smilemouth "[ellipses]"
    yellow happybrow @talkingmouth "Yes. I think I will."

else:
    red @talkingmouth sadbrow "I think I might just go backstage, and do this anyway. I mean, I've got a new suit I need to break in, right? And it'll piss Blue off."

    pause 0.5

    yellow @smilemouth "[ellipses]"
    yellow happybrow @talkingmouth "Yes. I think[ellipses] that's a good idea."

scene blank2 with splitfade

pause 0.5

if (protagin and yellowin):
    scene concerthallbackstage with splitfade

    narrator "You head backstage with Yellow. Through the thick curtain, you hear a few scattered, discontented mutters, both from backstage, and in the stands."

elif (protagin):
    scene concerthallbackstage with splitfade

    narrator "You head backstage alone. Through the thick curtain, you hear a few scattered, discontented mutters, both from backstage, and in the stands."

else:
    scene concerthallstagenight with splitfade

    narrator "You head out with Leaf. The sparse few people {i}in{/i} the coliseum are trailing out, a low hum of discontented muttering hanging like a shroud over the dim stage."

narrator "Perhaps during the past week, news of how the Millennium Drop had devolved had spread, and you were simply too busy with the party to notice."
narrator "Or perhaps the deflated atmosphere is simply so obvious it's immediately contagious to anyone who enters the coliseum."

pause 1.0

if (protagin):
    $ AddEvent('Game', 'AutoContest')
    if (yellowin):
        $ AddEvent('Yellow', 'AutoContest')

        show screen songsplash("Viridian Forest", "Zame")
        stop music fadeout 1.5
        queue music "audio/music/viridianforestgentle_start.ogg" noloop
        queue music "audio/music/viridianforestgentle_loop.ogg"

        show yellow contest blush sadbrow with Dissolve(2.0)

        pause 0.5

        red @surprisedbrow talking2mouth "Oh, wow. Yell', you look amazing. Is this what Leaf was getting for you?"

        yellow @talkingmouth "Actually[ellipses] Blue got this for me."
        yellow @happybrow talkingmouth "I think he was really worried if {i}he{/i} didn't get me a dress, I'd go with a suit."
        yellow @closedbrow talking2mouth "Of course, contest attire should really be skirts, but[ellipses] it was a nice thought."
        yellow @talkingmouth "No, what Leaf got for me, was, um[ellipses] Omny."

        $ SmartShift("yellow", pos=0.75)

        $ DisplayPokemon("Omanyte")

        red @happy "Woah! A Fossil Pokémon? That's big. Well, small and cute, but you know what I mean."

        yellow @talkingmouth "I mentioned I thought they were cute a few weeks ago. Leaf meant to give me more time with him before I had to use him in the actual contest, but[ellipses]"
        yellow @happybrow talkingmouth "Well, we know what happened there."

        $ HidePokemon()
        $ SmartShift("yellow", pos=0.5)

        if (yellowpath):
            yellow @talking2mouth "I'd like to use him in the contest, but[ellipses] our 'main' Pokémon can be someone else, if you want. I don't want to throw off the routine we practiced."

            red @talkingmouth "I'll see if we can find some room for him. Since, you know, this contest is kinda screwy already, we might as well have some fun with it."

            yellow @talkingmouth "[ellipses]Yes. {w=0.5}{nw}"
            extend @happybrow talkingmouth "Let's have fun."

        else:
            yellow @talking2mouth "I'd like to use him in the contest, but[ellipses] well, I've never used him before. He doesn't know any of the routines Chuchu and I practiced."

            red @talkingmouth "You know, this contest is kinda screwy already, we might as well have some fun with it. Maybe winning doesn't matter as much as trying does."

            yellow @talkingmouth "[ellipses]Yes. {w=0.5}{nw}"
            extend @happybrow talkingmouth "All that matters is I tried."

        pause 1.0

        yellow @surprised "Oh. I need to hem this dress a tiny bit. I don't want to trip."

        red @happy "Alright. Don't take too long! If we're doing this, we shouldn't give Phobos any more time to kill it."

        $ SmartMoveOut("yellow")

    else:
        redmind @sweat closedbrow "Alright. This contest is going to be a bit[ellipses] screwy. {nw}" 
        redmind @happy "But that's even more reason to just have fun with it."

pause 2.0

if (klarapath):
    $ MoveInSmart("klara shadow contest makeup angrybrow frownmouth hairpin shadow")

    pause 1.0

    red @thonk "[ellipses]"
    
    red @talking2mouth "You never wore {i}that{/i} when we were practicing our routines."

    if (HasEvent("Klara", "TrueKlara")):
        klara @talking2mouth "...The contest is canceled. Why are you still here?"

        red @talking2mouth "Why are {i}you?{/i}"

        klara @talking2mouth "Would you believe me if I said it was because I was looking forward to this, even before you were part of it?"
        
        red @sadbrow talkingmouth "Yeah."

        klara @angrybrow talking2mouth "Of course you would."
        klara @wrathbrow wrathmouth "Of course you would. Drop dead."

    else:
        klara @talking2mouth "...The contest is canceled. Why are you still here?"

    $ MoveOutSmart("klara")

    redmind @sad2eyes poutmouth "[ellipses]Not in the mood for conversation, I guess."

    pause 2.0

stop music fadeout 1.5
$ renpy.music.queue("Audio/Music/SoaringIllusions_Intro.ogg", channel='music', loop=None, tight=None)
$ renpy.music.queue("Audio/Music/SoaringIllusions.ogg", channel='music', loop=True, tight=None)

if (protagin):
    $ MoveInSmart("brendan contest angrybrow frownmouth", maintain=True)
    $ MoveInSmart("may contest sadbrow frownmouth")
else:
    $ MoveInSmart("brendan angrybrow frownmouth", maintain=True, atlist=[night])
    $ MoveInSmart("may sadbrow frownmouth", atlist=[night])

red @surprisedbrow frownmouth "[ellipses]"
red @happy "Hey, you two. You look great."
red @sadbrow talkingmouth "But you don't look like you {i}feel{/i} great."

brendan @talking2mouth "Yeah, I guess it's pretty obvious. Canceling the whole contest? Then what was the point of making me change my song?"

if (not HasEvent("Game", "Contest2")):
    red @surprised "He made you change your song?"

    brendan @talking2mouth "Yeah, earlier this week."

    red @thinking "From what to[ellipses] what?"

    brendan @talking2mouth "It was an old Hoennian hymn. A love song. But Phobos pretty much said that I wouldn't get anywhere singing {i}that{/i} one."
    brendan @sadbrow talking2mouth "[ellipses]But the song he gave me instead is pure garbage. Not even {i}Lisia{/i} could make it sound good."

    pause 0.5

    red @talkingmouth "If it's so bad, then[ellipses] why did you decide to sing it? Maybe Phobos doesn't know what he wants."

    brendan sadbrow @frownmouth "[ellipses]"

    may @talking2mouth "Phobos blackmailed Brendan. Phobos was going to[ellipses] 'talk' to me, unless Brendan sang his awful song."

    red @surprisedbrow talking2mouth "Holy shit, what?! That's insane! What--what did he mean by {i}talk{/i}?"

    brendan @talking2mouth "Probably just push May out of the contest, like he's been doing to all the other coordinators."
    brendan @angrybrow talking2mouth "'Course, turns out there wasn't even a point to that."

else:
    red @closedbrow talking2mouth "Right. That godawful song. Nightmare Power?"

    brendan @closedbrow talking2mouth "Dream Energy."

    may @sadbrow talkingmouth "But that name probably works better. I don't think even Brendan could make that one sound good. It {i}actually{/i} has a line about shareholders in it."

    red @wince talking2mouth "I heard."

pause 1.0

red @talkingmouth "Hey, since the contest is canceled, what do you think about putting on an unofficial show, anyway? I mean, my dormmates are up there."

if (yellowin):
    red @talking2mouth "Yellow's up for it."

pause 1.0

brendan @sadbrow talking2mouth "I dunno. Phobos has a lot of money, and a lot of influence in the coordinatin' world. I might get May in a lot of trouble."

may @sadbrow talkingmouth "Sweetheart, what do you {i}want{/i} to do?"

brendan @sadbrow frownmouth "[ellipses]"
brendan sadbrow -frownmouth @talkingmouth "Honestly, I kind of just want to compete against Melody. She's got some crazy moves. I want to know if I can put on a bigger show than her."

may -frownmouth @happy "Well, we might not be able to do that[ellipses] but you can still perform like you're performing against Melody!"

brendan @talkingmouth sadbrow "Yeah. Let's do it, babe. And sorry if we get in serious trouble for it."

may @talkingmouth "It'll be worth it!"

if (GetRelationshipRank("Brendan") == 1 and not HasEvent("Brendan", "NormanContest")):
    $ AddEvent("Brendan", "NormanContest")

    red @wince talking2mouth "A thought occurs. Uh, Brendan, is your Dad here?"

    brendan @talking2mouth "Nah. He'll come to some other contest. I smelled somethin' fishy about this a while ago, so I didn't tell him about {i}this{/i} contest."
    brendan @talkingmouth "Besides, it's an old Hoennian contest. He'd be able to watch contests like this in almost any town in Hoenn. We've been celebrating it for thousands of years."

    red @sadbrow talking2mouth "Damn. I'm sorry, man."

    may @talkingmouth sadbrow "Don't be. We'll[ellipses] we'll figure something out. Contest or no contest, we'll still put on a show."

if (not protagin):
    brendan @sweat sadbrow talking2mouth "Man, we should get changed. Faster we get this started, the more likely it is Phobos can't stop us."

    red @sadbrow talkingmouth "I'm sorry, you two."

    may @talkingmouth sadbrow "Don't be. We'll[ellipses] we'll figure something out. Contest or no contest, we'll still put on a show."

red @happy "I believe it."

$ MoveOutSmart("brendan")
$ MoveOutSmart("may", maintain=True)

scene blank2 with splitfade 

narrator "Hushed whispers echo around the arena as the rebellious coordinators, though lacking in numbers, conspire to put on a show."

if (protagin):
    brendan contest @angrymouth angrybrow "He calls himself a coordinator? You don't just {i}cancel{/i} a contest like this last-minute. Hasn't he ever heard of 'the show must go on'?"

    if (yellowin):
        narrator "The other coordinators grumble in agreement. You look around to see how Yellow is doing, and it occurs to you you haven't seen her in a while."

        pause 0.5 

        narrator "Suddenly[ellipses]"

        $ hideside = True

        stop music fadeout 1.5
        queue music "audio/music/tension_start.ogg" noloop
        queue music "audio/music/tension_loop.ogg"

        yellow "{size=40}I said {i}NO!{/i}{/size}"

        scene concerthallbackstage with splitfadefaster

        $ MoveInSmart("yellow contest angrybrow frownmouth", 0.5)

        pause 0.5

        $ hideside = False

        red @surprisedbrow talking2mouth "Yell'? What--"

        yellow @angrymouth "Phobos just said we're not allowed to perform, even unofficially!"

        $ MoveInSmart("brendan angrybrow frownmouth contest", maintain=True)
        $ MoveInSmart("may angrybrow frownmouth contest")

        red @angry "He {i}what?!{/i}"

        brendan @talking2mouth "Where is he?!"

    else:
        narrator "The other coordinators grumble in agreement."

        pause 0.5 

        narrator "Suddenly[ellipses]"

        $ hideside = True

        stop music fadeout 1.5
        queue music "audio/music/tension_start.ogg" noloop
        queue music "audio/music/tension_loop.ogg"

        may "{size=40}I said {i}NO!{/i}{/size}"
        
        scene concerthallbackstage with splitfadefaster

        $ MoveInSmart("may contest angrybrow frownmouth", 0.5)

        pause 0.5

        $ hideside = False

        red @surprisedbrow talking2mouth "May? What--"

        may @angrymouth "Phobos just said told me we can't perform! Not even unofficially!"

        $ MoveInSmart("brendan contest", maintain=True)
        $ MoveInSmart("may contest")

        red @angry "He {i}what?!{/i}"

elif (yellowin):
    leaf night @talking2mouth sadbrow "Uh[ellipses] do you think we should go backstage and see how Yellow is doing?"

    red night @talking2mouth "I[ellipses] don't know. It's been a while since we've seen her. What do you think the coordinators are doing backstage? Arguing with Phobos?"

    pause 1.0

    leaf @talkingmouth "Only one way to find out!"

    red @talking2mouth "You're just bored as hell, and want to get this started, so you can get it over with, right?"

    leaf @talking2mouth flirtbrow "Yeah, one hundred percent."

    blue night @talkingmouth "Finally, {i}someone{/i} said it."

    ethan night @talking2mouth "Ditto that."
 
    red @talking2mouth "Same. Let's go."

    scene blank2 with splitfade

    pause 0.5 

    scene concerthallbackstage with splitfade

    narrator "You've only just walked through the side door into the backstage, when[ellipses]"

    $ hideside = True

    stop music fadeout 1.5
    queue music "audio/music/tension_start.ogg" noloop
    queue music "audio/music/tension_loop.ogg"

    yellow "{size=40}I said {i}NO!{/i}{/size}"

    $ MoveInSmart("yellow contest angrybrow frownmouth", 0.5)
    
    $ AddEvent('Yellow', 'AutoContest')

    pause 0.5

    $ hideside = False

    red @surprisedbrow talking2mouth "Yell'? What--"

    yellow @angrymouth "Phobos just said we're not allowed to perform, even unofficially!"

    $ MoveInSmart("brendan angrybrow frownmouth contest", maintain=True)
    $ MoveInSmart("may angrybrow frownmouth contest")
    $ MoveInSmart("blue angrybrow frownmouth", maintain=True)
    $ MoveInSmart("ethan angrybrow frownmouth", maintain=True)
    $ MoveInSmart("leaf angrybrow frownmouth")

    red @angry "He {i}what?!{/i}"

    leaf @talking2mouth "That's too far! He should be starting the stupid thing, not trying to rig it more! Where is he?"

else:
    yellow @sadbrow talking2mouth "[ellipses]"

    pause 1.0

    red upeyes frownmouth "[ellipses]"

    red @talking2mouth "Maybe we should check in backstage."

    yellow @talking2mouth "What? I--I don't think we're allowed to do that[ellipses]"

    red @talking2mouth "Probably not, but what are they going to do? Cancel the contest again?"

    yellow @talking2mouth "[ellipses]Alright."

    red @surprisedbrow talking2mouth "Oh, for real? I didn't think you'd be down."

    yellow @sadbrow talkingmouth "I'm[ellipses] actually a little bored. Maybe it's not a great reason, but[ellipses]"

    blue night @talkingmouth "Well, {i}I'm{/i} bored as hell. It should be you up on that stage, Yellow. I'm not going to sit around patiently waiting for a bunch of nobodies."

    ethan night @talking2mouth "Ditto that, but without what I {i}think{/i} was meant to be a compliment?"

    red @sadbrow talking2mouth "I'll take it. Let's go."

    scene blank2 with splitfade

    pause 0.5 

    scene concerthallbackstage with splitfade

    narrator "You've only just walked through the side door into the backstage, when[ellipses]"

    $ hideside = True

    stop music fadeout 1.5
    queue music "audio/music/tension_start.ogg" noloop
    queue music "audio/music/tension_loop.ogg"

    may "{size=40}I said {i}NO!{/i}{/size}"

    $ MoveInSmart("may contest angrybrow frownmouth", 0.5)

    pause 0.5

    $ hideside = False

    red @surprisedbrow talking2mouth "May? What--"

    may @angrymouth "Phobos just said we can't perform, not even unofficially!"

    $ MoveInSmart("brendan angrybrow frownmouth contest")
    $ MoveInSmart("yellow angrybrow frownmouth", maintain=True)
    $ MoveInSmart("blue angrybrow frownmouth", maintain=True)
    $ MoveInSmart("ethan angrybrow frownmouth", maintain=True)
    $ MoveInSmart("leaf angrybrow frownmouth")

    red @angry "He {i}what?!{/i}"

    brendan @angry "He said he wouldn't if I sang that song of his! That lyin' piece of[ellipses] where is he?"

scene blank2 with splitfadefaster

pause 0.5

if (not protagin):
    narrator "You storm the stage, angry dorm members and coordinators in tow."

else:
    narrator "You storm the stage, angry coordinators in tow. Behind you, your dormmates spill in through the side entrances to back you up."

scene concerthallstagenight with splitfadefaster

pause 1.0

show phobos unamusedbrow frownmouth with dis

phobos @talking2mouth "Oh, delightful, {i}more{/i} unnecessary people."

$ MoveInSmart("brendan angrybrow frownmouth contest", maintain = True)
$ MoveInSmart("may angrybrow frownmouth contest")
if (yellowin):
    $ MoveInSmart("yellow angrybrow frownmouth contest", maintain=True)
else:
    $ MoveInSmart("yellow angrybrow frownmouth", maintain=True)
$ MoveInSmart("blue angrybrow frownmouth", maintain=True)
$ MoveInSmart("ethan angrybrow frownmouth", maintain=True)
$ MoveInSmart("leaf angrybrow frownmouth")

show phobos zorder 299

stop music fadeout 1.5
queue music "audio/music/lawrencetheme_start.ogg" noloop
queue music "audio/music/lawrencetheme_loop.ogg"

brendan @angrybrow angrymouth "You pushed the entire coordinator club out of competin', and now you're not even lettin' us put on a contest {i}for fun?{/i}"

phobos @upeyes talking2mouth "Oh, don't put on a {i}show{/i}. It's not {i}my{/i} fault you are all so unreliable."

yellow @talking2mouth "I was here {i}early.{/i}"

phobos @talking2mouth "Yes, yes, yes. Please stop making everything about you, and take some responsibility for causing this."
phobos @talking2mouth "I have need of my coliseum, so I'm afraid I must repetitiously assert that you cannot use it for your 'for fun' diversions. Now, begone, if you please."
phobos @talkingmouth "There aren't even enough of you to put on a proper contest, in any case."

may @talking2mouth "What do you mean?"

$ competitors = 0

if (protagin):
    if (yellowpath):
        $ competitors = 3

        phobos @talking2mouth "Can you count? To three? On your fingers? Because there's only three of you here. Brendan, yourself, and that twiggy blonde girl's group."

        blue @scaredeyes angryeyebrows angrymouth "{i}Twiggy?!{/i}"

    elif (klarapath):        
        if (yellowin):
            $ competitors = 4

            phobos @talking2mouth "Can you not count? Over three? On your fingers? Because there's only four of you here. Brendan, yourself, that twiggy blonde girl, and that pink whore's group."

            blue @scaredeyes angryeyebrows angrymouth "{i}Twiggy?!{/i}"

        else:
            $ competitors = 3

            phobos @talking2mouth "Can you not count? To three? On your fingers? Because there's only three of you here. Brendan, yourself, and that pink whore's group."

        red @unamusedbrow talking2mouth "She's not here anymore. We're competing separately."
        
        pause 0.5

        red @closedbrow talking2mouth sweat "Also, she's not a whore."

        phobos @confusedbrow talking2mouth "Competing separately? Whatever gave you the ingloribly wrong impression you were allowed to do that? You passed the tryouts as a pair."
        phobos @closedeyes sadeyebrows talkingmouth "Ah, I am afraid, no one has any guarantee of your quality apart."

    elif (yellowin and klarain):
        $ competitors = 4

        phobos @talking2mouth "Come now. In terms of {i}real{/i} coordinators, there aren't many here, are there? Not really? No, rather."
        phobos @sadbrow talkingmouth "Really, how many here {i}actually{/i} passed their tryout rounds?"

    elif (yellowin):
        $ competitors = 4

        phobos @talking2mouth "Can you not count? Over three? On your fingers? Because there's only four of you here. Brendan, yourself, that boy wearing a suit that is {i}so{/i} last season, and that twiggy blonde girl."

        blue @scaredeyes angryeyebrows angrymouth "{i}Twiggy?!{/i}"

    else:
        $ competitors = 3

        phobos @talking2mouth "Can you not count to three? On your fingers? Because there's only three of you here. Brendan, yourself, and that boy wearing a suit that is {i}so{/i} last season."

        red @unamusedbrow talking2mouth "You know my name."

elif (yellowin and klarain):
    $ competitors = 4

    phobos @talking2mouth "Come now. In terms of {i}real{/i} coordinators, there aren't many here, are there? Not really? No, rather."
    phobos @sadbrow talkingmouth "Really, how many here {i}actually{/i} passed their tryout rounds?"

elif (yellowin):
    $ competitors = 3

    phobos @talking2mouth "Can you count? To three? On your fingers? Because there's only three of you here. Brendan, yourself, and that twiggy blonde girl."

    blue @scaredeyes angryeyebrows angrymouth "{i}Twiggy?!{/i}"

elif (klarain):
    $ competitors = 3

    phobos @talking2mouth "Can you count? To three? On your fingers? Because there's only three of you here. Brendan, yourself, and... oh, where'd that pink whore go?"

    red @closedbrow talking2mouth sweat "She's not a whore."

else:
    $ competitors = 2

    phobos @talking2mouth "Can you not even count? To three? On your fingers? Because there's only two of you here. Brendan and yourself."

phobos @closedeyes sadeyebrows talkingmouth "Yes, there's still less than five of you. So there will be no official contest, and I'll save you the embarrassment of whatever your 'unofficial' contest might look like."
phobos @unamusedeyes angryeyebrows talking2mouth "Now, {i}go away{/i}."

brendan @talking2mouth "Look, I know what the Millennium Drop's rules are. If the highest-ranking performers of the tryout rounds don't show up, we just go down the list until we find substitutes."

phobos @upeyes talking2mouth "Oh, and this 'list.' Do you have it? This wonderful, glorious, physical, list? Do you happen to know how Fantina and Champion Wallace ranked your performances?"
phobos @sadbrow talkingmouth "Why, I could certainly give it my best estimate, if you want, but I'm afraid you may find {i}yourself{/i} falling three spots, right out of top five."

narrator "[ellipses]It doesn't seem like Phobos intends to let anyone perform at all."

$ HighlightCharacter("yellow", "contest")

yellow angrybrow frownmouth @angrybrow talking2mouth "We need to do something about this. Even if he canceled the contest, he can't stop us from performing."

if (not protagin):
    red @talking2mouth "No kidding. I'm not even part of this contest, and even I'm pissed. If Phobos wants the official contest dead, then we put on our own show. There's no way Drayden would let him do this, right?"
else:
    red @talking2mouth "No kidding. He can't stop us from putting on our own show. I just can't believe that. There's no way Drayden would let Phobos do this, right?"
    
yellow @closedbrow talking2mouth "[ellipses]Wait."
yellow @surprised "Where's Jasmine?"
yellow @talking2mouth "I think everyone else in the club was pushed out of the contest, but[ellipses] Jasmine never quit! She would {i}never!{/i} {i}And{/i} she won her tryout rounds!"

red @closedbrow sweat talking2mouth "Ah, man. That's rough. She might just be[ellipses] you know, she might not be feeling up to it. No matter how much she wanted to."

yellow sadbrow frownmouth @talking2mouth "[ellipses]{size=20}I could try healing her?{/size}"

red @confused "Huh?"

yellow @sadbrow talkingmouth "I could try healing her?"

pause 2.0

red @confused "Does it work on humans?"

yellow @closedbrow talking2mouth "Nevermind, it was a dumb suggestion."

red @confused "No, seriously, does it work on humans? Do you know?"

yellow @talking2mouth "I[ellipses] well, I tried once, but healing a nosebleed knocked me out."

red @sweat talking2mouth "Ah. So maybe not the safest thing to try. Then, how about we--"

show yellow surprisedbrow frownmouth with dis

red @surprisedbrow talking2mouth "Wait. What about Melody? Phobos didn't even count her!"

yellow @talkingmouth "Oh my gosh, you're right! She must still be backstage!"

show yellow:
    xpos 0.5 ypos 1.2 zoom 1.3 xzoom 1
    ease 0.2 xzoom -1 xpos 0.49
    ease 0.5 xpos 1.2 ypos 1.0 zoom 1.0

hide semiblank2 with Dissolve(0.3)

leaf @angrybrow angrymouth "{gradualsize=20-32}[ellipses]can't get away{/gradualsize} with this, right, [first_name]?! {w=1.0}{nw}"
extend @surprisedbrow talking2mouth "Wait, where'd they go?"

scene blank2 with splitfade

if (protagin):
    narrator "You rush backstage once more."
else:
    narrator "You rush backstage, following Yellow's lead[ellipses]"

stop music fadeout 1.5
queue music "audio/music/lament.ogg" fadein 3.0

scene concerthallbackstage 
show melody contest on sadbrow frownmouth at night:
    xpos 0.25 xzoom -1

if (yellowin):
    show yellow contest surprisedbrow frownmouth:
        xpos 1.2
        ease 0.5 xpos 0.66
else:
    show yellow surprisedbrow frownmouth:
        xpos 1.2
        ease 0.5 xpos 0.66
with splitfadefaster

yellow @talking2mouth "Melody!"

pause 0.5

show melody:
    xzoom -1 matrixcolor nightmatrix xpos 0.25
    ease 1.0 xzoom 1
    pause 0.5
    ease 1.0 matrixcolor daymatrix xpos 0.33

pause 0.5

melody -on @talking2mouth "Yeah?"

yellow @talking2mouth sadbrow "Phobos is saying that we can't start the contest! And he isn't even letting us put on our own, unofficial performance!"

melody "[ellipses]{nw}"
extend @talking2mouth "Yeah."

pause 0.5

melody @disgustedbrow talking2mouth "So what?"

yellow @sadbrow talking2mouth "Well, just[ellipses] just tell him that you want to participate! He'll listen to you!"

melody @talking2mouth "You sure about that?"
melody "[ellipses]"

show melody:
    xzoom 1 matrixcolor daymatrix xpos 0.33
    ease 1.0 xzoom -1
    pause 0.5
    ease 1.0 matrixcolor nightmatrix xpos 0.25

pause 1.0

melody on @talking2mouth "It doesn't matter."
melody @talking2mouth angrybrow "You realize you could have five, ten, thirty people who all want to compete, and he'd still get whatever he wanted, right?"
melody @talking2mouth "You can't just[ellipses] stop him. Or any of the sick old men like him. They'll get what they want, because {i}no-one{/i} stops them."

yellow @talking2mouth "I[ellipses]"

show melody:
    xzoom -1 matrixcolor nightmatrix xpos 0.25
    ease 0.3 xzoom 1 matrixcolor daymatrix xpos 0.33

melody @talking2mouth "Prove me wrong. Let's say you go out there, and challenge him to a battle."
melody @talking2mouth "You know what he'd say? 'No, no, no, I would never stoop to such inelegallantry. Tonight is for {i}contests!{/i} Not yours, granted, but the conceptualization of such.'"

redmind @surprisedeyes unamusedeyebrows unamusedmouth "That was a scarily-accurate impression."

melody @talking2mouth "And even if he {i}did{/i} let you battle him[ellipses] you wouldn't win. He's strong. Stupid strong."

yellow @talking2mouth "You've tried?"

melody @talking2mouth "Twice."

pause 0.5

melody @sadbrow talking2mouth "Can't help you. Won't."
melody @talking2mouth "He's a creep. A loser. But I'm[ellipses]"
melody @closedbrow angrymouth "I'm {i}on his side.{/i} {w=0.5}{size=30}Ugh.{/size}"

yellow @talking2mouth "But[ellipses] you don't need him to cancel the contest. You're {i}really{/i} good. Liz said so."
yellow @talking2mouth "Why are you okay with him[ellipses]"

melody @talking2mouth "Look, I don't agree with it. But Phobos thinks if I join the contest, I might lose, and then I don't get my wish."
melody @talking2mouth "I can't help you. And, in case you forgot, I don't want to."

yellow angrybrow frownmouth "[ellipses]"

show melody surprisedbrow frownmouth with dis

yellow @angrybrow talking2mouth "I'm disappointed in you."

melody @talking2mouth "What?"

yellow @closedbrow talking2mouth "I looked up to you as a coordinator. During the club meetings, I was watching {i}you{/i} more than anyone else."
yellow @talking2mouth "I desperately wanted to see you perform. You never did, but I was excited to see you perform today. It would make all the waiting worth it."
yellow @angrybrow talking2mouth "But you're so afraid of losing you don't even want to compete? You're going to ruin everyone else's chances, too?"
yellow @talking2mouth "I don't know what this 'wish' is, but I can't see how it could be worth it."

show melody:
    xzoom 1 matrixcolor daymatrix xpos 0.33
    ease 1.0 xzoom -1
    pause 0.5
    ease 1.0 matrixcolor nightmatrix xpos 0.25

pause 0.5

melody neutralbrow @talking2mouth "Well, sorry, or whatever you want to hear."

yellow @talking2mouth "I'm not the only one disappointed."

melody @talking2mouth "Yeah, sure, I bet there's a whole queue. Who else, [melody_name]?"

yellow @talking2mouth angrybrow "Your Pokémon are disappointed, too. {nw}"

show melody sadbrow sadmouth with dis

extend @talking2mouth angrybrow "They don't understand--and they think they've done something wrong, that you're mad at them."

pause 0.5

melody @talking2mouth "W-{w=0.5}well[ellipses] that's life."
melody @talking2mouth "Sometimes bad things happen to you."
melody @talking2mouth "Even if you didn't do anything wrong."

$ hideside = True

$ MoveOutSmart("melody")

melody @talking2mouth "Now you know."

pause 0.5

$ hideside = False

red @talking2mouth wince "Eesh. That was harsh. Was it, uh, true?"

yellow @closedeyes angryeyebrows talking2mouth "What do you think? That I'd lie about something like that?"

red @happy sweat "Forget I said anything."

pause 0.5

red @talking2mouth "Well. What do we do now?"

if (competitors == 4):
    yellow -angrybrow @talking2mouth "Well[ellipses] If Jasmine shows up, then we'd still have enough people to run the contest."

else:
    yellow -angrybrow @talking2mouth "Even if Jasmine shows up, we won't have enough people to run the contest without Melody[ellipses]"

red @pity "We're late, but she's {i}really{/i} late. If she was going to come, then I think she would've already."
red @sad2eyes talking2mouth "And it doesn't matter, since Phobos has decided the whole contest is canceled."

yellow "[ellipses]{nw}"
extend @talkingmouth "Maybe we could get Dean Drayden? Or any other Professor?"

red @sweat talking2mouth "It's pretty late--they're probably in the teacher dorms now. But yeah, we can probably find someone who's willing to step up and stop this."

pause 1.0

if (HasEvent("Dawn", "BirthdayFair")):
    yellow @talking2mouth "What is it?"

    red @sweat closedbrow talking2mouth "I just remembered that the teacher dorms are in 'Phobos Hall.' Guess I know who paid for them."

yellow @sadbrow talking2mouth "What if[ellipses] the teachers can't stop him, either? It sounds like he's given the school a {i}lot{/i} of money."

red @talking2mouth "I mean, yeah, if that's the case, then there's nothing I can do about it. But we still have to try, right? {i}Someone{/i} has to. Maybe--maybe I should battle him."

yellow @surprised "But Melody--"

red @talking2mouth "Melody said I couldn't beat him, sure, but you know how many people told me I couldn't beat Dawn?"

yellow "[ellipses]{nw}"
extend @talking2mouth "No?"

red @talking2mouth "Several. Like, seven, at least."

yellow @talking2mouth "I don't think you can whip out another one-in-a-million transformation at the perfect time."

red @sadbrow talkingmouth "Yeah, neither do I."

if (yellowpath):
    red @happy "But, c'mon, I'm not going to just sit back and watch as Phobos ruins this contest for us. We're a great team, and I want to show us off, you know?"

elif (protagin):
    red @happy "But, c'mon, I'm not going to just sit back and watch as Phobos ruins this contest for me. I was looking forward to participating, you know?"

else:
    red @happy "But, c'mon, I'm not going to just sit back and watch as Phobos ruins this contest for everyone."

pause 0.5

yellow @talking2mouth "But what if you beat him in battle and he just[ellipses] keeps on doing what he's doing? Or refuses to battle you? Or tries to get you expelled?"

red @sad2eyes talking2mouth "Uh[ellipses] yeah, those could all happen, I guess. But I think it's probably still worth it[ellipses]"
red @closedbrow talking2mouth sweat "Though I didn't really consider the 'expulsion' part. He could probably do that, couldn't he?"

yellow @talking2mouth "Dean Drayden might let you back in after Phobos leaves."

red @confused "He might, but he's already looked the other way once. I don't want to push my luck there."

yellow @closedeyes angryeyebrows talking2mouth "Then, maybe if I just talk to Melody again, then[ellipses]"

stop music fadeout 1.5

pause 1.0

yellow confusedeyebrows @talking2mouth "Do you hear singing?"

red @confused "Huh?"

scene blank2 with splitfade

pause 0.5

narrator "Meanwhile, while you were backstage[ellipses]"

queue music "audio/music/lawrencetheme_start.ogg" noloop
queue music "audio/music/lawrencetheme_loop.ogg"

call clearscreens() from _call_clearscreens_287

scene concerthallstagenight 
show blank2 zorder 1000
with splitfade

pause 1.0

show leaf angrybrow frownmouth behind blank2:
    xpos -0.3
show ethan angrybrow frownmouth behind blank2:
    xpos -0.2
show blue angrybrow frownmouth behind blank2:
    xpos -0.1
show brendan contest angrybrow frownmouth behind blank2:
    xpos 0.1
show may contest angrybrow frownmouth behind blank2:
    xpos 0.2
show phobos behind blank2
$ LineUp(0, exclude="phobos", prefilled=[0.5, 0.51], considerexcludes=True)

hide blank2 with splitfade

phobos @talking2mouth "{gradualsize=20-36}[ellipses]so that's why I simply{/gradualsize} {i}cannot{/i} begin the contest. At all. Or ever."
phobos @sadeyebrows talkingmouth "Alas, it's completely out of my hands."
phobos @angrybrow anger2 shadow talking2mouth "Now--and, I will reiterate this no longer--{i}get out of my sight.{/i}"

brendan @talking2mouth "That's {i}not{/i} what the rules of the contest are."

phobos @talking2mouth "Oh, rules, rules, {i}rules{/i}. What sort of coordinator are you, that you just keep harping on about rote dogma? Honestly."

$ PlaySound("!.ogg")

show brendan surprisedbrow frownmouth with dis

pause 0.5

show may surprisedbrow with dis

brendan @talking2mouth "You[ellipses] you don't actually believe a thing you're sayin', do you?"

phobos surprisedbrow @unamusedbrow talkingmouth "Hm? Whatsoever do you--"

show may flirtbrow bigblush -frownmouth with dis

brendan @talking2mouth "You're just[ellipses] {i}talking{/i}. You don't {i}mean{/i} a single thing you're sayin'. You're just speakin' to fill the air, to get us to quit 'cause we're too frustrated to bother any more."

phobos frownmouth -surprisedbrow @confusedeyebrows upeyes "[ellipses]"

pause 0.5

show brendan angrybrow 
show may angrybrow frownmouth -bigblush
with dis

phobos @talking2mouth "Ah, I suppose it would eventually be obvious to you. You {i}were{/i} always a higher quality of man."
phobos @sadbrow talkingmouth "Thus it pains me to remind you that even if what you say is true, there is naught that can be done about it."

blue @angrybrow angrymouth "Screw that! We'll battle, and if you lose--"

phobos @talking2mouth "Oh, what a surprise, the Battle Team thug wants to try {i}battling{/i} away his problems."

$ GroupExpression("surprisedbrow frownmouth", exclude="phobos")

$ LineUp(1.0, exclude="phobos", prefilled=0.5, inner_band=0.05, considerexcludes=True)

phobos @unamusedbrow talking2mouth "No."

pause 1.0

leaf @talking2mouth "'No?'"

phobos @closedbrow talkingmouth "No, no, no. Yes, it's no."

show contest_light:
    xcenter 0.5 ycenter 0.5 zoom 1.25

phobos @upeyes talking2mouth "You see, unlike you battle teamites, I aspire to a higher form of craft, and my perfectly-constructed Pokémon will not deign to--"

hide contest_light

brendan -surprisedbrow @talking2mouth "Uh, that's fine."

pause 0.5

phobos surprisedbrow @talking2mouth "What?"

brendan @talking2mouth "You don't want to battle, right? Totally fine. I get it. So let's do a contest showcase. One versus one. And if my Pokémon win, then you just let us run the contest without you."

phobos frownmouth "[ellipses]"
phobos @talking2mouth "That's--that's, ah, that's[ellipses] ah, ah."
phobos -surprisedbrow @talking2mouth confusedbrow sweat "What--what--what do you mean {i}without{/i} me? Without a {i}judge{/i}? You're just going to hand the Millennium Trophy to whomsoever you feel like?"
phobos -surprisedbrow @talking2mouth confusedbrow sweat "You understand, that with the contest as a default, it goes back to the school, yes?"

brendan @closedbrow talkingmouth "Don't worry about that."
brendan -frownmouth @happybrow talkingmouth "That's only going to matter if I outperform you, right?"

pause 1.5

$ GroupExpression("angrybrow", exclude=["phobos", "brendan"])

phobos @talking2mouth sweat closedbrow "W-well[ellipses] of course. Of course, I can[ellipses] I can perform. I can {i}still{/i} perform. Just as before. Hah hah."
phobos @winkeyes angryeyebrows talkingmouth "Yes, I'm afraid you've miscalculatored, dear Brendan. I shall easily outperform you--or any other inelegoon who steps onto my stage."
phobos -frownmouth @angryeyebrows talkingmouth "You must know of my many accomplishments? Trophies? Achievements? Victories, to put it shortly? Do you really wish to be so horrendeverously humiliated on this stage?"

pause 0.5

brendan @confusedbrow frownmouth "[ellipses]"
brendan @talking2mouth "Uh. Sir. I {i}do{/i} know what kind of coordinator you were."

phobos @surprised "You--you knew me?!"
phobos surprisedbrow frownmouth @surprisedbrow talking2mouth "Wait, w-{w=0.5}were?! What on earth are you implying?!"

brendan @talking2mouth "Do you really want me to say it here? In front of everyone? I don't want {i}anyone{/i} to be[ellipses] uh, {i}horrendeverously{/i} humiliated. I think."
brendan @talking2mouth closedbrow sweat "{size=30}Uh, I'm not sure what {i}horrendeverously{/i} means, but I know 'humiliated' means embarrassed.{/size}"

phobos shadow angrybrow frownmouth @talking2mouth "If you knew me[ellipses] then say it."

brendan @talking2mouth "Yeah. I looked up to you. I mean, you were one of the first male coordinators. There weren't a lot of options, I guess, but, still[ellipses] I {i}had{/i} to look up to the Fearless Flying Baron Phobos."

leaf @surprisedbrow  talking2mouth"{size=30}It was a stage name this whole time?!{/size}"

ethan @talking2mouth "Wait. Fearless[ellipses] {i}flying{/i} Baron Phobos?"

brendan @talking2mouth "Yeah. He used Flying-types as his specialty. But he was also[ellipses]"

phobos @talking2mouth "A trapeze artist. My routines were acrobatics--flips and spins, of the kind that no man would believe were not supported by wires."
phobos @angrybrow angrymouth "But they {i}never{/i} were. No wires. No nets. No doubts."

$ GroupExpression("sadbrow frownmouth", exclude=["ethan", "blue"])

show blue sad2eyes with dis

phobos @angrybrow angrymouth "And I paid for it {i}dearly{/i}. I was three millimeters from the greatest performance I'd ever put on. And three seconds later, I was ruined."

pause 2.0

$ GroupExpression("surprisedbrow frownmouth", exclude="ethan")

ethan @confused "Uh[ellipses] that's it?"

$ GroupExpression("angrybrow frownmouth", exclude=["ethan", "blue"])

show blue smilemouth closedeyes happyeyebrows with dis

may @angry "Ethan!"

ethan @talking2mouth "He's got a freudian excuse for being a dick. Sure. Doesn't change the fact he's a dick. {i}That{/i} was a choice."

phobos angrybrow @talking2sharkmouth "Do you think you can speak that way to me and maintain your position at Kobukan for three seconds longer?"

ethan @talking2mouth "Uh, yeah. This thing you're doing here is insane. You haven't left yourself any outs. It's obvious you're not planning on being at Kobukan after this. You know the Dean won't allow this."

$ GroupExpression("surprisedbrow frownmouth", exclude="phobos")

phobos @anger2 angrysharkmouth "Drayden will allow what I tell him to allow! Melody has that foolish old man in a collar, and through her, {i}I{/i} hold the leash!"

$ GroupExpression("angrybrow frownmouth", exclude="phobos")

pause 1.0

ethan @talking2mouth "Kinky, but fucked up."

brendan @talking2mouth "Sir, I am challenging you to a contest showcase. As a coordinator, you cannot refuse." 

phobos @talking2sharkmouth anger "Do you believe you can tell me what a coordinator {i}can{/i} or {i}cannot{/i} do?! You can't even recognize that your woman there barely has any interest in the art!"
phobos @angrysharkmouth anger2 "Now shut up, go away, and take your lackabout friends with you, or I'll ensure your girlfriend never steps on a stage again!"

pause 2.0

may @talking2mouth "Honey?"

brendan @talking2mouth "Babe?"

may @talking2mouth "I {i}really{/i} want him to stop talking."

brendan @closedbrow talking2mouth "{i}Sigh.{/i}"
brendan @talking2mouth "Alright, sir. Whether or not you allow it, I'm putting on a showcase. The coordinating club has been jerked around for three weeks--at the very least, we deserve to perform."

phobos @anger2 angrysharkmouth "Stop, damn you, stop, {i}stop{/i}! Don't you {i}dare{/i} sing a single note!"

brendan @sadbrow talkingmouth "Sorry, sir. And I won't be singing {i}your{/i} song, either."

show blank2 zorder 1000 with splitfade

pause 2.0

narrator "The following segment is best enjoyed with audio on. Additionally, it is intended to be played against a time limit, so skipping will be disabled, and text speed will be set to maximum."
narrator "If you have any physical or mechanical limitations that would make this difficult, then please indicate so now. There will be no difference in rewards for choosing to eliminate the time limit."

menu:
    "I can play the game with a time limit.":
        narrator "Understood. The game will proceed as normal."

        pass

    "I would prefer there is no time limit.":
        $ AddEvent("Game", "LimitlessShowcase")
        narrator "Understood. There will be no time limit."
        
        pass

narrator "One more question. Which difficulty level would you like to embrace? This will affect {i}all{/i} battles and contest showcases for the rest of the day."

menu:
    "Normal":
        $ AddEvent("Lawrence", "Normal")
        narrator "Understood. The game will proceed as normal."

    "Hard":
        $ AddEvent("Lawrence", "Hard")
        narrator "Understood. The game will proceed in a more difficult fashion."

    "Tyrannic":   
        $ AddEvent("Lawrence", "Tyrannic") 
        narrator "Understood. The game will proceed in an excruciating fashion."

if (HasEvent("Game", "LimitlessShowcase")):
    narrator "Attempt to outperform as many of Phobos' Pokémon as possible! It is not required that you win, but the better you do, the easier future challenges will be!"

else:
    narrator "Attempt to outperform as many of Phobos' Pokémon as possible before the song ends! It is not required that you win, but the better you do, the easier future challenges will be!"

narrator "How do you 'outperform' a Pokémon, you ask?"

pause 1.0

narrator "Well, it looks quite a bit like a battle."

$ BeginKaraokeBattle("brendan.wav")

show screen karaoke_overlay

python:
    trainer1 = MakeTrainer("brendan", TrainerType.Player)
    trainer2 = MakeTrainer("phobos", TrainerType.Enemy)
    if (HasEvent("Lawrence", "Hard")):
        for mon in trainer2.GetTeam():
            mon.UpdateLevel(30, updateMoves=False, force=True)
        GetTrainerTeam("Phobos", "Combee").Foreverals = ["Vespiquen Uneveral"]
        GetTrainerTeam("Phobos", "Dodrio").Foreverals = ["Dodrio Overal"]
    elif (HasEvent("Lawrence", "Tyrannic")):
        for mon in trainer2.GetTeam():
            mon.UpdateLevel(33, updateMoves = False, force=True)
        GetTrainerTeam("Phobos", "Combee").Foreverals = ["Vespiquen Uneveral"]
        GetTrainerTeam("Phobos", "Dodrio").Foreverals = ["Dodrio Overal"]

call Battle([trainer1, trainer2], customexpressions=["brendan contest angrybrow", "brendan contest happy", "phobos angrybrow frownmouth anger", "phobos angrybrow angrysharkmouth anger2"], gainexp=False, specialmusic="audio/music/vocals/brendan.wav", stopmusic=True, lockbag=True, dialogfunc=phobospeanutgallery, customswitchbrain=phobosswitchbrain) from _call_Battle_196
$ RecordBattle("Phobos1")
$ renpy.music.queue("Audio/Music/SoaringIllusions_Intro.ogg", channel='music', loop=None, tight=None)
$ renpy.music.queue("Audio/Music/SoaringIllusions.ogg", channel='music', loop=True, tight=None)

hide screen karaoke_overlay

$ EndKaraokeBattle()

python:
    phobosteam = {}
    mon_names = ["Tatsugiri", "Combee", "Wugtrio", "Dodrio", "Iron Jugulis"]
    for mon_name in mon_names:
        mon = GetTrainerTeam("Phobos", mon_name, False)
        if mon.GetFaintedTurn() > 0:
            phobosteam[mon_name] = "KO'd"

if (WonBattle("Phobos1")):
    show phobos surprisedbrow frownmouth
    show brendan contest surprisedbrow frownmouth:
        xpos 0.51
    show may blush -frownmouth
    with dis
else:
    show phobos shadow frownmouth angrybrow anger
    show brendan contest:
        xpos 0.51
    with dis

$ LineUp(exclude="phobos", prefilled=[0.5, 0.51], considerexcludes=True)

show leaf:
    ease 0.5 xpos 0.05
show blue zorder 1000:
    ease 0.5 xpos 0.25 ypos 1.05 xzoom -1
show ethan:
    ease 0.5 xpos 0.13 ypos 1.02

leaf @surprisedbrow talking2mouth "{size=30}Uh, guys? Phobos has Foreverals. That's, like, {i}a problem,{/i} right?{/size}"

blue @sadmouth closedbrow "{size=30}Gramps {i}didn't{/i} give them to him.{/size}"

ethan @sad2eyes talking2mouth "{size=30}I mean[ellipses] we know Professor Oak owes Phobos for his job, right? That'd also explain how Melody got hers[ellipses]{/size}"

blue @angry "{size=30}It {i}wasn't{/i} Gramps!{/size}"

leaf @talking2mouth "{size=30}Alright, alright, boys. Calm down. We'll table this.{/size}"

$ LineUp(exclude="phobos", prefilled=[0.5, 0.51], considerexcludes=True)

if (WonBattle("Phobos1")):
    phobos @surprisedbrow talking2sharkmouth "I[ellipses] I[ellipses] I was outshone[ellipses]?"
    phobos @angrybrow angrysharkmouth "No, no, no. Naturally, I simply held myself back, as it would not do to have a fledgling coordinatorling like you be so overcompensatorily lambasted by my grandeur!"
    phobos anger angrybrow shadow frownmouth @happybrow happysharkmouth sweat "W-why[ellipses] it's utterly {i}embarrassing{/i} you thought I was actually trying!"

else:
    phobos @talking2sharkmouth "Are you satisfied? Do you believe you've {i}made your point{/i}? Have you embarrassed yourself enough yet?"

brendan -surprisedbrow -frownmouth @talkingmouth "I'm not embarrassed at all, sir. I did pretty well, actually. I'm pretty proud of myself."

show may -blush with dis

phobos @talking2sharkmouth "You're a showoff, an eyesore, and you can't hold a note to save your life. Get off my stage."

show brendan surprisedbrow frownmouth with dis

show may:
    ease 0.2 xpos 0.51

pause 0.2

$ LineUp(prefilled=[0.5])

show brendan -surprisedbrow -frownmouth zorder 99 with dis

may angrybrow frownmouth @angrybrow angrymouth "Now, hold on! Brendan's been {i}nothing{/i} but polite to you, and now you're just insulting him?! How can you say he's a bad coordinator when {i}you{/i} didn't even perform?!"

show phobos:
    ease 0.5 xpos 0.5

phobos @upeyes talking2sharkmouth "I am unsurprised the intricacies of my performance were lost on a reneger like you, but--"

$ GroupExpression("surprisedbrow frownmouth")

show concerthallstagenight with vpunch

stop music fadeout 1.5
queue music "audio/music/tension_start.ogg" noloop
queue music "audio/music/tension_loop.ogg"

TempCharacter("{color=#00b8d0}???{/color}") "{size=40}{i}PHOBOS!{/i}{/size}"

pause 1.0

phobos @talking2sharkmouth upeyes "Oh, who is it {i}now?{/i} Why didn't someone just {i}lock{/i} that door?"

show grusha sweat angryeyes angryeyebrows:
    xpos 1.2
    ease 0.2 xpos 5/8

pause 0.2

$ LineUp(prefilled=[0.5])

phobos @angrybrow talking2sharkmouth "Jasmine's boy? You're not even a coordinator! You're not permitted to--"

show concerthallstagenight with vpunch

grusha @talking2mouth "Shut up!"

show grusha:
    ease 0.9 rotate -2 xpos 5/8 ypos 1.07

pause 1.5

show phobos:
    ease 0.333 xpos 0.5

grusha @winkeyes angryeyebrows sweat "*{i}Pant.{w=0.5} Pant.{/i}*"

if (SeenElectiveScene("Flying", 10) or SeenElectiveScene("Ice", 10)):
    ethan @talking2mouth "Grusha? Are you alright?"
else:
    blue @talking2mouth "Grusha? You shouldn't be running around like that."

grusha @winkeyes sweat talking2mouth "You--{w=0.5}You shut up too."
grusha @winkeyes angryeyebrows sweat "*{i}Pant.{w=0.5} Pant.{/i}*"

pause 1.5

phobos -surprisedbrow @unamusedbrow talking2sharkmouth "If you ran in here just to have a heart attack, would you kindly redirect yourself to the infirmary?"

pause 1.5

show grusha noscarf:
    ease 0.5 ypos 1.0 rotate 0 xpos 5/8

grusha @shadow talking2mouth "I just came from there."

phobos @confusedbrow frownmouth "[ellipses]"
phobos @talking2sharkmouth "Ah."

$ GroupExpression("angrybrow frownmouth")

show brendan angrybrow angrymouth with dis

grusha angrymouth angryeyebrows angryeyes "Why is Jasmine {i}in the infirmary{/i}, Phobos?"

phobos @talking2sharkmouth closedbrow sweat "I can {i}hardly{/i} be held responsible for her weak constitution."

grusha "What did you {i}do{/i} to Jasmine, Phobos?"

phobos @upeyes talking2sharkmouth "Oh, you're so desperate to believe {i}I'm{/i} the villain here. We simply talked."
phobos @sadbrow talkingsharkmouth "Granted, the conversation became spirited, and Jasmine[ellipses] well, she simply fainted. That's all that is to it."

grusha @talking2mouth "People don't {i}faint{/i} from {i}conversations,{/i} Phobos!"

phobos @talking2sharkmouth upeyes angryeyebrows "Oh, and you're a doctor? Of medicine? With a degree? I assure you, I have a fair amount of experience with doctors, so I quite know what I'm talking about."
phobos @talking2sharkmouth "In any case, I believe if poor Jasmine is not feeling well enough to join--ah, and she did {i}so{/i} well during her tryouts, too, she was {i}such{/i} a threat--she'll have to be considered a drop?"

pause 2.0

grusha tears @sadbrow talking2mouth "[ellipses]You don't know Jasmine. Someone like you couldn't, ever, {i}ever{/i} know her."
grusha @angrybrow "Everything she does is to help other people. When she coordinates, it's not for glory, it's to make other people happier. She wrote this song to--to--"

phobos @talking2mouth "Yes, yes, yes, I'm sure it's lovely, what a damn shame we'll never get to hear it, etc., etc., etc."
phobos @upeyes talking2mouth "Leave, now, if you please. I can't have {i}more{/i} rabble barging in while I'm trying to oust the old."

pause 2.0

grusha -angrymouth @talking2mouth "We {i}are{/i} going to hear her song."

pause 2.0

phobos @angrybrow shadow angrysharkmouth "{i}Not{/i} in her current state. She can hardly {i}whisper{/i}, never mind sing."

grusha @angrymouth "I didn't say {i}she{/i} was going to sing it. I watched her practice for this for weeks. I remember every line. I remember every note. I remember the feelings she wanted to share with everyone. And {i}I'll{/i} be the one to do it."

phobos angrysharkmouth "Again?! If you so much as open your mouth--!"

grusha @talking2mouth "What was it you coordinators called it? A 'showcase'? I challenge you, {i}hijo de perra!{/i}"

$ BeginKaraokeBattle("coldmetal.ogg")

show screen karaoke_overlay

python:
    trainer1 = MakeTrainer("grusha", TrainerType.Player)
    trainer2 = MakeTrainer("phobos", TrainerType.Enemy)
    
    if (not HasEvent("Lawrence", "Tyrannic")):
        for mon in GetTrainerTeam("Phobos"):
            if (mon.GetNickname() in phobosteam):
                if (phobosteam[mon.GetNickname()] == "KO'd"):
                    mon.ApplyStatus("demotivated")

    if (HasEvent("Lawrence", "Hard")):
        for mon in trainer2.GetTeam():
            mon.UpdateLevel(30, updateMoves = False, force=True)
        GetTrainerTeam("Phobos", "Combee").Foreverals = ["Vespiquen Uneveral"]
        GetTrainerTeam("Phobos", "Dodrio").Foreverals = ["Dodrio Overal"]
    elif (HasEvent("Lawrence", "Tyrannic")):
        for mon in trainer2.GetTeam():
            mon.UpdateLevel(33, updateMoves = False, force=True)
        GetTrainerTeam("Phobos", "Combee").Foreverals = ["Vespiquen Uneveral"]
        GetTrainerTeam("Phobos", "Dodrio").Foreverals = ["Dodrio Overal"]


call Battle([trainer1, trainer2], customexpressions=["grusha noscarf sweat angrybrow frownmouth", "grusha tears closedbrow talking2mouth", "phobos angrybrow frownmouth anger", "phobos angrybrow angrysharkmouth anger2"], gainexp=False, specialmusic="audio/music/vocals/coldmetal.ogg", stopmusic=True, lockbag=True, dialogfunc=phobospeanutgallery, customswitchbrain=phobosswitchbrain, healParty=False) from _call_Battle_197
$ RecordBattle("Phobos2")
queue music "audio/music/lawrencetheme_start.ogg" noloop
queue music "audio/music/lawrencetheme_loop.ogg"

hide screen karaoke_overlay

$ EndKaraokeBattle()

python:
    for mon_name in ["Tatsugiri", "Combee", "Wugtrio", "Dodrio", "Iron Jugulis"]:
        mon = GetTrainerTeam("Phobos", mon_name, False)
        if mon.GetFaintedTurn() > 0:
            phobosteam[mon_name] = "KO'd"

if (WonBattle("Phobos2")):
    show phobos surprisedbrow frownmouth
    show grusha noscarf winkbrow sweat angrymouth:
        xpos 0.51
    with dis
else:
    show phobos shadow frownmouth angrybrow anger
    show grusha noscarf winkbrow sweat angrymouth:
        xpos 0.51
    with dis

$ LineUp(exclude="phobos", prefilled=[0.5, 0.51], considerexcludes=True)

if (WonBattle("Phobos2")):
    phobos @talking2sharkmouth "{size=30}What? Not even a coordinator, and[ellipses]?{/size}"

    phobos angrybrow shadow frownmouth anger @closedbrow sweat talking2sharkmouth "{size=30}No, no, no.{/size} A fluke, just a fluke, only a fluke!"

phobos @talking2sharkmouth "{i}Enough{/i} of these interruptions!"

ethan @upeyes talking2mouth "What are we interrupting? It's not like--"

$ GroupExpression("surprisedbrow frownmouth", exclude="phobos")

phobos @angrysharkmouth "Shut up, shut up, shut up! Everyone, just--just--just {i}go away!{/i} This contest is over! Cancelled! {i}None of you{/i} get to participate! And you are {i}all{/i} expelled!"

pause 1.5

$ GroupExpression("angrybrow frownmouth", exclude="phobos")

brendan @talking2mouth "You can't do that, sir."

phobos @angrysharkmouth "Yes I {i}can!{/i} I can do whatever I want! My money is embedded in every brick of this castle! Kobukan is {i}mine!{/i}"
phobos @angrysharkmouth "I control Drayden! He won't dare raise a finger against {i}me{/i}, while I have Melody under my thumb!"
phobos @angrysharkmouth "I'm untouchable! And you're {i}really{/i} beginning to irritagonize me!"

scene blank2 with splitfade

pause 0.5

narrator "Meanwhile, backstage, Yellow has been working on Melody[ellipses]"

scene concerthallbackstage 
show melody contest on pissedbrow pissedmouth:
    xpos 0.33
show yellow contest sadbrow frownmouth:
    xpos 0.66
with splitfade

yellow @talking2mouth "Just--just {i}look{/i} at what Phobos is doing! He's forcing everyone out of the contest so you can win, but he isn't even letting you participate!"

melody @talking2mouth "You have {i}no{/i} idea what's going on here. This isn't about the stupid contest."

pause 0.5

yellow @talking2mouth "I know it isn't for him. But you[ellipses] you don't really think this is a stupid contest. It {i}is{/i} about the contest for you."
yellow @sad2brow talking2mouth "At least a bit."

melody @talking2mouth "Uh-huh. How do you figure?"

pause 0.5 

show melody surprisedbrow frownmouth with dis

yellow @talking2mouth "Why would someone who isn't planning to participate in the contest dress up, and do her hair?"

show melody disgustedbrow blush pissedmouth with dis

pause 0.5

melody @talking2mouth "Force of habit."

yellow @talking2mouth "You {i}accidentally{/i} put on a beautiful dress, straightened and shampooed your hair, and came backstage? For Phobos' plan, you don't even need to be here, do you? You could just be in your dorm."

melody -blush @talking2mouth "Just stop. {i}Stop.{/i} I'm not on your side. Get it? I {i}want{/i} Phobos to get away with this. I {i}want{/i} all of you to be disappointed."

yellow @angrybrow talking2mouth "No you {i}don't!{/i} You {i}want{/i} to go out on stage, and sing, and dance, and {i}really{/i} compete! You want it so much it's killing you!"

show melody:
    xpos 0.33
    ease 0.2 xpos 0.6

show yellow: 
    xpos 0.66
    pause 0.05
    ease 0.7 xpos 0.75
    
melody angrybrow angrymouth "What the hell do you think you know about me?"

yellow @talking2mouth "That's {i}all{/i} I know about you.{w=0.5} But I know I'm right."

pause 0.5

melody @talking2mouth "Even if I {i}do{/i} go out there, and I sing, Phobos still wins. He gets what he wants. Even if I don't win, he does. Men like him {i}always{/i} win."

yellow @talking2mouth "I don't care. All I care about is that {i}you{/i} get what {i}you{/i} want."

pause 0.5

show melody noglasses sadbrow frownmouth with dis:
    xpos 0.6
    ease 1.0 xpos 0.5

melody @talking2mouth "I don't--"

$ GroupExpression("surprisedbrow frownmouth")

$ hideside = True

show concerthallbackstage with vpunch

phobos @shadow frownmouth angrybrow anger angrysharkmouth "{size=30}I control Drayden, and he won't dare raise a finger against {i}me{/i}, while I have Melody under my thumb!{/size}"

pause 1.0

$ hideside = False

melody -surprisedbrow @disgustedbrow hatlessshadow talking2mouth "Oh."
melody angrybrow @angrybrow talking2mouth hatlessshadow "So {i}that's{/i} how he sees it, huh?"
melody @disgustedbrow talkingmouth "Fine, blondie. Let's have a talk with my {i}uncle{/i}."

pause 0.5

melody @talking2mouth "You too, [melody_name]."

red @upeyes angryeyebrows talking2mouth "Oh, great, you remembered I'm here."

if (melody_name != first_name):
    $ MoveOutSmart("melody")
    $ MoveOutSmart("yellow")

    red @sad2eyes angryeyebrows talking2mouth "{size=30}And my name's not [melody_name].{/size}"

scene concerthallstagenight 
show blank2 zorder 1000
with splitfade

pause 1.0

show leaf angrybrow frownmouth behind blank2:
    xpos -0.3
show ethan angrybrow frownmouth behind blank2:
    xpos -0.2
show blue angrybrow frownmouth behind blank2:
    xpos -0.1
show grusha noscarf angrybrow frownmouth behind blank2:
    xpos 0.1
show brendan contest angrybrow frownmouth behind blank2:
    xpos 0.2
show may contest angrybrow frownmouth behind blank2:
    xpos 0.3
show phobos anger2 frownmouth angrybrow behind blank2
$ LineUp(0, exclude="phobos", prefilled=[0.5], considerexcludes=True)

hide blank2 with splitfade

phobos @angrysharkmouth "{gradualsize=20-36}[ellipses]Every single one of you! Expelled! Let go! Released! I shan't have my crowning moment of triumph delayed one second further!{/gradualsize}"

melody contest on @talking2mouth "Yo, unc."

phobos -anger2 frownmouth surprisedbrow@surprisedbrow talking2sharkmouth "Melo--{i}why?!{/i} Why are you {i}here?!{/i} Why are you {i}dressed?!{/i}"

melody on @disgustedbrow talking2mouth "[ellipses]Phrasing?"
melody @talking2mouth angrybrow "This wasn't the deal." 

pause 0.5

melody @talking2mouth "Clear the stage. I'm talking with Phobos."

$ MoveOutSmart(["leaf", "ethan", "blue", "grusha", "brendan", "may"])

pause 0.5

$ MoveInSmart("melody contest angrybrow frownmouth", maintain=True)

pause 0.1

$ MoveInSmart(("yellow sadbrow frownmouth" if not yellowin else "yellow contest sadbrow frownmouth"))

$ smalltalks = [("Blue", "Wait, why did we listen to her?")]

phobos @talking2mouth "Melody--"

melody @talking2mouth "I'm talking. You're not."

pause 0.5

melody @talking2mouth "Just let me--{i}us{/i} perform."
melody @talking2mouth "I win, you get your trophy, and everyone still here gets a show. What's the problem?"

phobos -surprisedbrow @unamusedbrow "[ellipses]"

pause 0.333

show melody surprisedbrow
show yellow -sadbrow 
with dis

phobos @talking2sharkmouth closedbrow "You are not {i}nearly{/i} as good a coordinator as you think you are."
phobos @talking2sharkmouth upeyes angryeyebrows "Did you {i}really{/i} think I would let my master plan hinge on the performance of a broken schoolgirl?"
phobos @talking2sharkmouth "I'm afraid you've an overinflated sense of self-importance."

red @surprisedbrow frownmouth "[ellipses]"
red @surprisedbrow talking2mouth "{size=30}Hey, Ethan? Did I miss something? Why's he talking about master plans, now?{/size}"

ethan @confusedbrow talking2mouth "{size=30}Well, he'd kinda been going down the 'megalomaniacal crash' spiral for the past ten minutes or so--we've all been expelled--but this part's new.{/size}"

pause 0.5

ethan @talking2mouth angrybrow shadow "{size=30}But this might be serious.{/size}"

leaf @talking2mouth angrybrow "{size=30}Yeah. Grusha says he hurt Jasmine.{/size}"

red @angrybrow talking2mouth "{i}What?{/i}"

melody up @pissedbrow talkingmouth "Tch. What kind of stupid bluff is this? You need me to win the contest. That's the entire reason you brought me back into the school. You need me to sing."

show yellow angrybrow with dis

phobos @upeyes talking2sharkmouth "No, you stupid child, I needed you to get Wallace and Lisia to leave for Hoenn, and I needed Drayden to be powerless to raise a finger against me for the past two weeks."
phobos @talking2sharkmouth "Besides, there's a thousand other people who can sing just as well as you. I hardly need {i}you{/i} for that last step. I could most likely just dangle my wallet in front of Lisia, and there's little she wouldn't do for me."
phobos @happybrow happysharkmouth "Did you think I would achieve my goals in so pedestrian a fashion as 'winning'? Hah! I create the game, I don't {i}play{/i}!"

leaf @angrybrow talking2mouth "{size=30}Ethan, look up how to perform a citizen's arrest.{/size}"

ethan @confused "{size=30}Seriously?{/size}"

leaf @angrybrow talking2mouth "{size=30}Do I {i}look{/i} like I'm joking?{/size}"

blue @talking2mouth angrybrow "{size=30}{i}Please{/i} tell me it involves battling the person you're arresting.{/size}"

melody @talking2mouth "[ellipses]What?"

phobos @talkingsharkmouth "Yes, yes, yes, {i}finally!{/i} I was waiting for this moment--ah, ah, ah, the grand reveal!"
phobos @angrybrow angrysharkmouth "{i}Weeks{/i} of putting up with your horrendous attitude, your constant whining, your woe-is-me whinging, {i}finally!{/i}"
phobos @talking2sharkmouth "You've served your purpose. You can go."

melody @talking2mouth "You said you'd grant my wish."

phobos @winkbrow talkingsharkmouth "It's called acting, dear."

pause 3.0

melody @talking2mouth "Okay."
melody @talking2mouth "Fine."
melody @talking2mouth "Deal's off, then."

pause 3.0

show melody at highlightmove(0.5, 0.5, "right")

show concerthallstagenight at vpunch

melody angrybrow angrymouth "This man is a {i}terrorist!{/i}"

pause 0.5

ethan @surprisedbrow talking2mouth "{size=30}That's not the way I saw this going.{/size}"

melody @talking2mouth "Well?! {w=0.5}[first_name], Blue, Leaf, that other one! You guys are Battle Team members! Stop him!"

leaf @surprisedbrow talking2mouth "No, no, don't get me wrong, we're totally down, but what exactly are we trying to stop?"

phobos angrybrow frownmouth @happysharkmouth happybrow "My master plan! You see, when I--"

melody @talking2mouth "The trophy's a mythical Pokémon chrysalis, he's trying to steal it and use it for something bad."

phobos @talking2sharkmouth "This is why {i}nobody{/i} likes you, Melody."

blue @talking2mouth "Alright, Phobos. Get out your Poké Balls. We're going to settle this--"

$ GroupExpression("surprisedbrow frownmouth", exclude="yellow")

yellow angrybrow @talking2mouth "No."

pause 2.0

$ LineUp()

phobos @talking2mouth "The mouse speaks?"

melody @talking2mouth "What do you mean, no? Someone {i}needs{/i} to stop him!"

yellow @talking2mouth "And {i}someone{/i} will."

pause 1.0

melody @talking2mouth "The four--{w=0.5}count them, four--{w=0.5}Battle Team members?"

yellow @talking2mouth "It needs to be you. You let him get this far, so {i}you{/i} need to stop him."

pause 1.0

melody @talking2mouth "Um. I {i}can't{/i} do that."

pause 1.0

yellow @talking2mouth "Who told you that?"

melody @talking2mouth "What--what do you mean?"

yellow @talking2mouth "Did Phobos tell you that? If so, do you have any reason to believe him?"
yellow @talking2mouth "Sometimes, people[ellipses] we tell ourselves we {i}can't{/i} do something, so we don't need to try."
yellow @talking2mouth "But we can. And we should! And we {i}must!{/i} It doesn't matter if someone else can do it! {i}We{/i} have to!"

pause 1.0

show melody -surprisedbrow:
    xzoom 1
    ease 0.5 xzoom -1
    pause 2.0
    ease 0.5 xzoom 1
    pause 2.0
    ease 0.5 xzoom -1

pause 5.5

show phobos angrysharkmouth angrybrow shadow anger2 with dis

melody closedbrow frownmouth noglasses @talkingmouth "Eff it, I'll try."

phobos "Mel--{nw}"

$ BeginKaraokeBattle("melody.ogg")

hide yellow
show screen karaoke_overlay
with dis

python:
    trainer1 = MakeTrainer("melody", TrainerType.Player)
    trainer2 = MakeTrainer("phobos", TrainerType.Enemy)

    if (not HasEvent("Lawrence", "Tyrannic")):
        for mon in GetTrainerTeam("Phobos"):
            if (mon.GetNickname() in phobosteam):
                if (phobosteam[mon.GetNickname()] == "KO'd"):
                    mon.ApplyStatus("demotivated")

    if (HasEvent("Lawrence", "Hard")):
        for mon in trainer2.GetTeam():
            mon.UpdateLevel(30, updateMoves = False, force=True)
        GetTrainerTeam("Phobos", "Combee").Foreverals = ["Vespiquen Uneveral"]
        GetTrainerTeam("Phobos", "Dodrio").Foreverals = ["Dodrio Overal"]
    elif (HasEvent("Lawrence", "Tyrannic")):
        for mon in trainer2.GetTeam():
            mon.UpdateLevel(33, updateMoves = False, force=True)
        GetTrainerTeam("Phobos", "Combee").Foreverals = ["Vespiquen Uneveral"]
        GetTrainerTeam("Phobos", "Dodrio").Foreverals = ["Dodrio Overal"]

call Battle([trainer1, trainer2], customexpressions=["melody contest noglasses angrybrow frownmouth", "melody contest noglasses angrybrow smilemouth", "phobos angrybrow frownmouth anger", "phobos angrybrow angrysharkmouth anger2 shadow"], gainexp=False, specialmusic="audio/music/vocals/melody.ogg", stopmusic=True, lockbag=True, dialogfunc=phobospeanutgallery, customswitchbrain=phobosswitchbrain, healParty=False) from _call_Battle_198
$ RecordBattle("Phobos3")
queue music "audio/music/lawrencetheme_start.ogg" noloop
queue music "audio/music/lawrencetheme_loop.ogg"

hide screen karaoke_overlay

$ EndKaraokeBattle()

python:
    for mon_name in ["Tatsugiri", "Combee", "Wugtrio", "Dodrio", "Iron Jugulis"]:
        mon = GetTrainerTeam("Phobos", mon_name, False)
        if mon.GetFaintedTurn() > 0:
            phobosteam[mon_name] = "KO'd"

if (WonBattle("Phobos3")):
    show phobos angrybrow frownmouth anger2 shadow:
        xpos 0.33
    show melody up smilemouth contest:
        xpos 0.66 xzoom -1
    with dis
else:
    show phobos shadow frownmouth angrybrow anger:
        xpos 0.33
    show melody up smilemouth sadbrow contest:
        xpos 0.66 xzoom -1
    with dis

melody "[ellipses]{nw}"
extend @talkingmouth "Honestly, I missed that."

phobos @talking2sharkmouth "So now even {i}you{/i} betray me, Melodious Ball."

melody -sadbrow -smilemouth @talking2mouth "That's literally not my name."

phobos @closedbrow talking2sharkmouth "{size=30}Fine, fine, fine.{/size} If you all refuse to {i}listen{/i} to me, then I'll simply have to {i}deafen{/i} you!"

brendan contest @talking2mouth "{size=30}Um, I called the Rangers. I'm pretty sure Phobos is having a psychedelic episode, so I think we should get some doctors or nurses or EMS or somethin' here.{/size}"

may contest @talking2mouth "{size=30}It's 'psychotic episode,' sweetie. {/size}{nw}"
extend @happy "{size=30}But good thinking!{/size}"

show phobos:
    xpos 0.33 ypos 1.0
    parallel:
        ease 2.2 ypos 0.985
        ease 2.2 ypos 1.0
        repeat
    parallel:
        ease 3.0 xpos 0.338
        ease 3.0 xpos 0.322
        ease 3.0 xpos 0.33
        repeat

phobos goggles @angrybrow talking2sharkmouth "{i}STOP{/i} IGNORING ME!"

phobos @talking2sharkmouth "{gradualsize=36-40}Fine! Fine! {i}Fine!{/i}{/gradualsize} If you all want to ruin my show, I'll do what I could have done three weeks ago and just {i}steal{/i} the trophy!"

ethan @confused "Wait, why {i}didn't{/i} you just--"

phobos anger2 shadow angrysharkmouth "Because I {i}HATE{/i} you!"
phobos "You, Battle Team members who tormented and mocked and ruined me for daring to dream that Pokémon could be used for glory outside of battle!"
phobos "You, coordinators who tried to keep me from the contest world for the crime of being a man, then turned your backs on me when I could no longer perform!"
phobos "You, Kobukan students who will graduate into perfect lives, never knowing what it's like to lose everything and have to rebuild it all from a single trading card!"
phobos "{gradualsize=36-40}I hate you, I hate you, {i}I hate you!{/i}{/gradualsize}"

show phobos:
    xpos 0.33
    ease 0.3 xpos 1.2

show melody surprisedbrow surprisedmouth:
    xpos 0.66
    parallel:
        ease 0.3 xpos 0.8
    parallel:
        ease 0.6 rotate 2
    pause 0.5
    ease 0.5 xpos 0.66 xzoom 1

pause 1.5

melody angrybrow angrymouth "Get your hands off that trophy!"

hide phobos

$ SmartMoveOut("melody")

show millenniumtrophy at itemhover

narrator "You, Melody, and Yellow run toward Phobos, as his hand touches the rim of the trophy, when, suddenly[ellipses]"

stop music fadeout 1.5

$ Pokemon("Deoxys").PlayCry()

queue music "audio/music/deoxys_start.ogg" noloop
queue music "audio/music/deoxys_loop.ogg"

redmind @surprisedbrow frownmouth "[ellipses]Shit! What's AZOTH1 doing here?! {i}Now?!{/i}"
redmind @confused "Wait, where is it?"

pause 0.5

narrator "You look up."

brendan @surprised "Not again!"

call clearscreens() from _call_clearscreens_288

show brendanhasaflashback with Dissolve(3.0)

narrator "Descending from the sky like an avenging angel is, unmistakably, the figure of AZOTH1."

brendan @surprisedbrow sweat angrymouth "Gah... everyone, get behind me!"

redmind @wince angrymouth "I thought Nate--I thought he {i}did{/i} something with it! I didn't know what, but I didn't think I'd be seeing it again!"

TempCharacter("{gradient=#EC5124-#0B98B4}AZOTH1{/gradient}") "{font=fonts/alien.ttf}Deoxys.{/font}"

redmind @surprisedbrow frownmouth "Wait, does Brendan--did he say 'not again'? Does he know about AZOTH1?"

red @talking2mouth "Brendan, you know this thing?"

brendan @sadbrow talking2mouth "Yeah, Hoenn nearly blew up four years ago because of it! It was inside a big meteor, and--"

blue @scaredeyes angryeyebrows furiousmouth "Literally {i}none{/i} of that matters! We're stopping Phobos! We can handle the freaky-looking Pokémon later!"

red @surprisedbrow surprisedmouth "Wait, no! Blue, you don't understand, this thing's {i}really{/i} powerful!"

hide phobos

phobos @angrybrow happysharkmouth "Oh, fantastic! All three prizes in one place! I'll go ahead and take them {i}all{/i}!"

hide brendanhasaflashback with dis

narrator "Faster than your eyes can track, AZOTH1 flies over to Phobos and snatches the trophy from him."

show millenniumtrophy:
    xalign 0.5 yalign 0.5 zoom 0.75 rotate 0
    pause 0.5
    parallel:
        ease 0.25 rotate 360
        ease 0.25 rotate 0
        repeat
    parallel:
        ease 0.3 xpos 600 ypos 100 zoom 0.5
        ease 0.5 xpos 550 ypos 700 zoom 0.1
    parallel:
        ease 0.15 alpha 1.0
    parallel:
        pause 0.55
        ease 0.25 alpha 0.0

TempCharacter("{gradient=#EC5124-#0B98B4}AZOTH1{/gradient}") "{font=fonts/alien.ttf}D E O X Y S.{/font}"

yellow @talking2mouth sadbrow "They're[ellipses] they're being chased. Someone is trying to take their treasure. Is[ellipses] what's your treasure, Azoth?"

scene blank with transeye2

pause 1.0

call clearscreens() from _call_clearscreens_289
scene forest3 at sepia
show fulldeoxys at sepia:
    xanchor 0.6 xpos 0.5 xzoom -1 zoom .8 ypos 1.2 yanchor 1.0
    parallel:
        linear 0.1 xpos 0.51
        linear 0.1 xpos 0.5
        pause 4.0
        linear 0.1 xpos 0.49
        linear 0.1 xpos 0.5
        pause 4.0
        repeat
    parallel:
        ease 1.5 ypos 1.2
        ease 1.5 ypos 1.23
        ease 1.5 ypos 1.2
        ease 1.5 ypos 1.17
        repeat
show flashback

$ PlaySound("pokemon/cries/386.mp3")

TempCharacter("{gradient=#EC5124-#0B98B4}AZOTH1{/gradient}") "{font=fonts/alien.ttf}Deoxys.{/font}"

pause 1.0

nate @talking2mouth "AZOTH1. What are your intentions with this planet?"

show fulldeoxys at sepia:
    ease 0.5 xzoom -1
    parallel:
        linear 0.1 xpos 0.51
        linear 0.1 xpos 0.5
        pause 3.0
        linear 0.1 xpos 0.49
        linear 0.1 xpos 0.5
        pause 3.0
        repeat
    parallel:
        ease 1.0 ypos 1.2
        ease 1.0 ypos 1.23
        ease 1.0 ypos 1.2
        ease 1.0 ypos 1.17
        repeat

TempCharacter("{gradient=#EC5124-#0B98B4}AZOTH1{/gradient}") "{font=fonts/alien.ttf}Deoxys.{/font}"

python:
    removedautocontest = []
    if (HasEvent('Yellow', 'AutoContest')):
        RemoveEvent("Yellow", "AutoContest")
        removedautocontest.append("Yellow")
    if (HasEvent("Game", 'AutoContest')):
        RemoveEvent("Game", "AutoContest")
        removedautocontest.append("Red")

yellow @surprised "They're... they're afraid. They're running from something. A 'bad person.'"

redmind @surprisedbrow frownmouth "Wait... isn't that what Tia, said, too?"

show fulldeoxys at sepia:
    ease 0.5 xzoom 1
    parallel:
        linear 0.1 xpos 0.51
        linear 0.1 xpos 0.5
        pause 2.0
        linear 0.1 xpos 0.49
        linear 0.1 xpos 0.5
        pause 2.0
        repeat
    parallel:
        ease 0.5 ypos 1.2
        ease 0.5 ypos 1.23
        ease 0.5 ypos 1.2
        ease 0.5 ypos 1.17
        repeat

TempCharacter("{gradient=#EC5124-#0B98B4}AZOTH1{/gradient}") "{font=fonts/alien.ttf}D E O X Y S.{/font}"

yellow @sadbrow talking2mouth "They're... they're being chased. Someone is trying to take their treasure. Is... what's your treasure, Azoth?"

TempCharacter("{gradient=#EC5124-#0B98B4}AZOTH1{/gradient}") "{font=fonts/alien.ttf}Deoxys.{/font}"

pause 1.0

nate @talking2mouth "Well?"

yellow @sadbrow talking2mouth "I don't... I don't understand. They're becoming agitated."

$ PlaySound("pokemon/cries/386.mp3")

show fulldeoxys at sepia:
    ease 0.5 xzoom -1
    parallel:
        linear 0.1 xpos 0.51
        linear 0.1 xpos 0.5
        pause 1.0
        linear 0.1 xpos 0.49
        linear 0.1 xpos 0.5
        pause 1.0
        repeat
    parallel:
        ease 0.5 ypos 1.2
        ease 0.5 ypos 1.23
        ease 0.5 ypos 1.2
        ease 0.5 ypos 1.17
        repeat

nate @talking2mouth "AZOTH1! If you can understand me, I need you to surrender yourself into my custody. I'm a member of the--"

show fulldeoxys at sepia:
    ease 0.2 xpos 0.5 zoom 3 ypos 3.0 alpha 0.0

narrator "Suddenly, the strange creature lunges straight at [pika_name]!"

nate @surprised "Shit! [first_name], watch out!"

python:
    if ("Yellow" in removedautocontest):
        AddEvent("Yellow", "AutoContest")
    if ("Red" in removedautocontest):
        AddEvent("Game", "AutoContest")

scene concerthallstagenight with transeye
show fulldeoxys:
    xpos 0.5 xpos 0.5 yanchor 1.0 ypos 1.2
    parallel:
        linear 0.1 xpos 0.51
        linear 0.1 xpos 0.5
        pause 1.0
        linear 0.1 xpos 0.49
        linear 0.1 xpos 0.5
        pause 1.0
        repeat
    parallel:
        ease 0.5 ypos 1.2
        ease 0.5 ypos 1.23
        ease 0.5 ypos 1.2
        ease 0.5 ypos 1.17
        repeat

redmind @surprisedbrow frownmouth "Not again! It's going to--"

show blue:
    ease 0.2 xpos 0.33

show fulldeoxys:
    "images/Pokemon/fulldeoxyss.webp"
    ease 0.5 xpos 0.65 zoom 0.4 ypos 0.5

    parallel:
        linear 0.1 xpos 0.66
        linear 0.1 xpos 0.65
        pause 1.0
        linear 0.1 xpos 0.64
        linear 0.1 xpos 0.65
        pause 1.0
        repeat

    parallel:
        ease 0.5 ypos 0.5
        ease 0.5 ypos 0.53
        ease 0.5 ypos 0.5
        ease 0.5 ypos 0.47
        repeat

    parallel:
        pause 6.0

        linear 0.03 alpha 0.35 zoom 0.42 xpos 0.645
        linear 0.03 alpha 0.9 zoom 0.39 xpos 0.655
        linear 0.03 alpha 0.2 zoom 0.41 xpos 0.648
        "images/Pokemon/fulldeoxysa.webp"
        linear 0.05 alpha 1.0 zoom 0.4 xpos 0.65

        pause 6.0

        linear 0.03 alpha 0.35 zoom 0.42 xpos 0.655
        linear 0.03 alpha 0.9 zoom 0.39 xpos 0.645
        linear 0.03 alpha 0.2 zoom 0.41 xpos 0.652
        "images/Pokemon/fulldeoxysd.webp"
        linear 0.05 alpha 1.0 zoom 0.4 xpos 0.65

        pause 6.0

        linear 0.03 alpha 0.35 zoom 0.42 xpos 0.645
        linear 0.03 alpha 0.9 zoom 0.39 xpos 0.655
        linear 0.03 alpha 0.2 zoom 0.41 xpos 0.648
        "images/Pokemon/fulldeoxys.webp"
        linear 0.05 alpha 1.0 zoom 0.4 xpos 0.65

        pause 6.0

        linear 0.03 alpha 0.35 zoom 0.42 xpos 0.645
        linear 0.03 alpha 0.9 zoom 0.39 xpos 0.655
        linear 0.03 alpha 0.2 zoom 0.41 xpos 0.648
        "images/Pokemon/fulldeoxyss.webp"
        linear 0.05 alpha 1.0 zoom 0.4 xpos 0.65

        repeat

blue @talkingmouth "Oh, no, you {i}don't!{/i}"

pause 1.0 

redmind @unamusedbrow unamusedmouth "Oh, right. Yeah, Blue {i}would{/i} leap into battle again, wouldn't he?"

show phobos goggles shadow angrybrow anger2 angrysharkmouth:
    xpos 1.2
    ease 0.2 xpos 0.66

phobos "Get away from the alien! It's mine!"

show melody contest angrybrow angrymouth:
    xpos -0.2
    ease 0.5 xpos 0.5

pause 0.5

$ LineUp()

melody "You're not getting that trophy, Phobos!"

leaf @angrybrow talking2mouth "Blue, don't rush in!"

may contest @surprisedbrow talking2mouth "Are you--oh my god, babe, are you okay?!"

brendan contest @surprisedbrow surprisedmouth noshine sweat "It's back--it's back, and we don't--there's no-one to--"

grusha @winkeyes sadeyebrows noscarf sweat talking2mouth "{size=30}Oh, {i}mierda{/i}, this is going to be the one[ellipses] Jasmine, {i}lo siento[ellipses]{/i}{/size}"

pause 2.0

narrator "{glitch=5.00}There's a whirlwind of chaos around you.{/glitch}"
narrator "{glitch=10.00}The shouting of a dozen different parties all pursuing their own goals raises into a cacophonic scream.{/glitch}"
narrator "{glitch=15.00}In the center of the whirlwind is Phobos, a tyrant who used what little power he has to make other people's lives worse.{/glitch}"
narrator "{glitch=20.00}The scream echoes in your ears[ellipses]{/glitch}"

pause 1.0

if (IsCoordinator()):
    narrator "Normally, you wouldn't hesitate to throw yourself into battle."
    narrator "However, after several weeks immersing yourself in coordinating--a fairer art, though Phobos' pretensions do it no justice--you wonder if there is, perhaps, a situation you are more immediately suited to."

    pause 0.5

    narrator "How does one protect? With spear or open palm?"

    menu:
        ">Defeat Phobos in a battle.":
            $ AddEvent("Game", "MillenniumClimaxBattle")

        ">Calm down Deoxys in a contest.":
            $ AddEvent("Game", "MillenniumClimaxContest")

$ PlaySound("Pokemon/pikachu_angry3.ogg")

libpikachu glowing angry sparks "Piii[ellipses] Pika!"

show screen currentdate

if (HasEvent("Game", "MillenniumClimaxContest")):
    show yellow surprisedbrow frownmouth with dis

    $ HighlightCharacter("yellow", extras="surprisedbrow frownmouth")

    red @angrybrow talking2mouth "Yellow, I think we can calm down Deoxys."

    yellow "[ellipses]{nw}"
    extend @talkingmouth "Yeah. I was thinking the same thing."

    red @talking2mouth "Okay. Take the stage, Yellow."
    
else:
    red @angrybrow talking2mouth "We're going to battle Phobos."

    yellow @angrybrow talking2mouth "Okay. I'm going to calm down the Pokémon."

    red @talking2mouth "Good luck."

    yellow @angrybrow talking2mouth "You too."

if (HasEvent("Game", "MillenniumClimaxContest")):
    scene concerthallstagenight
    show fulldeoxys:
        xpos 0.65 zoom 0.4 ypos 0.5 yanchor 1.0

        parallel:
            linear 0.1 xpos 0.66
            linear 0.1 xpos 0.65
            pause 1.0
            linear 0.1 xpos 0.64
            linear 0.1 xpos 0.65
            pause 1.0
            repeat

        parallel:
            ease 0.5 ypos 0.5
            ease 0.5 ypos 0.53
            ease 0.5 ypos 0.5
            ease 0.5 ypos 0.47
            repeat

        parallel:
            pause 6.0

            linear 0.03 alpha 0.35 zoom 0.42 xpos 0.645
            linear 0.03 alpha 0.9 zoom 0.39 xpos 0.655
            linear 0.03 alpha 0.2 zoom 0.41 xpos 0.648
            "images/Pokemon/fulldeoxysa.webp"
            linear 0.05 alpha 1.0 zoom 0.4 xpos 0.65

            pause 6.0

            linear 0.03 alpha 0.35 zoom 0.42 xpos 0.655
            linear 0.03 alpha 0.9 zoom 0.39 xpos 0.645
            linear 0.03 alpha 0.2 zoom 0.41 xpos 0.652
            "images/Pokemon/fulldeoxysd.webp"
            linear 0.05 alpha 1.0 zoom 0.4 xpos 0.65

            pause 6.0

            linear 0.03 alpha 0.35 zoom 0.42 xpos 0.645
            linear 0.03 alpha 0.9 zoom 0.39 xpos 0.655
            linear 0.03 alpha 0.2 zoom 0.41 xpos 0.648
            "images/Pokemon/fulldeoxys.webp"
            linear 0.05 alpha 1.0 zoom 0.4 xpos 0.65

            pause 6.0

            linear 0.03 alpha 0.35 zoom 0.42 xpos 0.645
            linear 0.03 alpha 0.9 zoom 0.39 xpos 0.655
            linear 0.03 alpha 0.2 zoom 0.41 xpos 0.648
            "images/Pokemon/fulldeoxyss.webp"
            linear 0.05 alpha 1.0 zoom 0.4 xpos 0.65

            repeat

    show melody contest surprisedbrow up frownmouth:
        xpos 0.2
    show brendan contest surprisedbrow noshine surprisedmouth sweat:
        xpos 0.4 xzoom -1
    show may contest sadbrow surprisedmouth:
        xpos 0.6
    show grusha winkeyes angryeyebrows noscarf sweat angrymouth:
        xpos 0.8
    with splitfadefast

    yellow @talking2mouth "Listen to me, everyone! {nw}"

    show brendan -noshine frownmouth
    show may frownmouth
    show grusha surprisedbrow frownmouth
    with dis

    extend @talking2mouth "We need to {i}sing!{/i}"

    pause 1.5
    
    grusha @talking2mouth "Are you insane?"

    #Pokémon Ranger musical mind-control devices
    #Pokéflute
    #The mental monologue of Pokémon being music notes
    yellow @talking2mouth "No! Pokémon are musical creatures. Music speaks to them like nothing else--it's the best way of getting our feelings across to it!"

    melody @talking2mouth "It's true. Shamouti priestesses have used music to communicate with the Silver Deepness for centuries. And she's still a Pokémon."

    brendan @angrybrow angrymouth "That {i}thing{/i} ain't a Pokémon! It's a--a--it's a threat!"

    yellow @angrybrow talking2mouth "Fine, you can believe that. But sing it! Let it know {i}why{/i} you're scared of it! Let it know how you feel! Everyone, you need to {i}communicate{/i} with the Pokémon!"

    pause 1.0

    may @talkingmouth "In {i}song?{/i}"

    show fulldeoxys:
        "images/Pokemon/fulldeoxyss.webp"
        ease 0.3 xpos 0.65 ypos 0.5 zoom 0.4 alpha 1.0

        easein 0.18 xalign 0.63 ypos 0.6 zoom 0.48
        easein 0.22 xalign 0.60 ypos 1.05 zoom 0.75
        easein 0.20 xalign 0.5 zoom 1.25 alpha 0.0
    
    $ GroupExpression("surprised")
    $ LineUp(inner_band = 0.2)

    show concerthallstagenight with vpunch

    yellow @scaredeyes sadeyebrows surprisedmouth "Unless you want it to bring the contest coliseum down on us, yes!"

    scene blank2 with splitfade

    narrator "You need to sing your feelings to the Pokémon to calm it down."
    narrator "It has some history with Hoenn, according to Brendan, so it will probably appreciate seeing Pokémon from Hoenn."
    narrator "It's not clear what type it is, but life, sea, and sky, are planetary constants--so Ghost, Water, and Flying-types should make good ambassadors for Earth."
    narrator "Finally, you're not trying to scare this thing, so cute or beautiful Pokémon should perform well here."

    pause 2.0

    narrator "With everyone singing at once, whose voice do you wish to focus on? (This will only affect the background music.)"

    label choosecontestgm:

    stop music fadeout 1.5

    menu:
        ">Brendan's Song of Love":
            play music "audio/music/vocals/brendan.wav"

        ">Grusha and Jasmine's Song of Rage":
            play music "audio/music/vocals/coldmetal.ogg"

        ">Melody's Song of Endurance":
            play music "audio/music/vocals/melody.ogg"

    narrator "Are you sure?"

    menu:
        "Yes.":
            pass

        "Nevermind.":
            jump choosecontestgm
            
    pause 2.0

    narrator "With that, let's open the curtain on the \"Don't Get Hit By a Wild Psycho Boost\" Festival Contest!"

    python:
        protaggroup = CoordinatorGroup([
            Coordinator("Yellow", condition=150, contestsprite=("contest" if yellowin else ""), iscontrollable=True)
        ])

        if (HasEvent("Game", "MillenniumClimaxContest")):
            protaggroup.Coordinators.append(Coordinator(first_name, condition=coordinatingknowledge, isprotag=True, iscontrollable=True, contestsprite="sweat contest"))

        coordinators = [
            protaggroup,
            CoordinatorGroup([
                Coordinator("Brendan", condition=387, partner=GetTrainerTeam("Brendan", "Wailmer"), contestsprite="sweat contest")
            ]),
            CoordinatorGroup([
                Coordinator("May", condition=250, partner=GetTrainerTeam("May", "Scorbunny"), contestsprite="blush contest")
            ]),
            CoordinatorGroup([
                Coordinator("Grusha", condition=50, partner=GetTrainerTeam("Grusha", "Delibird"), contestsprite="noscarf sweat lightblush")
            ]),
            CoordinatorGroup([
                Coordinator("Melody", condition=431, partner=GetTrainerTeam("Melody", "Lombre"), contestsprite="noglasses -on contest blush")
            ])       
        ]

        judges = [
            Judge(deoxysa, biases={ ContestMoveType.Cute : 30, ContestMoveType.Beautiful : 30, ContestMoveType.Cool : 30, ContestMoveType.Clever : 30, ContestMoveType.Tough : 30 }, customsex=Genders.Unknown),
            Judge(deoxyss, biases={ ContestMoveType.Cute : 30, ContestMoveType.Beautiful : 30, ContestMoveType.Cool : 30, ContestMoveType.Clever : 30, ContestMoveType.Tough : 30 }, customsex=Genders.Unknown),
            Judge(deoxysd, biases={ ContestMoveType.Cute : 30, ContestMoveType.Beautiful : 30, ContestMoveType.Cool : 30, ContestMoveType.Clever : 30, ContestMoveType.Tough : 30 }, customsex=Genders.Unknown)
        ]

        contestconditions = {
            "Types" : ["Water", "Flying", "Ghost"],
            "Region" : range(252, 387),#Hoenn
            "Traits" : [ContestMoveType.Beautiful, ContestMoveType.Cute]
        }

    call DeoxysContest("Don't Get Hit By a Wild Psycho Boost Festival Contest", coordinators, judges, contestconditions) from _call_DeoxysContest

    stop music
    queue music "audio/music/ocean waltz_start.ogg" noloop
    queue music "audio/music/ocean waltz_loop.ogg"

    scene concerthallstagenight
    show fulldeoxys:
        xpos 0.5 zoom 0.7 ypos 1.0 anchor (0.5, 1.0)

        parallel:
            linear 0.3 xpos 0.51
            linear 0.3 xpos 0.5
            pause 1.0
            linear 0.3 xpos 0.49
            linear 0.3 xpos 0.5
            pause 1.0
            repeat

        parallel:
            ease 0.5 ypos 1.0
            ease 0.5 ypos 1.03
            ease 0.5 ypos 1.0
            ease 0.5 ypos 0.97
            repeat
    with Dissolve(4.0)

    pause 2.0

    brendan surprisedbrow contest @talking2mouth "Did[ellipses] did we do it?"

    pause 1.0

    $ Pokemon("Deoxys").PlayCry()

    TempCharacter("{gradient=#EC5124-#0B98B4}AZOTH1{/gradient}") "{font=fonts/alien.ttf}Deoxys.{/font}"

    brendan @surprised "Ah!"

    yellow @talkingmouth "No, it's fine. They've calmed down. They say they're called 'Deoxys,' and they're trying to retrieve their power."
    yellow @sadbrow talking2mouth "Every human that's approached them has tried to capture or destroy them, so they panicked when they saw us, but they're peaceful."
    yellow @talkingmouth "If we just give them back their gems, then they'll leave."

    grusha @sweat confused noscarf "Then what the hell are we waiting for?"

else:
    show concerthallstagenight at vpunch
    
    $ HighlightCharacter("phobos")

    $ GroupExpression("surprisedbrow frownmouth -anger2")

    show phobos goggles

    red @shadow angrybrow angrymouth "PHOBOS!"
    red @angrybrow shadow talking2mouth "If you were really doing all this just to piss us off, well, you succeeded!"

    $ PlaySound("Pokemon/pikachu_angry3.ogg")
    libpikachu glowing angry sparks "Piii[ellipses] Pika!"

    show phobos neutraleyebrows neutraleyes talkingsharkmouth with dis

    red @talking2mouth shadow angrybrow "You're going to wish you hadn't."

    scene concerthallstagenight 
    hide semiblank2
    with dis

    python:
        AddEvent("Lawrence", "LiberationBattle")
        AddEvent("Game", "LiberationBattle")
        HealParty()
        trainer1 = MakeRed()
        trainer2 = MakeTrainer("phobos", TrainerType.Enemy)
        
        if (not HasEvent("Lawrence", "Tyrannic")):
            for mon in GetTrainerTeam("Phobos"):
                if (mon.GetNickname() in phobosteam):
                    if (phobosteam[mon.GetNickname()] == "KO'd"):
                        mon.ApplyStatus("demotivated")

        if (HasEvent("Lawrence", "Hard")):
            for mon in trainer2.GetTeam():
                mon.UpdateLevel(30, updateMoves = False, force=True)
            GetTrainerTeam("Phobos", "Combee").Foreverals = ["Vespiquen Uneveral"]
            GetTrainerTeam("Phobos", "Dodrio").Foreverals = ["Dodrio Overal"]
        elif (HasEvent("Lawrence", "Tyrannic")):
            for mon in trainer2.GetTeam():
                mon.UpdateLevel(33, updateMoves = False, force=True)
            GetTrainerTeam("Phobos", "Combee").Foreverals = ["Vespiquen Uneveral"]
            GetTrainerTeam("Phobos", "Dodrio").Foreverals = ["Dodrio Overal"]

    call Battle([trainer1, trainer2], healParty=False, customexpressions=["red angrybrow frownmouth", "red angrybrow happymouth", "phobos angrybrow goggles frownmouth", "phobos angrybrow goggles angrysharkmouth"], specialmusic=("audio/music/theme_start.ogg","audio/music/theme_loop.ogg"), dialogfunc=phobosbattledialog, customswitchbrain=phobosswitchbrain) from _call_Battle_199
    $ RecordBattle("Phobos3")

    scene concerthallstagenight 
    hide semiblank2
    with dis

    if (not WonBattle("Phobos3")):
        show phobos angrybrow happysharkmouth goggles with dis

        jump gameover

    show phobos surprisedbrow surprisedsharkmouth goggles with dis

    phobos "[ellipses]"
    phobos "No."
    phobos angrybrow angrysharkmouth"No,{w=0.5} no,{w=0.5} no! {w=0.5}No! {w=0.5}{nw}"

    show concerthallstagenight with vpunch

    extend "No! {w=0.5}{nw}"
        
    show concerthallstagenight with vpunch

    extend "No!"

    pause 2.0

    red @unamusedbrow talkingmouth "Yeah."

    phobos angrysharkmouth anger2 shadow angrybrow "You think this is the end, you filthy, penniless, luddite?! You can't begin to grasp the power Eternity wields!"

    red @talking2mouth "Stand down. You're going to prison, Sir."

    phobos "Stop {i}{b}ignoring{/b}{/i} me!"

stop music

call clearscreens() from _call_clearscreens_290
scene blank2

$ GetTrainerTeam("Phobos", "Iron Jugulis").HasAbility("Eternity's Weapon")

phobos @shadow anger2 talking2mouth "Weapon! Use {i}Hyper Beam!{/i}"

#narrator "As though in slow motion, you see the supposedly-fainted Hydreigon's mouth open, and a lurid beam of white flame erupts from it."
narrator "You instinctively throw yourself in front of [pika_name], but Phobos wasn't aiming for him."

label deoxysdemo:

scene concerthallstagenight
show fulldeoxys:
    anchor (0.5, 1.0) xpos 0.5 zoom 0.7 ypos 1.0

    parallel:
        linear 0.3 xpos 0.51
        linear 0.3 xpos 0.5
        pause 1.0
        linear 0.3 xpos 0.49
        linear 0.3 xpos 0.5
        pause 1.0
        repeat

    parallel:
        ease 0.5 ypos 1.03
        ease 0.5 ypos 1.0
        ease 0.5 ypos 0.97
        ease 0.5 ypos 1.0
        repeat 4

    parallel:
        pause 3.5
        ease 0.5 xzoom -1
with Dissolve(4.0)

pause 2.0

show blank behind fulldeoxys
show fulldeoxys:
    matrixcolor BrightnessMatrix(-1)

pause 0.05

show meteor as meteor1:
    xpos 1.15 ypos 1.15 rotate 90 matrixcolor BrightnessMatrix(-1)
    ease 0.2 xpos 0.47 ypos 0.22 zoom 0.75
    pause 1.5
    matrixcolor BrightnessMatrix(1.0) * SaturationMatrix(0.0)
    linear 0.3 xpos -0.5 ypos -0.5 zoom 0.3

show meteor as meteor2:
    xpos 1.15 ypos 1.15 rotate 90 matrixcolor BrightnessMatrix(-1)
    ease 0.24 xpos 0.47 ypos 0.22 zoom 0.75
    pause 1.5
    matrixcolor BrightnessMatrix(1.0) * SaturationMatrix(0.0)
    linear 0.3 xpos -0.5 ypos -0.5 zoom 0.3

show meteor as meteor3:
    xpos 1.15 ypos 1.15 rotate 90 matrixcolor BrightnessMatrix(-1)
    ease 0.26 xpos 0.47 ypos 0.22 zoom 0.75
    pause 1.5
    matrixcolor BrightnessMatrix(1.0) * SaturationMatrix(0.0)
    linear 0.3 xpos -0.5 ypos -0.5 zoom 0.3

show meteor as meteor4:
    xpos 1.15 ypos 1.15 rotate 90 matrixcolor BrightnessMatrix(-1)
    ease 0.28 xpos 0.47 ypos 0.22 zoom 0.75
    pause 1.5
    matrixcolor BrightnessMatrix(1.0) * SaturationMatrix(0.0)
    linear 0.3 xpos -0.5 ypos -0.5 zoom 0.3

show meteor as meteor5:
    xpos 1.15 ypos 1.15 rotate 90 matrixcolor BrightnessMatrix(-1)
    ease 0.30 xpos 0.47 ypos 0.22 zoom 0.75
    pause 1.5
    matrixcolor BrightnessMatrix(1.0) * SaturationMatrix(0.0)
    linear 0.3 xpos -0.5 ypos -0.5 zoom 0.3

pause 1.5
hide blank
show blank2 behind fulldeoxys

$ PlaySound("shatter.ogg")

$ spawn_deoxys_breakaway_directional(20)

show fulldeoxys:
    rotate_pad False matrixcolor BrightnessMatrix(1.0)
    ease 10.0 xpos 0.46 ypos 0.96 rotate 8

show millenniumtrophy:
    xcenter 0.55 ycenter 0.45 zoom 0.0 matrixcolor BrightnessMatrix(1.0) * SaturationMatrix(0.0)
    parallel:
        ease 1.0 zoom 0.3
    parallel:
        easein 5.0 ypos 0.3
        easeout 5.0 ypos 0.6
    parallel:
        ease 10.0 xpos 0.75 rotate 35
    parallel:
        pause 7.0
        linear 3.0 alpha 0.0

transform deoxys_shard_burst(
    dx_fast=0.2,
    dy_fast=0.0,
    dx_total=0.3,
    dy_total=0.0,
    start_zoom=0.25,
    end_zoom=0.20,
    start_rot=0.0,
    spin=90.0,
    delay=0.0,
    tint="#f00"):

    anchor (0.5, 0.5)
    xpos 0.52
    ypos 0.40
    zoom start_zoom
    rotate start_rot
    alpha 0.0

    # Makes the sprite read as a colored silhouette.
    matrixcolor TintMatrix(tint) * BrightnessMatrix(1.0) * ContrastMatrix(0.0)

    pause delay
    linear 0.03 alpha 1.0

    # Initial fast "blown away" motion.
    easeout 0.14 xpos (0.52 + dx_fast) ypos (0.40 + dy_fast) rotate (start_rot + spin * 0.35)

    # Slow-motion continued drift.
    linear 4.78 xpos (0.52 + dx_total) ypos (0.40 + dy_total) zoom end_zoom rotate (start_rot + spin)

    linear 0.18 alpha 0.0

init python:
    def spawn_deoxys_breakaway_directional(count=20, layer="master"):
        colors = ["#f00", "#00f", "#ff0"]

        # Bias outward from the impact, mostly upward/sideways.
        base_angles = [
            math.radians(160),
            math.radians(180),
            math.radians(200),
            math.radians(220),
            math.radians(240),
            math.radians(260),
            math.radians(280),
        ]

        for i in range(count):
            base = renpy.random.choice(base_angles)
            angle = base + renpy.random.uniform(-0.35, 0.35)

            total_dist = renpy.random.uniform(0.18, 0.42)
            fast_portion = renpy.random.uniform(0.08, 0.18)

            dx_fast = math.cos(angle) * fast_portion
            dy_fast = math.sin(angle) * fast_portion

            dx_total = math.cos(angle) * total_dist
            dy_total = math.sin(angle) * total_dist

            start_zoom = renpy.random.uniform(0.16, 0.30)
            end_zoom = start_zoom * renpy.random.uniform(0.8, 0.95)

            start_rot = renpy.random.uniform(0, 360)
            spin = renpy.random.uniform(-180, 180)
            delay = renpy.random.uniform(0.0, 0.06)
            color = renpy.random.choice(colors)

            renpy.show(
                "foreveral",
                at_list=[ deoxys_shard_burst(
                    dx_fast=dx_fast,
                    dy_fast=dy_fast,
                    dx_total=dx_total,
                    dy_total=dy_total,
                    start_zoom=start_zoom,
                    end_zoom=end_zoom,
                    start_rot=start_rot,
                    spin=spin,
                    delay=delay,
                    tint=color
                ) ],
                tag="deoxys_shard_%02d" % i,
                layer=layer,
                behind=["fulldeoxys"]
            )

pause 5.0

$ PlaySound("pokemon/cries/slowdeoxys.mp3", otherchannel="altcry")

hide fulldeoxys with gaussdissolve

pause 7.0

scene concerthallstagenight 
show phobos unamusedbrow goggles frownmouth 
with Dissolve(3.0)

queue music "audio/music/lawrencetheme_start.ogg" noloop
queue music "audio/music/lawrencetheme_loop.ogg"

phobos @talking2sharkmouth "Oh, that's {i}frustrating.{/i} I was trying to {i}capture{/i} it. Oh well, same ends, if unintended means, one supposes."

if (HasEvent("Game", "MillenniumClimaxContest")):
    phobos @talking2sharkmouth "To make matters worse, this elegant weapon Eternity furnished me with is broken now. Tch. It was supposed to last {i}much{/i} longer."

    $ HighlightCharacter("phobos")

    show phobos goggles surprisedbrow frownmouth with dis

    show concerthallstagenight at vpunch

    red @shadow angrybrow angrymouth "Phobos!"
    red @angrybrow shadow talking2mouth "If you were really doing all this just to piss us off, well, you succeeded!"

    show screen currentdate with dis

    $ PlaySound("Pokemon/pikachu_angry3.ogg")
    libpikachu glowing angry sparks "Piii[ellipses] Pika!"

    show phobos neutraleyes neutraleyebrows talkingsharkmouth with dis

    red @talking2mouth shadow angrybrow "You're going to wish you hadn't."

    hide fulldeoxys
    hide semiblank2
    with dis

    python:
        AddEvent("Lawrence", "LiberationBattle")
        AddEvent("Game", "LiberationBattle")
        HealParty()
        trainer1 = MakeRed()
        trainer2 = MakeTrainer("phobos", TrainerType.Enemy)
        
        if (not HasEvent("Lawrence", "Tyrannic")):
            for mon in GetTrainerTeam("Phobos"):
                if (mon.GetNickname() in phobosteam):
                    if (phobosteam[mon.GetNickname()] == "KO'd"):
                        mon.ApplyStatus("demotivated")

        if (HasEvent("Lawrence", "Hard")):
            for mon in trainer2.GetTeam():
                mon.UpdateLevel(30, updateMoves = False, force=True)
            GetTrainerTeam("Phobos", "Combee").Foreverals = ["Vespiquen Uneveral"]
            GetTrainerTeam("Phobos", "Dodrio").Foreverals = ["Dodrio Overal"]
        elif (HasEvent("Lawrence", "Tyrannic")):
            for mon in trainer2.GetTeam():
                mon.UpdateLevel(33, updateMoves = False, force=True)
            GetTrainerTeam("Phobos", "Combee").Foreverals = ["Vespiquen Uneveral"]
            GetTrainerTeam("Phobos", "Dodrio").Foreverals = ["Dodrio Overal"]

        trainer2.GetTeam().remove(GetTrainerTeam("Phobos", "Iron Jugulis"))

    call Battle([trainer1, trainer2], healParty=False, customexpressions=["red angrybrow frownmouth", "red angrybrow happymouth", "phobos angrybrow goggles frownmouth", "phobos angrybrow goggles angrysharkmouth"], specialmusic=("audio/music/theme_start.ogg","audio/music/theme_loop.ogg"), dialogfunc=phobosbattledialog, customswitchbrain=phobosswitchbrain) from _call_Battle_200
    $ RecordBattle("Phobos3")

    hide blank2
    hide semiblank2

    if (not WonBattle("Phobos3")):
        show phobos angrybrow happysharkmouth goggles with dis

        jump gameover

    show phobos surprisedbrow surprisedsharkmouth goggles with dis

    phobos "[ellipses]"
    phobos "No."
    phobos angrybrow angrysharkmouth"No,{w=0.5} no,{w=0.5} no!{w=0.5} No! {w=0.5}{nw}"

    show concerthallstagenight with vpunch

    extend "No! {w=0.5}{nw}"
        
    show concerthallstagenight with vpunch

    extend "No!"

    pause 2.0

    red @unamusedbrow talkingmouth "Yeah."

    phobos angrysharkmouth anger2 shadow angrybrow "You think this is the end, you filthy, penniless, luddite?! You can't begin to grasp the power Eternity wields!"

phobos @sad2eyes sadeyebrows talking2sharkmouth "I'll hate to return home with only one prize to add to my collection, but this trophy is more than enough to grant me every prize I might desire."

red @talking2mouth "Give it up, Phobos. Your Pokémon are all fainted. You're not leaving with one 'prize.' You're not leaving at all."

phobos @angrybrow angrysharkmouth "Oh, is that quite so? Well, tell me. Do you happen to have one million, six hundred and sixty-five thousand Pokédollars to your name?"

if (money + bank >= 1665000):
    red @talking2mouth "Yes, because I cheated."

    jump gameover#lol

red @confusedeyebrows upeyes frownmouth "[ellipses]"
red @confused "No."

phobos @talking2sharkmouth "Then I doubt you have exactly three hundred and thirty-three Max Revives on you."

$ PlaySound("Heal_A.ogg")

narrator "ETERNITY PHOBOS used MAX REVIVE(s)!"

queue music "audio/music/lawrencetheme_start.ogg" noloop
queue music "audio/music/lawrencetheme_loop.ogg"

pause 2.0

phobos @talking2sharkmouth "I, however, do. {w=0.5}Did. {w=0.5}{nw}"
extend @upeyes angryeyebrows talking2sharkmouth "Whatsoever."

red @surprisedbrow frownmouth "[ellipses]"

phobos @angrybrow talking2sharkmouth "Do you {i}get it{/i} now, you brats? It doesn't matter how much you put in my way. I'm {i}above{/i} such things."
phobos @angrybrow talking2sharkmouth "I will win, because I have more money, and because I {i}don't care{/i} how much these Pokémon get hurt."

redmind @sadbrow frownmouth "There's no doubt, with everyone here, we could beat him again[ellipses] but if he's really willing to keep reviving his Pokémon over and over, then[ellipses]"
redmind @angrybrow angrymouth "We can't risk it. His Pokémon might actually die if he pushes them that hard."

pause 1.0

red @shadow angrybrow talking2mouth "You're evil."

phobos @talking2mouth "Blah, blah, blah, I'm {i}winning{/i}. Your weakness is your empathy."

$ MoveInSmart("yellow angrybrow frownmouth")

yellow @talking2mouth "No, Phobos. Only a weak man like you could think empathy is a weakness."

red @surprisedbrow talking2mouth "Yell'?"

yellow @talking2mouth "He's going to lose. [first_name], we need to battle him one more time."

red @talking2mouth "But his Pokémon will--"

yellow @talking2mouth "They'll be fine. I {i}promise{/i}."

show blank4 behind yellow with transeye2nopause
$ PlaySound("shine.ogg")
$ HealParty()
pause 1.0
hide blank4 with transeye2nopause

yellow glowhandseyes @talking2mouth "Heal."

pause 1.0

show yellow -glowhandseyes with dis

yellow @angrybrow talking2mouth "Please, [first_name], hold my hand. And listen to what I say. This won't work without you."

pause 2.0

show phobos surprisedbrow frownmouth with dis

red @talking2mouth "Okay."

phobos -surprisedbrow -frownmouth @happysharkmouth "If you want to hurt yourselves and these Pokémon more, be my guest! Hah hah hah!"

yellow @talking2mouth "No-one's going to get hurt, Phobos! Not even you, as much as you might deserve it."

phobos @angrybrow happysharkmouth "Oh, I think you'll find that one's {i}not quite{/i} up to you!"

python:
    AddEvent("Lawrence", "LiberationBattle2")
    AddEvent("Game", "LiberationBattle")
    trainer1 = MakeRed()
    trainer2 = MakeTrainer("Yellow", TrainerType.Ally)
    trainer3 = MakeTrainer("phobos", TrainerType.Enemy)

    if (HasEvent("Lawrence", "Hard")):
        for mon in trainer3.GetTeam():
            mon.UpdateLevel(30, updateMoves = False, force=True)
        GetTrainerTeam("Phobos", "Combee").Foreverals = ["Vespiquen Uneveral"]
        GetTrainerTeam("Phobos", "Dodrio").Foreverals = ["Dodrio Overal"]
    elif (HasEvent("Lawrence", "Tyrannic")):
        for mon in trainer3.GetTeam():
            mon.UpdateLevel(33, updateMoves = False, force=True)
        GetTrainerTeam("Phobos", "Combee").Foreverals = ["Vespiquen Uneveral"]
        GetTrainerTeam("Phobos", "Dodrio").Foreverals = ["Dodrio Overal"]

    trainer3.GetTeam().remove(GetTrainerTeam("Phobos", "Iron Jugulis"))

call Battle([trainer1, trainer2, trainer3], customexpressions=["red angrybrow frownmouth", "red angrybrow happymouth", "yellow angrybrow frownmouth", "yellow gloweyes angryeyebrows angrymouth", "phobos angrybrow goggles frownmouth", "phobos angrybrow goggles angrysharkmouth"], specialmusic=("audio/music/theme_start.ogg","audio/music/theme_loop.ogg"), dialogfunc=phobosbattle2dialog, customswitchbrain=phobosswitchbrain, gainexp=False) from _call_Battle_201

python:
    RecordBattle("Phobos4")
    RemoveEvent("Lawrence", "LiberationBattle2")
    RemoveEvent("Game", "LiberationBattle")

if (not WonBattle("Phobos4")):
    show phobos angrybrow happysharkmouth goggles with dis

    jump gameover

show phobos goggles surprisedbrow frownmouth with dis

phobos @talking2sharkmouth "Im... impossible. Inconceivable! In... in[ellipses]"

melody contest @talking2mouth "Inevitable, really."

show screen songsplash("Ranger School Theme", "Zame")
queue music "audio/music/natechill.ogg"

summer "Rangers! Everyone, hands {i}off{/i} your Poké Balls!"

redmind @surprisedbrow frownmouth "The rangers! They're finally here?!"

show summer angrybrow frownmouth:
    xpos 1.2 xzoom -1
    ease 0.2 xpos 0.1
    ease 0.5 xzoom 1 xpos 0.33

show kate sweat winkbrow angrymouth:
    xpos 1.2 xzoom -1
    pause 1.0
    ease 1.0 xpos 1.1
    pause 0.5
    ease 1.0 xpos 1.0
    pause 0.5
    ease 1.0 xpos 0.9
    pause 0.5
    ease 1.0 xpos 0.8
    pause 0.5
    ease 1.0 xpos 0.66

summer @talking2mouth "Who called us? Brendan? There a Brendan here?"

brendan contest sweat @talking2mouth "Uh, yeah, I'm--I'm Brendan. I called. Uh, that guy in the chair is, uh[ellipses]"

show summer surprisedbrow with dis

extend @talking2mouth "a terrorist?"
brendan @closedbrow talking2mouth "{size=30}That's what Melody said, anyway.{/size}"

summer -surprisedbrow @talking2mouth "Alright. Someone explain what's happening here. Dispatch said your call was mostly just someone screaming in the background."

pause 1.5

narrator "You and your friends look around at each other, at a loss to describe exactly what {i}did{/i} just happen here."

summer @unamusedbrow talking2mouth "Any time now."

leaf @talking2mouth "Uh, [first_name]? This would be a really good time to be believed."

red @sweat closedbrow talking2mouth "Alright, officer. This is what happened--"

show blank2 with splitfade

narrator "You eventually work your way through the long story of Phobos' mental breakdown."

hide blank2 with splitfade

summer @frownmouth "[ellipses]"
summer @talking2mouth "There's just one thing about your story that doesn't track with me."

red @sadbrow talkingmouth "Just the one?"

summer @talking2mouth "You said the alien-Pokémon died, right?"

red @sad2eyes talking2mouth "Yeah, Phobos forced his[ellipses] robo-Hydreigon to do it."

grusha noscarf @surprisedblankeyes tinycenter talking2mouth "{size=30}Guys, it's still right here. Someone help.{/size}" 

pause 1.5

summer @talking2mouth "So what's that?"

show phobos:
    ease 0.5 xpos 1.5

show kate:
    ease 0.5 xpos 1.5

show summer:
    ease 0.5 xzoom -1 xpos 0.66

show fulldeoxys:
    xpos -0.2 xanchor 0.5 zoom 0.6 yanchor 1.0 xzoom -1 ypos 0.9
    ease 0.5 xpos 0.2 
    parallel:
        linear 0.3 xpos 0.21
        linear 0.3 xpos 0.2
        pause 1.0
        linear 0.3 xpos 0.19
        linear 0.3 xpos 0.2
        pause 1.0
        repeat
    parallel:
        ease 1.5 ypos 0.9
        ease 1.5 ypos 0.93
        ease 1.5 ypos 0.9
        ease 1.5 ypos 0.87
        repeat

red @surprised "Deoxys! You're alive?"

brendan @surprised "{size=30}Gah, it's alive?!{/size}"

yellow @surprisedbrow talking2mouth "It--I think it regenerated? Its core is cracked, but I think it's holding together."

narrator "As if on cue, a small sliver of crystal falls from its body, landing on the floor."

yellow @sweat winkbrow frownmouth "[ellipses]{nw}"
extend @sweat winkbrow talking2mouth "mostly."

summer @talking2mouth "Well, alien or not, it's an injured Pokémon. We can fix that. I'll just use my Capture{nw}"

show fulldeoxys:
    linear 0.03 alpha 0.35 zoom 0.62 xpos 0.195
    linear 0.03 alpha 0.9 zoom 0.59 xpos 0.205
    linear 0.03 alpha 0.2 zoom 0.61 xpos 0.202
    "images/Pokemon/fulldeoxyss.webp"
    zoom 0.5
    linear 0.05 alpha 1.0 xpos 0.2
    pause 1.0
    ease 0.4 xpos 1.5 ypos 0.0 zoom 0.4

extend @surprisedbrow talking2mouth " Styler, and--"

pause 2.0

yellow @talking2mouth "They[ellipses] didn't like the word 'capture.'"

$ BecomeNamed("Kate")

summer @closedbrow talking2mouth "{size=30}Guardian Signs, give me strength.{/size}"
summer @talking2mouth "Kate, let headquarters know about this. About[ellipses] {i}all{/i} this."

show phobos:
    ease 0.5 xpos 0.5

show kate -winkbrow -angrymouth:
    ease 0.5 xpos 0.66

show summer:
    ease 0.5 xzoom 1 xpos 0.33

if (GetRelationshipRank("Grusha") > 0):
    kate @talking2mouth "Yes, Miss Ranger!"
    kate @surprised "Oh, but, Miss Ranger! The Ovitrace AeroTerraScan is showing strong traces of Mission Priority Number One right here!"

    summer @unamusedbrow talking2mouth "Then recalibrate it. And we've got a new number-one priority, now."

    kate @sadbrow talking2mouth "But Miss Ranger, the OATS is--"

    summer @talking2mouth "Kate, in the field, you have to be able to switch between priorities on the fly. We've got an injured, possibly aggressive, alien Pokémon flying over Inspira right now. Everything else comes second."

    pause 1.0

kate @talking2mouth "So[ellipses] should we not arrest this guy?"

summer @talking2mouth "We'll take him down to the Ranger Depot, then hand him off to the police. This isn't our jurisdiction."

brendan @surprisedbrow talking2mouth "Oh, seriously? Uh, sorry. I guess I should've just called the cops."

summer @unamusedbrow talking2mouth "Well, it's our jurisdiction {i}now.{/i}"

pause 1.0

summer @sadbrow talking2mouth "It sounds like you kids have been through a lot. I'd like you to come in for questioning in Inspira, when you have the time."
summer @talking2mouth closedbrow "I'll talk with Drayden about organizing a time sometime later. For now, just put all this out of mind, and leave it to the professionals."

ethan @talking2mouth "You want us to 'put out of mind' the time one of the board members of our school turned out to be a supervillain and an alien Pokémon attacked us?"

summer @unamusedbrow talking2mouth "Don't appreciate the attitude, blue-hair."

ethan @closedbrow talking2mouth sweat "{size=30}Just checking.{/size}"

pause 1.0

melody contest @talking2mouth "Hey, wait. Phobos still has the trophy."

show summer:
    xpos 0.33
    ease 0.5 xpos 0.5
    pause 0.5
    ease 0.5 xpos 0.33

pause 0.5

summer @talking2mouth "Right, you were holding some sort of contest here, right? Who won?"

redmind @upeyes confusedeyebrows frownmouth "[ellipses]"

brendan @confusedbrow frownmouth "[ellipses]"

ethan @confusedbrow frownmouth "[ellipses]"

grusha @surprisedblankeyes tinycenter frownmouth "[ellipses]"

melody @talking2mouth "Blondie."

show trophy:
    xpos 0.33 anchor (0.5, 0.5) zoom 0.0 alpha 0.0 ypos 0.5
    linear 0.3 alpha 1.0 zoom 0.3
    pause 0.3
    easein 0.4 xpos 0.4 ypos 0.3 zoom 0.4 rotate 10
    parallel:
        easeout 0.4 xpos 0.5 ypos 0.7 zoom 0.5 rotate 30
    parallel:
        pause 0.2
        easeout 0.2 alpha 0.0

narrator "The senior Ranger tosses the trophy to Yellow."

summer @talking2mouth "Congrats on your win."

show summer:
    ease 0.5 xpos 1.2

show phobos:
    ease 0.5 xpos 1.5

show kate:
    ease 0.5 xpos 1.7

show melody contest:
    xpos -0.2
    ease 2.0 xpos 1.3

show brendan contest:
    xpos -0.2
    pause 0.5
    ease 1.5 xpos 1.5

show may contest:
    xpos -0.4
    pause 0.5
    ease 1.5 xpos 1.3

show grusha noscarf surprisedblankeyes tinycenter frownmouth:
    xpos -0.7
    pause 1.5
    ease 0.4 xpos 2.0

show leaf:
    xpos -0.2
    pause 0.7
    ease 0.5 xpos 1.2

show ethan:
    xpos -0.2
    pause 0.7
    ease 0.5 xpos 1.5

show blue:
    xpos -0.2
    pause 0.7
    ease 1.0 xpos 1.7

yellow @heavyblush surprised "Hey--{w=0.5}wait--{w=0.5}no, I didn't--{w=0.5}stop!"

stop music fadeout 1.5

call clearscreens() from _call_clearscreens_291
scene blank2 with splitfade

pause 1.5

$ RemoveEvent('Game', 'AutoContest')
$ RemoveEvent('Yellow', 'AutoContest')

scene bedroommidnight with Dissolve(3.0)

queue music "audio/music/eterna_start.ogg" noloop
queue music "audio/music/eterna_loop.ogg"

red casual night hatless @upeyes sadeyebrows frownmouth "[ellipses]"

pause 1.0

red @talking2mouth "You okay, bud?"

$ PlaySound("Pokemon/pikachu_sad.ogg")

libpikachu downwardregularears @closedbrow "Piiiikaaaa."

redmind @upeyes frownmouth "Sleeping, huh? That makes one of us."

$ PlaySound("vibrate.ogg")

TempCharacter("Phone") "Bzzt! Bzzt! Bzzt!"

redmind @upeyes sadeyebrows "It's like she knows."

if (HasEvent("Leaf", "AcceptedConfession")):
    show phone_B
    show phone_A
    show leaf bedwear behind phone_A:
        zoom 0.8 ypos 0.9
    with fadeinbottom

    pause 1.0

    leaf @talkingmouth "Guess you're awake?"

    red @lightblush sad2eyes sweat talkingmouth "{i}Now{/i} I am."

    leaf @surprisedbrow talking2mouth "Really? I haven't been able to even close my eyes."

    scene andtheyweredormmates with Dissolve(3.0)

    red casual night hatless @talking2mouth closedbrow "Nah, me neither. There's no getting around it--we were attacked in the middle of Kobukan."

else:
    show phone_B
    show phone_A
    with fadeinbottom

    show phone_C behind phone_A with dis

    show phone_msg1 behind phone_A with dis
        
    $ title = Text("A Real Girl",size=30,font="fonts/consola_0.ttf",color="#313131")

    image msg8 = Text("you up?",size=21,color="#ffffff",line_spacing=5,text_align=0.0)

    show text title behind phone_A:
        xalign 0.51 yalign 0.34
    show msg8 behind phone_A:
        xpos .41 ypos .4
    with dis

    red @angryeyebrows sad2eyes frownmouth "How am I supposed to sleep? There's no getting around it--we were attacked in the middle of Kobukan."

    scene andtheyweredormmates with Dissolve(3.0)

red @closedbrow sweat talking2mouth "I think things only worked out because Phobos is an idiot. But what worries me is he wasn't working alone[ellipses]"

leaf bedwear night @talking2mouth "Yeah, I know what you mean. He mentioned something called 'Eternity' a few times. Do you think it's like a Team Rocket situation?"

red @talking2mouth "I can't imagine anyone {i}wanting{/i} to team up with him. But[ellipses] maybe."

pause 1.0

leaf @talkingmouth "Hey.{w=0.5} We'll be okay. Even if Phobos had some people he was working with[ellipses]"
leaf @flirtbrow talkingmouth "I mean, look at the company they keep. I don't think we've got much to worry about."

pause 1.0

red @talking2mouth "Still. If the trophy is some kind of powerful Pokémon's chrysalis[ellipses] I'm not sure we're the best people to be hanging onto it."

leaf @flirtbrow talkingmouth "What, you think Yellow won't guard it with her life?"

red @sadbrow talkingmouth "Frankly, I hope she doesn't have to."

leaf @talking2mouth "Yeah[ellipses] I get you. Tomorrow morning, we can talk to Drayden about finding a safer place for it."

red @talking2mouth "Good plan."

if (GetRelationshipRank("Jasmine") >= 1):
    red @talking2mouth "I swung by the infirmary before we came back. Nurse Miriam said it was late, so Jasmine was already asleep."
    red @talking2mouth "I'd like to see her tomorrow, as well."

    leaf @talking2mouth "Okay. That's really kind of you."

else:
    leaf @talking2mouth "We should also drop by the infirmary tomorrow and see how Jasmine's doing."

    red @talking2mouth "Yeah, that'd be a nice thing to do."

pause 1.0

leaf @embarrassed blush "Um[ellipses] on the topic of good plans[ellipses] I wanted to apologize again for yesterday."

red @confusedbrow frownmouth "[ellipses]"
red @happy "Oh, right! Man, with everything that happened today, yesterday seemed a year ago. I barely remembered."

leaf @closedbrow talking2mouth "Well[ellipses] still. I'm sorry, again."

red @sadbrow talkingmouth "It's alright. I mean, we definitely kinda just took the riskiest option without really thinking about why you might hate it."

leaf @talkingmouth "Well[ellipses] I didn't."

pause 1.0

red @talking2mouth "Think the school's going to find a way to blame me for today's drama?"

leaf @closedbrow talking2mouth "Beyond a shadow of a doubt."

red @talking2mouth closedbrow "Yeah, that makes sense."
red @upeyes sadeyebrows talkingmouth "On the other hand, there weren't {i}that{/i} many people there. Maybe the school'll be able to keep it under wraps?"
red @talkingmouth sadbrow "It wasn't {i}that{/i} big an event."

pause 1.0

leaf @talking2mouth "What's that phrase that Ethan uses? Huffing copium?"

red @talking2mouth closedbrow sweat "Alright, I'm going to bed."

leaf @talkingmouth winkbrow "Knew I could bore you into tiredness."

red @upeyes angryeyebrows talkingmouth "Yeah, that's what did it."

pause 1.0

leaf @talkingmouth "Thanks for today. You were very brave."

red @closedbrow talking2mouth "I'm going to try not to make a habit of it."

leaf @winkbrow talkingmouth "To quote the initimable Baron Phobos--I think you'll find that one's not up to you!"

pause 0.5

leaf @sad "{size=30}Oh, god, I think I threw up in my mouth a little.{/size}"

pause 0.5

red @closedbrow talkingmouth "Goodnight, Leaf."

leaf @talkingmouth "Goodnight, [first_name]."

if (HasEvent("Leaf", "AcceptedConfession")):
    leaf blush @talkingmouth "Sweet dreams."

    red @winkbrow talkingmouth "They can't be any sweeter than right now."

    scene blank2 with splitfade

    pause 2.0

    $ PlaySound("vibrate.ogg")

    show phone_B
    show phone_A
    with fadeinbottom

    show phone_C behind phone_A with dis

    show phone_msg1 behind phone_A with dis
        
    $ title = Text("A Real Girl",size=30,font="fonts/consola_0.ttf",color="#313131")

    image msg9 = Text("💚",size=21,color="#ffffff",line_spacing=5,text_align=0.0)

    show text title behind phone_A:
        xalign 0.51 yalign 0.34
    show msg9 behind phone_A:
        xpos .41 ypos .4
    with dis

    pause

else:
    leaf @talkingmouth "Sleep well."

stop music fadeout 3.0

scene blank2 with splitfade

pause 2.0

narrator "Meanwhile, across an ocean[ellipses]"

pause 1.0

play music "audio/shiprain.ogg" fadein 6.0 loop

show eternityship 
$ renpy.show("rain", [thirtydegrees])
with superslowdis

TempCharacter("Radio") "...strange 'gems' scattered all over Inspira City in the flight of the injured Pokémon!"
TempCharacter("Radio") "The origin and danger of these gems cannot be identified at present, but we have already received {i}many{/i} reports of their massive effect on Pokémon."
TempCharacter("Radio") "The local Ranger division, and the police force, are instructing everyone to stay away from these gems, and to keep Pokémon away at all costs."
TempCharacter("Radio") "However, the number of reports we've already received regarding the effects on Pokémon suggests that hundreds--"
TempCharacter("Radio") "{i}*Click.*{/i}"

pause 1.0

TempCharacter("{color=#4775BB}???{/color}") "He has failed to a degree greater than I expected."

pause 1.5

TempCharacter("{color=#4E3A54}???{/color}") "He was going to betray you. Use the chrysalis himself. Probably best he {i}did{/i} fail."

TempCharacter("{color=#4775BB}???{/color}") "Perhaps. I planned for his betrayal, in any case. The substitute should be able to obtain the chrysalis with little difficulty."

TempCharacter("{color=#4E3A54}???{/color}") "You want to send me in, just say it. You know I'd get results--faster than anyone else."

pause 0.5

TempCharacter("{color=#4775BB}???{/color}") "There is no rush. We have as much time as we need."

pause 1.0

TempCharacter("{color=#4E3A54}???{/color}") "Ar--"

TempCharacter("{color=#4775BB}???{/color}") "J."

TempCharacter("{color=#4E3A54}J{/color}") "{i}*Sigh.*{/i}"
TempCharacter("{color=#4E3A54}J{/color}") "Right. Sorry, {i}Eternity{/i}."
TempCharacter("{color=#4E3A54}J{/color}") "Do you want my opinion? I'm offering it as a freebie."

TempCharacter("{color=#4775BB}Eternity{/color}") "I will hear it."

TempCharacter("{color=#4E3A54}J{/color}") "You didn't need Phobos, and you don't need your backup plan. You don't even need me--or any of the others."
TempCharacter("{color=#4E3A54}J{/color}") "You should just handle this whole operation by yourself. Everyone you bring aboard is another weak link."

pause 1.0

$ PlaySound("lightning.ogg")

show eternityshipbright at night

pause 0.02

hide eternityshipbright

TempCharacter("{color=#4775BB}Eternity{/color}") "[ellipses]That is my final option."

$ PlaySound("lightning.ogg")

show eternityshipbright at night

pause 0.02

hide eternityshipbright
show eternity behind rain:
    matrixcolor BrightnessMatrix(-1)
show eternityship behind eternity

TempCharacter("{color=#4775BB}Eternity{/color}") "If all else fails, then I shall take the rains once more and flood this world with my power."

pause 0.5

TempCharacter("{color=#4775BB}Eternity{/color}") "But not yet."

pause 0.5

$ PlaySound("lightning.ogg")

show eternityshipbright at night

pause 0.02

hide eternityshipbright
show eternity at chroma_glitch(strength=1.5, aberration=8.0, jitter=5.0, scanline=0.2, flicker=0.3):
    matrixcolor BrightnessMatrix(-0.6) * ContrastMatrix(1.3) xpos 0.488
show eternityeye
pause 0.35
show eternity at chroma_glitch(strength=0.55, aberration=2.75, jitter=1.25, scanline=0.10, flicker=0.12):
    xpos 0.488

TempCharacter("{color=#4775BB}Eternity{/color}") "For what king does not give his subjects the opportunity to kneel?"

stop music fadeout 9.0
scene blank2 
show eternityeye
with Dissolve(9.0)

pause 1.0

hide eternityeye

pause 1.0

jump enddemo