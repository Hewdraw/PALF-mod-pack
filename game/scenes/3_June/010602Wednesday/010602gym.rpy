label gym010602:

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

rowan @talking2mouth "Well! I see you have all made it to class promptly today. I'm glad to see it!"

if (lastclassmood == 10):
    redmind uniform @thinking "I was only able to make it because [altclasstaught[lastclass]] let us go ten minutes early, so Rowan wouldn't yell at us..."

rowan @talking2mouth "I watched you all intently yesterday. I've heard much about this class--much about this year, as a whole." 
rowan @closedbrow talking2mouth "What I heard is worth naught one whit. What I have {i}seen{/i} informs my thoughts, reflections, and opinions moving forward."

redmind uniform @thinking "You could hear a pin drop..."

rowan @talking2mouth "I am, overall, pleasantly surprised. This is a powerful year. Your strength begets strength. You battle each other, learning more about each other, training each other, and making yourselves stronger."
rowan @talking2mouth "This is a cycle we at Kobukan wish to encourage, and I've rarely seen it demonstrated so successfully."

gardenia uniform @sadbrow talking2mouth "{size=30}Five bucks he's about to namedrop Cynthia.{/size}"

rowan @talking2mouth "Yes, the last time I saw a class this powerful, it was when Champion Cynthia was my student, almost a decade ago."

gardenia @happy "{size=30}Knew it.{/size}"

if (money >= 5):
    menu:
        ">Give her five bucks":
            $ money -= 5
            $ AddEvent("Gardenia", "GaveFiveBucks")
            $ ValueChange("Gardenia", 1, 0.1)

            gardenia @surprised "{size=30}Oh, seriously, partner? I was joking.{/size}"

            red @closedbrow talkingmouth "{size=30}I'm broke, but not the kind of broke that can't spare $5.{/size}"

            gardenia @flirtbrow smirkmouth "{size=30}That shows strength of character. Pretty cool of you.{/size}"

            red @sadbrow talkingmouth "{size=30}Thanks. But let's pay attention to what your homeroom teacher's saying, now. Guy's scary.{/size}"

        ">Miser your money":
            $ AddEvent("Gardenia", "DidNotGiveFiveBucks")
            red @sweat closedbrow talking2mouth "{size=30}I didn't agree to this.{/size}"
            red @closedbrow talking2mouth "{size=30}Anyway, let's pay attention to what your homeroom teacher's saying, now. Guy's scary.{/size}"

else:
    red @sadbrow talkingmouth "Sorry, I don't have $5 on me."

    gardenia @surprisedbrow talkingmouth "{size=30}Seriously? Partner, that's not good. I understand you want to put money in the bank for interest, but you need to keep {size=30}some{/size} on you.{/size}"
    gardenia @talking2mouth "{size=30}There's going to be tons of one-time deals that you won't be able to take advantage of if you don't have any money on you.{/size}"
    gardenia @sadbrow talkingmouth "{size=30}Keep it in mind, alright?{/size}"

    red @closedbrow talking2mouth "{size=30}Alright. But let's pay attention to what your homeroom teacher's saying, now. Guy's scary.{/size}"

rowan @closedbrow talking2mouth "...so, in summary, I expect better. Especially of my Sinnohan students. If anyone wishes to challenge Champion Cynthia, you must advance yourselves greatly before attempting such a thing. That will be all."

$ renpy.music.play("Audio/school_crowd.ogg", channel='crowd', loop=True, fadein=1.0)

show bruno surprisedbrow frownmouth with dis

rowan @talking2mouth "Bruno, assign the partners. I will be watching these battles, and I expect everyone to stay alert afterwards, as I will be directly critiquing battlers' performances."

bruno -surprisedbrow -frownmouth @talking2mouth "Yes. Bea, please battle [first_name]."

show bea uniform with dis:
    xpos 0.15

bea @talking2mouth "Sir."

hide rowan
hide bruno
with dis

show bea:
    xpos 0.15
    ease 0.5 xpos 0.5

