############################################################################################################################################################################################################################
# FIRST DAY ON CAMPUS: PLAYER MEETS HALL GUIDE, PROCEEDS TO LOOK FOR POTENTIAL ROOMMATE MATCH, MEETS BLUE, THEN HAS CHOICE OF ROOMMATE BETWEEN BRENDAN, CALEM, CHEREN AND TIERNO.
# PATH DIVERGES UPON SELECTING ROOMMATE, PLAYER SEPARATES FROM ROOMMATE, GETS LOST AND MEETS LEAF, REUNITES WITH ROOMMATE, THEN PROCEEDS TO THE ORIENTATION.
# PLAYER SEES ROXANNE AT ORIENTATION, ALTERNATIVE DIALOGUE DEPENDING ON ROOMMATE, PLAYER RETURNS TO ROOM WITH ROOMMATE AND SELECTS TYPE ELECTIVE CLASSES.

label day010402:    
    $ renpy.pause(1.0, hard=True)
    scene lobby with dissolve

    show falkner uniform with dis
        
    pause 0.5

    falkner @talkingmouth "Hello. Welcome to Relic Hall, one of the three residence halls of this esteemed academy."
    
    hide relichall_A
    hide blank
    
    falkner @closedbrow talking2mouth "Are you here to reserve a dorm? If so, may I have your name? First and last."
    
    red happy "Sure, it's [first_name] [last_name]! And I think I'm here to reserve a dorm. That's what Brawly said to do."
    falkner @closedbrow talkingmouth "Hm. You met Brawly, then."
    red -happy @talkingmouth "You know him?"

    $ BecomeNamed("Falkner")
    
    falkner @talking2mouth "We've met. I'm Falkner, and we work together on the Student Council.{w=0.5} ...Though work may be too strong a word, in his case."

    red closedeyes angryeyebrows talking2mouth "I've been hearing that a lot about Brawly, but he seems great, to me."

    falkner @closedbrow happymouth "I'm sure he appreciates that."
    falkner @talkingmouth "In any case, suites are first-come, first-serve. If you have permission from the school to dorm with someone in particular, let me know. Otherwise, I can assign you a suite."
    falkner @sadbrow talking2mouth "...I can also ensure that you don't dorm with someone you'd rather not spend a year with."

    red happy "If you could make sure I don't dorm with 'Blue Oak,' then I'm good with anyone else!"

    falkner @closedbrow talking2mouth "Very well. You'll be in Dorm... 151. Carry on down this hallway, take a left at the Tranquill Wing's exit and continue diagonally past the skywalk." 
    falkner @talkingmouth "After you drop off your luggage, you may want to head to the lobby. To... 'mingle.'"
    
    red @talkingmouth "Will do.{w=0.5} Thanks!"

    hide falkner with dis

    pause 1.0
    
    redmind @confusedbrow frownmouth "Okay, the way he just said 'mingle' was mega-weird."
    redmind "But whatever, it's time to head to my dorm!"

stop music fadeout 1.5
$ renpy.pause(1.5, hard=True)
scene hall_A2b with Dissolve(1.0)
pause 1.0

show hall_A2:
    xalign 0.0 yalign 1.0 xpos 0 ypos 1080 zoom 0.625
    parallel:
        ease 1.2 xalign 0.0 yalign 1.0 xpos -300 ypos 1120
    parallel:
        ease 1.0 zoom 0.8
        
$ renpy.pause(1.2, hard=True)

show hall_A2:
    xalign 0.0 yalign 1.0 xpos -300 ypos 1120 zoom 0.8
    parallel:
        ease 1.2 xalign 0.0 yalign 1.0 xpos -100 ypos 1200
    parallel:
        ease 1.0 zoom 0.85
        
$ renpy.pause(1.4, hard=True)

show hall_A2:
    xalign 0.0 yalign 1.0 xpos -100 ypos 1200 zoom 0.85
    parallel:
        ease 1.2 xalign 0.0 yalign 1.0 xpos -550 ypos 1300
    parallel:
        ease 1.0 zoom 0.9

$ renpy.pause(1.5, hard=True)

show hall_A2:
    xalign 0.0 yalign 1.0 xpos -550 ypos 1300 zoom 0.9
    ease 1.0 xalign 0.0 yalign 1.0 xpos -480 ypos 1250 zoom 0.85

red @frownmouth "[ellipses]"

red happy "Yep. I'm lost."

redmind closedeyes frownmouth "I guess my lucky streak of running into every single Student Council member had to end eventually."

show hall_A2:
    xalign 0.0 yalign 1.0 xpos -480 ypos 1250 zoom 0.85

redmind "I must've left the area where the dorms are, though. When I was there, there were tons of students around, but now it's just me."
redmind happy "Well. If I just pick a direction and run, then, I bet I'll find my way back to where I was!"
redmind -happy "Just going to tighten my laces, and then..."

pause 1.0

show hall_A2:
    xalign 0.0 xpos -480 ypos 1250 zoom 0.85
    ease 1.5 xpos -530 ypos 1120 zoom 0.8

pause 1.0

redmind sadeyes sadeyebrows frownmouth "Actually... Maybe I should hold off. I don't want to knock a vase over or anything. They look expensive."

show hall_A2:
    xpos -530 ypos 1120 zoom 0.8

Character("{color=#00b23f}???{/color}") "\"{size=30}{i}Hey, skippy. What do you think you're doing?{/i}{/size}\""

show hall_A2 with vpunch:
    xalign 0.0 xpos -530 ypos 1120 zoom 0.8
    ease 0.1 xpos -100 ypos 1100 zoom 0.7

show leaf surprisedbrow frownmouth with dis:
    xpos 0.5

red surprisedbrow frownmouth @surprised "Gah!"

$ renpy.music.queue("Audio/Music/Pallet Town A.ogg", channel='music', loop=True, fadein=1.0, tight=None)

show hall_A2:
    xpos -100 ypos 1100 zoom 0.7

red closedeyes talking2mouth "Geez, talk about heart attacks..."

show leaf -surprisedbrow -frownmouth -surprised frownmouth with dis

red happy "Sorry, you scared the hell out of me! You make a habit of skulking up behind people and whispering in their ears?"

leaf @talking2mouth "{i}I'm{/i} the one skulking?{w=0.5} Do you have {i}any{/i} idea where you are?"

red -happy @talking2mouth "Um..."
red @talking2mouth "Just... just a random set of dorms, right?"

show hall_A2:
    xalign 0.0 xpos -100 ypos 1100
    ease 1.0 xpos 0 ypos 1175
        
show leaf flirt with dis:
    subpixel True
    xpos 0.5 ypos 1.0
    ease 1.0 xpos 0.6 ypos 1.1

red @sad2eyes talking2mouth "Oh, wait, there's something on the sign here..."

show leaf happy with dis
    
red talking2mouth "{cps=12}'Cheer Squad's Changing Rooms'{/cps}{w=0.5}"

pause 1.5

red @closedbrow talking2mouth "Huh. Okay, so, I guess I'm {i}very{/i} lost."

pause 1.0

red closedeyes talking2mouth "Ah, damn it.{w=0.5} You're not going to spread weird rumors about me, are you?"

show hall_A2:
    xalign 0.0 yalign 1.0 xpos 0 ypos 1175
    ease 1.0 xpos -100 ypos 1100
        
show leaf happy:
    subpixel True
    xpos 0.6 ypos 1.1
    ease 1.0 xpos 0.5 ypos 1.0

red sadeyes sadeyebrows @talking2mouth "Seriously, I just wandered up here by accident. It's obvious, right? And it's pretty dumb for the cheer squad to have their changing rooms so far away from the fields."

show leaf happy:
    xpos 0.5 ypos 1080

leaf -happy @talkingmouth "I'm going to be honest, I feel like I'm watching a Growlithe chase its own tail."
leaf @flirtbrow talkingmouth "It's kinda cute."

red @confused "Cute?"

leaf @happybrow talkingmouth "Yeah, I've always thought that a shitty sense of direction was a massive turn-on."

red @sad2eyes angryeyebrows frownmouth "[ellipses]"
red @talkingmouth "Well, great. Glad I could do that for you. Mind pointing me in the right direction, now?"

leaf -happybrow -talkingmouth @talkingmouth "I don't think the brochure's that hard to follow.{w=0.5}{nw}"
leaf @talkingmouth "I don't think the brochure's that hard to follow.{fast} I mean, the design of the dorm's wings are laid out in a grid, so it should be really easy to navigate."
leaf @happy "Here, let me see yours."

show leaf:
    xpos 0.5 ypos 1.0
    ease 1.0 zoom 1.2 ypos 1.1 xpos 0.6

red -angrybrow closedeyes @talkingmouth "I... don't have one of those."
red @talkingmouth "Though, now that you mention it, I vaguely remember some other students carrying around some small leaflets... Damn. Guess I missed the boat on that one."

leaf surprisedbrow sadmouth "You {i}seriously{/i} went all this time without a map?{w=0.5} And then you made it all the way here from the main hall?"

leaf @blush talkingmouth "I have to say, your sense of direction is amazing.{w=0.7} Uh, wait, no it's not.{w=0.5}{nw}"
leaf @happy "I have to say, your sense of direction is amazing. Uh, wait, no it's not.{fast} It's just hopeless!"
    
show leaf happy:
    zoom 1.2 ypos 1.1 xpos 0.6
    ease 1.0 zoom 1.0 xpos 0.5 ypos 1.0

extend -happy @happy " Ha ha ha!"
$ renpy.music.set_volume(1.0, delay=0.0, channel="ctc")
    
red @closedbrow talking2mouth "You're not winning any points with me, personality-wise, right now..."

leaf -fullblush @flirtbrow talkingmouth "Oh, so I'm winning points in other ways? Maybe it's my fashion sense?"

red @sad2eyes angryeyebrows talking2mouth "Sure, let's go with that. Now, are you just going to keep laughing or are you going to point me out of here?"

leaf -flirt @closedbrow talking2mouth "Since you asked so nicely, I'll take you up on that offer."

show leaf:
    xpos 0.5
    ease 0.5 xpos -0.5
        
leaf happy "Ha ha ha! Ha ha ha ha ha!"

red @angrybrow talking2mouth "Hey! You--"

TempCharacter("Female Student") "{gradualsize=20-36}--yeah, she was totally ditching us to go shop--{/gradualsize}"

redmind @closedbrow sweat frownmouth "Ah, great. More. Sounds like I'll have to explain myself to a whole group, now. Maybe if I just keep my head down, I can walk on by."

show leaf surprisedbrow frownmouth blush with dis:
    xpos 0.4
    ease 0.6 xpos 0.5

pause 0.6

show leaf surprisedbrow frownmouth blush:
    xpos 0.5 alpha 1.0
    
show hall_A2:
    xalign 0.0 xpos -100 ypos 1100 zoom 0.7
    ease 2.5 xpos -2000 ypos 2640 zoom 2.0 
show leafintro_A with dis:
    alpha 0.0 xalign 0.5 yalign 0.5 zoom 1.08
    pause 1.5
    ease 1.25 zoom 1.0 alpha 1.0
        
show leaf surprisedbrow frownmouth blush:
    alpha 1.0
    pause 1.5
    ease 1.0 alpha 0.0

red -angrybrow surprised "Gah! Jeez, that's a firm grip."
red closedeyes @talkingmouth "Hey, I appreciate it, but you don't need to bail me out here.{w=0.5} I can just explain to them what happ--"

show leafintro_A:
    alpha 1.0
hide leaf with dis

leaf surprisedbrow frownmouth @surprised "I'm not bailing you out! I'm bailing myself out. I don't want rumors spreading that I'm hanging out with the cheerleader changing room skulker before I've even had my first class!"
red @upeyes talking2mouth "And here I was, briefly having the thought that maybe you were doing something selfless."
red @closedbrow talking2mouth "Thanks for clearing that up for me."

show leafintro_A:
    xalign 0.5 yalign 0.5 zoom 1.0 alpha 1.0

$ PlaySound("GenericDoorOpen.ogg")
leaf @talking2mouth "Oh, stop whining. Just stay here!"

$ PlaySound("GenericDoorClose.ogg")

redmind @thinking "...She just went into the women's restroom."
redmind @confusedbrow frownmouth "[ellipses]"
redmind "This is going to be so dumb."

pause 1.0

$ PlaySound("GenericDoorOpen.ogg")

leaf happy "Okay, hide in here. I'll come get you when the coast is clear."

red @talkingmouth "Didn't think I'd have to point this out to you, but that's the women's room."

$ PlaySound("GenericDoorClose.ogg")
leaf firtbrow talking2mouth "Yeah, I have eyes, too. It's the only room that's not locked in this hallway, so get in before they see us!"

red @confusedbrow talking2mouth "[ellipses]{nw}"
extend @confused "I'm struggling to find the words necessary to explain why this is not going to happen." 

leaf angrybrow talking2mouth "What's your problem? It's just a girls' bathroom, not some kind of private sanctuary! Believe me, you're {i}definitely{/i} not going to defile it with {i}your{/i} male presence."

red angrybrow frownmouth "[ellipses]{nw}"
extend @talking2mouth "Okay, I don't like how you emphasized the 'your' there. I promise you, I'm definitely male."

leaf angrybrow talkingmouth "Really? Because you're being a total girl right now."

red angrybrow talking2mouth "That's sexist."

leaf angry "Just get in the damn bathroom!"

if (profanity):
    menu:
        ">Get in the damn bathroom":        
            red -angrybrow @talkingmouth "Okay, I'll do it. But I'm covering my eyes while I'm in there."
            
            show leafintro_happy with dis
            
            leaf @happy "What a gentleman you are."

            pause 1.0
            
            leaf @talkingmouth "Now, not a peep from you while I'm gone."
            
            $ PlaySound("GenericDoorOpen.ogg")
            
            leaf @flirtbrow talkingmouth "Ladies first."
            
            red @unamusedbrow talking2mouth "Ha.{w=0.5} Ha."
            
        ">Don't get in the damn bathroom":        
            red @closedbrow talking2mouth "Fat chance. I've never been inside of a women's bathroom for eighteen years and I'm not about to start now. {w=0.25}That goes against everything I stand for.{w=0.5} Besides, what if someone else is in there?{w=0.5} Then we'd really be in trouble."
            
            leaf angry "You got memory problems? I {i}just{/i} checked!"

            red @surprisedeyes surprisedeyebrows talking2mouth "Yeah, but... someone could've come in since then. I mean, we've been watching the door, but there's windows on the inside."
            
            show leafintro_mad with dis:
                alpha 1.0

            red @winkeyes sadeyebrows sweat talking2mouth "So someone could've, like... {cps=20}climbed up from outside, and... {cps=15}gone in there..."
            
            leaf @angrysmilemouth angrybrow "[ellipses]"
            leaf @angry "{cps=12}{i}Through the window?!{/i}"
            
            $ PlaySound("GenericDoorOpen.ogg")
            
            red @closedeyes talking2mouth "Yeah, you know what, I can hear it now. I'll just go in."
            
        ">Jump out the damn window":
            $ leafwindowjump = True
            
            red @closedbrow talking2mouth "Fat chance. I've never been inside of a women's bathroom for eighteen years and I'm not about to start now. Anyway, I have a better idea."
            
            leaf surprised "You do? What?"

            red @closedeyes talking2mouth "Okay, we're on the second floor, right? And it's all grass on the ground outside."

            show leafintro_mad with dis

            leaf @angrysmilemouth angrybrow "[ellipses]"

            red -closedeyes -frownmouth @talkingmouth "I should be able to survive a two-story fall if I just go through the window."
            
            leaf @angrysmilemouth angrybrow "[ellipses]"
            leaf @angry "{cps=12}{i}Through the window?!{/i}"
            
            $ PlaySound("GenericDoorOpen.ogg")
            
            red @closedeyes talking2mouth "Yeah, you know what, I can hear it now. I'll just go in."
