label secondhomeroom010602:

scene blank2 with splitfade

play music "Audio/Music/Oak Intro.ogg" noloop
queue music "Audio/Music/Oak Class.ogg"
$ renpy.music.queue("Audio/bigcrowdloop.ogg", channel='crowd', loop=True, fadein=0.5)

show homeroom behind blank2

show oakbg behind blank2
    
$ renpy.transition(dissolve)
show screen currentdate

hide blank2 with splitfade

oak @happy "Welcome back to class, ladies and gentlemen!" 

pause 1.0

oak @talking2mouth "I'm of sound enough mind to recognize that you're all far too interested in the upcoming Millennium Drop Water Festival Contest tryouts for me to impart much knowledge today."
oak @sadbrow talkingmouth "Ah... perhaps a professor of greater skill could, but I believe I'm at my limit, in that regard."
oak @closedbrow talkingmouth "Well, that's fine. Perhaps we'll just do some review for now. Tomorrow's quiz should not be overly challenging, as long as one understands the intricacies of spread moves."
oak @talkingmouth "Now, who remembers what we were talking about this morning? Yes, Explosion. A classic Normal-type move, one with 250 power. Let's carry on that topic[ellipses]"

scene blank2 with splitfade

$ PlaySound("bellchime.ogg")

pause 1.0

narrator "[bluecolor]After your free time is over, it will be time to attend the Millennium Drop Water Festival Contest tryouts.{/color}"
narrator "You will need to decide whether you want to join, and if so, whether you want to partner with someone, and if so, whom with."
narrator "[bluecolor]Make sure to handle any last-minute business you need to before the tryouts!{/color}"

$ skipnightscenes = True
call freeroam() from _call_freeroam_40
$ skipnightscenes = False

scene blank2 with splitfade

narrator "It is finally time. Time to decide. Will you attend the Millennium Drop Water Festival Contest Tryouts?"
narrator "If you do not, it is quite possible that {color=#f00}you will never attain success as a coordinator.{/color}"

$ removestudents = { "Leaf", "Ethan", "Blue", "Yellow", "May", "Brendan", "Klara", "Jasmine", "Misty", "Serena", "Dawn", "Tia", "Calem", "Grusha", "Gardenia" }

menu:
    ">Attend":
        $ AddEvent("Professor Oak", "ParticipateMDTryouts")

    ">Attend, and decide when you get there":
        $ AddEvent("Professor Oak", "WatchMDTryouts")

    ">Go back to the dorm":
        $ AddEvent("Professor Oak", "IgnoreMDTryouts")
        scene relichall_B
        show klara neutralcoat makeup hairpin at night
        with splitfade

        jump klaraconvince

if (not HasEvent("Professor Oak", "LearnedAboutContestColiseum")):
    $ AddEvent("Professor Oak", "LearnedAboutContestColiseum")

    narrator "By asking around, you're able to learn the location of the Contest Coliseum, where the Millennium Drop Tryouts are meant to be held..."

$ hideside = True
call clearscreens() from _call_clearscreens_260

scene blank2
show blank2 as secondblank2
with splitfade

pause 1.0

$ HealParty()

show concerthallstagemidnight behind secondblank2
show blank as secondblank behind secondblank2
$ renpy.music.play("Audio/Stadium_crowd.ogg", channel='crowd', loop=True, fadein=1.5)
$ renpy.music.play("Audio/Stadium_chant.ogg", channel='crowd2', loop=True, fadein=1.5)

$ renpy.pause(0.75, hard=True)
stop music fadeout 1.5

$ renpy.music.queue("Audio/Music/contestintro.ogg", channel='music', loop=True, fadein=1.5, tight=None)
show screen songsplash("Pokémon Contest! (Hoenn) Remastered", "Zame")

$ renpy.pause(1.0, hard=True)

hide secondblank2 with transball
$ renpy.pause(0.25, hard=True)
show blank as secondblank:
    alpha 1.0
    ease 0.5 alpha 0.0

show concerthallstagemidnight:
    subpixel True
    zoom 3.0 alpha 0.65 xalign 0.15 ypos 2600
    ease 1.25 alpha 1.0 xalign 0.0 ypos 3000
    xalign 0.85 alpha 0.65 ypos 2600
    ease 1.25 alpha 1.0 xalign 1.0 ypos 3000
    xalign 0.5 alpha 0.4 ypos 2400
    ease 1.0 alpha 1.0 zoom 1.0 ypos 1080

lisia "{size=50}LADIES!{/size}"

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

hide blank as firstblank
hide evening
hide blank
        
pause 2.0

lisia "{size=50}AND!{/size}"

pause 2.0

show concerthallstagenight behind beam1:
    alpha 1.0 zoom 1.0 yalign 1.0 xalign 0.5
show blank behind beam1

pause 0.05

hide blank with slowdis

lisia "{size=50}GENTLEMEN!{/size}"

pause 1.0

$ hideside = False

if (HasEvent("Professor Oak", "ParticipateMDTryouts")):
    red @sadbrow talkingmouth "Oh, man. This is reminding me of the Battle Team tryouts. Only difference is, in the tryouts, I knew what I was doing."
    red @happy "This time, I'm pretty much going in blind!"

else:
    red @talkingmouth "Huh, this kind of reminds me of the Battle Team tryouts."

stop music fadeout 3.5 channel "crowd2"

show lisia with Dissolve(2.0)

lisia @happymouth "Ladies and gentlemen! Thank you so much for coming out here, today! Are you excited to watch the Millennium Drop Water Festival tryouts?!"

$ PlaySound("crowd_cheer.ogg")

pause 0.5

