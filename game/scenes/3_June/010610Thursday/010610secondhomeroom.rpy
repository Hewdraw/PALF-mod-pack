label secondhomeroom010610:

scene blank2

play music "Audio/Music/Oak Intro.ogg" noloop
queue music "Audio/Music/Oak Class.ogg"

show homeroom behind blank2
    
$ renpy.transition(dissolve)
show screen currentdate

hide blank2 
with splitfade

narrator "The moment you walk into homeroom[ellipses]"

show oak happy with vpunch 

oak @happybrow talkingmouth "Oh, good, you're here! Quickly now, sit down, sit down!"

hide oak 
show oakbg 
with dis

oak @talkingmouth "Now, are we all--well, it's probably close enough! Let's begin, then[ellipses]"

whitney uniform @talkingmouth "{size=30}Psst. What's up with your bestie?{/size}"

red uniform @talkingmouth "{size=30}Professor Oak? Beats me.{/size}"

may uniform @talkingmouth "{size=30}Yesterday, he talked about my Dad. Maybe he's really excited to talk about some of the other Professors?{/size}"

red @talkingmouth "{size=30}Huh. I guess he's kind of like[ellipses] a {i}fan{/i} of the other faculty here?{/size}"
red @talkingmouth "{size=30}He probably read their papers, and knew of them in an academic context, but I guess he never had the chance to meet them face-to-face before.{/size}"

whitney @confusedbrow talkingmouth "{size=30}Didn't he go to conferences and stuff?{/size}"

red @talking2mouth "{size=30}He'd usually send an aide in his place. I never really thought about {i}why{/i} he'd do that before[ellipses]{/size}"

show oak angrybrow frownmouth with vpunch:
    ypos 1.2 zoom 1.3

oak frownmouth @talking2mouth "Shush!"

show oak:
    ypos 1.2 zoom 1.3
    ease 0.5 ypos 1.0 zoom 1.0

red @wince talking2mouth "Sorry, Professor."

melody on @talking2mouth "Yeah, [melody_name], don't be effing {i}rude{/i}."

redmind @unamusedbrow unamusedmouth "[ellipses]She says while not even wearing her uniform."

oak -angrybrow -frownmouth @talking2mouth "Now, I told you about Professor Birch yesterday. I planned to move onto Professor Rowan today, but realized, given your recent interactions with him, that he may already be fresh in your minds."

may @sadbrow talkingmouth "{size=30}He {i}sure{/i} is[ellipses]{/size}"

if (GetRelationshipRank("May") > 1):
    pause 1.0

    redmind @closedbrow frownmouth "I guess what Rowan said to her still bothers her."

    red @happy "{size=30}Hey. Chin up.{/size}"

    may @sadbrow "{size=30}Mm.{/size}"

    $ ValueChange("May", 1, 0.25)

oak @happy "So, who better to take Rowan's place than his very own student?"
oak @talkingmouth "I speak, of course, of Professor Augustine Sycamore. I plan to have a short meeting with him before class tomorrow, so who better to discuss?"

pause 0.5

oak @closedbrow talking2mouth "{i}Ahem.{/i}"
oak @talkingmouth "In many ways, Sycamore is a student of mine, as well. In fact, I have a letter from him stating as much."

redmind @happy "Oh, yeah, Sam's {i}definitely{/i} a fan."

oak @talkingmouth "You see, I am primarily a Poké-Homo Psychosociologist."

pause 1.0

flannery uniform @talking2mouth "{size=30}Wait, hold on, don't tell, me, I can--{/size}"

whitney @closedbrow talking2mouth "{size=30}'Poké' means Pokémon. 'Homo' means human. 'Psycho' means the mind, and 'socio' means society, and inter-person interactions.{/size}"
whitney @happy "{size=30}So he's a doctor who studies the relationships between humans and Pokémon!{/size}"

flannery @upeyes talkingmouth angryeyebrows "{size=30}Nurse course.{/size}"

pause 0.5

oak @talkingmouth "I invented the modern digital Pokédex primarily so humans could understand more about the mysterious Pokémon which live around us."
oak @closedbrow talkingmouth "It was my belief that greater knowledge would lead to stronger bonds."
oak @happy "Professor Sycamore takes this belief a step further. His thesis is that stronger bonds lead to stronger Pokémon!"
oak @talkingmouth "Augustine is the world's {i}premier{/i} researcher on the topic of Mega Evolution. And it is his conviction that Mega Evolution is possible only when a strong bond exists between trainer and Pokémon."

pause 1.0

oak @talking2mouth "There are many trainers--even skilled ones--who have made exhaustive attempts to achieve Mega Evolution, with no result."
oak @talking2mouth "Even with the appropriate Mega Stone, and a Keystone held in the trainer's grip, sometimes nothing happens."
oak @talkingmouth "It is Professor Sycamore's belief that, in cases such as these, the bonds between Pokémon and trainer simply aren't strong enough."
oak @closedbrow talking2mouth "One can understand the perspective of the Pokémon. Mega Evolution is an explosive--even dangerous--transformation. Some believe it can even be painful."
oak @sadbrow talkingmouth "If this is true, surely no Pokémon would subject themselves to Mega Evolution without absolute faith that they are in good hands."
oak @talking2mouth "The bond of trust between Pokémon and Trainer must, therefore, be unbreakable for Mega Evolution to occur."

