label day010408:
python:
    for mon in playerparty:
        if (mon.GetId() == 25):
            pikachuobj = mon
    playerparty.remove(pikachuobj)
    timeOfDay = "Morning"
call calendar(1) from _call_calendar_3
$ calDate = calDate.replace(day=8, month=4, year=2004)


show morning at vspaz

$ renpy.music.queue("Audio/Music/Oak Class.ogg", channel='music', loop=None, fadein=1.5, tight=None)

show homeroom behind oakbg

$ renpy.transition(dissolve)
show screen currentdate

hide blank2 with splitfade    
hide morning

$ renpy.pause(0.6, hard=True)

redmind uniform @thinking "And now it's straight back to the grind.{w=0.5} If I remember right, Sam said we'd have a quiz today."
redmind "Shouldn't be a problem...{w=0.5} I hope."

Character("Gossiping Student") "\"Hey, isn't that the guy that got chewed out yesterday by Lance?\""
Character("Loud Student") "\"What? No, that guy had red hair. And he looked... stabby.\""
Character("Gossipping Student") "\"Wait, the student with the red hair was a guy? But her hair was real long, wasn't it?\""
Character("Loud Student") "\"I dunno, maybe there were two students yelling at Lance? I wasn't really close enough to hear.\""
Character("Gossiping Student") "\"God, can you imagine yelling at a teacher like that? Some jackasses with more money than sense think they can do anything in this school.\""

pause 1.0

redmind @angrybrow frownmouth "[ellipses]"    
redmind @thinking "...Well, I guess what happened yesterday did happen in front of countless other students, so I can't say I'm too surprised."

menu:
    "{color=#ff8412}[[Courage]{/color} I'd better handle this.":
        redmind @angrybrow frownmouth "...Still, I'd better handle this."

        $ TraitChange("Courage")

        red @closedeyes talking2mouth "You guys, I--"

    "{color=#e226a6}[[Patience]{/color} I'd better stay out of this.":

        $ TraitChange("Patience")

        redmind @angrybrow frownmouth "...I'd better stay out of this."

show whitney uniform angrybrow frownmouth with dis:
    xpos 850
    ease 0.25 alpha 1.0 xpos 650
    
whitney @angrymouth "I'd say you two are the real jackasses here."

show whitney angry with dis:
    alpha 1.0 xpos 650

Character("Gossiping Student") "\"Huh?\""

redmind @surprisedeyes surprisedeyebrows frownmouth "Okay, I guess the decision was made for me."

Character("Loud Student") "\"What did you say?\""

show flannery uniform angry:
    alpha 0.0 xpos 1200
    ease 0.5 alpha 1.0 xpos 1050

flannery "So you turds are deaf, too, huh?{w=0.5}{nw}"

show flannery angry veins with dis:
    alpha 1.0 xpos 1050

extend @talkingmouth " I'm not too surprised, considering anybody with normal hearing would gouge their own ears out after listening to the way you douchebags talk."

Character("Loud Student") "\"W-What's your problem?!\""

show whitney surprisedbrow frownmouth with dis:
    xpos 650
    ease 0.7 xpos 720

whitney @angrymouth "{i}Her{/i} problem?{w=0.5} What's {i}your{/i} problem?"

show whitney angry with dis:
    xpos 720
    ease 0.3 xpos 670

whitney @talking2mouth "You guys barely even know what happened, but you're sucking up to Lance?"

show whitney angry:
    xpos 670

flannery @talking2mouth "You creeps really think a two-time regional Champion needs a couple of twerps like you stepping up to bat for him? Get real!"

whitney @angry "Yeah! You don't even know who was at fault, you just want to seem like you're on the stronger side!"

flannery furiousmouth angrybrow "I really hate dealing with stuff like this so early in the morning so you guys better beat it before I get angry!"

show flannery furious with dis:
    xpos 1050
    ease 0.5 xpos 1000
    
flannery @talking2mouth "Get outta here!{w=0.5} Go on, SCRAM!"