lisia @happy "{i}Great!{/i} I am, too! The Millennium Drop is one of the oldest contests practiced in Hoenn, performed for over two thousand years!"
lisia @angrybrow talkingmouth "It's a celebration of the fundamentals of contest--Beauty and Cuteness! For everyone who ever wanted to be a Coordinator, there's no place better to start than the Millennium Drop Water Festival Contest!"
lisia @happy "And {i}today{/i} we'll be holding the tryouts to see who can pass into the consideration rounds! The winner of each tryout group will be able to perform for a worldwide broadcast--a live, televised match, announced by me, Lisia!"

$ PlaySound("crowd_cheer.ogg")

pause 1.0

show phobos:
    xpos 1.2
    ease 0.5 xpos 0.66

python:
    renpy.music.set_volume(0.7, delay=1.0, channel="music")
    renpy.music.set_volume(0.7, delay=1.0, channel="crowd")
    renpy.music.set_volume(0.7, delay=1.0, channel="crowd2")

show lisia surprisedbrow frownmouth with dis:
    xpos 0.5
    ease 0.5 xpos 0.33

phobos @sadbrow talkingmouth "Oh dearie, dearie, {i}dearie{/i} me, Lisia. Has no-one told you? It seemed there was a bit too large a crowd here."

lisia @talking2mouth "Sorry, Baron Lawrence Phobos?"

phobos @closedbrow sweat talking2mouth "'The Third,' if you please, but good effort."
phobos @talkingmouth "Well, I'm terribly afraid that it seems someone may have disconcaredly dropped the ball, as it were. The Poké Ball, if I may perhaps permit punitive punnery posthaste."

lisia @sadbrow talkingmouth "Baron Lawrence Phobos... {w=0.5}{i}The Third{/i}, what do you mean? I'm doing a show right now, I--"

phobos @happy "This shan't take three minutes of your time."

phobos @talkingmouth "You see, I'm afraid, though it appears you have failed to keep yourself informed, I'm here to rescue you, by clarifying the particulars of the issue."
phobos @closedbrow talkingmouth "Yes, all these... {i}others{/i} simply do not need to be here. This contest is open to Kobukan Students only."

pause 1.0

lisia sadbrow frownmouth @talkingmouth "What?"

phobos @happy "Yes, yes, yes, it's quite necessary, I'm afraid. Nothing that can be done about it, as I requested it, and have no inclination to change my mind."

lisia @talking2mouth "...Why? There's--there's so many people here, from all different regions, who came here just to participate. The Millennium Drop Water Festival Contest is a contest to celebrate togetherness, and wishes coming true."
lisia @sadmouth "So many people's wishes will--"

phobos @happybrow talkingmouth "Now, now, now. There's no need to coordinatorsplain to me. I'm quite aware of the history behind this contest."
phobos @closedbrow talking2mouth "We simply have the opportunity to make the tryouts... mmm, shorter."
phobos @winkbrow talkingmouth "Why, you know that one of your club members would win, no? Why bother with the hassle of weeding out all this chaff when I could do the same thing with the stroke of a pen?"

pause 1.0

phobos @talking2mouth "Otherwise, we would be here all night. By eliminating this indelicate refuse, we can shorten the contest to the work of half an hour. More efficient, no?"

lisia @sadbrow talking2mouth "It's a contest. Performing in them is meant to be {i}fun{/i}. It doesn't matter how long it takes if everyone's having fun, right?"

phobos frownmouth @closedbrow talking2mouth "Well, {i}I'm{/i} no longer having fun, and have grown quite bored of this conversation. May I assume your unconditional capitulation?"

lisia "[ellipses]"
lisia angrybrow frownmouth @poutmouth "You may not."

phobos @confused "Oh? I was given to understand that you wished to impress me by placing your club members on the winner's podium."

lisia @talking2mouth "I {i}do{/i} want to. And I will. But if only my club members can participate, then of course they're going to be on the podium! There's no glory in that. The Millennium Drop Water Festival Contest--"

phobos angrybrow frownmouth @angry "Must you say the entire thing {i}every{/i} time?! Clearly, you do not care for the time you waste, but I rather care for mine!"

pause 1.5

phobos -angrybrow -frownmouth @closedbrow talking2mouth "Apologies, that outburst was beneath me."
phobos @sadbrow talkingmouth "I simply wished to ensure that my--{i}your{/i} club members have the greatest chance of attaining all three victory slots."
phobos @sad2brow talkingmouth "It would be {i}embarrassing{/i}, I'm sure you agree, if some greasy nobody crawled out of Inspira and sullied the podium that rightfully ought to be our--{w=0.5}our students'."

lisia -angrybrow  @talking2mouth "I understand. Maybe I was being a bit hostile, as well. I'm sorry, I've just... I've never heard of a judge trying to stop people from participating in a contest."

phobos @happy "Such a thing does require an uncommon mind, yes."

show lisia surprisedbrow with dis

phobos @talkingmouth "So, we're agreed? You'll send this rabble back? If you'd prefer, I can make the announcement."

pause 1.0

show phobos angryeyebrows playfuleyes frownmouth with dis

lisia angrybrow @talking2mouth "No. If there's anyone out there who wants to participate in the tryouts, we'll let them. We can't be scared of a little competition."

pause 1.0

phobos @upeyes talking2mouth "I shan't ask a third time."

lisia @talking2mouth "I'm not going to say 'no' a third time, either."

pause 1.0

phobos angrybrow @angry "It will be difficult for you, or any of your clubmates, to {i}impress{/i} me, Lisia, if my feelings remain hurt."

lisia @talking2mouth "We'll figure something out. We appreciate how you've fought for this club, and what you've said you'll do for us. But I need to put my foot down here."

phobos @talking2mouth "I suppose that is the prerogative of the abled. I will be keeping a very keen eye on your future club meetings, Lisia--and I suggest you do {i}not{/i} debate my meritorious ideas in the future."

lisia "[ellipses]"

phobos "[ellipses]"
phobos neutraleyebrows neutraleyes neutralmouth @talkingmouth "What's my name?"

