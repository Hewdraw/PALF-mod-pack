label gym010408:

$ timeOfDay = "Noon"

  

play music "Audio/Music/Gym_Start.ogg" noloop
queue music "Audio/Music/Gym_Loop.ogg"

$ renpy.transition(dissolve)
show screen currentdate

scene gym with dis

show blank2 behind gym

$ renpy.pause(2.0, hard=True)

hide blank2

show alder spunky2 with dis:
    xpos 0.66

show bruno think with dis:
    xpos 0.33

alder @talkingmouth "And that concludes the lecture!"

pause 2.0

alder norm @norm2 "[first_name]. Might I have your ear for a moment?"

red uniform @surprised "Oh? Uh, yes, of course, Professor."
redmind @thinking "Crap. I hope this isn't about what Lance said..."

if (WonBattle("Blue1") and WonBattle("Cheren1")):
    alder happy2 "You've been winning quite a bit. Against Blue, Cheren... Which is a good thing, of course."
    alder sad @sad2 "But that comes with certain expectations."
elif (not (WonBattle("Blue1") or WonBattle("Cheren1"))):
    alder sad @sad2 "You haven't been doing too well against your classmates so far, and I think Bruno and I have figured out why."

bruno @think2 "Your Pokémon are not improving."

red @surprised "...Huh?"

alder norm @norm2 "Well, it's as he said. That [starter_species_name] of yours has been in a couple battles now, but nothing's changed."

bruno norm @norm2 "You've been very lucky that it's following your commands. I've never seen a Pokémon so well-behaved."

alder @spunky2 "But even the most well-behaved Pokémon is going to struggle against another twice its level!"

$ startergenderpronoun = "him" 
if (playerparty[0].GetGender() == Genders.Female):
    $ startergenderpronoun = "her"
elif (playerparty[0].GetGender() == Genders.Unknown):
    $ startergenderpronoun = "them"
red @closedbrow talking2mouth "Oh. Well... how do I make [startergenderpronoun] stronger, then?"

show bruno surprisedbrow frownmouth
show alder surprisedbrow frownmouth
with dis

show blue uniform at rightside with dis:
    xzoom -1 xpos 0.85

blue @happybrow happymouth "HAH! What kind of idiot doesn't know how to train a Pokémon? You don't deserve to be in this school!"

pause 2.0

show bruno norm with dis

alder angry2 "...Mr. Oak. We don't tolerate that sort of talk in this class. {w=1.0}{nw}"
extend happy @happy2 "Besides, what's Kobukan for if not to teach people how to train Pokémon? Seems Mr. [last_name] here is getting the most bang for his buck!"

pause 1.0

blue closedbrow talkingmouth "Psh, whatever. I'll be over here {i}not{/i} wasting faculty time."

redmind @unamusedbrow unamusedmouth "Kinda feels like if he already knows everything, he's just wasting his own time, then...?"

hide blue at rightside with dis

red @happy "Anyway... training? How do?"

bruno @norm2 "You must criticize your Pokémon."

red @surprised "W-wait, what? Criticize? That's... I mean, [starter_name] is my little buddy. I'm not sure I want to do that..."

alder norm3 @norm4 "Criticize might be a bit of a harsh word, but Bruno's right." 
alder @norm4 "You need to let your Pokémon know when they're doing poorly, and when they're doing well. Otherwise, they'll just keep doing the same thing over and over, and never gain any experience."

red @sadeyes sadeyebrows talking2mouth "But... I mean, I've {i}never{/i} done that before. I mean, I even let my Pikachu back home get on the counter."

alder sad @sad2 "...What's your dream, [first_name] [last_name]?"

red @talking2mouth "Um. To become a Champion. Like you, Sir."

alder happy @happy2 "Well, for your sake, I hope you end up much better than me! But let me tell you something about Pokémon."
alder spunky @spunky2 "They're smart. Real smart, smarter than even the Professors that study them know."

alder norm @norm2 "But they need humans to do anything with those smarts. Human and Pokémon are the perfect pair." 
alder sad @sad2 "One's got power; the other knows how to use it. Er, not that power for power's sake is a good thing, but that's a different lecture."

red @closedbrow talking2mouth "Well... what should I do, then, Sir?"

alder @happy2 "If your Pokémon misses a move, tell 'em why. If they were too slow to react, encourage 'em to speed up. If they don't take your foe seriously, tell them off."
alder norm @angry2 "Don't let your Pokémon give you anything less than what you know they're capable of."