else:
    menu:
        ">Get in the **** bathroom":        
            red -angrybrow @talkingmouth "Okay, I'll do it. But I'm covering my eyes while I'm in there."
            
            show leafintro_happy with dis
            
            leaf @happy "What a gentleman you are."

            pause 1.0
            
            leaf @talkingmouth "Now, not a peep from you while I'm gone."
            
            $ PlaySound("GenericDoorOpen.ogg")
            
            leaf @flirtbrow talkingmouth "Ladies first."
            
            red @unamusedbrow talking2mouth "Ha.{w=0.5} Ha."
            
        ">Don't get in the **** bathroom":        
            red @closedbrow talking2mouth "Fat chance. I've never been inside of a women's bathroom for eighteen years and I'm not about to start now. {w=0.25}That goes against everything I stand for.{w=0.5} Besides, what if someone else is in there?{w=0.5} Then we'd really be in trouble."
            
            leaf angry "You got memory problems? I {i}just{/i} checked!"

            red @surprisedeyes surprisedeyebrows talking2mouth "Yeah, but... someone could've come in since then. I mean, we've been watching the door, but there's windows on the inside."
            
            show leafintro_mad with dis:
                alpha 1.0

            red @winkeyes sadeyebrows sweat talking2mouth "So someone could've, like... {cps=20}climbed up from outside, and... {cps=15}gone in there..."
            
            leaf @angrysmilemouth angrybrow "[ellipses]"
            leaf @angry "{cps=12}{i}Through the window?!{/i}"
            
            $ PlaySound("GenericDoorOpen.ogg")
            
            red @closedeyes talking2mouth "Yeah, you know what, I can hear it now. I'll just go in."
            
        ">Jump out the **** window":
            $ leafwindowjump = True
            
            red @closedbrow talking2mouth "Fat chance. I've never been inside of a women's bathroom for eighteen years and I'm not about to start now. Anyway, I have a better idea."
            
            leaf surprised "You do? What?"

            red @closedeyes talking2mouth "Okay, we're on the second floor, right? And it's all grass on the ground outside."

            show leafintro_mad with dis

            leaf @angrysmilemouth angrybrow "[ellipses]"

            red -closedeyes -frownmouth @talkingmouth "I should be able to survive a two-story fall if I just go through the window."
            
            leaf @angrysmilemouth angrybrow "[ellipses]"
            leaf @angry "{cps=12}{i}Through the window?!{/i}"
            
            $ PlaySound("GenericDoorOpen.ogg")
            
            red @closedeyes talking2mouth "Yeah, you know what, I can hear it now. I'll just go in."
        
scene bathroom_light with splitfadefast
$ renpy.pause(0.75, hard=True)

hide leafintro_A
hide leafintro_mad
hide leafintro_happy

red night @unamusedbrow talking2mouth "Oh, yeah, shut the lights off, too. That's not creepy at all."

leaf @sarcastic "Just be good and sit there. I'll be right back."

$ PlaySound("GenericDoorClose.ogg")
show bathroom_dark with splitfadefaster

redmind @sadeyes sadeyebrows frownmouth "I really... didn't think this is what Kobukan was going to be like.{w=0.5} Shut up in the women's bathroom,{nw}"
$ PlaySound("fading_footsteps.ogg")
extend @closedbrow sweat frownmouth " and the girl who did it is running away."

pause 1.0

redmind @sad2eyes angryeyebrows frownmouth "I'll give her five minutes to come back, then I'm going through the window."

pause 1.0

$ PlaySound("GenericDoorOpen.ogg")
hide bathroom_dark with splitfadefast

leaf @happy "Okay, come on out."

window hide
hide leaf
    
scene hall_A2 with splitfade:
    xanchor 0.0 zoom 0.7
    
$ renpy.pause(1.0, hard=True)

show leaf with dis

red @talkingmouth "That was fast. What'd you say to them?"
    
leaf @happy "I just told them that I saw a shiny Eevee in the tall grass on the opposite side of the building. That should keep them busy for a while."

red @surprised "That's almost cruel! Even if I was ninety-nine percent sure that you were lying, I'd have to take that chance."

leaf @flirtbrow talking2mouth "I've never seen a group of people turn heel and run so fast before.{w=0.5}{nw}" 
extend @sad " I'll admit, I felt a bit guilty, too."

red @confusedeyebrows frownmouth "[ellipses]"

leaf @talkingmouth "Okay, over it. {w=0.25}Now, before I forget, {w=0.25}here, I took one of the brochures they dropped."

show leaf at getcloser

pause 1.0
    
leaf @happy "If I recall, you really need it."

red @talkingmouth "Thanks, I guess. I'm not sure any of that really needed to be done, but you did it... {w=0.5}{nw}"
extend @sadeyebrows sadeyes talkingmouth "well...?"

leaf @talking2mouth flirtbrow "You'd be a lot cuter if you'd ended that sentence after 'thanks.'"

red @sad2eyes sweat talkingmouth "I'll keep that in mind the next time a girl shoves me into the women's bathroom to preserve her reputation from high-school level rumors."

show leaf at getfurther

leaf closedbrow happymouth "You'll thank me. Trust me, I know {i}all{/i} about navigating social intrigue." 
leaf -happymouth @talking2mouth "But you know, despite everything that happened, it was...{w=0.6} kind of.{w=0.25}.{w=0.25}."

$ renpy.pause(2.0, hard=True)

leaf sadbrow blush -frownmouth @talkingmouth "...a lot of fun.{w=0.5} Probably the most fun I've had in a while."
leaf -sadbrow @happy "Let's do this again sometime!"

show leaf:
    alpha 1.0 ypos 1.0 zoom 1.0

red @closedeyes talkingmouth "I'm going to do my best to avoid that, but if I can't... {w=0.5}{nw}"
extend @happy "sure."

show leaf happy with dis:
    xpos 0.5 zoom 1.0 ypos 1.0
    ease 1.5 xpos 1.0 zoom 1.35 ypos 1.5

pause 2.0

hide leaf
hide leafintro_A

redmind "...She seemed nice."

window hide
$ renpy.pause(1.5, hard=True)

redmind @wince frownmouth "Oh. I forgot to ask her name."

window hide
stop music fadeout 2.5

scene blank2 with Dissolve(1.5)
$ renpy.pause(1.5, hard=True)

queue music "Audio/Music/SoaringIllusions_Intro.ogg" noloop
queue music "Audio/Music/SoaringIllusions.ogg"

show dorm_empty_A with Dissolve(1.0):
    zoom 1.0 xpos 0 ypos 0 xanchor 0 yanchor 0
    ease 4.0 zoom 1.18 xpos -170 ypos -180

$ PlaySound("Door_Open1.ogg")

redmind @thinking "Huh. So this is my room."

pause 1.0

redmind @thinking "For the next year..."

pause 1.0

redmind @thonk "Hm, wasn't this meant to be a suite? I don't see anyone else's stuff here, though, even though there are four more beds."

$ PlaySound("Chime.ogg")

TempCharacter("{color=#a2254b}Roxanne's Voice{/color}") "Attention, new students. The time is now 2:00 p.m. There will be an orientation taking place in the auditorium of Relic Hall starting in one hour. All new students are advised to attend."

redmind thinking "Maybe I'm just the first of my dormmates to get here? They're cutting it a bit close, though."

$ PlaySound("Door_Open1.ogg")

pause 1.0

show dorm_empty_A:
    zoom 1.18 xpos -170 ypos -180 xanchor 0 yanchor 0
    ease 0.4 zoom 1.0 xpos 0 ypos 0

TempCharacter("{color=#c1861e}Young Voice{/color}") "{gradualsize=20-36}...cutting it a bit close, though.{/gradualsize}"

show ethan with dis:
    xpos 1.5
    ease 1.0 xpos 0.5

show red happy at Transform(xpos=0.08, yanchor=0.35)
show ethan happybrow talkingmouth with dis
Character("{color=#cf0000}[first_name]{/color} & {color=#c1861e}???{/color}") "\"Oh, hey!\""

show ethan surprisedbrow frownmouth -talkingmouth with dis
show red surprisedbrow frownmouth with dis

red @thinking "[ellipses]"
ethan @thinking "[ellipses]"

show red talkingmouth with dis
show ethan talkingmouth -surprisedbrow -frownmouth -surprised with dis
Character("{color=#cf0000}[first_name]{/color} & {color=#c1861e}???{/color}") "\"Do you want to talk first?\""

show ethan happybrow talkingmouth with dis
show red happybrow talkingmouth with dis
Character("{color=#cf0000}[first_name]{/color} & {color=#c1861e}???{/color}") "\"Hey, sorry about this, it's so weird.\""

show ethan angrybrow talking2mouth with dis
show red angrybrow talking2mouth with dis
Character("{color=#cf0000}[first_name]{/color} & {color=#c1861e}???{/color}") "\"Here, go ahead.\""

show ethan surprisedbrow frownmouth with dis
show red surprisedbrow frownmouth with dis
Character("{color=#cf0000}[first_name]{/color} & {color=#c1861e}???{/color}") "\"...\""

show ethan angrybrow surprisedmouth with dis
show red angrybrow surprisedmouth with dis
Character("{color=#cf0000}[first_name]{/color} & {color=#c1861e}???{/color}") "\"Oogabooga!\""

pause 1.0

hide red at Transform(xpos=0.08, yanchor=0.35) with dis

pause 1.0

hide red

ethan -angrybrow -surprisedmouth @happy "Ethan."

red @talkingmouth sadbrow "Oh, thank god, we broke the curse. Who's Ethan?"

$ BecomeNamed("Ethan")

ethan @talkingmouth "I am. Looks like I'm one of your dormmates, too."

red @talkingmouth "Cool. Nice to meet you. My name's [first_name] [last_name]."

ethan @talkingmouth "So, hey, what's your story?"

red @talkingmouth "Well, I'm from Pallet Town in Kanto. {w=0.5}...That's pretty much it."

ethan @talking2mouth "Pallet? Oh, I know that place! That's where Professor Oak lives, right? I went to his lab once on a field trip. I'm from New Bark Town in Johto."

red @surprised "...Sorry, Professor Oak? You mean Sam?"

ethan @confusedeyebrows talking2mouth "You're kidding, right? Yeah, sure, maybe he's a bit old, but he's a world-famous Pokémon researcher. He's a bit more than 'Sam.'"

red @talkingmouth "Huh."
red -surprisedbrow -frownmouth -surprised @sadbrow talkingmouth "To me, he was just my neighbor."

ethan @talkingmouth "Wow, you lived next to him? Wait..."
ethan @surprised "Shit, I remember you! You nearly ran our teacher over while we were walking through the center of town!"

red @happy "I don't remember that, but that sounds like me, alright!"

ethan @happy "Huh. Small world."

show ethan -surprisedbrow -frownmouth -surprised with dis

red @talkingmouth "Looks like we arrived at pretty much the same time. You want to grab these two beds? We can unpack our stuff now."

ethan @talking2mouth "Sure! Wondering who the other three'll be, though."

red @confused "Hopefully we don't go through the whole talking-at-the-same-time routine with the other three as well."
red @happy "With all five of us talking at once, we'd blow the ears out of a Loudred."

ethan @happy "Haha, yeah."

pause 1.0

ethan @sadbrow happymouth "A what?"

show ethan surprisedbrow frownmouth with dis

red @talkingmouth "Oh, it's a Pokémon from Hoenn. Normal-type. Has two big ears that can both receive and emit sound. Most of them are completely immune to sound-based attacks."

ethan @surprised "Dude... you just know that?"

red @sadeyes sadeyebrows talkingmouth "Well... yeah. I've studied a bit."

ethan -surprisedbrow -frownmouth @happy "Pretty impressive, [first_name]. I think I know who I'm going to want to have as a study partner."

red @happy "Well, let's handle that after we finish setting up our room."

$ PlaySound("Door_Open1.ogg")

show ethan surprisedbrow frownmouth with dis

pause 1.0

show calem with dis:
    xpos 1.5 xzoom -1
    ease 1.0 xpos 0.66

show ethan: 
    xpos 0.5
    ease 1.0 xpos 0.33

calem @talkingmouth "Yes, this looks like the right spot."

$ BecomeNamed("Calem")

calem @talking2mouth "A pleasure. My name is Calem. What's yours?"

ethan -surprisedbrow -frownmouth @happy "Hey, Calem! I'm Ethan, and this guy here is [first_name]."

red @talkingmouth "Nice to meet you!"

calem @happymouth "Likewise. Getting to my dorm was one of my top priorities, but it looks like I was a bit late."

ethan @talkingmouth "Don't worry about it, [first_name] and I were just about to unpack."
ethan @playfulbrow talkingmouth "Hey, is that a Kalosian accent?"

calem @closedbrow talkingmouth "Yes, that's right. I'm from Vaniville Town, in the Southeast of Kalos."
ethan @happy "Man, you probably get mad luck with the ladies, then! I know they go crazy for a sexy Kalosian accent."

show ethan surprisedbrow frownmouth with dis

calem @angrybrow talking2mouth "One may be surprised. I've been told that I'm given to pretention."

pause 1.0

ethan -surprisedbrow -frownmouth -surprised @confused "Dude. 'Given to pretention'...?"

calem smilemouth @closedbrow talking2mouth "Yes, I suppose that's a self-demonstrating flaw."

pause 1.0

red @talkingmouth "Well, do you have any preferences where you bed down?"

calem -closedbrow @talking2mouth "I prefer not to sleep too close to any other men. I'll take that fifth bed off to the side."

ethan @talkingmouth "Cool. Let's just get our stuff unpacked, then--"

$ PlaySound("Door_Open1.ogg")

ethan @surprisedbrow talking2mouth "Oh, a new challenger?"

show ethan surprisedbrow frownmouth
show calem surprisedbrow frownmouth
with dis

show hilbert with dis:
    xpos 1.5
    ease 1.0 xpos 0.75

show calem:
    xpos 0.66 xzoom -1
    ease 1.0 xpos 0.5 xzoom 1

show ethan: 
    xpos 0.33
    ease 1.0 xpos 0.25

pause 2.0

hilbert @angrybrow talkingmouth "Well? What are you staring for?"

show calem:
    xpos 0.5 xzoom 1

calem -surprisedbrow -frownmouth @closedbrow talking2mouth "I'm assuming by the way you walked in here you're one of our dormmates, yes? Your first priority, then, should be giving us your name."

ethan -surprisedbrow -frownmouth @happy "Yeah, I'm Ethan, this guy's [first_name], and this dude's Calamari!"

calem @sadbrow talkingmouth "{size=30}Calem, actually.{/size}"

show calem angrybrow
show ethan angry
with dis

hilbert @sadbrow talkingmouth "...I don't remember asking. And I definitely don't care."

show hilbert:
    xpos 0.75
    linear 1.0 xpos 0.375

pause 1.0

show dorm_empty_A at vpunch

show calem surprisedbrow frownmouth with dis
show ethan surprisedbrow frownmouth with dis
show hilbert angrybrow with dis
red angry "Tell us your name, or we're calling you 'Edgelord' for the next year."

pause 1.0 

hilbert @thinking "[ellipses]"

red frownmouth "[ellipses]"

TempCharacter("{color=#353535}Edgelord{/color}") "[ellipses]"

red @thinking "[ellipses]"

$ BecomeNamed("Hilbert")

hilbert @closedbrow talkingmouth "...Hilbert."
hilbert @sadbrow talkingmouth "And I'm taking the bed over there."

show hilbert:
    xpos 0.375
    ease 1.0 xpos -0.5

pause 1.0

show ethan -surprisedbrow -frownmouth -surprised with dis

calem -surprisedbrow -frownmouth -surprised smilemouth @closedbrow talkingmouth "{size=30}That was going to be my bed... {/size}Well, whatever. Nicely handled, [first_name]."

ethan @happy "Yeah, that was pretty cool!"
ethan @sad "...I guess we're spending the next year with Hindenburg, then, huh..."

