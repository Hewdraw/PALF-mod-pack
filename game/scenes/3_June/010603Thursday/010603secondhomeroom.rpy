label secondhomeroom010603:

scene blank2

play music "Audio/Music/Oak Intro.ogg" noloop
queue music "Audio/Music/Oak Class.ogg"

show homeroom behind blank2
    
$ renpy.transition(dissolve)
show screen currentdate

show oak 
hide blank2 
with splitfade

oak @talkingmouth "Welcome back to class, ladies and gentlemen."
oak @talking2mouth "Time for your quiz! The lectures over the past couple of days should have prepared you for this."
oak closedbrow @talkingmouth "And, based on the slight upward curve in my gradebook, the evidence supports the hypothesis! Hmhmhm.~"

pause 0.5

oak -closedbrow @talking2mouth "Ahem. For this test, we'll be revisiting a concept. Who here remembers 'Blinding Fog'? This field effect makes it so that if a move has a chance to miss, it {i}will{/i}."
oak @talkingmouth "The key to winning this test is quite simple--don't miss. If you leave even the slightest thing up to luck, you will lose." 
oak @talking2mouth "Hilbert, please recap the ways lowered accuracy might be mitigated."

show hilbert uniform:
    xpos 0.75

hilbert @talking2mouth "Use 100%%-accurate moves. Utilize Gravity, which increases the accuracy of all moves by 66%% and prevents airborne moves from being used. Or use moves that are auto-hits under certain conditions."

oak @talkingmouth "Quite right. And these certain conditions are... Melody?"

show melody uniform:
    xpos 0.25

show oak unamusedbrow frownmouth with dis

melody on @talking2mouth "No, we're not there yet."

hide melody with dis

oak -unamusedbrow -unamusedmouth @upeyes angryeyebrows talking2mouth "Of all the... fine, Blue?"

show blue uniform with dis:
    xpos 0.25

blue surprised "Wait, you're calling on {i}me{/i}?"

oak @confused "Er... yes? Is there something wrong?"

blue @talking2mouth "You've never done that before."

oak @confused "Hm. Never?"

blue @talking2mouth "Never."

pause 1.5

oak @confused "You {i}do{/i} know the--"

blue @angrybrow talking2mouth "Yes, I know the answer! Earthquake and Magnitude will always hit digging foes. Whirlpool and Surf will hit divers, Toxic will hit {i}anything{/i} as long as a Poison-type is using it, and..."
blue @talking2mouth "And there's a ton of different moves that hit airborne foes, but Sky Uppercut, Thunder, Gust, and Twister are a few of them."

oak @talkingmouth "Quite right. Thank you, Blue. Thank you, Hilbert."

hide blue
hide hilbert 
with dis

oak @talkingmouth "I see no further need to elaborate on this point--you all know quite well what you need to succeed."
oak @angrybrow talking2mouth "I'm quite serious--look over the moves, items, and abilities of your Pokémon. If you do not, and you do poorly, as a result of it, I will be {i}quite{/i} put out."
oak @angrybrow talking2mouth "Each opponent Pokémon is equipped with a Lum Berry, except for one. The implications should be obvious."
oak @talking2mouth "The last bit of information you should know is that your foes will exclusively use the moves 'Dig' and 'Fly.'" 
oak @closedbrow sweat talking2mouth "I trust it is obvious which Pokémon will use which. Don't worry, there won't be any digging Ninjask in this quiz."
oak @happy "So, without further ado, please take out your pencils, and remember [bluecolor]this will be graded!{/color}"

#use smack down to hit an airborne foe
#use gravity to smack down a foe in midair, then they'll struggle to death. You'll faint first, so use endure to stall a turn
#use Toxic to hit a foe in the middle of a dig turn
#use Magnitude to hit a foe in the middle of a dig turn

