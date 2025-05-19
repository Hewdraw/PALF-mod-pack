label secondhomeroom010407:

$ timeOfDay = "Evening"

$ renpy.music.queue("Audio/Music/Oak Class.ogg", channel='music', loop=True, fadein=1.0, tight=None)

scene blank2

show homeroom behind blank2

$ renpy.transition(dissolve)
show screen currentdate

hide blank2 with dis

show oak with dis

narrator "You sprint to your homeroom, managing to corner Professor Oak before class begins."

red uniform @angrybrow talkingmouth "Sam! We need to talk."

oak @talkingmouth "That we do, [first_name]. But now is neither the time, nor place, for that."

red @sad "...But why, Sam? Have I done something wrong?"

oak @happyeyes happyeyebrows talkingmouth "You, of all people, should know that if I believe someone is doing something wrong, I tell them."
oak @talkingmouth "No, lad, you've done nothing wrong." 
oak @closedeyes talkingmouth "I simply need time to collect my thoughts. Given the importance of the conversation we're to have, it wouldn't do to tell you anything... incorrect."

hide oak 
show oakbg 
with dis

redmind @closedbrow frownmouth sweat "That's Sam for you. A brilliant, brilliant man, but nothing short of a miracle can get him to move on anyone else's schedule..."

show blank2
hide oakbg 
with dis

pause 2.0

$ PlaySound("BellChime.ogg")
$ renpy.pause(1.5, hard=True)

$ renpy.music.play("Audio/Music/Beyond2.ogg", channel='music', loop=True, fadein=1.0)

$ renpy.pause(2.0, hard=True)

hide blank2 with splitfade

$ renpy.transition(dissolve)
show screen currentdate

$ renpy.pause(1.5, hard=True)

$ PlaySound("vibrate.ogg", instant=True)
$ renpy.pause(0.5, hard=True)

redmind @thonk "Hmm?"

show phone_B
show phone_A
with fadeinbottom

show phone_C behind phone_A with dis

show phone_msg1 behind phone_A with dis

$ roommate_msg = Text("Calem",size=30,font="fonts/consola_0.ttf",color="#313131")

image calem_msg = Text("There's something I need to take care of\nback at Relic Hall before I can go. B&E are\nwith. You go ahead, I'll see you in a bit.",size=21,color="#ffffff",line_spacing=5,text_align=0.0)

show text roommate_msg behind phone_A:
    alpha 0.0 xalign 0.51 yalign 0.34
    ease 0.25 alpha 1.0

show calem_msg behind phone_A:
    alpha 0.0 xpos .41 ypos .4
    ease 0.25 alpha 1.0

pause 5.0

redmind "B&E? ...Oh, Brendan and Ethan. Well, I guess that can't be helped.{w=0.5} I'll check the place out myself then."

hide phone_A
hide phone_B
hide phone_C
hide phone_msg1
hide text roommate_msg
hide calem_msg 
with fadeoutbottom
    
$ renpy.transition(dissolve)
call clearscreens from _call_clearscreens_28
stop music fadeout 1.5

window hide

show blank2 with splitfade
$ renpy.pause(1.5, hard=True)
show stadium_empty behind blank2

play music "Audio/Music/League_Start.ogg" noloop
queue music "Audio/Music/League_Loop.ogg"

$ renpy.transition(dissolve)
show screen currentdate
hide blank2 with splitfade

$ renpy.pause(0.5, hard=True)

############################################################################################################################################################################################################################
#### JANINE INTRO ##########################################################################################################################################################################################################
############################################################################################################################################################################################################################

scene stadium_empty

redmind uniform "Man, just when I thought I was getting used to this school's extravagance..."
redmind "I get that our Battle Team's supposed to be super successful and all, but exactly how much money did the school pour into this stadium?{w=0.5} This place is huge!"

blue uniform angry "{gradualsize=18-38}--telling you to get out of my way!{/gradualsize}"

redmind @unamusedbrow unamusedmouth "Oh, great. [blue_name].{w=0.5} What's he trying to start now?"

show blue with dis:
    xpos 0.66 xzoom -1

show janine with dis:
    xpos 0.33

janine @talking2mouth"And I'm telling you we're not open for new memberships yet!{w=0.5} All that hair must be weighing down on that puny brain of yours!"

red @talkingmouth "Uh, hi. Is this where the Battle Team meets?"
    
janine @angrybrow talking2mouth "Another one?"
janine @closedbrow talking2mouth "Look, if you have any complaints about our selection process, I don't want to hear them."

red @talkingmouth "Me? No, I'm not trying to join. I mean, right now, anyway.{w=0.5} Is that what [blue_name]'s trying to do?"

janine @closedbrow talking2mouth "Yes. Do you know him?{w=0.7}{nw}"
extend @angrybrow talkingmouth " Please tell him that the only thing he's going to get in by harassing me is my 'absolutely not' list!"

red @happy "Did you hear that, [blue_name]? She said--"

blue @angry "Shut up and let me in!{w=0.5} Do you have any idea what I can do?"

janine @talking2mouth "I know you're annoying as hell."
janine angry "This conversation is over."

$ renpy.music.stop(channel="crowd")

show blank2
call clearscreens from _call_clearscreens_29
$ PlaySound("Metal Door Slam.ogg")

stop music fadeout 2.0

hide janine
hide blue
hide stadium_empty

$ renpy.pause(2.0, hard=True)

show map behind blank2
show map_corner behind blank2:
    xalign 0.0 yalign 1.0
    
$ renpy.transition(dissolve)
show screen currentdate

show blank2:
    alpha 1.0
    ease 2.0 alpha 0.0
    
play music "Audio/Music/Beyond2.ogg" loop fadein 2.0
$ renpy.pause(2.5, hard=True)

hide blank2

blue uniform angry "Psh! She thinks she's so high and mighty just because she's the daughter of an Elite Four member."
blue @talkingmouth "So, what are you doing here?{w=0.5}{nw}"
extend @angrybrow talkingmouth " Wait, let me guess. You're trying to join the Battle Team, too, aren't you?"

red @talkingmouth "No, I was just gonna--"

if WonBattle("Blue1"):
    blue @angry "Don't even bother!{w=0.5} You must think you're a real hotshot now that you beat me in that practice match."
    blue @angry "Well, guess what? I wasn't even trying!{w=0.5} Yeah, you beat me with beginner Pokémon the school gave us, big whoop!"
    blue @angry "Just you wait! My Pokémon are gonna be the strongest in this school.{w=0.5} {i}Then{/i} we'll see who's the better Trainer!"

else:
    blue @talkingmouth "HA! You're even dumber than I thought!{w=0.5} You're a hundred years too early to even be {i}thinking{/i} about getting in!"
    blue @happy "I went easy on you in the practice match, and you couldn't even beat me!"
    blue @closedbrow talkingmouth "If you try to get in now, you'd be the laughingstock of the whole school.{w=0.5} You'd ruin our town's reputation!"

    redmind @confusedeyebrows frownmouth "What reputation?"

    blue @closedbrow talkingmouth "Wait, if they find out that we're both from Pallet Town, then they would.{w=0.25}.{w=0.25}.{w=0.5} and I..."
    
    pause 1.0
    
    blue "[ellipses]"
    
    pause 1.5
    
    show map:
        parallel:
            xalign 0.0
            ease 0.03 xpos -15
            ease 0.03 xpos 15
            ease 0.03 xpos 0
            repeat 3
        parallel:
            yalign 0.0
            ease 0.03 ypos -30
            ease 0.03 ypos 30
            ease 0.03 ypos 0
            repeat 3
    
    blue angry "Listen, [first_name]! You better get your shit together!{w=0.5} If you keep sucking ass like you do now, you're gonna ruin my reputation!"
    
    red @talkingmouth "I don't think you need to worry about that."
    
red @confused "...Anyway, what's the deal?{w=0.5} Don't tell me you actually expected them to let you join just like that."

blue @angry "What's that got to do with anything?{w=0.5} It's only natural for me to fight the toughest Trainers in this school."
blue @closedbrow talkingmouth "Whatever. It doesn't matter if they don't want a fight.{w=0.5} I'll see all their strats for myself in a few hours."
blue @closedbrow talkingmouth "I bet you had no idea, but the Captain of the Battle Team is hosting an exhibition match here tonight.{w=0.5} Everyone in school's gonna be showing up."

red @talking2mouth "That's a lot of hype for just an exhibition."

blue @angry "Are you dense or what?{w=0.5} This is {i}Kobukan Academy's Battle Team{/i} we're talking about."
blue @closedbrow talkingmouth "Tch, why are you even in this school?"
blue @angrybrow talkingmouth "Whatever, someone has to represent Pallet and it sure won't be you! Smell ya!"

pause 2.0

redmind "[blue_name]'s antics aside, that exhibition match sounds like it might make for an entertaining night.{w=0.5} It sure beats sitting around in my room."
redmind @thinking "Anyway, this door doesn't look like it's gonna open anytime soon."
redmind "I should let the guys know about the exhibition."

pause 1.0

show blue angry with vpunch

blue frownmouth @talkingmouth "Hey!"

red @unamusedbrow talking2mouth "Oh, joy. You came back."

blue angry "When I'm at that exhibition--don't try to find me or anything weird like that! I don't want my other friends to think I know you or anything!"

hide blue with dis

redmind @thonk "He's been... weirdly secretive recently. I guess we hadn't talked in a while back in Pallet, but, still, it was a tiny town. He was practically always within yelling distance, except for the odd trip to Viridian."
redmind @thonk "I know he's not actually hanging out with another friend or anything. So what's he {i}really{/i} doing?"

pause 1.0

redmind @sigh "Not my circus, not my Grookey."


stop music fadeout 1.0
$ renpy.transition(dissolve)
call clearscreens from _call_clearscreens_30
    
show blank2 with splitfadefast
$ renpy.pause(1.0, hard=True)

hide map
hide map_corner

############################################################################################################################################################################################################################
#### ROOMMATES' Pokémon ####################################################################################################################################################################################################
############################################################################################################################################################################################################################

