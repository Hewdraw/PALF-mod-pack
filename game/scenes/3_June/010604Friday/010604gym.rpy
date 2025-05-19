label gym010604:

stop music fadeout 1.5
queue music "Audio/Music/rowan.ogg"

$ renpy.music.play("Audio/school_crowd.ogg", channel='crowd', loop=True, fadein=1.0)

$ renpy.transition(dissolve)
show screen currentdate

scene gym
show bruno think:
    xpos 0.33
show rowan coat:
    xpos 0.66 xzoom -1
with Dissolve(2.0)

stop music fadeout 1.5 channel "crowd"

$ renpy.pause(2.0, hard=True)

rowan @talking2mouth "Since we talked yesterday, I have done, for eighteen hours, that which I hate most, besides going to that blasted otolaryngologist. I know I'm going deaf, why must I pay you thousands to tell me?! Harrumph!"
rowan @closedbrow talking2mouth "In any case... that which I hate most is research. But not any research--I have studied Pokémon evolution for forty years, and have no intention of stopping."
rowan @angrybrow talking2mouth "What I hate is having to research {i}people{/i}. Arrogant, entitled, proud {i}people{/i}, whom fill this world with unnecessariness."
rowan @closedbrow talking2mouth "Pokémon are perhaps the sole sane life-forms on this planet--they did not fall into the foolhardiness of rumors, or reputation, or so-called {i}respect{/i}."

pause 1.0

rowan @closedbrow talking2mouth "This process was made {i}all the more{/i} difficult by the reoccurrence of one name. One name that has begun to irk me to no end."

pause 1.0

rowan @angrybrow talking2mouth "[first_name]. Step up."

red uniform @closedbrow talking2mouth "{size=30}Yeah, I figured.{/size}"

rowan @talking2mouth "No matter who I talked to, your name was dropped onto my lap, with the {i}clear{/i} expectation that I should know, or perhaps consider you excessively, as though you were anything but another student."

pause 1.0

rowan @talking2mouth "[first_name]. Do you consider {i}yourself{/i} to be something other than 'just another student'?"

menu:
    "Yes.":
        $ AddEvent("Professor Rowan", "NotAnotherStudent")
        rowan @angrybrow talking2mouth "A proud answer demands a strong justification."

        red uniform @talking2mouth "I'm different from the other students." 

    "No.":
        $ AddEvent("Professor Rowan", "JustAnotherStudent")
        rowan @angrybrow talking2mouth "Have some damned self-awareness. You {i}must{/i} be Samuel's protege, with that level of nescience." 
        rowan @confusedbrow "Would 'just another student' have ended up in the smallest Battle Team we've fielded since I joined this school many years ago?"
        rowan @talking2mouth "Being 'different' is not bad. Nor is it good. It is fact, and fact must be acknowledged. Now, try again. You {i}are{/i} different. How?"

red @happy "I'm luckier. I'm {i}so{/i} much luckier than almost everyone I know. I've been given amazing friends, opportunities, and I have the best Pokémon partner that ever existed."

$ PlaySound("Pokemon/ball sound.ogg")
$ PlaySound("Pokemon/pikachu_angry1.ogg")

pause 0.3

libpikachu angryeyes happymouth "Pika!"

rowan @talking2mouth "Do you think {i}luck{/i} will carry you to your dreams of championship?"

red @talking2mouth "No, Rowan. I'll {i}earn{/i} my way there."

rowan @angrybrow talking2mouth "Hrmph. Fine. You'll do. Everyone else, partner off. I will deal with [first_name]."

bruno @talking2mouth "I will assign the partners, then."

hide bruno with dis

red @surprisedbrow talking2mouth "You'll battle me?"

python:
    bestinstructor = None
    for key, item in classtaught.items():
        if (item == GetStatRank(0)):
            bestinstructor = key
            break
    gender = "his" if persondex[bestinstructor]["Sex"] == Genders.Male else "her"
    if (bestinstructor != "Burgh"):
        bestinstructor = bestinstructor.split(" ")[1]

