label secondhomeroom010531:

scene blank2

play music "Audio/Music/Oak Intro.ogg" noloop
queue music "Audio/Music/Oak Class.ogg"

show homeroom behind blank2
    
$ renpy.transition(dissolve)
show screen currentdate

show oak 
hide blank2 
with splitfade

oak @talkingmouth "Right, let's get into it. This exam should not take very long, but I'd like to be able to field questions on the lecture before we start."

oak @talking2mouth "Who can provide a quick summary of where we were last time in the lesson?"

flannery uniform @talkingmouth "You were telling us how we can make Synchronoise useful, even if our opponents don't have any Pokémon with the same types we do."

oak @closedbrow talkingmouth "Yes, very good."

oak @talking2mouth "It's quite simple; change the opponent's type. There are various moves and abilities that can do such things."
oak @talking2mouth "As you may remember from the Camouflage test last week, some Pokémon like Frogadier or Scorbunny are capable of changing their own types, based on the moves they use."
oak @closedeyes angryeyebrows talking2mouth "If you're able to lure the opponent into using a move that puts you in an advantageous position for follow-up, you may find they're forced to battle suboptimally, out of fear of what you {i}could{/i} do in retaliation."
oak @talking2mouth "You could also hit a Pokémon with Color Change with a move that you can follow-up on super-effectively... or, in our specific case of Synchronoise, effectively."

pause 1.0

oak @talking2mouth "Ah, yes. One must also not forget that you can forcibly change an opponent's type through the usage of your own moves."
oak @talkingmouth "Soak makes an opponent's Pokémon pure Water-type, likely denying them the usage of their own powerful same-type moves."
oak @closedbrow talkingmouth "Trick-Or-Treat and Forest's Curse are able to confer the Ghost and Grass typings onto a foe, respectively."

pause 1.0

oak @talking2mouth "Yes, Hilbert. Thank you for raising your hand."

hilbert uniform @talking2mouth "What happens if a Pokémon already has two types?"

oak @talking2mouth "It's quite simple. They gain a third type."

flannery uniform @surprised "{size=30}Woah, you can do that?{/size}"

oak @talkingmouth "Though it's worth mentioning that the effects of those two moves are mutually exclusive. You cannot add a {i}fourth{/i} type to a Pokémon by using both."
oak @winkbrow talkingmouth "Though there may be other ways to do that, if you're so inclined."

pause 1.0

oak @closedbrow talkingmouth "Of course, my coworkers have created various other moves that enable the changing of types. "
oak @talkingmouth "Instructor Byron, for one, teaches his students the move 'Metallize', which adds the Steel-type to any Pokémon, including Pokémon that are already Steel-type."
oak @talking2mouth "Instructor Lenora, for her part teaches Simple World, a move that causes all grounded Pokémon to become pure Normal-type for five standard turns."
oak @happy "Now, that won't be on the test--this class is meant to prepare you for the sorts of challenges you'll face in the realm of theory, and a Kobukan education is not within theory's repertoire."
oak @talkingmouth "That being said, it's still something to be aware of while battling classmates."

oak @talkingmouth "Right. With that out of the way, it's time to begin your exam!"
oak @talking2mouth "The last piece of information you should be aware of is that [bluecolor]all your foes are equipped only with the move Hyper Beam, and have just used it.{/color}" 
oak @angrybrow talkingmouth "As such, you have one turn to do whichever you wish, before they recharge and fire again. Make use of that time!"
oak @closedbrow talkingmouth "As always... [bluecolor]this will be graded!{/color}"

