label secondhomeroom010607:

scene blank2

play music "Audio/Music/Oak Intro.ogg" noloop
queue music "Audio/Music/Oak Class.ogg"

show homeroom behind blank2
    
$ renpy.transition(dissolve)
show screen currentdate

show oak 
hide blank2 
with splitfade

oak @talkingmouth "Good afternoon, students. Before we begin this evening's quiz, let's talk about items, and how Pokémon can draw strength from them."
oak @talking2mouth "I believe Champion Alder, at one point, mentioned that a Life Orb, given to a Pokémon with the ability Sheer Force, is capable of drawing strength from the item without the secondary effect of damage. What does this tell us?"

pause 1.0

oak @talking2mouth "Yes, Ms. Moore."

flannery uniform @talkingmouth "Uh, it means that Pokémon's items can be affected by their abilities."

oak @talkingmouth "Quite right, and the inverse is also true. There are some items that affect abilities, or prevent them from being affected--the Ability Shield is an example of the latter."
oak @talkingmouth "Abilities are sometimes used to enhance the strength of an item. More commonly, items are used to enhance the strength of an ability--or even allow it to be useful in the first place."

oak @talkingmouth "Who can name two items with negative effects on the holding Pokémon? Ms. Milton?"

whitney uniform @talking2mouth "Um. The Toxic Orb and the Flame Orb, Professor. We get a lot of students in the infirmary who gave one to their Pokémon and don't know why it's hurt." 
whitney @sadbrow talkingmouth "A lot of trainers think they boost the power of Poison or Fire-type moves."

oak @sadbrow talkingmouth "Unfortunate. Then I won't assume everyone in this class knows how they {i}do{/i}, in actuality, work." 
oak @talkingmouth "The Toxic Orb inflicts worsening poison on the holder. The Flame Orb inflicts a burn."
oak @confused "These seem to be strictly negative, then--hence, perhaps, the confusion--but there's a reason they continually show up in high-level matches."
oak @talking2mouth "Now, what would a use case be for them? [ellipses]Mr. [last_name]?"

menu:
    "[knowledgeoption] Give the standard use case.":
        red uniform @talking2mouth "A Toxic Orb could be given to a Pokémon with Poison Heal, to activate their ability immediately. The Flame Orb could do the same thing for a Pokémon with Flare Boost."
        red @talkingmouth "Both could be given to a Pokémon with Magic Guard, to make them immune to Sleep, Paralysis, Freeze[ellipses] though you wouldn't want to give the Flame Orb to a physical attacker."
        red @happy "Even if you aren't taking damage from the burn, it'll still cut your attack in half."
        red @closedbrow talking2mouth "But, uh, there aren't any Physically-attacking Pokémon with Magic Guard that I can think of[ellipses]"

        $ TraitChange("Knowledge", 1)

        oak @talkingmouth "Yes, quite right."
        oak @talkingmouth "There are also, of course, more obscure use cases one could imagine, though many are relegated to the realm of hypothetical."
        oak @closedbrow talkingmouth "For example, do all of you remember last week's test, when you were tasked with poisoning a Steel-type by using the the ability Corrosion?" 
        oak @talkingmouth "It may interest you to know that corrosive Pokémon interact with the Toxic Orb in a fascinating way."
        oak @surprisedbrow talking2mouth "Regardless of their own typing--whether they are Steel-type, or Poison-type--a Pokémon with Corrosion is capable of using a Toxic Orb to badly poison {i}itself{/i}!"
        oak @talkingmouth "Though of dubious likelihood, one could imagine a situation in which you may force your Toxic Orb onto an opponent's Pokémon with Corrosion." 
        oak @happy "That would let you punish the sort of Pokémon who normally uses poison as a weapon with a taste of its own medicine! My good friend in the Elite Four would hate to have seen that!"

    "[witoption] Think up a new use case.":
        red uniform @talking2mouth "A Toxic Orb could be forced onto an opponent's Pokémon with Corrosion. You said that abilities can affect their items, right?" 
        red @talkingmouth "The only Pokémon that have the ability Corrosion are Poison-type, but if a corrosive Pokémon is holding a Toxic Orb, it can still be poisoned."

        oak @closedbrow talkingmouth "Very clever out-of-the-box thinking. Yes, that's true--I suppose you remember last week's test, when you had to poison a Steel-type with your own Salandit."
        oak @talkingmouth "Do you have a similarly creative use case for the Flame Orb, though?"

        red @sweat happy "Uh[ellipses] you could probably put one around a Pokémon egg you're trying to incubate to replicate the effects of Flame Body, even if you don't have a Flame Body Pokémon with you?"

        pause 1.0

        oak @confused "Would that work?"

        red @sadbrow talkingmouth "I don't know."

        oak @closedbrow talking2mouth "Perhaps I'll ask Professor Elm's opinion on the matter. Regardless, another {i}very{/i} creative answer--though keep in mind that there's nothing wrong with the tried-and-true answers, either, if they're correct."

        redmind @closedbrow sweat "Yeah, maybe I was showing off a bit."

        $ TraitChange("Wit", 1)

        oak @talkingmouth "Remember, everyone, the standard use cases--Toxic Orbs are frequently given to a Pokémon with Poison Heal, to activate their ability immediately. The Flame Orb could do the same thing for a Pokémon with Flare Boost."
        oak @talking2mouth "Both could be given to a Pokémon with Magic Guard, to make them immune to Sleep, Paralysis, Freeze[ellipses] though you wouldn't want to give the Flame Orb to a physical attacker."
        oak @happy "Even if you aren't taking damage from the burn, it'll still diminish your physical offense."
        oak @closedbrow talking2mouth "Of course, that's an unnecessary distinction--there are no Pokémon with Magic Guard that typically rely on Physical attacks."