rowan @closedbrow talking2mouth "Yes. Single battle. I must see if Samuel and [bestinstructor]'s constant praise has any merit."
rowan @angrybrow talking2mouth "Or if, as I suspect, you are just another fragile balloon full of hot air."

red @talking2mouth "I don't know what you heard about me. But I'll prove it to you."

rowan @closedbrow talking2mouth "Harrumph! I've heard that before. And far more than half of those overinflated egos cowardly ran away before I even had the chance to defeat all their Pokémon."

show rowan nocoat nocase with dis

$ PlaySound("Thud.ogg")

narrator "Rowan tosses his coat onto the floor, drops his briefcase, and flexes his muscles with an audible cracking. He pulls out a well-weathered Poké Ball, and gets into a battle stance."

rowan @talking2mouth "[first_name], a balloon is very susceptible to being pricked, revealing the truth of what's inside."
rowan @talking2mouth "And in your case, I believe I'm just the prick needed."

red @talking2mouth "I've heard a lot about you, too--how you're a great teacher for the people who can survive your class."
red @angrybrow talking2mouth "But I haven't seen any proof of that. All I've seen you do is be a bully. So maybe I should stop relying on {i}your{/i} reputation, and see who you really are for myself."

rowan @angrybrow happymouth "Harrumph! I would like nothing more than if you did! And there's only one way for two trainers--two {i}men{/i}--to do that!"

red @angrybrow talking2mouth "Battle!"

python:
    AddEvent("Professor Rowan", "RowanBattle")
    trainer1 = MakeRed()
    trainer2 = MakeTrainer("Rowan")

call Battle([trainer1, trainer2], uniforms=[True, False], customexpressions=["red uniform angrybrow frownmouth", "red uniform angrybrow talking2mouth", "rowan nocoat nocase angrybrow", "rowan nocoat nocase angrybrow angrymouth"], dialogfunc=rowanbattledialog) from _call_Battle_179
$ RecordBattle("Rowan1")
$ RemoveEvent("Professor Rowan", "RowanBattle")

queue music "Audio/Music/rowan.ogg"

if (Fled):
    $ AddEvent("Professor Rowan", "FledBattle")
    show rowan nocoat nocase surprisedbrow with dis

    red @talking2mouth "I concede. Okay? I concede, you win."
    red @angrybrow talking2mouth "I've got something more important to do. Yell at me later, {i}after{/i} I've helped a Pokémon that needs me."

    rowan @talking2mouth "[first_name]-"

    red @angry "{i}Later{/i}!"

    jump frenzydodriobattle

elif (WonBattle("Rowan1")):
    show rowan nocoat nocase with dis
    
    rowan @talking2mouth "Hmph. In spite of the distractions, in spite of what seemed like an ill-conceived attempt to throw me off... it appears you have won."

    rowan @closedbrow talking2mouth "Well done. I will make good on my promise."

    jump rowancallscynthia

else:
    show rowan nocoat nocase angrybrow with dis 

    pause 1.0

    red uniform @sadbrow talking2mouth "I'm sorry. I tried my hardest--I tried to see it through, I tried to-- Rowan?"

    rowan @sadbrow "[ellipses]"
    rowan @talking2mouth "I[ellipses] I cannot hear you."

    red @surprisedbrow talking2mouth "Rowan?"

    rowan @closedbrow talking2mouth "I cannot hear[ellipses] anything. I cannot hear myself."

    pause 1.0

    rowan @closedbrow talking2mouth "Suppose {i}that{/i} was the last battle I ever heard? Harrumph."
    rowan sadbrow @talking2mouth "What a {i}waste{/i}."
    rowan @talking2mouth "Gardenia, come with me. I need to go to Miriam. These things have passed before, but... they are more frequent."

    gardenia uniform @surprisedbrow talking2mouth "Oh! Um, okay."

    narrator "Gardenia gives him an awkward thumbs-up."

    rowan @closedbrow talking2mouth "Everyone else, you are dismissed. Remember what I have taught this week. It will serve you well."
    rowan @angrybrow talking2mouth "Connections are everything. When you are old and weak, you will want to have people grateful to you. Trainers are not strong alone--but through their Pokémon, and their allies."
    rowan @talking2mouth "Dignity, connection, evolution. Remember this. Harrumph!"

    call clearscreens() from _call_clearscreens_261
    scene blank2 with splitfade

    $ HealParty()

    scene blank2
    
    show afternoon at vspaz
        
    pause 3.5

    $ timeOfDay = "Afternoon"

    pause 2.0

    narrator "You spend all lunch searching in the garden for the Pokémon you heard crying out, but aren't able to find it..."

    narrator "What a bust of a day. You'll be glad for the weekend."

    jump PickElective

