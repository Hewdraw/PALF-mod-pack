label secondhomeroom010609:

scene blank2

play music "Audio/Music/Oak Intro.ogg" noloop
queue music "Audio/Music/Oak Class.ogg"

show homeroom behind blank2
    
$ renpy.transition(dissolve)
show screen currentdate

show oak 
hide blank2 
with splitfade

oak @frownmouth "[ellipses]"
oak @talking2mouth "Students, pardon me, if you will. How much do you know about my colleagues here at Kobukan?"

redmind uniform @thonk "Huh? Where's this coming from?"

oak surprisedbrow frownmouth @neutraleyes neutraleyebrows talkingmouth "Yes, Miss Birch."

may uniform @talkingmouth "I know a lot about Professor Birch!"

narrator "A small chuckle echoes around the classroom."

oak @closedbrow talkingmouth "Yes[ellipses] I suppose you would, wouldn't you?"
oak -surprisedbrow -frownmouth @talkingmouth "I suppose Professor Birch is as good a place to start as any."

oak @talking2mouth "Professor Birch is a good man. Many geniuses suffer from a lack of social skills. Perhaps I say so immodestly."
oak @talkingmouth "Though undoubtedly a genius, he has escaped that stereotype. He has a beautiful wife, and, to my recollection, two children. One of which sits in this classroom."

narrator "Sam tilts his head at May."

oak @talkingmouth "He is apparently well-liked by his students, and a lot of that is due to his fondness for field trips."
oak @closedbrow talkingmouth "Yes, my students, field trips. He supposedly takes his students out for one every other day. A novel approach."
oak @surprisedbrow talking2mouth "Oh, but you're familiar with that already, it occurs to me. Professor Cherry took you out for one when she was teaching this class, no?"

red @happy "{size=30}Yeah, and remember how you rode that Cyclizar and yelled--{/size}"

pause 1.0

redmind @sad2eyes frownmouth "Oh. Right. She's not here."

oak @talkingmouth "In any case, Birch, as the foremost expert on Pokémon habitats and environments, believes immersing his students in said environments is beneficial to their understanding."
oak @angrybrow talkingmouth "And I {i}do{/i} mean immersing. The good Professor wears mud much like an overcoat. His students, too, rarely escape these field trips spotless."

may @happy "But he always wipes his feet before he comes inside!"

oak @closedbrow talkingmouth "A good man of good manners. Naturally."

pause 1.0

oak @talking2mouth "Though I mean this as no disparagement, some of the elective instructors have told me they expect the Birch students to be a bit late."
oak @talkingmouth "Supposedly, they can often be seen running into class covered in dirt and twigs from the day's expedition."

may @talkingmouth sadbrow "He says you can't {i}really{/i} explore a Pokémon's home if you're too worried about how you'll get back to yours. That means no checking the time[ellipses] and {i}long{/i} trips out into rainy jungles."

oak @talkingmouth "Demanding work, surely, but the results speak for themselves."
oak @happy "He was the first scientist to recognize that the constant rainfall that accompanied Pelipper habitats was not a result of typical weather patterns, but an innate ability some Pelipper had."
oak @talking2mouth "This discovery, once made, quickly spread like wildfire. The scientific community swiftly realized that other Pokémon had these weather-altering abilities."
oak @surprisedbrow talking2mouth "Your generation takes them for granted, but you {i}must{/i} understand the scientific and historical context of these abilities--they were previously thought to be exclusively the domain of legends."
oak surprisedbrow frownmouth @happy "The next Pokémon found to have a weather-changing ability was Torkoal--which Professor Birch discovered before the Hoenn Science Committee had even finished reviewing his Pelipper Paper."

melody uniform on @talking2mouth "Pelippaper."

pause 1.0

oak @talking2mouth "Er[ellipses] I beg your pardon?"

melody @sadbrow talking2mouth "Genuinely no idea what came over me. Sorry."

pause 1.5

melody @angrybrow talking2mouth "Move on."

oak -surprisedbrow -frownmouth @confused "Right, well[ellipses] yes, continuing on the theme of good Professor Birch[ellipses]"
oak @talkingmouth "His students' grades are quite fair, but where they {i}excel{/i} is in their teams. His students tend to have very diverse and powerful teams, and a keen ability to locate and capture more strong Pokémon."
oak @closedbrow talkingmouth "Get a Birch student to lead your capturing party, I say. You may get muddy, wet, parched, sandblown, or frozen--but you'll certainly have an adventure."

oak @talking2mouth "Well[ellipses] I believe that's everything to say on the matter of Professor Birch. Do you have any questions for me? Or perhaps Miss Birch?"

pause 1.0

oak frownmouth @talking2mouth "Yes, Mr.--{w=0.5}er, Hilbert."

hilbert uniform @talkingmouth "What was the point of this?"

oak @sad2eyes "[ellipses]"
oak @talkingmouth "There is no reason in particular. My colleagues ought to be praised more for what they do, I think."
oak @sadbrow talkingmouth "I fear that my presence at Kobukan may have[ellipses] inadvertently {i}taken{/i} something from them."

pause 1.0