queue music "Audio/Music/SoaringIllusions_Intro.ogg" noloop
queue music "Audio/Music/SoaringIllusions.ogg"

show lobby behind blank2

$ renpy.transition(dissolve)
show screen currentdate

hide blank2 with splitfade
$ renpy.pause(0.5, hard=True)

scene lobby

pause 1.0

show brendan at rightside with dis
show ethan at centerside with dis
show calem at leftside with dis

red uniform @talkingmouth "Oh, hey, guys! I was just looking for you."

calem @happy "[first_name]. Is that so? We were just about to try and find {i}you.{/i}"

red @happy "What kept you guys?"

brendan @happy "Let's show ya!"

brendan @talking2mouth "Ready, guys?"

ethan @talkingmouth "Three..."
calem @talkingmouth "Two..."
brendan @talking2mouth "One..."

play sound ["Audio/Pokemon/Ball sound.ogg", "audio/pokemon/cries/669.mp3", "audio/pokemon/cries/172.mp3"]
show pichu at pokeball, centerside:
    yalign 1.0 xanchor 0.5
show flabebe at pokeball, leftside:
    yalign 1.0 xanchor 0.5

pause 2.0

brendan @surprised "Oh! I thought we were going on 'go.'"
play sound ["Audio/Pokemon/Ball sound.ogg", "audio/pokemon/cries/285.mp3"]
show shroomish at pokeball, rightside:
    yalign 1.0 xanchor 0.5

red @happy "Hey there, little guys! These must be your Pokémon from home, then?"

calem @talkingmouth "That's right!"
ethan @sadbrow talking2mouth "It took ages for them to get through customs, and the shipping fees were ridiculous..."
calem @talking2mouth "At least we're not in Galar. We wouldn't be allowed to bring them here at all, were that the case."
brendan @closedbrow talking2mouth "I think the little guy missed me. When I let him out at the Pokécenter, he let his spores out everywhere!"
brendan @surprised "Got in a little trouble for that..."
calem @closedbrow talking2mouth "Yes, and my Flabébé is being... tsundere."

narrator "You notice Calem's Flabébé is very purposefully not paying any attention to him."

ethan @happy "Guess the little guys didn't like being left alone for a bit!"

calem @happy "Seems so, yes."

show flabebe:
    xpos 0.25
    ease 1.0 xpos -0.5

show shroomish:
    xpos 0.75
    ease 1.0 xpos 1.5

show brendan surprisedbrow frownmouth
show calem surprisedbrow frownmouth
with dis

brendan @talking2mouth "Shroomish, where are you going? Wait for me!"
calem @talkingmouth "Flabébé? Please, not now! I'll give you lots of attention!"

show brendan:
    xpos 0.75
    ease 1.0 xpos 1.5

show calem:
    xpos 0.25
    ease 1.0 xpos -0.5

pause 2.0

ethan "{w=0.5}.{w=0.5}.{w=0.5}."
ethan @talkingmouth "Well, Pichu? You wanna run off as well?"

$ PlaySound("pokemon/cries/172.mp3")

Character("Pichu") "\"Pi-chu!\""

narrator "The Spiky-Eared Pichu tightly hugs Ethan's leg, clearly not intending to leave. It doesn't seem scared; it just seems overly affectionate."

ethan @happy "What a cutie."

pause 1.0

ethan @talkingmouth "Oh, yeah, [first_name], you wanted to talk with us, right? What about?"

red @happy "There's an exhibition match at the Battle Hall! Sounds like the Battle Team's captain is going to show off for us. Thought you guys might want to come!"

ethan @happy "Oh, yeah? That sounds great! Hey, you should run back to the room, and get [pika_name]. Then we can have all our Pokémon from home watch the game together!"

red @talkingmouth "Good idea! Though... Brendan and Calem's Pokémon might..."

ethan @closedbrow talking2mouth "Yeah... still no luck figuring out what's up with us. Or our Pokémon, I guess. I've tried to ask Professor Cherry a few times, but I haven't learned anything."

red @sigh "Same here. I think Professor Oak is going to tell me something soon, though."

ethan @happy "Well, let's just cross our fingers on that front."

red @happy "Yeah. I'm going to run back to the room now. See you in a bit?"

ethan @talkingmouth "See ya."

hide ethan
hide pichu 
with dis

redmind "I wonder how [pika_name] will like watching competitive Pokémon battles?{w=0.5} Since he's going to be a Champion's Pokémon someday, we'd better get used to them. [starter_name], too."

hide flabebe
hide brendan
hide shroomish
hide calem
hide blue
hide janine

show blank2 with dis

stop music fadeout 1.5

$ renpy.transition(dissolve)
call clearscreens from _call_clearscreens_31

$ renpy.pause(3.0, hard=True)
    
show evening at vspaz
$ timeOfDay = "Evening"
    
pause 3.5

hide lobby

$ playerparty.append(Pokemon(25, level=7, nickname=pika_name, ivs=[3, 2, 5, 6, 3, 4], nature=Natures.Lax, gender=Genders.Male, ability="Freelectric"))

show blank as firstblank behind blank2
show stadium_full behind blank2
show blank as secondblank behind blank2
$ renpy.music.play("Audio/Stadium_crowd.ogg", channel='crowd', loop=True, fadein=1.5)
$ renpy.music.play("Audio/Stadium_chant.ogg", channel='crowd2', loop=True, fadein=1.5)

$ renpy.pause(0.75, hard=True)

$ renpy.music.queue("Audio/Music/Indigo_Start.ogg", channel='music', loop=None, fadein=1.0, tight=None)
$ renpy.music.queue("Audio/Music/Indigo_Loop.ogg", channel='music', loop=True, tight=None)

$ renpy.pause(1.0, hard=True)

hide blank2 with transball
$ renpy.pause(0.25, hard=True)
show blank as secondblank:
    alpha 1.0
    ease 0.5 alpha 0.0

show stadium_full:
    subpixel True
    zoom 3.0 alpha 0.65 xalign 0.15 ypos 2600
    ease 1.25 alpha 1.0 xalign 0.0 ypos 3000
    xalign 0.85 alpha 0.65 ypos 2600
    ease 1.25 alpha 1.0 xalign 1.0 ypos 3000
    xalign 0.5 alpha 0.4 ypos 2400
    ease 1.0 alpha 1.0 zoom 1.0 ypos 1080

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
        
pause 3.5

hide blank as firstblank
hide evening
hide blank

$ renpy.transition(dissolve)
show screen currentdate

show stadium_full:
    alpha 1.0 zoom 1.0 yalign 1.0 xalign 0.5

redmind -uniform @surprisedbrow frownmouth "Wow, the whole school is here.{w=0.5} I guess it's a good thing we showed up early after all."

$ renpy.music.stop(channel='crowd2', fadeout=7.0)

show brendan at rightside with dis

brendan @surprised "Yeah, I knew it was gonna be crazy, but this is ridiculous."

show calem at leftside with dis

calem @talking2mouth "Seems some people are still trying to get in. I do hope no-one gets crushed."

show ethan at centerside with dis

ethan @sadbrow talkingmouth "It's orientation week all over again.{w=0.5} I still can't get used to big crowds like this."

brendan @talking2mouth "Oh yeah, you're from New Bark Town.{w=0.5} Isn't the population there under 1,000 or somethin'?"

ethan @happy "Something like that."

if (classstats["Ground"] == 0):
    brendan @happybrow talkingmouth "I brought some Lava Cookies, by the way.{w=0.5} Sorry if you're not a fan of sweet things, I'm not big on them either, but they're a Hoenn specialty!"
    
else:
    brendan @happybrow talkingmouth "I brought some Lava Cookies, by the way.{w=0.5} Not sure if you had any from Bertha's class, but they're a Hoenn specialty and May's {i}all{/i} over these."

show lavacookie at itemhover

$ PlaySound("item_get.ogg")

pause 1.0

show lavacookie at itemhide
$ renpy.pause(1.5, hard=True)

hide lavacookie

calem @happybrow talkingmouth "I imagine you brought enough to share with the group, yes?"

brendan @happy "Of course! And some for our Pokémon, too. Even brought enough to share with Hilbert, if he shows up!"

ethan @talking2mouth "It'd be weird, I think, if he didn't. No way he'd miss such a high-profile battling thing, right?"

calem @closedbrow talking2mouth "His presence is no guarantee we'll see him, though."

$ renpy.music.play("Audio/Pokemon/pikachu_pikapika1.ogg", channel="altcry", loop=None)

pikachu happy_3 "Pika-pika!"

ethan @surprised "Oh, hey, [pika_name]! You hungry, too?"

$ renpy.music.stop(channel='crowd', fadeout=2.0)
$ renpy.music.stop(channel='crowd2', fadeout=2.0)
$ renpy.music.play("Audio/Stadium_murmur.ogg", channel='crowd3', loop=True, fadein=1.5)
stop music fadeout 1.0

pause 1.0

$ renpy.music.play("Audio/Pokemon/pikachu_confused.ogg", channel="altcry", loop=None)
pikachu neutral_4 "Pika?"

red @confusedeyebrows talking2mouth "Is it me or did everyone get really quiet?"

brendan surprisedbrow frownmouth @surprised "Yo, look over there, [first_name]!"

hide brendan at rightside with dis
hide calem at leftside with dis
hide ethan at centerside with dis
    
$ renpy.music.queue("Audio/Music/DragonDenStart_B.ogg", channel='music', loop=None, tight=None)
$ renpy.music.queue("Audio/Music/DragonDenLoop.ogg", channel='music', loop=True, tight=None)

$ PlaySound("crowd_cheer.ogg")

$ renpy.music.stop(channel='crowd3', fadeout=2.0)
$ renpy.music.play("Audio/Stadium_crowd.ogg", channel='crowd', loop=True, fadein=1.5)

show lance with dis:
    xpos 200
    ease 1.0 xpos 500

pause 1.5

hide calem
hide brendan
hide ethan