oak @talkingmouth "You can assume, I'm sure, that I don't mention these interactions {i}purely{/i} for the fun of it." #Always a struggle to balance Oak's obtuse language with the player's ability to comprehend him
oak @talking2mouth "They will be of the utmost importance in our upcoming test, which we will be engaging in immediately. As always, pay attention to the moves, abilities, and items, of the Pokémon on your side."
oak @closedbrow talkingmouth "Remember, there is a guaranteed way to pass every single one of these tests--{i}without{/i} relying on luck."
oak @talking2mouth "Finally[ellipses] the last Pokémon you need face in this test is a [bluecolor]Glimmora{/color} with [bluecolor]Corrosion.{/color}"
oak @happy "Consider that the 'Champion' of this test!"

pause 1.0

oak @talkingmouth "And with that, please take out your pencils, and [bluecolor]remember this will be graded!{/color}"

label stalltest:

python:
    trainer1 = Trainer("red", TrainerType.Player, [
        Pokemon("Porygon2", level=40, moves=["Mimic", "Protect", "Trick", "Conversion"], nature=Natures.Serious, ivs=[0, 0, 0, 0, 0, 0], ability="Trace")
        
    ], number=1)

    trainer2 = Trainer("oak", TrainerType.Enemy, [
        Pokemon("Breloom", level=70, moves=["Toxic"], nature=Natures.Serious, ivs=[0, 0, 0, 0, 0, 0], ability="Poison Heal"),
        Pokemon("Slaking", level=70, moves=["Giga Impact"], nature=Natures.Serious, ivs=[0, 0, 0, 0, 0, 0], ability="Truant", item=Item.ToxicOrb),
        Pokemon("Chesnaught", level=50, moves=["Hammer Arm"], nature=Natures.Serious, ivs=[0, 0, 0, 0, 0, 0], ability="Bulletproof", item=Item.Leftovers),
        Pokemon("Staraptor", level=70, moves=["Fly"], nature=Natures.Serious, ivs=[0, 0, 0, 0, 0, 0], ability="Intimidate"),
        Pokemon("Dugtrio", level=70, moves=["Dig"], nature=Natures.Serious, ivs=[0, 0, 0, 0, 0, 0], ability="Arena Trap"),
        Pokemon("Glimmora", level=70, moves=["Solar Beam"], nature=Natures.Serious, ivs=[0, 0, 0, 0, 0, 0], ability="Corrosion", item=Item.BlackSludge)
    ], number=1)

    #for mon in trainer1.GetTeam():
    #    mon.AdjustHealth(1, True)
        
    for mon in trainer2.GetTeam():
            mon.ApplyStatus("forecasting")
            mon.ChangeStats(Stats.Accuracy, 1)

    trainer1.GetTeam()[0].Health = 1
    trainer1.GetTeam()[0].GetMoves()[0].PP = 1
    trainer1.GetTeam()[0].GetMoves()[1].PP = 7
    trainer1.GetTeam()[0].GetMoves()[2].PP = 4
    trainer1.GetTeam()[0].GetMoves()[3].PP = 1

    trainer2.GetTeam()[0].Health = 1
    trainer2.GetTeam()[0].ApplyStatus("burned")
    trainer2.GetTeam()[2].Health -= 60
    trainer2.GetTeam()[3].Health = 1
    trainer2.GetTeam()[4].Health = 1
    trainer2.GetTeam()[5].Health -= 5

