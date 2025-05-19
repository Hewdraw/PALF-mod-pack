label gym010603:

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

rowan @talking2mouth "Hm."

pause 1.0

wally uniform @sadbrow talkingmouth "Heads up, [wally_name]. Rowan was really quiet in morning homeroom. He even gave me a compliment."

red uniform @confused "Is that a bad thing?"

wally @closedbrow talking2mouth "Normally, it means someone's about to die..."

red @talking2mouth "Noted. I'll prepare my last will and testament."

wally @sadbrow talkingmouth "I don't think you need to do that. It {i}probably{/i} won't be you."

rowan @angrybrow talking2mouth "A-{i}hem{/i}!"

pause 1.0

rowan @talking2mouth "My time with this class is coming to a close. I have seen improvement--and I have seen some measure of disappointment, too."
rowan @closedbrow talking2mouth "However. Within this class, there is no-one that I would... 'write off.'"
rowan @talking2mouth "I posit that you all have the {i}potential{/i} to be Pokémon Champions. Though, perhaps, not at Champion Cynthia's caliber."

pause 0.5

rowan @talking2mouth "There is one person, and one person, only, who could bring you to that level."

bianca uniform @excitedeyes happyeyebrows happymouth "Is it us? We just need to believe in ourselves?"

rowan @closedbrow talking2mouth "That is absolutely ridiculous. Do not speak again."

bianca @doteyes shockedeyebrows omouth "[ellipses]"

redmind @confusedeyebrows angryeyes frownmouth "Come on, Rowan. Her father just died a couple weeks ago. Have some sympathy."

rowan @talking2mouth "The only one who can get you to Champion Cynthia's level is Champion Cynthia herself."
rowan @closedbrow talking2mouth "Naturally, she does not teach at Kobukan--my attempts to convince her to do so have been for naught. But I can understand wanting to retain one's full-time championship for as long as possible. I was no different."
rowan @talkingmouth "So. How can you attain Champion Cynthia's guidance without her suddenly, if not uncharacteristically, deciding to change careers?"

pause 1.0

play music "audio/stadium_murmur.ogg" fadein 0.5 channel "crowd" noloop

rowan @talking2mouth "It is through me."
rowan @angrybrow talking2mouth "And I {i}do{/i} mean {i}through{/i} me. Today, I will be examining each of you carefully--{i}very{/i} carefully."
rowan @talking2mouth "I will examine the speed at which you make decisions in battle. I will examine the effectiveness of your moves. And I will examine the strength of the Pokémon you brought into the match."
rowan @closedbrow talking2mouth "The student who stands out to me most will gain the chance to battle me."

play music "audio/stadium_murmur.ogg" fadein 0.5 channel "crowd" noloop

gardenia uniform @surprisedbrow talking2mouth "What? But, Sir, you're a Champion--"

rowan @angrybrow talking2mouth "Do not call me sir, and do not call me Champion, blast it! I'm Rowan. I haven't defended a Hall of Fame in many decades."
rowan @talking2mouth "I will be battling as an old man whose prime has long since passed, and if you cannot beat me, then I question what you're getting out of this school!"

pause 1.0

rowan @talking2mouth "I will make clear my expectations. Defeat me, and I will call Champion Cynthia, and recommend that you be hired for a position in the Sinnoh League immediately upon graduation."
rowan @closedbrow talking2mouth "I believe Byron is seeking a successor. Perhaps it could be you?"
rowan @talking2mouth "Naturally, this reward comes with risk."
rowan @angrybrow talking2mouth "Fail to defeat me, and I will write a strongly-worded letter to your homeroom professor--and you will be mentioned in less-than-pleasant terms in my report for Alder's return."

redmind @closedbrow sweat frownmouth "Eesh. He's so far up the totem pole he can even chew out the other homeroom professors, huh?"

rowan @talking2mouth "Now, enough of this yammering we must continually inflict upon ourselves. Show your strength to me! Prove you can stand in the same league as Champion Cynthia."
rowan @closedbrow talking2mouth "Bruno, the partners, if you will."

hide rowan with dis

bruno @sadbrow "[ellipses]"
bruno @sadbrow talking2mouth "{size=30}I miss Alder...{/size}"

hide bruno with dis

pause 1.0

show flannery tiredbrow frownmouth uniform with dis

flannery @talking2mouth tiredbrow "Hey."

red @talkingmouth "Hey. Sorry, zoned out for a moment. Did Bruno pair us?"

flannery @talking2mouth "Yeah."

pause 2.0

flannery @talking2mouth "Are we battling, or what?"

red @sadbrow talkingmouth "Uh... yeah, sure. Sorry, are you feeling alright?"


if (GetRelationshipRank("Flannery") > 0):
    $ ValueChange("Flannery", 1)

    flannery @sadbrow talkingmouth "Ugh... thanks for asking, but it's nothing new."
    flannery @closedbrow talking2mouth "Spend all day worrying about the gym. Can't go to sleep, so I stay up too late, writing. Same as ever."

else:
    flannery @talking2mouth "Same as always. Just tired."
    flannery @closedbrow talking2mouth "Up too late, writing. Nothing new there."

if (HasEvent("Whitney", "Whitney2Part2")):
    flannery @lightblush sad2eyes talking2mouth "But, uh, recently, there's this new thing with Whit, and[ellipses]"
    flannery @closedeyes talking2mouth "Well, I'm sleeping even less now."

red @talkingmouth "Lunch is after this battle. Maybe we can get you some midday coffee?"

flannery @closedbrow talking2mouth "Don't let anyone in the nurse course hear that. They'd chew my ears off."