lisia @surprisedbrow talking2mouth "I--I beg your pardon?"

phobos @talkingmouth "I don't care to repeat myself. Repeating myself is one of my least favorite things to do. Given my dislike of repeating myself, this is the last time I'll ask. What's my name?"

lisia @sadbrow frownmouth "[ellipses]"

phobos @closedbrow talking2mouth "Slipped your mind? Not a good look, to forget the name of the man who bought the floor you're standing on.{w=0.5} (And every wall.)"

lisia "[ellipses]"
lisia @angrymouth "Baron Lawrence Phobos.{w=0.5} The Third."

phobos @happy "Well done."

hide phobos with dis

lisia angrybrow frownmouth "[ellipses]"

pause 3.0

lisia -angrybrow -frownmouth @happy "Alright, contestants, please proceed to the backstage area! We're so happy to have all of you here--Inspira citizens, Kobukan students, and everyone else!"

hide lisia with dis

redmind @sadbrow "She's a professional to the end."

show leaf with dis:
    xpos 0.33 xzoom -1

leaf @talking2mouth "So, that was {i}gross{/i}."

red @closedbrow talking2mouth "You're telling me. Lisia's World Contest Champion, but I guess even the World Contest Champion has to respect people with a lot of money."

show blue with dis:
    xpos 0.66 xzoom -1

blue @talking2mouth "Lisia could've whupped that guy's ass. He wouldn't last two minutes in the ring with her Altaria."

leaf @talkingmouth "I kinda agree. I guess she's thinking about the long-term health of Coordinating, as an entire hobby or whatever."

blue @closedbrow talking2mouth "It's not just a hobby. It's a lifestyle, like being a Pokémon Trainer."

leaf @happy "Hey! Blue up to bat for the girls in skirts?"

blue @embarrassedbrow embarrassedmouth "Uh, it's just... it's just something Yellow's said over and over for the past week."

leaf surprisedbrow frownmouth @neutralbrow talking2mouth "Speaking of which, where {i}is{/i} our cinnamon roll?"

blue @closedbrow talking2mouth "Backstage."

leaf @talking2mouth "Wait, you mean she--she's doing it?"

blue @closedbrow talking2mouth "I guess you wore her down. You {i}do{/i} do that.{nw}" 

show leaf flirtbrow frownmouth with dis

extend @closedbrow talking2mouth " Like mold."

leaf @sarcastic "So close, but that's still not how regular people interact. You'll get it next time."

blue @angry "What do you want from me?! I wish you {i}hadn't{/i} convinced Yellow to go through with it! Now I'll probably have to go to more of these dumb things!"

leaf @closedbrow talkingmouth "Yeah, well, I'm an instigator."

blue surprisedbrow frownmouth @glancebrow talking2mouth "Yeah, like--"

leaf @sarcastic "Dude, shut up. I've been trying to talk to [first_name] here for, like, five minutes."

blue angry "Gah!"

show blue:
    xpos 0.66
    ease 0.7 xpos 0.68
    ease 0.2 xpos -0.2

pause 1.0

show leaf:
    xpos 0.33 xzoom -1
    ease 0.5 xpos 0.5

leaf -flirtbrow -frownmouth @talkingmouth "So, we know Yellow's doing it. I'm really glad."
leaf @sadbrow talkingmouth "I can't really understand why she doesn't like battling, but hopefully contests become her 'thing.'"

red @happy "Everyone needs a 'thing.'"

leaf @talkingmouth "True."
leaf @talkingmouth "So. Moment of truth, big guy. Are you going to participate in the tryouts?"

if (HasEvent("Professor Oak", "ParticipateMDTryouts")):
    red @happy "Sure am. Never done it before, but, hey, I never beat an Altaria before I did, either."

    jump leafjoinresponse

menu:
    "Yeah.":
        jump leafjoinresponse

    "Nah, I just came to watch.":
        leaf @talkingmouth "Fair. You've got so much going on. Not sure how you find time for it all, nevermind everything that learning to be a Coordinator would add to it."

        leaf @happy "Come sit with me, then. Ethan's there, too. We bought some shaved ice."

        red @happy "Sure."

        hide leaf with dis

        pause 1.0

        show klara neutralcoat makeup hairpin with dis

        jump klaraconvince

label leafjoinresponse:
    $ ValueChange("Leaf", 1)

    leaf @happy "Seriously? Dude, that's incredible. You do so much, already, I don't know how you'll even have time for this."
    leaf @sadbrow talkingmouth blush "But if anyone can do it, I bet it's you. Hey, maybe this'll be the first Pokémon Contest I don't fall asleep during!"

    red @winkbrow talkingmouth "Wish me luck."

    leaf @flirtbrow talkingmouth "You don't need it. Knock 'em dead, Skippy."

    jump mdtryouts

label klaraconvince:
    stop music fadeout 1.5
    
    queue music "audio/music/everyonesfavoritegirl_start.ogg" noloop
    queue music "audio/music/everyonesfavoritegirl_loop.ogg"

    klara @happy "Heeyyyy, [first_name]!"

    red night @happy "Oh, hey, Klara."

    klara surprisedbrow frownmouth @neutralbrow talkingmouth "I'm glad I caught you. C'mon."

    red @talking2mouth "Ah, nah, sorry."

    pause 1.0

    klara @talking2mouth "Um. Sorry, I think I misheard you?"

    red @talkingmouth "I'm not going to participate in the tryouts. Sorry."

    klara "[ellipses]"