pause 1.0

redmind @thinking "That makes sense, but[ellipses] what about that Wild Lopunny? What about the Megaverals? How does all that tie into this?"
redmind @thinking "Are the Megaverals {i}actually{/i} Mega-evolving the Pokémon, or is it only an imitation, like how Minigigamax is an imitation of Gigantamax?"

pause 0.5

redmind @happy "Suddenly, I get why people might want to become researchers!"

pause 1.0

oak @talking2mouth "Of course, all of this is theory, not dogma. Whether Mega Evolution is dangerous {i}at all{/i} is much debated within the scientific community, who are largely split along regional lines."
oak @surprised "There are even regions where the belief that Mega Evolution harms the Pokémon is so prevalent it's {i}banned{/i} outright."
oak @talking2mouth "Galar was the first to take that step--though there are rumors that was due to the fear Mega Evolution might eclipse Dynamax in popularity, rather than concern for the Pokémon's well-being."
oak @talkingmouth "Professor Sycamore's position, stated firmly and publicly, is that Mega Evolution is draining but quite safe. In lieu of personal experience, I choose to trust the expert."
oak @sweat closedbrow talking2mouth "Though perhaps this is a moot point. I'm quite far from the age where I could be attempting any of these new 'gimmicks,' anyway."

pause 1.0

oak @talkingmouth "We can credit the general public knowledge of all this information to Professor Sycamore, incidentally."
oak @closedbrow talkingmouth "Even though he is on the younger side, he is the one who popularized and recorded much of the information we have about Mega Evolution." 
oak @talkingmouth "Though known about and practiced for centuries, it was relatively obscure knowledge passed down between secretive Mega Evolution sects that concealed themselves in ancient towers, castles, and other such places."

pause 1.0

oak @happy sweat "Ah, but I've said very little about the man, Professor Sycamore, haven't I?"
oak @talkingmouth "Apologies. He's a splendid Professor. He drives a very student-directed classroom, encouraging students to lead his lectures and lessons." 
oak @angrybrow talkingmouth "It would be remiss of you to misinterpret this as laziness, though. I assure you, his strategy is an extremely effective and empirically-supported way of teaching." 
oak @talking2mouth "There is no better way to learn, some say, than to teach. This year I have found that to be {i}very{/i} true--as have Professor Sycamore's students." 
oak @talkingmouth "Reinforcing knowledge with emotion is also one of Augustine's specialties. He'd tell you it comes with being Kalosian."
oak @talking2mouth "Professor Sycamore is quite effective at bringing out the emotions of his students, by playing on the bonds that exist between all people."
oak @closedbrow talkingmouth "Romances, rivalries, gratitude, spite[ellipses] every feeling can be used to teach a lesson. It's a masterful technique I can't even begin to approach."
oak @talkingmouth "The effectiveness of this strategy is apparent. His students are typically self-driven, often leading their classmates in groups, and have exceptional recall of what they've learned and taught."

pause 1.0

oak @talkingmouth happybrow "Or so he says. This is my first year at Kobukan, of course, so I've little option but to take some of his claims at face value."
oak @happy "Regardless, I've found him to be pleasant, generous, fun-loving, intelligent[ellipses]"

redmind @upeyes sadeyebrows "Geez, does Sam have a crush? If I didn't know he was straight as a rail, I'd think so. He's outright {i}gushing{/i} over Sycamore, now."

oak @talkingmouth "{gradualsize=20-36}[ellipses]but gets terribly homesick,{/gradualsize} so he sometimes visits Instructrice--or was it Instructeur?--Fantina, just to hear a bit of Kalosian."
oak @closedbrow sweat talking2mouth "Er, but that's enough about him. Unless, er, anyone has any more questions about Doctor Sycamore?"

pause 1.0

oak @talkingmouth "Yes, Blue."

blue uniform @talking2mouth "I heard he {i}dropped out{/i} of that Mega Evolution school they have there in Kalos."
blue @surprised "How can you be the world's expert on Mega Evolution if you can't pull it off yourself?"

oak @talking2mouth "A fair question. Though I must correct an assumption here--he {i}can{/i},{w=0.5} and I've seen him do so."
oak @talkingmouth "I believe his decision to end his education at the Tower of Mastery was a practical one. He understood that learning how to Mega Evolve was a tremendous boost in his competency as a battler, and his future career."
oak @talkingmouth "Remaining at the Tower for another ten years to {i}Master{/i} Mega Evolution would, perhaps, have brought significantly diminishing returns."

blue @closedbrow "Sounds like he was a quitter who couldn't hack it. Ten years? I'd have mastered that shit in six months."

