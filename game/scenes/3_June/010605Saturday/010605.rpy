label day010605:

$ timeOfDay = "Morning"
call clearscreens() from _call_clearscreens_265
call calendar(1) from _call_calendar_61

$ calDate = calDate.replace(day=5, month=6, year=2004)

$ HealParty()

stop music fadeout 1.5
show screen songsplash("Pallet Town", "Zame")
queue music "audio/music/palletpiano.ogg"

scene suite
show yellow:
    xpos 0.75
show blue:
    xpos 0.25
show ethan:
    xpos 0.5
with splitfade

narrator "When you leave your bedroom after waking up, you walk into the common room and are surprised to see Ethan, Yellow, and Blue all huddled around a laptop."

red @confused "Uh, hey, guys. Good morning. What are you doing?"

ethan @talking2mouth "Looking up contest outfits for Yellow."

red @happy "Oh, I getcha. Maybe finding something online will be less, uh, intimidating than looking in the mall?"

ethan @talkingmouth "That's the hope!"

blue @surprisedbrow talking2mouth "It's so much cheaper online than at the mall, and if we order, it'll get here in, like, a day, anyway. Why does anyone even {i}go{/i} to the mall?"

ethan @talking2mouth closedbrow "Apparently, the female of the species finds it fun. Baffling, I know."

blue surprisedbrow frownmouth @closedbrow talking2mouth "Pfft. If they--"

yellow @closedbrow talking2mouth "Blue, I really don't appreciate whatever you're about to say."

blue @surprised "How do you know what I was about to say? Maybe it was something complimentary."

pause 1.0

show yellow unamusedbrow unamusedmouth with dis

ethan @sad2eyes playfuleyebrows unamusedmouth "[ellipses]"

show yellow -unamusedbrow -unamusedmouth with dis

ethan @closedbrow talking2mouth "[first_name], we're probably going to be here a while. Need us for anything?"

red @happy "Nah, should be a pretty low-key day. Did Leaf already leave for her party?"

yellow @talking2mouth "She has a party? She didn't tell us."

ethan @talking2mouth "It's always parties with that girl. God knows when she studies. Anyway, no, she's--"

show leaf hatless angrybrow angrysmilemouth:
    xpos -0.2 xzoom -1
    ease 0.5 xpos 0.2
show yellow:
    xpos 0.75
    ease 0.5 xpos 0.8
show blue:
    xpos 0.25
    ease 0.5 xpos 0.4
show ethan:
    xpos 0.5
    ease 0.5 xpos 0.6

leaf @talking2mouth "--Right here, and she's doing {i}fine{/i}, academically, thank you very much!"

ethan @talking2mouth "Whatever. You dropped out of Dragon Class, that's all I know."

leaf @angrymouth "C'mon, Ethan! It was {i}Dragon{/i} class! Dropping out is practically expected!"

if (not HasEvent("Instructor Clair", 2.1)):
    ethan @closedbrow talking2mouth "Blue didn't."

    leaf @closedbrow talking2mouth "Well, that's--that's different. Right, [first_name]?"

else:
    ethan @talking2mouth "Blue didn't. [first_name], what about you? We've taken a couple Dragon classes together. Would you say {i}we've{/i} 'dropped out'?"

red @sweat sadbrow talking2mouth "I'm not getting involved here."

leaf @talking2mouth "You know, one of these days, we're really going to have to battle it out, Ethan. I think you've gotten a {i}bit{/i} too comfortable digging at me."

ethan @talking2mouth "You know what, sure. Soon as we find something for Yellow to wear, or give up on it? Battle Hall should be good."

leaf -angrybrow -angrysmilemouth @happy "Sure! That'd be fun."

if (GetRelationshipRank("Ethan") > 0):
    leaf @talkingmouth "You've got a new Quilava, right? I've wanted to battle against it for a while."

ethan @confused "Uh, did you forget that this was meant to be an 'airing of grievances' kind of thing?"

leaf @flirtbrow talkingmouth "No. It can be that {i}and{/i} fun."

ethan @talkingmouth "Alright."

show leaf surprisedbrow frownmouth with dis

yellow @sadbrow talkingmouth "I hate to ruin this moment of connection--it's really great, and I'm proud of you guys--but didn't you have a party, Leaf?"

show leaf sadbrow -frownmouth with dis

leaf @talkingmouth "Yessss... but battling Ethan would give me an excuse to 'forget' it."

red @happy "Aw, c'mon. Is this just 'cause you're nervous about it?"

leaf @talkingmouth "Yeah, entirely."

if (HasEvent("Klara", "BrokeBond")):
    red @talkingmouth "Well, that's no reason to ditch a commitment. I mean, c'mon, you already said you'd go--and besides, you're on a mission, right? You gotta find out what's up with Klara."

else:
    red @talkingmouth "Well, that's no reason to ditch a commitment. I mean, c'mon, you already said you'd go--and besides, you know you'll have fun once you're there."

leaf @sadbrow talkingmouth "Right as always. Okay, I'm--I'm going back in my room. And I'm going to get ready. And I'm going to have fun!"

blue @closedbrow talking2mouth "Stop telling us about it and just {i}do{/i} it, then."

leaf @angrybrow frownmouth "[ellipses]"

show leaf with dis:
    xzoom -1 xpos 0.2
    ease 0.5 xzoom 1

leaf @talking2mouth "{size=30}Blue has {i}no{/i} respect for my character development.{/size}"

red @talking2mouth "{size=30}The only kind of 'developing' he's interested in is his Pokémon's strength.{/size}"
red @confused "{size=30}And urban development, actually, but that doesn't come up very often.{/size}"

leaf @sarcastic "{size=30}A regular bottomless pit of surprises and hidden depths, that boy.{/size}"
leaf @winkbrow talkingmouth "Alright, seeya. Probably tonight. Late, if I'm lucky."

red @happy "Don't do anything I wouldn't do!"
red @closedbrow sweat talking2mouth "Also, don't do several things I {i}would{/i} do."

leaf @closedbrow talkingmouth "I'll use my best judgment."

show leaf:
    xpos 0.2
    ease 0.2 xpos -0.2

pause 1.5

ethan @talking2mouth "Alright, so back to this. I think a nice cobalt blue might work well here?"

blue @surprised "You crazy? Her color's obviously green."

yellow @talking2mouth "Well, that {i}is{/i} my favorite, but for a dress, maybe..."

redmind @sadbrow "...They seem pretty into it. It's nice to see them getting along."

$ removestudents = { "Leaf", "Klara", "Blue", "Ethan", "Klara", "Yellow", "Brendan", "Misty", "Nessa"}

call freeroam() from _call_freeroam_42

$ removestudents = set()

call texting() from _call_texting_31