label klaraconvincepartner:
    $ AddEvent("Klara", "UsedLeverage")

    klara @happy "Hey, [first_name], what are you saying? Is this some kind of unfunny joke?"

    if (HasEvent("Klara", "DenyPartner")):
        red @sadbrow talkingmouth "No, sorry. I just--I was talking to Yellow, and I don't think I have the skills for this. I'm pretty sure I'd just drag you down. I mean, I've never coordinated before. At {i}all{/i}."

        klara @happy "Oh, don't worry about that. You'll be a natural. Come on, let's go. I need a partner, after all!"

    else:
        red @sadbrow talkingmouth "No, sorry. I've just got a {i}ton{/i} going on, you know? I can't take on learning to be a coordinator at the same time."

        klara @happy "Oh, don't worry about that. You'll be a natural. Come on, let's go. I need a partner, after all!"
        
    menu:
        "Alright, you got me.":
            $ AddEvent("Klara", "AgreePartner")
            if (HasEvent("Professor Oak", "IgnoreMDTryouts")):
                jump mdtryouts
            else:
                jump mdtryoutsbegin

        "No, I'm serious.":
            $ AddEvent("Klara", "UsedLeverage2")
            klara "[ellipses]"

            klara @talking2mouth "Okay, I'm just a bit confused. You said you'd partner with me."

            red @wince talking2mouth "I[ellipses] okay, I don't remember saying that, but if I did, I'm sorry. I guess I changed my mind...?"

            klara sadbrow @sadbrow talking2mouth "[first_name], I really like you. And I like you because of how you always do what you say. You know what I mean, right...?"

            red @sadbrow talkingmouth "I think so? But, again, I'm really sorry, I don't remember ever agreeing to partner with you. I mean, I remember you saying you wanted to partner with me, but..."

            klara @sadbrow talking2mouth "I... guess you don't remember that conversation."
            klara @sad "Well... it meant a lot to me. But I guess I {i}often{/i} feel too hard."
            klara @sadbrow talking2mouth "I'm sorry. I should've told you how I felt. How {i}important{/i} this was to me."
            klara @sadbrow talking2mouth "This contest means everything to me. {i}Everything{/i}. Participating in the Millennium Drop Water Contest Festival is the entire reason I'm at Kobukan."
            klara @puppybrow talkingmouth "I... I dreamed that I'd take the stage, with a man as handsome and strong as you by my side, and... and maybe, for once, people would look at me with something other than disgust."

            red @sadbrow talkingmouth "What? Disgust? Why would they...?"

            klara @talking2mouth "I know you probably can't understand it, and I hope you don't think I was, like, lying to you or anything, but..."
            klara @sadbrow talking2mouth "I'm poor. I'm {i}really{/i} poor, [first_name]. I don't even know how I'll pay for Kobukan. I thought the scholarship from this contest could... could fix that."
            klara frightenedbrow frownmouth @talking2mouth "I know, it's... it's silly. I'm sorry. I'm really scared of telling you that, so... please, {i}please{/i} don't make fun of me."

            red @sadbrow talking2mouth "N-no. No, I wouldn't make fun of you for that. I... I mean, I also..."

            klara puppybrow -frightenedmouth @talkingmouth "I {i}need{/i} to win this contest. I need to win, so I can afford Kobukan, so I can make something of myself, {i}force{/i} people to pay attention to me, and bring light back to my hometown."

            if (HasEvent("Professor Oak", "WatchMDTryouts") or HasEvent("Klara", "DenyPartner")):
                show klara:
                    ypos 1.0
                    ease 0.5 ypos 1.2 zoom 1.3
            
            else:
                show klara at night:
                    ypos 1.0
                    ease 0.5 ypos 1.2 zoom 1.3


            klara @talking2mouth "That's why I need you. Please. {i}Please,{/i} [first_name]."

            menu:
                "How could I say no?":
                    $ AddEvent("Klara", "AgreePartner")
                    if (HasEvent("Professor Oak", "IgnoreMDTryouts")):
                        jump mdtryouts
                    else:
                        jump mdtryoutsbegin

                "I said no.":
                    if (GetRelationshipRank("Klara") < 1):
                        $ AddEvent("Klara", "RejectNoLeverage")
                        show klara wrathbrow frownmouth with dis

                        $ ValueChange("Klara", -30)

                        pause 1.0

                        klara angrybrow madmouth "{i}Ffffine.{/i}"

                        hide klara with dis

                        pause 1.5

                        redmind @thinking "I mean... I feel a bit bad about it, but I'm really not sure if I could even help her..."
                        
                        if (HasEvent("Klara", "DenyPartner")):
                            jump formpartner

                        elif (HasEvent("Professor Oak", "IgnoreMDTryouts")):
                            scene suitenight with splitfade

                            narrator "You arrive back at the dorm[ellipses] but find there's no-one there."

                            red @closedbrow talking2mouth "Oh, yeah, they're probably at the tryouts, if they went with Yellow."
                            red @happy "Well, I don't know about {i}them{/i}, but I'm going to bed!"

                            call texting() from _call_texting_23
                        
                        else:
                            narrator "Hurt and confused, you forgo texting, and decide to head straight to bed."

                        jump day010603   

                    $ AddEvent("Klara", "UsedLeverage3")
                    klara "[ellipses]"

                    klara -puppybrow frownmouth @talking2mouth "[first_name], you're a good guy."
                    klara @talkingmouth "A lot of people spread awful rumors about you, but I never believed them. I know that, when the chips are down, you'll help your friends."
                    klara @sadbrow talkingmouth "And we're friends, right? So... you'll help me, right?"

                    red @confused "Um. Look, I feel like we're going in circles. You need to take 'no' for an answer, because it's the only one I'm giving."

                    if (HasEvent("Leaf", "RejectedConfession")):
                        klara @talking2mouth "Really? Because Leaf didn't take no for an answer, and she still got a date."

                        red @closedbrow sweat talking2mouth "That wasn't a date. We were hanging out, like friends. If just hanging out at a café was a date, then I've gone on dozens of dates this year."
                        red @unamusedbrow sweat talking2mouth "And for what it's worth, she {i}did{/i} take no for an answer. She asked me, once, if I wanted to go on a date with her. You've asked me three times, in this conversation, if I'll partner with you."

                    klara @restrainedbrow talking2mouth "[first_name], you're... you're a great guy, really."
                    klara @wrathmouth restrainedbrow "And I {i}really{/i} want everyone to keep seeing you like this."
                    klara @sadbrow talkingmouth "But I have a lot of friends, you know? And if I can't stay in Kobukan, because you decided you didn't want me around, they'll ask me why I have to leave, and then I'll have to tell them."

                    red @confused "...Wait."

                    klara @sadbrow talkingmouth "I'm not threatening you! I'm really not. I'd never do that. I think you're the coolest, nicest guy, ever."
                    
                    $ penalty = 0

                    if (HasEvent("Klara", "FirstKiss")):
                        $ penalty += 1
                        klara @sadbrow talking2mouth "It's just... you know, we kissed in the garden. You came to me. And you were so forceful, and manly, and[ellipses]"
                        klara @sadbrow talkingmouth "I mean, I really thought we'd hit it off. We {i}kissed{/i}, [first_name]."
                        klara @sadbrow talking2mouth "I'm not one of those sluts who gets on her knees on the first date. A kiss {i}means{/i} something to me. And I thought it meant something to you."
                        klara @happy "I really liked it."

                    if (not HasEvent("Klara", "VeryCharming")):
                        $ penalty += 1
                        klara @sadbrow talkingmouth "When we went on our date, I tried to make myself look really good, you know? I dressed up all nicely. And the first thing you did when you saw me was insult my outfit."

                    if (HasEvent("Klara", "DrinkWithKlara")):
                        $ penalty += 1
                        klara @sadbrow talkingmouth "Then, when I took you to the club, well, I really appreciate that you drank with me, but[ellipses] you really {i}shouldn't{/i} have, you know? We're in Kobukan, not Kanto or Galar."

                    if (HasEvent("Klara", "PaidForDrinks")):
                        $ penalty += 1
                        klara @sadbrow talkingmouth "You paid for me to drink. Which, you know, I really liked. It was {i}very{/i} gentlemanly of you." 
                        klara @happy "But, um, it is a {i}bit{/i} illegal... and kind of suspicious? Someone who likes you less might see that and think you were trying to take advantage of me."

                    klara @blush talkingmouth "And after, when we went to Wallace's pool... well, we shouldn't have been there, in the first place."
                    klara @happy "I mean, I was really drunk! Bringing a drunk girl into the faculty pool? {i}Everyone{/i} knows what that means."
                    klara @ojoubrow talkingmouth "And what it means doesn't really look great for the guy, you know?"
                    
                    if (HasEvent("Klara", "FirstBase")):
                        if (HasEvent("Klara", "YouAreDrunk")):
                            $ penalty += 1
                            klara @talking2mouth "I mean, you even pointed out I was drunk."
                            klara @angrybrow talking2mouth "But we still had sex."
                        else:
                            $ penalty += 1
                            klara @angrybrow talking2mouth "And then we had sex."                        

                    red @wince talking2mouth "Please don't say that so loudly."

                    klara @sadbrow talkingmouth "I'm trying to protect you, [first_name]."
                    klara @talking2mouth "I just don't want anyone to hear any of this and think less of you for it."
                    klara @sadbrow talkingmouth "I'm amazing at keeping secrets. No-one will get anything from me. But... you know, secrets have a way of spilling..."

                    red @sadbrow talking2mouth "I[ellipses]"

                    pause 1.0

                    narrator "Your throat starts to tighten up, in that familiar, uncomfortable, restricting way."

                    red @closedbrow talking2mouth "I think... I think I need some fresh air, I... I need some time to think, I..."
                    
                    klara @happybrow talkingmouth "You don't need time to think, [first_name]. Just be my partner, and everything will be fine. People will see that whatever you did, it's fine, because we're besties."

                    menu finalklaraleveragechoice:
                        "Yes. Besties.":
                            $ AddEvent("Klara", "AgreePartner")
                            klara happy "Yay! Knew we could get there eventually."

                            if (HasEvent("Professor Oak", "IgnoreMDTryouts")):
                                jump mdtryouts
                            else:
                                jump mdtryoutsbegin

                        "N-no. No, I can't." if (not HasEvent("Klara", "FinalKlaraLeverageChoice1")):
                            $ AddEvent("Klara", "FinalKlaraLeverageChoice1")
                            pause 1.0

                            klara wrathbrow wrathmouth "What?"

                            narrator "...Please, [first_name], think about this. If people find out... you've done {i}so{/i} well, recovering your reputation after the Frienergy thing. This could be a disaster."
                            narrator "Don't put us through that again."

                            jump finalklaraleveragechoice

                        "No. No, I can't." if (HasEvent("Klara", "FinalKlaraLeverageChoice1") and not HasEvent("Klara", "FinalKlaraLeverageChoice2")):
                            $ AddEvent("Klara", "FinalKlaraLeverageChoice2")

                            pause 1.0

                            narrator "God damn it! Why are you being stubborn?! She's the correct option! You'll get everything you want! A fast lay, the strongest partner in the contest, a guaranteed shot at the scholarship!"
                            narrator "Do you want to play the game or not?! What the hell are you trying to prove?! Gonna screenshot yourself rejecting her and put it up on the internet, like you're virtue-signalling turning down a digital girl?"
                            narrator "This is pathetic. Just partner with her. {i}That's how it's supposed to go.{/i}"

                            jump finalklaraleveragechoice

                        "No! No, I won't!" if (HasEvent("Klara", "FinalKlaraLeverageChoice2") and not HasEvent("Klara", "FinalKlaraLeverageChoice3")):
                            $ AddEvent("Klara", "FinalKlaraLeverageChoice3")
                            
                            pause 1.0

                            if (HasEvent("Klara", "FirstBase") and HasEvent("Klara", "YouAreDrunk")):
                                $ penalty += 2

                            narrator "Alright. Cards on the table. Klara's going to spread rumors about you. Every single bondable is going to take a negative [IntToWord(penalty)] to their bond {i}and{/i} mood."
                            
                            python:
                                highestbond = "Ethan"
                                secondhighestbond = "Leaf"
                                highestbondvalue = GetCharValue("Ethan")
                                secondhighestbondvalue = GetCharValue("Leaf")
                                for char in persondex.keys():
                                    if (char == "Klara"):
                                        continue
                                    val = GetCharValue(char)

                                    if (val > highestbondvalue):
                                        secondhighestbond = highestbond
                                        secondhighestbondvalue = highestbondvalue
                                        highestbond = char
                                        highestbondvalue = val
                                    elif (val > secondhighestbondvalue and char != highestbond):
                                        secondhighestbond = char
                                        secondhighestbondvalue = val

                            if (HasEvent("Klara", "FirstBase")):
                                narrator "Plus, every character will know you slept with her. I'm serious, there's a database. Trying to stay all 'pure' and 'virginal' for [highestbond] or [secondhighestbond]? Well, now you can't."
                            narrator "This isn't a fakeout or a secret test of character. There are literal, permanent, mechanical, disadvantages to taking this course of action. So PICK.{w=0.5} SOMETHING.{w=0.5} ELSE."

                            jump finalklaraleveragechoice

                        "No." if (HasEvent("Klara", "FinalKlaraLeverageChoice3")):
                            pause 1.0

                            $ AnimateValueChange(-GetValue("Klara"), 0.5, True)

                            klara wrathbrow wrathmouth "God {i}damn{/i} it."

                            hide klara with dis

                            stop music fadeout 1.5

                            python:
                                AddEvent("Klara", "FormerBond" + str(GetValue("Klara")))
                                AddEvent("Klara", "BrokeBond")
                                persondex["Klara"]["Mood"] = 0
                                persondex["Klara"]["Value"] = 0
                                persondex["Klara"]["Nature"] = TrainerNature.Special

                            narrator "You're confused and hurt. The one thing you {i}can{/i} understand, though, is that your understanding of Klara was entirely incorrect."
                            narrator "[bluecolor]Your bond with Klara has been revealed to be fake.{/color}"

                            pause 1.0
                            
                            if (HasEvent("Klara", "DenyPartner")):
                                jump formpartner

                            elif (HasEvent("Professor Oak", "WatchMDTryouts")):
                                $ renpy.music.queue("Audio/Music/contestintro.ogg", channel='music', loop=True, fadein=1.5, tight=None)
                                show screen songsplash("Pokémon Contest! (Hoenn) Remastered", "Zame")

                                narrator "You go back to where the rest of your dormies are sitting, and watch the tryouts as they unfold."
                                narrator "All of you cheer very loudly when it's Yellow's turn to perform. She seems nervous, but squints out into the stands, seems to see you, and gives you a little wave."
                                
                                $ ValueChange("Leaf", 3, 0.25, False)
                                $ ValueChange("Ethan", 3, 0.5, False)
                                $ ValueChange("Blue", 3, 0.75)

                                narrator "You cheer on Yellow with your dormmates! By the end of it, you're exchanging high-fives, and are starting to see what {i}some{/i} people see in contests--even if it's not {i}exactly{/i} your speed."
                                narrator "Eventually, the night wraps up..."

                                $ coordinatingknowledge += 20
                                narrator "For watching your first Pokémon contest... your [contestcolor]Coordinating Knowledge{/color} went up by twenty!"

                                jump day010603

                            else:
                                narrator "Hurt and confused, you forgo texting, and decide to head straight to bed."

                                jump day010603   