python:
    AddEvent("Professor Oak", "KecleonTest")
    trainer1 = Trainer("red", TrainerType.Player, [
        #smack down the skarmory
        Pokemon("Graveler", level=30, moves=["Smack Down", "Self-Destruct", "Fire Blast", "Rock Polish"], ivs=[0, 0, 0, 0, 0, 0], ability="Sturdy", nature=Natures.Serious),
        
        # gravity the cramorant, then Endure (then let it faint)
        Pokemon("Stonjourner", level=30, moves=["Stone Edge", "Gravity", "High Horsepower", "Endure"], ivs=[0, 0, 0, 0, 0, 0], ability="Power Spot", nature=Natures.Serious),
        
        #toxic the excadrill
        Pokemon("Salandit", level=30, moves=["Poison Fang", "Steady Flame", "Double Slap", "Toxic"], ivs=[0, 0, 0, 0, 0, 0], gender=Genders.Male, ability="Corrosion", nature=Natures.Serious, item=Item.StickyBarb),
        
        #magnitude the zangoose
        Pokemon("Sandslash", level=30, moves=["Fury Cutter", "Magnitude", "Rollout", "Slash"], ivs=[0, 0, 0, 0, 0, 0], ability="Sand Rush", nature=Natures.Serious)
    ])

    trainer2 = Trainer("oak", TrainerType.Enemy, [
        Pokemon("Skarmory", level=70, moves=["Fly"], ability="Sturdy", ivs=[0, 0, 0, 0, 0, 0], item=Item.LumBerry, nature=Natures.Serious),
        Pokemon("Cramorant", level=70, moves=["Fly"], ability="Gulp Missile", ivs=[0, 0, 0, 0, 0, 0], item=Item.LumBerry, nature=Natures.Serious),
        Pokemon("Excadrill", level=70, moves=["Dig"], ability="Sand Force", ivs=[0, 0, 0, 0, 0, 0], item=Item.AirBalloon, nature=Natures.Serious),
        Pokemon("Zangoose", level=70, moves=["Dig"], ability="Immunity", ivs=[0, 0, 0, 0, 0, 0], item=Item.LumBerry, nature=Natures.Serious)
    ])

    for mon in trainer1.GetTeam() + trainer2.GetTeam():
        mon.AdjustHealth(1, True)

    for mon in trainer2.GetTeam():
        mon.ChangeStats(Stats.Accuracy, 3)

    for mon in trainer1.GetTeam():
        if (mon.GetNickname() not in ["Salandit", "Stonjourner"]):
            mon.ApplyStatus("poisoned")
        elif (mon.GetNickname() == "Salandit"):
            mon.AdjustHealth(19, True)
        for move in mon.GetMoves():
            move.PP = 1


call Battle([trainer1, trainer2], currentWeather=("blinding fog", 999), clearstats=False, gainexp=False, healParty=False, uniforms=[True, False], lockbag=True, lockluck=True, preserveAllStats=True) from _call_Battle_178
$ RecordBattle("Oak13")
$ renpy.transition(dissolve)
show screen currentdate

play music "Audio/Music/Oak Intro.ogg" noloop
queue music "Audio/Music/Oak Class.ogg"

show homeroom
show oak 
with dis

pause 2.0

if (WonBattle("Oak13")):
    redmind uniform @happy "Nice. I knew this'd work."

else:
    redmind uniform @wince frownmouth "Well, Sam's a better teacher than he was at the start of the year, but it's still not a cakewalk."
    redmind @happy "But who goes into Kobukan expecting a cakewalk?"

oak @talking2mouth "At a glance[ellipses] it seems we didn't do quite as well this week as we did last Thursday."
oak @sweat talking2mouth "Well, no-one expected an upward curve without the odd dip, I'm sure."

pause 0.5

oak @talking2mouth sad2eyes talking2mouth "I, er, most certainly didn't. It would be ridiculous to imagine a man at my age taking to something entirely new and excelling at it first try."
oak @upeyes talking2mouth "{size=30}Well, fourteenth try.{/size}"
oak @happy "Alright, everyone, that'll be all for today. Please, go enjoy your evenings!"

hide oak with dis

pause 1.0

show blue uniform:
    xpos 0.33
show leaf uniform:
    xpos 0.66
with dis

leaf @talkingmouth "Hey. We're going shopping."

blue @talking2mouth "No, the fuck we're not."

leaf @sarcastic "We're going shopping to get Yellow a coordinator's dress."

blue @sad2eyes angryeyebrows talking2mouth "Then you should've lead with {i}that{/i}."

leaf surprisedbrow frownmouth @flirtbrow talkingmouth "Alright. Let's go back to the dorm and grab Yellow."

red @talkingmouth "And Ethan, right?"

leaf @talking2mouth "Um, yeah. Ethan, too, of course."

red @happy "Cool. Let's go."

$ location = "city"

scene mall 
show blue:
    xpos 0.2
show ethan:
    xpos 0.4
show yellow:
    xpos 0.6
show leaf:
    xpos 0.8    
with splitfade

leaf @talkingmouth "This is the first time you guys have been to {i}Join{/i}, right?"

if (HasLocation("JoinAvenue")):
    red @talking2mouth "Nah, I've been here before."

    if (GetRelationshipRank("Rosa") >= 3):
        show leaf surprisedbrow frownmouth with dis

        red @winkbrow talking2mouth "With Rosa, by the way."

        leaf @talking2mouth "Can you--can you {i}leak{/i} jealousy? Because I feel like I'm leaking jealousy right now."

    else:
        leaf @surprised "Oh, so you know about that nose-cream salesman, right? Seriously, everyone else, {i}watch out.{/i} Last time I walked by his stall, I had to hide in a trash can to avoid getting collared by him."

        ethan @talking2mouth "I can't believe that was your only option."

        leaf @closedbrow talkingmouth "Probably not, but it was the first one I thought of, so[ellipses]"

