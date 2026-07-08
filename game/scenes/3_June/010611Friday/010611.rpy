label day010611:

stop music fadeout 1.5

call calendar(1) from _call_calendar_64

python:
    calDate = calDate.replace(day=11, month=6, year=2004)
    timeOfDay = "Morning"
    renpy.pause(2.5, hard=True)
    renpy.music.queue("Audio/bigcrowdloop.ogg", channel='crowd', loop=True, fadein=0.5)
    renpy.music.queue("Audio/Music/Oak Class.ogg", channel='music', loop=None, fadein=1.5, tight=None)

scene homeroom
show screen currentdate
with splitfade

pause 2.0

red uniform @confused "Why[ellipses] does this feel familiar?"

show hilbert uniform with dis:
    xanchor 0.0 xpos 1.0
    ease 0.5 xpos 0.66 xanchor 0.5

hilbert @talking2mouth "Professor Oak is late again."

red @talking2mouth "Yeah, seems like it. That's weird, but--"

hilbert @talking2mouth "Blue is also not here."

red @talking2mouth surprisedbrow "Oh[ellipses]"
red @closedbrow talking2mouth "Crap. Yeah, I just remembered. Blue said he was going to get us some more time last night, and he must've--"

#talking with him about the party should be unavoidable by this point
hilbert @talking2mouth "Time? For what? That ridiculous party you have planned?"

red @talking2mouth angryeyebrows sad2eyes "Hey, we're doing it for Leaf. Not {i}that{/i} ridiculous." 

hilbert @closedbrow talking2mouth "Whatever. If Blue wants to waste his time at Kobukan on foolishness like this, then the least we can expect is he won't waste {i}our{/i} time, too, by dragging the teacher away."

redmind @sadbrow frownmouth "Kinda gotta admit he has a point, here. I mean, I've pretty much talked to everyone in this class already. It's not like I need more time {i}here{/i}."
redmind @sadbrow "But, hey, he was trying to help out. I guess that's the important part."

red @happy "Well, maybe I should carpe this diem and take the opportunity to try and change your mind about the party? Would you--"

hilbert @talking2mouth closedbrow "I am,{w=0.5} {i}generously{/i},{w=0.5} giving you five seconds to stop speaking."

red @sweat closedbrow talking2mouth "{size=30}Nevermind.{/size}"

pause 1.0

hilbert @surprisedbrow frownmouth "Hm? My phone..."

$ PlaySound("vibrate.ogg")

red @confusedbrow talking2mouth "Huh? Mine too."

show phone_B
show phone_A
with fadeinbottom

red @confused "Huh, a video message from an unknown number? What's--"

show janine behind phone_A:
    zoom 0.95
with fadeinbottom

janine @talking2mouth "Battle Hall, now."

pause 1.0

red @confused "I'm--I'm in the middle of class."

janine @talking2mouth "This is a video message, so I can't tell if you said something like 'I'm in the middle of class', but if you did, don't talk back to me, and come here, {i}now{/i}."

hide phone_B
hide phone_A
hide janine
with fadeoutbottom

pause 1.0

redmind @thonk "Wait, my phone doesn't have that message in its history. How did she[ellipses] does she send ninja videomails, too?"

red @talking2mouth "Well, I[ellipses] I guess since Professor Oak isn't here, we should go[ellipses]?"

hilbert @closedbrow talking2mouth "This must have something to do with Blue."

red @talking2mouth sweat closedbrow "Yeah, I can't disagree on that one."

hilbert @talking2mouth "Then let's go."

call clearscreens() from _call_clearscreens_279
scene blank2 
with splitfadefast

pause 1.0

scene homeroom
show whitney uniform:
    xpos 0.25
show flannery tiredbrow tiredmouth uniform:
    xpos 0.75 xzoom -1
show may uniform:
    xpos 0.5
with dis

may @talking2mouth "You two saw [first_name] and Hilbert just run out the classroom, right?"

flannery @talking2mouth "Leaf's been gone all week, and [oldblue_name] wasn't here when class started[ellipses]"

