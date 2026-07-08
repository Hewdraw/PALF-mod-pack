label gym010611:

play music "Audio/Music/Gym_Start.ogg" noloop
queue music "Audio/Music/Gym_Loop.ogg"

show screen currentdate
scene gym 
with dis

$ renpy.pause(2.0, hard=True)

show alder with dis:
    xpos 0.66

show bruno think with dis:
    xpos 0.33

alder @happy2 "Morning, students!"
alder @norm2 "I guess most of you are still recovering from the battle with Professor Sycamore this morning, huh?"

bruno norm @norm2 "It was quite a spectacle. The power of Mega Evolution is always impressive to witness."
bruno @sadbrow talking2mouth "But it cannot be relied on in every situation. Pure strength does not rely on timers, bonds, or special stones."

alder @spunky2 "Right! Mega Evolution is just one of many ways to battle. It's not the end-all-be-all of being a Trainer."

pause 1.0

alder @surprised2 "Uh... Hilbert?"

redmind uniform @surprisedbrow frownmouth "Woah. Hilbert's raising his hand in {i}{b}other{/b}{/i} classes now, too?"

show hilbert uniform with dis:
    xpos 0.5 xzoom -1

show bruno:
    xpos 0.33
    ease 0.5 xpos 0.25

show alder:
    xpos 0.66
    ease 0.5 xpos 0.75

hilbert @talking2mouth "I'm from Unova, like you. We don't have Dynamax, Terastallization, or Z-Moves. And Mega Evolution is {i}barely{/i} practiced." 
hilbert @sadbrow talking2mouth "The only Unovan Pokémon I know that can Mega Evolve is {i}Audino{/i}."#FIX THIS: When Z-A comes out, presumably. (EDIT: Apparently not! Alright, when Wind/Waves come out?)

whitney uniform @angrybrow talking2mouth "Whatchu sayin' 'bout Audino, Hilbert?!"

bruno @talking2mouth "You believe your lack of familiarity with these techniques places you at a disadvantage?"

hilbert @angrybrow talking2mouth "It {i}does{/i}."

alder @norm3 "[ellipses]"
alder norm3 @norm4 "So, uh, I see your point, but it's not like I can teach you how to Mega Evolve in this classroom. And Kobukan's not built over a Power Spot, either."

hilbert @sadbrow talking2mouth "I[ellipses] I know that, but[ellipses]"

alder norm @spunky2 "But I've got something even better than regional gimmicks for you! Someone write this down, because I'm {i}agreeing{/i} with Bruno!"

bruno @closedbrow talkingmouth "Wonders never cease."

alder @norm4 "It's like he said, pure strength can overcome any of those gimmicks. That's not saying you should shun them or anything--I've even used a couple myself."
alder @norm4 "You're going to want to {i}learn{/i} about them, because even if you don't use them, other people will, and you'll want to know how to counter them."

alder @closedbrow talkingmouth "But you've probably noticed something about trainers who use those techniques, right? If they have a Mega Evolving Pokémon, or a Z-Ring, or a Tera Orb, they'll pretty much always send their Pokémon out last."

hilbert @surprisedbrow frownmouth "[ellipses]"
hilbert @closedbrow talking2mouth "That's[ellipses] true. Why?"

alder @sadbrow talkingmouth "Techniques like that tire Pokémon out. They take time to charge between battles, and the more you use them, the more tired your Pokémon get. And not just the Pokémon! Trainers, too."
alder @norm4 "If a Pokémon has only ever been trained to use those techniques, then they won't be able to fight at full strength without them--but at the same time, trainers are going to want to use them as little as possible."
alder @talking2mouth "So they'll leave their strongest Pokémon--their ace--at the back. And that's pretty much where you want them!"

pause 1.0

hilbert @talking2mouth "I don't follow."