show flannery:
    xpos 1000
    
Character("Loud Student") "\"Tch! This is our classroom, too, you crazy... {w=0.5}{size=30}nevermind.{/size}\""

show whitney -angry with dis

show flannery angrybrow frownmouth with dis:
    xpos 1000
    ease 0.75 xpos 1100

flannery @talking2mouth "Assholes..."

show flannery:
    xpos 1100
    
pause 1.5

redmind @surprisedbrow frownmouth "[ellipses]"

show whitney:
    xpos 670
    ease 0.5 xpos 720

whitney @happy "Oh, hi, [first_name]!{w=0.5}{nw}"

show whitney happybrow with dis:
    xpos 720

extend @talkingmouth " Ready for another jolly, fun-filled day of learning?"

show flannery -veins -angrybrow 
show whitney happy
with dis

red @sigh "I, uh... yeah. Yeah. Hey, Whitney, Flannery.{w=0.5} Thanks for that."
red @happy "I'd like to say I prefer to fight my own battles, but I really appreciate it."

show whitney -happy with dis:
    xpos 720
    pause 0.75
    ease 0.2 xpos 980
    ease 0.25 xpos 820
  
flannery tiredbrow @talking2mouth "I don't know what you're talking ab--{w=0.2}{nw}"

$ PlaySound("Body punch.ogg")

show flannery surprisedbrow frownmouth with dis:
    xpos 1100
    pause 0.25
    ease 0.1 xpos 1150
extend @talkingmouth " {i}oompf! {/i}"

show flannery:
    xpos 1150

whitney @happybrow smilemouth "She meant to say, 'Not a problem, [first_name]!'"
whitney @talking2mouth "Sorry, she gets a little shy sometimes.{w=0.5} Especially when it comes to stuff like this."

flannery -surprisedbrow -frownmouth -surprised frownmouth @angry "I do not!"

whitney @talking2mouth "Anyway, take it easy, hotshot.{w=0.5} Try not to let those insecure idiots get to you."
whitney happy "You live how you want!"
whitney -happy @happybrow smilemouth "Besides, we couldn't let those jerks just badmouth that red-haired girl like that."

flannery @closedbrow talkingmouth "We redheads have to stick together, after all."

redmind @thinking "...Should I tell them that Silver is a guy?"

pause 1.0

redmind @happy "Nah, this is funnier."

show leaf uniform with dis:
    xpos 0
    ease 0.75 xpos 270

leaf @happybrow talkingmouth "Good morning, [first_name]!{w=0.5} And good morning to you, too, Whitney and Flannery!"

whitney @talking2mouth "Good morning, Leaf!"
flannery tiredbrow frownmouth @talking2mouth "No, it isn't."

leaf @happy "You should be getting to your seat, too, [first_name].{w=0.5}{nw}"
extend -happy @talkingmouth " Class is starting soon!"

red @happy "Yeah, I know."

hide leaf with dis
    
pause 1.0

redmind @thinking "I know I haven't spent much time with Whitney before, but I never expected her to be so...{w=0.33} charismatic."

flannery @talking2mouth "Whitney, class is starting."

hide flannery with dis

whitney happy "All right, talk to you later, [first_name]!"

hide whitney with dis

pause 1.5

redmind @sadbrow frownmouth "I gotta say, those two renewed my faith in humanity, at least for a little bit."

$ renpy.music.set_volume(0.0, delay=1.0, channel="music")
$ renpy.transition(dissolve)
call clearscreens from _call_clearscreens_34

$ PlaySound("BellChime.ogg")
$ renpy.music.set_volume(1.0, delay=1.0, channel="music")

show blank2 with Dissolve(1.5)

$ renpy.transition(dissolve)
call clearscreens from _call_clearscreens_35
$ renpy.music.stop(channel='crowd', fadeout=1.5)
stop music fadeout 1.5
$ renpy.pause(2.5, hard=True)

jump PickElective