jump day010606

label klarapartyscene1:
    stop music fadeout 1.5

    scene blank2 with splitfade

    python:  
        oldinventory = copy.copy(inventory)
        oldpersonalstats = copy.copy(personalstats)
        oldparty = copy.copy(playerparty)
        oldpersondex = copy.copy(persondex)
        oldclassstats = copy.copy(classstats)
        playercharacter = "Leaf"
        playerparty = GetTrainerTeam("Leaf")

        inventory = {
            Item.PokeBall : 12,
            Item.GreatBall : 5,
            Item.Potion : 4,
            Item.ParalyzeHeal : 2,
            Item.BurnHeal : 7,
            Item.DragonFang : 1,
            Item.MiracleSeed : 1,
            Item.Magnet : 1,
            Item.Diary : 1,
            Item.Towel : 1,
            Item.RootFossil : 1,
            Item.AirHorn : 1,
            Item.ExperienceShare : 1
        }

        personalstats = {
            "Charm" : 43,
            "Knowledge" : 8,
            "Courage" : 4,
            "Wit" : 24,
            "Patience" : -3
        }

        persondex = copy.deepcopy(defaultpersondex)
        persondex["Rosa"] = {"Named" : True, "Value" : 10427, "Contact": True, "Sex": Genders.Female, "Relationship": "Idolater", "RelationshipRank": 0, "Events": [] }
        persondex[first_name] = {"Named" : True, "Value" : oldpersondex["Leaf"]["Value"] * 3, "Contact": True, "Sex": Genders.Male, "Relationship": ("Pursuer" if HasEvent("Leaf", "RejectedConfession") else "Date"), "RelationshipRank": 0, "Events": [] }
        persondex["Leaf"] = {"Named" : True, "Value" : 0, "Contact": True, "Sex": Genders.Female, "Relationship": "Self", "RelationshipRank": 0, "Events": [] }
        persondex["Blue"] = {"Named" : True, "Value" : 98, "Contact": True, "Sex": Genders.Male, "Relationship": "Rival", "RelationshipRank": 0, "Events": [] }
        persondex["Professor Cherry"] = {"Named" : True, "Value" : 24, "Contact": True, "Sex": Genders.Female, "Relationship": "Student", "RelationshipRank": 0, "Events": [] }
        persondex["May"] = {"Named" : True, "Value" : 32, "Contact": True, "Sex": Genders.Female, "Relationship": "Former Dormmate", "RelationshipRank": 0, "Events": [] }
        persondex["Bianca"] = {"Named" : True, "Value" : 45, "Contact": True, "Sex": Genders.Female, "Relationship": "Former Dormmate", "RelationshipRank": 0, "Events": [] }
        persondex["Hilda"] = {"Named" : True, "Value" : 29, "Contact": True, "Sex": Genders.Female, "Relationship": "Former Dormmate", "RelationshipRank": 0, "Events": [] }
        persondex["Serena"] = {"Named" : True, "Value" : 32, "Contact": True, "Sex": Genders.Female, "Relationship": "Former Dormmate", "RelationshipRank": 0, "Events": [] }
        persondex["Ethan"] = {"Named" : True, "Value" : 3, "Contact": True, "Sex": Genders.Male, "Relationship": "Dormmate", "RelationshipRank": 0, "Events": [] }
        persondex["Brendan"] = {"Named" : True, "Value" : 18, "Contact": True, "Sex": Genders.Male, "Relationship": "Friend", "RelationshipRank": 0, "Events": [] }
        persondex["Cheren"] = {"Named" : True, "Value" : 7, "Contact": True, "Sex": Genders.Male, "Relationship": "Ugh.", "RelationshipRank": 0, "Events": [] }
        persondex["Hilbert"] = {"Named" : True, "Value" : 13, "Contact": True, "Sex": Genders.Male, "Relationship": "Teammate", "RelationshipRank": 0, "Events": [] }
        persondex["Calem"] = {"Named" : True, "Value" : 16, "Contact": True, "Sex": Genders.Male, "Relationship": "Friend", "RelationshipRank": 0, "Events": [] }
        persondex["Gardenia"] = {"Named" : True, "Value" : 35, "Contact": True, "Sex": Genders.Female, "Relationship": "Classmate", "RelationshipRank": 0, "Events": [] }
        persondex["Whitney"] = {"Named" : True, "Value" : 47, "Contact": True, "Sex": Genders.Female, "Relationship": "Classmate", "RelationshipRank": 0, "Events": [] }
        persondex["Flannery"] = {"Named" : True, "Value" : 22, "Contact": True, "Sex": Genders.Female, "Relationship": "Friend", "RelationshipRank": 0, "Events": [] }
        persondex["Nate"] = {"Named" : True, "Value" : 11, "Contact": True, "Sex": Genders.Male, "Relationship": "Suspicious", "RelationshipRank": 0, "Events": [] }
        persondex["Sonia"] = {"Named" : True, "Value" : 28, "Contact": True, "Sex": Genders.Female, "Relationship": "Underclassman", "RelationshipRank": 0, "Events": [] }
        persondex["Silver"] = {"Named" : True, "Value" : 17, "Contact": True, "Sex": Genders.Male, "Relationship": "Teammate", "RelationshipRank": 0, "Events": [] }
        persondex["Bea"] = {"Named" : True, "Value" : 43, "Contact": True, "Sex": Genders.Female, "Relationship": "Teammate", "RelationshipRank": 0, "Events": [] }
        persondex["Erika"] = {"Named" : True, "Value" : 30, "Contact": True, "Sex": Genders.Female, "Relationship": "Teammate", "RelationshipRank": 0, "Events": [] }
        persondex["Janine"] = {"Named" : True, "Value" : 56, "Contact": True, "Sex": Genders.Female, "Relationship": "Mentee", "RelationshipRank": 0, "Events": [] }
        persondex["Dawn"] = {"Named" : True, "Value" : 67, "Contact": True, "Sex": Genders.Female, "Relationship": "Friend", "RelationshipRank": 0, "Events": [] }
        persondex["Tia"] = {"Named" : True, "Value" : 78, "Contact": True, "Sex": Genders.Female, "Relationship": "Secret-Keeper", "RelationshipRank": 0, "Events": [] }
        persondex["Yellow"] = {"Named" : True, "Value" : 5, "Contact": True, "Sex": Genders.Female, "Relationship": "Friend", "RelationshipRank": 0, "Events": [] }
        persondex["Klara"] = {"Named" : True, "Value" : 212, "Contact": True, "Sex": Genders.Female, "Relationship": "Bestie{size=10}?{/size}", "RelationshipRank": 0, "Events": [] }

        classstats = { 
            "Normal" : AimLevel() + 2,
            "Fire" : 1,
            "Water" : 0,
            "Grass" : AimLevel() + 4,
            "Electric" : AimLevel() + 3,
            "Ice" : 1,
            "Fighting" : 1,
            "Poison" : 1,
            "Ground" : 1,
            "Flying" : 1,
            "Psychic" : 1,
            "Bug" : 1,
            "Rock" : 1,
            "Ghost" : 1,
            "Dark" : 1,
            "Dragon" : 23,
            "Steel" : 1,
            "Fairy" : 1
        }

        renpy.music.queue("Audio/Music/Cinnabar_Start.ogg", channel='music', loop=None, fadein=0.0, tight=None)
        renpy.music.queue("Audio/Music/Cinnabar_Loop.ogg", channel='music', loop=True, tight=None)

    narrator "Meanwhile..."
    narrator "[leafcolor]You are no longer you.{/color}"

    scene leafbedroom 
    show screen currentdate
    with splitfade

    leafmind hatless @closedbrow frownmouth "Okay. Okay, okay. I'm going to do this."
    leafmind @sadbrow "I mean, Klara's done so much for me, right? I need to pay her back. The {i}least{/i} I can do is go to her party."

    if (HasEvent("Klara", "BrokeBond")):
        leafmind @angrybrow frownmouth "Besides... no matter what she's done for me, if she actually {i}did{/i} blackmail [first_name], she needs a stern talking-to."

        pause 1.0

        leaf @flirtbrow frownmouth "[ellipses]"

        leafmind @closedbrow frownmouth "Okay, I don't know what I'll do if it turns out she actually {i}was{/i} a jerk. Battle her, I guess. But at least I can tell [first_name], and everything will be out in the open."

    pause 1.0

    $ PlaySound("vibrate.ogg")

    pause 1.0

    leafmind @surprisedbrow "Hm? A text?" 

    show phone_B
    show phone_A
    with fadeinbottom

    show phone_C behind phone_A with dis

    show phone_msg1 behind phone_A with dis
        
    $ title = Text("Klara galarpinkhair",size=30,font="fonts/consola_0.ttf",color="#313131")

    image msg7 = Text("Bestiiiiie!\nWhere r u, girl?\nBunny suit debut?\nParty starts on 12!",size=21,color="#ffffff",line_spacing=5,text_align=0.0)

    show text title behind phone_A:
        xalign 0.51 yalign 0.34
    show msg7 behind phone_A:
        xpos .41 ypos .4
    with dis

    pause

    hide phone_B 
    hide phone_A
    hide phone_C
    hide phone_msg1
    hide text title
    hide msg7
    with fadeoutbottom 

    leafmind @surprisedbrow frownmouth "Oh, that's right! I need to get going."
    leafmind @sadbrow blush "Alright, I'll throw my costume in my bag... grab my hat..."
    leafmind -hatless @happybrow "Okay! Finally, time to go to a party I didn't plan! A {i}real{/i} party, with hot girls and expensive snacks, and--and--"
    if (HasEvent("Klara", "BrokeBond")):
        leafmind @sadbrow "Maybe a blackmailer?"
    else:
        leafmind @sadbrow "I'm not sure what else is at college parties. Beer, maybe?"
    leafmind @happybrow "Well, I'll know when I get there."
    leafmind @closedbrow frownmouth "Let's see... the sorority's dorm block is in Pledge Hall, right? I think Klara said we'd meet in front of Relic, since it's midway between us."
    leafmind @angrybrow "Okay. Here I go. I am carpe-ing this goddamn diem."

    scene blank2 with splitfade

    pause 1.0

    scene relichall_a with splitfade

    leaf @happy "Oh, there's Klara, I--"
    leaf @surprisedbrow frownmouth "[ellipses]"

    show klara bunny makeup with Dissolve(2.0)

    klara @happy "Bestie, hi!"

    leaf @surprisedbrow blush talking2mouth "H-hi."

    klara surprisedbrow frownmouth @surprisedbrow talking2mouth "Huh, wait..."
    klara @sadbrow talkingmouth "Oh, I'm sorry. You're not wearing a costume? I guess you couldn't find one that fit?"

    leaf @surprisedbrow talking2mouth "N-no! No, I found one! And it fits--I mean, I think."

    if (HasEvent("Leaf", "SawBunny")):
        leaf @sadbrow talkingmouth "I-if it doesn't, then, um, [first_name] didn't tell me, but I think it does."
    else:
        leaf @sadbrow talkingmouth "The person I was going to ask about it kinda, um, turned me down, but I'm pretty sure it does!"

    klara sadbrow @talkingmouth "Oh. So, why...? Are you not confident in your body? Because I can understand that, really."

    leaf @sadbrow talkingmouth "No, no, it's not that. I'm sorry, I... I thought I would change there. I just didn't think, I guess?"

    klara @happy "Great, I was really worried. Well, you should go put it on! You'll never feel comfortable walking across campus in your bunny suit without practicing first."

    leaf @surprisedbrow talking2mouth "Wait, walking across--why do I need to do that? Can't I just change there?"

    klara @happy "Imagine if you walked into the party in your full clothes, and you opened the door and everyone else was in their costumes? That'd be really embarrassing, right?"

    leaf @sadbrow talkingmouth "...Really, yeah."

    klara -sadbrow @happy "Well, that's why I'm here, to look out for you!"
    klara @talkingmouth "But... I kinda don't want to stay out here any longer than I have to. I mean, the idea of debuting the suits to each other before the party was {i}fun{/i}, but[ellipses] I'm not sure it's worth it!" 
    klara -frownmouth @sadbrow talkingmouth "I mean, it's one thing to come out in your bunny suit to show off to your bestie, but I don't {i}really{/i} want to just stand around here while I wait for you to run back to your dorm to change. Can you hurry?"

    leaf @sadbrow talkingmouth "Oh--no, no, you don't have to do that!"
    leaf @happy "Sorry, I really should've thought about this before. You can, um, you can just see my costume when the party starts, since it's so soon, right?"
    leaf @sadbrow talkingmouth "You go ahead. Where's the room block?"

    klara @talkingmouth "We're meeting in Aura Hall, room 303. We'll probably spread out to other rooms as the night goes on, but, we'll keep it small to start off."
    klara @winkbrow talkingmouth "Best way to keep the party going {i}all{/i} night. If you want to do some {i}real{/i} damage, you have to be subtle. Cheren never figured that out."

    leaf @talkingmouth "Right, you don't want the disciplinary committee busting in and ruining our good time."

    klara @happy "So true, bestie."

    leaf @talking2mouth "Okay, I'll just find a bathroom or something somewhere in Relic Hall, and get changed then."

    klara @happy "And put your makeup on, right?"

    pause 1.0

    show klara surprisedbrow frownmouth with dis

    leaf @talking2mouth "I[ellipses] I have some on."

    klara @talking2mouth "Oh."

    pause 1.0

    klara -surprisedbrow -frownmouth @happy "Well, it wouldn't hurt to put on a {i}little{/i} more, sweetheart."

    leaf @talkingmouth sadbrow "O-okay. Okay. Sure! I'll need to run back to my dorm to grab mine, but..."

    klara @talkingmouth "Oh, don't worry about that. I've actually got some with me."

    narrator "Klara takes a quick look around and reaches into her corset. [ellipses]Her hand keeps going.{w=0.5} And going.{w=0.5} And going."

    leafmind @surprisedbrow frownmouth "Holy shit, how much space does she {i}have{/i} in there?!"

    narrator "Finally, she pulls out a little black tube of makeup, adorned with a foppish silhouette outlined in gold. It looks vaguely familiar[ellipses]"

    show klara:
        ypos 1.0 zoom 1.0
        ease 0.5 ypos 1.2 zoom 1.3

    klara @talkingmouth "Here, bestie. The top is eyeshadow, the bottom is lipstick."

    show klara:
        ypos 1.2 zoom 1.3
        ease 0.5 ypos 1.0 zoom 1.0

    leaf @sadbrow talkingmouth "Thanks. Sorry I've been dropping the ball so much."

    klara @happy "It's alright. I'm just glad you can come to the party!"

    leaf @sadbrow talkingmouth "Thanks! See you in a bit."

    scene blank2 with splitfade

    pause 1.0

    narrator "Meanwhile..."

    python:
        playerparty = oldparty
        playercharacter = None
        inventory = oldinventory
        personalstats = oldpersonalstats
        persondex = oldpersondex
        classstats = oldclassstats

    return