whitney @confused "Maybe something big is going on with the Battle Team?"

show whitney uniform angrybrow frownmouth:
    xpos 0.25
    ease 0.5 xpos 0.2
show flannery tiredbrow tiredmouth uniform:
    xpos 0.75 xzoom -1
    ease 0.5 xzoom 1 xpos 0.6
show may uniform angrybrow frownmouth:
    xpos 0.5
    ease 0.5 xpos 0.4
with dis

show melody uniform on:
    xpos 1.2 xzoom -1
    ease 0.5 xpos 0.8

melody @talking2mouth "As always. Twenty-four-seven drama with those guys."
melody @happybrow talkingmouth "Spend more time measuring each other's dicks than they do battling. No wonder they implode every month."
melody @talking2mouth "It's been about a month since the last big thing, hasn't it? When Pinky over there dropped?"

dawn uniform @surprisedbrow frownmouth "[ellipses]"

pause 1.0

flannery @talking2mouth "Do you know what's going on? 'Cause if not, butt out of {i}our{/i} conversation."

melody @talking2mouth "No idea. Thought you might know."

whitney @angrybrow talking2mouth "Why would {i}we{/i} know anything? We're not on the Battle Team."

pause 1.0

melody @talking2mouth "You've talked?"
melody @talking2mouth "With people?"
melody @talking2mouth "Who are?"
melody @talking2mouth "On it?"

may @talking2mouth "Go {i}away{/i}, Melody. We don't know anything."

whitney @confused "And if we {i}did{/i}, why would we tell you?"
whitney @angry "You screwed me over on that Wonder Guard quiz. I haven't forgotten that!"

show flannery tiredbrow tiredmouth uniform:
    xpos 0.6 xzoom 1
    ease 0.5 xzoom -1

flannery @talking2mouth "C'mon, Whit, don't pay any attention to her. Let's get some studying in before Professor Oak comes back."

hide whitney
hide flannery
hide may
with dis

melody @bubblemouth "[ellipses]"
melody @talking2mouth "Guess I don't still got it. Baiting people used to be easy."

pause 1.0

melody @angrybrow talking2mouth "Eff staying here. I'm figuring out what's going on."

scene blank2 with splitfade

stop music fadeout 1.5

pause 1.0

scene stadium_empty with splitfade

red uniform @talking2mouth unamusedbrow "Give me a {i}break{/i}."

queue music "audio/music/sycamore.ogg"

show sycamore happybrow talkingmouth:
    xpos 0.66
show blue uniform angrybrow:
    xpos 0.33
with dis

pause 2.0

show sycamore happybrow talkingmouth:
    xpos 0.66 zoom 1.0 ypos 1.0
    ease 0.5 zoom 0.9 ypos 0.9
show blue uniform angrybrow:
    xpos 0.33 zoom 1.0 ypos 1.0
    ease 0.5 zoom 0.9 ypos 0.9

show blank2 with dis:
    alpha 0.3

narrator "As you look around, you notice students from various classrooms are filtering into the Battle Hall. Whatever brought them here[ellipses] was {i}not{/i} well-organized."

#STRETCH: Show a cropped version of Professor oak's sprite in the bleachers

redmind uniform @surprisedbrow frownmouth "Wait--up there! In the bleachers. Isn't that Sam?"
redmind @thonk "I guess he said he was going to speak with Professor Sycamore this morning, didn't he? Maybe this has something to do with that?"
redmind @thinking "Then that would make that man there[ellipses]"

$ BecomeNamed("Professor Sycamore")

show janine uniform with dis:
    xpos 0.25

red @talking2mouth "Janine? Did you actually send out that video message calling all the Battle Team members here?"

janine @talking2mouth "Yeah."

red @talking2mouth "In the middle of morning homeroom?"

janine @talking2mouth "This is more important, trust me."

red @confused "Blue picking a fight with a Professor? This isn't even the first time he's done that {i}this week.{/i}"

janine @closedbrow talkingmouth "Just watch."

show janine:
    xpos 0.25 alpha 1.0 zoom 1.0 ypos 1.0
    ease 0.5 alpha 0.0 zoom 1.3 ypos 1.2