call Battle([trainer1, trainer2], clearstats=False, gainexp=False, healParty=False, uniforms=[True, False], lockbag=True, lockluck=True, customswitchbrain=oakstalltestswitchbrain, preserveAllStats=True) from _call_Battle_187
$ RecordBattle("Oak14")

play music "Audio/Music/Oak Intro.ogg" noloop
queue music "Audio/Music/Oak Class.ogg"

show oak with dis

oak @surprisedbrow talking2mouth "Incredible! This was one of the hardest tests I'd prepared for this semester. {i}Splendidly{/i} well done, to everyone who passed--everyone who didn't, my office hours will be open right after class."

if (WonBattle("Oak14")):
    oak @talking2mouth "Mr. [last_name], I notice you did rather well on this test. Could you explain your thought process?"

    red uniform @talkingmouth "It's like you said this morning, Professor--just use whichever move lets you last one more turn."
    red @happy "If there's multiple moves that fit that criteria, then use whichever move sets you up best for the next turn." 
    red @talkingmouth "Keep hold of valuable items, conserve the PP of your best moves, and do everything you can to hold onto your HP. If you don't know what's coming next, you need to be ready to take a hit."

    oak @closedbrow talkingmouth "Splendidly put."

else:
    oak @talkingmouth "Room for improvement, amongst some of you. Not to worry. If you have any questions, I'll be holding office hours quite shortly."

    red uniform @sad2eyes poutmouth "Maybe I should swallow my pride and actually attend one of them one of these days..."

    oak @talking2mouth "As a general word of advice, consider the following tenets of stall strategies:"
    oak @talkingmouth "Firstly: Use whichever move lets you last one more turn."
    oak @happy "Secondly: If there's multiple moves that fit that criteria, then use whichever move sets you up best for the next turn." 
    oak @talkingmouth "Thirdly: keep hold of useful items, conserve the PP of your best moves, and do everything you can to hold onto your HP." 
    oak @talking2mouth "Stall strategies excel in not getting hit. But it is a core truth of every stall-focused Pokémon that you {i}will{/i} eventually get hit, and you need to be able to resist the hit, when it comes."

$ PlaySound("bellchime.ogg")

queue music "Audio/school_crowd.ogg" channel "crowd" fadein 1.5

oak @talkingmouth "Very well done, class. Enjoy the rest of your day!"

hide oak with dis

pause 1.5

label homeroom010607bunnyrecruit:

python:
    bunnyrecruits = []
    for char in ["Hilbert", "Whitney", "Flannery", "Dawn", "May"]:
        if (CanBunnyRecruit(char)):
            bunnyrecruits.append((char, char))

if (len(bunnyrecruits) > 0):
    narrator "Now seems like it might be a good time to mention the party on Saturday[ellipses] whom should you approach?"
    python:
        classchar = renpy.display_menu(bunnyrecruits)
        renpy.transition(dis)
        renpy.show(GetCharacterSprite(classchar, None, True))

    "You want to talk to [classchar]?"

    menu:
        "Yes.":
            call BunnyRecruit(classchar, True) from _call_BunnyRecruit_4

        "No.":
            $ renpy.hide(classchar.lower())

            jump homeroom010607bunnyrecruit

scene blank2 with splitfade

pause 1.0

show hallway_b 
show brendan shadow angrybrow frownmouth 
with splitfade

if (GetRelationshipRank("Brendan") > 0):
    redmind @surprisedbrow frownmouth "[ellipses]Woah. I've only seen Brendan wear that expression once before, when we were talking about his father[ellipses]"

else:
    redmind @surprisedbrow frownmouth "[ellipses]Woah. That's an expression I haven't seen before."

pause 1.0

red @sadbrow talkingmouth "Hey, Brendan. Is something biting you?"

brendan -shadow -angrybrow @surprisedbrow talking2mouth "[first_name]?"
brendan @talking2mouth "Man, I gotta get better at hiding my feelings on my face."

