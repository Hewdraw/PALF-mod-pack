label bugelective:

$ renpy.transition(dissolve)
show screen currentdate

scene map
show blank2:
    alpha 0.8

show classroom
show bugtype:
    xalign 0.5 yalign 1.0
with dis

$ location = "bug"
$ passedclass = False

############################################################################################################################################################################################################################
#### 13. BUG         #######################################################################################################################################################################################################
############################################################################################################################################################################################################################
$ renpy.pause(1.0, hard=True)

call klaraevent from _call_klaraevent
call rosaevent from _call_rosaevent
call ethanevent from _call_ethanevent
call skylaevent from _call_skylaevent_1
call mayevent from _call_mayevent

label afterbugsetup:

if (HasEvent("Burgh", 2.1)):
    menu:
        "{b}>General Studies{/b}":
            pass

        ">Ask for move tutoring":
            jump movetutorbug

        ">Craft items" if (HasEvent("Burgh", 3.1)):
            jump itemcraftbug

if (not HasEvent("Burgh", 1)): #first class
    $ AddEvent("Burgh", 1)
    $ renpy.pause(1.0, hard=True)

    ethan uniform @confusedeyebrows talking2mouth "Okay, I see plenty of students in here, but where's the--"

    show bugsy:
        xpos 2.0
        ease 0.66 xpos 0.5

    $ AddEvent("Bugsy", "RenamedInstructor")
    $ BecomeNamed("Bugsy")

    bugsy @happy "Hey there, strangers! I'm Bugsy! Welcome to Kobukan's most buzzed-about class, where you'll be studying {color=#0048ff}Bug-type Pokémon{/color}!"

    if (not IsDate(5, 4, 2004)):
        bugsy @talkingmouth "Are you guys transfering in? {i}Wow{/i} did you make the right call."
        bugsy @happy "No offense to, um, all of the other instructors--they're all great, sorta, mostly--but this is one zillion percent the place you wanna be."

    bugsy @talkingmouth "There's just {i}so much{/i} to learn--like all the species of bugs, and where they live, and how their anatomy works, and about their evolution, and about their {i}evolution{/i} evolution--"
    bugsy @happy "--and just wait until we get into Bug-type fossils! Oh, and we'll get to see {i}plenty{/i} of the little guys up close and personal, especially when we're drawing them--"
    ethan @surprised "Drawing them?"
    bugsy @talkingmouth "Oh, yeah! There's gonna be sculpting, too, and I bet Valerie will come by and show off her Bug-inspired designs--she's working on this {i}great{/i} Ribombee dress, and when it's done--"
    red uniform @sadeyebrows talkingmouth "Um, Instructor Bugsy? We really appreciate the welcome, but maybe we could sit down before--"
    bugsy @surprised "Wait."
    pause 0.5
    bugsy @surprisedbrow talking2mouth "...Instructor?"
    pause 1.0
    bugsy @happy "HAhahAHhaHahAHAhaAhHAHahAhHAHa!!"
    bugsy @happy "{size=40}Hey, Burgh! We've got two more new guys!{/size}"
    ethan @unamusedeyebrows talking2mouth "I am so lost."
    show bugsy with dis:
        xpos 0.5
        ease 0.5 xpos 0.33
    show burgh with dis:
        xpos 2.0
        ease 1.0 xpos 0.55
    $ BecomeNamed("Burgh")
    $ RemoveEvent("Bugsy", "RenamedInstructor")
    burgh @norm2 "Oh! Hello, there--I'm sorry I didn't see you come in!"
    burgh @happy2 "Welcome to your first {color=#0048ff}Bug-type class{/color}. As I'm sure Bugsy has explained, I'm your instructor, Burgh."
    ethan @unamusedeyebrows talking2mouth "Mostly Bugsy's explained that bugs are super great. And that we're gonna be drawing them, apparently."
    burgh @happy2 "They're quite right, on both counts."
    red @confused "Wait, so, Bugsy is...?"
    bugsy @happy "Burgh's my dad. I've seen him teach this class, like, three times."
    burgh @norm2 "And now you're a proper student. Which means no parental favoritism--and that you {i}really{/i} shouldn't be ruining your uniform before class."
    bugsy @surprised "But the Combee in that thornbush was {i}female{/i}! And you said it was an awesome tackle!"
    burgh @norm2 "{size=30}...It was.{/size}"
    burgh @happy2 "Go on, now--class will be starting in just a moment."
    show bugsy with dis:
        xpos 0.33
        ease 0.5 xpos -0.5
    show burgh with dis:
        xpos 0.55
        ease 0.5 xpos 0.5
    hide bugsy with dis
    burgh @happy2 "Apologies for the confusion. I'm sure you'll find that Bugsy's enthusiasm is one of their greatest strengths. Why don't you find your seats as well?"
    red @happy "Sure thing, Instructor."
    
    show burgh norm:
        alpha 1.0
        ease 0.5 alpha 0.0

    hide burgh
    pause 0.5
    
    show burghbg:
        alpha 0.0 xalign 0.5 yalign 1.0
        ease 0.5 alpha 1.0
    
    burgh "Welcome to your {color=#0048ff}Bug-type class{/color} for this semester.{w=0.5} As you might have guessed, I'm your instructor, Burgh."
    
    $ BecomeNamed("Burgh")
    burgh happy2 "Please do just call me Burgh. None of this 'Mr. Burgh' or 'Instructor Burgh' nonsense."
    burgh norm2 "I'd rather you think of me as your friend than as your boss.{w=0.5} It {i}is{/i} my job to care about my students, after all."
    
    burgh "And I'd like you to think of this class not as a lecture, but a studio of sorts."

    burgh norm2 "We'll be studying the anatomy and phylogenetics of Bug Pokémon for the first part of the semester, and then we'll move on to rendering live models."
    burgh happy "If we're lucky, perhaps we can take a field trip to attend one of Johto's Bug-catching contests!"

    ethan "Seriously?! That'd be so rad! I loved those!"

    burgh norm "Are there any questions so far?"

    show skyla uniform at rightside with dis

    pause 0.5

    burgh norm2 "Yes, in the front."
    
    skyla @sadbrow talkingmouth "...Um, what, uh, what does 'rendering models' mean?"

    hide skyla at rightside with dis

    burgh "Ah. Later in class, you will all be responsible for choosing an art medium and using it to apply your understanding of Bug Pokémon anatomy."
    burgh norm2 "We will have live models available so you don't have to worry about drawing from memory."
    burgh surprised "Wasn't this all on the online syllabus?"
    burgh norm2 "No matter. We should have plenty of time to prepare before we start."

    burgh happy "I have a slideshow ready, to start us off with a bit of inspiration!"
    
    narrator "Burgh flips through images of wings, scales, and mandibles, rhapsodizing about each..."

    pause 1.0
    
    narrator "Everyone has their tastes."

    hide burgh

