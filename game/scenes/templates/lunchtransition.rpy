label lunchtransition:

$ PlaySound("BellChime.ogg")

pause 2.0

$ showingboth = renpy.showing("bruno") and renpy.showing("alder")

if (not renpy.showing("bruno")):
    show bruno think:
        xpos -0.2 xzoom -1

if (not renpy.showing("alder")):
    show alder norm:
        xpos 1.2 xzoom -1

python:
    if (not showingboth):
        LineUp(duration = 1.0)
    scenecount = 8#ADDRESS THIS IF YOU ADD MORE SCENES
    scenechoice = RandInt(0, scenecount - 1)
    renpy.jump("lunchtransition" + str(scenechoice))

label lunchtransition0:
    alder happy2 "That'll be all for today.{w=0.5} Enjoy the rest of your day!"
    jump afterlunchtransition

label lunchtransition1:
    alder happy2 "Geez, is that the bell already? Go on, then. Get out of here!"
    jump afterlunchtransition

label lunchtransition2:
    alder happy2 "Looks like class is over, then. Keep an eye out for sharp rocks on the ground! Don't go stepping on any!"
    jump afterlunchtransition

label lunchtransition3:
    alder happy2 "Oh, is it time for lunch already? Fantastic! I'm famished."
    jump afterlunchtransition

label lunchtransition4:
    $ level = AimLevel()
    narrator "As the class files out, Alder addresses another student, nervously holding a Poké Ball."
    alder happy2 "Level [level]? No, kid, don't worry about it, that's exactly where you should be. You relax, and go enjoy the rest of your day."
    jump afterlunchtransition

label lunchtransition5:
    narrator "As the class files out, Alder addresses another student who's kicking the ground angrily."
    alder happy2 "Ah, rookie mistake. You never let your opponent get off that {i}third{/i} Quiver Dance. That's the killer. Good fundamentals, though! Go have some lunch--you'll do better next time."
    jump afterlunchtransition

label lunchtransition6:
    alder happy2 "Hey, those battles today were pretty 'lit!' All your Pokémon were absolutely 'on fleek', 'fam.' No 'cap.'"
    narrator "Alder's knowledge of modern slang continues to embarrass..."
    jump afterlunchtransition

label lunchtransition7:
    alder happy2 "Those were some good battles today! I'm confident that our leagues are in good hands, with you students taking the reins."
    jump afterlunchtransition

label afterlunchtransition:

scene blank2 with dis

stop music fadeout 1.5

$ renpy.transition(dissolve)
call clearscreens from _call_clearscreens_51

pause 1.0

$ HealParty()
    
show afternoon at vspaz
    
pause 3.5

$ timeOfDay = "Afternoon"

show cafe behind blank2
$ renpy.music.play("Audio/bigcrowdloop.ogg", channel='crowd', loop=True, fadein=0.5)

queue music "Audio/Music/Route 1 Anime.ogg"

$ renpy.transition(dissolve)
show screen currentdate

hide blank2 with splitfade
$ renpy.pause(0.5, hard=True)

hide afternoon

$ jumpto = "lunch"
$ jumptoyear = "01"
$ jumptomonth = ("0" if calDate.month < 10 else "") + str(calDate.month)
$ jumptodate = ("0" if calDate.day < 10 else "") + str(calDate.day)
$ renpy.jump(jumpto + jumptoyear + jumptomonth + jumptodate)