calem @closedbrow talkingmouth "Hm.{w=0.5} Lance.{w=0.5} It makes sense that he'd be here."
brendan @surprisedbrow talking2mouth "Yeah. I mean, he {i}is{/i} the manager of the Battle Team."

hide lance with dis
show brendan at rightside
show calem at leftside
show ethan at centerside 
with dis

ethan @closedbrow talking2mouth "It's freakin' crazy to me that a National Champion has the time to manage a random school's Battle Team."
calem @angrybrow talkingmouth "That would be crazy, but this is {i}Kobukan Academy.{/i} Our Battle Team is basically a Champion assembly line."
brendan @happy "Hilbert told me he actually won two National Championships! Becomin' a National Champion twice is pretty unheard of."
red @talking2mouth "Yeah... I'm fuzzy on the details, but I think that's why the Kantonian and Johtonian leagues merged into the Indigo League, like, three years ago."
ethan @sad "It's impressive, but I heard what he really wants is to be world Champion."
calem @sad "Yes... I heard he hasn't had any luck there. But, really, how was he supposed to beat Leon and Cynthia?" 
calem @closedbrow talking2mouth "Besides the top four, the last world Championships was a slaughter."

red @happy "You look upset, Calem! Didn't Diantha place in the top four, higher than Lance?"

calem @happy "Oh, sure, sure. And that was a moment of national pride, for sure. But Lance is somewhat of a personal hero of mine." 
calem @closedbrow happymouth "Actually, I learned the language simply to talk to him some day."

brendan @happy "Dude! You could've had your chance in gym class!"

calem @sadbrow talkingmouth "Er... yes. And I'm still kicking myself that I missed that."

redmind "Wow. If this guy is so famous, I wonder why I've never heard [blue_name] crowing about him before?"
redmind "In any case, Lance sounds like the kind of guy that makes me wonder what I'm doing with my life..."

$ renpy.music.play("Audio/Pokemon/pikachu_excite5.ogg", channel="altcry", loop=None)

pikachu happy_3 "Pikachu~!"

narrator "[pika_name] begins stuffing his cheeks with Brendan's snacks."

show brendan surprisedbrow frownmouth
show ethan surprisedbrow frownmouth
show calem surprisedbrow frownmouth
with dis

show lance:
    alpha 0.0 zoom 1.25 xpos 0 ypos 1270
    pause 1.5
    parallel:
        ease 1.5 zoom 1.0 ypos 1080 xpos 250
    parallel:
        ease 0.5 alpha 1.0

red @talkingmouth "Whoa, slow down, [pika_name]!{w=0.5} You're gonna leave crumbs all over my clothes."

show lance:
    ease 0.75 alpha 1.0 zoom 1.0 ypos 1080 xpos 250
    
show brendan:
    xpos 0.75
    ease 0.5 xpos 0.85
show ethan:
    xpos 0.5
    ease 0.5 xpos 0.75
show calem:
    xpos 0.25
    ease 0.5 xpos 0.65

lance  @talking2mouth "You there."

$ renpy.music.stop(channel='crowd', fadeout=1.0)

show lance:
    zoom 1.0 xpos 250 alpha 1.0
    
red @talkingmouth "Huh?"

$ renpy.music.play("Audio/Pokemon/pikachu_question.ogg", channel="altcry", loop=None)
pikachu neutral_4 "Pika?"

show brendan:
    xpos 0.85
    ease 0.5 xpos 0.95
show ethan:
    xpos 0.75
    ease 0.5 xpos 0.85
show calem:
    xpos 0.65
    ease 0.5 xpos 0.75

redmind @wince frownmouth "...I can feel everyone's eyes on me.{w=0.5} What did I do?"
red @confusedeyebrows talkingmouth "Uh... can I help you? Mr. Lance? Sir?"

lance @talking2mouth "Unacceptable."
lance @sadbrow talking2mouth "Feeding your Pokémon this...{w=0.5}{nw}"
extend @angrybrow talkingmouth " this {i}swill.{/i}"

lance @sadbrow talking2mouth "Do you not have the vaguest idea of the dietary needs of a Pokémon?"

red @talking2mouth confusedeyebrows "I[ellipses] thought I did?"

redmind @angrybrow frownmouth "Guys, what the hell! We were all doing it! Help me out!"

show brendan thinking with dis:
    xpos 0.95
    pause 1.5
    ease 0.2 xpos 1.5

show ethan thinking with dis:
    xpos 0.85
    pause 1.5
    ease 0.2 xpos 1.5

show calem thinking with dis:
    xpos 0.75
    pause 1.5
    ease 0.2 xpos 1.5

$ renpy.pause(3.0, hard=True)

redmind @angrybrow frownmouth "[ellipses]Assholes."

show lance angry with dis:
    zoom 1.0 xpos 250/1920.0 ypos 1080
    ease 0.5 xpos 450/1920.0 zoom 1.25 ypos 1270
    pause 1.25
    ease 0.5 xpos 0.5 zoom 1.0 ypos 1080
    
show lavacookie:
    alpha 0.0 xpos 700 ypos 300 zoom 0.75 rotate 0
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
            
narrator "{color=#e70000}Lance snatches the Lava Cookies away from [pika_name].{/color}"

$ renpy.music.play("Audio/Pokemon/pikachu_confused2.ogg", channel="altcry", loop=None)
pikachu surprisedbrow frownmouth @surprised "Pika?!"

show lance -angry with dis:
    xpos 0.5 zoom 1.0
    
lance @talking2mouth "Junk food like that will only serve to rot their body and mind.{w=0.5} If your Pokémon want snacks, feed them Poké Beans or berries."

pause 1.0

$ renpy.music.set_volume(0.25, delay=0.5, channel="music")

redmind @thinking "...I need to say something. But..."
redmind @sad "I can't. If only my friends had stayed here... but, in front of the eyes of the entire school, and with Lance being a National Champion..."
redmind @sad "I can't."

$ renpy.music.set_volume(1.0, delay=2.0, channel="music")

red talking2mouth angryeyes angryeyebrows "Understood.{w=0.5} Sir.{w=0.5} I'll be sure to remember that."

show lance sadbrow with dis

$ renpy.music.play("Audio/Pokemon/pikachu_angry3.ogg", channel="altcry", loop=None)
pikachu angry_3b "Pi-pika...!"

lance @talking2mouth "Hold on."

show lance -sadbrow with dis:
    xpos 0.5
    ease 0.6 xpos 0.6
    
red talking2mouth angryeyes angryeyebrows "What?"

lance @talking2mouth "This Pikachu.{w=0.5} Do you plan on including it in your academy evaluations?"

red @talkingmouth "Yeah, of course. He's my partner.{w=0.5} If there's anyone I can count on, it's{nw}"

show lance closedbrow with dis:
    xpos 0.6
    ease 0.6 xpos 0.5

lance @talking2mouth "Remove him at once."

red surprisedbrow talking2mouth @noshine "What?"

lance @talking2mouth "Your Pikachu is inadequate.{w=0.5} Using such a weak Pokémon will get you nowhere in this academy."
lance @talking2mouth "If, for example, a student applied to the Battle Team with this Pokémon on their team..."
lance @angrybrow talking2mouth "I would disqualify them at once, regardless of their battle skills."

$ renpy.music.play("Audio/Stadium_murmur.ogg", channel='crowd3', loop=True, fadein=1.0)

pause 1.5

lance -closedbrow @talking2mouth "Even though you're allowed six, a single Pokémon like that will only serve to be a crippling liability to your party."
lance @talking2mouth "Its nature is suboptimal, its genealogy is clearly lacking... you could throw a stone anywhere in Viridian Forest and hit a superior alternative."

redmind @sad "Wh-what...? C'mon... Brendan, Ethan, Calem... Someone, speak up for us... someone?"

pause 2.0

redmind @surprised "Wait... I hear running. Is someone--{nw}"

show silver:
    xpos -0.5
    ease 0.2 xpos 0.25

show lance angry with dis:
    xpos 0.5
    ease 0.5 xpos 0.75

silver angry "You don't know what the hell you're talking about, you bastard!"

red @surprised "S-Silver?!"

silver @talkingmouth "You think because you're a Champion, you know what makes a Pokémon good or bad? You think you can tell the worth of a Pokémon at a glance?!"

silver @angrybrow talkingmouth "Well, I'm from Johto, and let me tell you, every Johtonian knows you're carried by those three Dragonite on your belt. Fuckin' amazing team-building skills there."
silver @talkingmouth "You know what your problem is?! Because you can't get your dick hard unless you're a World Champ, and you failed at that, you're looking for someone else to blame."
silver @angrybrow talkingmouth "Newsflash, washout. It's not your Pokémon's fault. {i}No{/i} Pokémon is a liability. {i}No{/i} Pokémon is inadequate."
silver @sadbrow talkingmouth "Instructor Karen says that only selfish trainers call Pokémon 'strong' or 'weak.' But you aren't selfish. You're just a coward who can't admit your failure is {i}your{/i} fault."
silver @talkingmouth "I knew another guy who couldn't accept his own failure. And he took a trip down Tohjo falls. The fast way."

pause 2.0

redmind @surprised "H-holy shit. No matter what Lance says to me now... or said to me before... {i}I'm{/i} not going to be the one people remember here."

silver @talkingmouth "And you! [first_name]!"

red @surprised "H-huh?!"

silver -angry @closedbrow talkingmouth "You should stand up for your Pokémon."

red @talking2mouth "Er... r-right..."

pause 2.0

lance -angry @talking2mouth "Silver, was it?{w=1.0} Please, tell me. What do you think is the appropriate punishment for this flagrant display of disrespect?"

show silver -angry with dis

pause 2.0

silver @closedbrow talkingmouth "Expel me. Wouldn't be the first school I've been kicked out of."

lance closedbrow @talking2mouth "As a part-time employee of this school, I cannot do that."

pause 1.0

lance @talking2mouth "So hear this, instead." 
lance -closedbrow @talking2mouth "Regardless of your skills.{w=0.5} Regardless of the Pokémon you have on-hand.{w=0.5} Regardless of how much you {i}deserve{/i} it."
lance @angrybrow talking2mouth "You two will {i}not{/i} join the Battle Team."