else:
    $ RecordKnownLocations("Leaf", "JoinAvenue")

    red @talking2mouth "Yeah, first time. You said it's called {i}Join{/i}?"

    leaf @talkingmouth "Short for 'Join Avenue of Inspira.' It's a series of malls that started in Unova, then spread out. Rosa's the manager for a bunch of them!"

    ethan @confused "How does she have the time?"

    leaf @talkingmouth "{i}Honorary{/i} manager, I guess."
    leaf @happybrow talkingmouth "But I'm pretty sure she's contractually obligated to drop in at least once a month. You think if I camp in one of the empty dumpsters out back, I can be first in line to greet her when she does her monthly visit?"

    blue @closedbrow talking2mouth "Ew."

ethan @happy "That's enough about your poor hygiene, Leaf."

leaf @flirtbrow talkingmouth "Says 'Mr. What Is A Shower?'"

ethan @talking2mouth "I've {i}heard{/i} of them."

leaf @talkingmouth "Alright, that's enough banter. We're here on a serious mission!"

show yellow surprisedbrow frownmouth with dis

if (HasEvent("Professor Oak", "ParticipateMDTryouts")):
    leaf @talkingmouth "We're getting Yellow and [first_name] coordinator outfits. They'll need them, if they're going to be the number-one coordinator group in the world some day!"
    
    if (not HasEvent("Game", "WonMDTryouts")):
        if (HasEvent("Yellow", "AcceptPartner")):
            red @closedbrow talking2mouth "We didn't even win our tryout round, Leaf."

        else:
            red @closedbrow talking2mouth "I didn't even win my tryout round, Leaf."

        leaf @talkingmouth "Yeah? And I bet you didn't win your first battle, either."

        ethan @happy "She's spitting facts!"

else:
    leaf @talkingmouth "We're getting Yellow a coordinator outfit. She'll need one, if she's going to be the number-one coordinator in the world some day!"

yellow @talking2mouth "W-wait... {i}that's{/i} what we're doing?"

blue @surprised "Uh, yeah? What, didn't I tell you?"

yellow @closedbrow talking2mouth "Blue, you tell me to come and go to so many places, and you never tell me what {i}any{/i} of them are before we get there."
yellow -surprisedbrow @unamusedbrow talking2mouth "At this point, I know to just follow, and figure it out when we arrive."

pause 0.5

blue @talking2mouth "Huh."

pause 0.5

blue @closedbrow talking2mouth "We're going to Join Avenue to get you a coordinator dress."

leaf @talking2mouth "Coordinator {i}outfit{/i}. If she wants a suit, she can have one."

blue angry "Hey, you said we'd be getting her a coordinator {i}dress!{/i}"

show yellow sadbrow -frownmouth with dis

leaf @sarcastic "Is this really an argument you want to have? Now?"

blue -angry @closedbrow talking2mouth "Suit's fine. {size=30}I guess.{/size}"

ethan @talking2mouth "Hey, about that... why {i}do{/i} you wear the male uniform, Yellow? No judgment, 'course, just wondering."

yellow @talking2mouth "Oh. Um, it's nothing big. I just... the skirt is a bit..."
yellow @sadbrow challengingmouth blush "You know?"

ethan @confused "Not a clue, sorry."

yellow -sadbrow @closedeyes angryeyebrows talking2mouth "I just don't feel comfortable in that kind of clothing."

ethan @closedbrow talking2mouth "Alright. I'm pretty sure if I push any further, Leaf'll yell at me, so I'll drop it."

pause 1.0

ethan @confused "Wait, actually, do you still have a female uniform?"

yellow @talking2mouth "Hm? Yes. I, um, I actually sewed my uniform, but I have the school uniform that Kobukan gave me, and that's the woman's uniform."

ethan @talkingmouth "Cool, just wondering. And, hey, well done on the tailoring or whatever for the uniform you made. Looks seriously professional-quality. You're a good seamstress."

yellow @sad2eyes talkingmouth "Oh, not really. Um, the seams aren't really straight. The cuffs are a bit too long, I had to roll them back multiple times, and there's a couple snags if you look {i}really{/i} closely, so--"

show ethan surprisedbrow frownmouth
show yellow surprisedbrow frownmouth
show blue surprisedbrow frownmouth
with dis

