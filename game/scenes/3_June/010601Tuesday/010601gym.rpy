label gym010601:

stop music fadeout 1.5
queue music "Audio/Music/Gym_Start.ogg" noloop
queue music "Audio/Music/Gym_Loop.ogg"

$ renpy.music.play("Audio/school_crowd.ogg", channel='crowd', loop=True, fadein=1.0)

$ renpy.transition(dissolve)
show screen currentdate

scene gym
show bruno think:
    xpos 0.33
show rowan coat:
    xpos 0.66 xzoom -1
with Dissolve(2.0)

$ renpy.pause(2.0, hard=True)

redmind uniform @confusedbrow frownmouth "Hm? Who's that?"

pause 1.0

show rowan angrybrow with dis

pause 2.0

rowan -angrybrow @talking2mouth "Silence."

stop music fadeout 0.5 channel "crowd"
stop music fadeout 0.5

pause 1.5

$ BecomeNamed("Professor Rowan")

rowan @talkingmouth "I am Professor Rowan Nanakamado."

pause 0.5

$ AddEvent("Professor Rowan", "Rename1")

rowan @closedbrow talking2mouth "I do not expect you to waste my, or anyone else's time, by calling me by that full nonsense."

$ AddEvent("Professor Rowan", "Rename2")

rowan @talking2mouth "To you, I am Rowan. There's no man worth the time it takes to say his title."

pause 1.0

$ AddEvent("Professor Rowan", "Rename3")

queue music "Audio/Music/rowan.ogg"

rowan @talking2mouth "Now. There are three things I would have you know before we begin the consternation of battle."

pause 0.5

rowan @angrybrow talking2mouth "I do not seek equity in my work as an instructor. I seek {i}excellence.{/i}"
rowan @talking2mouth "I will grant special attention to those I believe have the qualities necessary to succeed. Others, I will aid as my contract requires."
rowan @angrybrow talking2mouth "There are many who come to Kobukan believing that merely associating with the name will grant them the success they require."
rowan @talkingmouth "To that I say 'pish and tosh.' A name is worth nothing. A reputation is worth nothing. People ought to be evaluated based on the merits they display in front of you."

pause 1.0

rowan @talking2mouth "To any fools who believe they can skate by under the radar in this class, due to its lack of gradation, I warn you now that I can make this class {i}very{/i} impactful, without touching your gradebook whatsoever."
rowan @talking2mouth "Money, reputation, and association are worth nothing in my eyes, nor in the eyes of any man of character, like Champion Cynthia."

may uniform @surprised "{size=30}Woah! Did he say Cynthia?{/size}"

gardenia uniform @talking2mouth "{size=30}He sure did. He brings her up {i}all{/i} the time in homeroom. He was her homeroom teacher when she attended Kobukan.{/size}"

may @sadbrow talkingmouth "{size=30}You're in his homeroom? What's it like, having him as a homeroom teacher?{/size}"

gardenia @happy "{size=30}It's a warzone! He pits us against each other for practically everything. A bunch of kids have dropped out already, actually...{/size}"

may @sadbrow talking2mouth "{size=30}That's not good...{/size}"

gardenia @sadbrow talking2mouth "{size=30}The thing is, though, he's a really good teacher[ellipses] {/size}{nw}"
extend @happy "{size=30}if you can pay the price!{/size}"

rowan @talkingmouth "Right. That's quite enough going on about myself. As I understand it, you are in the middle of a triple battle unit?"

bruno -think @talking2mouth "That is correct."

rowan @talkingmouth "Harrumph. Unovan battling style. Lots of room for creativity. Perhaps a tad too much."
rowan @closedbrow talking2mouth "Even so, this is the world we live in. There's no point blathering on about how battles 'used' to be. Battles evolve just like Pokémon. Trainers must evolve alongside their partners!" 
rowan @talkingmouth "International battles are getting more and more common. If Champion Cynthia didn't understand how that Galarian Gigantamaxing worked, she'd be at a disadvantage when battling that Leon boy."
rowan @talking2mouth "Let that be your first lesson. There is no excuse for not knowing something. You have phones. You have brains. And you have eyes. Between those three traits, you should be able to gather any information that may benefit you."

pause 1.0

rowan @talking2mouth "Now, your second lesson--"