label mdtryouts:
    $ AddEvent("Professor Oak", "ParticipateMDTryouts")

    stop music channel "crowd" fadeout 2.5
    stop music channel "crowd2" fadeout 2.5

    scene concerthallbackstage
    show yellow sadbrow frownmouth 
    with splitfade

    yellow @talkingmouth "{size=30}Cool, Beautiful, Cute, Clever, Tough. Cool, Beautiful, Cute, Clever--{/size}"

    red @talkingmouth "Hey, Yellow."

    yellow @surprisedbrow talking2mouth "Oh. Hello."
    yellow -frownmouth @sadbrow talking2mouth "I guess I'm doing this..."

    red @happy "You'll be great. Don't worry about it."

    yellow @sadbrow talkingmouth "I hope so. I... I hope I, at least, am not the worst in my group."
    yellow @sadbrow talkingmouth "But everyone else here has probably performed so many times, and I'm a complete novice."
    yellow @sadbrow talkingmouth "It almost seems silly to imagine that I could even... do {i}anything{/i}."

    red @sadbrow talkingmouth "Even Cynthia was a novice once. Don't worry about it."
    red @talking2mouth "Oh, yeah, do you have a partner?"

    yellow @happy "Oh, I should've, but since I only decided I was actually going to do it about half an hour ago, I didn't get one."
    yellow @surprisedbrow talking2mouth "Oh! That reminds me--I need to pick up some props. Um, if they try to start without me, then--"
    yellow @sadbrow happymouth "...Let them?"

    hide yellow with dis

    if (HasEvent("Klara", "AgreePartner")):
        klara makeup hairpin neutralcoat @happy "Cute girl. She's really not a threat at all, is she?"

        red @confused "Huh?"

        klara @winkbrow talkingmouth "No~othing!"
        
        jump mdtryoutsbegin

    else:
        red @talking2mouth "Huh. I thought she was going to--"

        show klara neutralcoat makeup hairpin with vpunch
        
        play music "audio/music/everyonesfavoritegirl_start.ogg" noloop
        queue music "audio/music/everyonesfavoritegirl_loop.ogg"

        klara @happy "Heeyyyy, [first_name]!"

        red @happy "Oh, hey, Klara."

        klara surprisedbrow frownmouth @neutralbrow talkingmouth "I'm glad I caught you. Partners, right?"

        menu: 
            "Ah, nah, sorry.":
                $ AddEvent("Klara", "DenyPartner")
                pause 1.0

                klara @talking2mouth "Um. Sorry, I think I misheard you?"

                red @talkingmouth "I'm not going to partner with you. Sorry."

                klara "[ellipses]"

                jump klaraconvincepartner

            "Yep, let's go!":
                $ AddEvent("Klara", "AgreePartner")
                $ ValueChange("Klara", 10)

                klara @happy "Cool. That's another thing I love about you. You always do what you say you will!"

                jump mdtryoutsbegin