silver surprisedbrow @surprised "W-wait. [first_name], too? I was the one who--{nw}"

lance @closedbrow talking2mouth "I have said it;{w=1.0} It is so."

red @angrybrow frownmouth "[ellipses]"

show silver sadbrow with dis

redmind angrybrow neutralmouth "I know I should just walk away and keep my mouth shut, but I can't just let that slide."
redmind "I don't care if this guy's a two-time national Champion or whatever.{w=0.5} I won't let him walk all over me, Silver, and [pika_name] when he doesn't know a thing about us."

red @talking2mouth "With all due respect, Sir, there's just no way that's going to happen."

$ renpy.music.play("Audio/Stadium_crowd.ogg", channel='crowd', loop=True, fadein=1.0)

pause 1.5

show lance angrybrow
show silver -sadbrow 
with dis

pause 1.5

lance @talking2mouth "Is that right?"

red @talking2mouth "[pika_name] and I've been best friends since we were kids.{w=0.5} I know we're not the most experienced when it comes to battling and training, but we don't do anything without each other."
red @talking2mouth "For better or worse, we're seeing this through to the end, together. And we're getting on that Battle Team. We're going to be so good that you can't ignore us."

red @closedbrow talking2mouth "Instructor Bruno said we needed the vote of the captain of the Battle Team. He didn't say anything about your vote."
red @angrybrow talking2mouth "So go ahead and 'advise' the team not to take us. Me, Silver, [pika_name]. We're getting in anyway. Because we're friends."

show lance sadbrow with dis

$ renpy.music.play("Audio/Pokemon/pikachu_excite3.ogg", channel="altcry", loop=None)
pikachu neutral_2b "Pika pika!"

lance @closedbrow talking2mouth "...Naive."
lance @angrybrow talking2mouth "The world doesn't work like that.{w=0.5} Say what you want about your Pokémon, 'friendship' will not help you any more than twiddling your thumbs."
lance @angrybrow talking2mouth "Get stronger Pokémon. And a sense of which fights you {i}cannot{/i} win. In this world, only the best of the best can survive.{w=0.5} The weak and foolish are purged."
    
red @thinking "[ellipses]"

lance @closedbrow talking2mouth "I'd take my advice if I were you. And as for you, Silver... learn to hold your tongue, else you're liable to lose it."
lance @talking2mouth "I take my leave of you."

hide lance with dis

$ renpy.music.stop(channel='crowd3', fadeout=2.0)

$ renpy.pause(2.0, hard=True)

hide lance

stop music fadeout 2.5

red @sad "Silver...?"

silver @angry "Don't."

$ PlaySound("fading_footsteps.ogg")
hide silver at leftside with dis

pause 1.5

show brendan sadbrow frownmouth at rightside
show ethan sadbrow frownmouth at centerside 
show calem sadbrow at leftside 
with dis

ethan @sadbrow talking2mouth "H-hey... [first_name].{w=0.5} Are you alright?"
    
brendan @sadbrow talking2mouth "That looked painful."

red @talking2mouth "...I'm fine. Silver took most of the heat."

show brendan thinking 
show ethan thinking
with dis

redmind "Yeah, they don't believe me.{w=0.5} I don't think I'm fine either."

calem @talking2mouth "I never could have imagined that that's the sort of man Lance was..."
ethan -thinking frownmouth @talking2mouth "They say 'never meet your heroes,' y'know."
brendan -thinking frownmouth @angry "What a dick!"

red @closedeyes talking2mouth "It's not a big deal. I'm just glad it didn't turn out to be anything..."

redmind @thinking "Still, Lance was right in a way.{w=0.5} I hate to admit it, but everyone else in this academy is way stronger than us in almost every sense."
redmind @thinking "But he doesn't know about me and [pika_name].{w=0.5} We'll show him what we can really do."

brendan @talking2mouth "But damn, I was really surprised when that red-haired kid said all that stuff to him.{w=0.5} That was incredible!"

show ethan sadbrow frownmouth
show brendan sadbrow frownmouth 
show calem sadbrow frownmouth
with dis

red @angrybrow talking2mouth "Yeah, well, someone had to stand up for [pika_name] and I."

brendan @talking2mouth "Oh yeah. H-heh.{w=0.5}{nw}"
extend @sad " Y'know, Lance is kind of a big deal, and if I said the wrong thing it might've made you look worse and--"

calem @sadbrow talking2mouth "I apologize. I failed in my first priority as your roommate--as your friend."
ethan @sadbrow talking2mouth "Yeah, me too. I just figured if I stepped in, then he'd start yelling at me... 'cause I'm kinda in the same boat as you..."

red @angrybrow frownmouth "{w=0.5}.{w=0.5}.{w=0.5}." 

show brendan -sadbrow -frownmouth
show calem -sadbrow -frownmouth
show ethan -sadbrow -frownmouth
with dis

red @closedeyes talking2mouth "I'm still mad, but I'll get over it. Let's go take our seats."

may @talkingmouth "Hey, Brendan, [first_name]!"
    
$ renpy.music.queue("Audio/Music/Indigo_Loop.ogg", channel='music', loop=None, fadein=3.0, tight=None)
    
show may at midrightside with dis

show leaf at midleftside with dis

may @talkingmouth "We were looking all over for you two!"

leaf @talking2mouth "Yeah, this place is so packed just getting here was like trying to navigate a maze."

window hide
pause 1.0

show leaf surprisedbrow frownmouth with dis

pause 1.0

show may surprisedbrow frownmouth 
show brendan surprisedbrow frownmouth
with dis

show leaf at getcloser, midleftside

leaf @talking2mouth "Who's this little guy?{w=0.5} Is he one of your Pokémon from home?"

show brendan happy
show may happy 
with dis

red happy "Yeah, this is [pika_name]."

show leaf -surprisedbrow -frownmouth -surprised 
show brendan -happy
show may -happy
with dis

may @talkingmouth "Aw! And is [pika_name] getting along well with your li'l Shroomy, Brendan?"
brendan @happy "Well, uh, they haven't actually met yet. Didn't think it was a good idea to let him out in here."
may @closedbrow talking2mouth "Oh, that's probably smart..."

$ renpy.music.play("Audio/Pokemon/pikachu_norm1.ogg", channel="altcry", loop=None)

pikachu neutral_2 "Pikachu!"

show leaf at getfurther, midleftside

may @happybrow talkingmouth "He's such a cutie!"

show may at getcloser, midrightside

pause 0.5

show brendan surprisedbrow frownmouth with dis
    
narrator "May lightly pets [pika_name]'s head."

may @happybrow talkingmouth "Aww, his fur's so soft!"
show may happy
show leaf happy
with dis

$ renpy.music.play("Audio/Pokemon/pikachu_happy1.ogg", channel="altcry", loop=None)

pikachu happy_2 "Chaaa~"

show may surprisedbrow frownmouth
show leaf surprisedbrow frownmouth
with dis

brendan surprisedbrow frownmouth @surprised "Hey, how come he's not shocking {i}her?{/i} What's up with that?!"

leaf @surprisedbrow talking2mouth "What?"

may @talkingmouth "Oh, is [pika_name] getting along with your [starter_species_name]?"

show brendan -surprisedbrow -frownmouth -surprised
show may -surprisedbrow -frownmouth -surprised
show leaf -surprisedbrow -frownmouth -surprised
with dis

red @talkingmouth "For the most part, yeah.{w=0.5} I don't think they know how to feel about each other yet."
red @talking2mouth "[pika_name]'s been my only Pokémon since I got him so I guess he's not used to me giving attention to another one."

show may at getfurther, midrightside
    
may @talkingmouth "That's understandable.{w=0.5} I'm sure once they've spent enough time together they'll get along great."
    
leaf @talking2mouth "How long have you and [pika_name] been together?"
    
red @closedbrow talking2mouth "Since I was 10 years old.{w=0.5} Sam gave me and [blue_name] a Pokémon each as a present."

may @surprised "'[blue_name]?' That spiky-haired weirdo in our homeroom?"

red @talkingmouth "Yeah, that's him. Anyway, we've been best friends ever since then.{w=0.5} [pika_name], not [blue_name].{w=0.5} [pika_name] and I do everything together."
red @happy "...Even if he tries to get out of our runs!"

leaf @talking2mouth "So, how come you haven't evolved him yet?"

$ renpy.music.play("Audio/Pokemon/pikachu_confused.ogg", channel="altcry", loop=None)

pikachu neutral_4 "Pika?"

red @closedeyes talking2mouth "Well... it's a bit embarrassing, but Raichu eat a lot more than Pikachu, and back home, we couldn't really afford that."
leaf @surprised "Really? Well, if you're in Kobukan, you must be able to afford that now, right?"
redmind @thinking "Eh... not really. I mean, I could feed him well enough with the free food that Kobukan provides, but I don't know how long it'll be before the school realizes I can't pay..."
redmind @happy "And what would I do with a Raichu then? I'd have to give him away! No chance of that!"
redmind @thinking "[ellipses]"
redmind @thinking "Although... what will I do with [starter_name] when I get kicked out?"

may @happy "I bet you'll be a perfect addition to the coordinator's club!{w=0.5} Pikachu are very popular in Pokémon contests."

$ renpy.music.play("Audio/Pokemon/pikachu_pikapika1.ogg", channel="altcry", loop=None)

pikachu happy_2 "Pika pika~!"
    
may @happybrow talkingmouth "See? Even [pika_name] thinks he'll be great."

leaf @happybrow talkingmouth "Well, it's fine as long as you're not using him for battling.{w=0.5} Pikachu are {i}way{/i} cuter than Raichu, anyway."
    
leaf @talkingmouth "Speaking of battling, are you guys excited to see Janine?"

red @talkingmouth "Who's Janine?"

leaf @surprisedbrow talking2mouth "You don't know?{w=0.5} She's the Battle Team captain two years running! Everyone thinks she'll be the next Kobukan Champion."

brendan @surprised "Wait? Battle Team captain two years runnin'? How does that work? This's a one year program."