elif (not HasEvent("Burgh", 2.1) and classstats["Bug"] >= 10):#Chrysalize
    show burgh with dis
    if (not HasEvent("Burgh", 2)):
        $ renpy.pause(1.0, hard=True)

        narrator "The class is working hard on sketching Bug-type Pokémon. You are almost finished with a very detailed rendition of a Sizzlipede's mandibles, when..."

        burgh norm3 "...Hm."

        redmind uniform @thinking "Uh-oh. Instructor Burgh doesn't look pleased."

        burgh @surprised2 "[first_name], why don't you tell me a little about what you're creating here?"

        red @happy "Well, uh, it's meant to be a Sizzlipede! I'm just finishing up the mandibles here. Think I might've over-furred it though, so it looks kinda like it has a moustache."

        show may uniform at rightside 
        show skyla uniform at farrightside 
        with dis

        skyla @happy "Hey, don't say that! I think it looks great."

        may @closedbrow talking2mouth "Well... the proportions are a bit wrong..."
        may @happy "But it's very recognizable!"

        show rosa uniform at leftside with dis

        rosa @talkingmouth "Yeah, don't worry about it if a couple details are off. People never notice that stuff. Their eyes'll be drawn to the focal point, which is..."
        rosa @closedbrow talking2mouth sweat "Um, the heat spot right underneath the mandibles. Hm. Well, maybe they {i}will{/i} notice the mous--mandibles!"

        show bugsy uniform behind rosa at farleftside with dis

        skyla @talkingmouth "Yeah, and the mandibles look kinda like a moustache anyway, so you're good!"
        
        bugsy @happy "Did somebody say mandibles? People always call those big spiky things on top of a Pinsir 'horns', but they're mandibles too! And they're really flexible! Pinsir can point them in all sorts of different directions!"
        bugsy @talkingmouth "And, hey, did you know that Trapinch has the strongest mandibles, for its size, of any bug Pokémon? I mean, it's not technically a {i}Bug Pokémon{/i} but it's definitely a bug Pokémon, right? Just look at its--"

        red @closedeyes talking2mouth "Guys? I'm not done. I get you're trying to talk me up, but you can stop now."

        burgh @sad2 "Hm. That's the first thing you've done that I actually have a problem with, [first_name]."

        red @surprised "Instructor Burgh?"

        burgh happy @happy2 "Just Burgh, please. Actually, this could be a good group discussion. Everyone, let's go out to the gardens."

        scene garden with Dissolve(2.0)

        pause 1.0

        show skyla uniform at farrightside 
        show may uniform at rightside
        show bugsy uniform at farleftside
        show rosa uniform at leftside
        show burgh
        with dis

        burgh norm2 "Alright. Everyone comfy? If you want to stand up, feel free, but if you want to sit in the grass, go ahead."
        burgh happy @happy2 "Now. Who can tell me what makes Bug-types unique?"

        may @happy "How fast they evolve!"
        
        skyla @closedbrow talking2mouth "Uh, a lot of 'em have cocoon stages?"

        rosa @talkingmouth "Is it that they're not very strong?"

        bugsy @angry "Hey! Be nice to bugs!"
        bugsy @talkingmouth "Anyway, it's that they have a segmented exoskeleton, which has a cuticle made of chitin, and an open circulatory system filled with haemolymph."

        burgh @norm2 "Well, you're all right. And the 'right' answer is for each one of you to decide, anyway."
        burgh @norm2 "But there's one thing that I didn't hear mentioned I'd like to float into your brainspaces."
        burgh @happy2 "Bug Pokémon are {i}humble.{/i}"
        burgh @norm2 "Many bug Pokémon aren't very strong, true, Rosa. And the ones that cocoon themselves often get weaker, in certain ways." 
        burgh @happy2 "More limited movepools, decreased maneuverability--you've studied them enough to know what I mean by this point."

        skyla @sadbrow talkingmouth "Uh... Burgh, it kind of sounds like you're saying we shouldn't be training Bug-types."

        burgh @surprised2 "It does? Well, I'm saying the opposite."
        burgh @happy2 "Training Bug-types is a challenge. It's hard, time-consuming, and sometimes unrewarding. Just like art."
        burgh @norm2 "But, just like the artist, the Bug-type is resilient, and can endure all the attacks thrown its way while in its chrysalis."

        burgh @happy2 "And when it emerges... it's beautiful, my darlings."

        red uniform @closedbrow talking2mouth "So... what you said before..."

        burgh @sad2 "Bug-types cocoon themselves to endure until their true selves can be revealed--whether it's a Beautifly, a Dustox, or even a Scolipede."
        burgh @norm2 "But until that time, they endure--they defend. It's a struggle. But bugs are the best at struggling."
        burgh @happy "Humility and patience. Every attack just makes you, and your Bug-types stronger. So welcome them."

        pause 2.0

        red @happy "Is this just a roundabout way of saying I shouldn't have stopped my friends from saying that my Sizzlipede drawing sucked ass?"

        burgh @surprised2 "Oh, we don't use that sort of phrasing around here. It's better to think of it as... you're still discovering your personal rendition of Sizzlipede."

        red @happy "Well, I hope I discover a personal Sizzlipede that doesn't suck ass, Instructor Burgh."

        burgh @happy2 "Now, enough of that. And I told you before, it's just Burgh."

        red @talkingmouth "Sorry, Burgh. Force of habit. Just doing it as a sign of respect."

        burgh @norm2 "That's alright. {i}I{/i} respect {i}you{/i} too much to ask you to call me by some stuffy title."

        burgh @norm2 "Actually, I think it's about time that I advanced you to the next level of the curriculum."

        red @talkingmouth "Oh?"

        burgh @norm2 "I'll just give you a simple test battle. You can use any of the Pokémon you have on hand right now, but this will be a one-on-one battle."

        red @happy "Cool. What do I get if I win?"

        burgh @happy2 "Well, I'll be able to teach any of your bug Pokémon the move {i}Chrysalize.{/i}"

        red @surprised "Huh? I'm not sure I know that move."

        burgh @norm2 "It's an original piece I composed. Your Pokémon will fall asleep for two turns, but will recover to full health, clear its status, and raise its defenses."

        red @surprised "Wow! That sounds really powerful."

        burgh @happy2 "Well, I hope you'll find a use for it. But you'll have to earn it, first!"

        red @angrybrow happymouth "Oh, I'm more than ready, Burgh!"

        $ AddEvent("Burgh", 2)
    else:
        red uniform @talking2mouth "Burgh, I've studied since the last time we fought--and now I'm more than ready to beat you."

    burgh @norm2 "Well, we'll see. Now, which Pokémon will you be using against me? {color=#0048ff}I recommend picking a Bug-type.{/color}"

    python:
        trainer1 = Trainer("Red", TrainerType.Player, playerparty)
        for mon in playerparty:
            mon.Owner = trainer1
        hidebattleui = True
        mustswitch = True
        renpy.transition(dissolve)
        newindex = renpy.call_screen("switch", trainer1)

    burgh @happy2 "Alright. Let's see your style, then."
    $ hidebattleui=False
    $ mustswitch = False
    $trainer1 = Trainer("red", TrainerType.Player, [playerparty[newindex]])
    $trainer2 = Trainer("burgh", TrainerType.Enemy, [
        Pokemon(686, level=11, moves=[GetMove("Payback"), GetMove("Wrap"), GetMove("Hypnosis"), GetMove("Tackle")], ability="Contrary")
    ])

    call Battle([trainer1, trainer2], customexpressions=["red uniform", "red uniform angrybrow happymouth", "burgh norm", "burgh happy2"], reanchor=[False, True]) from _call_Battle_24
    $ battlehistory["Burgh1"]  = _return

    show burgh with dis

    if (WonBattle("Burgh1")):
        $ AddEvent("Burgh", 2.1)

        burgh @happy2 "Well done. You've dipped your paintbrush in--the first step of a thousand brushstrokes."
        burgh @norm2 "I look forward to seeing the masterpiece you create."

        $ passedclass = True

        jump aftertutorintrobug
    
    else:
        burgh @sad2 "Ah."
        burgh @norm2 "...Well, that could have gone better. Remember, Inkay is very weak to Bug-type moves."
        burgh @norm2 "Perhaps you need a bit more time in your cocoon, to get stronger?" 
        burgh @happy2 "That's fine. I know you'll come back out, and dazzle us with your true self."

        redmind uniform @thinking "Damn... that was an embarrassing loss. Still, at least I learned something..."

    hide burgh with dis