bea @talking2mouth "'Lo."

red @talking2mouth "Hey, Bea."

bea @talking2mouth "Rowan will be watching us. We should battle to the best of our ability, so that he sees the true strength we hold."

red @talking2mouth "That's the plan. What do you think of him?"

bea @talking2mouth "I have little opinion. He judges others by his actions--I am all too happy to extend the same courtesy to him."
bea @closedbrow talking2mouth "I do not know if I would manage to succeed in his homeroom--I have heard stories that seem to indicate it would be difficult for me. But his manner, though rigid and demanding, has not yet put me off."

red @happy "Fair enough."

bea @talking2mouth "Now, are you ready?"

red @winkbrow happymouth "I am, but you're not."

bea angrybrow talkingmouth "Hmph. You may test that assumption imminently."

show gym:
    xalign 0.5 yalign 0.5
    ease 2.0 zoom 1.2

show bea:
    xpos 0.5
    ease 2.0 ypos 1.2 zoom 1.3

bea @closedbrow talking2mouth "Now..."

bea angry "Begin!"

show bea:
    ease 0.3 ypos 2.0 zoom 3.0 alpha 0.0

pause 0.3

python:
    trainer1 = MakeRed(3)
    if (beahastyrogue):
        trainer2 = MakeTrainer("Bea", number=3, order=["Rolycoly", "Tyrogue", "Machop", "Falinks", "Clobbopus"])
    else:
        trainer2 = MakeTrainer("Bea", number=3, order=["Rolycoly", "Falinks", "Machop", "Clobbopus"])

call Battle([trainer1, trainer2], uniforms=[True, True], customswitchbrain=beaswitchbrain) from _call_Battle_176
$ RecordBattle("Bea2")

show bea uniform with dis

if (WonBattle("Bea2")):
    bea @talking2mouth "Hm. There is, perhaps, room for improvement."

    $ ValueChange("Bea", 3)

    bea @talkingmouth "Thank you for opening my eyes to this."

else:
    bea @talking2mouth "Hm. There is, perhaps, room for improvement. On both our sides, naturally."

red uniform @happy "Thanks for the tough battle! Triple battles might be your thing. That strong defensive [('Hitmontop' if beahastyrogue else 'Falinks')] in the center of your formation made it difficult to break through."

bea @talking2mouth "Yes. In a phalanx, every man must hold his shield to fight as a single, impenetrable unit. That is the source of the phalanx's strength. Each soldier protects the man to his left, from thigh to neck, with his shield."
bea @talking2mouth "A single weak spot, and the phalanx shatters. Hence the importance of having a Pokémon in the center--the most targeted spot--that can take many blows."

if (WonBattle("Bea2")):
    bea @sadbrow talkingmouth "Well... that is the theory. Execution, perhaps, I am lacking--but I will build a shield that no force can shatter with further training."

    red @talkingmouth "Look forward to seeing it again in the future."

else:
    red @talkingmouth "I'll keep that in mind."

red @happy "Now, let's--"

show rowan angrybrow:
    xpos 0.33
with vpunch

show bea surprisedbrow with dis:
    xpos 0.5 
    ease 0.5 xpos 0.66

rowan @talking2mouth "{i}Inexcusable!{/i}"

red @surprised "Gah! Sorry, Sir, what--"

rowan -angrybrow @closedbrow talking2mouth "Not you."

show rowan:
    xpos 0.33 alpha 1.0 ypos 1.0 zoom 1.0
    ease 0.5  xpos 0.1 alpha 0.0 ypos 1.2 zoom 1.3

red @closedbrow talking2mouth "{size=30}Oh, thank God.{/size}"

scene gym
show rowan angrybrow:
    xpos 0.66 xzoom -1
show dawn surprisedbrow frownmouth uniform:
    xpos 0.33
with splitfade

rowan @talking2mouth "You! What's your name?"

dawn @talking2mouth "D-{w=0.5}D-{w=0.5}D-{w=0.5}Dawn... Berlitz...?"