leaf @happy "Hey, [first_name]. I'm going to give you a compliment. You look nice today!"

red @happy "Thanks, Leaf! You too."

show yellow sadbrow -frownmouth
show blue embarrassedbrow frownmouth lightblush
show ethan unamusedbrow unamusedmouth
with dis 

leaf @angrybrow talking2mouth "See?! That's how you accept compliments! You say thanks, and 'you too!' You're all {i}awful{/i} at accepting compliments."

ethan @talking2mouth "Do you {i}ever{/i} compliment me?"

leaf @flirtbrow talking2mouth "I mean, I must've at some point. I hand them out like candy."

ethan @talking2mouth "Yeah, well, I don't accept candy from strangers, and they don't come stranger than you."

scene blank2 with splitfade

narrator "Your dormmates' bickering continues for a while, until you finally manage to corral them into {i}Join{/i}."

scene insidemall
show blue:
    xpos 0.2
show ethan:
    xpos 0.4
show yellow:
    xpos 0.6
show leaf:
    xpos 0.8    
with splitfade

blue @talking2mouth "Alright, so... like, what do we do here? Is there a specific store for contest dress--{w=0.5}{i}outfits{/i}?"

leaf @talkingmouth "Not particularly. We kinda just wander around until we see something we can use."

blue @closedbrow talking2mouth "Fine."

leaf @happy "Ooh, this store looks like it might do it! I {i}think{/i} Whitney recommended it to me, once. Hang on a second!"

show leaf:
    xpos 0.8
    ease 0.7 xpos 0.81
    ease 0.3 xpos -0.2

pause 1.0

blue @talking2mouth "She'll be a while. I'm going to go look at winter clothes. Not going to freeze my ass off {i}this{/i} Snowfall."

show blue:
    xpos 0.2
    ease 0.5 xpos 1.2

pause 0.5

ethan @talkingmouth "I guess if we're splitting up, I'll head out, too. I'll be at that Allhallows costume store, dude. Drop by before you leave!"
ethan @winkbrow talkingmouth "I heard that people who get lost in Allhallows Costume stores become ghosts, you know."

show ethan:
    xpos 0.4
    ease 0.5 xpos 1.2

pause 1.0

yellow @talkingmouth "[ellipses]Um. Should I go somewhere?"

red @sadbrow talkingmouth "Not if you don't want to."

if (HasEvent("Professor Oak", "ParticipateMDTryouts")):
    yellow @sadbrow talking2mouth "I guess I should probably look for that coordinator outfit. I mean, that's half of why we're here."

else:
    yellow @sadbrow talking2mouth "I guess I should probably look for that coordinator outfit. I mean, that's why we're all here."

red @sadbrow talkingmouth "I guess you're not feeling it, though?"

yellow @sadbrow talking2mouth "I want to, but..."
yellow @closedbrow talking2mouth "When I imagine myself in one of those pretty dresses, I think... that it's... it's fake. It's a lie, and everyone can see through it."
yellow @sadbrow talking2mouth "It doesn't matter what I see in the mirror. Even if I--even if I look good. I can't help thinking I'm someone--{i}something{/i} else."
yellow frownmouth @sad2brow talking2mouth "Something that couldn't be a coordinator. Something that... that disgusts people. And, for now, they're just being polite, but one day..."

pause 1.0

red @sadbrow talkingmouth "Mind if I sit?"

yellow @talking2mouth "Go ahead."

show yellow:
    ypos 1.0 zoom 1.0 xpos 0.6
    ease 0.5 xpos 0.5 ypos 1.2 zoom 1.3

red @upeyes frownmouth "[ellipses]"
red @talking2mouth "I... kinda get what you mean."

pause 0.5

red @talkingmouth "I want to be a Champion. That's my 'thing.' But I'm a kid from the countryside who's had as much experience with Pokémon as your average Rattata-toting youngster." 
red @wince talking2mouth "Sure, I have a mental Pokédex, but you know what everyone else has? A Pokédex that doesn't stop working if they're sleepy."
red @talkingmouth "When I say I'll be a champion... that feels like a lie. The odds aren't with me, and I don't have any proof of it. But I keep saying it. Over and over."
red @sadbrow talking2mouth "I can't believe it. Still can't. Not even now, not even now that I'm in Kobukan, and am training a super-rare Pokémon."
red @talkingmouth "But if I act like I believe it... and just {i}never{/i} stop acting like I believe it... what's the difference, at the end of the day? Maybe it'll even happen."

pause 1.0

yellow @sadbrow challengingmouth "Your coping strategy is denial?"

red @winkbrow talkingmouth "It's taken me this far."