calem @closedbrow talking2mouth "{size=30}Fairly certain it was 'Hilbert.'{/size}"
calem @talkingmouth sadbrow "Anyway, with a school as prestigious as this, I can understand if someone isn't in a particular mood to forge friendships."
calem @talking2mouth angrybrow "The competitive nature of our environment is absolutely no excuse for poor manners, though."

ethan @happy "Right? It's like, okay dude, we get that you were the toughest guy in your high school. You can chill out."

red @wince talking2mouth "Well, hopefully whoever our last dormmate is is... not like that."

pause 1.0

$ PlaySound("Door_Open1.ogg")

pause 1.0

calem angrybrow -smilemouth @surprisedbrow talkingmouth "{i}En parlant du loup...{/i}"

ethan @happy "You said it, Calamari!"

pause 1.0

calem -angrybrow @happybrow talkingmouth "Calem, Ethan. It's Calem."

show brendan happy with dis:
    xpos 1.5
    ease 1.0 xpos 0.75

brendan @happy "Hey, dudes!"

$ BecomeNamed("Brendan")

brendan -happy @talking2mouth "Brendan's the name and Pokémon's my game! What's goin' on?"

show calem angrybrow with dis

ethan happy "Now that's more like it! Hey, Brendan! I'm Ethan, this guy's [first_name], Mr. Sexy Accent is Calamari, and short, dark and brooding over there is Hildegard."

pause 2.0

calem sadbrow @angry "Why do we continually allow Ethan to introduce us? And why does he only get your name right?"

show ethan -happy with dis

red @happy sweat "Yeah, uh, this guy's Calem, and that guy's Hilbert. Nice to meet ya, Brendan!"

show brendan at getcloser, rightside
show ethan surprisedbrow frownmouth with dis
show calem surprisedbrow with dis

brendan surprisedbrow frownmouth @surprised "Bro! You and I, we're kindred spirits. I can tell!"

red @confused "Oh yeah...?"

brendan -surprisedbrow -frownmouth -surprised @happy "Your thighs, man! They're hella toned. You run a lot, right?"

show calem closedbrow smilemouth with dis
show ethan -surprisedbrow -frownmouth with dis

red @happy "Oh. Uh, yeah. All the time, actually. Once a day, if I can."

show brendan -surprisedbrow -frownmouth at getfurther, rightside with dis

brendan @talkingmouth "Sick. You and I, we'll run together, then. You can make sure I don't skip leg day."
red @talkingmouth "That's quite a responsibility, but I'll do what I can."
ethan @happy "Guys, you see what this means? All five of us are here now! The five roommates that'll spend the next year together! Isn't that incredible?"
calem @happybrow talkingmouth "It certainly does seem like the start of something rather excellent. I look forward to learning about, and perhaps even befriending, all of you."
brendan @happy "Likewise, guys! Hey, if any of you need any help with anything, or you want to work out, you just let me know. Brendan's here for friendin'!"

show brendan angrybrow frownmouth with dis
show calem closedbrow -smilemouth with dis
show ethan angrybrow frownmouth with dis

show brendan:
    xpos 0.75
    ease 1.0 xpos 0.8

show hilbert sadbrow with dis:
    xpos -0.5
    ease 1.0 xpos 0.2

show calem:
    xpos 0.5 xzoom 1
    ease 1.0 xpos 0.6 xzoom -1

show ethan: 
    xpos 0.25
    ease 1.0 xpos 0.4

stop music fadeout 1.0

hilbert @sadbrow talkingmouth "...Pathetic."

show brendan:
    xpos 0.8

show hilbert sadbrow with dis:
    xpos 0.2

show calem:
    xpos 0.6 xzoom -1

show ethan: 
    xpos 0.4

$ renpy.music.queue("Audio/Music/Littleroot_Start.ogg", channel='music', loop=False, fadein=1.0, tight=None)
$ renpy.music.queue("Audio/Music/Littleroot_Loop.ogg", channel='music', loop=True, fadein=0.0, tight=None)

ethan @angry "What the hell's your problem, man?"

show hilbert:
    xzoom 1 xpos 0.2
    ease 0.5 xzoom -1 xpos 0.2

hilbert @angrybrow talkingmouth "You're all talking about friendship and camaraderie, and {i}working together{/i}. Don't you realize what this school is going to put you through?"

show hilbert:
    xzoom -1 xpos 0.2

calem @closedbrow talkingmouth "Whatever it puts us through, handling it with allies is certainly a better strategy than going it alone."

hilbert @talkingmouth "You have to go it alone. [first_name]. I can tell from your eyes you know what I'm talking about. Explain it to them."

red @angrybrow frownmouth "[ellipses]"

ethan @surprised "Wait, [first_name]? Do you know what he's talking about?"

red -angrybrow @sadeyes talking2mouth "...Kobukan Academy has an enforced 80%% graduation rate. The students in the bottom 20%% aren't permitted to graduate. You're allowed to try again, but..."

show brendan surprisedbrow frownmouth with dis

red @closedeyes talking2mouth "...But you aren't eligibile for financial aid if you ever failed to graduate, so in practice, if you don't graduate once, you never will, unless you're ridiculously wealthy."
calem @sad "This is possible only due to Kobukan's unique one-year curriculum. If Kobukan were a standard three-year program, then students would spend far more time and money before being told they're not permitted to graduate."

show ethan sadbrow frownmouth
show calem sadbrow
show brendan sadbrow frownmouth
with dis

pause 2.0

hilbert @angrybrow talkingmouth "See what I'm saying? One out of every five students won't graduate. There's five of us here."
hilbert angry "Do the math."

show hilbert:
    ease 1.0 xpos 1.5

pause 0.9

$ PlaySound("Door_Slam.ogg")

pause 1.0

show calem -sadbrow -frownmouth with dis
show brendan -sadbrow -frownmouth with dis

ethan@ happy "W-well, uh, let's all do so well that Himbo's the one who gets kicked out instead of any of us!"

red @happy "That's the spirit, Ethan!"

ethan @happy "Yeah!"
ethan @thinking "[ellipses]"
ethan @sadbrow talkingmouth "Okay, I'll be real with you guys, I {i}did not know{/i} that, and I'm kinda freaking out about it."

calem @talkingmouth "We should certainly be aware of our odds, but there is little a clear mind and a defined set of priorities cannot solve."

brendan @angrybrow happymouth "Yeah! I didn't sign all those papers and do all those tests just to get scared off by previous years' stats! Heck, maybe we'll be so good that this year, they'll decide to bin the 80 percent acceptance rate thing!"

red @happy "Heck yeah. Don't worry. I may have just met you, Ethan, but I bet that you'll graduate just as easily as any of us. And near the end of the year, when Hilbert begs us to help him study, maybe we'll be gracious and say yes."

stop music fadeout 1.0

ethan -frownmouth @sadbrow talkingmouth "Alright..."

queue music "Audio/Music/SoaringIllusions_Intro.ogg" noloop
queue music "Audio/Music/SoaringIllusions.ogg"

ethan happy "Alright! I'm not giving up yet! Not before things have even begun!"

show calem happy with dis
show brendan happy with dis

red @talkingmouth "Right on."

$ renpy.music.set_volume(0.3, delay=3.0, channel="music")

show flashback with Dissolve(2.0)

redmind @thinking "I knew those stats before, but... even though I somehow got in, I'm still in the bottom tenth percentile."
redmind @thinking "If I want to make it through the year, I'm going to need to work harder than I ever have before..."
redmind @happy "But that's fine! I'm going to be a Champion someday, and I always knew I'd have to work insanely hard to make that happen. Might as well start now!"

$ renpy.music.set_volume(1.0, delay=1.0, channel="music")

hide flashback
show ethan -happy
show brendan -happy
show calem -happy 
with dis

calem @closedbrow talkingmouth "I originally planned on unpacking before the orientation, but we're running a bit short on time. Perhaps we should attend orientation, then come back?"

ethan @talkingmouth "Sure, sounds like a plan."

stop music fadeout 1.0
$ renpy.pause(1.25, hard=True)

queue music "Audio/Music/Kalos_Start.ogg" noloop
queue music "Audio/Music/Kalos_Loop.ogg"

scene orientation with dissolve
$ renpy.pause(1.0, hard=True)

$ renpy.music.play("Audio/school_crowd.ogg", channel='crowd', loop=True, fadein=1.0)

red surprisedbrow frownmouth @surprised "Wow. It's impressive how many students are crammed in here."

show calem with dis

calem @closedbrow talking2mouth "One has to wonder how many students this school would have if it were a standard three-year academy. Seems as though it has its hands full, as-is."

red -surprisedbrow -frownmouth -surprised @talkingmouth "You don't seem fazed."
calem @talking2mouth "I do my best not to. I assure you, though, I'm quite impressed. But I have spent quite some time in Lumiose City, which exceeds even Inspira in size."

pause 1.0

show brendan sadbrow frownmouth at rightside with dis

brendan @talking2mouth "Huh... I don't see her."

show ethan at leftside with dis

ethan @talkingmouth "Who ya looking for, Brendan?"

calem @angry "{size=30}Well, at least he's not only getting {i}my{/i} name wrong.{/size}"

brendan @talking2mouth "My girlfriend. She said she'd meet up with me during orientation."

show calem surprisedbrow with dis

ethan @surprised "Damn, dude! You have a girlfriend here already?!"

show calem closedbrow smilemouth with dis

brendan -sadbrow -frownmouth @happy "Oh, nah, dude, you got it wrong. She's my friend from childhood. We enrolled here together."

ethan @sweat happy "Ohhhhh, okay. I was going to say, man, that's scary fast."

brendan @happy sweat "Hah, it would be, wouldn't it? {w=0.5}{nw}"
extend @surprised "Oh, wait, there she is!"

show calem:
    xpos 0.5 xzoom 1
    ease 1.0 xpos 0.8 xzoom -1

show ethan:
    xpos 0.25
    ease 1.0 xpos 0.6

show brendan:
    xpos 0.75
    ease 1.0 xpos 0.4

show may happy with dis:
    xpos -0.5
    ease 1.0 xpos 0.2

may happybrow @happy "Hey, sweetheart!"

show calem:
    xpos 0.8 xzoom -1

show brendan:
    xpos 0.4

show may:
    xpos 0.2

show ethan at getcloser:
    xpos 0.6

ethan surprisedbrow frownmouth @surprised "{size=30}Holy shit, she's so cute!{/size}"
red @sad2eyes angryeyebrows talking2mouth "{size=30}Yeah, and she's our dormmate's girlfriend, so keep it in your pants.{/size}"
ethan -surprisedbrow -frownmouth @sadbrow talkingmouth "{size=30}Er... of course, hah hah...{/size}"

show ethan at getfurther:
    xpos 0.6

$ BecomeNamed("May")

brendan @talking2mouth "Guys, this is my girlfriend, May. We grew up in Littleroot Town together."

ethan @talkingmouth "Oh, I know that place. That's where Professor Birch lives. Hoenn, right?"

may -happybrow @happy "Oh, you know about it? Yep, that's right!"

brendan @surprisedbrow talking2mouth "Huh, you know about May's old man?"

ethan @surprised "Old man...? Wait, you mean...!"

may @sadbrow talkingmouth "Yep! May Birch is my full name."

ethan @closedbrow talking2mouth sweat "Huh. [first_name] knows Professor Oak, Brendan knows Professor Birch, I know Professor Elm..."

calem @closedbrow talking2mouth "...It might be worth mentioning that I worked as Professor Sycamore's intern for a couple years."

ethan @confused "What the heck...?{w=0.5} So we all, except for Hickey, have a personal connection with a prominent Professor from our region?"

brendan @closedbrow talkingmouth "I mean, we don't know whether he does or not. Probably wouldn't tell us, anyway."

may @sadbrow talkingmouth "What're you talking about?"

calem @thinking "[ellipses]"

brendan @closedbrow talkingmouth "I wonder if...{w=0.5} nah, it's nothing."
brendan @talking2mouth "Anyway, babe, how's your suite? You got some dudes as cool as the guys I ended up with?"

may @angrybrow happymouth "Well, they're a bit less dude-ish, but yeah, I think they're some pretty cool people!"

calem @talkingmouth "I would have preferred if we could pick our roommates directly, but at least things largely seemed to turn out well."

may -angrybrow @happy "Oh, I just love the randomness of it! Even if we could pick, I would've gone random, just to see who I ended up with."

brendan @happy "Yeah, May always loved leaving things up to chance! Heck, the first time I asked her out, she decided whether or not to accept on a coinflip!"

may @sadbrow talkingmouth "...I wouldn't mind if you stopped telling people that..."

calem @surprised "!"

calem @talkingmouth "Oh, look up at the stage. I believe the speaker's about to start. We should find some seats."

redmind @thinking "Hm. He saw that moment of awkwardness and immediately changed the subject. Pretty slick."

ethan @talkingmouth "Yeah, let's go."

stop music

$ PlaySound("Mic_Feedback.ogg")
$ renpy.music.stop(channel='crowd', fadeout=0.5)

show orientation:
    parallel:
        xalign 0.0
        ease 0.02 xpos -30
        ease 0.02 xpos 30
        ease 0.02 xpos 0
        repeat 40
    parallel:
        yalign 0.0
        ease 0.02 ypos -15
        ease 0.02 ypos 15
        ease 0.02 ypos 0
        repeat 40

show calem surprisedmouth deadbrow at monochrome:
    parallel:
        xpos 0.8
        ease 0.02 xpos 0.85
        ease 0.02 xpos 0.75
        ease 0.02 xpos 0.8
        repeat 40
    parallel:
        yalign -0.11
        ease 0.02 ypos 25
        ease 0.02 ypos -25
        ease 0.02 ypos 0
        repeat 40
    
show brendan surprisedmouth deadbrow at monochrome:
    parallel:
        xpos 0.4
        ease 0.02 xpos 0.45
        ease 0.02 xpos 0.35
        ease 0.02 xpos 0.4
        repeat 40
    parallel:
        yalign -0.11
        ease 0.02 ypos 25
        ease 0.02 ypos -25
        ease 0.02 ypos 0
        repeat 40

show may surprisedmouth deadbrow at monochrome:
    parallel:
        xpos 0.2
        ease 0.02 xpos 0.25
        ease 0.02 xpos 0.15
        ease 0.02 xpos 0.2
        repeat 40
    parallel:
        yalign -0.11
        ease 0.02 ypos 25
        ease 0.02 ypos -25
        ease 0.02 ypos 0
        repeat 40

show ethan surprisedmouth deadeyes surprisedeyebrows at monochrome:
    parallel:
        xpos 0.6
        ease 0.02 xpos 0.65
        ease 0.02 xpos 0.55
        ease 0.02 xpos 0.6
        repeat 40
    parallel:
        yalign -0.11
        ease 0.02 ypos 25
        ease 0.02 ypos -25
        ease 0.02 ypos 0
        repeat 40

show red:
    xpos -0.5

red @talkingmouth "{cps=0}Oh, GOD. {size=44}WHY?{w=0.5} HOLY CRAP.{/size}{/cps} This noise! {cps=120}It's like a thousand Pokémon got together and used Screech and Supersonic at the same time!{w=0.5} I can't tell if I'm screaming from the pain or if it's still the feedback!{/cps}"

window hide

show calem at monochrome:
    xpos 0.8 ypos 1.0
    ease 0.5 xpos 0.78 ypos 1.1 rotate -10.0
show ethan at monochrome:
    xpos 0.6 ypos 1.0
    ease 0.5 xpos 0.62 ypos 1.1 rotate 10.0
show brendan at monochrome:
    xpos 0.4 ypos 1.0
    ease 0.5 xpos 0.38 ypos 1.1 rotate -10.0
show may at monochrome:
    xpos 0.2 ypos 1.0
    ease 0.5 xpos 0.22 ypos 1.1 rotate 10.0