if (HasEvent("Whitney", "Whitney2Part2")):
    flannery @surprisedbrow frownmouth "[ellipses]"
    flannery @closedeyes talking2mouth "{size=30}Hm... Whitney... biting ears... there's something there.{/size}"

    red @thonk "[ellipses]?"

flannery @talking2mouth "Ugh. Anyway, let's battle. I might just fall asleep on my feet, at this rate."

python:
    trainer1 = MakeRed(3)
    if (HasEvent("Flannery", "HasMagby")):
        trainer2 = MakeTrainer("Flannery", number=3, order=["Onix", "Numel", "Darumaka", "Quilava", "Charcadet", "Magby"])
    else:
        trainer2 = MakeTrainer("Flannery", number=3, order=["Onix", "Numel", "Darumaka", "Quilava", "Charcadet"])

call Battle([trainer1, trainer2], uniforms=[True, True], custombrain=flannerybattlebrain) from _call_Battle_177
$ RecordBattle("Flannery2")

show flannery tiredbrow frownmouth uniform with dis

if (WonBattle("Flannery2")):
    flannery @talking2mouth "Well done, challenger. For your victory, you've earned the--"
    flannery @surprisedbrow frownmouth "[ellipses]"
    flannery -frownmouth @happy sweat "Oops. Force of habit."

    $ ValueChange("Flannery", 3)

red @happy "Good battle, Flannery. Where'd you get those Air Balloons, though?"

flannery @talking2mouth "Coworker back in Hoenn. Well, 'coworker'... he's more like an uncle. Wattson. He was in the Air Force--apparently, in the military, they hand them out like candy."

red @sweat talkingmouth "I wouldn't mind a couple of my own. You'd probably appreciate one when you're not using a Foreveral, right, [pika_name]?"

if (pikachuobj.GetHealthPercentage() > 0.25):
    $ PlaySound("pokemon/pikachu_excite1.ogg")

    libpikachu @angryeyes happymouth "Pi-KAAA!"

else:
    $ PlaySound("pokemon/pikachu_sad2.ogg")

    libpikachu @dizzyeyes surprised2mouth "Pika... piiiikaaaa."

    flannery @sadbrow talkingmouth "Oh... guess I hit him a bit hard."

    red @happy "It's alright. C'mon, buddy, let's get you healed up."

show blank2 with splitfade

$ PlaySound("BellChime.ogg")

pause 2.0

scene gym
show bruno think:
    xpos 0.33
show rowan coat:
    xpos 0.66 xzoom -1
with Dissolve(2.0)

bruno @talking2mouth "Have you decided who you will battle?"

rowan @closedbrow talking2mouth "...I am still ruminating."
rowan @angrybrow talking2mouth "I {i}do{/i} intend dire consequences for any student who fails to defeat me. This is not a burden I would place on a student lightly."
rowan @closedbrow talking2mouth "Ideally, there is a student out there who has strength enough to succeed in spite of whatever blockers I may halt him or her with."
rowan @talking2mouth "Someone with the wit and presence to take advantage of the victory they earn--but the sheer bullheadedness to smash through their failure, if it comes to that."

pause 1.0

bruno @talking2mouth "Perhaps Blue Oak would--"

rowan @closedbrow talking2mouth "I do not like his attitude."

bruno @closedbrow talking2mouth "Few do."

pause 1.0

bruno @talking2mouth "Raihan Kaasib?"

rowan @closedbrow talking2mouth "Possible. That's a stubborn man. Stubborn like a rock. But what benefit could he derive from an invitation to the Sinnoh League? It would be wasted on him."

pause 1.0

bruno @talking2mouth "I can recommend two more names."

if (HasEvent("Alder", "Volunteer")):
    bruno @talking2mouth "Two weeks ago, Alder and I fought each other, alongside two students. By my side was Bea Langston. [first_name] [last_name] fought aside Alder's."

    rowan @closedbrow talking2mouth "Bea and [first_name]... Hm, yes, those two battled yesterday."

    if (WonBattle("Bea2")):
        rowan @talking2mouth "[first_name] won, I seem to recall."

    else:
        rowan @talking2mouth "Bea won, I seem to recall."

    rowan @talking2mouth "What about the battle against Alder? How did your party fare?"

    if (WonBattle("BeaBruno1")):
        bruno @talking2mouth "We were soundly, and fairly, defeated."

    else:
        bruno @talking2mouth "Our victory had a narrow margin."

else:
    bruno @talking2mouth "Two weeks ago, Alder and I fought each other, alongside two students. By my side was Bea Langston. Leaf Green fought aside Alder's."

    rowan @closedbrow talking2mouth "Bea and Leaf... Hm, yes, I've seen those two battle."

    if (WonBattle("Bea2")):
        rowan @talking2mouth "Bea lost her match against [first_name] yesterday, I seem to recall."

        bruno @closedbrow talking2mouth "A testament to [first_name] [last_name]'s strength."

    else:
        rowan @talking2mouth "Bea won her match against [first_name] yesterday, I seem to recall."

        bruno @closedbrow talking2mouth "A testament to her strength. [first_name] [last_name] is a member of the Battle Team, as is she."

    rowan @talking2mouth "What about the battle against Alder? How did your party fare?"

    bruno @talking2mouth "We were soundly, and fairly, defeated."

rowan @closedbrow talking2mouth "Harrumph. Much to think on, then. Though I detest the thought, perhaps I will have to do some research into these candidates."

pause 1.0

rowan @surprisedbrow talking2mouth "Hm? Did you say something?"

bruno @talking2mouth "I did not."

pause 1.0

rowan @sadbrow talking2mouth "Oh. I thought I saw your lips moving, and--er."
rowan @closedbrow talking2mouth "Harrumph!"

jump afterlunchtransition