python:
    trainer1 = Trainer("red", TrainerType.Player, [
        Pokemon("Lotad", level=20, moves=["Water Gun", "Growth", "Rain Dance", "Natural Gift"], nature=Natures.Serious, ivs=[0, 0, 0, 0, 0, 0]),
        Pokemon("Crabrawler", level=20, moves=["Bulk Up", "Bubble Beam", "Leer", "Rest"], nature=Natures.Serious, ivs=[0, 0, 0, 0, 0, 0]),
        Pokemon("Tadbulb", level=20, moves=["Charge", "Rain Dance", "Soak", "Electric Terrain"], nature=Natures.Serious, ivs=[0, 0, 0, 0, 0, 0]),
        Pokemon("Golduck", level=50, moves=["Synchronoise"], nature=Natures.Serious, ivs=[0, 0, 0, 0, 0, 0], ability="Swift Swim"),
        Pokemon("Umbreon", level=50, moves=["Synchronoise"], nature=Natures.Serious, ivs=[0, 0, 0, 0, 0, 0]),
        Pokemon("Noctowl", level=50, moves=["Synchronoise"], nature=Natures.Serious, ivs=[0, 0, 0, 0, 0, 0])
    ], number=3)

    trainer2 = Trainer("oak", TrainerType.Enemy, [
        Pokemon("Kecleon", level=70, moves=["Hyper Beam"], nature=Natures.Serious, ivs=[0, 0, 0, 0, 0, 0], ability="Color Change"),
        Pokemon("Typhlosion", level=70, moves=["Hyper Beam"], nature=Natures.Serious, ivs=[0, 0, 0, 0, 0, 0], ability="Blaze"),
        Pokemon("Castform", level=70, moves=["Hyper Beam"], nature=Natures.Serious, ivs=[0, 0, 0, 0, 0, 0])
    ], number=3)

    for mon in trainer1.GetTeam():
        mon.AdjustHealth(1, True)
        
    for mon in trainer2.GetTeam():
            mon.AdjustHealth(50, True)
            mon.ApplyStatus("recharging", 1)
            mon.ChangeStats(Stats.Accuracy, 1)
            mon.ChangeStats(Stats.SpecialDefense, -6)

call Battle([trainer1, trainer2], clearstats=False, gainexp=False, healParty=False, uniforms=[True, False], lockbag=True, lockluck=True) from _call_Battle_174
$ RecordBattle("Oak11")

play music "Audio/Music/Oak Intro.ogg" noloop
queue music "Audio/Music/Oak Class.ogg"

show oak with dis

if (WonBattle("Oak11")):
    oak @talkingmouth "Hm! Well done."

else:
    oak @closedbrow talkingmouth "Room for improvement, amongst some of you. Not to worry. If you have ny questions, I'll be holding office hours quite shortly."

pause 1.0

oak @surprisedbrow talking2mouth "Hm? Melody, you have a question?"

$ PlaySound("Complaining.ogg")

pause 1.5

melody uniform on @surprisedbrow talking2mouth "Wow, rude."

pause 0.5 

show oak surprisedbrow frownmouth with dis

melody uniform @talking2mouth "In your own words, what's the point of these tests that ask us to get out of situations we'll never realistically be in?"
melody @talking2mouth "Like, wouldn't our time be better spent memorizing the types and stats of Pokémon? Ones we'll actually battle?"

pause 2.0

redmind uniform @closedbrow sweat frownmouth "Wait, that's actually a good question."

oak -surprisedbrow -frownmouth @talkingmouth "That's a very insightful question, Melody. I can give you two answers: the first is that this is, quite simply, what the school has done for centuries, to great effect."

melody @talking2mouth sadbrow "Really hope your second answer is better than that one."

oak @closedbrow sweat talking2mouth "The second answer is that the curriculum needs to change with the reality of being a trainer nowadays."
oak @sad2eyes talking2mouth "In my youth, memorization was a valid strategy, and a way to secure victory."
oak @talking2mouth "In the modern era, every trainer is carrying around a Pokédex. There is little to no point in memorizing something that's only a second or two from being read out to you, digitally."
oak @closedbrow talking2mouth "As such, it makes sense for Kobukan's test to train your ability to strategize, think creatively, and {i}utilize{/i} the information that you no longer need to memorize."
oak @talking2mouth "Admittedly, it is unlikely you will ever be in a situation where Synchronoise is the only way you can possibly win a battle."
oak @talkingmouth "But it is very possible you will be in a situation where an unlikely move, used at an unlikely time, can propel you to unlikely heights. The neural pathways these tests forge and reinforce will help, then."

pause 1.5

oak playfuleyes playfuleyebrows frownmouth @confused "Melody? Was that answer to your satisfaction?"

melody @talking2mouth "I'm still here, with my uniform on, and my phone's in my pocket. Read between the lines."

oak @talking2mouth "{size=30}...'Become a teacher', I thought. It's easy, I thought. Kobukan's the perfect place to test my theories, I thought.{/size}"

oak closedbrow talking2mouth "Right. Class dismissed. Well done on the exam, everyone. I'll see you tomorrow."

call freeroam from _call_freeroam_38