label frenzydodriobattle:

stop music fadeout 1.5

queue music "audio/music/reliccastle_start.ogg" noloop fadein 10.0
queue music "audio/music/reliccastle_loop.ogg"
scene blank2 with splitfadefast

pause 0.1

scene garden:
    zoom 0.625
show clouds behind garden
with splitfadefast

red sweat uniform hatless @talking2mouth "Crap, lost my hat somewhere back there, while I was running. But the cry was definitely coming from here, and--"

$ sidemonnum = 85
$ PlaySound("pokemon/cries/85.mp3")

show sideportraitfull:
    zoom 0.5 ypos 0.3 xpos 1.2
    ease 0.5  ypos 0.3 xpos -0.2

pause 1.0

redmind @surprisedbrow frownmouth "I knew it. Another Frenzy. A Dodrio..."

$ sidemonnum = 85
$ PlaySound("pokemon/cries/85.mp3")

show sideportraitfull:
    zoom 0.7 ypos 0.5 xpos -0.2 xzoom -1
    ease 0.5  ypos 0.5 xpos 1.2 xzoom -1

if (HasEvent("Whitney", "FrenzBee")):
    redmind @thonk "How do they keep getting on-campus?"
else:
    redmind @thonk "How did it get on-campus?"

redmind @angrybrow frownmouth "It doesn't matter right now. Right now, my job is to make sure it's not suffering anymore."

red @talking2mouth "Come here, Dodrio. I'll help you!"

$ PlaySound("pokemon/cries/85.mp3")
sidemon "Dododododrio!!!"

show sideportraitfull:
    zoom 1.0 ypos 0.8 xpos 1.2 yanchor 1.0 xanchor 0.5
    linear 0.3 ypos 0.8 xpos 0.5
    ease 0.3 xpos 0.48 ypos 0.8
    ease 0.6 xpos 0.46 ypos 0.8
    pause 0.3
    ease 0.5 xpos 0.5 ypos 1.1 zoom 3.0 alpha 0.0

pause 1.8

python:
    trainer1 = Trainer("red", TrainerType.Player, playerparty, number=3)

    dodrioobj = Pokemon("Dodrio", level=33.3, moves=["Acupressure", "Tri Attack", "Drill Peck", "Frustration"], foreverals=["Dodrio Overal"], frenzynerf=(23, ["Return", "Roost", "Wing Attack", "Double Hit"], 84), intelligence=3)
    dodrioobj.ApplyStatus("frenzied")
    trainer2 = Trainer("sideportraitfull", TrainerType.Enemy, [dodrioobj], isPokemon=True)

call Battle([trainer1, trainer2], customexpressions=["red hatless uniform angrybrow sweat frownmouth", "red hatless uniform angrybrow sweat frownmouth", "sideportraitfull", "sideportraitfull"], healParty = False, specialmusic="Nothing") from _call_Battle_180
$ RecordBattle("Dodrio1")

pause 2.0

red sweat hatless @talking2mouth "...I did it."

if (dodrioobj in AllPokemon()):
    red @closedbrow talking2mouth "Capturing it broke the Foreveral."

elif (WonBattle("Dodrio1")):
    red @closedbrow talking2mouth "The Foreveral broke in the battle."

else:
    red @sweat closedbrow talkingmouth "It kicked my ass, but... at least the Foreveral shattered during the battle." 

if (HasEvent("Whitney", "FrenzBee")):
    redmind @closedbrow talking2mouth "That's just like with the Combee..."

show rowan coat with Dissolve(2.0)

queue music "Audio/Music/rowan.ogg"

rowan @talking2mouth "So, that's where you got off to."