label formpartner:
    stop music fadeout 1.5

    $ renpy.music.queue("Audio/Music/contestintro.ogg", channel='music', loop=True, fadein=1.5, tight=None)
    show screen songsplash("Pokémon Contest! (Hoenn) Remastered", "Zame")
    
    show yellow with dis
        
    yellow @closedbrow talking2mouth "Okay, got them. I--"
    yellow surprisedbrow frownmouth @talking2mouth "Oh. You're still here? I thought you would've... um..."

    pause 1.0

    show yellow scaredbrow heavyblush frownmouth with dis

    show concerthallbackstage with vpunch

    yellow scaredbrow heavyblush frownmouth @worriedmouth "Please be my partner! In the contest! As coordinators!"

    menu:
        "Nah.":
            $ AddEvent("Yellow", "RejectPartner")
            yellow @talking2mouth "Oh. Okay."

            pause 1.0

            yellow @happy "Well... I'm glad I asked, at least."
            yellow @challengingmouth happybrow "I'll see you on the stage."

            red @happy "Same to you."

        "Sure.":
            $ AddEvent("Yellow", "AcceptPartner")
            yellow @talking2mouth "Oh. Okay."

            pause 0.5

            yellow blush -scaredbrow -frownmouth @talking2mouth "I was expecting that to be a much harder sell."

            red @happy "Not everything has to be a federal issue."
            red @talkingmouth "Now, c'mon. I think I hear Lisia announcing something. Let's pay attention."