scene blank2 with splitfade 

narrator "You make your way back to the dorm, and are surprised when Blue nearly runs into you as soon as you open the door."

scene suitenight
show ethan casual:
    xpos 0.6
show blue og:
    xpos 0.4
show leaf hatless:
    xpos 0.2 xzoom -1
show yellow:
    xpos 0.8
with splitfadefaster

pause 1.0

blue @angry "Finally! We've been waiting for {i}ages.{/i}"

red @confused "Uh... what did I miss?"

ethan @happy "What, did you forget about game night?"

if (not HasEvent("Blue", "RejectGame")):
    red @unamusedbrow talking2mouth "I'll be honest, after that one time we played {i}Pokémon Mystery Dungeons & Dragons{/i} as a dorm, then never played it again, I kinda figured game night was canceled."

else:
    red @unamusedbrow talking2mouth "I'll be honest, after that one time you guys played {i}Pokémon Mystery Dungeons & Dragons{/i} as a dorm, I ditched, then you never played it again, I kinda figured game night was canceled."

blue @closedbrow talkingmouth "Nah. We've just had some scheduling issues. Every group has them."
blue @angrybrow "Only quitters let something small like having to cancel the game four times in a row derail a good campaign!"

ethan @closedbrow talkingmouth "{size=30}There's determination, and then there's whatever Blue's got...{/size}"

leaf @sarcastic "{size=30}Denial.{/size}"

blue @angry "If you two are done {i}yapping{/i}, I'd like to get started!"

show yellow surprisedbrow frownmouth with dis

blue @closedbrow "Today's session is going to be pretty different. Since {i}everyone's{/i} talking about contests and junk, I figured I should put a contest in the campaign." 
blue @surprisedbrow talkingmouth "For historical accuracy, of course. Apparently the ancient Hoennians have been doing it for centuries..."
blue @happy "Guess that's why their best battler is some male model who wiped out after, like, two weeks."

if (HasEvent("Instructor Wallace", 2.1)):
    red @closedbrow talking2mouth "{size=30}It was eighty days...{/size}"

yellow @talking2mouth "Um. Sorry, you said... you're going to DM a contest?"

blue @talking2mouth "Yeah. What about it? You've been just going {i}on{/i} and {i}on{/i} and {i}on{/i} about them, so I thought I'd... I dunno, put one in the campaign."
blue @closedbrow talking2mouth "I'm {i}trying{/i} to pretend to be interested in whatever stuff you're interested in."

yellow "[ellipses]"

show blue surprisedbrow frownmouth with dis

yellow blush -frownmouth -surprisedbrow @sadbrow talkingmouth "Thank you, Blue."

pause 1.0

blue -surprisedbrow -frownmouth @surprisedbrow lightblush talking2mouth "Whatever."

if (not HasEvent("Blue", "RejectGame")):
    blue @talkingmouth "[first_name], are you going to join us again?"

    menu:
        "Yeah.":
            $ ValueChange("Blue", 1, 0.4, pausing=False)
            $ ValueChange("Leaf", 1, 0.2, pausing=False)
            $ ValueChange("Ethan", 1, 0.6)

        "Sorry, not tonight.":
            $ AddEvent("Blue", "RejectGame2")

            blue @closedbrow talkingmouth "Whatever."

            ethan @talking2mouth "Going to bed, huh?"

            leaf @happy "We'll see you tomorrow, then!"

            yellow @talkingmouth "Goodnight."

            jump aftercontesttutorial

else:
    blue @angrybrow talkingmouth "[first_name], are you going to ditch us again?"

    menu:
        "Nah, I'll join.":
            $ ValueChange("Blue", 1, 0.4, pausing=False)
            $ ValueChange("Leaf", 1, 0.2, pausing=False)
            $ ValueChange("Ethan", 1, 0.6)

        "Yep..":
            $ AddEvent("Blue", "RejectGame2")

            blue @closedbrow talkingmouth "Whatever. You're missing out."

            ethan @talking2mouth "Going to bed, huh?"

            leaf @happy "We'll see you tomorrow, then!"

            yellow @talkingmouth "Goodnight."

            jump aftercontesttutorial

blue @closedbrow talking2mouth "Alright. Let's just sit around the table here."

show ethan casual:
    xpos 0.6 ypos 1.0
    ease 0.5 ypos 1.2