red @talking2mouth sad2eyes "Sorry for running out on you in the middle of class."

rowan @sadbrow "[ellipses]"
rowan @talking2mouth "Your hat, young man. You dropped it."

show rowan:
    ypos 1.0 zoom 1.0
    ease 0.5 ypos 1.2 zoom 1.3

red @surprisedbrow talking2mouth "Oh."

pause 1.0

red -hatless @closedbrow sweat talking2mouth "Uh, thanks."

show rowan:
    ypos 1.2 zoom 1.3
    ease 0.5 ypos 1.0 zoom 1.0

pause 1.0

rowan @sadbrow talking2mouth "Championship, young man[ellipses]"

pause 0.5

rowan @closedbrow talking2mouth "Championship is everything you've heard of it. It is the greatest high. The most noble pursuit. It is the apex of trainerdom, and the worthiest goal for a man such as you."

pause 0.5

rowan @sadbrow talking2mouth "But it is also a series of losses. A series of losses that {i}does not end{/i} when you vacate the championship seat."

rowan @talking2mouth "Naturally, I lost my title. This was fine; to be expected. Then I started seeing my name disappearing from newspapers. I was Champion Nanakamado. Then I was Nanakamado. Then I was 'former Champion Nanakamado'..."
rowan @sadbrow sadmouth "Then Rowan."
rowan @talking2mouth "I believed I had little to offer the world after my championship. But my research kept me going, as did the company of my cherished assistant,{w=0.5} Lucas."

show rowan:
    xpos 0.5
    ease 0.5 xpos 0.33

$ DisplayPokemon("Torterra")

sidemon "Torrrr..."

rowan @closedbrow talking2mouth "Dawn received my Chimchar. A boy from Twinleaf received my Piplup. And this Turtwig was meant to be Lucas'. Until... he disappeared, quite suddenly."

$ HidePokemon()

show rowan:
    xpos 0.33
    ease 0.5 xpos 0.5

rowan @sadbrow talking2mouth "I damn Arceus every day for taking that boy away from me. Blast the years between us, we were friends."

red @sadbrow talking2mouth "I understand. Sam and I[ellipses] we're also friends."

rowan @closedbrow talking2mouth "After him, I had nothing but my research. I managed to earn a position here, at Kobukan, and the rest, perhaps, is history."
rowan @sadbrow talkingmouth "Ancient history, now, though."
rowan @talking2mouth "The only bright spot in my life since Lucas, my dearest friend, was taken was when I met Champion Cynthia."
rowan @talking2mouth "When she came to Kobukan, she was unassuming--a small, nervous, girl from an isolated rural community. You remind me of her."
rowan @happybrow talking2mouth "Harrumph. Pigtails, braces, and the ugliest plaid sweaters one ever did see. Her unassuming manner misled one from her strength. There was a time, I recall, when, in a moment of drunken weakness, I mentioned Lucas, and she..."

pause 1.0

rowan @closedbrow talking2mouth "For the first time in her life, she opened a history book. And I don't believe she's ever stopped since. She seems confident she can find some mark of that boy in the tales of the ancient past."
rowan @sadbrow sadmouth "I believe she can do anything. But... {i}that{/i}? No, not that."

pause 1.0

rowan @talking2mouth sadbrow "Ten years since I taught Champion Cynthia. Ten years since I have done anything I felt justified my continuation. No-one since has compared."
rowan @closedbrow talking2mouth "Then, two years ago, I started losing my hearing. Perhaps adopting Giga Impact as a signature move had long-term effects I hadn't foreseen."
rowan @sadbrow talkingmouth "The young do not think of such things."

pause 1.0

rowan @closedbrow sadmouth "I fear that in my desire to perpetuate, to prove there is a reason to, and to hold onto what I still have, I have[ellipses] lost the path."

red @sadbrow talking2mouth "Do you want my opinion?"

rowan @talking2mouth "There have been three persons whose opinions I have ever paid heed to. That being said, share your thoughts."