$ renpy.pause(0.5, hard=True)
show calem at monochrome:
    xpos 0.78 ypos 1.1 rotate -10.0
    ease 0.5 xpos 0.8 ypos 1.2 rotate 10.0
show ethan at monochrome:
    xpos 0.62 ypos 1.1 rotate 10.0
    ease 0.5 xpos 0.6 ypos 1.2 rotate -10.0
show brendan at monochrome:
    xpos 0.38 ypos 1.1 rotate -10.0
    ease 0.5 xpos 0.4 ypos 1.2 rotate 10.0
show may at monochrome:
    xpos 0.22 ypos 1.1 rotate 10.0
    ease 0.5 xpos 0.2 ypos 1.2 rotate -10.0
$ renpy.pause(1.0, hard=True)
hide calem
hide ethan
hide brendan
hide may
with moveoutbottom
show orientation at vpunch

hide red
$ PlaySound("Thud2.ogg")
$ PlaySound("Thud.ogg")
$ renpy.pause(0.5, hard=True)

$ PlaySound("Complaining.ogg")
    
red @wince talking2mouth "What kind of terrible speaker makes a sound like that?!"

$ PlaySound("Mic_Feedback2.ogg")

roxanne uniform @angry "--telling you this stupid thing won't work!"    
roxanne @surprised ".{w=0.25}.{w=0.25}.{w=0.5}{nw}"

queue music "Audio/Music/Kalos_Start.ogg" noloop
queue music "Audio/Music/Kalos_Loop.ogg"

roxanne @happy "...{fast}Oh, there we go!"

redmind -angrybrow @closedbrow frownmouth "I don't think she's aware half the people in this room are still brain dead on the floor after that uproar..."
redmind @wince frownmouth "If my ears had eyes, they'd be crying."
    
wally @sadbrow surprised2mouth sweat "Ah... my ears...{w=0.5} What was that? Some kind of hazing ritual?!"

grusha @wince "{i}Tranquilo, tranquilízate.{/i} Take deep breaths. It's fine. {size=30}It's fine.{/size}"
    
show flannery furious veins:
    xpos 0.5 ypos 1.6
    ease 0.25 xpos 0.5 ypos 1.0

show whitney surprisedbrow sadmouth:
    xpos 0.75 ypos 1.6 rotate -15.0
    pause 0.75
    ease 0.25 xpos 0.65 ypos 1.0 rotate -15.0

flannery "{size=45}I'LL KILL YOU!{/size}{w=0.75}{nw}"

$ BecomeNamed("Flannery")

whitney "Flannery!{nw}"

show flannery angry with dis:
    subpixel True
    xpos 0.5
    ease 0.5 xpos 0.4

show whitney:
    subpixel True
    xpos 0.65 rotate -15.0
    ease 0.5 xpos 0.55 rotate -15.0
    
extend @talkingmouth " Not here!{w=1.5}{nw}"

show flannery:
    subpixel True
    xpos 0.4
    ease 0.7 xpos 0.3
        
show whitney thinking with dis:
    subpixel True
    xpos 0.55 rotate -15.0
    ease 0.7 xpos 0.45 rotate -15.0

whitney @talking2mouth "Unf!{w=1.0}{nw}"

show flannery:
    subpixel True
    xpos 0.3
    ease 0.5 xpos 0.2
        
show whitney surprisedbrow sadmouth with dis:
    subpixel True
    xpos 0.45 rotate -15.0
    ease 0.5 xpos 0.35 rotate -15.0
    
whitney @talking2mouth "You need to lay off the Lava Cookies, girl!"

show flannery:
    subpixel True
    xpos 0.2 
    ease 0.8 xpos -0.3
        
show whitney thinking with dis:
    subpixel True
    xpos 0.35 rotate -15.0
    ease 0.8 xpos -0.15 rotate -15.0
        
show hilbert with dis:
    xpos 1540
    ease 0.5 xpos 1540
    
pause 0.5

hide flannery
hide whitney

hilbert @talkingmouth ".{w=0.25}.{w=0.25}.{w=0.6}{nw}"

show hilbert angry

extend @talkingmouth "Try that again."

hide hilbert angry
with moveoutright

show sabrina:
    xpos 0.5 ypos 1.8
    ease 1.5 xpos 0.75 ypos 1.0

pause 2.5 

sabrina neutralpowered poweredbrow "[ellipses]"

show sabrina neutralpowered poweredbrow:
    xpos 0.75 alpha 1.0
    ease 1.5 xpos 1.5 alpha 0.0

$ renpy.pause(1.75, hard=True)

show orientation
with vpunch

hide sabrina

roxanne @angry "{size=44}Come on now, we're on a schedule! GET MOVING!{/size}"

red @talking2mouth "Eeesh. I only met Roxanne for a moment, but I'm not exactly... endeared by her, right now."

show ethan sad:
    ypos 2.0 xpos 0.5 rotate 10.0
    ease 2.0 ypos 1.2 xpos 0.75 rotate 10.0

pause 1.0

$ ethanmisname = False

ethan "Who's... Roxanne?"

$ ethanmisname = True

show roxie_orientation behind ethan with dis

pause 1.0

red @talkingmouth "The one on the microphone up there."

show ethan closedbrow sadmouth:
    ypos 1.2 xpos 0.75 rotate 10.0
    ease 2.0 ypos 2.0 xpos 0.75 rotate 0.0

ethan "Ohhhhh..."

window hide

show calem thinking:
    ypos 2.0 xpos 0.65
    ease 2.0 ypos 1.2 xpos 0.65

calem @talkingmouth "There are better places to take a nap than on the ground, you know."

hide ethan

calem @talking2mouth "Here, grab my hand."

show calem:
    ypos 1.2 xpos 0.65 rotate 0.0
    ease 1.0 ypos 1.4 xpos 0.65 rotate 10.0
    pause 1.0
    ease 1.0 ypos 1.0 xpos 0.65 rotate 0.0

show ethan:
    ypos 2.0 xpos 0.75 rotate 10.0
    pause 2.0
    ease 1.0 ypos 1.0 xpos 0.75 rotate 0.0

pause 3.0

ethan @happy "Thanks, Kallen!"
calem @closedbrow talkingmouth "Well, it's closer than Calamari."
calem @surprisedbrow frownmouth "[ellipses]"

pause 1.0

show calem:
    xpos 0.65
    ease 0.25 xpos 0.25

calem smilemouth @sadbrow talkingmouth "...Personal space, please."
ethan @surprised "Huh? Oh, uh, sure."

show brendan angrybrow frownmouth:
    xpos 0.5 ypos 2.0
    ease 0.25 xpos 0.6 ypos 1.0

show may angrybrow frownmouth:
    xpos 0.5 ypos 2.0
    ease 1.0 xpos 0.4 ypos 1.0

brendan @talking2mouth "What's the big idea, blowing a guy's ears out like that!"
may @angrybrow talking2mouth "Seriously! Just to get our attention? She's louder than a Loudred!"
ethan @happy "Hey, I know what that is!"
calem @surprisedbrow frownmouth "[ellipses]"
calem @talkingmouth "Well done."

show roxie_orientation:
    zoom 1.0 xpos 0 ypos 0 xanchor 0 yanchor 0
    ease 5.0 zoom 1.1 xpos -80 ypos 0

stop music fadeout 1.5
    
$ renpy.music.play("Audio/Music/Hoenn_Start.ogg", channel='music', loop=None, fadein=1.5, tight=None)
$ renpy.music.queue("Audio/Music/Hoenn_Loop.ogg", channel='music', loop=True, tight=None)

roxanne @happy "Good evening, our new friends!{w=4.0}{nw}"

show roxspeech with Dissolve(2.0):
    subpixel True
    zoom 1.25 xalign 0.5
    ease 40.0 zoom 1.0

roxanne uniform @talkingmouth "I am Roxanne, and to start I would like to thank the academy staff here for allowing the council to hold this special event."
roxanne @closedbrow talkingmouth "I hope you will all make the most out of this occasion and grant me the opportunity to officially welcome every one of you to this prestigious establishment."
roxanne @happy "Everyone...{w=0.5} welcome to the Kobukan Academy of Advanced Pokémon Arts & Sciences."
roxanne @teachingmouth "While we are calling this event an orientation, I'd like to ask for your patience in this initial assembly before you all return to socializing or attending your personal agendas."

redmind @thinking "It's coming.{w=0.5} This is gonna be one of those long, insomnia-curing speeches."

roxanne @talkingmouth"For the first thing I'd like to mention, I hope you've all managed to reserve your own suites in one of the three student residential halls."
roxanne @talking2mouth "The one here is {color=#0048ff}Relic Hall{/color} and the other two, {color=#0048ff}Pledge Hall{/color} and {color=#0048ff}Aura Hall,{/color} are located east and west, respectively, from this location."
roxanne @teachingmouth "Another important item to cover is class scheduling."
roxanne @angrybrow talkingmouth "All of you here will follow a preset class schedule of six periods per day.{w=0.5} Pay close attention, because you'll be doing this for the next year."

hide roxie_orientation
hide calem
hide ethan
hide may
hide brendan

red @closedbrow talking2mouth "...They said all this on the website."

calem @happy "It could still be a nice refresher for those who came in less-informed."
    
roxanne @closedbrow talkingmouth "{color=#0048ff}The first period of each day is homeroom,{/color} lasting two hours. Core subjects will be covered here by your professor."

brendan @surprised "Two hours?!"
calem @closedbrow talking2mouth "I know. Two hours is hardly enough time to cover all the material."
may @sad "Especially since we only have a year..."
ethan @surprised "Uh, that's not what he was implying, guys."
red @happy "I spent two hours in Mt. Moon with no repels once. Can't be any worse than that."
ethan @angry "Oh, god, Zubat everywhere, right? You know, they're an invasive species--Kanto has a lot to answer for, for letting them cross the border and mess up Johto like they have."
red @confused "What're we supposed to do, set up a big net?"

roxanne @talkingmouth "{color=#0048ff}Following homeroom will be an hour of one Pokémon type elective{/color} of your choice.{w=0.5} You'll be able to select {color=#0048ff}{i}two{/i} out of the eighteen known Pokémon types{/color} to focus your studies on for each individual day."

ethan @surprised "Whoa, hold up."
ethan @confused "Are we specializing in two Pokémon types?{w=0.5} Only two out of eighteen?"
calem @talkingmouth "Not quite. You can certainly take only the same two electives every day, if you wish, but you're permitted to switch between electives at will."
brendan @surprised "Huh?! How does that work?"
calem @talkingmouth "Due to the high teacher-to-student ratio Kobukan boasts, instructors are able to adjust the curriculum to be appropriate to any student's level, even if they've never taken that class before."
red @talkingmouth "That's another advantage of Kobukan's unique one-year program. We have to work three times as hard, and three times as fast, as other schools, but students can customize their education."
redmind @thinking "I know a lot of Kobukan students, especially the ones that went on to excel, focused on two to three electives. Mastering all eighteen types in one year just doesn't seem feasible."
redmind @frownmouth angrybrow "Even an amazing student could probably only handle {color=#0048ff}six{/color} electives."

show roxspeech:
    ease 0.75 zoom 1.0

roxanne @talkingmouth "In addition to your elective classes, you will each also have a period of gym and lunch."
roxanne @closedbrow teachingmouth "Your last class will end at 3 PM."
roxanne @talkingmouth "After that, those of you taking part in research or extracurricular activities are free to use our campus buildings."
roxanne @sadbrow talking2mouth "As is tradition, there will be a curfew in place. As such, students seen outside of their dorms after 8 PM are subject to severe disciplinary action."

show roxspeech:
    zoom 1.0

red @surprised "8 PM?{w=0.5} That's--"

show roxspeechmad with dis:
    zoom 1.0 xalign 0.5

brawly uniform @angrybrow talking2mouth "Yeah, 8 PM! That's way too early! I mean, seriously, it was a {i}pain{/i} last year, and the fact we're {i}keeping it is ridiculous! I mean, c'mon, the evening only {i}starts{/i} at 8 PM!"

roxanne @angrybrow talking2mouth "{i}Ahem{/i}... And don't think you can just sneak out, either!{w=0.5} There are security cameras in every room in every building."

roxanne @closedbrow talking2mouth "Unless you have a special notice from a staff member, student council member, or someone empowered to give permission by the same, there will be no exceptions to--"

brawly @angrybrow talking2mouth "Yeah, yeah, I know about the cameras. I just think the whole thing is dumb! Like, what are the students supposed to do, sit around all night? {i}Studying?!{/i}"

falkner uniform @talking2mouth "We all have to follow the rules, Brawly."

brawly @sad "I mean... yeah, I know we already tried, but we could talk to Drayden again about it, and maybe--"

roxanne @angry "Will you {i}be quiet?!{/i} We're in the middle of an assembly right now!"

roxanne @closedbrow angrymouth "If you have a problem with the way this school is run, throwing our dirty laundry out on the auditorium floor in front of everyone is hardly the way to deal with it. Have some decorum!"

redmind @sad "Oh, poor Brawly. To get tongue-lashed like this in front of the entire auditorium..."

falkner @closedbrow talkingmouth "Roxanne. Your speech."

roxanne @angrybrow talking2mouth "When this is over, we're going to have a little talk, you and I!"
    
show roxspeechmad:
    alpha 1.0
    ease 0.33 alpha 0.0

roxanne @closedbrow frownmouth "{i}Ahem{/i}... Where was I?"
roxanne @happy "Oh, yes. As I was saying, it is a privilege to be a part of this great school we call Kobukan Academy.{w=0.4} Now is the opportunity of a lifetime to open a new door!"

calem @surprised "She switched gears that easily?{w=0.5} That's formidable."

roxanne @talkingmouth "Only by working together can we realize our goals and foster our talents.{w=0.5} But in the end, it will be up to you to find your own path and seize the day with your own hands!"

$ PlaySound("Big Applause.ogg")

roxanne @happy "And with that, I formally welcome you to Kobukan Academy!"

window hide

hide roxspeechmad

show roxspeech:
    alpha 1.0
    ease 2.0 alpha 0.0

show orientation:
    zoom 1.1 xpos -80 ypos 0 xanchor 0 yanchor 0
    ease 4.0 zoom 1.0 xpos 0 ypos 0   

$ renpy.pause(2.5, hard=True)

roxanne @closedbrow teachingmouth "Have a great rest of the day, everyone. And don't forget to get those signups done!"

show brendan happy with dis:
    xpos 0.2 xzoom -1

show may happy with dis:
    xpos 0.4

show ethan happy with dis:
    xpos 0.6

show calem happy with dis:
    xpos 0.8 xzoom -1
    
pause 1.0

show brendan -happy with dis
show may -happy with dis
show ethan -happy with dis
show calem -happy with dis

calem @talkingmouth "Well, what did you think, everyone?"

brendan @talking2mouth "About what? The speech?"

calem @closedbrow talking2mouth "Well, I guess that's something, too."
calem @talkingmouth "But I'm more focused on the class scheduling part."
calem @closedbrow talkingmouth "We're completely set on the room situation so there's nothing left for us to do there."

calem @talking2mouth "It'll be tough picking two type electives out of eighteen. {color=#0048ff}And we'll have different instructors and classmates depending on the types we choose...{/color}"
calem @talkingmouth "Even though we have the freedom to swap between electives at any time, many students will choose instead to focus on two or three types for the entire year."

redmind @thinking "That might work for other students, but if I want to become a Champion, {color=#0048ff}I should probably swap between electives depending on what kind of Pokémon I'm trying to raise.{/color}"

calem @closedbrow talkingmouth "A large decision awaits us when we come back to our room, I believe. Handling that should be our first priority."

brendan @happy "Great!"
brendan @talking2mouth "I'll tell you what, [first_name], I'm gonna pick the same electives as you!"
brendan @happy "Then we'll be class buddies, too! It'll be great!"

red @surprisedeyes surprisedeyebrows sadmouth "I.{w=0.25}.{w=0.25}."