show blue og:
    xpos 0.4 ypos 1.0
    ease 0.5 ypos 1.2
show leaf hatless:
    xpos 0.2 ypos 1.0
    ease 0.5 ypos 1.2
show yellow:
    xpos 0.8 ypos 1.0
    ease 0.5 ypos 1.2

blue @closedbrow talking2mouth "So, uh... you probably want some kind of narrative justification for this, or something?"

leaf @angrybrow talkingmouth "How about... our spaceship crash-landed on a planet where they only communicate through the medium of contests!"

ethan @confused "This is fantasy, not sci-fi."

leaf @closedbrow talkingmouth "It can be both."

show ethan surprisedbrow frownmouth 
show leaf surprisedbrow frownmouth
with dis

blue @closedbrow talkingmouth "No, it can't."

pause 1.5

ethan @talkingmouth "Uh... did you just agree with me?"

show leaf -surprisedbrow -frownmouth with dis

blue @angryeyebrows talkingmouth "I'm not going to disagree with you if you're {i}objectively{/i} right."

ethan -surprisedbrow -frownmouth @surprisedbrow talking2mouth "{size=30}Bizarro world to Ethan--beaming in for pickup. You've gone off the path.{/size}"

blue @closedbrow frownmouth "[ellipses]"
blue @talkingmouth "Alright. I've got a story for this, now. Uh, basically, after making it out of the basement with the giant monstrous beast, the townspeople think that {i}you're{/i} the one who unleashed the wild monsters on the town."
blue @closedbrow talkingmouth "In order to prove your innocence, you need to... uh... show off your Pokémon's skills in a contest. Or something."

pause 1.5

leaf @sarcastic "That's basically just my 'spaceship crash-landed idea' but with peasants instead of aliens."

blue frownmouth closedbrow @angrybrow talkingmouth "Whatever, Princess! This is weird enough for me--stop getting on my ass about this!"

pause 1.0

blue @talkingmouth "The, uh, the peasants are pretty much only familiar with Normal, Grass, and Bug-types."

leaf @sadbrow talkingmouth "{size=30}Ew. Bug-types again?{/size}"

blue -closedbrow @talkingmouth "They're Kantonian peasants. So they'll want to see more Pokémon from Kanto."

red @happy "Like [pika_name]?"

blue @closedbrow talking2mouth "Nah. Your rat's Unovan. No-one in Pallet would have any idea what it even is."

red @upeyes angryeyebrows talking2mouth "Pallet Town is sheltered, not brain dead. {size=30}[pika_name] is {i}clearly{/i} still a Pikachu...{/size}"

blue @talking2mouth "Finally, the peasants will be very impressed by Pokémon that are Clever-looking or Tough. Brains and Brawn's the only way to get through to them."

pause 1.0

yellow @talking2mouth "You're basing this off of Kobukan contest rules..."

blue @surprisedeyes talkingmouth "So what? They're the only ones I know."

yellow @happy "You didn't know {i}any{/i} contest rules a couple weeks ago."

blue @glanceeyes lightblush frownmouth "[ellipses]"

blue @talkingmouth "Let's just get started. I'm not giving you a big tutorial, this time. Just figure it out as you go."

yellow @closedbrow talkingmouth "Hold on. There's something everyone should know before we begin."

blue @talkingmouth "Yeah?"

yellow @talkingmouth "At the end of round five, however many points you earned will be {i}doubled{/i}. At the end of round ten, the points you earned in that round will be {i}tripled{/i}."
yellow @closedbrow talkingmouth "That's the best time to try and go for a big combo."

ethan @closedbrow talking2mouth "Hm... there's something about STAB moves here as well, isn't there?"

yellow @surprised "Oh! Yes, there is. Um, if you use a STAB move, you get energy, which--"

blue @angrybrow talking2mouth "We can figure it out as we go! Do we want to sit around here tutorializing forever, or do we want to get {i}into{/i} it?"

ethan @closedbrow talking2mouth "{size=30}Geez, he's pushy...{/size} Look, if you need a referesher on how contests work, just click the 'Contest Help' button at the bottom of the screen."

blue @surprised "What? There's nothing like that here."

ethan @happy "Well, not yet!"

blue @closedbrow talking2mouth "Whaaat{i}ever{/i}. Let's just get this over with."