elif (not HasEvent("Burgh", 3.1) and classstats["Bug"] >= 20):#Silver Powder
    show burgh with dis
    if (not HasEvent("Burgh", 3)):
        $ renpy.pause(1.0, hard=True)

        burgh "{w=0.5}.{w=0.5}.{w=0.5}."

        burgh @norm2 "[first_name]?"

        red uniform @talkingmouth "Yeah?"

        burgh @happy2 "I'm impressed by your advancements in this class so far."

        burgh @norm2 "It looks like you're really discovering your voice."

        red @happy "Thanks!"

        burgh happy2 "No, thank {i}you.{/i} I really appreciate having a student so committed to the Bug-type."

        red @talkingmouth "Does that mean I get to take another advancement exam?"

        burgh @norm2 "Yes, I think it does. If you pass this exam, I'll teach you how to grind up Silver Powder made from shed chrysalises, which boosts the power of your Bug-type moves by 10%%."

        burgh @happy2 "Tell me when you're ready."

        red @happy "Oh, I'm definitely ready now!"

        $ AddEvent("Burgh", 3)
    else:
        red uniform @talking2mouth "Burgh, I've studied since the last time we fought--and now I'm more than ready to beat you."

    burgh @norm2 "I very much hope so! Now, which Pokémon will you be using against me? {color=#0048ff}I'll be using a single Bug-type.{/color}"

    python:
        trainer1 = MakeRed()
        for mon in playerparty:
            mon.Owner = trainer1
        hidebattleui = True
        mustswitch = True
        renpy.transition(dissolve)
        newindex = renpy.call_screen("switch", trainer1)

    burgh @happy2 "Show me your Pokémon's true colors."
    $ hidebattleui=False
    $ mustswitch = False
    $trainer1 = Trainer("red", TrainerType.Player, [playerparty[newindex]])
    $trainer2 = Trainer("burgh", TrainerType.Enemy, [
        Pokemon("Swadloon", level=21, moves=[GetMove("Bug Bite"), GetMove("Razor Leaf"), GetMove("Grass Whistle"), GetMove("Protect")], ability="Overcoat", item="Oran Berry")
    ])

    call Battle([trainer1, trainer2], customexpressions=["red uniform", "red uniform angrybrow happymouth", "burgh norm", "burgh happy2"], reanchor=[False, True]) from _call_Battle_74
    $ battlehistory["Burgh2"]  = _return

    show burgh with dis

    if (WonBattle("Burgh2")):
        $ AddEvent("Burgh", 3.1)

        burgh @happy2 "It looks like your masterpiece is really starting to take form."
        burgh @norm2 "I'm excited to see where your brush strays next."

        burgh @happy2 "Here, take this. Maybe it'll provide some inspiration for your next work."

        $ GetItem("Silver Powder", 1, "You gained a Silver Powder! It tickles your nose a little bit.")

        $ renpy.pop_call()
        jump aftertutoring
    
    else:
        burgh @sad2 "Ah."
        burgh @norm2 "...Well, that could have gone better. Remember, Swadloon is very weak to Fire and Flying-type moves." 
        burgh @happy2 "On your next attempt, try using Bug-type weaknesses as your strengths!"

        redmind uniform @thinking "Damn... that was an embarrassing loss. Still, at least I learned something..."

    hide burgh with dis