calem @talkingmouth "It can be. Similarly to the Student Council, students can elect to stay onboard and train newcomers. She's just done that twice."

ethan @talkingmouth "I heard Janine's not going to leave until she finds someone better than her to captain the Battle Team."

red @surprised "How can she afford that?"

may @surprised "{i}I{/i} heard she's the daughter of one of the academy's teachers."

red @closedbrow talking2mouth "Oh, yeah, I think [blue_name] mentioned she was the daughter of an Elite Four member..."

calem @closedbrow talkingmouth "Seems there's very little Janine {i}doesn't{/i} have going for her."

leaf @closedbrow talkingmouth "She's a tough one, alright. {i}I{/i} heard she has magic ninja powers."

red @confused "Wait... magic ninja? Come to think of it, I {i}did{/i} see a strangely-dressed woman who..."

$ renpy.music.play("Audio/Stadium_chant.ogg", channel='crowd2', loop=True, fadein=0.5)

pause 1.5

show leaf surprisedbrow frownmouth
show may surprisedbrow frownmouth
show brendan surprisedbrow frownmouth
show calem surprisedbrow frownmouth
show ethan surprisedbrow frownmouth
with dis

brendan @talking2mouth "Hey, I think they're starting!"

hide leaf surprised at midleftside with dis
hide may surprised at midrightside with dis
hide brendan surprised at rightside with dis
hide calem surprised at leftside with dis
hide ethan surprised at centerside with dis

$ renpy.music.stop(channel='crowd2', fadeout=1.0)
$ renpy.pause(0.5, hard=True)

$ PlaySound("crowd_cheer.ogg")

$ renpy.pause(0.5, hard=True)

show janine uniform:
    alpha 0.0 xpos 300
    parallel:
        ease 0.5 alpha 1.0
    parallel:
        ease 1.0 xpos 720
        
$ renpy.pause(1.0, hard=True)

$ BecomeNamed("Janine")
redmind neutralbrow neutralmouth "That must be Janine, and, like I thought, that's the woman who kicked Blue out of the Battle Hall!"
redmind @angrybrow frownmouth "And, more importantly, that's the woman I need to convince to let me onto the Battle Team."

show janine thinking:
    alpha 1.0 xpos 720
    pause 0.5
    ease 1.0 alpha 0.0 xpos 670

show stadium_full:
    parallel:
        xalign 0.0
        ease 0.02 xpos -15
        ease 0.02 xpos 15
        ease 0.02 xpos 0
        repeat 6
    parallel:
        yalign 0.0
        ease 0.02 ypos -15
        ease 0.02 ypos 15
        ease 0.02 ypos 0
        repeat 6

Character("Announcer") "\"Welcome ladies and gentlemen, boys and girls, to this special exhibition match hosted by Kobukan Academy's Battle Team! How're you all feeling tonight?\""

show janine -thinking:
    alpha 0.0 xpos 670

$ PlaySound("crowd_cheer.ogg")

show stadium_full:
    pause 0.75
    parallel:
        xalign 0.0
        ease 0.02 xpos -15
        ease 0.02 xpos 15
        ease 0.02 xpos 0
        repeat 25
    parallel:
        yalign 0.0
        ease 0.02 ypos -15
        ease 0.02 ypos 15
        ease 0.02 ypos 0
        repeat 25

pause 1.5

$ renpy.music.play("Audio/Stadium_chant.ogg", channel='crowd2', loop=True, fadein=3.0)

show stadium_full:
    xalign 0.5 yalign 1.0

Character("Announcer") "\"Awesome! Let's get right to it then!\""
Character("Announcer") "\"Boy, do we have a treat for you all.{w=0.5} First up to grace the battlefield is none other than our Battle Team's very own captain, Janine!\""

$ PlaySound("crowd_cheer.ogg")

show janine with Dissolve(0.5):
    xpos 500
    parallel:
        ease 0.75 xpos 300

pause 1.0

$ renpy.music.play("Audio/Pokemon/Venomoth_Ball.ogg", channel="altcry", loop=None)

show venomoth at pokeball behind beam3:
    xanchor -1.0 alpha 0.0 xzoom 0.0 yzoom 0.0 yalign 1.0 ypos 1380 xpos 500
    block:
        parallel:
            ease 0.33 alpha 1.0 ypos 600 xpos 650
            ease 0.67 ypos 1080 xpos 700
        parallel:
            ease 0.5 xzoom -1 yzoom 1.0

$ renpy.pause(1.0, hard=True)

show venomoth:
    subpixel True
    alpha 1.0 ypos 1080 xpos 700
    block:
        parallel:
            ease 1.1 ypos 820
            ease 1.0 ypos 960
            ease 1.1 ypos 850
            ease 1.0 ypos 1000
            ease 1.1 ypos 825
            ease 1.0 ypos 980
            repeat
        parallel:
            ease 0.52 xpos 630
            ease 0.6 xpos 730
            ease 0.62 xpos 620
            ease 0.7 xpos 725
            ease 0.58 xpos 600
            ease 0.65 xpos 700
            repeat

show janine:
    alpha 1.0 xpos 300

Character("Announcer") "\"Janine is starting out strong with her signature Pokémon, Venomoth!{w=0.5} These two have dominated the Kobukan leaderboards since their arrival and they show no signs of stopping!"

pause 0.25

show janine thinking:
    alpha 1.0 xpos 300
    parallel:
        ease 0.75 alpha 0.0
    parallel:
        ease 1.0 xpos 100

show venomoth:
    subpixel True
    parallel:
        ease 2.0 xpos 0
    parallel:
        ease 0.5 ypos 1000
        ease 0.5 ypos 840
        ease 0.5 ypos 900
        ease 0.5 ypos 800

$ renpy.pause(2.0, hard=True)

show venomoth:
    subpixel True
    xpos 0 ypos 800 xzoom -1 yzoom 1.0
    block:
        parallel:
            ease 1.1 ypos 620
            ease 1.0 ypos 760
            ease 1.1 ypos 650
            ease 1.0 ypos 800
            ease 1.1 ypos 625
            ease 1.0 ypos 780
            repeat
        parallel:
            ease 0.52 xpos 80
            ease 0.6 xpos 30
            ease 0.62 xpos 120
            ease 0.7 xpos 25
            ease 0.58 xpos 100
            ease 0.65 xpos 0
            repeat
        parallel:
            ease 1.0 xzoom -0.5 yzoom 0.5


$renpy.music.play("audio/pokemon/ball sound.ogg", channel="altcry", loop=None)
$ renpy.music.queue("audio/pokemon/cries/419.mp3", channel="altcry", loop=None)

show floatzel at pokeball behind beam3:
    alpha 0.0 zoom 0.0 yalign 1.0 ypos 1000 xpos 1900
    block:
        parallel:
            ease 0.33 alpha 1.0 ypos 200 xpos 1500
            ease 0.67 ypos 850 xpos 1400
        parallel:
            ease 0.5 zoom 0.5

$ renpy.pause(1.0, hard=True)

show floatzel:
    alpha 1.0 zoom 0.5 xpos 1400 ypos 850
    parallel:
        ease 0.3 ypos 820
        ease 0.15 ypos 850
        repeat
    parallel:
        ease 0.3 xpos 1370
        ease 0.15 xpos 1340
        ease 0.3 xpos 1370
        ease 0.15 xpos 1400
        repeat

show venomoth:
    subpixel True
    xanchor -1.0 ypos 620 xpos 30
    block:
        parallel:
            ease 1.0 xanchor -1.5
        parallel:
            ease 1.1 ypos 620
            ease 1.0 ypos 760
            ease 1.1 ypos 650
            ease 1.0 ypos 800
            ease 1.1 ypos 625
            ease 1.0 ypos 780
            repeat
        parallel:
            ease 0.52 xpos 80
            ease 0.6 xpos 30
            ease 0.62 xpos 120
            ease 0.7 xpos 25
            ease 0.58 xpos 100
            ease 0.65 xpos 0
            repeat

Character("Announcer") "\"On the other side, her opponent sends out a Floatzel, a Pokémon well-known for its agility in the ring!{w=0.5} Can these two rise up to the challenge?"

hide janine

janine uniform @talking2mouth "He's going to need a lot more than just speed to match my Venomoth."

$ renpy.music.play("Audio/Pokemon/Venomoth.ogg", channel="altcry", loop=None)

show venomoth:
    subpixel True
    parallel:
        block:
            parallel:
                ease 1.0 ypos 450
            parallel:
                ease 0.05 xpos 20
                ease 0.05 xpos 40
                repeat 10
    parallel:
        pause 1.0
        block:
            parallel:
                ease 1.1 ypos 620
                ease 1.0 ypos 760
                ease 1.1 ypos 650
                ease 1.0 ypos 800
                ease 1.1 ypos 625
                ease 1.0 ypos 780
                repeat
            parallel:
                ease 0.52 xpos 80
                ease 0.6 xpos 30
                ease 0.62 xpos 120
                ease 0.7 xpos 25
                ease 0.58 xpos 100
                ease 0.65 xpos 0
                repeat

Character("Venomoth") "\"Vennn!\""

stop music fadeout 3.0

Character("Announcer") "\"And now the moment you've all been waiting for!{w=0.5} The first round of the annual Kobukan Academy Battle Team exhibition!\""

$ renpy.music.queue("Audio/Music/KantoGym_Start.ogg", channel='music', loop=None, fadein=1.0, tight=None)
$ renpy.music.queue("Audio/Music/KantoGym_Loop.ogg", channel='music', loop=True, tight=None)

$ renpy.music.stop(channel='crowd2', fadeout=2.0)

$ PlaySound("crowd_cheer.ogg")

$ renpy.transition(dissolve)
call clearscreens from _call_clearscreens_32

show blank with transball

$ renpy.pause(2.0, hard=True)

show exhibition01 behind blank:
    zoom 1.1
show exhibit01veno behind blank:
    zoom 1.1
show exhibit01float behind blank:
    zoom 1.1

$ renpy.pause(0.5, hard=True)