rowan @talking2mouth "Speak up! I'm almost deaf, you know!"

dawn @talking2mouth "Dawn! Berlitz!"

rowan @closedbrow talking2mouth "Dawn. Are you scared of me?"

dawn @talking2mouth "Yes, terrified."

rowan @talking2mouth "Why are you scared of me?"

dawn @talking2mouth "Because I'm afraid you're going to yell at me?"

rowan @angrybrow angrymouth "Why am I going to yell at you?"

dawn @talking2mouth "Because I'm asking my Pokémon to battle like they're forty levels higher, and I know it isn't working, but I don't know what else to do?"

rowan @closedbrow talking2mouth "That's completely correct. You already know ninety-five percent of what you need to know, and so you have excused yourself from learning that last five percent."
rowan @angrybrow talkingmouth "You do not have permission to. The missing five percent is what will allow you to claim victory over Champion Cynthia when you challenge her again."

dawn -surprisedbrow @talking2mouth "Wait... you remember me?"

rowan -angrybrow @closedbrow talking2mouth "Yes. Chimchar. Impish Nature, I seem to recall. Proud of its power. Where is it now?"

dawn surprisedbrow @happybrow talkingmouth "It's in Alola, along with--"

rowan @talking2mouth "You're training a Frigibax, not a Monferno. You cannot expect your Frigibax to perform the acrobatic feats that Monferno performed."
rowan @talking2mouth "Dodging moves is not an option. Outspeeding the foe rarely is. You must control the pace of the battlefield using your Frigibax's Legacy move."
rowan @angrybrow talking2mouth "By lowering the speed of an opponent in the middle of the round through Paralysis, you can make them move after an ally who would hit harder, but does not have much speed to speak of--your Tinkatuff, perhaps."

pause 0.5

rowan @talking2mouth "Your Pokémon cannot use brute force and speed to succeed anymore."
rowan @closedbrow talking2mouth "Given your performance against Champion Cynthia, it seems clear they never could."
rowan @talking2mouth "Strong moves, used by strong Pokémon, have a place in battles, but you have neither at present. If I see you attempting to win battles by using a strategy that does not work for you, you will be thoroughly chastised."

dawn bamboozledeyes embarrassedmouth @sadeyebrows talking2mouth "You mean {i}this{/i} wasn't thoroughly chastising...?"

rowan happybrow @happybrow talkingmouth "Oh ho ho ho ho!"

pause 1.0

show dawn bamboozled2eyes with dis

rowan -happybrow @angrybrow talking2mouth "No. This was {i}teaching{/i}. When you are chastised, you {i}will{/i} know."

show dawn:
    xpos 0.33 rotate 0 ypos 1.0
    ease 1.5 rotate -4 ypos 1.05

show calem uniform behind dawn:
    xpos -0.1
    ease 1.0 xpos 0.25

calem @talkingmouth "Come along, Dawn. Let's get you some water."

dawn @talking2mouth "Water[ellipses]? Water. {gradualsize=30-18}Strong against Fire. Fire. Strong against ice. Ice. Strong against...{/gradualsize}"

show calem:
    xpos 0.25
    ease 0.5 xpos -0.2

show dawn:
    xpos 0.33 rotate -4 ypos 1.05
    ease 0.5 xpos -0.17

pause 1.0

rowan @closedbrow talking2mouth "Hmph. Promise in that girl, but I've no stock in promises. Who can assert the future with certainty?"
rowan @angrybrow talking2mouth "Blast your promises of the future, and do it now! {w=0.5}Quite!"

pause 1.0

show rowan closedbrow with dis

pause 1.0

show rowan angrybrow with dis

pause 1.0

rowan angrymouth "You! Unacceptable!"

show rowan with dis:
    xpos 0.66
    ease 0.3 xpos 1.2

pause 1.0

scene blank2 with splitfade

$ PlaySound("BellChime.ogg")

pause 2.0

redmind uniform @wince frownmouth "Thank god that he's only taking over this class for a week."

jump afterlunchtransition