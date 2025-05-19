label secondhomeroom010604:

scene blank2

play music "Audio/Music/Oak Intro.ogg" noloop
queue music "Audio/Music/Oak Class.ogg"

show homeroom behind blank2
    
$ renpy.transition(dissolve)
show screen currentdate

show oakbg
hide blank2 
with splitfade

$ PlaySound("BellChime.ogg")

oak "{gradualsize=20-36}...so, if you can find them,{/gradualsize} a Flying Gem combined with Acrobatics and the ability Unburden is an effective way to kill three birds with one stone!"
oak "Except, in most of these situations, it's the bird killing {i}you{/i}, with the help of a stone!"

pause 1.0

oak "Well, technically, it's a mineral, but... perhaps there's little point in quibbling over that."

$ PlaySound("BellChime.ogg")

pause 0.5

oak "Oh, the bell! A timely save. I was quite running out of steam. Go enjoy your weekends, but be sure to read up on Water-type move interactions for Monday's test!"

narrator "You have some time before your Battle Team meeting. Better spend it wisely!"

call freeroam() from _call_freeroam_41

stop music fadeout 3.0

scene stadium_empty
show screen currentdate
with Dissolve(2.0)

$ HealParty()

pause 0.5

show blue battleteam:
    xpos 1.0/9.0
show leaf battleteam:
    xpos 5.0/9.0
show sonia battleteam:
    xpos 8.0/9.0
show erika battleteam:
    xpos 6.0/9.0
show ethan battleteam:
    xpos 4.0/9.0
show silver battleteam:
    xpos 2.0/9.0
show bea battleteam behind ethan:
    xpos 3.5/10.0
show hilbert battleteam behind sonia:
    xpos 7.0/9.0
with dis

pause 1.0

show smoke:
    animation
    alpha 0.0 yalign 3.0 xalign 0.5
    parallel:
        ease 3.0 yalign 0.5
    parallel:
        ease 0.5 alpha 1.0
        pause 0.5
        ease 3.0 alpha 0.0 

pause 2.0

stop music
show screen songsplash("Fuchsia City", "Zame")

queue music "Audio/Music/fuchsia_start.ogg" noloop
queue music "audio/music/fuchsia_loop.ogg"

pause 1.0

show blank
show janine behind blank

pause 0.1

hide smoke
hide blank

show lance:
    xpos 1.1 ypos 1.0
    ease 0.5 xpos 0.66

show janine behind lance:
    ease 0.5 xpos 0.33

pause 1.0

janine @closedbrow talking2mouth "Line up."

show blue:
    ease 0.8 xpos 1.5
show leaf:
    ease 0.5 xpos -0.5
show erika:
    ease 1.0 xpos 1.5
show ethan:
    ease 0.4 xpos 1.5
    pause 0.2
    ease 0.4 xpos -0.5
show silver:
    ease 0.5 xpos -0.5
show bea:
    ease 0.5 xpos 1.5
show sonia:
    ease 0.5 xpos 1.5
show hilbert:
    ease 0.5 xpos -0.5

janine @talking2mouth "Who's been watching that Millennium Drop contest?"

if (HasEvent("Professor Oak", "ParticipateMDTryouts") or HasEvent("Professor Oak", "WatchMDTryouts")):
    narrator "You, Leaf, Ethan, and Blue raise their hands."

else:
    narrator "Leaf, Ethan, and Blue raise their hands." 

janine @talking2mouth "Now, who's {i}participated?{/i}"

narrator "Leaf, Ethan, and Blue lower their hands."

if (HasEvent("Professor Oak", "ParticipateMDTryouts")):
    narrator "You are now the only one with a hand still raised."
    
    janine @talking2mouth "[first_name]?"

    if (HasEvent("Game", "WonMDTryouts")):
        red battleteam @talkingmouth "Won't take time from the Battle Team, I promise."
    else:
        red battleteam @sadbrow talkingmouth "I didn't win. So it won't take time from the Battle Team, I promise."

    janine @closedbrow talking2mouth "See that it doesn't."

    janine @talking2mouth "If your attention is divided, I'll notice. And I'll correct you."

    if (HasEvent("Janine", "Domming")):
        narrator "You bow your head submissively, and Janine lets out a low chuckle, quiet enough you don't think anyone else heard."

        red @downeyes frownmouth lightblush "[ellipses]"
    
    else:
        red @talking2mouth "I promise you won't need to."

    $ ValueChange("Janine", 5, 0.33)
    janine @talking2mouth "Good."

else:
    $ ValueChange("Janine", 5, 0.33)
    janine @talking2mouth "Good. That's what I want to see. You don't have time to be both a Coordinator and a Battler."
    janine @talking2mouth "If you're going to give yourself to something, you need to give {i}all{/i} of yourself. Right now, you're the Battle Team's--you're {i}mine{/i}."
    janine @closedbrow talking2mouth "Stay focused on {i}our{/i} mission. The national tournament."

janine @closedbrow talking2mouth "I don't have any special instruction for today. We'll go through the same drills--just harder and faster than last time."

janine @talking2mouth "Any questions?"

show hilbert battleteam:
    xpos 0.75

show lance:
    xpos 0.66
    ease 0.5 xpos 0.25

show janine:
    xpos 0.33
    ease 0.5 xpos 0.5

pause 1.0

janine @talking2mouth "Go ahead."

hilbert @talking2mouth "If we pass through all four Quarter Qlashes, we can enter the National Tournament, right?"

janine @talking2mouth "Yeah."

hilbert @talking2mouth "The winner of the National Tournament can challenge the Kobukan Champion?"

janine @talking2mouth "You're still there. What's the question?"

hilbert @talking2mouth "Why is the champion seat empty?"