python:
    coordinators = [
        CoordinatorGroup([
            Coordinator(first_name, condition=coordinatingknowledge, isprotag=True, contestsprite="")
        ]),
        CoordinatorGroup([
            Coordinator("Blue", condition=0, partner=GetTrainerTeam("Blue", "Pidgeotto"), contestsprite="og")
        ]),
        CoordinatorGroup([
            Coordinator("Yellow", condition=75, partner=GetTrainerTeam("Yellow", "Rattata"), contestsprite="")
        ]),
        CoordinatorGroup([
            Coordinator("Leaf", condition=25, partner=GetTrainerTeam("Leaf", "Bulbasaur"), contestsprite="hatless")
        ]),
        CoordinatorGroup([
            Coordinator("Ethan", condition=50, partner=GetTrainerTeam("Ethan")[0], contestsprite="casual")
        ])        
    ]

    judges = [
        Judge(hiker, biases={ ContestMoveType.Cute : 20, ContestMoveType.Beautiful : 20, ContestMoveType.Cool : 20, ContestMoveType.Clever : 20, ContestMoveType.Tough : 20 }, customsex=Genders.Male),
        Judge(hiker2, biases={ ContestMoveType.Cute : 20, ContestMoveType.Beautiful : 20, ContestMoveType.Cool : 20, ContestMoveType.Clever : 20, ContestMoveType.Tough : 20 }, customsex=Genders.Male),
        Judge(hiker3, biases={ ContestMoveType.Cute : 20, ContestMoveType.Beautiful : 20, ContestMoveType.Cool : 20, ContestMoveType.Clever : 20, ContestMoveType.Tough : 20 }, customsex=Genders.Male)
    ]

    contestconditions = {
        "Types" : ["Grass", "Normal", "Bug"],
        "Region" : range(1, 152),#Kanto
        "Traits" : [ContestMoveType.Tough, ContestMoveType.Clever]
    }

call Contest("Dorm 25 Central Suite Grand Open", coordinators, judges, contestconditions) from _call_Contest_1

scene suitenight
show ethan casual:
    xpos 0.6 ypos 1.2
show blue og:
    xpos 0.4 ypos 1.2
show leaf hatless:
    xpos 0.2 ypos 1.2 xzoom -1
show yellow:
    xpos 0.8 ypos 1.2
with Dissolve(2.0)

#depending on who the winner is, react here

$ winner = contesthistory["Dorm 25 Central Suite Grand Open"][0].GetName()

if (winner == first_name):
    red @happy "Hey, I won! That's not bad for my first, uh, contest-like experience."

elif (winner == "Ethan"):
    ethan @confused "Wait... I won? Hold on, let me check the script. I'm pretty sure that's wrong."

elif (winner == "Leaf"):
    leaf @surprised "I... won a contest?"

    pause 1.0

    leaf @sad "I feel unclean."

elif (winner == "Blue"):
    blue @angry "Wait, I won?! Come the fuck on, were you even trying?! Do you know what I set my coordinating knowledge to? Zero! I was picking choices at random, just to fill the empty spot! How the hell did you guys screw this up?"

    ethan @closedbrow talking2mouth "Relax, no-one's {i}actually{/i} seeing this dialog. They're just reading it from the script."

elif (winner == "Yellow"):
    leaf @happy "Look at that, Yellow! You won! I knew you would, of course--didn't I say you'd be a good Coordinator?"

yellow @closedbrow talkingmouth "Well... keep in mind that actual contests involve a lot more actual moving and performing. It's good to get the theory down in something like this, but only actual practice can make you better."
yellow @happy "Still. This was really fun. Thank you, Blue."

$ coordinatingknowledge += 10
narrator "Your [contestcolor]Coordinating Knowledge{/color} went up by ten!"

blue @closedbrow talking2mouth "Yeah, well... I'm glad you had fun. I didn't like it. {i}Next{/i} Monday, we're going back to battling."

pause 1.0

show leaf angrybrow angrysmilemouth 
show yellow surprisedbrow frownmouth blush
with dis

blue @glanceeyes talking2mouth "But you should probably listen to Leaf, Yellow. She doesn't say much smart stuff, so it's a waste to ignore it when she does."

hide blue with dis

pause 1.0

leaf @talking2mouth "Next time we battle, fancy rock or not, I'm turning him into a pancake. Mark my words."

label aftercontesttutorial:

call texting from _call_texting_17

jump day010601