red @closedbrow talking2mouth "I don't think you're all wrong. You're right about, like, dignity, and making sure you don't accept people's reputation as gospel."
red @sadbrow talkingmouth "But I think it's fine, once or twice, to... to give someone the benefit of the doubt. It's fine to be kind."
red @closedbrow talking2mouth "You know more about Pokémon, and teaching, than I ever will, probably. But I've talked to some of your students, and..."
red @sadbrow talkingmouth "Frankly, I think they all need a cup of hot coffee and a warm blanket. I'm sure there's a way you can teach them to be champions {i}without{/i} giving them a therapy bill, too."

pause 1.0

rowan @talking2mouth "Four."

pause 1.0

rowan @closedbrow talking2mouth "You've given me much to think on, [first_name]."

red @talkingmouth sadbrow "And you've given me a bunch to think about too, Profe--er, Rowan."

rowan @talking2mouth "Harrumph. Have we further business here?"

red @sadbrow sweat talkingmouth "Well, you said you'd call Champion Cynthia?"

rowan @angrybrow talking2mouth "Harrumph. I hoped you'd forgotten. I don't like her to see me when I'm so emotional."

redmind @surprisedbrow frownmouth "This is {i}emotional{/i}?"

rowan @closedbrow talking2mouth "Very well. Just let me..."

label rowancallscynthia:

narrator "Rowan pulls out a bricky, clunky, phone, and presses in a number. After a moment's consideration, he presses the 'Speaker' button, though still holds it up to his ear."

pause 1.0

narrator "A moment later, a voice that rings with gentle power--a voice unmistakably recognizable--comes out of the phone's speaker."

cynthia silhouette "Professor Rowan? How pleasant it is to hear from you. It's been[ellipses]"
cynthia "{size=30}Lucian, how long has it been?{/size}"

TempCharacter("Lucian") "{size=30}You last talked on March 30th, during last year's World Championships, milady.{/size}"

cynthia "{size=30}As reliable as always. Thank you.{/size}"
cynthia "Rowan, it's been over a year! We really must catch up more frequently."

rowan @closedbrow talking2mouth "Oh, far be it from me to interrupt the busy day-to-day of a Champion."

cynthia "You're joking, my dear Rowan. I'm bored out of my gourd. I've so little to do I've been researching Unown. {i}Unown{/i}, dear Rowan!"
cynthia "I would sacrifice this championship in an {i}instant{/i} for the chance to do {i}something{/i} with it."
cynthia "[ellipses]Which,{w=0.5} upon reflection,{w=0.5} seems a rather paradoxical paradigm, but I'll stand by it."

rowan @happy "It's... it's really too much fun to hear from you again. I quite forgot how much I enjoyed your sense of humor."

cynthia "I rather remember you calling it my 'inordinate fondness for playing the fool,' back in the day."

rowan @talking2mouth "Well, what can I say? We were all fools back then."

cynthia "May I assume, then, that if you're calling me in spite of my perceived busyness, there's something rather important you'd like to share?"

rowan @talking2mouth "Correct, Lady Champion. There is a boy I would recommend to you. A Kobukan student--I believe you could find a good position for him in the Sinnoh League."

pause 2.0

cynthia "Oh my. Your recommendation comes rarely, and even more rarely, so emphatically. Who is this boy?"

redmind @closedbrow frownmouth sweat "Um. '{i}Man{/i}.' Please."

rowan @talking2mouth "[first_name]. [first_name] [last_name]."

pause 1.0

cynthia "Hmhmhm.~ I recognize that name, I think. Now, why would I...?"

TempCharacter("Lucian") "{size=30}The memes, milady. He is the one who defeated Dawn Berlitz, your challenger from 2002.{/size}"

cynthia "No, no, I don't think it was that. [first_name] [last_name]... [first_name] [last_name]..."
cynthia "Does he have any family in the archeological or mythological fields?"

show rowan surprisedbrow with dis

narrator "Rowan puts a hand over his phone and looks at you quizzically."

red @closedbrow talking2mouth sweat "The only fields my family is outstanding in are the ones where you grow wheat. Sometimes rice."

if (WonBattle("Rowan1")):
    rowan surprisedbrow @neutralbrow talking2mouth "No, I don't believe so. But he is focused, ambitious, and a fine battler, besides. I--"