elif (not HasEvent("Burgh", 4.1) and classstats["Bug"] >= 30):#Silver Wind
    show burgh with dis
    if (not HasEvent("Burgh", 4)):
        $ renpy.pause(1.0, hard=True)

        burgh @happy2 "[first_name]!"

        red uniform @talkingmouth "Yessir!"

        burgh @sad2 "No 'Sir', please. I just got you to stop calling me Instructor..."

        red @happy "Oops. Sorry. It's just a country habit of mine..."

        burgh @norm2 "It's alright."
        burgh @happy2 "Actually, it's better than alright. Can you tell me what time it is?"

        if (timeOfDay == "Morning"):
            red @confused "[ellipses]10:47?"

        else:
            red @confused "[ellipses]2:47?"

        burgh @sad2 "Technically correct. But must you think so literally?"
        burgh @happy2 "An artist seeks to express {i}truth{/i}, not just the mundanity of {i}fact{/i}!"

        red @closedbrow talking2mouth "I don't understand."

        burgh @happy2 "You will. You're very bright. And you've advanced in this class so quickly."

        red @happy "Thanks, Ins-- Burgh."

        burgh @norm2 "Anyway, the {i}actual{/i} time is 'advancement exam time'!"

        red @surprised "Oh, really? Alright, I'm ready!"

        burgh @happy2 "I'm not surprised. Beat me, and I'll teach you the move Silver Wind, which... ah, well, you know what that one does."

        $ AddEvent("Burgh", 4)
    else:
        red uniform @talking2mouth "Burgh, I've studied since the last time we fought--and now I'm more than ready to beat you."

    burgh @norm2 "Pick a Pokémon to use against me. {color=#0048ff}I wouldn't recommend using Bug-types for this fight!{/color}"

    python:
        hidebattleui = True
        mustswitch = True
        renpy.transition(dissolve)
        newindex = renpy.call_screen("switch", MakeRed())

    burgh @happy2 "I'm feeling inspired!"
    $ hidebattleui=False
    $ mustswitch = False
    $ trainer1 = Trainer("red", TrainerType.Player, [playerparty[newindex]])
    $ trainer2 = Trainer("burgh", TrainerType.Enemy, [
        Pokemon("Heatmor", level=31, moves=[GetMove("Flame Burst"), GetMove("Snatch"), GetMove("Fire Spin"), GetMove("Fury Swipes")], ability="White Smoke", item="Sitrus Berry")
    ])

    call Battle([trainer1, trainer2], customexpressions=["red uniform", "red uniform angrybrow happymouth", "burgh norm", "burgh happy2"], reanchor=[False, True]) from _call_Battle_75
    $ battlehistory["Burgh3"]  = _return

    show burgh with dis

    if (WonBattle("Burgh3")):
        $ AddEvent("Burgh", 4.1)

        burgh @happy2 "Fantastic work. You've managed to beat a team weak to bugs, one that uses bugs, and one strong against bugs."
        burgh @norm2 "I think, for future tests, I might use a few more Pokémon. Three, perhaps. So, I hope you're prepared for that."
        burgh @happy2 "It makes me proud to see you metamorphose as both a battler and an artist."

        $ passedclass = True

        jump aftertutorintrobug
    
    else:
        burgh @sad2 "Ah."
        burgh @norm2 "...Well, that could have gone better. Heatmor's a strong Pokémon, but he can't do much against a good Rock, Ground, or Water-type."
        burgh @norm2 "Perhaps you can think of some Bug-types which fit the bill?" 
        burgh @happy2 "Take your time! I know your metamorphosis is well underway."

        redmind uniform @thinking "Damn... that was an embarrassing loss. Still, at least I learned something..."

    hide burgh with dis

