label gym010406:

$ timeOfDay = "Noon"

  

play music "Audio/Music/Gym_Start.ogg" noloop
queue music "Audio/Music/Gym_Loop.ogg"

$ renpy.transition(dissolve)
show screen currentdate

scene gym with dis

show blank2 behind gym

$ renpy.pause(2.0, hard=True)

hide blank2

show alder norm2 with dis:
    xpos 0.66

show bruno think with dis:
    xpos 0.33

alder @talkingmouth "Welcome back, everyone.{w=0.5} Are you all ready for a productive day here in the gym?"
alder happy2 "Well, it really doesn't matter if you are, because you're gonna have one whether you like it or not.{w=0.5} That's what the school pays us to make you do, ha ha!"
alder norm2 "I'll bet all of you are wondering just exactly what I'm talking about."
alder spunky2 "Well, I'll show you."

show bruno think:
    xpos 0.33
    ease 0.7 xpos 0.25

show alder norm2:
    xpos 0.66
    ease 0.5 xpos 0.5
    
alder @talkingmouth "Come on out!"

show alder norm:
    xpos 0.5

$ renpy.music.play("Audio/Pokemon/Volcarona_Ball.ogg", channel="altcry", loop=None)

show volcarona at pokeball behind alder:
    xpos 800 + 800 ypos 1080 zoom 1.8

$ renpy.pause(1.0, hard=True)

show volcarona:
    subpixel True
    zoom 1.8 ypos 1080 xpos 800 + 800
    block:
        parallel:
            ease 1.0 ypos 900
            ease 1.3 ypos 1040
            ease 0.9 ypos 930
            ease 1.5 ypos 1080
            ease 1.2 ypos 905
            ease 1.4 ypos 1160
        parallel:
            ease 0.8 xpos 750 + 800
            ease 1.4 xpos 825 + 800
            ease 1.1 xpos 860 + 800
            ease 1.6 xpos 830 + 800
            ease 1.25 xpos 775 + 800
            ease 1.3 xpos 800 + 800
        repeat

show bruno think:
    xpos 0.25

pause 1.0

blue uniform surprised "A Volcarona--?!"

hilbert uniform @talkingmouth "As expected from Unova's Champion..."

bianca uniform @excitedeyes talkingmouth "Wow--!{w=0.5} {cps=200}That's so cool! Oh gosh, look at its wings, they're, like, the prettiest things I've ever seen!{/cps}{w=0.4}"
show alder happy with dis
bianca @happy "Can I take a picture real quick?"

may uniform angrybrow ".{w=0.2}.{w=0.2}.{w=0.2}{nw}"
extend @talkingmouth "I'm going to get a Volcarona."

alder norm2 "Settle down, class, I'm only using her as a demonstration."
alder norm2 "Bruno, bring out the dummy."
show alder norm with dis

hide bruno with dis

pause 1.5

show balloonbot with dis:
    subpixel True
    yalign 0.5 xpos -0.5#    xalign -2.0
    parallel:
        ease 0.9 xpos 0.05
    parallel:
        ease 1.5 yalign 0.4
        ease 1.3 yalign 0.8
        ease 1.6 yalign 0.5
        ease 1.4 yalign 0.7
        repeat

show bruno norm with dis:
    xpos -100
    parallel:
        ease 0.75 xpos 200

pause 1.0

show bruno norm2:
    xpos 200

show balloonbot:
    block:
        ease 1.5 yalign 0.4
        ease 1.3 yalign 0.8
        ease 1.6 yalign 0.5
        ease 1.4 yalign 0.7
        repeat

bruno @talkingmouth "Is this good?"
show bruno norm with dis
alder norm2 "That's perfect."
show alder norm

calem uniform @surprised "A balloon bot?{w=0.5} Are we Super Training today?"

hide ethan
ethan uniform @closedbrow talkingmouth "'Super Training?'{w=0.5} That sounds like something out of a video game."

alder happy2 "Ha ha, no, not today. It's still too early in the semester for that.{w=0.5}{nw}"
extend norm2 " Today, it'll be something a little simpler."
show alder norm with dis