may @happy "Imagine if you two also get the same homeroom teacher?{w=0.5} Then you guys'll look like a couple!"

red @closedbrow talkingmouth "I'm not sure how I should feel about that."

brendan @happy "Aw, jokes, dude! I'm just messin.'"
brendan surprisedbrow frownmouth @neutralbrow talking2mouth "I haven't decided on which electives I'm picking yet, so if I do end up pickin' the same ones as you, it's totally by chance!"

may @talkingmouth "Honey, isn't Champion Wallace teaching at this school? I think he teaches Water-type classes."

brendan -surprisedbrow -frownmouth @happy "No shot?! Well, that decides one of my choices for me!"

may @happy "[first_name], I know one of my choices will be Fire, so if you also decide to choose Fire, you'll have at least one familiar face there."

show may surprisedbrow frownmouth
show calem surprisedbrow frownmouth
show brendan surprisedbrow frownmouth 
with dis

red @closedbrow talking2mouth "I think I'll probably swap between electives."

ethan @surprised "Really?! I heard that's really tricky to do right, though!"

red @sadbrow talkingmouth "So have I. But almost all the Champions that graduated from Kobukan did it. I wouldn't be the first."

show may -surprisedbrow -frownmouth
show calem -surprisedbrow -frownmouth
show brendan -surprisedbrow -frownmouth 
with dis

ethan @happy "Huh. Well, I'm not going to tell you to stop! I was going to do the same thing."

red @surprised "Oh, really?"

ethan @talkingmouth "Yeah! Only downside is, I guess if we're both hopping between electives, we're probably not going to have too many classes together."

red @happy "Well, when we do, we'll appreciate them even more." 

brendan @talkingmouth "Wanna come with us and decide on electives, May?"

may @sadbrow happymouth "I'll have to pass, boys,{w=0.5}{nw}"
extend @happy " I already agreed to meet with Leaf later."

red @talkingmouth "Leaf?"

brendan @talking2mouth "One of her dormmates."
brendan @talkingmouth "I met up with all of them before I actually got to our room! {nw}{w=0.5}"
extend @sadbrow talking2mouth "What,{w=0.5} uh,{w=0.5} what were their names, again?"

may sadbrow frownmouth @talking2mouth "...You weren't listening?"

brendan sadbrow @talkingmouth "N-no, I totally was!{w=0.5} I'm just, uh, so bad with names.{w=0.5} Isn't that right, Erick?"

ethan @angrybrow frownmouth "[ellipses]"

show brendan angrymouth closedbrow sweat with dis

ethan @angrybrow talking2mouth "It's Ethan. That's pretty inconsiderate of you, to get my name so wrong, Brantham."

show brendan -angrymouth -closedbrow -sweat
show may -sadbrow -frownmouth
with dis

calem @closedbrow talking2mouth "Let's get back on topic. May, what are your dormmates' names?"

may @closedbrow talkingmouth "Well... there's me, Leaf, then a girl from Unova named Hilda--"

show orientation with hpunch

show brendan surprisedbrow frownmouth with dis:
    xpos 0.2 xzoom -1
    ease 0.5 xpos 0.5 xzoom 1

show may surprisedbrow frownmouth with dis:
    xpos 0.4
    ease 0.5 xpos 0.6

show ethan surprisedbrow frownmouth with dis:
    xpos 0.6
    ease 0.5 xpos 0.7

show calem surprisedbrow with dis

show hilbert angrybrow:
    xpos -0.5 xzoom -1
    ease 0.25 xpos 0.2

hilbert @angry "What?! Hilda?!"

pause 1.0

calem @closedbrow talkingmouth "Personal space, please."

show calem:
    xpos 0.8
    ease 1.0 xpos 0.1

pause 1.0

calem @frownmouth "[ellipses]"
calem @sad "Nevermind, this is far worse."

show calem:
    xpos 0.1
    ease 1.0 xpos 0.8

pause 1.0

hilbert @angry "Did you say Hilda?! Answer me!"

show brendan:
    xpos 0.5
    ease 0.5 xpos 0.4

brendan angrybrow @angry "Hey, man, back off."
may sadbrow @sad "Y-yeah...? Hilda's her name. Um, do you know her?"
hilbert sadbrow "[ellipses]"
hilbert @sadbrow talkingmouth "Probably not. It's a common name."
hilbert @closedbrow talkingmouth "Nevermind."

show hilbert:
    xpos 0.2
    ease 1.0 xpos -0.5

calem @closedbrow talkingmouth "...What an unpleasant man. Let him serve as a reminder of how not to react. Please, May, continue."

may @sadbrow talkingmouth "U-uh... well, after Hilda is this Kalosian girl named Serena--"

show brendan surprisedbrow frownmouth with dis:
    xpos 0.4 xzoom 1
    ease 0.5 xpos 0.2 xzoom -1

show may surprisedbrow frownmouth with dis:
    xpos 0.6
    ease 0.5 xpos 0.3

show ethan surprisedbrow frownmouth with dis:
    xpos 0.7
    ease 0.5 xpos 0.4

show calem surprisedbrow with dis

show orientation with hpunch

calem @surprised "WHAT?!"

ethan @confused "What now?"

calem @sad "Please, describe her to me!"

show ethan surprisedbrow frownmouth with dis

may @closedbrow blush talkingmouth "Um, well, she's got flawless skin, a massive chest, really long legs--"
calem sadbrow @sad "Sunglasses? Does she have sunglasses?"

show brendan happy with dis

may @happy "Oh, yes! They kinda make her look like a Hoothoot. She laughed when I said that."

calem @closedbrow sadmouth "...That cannot be. {size=30}She's not meant to...{/size}"

show may sadbrow frownmouth with dis
show brendan sadbrow frownmouth with dis
show ethan sadbrow frownmouth with dis

pause 1.0

red sadeyebrows sadeyes talking2mouth "Hey. Calem. You good?"

calem @talkingmouth "Yes... except for the sinking realization that I made the hardest decision of my life for absolutely naught."

ethan @confused "...Translation?"

calem @closedbrow talkingmouth "One often meets their destiny on the road to avoid it."

ethan @unamusedbrow talking2mouth "Calamari. Dude. None of us know what that means."

show brendan surprisedbrow frownmouth with dis:
    xpos 0.2 xzoom -1
    ease 1.0 xpos 0.5 xzoom 1

show may surprisedbrow frownmouth with dis:
    xpos 0.3
    ease 1.0 xpos 0.6 ypos 1.0 rotate 0

show ethan surprisedbrow frownmouth with dis:
    xpos 0.4
    ease 1.0 xpos 0.7

show calem closedbrow with dis

show serena:
    xpos -0.5
    ease 1.5 xpos 0.2

serena @talkingmouth "Excuse me. Is that you, Calem?"

$ BecomeNamed("Serena")

redmind @surprisedbrow frownmouth "{cps=*0.2}...{/cps}Well, she certainly fits the description May gave, vague as it was. With those sunglasses and that accent, I'm pretty sure that's Serena."

calem -closedbrow @talkingmouth "Oh, hello, Serena."

show ethan closedbrow:
    xpos 0.7
    ease 10.0 xpos 1.5

show may:
    xpos 0.6 rotate 0
    ease 3.0 xpos 0.1 
    pause 2.0
    "may blush flirtbrow poutmouth"
    ease 2.0 rotate -5.0 ypos 1.2
    pause 1.0
    ease 1.0 xpos -0.5

show brendan:
    xpos 0.5
    ease 2.0 xpos -0.5
    pause 5.0
    ease 1.0 xpos 0.05
    pause 1.0
    ease 1.0 xpos -0.5

calem @closedbrow talkingmouth "Uh..."
calem @happybrow talkingmouth "I had no idea you were enrolled here."

serena @talkingmouth "Same for me.{w=0.5}{nw}" 
extend @happy " What a pleasant serendipity."
serena @talkingmouth "In any case, since we've managed to find each other by pure chance, let's not let this opportunity go to waste. Are you busy?"

pause 1.0

narrator "Calem gestures at you vaguely."
    
show serena at getcloser:
    xpos 0.2

pause 1.0

serena @sadbrow talkingmouth "Oh? And who might you be?"

red @happy "Me? Oh, uh, I'm [first_name], and..."

menu:   
    "With those glasses, I bet people mistake you for a Hoothoot.":
        show calem surprisedbrow with dis
        show serena surprisedbrow frownmouth with dis

        pause 2.0
        
        redmind @wince frownmouth "This was a gamble."

        show calem -surprisedbrow smilemouth with dis

        serena @closedbrow frownmouth "Hee... Hee..."

        redmind -talkingmouth -frownmouth @confusedbrow frownmouth "She's either crying or laughing."

        serena -surprisedbrow -frownmouth @happy "Heeheeheehahahahaha!"

        $ ValueChange("Serena", 1, 0.2)

        serena @happy "That's actually the second time I've heard that today! It's true, isn't it?"
        serena @talkingmouth "Would you believe me if I told you they were a present from my mother?"
        serena @happy "Everyone thinks they're silly-looking, but I think they're adorable!"

        redmind @closedbrow sweat "Nailed it."
        
    "It's a pleasure to meet you.":        
        red @happy "It's a pleasure to meet you."

        serena @happy "And the same to you, I'm sure."

pause 1.0

serena @surprised "Oh my, look at the time!"

show serena at getfurther:
    xpos 0.2

serena @sadbrow talkingmouth "I have to get going. I'm going to run some errands with a few girls I met earlier today."

serena @happy "But it's really great to see you here!"
serena @happybrow talkingmouth "Let's catch up later!"

calem @happy "Sure, I'll see you around."

hide serena with dis
    
pause 1.0

show calem sadbrow with dis

show calem:
    xpos 0.8
    ease 0.5 xpos 0.5

stop music fadeout 3.0

red @talkingmouth "And she's gone."

pause 1.0

red @angrybrow talking2mouth "...And, so, apparently, is everyone else."

pause 1.0

red @sadbrow talking2mouth "Hey, seriously, Calem, are you alright?"
calem @sadbrow talking2mouth "[ellipses]No, but I will be."

pause 1.0

red -angrybrow -frownmouth @talkingmouth "Alright. But you know, I'm here to talk. Might need to get a lunch or two together, get a better feel for each other, you know, but I {i}am{/i} here."

calem @happy "Thank you for your concern. I assure you my friendship does not normally involve so much drama."

$ renpy.music.queue("Audio/Music/SoaringIllusions.ogg", channel='music', loop=True, fadein=3.0, tight=None)

red @talkingmouth "Friend of yours?"

calem @talkingmouth "You can say that."
calem @closedbrow talkingmouth "We were neighbors. As you've doubtlessly gathered, though, I was not made aware she would be enrolling here. I wonder why.{w=0.25}.{w=0.25}."

calem @surprised "Ah.{w=0.75}{nw}"
extend smilemouth @talkingmouth happybrow " Since we're going to be dormmates, we should exchange contact information. You know, in case we need to call each other if there's an emergency."

red @talkingmouth "Oh, yeah. Good thinking."

$ BecomeContacted("Calem")

calem @talkingmouth "All right. It appears that we've been 'ditched,' so I'm going to resolve a few errands."
calem @closedbrow talking2mouth "I have some personal business to take care of at the registration office. Something about my recommendation letters, if I remember correctly."
calem @talkingmouth "I'm suspecting other students are probably there for other reasons, so I'd like to get there before it closes."

red @talkingmouth "Okay, cool. Need me to come with you?"

calem @talking2mouth "No, it's all right."
calem @happy "I believe that androgynous Student Council member recommended we head to the lobby to mingle. Why don't you head there?"
calem @closedbrow talking2mouth "You never know what connections you might make."

red @playfuleyes confusedeyebrows talkingmouth "Oh, so it's really just about making contacts you can leverage later?"

calem @sadbrow talkingmouth "You think so little of me? I'm not Hilbert, you know. No, I think forming bonds with other people is genuinely fun. Regardless of what boons they may come with."

red @happy "Just joking, I know you're not like that. Anyway, I'll catch you later?"

calem @happy "Yes, give me a call if you need anything."
calem smilemouth @talkingmouth "{i}Au revoir.{/i}"

show calem:
    xpos 0.5
    ease 1.0 xpos 1.5

pause 2.0

redmind @thinking "Alright, time to find that lobby! Let's see... if I just start running in a random direction, then..."

show hall_A2b at sepia with dis
show flashback with dis

$ renpy.pause(1.0, hard=True)

show leaf flirtbrow angrysmilemouth at sepia, dissolvein behind flashback

pause 1.5

leaf @talking2mouth "Hey, did I give you that brochure for nothing? Use it, dummy!"

show blank with splitfade

hide leaf
hide hall_A2b
hide flashback
hide blank with dis

redmind "Oh, great, now there's two of them in my head. Fine, I'll use the brochure!"
red surprisedbrow frownmouth @surprisedbrow "[ellipses]"
redmind thinking "Huh. This is actually super-easy to follow. Maybe that girl had a point."
red angrybrow happymouth "Okay! Lobby time. Let's go!"

$ renpy.pause(1.0, hard=True)

show blank2:
    alpha 1.0
    ease 1.5 alpha 0.0

show hall_B behind blank2:
    xpos 960 xalign 0.5 ypos 1080 yalign 1.0 zoom 0.9
    ease 0.5 zoom 0.95

$ renpy.pause(0.5, hard=True)

show hall_B:
    alpha 1.0 zoom 0.95
    ease 1.2 zoom 1.0
    block:
        ease 0.03 xpos 940 ypos 1060
        ease 0.03 xpos 980 ypos 1100
        ease 0.03 xpos 960 ypos 1080
        repeat 2

$ showredonly = True

show misty surprisedbrow frownmouth:
    xpos -0.5 zoom 1.0 ypos 1.0
    pause 1.1
    ease 0.3 zoom 1.5 ypos 1.3 xpos 0.5
    ease 0.7 rotate 45.0 ypos 3.0

$ renpy.pause(1.2, hard=True)

stop music fadeout 1.0

$ PlaySound("Body Crash.ogg")
$ renpy.pause(0.4, hard=True)

hide blank2

misty @talkingmouth "{size=48}HEY! WATCH IT!{/size}"
    
red surprisedbrow frownmouth @surprised "Whuh?"

queue music "Audio/Music/CeruleanCity.ogg"

$ showredonly = False

show misty angry:
    ypos 3.0 rotate 45.0 zoom 1.0
    ease 1.5 ypos 1.0 rotate 0.0
        
misty @talkingmouth "Don't 'whuh' me! What's with that dumbass look on your face?"
misty @talkingmouth "Are you deaf or just stupid?! Don't just stand there and stare! At least admit you weren't paying attention!{w=0.25} 'Cause clearly you weren't!"