else:
    rowan surprisedbrow @neutralbrow talking2mouth "No, I don't believe so. But he has strength of character, and he's a fine battler, besides. I--"

cynthia "Oh! Yes, I remember now. I've read about him."

rowan @surprisedbrow talking2mouth "You... have, Lady Champion?"

cynthia "Yes."

pause 2.0

cynthia "Was there anything else?"

rowan -surprisedbrow @talking2mouth "Well... I suppose not. If you wish for more details about this boy, I am at your disposal, Lady Champion."

cynthia "You are much appreciated, dear Rowan. But, please, no more of this 'Lady Champion' nonsense. There's no man worth the time it takes to say his title, no?"

rowan @closedbrow talking2mouth "Well... perhaps there is one."

cynthia "Hmhmhm.~"

pause 1.0

cynthia "Oh, yes, one more thing. Am I on speakerphone?"

if (WonBattle("Rowan1")):
    rowan surprisedbrow @neutralbrow talking2mouth "Yes. The entire gym class is with me. I took over for Alder."

    cynthia "Splendid. Students, Professor Rowan would much appreciate a box of Rage Candy Bars as thanks for teaching you."

else:
    rowan surprisedbrow @neutralbrow talking2mouth "Yes. [first_name] [last_name] is with me."

    cynthia "Splendid. [first_name], Professor Rowan would much appreciate a box of Rage Candy Bars as thanks for namedropping you."

rowan -surprisedbrow @closedbrow talking2mouth "N-nonsense, that's... I would not eat that sugary garbage."

cynthia "Hmhmhm.~ Then perhaps I'll recall the shipment I've had Lucian send to you for your birthday?"

rowan @talking2mouth "{size=30}That won't be necessary.{/size}"

cynthia "Of course. Take care of yourself, dear Rowan."

pause 1.0

cynthia "Oh, wait, one more one more thing. Is [first_name] still here?"

rowan @sadbrow talking2mouth "Yes[ellipses] though I'm now a bit concerned what you might say to him."

cynthia "Do not fear. All I wish to say to him is:"
cynthia "We will meet in eternity's ripples."

pause 2.0

cynthia "{size=30}That was a nice line, right, Lucian?{/size}"

TempCharacter("Lucian") "{size=30}Fantastic, milady.{/size}"

narrator "Rowan hangs up."

rowan @talking2mouth "Well, I've no idea what she's on about, but perhaps it'll make some sense to you."

red @talking2mouth "Is... is she crazy?"

rowan @talking2mouth "Yes. In the best way."

if (WonBattle("Rowan1")):
    pause 2.0

    rowan @angrybrow talking2mouth "Now, off with you, students. You've heard the voice of the Strongest Woman in the World--and that is the greatest thing I, as a teacher, can do for any of you. Go, now! Off you go!"

    call clearscreens() from _call_clearscreens_262
    scene blank2 with splitfade

    $ HealParty()

    scene blank2
    
    show afternoon at vspaz
        
    pause 3.5

    $ timeOfDay = "Afternoon"

    pause 2.0

    narrator "You spend all lunch searching in the garden for the Pokémon you heard crying out, but aren't able to find it..."

    narrator "It's unfortunate, but at least you won the battle. Cynthia's voice keeps ringing in your ears."

    jump PickElective

else:
    pause 2.0

    rowan @angrybrow talking2mouth "Now, off with you, boy. I've gotten far too personal with you, and I need to down some scotch to get my head on straight and really figure out where to go from here."

    red @happy "Alright. Bye, Professor. I'll see you later."

    rowan @closedbrow talking2mouth "I will be expecting a rematch later this year, boy. And I'll be expecting you to {i}win{/i}, next time."

    red @happy "Trust me: you'll get it."

    scene blank2 with splitfade

    call clearscreens() from _call_clearscreens_263
    scene blank2 with splitfade

    $ HealParty()

    scene blank2

    show afternoon at vspaz
        
    pause 3.5

    $ timeOfDay = "Afternoon"

    pause 2.0

    narrator "The business in the garden took more time than you thought it would... no time for lunch, you've got to head to your next elective immediately!"

jump PickElective