show blank:
    alpha 1.0
    ease 1.0 alpha 0.0

show exhibition01:
    subpixel True
    zoom 1.1
    ease 5.0 zoom 1.0
show exhibit01veno:
    subpixel True
    zoom 1.1
    ease 5.0 zoom 1.0
show exhibit01float behind exhibit01veno:
    subpixel True
    zoom 1.1
    ease 5.0 zoom 1.0
show exhibit01aqua behind exhibit01veno:
    subpixel True
    zoom 1.1 alpha 0.0
    parallel:
        ease 5.0 zoom 1.0
    parallel:
        ease 2.0 alpha 1.0
show exhibit01aquaglow:
    subpixel True
    zoom 1.1 alpha 0.0
    parallel:
        ease 5.0 zoom 1.0
    parallel:
        ease 2.0 alpha 1.0
    
Character("Announcer") "\"And we're underway!{w=0.5} It looks like the challenger's Floatzel is jumping straight in with Aqua Jet!\""

hide floatzel
hide venomoth
hide leaf
hide brendan
hide may
hide calem
hide ethan
hide leaf
hide janine

$ PlaySound("Pokemon/Moves/AquaJet.ogg")
$ renpy.pause(1.9, hard=True)

show exhibition01
show exhibit01veno
show exhibit01float
show exhibit01aqua
show exhibit01aquaglow
with vpunch

Character("Announcer") "\"...Well, that didn't seem to do much!\""

show exhibit01aqua:
    alpha 1.0
    ease 1.0 alpha 0.0
show exhibit01aquaglow:
    alpha 1.0
    ease 1.0 alpha 0.0

leaf @talking2mouth "You know, with Floatzel's speed, it's probably able to hit first, even without the boost from Aqua Jet."

hide exhibit01aqua
hide exhibit01aquaglow

leaf @surprised "You'd think the guy would try a different move to start things off."


$ PlaySound("Pokemon/Moves/StunSpore.ogg")

show exhibit01spore behind exhibit01veno with dis:
    alpha 1.0
    pause 4.0
    ease 1.0 alpha 0.0

show stunspore:
    subpixel True
    alpha 0.0 zoom 1.5 yalign 0.5 xpos -500
    parallel:
        ease 1.0 alpha 1.0
        pause 3.0
        ease 1.0 alpha 0.0
    parallel:
        ease 6.0 xpos 0

Character("Announcer") "\"What's this?{w=0.5} The arena is being filled with Venomoth's Stun Spore! Spectators close to the ring please avoid inhaling too much of it!\""

$ PlaySound("Pokemon/Moves/Paralyzed.ogg")

show exhibition01:
    parallel:
        xalign 0.0
        ease 0.02 xpos -10
        ease 0.02 xpos 10
        ease 0.02 xpos 0
        repeat 8
    parallel:
        yalign 0.0
        ease 0.02 ypos -10
        ease 0.02 ypos 10
        ease 0.02 ypos 0
        repeat 8
show exhibit01veno:
    parallel:
        xalign 0.0
        ease 0.02 xpos -10
        ease 0.02 xpos 10
        ease 0.02 xpos 0
        repeat 8
    parallel:
        yalign 0.0
        ease 0.02 ypos -10
        ease 0.02 ypos 10
        ease 0.02 ypos 0
        repeat 8
show exhibit01para behind exhibit01veno:
    parallel:
        xalign 0.0
        ease 0.02 xpos -10
        ease 0.02 xpos 10
        ease 0.02 xpos 0
        repeat 8
    parallel:
        yalign 0.0
        ease 0.02 ypos -10
        ease 0.02 ypos 10
        ease 0.02 ypos 0
        repeat 8
hide exhibit01float

Character("Announcer") "\"Oh no, it looks like Floatzel is paralyzed!{w=0.5} Things are definitely not looking good for our challenger!\""

show exhibit01spore:
    ease 0.5 alpha 0.0
show stunspore:
    ease 0.5 alpha 0.0

calem @talkingmouth "It was a good idea to lock down the Floatzel's speed and her opponent did a poor job reacting to it."
calem @closedbrow talking2mouth "Now the Venomoth can take out the Floatzel at its own pace."
ethan @closedbrow talking2mouth "That Floatzel... what is it, a water type? I think I've seen some Venomoth with Energy Ball."
    
hide exhibit01spore
hide stunspore
    
show energyball:
    alpha 0.0 zoom 1.5 xalign 0.8 yalign 0.5
    parallel:
        ease 2.0 xalign 0.5 yalign 1.0 zoom 1.0
    parallel:
        ease 1.0 alpha 0.9
        pause 0.75
        ease 0.5 alpha 0.0

$ renpy.music.play("Audio/crowd_cheer.ogg", channel='crowd3', loop=None, fadein=0.0)
$ PlaySound("Pokemon/Moves/EnergyBall.ogg")
$ renpy.pause(1.9, hard=True)

$ renpy.music.play("Audio/Stadium_chant.ogg", channel='crowd2', loop=True, fadein=1.0)

$ renpy.music.play("Audio/pokemon/cries/419.mp3", channel="altcry", loop=None)
show exhibition01
show exhibit01veno
show exhibit01para
show energyball
with vpunch

show exhibit01para:
    alpha 1.0
    ease 0.5 alpha 0.0

Character("Announcer") "\"Spectacular! With a surprise Energy Ball, Floatzel is down and out in one hit!{w=0.5} How will Janine's opponent respond to this explosive power?\""   

hide exhibit01para
hide energyball

show exhibition02 behind exhibition01:
    zoom 1.1
show exhibit02veno behind exhibition01:
    zoom 1.1
show exhibit02clay behind exhibition01:
    zoom 1.1

brendan @surprised "Well, there we go."
brendan @happybrow talkingmouth "Heh, why bother with tactics when you can just go for a knockout punch, huh?"
may @surprised "I didn't know Venomoth could learn that move! Bug-types really are versatile, huh?"
red @talkingmouth "I don't think it can learn it on its own, but you should be able to teach it."
leaf @talking2mouth "It was smart of her not to reveal it so soon.{w=0.5} That Floatzel's Trainer was totes caught off guard."
leaf @talkingmouth "But... I wonder why she bothered with the Stun Spore?"
calem @closedbrow talking2mouth "Perhaps she wasn't certain of her ability to KO. If your opponent is of an unknown strength, it's usually a good strategy to lower their potential to manageable levels before attempting an attack."
    
$ renpy.music.stop(channel='crowd2', fadeout=3.0)

$renpy.music.play("audio/pokemon/ball sound.ogg", channel="altcry", loop=None)
$ renpy.music.queue("audio/pokemon/cries/344.mp3", channel="altcry", loop=None)
$ renpy.pause(0.6, hard=True)

show exhibition01:
    alpha 1.0
    ease 1.0 alpha 0.0
show exhibit01veno:
    alpha 1.0
    ease 1.0 alpha 0.0

show exhibition02:
    subpixel True
    zoom 1.1
    ease 5.0 zoom 1.0
show exhibit02veno:
    subpixel True
    zoom 1.1
    ease 5.0 zoom 1.0
show exhibit02clay:
    subpixel True
    zoom 1.1
    ease 5.0 zoom 1.0

Character("Claydol") "\"Clay.{w=0.33} Dol.\""

Character("Announcer") "\"And the next Pokémon out of the gate is Claydol, a dual Ground and Psychic-type Pokémon!{w=0.5} What can the challenger be planning to use with such a peculiar Pokémon?\""

hide exhibition01
hide exhibit01veno

red @talking2mouth "Hm. Claydol. Hoenn-native. It has high defenses, normally. Only ability is Levitate, but that's probably not going to come up here..."
    
leaf @talking2mouth "I might go with Venomoth on this one.{w=0.5}{nw}"
extend leaf @closedbrow talking2mouth " Claydol's got the defensive advantage since it's tankier by nature, but that Venomoth might have another trick up its sleeve."

may surprisedbrow frownmouth @surprised "You really think Venomoth's that strong?"

leaf happy "Hey, this {i}is{/i} Janine we're talking about here.{w=0.5} You never know."

calem @closedbrow talking2mouth "A lot of people take note of Claydol's bulk, but it also boasts a respectable offensive moveset.{w=0.5} Keep in mind its super-effective Psychic moves."

brendan @talking2mouth "Nah, my money's still on Venomoth."

ethan @happy "Yeah, did you see how it took down Floatzel? Besides, if you're counting Claydol's Psychic attacks, you can't forget Venomoth's Bug attacks!"

calem @closedbrow happymouth "Of course. I'm merely playing devil's advocate."
    
redmind @thinking "Looks like nobody knows who's got the clear advantage. Both of them have an offensive type advantage over the other, but..."
redmind @thinking "Taking into account all the factors of both Pokémon, in the matchup against Venomoth... It should be fifty-fifty."
redmind @angrybrow frownmouth "But it's not. Not even close."

$ renpy.music.play("Audio/crowd_cheer.ogg", channel='crowd3', loop=False, fadein=0.0)
    
Character("Announcer") "\"And the second round is underway!{w=0.5} Let's see what our challenger's Claydol has in store for Janine's Venomoth!\""

show exhibit02dance1 orb1 with dis:
    alpha 1.0
show exhibit02dance1 orb1 with dis:
    alpha 1.0

$ PlaySound("Pokemon/Moves/QuiverDance_Base.ogg")
$ renpy.pause(2.0, hard=True)
$ PlaySound("Pokemon/Moves/QuiverDance_Boost.ogg")

Character("Announcer") "\"Oh! It looks like Venomoth is opening this round with two successive Quiver Dances, ladies and gentlemen!{w=0.5} It's quickly raising its strength! How will our challenger respond?\""

show exhibit02dance1 base:
    alpha 1.0
show exhibit02dance2 floor1:
    alpha 1.0

$ renpy.music.play("Audio/crowd_cheer.ogg", channel='crowd3', loop=False, fadein=0.0)
$ PlaySound("Pokemon/Moves/Psybeam.ogg")