redmind @thonk "Hm[ellipses] Professor Oak is probably the most famous homeroom teacher at Kobukan, but it's not like students in other classes are complaining about their teachers and saying they want to be in Oak's."

pause 0.5

redmind @thonk "Are they?"
redmind @closedbrow sweat "I mean, being honest, if they {i}were{/i} in this homeroom, at least at the beginning of the year, they'd probably {i}want{/i} to be in Birch's or Cherry's, or whoever's, instead."

pause 1.0

redmind @thonk "Maybe I should ask Yellow and Ethan about this?"

oak @talkingmouth "Well, it's just a fear, as I say, and I'm doing my best to alleviate it now by extolling their virtues. Perhaps I'll take five minutes in the next few classes to tell you about my other distinguished colleagues."
oak @happy "For now, though, we must attend to the equally-exciting work of speed{nw}" 
$ PlaySound("Complaining.ogg")
extend @happy " tie probability matrices!"

hide oak
show oakbg
with dis

narrator "You and your classmates calculate odds until your brains feel like mush[ellipses]"

$ PlaySound("bellchime.ogg")

pause 1.5

label homeroom010609bunnyrecruit:

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
            call BunnyRecruit(classchar, True) from _call_BunnyRecruit_10

        "No.":
            $ renpy.hide(classchar.lower())

            jump homeroom010609bunnyrecruit

scene blank2 with splitfade

pause 1.0

$ removestudents = { "May", "Brendan", "Klara", "Jasmine", "Yellow", "Misty", "Serena", "Dawn", "Tia"} | ({"Calem", "Grusha", "Gardenia" } if not (HasEvent("Game", "Contest1") or HasEvent("Klara", "AcceptCoordinatorClub")) else set())

call freeroam() from _call_freeroam_47

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

ethan @talking2mouth "Hey, man. Welcome back."

red @talkingmouth "Thanks. Time for a debriefing?"

show yellow surprisedbrow blush frownmouth with dis

ethan @closedbrow talking2mouth "Nah, Yellow gets shy."

yellow angrybrow @talking2mouth "You're not funny."

red @happy "He's a little bit funny."

yellow -angrybrow -frownmouth @sad2eyes blush talking2mouth "Okay, maybe a {i}little{/i} bit[ellipses]"

blue @talkingmouth "Did you get more people to come to the party today?"

call BunnyRecruitRecap() from _call_BunnyRecruitRecap_2

yellow @talking2mouth "Okay. Things are getting tight, but we still have time."

ethan @talking2mouth "Hey, have you taken any elective classes you wouldn't normally, specifically to talk to someone?"

red @confused "Dude, you're asking me? You were {i}there{/i}."

ethan @closedbrow talking2mouth "I mean, I don't know {i}why{/i} you went to class. I know why {i}I{/i} went, and it sure wasn't to try to convince someone to put on a bunny suit."

red @happy "Fair enough."

ethan @talkingmouth "So, have you?"

menu:
    "Yeah.":
        ethan @talkingmouth "Cool. Just thinking about our deadline. Only two days, so four electives, you know?"

    "Nah.":
        ethan @talkingmouth "Alright, man. Just think about it. Only two days, so four electives, you know?"

red @happy "I got it, don't worry."

ethan @talking2mouth "Alright. I'm going to wake up early tomorrow--{w=0.5}I know, I'm shocked too--{w=0.5}to go shopping again."

blue @talking2mouth "{i}Paldean{/i} seasoning this time. That Kalosian stuff tastes {i}nothing{/i} like the real thing. I bet some Unovan just threw some herbs and spices in a jar and called it Kalosian."

ethan @talkingmouth winkeyes "Wii wii, mon-sewer."

if (GetRelationshipRank("Calem") > 0):
    pause 1.0

    narrator "You're fairly certain you can hear Calem screaming somewhere in your subconscious."

    pause 1.0

ethan @talking2mouth "Anyway, since I'm doing the whole 'waking up early' thing[ellipses] I'm going to bed now. Seeya."

red @happy "Yeah, see you guys."

hide ethan with dis

pause 1.5

blue @closedbrow talking2mouth "Hey, uh[ellipses] Ethan wasn't wrong. You {i}do{/i} get shy."
blue @surprisedbrow talking2mouth "Are you even going to be able to be at the party? I mean, if everyone is wearing bunny suits, then[ellipses]"

yellow @closedbrow talking2mouth "I can make an outfit, but[ellipses]"
yellow @sad2eyes talking2mouth "I don't think I'll actually be at the party. I'm saving up all my bravery for the Millennium Drop."

pause 1.0

blue @talkingmouth "You should--"

pause 1.5

yellow @talkingmouth "Blue? Are you going to finish that?"

blue @glancebrow frownmouth "[ellipses]"

show yellow surprisedbrow frownmouth blush with dis

blue @talking2mouth closedbrow "Nah."

show blue:
    xpos 0.25 xzoom 1 
    ease 0.5 xzoom -1

blue @talking2mouth "I'll be in the kitchen."

show blue:
    xpos 0.25 xzoom -1 
    ease 0.5 xpos -0.25

pause 1.0

show yellow sadbrow -frownmouth with dis

pause 2.0

call texting() from _call_texting_34

jump day010610