hide blank2 with dis

show sycamore -happybrow -talkingmouth:
    xpos 0.66 zoom 0.9 ypos 0.9
    ease 0.5 zoom 1.0 ypos 1.0
show blue uniform -angrybrow:
    xpos 0.33 zoom 0.9 ypos 0.9
    ease 0.5 zoom 1.0 ypos 1.0
with dis

sycamore @talkingmouth "{i}Ah, Monsieur Oak! C'est tellement agréable d'entendre ma langue maternelle à nouveau et avec une telle aisance! Quel dommage que vous ne soyez pas tombé dans ma classe.{/i}"

blue @talking2mouth "{i}Bonjour! Ouais, euh, moi suis très cool. Bonjour! Je sais beaucoup... trucs. Comme, je sais toi es genre un... gros chef Méga Évolution? Moi veux voir ça moi-même! Bonjour!{/i}"

show sycamore happybrow talkingmouth:
    xpos 0.66 zoom 1.0 ypos 1.0
    ease 0.5 zoom 0.9 ypos 0.9
show blue uniform angrybrow:
    xpos 0.33 zoom 1.0 ypos 1.0
    ease 0.5 zoom 0.9 ypos 0.9

show blank2 with dis:
    alpha 0.3

pause 1.0

show ethan:
    xpos 0.75

ethan uniform @talking2mouth "Did he just say he's a meme?"

red @surprisedbrow talking2mouth "Ethan? What're you--"
red @closedbrow talking2mouth "Oh, right, Janine called you."

ethan @talking2mouth "Didn't know Blue spoke Kalosian."

red @talking2mouth "He doesn't. He visited Kalos for a {i}Summer{/i}. How is he[ellipses]?"

show yellow uniform with dis:
    xpos 0.25 xzoom -1

yellow @talking2mouth "He spent all night studying. Um[ellipses] but he did know a {i}little{/i} bit before. Mostly just 'Bonjour.'"

red @confused "Yellow?! What are {i}you{/i} doing here?"

yellow @talkingmouth "Well, when Sonia, Silver, and Ethan suddenly got up in the middle of Professor Cherry's class and headed towards the Battle Hall, Professor Cherry stopped class and told us all to follow them."

red @closedbrow talking2mouth "I guess three of the strongest battlers in class suddenly leaving together would make her curious. It'd make {i}anyone{/i} curious, probably."

ethan @happy "Not sure I'd say I'm one of the three strongest battlers, but, hey, I appreciate it."

show raihan uniform behind yellow with dis

raihan @happy "[last_name]! What're you doing here?"

red @talking2mouth "What am {i}I{/i}--what are {i}you{/i} doing here?"

raihan @talking2mouth "Rowan heard his protégé was going to be battling a student, and wanted to watch. Come to think of it, it looks like[ellipses] {nw}"
extend @surprisedbrow talking2mouth "hold on, is {i}every{/i} class here?"

ethan @talking2mouth "Huh. Kinda looks like it. Did the whole school come out to see this?"

pause 1.0

red @surprisedbrow frownmouth "[ellipses]"
red @talking2mouth "Damn. This was actually[ellipses] a good idea."

show blank2 behind blue

show blank2 as blank2two behind blue:
    alpha 0.3

show yellow surprisedbrow frownmouth behind blank2two:
    xpos 0.25
    linear 0.2 xpos 0.1

show raihan surprisedbrow frownmouth behind blank2two:
    xpos 0.5
    linear 0.2 xpos 0.75

show ethan surprisedbrow frownmouth behind blank2two:
    xpos 0.75
    linear 0.2 xpos 0.9

show blue: 
    xpos 0.33 zoom 0.9 ypos 0.9
    ease 0.5 xpos 0.33 zoom 1.3 ypos 1.2

blue frownmouth @angrybrow talking2mouth "{i}Alors arrête de perdre du temps et parle aux gens! Utilise le temps que je t'ai gagné!{/i}"

pause 2.0

red @talking2mouth "Wrong language."