ethan @surprised "So Super Training is a real thing...?"

show bruno think with dis
alder happy2 "Let's get started!"

hide alder          
hide bruno
hide volcarona
hide balloonbot
with dis

$ trainer1 = MakeTrainer("Alder", TrainerType.Ally)
$ trainer2 = Trainer("bruno", TrainerType.Enemy, [Pokemon(pokedexlookupname("Balloon Bot", DexMacros.Id), level=70, moves=[GetMove("Splash")], gender="Unknown")])

call Battle([trainer1, trainer2], customexpressions=["alder", "alder spunky2", "bruno", "bruno angry3"], gainexp=False) from _call_Battle_1

stop music fadeout 1.0
pause 1.0

show alder norm3 with dis:
    xpos 0.66

show bruno think with dis:
    xpos 0.33

$ renpy.music.play("Audio/Music/Gym_Loop.ogg", channel='music', loop=True, fadein=1.25, tight=None)
    
$ renpy.transition(dissolve)
show screen currentdate

$ renpy.pause(1.5, hard=True)

$ _game_menu_screen = "game_menu"

hide blank2

show alder norm4
alder @talkingmouth "Now... who was it that said 10-year-olds can get by here.{w=0.25}.{w=0.25}.{w=0.7}{nw}"

extend happy2 " Ah-ha, there you are."

show alder norm:
    xpos 0.66 xzoom 1
    ease 0.75 xpos 0.5 xzoom -1

show bruno norm:
    xpos 0.33
    ease 1.0 xpos 0.25

show blue uniform with dis:
    xpos 0.75 xzoom -1

$ renpy.pause(1.0, hard=True)

show alder:
    xzoom -1 xpos 0.5

show bruno:
    xpos 0.25

alder norm3 "Hmm..."
alder norm2 "Oh, that's right!{w=0.5} You're the one interested in joining the academy's Battle Team."

show blue angry with dis

alder @talkingmouth "Are you serious about that, boy?"

show alder norm with dis

show bruno norm with dis

blue @talkingmouth angrybrow "Yeah, that's right!{w=0.5} Why wouldn't I be?"

blue @happybrow talking2mouth "It's obviously the perfect stepping stone for me and becoming World Champion!"
show blue -angry with dis

$ renpy.music.play("Audio/hall_crowd.ogg", channel='crowd', loop=True, fadein=0.5)
pause 1.5

alder @talkingmouth "Hmm.{w=0.25}.{w=0.25}.{w=0.5}{nw}"
extend norm2 " so that's your goal.{w=0.5} World Champion."

alder norm "Hmm.{w=0.25}.{w=0.25}.{w=0.5}{nw}"
extend happy2 " I'm sorry, there's a whole lot of you in this class and I haven't memorized everyone's names yet."

alder norm2 "You are?"
show alder norm with dis

blue @talkingmouth "Blue."

redmind uniform @thonk "I'm surprised he didn't include his last name.{w=0.5} I bet it could've at least triggered some response from Alder or Bruno."

alder norm2 "You! In the red hat!"
show alder norm with dis

red @surprised "H-Huh?"

calem uniform @talkingmouth "He's definitely not looking at me."
hilbert uniform @closedbrow talkingmouth "Nor me."
bianca happy uniform "Right? It's confusing, isn't it?"

red @talkingmouth "Uh, Sir?"

show blue surprisedbrow frownmouth with dis

alder happy2 "Yes! Yes, you.{w=0.5}{nw}"    
extend norm2 " What's your name?"
show alder norm with dis

show blue -surprisedbrow -frownmouth -surprised with dis

red @talkingmouth "Uh, [first_name]. [first_name] [last_name]."

show blue surprisedbrow frownmouth with dis
alder happy2 "[first_name]!{w=0.6} Why don't you and Blue have a spar right here in front of your fellow classmates?"
show alder happy with dis

show blue happybrow with dis

red surprisedbrow frownmouth @surprised "What?"

show bruno think with dis
alder happy2 "You heard me."
show alder happy with dis

blue @happy "Perfect!{w=0.5} I've been waiting for this!"
show blue -happy with dis
    