red @happy "Nah. Then I wouldn't have asked you what was up. So[ellipses] what's up?"
red @sadbrow talkingmouth "Is it about the party? Because we're really grateful you agreed to help with the suits, but if it's too much of a problem, then[ellipses]"

brendan @talking2mouth "Nah. Honestly, the party stuff is a nice distraction. I've got one suit about halfway done already."

red @surprised "Woah! That's--that's {i}really{/i} fast, right?"

brendan @closedbrow talking2mouth "It's alright. I've made one before. They're not difficult, usually. Not a lot of fabric. Tearing the silk's the biggest thing you got to look out for."

pause 1.0

red @talkingmouth "So if it's not party stuff, then...?"

if (IsCoordinator()):
    brendan @talking2mouth "Remember during the Millennium Drop tryouts, when Phobos was really getting up in Lisia's face?"

    red @confused "Vaguely. I saw something, but didn't hear it. Know what he said?"
else:
    brendan @talking2mouth "You weren't there, but during the Millennium Drop tryouts, Phobos {i}really{/i} got up in Lisia's face."

    red @confused "What was he doing?"

brendan @talking2mouth "Not totally sure. But I think Liz stopped him."
brendan @angrybrow talking2mouth "And[ellipses] he didn't like that."

red @talking2mouth "Ugh. Has he been causing problems for the Coordinator Club since then?"

brendan @talking2mouth "I mean, it's only the first schoolday since then. But[ellipses] yeah. I mean, I arrived early, he just rolled in, and he started sayin' stuff to Liz that[ellipses]" 
brendan @angrybrow talking2mouth "I had to get some fresh air and cool my head. Didn't want to do something stupid in front of her."
brendan @talking2mouth "I thought that asshole at least {i}liked{/i} contests, but I think he just doesn't like battling, and became a coordinator to have an excuse to get out of it."
brendan @sweat closedbrow talking2mouth "'Course, when I lay it out like that, it sounds pretty familiar."

if (GetRelationshipRank("Brendan") > 0):
    red @angrybrow talking2mouth "Hey, even {i}if{/i} that's why he's a coordinator, you two are {i}completely{/i} different."

    brendan @confusedbrow talking2mouth "Yeah? How'd you figure?"

    if (HasEvent("Melody", "PhobosDick")):
        red @talking2mouth closedbrow "He's a dick. I've been saying it since the day I saw him."
    elif (HasEvent("Melody", "PhobosDick")):
        red @talking2mouth closedbrow "He's a dick. I wasn't sure how I felt about him, at first, but I {i}definitely{/i} know now."
    else:
        red @talking2mouth closedbrow "He's a dick. I can't believe I ever thought he was pretty cool."

    $ ValueChange("Brendan", 1)

    brendan -frownmouth @sadbrow talkingmouth "Thanks, bro."

brendan @closedbrow talking2mouth "Anyway, I gotta go back to my dorm, get changed, pick up May, and go back in. Can't leave Liz there alone with him."

pause 1.0

if (IsCoordinator()):
    brendan @talking2mouth "Hey, since you're competing in the Millennium Drop Water Festival Contest, why don't you join me?"
    brendan @talkingmouth "You'll learn a bit more about contests from watching another meeting, and when there's some downtime, you can tell people about the party on Saturday."

else:
    brendan @talking2mouth "Hey, why don't you join me? Even though you're not a Coordinator, when there's some downtime, you can tell people about the party on Saturday."

brendan @talking2mouth angrybrow "And[ellipses] maybe Phobos won't be as {i}much{/i} of a dick if the person who beat Melody is there."

red @confused "You know about that?"

brendan @talking2mouth "Yeah, Melody mentioned it. Misty saw her Wimpod had one of those rocks you use, and thought she stole it from you."
brendan @talking2mouth "Then Melody said that she couldn't even beat you in a battle, so, uh, how would she steal one of your[ellipses] crystals?"

pause 1.0

red @confused "Didn't see that coming. Did she mention how she got it, then? It's true she didn't steal it from {i}me{/i}, but I don't know how she got it, either."

brendan @talking2mouth "Nah, she didn't say. I'd keep an eye on Phobos, though. I figure he's involved, somehow. I mean, the two are related."

red @talking2mouth "Yeah[ellipses] weird."

pause 1.0

brendan @talking2mouth "So, bro, are you in?"