menu:
    "I'm very sorry.":
        show misty surprisedbrow -angrymouth with dis
        red @talkingmouth "I was in kind of a hurry and turned the corner too quickly. Are you okay?"      
            
        misty @closedbrow talking2mouth "{i}*Sigh.*{/i}"
        
        misty @talkingmouth "I'm fine."
        
        misty @angry "I'm fine!{w=0.6} It's fine!"
        misty @closedbrow talkingmouth "Just try to not run over any more girls on the way to... {w=0.5}{nw}"
        extend @sadbrow talkingmouth "wherever you're going."
        
        hide misty with dis
            
        stop music fadeout 2.0
        
        redmind @thinking "Yeah. Okay. Tear my head off, then strut out without even giving your name. Nice."
        redmind @sad2eyes frownmouth "Ugh, groveling like that left a bad taste in my mouth..."

    "You ran into me!":
        show misty surprisedbrow frownmouth with dis
        red @talking2mouth angrybrow "Lay off the insults for a second, and maybe you'd realize that this was totally your fault."

        $ ValueChange("Misty", -1, 0.5)

        misty "You...{w=0.7}{nw}"
        extend angry " JERK!"
        
        show misty angry:
            zoom 1.0 ypos 1.0 xpos 960
            ease 0.5 zoom 1.25 ypos 1.2 xpos 720
        
        $ renpy.pause(1.0, hard=True)
        $ PlaySound("Slap.ogg")
        pause 0.1
        
        show misty angry:
            xpos 720 ypos 1.2 zoom 1.25 rotate 0
            ease 0.1 xpos 520 ypos 1.1 zoom 1.33 rotate -3
        
        show hall_B at hall_move1
        
        pause 1.0
        
        show misty angry:
            xpos 520 ypos 1.1 zoom 1.33 rotate -3
            ease 0.2 xpos 360 ypos 1.0 zoom 1.25 rotate 0
        
        show hall_B at hall_move2
        
        redmind @closedbrow frownmouth "Ow."
        
        show misty angry:
            zoom 1.25 xpos 360 ypos 1.0 alpha 1.0
            parallel:
                pause 0.5
                ease 0.5 alpha 0.0
            parallel:
                ease 1.0 xpos -200
        
        stop music fadeout 2.0
        
        pause 1.0
        
        red @angry "Ugh. Has anyone ever told you... {size=40}you don't take criticism too well?!{/size}"

    "My bad, but tone it down.":
        show misty surprisedbrow -angrymouth with dis
        red @talkingmouth "I was just figuring out what to say. So, sorry, alright? No need to blow up like that. Now, are you okay?"
        
        $ ValueChange("Misty", 1, 0.5)        
            
        misty @closedbrow talking2mouth "{i}*Sigh.*{/i}"
        
        misty @talkingmouth "I'm fine."
        
        misty @angry "I'm fine!{w=0.6} It's fine!"
        misty @closedbrow talkingmouth "Just try to not run over any more girls on the way to...{w=0.5}{nw}"
        extend -closedbrow -angrymouth @angry " wherever you're going."
        
        hide misty with dis
            
        stop music fadeout 2.0
        
        redmind @unamusedbrow frownmouth "Yeah. Okay. Tear my head off, then strut out without even giving your name. Nice."

pause 1.0

$ renpy.music.play("Audio/mediumcrowdloop.ogg", channel='crowd', loop=True, fadein=1.0)

scene lounge:
    alpha 0.0 zoom 1.0
    ease 3.0 alpha 1.0 zoom 1.1 ypos -100

show hall_B behind lounge

$ renpy.pause(2.5, hard=True)

redmind "Huh, looks like most people are discussing the orientation."
redmind "I imagine a lot of people are coordinating their type electives, and figuring out their schedules."

show lounge:
    zoom 1.1 ypos -100 alpha 1.0
    ease 0.75 zoom 1.0 ypos 0

redmind "I don't see any of my dormmates around here...{w=0.5} but that's fine. I think I'd like to start a conversation with someone new, anyway."

show lounge:
    zoom 1.0
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

stop music fadeout 1.0
$ cap_player = first_name.upper()
"{color=#3110dd}???{/color}" "\"{size=45}[cap_player]!!{/size}\""

red happy "Whoa! That guy has the right idea!"

show lounge:
    yalign 1.0 xalign 0.5

show blue angry with dis:
    xpos 720

pause 0.5
play music "Audio/Music/RivalTune.ogg" noloop
$ renpy.music.queue("Audio/Music/Show Me Around.ogg", channel='music', loop=None, fadein=1.0, tight=None)
    
$ renpy.pause(0.5, hard=True)

red unamusedbrow talking2mouth "Oh. I should've known."

blue @talkingmouth "What the hell are you stalking me for?{w=0.25} Wait, how'd you even get in here?"

show blue:
    zoom 1.0 ypos 1.0
    ease 0.5 zoom 1.25 ypos 1.1 xpos 600

blue @surprisedbrow talkingmouth "Did you sneak in just to follow me around?! That's creepy as shit! Someone told me that a guy who looked like you was here, but I thought she was wrong... but you really {i}are{/i} that desperate!"
blue frownmouth angrybrow @angry "You better scram before I call security on your ass!"

red @talkingmouth "Give me a break.{w=0.5} I've got an invitation, just like you, [blue_name]."

show blue:
    zoom 1.25 ypos 1.1 xpos 600
    ease 0.5 zoom 1.0 ypos 1.0 xpos 720

blue sweat @surprisedbrow angrymouth "You...{w=0.5} got an invitation?"

show blue surprisedbrow frownmouth with dis
red @closedbrow sweat "Yeah, last month.{w=0.5} Actually, we thought it was yours, at first, but--"

show blue angry:
    zoom 1.0 ypos 1.0
    ease 0.25 zoom 1.25 ypos 1.1 xpos 600

blue -sweat @angrybrow talking2mouth "Bullshit! Let me see it!"
    
show letter at itemgive

red @upbrow talking2mouth "Sure, if it'll make you feel better."
red @angrybrow talking2mouth "...But don't even think about so much as folding it roughly."

hide letter with dis

pause 1.5
    
blue -angry surprisedmouth ".{w=0.4}.{w=0.4}."

red -angrybrow talking2mouth "Hey. Earth to [blue_name]. Are you happy now?"

blue surprisedbrow frownmouth @surprised "[ellipses]"

show blue:
    zoom 1.25 ypos 1.1 xpos 600
    ease 0.5 zoom 1.0 ypos 1.0 xpos 720

blue sad "This means...{w=0.5} then why didn't Gramps...?"
blue @talkingmouth "...That makes no sense.{w=0.5}{nw}"
blue angry "...That makes no sense.{fast} Why are you here? You're the last guy in the world that should be in here!"
red angrybrow "...And yet I am, just as much as you are. So what does that say about you?"
blue @talkingmouth "You're such a waste of space, it's disgusting that Gramps recommended you.{w=0.5} He must've just felt bad that you didn't have any friends!"

show blue closedbrow:
    xpos 720
    ease 0.5 xpos 500

blue @talkingmouth "Psh, talking about this with you is a waste of time."

blue angry "Whatever happens, just quit holding me up and we won't have a problem, got it, [first_name]?"

blue -angry @talkingmouth "Now excuse me, I got things to do."

show blue:
    xpos 500 alpha 1.0
    ease 0.4 xpos 0 alpha 0.0

blue happybrow angrymouth "Smell ya, loser!"

pause 2.0

redmind -angrybrow sad "That was utterly miserable. I'll just see if there's someone else to talk to, then I'm out."

cheren @closedbrow talking2mouth "Pardon me."
red @talkingmouth "Oh, hey."

show cheren with dis

cheren @disappointed "On the behalf of my classmate, I'd like to apologize for his disastrous conduct."
red @happy "Hah, what? You don't need to apologize for [blue_name]. It's him, and only him, that's responsible for how he acts."
cheren @sad "Nevertheless, to have some of your first moments at this prestigious academy marred by that man's atrocious manners..."
red @happy "It's fine, really. I know how to roll with the punches."
red @confused "Anyway, I appreciate your concern, but, uh, how are you involved in this? You're a normal student, right?"
cheren @talkingmouth "For now. I aim to join the Student Council shortly, though."
red @surprised "Oh, yeah? Actually, that reminds me of a question I had. This school's got a one-year curriculum. How does the Student Council work? How can there be one before the school year's even started?"
cheren @happy "It'd be my pleasure to explain! Last year's students can elect to remain with the school after graduation."
cheren @sadmouth "They take on a supervisory role for a number of months, ensuring the incoming class becomes acclimated." 
cheren @closedbrow talking2mouth "However, a month after the year begins, a new election is held to determine this year's Student Council. From there, the Council votes internally to determine who their president will be."
red @confused "Wow, so you only have a month to start up a campaign, and get people to vote for you?"
cheren @sad "That's the sum of it, yes."
red @happy "Well, what are your positions? Convince this voter."
cheren surprisedbrow frownmouth @surprised "Oh? Er, then... my positions, yes..."

pause 2.0

red @sadeyes sadeyebrows talkingmouth "You good?"

pause 1.0

cheren -surprisedbrow -frownmouth -surprised @disappointedbrow happymouth "{i}...Absolutely.{/i}"

pause 1.0

cheren @angry "My positions are thus: The introduction of co-ed dorms. Raises for non-academic staff. Repeal of the school's frankly absurd curfew! We are adults, after all."
cheren @disappointedbrow talking2mouth "Furthermore, the benefits granted by tenure in this school allow for far too much 'creativity' in how classes are run. On the other hand, the staff should absolutely be permitted to unionize."
cheren @closedbrow talkingmouth "Even further more, financial aid ought to be dispersed towards those who need it most, not those who are most well-connected."
cheren @angry "Finally, the number of highly suspicious stories about how this school decides admission must be looked into, resolved, and, if necessary, terminated."

redmind @surprisedbrow frownmouth "...Oh, crap, this guy's intense."
redmind @frownmouth closedbrow "And I think he's looking into something that could cause some serious problems for me."
red @confused "That's pretty ambitious. Does the Student Council have the authority to do all that? A lot of it sounds like stuff the staff would want to handle themselves."
cheren @closedbrow talkingmouth sweat "It certainly is. But what is politics, if not the wresting of power from those who wish to hold it evermore?"
cheren @sad "Regrettably, what I can promise is limited, given the scope of my ambition. And many have overscoped themselves into an early grave."
cheren @angrybrow happymouth "But I assure you, if you elect me to the Student Council, I'll never stop fighting for a more egalitarian, just, and modernized Kobukan Academy."

pause 2.0

cheren @disappointed "Oh, and also, we'll put five-ply toilet paper in the washrooms."
cheren @upeyes talking2mouth "That's a very popular request amongst a certain lobby, so{cps=*0.2}..."

pause 1.0

red @happy "Well, you've got my vote. Who am I voting for?"

$ BecomeNamed("Cheren")

cheren @surprised "Oh! Of course. My name is Cheren, of Aspertia City. In Unova."

red @happy "Sounds good. Hope you succeed."

cheren happy "I very much appreciate your support. Good day."

hide cheren with dis

redmind thinking "...Well, he seems nice. I'm worried about what he might find, though. But... given what he says he wants to do, surely he won't actually make enough progress to find anything out about me, right?"
redmind sadeyes sadeyebrows "{cps=*0.2}Right...?{/cps}"

$ renpy.music.stop(channel='crowd', fadeout=2.0)

show blank2 with dis:
    alpha 1.0

pause 2.0

redmind "Alright. I still haven't unpacked my stuff yet, so I should probably run back to my room now."

scene hall_A with dissolve    

queue music "Audio/Music/CeruleanCity.ogg"

$ renpy.pause(1.5, hard=True)

pause 1.5

red surprisedbrow frownmouth @surprised "Uh."

show misty with dis:
    xpos 860

pause 1.0
    
misty @surprised "Seriously? Didn't I {i}just{/i} see you?"
misty "{w=0.5}.{w=0.5}.{w=0.5}."
misty @angry "You're the guy that ran me over."

if (persondex["Misty"]["Value"] > 0):
    misty @talkingmouth "But at least you were a decent enough human being and apologized."
    misty @sad "Not many people own up to their mistakes.{w=0.5}{nw}"
    extend @closedbrow sweat talkingmouth " I, uh, appreciated it."

$ renpy.pause(1.5, hard=True)
misty @closedbrow talkingmouth "Tch. Whatever. I won't hold it against you."
$ renpy.pause(1.5, hard=True)

$ BecomeNamed("Misty")
misty @surprisedbrow talkingmouth "...Well? Introduce yourself. I'm Misty."

if (persondex["Misty"]["Value"] > 0):
    red @happy "I'm [first_name]. Nice to meet you."
else:
    red @happy "I think we got off on the wrong foot. Let's start over. I'm [first_name], and it's nice to meet you."

if first_name in ["John", "Johnny", "Jonathan", "Jon", "Joe", "Joseph", "Joey", "Raj", "Petra", "Salamander", "Juno", "Nikolai", "Michael", "Mike", "Mikey", "Robert", "Rob", "James", "Will", "William", "Bill", "Billy", "David", "Dave", "Richard", "Rich", "Richie", "Charles", "Charlie", "Chuck", "Chuckie", "Chucky", "Thomas", "Tom", "Tommy", "Timothy", "Timmy", "Tim", "Christopher", "Chris", "Daniel", "Danny", "Dan", "Paul", "Mark", "Donald", "Donny", "Don", "George", "Kenneth", "Kenny", "Ken", "Steven", "Stephen", "Stephan", "Steve", "Edward", "Edwin", "Eddie", "Eddy", "Ed", "Brian", "Ronald", "Ronny", "Ron", "Anthony", "Tony", "Kevin", "Kev", "Jason", "Jay", "Matthew", "Matt", "Larry", "Jeffrey", "Jeff", "Geoffrey", "Frank", "Frankie", "Scott", "Erik", "Eric", "Andrew", "Andy", "Drew", "Raymond", "Ray", "Gregory", "Greg", "Joshua", "Josh", "Jerry", "Jeremy", "Dennis", "Denny", "Walter", "Walt", "Patrick", "Pat", "Patty", "Pattie", "Peter", "Harry", "Harold", "Jack", "Jackie", "Jacky", "Roger", "Carl", "Henry", "Justin", "Terry", "Samuel", "Sam", "Nicholas", "Nick", "Nicky", "Nickie", "Adam", "Benjamin", "Ben", "Benny", "Brandon", "Phillip", "Philip", "Phil", "Sean", "Fred", "Freddy", "Freddie", "Emmet", "Ethan"]:
    misty @surprised "'[first_name]?' For real?{w=0.5} That sounds so basic."
    red @unamusedbrow talking2mouth "I stand corrected."
    misty @surprised "Uhh, I just mean I didn't expect your name to be so normal, is all!"

else:
    misty @surprised "'[first_name]?' For real?{w=0.5} What kind of name is that?"
    red @unamusedbrow talking2mouth "I stand corrected."
    misty @surprised "Uhh, I just mean I don't know many people named that, is all!"

misty @sadbrow sweat talkingmouth "I'm not implying it's weird or anything, honest!"

redmind @unamusedbrow frownmouth "Go on. Keep digging."
misty -sweat surprised @sad "{size=30}{i}Ugh, why am I always so...{/i}{/size}"

red @closedbrow talking2mouth "You're going to have to speak up a bit. You started trailing off on that last sentence."

misty -surprisedbrow -frownmouth -surprised @angry "I didn't say anything!"

pause 1.0

redmind @thinking "Tch, she's tenser than a coiled spring. I'm not sure if this conversation is even worth the minefield, but..."

menu:
    "Do you live here?":
        red @talkingmouth "This is your room, right here?"
        misty @surprised "Yeah? So what?"

        $ renpy.pause(1.0, hard=True)

        misty @closedbrow talkingmouth "Oh, great. Now you know where I live."
        misty @angry "Don't get any funny ideas, buster!"
        red @happy "Hey, I'm a nice guy.{w=0.5} I wouldn't dream of doing anything like that."
        misty @closedbrow talkingmouth "Hmmm."
        
        misty @talkingmouth "I guess I can trust you.{w=0.75}{nw}"
        misty @angrybrow talkingmouth "Just be sure to watch where you're going when classes start!"
        redmind @thinking "You can drop that anytime, you know..."
        
    "How was your day?":
        red -angrybrow -talking2mouth @talkingmouth "So, how was your first day here?"
        misty @talkingmouth "Other than you tackling me to the ground?{w=0.5} Just peachy."
        redmind @thinking "You can drop that anytime, you know..."

    "Is that a Cerulean outfit?":
        show misty happy with dis        
        $ ValueChange("Misty", 1, 0.5)

        misty smilemouth -happy @happy "You know Cerulean City?"
        
        red @talkingmouth "Sure! My mom and I used to go to their water parks all the time when I was a little kid."
        red @sadeyes sadeyebrows talkingmouth "Though, those Gyarados rides always scared the pants off me back then."
        
        misty @sadbrow talkingmouth "Aw, no way!{w=0.5} Where are you from?"
        
        red @talkingmouth "I'm from Pallet Town.{w=0.5} It's not the most well-known place in Kanto but I'm sure you've heard of it."
        
        misty -smilemouth @surprisedbrow talkingmouth "What town? Pewter?"
        
        red @closedbrow talkingmouth "Uh, no. Pallet Town?{w=0.5} You know, the one with all the trees and grass?{w=0.5} South of Viridian?{w=0.5}"
        red @sadbrow talkingmouth "Does any of this ring a bell?"

        misty @closedbrow talkingmouth "Nope. Sorry."

        redmind @closedbrow frownmouth "Damnit! I was so close to a full conversation! Curse my humble upbringing!"