show yellow:
    xpos 0.5 ypos 1.2 zoom 1.3
    ease 0.5 xpos 0.5 ypos 1.0 zoom 1.0

yellow @talking2mouth "I'm just not sure it'll work for me."

red @thonk "[ellipses]"

pause 0.5 

red @talking2mouth "Hey, a couple times, I've walked in on you chanting something to yourself. Like, a mantra."

yellow @talking2mouth "Oh, yes. Memorization and repetition. I sometimes repeat things to myself. Sorry, was it annoying?"

red @talkingmouth "Nah. I'd just like to suggest a new one for you."

yellow surprisedbrow frownmouth @confusedbrow talking2mouth "Yes...?"

red @happy "I am Yellow. I am a coordinator. I am good enough."

yellow sadbrow frownmouth @talking2mouth "{size=30}D-don't...{/size}"

red @talkingmouth "I'm serious. Whenever you start to feel like you're not enough, or you're faking it, just repeat it to yourself. Out loud. Whatever you say out loud will always be louder than whatever's in your mind, right?"

if (GetRelationshipRank("Sabrina") > 0):
    redmind @surprisedbrow frownmouth "[sabrinacolor]Not {i}always{/i}.{/color}"

    redmind @upeyes angryeyebrows frownmouth "Not the time, Sabrina."

red @happy "C'mon, say it with me. I am Yellow. I am a coordinator. I am good enough."

yellow blush @talking2mouth "{size=30}Please stop...{/size}"

red @happy "I am Yellow! I am a coordinator! I am good enough!"

yellow heavyblush @talking2mouth "{size=30}noooooooooo...{/size}"

red @happy "{size=45}I am Yellow! I am a coordinator! I am good enough!{/size}"

show insidemall with vpunch

pause 1.0

show ethan surprisedbrow frownmouth behind yellow:
    xpos 1.2
    ease 0.5 xpos 0.7

show blue surprisedbrow frownmouth behind ethan:
    xpos 1.2 xzoom -1
    ease 0.5 xpos 0.9

show leaf surprisedbrow frownmouth:
    xpos -0.2 xzoom -1
    ease 0.5 xpos 0.25

pause 1.5

red @closedbrow talking2mouth "Okay, I {i}promise{/i} there's a good reason I was shouting that."

pause 1.0

red @unamusedbrow talking2mouth "Okay, it {i}seemed{/i} like a good reason, at least."

scene blank2 with splitfade

pause 1.0

narrator "A few more hours pass as the five of you dive into the various shops around the mall."
narrator "Unfortunately..."

scene insidemall
show blue glancebrow frownmouth:
    xpos 0.2
show ethan frownmouth:
    xpos 0.4
show yellow frownmouth sadbrow:
    xpos 0.6
show leaf sadbrow frownmouth:
    xpos 0.8    
with splitfade

yellow @sadbrow talkingmouth "I'm sorry."

leaf -sadbrow -frownmouth @sadbrow talkingmouth "It's alright, sweetie. If you can't find anything you'd be comfortable in, then... well, that's that."

blue @closedeyes talking2mouth "Yeah. There's, uh, always later, or whatever. The actual Millennium Drop isn't until, what, next Saturday?"

yellow -sadbrow @talking2mouth "June 13th. Next {i}Sunday{/i}."

ethan -frownmouth @closedbrow talking2mouth "That gives you time to get something before then. Worst-case scenario, you can just overnight ship it. Or even overday ship it."

leaf surprisedbrow @surprisedbrow talking2mouth "Wait. Over-day shipping? That exists?"

ethan @winkbrow talkingmouth "It does with a {i}gold card{/i}, Leaf."

leaf -surprisedbrow @angrybrow talkingmouth "I don't know what that is, but I need it {i}immediately{/i}."

blue -glancebrow  -frownmouth @closedbrow talking2mouth "Well, this has been a bust. Should we go back to campus?"