menu:
    "Sure.":
        $ ValueChange("Brendan", 1)

        brendan @talking2mouth "Thanks, bro. Let's go."

        scene blank2 with splitfade

        if (not HasEvent("Klara", "AcceptCoordinatorClub")):
            brendan contest @talkingmouth "May's at Relic Hall--she had some stuff to do before she got changed for the meeting. We'll meet her there."

        call contestscenequeue() from _call_contestscenequeue_1

        label contest0607bunnyrecruit:

        if (IsAfter(6, 6, 2004) and IsBefore(12, 6, 2004)):
            python:
                bunnyrecruits = []
                allpresent = { "May", "Jasmine", "Yellow", "Misty", "Serena", "Dawn", "Tia"} | ({"Calem", "Grusha" } if not HasEvent("Game", "Contest2") else set())
                if (HasEvent("Game", "Contest3")):
                    allpresent.remove("Tia")
                for char in allpresent:
                    if (CanBunnyRecruit(char)):
                        bunnyrecruits.append((char, char))

            scene concerthallstage with splitfade

            if (len(bunnyrecruits) > 0):
                narrator "As the coordinators (and guests) leave the building, now seems like it might be a good time to mention the party on Saturday[ellipses] whom should you approach? "

                python:
                    contestchar = renpy.display_menu(bunnyrecruits)
                    renpy.transition(dis)
                    extra = "contest" if contestchar in ["May", "Jasmine", "Yellow", "Misty", "Serena", "Dawn", "Tia"] else ""
                    renpy.show(GetCharacterSprite(contestchar, None, False, extra))

                "You want to talk to [contestchar]?"

                menu:
                    "Yes.":
                        call BunnyRecruit(contestchar, False, extra) from _call_BunnyRecruit_5

                    "No.":
                        $ renpy.hide(contestchar.lower())

                        jump contest0607bunnyrecruit

                call nightscenequeue() from _call_nightscenequeue_2

    "Nah.":
        $ AddEvent("Professor Oak", "LearnedAboutContestColiseum")

        brendan @talking2mouth "Alright, bro. Well, if you ever change your mind, just pop over at the Contest Coliseum--remember, you can get there from the path behind the Battle Hall."

        red @talkingmouth "I'll keep it in mind. Thanks."

        hide brendan with dis

        $ removestudents = { "May", "Brendan", "Klara", "Jasmine", "Yellow", "Misty", "Serena", "Dawn", "Tia", "Calem", "Grusha", "Gardenia" }

        call freeroam() from _call_freeroam_45

stop music fadeout 1.5
queue music "audio/music/NewFriends_start.ogg" noloop
queue music "audio/music/NewFriends_loop.ogg"

scene blank2 with splitfade

pause 1.0

scene suitenight
show ethan
show blue og:
    xpos 0.25
show yellow:
    xpos 0.75
with splitfade

if (GetEventDatetime("Game", "Contest1") == calDate or ((GetEventDatetime("Game", "Contest2") == calDate or GetEventDatetime("Game", "Contest3") == calDate) and HasEvent("Yellow", "AcceptPartner"))):
    blue @talking2mouth "{i}There{/i} you two are. About time."
    blue @angry "You better not distract Yellow too much from what we're {i}supposed{/i} to be doing here, [first_name]."

    yellow @talking2mouth "Blue, please don't get worked up. We were only gone for a couple hours, watching the coordinators practice."

    red @talking2mouth "Yeah, I took the time to drop some lines on the party. Don't worry, we were multitasking."

else:
    blue @talking2mouth "{i}There{/i} you are. About time."
    blue @angry "You better not get distracted from what we're {i}supposed{/i} to be doing here, [first_name]."

    if (calDate in [GetEventDatetime("Game", "Contest1"), GetEventDatetime("Game", "Contest2"), GetEventDatetime("Game", "Contest3")]):
        red @closedbrow talking2mouth "Calm down. I was only gone for a couple hours, watching the coordinators practice. I asked around about the party while I was there. I was multitasking."

        if (HasEvent("Klara", "AcceptPartner")):
            blue @talking2mouth "{size=30}Spending time with the person who {i}caused{/i} this, probably.{/size}"

            red @sad2eyes sadeyebrows frownmouth "[ellipses]"

    else:
        red @closedbrow talking2mouth "Calm down. It's only Monday. We'll be fine."

blue @talking2mouth "Whatever. How did everyone do?"

yellow @talking2mouth "I've made a decent start on a couple suits--I'll need to run out to Inspira for some more fabric soon, though."

ethan @talking2mouth "I'll grab it. Just give me a list--I'll do it tomorrow, soon as classes let out."

