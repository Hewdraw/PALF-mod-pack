label gym010608:

play music "Audio/Music/Gym_Start.ogg" noloop
queue music "Audio/Music/Gym_Loop.ogg"

$ renpy.transition(dissolve)
show screen currentdate

scene gym with dis

show blank2 behind gym

$ renpy.pause(2.0, hard=True)

hide blank2

show alder with dis:
    xpos 0.66

show bruno think with dis:
    xpos 0.33

alder @happy2 "Good morning, students!"

bruno @norm2 "We watched you in class yesterday. We saw much passion in your battles."

alder @norm2 "Makes sense. You were battling the people you {i}really{/i} wanted to! Battles between two people who {i}really{/i} want to battle each other will always be the best."

bruno @talking2mouth "Some would say that battles one undertakes out of duty, not preference, are more worthy. If a battle could be described as 'good,' surely a battle between hated foes would be it?"

alder @surprised2 "Hm... yeah, I guess that makes sense, too."
alder @happy2 "Not sure how relevant battles between hated foes are in the year 2004, though."
alder @norm4 "But that brings up a good question. A good battle[ellipses] what would you call a good battle? Any thoughts? Just shout 'em out."

hilbert uniform @closedbrow talking2mouth "A good battle is one where you win."

hilda uniform @closedbrow talking2mouth "{size=30}Oh, for the love of[ellipses]{/size} a good battle is a battle that you {i}enjoy{/i}."

sonia uniform @talkingmouth "A good battle is one that teaches you something new about Pokémon, or strategies, or moves."

flannery uniform @talkingmouth "A good battle is one where you get a bit closer to yourself and your Pokémon, where you learn how you {i}truly{/i} battle together!"

alder @happy2 "Heh. You should all know me enough by now I'm not going to say any one of you is more correct than any other."
alder @spunky2 "Good answers all around. Maybe there's one I like more."

narrator "You notice Alder winks at Flannery, specifically[ellipses]"

alder @happy2 "Alright. Short lecture today, but all this talk about good battles has made me want to see some. Pair up. Only rule is you can't double-dip with the person you picked yesterday."

hide alder
hide bruno 
with dis

call pickgympartner() from _call_pickgympartner_1

python:
    battlechar = _return
    trainer1 = MakeRed()
    trainer2 = MakeTrainer(battlechar)

call Battle([trainer1, trainer2], uniforms = [True, True]) from _call_Battle_188

python:
    renpy.transition(dis)
    renpy.show(GetCharacterSprite(battlechar, 1, True))

$ RecordBattle("Week10TuesdayGym")
if (WonBattle("Week10TuesdayGym")):
    $ ValueChange(battlechar, 3)

    narrator "[battlechar] seems impressed!"

if (CanBunnyRecruit(battlechar)):
    redmind uniform @thinking "Maybe now would be a good time to bring up Saturday's party...?"
    call BunnyRecruit(battlechar, True) from _call_BunnyRecruit_7 

scene gym with dis

jump lunchtransition