serena uniform @surprised "{size=30}Ah... his first lesson was a single sentence?{/size}"

raihan uniform @closedbrow talkingmouth "{size=30}Man of few words. He expects you to understand and memorize the lesson as soon as he says it. He's always like this in homeroom.{/size}"
raihan @sadbrow talkingmouth "{size=30}Oh, and the shouting... he can't hear too well, so that's kinda just how he talks.{/size}"

serena @sadbrow talking2mouth "{size=30}I... see. I'm not sure I could fully embrace that teaching philosophy.{/size}"

raihan @talkingmouth "{size=30}Not for everyone, true enough. I've got no problem with it, though.{/size}"
raihan @sadbrow sadmouth "{size=30}Not a big fan of how often he dismisses Leon, though. Bloke seems to think Cynthia would roll over him. Nah, for my money, it'd be the other way around.{/size}"

rowan @talking2mouth "Now, your second lesson is about battlefield conduct."

pause 2.0

rowan @angrybrow talking2mouth "You!"

redmind @surprisedbrow frownmouth "Me?"

rowan @talking2mouth "Do you know what I mean by 'battlefield conduct?'"

menu:
    "[courageoption] How the trainer treats his Pokémon while battling.":
        show rowan surprisedbrow with dis
        $ TraitChange("Courage")

    "[charmoption] How the trainer treats his opponent while battling.":
        show rowan surprisedbrow with dis
        $ TraitChange("Charm")

rowan @talking2mouth "Harrumph! A thoughtful answer."
rowan -surprisedbrow @talkingmouth "But only partially correct."

pause 1.0

rowan @talkingmouth "Dignity, students. Battlefield conduct is how one expresses their dignity."
rowan @closedbrow talking2mouth "If one needs to shout at their Pokémon--this ridiculous 'dodge it', or 'go full-power' nonsense--you are sacrificing something greater than the battle."
rowan @angrybrow talking2mouth "You are sacrificing your dignity. The perfect trainer could communicate with their Pokémon without ever saying a word."

sabrina uniform @surprisedbrow "[ellipses]"
tia uniform hat @surprisedbrow "[ellipses]"

rowan @talking2mouth "Now, not only does this save you the embarrassment of looking like a fool, it is also tactically sound." 
rowan @closedbrow happymouth "Your opponent can hardly react to your moves if you aren't screaming them at the top of your lungs across the battlefield, can they?"
rowan @closedbrow talking2mouth "I had the misfortune of missing the last Quarter Qlash round, but I was told there was one trainer who lost because she simply could not communicate with her Pokémon without yelling her commands, like some sort of adolescent."

dawn uniform @surprisedbrow frownmouth "[ellipses]"

rowan @talking2mouth "If you look at the performances of various Champions, you'll find most of them are all but silent in their battles."
rowan @angrybrow talking2mouth "Except that {i}Leon{/i} boy... but that may be due to the Galarian league's expectation of showmanship, and not a {i}personal{/i} failing."

pause 1.0

rowan @talkingmouth "No matter. To summarize your second lesson: if you cannot already communicate with your Pokémon without letting your opponent know what you're doing, you must do learn to do so."
rowan @talking2mouth "There are many different options for ways you could do such a thing... code words, hand signs, telepathy for those for whom it is an option, perhaps even music."
rowan @talking2mouth "Do not make the excuse such things are too difficult to learn. Even at my age, I have begun to pick up a sign dialect."
rowan @talking2mouth angrybrow "{i}Anything{/i} would be better than that childish shouting. Deplorably undignified."

leaf uniform @sadbrow talking2mouth "{size=30}Nonvocal battling is a {i}really{/i} advanced skill, though...{/size}"

ethan uniform @talking2mouth "{size=30}I guess he expects us {i}all{/i} to be Cynthia.{/size}"

rowan @talking2mouth "There is one more thing a trainer can do to sacrifice their dignity."

pause 1.0

rowan @closedbrow talking2mouth "Forfeiting a match is an affront to the very core of being a Pokémon trainer." 
rowan @talking2mouth "You indignify your Pokémon, yourself, your opponent, and our very Pokémon world by running away from a trainer battle."
rowan @angrybrow talking2mouth "I hope I never see any of you attempt such a thing. If I do, rest assured that it is the last mistake you will ever make at Kobukan."