if (HasEvent("Professor Oak", "ParticipateMDTryouts")):
    yellow @talking2mouth "Hold on. We need to get [first_name] a Coordinator outfit, too, right?"

    blue @closedbrow talking2mouth "Shit, yeah. I keep trying to forget that he's a Coordinator now, too."

    red @happy "You're mad I'm prettier {i}and{/i} stronger than you?"

    blue @angrybrow talkingmouth "The only way anyone could call you pretty is if they were saying you're pretty ugly, tubbo."

    red @unamusedbrow talking2mouth "Eight percent body fat percentage at my last checkup. You're never going to get me that way."

    ethan @talking2mouth "I think I saw some male Coordinator outfits in a store back there. Assuming you don't want a dress?"

    red @sweat talking2mouth closedbrow "You have assumed correctly."

    ethan @closedbrow talkingmouth "{size=30}Missing out, but okay.{/size}"

    leaf @talking2mouth "Hm... let's see what we can find... in {i}this{/i} store!"

    show leaf:
        xpos 0.8
        ease 0.7 xpos 0.81
        ease 0.3 xpos -0.2

    pause 0.5

    ethan @sadbrow talkingmouth "Great, even more offscreen shopping."

    scene blank2 with splitfade

    pause 1.0

    show evenmoreoffscreenshoppinglater at vspaz

    pause 3.5

    red @talking2mouth "You're kidding me."

    leaf @happy "C'mon, try it! It's dignified and noble. It makes you look like a little prince!"

    red @sadbrow talkingmouth "Noble? Leaf, this outfit looks so old-fashioned, I think [pika_name] might try to Liberage me."

    $ PlaySound("Pokemon/pikachu_happy1.ogg")
    libpikachu @happy "Pikachu!"

    red @sadbrow talkingmouth "See?"

    leaf @happy "C'mon. Contests are about self-expression. Haven't you ever wanted to express yourself?"

    red @talking2mouth "Yeah, express {i}myself{/i}, not some 1700s Kalosian nobleman that probably owned slaves."
    red @talkingmouth "Besides, don't I look kinda ridiculous? Who could take me seriously in that?"

    leaf @talking2mouth "I heard what you said to Yellow. It's not about if other people take you seriously, it's about if you can take {i}yourself{/i} seriously--because then you can make {i}them{/i} take you seriously."

    red @upeyes angryeyebrows talking2mouth "Damn you for using something that vaguely resembles my words against me."

    leaf @winkbrow talkingmouth "I'll let you get changed. But don't change {i}too{/i} much!"

    scene insidemall with splitfade

    pause 1.0

    show red sad2eyes lightblush contest frownmouth with Dissolve(2.0)

    pause 2.0

    red @talking2mouth "Go ahead."

    show red surprisedbrow with dis

    yellow @surprisedbrow talking2mouth "Oh! A perfect reproduction of the suit worn by Miette Millefeui's date at Monsieur Pierre's 1996 Grand Ball?! The one where Kalos Queen Aria Ellestar battled alongside Monsieur Pierre?"

    pause 1.0

    show red surprisedbrow -lightblush with dis

    ethan @confused "Hey, Blue, you visited Kalos for a summer, right? Can you translate?"

    blue @talking2mouth "I visited for a {i}summer{/i}. I have no idea what Yellow just said."
    blue @confused "Yellow, what did you just say?" 

    show red -surprisedbrow with dis

    yellow @sad2brow blush talking2mouth "Oh. Um. Well, Monsieur Pierre is the emcee for Pokémon Showcases, which are kind of like Pokémon Contests, but for women only, and Kalosian, and--"

    leaf @talking2mouth "Wait, the head boss of this women-only competition is a {i}man{/i}?"

    yellow @talking2mouth "Yes, but there's a historical reason for it."

    show red unamusedbrow unamusedmouth with dis

    leaf @angry "Historical reason, my ass! It's the goddamn patriarchy again!"

    ethan @talking2mouth "Shit, she's onto us. Gotta report back to the Council of Men. We need a subtler strategy."

    scene insidemall
    show blue:
        xpos 0.2
    show ethan:
        xpos 0.4
    show yellow:
        xpos 0.6
    show leaf:
        xpos 0.8    
    with splitfade

    red contest @talking2mouth "You know, I'm glad no-one's making fun of me, but I'm also kinda offended that you're not even acknowledging me."

    blue @talking2mouth "Whatever, pansy. You look fine, no-one'll laugh, you don't look any sillier than anyone else onstage. No-one watches the guys, anyway."

    show ethan happy 
    show leaf happy
    with dis

    TempCharacter("{color=#00b23f}Leaf{/color} & {color=#c1861e}Ethan{/color}") "Speak for yourself!"

    show ethan -happy
    show leaf -happy
    with dis

    red -unamusedbrow -unamusedmouth @sadbrow talkingmouth "Moving on. I'm sure we're all acutely aware that I can't afford this, right?"

    leaf @talking2mouth "Sure, just like you're aware you have the best best friend in the world."

    $ renpy.music.play("Audio/Pokemon/pikachu_angry1.ogg", channel="altcry", loop=None)
    libpikachu @angryeyes frownmouth "Pika!"

    leaf @sadbrow talkingmouth "After you, cutie, of course."

    $ renpy.music.play("Audio/Pokemon/pikachu_angry1.ogg", channel="altcry", loop=None)
    libpikachu @closedbrow frownmouth "Pika."

    red @sadbrow talkingmouth "Leaf, c'mon, this costs more than... more than, like, {i}all{/i} my other clothes put together. I don't want to be dependent on you."

    leaf @flirtbrow blush talkingmouth "[first_name], trust me when I say I'm {i}mostly{/i} doing this for me."

    blue @closedbrow talking2mouth "Ew. That's enough out of you two. [first_name], if you don't like it, just take it back to the mall later, or something. Now, can we be {i}done{/i}?"