label mdtryoutsbegin:
$ renpy.music.play("Audio/Music/contestintro.ogg", channel='music', loop=True, fadein=1.5, tight=None, if_changed=True)
show screen songsplash("Pokémon Contest! (Hoenn) Remastered", "Zame")
$ AddEvent("Professor Oak", "ParticipateMDTryouts")

scene concerthallstagenight
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
with splitfade

python:
    if (HasEvent("Yellow", "AcceptPartner")):
        coordinatorpartner = "Yellow"
    elif (HasEvent("Yellow", "RejectPartner")):
        coordinatorpartner = None
    else:
        AddEvent("Klara", "AgreePartner")
        coordinatorpartner = "Klara"

if (coordinatorpartner != None):
    narrator "You and [coordinatorpartner] listen from backstage as the judges are introduced."

else:
    narrator "You listen from backstage as the judges are introduced."

show lisia behind beam1 with Dissolve(1.0) 

lisia @happy "Ladies and gentlemen, please say hi to our three celebrity guests! All coordinators of incredible skill and fame, these judges are responsible for putting coordinating where it is nowadays!"

show lisia:
    xpos 0.5 
    ease 0.5 xpos 0.66

show fantina behind lisia:
    xpos 1.2
    ease 0.5 xpos 0.25

lisia @happy "First up, Fantina Morand! This coordinator from Kalos is a member of the Sinnoh League, and Kalos Queen, having collected all three Princess Keys required to win the Master Rank Pokémon Showcase!"

$ PlaySound("crowd_cheer.ogg")

show fantina happy with dis

fantina @happy2 "{i}Bonjour, bonjour!{/i} It is the greatest pleasure to be here!"

show lisia:
    xpos 0.66 
    ease 0.5 xpos 0.75

show wallace behind lisia:
    xpos 1.2
    ease 0.5 xpos 0.5

lisia @happy "The Head Judge is Champion Wallace Waters! You know him, you love him--he was World Contest Champion, and Battle Champion of Hoenn, too! Is he the most powerful Coordinator ever? I'd say so, and I should know--he's my uncle!"

if (GetRelationshipRank("Flannery") > 0):
    flannery @surprised "Wait, {i}that's{/i} Walmart?!"

$ PlaySound("crowd_cheer.ogg")

wallace @talkingmouth "Please, please, hold your applause. It's not for me, tonight. Let's instead point the spotlight at all these fine new potential coordinators, no?"

show lisia:
    xpos 0.75 
    ease 0.5 xpos 0.85

show phobos happybrow behind lisia:
    xpos 1.2
    ease 0.5 xpos 0.75

lisia @talking2mouth "Finally, it's Baron Lawrence Phobos The Third!" 

lisia @talkingmouth "He's[ellipses]{nw}" 

show wallace surprisedbrow frownmouth
show fantina surprisedbrow frownmouth 
show phobos surprisedbrow frownmouth
with dis

pause 1.0

extend @happybrow talkingmouth " a coordinator!"

pause 1.0

show wallace angrybrow -frownmouth 
show fantina happybrow -frownmouth
show phobos angry
with dis

pause 1.0

show lisia:
    xpos 0.85
    ease 0.5 xpos 0.5

show fantina behind lisia:
    xpos 0.25
    ease 0.5 xpos 0.1

show wallace behind fantina:
    xpos 0.5
    ease 0.5 xpos 0.3

show phobos behind lisia:
    xpos 0.75
    ease 0.5 xpos 0.8