pause 1.0

rowan @talking2mouth "As long as both trainers have one Pokémon left standing, the match has not ended. There is not a single excuse to forfeit a battle before both trainers have given everything within their power to defeat the other."
rowan @talking2mouth "If it were up to me, forfeiting a Pokémon match would come with a heavy prison sentence... but, {w=0.5}harrumph, {w=0.5}{nw}"
extend @closedbrow talking2mouth "non-trainers with Pokémon may be unfairly punished by that rule." 
rowan @sadbrow talking2mouth "We can't expect them to understand the great dignity that being a Pokémon trainer comes with."
rowan @angrybrow talking2mouth "I, however, {i}can, and do,{/i} expect it out of each and every one of you. Dignity is your keyword, and if it isn't now, it very well ought to be!"

pause 1.0

rowan @angrybrow talking2mouth "Well? What are you all lollygagging about for? I've given the blasted lecture! Start battling!"

bruno @closedbrow talking2mouth "Rowan, I need to assign the partners first."

rowan @closedbrow talking2mouth "{size=30}Are they so incapable they cannot find their own partners? Harrumph.{/size}"

hide rowan
hide bruno
with dis

pause 1.0

show may sadbrow uniform with dis

may @talkingmouth "Hi!"

red @talkingmouth "Hi. Rowan's pretty intense, huh?"

may @closedbrow talking2mouth "{i}Seriously{/i} intense. I feel... kinda dizzy, to be honest. I can't imagine what homeroom with him is like."

red @talkingmouth "Probably pretty different from Professor Oak's. But he taught Cynthia, so it must work for some people."

may @talkingmouth "I guess!"

pause 1.5

red @talkingmouth "Guess we should battle now?"

may angrybrow talkingmouth "No running away!"

python:
    trainer1 = MakeRed(number=3)
    trainer2 = MakeTrainer("May", number=3)

call Battle([trainer1, trainer2], uniforms=[True, True]) from _call_Battle_175
$ RecordBattle("May2")

show may uniform with dis

if (WonBattle("May2")):
    show may uniform closedbrow poutmouth with dis

    may @talking2mouth "Oh, boo..."

    pause 0.5

    $ ValueChange("May", 3)

    may -closedbrow -poutmouth @sadbrow talkingmouth "Good job. It's frustrating to lose, but I know I did my best, at least. Hopefully Professor Rowan was watching."

else:
    may @happy "Nice, I won! Hopefully Professor Rowan was watching!"

show rowan:
    xpos 0.33
show may surprisedbrow frownmouth:
    xpos 0.5
    ease 0.5 xpos 0.66
with dis

rowan @talking2mouth "He was."

pause 2.0

may @surprised "Oh! Um[ellipses] what are your thoughts[ellipses]?"

rowan @closedbrow talking2mouth "Harrumph. You're the Birch girl. Sapphire, yes?"

may @closedbrow talking2mouth "Oh, that's... embarrassing. No, Sapphire's my middle name. I'm May."

rowan "[ellipses]"

rowan @talking2mouth "You aren't committing to your choices. In every move you make, you leave yourself an 'out.'"
rowan @closedbrow talking2mouth "That can be useful in battle, occasionally... but only if you capitalize on it."

may -surprisedbrow -frownmouth @sadbrow talkingmouth "Oh, well... I'm really more of a Coordinator."

pause 1.0

show may surprisedbrow frownmouth with dis

rowan @closedbrow talking2mouth "Are you."

pause 2.0

rowan @closedbrow talking2mouth "Harrumph!"

hide rowan with dis

if (GetRelationshipRank("May") > 1):
    show may sadbrow with dis

    red @closedbrow talking2mouth "Hey, May, I... I'm sorry. He didn't know what you're going through. He didn't know what we talked about--you know, about your Coordinating."

    may @talkingmouth "I kinda think he did, though. I guess it's pretty obvious..."

    pause 1.5

    $ ValueChange("May", 1, 0.66)

    may @sadbrow talkingmouth "Thanks anyway. Maybe he would've been a bit more tactful if he knew about... you know."

    red @sadbrow talkingmouth "Maybe."

$ PlaySound("BellChime.ogg")

pause 2.0

jump afterlunchtransition