leaf blush @sadbrow talkingmouth "Um. Not yet. There's some clothing {i}I{/i} need to get."

show ethan unamusedbrow playfulmouth 
show blue confused 
show yellow blush
with dis

leaf @happy "But it's kinda a private thing, so[ellipses]"

if (HasEvent("Leaf", "AcceptedConfession")):
    leaf @talkingmouth "[first_name], you stick with me. Everyone else, you can go."

else:
    leaf @talkingmouth "Everyone else, you can go, but I'll stick around here for a while longer."

ethan @talkingmouth "Say no more. {i}Mrowr{/i}."

blue "Huh? I don't get it. What's private? It's just clothes, right?"

yellow @sadbrow talkingmouth "Um... yes, we'll, um, we'll go. Quickly."

show blue:
    xpos 0.2 xzoom 1
    pause 0.15
    ease 0.5 xzoom -1
    pause 0.15
    ease 0.5 xpos -0.2

show yellow behind blue:
    xpos 0.6
    ease 0.5 xpos -0.2

blue @confusedbrow talkingmouth "No, Seriously? What's going on? Did I miss something?"

yellow @sadbrow talking2mouth "Um, Blue, when someone says 'private clothes,' that means, um..."

show ethan playfuleyes neutraleyebrows
pause 0.2
show ethan playfuleyebrows
pause 0.2
show ethan neutraleyebrows
pause 0.2
show ethan playfuleyebrows
pause 0.2
show ethan neutraleyebrows
pause 0.2
show ethan playfuleyebrows
pause 0.2
show ethan neutraleyebrows
pause 0.2
show ethan playfuleyebrows
pause 0.2
show ethan neutraleyebrows
pause 0.2
show ethan playfuleyebrows

if (HasEvent("Leaf", "AcceptedConfession")):
    leaf @sarcastic "Yes, we saw the eyebrow thing."

else:
    leaf @sarcastic "Yes, I saw the eyebrow thing."

ethan @happy "Just making sure."

show ethan:
    xpos 0.4
    ease 0.5 xpos 1.2

pause 0.5

show leaf:
    xpos 0.8
    ease 0.5 xpos 0.5

if (not HasEvent("Leaf", "AcceptedConfession")):
    pause 0.5

    red @happy "Seeya."

    leaf @talking2mouth "Uh... you don't have to go, if you don't want to."
    leaf @happy "I'd appreciate your eye on an outfit I'm planning on buying, but, like, no pressure."
    leaf @sadbrow talkingmouth "And, full, confession, the outfit's a bit, um... 'skimpy?'"
    leaf @sadbrow talking2mouth "So, like, I'm not trying to seduce you by showing off my new outfit. I just, uh, feel a {i}tiny{/i} bit uncomfortable about it. Thought you might be able to help?"

    menu:
        "Skimpy outfits? Sign me up.":
            leaf @flirtbrow talking2mouth "Whoever said the way to a man's heart is through his stomach aimed too high."

            leaf @happy "But thanks, anyway. I appreciate you being here."

        "Nah, this sounds like trouble.":
            leaf @talkingmouth "Fair enough."

            red @talkingmouth "Won't be a problem, will it?"

            leaf @winkbrow talkingmouth "Nah, no problem. {i}Au revoir{/i}, Skippy."

            jump afterevents

$ AddEvent("Leaf", "SawBunny")

pause 1.0

red @confused "So, I'm flattered I'm here, but what exactly am I here for?"

leaf @talkingmouth "To stand there and look pretty, and tell me {i}I{/i} look pretty, mostly."

red @talkingmouth "You're always pretty, but you don't normally need me to tell you that. Something up?"

leaf @sadbrow talkingmouth "Um, yeah. Well, no. It's... Klara's party has a theme."

red @talking2mouth "Girls-only, right?"

leaf @sadbrow talkingmouth "Bunnies."

red @happy "Oh, that's cute."

leaf @flirtbrow talkingmouth "{i}Sexy{/i} bunnies."

red @surprised "Oh, that's hot."

leaf @happy "I've been to some wild parties before. I went to school in Goldenrod, you know? Party capital of Johto."
leaf @sadbrow talkingmouth "But that was high school. College is a different ball game."
leaf @closedbrow talking2mouth "And I just need you to come with me as I buy an outfit, put it on, and reassure me that I look like a bunny, and not a pig."

