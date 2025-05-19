label day010407:
call calendar(1) from _call_calendar_2
$ calDate = calDate.replace(day=7, month=4, year=2004)

$ timeOfDay = "Morning"

$ PlaySound("Alarm.ogg")
$ renpy.pause(4.0, hard=True)

redmind hatless casual tired @closedeyes frownmouth "Ughh..."

$ renpy.music.play("Audio/Morning_ambience.ogg", channel='crowd', loop=True, fadein=1.0)

scene dorm_A with transeye2

$ renpy.transition(dissolve)
show screen currentdate

$ renpy.pause(1.5, hard=True)

hide blank2

show ethan uniform at centerside with dis
show calem uniform at leftside with dis
show brendan uniform at rightside with dis

$ renpy.music.stop(channel='crowd', fadeout=1.0)

ethan @happy "Good morning, sleepyhead!"

calem @talkingmouth "Sleep well?"

red hatless casual @sadbrow talkingmouth "Ugh. Too well. I probably don't have much time to get changed and get to homeroom, do I?"

brendan @talking2mouth "'Fraid not. We just hung back to make sure you woke up."
brendan @happy "You snored like an Exploud!"

calem @closedbrow talkingmouth "Exploud? I would've thought Snorlax would be a more apt comparison."

brendan @happy "Yeah, probably, but I don't know what that is."

red -tired @talkingmouth "Hey, guys, focus up. Did anyone notice what time I went to bed last night?"

ethan @confused "What, like we'd watch you sleep? Nah, man."

pause 2.0

show ethan surprisedbrow frownmouth with dis:
    xpos 0.5
    ease 0.5 xpos 0.6
show brendan surprisedbrow frownmouth with dis:
    xpos 0.75
    ease 0.5 xpos 0.8
show calem surprisedbrow frownmouth with dis:
    xpos 0.25
    ease 0.5 xpos 0.4
show hilbert uniform:
    xpos -0.2 xzoom -1
    ease 0.5 xpos 0.2

hilbert @talkingmouth "1:12. In the morning, obviously."

pause 1.5

hilbert @surprised "What?"
hilbert @angry "You all are just unobservant."

show ethan surprisedbrow frownmouth with dis:
    xpos 0.6
    ease 0.5 xpos 0.5
show brendan surprisedbrow frownmouth with dis:
    xpos 0.8
    ease 0.5 xpos 0.75
show calem surprisedbrow frownmouth with dis:
    xpos 0.4
    ease 0.5 xpos 0.25
show hilbert uniform:
    xpos 0.2
    ease 0.5 xpos 1.2

pause 1.0

$ PlaySound("Door_Slam.ogg")

pause 1.0

show ethan -surprisedbrow -frownmouth 
show brendan -surprisedbrow -frownmouth
with dis

calem @closedbrow talking2mouth "If he keeps slamming that door, we're going to have to pay to repair it..."

brendan @surprised "Well, whatever, dude. One in the morning's way too late to stay up! You gotta put your health first."

red @closedeyes talkingmouth "Yeah, that was a bad idea. Won't happen again."

ethan @happy "Cool! And now that we've saved your life, you'll come with us to the Battle Hall after classes today, right?"

red @confused "Huh? Well, sure."

calem @closedbrow talkingmouth "For context, we were discussing it amongst ourselves, and decided we wanted to see if we could watch some battles."

brendan @talkingmouth "Yeah, the Battle Team's meant to be there, right? {w=0.5}{nw}"
extend @talkingmouth "I'm not all that interested in the Big BT, myself, but they're meant to be pretty huge in the school."

ethan @happy "Yeah, and I'm interested in 'em! So you'll come, right?"

red @happy "Yeah, of course. It'll be fun."

ethan @talkingmouth "Sick. First, though, we should really get to class. It's already--{w=0.5}{nw}"

show calem surprisedbrow frownmouth 
show brendan surprisedbrow frownmouth
with dis

extend surprisedbrow frownmouth @surprised "Wait, it's {i}what{/i} time?!"

red surprisedbrow frownmouth @surprised "Crap! You guys go on without me, I'll only slow you down!"

scene blank2 with splitfadefast

jump PickElective