show misty surprisedbrow frownmouth with dis

red @happy "Anyway, I need to unpack my stuff. I shouldn't keep holding you up."

red @talkingmouth "Here, let me take your bags in for you. To make up for earlier."
red @surprised "...Huh. These are some awfully fancy bags. And what does that name tag say? Something about a Gym...?"

misty angry "Don't touch those!"

show misty:
    xpos 860 ypos 1080 zoom 1.0
    ease 0.4 zoom 1.2 ypos 1250 xpos 780
    
$ renpy.pause(0.5, hard=True)

red @confused "Uh, okay. Looks like you got it."

show misty angry:
    xpos 780 ypos 1250 zoom 1.2
    ease 0.5 zoom 1.0 ypos 1080 xpos 820

misty @talkingmouth "You-- inconsiderate, pigheaded-- you--"

show misty angry:
    xpos 820 zoom 1.0

misty @talkingmouth "Don't go around touching a girl's things!"

show misty angry:
    xpos 820 alpha 1.0
    ease 0.33 xpos 200 alpha 0.0
    
pause 0.33

$ PlaySound("Door_Slam.ogg")
show hall_A:
    yalign 0.0
    ease 0.03 ypos -10
    ease 0.03 ypos 10
    ease 0.03 ypos 0
    repeat 3

red @unamusedbrow frownmouth "[ellipses]"

if (persondex["Misty"]["Value"] == 2):
    redmind @happy "Nope, you're not turning me off that easily. I'm gonna be your friend, and there's nothing you can do about it."
elif (persondex["Misty"]["Value"] == -1):
    redmind @unamusedbrow frownmouth "...Ugh. I'm so done with her."
else:
    redmind @unamusedbrow frownmouth "I sense I've committed some sort of faux pas..."

hide misty

stop music fadeout 1.5

$ renpy.pause(1.5, hard=True)
    
scene dorm_empty_B with dis

$ PlaySound("Door_Open1.ogg")

$ renpy.pause(2.5, hard=True)

hide blank2

redmind @thonk "...?"
redmind @thinking "Something... is off."
redmind @thonk "It's like one of those games I played as a kid where I tried to spot the difference between two similar pictures."
redmind @thonk "Something is definitely out of place, but I can't put my finger on it."

$ PlaySound("Door_Close1.ogg")

show calem at leftside with dis
show brendan at rightside with dis
show ethan at centerside with dis

calem @talkingmouth "Is something wrong, [first_name]?"
red @confused "I'm... not sure."
calem @talkingmouth "Have you been drinking water? With all the excitement, it's easy to forget.{w=0.5} Dehydration is a killer."
brendan @surprised "Oh, crap. Does your head hurt? Stomachache, maybe?{w=0.5} Gimme a sec, I think May dropped some Lum Berries off in my bag!"

red @confused "In your bag[ellipses]?"
red @surprisedbrow talking2mouth "...bag."

pause 2.0

show dorm_empty_B:
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

queue music "Audio/Music/Found It.ogg" noloop
$ renpy.music.queue("Audio/Music/Sneaking Again.ogg", channel='music', loop=True, tight=None)

show brendan surprisedbrow frownmouth
show ethan surprisedbrow frownmouth
show calem surprisedbrow
with dis

red @angry "{size=42}My bag is gone!{/size}"

ethan @surprised "What? That black and yellow one, right?"

calem @sadbrow talkingmouth "Yes, I saw it too. Where was it last...?"

red @sad "Damn it, I need that! It's got pretty much everything except my clothes in it!"

brendan angrybrow @angry "Someone must've stolen it! I'll battle that asshole inside out!"

calem -surprisedbrow @talkingmouth "Be calm. Only us five and the staff can get in here."

red @confused "...Us {i}five?{/i}"

ethan @angry "Wait a minute... Hillenbrand isn't here!"

calem @surprised "...That's truly baffling."
calem @closedbrow talkingmouth "In any case, he might not be, but all his luggage is. It doesn't make sense for him to abscond with your backpack and leave all his possessions here at our mercy."

brendan @closedbrow sweat talking2mouth "Huh... that Roxanne chick. She said that there's a buncha security cameras, right?"

red @angrybrow happymouth "Yeah, that's right! Good thinking. I'm going to the security office right now."

pause 1.0

show calem sadbrow smilemouth with dis
show ethan closedbrow frownmouth sweat with dis
show brendan sadbrow frownmouth with dis

red -angrybrow @sad "Er..."

pause 1.0

calem @talking2mouth "Am I right in assuming that none of us know where the security office is?"

pause 1.0

red @closedbrow talking2mouth "Yep... But..."

show ethan -sweat happy with dis
show brendan happy with dis
show calem surprisedbrow frownmouth with dis

red @angrybrow happymouth "If we pick a direction and just start running, we're bound to run into it eventually!"

ethan @happy "Hell yeah!"

brendan @happy "Leg day, here we go!"

show brendan:
    xpos 0.75
    ease 0.4 xpos 1.5

show ethan:
    xpos 0.5
    ease 0.4 xpos 1.5

pause 0.4

$ PlaySound("Door_Slam.ogg")

pause 2.0

calem @sadbrow talkingmouth "That's... that's not how geometry works..."
calem @sadbrow frownmouth "[ellipses]"
calem happy "Oh, whatever. Wait up!"

show calem:
    xpos 0.25
    ease 1.0 xpos 1.5

pause 0.5

show blank2 with splitfadefast

$ renpy.pause(1.0, hard=True)

show lobby_night behind blank2
hide dorm_empty_B

$ renpy.pause(0.5, hard=True)
$ renpy.music.play("Audio/hall_crowd.ogg", channel='crowd', loop=True, fadein=1.5)

hide blank2 with splitfadefast

red @talking2mouth "Wha... what's everyone yelling and shouting about?"

show face with dis:
    xpos 0.6

face angrybrow @surprised "You again? Did you have something to do with this?"

red @confused "...What?"

show mace with dis:
    xpos 0.4

hide brendan

mace @talkingmouth "There was something skittering around the lobby a few minutes ago.{w=0.5} Whenever it touched someone, it blasted them with some kind of electricity. Though it seemed... buglike."

red @talkingmouth "What could that be? A Galvantula? Or a Charjabug?"

mace @surprised "Oh, so you know your Pokémon. Hmph. {nw}"
extend @talkingmouth "That being the case, you should know it couldn't have been a Charjabug since it moved too fast. Though it also seemed too small to be a Galvantula."

face @closedbrow talkingmouth "Didn't it look something like a bag? Like a yellow and black bag."

mace @closedbrow talkingmouth "I believe it rather did."

hide mace
hide face
with dis

show brendan with dis:
    xpos 0.75
    
brendan frownmouth @talking2mouth "Huh. That's a pretty big coincidence."

hide calem

if (profanity):
    red @confused "Coincidence, my ass!{w=0.5} What's my bag doing running around the lobby floor?!"
else:
    red @confused "Coincidence, my ***!{w=0.5} What's my bag doing running around the lobby floor?!"

show calem thinking with dis:
    xpos 0.25

calem @closedbrow talkingmouth "...Interesting.{w=0.5} What did you say you packed in your bag again, [first_name]?"

show calem surprisedbrow frownmouth with dis

red @closedbrow talking2mouth sweat "I didn't pack a Galvantula, I'll tell you that much!{w=0.5} Whatever's going on, all I know is that I need that bag back!"

show calem -surprisedbrow -frownmouth -surprised with dis

red @closedbrow talking2mouth "Which way did it go?"

hide ethan
show ethan with dis

ethan @talkingmouth "I mean, the commotion's that way. I'd just follow the screaming. But if we don't hurry, campus police'll probably get to it, first... or another student."

brendan @angry "Aw, hell no. That's your bag, right, [first_name]?{w=0.5} If you let those other guys get it before you, there's no tellin' what's gonna happen to your stuff!"
brendan @sad "I'm not entirely sure what's happenin' right now, but if something really weird {i}is{/i} in your bag, aren't you gonna be in huge trouble if they find out it's yours?"

calem @talkingmouth sadbrow "Arguably, we'd be in more trouble for interfering in the operations of the school's security team..."

ethan @surprised "Uh... I'll pass here. Whatever you think we should do is probably best."
     
red @closedbrow sweat talking2mouth "Whatever's happening, that's still my bag out there, and I want it back."
red @talkingmouth sad2eyes angryeyebrows "The situation's gone a little crazy, but that's all the more reason why I have to take care of it myself."

calem @closedbrow talkingmouth "If you say so.{w=0.5} I won't question your choice, so if you think this is for the best, then I'll follow along."
calem @happy "Anyway, somebody has to make sure you don't do something silly."

brendan @happy "Hell yeah! That bag's yours and we're not lettin' nobody touch it with their grubby hands!"
brendan @angry "You lead the way, [first_name]!{w=0.4} I'll be right behind you!"

ethan @happy "Allons-y!"

show blank2 with splitfade

$ renpy.pause(1.5, hard=True)

show text "{color=#ffffff}.{/color}" as text1:
    alpha 1.0
    pause 0.5
    ease 0.0 alpha 0.0
show text "{color=#ffffff}..{/color}" as text2:
    alpha 0.0
    pause 0.5
    block:
        ease 0.0 alpha 1.0
        pause 0.5
        ease 0.0 alpha 0.0
show text "{color=#ffffff}...{/color}" as text3:
    alpha 0.0
    pause 1.0
    block:
        ease 0.0 alpha 1.0
        pause 1.5
        ease 1.0 alpha 0.0

$ renpy.music.stop(channel='crowd', fadeout=1.5)

hide lobby_night

$ renpy.pause(3.0, hard= True)

show hall_B_night behind brendan:
    subpixel True
    xalign 0.5 yalign 1.0 zoom 1.0
    ease 2.5 xalign 0.5 yalign 1.0 zoom 1.07

hide blank2 with splitfade

$ renpy.music.play("Audio/hall_crowd.ogg", channel='crowd', loop=True, fadein=1.5)

$ renpy.pause(1.5, hard= True)

show calem surprisedbrow frownmouth with dis
show ethan surprisedbrow frownmouth with dis
show brendan surprisedbrow frownmouth with dis

red @surprised "I can hear people yelling.{w=0.5} We have to be getting close!"

show hall_B_night:
    xpos 960 ypos 1080 zoom 1.07

hide text
hide text1
hide text2
hide text3

ethan @surprised "Hey, over there, I see your bag!{w=0.5} It's.{w=0.25}.{w=0.25}.{w=0.5}{nw}"
extend @confused " really moving by itself?!"
calem @talkingmouth "Obviously not. Whatever's inside it must be propelling its locomotion."

show backpack with dis:
    alpha 1.0
    
pause 0.5

$ PlaySound("Pokemon/Moves/Paralyzed.ogg")

$ renpy.pause(1.0, hard=True)

show backpack

redmind @thinking "Sure enough, my bag's darting between people's legs like it's some kind of small Pokémon.{w=0.5} The bigger problem, though, are all the people trying to grab it...!"
red @angry "Hey, stop! That's mine!"

Character("Greedy Student") "\"No way, I saw it first!\""
Character("Rude Student") "\"Yeah, right! Finder's keepers, idiot!\""

red @wince talking2mouth "No, I mean it's {i}literally{/i} mine! It's got my name on it!"

brendan @happymouth angrybrow "Don't worry, [first_name], I got it!{w=0.5} I've dealt with this kind of thing b--"

$ PlaySound("thunder.ogg")
show blank:
    alpha 0.5
    pause 0.1
    alpha 0.0
    pause 0.1
    repeat 5

show backpack:
    parallel:
        xalign 0.0
        ease 0.03 xpos -20
        ease 0.03 xpos 20
        ease 0.03 xpos 0
        repeat 8
    parallel:
        yalign 0.0
        ease 0.03 ypos -20
        ease 0.03 ypos 20
        ease 0.03 ypos 0
        repeat 8

show hall_B_night:
    parallel:
        xalign 0.0
        ease 0.03 xpos -20
        ease 0.03 xpos 20
        ease 0.03 xpos 0
        repeat 7
    parallel:
        yalign 0.0
        ease 0.03 ypos -20
        ease 0.03 ypos 20
        ease 0.03 ypos 0
        repeat 7

show calem surprisedmouth deadbrow at leftside, monochrome behind backpack
show ethan surprisedmouth deadeyes surprisedeyebrows at monochrome behind backpack
show brendan surprisedmouth deadbrow at rightside, monochrome behind backpack

Character("Dormies") "\"{size=48}AaaaarrrRGBLRLBLRBLLBR{/size}\""

hide blank

hide backpack with dis

$ renpy.pause(1.0, hard=True)

show calem:
    ypos 1.0 xpos 0.25
    ease 1.0 ypos 1.1 rotate 5.0
show ethan:
    ypos 1.0
    ease 1.0 ypos 1.2 rotate -5.0
show brendan:
    ypos 1.0 xpos 0.75
    ease 1.0 ypos 1.15 rotate 7.0

$ renpy.pause(1.5, hard=True)

red @angry "Hey, guys!{w=0.5} Get a hold of yourselves!"

show calem:
    ypos 1.1 rotate 5.0 xpos 0.25
    ease 0.5 ypos 2.0 rotate 30.0
show ethan:
    ypos 1.2 rotate -5.0
    ease 0.5 ypos 2.0 rotate -30.0
show brendan:
    ypos 1.15 rotate 7.0 xpos 0.75
    ease 0.5 ypos 2.0 rotate 35.0

$ renpy.pause(0.5, hard=True)

$ PlaySound("Body Roll.ogg")

show hall_B_night with vpunch

$ renpy.pause(1.5, hard=True)

stop music
show flashback with dis

$ renpy.music.queue("Audio/Music/RelicCastle_Start.ogg", channel='music', loop=None, tight=None)
$ renpy.music.queue("Audio/Music/RelicCastle_Loop.ogg", channel='music', loop=True, tight=None)

redmind @thinking "Okay. Something's in my bag. Almost certainly an electric type. Fast, small. Not powerful, but determined to do whatever it's doing..."
redmind @thinking "Not a Rotom, because my bag's non-mechanical. It's staying on the ground, so it can't fly or levitate. It's able to see where it's going, so its head must be low to the ground--it runs on all fours."
redmind @thinking "Less than twenty inches long. Base speed of--at this tilt--somewhere in the range of eighty to one hundred."
redmind @thinking "Then... it could be a Pachirisu, a Minun, a Togedemaru, or even a--"

stop music
hide flashback
show hall_B_night with vpunch

security @talkingmouth "Watch out, kid!"

red @surprised "Gwaah!"

show hall_B_night with vpunch

red @wince angrymouth "{size=42}Can't dodge--!{/size}"

stop music fadeout 1.0

red @closedbrow talking2mouth ".{w=0.25}.{w=0.25}.{w=0.75}{nw}"
extend @closedbrow talking2mouth "Huh?"
red @confused "It's...{w=0.5} not doing anything."
red @thonk "[ellipses]"
red @happy "Well, why don't we just open you up and see what's happening here, huh?"

security @talkingmouth "H-Hey, kid! Don't make any sudden movements!{w=0.5} That thing's dangerous!"

$ PlaySound("Pokemon/Unzip Pikachu.ogg")
$ renpy.pause(3.0, hard=True)