blue lightblush @closedbrow talking2mouth "{size=30}{i}Merde.{/i}{/size}{w=0.5} I said 'then stop wasting time and talk to people! Use the time I bought you!'"

red @talking2mouth "On it."

menu:
    "Thanks.":
        $ ValueChange("Blue", 1, 0.33)
        blue -frownmouth @closedbrow "I did this for the {i}party{/i}, remember. And now I'm going to wipe the stadium floor with that Megaschool dropout."

    "Go kick his ass.":
        $ ValueChange("Blue", 1, 0.33)
        blue -frownmouth @closedbrow "Already on it. I'm going to wipe the stadium floor with that Megaschool dropout."

    "Try to last as long as you can.":
        blue -frownmouth @happy "{i}Last{/i}? Psh. I'm going to wipe the stadium floor with that Megaschool dropout."

show ethan:
    xpos 0.9 alpha 1.0 ypos 1.0 zoom 1.0
    ease 0.5 xpos 1.2 alpha 0.0 ypos 1.2 zoom 1.3
show raihan:
    xpos 0.75 alpha 1.0 ypos 1.0 zoom 1.0
    ease 0.5 xpos 1.05 alpha 0.0 ypos 1.2 zoom 1.3
show yellow:
    xpos 0.1 alpha 1.0 ypos 1.0 zoom 1.0
    ease 0.5 xpos -0.2 alpha 0.0 ypos 1.2 zoom 1.3
show blue: 
    xpos 0.33 xpos 0.33 zoom 1.3 ypos 1.2 
    ease 0.5 zoom 0.9 ypos 0.9
hide blank2two
hide blank2
with dis

blue -lightblush @talking2mouth "{i}Pardon, moi suis revenu. Bonjour. Je juste parler avec mon ami {b}stupide{/b}. {w=0.5}[ellipses]Bonjour{/i}."

sycamore @talkingmouth "Ah, ah, fantastic! I can sense your fiery passion, {i}Monsieur{/i} Oak. Like a roaring flame!"
sycamore @angrybrow talkingmouth "Yes, yes, your Pokémon are shaking in their Poké Balls out of excitement. I haven't battled in a good while, but[ellipses] I am more than happy to, now!"
sycamore @talkingmouth "Gather around, students! Professor Sycamore's about to give a very special demonstration on the power of Mega Evolution, in battle against the Battle Team's very own ace!"

redmind @unamusedbrow unamusedmouth "Oh, boy. What has Blue been telling Sycamore in the {i}hour{/i} I let him out of sight?"

show janine uniform with dis:
    xpos 0.2 alpha 1.0 zoom 1.0 ypos 1.0

janine @talking2mouth "Stand by for the level balancer activation. Takes a few minutes to spin up. If you feel static on the back of your head, that means it's working."#FIX THIS: Figure out a cool place to Chekov's gun this

blue frownmouth sad2brow @angry "I don't need the level balancer!"

janine @talking2mouth "If you want to last more than five turns against Professor Sycamore[ellipses] yeah. You do."

pause 1.0

blue @talking2mouth "Whatever[ellipses]"

hide raihan
hide ethan
hide yellow
hide janine 
with dis

python:
    trainer1 = MakeTrainer("Blue", trainertype = TrainerType.Ally)
    trainer2 = MakeTrainer("Sycamore")

call Battle([trainer1, trainer2], uniforms=[True, False], gainexp=False, levelscale=50, dialogfunc=sycamoredialog, customswitchbrain=sycamoreswitchbrain) from _call_Battle_191

queue music "audio/music/sycamore.ogg"

if (_return):
    $ AddEvent("Blue", "BeatSycamore")
    show sycamore happybrow:
        xpos 0.66
    show blue uniform angrybrow:
        xpos 0.33
    with splitfade

else:
    $ AddEvent("Blue", "LostToSycamore")
    show sycamore happybrow:
        xpos 0.66
    show blue uniform frownmouth:
        xpos 0.33
    with splitfade