red @sadbrow talkingmouth "I can {i}guarantee{/i} you'll look great. If not more than great."
red @happy "You know, I {i}just{/i} went through this with Yellow. Want me to start chanting you a mantra, too?"

leaf @sarcastic "I'd rather you called me a pig, honestly."

scene blank2 with splitfade

pause 1.0

scene clothingstore with splitfade

redmind @think "Leaf's been a while[ellipses]"
redmind @closedbrow frownmouth "Maybe the outfit's hard to get on? I've got no idea how those things work."

pause 1.0

redmind @frownmouth "I wonder if I could make a game to pass the time. 'Is there anywhere I can look that does {i}not{/i} have the color pink within my field of vision?'"

pause 1.0

redmind @unamusedbrow unamusedmouth "And... I've lost already."

redmind @poutmouth "Maybe if I narrow my field of vision? Like, if I squint...?"

redmind @unamusedbrow unamusedmouth "[ellipses]Kinda? It's kinda working? I think I just need to squint some more--"

show blank2 with transeye

pause 1.0

redmind @closedbrow frownmouth "Nope, roll it back. That was too far. That was too much. You've closed your eyes now."
redmind @closedbrow poutmouth "Although... if we're doing a literalist interpretation of the very loosely-defined rules of the game... maybe this is allowed?"

pause 1.0

red @closedbrow talking2mouth "I'm going insane. I've been left alone for five minutes, and I'm already going insane."

$ showredonly = True

leaf "Good news, then, Skippy. I'm back."

$ showredonly = False

hide blank2 
show leaf blush bunny
with transeye2

red @surprisedbrow talking2mouth "{size=30}Wow.{/size}"
red @sweat talkingmouth "Well, don't you look like a walking felony?"

leaf @happy "Thank you. You're so sweet."
leaf @flirtbrow talkingmouth "So, piggy or bunny?"

red @talking2mouth "Yeah, uh, lots of thoughts are coming to mind, but 'oink oink' is not one of them."

leaf @flirtbrow talkingmouth "Good to hear. You think I'll be popular at the party, then? Drive all the boys wild?"

red @happy "All the boys at this girls-only party? Yeah, absolutely."

leaf @closedbrow talkingmouth "Alright. I can't walk in these shoes, but it's not like I'm going to need to run anywhere, so... I'd call this a success."

red @talking2mouth "It will take every molecule of my being to not ask for every sordid detail about that party."

leaf @happy "Oh, if there are any worth sharing, you won't have to ask."

if (HasEvent("Klara", "BrokeBond")):
    leaf @sadbrow talkingmouth "But I won't have {i}too{/i} much fun. My mission number one is to figure out why Klara was being weird."

    leaf @closedbrow talking2mouth "You know, it just occurred to me I might have to have a friend-breakup while wearing this outfit."

    red @sadbrow talking2mouth "Well, Klara'll be wearing one as well. Better than being overdressed in that case, I think."

    leaf @talkingmouth "True."

leaf @closedbrow talkingmouth "Anyway, I'm... actually feeling pretty confident now, so, um, thanks. I appreciate you being here for me."

red @talkingmouth "I can pretty much guarantee that anytime you're in a bunny suit, I'll be there for you."

leaf @flirtbrow talkingmouth "Except at the girls-only party."

red @talking2mouth "Damn my lactose intolerance. It's the only thing stopping me."

leaf @happy "Alright, I'm getting out of this very cute and sexy item of objectification. Can't let the matriarchy know I'm making deals with the patriarchy's agent to get access to his gold card."

red @sadbrow talkingmouth "Leaf, I'm just going to come out and say it--I think we have too many running jokes."

leaf @closedbrow talkingmouth "You're allowed to be wrong."

scene blank2 with splitfade

pause 1.0

narrator "Leaf changes, purchases the costume, then heads back to campus. You decide to wander around Inspira for a while longer before heading back..."

label afterevents:

$ location = "city"
call silence() from _call_silence_2
$ renpy.music.queue("audio/music/GSCBike_Start.ogg", channel='music', loop=None, fadein=1.0, tight=None)
$ renpy.music.queue("audio/music/GSCBike_Loop.ogg", channel='music', loop=True)
$ freeroaming = True

call city() from _call_city_1

call clearscreens() from _call_clearscreens_272

scene blank2 with splitfade

show night at vspaz

pause 3.0

$ timeOfDay = "Night"

show screen currentdate with dis

if (not skipnightscenes):
    call nightscenequeue from _call_nightscenequeue_1

call texting() from _call_texting_29

jump day010604
