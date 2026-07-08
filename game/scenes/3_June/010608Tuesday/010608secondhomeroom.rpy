label secondhomeroom010608:

scene blank2

play music "Audio/Music/Oak Intro.ogg" noloop
queue music "Audio/Music/Oak Class.ogg"

show homeroom behind blank2
    
$ renpy.transition(dissolve)
show screen currentdate

show oak 
hide blank2 
with splitfade

oak @talkingmouth "...which resulted in, {i}finally{/i}, the {i}formal{/i} reclassification of Magnemite and Magneton to both the Electric and Steel types."
oak @closedbrow talking2mouth "Just think, if those Kantonian researchers hadn't collaborated with their Sinnohan colleagues, we might still have trainers expecting their Magneton's decent defenses to save them from an Earthquake!"
oak @closedbrow talkingmouth "It is not often that our understanding of science is turned on its head. But whenever it is, it's invariably the result of further research into the fantastic creatures we call Pokémon."

$ PlaySound("bellchime.ogg")

queue music "Audio/school_crowd.ogg" channel "crowd" fadein 1.5

oak @happy "Lovely, seems I finished right on time!"
oak @closedbrow talkingmouth "{size=30}Perhaps I'm getting the hang of this, after all.{/size}"

redmind uniform @sadbrow "[ellipses]"

oak @talkingmouth "You go off, now. Remember, coordinators, that the Millennium Drop is on Sunday. Everyone else, there will {i}not{/i} be a quiz on Thursday--so I will be delivering a special lecture during that time."

hide oak with dis

pause 1.5

label homeroom010608bunnyrecruit:

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
            call BunnyRecruit(classchar, True) from _call_BunnyRecruit_8

        "No.":
            $ renpy.hide(classchar.lower())

            jump homeroom010608bunnyrecruit

scene blank2 with splitfade

pause 1.0

narrator "You remember Brendan's invitation, yesterday[ellipses] if you want to attend a Coordinator Club meeting, [bluecolor]you should go to the Battle Hall,{/color} then head West."

$ removestudents = { "May", "Brendan", "Klara", "Jasmine", "Yellow", "Misty", "Serena", "Dawn", "Tia"} | ({"Calem", "Grusha", "Gardenia" } if not (HasEvent("Game", "Contest1") or HasEvent("Klara", "AcceptCoordinatorClub")) else set())

call freeroam() from _call_freeroam_46

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

blue @talking2mouth "You're back. I've got a ham in the oven, so let's make this quick."

red @confused "A ham? Aren't you jumping the gun a bit? Party's not 'til Saturday."

blue @closedbrow "It's a {i}practice{/i} ham. Unlike {i}some{/i} people, I don't expect to just be amazing at whatever I do the first time I do it."
blue @angrybrow happymouth "You should see how good I've gotten just from one day of practice! And I haven't slipped on my studies, either!"

ethan @talkingmouth "It's true. Dude's been mixing a glaze with one hand and taking notes on the readings with his other. Kinda scary how intense he got."

yellow @closedbrow talkingmouth "Blue's incredibly focused. No matter what he puts his mind to, he puts everything he has into it. It's admirable."

blue @closedbrow talking2mouth "Yeah, I know. Whether it's battles or baking, I'm a badass."

red @talking2mouth "Pat yourself on the back a bit harder. As long as it {i}looks{/i} good--"

blue @angry "I told you it'll look edible! Will you get off my ass about that?!"

pause 1.0

redmind @thinking "Maybe now isn't the time to point out we're trying to aim for higher than 'edible.'"

blue @talking2mouth "Anyway, I've been busting my ass in the kitchen for the past forty-eight hours, so I better not hear that you guys have been slacking."
blue @surprised "You at least talked to {i}someone{/i}, right, [first_name]?"

call BunnyRecruitRecap() from _call_BunnyRecruitRecap_1

yellow @talking2mouth "[ellipses]Not bad. We've still got three days until Saturday. We should probably be able to contact everyone we want to, if [first_name] keeps up his pace."

red @closedbrow sweat talking2mouth "Pretty sure I can. Biggest thing I'm worried about is just running out of people I can talk to about this, honestly. There are some classmates I only see in my elective classes every once in a while."
red @talkingmouth "Like, I know I'll get around to everyone in homeroom, but for students outside of that[ellipses] I kinda have to go out of my way, you know?"

ethan @talking2mouth "Hey, don't forget we've got the Battle Team meeting Friday. You can ask someone about the party, then, if you want to ask[ellipses] I dunno. Blue? Me? Loa[ellipses]"

show blue frownmouth 
show yellow frownmouth
with dis

ethan frownmouth @closedbrow talking2mouth "Shit. Leaf. She probably won't be there, will she?"

narrator "The four of you take a quick glance at her door, imagining the empty room behind it."

red @sadbrow talkingmouth "She {i}really{/i} likes battles. Maybe that'll lure her back to campus?"

ethan @sadbrow talkingmouth "Or maybe she'll feel too crap to leave the hotel, and Janine'll kick her from the team for not showing up."

red @sad2eyes angryeyebrows frownmouth "[ellipses]"
red @talking2mouth "I guess, yeah, maybe that'll happen. But we can try to explain what happened, and maybe Janine'll give Leaf a break."

ethan @sadbrow talkingmouth "Don't wanna be a debbie downer, dude, but when has Janine given {i}anyone{/i} a break? She breaks people, she doesn't give them breaks."

if (GetRelationshipRank("Janine") > 1):
    red @sad2brow talkingmouth "You know, she's not as scary as she seems. She likes Ariados-Man."

    ethan @closedbrow talking2mouth "Well, you can be the one to try and beg for mercy on Leaf's behalf, then."

yellow @talking2mouth "I don't think worrying about what {i}might{/i} happen on Friday is very productive right now. A lot can change in seventy-two hours."

show ethan -frownmouth 
show blue -frownmouth
show yellow -frownmouth
with dis

yellow @talkingmouth "We should focus on what we {i}can{/i} change--tomorrow."
yellow @happy "And we can change it for the better. Don't be disheartened, okay? We're doing this to make Leaf feel better--there's no point in having a feel-good party if we feel bad while making it."

pause 1.0

blue scaredbrow frownmouth @talkingmouth closedbrow "Yeah. You're right. See, why can't you two just--"

show ethan happy
show yellow happybrow
with dis

red @confused "Hey, didn't you have a ham?"

show suitenight with vpunch

blue @scaredmouth "{size=40}My {i}ham!{/i}{/size}"

show blue:
    xpos 0.25 xzoom 1
    ease 0.3 xzoom -1
    pause 0.2
    ease 0.2 xpos -0.25

pause 1.5

scene blank2 with splitfadefast

call texting() from _call_texting_33

jump day010609