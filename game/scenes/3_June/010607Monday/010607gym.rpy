label gym010607:

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

alder @happy2 "Good morning, everyone! I'm very glad to be back in class!"

narrator "An audible sigh of relief comes from the crowd as Alder walks through the door, Bruno in tow."

if (not HasEvent("Professor Rowan", "FledBattle")):
    redmind uniform @sadbrow "I guess most of my classmates couldn't take any more Rowan. Frankly, neither could I. It's good to see Instructor Alder again."
else:
    redmind uniform @sadbrow "I guess most of my classmates couldn't take any more Rowan. ...I understand him a bit better now, but I can't deny it's good to see Instructor Alder again."

alder @sadbrow talkingmouth "Judging by the sound of that sigh, I'm guessing I was missed?"

bruno @sadbrow talking2mouth "{size=30}I found myself incapable of lecturing by myself.{/size}"

alder @closedbrow talking2mouth "{size=30}Ah, so you brought in Rowan.{/size}" 
alder @happy2 "Say no more! I get the picture."
alder @winkbrow talkingmouth "Well, if there's one thing I've tried to impart on you in this class, it's that people with very different philosophies to battling, Pokémon, and friendship {i}can{/i} still be friends." 
alder @talkingmouth "Rowan and I might teach you in completely opposite ways--but that doesn't mean I think you can't get anything from his lessons!"
alder @happy2 "And to those of you who are normally in the back, yawning, maybe now you appreciate {i}my{/i} style a bit more!"

pause 1.0

$ PlaySound("Scattered Applause.ogg")

alder @surprised2 "Applause? For a joke that was weak by even {i}my{/i} standards?" 
alder @sadbrow talking2mouth "{size=30}Phew, Rowan did a number on these kids[ellipses]{/size}"

pause 1.0

alder @happy2 "Looks like maybe everyone could do with a little lift to their spirits. How about we bring out the {i}special{/i} lesson plan this week, Bruno?"

pause 1.0

bruno smilemouth @talkingmouth closedbrow "I believe the students would appreciate that."

alder @happy2 "They usually do."
alder @talking2mouth "You've done double, triple, paired, and single battles before. You've had all kinds of battles over the past nine weeks. But the one constant thing is that Bruno and I have assigned your partners."
alder @happy2 "Well, for this week, we're just going to give you up to each other. Pick whoever you want and battle 'em. All that's necessary is that your partner agrees to it--and you do single battles, of course."
alder @closedbrow talking2mouth "Oh, and don't pick the same person twice. You don't get better at battling by battling the same person over and over, you just get better at battling that {i}specific{/i} person."
alder @winkbrow talkingmouth "Have fun!"

hide alder
hide bruno
with dis

pause 2.0

show ethan with dis

ethan uniform @talking2mouth "Dude, can he {i}do{/i} that?"

red uniform @closedbrow talking2mouth "I guess so? I mean, we're still battling. I just... I always thought the way we were partnered up for gym battles was important?"

ethan @sadbrow talkingmouth "Maybe this really {i}is{/i} a break, then."
ethan @happy "And it couldn't have come at a better time! You know what this means--you can ask people about the party after battling them!"

red @talkingmouth "Good idea."

ethan @winkbrow talkingmouth "That's my one for the week. Seeya later."

hide ethan with dis

pause 1.0

narrator "[bluecolor]This week, you can pick whomever you wish (that is available) to battle!{/color}"

call pickgympartner() from _call_pickgympartner

python:
    battlechar = _return
    trainer1 = MakeRed()
    trainer2 = MakeTrainer(battlechar)

call Battle([trainer1, trainer2], uniforms = [True, True]) from _call_Battle_186

python:
    renpy.transition(dis)
    renpy.show(GetCharacterSprite(battlechar, 1, True))

$ RecordBattle("Week10MondayGym")
if (WonBattle("Week10MondayGym")):
    $ ValueChange(battlechar, 3)

    narrator "[battlechar] seems impressed!"

if (CanBunnyRecruit(battlechar)):
    redmind uniform @thinking "Maybe now would be a good time to bring up Saturday's party...?"
    call BunnyRecruit(battlechar, True) from _call_BunnyRecruit_3 

scene gym with dis

jump lunchtransition