label klarapartyscene2:
    stop music fadeout 1.5

    scene blank2 with splitfade

    python:  
        oldinventory = copy.copy(inventory)
        oldpersonalstats = copy.copy(personalstats)
        oldparty = copy.copy(playerparty)
        oldpersondex = copy.copy(persondex)
        oldclassstats = copy.copy(classstats)
        playercharacter = "Leaf"
        playerparty = GetTrainerTeam("Leaf")

        inventory = {
            Item.PokeBall : 12,
            Item.GreatBall : 5,
            Item.Potion : 4,
            Item.ParalyzeHeal : 2,
            Item.BurnHeal : 7,
            Item.DragonFang : 1,
            Item.MiracleSeed : 1,
            Item.Magnet : 1,
            Item.Diary : 1,
            Item.Towel : 1,
            Item.RootFossil : 1,
            Item.AirHorn : 1,
            Item.ExperienceShare : 1
        }

        personalstats = {
            "Charm" : 43,
            "Knowledge" : 8,
            "Courage" : 4,
            "Wit" : 24,
            "Patience" : -3
        }

        persondex = copy.deepcopy(defaultpersondex)
        persondex["Rosa"] = {"Named" : True, "Value" : 10427, "Contact": True, "Sex": Genders.Female, "Relationship": "Idolater", "RelationshipRank": 0, "Events": [] }
        persondex[first_name] = {"Named" : True, "Value" : oldpersondex["Leaf"]["Value"] * 3, "Contact": True, "Sex": Genders.Male, "Relationship": ("Pursuer" if HasEvent("Leaf", "RejectedConfession") else "Date"), "RelationshipRank": 0, "Events": [] }
        persondex["Leaf"] = {"Named" : True, "Value" : 0, "Contact": True, "Sex": Genders.Female, "Relationship": "Self", "RelationshipRank": 0, "Events": [] }
        persondex["Blue"] = {"Named" : True, "Value" : 98, "Contact": True, "Sex": Genders.Male, "Relationship": "Rival", "RelationshipRank": 0, "Events": [] }
        persondex["Professor Cherry"] = {"Named" : True, "Value" : 24, "Contact": True, "Sex": Genders.Female, "Relationship": "Student", "RelationshipRank": 0, "Events": [] }
        persondex["May"] = {"Named" : True, "Value" : 32, "Contact": True, "Sex": Genders.Female, "Relationship": "Former Dormmate", "RelationshipRank": 0, "Events": [] }
        persondex["Bianca"] = {"Named" : True, "Value" : 45, "Contact": True, "Sex": Genders.Female, "Relationship": "Former Dormmate", "RelationshipRank": 0, "Events": [] }
        persondex["Hilda"] = {"Named" : True, "Value" : 29, "Contact": True, "Sex": Genders.Female, "Relationship": "Former Dormmate", "RelationshipRank": 0, "Events": [] }
        persondex["Serena"] = {"Named" : True, "Value" : 32, "Contact": True, "Sex": Genders.Female, "Relationship": "Former Dormmate", "RelationshipRank": 0, "Events": [] }
        persondex["Ethan"] = {"Named" : True, "Value" : 3, "Contact": True, "Sex": Genders.Male, "Relationship": "Dormmate", "RelationshipRank": 0, "Events": [] }
        persondex["Brendan"] = {"Named" : True, "Value" : 18, "Contact": True, "Sex": Genders.Male, "Relationship": "Friend", "RelationshipRank": 0, "Events": [] }
        persondex["Cheren"] = {"Named" : True, "Value" : 7, "Contact": True, "Sex": Genders.Male, "Relationship": "Ugh.", "RelationshipRank": 0, "Events": [] }
        persondex["Hilbert"] = {"Named" : True, "Value" : 13, "Contact": True, "Sex": Genders.Male, "Relationship": "Teammate", "RelationshipRank": 0, "Events": [] }
        persondex["Calem"] = {"Named" : True, "Value" : 16, "Contact": True, "Sex": Genders.Male, "Relationship": "Friend", "RelationshipRank": 0, "Events": [] }
        persondex["Gardenia"] = {"Named" : True, "Value" : 35, "Contact": True, "Sex": Genders.Female, "Relationship": "Classmate", "RelationshipRank": 0, "Events": [] }
        persondex["Whitney"] = {"Named" : True, "Value" : 47, "Contact": True, "Sex": Genders.Female, "Relationship": "Classmate", "RelationshipRank": 0, "Events": [] }
        persondex["Flannery"] = {"Named" : True, "Value" : 22, "Contact": True, "Sex": Genders.Female, "Relationship": "Friend", "RelationshipRank": 0, "Events": [] }
        persondex["Nate"] = {"Named" : True, "Value" : 11, "Contact": True, "Sex": Genders.Male, "Relationship": "Suspicious", "RelationshipRank": 0, "Events": [] }
        persondex["Sonia"] = {"Named" : True, "Value" : 28, "Contact": True, "Sex": Genders.Female, "Relationship": "Underclassman", "RelationshipRank": 0, "Events": [] }
        persondex["Silver"] = {"Named" : True, "Value" : 17, "Contact": True, "Sex": Genders.Male, "Relationship": "Teammate", "RelationshipRank": 0, "Events": [] }
        persondex["Bea"] = {"Named" : True, "Value" : 43, "Contact": True, "Sex": Genders.Female, "Relationship": "Teammate", "RelationshipRank": 0, "Events": [] }
        persondex["Erika"] = {"Named" : True, "Value" : 30, "Contact": True, "Sex": Genders.Female, "Relationship": "Teammate", "RelationshipRank": 0, "Events": [] }
        persondex["Janine"] = {"Named" : True, "Value" : 56, "Contact": True, "Sex": Genders.Female, "Relationship": "Mentee", "RelationshipRank": 0, "Events": [] }
        persondex["Dawn"] = {"Named" : True, "Value" : 67, "Contact": True, "Sex": Genders.Female, "Relationship": "Friend", "RelationshipRank": 0, "Events": [] }
        persondex["Tia"] = {"Named" : True, "Value" : 78, "Contact": True, "Sex": Genders.Female, "Relationship": "Secret-Keeper", "RelationshipRank": 0, "Events": [] }
        persondex["Yellow"] = {"Named" : True, "Value" : 5, "Contact": True, "Sex": Genders.Female, "Relationship": "Friend", "RelationshipRank": 0, "Events": [] }
        persondex["Klara"] = {"Named" : True, "Value" : 212, "Contact": True, "Sex": Genders.Female, "Relationship": "Bestie{size=10}?{/size}", "RelationshipRank": 0, "Events": [] }

        classstats = { 
            "Normal" : AimLevel() + 2,
            "Fire" : 1,
            "Water" : 0,
            "Grass" : AimLevel() + 4,
            "Electric" : AimLevel() + 3,
            "Ice" : 1,
            "Fighting" : 1,
            "Poison" : 1,
            "Ground" : 1,
            "Flying" : 1,
            "Psychic" : 1,
            "Bug" : 1,
            "Rock" : 1,
            "Ghost" : 1,
            "Dark" : 1,
            "Dragon" : 23,
            "Steel" : 1,
            "Fairy" : 1
        }

        renpy.music.queue("Audio/Music/Cinnabar_Start.ogg", channel='music', loop=None, fadein=0.0, tight=None)
        renpy.music.queue("Audio/Music/Cinnabar_Loop.ogg", channel='music', loop=True, tight=None)

    narrator "Meanwhile..."
    narrator "[leafcolor]You are no longer you.{/color}"

    scene blank2 with splitfade

    pause 2.0

    leaf bunny blush makeup @angrybrow angrysmilemouth "[ellipses]"
    leafmind @sadbrow bigblush "I'm so embarrassed."
    leafmind @closedbrow frownmouth "I thought this would be an empowering, fun, sexy, thing, but now I just want to throw on a blanket and lay on a couch for the next year."
    leafmind @frownmouth "I can't do this."

    show red hatless swimsuit noeyes shadow with dis:
        xpos 0.5

    red @happyeyebrows talkingmouth "'Course you can. You're Leaf Gracidea Green. You can fly across an ocean--you can attend a party."

    pause 2.0

    leaf @talking2mouth "Okay, sure, but why are you in your swimsuit, mind-[first_name]?"

    red @confusedeyebrows talking2mouth "Taking a dip in the mind-pool. Hey, why does your mind-palace have a mind-pool if you're scared of water?"

    leaf -blush @sadbrow talking2mouth "Have you seen the mind-price of mind-concrete nowadays? It would cost way too much to fill the mind-pool up."

    red @sadeyebrows sadmouth "Damn. The mind-market isn't doing too hot, huh?"

    leaf @closedbrow talkingmouth "It's in shambles, yeah."

    pause 1.0

    red @happyeyebrows talkingmouth "Alright, dork, get out there. Worst-case scenario, tell Klara you really appreciated the invite, but just aren't comfortable. Maybe you can come back, in, like, a bunny onesie or something."

    leaf @talkingmouth sadbrow "Thanks, mind-[first_name]."

    red @happyeyebrows happymouth "Any mind-time."

    show screen currentdate
    scene relichall_A 
    with splitfade

    leafmind bunny makeup @sadbrow "Alright, this isn't so bad. Saturday evening, probably everyone's already at parties, or still in Inspira. I'll just run to Pledge. Not a problem."

    scene blank2 with splitfadefaster

    narrator "You quickly dash between bushes and buildings, hiding from nonexistant eyes. The serpentine route you take somewhat delays your arrival at the dorm--but you eventually arrive in front of Dorm 303."

    scene door with splitfade

    leafmind bunny blush makeup "Okay. Moment of truth. Mind-[first_name] {b}and{/b} real [first_name] gave me a pep talk. Just because I haven't had two months to agonize over it doesn't mean this won't be fun."

    pause 0.5

    leafmind @closedbrow frownmouth "Wait. Do you knock on the door before a party you've been invited to? Probably not, right?"

    pause 1.0

    leafmind @angrybrow angrysmilemouth "I'm overthinking this. I'll just knock, and I'm sure that won't be the worst faux pas I'll commit this evening."

    $ PlaySound("Knock.ogg")

    narrator "*Knock*{w=0.5} *knock*{w=0.5} *knock*"

    $ hideside = True

    pause 1.0

    klara @happy "Come iiiiiiin!"

    pause 1.0

    show dooropen with dis 

    pause 2.0

    $ hideside = False

    call clearscreens() from _call_clearscreens_266
    scene blank 
    with splitfadeslow

    pause 1.0

    narrator "Meanwhile..."

    python:
        playerparty = oldparty
        playercharacter = None
        inventory = oldinventory
        personalstats = oldpersonalstats
        persondex = oldpersondex
        classstats = oldclassstats

    return