ethan uniform surprised "Oh, geez, Alder's really going to make you do it? Guess he doesn't know about your history with [blue_name]."
ethan happy "Still, you've got this!"

calem uniform happy "Good luck, [first_name]. I trust in your ability."
brendan uniform happy "Kick his ass, bro!"
may uniform happy "We're all cheering for you!"
hilbert uniform angrybrow "Don't disgrace our dorm."
serena uniform happymouth closedbrow "Please, give us a show."

show blue scaredbrow frownmouth with dis

TempCharacter("{color=#f2a634}???{/color}") "{size=30}You can do it, Blue!{/size}"

show blue angry with dis

redmind @thonk "Huh? Who said that?"
redmind @thonk "...I don't see anyone. Are they just... short?"

leaf uniform talkingmouth "First battle of the new school year? You better make this count."
leaf flirttalk "No pressure."

red @confused "None received."

hide alder happy           
hide bruno think
hide blue
with dis
    
$ trainer1 = Trainer("red", TrainerType.Player, playerparty)
$ trainer2 = Trainer("blue", TrainerType.Enemy, [Pokemon(pokedexlookupname("Eevee", DexMacros.Id), level=5, moves=[GetMove("Tackle"), GetMove("Sand Attack"), GetMove("Tail Whip"), GetMove("Growl")], gender=Genders.Male, ability="Run Away")])#Eevee

call Battle([trainer1, trainer2], uniforms=[True, True], gainexp=False) from _call_Battle_2
$ battlehistory["Blue1"] = _return

stop music fadeout 1.0
pause 1.0

show alder norm with dis:
    xpos 0.5 xzoom -1

show bruno norm with dis:
    xpos 0.25
    
if WonBattle("Blue1"):
    show blue uniform angry with dis:
        xpos 0.75 xzoom -1
else:
    show blue uniform with dis:
        xpos 0.75 xzoom -1

$ renpy.music.queue("Audio/Music/Gym_Loop.ogg", channel='music', loop=True, fadein=1.25, tight=None)

hide blank2 with dis
    
$ renpy.transition(dissolve)
show screen currentdate

$ renpy.pause(1.5, hard=True)

hide blank2

if WonBattle("Blue1"):
    blue @angry "N-No way!{w=0.5} I was just careless!"
    red uniform @happy "Great job, [starter_name]!"

else:
    blue @happy "Yeah! Am I great or what?"
    red uniform @sad "Oh, no... I'm sorry, [starter_name]."

alder happy2 "Nicely done! That was a good battle.{w=0.5}{nw}"
extend norm2 " You both should be proud of yourselves and your Pokémon."

alder @talkingmouth "Speaking of which, let's get them fixed up."

show alder norm with dis

pause 0.5

$ renpy.music.set_volume(0.0, delay=0.0, channel="music")
$ PlaySound("recovery.ogg")
$ HealParty()
pause 2.5
$ renpy.music.set_volume(1.0, delay=1.0, channel="music")

show alder norm2:
    xpos 0.5 xzoom -1
    ease 0.5 xpos 0.66 xzoom 1

show bruno norm:
    xpos 0.25
    ease 0.5 xpos 0.33

hide blue with dis

alder @talkingmouth "Once again, thank you, Blue and [first_name], for showing us a fine Pokémon battle.{w=0.5}{nw}"

extend norm2 " The Pokémon certainly looked like they were enjoying themselves."

alder @talkingmouth "Remember to always keep this in mind. Pokémon battles aren't just about winning.{w=0.5} What matters most is how you and your Pokémon work together as a team."
show alder norm with dis

$ PlaySound("BellChime.ogg")

show bruno think with dis
alder happy2 "And that'll be all for today.{w=0.5} Enjoy the rest of your day!"
show alder norm with dis

show blank2 with dis

stop music fadeout 1.5

$ renpy.transition(dissolve)
call clearscreens from _call_clearscreens_17 

$ renpy.pause(2.0, hard=True)

scene blank2
    
show afternoon at vspaz
    
pause 3.5

jump lunch010406