lance @talking2mouth "Some people cannot handle the burden of Championship. The former Champion was neither a Kobukan student, nor a member of the Battle Team." 
lance @angrybrow talking2mouth "If they {i}were{/i}, they surely would have had the werewithal to stick around for longer than the crowning ceremony."

#janine @closedbrow talking2mouth "I... was only looking for the strong, last year. There were some people I turned away I shouldn't have."

#lance @closedbrow talking2mouth "Janine's rejection was correct. The champion's seat was empty a day after the crowning. If a Battle Team member had done that[ellipses]"
lance @closedbrow talking2mouth "This was embarrassing for Kobukan--not only that we were beaten by one who did not even attend our academy, but that we were beaten by one of so little quality of character."#It would have brought further embarrassment to Kobukan. It was embarrassing enough that a Kobukan student abandoned the post so quickly."

hilbert @closedbrow talking2mouth "So whoever wins the National Tournament this year will become Kobukan Champion. No challenge necessary."

janine surprisedbrow @talking2mouth "That's the plan."

hilbert @talking2mouth "Do you think that Kobukan will ever have a traditional eight-gym system?"

janine -surprisedbrow @closedbrow frownmouth "[ellipses]Hm."
janine @talking2mouth "No. Not until some actual Kobukanians start attending this school, at any rate."

lance @sad2eyes talking2mouth "One must imagine Kobukan both a blessing and curse to the Inspirans. Kobukan supports their economy and brings in wealthy tourists and short-term residents from across the globe."
lance @closedbrow talking2mouth "At the same time, this academy's existence guarantees that every skilled trainer who ever existed in Kobukan must one day return home."

hilbert @talking2mouth "Thank you."
hilbert @closedbrow talking2mouth "No further questions."

hide hilbert with dis

janine @talking2mouth "Alright. Lance and I will help your Pokémon remember any moves you need."
janine @talking2mouth "Though... that's kind of a misnomer. There are some moves that Pokémon can learn, even from level one. They just need to be taught them by a trainer who knows how."
janine @talking2mouth "Even if you think you don't have any moves you want your Pokémon to remember, try it out. See what your options are."

hide janine with dis

show lance:
    xpos 0.25
    ease 0.5 xpos 0.5

pause 1.0

lance @talking2mouth "Rowan informed me you battled him earlier today."

red @talking2mouth "Yeah. I assume I disappointed you, somehow?"

if (not WonBattle("Rowan1")):
    lance @talking2mouth "You did not win. That's disappointment enough."
else:
    lance @talking2mouth "This time, you have managed to narrowly escape my disappointment."

if (HasEvent("Professor Rowan", "FledBattle")):
    red @talking2mouth "He told you {i}why{/i} I didn't win, though. The hurt Dodrio?"

    lance @talking2mouth "I stand by my previous assertion."

red @unamusedbrow unamusedmouth "[ellipses]"

lance @talking2mouth "You know what has been asked of me. I am here to provide."

label movetutor604:

call screen SelectMon
$ tutormon = _return

if (tutormon == 'back'):
    lance @closedbrow talking2mouth "Are you certain?"

    menu:
        "I don't want to teach any of my Pokémon a new move.":
            lance @closedbrow talking2mouth "Very well."

        "On second thought...":
            jump movetutor604

elif (tutormon == pikachuobj):
    lance @talking2mouth "I am unable to teach this... creature. I cannot begin to determine what skills it may have possessed in the past."

    jump movetutor604

else:
    $ tutormon = _return
    $ tutormonname = pokedexlookup(tutormon.GetId(), DexMacros.Name)

    lance @talking2mouth "Your [tutormonname]. Very well."
    
    $ rememberablemoves = GetRememberableMoves(tutormon)

    if (len(rememberablemoves) == 0):
        lance @talking2mouth "This Pokémon has no moves I can teach it. Avoid wasting my time."

        jump movetutor604

    else:        
        lance @talking2mouth "Fine. What do you want me to teach this Pokémon?"

        $ learnmove = renpy.call_screen("rememberablemoves", tutormon)

        if (learnmove == "Back"):
            lance @talking2mouth "Avoid wasting my time."

            jump movetutor604

        else:
            $ tutormon.LearnNewMove([(0, learnmove)])

            if (learnmove not in tutormon.GetMoveNames()):
                jump movetutor604

lance @talking2mouth "It is done. I take my leave of you."

hide lance with dis

pause 1.0

show janine with dis
hide ethan

janine @talking2mouth "Alright, we're all done here?{w=0.5} Yeah?{w=0.5} Good.{w=0.5} We're going to spar, now. I'll pick one of you at a time, and add more opponents to the fight until you fall."

ethan battleteam @angrybrow talkingmouth "A Zerg rush of BTers... kekekeke."

janine @closedbrow talking2mouth "I could pretend I'm picking randomly, but we all know I'm not, so, [first_name], you're first on the chopping block."

red @happy "Ready to go down swinging, Janine."

if (HasEvent("Janine", "Domming")):
    janine @blush sadbrow talking2mouth "Yeah, well, stay up for as long as you can. If it's over too fast, I'll be... disappointed."

else:
    janine @closedbrow talking2mouth "Make sure you do."
  
call clearscreens() from _call_clearscreens_264 
scene blank2 with splitfade

$ BattleTeamTraining()

narrator "After beating off more of your teammembers in a row than you thought you could, Janine finally releases you."

red battleteam @closedbrow talking2mouth "Phew. She really knows {i}right{/i} where the edge is, and how to take us to it, huh?"

ethan battleteam @confusedbrow frownmouth "[ellipses]"

leaf battleteam @closedbrow talkingmouth "{size=30}I'm not going to say it, Ethan, but {i}someone{/i} has to.{/size}"

red @happy "C'mon, guys, let's get back to the dorm. Dibs on first shower."

jump day010605