label klarapartyscene3:
    stop music fadeout 1.5

    scene blank2 with splitfade

    python:  
        oldinventory = copy.copy(inventory)
        oldpersonalstats = copy.copy(personalstats)
        oldparty = copy.copy(playerparty)
        oldpersondex = copy.copy(persondex)
        oldclassstats = copy.copy(classstats)
        playercharacter = "Leaf"
        playerparty = GetTrainerTeam("Leaf")

        inventory = {
            Item.PokeBall : 12,
            Item.GreatBall : 5,
            Item.Potion : 4,
            Item.ParalyzeHeal : 2,
            Item.BurnHeal : 7,
            Item.DragonFang : 1,
            Item.MiracleSeed : 1,
            Item.Magnet : 1,
            Item.Diary : 1,
            Item.Towel : 1,
            Item.RootFossil : 1,
            Item.AirHorn : 1,
            Item.ExperienceShare : 1
        }

        personalstats = {
            "Charm" : 43,
            "Knowledge" : 8,
            "Courage" : 4,
            "Wit" : 24,
            "Patience" : -3
        }

        persondex = copy.deepcopy(defaultpersondex)
        persondex["Rosa"] = {"Named" : True, "Value" : 10427, "Contact": True, "Sex": Genders.Female, "Relationship": "Idolater", "RelationshipRank": 0, "Events": [] }
        persondex[first_name] = {"Named" : True, "Value" : oldpersondex["Leaf"]["Value"] * 3, "Contact": True, "Sex": Genders.Male, "Relationship": ("Pursuer" if HasEvent("Leaf", "RejectedConfession") else "Date"), "RelationshipRank": 0, "Events": [] }
        persondex["Leaf"] = {"Named" : True, "Value" : 0, "Contact": True, "Sex": Genders.Female, "Relationship": "Self", "RelationshipRank": 0, "Events": [] }
        persondex["Blue"] = {"Named" : True, "Value" : 98, "Contact": True, "Sex": Genders.Male, "Relationship": "Rival", "RelationshipRank": 0, "Events": [] }
        persondex["Professor Cherry"] = {"Named" : True, "Value" : 24, "Contact": True, "Sex": Genders.Female, "Relationship": "Student", "RelationshipRank": 0, "Events": [] }
        persondex["May"] = {"Named" : True, "Value" : 32, "Contact": True, "Sex": Genders.Female, "Relationship": "Former Dormmate", "RelationshipRank": 0, "Events": [] }
        persondex["Bianca"] = {"Named" : True, "Value" : 45, "Contact": True, "Sex": Genders.Female, "Relationship": "Former Dormmate", "RelationshipRank": 0, "Events": [] }
        persondex["Hilda"] = {"Named" : True, "Value" : 29, "Contact": True, "Sex": Genders.Female, "Relationship": "Former Dormmate", "RelationshipRank": 0, "Events": [] }
        persondex["Serena"] = {"Named" : True, "Value" : 32, "Contact": True, "Sex": Genders.Female, "Relationship": "Former Dormmate", "RelationshipRank": 0, "Events": [] }
        persondex["Ethan"] = {"Named" : True, "Value" : 3, "Contact": True, "Sex": Genders.Male, "Relationship": "Dormmate", "RelationshipRank": 0, "Events": [] }
        persondex["Brendan"] = {"Named" : True, "Value" : 18, "Contact": True, "Sex": Genders.Male, "Relationship": "Friend", "RelationshipRank": 0, "Events": [] }
        persondex["Cheren"] = {"Named" : True, "Value" : 7, "Contact": True, "Sex": Genders.Male, "Relationship": "Ugh.", "RelationshipRank": 0, "Events": [] }
        persondex["Hilbert"] = {"Named" : True, "Value" : 13, "Contact": True, "Sex": Genders.Male, "Relationship": "Teammate", "RelationshipRank": 0, "Events": [] }
        persondex["Calem"] = {"Named" : True, "Value" : 16, "Contact": True, "Sex": Genders.Male, "Relationship": "Friend", "RelationshipRank": 0, "Events": [] }
        persondex["Gardenia"] = {"Named" : True, "Value" : 35, "Contact": True, "Sex": Genders.Female, "Relationship": "Classmate", "RelationshipRank": 0, "Events": [] }
        persondex["Whitney"] = {"Named" : True, "Value" : 47, "Contact": True, "Sex": Genders.Female, "Relationship": "Classmate", "RelationshipRank": 0, "Events": [] }
        persondex["Flannery"] = {"Named" : True, "Value" : 22, "Contact": True, "Sex": Genders.Female, "Relationship": "Friend", "RelationshipRank": 0, "Events": [] }
        persondex["Nate"] = {"Named" : True, "Value" : 11, "Contact": True, "Sex": Genders.Male, "Relationship": "Suspicious", "RelationshipRank": 0, "Events": [] }
        persondex["Sonia"] = {"Named" : True, "Value" : 28, "Contact": True, "Sex": Genders.Female, "Relationship": "Underclassman", "RelationshipRank": 0, "Events": [] }
        persondex["Silver"] = {"Named" : True, "Value" : 17, "Contact": True, "Sex": Genders.Male, "Relationship": "Teammate", "RelationshipRank": 0, "Events": [] }
        persondex["Bea"] = {"Named" : True, "Value" : 43, "Contact": True, "Sex": Genders.Female, "Relationship": "Teammate", "RelationshipRank": 0, "Events": [] }
        persondex["Erika"] = {"Named" : True, "Value" : 30, "Contact": True, "Sex": Genders.Female, "Relationship": "Teammate", "RelationshipRank": 0, "Events": [] }
        persondex["Janine"] = {"Named" : True, "Value" : 56, "Contact": True, "Sex": Genders.Female, "Relationship": "Mentee", "RelationshipRank": 0, "Events": [] }
        persondex["Dawn"] = {"Named" : True, "Value" : 67, "Contact": True, "Sex": Genders.Female, "Relationship": "Friend", "RelationshipRank": 0, "Events": [] }
        persondex["Tia"] = {"Named" : True, "Value" : 78, "Contact": True, "Sex": Genders.Female, "Relationship": "Secret-Keeper", "RelationshipRank": 0, "Events": [] }
        persondex["Yellow"] = {"Named" : True, "Value" : 5, "Contact": True, "Sex": Genders.Female, "Relationship": "Friend", "RelationshipRank": 0, "Events": [] }
        persondex["Klara"] = {"Named" : True, "Value" : 212, "Contact": True, "Sex": Genders.Female, "Relationship": "Bestie{size=10}?{/size}", "RelationshipRank": 0, "Events": [] }

        classstats = { 
            "Normal" : AimLevel() + 2,
            "Fire" : 1,
            "Water" : 0,
            "Grass" : AimLevel() + 4,
            "Electric" : AimLevel() + 3,
            "Ice" : 1,
            "Fighting" : 1,
            "Poison" : 1,
            "Ground" : 1,
            "Flying" : 1,
            "Psychic" : 1,
            "Bug" : 1,
            "Rock" : 1,
            "Ghost" : 1,
            "Dark" : 1,
            "Dragon" : 23,
            "Steel" : 1,
            "Fairy" : 1
        }

        renpy.music.queue("Audio/Music/Cinnabar_Start.ogg", channel='music', loop=None, fadein=0.0, tight=None)
        renpy.music.queue("Audio/Music/Cinnabar_Loop.ogg", channel='music', loop=True, tight=None)
        location = "school"

    scene blank2 with splitfade

    narrator "Meanwhile..."
    narrator "[leafcolor]You are no longer you.{/color}"

    show blank with dis

    pause 0.25

    show suite
    show brendan casual surprisedbrow frownmouth:
        xpos 0.8
    show nessa surprisedbrow frownmouth behind brendan:
        xpos 0.6
    show klara surprisedbrow frownmouth casual:
        xpos 0.4 xzoom -1
    show misty:
        xpos 0.2 xzoom -1
    with superslowdis

    leaf makeup bunny blush @happy "Did anyone order a leafy bunny? Sorry I'm late, guys, but I brought[ellipses]"
    leaf @scaredbrow talking2mouth "I[ellipses] I brought[ellipses]"

    klara @sadbrow talkingmouth "Oh... oh no! Oh noooo, Leaf, sweetie, what happened? You're here too early!"

    #klara angrybrow @closedbrow talking2mouth "God, {i}again{/i}?"

    leaf @scaredbrow talking2mouth "{size=30}I--{w=0.5}I-- early?{/size}"

    misty -surprisedbrow @talkingmouth "{size=30}Klara, do you know this girl? Is she, uh[ellipses] you know?{/size}"

    klara @talking2mouth "{size=30}What? No... I think she just gets confused easily.{/size}"

    leafmind @scaredbrow embarrassedmouth "What's...? What's happening...?"

    show klara with dis:
        ypos 1.0 xpos 0.4
        ease 0.5 ypos 1.2 zoom 1.3

    klara @talking2mouth "Leaf, sweetheart, you {i}really{/i} need to listen when people are talking to you. The party's on {i}Saturday{/i}."

    leaf @scaredbrow talking2mouth "It-- it {i}is{/i} Saturday--"

    klara surprisedbrow @angrybrow talking2mouth "{i}Next{/i} Saturday. Like I told you."

    pause 1.0

    leaf @angrybrow angrymouth "No you {i}didn't!{i} You said, multiple times, it was {i}this{/i} Saturday!"

    klara @sadbrow talking2mouth "Wait, you're getting angry at me because {i}you{/i} misunderstood? Please don't, I don't like drama."

    leaf @angrybrow talking2mouth "You said {i}this{/i} Saturday! At lunch on Wednesday and--and at--I've got the texts right here!"

    show phone_B
    show phone_A
    with fadeinbottom

    show phone_C behind phone_A with dis

    show phone_msg1 behind phone_A with dis
        
    $ title = Text("Klara galarpinkhair",size=30,font="fonts/consola_0.ttf",color="#313131")

    image msg7 = Text("Bestiiiiie!\nWhere r u, girl?\nBunny suit debut?\nParty starts on 12!",size=21,color="#ffffff",line_spacing=5,text_align=0.0)

    show text title behind phone_A:
        xalign 0.51 yalign 0.34
    show msg7 behind phone_A:
        xpos .41 ypos .4
    with dis

    pause

    hide phone_B 
    hide phone_A
    hide phone_C
    hide phone_msg1
    hide text title
    hide msg7
    with fadeoutbottom 

    klara @talking2mouth "Uh, yup. Party starts on 12. The party starts on the twelfth, next Saturday."

    leaf @angry "That is {i}not{/i} what that means! You're-- you're trying to--"

    klara @sadbrow talking2mouth "I'm trying to what? Because I've really just been a good friend to you, and you suddenly showing up and screaming at me is making me feel really unappreciated."
    klara surprisedbrow frownmouth @sadbrow talkingmouth "It's also a bit, um, embarrassing? Because, you know, you're going a bit crazy in front of three people who don't know you."

    brendan @talking2mouth "What? Uh, Klara, I know her. That's Leaf--"

    klara @talking2mouth "You knew her? So you knew she'd totally misunderstand when I was holding a party, dress up in a kinda weird outfit, then scream at me like {i}I'm{/i} at fault?"

    brendan sadbrow frownmouth @talking2mouth "Well, uh, no, but--"

    klara @talking2mouth "Uh, {i}yeah{/i}, {i}no{/i}. I mean, I'm surprised, too. I thought you were way more chill than this, Leaf."
    klara @talkingmouth sadbrow "It's totally alright to admit when you've made a mistake, okay? Even one like this. But it's not really okay to blame someone innocent for it."
    klara @happy "C'mon, Leaf, just admit that you made a big mistake, embarrassed yourself, and we can put this behind us."

    leaf @talking2mouth "You. Me. Outside."

    klara @talking2mouth "Oh, Leaf, I {i}really{/i} don't want to battle you[ellipses]"

    leaf @talking2mouth "We're not going to battle. We're going to {i}talk{/i}."

    klara @sadbrow talkingmouth "Oh[ellipses] okay."
    klara @sadbrow talking2mouth "Sorry, Misty, Nessa, Brendan, I guess Leaf just {i}really{/i} needs to talk to me right now. I know it's a tiny bit inconvenient, but can you carry on the study group without me?"

    misty @talkingmouth "Uh, yeah. Just don't take too long."

    $ DisplayPokemon("Tentacool")

    klara @talking2mouth "Tentacool, keep practicing your Bubble Beam. I want it perfect by the time I come back, alright?"
    klara @winkbrow talkingmouth "Sorry, guys, this will only take a minute!"

    pause 1.0

    klara @happybrow madmouth "C'mon, let's sort this out."

    narrator "You move back to the door, gesturing toward it impatiently as Klara marches through the doorframe. Your cheeks are a flaming red, as are your ears, and you try not to make eye contact with Brendan, who looks pityingly at you."

    scene dooropen 
    show klara casual frownmouth angrybrow
    with dis

    pause 2.0

    scene door
    show klara casual frownmouth angrybrow

    pause 2.0

    leaf bunny makeup cry bigblush @angry "Drop the act. Why the hell did you do this?!"

    klara surprisedbrow @talking2mouth "Bestie, you weren't listening. {i}I{/i} didn't do anything. You just screwed up, and this is what happened."

    leaf @angrybrow talking2mouth "You {i}lied{/i} to me! You {i}lied{/i} to me, multiple times, to trick me into coming here in-- in {i}this{/i} thing!"

    klara @talking2mouth "Leaf, I didn't. The party's next week. I {i}always{/i} told you that."
    klara @sadbrow talkingmouth "I {i}really{/i} don't appreciate you throwing these accusations around, like I'm {i}trying{/i} to embarrass you, okay?"
    klara @closedbrow talking2mouth "I know you don't think of me as much of a friend as I think of you, but you[ellipses] um, this is pretty low, you know?"

    pause 1.0

    klara @talking2mouth "Did {i}I{/i} do something? Is that why you pretended to think today's the party day? Were you actually trying to embarrass me?"

    leaf @angry "Pre--{i}pretended?!{/i}"

    if (HasEvent("Klara", "AgreePartner")):
        klara @sadbrow talkingmouth "You know, [first_name] told me while we were coordinating together that you and he were having some problems. Is this because of that?"

    else:
        klara @sadbrow talkingmouth "You know, [first_name] said he couldn't be my partner for the Millennium Drop. I thought that seemed weird, since he said he would be, before. Did you say something to him?"

    leaf @surprised "Wh-what?! No, [first_name] has {i}nothing{/i} to do with this, he--"
    leaf @angry "Wait, is {i}that{/i} what this is about?! Are you {i}jealous{/i} or something?"
    if (HasEvent("Leaf", "RejectedConfession")):
        leaf @angry "You know we're not dating, right?! You have literally {i}nothing{/i} to be jealous of!"

    klara @wrathbrow wrathmouth shadow "I'm really not jealous, no. I mean, this has nothing to do with {i}him{/i}--it's always been all about you."

    leaf @sadbrow talking2mouth "What?"

    klara @sadbrow talkingmouth "Like I said, bestie, it's you. You just made a silly mistake, and now, instead of admitting you were wrong, you're doubling down and making yourself look worse."
    klara surprisedbrow frownmouth @sadbrow talkingmouth "I think maybe you need to take a nap. Or maybe eat something? I know Kobukan gets really stressful--that's why my Water-type study group--"

    leaf @angrybrow angrymouth "And that's another thing! You just tricked me into walking into a group of Water-type students?! {i}Water-type?!{/i} I don't believe that's a coincidence, even for a moment."

    klara sadbrow -frownmouth "[ellipses]"
    klara surprisedbrow frownmouth @sadbrow talkingmouth "You think I tricked you into wearing a bunny suit and crashing my Water-type study group, because...?"

    leaf @angrybrow talking2mouth "Because you {i}know{/i} I'm scared of water."

    pause 2.0

    klara --frownmouth sadbrow @talkingmouth "Leaf, sweetie, I didn't. And you know how crazy that sounds, right?"

    show klara surprisedbrow frownmouth with dis:
        ypos 1.0 zoom 1.0
        ease 0.5 ypos 1.2 zoom 1.3

    narrator "You push your face right up against Klara's, glaring at her, not daring to blink."

    leaf @angrybrow talking2mouth "I'm. {w=0.5}Not. {w=0.5}Crazy."

    pause 1.5

    klara @talking2mouth "Leaf, I think you should probably go back to your dorm. It's clear you've really upset yourself, and... well, I think you should probably be alone, for a good, long, while."

    pause 1.0

    leaf @angrybrow talking2mouth "No. I'm going back into that room, and I'm explaining what you did to Brendan and the others. Then I'm explaining it to {i}everyone{/i} else--[first_name] first."

    klara @talking2mouth "Oh, bestie, you {i}really{/i} don't want to do that."

    show dooropen
    show klara wrathbrow madmouth:
        xpos 0.5 alpha 1.0
        ease 0.5 xpos 1.0 alpha 0.0
    with dis

    leaf @angrybrow talking2mouth "Don't call me bestie. I'm going in there right now, and--"

    scene blank with transeye2

    $ PlaySound("splash.ogg")

    pause 1.0

    narrator "The moment you open the door, a full-power blast of water hits you in the face."

    pause 3.0

    show blank with vpunch

    narrator "Waves."

    narrator "Heat."

    narrator "Noise."

    narrator "Then... hands. Eighty hands, wrapping around your limbs, your neck, stinging you with a paralytic poison, grabbing, pulling, pushing, {i}taking{/i}--and the memory of a cry for reprieve."

    TempCharacter("[leafcolor]Younger Leaf{/color}") "MOOOOM! DAAAD! HEEEELP ME! The Tentacruel, they're-- they're--they're drowning me! They're drowning me! HELP! I'm DROWNING! I'M DROWNING! HEEEEELP MEEEEE!"

    pause 1.0

    show suite
    show brendan casual surprisedbrow frownmouth:
        xpos 0.8
    show nessa surprisedbrow frownmouth behind brendan:
        xpos 0.6
    show klara casual shadow madmouth restrainedbrow:
        xpos 0.4 xzoom -1
    show misty:
        xpos 0.2 xzoom -1
    with superslowdis

    klara @talking2mouth "Oh, no! Naughty, {i}naughty{/i} Tentacool. I'm so sorry, I think my Tentacool got a bit too excited."
    klara @talkingmouth "I'm sorry, your makeup--huh? Oh, it's not running at all? That must be Wallace's special heavy-duty waterproof makeup! I bet you won't be able to get it off for a week."
    klara @happy "Well, sorry about the confusion, and my little Tentacool here getting a bit too enthusiastic. We're just finishing up our study session, so you should probably go back to your dorm to dry up."

    pause 2.0

    klara @shadow talking2mouth "Or was there something you wanted to say?"

    pause 1.0

    leaf bunny cry @scaredbrow talking2mouth "Ah..."

    narrator "Klara picks up a notebook and flips to an apparently random page. Though your vision is blurred by water and tears, you can make out its contents, in bold, thick, lettering..."
    
    show screen book_mixed_text(klarathreat) with Dissolve(3.0)

    show klara wrathbrow madmouth

    pause

    klara @talking2mouth "{i}Well{/i}? Was there something you wanted to say?"

    pause 2.0

    leaf @closedbrow cry2 sadmouth "Ahhh!"

    show klara surprisedbrow frownmouth with dis

    call clearscreens() from _call_clearscreens_267

    narrator "You ran away."

    show nessa sadbrow frownmouth
    show misty sadbrow frownmouth
    show brendan sadbrow frownmouth
    with dis

    pause 1.5

    klara -shadow -frownmouth -surprisedbrow @talking2mouth "She's really sensitive, I guess. Doesn't take criticism well."
    klara @talkingmouth "Anyway, should we continue? Bestie, you were questioning me, right?"

    misty -sadbrow @surprisedbrow talkingmouth "Yeah. Uh, should we care about--"

    show nessa -sadbrow with dis

    klara @talkingmouth "No, not really. What was your question?"

    misty @closedbrow talking2mouth "Uh, how much PP does Bubble Beam have?"

    klara @winkbrow talkingmouth "Oh, that one's easy. Twenty."

    klara shadow happybrow madmouth "Or thirty-two, with a PP Max."

    call clearscreens() from _call_clearscreens_268
    scene blank2 with Dissolve(2.0)

    pause 1.0

    narrator "Meanwhile..."

    python:
        playerparty = oldparty
        playercharacter = None
        inventory = oldinventory
        personalstats = oldpersonalstats
        persondex = oldpersondex
        classstats = oldclassstats

    return