$ renpy.music.queue("Audio/Music/New_Adventure_Start.ogg", channel='music', loop=None, tight=None)
$ renpy.music.queue("Audio/Music/New_Adventure_Loop.ogg", channel='music', loop=True, tight=None)

$ renpy.pause(1.0, hard=True)

red surprisedbrow frownmouth @surprised "This is...!{w=0.75}{nw}"

show redpika01:
    alpha 0.0 zoom 1.1 yalign 1.0 xalign 0.5
    ease 1.0 zoom 1.0 yalign 1.0 xalign 0.5 alpha 1.0

extend @talkingmouth ""

red @talkingmouth "[pika_name]?!{w=0.5} What... How--"

$ PlaySound("Pokemon/pikachu_happy3.ogg")

hide pikachu

pikachu happy_3 "Pipipi... Pika!"

hide calem
hide ethan
hide brendan

calem @sadbrow talking2mouth "...You brought a Pikachu?{w=0.5} You didn't mention that when I asked you what was in the bag."

red @surprised "No! I left him with my mom and...{w=0.25} how did you get here?{w=0.5} Did you stow away in my suitcase?!"

$ PlaySound("Pokemon/pikachu_excite5.ogg")

pikachu neutral_2 "Piii-kaaaa-chuuu!"

red @angry "Didn't I tell you to stay with Mom? Does she even know you're here right now?{w=0.5} What if I'd put you in the baggage hold? You could've frozen, you furry idiot!"

$ PlaySound("Pokemon/pikachu_sad.ogg")
pikachu neutral_4 "P-Pika...{w=0.5}{nw}"
$ PlaySound("Pokemon/pikachu_happy2.ogg")
extend pikachu neutral_2b " Pikaaaaa!~"

red @sad "...You wanted to see me that badly, huh?"
red @happy "Oh, how could I say no to you?{w=0.5} Welcome back, [pika_name]!"

$ PlaySound("Pokemon/pikachu_excite3.ogg")
pikachu @happy_3 "Pika pika!"

hide redpika01 with Dissolve(1.0)

pause 1.0   
     
stop music fadeout 2.0

redmind @happy "Alright! All's well that ends well. Except for...{w=0.5}{nw}"
extend @wince frownmouth " one problem."

$ renpy.music.queue("Audio/Music/Littleroot_Start.ogg", channel='music', loop=False, fadein=1.0, tight=None)
$ renpy.music.queue("Audio/Music/Littleroot_Loop.ogg", channel='music', loop=True, fadein=0.0, tight=None)

pause 1.0

security @talkingmouth "So, this is what's causing all the commotion.{w=0.5} Young man, is that your Pokémon?"

red @sad "Yes, Sir. He is."
    
security @talkingmouth "Young man, allowing your Pokémon to freely roam the residence hall is one thing, but endangering the students and faculty in this hall?"
security @talkingmouth "I'm afraid I'm going to have to ask you and your Pokémon to come with me to the office."

show calem at leftside with dis

calem @talkingmouth "Pardon, Sir, but I don't think that's very fair for [first_name] or his Pikachu."
calem @closedbrow talkingmouth "We can hardly blame him for being frightened by an unfamiliar environment.{w=0.5} He was only trying to reach [first_name] before everyone here began to aggravate him."
    
show brendan at rightside with dis

brendan @angry "Yeah, wait a sec! What's the big deal?{w=0.5} Pikachu was just tryin' to find [first_name] like any Pokémon would its Trainer!"
brendan frownmouth @angrybrow talking2mouth "You guys were the ones chasin' him around all over the place and freakin' him out so of course he's gonna shock some people!"

show ethan with dis

ethan frownmouth @angry "Yeah!{w=0.5} [first_name] didn't even know his Pikachu was in his bag."

calem @sadbrow talkingmouth "That being the case, isn't it sensible to assume the fault here lies somewhere, perhaps... closer to home?"

brendan @closedbrow talking2mouth "Right?{w=0.5} What kinda security system do you have where someone can {i}accidentally{/i} bring a whole-ass Pikachu in here?"    

security @talkingmouth "Hmph. {w=0.5}I see what you're doing, boys, but the rules are very clear here. I'll need to take this young man to the office, and if you interfere, I'll have to report you, too."

show calem surprisedbrow frownmouth with dis
show brendan surprisedbrow frownmouth with dis

ethan @surprised "R-report us?! For what?! Standing up for a friend?"

red @happy "Hey, guys, chill. Don't worry, I'll figure something out. Don't get in trouble for me."

show calem sadbrow frownmouth with dis
show brendan sadbrow frownmouth with dis

ethan @sad "B-but..."

pause 1.0

security @talkingmouth "That's better. Now, young man, come along and--"

show hilbert:
    xpos -0.5 zoom 1.0 ypos 1.0
    ease 0.5 xpos 0.3 zoom 1.2 ypos 1.1

show ethan surprisedbrow frownmouth:
    xpos 0.5
    ease 0.5 xpos 0.8

show brendan surprisedbrow frownmouth:
    xpos 0.75
    ease 0.5 xpos 0.9

show calem surprisedbrow frownmouth:
    xpos 0.25
    ease 0.5 xpos 0.7

show hall_B_night with vpunch

stop music

$ renpy.music.queue("Audio/Music/DragonDenStart_B.ogg", channel='music', loop=False, fadein=1.0, tight=None)
$ renpy.music.queue("Audio/Music/DragonDenLoop.ogg", channel='music', loop=True, fadein=0.0, tight=None)

hilbert angrybrow @angry "{size=42}Pathetic.{/size}"

security @talkingmouth "Y-young man...?"

hilbert @closedbrow talkingmouth "I live in the dormitory this bag came from. I was there before anyone else. I saw everything."

pause 1.0

hilbert @angry "What I saw was {i}pathetic{/i}. 'Security Team?' Don't make me laugh. You and your band of incompetents couldn't secure a pizza."
hilbert @talkingmouth "When was the last time {i}any{/i} of you passed a physical? And your communication? Laughable. I heard you arguing over which 'code' this was for five minutes."
hilbert @angry "You're direly lucky this was just a Pikachu. If it was anything bigger, people could have {i}died.{/i} Would that make you realize how unqualified you are to keep {i}anyone{/i} safe? Or will you just quit now?"

pause 1.0

hilbert sadbrow @talkingmouth "Get out of my sight."

hide hilbert with Dissolve(1.5)

pause 2.0

stop music 

show ethan -surprisedbrow -frownmouth:
    xpos 0.8
    ease 0.5 xpos 0.5

show brendan -surprisedbrow -frownmouth:
    xpos 0.9
    ease 0.5 xpos 0.75

show calem -surprisedbrow -frownmouth:
    xpos 0.7
    ease 0.5 xpos 0.25

$ renpy.music.queue("Audio/Music/New_Adventure_Start.ogg", channel='music', loop=None, tight=None)
$ renpy.music.queue("Audio/Music/New_Adventure_Loop.ogg", channel='music', loop=True, tight=None)

red @surprised "H-holy shit..."

ethan @talkingmouth "Dude.{w=0.5} Was Hillenbrand actually going easy on us before...?"

pause 1.0

red @sad "Uh, if it makes you feel any better, Sir, I don't think you did that bad a job...?"
red @thonk "[ellipses]"
red @confused "Wait, where'd he go?"

calem @closedbrow talkingmouth "Ran off that way.{w=0.5} Crying, I believe."

red @confused "Well, I guess we should start heading back to our room?{w=0.5} It's getting close to curfew, and Cheren hasn't become president yet, so..."

ethan @confused "Who?"

red @happy "Oh, he's great. He's this guy who's running for Student Council, and..."

pause 1.5

window hide
show blank2 with splitfade
stop music fadeout 1.5
$ renpy.pause(2.0, hard=True)

hide calem
hide ethan
hide brendan

$ renpy.music.queue("Audio/Music/SoaringIllusions_Intro.ogg", channel='music', loop=None, tight=None)
$ renpy.music.queue("Audio/Music/SoaringIllusions.ogg", channel='music', loop=True, tight=None)

$ renpy.pause(1.0, hard=True)

show phone_B behind blank2
show phone_A behind blank2
with fadeinbottom

show mom behind phone_A:
    xalign 0.5 zoom 0.95

mom sad "{i}Oh, I'm sorry, honey!{w=0.5} When he decided to follow you, I just couldn't bring myself to stop him!{/i}"
mom -sad @talkingmouth "{i}I meant to call you, but I don't think airplanes get reception when they're in the air!{/i}"
    
show dorm_empty_B behind phone_B

hide blank2 with dis

red sad "Then what about after I landed?"

mom @talkingmouth "{i}Well, by the time I remembered, I figured you would've already found him.{/i}{w=0.5}{nw}"
mom @happy "{i}Well, by the time I remembered, I figured you would've already found him. {fast}In fact, I was more surprised that you didn't call me first!{/i}"

hide blank2

show mom surprisedbrow frownmouth with dis

red @closedbrow talking2mouth "Ugh, Mom... you're lucky my roommate was there to cover for me or I would've been in big trouble!"

mom @happy "{i}Oh, how{/i} is {i}your roommate?{w=0.5} Is he a nice boy? Where is he from? What does he look like?{/i}"

hide hilbert

red @happy "Well, actually, I have four of them. But the one who covered for me was called Hilbert. He's, uh... a character."

show mom -surprisedbrow -frownmouth with dis

red @talkingmouth "Anyway, I'll tell you all about them tomorrow.{w=0.5} I still have some stuff to sort out before heading to bed."
red @sweat sadbrow talkingmouth "Getting ready for the first day of classes on Monday and all that."

mom @happy "{i}Oh, of course!{w=0.5} Good night, my beloved Champion! Talk to you tomorrow!{/i}"

show phone_B:
    ypos 1.0
    ease 1.0 ypos 3.0
        
show mom:
    parallel:
        ypos 1.0
        ease 1.0 ypos 3.0
    parallel:
        alpha 1.0
        ease 0.25 alpha 0.0
        
show phone_A:
    ypos 1.0
    ease 1.0 ypos 3.0

$ renpy.pause(2.0, hard=True)  


show hilbert with dis:
    xpos 0.2 xzoom -1

show ethan with dis:
    xpos 0.4

show brendan with dis:
    xpos 0.6

show calem with dis:
    xpos 0.8 xzoom -1

ethan @confused "So, hey, [first_name] and I are going to be swapping between electives, but what about you guys? Where will you be?"

brendan @angrybrow happymouth "Grass and Ground for me! I've got lots of experience with those, back home in Hoenn."

pause 1.0

brendan @happy "Oh, and Water, too! {i}Champion Wallace{/i} is teaching that class. Love that guy. His reign was the best Spring Break I ever had."

calem @talkingmouth "Fighting, Flying, and Fairy are my preferences. I may dabble in another elective or two, for variety, but I imagine I'm largely set."

pause 1.0

ethan @angrybrow talking2mouth "I was asking you, too, Hillenbrand."

hilbert @sadbrow talkingmouth "It's Hilbert."
hilbert @thinking "[ellipses]"
hilbert @closedbrow talkingmouth "And I'll be in Steel, Ice, and Ghost."

show hilbert at dissolveaway:
    xpos 0.2

pause 2.0

ethan happy "Of course he will. What an edgelord!"

show hilbert angry:
    xpos 0.2

show ethan surprisedbrow frownmouth with dis
show brendan surprisedbrow frownmouth with dis
show calem surprisedbrow frownmouth with dis

show dorm_empty_B at vpunch

pause 1.0


hilbert @talkingmouth "It's nothing like that! Ice is the most powerful offensive type, and steel is the most powerful defensive type! Choosing those two is just logical, and Ghost covers their Fighting weaknesses!"

pause 1.0

hilbert sadbrow talkingmouth "Tch. I don't need to explain myself to you."

show hilbert at dissolveaway:
    xpos 0.2

pause 2.0

show calem thinking with dis
show ethan thinking with dis

brendan frownmouth @sadbrow talking2mouth "Is... is that true? Are Ice and Steel the best types?"

calem @talkingmouth closedbrow "That depends on what you're looking for. Certainly, Steel types are known for their high defenses, and Ice types are known for their strong elemental advantages."
calem -closedbrow -thinking @talkingmouth "But Grass and Ground types can do many things that the average Steel type or Ice type entirely lacks."

show brendan -frownmouth with dis

ethan -thinking @happy "What he's saying is...{w=0.5} don't worry about it! No matter what you pick, you can't screw your education up {i}too{/i} badly."

calem @talkingmouth "As long as you restrict yourself to two or three types, that is. It's certainly possible to 'screw yourself over' by spreading yourself too thinly."

ethan @sad "Er...{w=0.5} yeah." 
ethan @happy "Hahaha.{w=0.5} I know that. Don't worry, I've got plans!"

red @happy "So do I! My plan right now, though, is to go to sleep!"
red @talkingmouth "You ready for bed, [pika_name]?"

$ renpy.sound.play("Audio/Pokemon/pikachu_excite2.ogg", channel="altcry", loop=None)
pikachu happy_2 "Pika!"

calem @surprised "You're not going to keep him in his Poké Ball?"

red @confused "No, why?"

stop music fadeout 2.0

calem @sadbrow talkingmouth "I...{w=0.5} Well, where do you usually put him before you go to bed?"

queue music "Audio/Music/Opening_Intro.ogg" noloop

red @talkingmouth "Right here with me.{w=0.5} Is that weird?"

calem @happy "No, I suppose not."

brendan @happy "I think it's weird!{w=0.5} But if you don't get shocked, then I guess it's fine?"

ethan @talkingmouth "It's not weird! My Pichu back home does that exact same thing."
ethan @closedbrow talking2mouth sweat "If I ever try to put her in her Poké Ball when I go to sleep, I wake up with her on my face at four in the morning."

brendan @surprised "Huh! Maybe I'm the weird one, then."
brendan @happy sweat "Whatever. I'm gonna hit the hay now, dudes.{w=0.5} Night, [first_name], Calem, Ethan, Hilbert, and [pika_name]!"

show brendan at dissolveaway:
    xpos 0.6

calem happy "Yes, goodnight, all."

show calem at dissolveaway:
    xpos 0.8

ethan happy "See y'all tomorrow!"

show ethan at dissolveaway:
    xpos 0.4
    
red -sadeyebrows -sadeyes @talkingmouth "Goodnight, guys."
red @happy "Let's get some sleep, [pika_name].{w=0.5} We've got plenty of things to do this weekend before classes start."

$ PlaySound("pokemon/pikachu_norm3.ogg")
pikachu neutral_2b "Pika."

window hide

show blank2 with Dissolve(1.0)
$ renpy.pause(1.0, hard=True)

show relichall_B with dis

redmind casual hatless night @closedeyes frownmouth "I'll admit. I'm a little scared that if I go to sleep now, I'll wake up and realize that getting into Kobukan Academy, which was always my dream, was just that--a dream."
redmind @sadbrow frownmouth "But now I know it's real.{w=0.5} My subconscious isn't clever enough to have [pika_name] hitch a ride to Kobukan in my luggage. Even my wildest fantasies of getting into Kobukan didn't have that."
redmind @happy "I'm glad he's here."
redmind @thinking sweat "...But we {i}really{/i} need to work on his patience."

window hide

scene blank2 with transball

stop music fadeout 1.0
$ renpy.pause(1.0, hard=True)

hide calem
hide brendan
hide ethan
hide hilbert

hide dorm_empty_B

$ renpy.pause(1.0, hard=True)

show text "{color=#ffffff}{size=40}Pokémon Academy Life{/size}{/color}":
    alpha 1.0 yalign 0.5 xalign 0.5
    pause 3.0
    linear 1.0 alpha 0.0
    
$ renpy.pause(4.0, hard=True)

$ renpy.movie_cutscene('images/videos/Intro.webm')
    
$ renpy.pause(2.0, hard=True)

jump day010405