show exhibition02:
    parallel:
        xalign 0.0
        ease 0.033 xpos -12
        ease 0.033 xpos 12
        ease 0.033 xpos 0
        repeat 20
    parallel:
        yalign 0.0
        ease 0.033 ypos -5
        ease 0.033 ypos 5
        ease 0.033 ypos 0
        repeat 20
show exhibit02veno:
    parallel:
        xalign 0.0
        ease 0.033 xpos -12
        ease 0.033 xpos 12
        ease 0.033 xpos 0
        repeat 20
    parallel:
        yalign 0.0
        ease 0.033 ypos -5
        ease 0.033 ypos 5
        ease 0.033 ypos 0
        repeat 20
show exhibit02dance1 base:
    parallel:
        xalign 0.0
        ease 0.033 xpos -12
        ease 0.033 xpos 12
        ease 0.033 xpos 0
        repeat 20
    parallel:
        yalign 0.0
        ease 0.033 ypos -5
        ease 0.033 ypos 5
        ease 0.033 ypos 0
        repeat 20
show exhibit02dance2 floor1:
    parallel:
        xalign 0.0
        ease 0.033 xpos -12
        ease 0.033 xpos 12
        ease 0.033 xpos 0
        repeat 20
    parallel:
        yalign 0.0
        ease 0.033 ypos -5
        ease 0.033 ypos 5
        ease 0.033 ypos 0
        repeat 20
show exhibit02clay:
    parallel:
        xalign 0.0
        ease 0.033 xpos -12
        ease 0.033 xpos 12
        ease 0.033 xpos 0
        repeat 20
    parallel:
        yalign 0.0
        ease 0.033 ypos -5
        ease 0.033 ypos 5
        ease 0.033 ypos 0
        repeat 20
show exhibit02psy behind exhibit02clay:
    alpha 0.0
    parallel:
        ease 0.25 alpha 1.0
        pause 3.0
        ease 0.75 alpha 0.0
    parallel:
        xalign 0.0
        ease 0.033 xpos -12
        ease 0.033 xpos 12
        ease 0.033 xpos 0
        repeat 20
    parallel:
        yalign 0.0
        ease 0.033 ypos -5
        ease 0.033 ypos 5
        ease 0.033 ypos 0
        repeat 20
        
show psybeam behind exhibit02psy:
    alpha 0.0
    parallel:
        ease 0.25 alpha 1.0
        pause 1.5
        ease 0.25 alpha 0.0
    parallel:
        parallel:
            xalign 0.4
            ease 0.033 xpos -30
            ease 0.033 xpos 30
            ease 0.034 xpos 0
            repeat 20
        parallel:
            pause 1.9
            ease 0.1 xalign 1.0
    parallel:
        parallel:
            yalign 0.33
            ease 0.033 ypos -10
            ease 0.033 ypos 10
            ease 0.034 ypos 0
            repeat 20
        parallel:
            pause 1.9
            ease 0.1 yalign 0.5
        

$ renpy.pause(2.0, hard=True)

Character("Announcer") "\"And Claydol attacks with a powerful Psybeam!{w=0.5} Folks, I think that's it for Venomoth!"

$ renpy.music.play("Audio/Pokemon/Venomoth.ogg", channel="altcry", loop=None)
$ renpy.music.play("Audio/crowd_cheer.ogg", channel='crowd3', loop=False, fadein=0.0)

Character("Venomoth") "\"Vennt!\""

Character("Announcer") "\"Wait, what's this?{w=0.33} I don't believe it! Venomoth completely shrugged it off!{w=0.5} There's barely a scratch on it thanks to Quiver Dance!\""

hide venomoth
hide psybeam

show exhibit02dance1 orb2
show exhibit02dance2 floor2
with dis

$ PlaySound("Pokemon/Moves/QuiverDance_Boost.ogg")

Character("Announcer") "\"...And Venomoth still continues to power up with its {i}third{/i} use of Quiver Dance!{w=0.5} If our challenger doesn't have an answer, Venomoth will be unstoppable!\""

$ PlaySound("Pokemon/Moves/CosmicPower_Boost.ogg")

show exhibit02psy with dis:
    alpha 1.0

Character("Announcer") "\"It looks like Claydol is responding by using Cosmic Power to bolster its defenses, but it might be too little too late!{w=0.5} Is this the end of the road for Claydol?\""

show exhibition02:
    parallel:
        xalign 0.0
        ease 0.033 xpos -12
        ease 0.033 xpos 12
        ease 0.033 xpos 0
        repeat 10
    parallel:
        yalign 0.0
        ease 0.033 ypos -5
        ease 0.033 ypos 5
        ease 0.033 ypos 0
        repeat 10
show exhibit02veno:
    parallel:
        xalign 0.0
        ease 0.033 xpos -12
        ease 0.033 xpos 12
        ease 0.033 xpos 0
        repeat 10
    parallel:
        yalign 0.0
        ease 0.033 ypos -5
        ease 0.033 ypos 5
        ease 0.033 ypos 0
        repeat 10
show exhibit02clay:
    parallel:
        xalign 0.0
        ease 0.033 xpos -12
        ease 0.033 xpos 12
        ease 0.033 xpos 0
        repeat 10
    parallel:
        yalign 0.0
        ease 0.033 ypos -5
        ease 0.033 ypos 5
        ease 0.033 ypos 0
        repeat 10
show exhibit02dance1 orb2:
    parallel:
        xalign 0.0
        ease 0.033 xpos -12
        ease 0.033 xpos 12
        ease 0.033 xpos 0
        repeat 10
    parallel:
        yalign 0.0
        ease 0.033 ypos -5
        ease 0.033 ypos 5
        ease 0.033 ypos 0
        repeat 10
show exhibit02dance2 floor2:
    parallel:
        xalign 0.0
        ease 0.033 xpos -12
        ease 0.033 xpos 12
        ease 0.033 xpos 0
        repeat 10
    parallel:
        yalign 0.0
        ease 0.033 ypos -5
        ease 0.033 ypos 5
        ease 0.033 ypos 0
        repeat 10
        
show greenorb1 as orb1:
    alpha 1.0 xpos 1750 ypos 900 zoom 0.0
    block:
        ease 0.12 zoom 1.0 xpos 700 ypos 700
        ease 0.1 xpos 550 ypos 250
        ease 0.15 zoom 0.0
    repeat 4
show greenorb1 as orb2:
    alpha 1.0 xpos 1750 ypos 900 zoom 0.0
    block:
        ease 0.14 zoom 1.2 xpos 800 ypos 200
        ease 0.14 xpos 550 ypos 250
        ease 0.12 zoom 0.0
    repeat 5
show greenorb2 as orb3:
    alpha 1.0 xpos 1750 ypos 900 zoom 0.0
    block:
        ease 0.09 zoom 0.9 xpos 600 ypos 500
        ease 0.13 xpos 550 ypos 250
        ease 0.12 zoom 0.0
    repeat 4
show greenorb2 as orb4:
    alpha 1.0 xpos 1750 ypos 900 zoom 0.0
    block:
        ease 0.13 zoom 1.25 xpos 740 ypos 50
        ease 0.14 xpos 550 ypos 250
        ease 0.11 zoom 0.0
    repeat 5
show greenorb3 as orb5:
    alpha 1.0 xpos 1750 ypos 900 zoom 0.0
    block:
        ease 0.12 zoom 1.25 xpos 650 ypos 300
        ease 0.1 xpos 550 ypos 250
        ease 0.14 zoom 0.0
    repeat 3
show greenorb3 as orb6:
    alpha 1.0 xpos 1750 ypos 900 zoom 0.0
    block:
        ease 0.15 zoom 1.0 xpos 700 ypos 100
        ease 0.1 xpos 550 ypos 250
        ease 0.11 zoom 0.0
    repeat 5

$ renpy.music.play("Audio/crowd_cheer.ogg", channel='crowd3', loop=False, fadein=0.0)
$ PlaySound("Pokemon/Moves/GigaDrain.ogg")
$ renpy.pause(1.5, hard=True)
$ renpy.music.play("Audio/pokemon/cries/344.mp3", channel="altcry", loop=None)
$ renpy.pause(0.25, hard=True)
$ renpy.music.play("Audio/Stadium_chant.ogg", channel='crowd2', loop=True, fadein=0.5)

show exhibit02dance1 base:
    alpha 1.0
    ease 0.5 alpha 0.0
show exhibit02dance2 floor1:
    alpha 1.0
    ease 0.5 alpha 0.0
show exhibit02psy:
    alpha 1.0
    ease 0.5 alpha 0.0
show exhibit02clay:
    alpha 1.0
    ease 0.75 alpha 0.0

show venomoth behind beam3:
    subpixel True
    xanchor -1.5 xzoom -0.5 yzoom 0.5 yalign 1.0 ypos 620 xpos 30 alpha 1.0
    block:
        parallel:
            ease 1.1 ypos 620
            ease 1.0 ypos 760
            ease 1.1 ypos 650
            ease 1.0 ypos 800
            ease 1.1 ypos 625
            ease 1.0 ypos 780
            repeat
        parallel:
            ease 0.52 xpos 80
            ease 0.6 xpos 30
            ease 0.62 xpos 120
            ease 0.7 xpos 25
            ease 0.58 xpos 100
            ease 0.65 xpos 0
            repeat

Character("Announcer") "\"Ouch!{w=0.3} And there it is! A direct hit with Giga Drain!{w=0.5} Claydol is down and out for the count! Janine and Venomoth easily take round two!\""
Character("Announcer") "\"The challenger is down to his last Pokémon!{w=0.5} Is this Pokémon the key to a surprise reversal or will this be yet another clean sweep from Janine?\""

hide greenorb1 as orb1
hide greenorb1 as orb2
hide greenorb2 as orb3
hide greenorb2 as orb4
hide greenorb3 as orb5
hide greenorb3 as orb6    
hide exhibit02dance1
hide exhibit02dance2
hide exhibit02clay
hide exhibit02psy

show exhibition02:
    alpha 1.0
    ease 1.5 alpha 0.0