alder @happy2 "Think of it this way. If your opponent only has one Pokémon left, then you know exactly what they're going to do. You know they're going to Mega Evolve, or use a powerful Z-Move, or change their type through Terastallization."
alder @talkingmouth "Build up buffs on the other Pokémon on their team, and then when their ace comes out, you can just sweep it away with a big ol' regular attack. You want to know what's a good counter to Mega Evolution? Three Quiver Dances."
alder @spunky2 "If you know what basket they're putting all their eggs into before the battle, then are they really even using a special technique? Or just a normal Pokémon that's maybe a bit stronger than the others on their team?"
alder @norm4 "Augustine Sycamore is one of the few people I know who is capable of Mega-Evolving multiple Pokémon--so he avoids the predictability of always sending his Mega-Evolver out at the end of the battle."
alder @spunky2 "But he literally wrote the book on Mega Evolution, so that might be a tiny bit above your level!"

if (HasEvent("Blue", "BeatSycamore")):
    blue uniform @talking2mouth "Hah. He wasn't so tough."

hilbert @closedbrow talking2mouth "[ellipses]The raw stats of a Mega-Evolved Pokémon are still higher than a normal Pokémon, even if their presence is predictable."

alder @sadbrow talkingmouth "Well, yeah, but some Pokémon are just stronger than others. That doesn't mean you can't beat them with a little strategy and some good old-fashioned training."
alder @spunky2 "Sure. You bring in a Budew against a Mega Salamence, and you'll probably lose. But if you do, it's not because your opponent had a fancy rock."
alder @sadbrow talkingmouth "And, just between you, me, and the rest of the class, I reckon we Unovans have an even better gimmick: type gems."
alder @spunky2 "Z-Moves might be more flashy, but {i}every{/i} Pokémon can carry a type gem, and you don't need an Alolan bracelet to use 'em, either."

hilbert @closedbrow "[ellipses]"
hilbert @talking2mouth "I understand. Thank you, Champion Alder."

alder @spunky2 "Just Alder, kiddo. But you're welcome."

hide hilbert with dis

show bruno:
    xpos 0.25
    ease 0.5 xpos 0.33

show alder:
    xpos 0.75
    ease 0.5 xpos 0.66

alder @talkingmouth "Alright! Now that we've got that out of the way, does anyone else have any questions about Mega Evolution, Dynamax, or any other fun thing those guys overseas can do?"

may uniform @talkingmouth "Sir!"

alder surprisedbrow frownmouth @happy2 "May?"

may @talkingmouth "Are there any examples of a Pokémon using two of those techniques at once? Could a Pokémon Terastallize and Mega Evolve at the same time, for example?"

stop music fadeout 1.0

pause 1.0

alder sadbrow @talking2mouth "Don't do it. That's all I'll say. Don't do it. It's too much for your Pokémon--and it's too much for you, too."

may @sadbrow talking2mouth "O-oh. {w=0.5}Okay."

pause 1.0

play music "Audio/Music/Gym_Loop.ogg" fadein 2.0

bruno @talking2mouth "Let's start the battles."

alder @closedbrow talkingmouth "Right. {size=30}Thanks, Bruno.{/size}"

hide alder
hide bruno 
with dis

call pickgympartner() from _call_pickgympartner_4

python:
    battlechar = _return
    trainer1 = MakeRed()
    trainer2 = MakeTrainer(battlechar)

call Battle([trainer1, trainer2], uniforms = [True, True]) from _call_Battle_192

python:
    renpy.transition(dis)
    renpy.show(GetCharacterSprite(battlechar, 1, True))

$ RecordBattle("Week10FridayGym")
if (WonBattle("Week10FridayGym")):
    $ ValueChange(battlechar, 3)

    narrator "[battlechar] seems impressed!"

if (CanBunnyRecruit(battlechar)):
    redmind uniform @thinking "Maybe now would be a good time to bring up Saturday's party...?"
    call BunnyRecruit(battlechar, True) from _call_BunnyRecruit_13 

scene gym with dis

jump lunchtransition