sycamore @talkingmouth "Ah, ah, magnifique! Your passion blazed like fire in this battle--truly, you are something beyond an ordinary student! I am most impressed!"

if (HasEvent("Blue", "BeatSycamore")):
    blue surprisedbrow frownmouth @closedbrow talkingmouth "You're just saying that 'cause I kicked your ass."

    sycamore @happy "Oui! What other reason would I have to say it? I have been thoroughly thrashed--and what a kick it was!"

    blue @confusedbrow talking2mouth "Wait. You--you're {i}accepting{/i} that I kicked your ass? Like, you're not going to say you were only using a tenth of your power, or some bullshit like that?"

    sycamore -happybrow @sadbrow talkingmouth "Do you think so little of my character, Monsieur Oak? We battled as equals. This was a fair and full win."

    pause 1.0

    show blue lightblush with dis

    pause 1.0

    redmind uniform @sweat sadbrow "I can practically hear Blue's brain short-circuiting from over here. Not everyone's as sore a loser as you are."

else:
    blue @closedbrow talking2mouth "Whatever. I wasn't even trying to win. I was just trying to buy time for [first_name]."

    sycamore -happybrow @sadbrow talkingmouth "Oh, no, Monsieur Oak. Please do not say that. I know you truly wanted to win--such passion cannot come from anything but the burning yearn for victory."

    blue @talking2mouth "Pfft. Doesn't matter if I was 'passionate' or not. I lost."

    sycamore @talkingmouth "My dear boy, that is quite simply untrue. You are a student at Kobukan Academy, and you have lost to a Professor. That is not a loss, but a lesson--and one that I am sure you will learn from."
    sycamore @happy "I can say nothing but {i}bien joué{/i} to you, Monsieur Oak--well done!"

    pause 1.0

    show blue closedbrow with dis 

    blue @talking2mouth "Uh[ellipses] thanks."

pause 1.0

sycamore @surprisedbrow talkingmouth "Ah, but we have gathered such an audience! I was quite unaware. Come now, students, should you not be in your homerooms?"

show blue -lightblush with dis

show kris with dis:
    xpos 0.2

show rowan with dis:
    xpos 0.8 xzoom -1

kris @talkingmouth "Sorry, Augustine. My Battle Team members were called here, and I figured I should come along to see what was going on."

rowan @talking2mouth "Harrumph. I was told that my protégé was going to be battling a student, and I wanted to see it for myself. This 'Mega Evolution' ability of yours[ellipses] my students wouldn't stop pestering me for a demonstration."
rowan @angrybrow talking2mouth "Bah! If I've told them once, I've told them too often. I study 'normal' evolution, not 'Mega' evolution!"

kris @angrybrow frownmouth "Ahem."

rowan @closedbrow talking2mouth "Yes, yes, 'good morning.' Sycamore was my student for ten years, he knows not to expect any unnecessary blarney."

sycamore @talkingmouth happybrow "How splendid it is to see you two here! Oh, and I see Professor Birch is there, as well, untangling himself from his students. How serendipitous that we would all be brought here by Monsieur Oak."

show blue surprisedbrow frownmouth with dis

sycamore @happy "But perhaps this is less coincidence, and more habit? Your passion must appoint you to be the center of your social circles, {i}non?{/i} I imagine you're quite popular amongst your classmates!"

pause 1.0

show sycamore surprisedbrow frownmouth
show kris surprisedbrow frownmouth
show rowan angrybrow frownmouth
with dis

blue happy "Hah!"

show stadium_empty with vpunch

blue "{i}Hah!{/i}"

sycamore happy @talkingmouth "Ahahaha! Monsieur Oak, say no more! Your hilarity makes the correctness of my assertion all too apparent! I am truly, ah, 'right on the money!'"

blue "{i}{b}H A H !{/b}{/i}"

redmind @sadbrow "[ellipses]Professor Sycamore isn't, uh[ellipses]"
redmind @closedbrow sweat "He's not a great judge of character, huh?"

call clearscreens() from _call_clearscreens_280
scene blank2 with Dissolve(1.0)

$ PlaySound("BellChime.ogg")

jump PickElective