show exhibit02veno:
    alpha 1.0
    ease 1.5 alpha 0.0

leaf @happy "Brutal! That's what I like to see from Kobukan Academy's Battle Team's Captain!"
calem @closedbrow talking2mouth "Splendid. She made no wrong moves. It's like watching a skilled painter..."
ethan @closedbrow talking2mouth "Yeah, but why'd she have Giga Drain {i}and{/i} Energy Ball? I don't know if that was the play."
may @happy "Well, it worked out for her, in any case!"

hide exhibition02
hide exhibit02veno

redmind @thinking "That round was over in the blink of an eye, even though the Claydol, theoretically, should have lasted much longer than Floatzel."
redmind @thinking "Can the difference between two Pokémon really be that great?"
redmind @thinking "Is this what Lance was trying to tell me?"

$ renpy.music.stop(channel='crowd2', fadeout=4.0)

Character("Announcer") "\"Now we're here in the third round!{w=0.5} Has the challenger figured out a way to deal with Janine's Venomoth?\""

$ renpy.music.play("Audio/Pokemon/Victreebel_Ball.ogg", channel="altcry", loop=None)

show victreebel at pokeball behind beam3:
    alpha 0.0 zoom 0.0 yalign 1.0 ypos 600 xpos 1800
    block:
        parallel:
            ease 0.33 alpha 1.0 ypos 300 xpos 1500
            ease 0.67 ypos 850 xpos 1300
        parallel:
            ease 0.5 zoom 0.5

$ renpy.pause(1.0, hard=True)

show victreebel:
    alpha 1.0 zoom 0.5 xpos 1300 ypos 850
    parallel:
        ease 0.4 ypos 845
        ease 0.2 ypos 850
        repeat
    parallel:
        ease 0.6 xpos 1280
        ease 0.6 xpos 1300
        repeat

Character("Announcer") "\"It's a... Victreebel!{w=0.5} Can this Pokémon be the saving grace for our challenger or will Janine take yet another victory under her belt?\""

may @surprised "Two Kanto Pokémon... I'm not familiar with 'em, but this looks like another even match, right?"
leaf @closedbrow talking2mouth "Not even.{w=0.5} With those Quiver Dances, Venomoth's got everything it needs to mop up that Victreebel."

$ renpy.music.play("Audio/Pokemon/Veno-Victree.ogg", channel="altcry", loop=None)

show venomoth:
    subpixel True
    parallel:
        ease 2.0 ypos 450
    parallel:
        ease 0.05 xpos 20
        ease 0.05 xpos 40
        repeat 20

show victreebel:
    parallel:
        block:
            ease 0.4 ypos 845
            ease 0.2 ypos 850
        block:
            ease 0.6 xpos 1000
    parallel:
        block:
            pause 0.5
            parallel:
                ease 0.4 ypos 845
                ease 0.2 ypos 850
                repeat
            parallel:
                ease 0.6 xpos 1020
                ease 0.6 xpos 1000
                repeat
    
show blank2 with dis:
    alpha 1.0

show revjan:
    subpixel True
    alpha 0.0 xpos -100
    parallel:
        pause 1.5
        ease 1.5 alpha 1.0
    parallel:
        pause 1.5
        ease 7.0 xpos 0

show revveno:
    subpixel True
    alpha 0.0 xpos 100
    parallel:
        pause 1.5
        ease 1.5 alpha 1.0
    parallel:
        pause 1.5
        ease 7.0 xpos 0
        
show revred:
    alpha 0.0 zoom 1.0 xalign 0.5 yalign 1.0
    parallel:
        pause 0.75
        ease 1.5 alpha 1.0

redmind @sad "Is it that simple?{w=0.5} That whoever has the weaker Pokémon, no matter the circumstances, and no matter how much they try to fight back..."

Character("Announcer") "\"And here we go, ladies and gentlemen!{w=0.5} We have Venomoth and Victreebel facing off in the third and what could be the final round of this exhibition match!\""

hide venomoth
hide victreebel

$ renpy.music.play("Audio/crowd_cheer.ogg", channel='crowd3', loop=False, fadein=0.0)
$ PlaySound("Pokemon/Moves/Psychic.ogg")

show psychattack behind revred:
    alpha 0.0 zoom 1.0 xalign 0.5
    parallel:
        ease 0.75 alpha 0.75 zoom 1.1
        pause 0.25
        ease 0.25 zoom 1.0
    parallel:
        block:
            parallel:
                xalign 0.0
                ease 0.033 xpos -9
                ease 0.033 xpos 9
                ease 0.033 xpos 0
                repeat 25
            parallel:
                yalign 0.0
                ease 0.033 ypos -3
                ease 0.033 ypos 3
                ease 0.033 ypos 0
                repeat 25
    
show revjan:
    alpha 1.0
    pause 0.75
    ease 0.25 alpha 0.0

show revveno:
    alpha 1.0
    pause 0.75
    ease 0.25 alpha 0.0

Character("Announcer") "\"Venomoth attacks with a powerful Psychic attack, but Victreebel is trying to recover with Synthesis!{w=0.6}{nw}"

$ PlaySound("Pokemon/Moves/Synthesis.ogg")

extend @talkingmouth " Can our challenger hang on?"


hide revjan
hide revveno

show psychattack:
    alpha 0.85
    ease 1.5 alpha 0.0

show revlance with dis:
    alpha 1.0

redmind -happy frownmouth sadbrow "They're in perfect sync. Is it just because Janine trained her Venomoth well?{w=0.5} Meanwhile, all her opponent can do is try to keep up."

if (classstats["Dark"] > 0):
    redmind "Lance talks about a Pokémon's strength like it's the be-all and end-all element in battle, but Instructor Karen would call that philosophy selfish.{w=0.5} So who's right?"
    redmind "There's just gotta be more to battles than raw power.{w=0.5} There {i}has{/i} to be."
elif (classstats["Poison"] > 0):
    redmind "Lance talks about a Pokémon's strength like it's the be-all and end-all element in battle, but Instructor Koga would beg to differ.{w=0.5} So who's right?"
    redmind "There's just gotta be more to battles than raw power.{w=0.5} There {i}has{/i} to be."
else:
    redmind "Lance talks about a Pokémon's strength like it's the be-all and end-all element in battle, but there's just gotta be more to it than that.{w=0.5} There {i}has{/i} to be."

$ PlaySound("Pokemon/Moves/Psychic.ogg")

$ renpy.music.play("Audio/crowd_cheer.ogg", channel='crowd3', loop=False, fadein=0.0)
$ renpy.music.play("Audio/Stadium_chant.ogg", channel='crowd2', loop=True, fadein=0.5)

Character("Announcer") "\"And Victreebel is down! Another absolutely crushing victory for Janine!\""

show janine uniform:
    alpha 0.0 xpos 300
    ease 0.75 alpha 1.0

show venomoth:
    subpixel True
    alpha 0.0 yalign 1.0 ypos 1080 xpos 700
    parallel:
        ease 0.75 alpha 1.0
    parallel:
        block:
            parallel:
                ease 1.1 ypos 820
                ease 1.0 ypos 960
                ease 1.1 ypos 850
                ease 1.0 ypos 1000
                ease 1.1 ypos 825
                ease 1.0 ypos 980
                repeat
            parallel:
                ease 0.52 xpos 630
                ease 0.6 xpos 730
                ease 0.62 xpos 620
                ease 0.7 xpos 725
                ease 0.58 xpos 600
                ease 0.65 xpos 700
                repeat

show blank2:
    alpha 1.0
    ease 1.0 alpha 0.0
show revred:
    alpha 1.0
    ease 1.0 alpha 0.0
show revlance:
    alpha 1.0
    ease 1.0 alpha 0.0

Character("Announcer") "\"Is anyone surprised at the results?{w=0.5} Once again Janine has proven why she is the captain of Kobukan Academy's Battle Team!\""

hide janine
hide venomoth
with Dissolve(0.75)
    
hide blank2
hide revred
hide revlance

pause 0.5

hide brendan
hide may
hide calem
hide leaf
hide ethan

show brendan surprisedbrow frownmouth at rightside with dis
show may at farrightside with dis
show leaf at farleftside with dis
show calem at leftside with dis
show ethan at centerside with dis

may @angrybrow talkingmouth "Geez, I don't know what I was expecting when you said 'exhibition match,' but {i}that{/i} definitely wasn't one.{w=0.5} Why'd you want to watch this?"

hide janine
hide venomoth

show leaf happy
show may -surprisedbrow -frownmouth -surprised 
with dis
    
brendan -surprisedbrow -frownmouth -surprised @sadbrow happymouth "Hey, this was my first time, too!{w=0.5} How was I gonna know the guy's Pokémon would get stomped like that?"

show leaf surprisedbrow with dis

red @frownmouth "[ellipses]"

leaf -surprisedbrow @talkingmouth surprisedbrow "You okay, [first_name]?{w=0.5} You look really pale."

red @wince talking2mouth "Huh?{w=0.25} Oh, yeah, I'm fine.{w=0.5} It's probably from all the excitement just now."

leaf @happy "That? You call that exciting?{w=0.5} Trying to find seats was more exciting than that!"

calem @surprised "!"

calem @closedbrow talkingmouth "Oh, look. The next matches are starting soon."
    
$ PlaySound("crowd_cheer.ogg")

show blank2 with dis

$ renpy.transition(dissolve)
call clearscreens from _call_clearscreens_33

narrator "You stay to watch the rest of the exhibition matches, but that first match still stands head and shoulders above the others."

scene blank2

$ renpy.music.stop(channel='crowd2', fadeout=10.0)

redmind frownmouth "I can't stop replaying it in my head.{w=0.5} The difference in power between the two Trainers and their Pokémon was staggering."

$ renpy.music.stop(channel='crowd', fadeout=10.0)

redmind "I wonder if [pika_name], [starter_name], and I could..."

stop music fadeout 7.5

redmind @thinking "Ugh, I can't think of stuff like this right now.{w=0.5} I have more important things to worry about."
redmind "But still..."

jump day010408