red @closedbrow talking2mouth "How will I know what they're capable of, though?"

alder @norm2 "Some of that you'll just have to study and learn through experience. Otherwise, {color=#0048ff}your type elective classes should give you an idea of what your Pokémon are capable of.{/color}"

bruno norm @norm2 "{color=#0048ff}Your electives will increase the maximum power your Pokémon can attain. Your battles, such as in this gym, will increase their actual power.{/color}"

red @closedbrow talking2mouth "I see... I'm jumping between electives, but if I focus really hard on one elective, could I make my Pokémon super-strong right away?"

bruno think @think2 "No. You'd still need to actually train your Pokémon up through battle." 
alder happy @happy2 "There's not much you can do to speed that up, besides waiting for time to pass. Your classmates will get stronger over time, so they'll be more challenging opponents who reward you more greatly if you try to beat 'em."

red @closedbrow talking2mouth "I see...{nw}" 
extend @confused " Wait, what happens if I train a Pokémon in battle before I've taken enough electives to know what it's capable of?"

bruno norm @norm2 "If you take the elective after, that's fine. You and your Pokémon will both remember the experience--you can make use of it next time you battle."

red @closedbrow talking2mouth "Okay."

bruno think @think2 "One more thing. You will learn more from losing than you learn from winning."
alder happy @happy2 "But... if you want to maintain your classmates' respect, as well as your Pokémon's, don't purposefully take a dive. Your battles in this class aren't graded, but we {i}will{/i} notice if you're losing too much!" 

if (WonBattle("Blue1") and WonBattle("Cheren1")):
    alder @happy2 "Not that that should be a concern for you, if you continue as you are."

alder @happy2 "Anyway, your opponent for today will be this young man! I believe you're acquainted."

show alder spunky2 with dis:
    xpos 0.66 alpha 1.0
    ease 0.75 alpha 0.0

show bruno think with dis:
    xpos 0.33 alpha 1.0
    pause 0.25
    ease 0.75 alpha 0.0

show silver uniform with dis

pause 2.0

red @surprised "Oh." 
red @wince talking2mouth "Hey, Silver."

silver "{w=0.5}.{w=0.5}.{w=0.5}."

red @happyeyes happyeyebrows talkingmouth "Uh... thanks for standing up for me back there."

silver "[ellipses]{nw}"
extend @talkingmouth "Did you mean what you said?"

red @surprised "Huh?"

silver @sad "About getting on the Battle Team. No matter what."

red @talkingmouth "Yeah. It'll happen for me and [pika_name]. And, if you want it, for you, too."

silver "{w=0.5}.{w=0.5}.{w=0.5}."

silver angry "Prove it."

$ HealParty()
$ trainer1 = Trainer("red", TrainerType.Player, playerparty)
$ trainer2 = Trainer("silver", TrainerType.Enemy, [Pokemon(451, gender=Genders.Male, level=3, moves=[GetMove("Poison Sting"), GetMove("Leer"), GetMove("Hone Claws")], ability="Sniper")])#Skorupi

call Battle([trainer1, trainer2], uniforms=[True, True]) from _call_Battle_3
$ battlehistory["Silver1"]  = _return

$ HealParty()

stop music fadeout 1.0

hide alder
hide bruno

pause 1.0

show alder norm at centerside with dis
show bruno think at leftside with dis
show silver uniform at rightside with dis

$ renpy.music.play("Audio/Music/Gym_Loop.ogg", channel='music', loop=True, fadein=1.25, tight=None)
    
$ renpy.transition(dissolve)
show screen currentdate

$ renpy.pause(1.5, hard=True)

hide blank2

if (WonBattle("Silver1")):
    silver @angrymouth closedbrow "Damn it. I let you down, Skorupi. I'm sorry."

    red uniform @happy "That was a good battle! Don't beat yourself up over it."

    silver @sad "...Lance is right.{w=0.5} Power's all that matters in this world."

    red @surprised "What?"

    $ ValueChange("Silver", 3, 0.75)

    silver smilemouth @happy "But power isn't what he thinks it is. Show me more of yours, [first_name]."

else:
    silver "[ellipses]{nw}"
    extend @talkingmouth "That's not good enough. You need to get better if you don't want to let your Pokémon down."

    red uniform @closedeyes talking2mouth "I know. I'm working on it."

    silver @closedbrow talkingmouth "...Yeah. Seeya."

jump lunchtransition