elif (FindGenericClassScene(True)):#generic scene
    $ renpy.call(FindGenericClassScene())
    hide burgh with dis
else: # _really_ generic scene
    show burgh with dis
    burgh "[timeOfDay], students. I was thinking about what to do for our lessons today last night, when suddenly, inspiration struck!"
    hide burgh with dis
    show burghbg with dis
    burgh "Now, before we get started on the lesson proper, why don't we all share where we get our inspiration from? Personally, I find the wings of a Bug Pokémon to be..."
    narrator "Class proceeds without incident."

return

label movetutorbug:
show burgh with dis
burgh @norm2 "You'd like me to add a Bug-type move to your Pokémon's palette? Sure. Which move do you want to teach?"
burgh @norm2 "I can teach Chrysalize, which is a move that raises your Pokémon's defenses, and restores their health, but puts them to sleep for two turns."
if (HasEvent("Burgh", 4.1)):
    burgh @happy2 "I can also teach Silver Wind, which has a 10%% chance of raising all your Pokémon's stats by one stage."

label aftertutorintrobug:
$ taughtmove = None

menu:
    ">Learn Chrysalize":
        $ taughtmove = "Chrysalize"
    ">Learn Silver Wind" if (HasEvent("Burgh", 4.1)):
        $ taughtmove = "Silver Wind"
    "Nevermind":
        burgh @surprised2 "Uh... alright."

        if (passedclass):
            $ renpy.pop_call()
            jump aftertutoring
        else:
            jump afterbugsetup
python:
    hidebattleui = True
    renpy.transition(dissolve)
    newindex = renpy.call_screen("switch", MakeRed())
    if (newindex != "back"):
        newmon = playerparty[newindex]
    hidebattleui=False
if (newindex == "back"):
    burgh @surprised2 "Uh... alright."
elif (MonCanLearn(newmon, taughtmove)):
    $ newmon.LearnNewMove([(1, taughtmove)])
    if (taughtmove in newmon.GetMoveNames()):
        jump endclass
else:
    burgh @sad2 "Sorry, I'm not sure I know how to teach that Pokémon [taughtmove]..."
    
jump aftertutorintrobug

label itemcraftbug:
show burgh with dis

burgh @happy2 "I can help you create some battle items. It's always a good day when I can break out the art supplies."
burgh @norm2 "I can help you make a Silver Powder. This is a held item that boosts the power of Bug-type moves by 10%%."

menu:    
    ">Craft Silver Powder" if (HasEvent("Burgh", 3.1)):
        $ GetItem("Silver Powder", 1, "You craft the Silver Powder from shed chrysalises!")
        jump endclasscraft
    "Nevermind":
        burgh @surprised2 "Uh... alright."
        jump afterbugsetup
