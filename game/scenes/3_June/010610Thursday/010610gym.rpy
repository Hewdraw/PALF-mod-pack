label gym010610:

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
alder @surprised2 "Eh[ellipses] look at all those serious faces. I tell you {i}one{/i} story about how I used to have a fancy chair to sit on, and you suddenly all start acting like this class is a morgue."
alder @spunky2 "Relax. I'm still just Alder. Your goofy gym class teacher. Whatever I was before doesn't matter, except that it made me qualified for this job."

bruno norm @norm2 "Not necessarily. Skill in battle and skill as a teacher are very different skillsets."
bruno surprised @closedbrow talking2mouth "It is certainly possible to be skillful in one--but lacking in the other."

alder surprised @happy2 "And then there's you, who's crap at both!"

pause 1.5

bruno closedbrow smilemouth @closedbrow talkingmouth "Just for that, I will spend today's lunch period tutoring students in the usage of Stealth Rock."

alder @sadbrow talkingmouth "H-hey, Bruno, buddy, come on, {nw}"

show bruno:
    xpos 0.33
    ease 3.0 xpos -0.2

show alder:
    xpos 0.66
    pause 1.0
    ease 3.0 xpos -0.2

extend @sadbrow talkingmouth "{gradualsize=36-20}you know I was joking[ellipses] you don't need to do anything drastic[ellipses]{/gradualsize}" 

narrator "Alder's nervous pleading falls on deaf ears as everyone in Gym Class picks out a partner[ellipses]"

hide alder
hide bruno 
with dis

call pickgympartner() from _call_pickgympartner_3

python:
    battlechar = _return
    trainer1 = MakeRed()
    trainer2 = MakeTrainer(battlechar)

call Battle([trainer1, trainer2], uniforms = [True, True]) from _call_Battle_190

python:
    renpy.transition(dis)
    renpy.show(GetCharacterSprite(battlechar, 1, True))

$ RecordBattle("Week10ThursdayGym")
if (WonBattle("Week10ThursdayGym")):
    $ ValueChange(battlechar, 3)

    narrator "[battlechar] seems impressed!"

if (CanBunnyRecruit(battlechar)):
    redmind uniform @thinking "Maybe now would be a good time to bring up Saturday's party...?"
    call BunnyRecruit(battlechar, True) from _call_BunnyRecruit_11 

scene gym with dis

jump lunchtransition