blue @talking2mouth "Are you trying to get out of giving your report? What did {i}you{/i} do today?"

ethan @closedbrow talking2mouth "{size=30}Damn, already caught out.{/size} Yeah, I, uh, kinda figured out that I had no idea what I was doing. Turns out I can't figure out how to hack a security system in five days."
ethan @sadbrow talkingmouth "So I'm trying to be helpful by grabbing stuff for people who can actually contribute."
ethan @sad2eyes sadeyebrows shadow talkingmouth "{size=30}Unless you need me to make a Pokémon go crazy again...?{/size}"

blue @frownmouth "[ellipses]"
blue @talking2mouth "Then can you pick up some ingredients tomorrow, too?"

ethan @surprisedbrow talking2mouth "Huh? I mean, yeah, totally, man. Uh, what are you thinking? Green stuff? Meat?"

blue @lightblush frownmouth glancebrow "[ellipses]"
blue @talking2mouth "Icing. And, uh, sugar. Sprinkles. That kind of stuff."

redmind @happy "He almost seems embarrassed to admit he's going to try and make something sweet."

blue @talking2mouth "I'll write a list and give it to you in the morning."

ethan @talking2mouth "Sure thing, man."
ethan @talkingmouth "What about you, [first_name]? Anything I can get for you?"

red @talking2mouth "Uh, don't think so. Thanks, though."

yellow @talking2mouth "Did you have any success, um, telling people about the party?"

call BunnyRecruitRecap() from _call_BunnyRecruitRecap

red @sadbrow talkingmouth "Sounds like we're all caught up, then. I guess the only question left is[ellipses]"

pause 1.5

ethan @talking2mouth "No change. Leaf spent all day in the bathroom again."

blue @talking2mouth "Guess that makeup really {i}is{/i} waterproof."

show blue surprisedbrow frownmouth
show ethan surprisedbrow frownmouth
with dis

yellow @sadbrow talking2mouth "Um... Actually, she moved out of the dorm last night."

pause 1.5

red @surprisedbrow talking2mouth "What?! She moved out?"

show blue -surprisedbrow
show ethan -surprisedbrow
with dis

yellow @sadbrow talking2mouth "Not forever, {size=30}I think{/size}. She texted me that she's booked a hotel room through Friday. But she hasn't replied to me since."

blue @angrybrow talking2mouth "Well, geez, {i}that's{/i} something you could've mentioned this morning!"

yellow @closedbrow talking2mouth "Leaf didn't want any of you to know where she's gone. She just wanted to tell us she's eating, so we don't break down the door or call the police."

blue @closedbrow talking2mouth "Ugh. I don't get it. Who {i}cares{/i} if she has smudgy makeup or whatever? She's missing school."

yellow @closedbrow talking2mouth "She {i}knows{/i} that, Blue. She's upset."

blue @closedbrow talking2mouth "Still. What happened sucks, but scrubbing her face raw for a week straight won't make it any better for her."

pause 1.0

red @talking2mouth "Did we make a decision on if we were going to tell her about the party?"

ethan @talking2mouth "I was going to as soon as I saw her, but I guess that's not happening 'til Saturday."
ethan @sadbrow talking2mouth "Maybe she overheard us and already knows about it?"

red @closedbrow talking2mouth "Probably not."

blue @closedbrow talking2mouth "We shouldn't tell her until we're sure this'll work."
blue @closedbrow talking2mouth "If {i}someone{/i} doesn't pull their weight, and this party is a flop, I don't want her thinking that it was my fault."

ethan @talkingmouth "If you {i}really{/i} squint, it sounds like Blue's saying he doesn't want to get her hopes up."

blue @talking2mouth "You can't squint at something you hear, dumbass."

ethan @upeyes angryeyebrows talking2mouth "Whatever. I'm going to bed."

hide ethan with dis

pause 1.0

red @talking2mouth "Don't be a dick to Ethan. I know you can't stop it when it comes to me, but he wants to be your friend."
red @closedbrow talking2mouth "I mean, you gave him a Foreveral. That's, what, second base?"

blue @glancebrow talking2mouth "Stop being weird. And unless you're going to help me with the cooking, or Yellow with sewing, go to bed. You've got a bigger job than both of us, and we can't have you screwing it up."

red @unamusedbrow talkingmouth "Your faith in me is {i}so{/i} appreciated."

call texting() from _call_texting_32

jump day010608