oak @happy "An interesting philosophy. Perhaps his Mega-Evolved Kangaskhan would be able to change your mind."
oak @sadbrow happymouth "Oh[ellipses] I said that in jest, but, truthfully, that would be an {i}incredible{/i} battle to watch. Perhaps before the school year is over[ellipses]"

blue @angrybrow talkingmouth "Bring it {i}on!{/i}"

redmind @upeyes "Oh, Blue[ellipses] you'll always bring a little bit of [oldblue_name] with you, won't you?"

scene blank2 with dis

$ PlaySound("bellchime.ogg")

pause 1.5

label homeroom010610bunnyrecruit:

python:
    bunnyrecruits = []
    for char in ["Hilbert", "Whitney", "Flannery", "Dawn", "May"]:
        if (CanBunnyRecruit(char)):
            bunnyrecruits.append((char, char))

if (len(bunnyrecruits) > 0):
    scene homeroom with dis

    narrator "Now seems like it might be a good time to mention the party on Saturday[ellipses] whom should you approach?"
    python:
        classchar = renpy.display_menu(bunnyrecruits)
        renpy.transition(dis)
        renpy.show(GetCharacterSprite(classchar, None, True))

    "You want to talk to [classchar]?"

    menu:
        "Yes.":
            call BunnyRecruit(classchar, True) from _call_BunnyRecruit_12
            
            scene blank2 with splitfade

            pause 1.0

        "No.":
            $ renpy.hide(classchar.lower())

            jump homeroom010610bunnyrecruit

if (not HasEvent("Game", "Contest3")):
    $ removestudents = { "May", "Brendan", "Klara", "Jasmine", "Yellow", "Misty", "Serena", "Dawn", "Tia"} | ({"Calem", "Grusha", "Gardenia" } if not (HasEvent("Game", "Contest1") or HasEvent("Klara", "AcceptCoordinatorClub")) else set())

call freeroam() from _call_freeroam_48

stop music fadeout 1.5
queue music "audio/music/NewFriends_start.ogg" noloop
queue music "audio/music/NewFriends_loop.ogg"

scene blank2 with splitfade

pause 1.0

scene suitenight
show ethan
show blue og:
    xpos 0.25
show yellow closedeyes angryeyebrows frownmouth:
    xpos 0.75
with splitfade

red @talkingmouth "Hey guys. I'm back."

pause 0.5

red @talkingmouth "Yellow, what's up?"

yellow "[ellipses]"

ethan @talking2mouth "She's doing deep-breathing exercises. She's kinda nervous about this party--she {i}really{/i} wants to get it perfect."

if (HasEvent("Yellow", "AcceptPartner")):
    ethan @talking2mouth "About the Millennium Drop, too. I hope you've found some time to practice, because Yell's giving it her all."

red @happy "Hey, perfection--"

yellow @talking2mouth "--can only be sought, never attained, I know."

yellow -closedeyes -angryeyebrows @sadbrow talkingmouth "I just[ellipses] {i}really{/i} want to make sure we're seeking as much as we can."

red @talkingmouth "Well, we've got one more day, right?"

yellow @talking2mouth "I'm just not sure we'll have enough time[ellipses]"

blue @glanceeyes "[ellipses]"
blue @talkingmouth "You two are in Cherry's class, right?"

yellow @talking2mouth surprisedbrow "Y-yes. Um[ellipses] why?"

blue @talking2mouth "I think I can get us some more time."

ethan @talkingmouth "Huh? You got some kind of plan?"

blue @talking2mouth "Of course I do. What, you thought Leaf was the only one in this dorm who can plan? I'll get us more time, believe me."

ethan @happy "Cool. Maybe we won't need it, though. How have you been doing, [first_name]? Recruit any more people?"

call BunnyRecruitRecap() from _call_BunnyRecruitRecap_3

yellow @talking2mouth "Okay. I think however much extra time you can get us will be useful, Blue."

blue @happy "Like I said!"
blue "But don't worry about it. I'm going to get us so much extra time, [first_name]'s not going to have any idea what to do but sit with his thumb up his--"

red @upeyes talkingmouth "Oh my god, can you brag like a {i}normal{/i} person? Without putting someone down?"

blue @closedbrow talking2mouth "Whatever. You'll be thanking me when you see what I do for this party."
blue @talkingmouth "Speaking of which--I gotta go back into the kitchen. Yellow, how's that suit you were working on?"

yellow @surprisedbrow talking2mouth "Oh, the one this morning? I, um, finished that. I'm working on a new one now."

blue @closedbrow "Seriously? Damn, we're good. We're going to throw such a badass party no-one will ever go to anyone else's."

hide blue with dis

pause 1.0

ethan @talkingmouth "I mean, he still put someone else down, but at least he said 'we' this time."

red @closedbrow talking2mouth "Small miracles, yeah. There're worse things for him to be Type A about."

call texting() from _call_texting_35

jump day010611