lisia @happy "These three judges will be watching the tryouts. There's a lot of you here, so we'll bring you up to perform in groups of five."
lisia @angrybrow talkingmouth "And I'll be watching each and every one of you, announcing for you, and cheering you on, even if you've never coordinated before!"

wallace @surprisedbrow frownmouth "Hm."
wallace @happybrow talkingmouth "Why, my darling niece seems rather fired-up. I wonder what happened?"

lisia @happy "Uncle! Why don't you tell the audience about what you're going to give to the coordinator who impressed you the most?"

wallace surprisedbrow frownmouth @talking2mouth "A speech? Oh, dear Lisia, you really mustn't put me on the spot like this. I'm so {i}terribly{/i} unprepared."

lisia @happy "Here, take my microphone."

wallace -surprisedbrow -frownmouth @closedbrow talkingmouth "{size=30}No need, I brought my own.{/size}"
wallace @angrybrow talkingmouth "Ladies and gentlemen, distinguished guests, and those of you lucky enough to partake in this most-revered contest!"
wallace @closedbrow talking2mouth "Every time one steps on the coordinator's stage, there is much at stake. Triumph. Glory. Pride!"
wallace @happy "Allow me to manifest these in physical form! The coordinator who stands out most to me--"
wallace @happy "That is, to {i}we{/i}--will receive a prize of unparalleled significance and generosity."
wallace @talkingmouth "An egg, begat by my own Milotic, who has excelled in countless contests worldwide--and besides that, successfully defended the Hoenn Battle Champion's throne a great many times!"
wallace @happybrow talkingmouth "Can you imagine a greater pedigree? I, certainly, cannot! Take this top prize as proof of a Champion's belief in you, darlings!"

$ PlaySound("crowd_cheer.ogg")

lisia @talkingmouth "That's my uncle for you! Good luck to everyone trying to claim that Feebas! (And in case you cannot or do not want to receive it, we'll make a sizable donation to a charity of your choice.)"
lisia @angrybrow talkingmouth "Alright--that's enough preamble! Let's get this show going---I expect to see amazing performances for our judges!"
lisia happy "Group one--please come to the stage! And let's ring in the beginning of the Millennium Drop Water Festival Contest Tryouts!"

python:
    protaggroup = CoordinatorGroup([
        Coordinator(first_name, condition=coordinatingknowledge, isprotag=True, contestsprite="")
    ])

    if (coordinatorpartner == "Yellow"):
        protaggroup.Coordinators.append(Coordinator("Yellow", condition=75, partner=GetTrainerTeam("Yellow", "Rattata"), contestsprite=""))
    elif (coordinatorpartner == "Klara"):
        protaggroup.Coordinators.append(Coordinator("Klara", condition=13, partner=GetTrainerTeam("Klara", "Slowpoke"), contestsprite="makeup hairpin neutralcoat"))

    coordinators = [
        protaggroup,
        CoordinatorGroup([
            Coordinator("Hiker", condition=25, partner=Pokemon("Geodude"), contestsprite="")
        ]),
        CoordinatorGroup([
            Coordinator("Hex Maniac", condition=200, partner=Pokemon("Gastly"), contestsprite="")
        ]),
        CoordinatorGroup([
            Coordinator("Old Man", condition=125, partner=Pokemon("Beedrill"), contestsprite="")
        ]),
        CoordinatorGroup([
            Coordinator("Roughneck", condition=50, partner=Pokemon("Scraggy"), contestsprite="")
        ])       
    ]

    judges = [
        Judge(fantina, biases={ ContestMoveType.Cute : 50, ContestMoveType.Beautiful : 40, ContestMoveType.Cool : 20, ContestMoveType.Clever : 30, ContestMoveType.Tough : 10 }, customsex=Genders.Female),
        Judge(wallace, biases={ ContestMoveType.Cute : 30, ContestMoveType.Beautiful : 50, ContestMoveType.Cool : 40, ContestMoveType.Clever : 20, ContestMoveType.Tough : 10 }, customsex=Genders.Male),
        Judge(phobos, biases={ ContestMoveType.Cute : 30, ContestMoveType.Beautiful : 40, ContestMoveType.Cool : 20, ContestMoveType.Clever : 50, ContestMoveType.Tough : 10 }, customsex=Genders.Male)
    ]

    contestconditions = {
        "Types" : ["Water", "Flying", "Ghost"],
        "Region" : range(252, 387),#Hoenn
        "Traits" : [ContestMoveType.Beautiful, ContestMoveType.Cute]
    }

call Contest("Millennium Drop Water Festival Contest Tryouts", coordinators, judges, contestconditions) from _call_Contest_2

scene blank with transeye

scene concerthallstagenight
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
with transeye2

show lisia behind beam1 with dis

$ winner = contesthistory["Millennium Drop Water Festival Contest Tryouts"][0]
$ winnername = winner.GetName()
if (winner.IsProtag()):
    $ AddEvent("Professor Oak", "WonMDTryouts")
lisia @happy "A brilliant start to the night, everyone! [winnername] ['is the winner!' if 'and' not in winnername else 'are the winners!']"
lisia @talkingmouth "So [GetHePronoun(winner.GetSex())]'ll be moving onto the consideration rounds for the Millennium Drop Water Festival Contest."
lisia @sadbrow talkingmouth "I'm really sorry to everyone else, but we can't bring {i}everyone{/i} into the next round. But don't be discouraged! You did really well, each and every one of you!"

$ coordinatingknowledge += 30
narrator "For performing in a contest for the first time... your [contestcolor]Coordinating Knowledge{/color} went up by thirty points!"

scene blank2 with splitfade

narrator "You watch the rest of the performances, but eventually leave to go to bed, when it starts getting extremely late."
narrator "There are still twenty groups to go through by the time you finally call it for the night[ellipses]"

jump day010603