init python:
    bunnypartydex = {
        "Recruitment" : ["Bea", "Cheren", "Skyla", "Silver", "Erika", "Flannery", "Grusha", "Hilbert", "Janine", "Jasmine", "Misty", "Raihan", "Sabrina", "Serena", "Tia", "Bianca", "Wally"],#kris omitted via technicality
        "Tech" : ["Nate", "Sonia", "Iono"],#"Ethan", 
        "Tailor" : ["Calem", "Dawn", "Hilda", "Whitney", "Gardenia"],#"Yellow", "Brendan", 
        "Food" : ["May",  "Hilda", "Sonia", "Gardenia"],#"Red", "Blue"
        "Bunny" : ["May", "Nate", "Nessa", "Whitney", "Rosa"]#"Ethan", "Leaf", "Red", "Mallow"
    }

    def BunRecruitCategory(category):
        count = 0
        checked = set()
        for name in bunnypartydex[category]:
            if BunRecruit(name):
                count += 1
        return count

    def BunRecruit(name):
        return HasEvent(name.title(), "BunnyRecruit")

    def FoodBunnies():
        foodbunnies = []
        for name in bunnypartydex["Food"]:
            if BunRecruit(name):
                foodbunnies.append(name)
        return foodbunnies

    def BunnyAmount():
        count = 0
        checked = set()
        for category in ["Tech", "Tailor", "Food", "Bunny"]:
            for name in bunnypartydex[category]:
                if name not in checked:
                    checked.add(name)
                    if BunRecruit(name):
                        count += 1
        return count

    def HighlightCharacter(charlist, extras="", reset=False):
        renpy.transition(dis)
        if reset:
            renpy.hide("semiblank2")
            LineUp()

        renpy.show("blank2", [Transform(alpha=0.3)], tag="semiblank2", zorder=6)

        # Normalize to list
        if not isinstance(charlist, list):
            charlist = [charlist]

        # Gather entries with original visual x and orientation
        entries = []
        for ch in charlist:
            tag = ch.lower()
            try:
                startx = _visual_x(tag)
            except Exception:
                startx = 0.5  # safe fallback to center if unavailable
            try:
                orientation = persondex[imageToCharDict[tag]]["Direction"]
            except Exception:
                orientation = "Right"
            entries.append((tag, startx, orientation))

        # Sort by original x (ascending: left -> right)
        entries.sort(key=lambda tup: tup[1])

        # Evenly spaced target positions (open interval) for N characters
        n = len(entries)
        charpos = [1.0 / (n + 1) * i for i in range(n + 1)]

        # Place in the same left->right order they originally appear
        for i, (tag, startx, orientation) in enumerate(entries, start=1):
            neutrals = " neutralbrow neutralmouth"
            if ("brow" in extras or "mouth" in extras):
                neutrals = ""
            renpy.show(
                GetCharacterSprite(tag, 1, "uniform" in extras, extras) + neutrals,
                [highlightmove(charpos[i], startx, orientation)],
                zorder=300
            )

    def CanBunnyRecruit(char):
        if char == "Professor Cherry":
            char = "Kris"
        return IsAfter(6, 6, 2004) and IsBefore(12, 6, 2004) and renpy.has_label(char + "BunnyRecruit") and not HasEvent(char, "BunnyRecruit")

label PostContestBunnyCheck():
    if (IsAfter(6, 6, 2004) and IsBefore(12, 6, 2004)):
        python:
            bunnyrecruits = []
            allpresent = { "May", "Jasmine", "Yellow", "Misty", "Serena", "Dawn", "Tia"} | ({ "Calem", "Grusha" } if not HasEvent("Game", "Contest2") else set())
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
                    call BunnyRecruit(contestchar, False, extra) from _call_BunnyRecruit_6

                "No.":
                    $ renpy.hide(contestchar.lower())

                    jump PostContestBunnyCheck

    return

label BunnyRecruit(char, uniform=True, extras = ""):
    stop music fadeout 1.5
    queue music "audio/music/NewFriends_start.ogg" noloop
    queue music "audio/music/NewFriends_loop.ogg"

    python:
        if (timeOfDay != "Evening"):
            AddEvent("Game", "AutoUniform")
        HighlightCharacter(char, ("uniform " if uniform else "") + extras)
        AddEvent(char, "BunnyRecruit")
        if (char == "Professor Cherry"):
            char = "Kris"
        renpy.call(char + "BunnyRecruit", char)
    return

label EndBunnyRecruit(char):
    stop music fadeout 1.5
    python:
        RemoveEvent("Game", "AutoUniform")
        renpy.transition(dis)
        renpy.hide("semiblank2")
        renpy.hide(char.lower())

    return

label BeaBunnyRecruit(char):#Points you to Nate
    red @talkingmouth "Hey, Bea. We're planning a party for Saturday. The theme is, uh, bunnies."

    bea @talking2mouth "Hm? Bunnies--as in Scorbunny? Wasn't Springsday a decent while ago?"

    show bea surprisedbrow lightblush with dis

    red @sweat talking2mouth "Uh... not exactly. It's less 'miracle of new life' bunnies and moreso, um, 'sexy' bunnies."

    bea @talking2mouth "Oh."

    pause 1.0

    red @talkingmouth "Any interest in coming? There'll be food, we've got a plan for keeping Security and the Disciplinary Committee off our backs, and, you know, lots of people in cute outfits."

    bea -surprisedbrow -lightblush @talking2mouth "While the idea of a costume themed around Mega Lopunny is surprisingly appealing, and warrants further consideration, I'm afraid I already have a commitment for that day."

    red @happy "Oh well. Know anyone else who maybe I should talk to?"

    bea @closedbrow talking2mouth "I believe Nate may have what you're looking for."

    if (not HasEvent("Nate", "BunnyRecruit")):
        red @talking2mouth "Hm? How?"

        bea @closedbrow talking2mouth "Well, he regularly runs rings around the school's Security, which may prove useful to you."
        bea @talkingmouth "That is secondary to the absolute lack of self-awareness with which he conducts himself, though."
        bea @sadbrow heavyblush talkingmouth "I'm quite certain that, if he was given the opportunity to dress in something outlandish, he would do so without a second thought."

        red @happy "Noted. Maybe I'll ask him, then. Thanks a bunch."

    else:
        bea @closedbrow talking2mouth "He regularly runs rings around the school's Security, which may prove useful to you."
        bea @talkingmouth "That is secondary to the absolute lack of self-awareness with which he conducts himself, though."
        bea @sadbrow heavyblush talkingmouth "I'm quite certain that, if he was given the opportunity to dress in something outlandish, he would do so without a second thought."

        red @happy "Guess we were on the same page. I already asked him. But thanks anyway."

    bea @talking2mouth closedbrow "I wish you the best in your bunny-hunting efforts."

    call EndBunnyRecruit(char) from _call_EndBunnyRecruit

    return

label CherenBunnyRecruit(char):#Points you to Gardenia
    red @talking2mouth "Cheren."

    cheren @sad2brow talking2mouth "Do not tell me anything I would be obligated to stop."

    pause 1.0

    cheren @talking2mouth "Talk to Gardenia."

    if (not HasEvent("Gardenia", "BunnyRecruit")):
        pause 1.0

        red @talking2mouth "Fine."
    else:
        red @talking2mouth "I already did."

        cheren @talking2mouth "Then there is no need for further words between us."

    call EndBunnyRecruit(char) from _call_EndBunnyRecruit_1

    return

label SkylaBunnyRecruit(char):#Points you to Gardenia
    show skyla surprisedbrow frownmouth with dis

    red @talkingmouth "Hey, Skyla. We're planning a party for Saturday. The theme is, uh, bunnies."

    skyla @talking2mouth "Wait, like... sexy bunnies?"

    red @wince talkingmouth "That's in the eye of the beholder, but, uh, yeah, I think that's what we're going for."

    pause 1.0

    red @talkingmouth "Any interest?"

    skyla -surprisedbrow -frownmouth @sadbrow talkingmouth "I'd be {i}way{/i} too embarrassed, being that exposed I mean, yes, I'm {i}very{/i} interested, but... sorry!"

    pause 1.0

    redmind @thonk "She... {i}really{/i} does not realize what she wears pretty much every day, does she?"

    show skyla sadbrow with dis

    red @happy "Alright, no pressure. Know anyone else who might be interested? We're looking for help with food, tailoring, and... uh... running interference."

    pause 1.0

    red @closedbrow talking2mouth sweat "Probably shouldn't have said that last part."

    pause 1.0

    skyla @sadbrow talkingmouth "Look, I know you guys aren't going to hurt anyone, and[ellipses] Cheren's stressed enough without me telling him about this."

    red @sadbrow talkingmouth "Thanks. We'll be safe, seriously. The only rule we'll break will be the curfew."

    skyla -sadbrow @talkingmouth "Anyway, {i}I{/i} can't go, but I bet you should ask Gardenia."

    if (HasEvent("Gardenia", "BunnyRecruit")):
        red @happy "I actually already did."

        skyla @surprised "Woah! You're more on top of things than my plane!"
        skyla @happy "Guess there's nothing I can tell you to help you out right now, then[ellipses] but I'll keep an eye out!"
        skyla @winkbrow talkingmouth "Or maybe {i}close{/i} an eye, if I feel like it."
    
    else:
        red @talkingmouth "Go on?"

        skyla @talking2mouth "She might not want to be there at the party herself--she's so busy, she probably {i}can't{/i} be--but she's an absolute wizard at logistics."
        skyla @talkingmouth "If you need food transported, or grills brought to wherever you're doing this, or, really, large quantities of {i}anything{/i} moved {i}anywhere{/i}, my dormmate's the person to do it!"

        red @happy "Thanks for the heads-up. I'll see what she says."

        skyla @happy "Sounds good to me. Have fun, and stay safe. I'll keep an eye out!"
        skyla @winkbrow talkingmouth "Or maybe {i}close{/i} an eye, if I feel like it."

    call EndBunnyRecruit(char) from _call_EndBunnyRecruit_2

    return
    
label SilverBunnyRecruit(char):#Points you to Gardenia
    show silver surprisedbrow frownmouth with dis

    red @talkingmouth "Hey, Silver. We're planning a party for Saturday. The theme is, uh, bunnies."

    silver @surprisedbrow talking2mouth "And you told me this? A member of the Disciplinary Committee?"
    silver @sadbrow talking2mouth "I'm going to make both our lives easier and pretend I didn't hear that. If you need help, talk to Gardenia. Otherwise, let me be ignorant."

    hide silver with dis

    pause 2.0

    if (HasEvent("Gardenia", "BunnyRecruit")):
        redmind @closedbrow frownmouth "Not my best idea. And I already talked to Gardenia, anyway[ellipses]"
    
    else:
        redmind @happybrow sweat "Not my best idea. But at least I got a new lead out of it!"

    call EndBunnyRecruit(char) from _call_EndBunnyRecruit_3

    return   
    
label ErikaBunnyRecruit(char):#Points you to Hilda
    if (GetRelationshipRank("Erika") == 0 and HasEvent("Erika", "RejectApology")):
        show erika surprisedbrow frownmouth with dis

    red @talkingmouth sweat "Hey, Erika. I'm sure it's a bit out of your comfort zone, but we're planning a party on Saturday. Would you be interested in coming?"

    if (GetRelationshipRank("Erika") == 0 and HasEvent("Erika", "RejectApology")):
        erika @talking2mouth "Is this... is the means by which you mean to indicate you've accepted my apology? Has the bad blood between us lessened?"

        red @closedbrow talking2mouth sweat "I[ellipses] no. I'm just asking you if you want to attend a party."

    erika @talking2mouth "Oh... I'm sure it would be a pleasure, but I'm afraid that I have extra tutoring on Saturday. Calligraphy."

    red @sadbrow talkingmouth "Ah, well."

    redmind @closedbrow frownmouth "I didn't even get to the point where I could tell her it was bunny-themed[ellipses]"

    red @talking2mouth "Well, we're also looking for some students who could help us with food, tailoring, and, uh, other stuff. Know anyone like that?"

    erika @happy "Oh, yes. Hilda, with whom I share my Poison class, is especially adroit with both knitting needle and carving knife--or so I've been told." #Should "poison" be capitalized in this line?
    erika @closedbrow talkingmouth "Instructor Koga seems to highly prize these skills--'life skills', so he calls them." 
    erika @sad2brow talking2mouth "I find myself in the peculiar position where one of my station is expected to know them, yet is discouraged from learning."
    erika @sadbrow talkingmouth "A common sentiment, I'm sure. In any case, I pray that the map I laid out leads you to the treasure you seek."
    erika @happy "Good day."

    hide erika with dis

    if (not HasEvent("Hilda", "BunnyRecruit")):
        redmind @thonk "Hilda, huh? Yeah, that makes sense. I'll see what she says."

    else:
        red @sadbrow "[ellipses]I don't have the heart to tell her I've already asked Hilda."

    call EndBunnyRecruit(char) from _call_EndBunnyRecruit_4

    return 

label FlanneryBunnyRecruit(char):#Points you to Whitney
    show flannery lightblush surprisedbrow frownmouth with dis

    if (timeOfDay == "Morning"):
        red uniform @talkingmouth "Hey, Flannery. Maybe you heard already, but we're planning a party for Saturday. A big, bunny-themed party."

    else:
        red @talkingmouth "Hey, Flannery. Maybe you heard already, but we're planning a party for Saturday. A big, bunny-themed party."

    flannery @talkingmouth "Dude, {i}seriously?{/i}"

    red @talkingmouth "Sure am. Any interest in coming?"

    flannery -surprisedbrow @sad2brow talkingmouth "Will, uh, will everyone there be wearing bunny suits?"

    red @talkingmouth "That's the plan. Guys and girls. Whoever wants to come."

    flannery -frownmouth -lightblush @closedbrow lightblush talkingmouth "Hey, I'm sure it'll be great, and this sounds {i}right{/i} up Whit's alley. I'm just not sure that I can[ellipses]"
    flannery @sad2brow talking2mouth "That's a {i}lot{/i}, you know? Fair to anyone confident enough to pull that off, but I'm not one of them."

    red @happy "Totally fine, Flannery. {i}No{/i} pressure."

    flannery @closedbrow talking2mouth "{i}Phew.{/i}"
    flannery @talkingmouth surprisedbrow "Oh, but, like I said, you should {i}definitely{/i} ask Whitney about this. No way she'll turn this down. I bet she'll even make an extra outfit for you, if you catch her early enough."

    if (not HasEvent("Whitney", "BunnyRecruit")):
        red @talkingmouth "Thanks a bunch. I'll definitely ask her, yeah."

    else:
        if (GetEventDatetime("Whitney", "BunnyRecruit") < calDate):
            red @happy "Already did. Surprised she hasn't told you yet, actually."

            flannery @talking2mouth "{size=30}Come to think of it, she has been spending a {i}lot{/i} of time in her room[ellipses] guess that sound was a sewing machine, after all.{/size}"
        else:
            red @talkingmouth "I just did. She'll probably tell you later today."

    flannery @talking2mouth "Well, thanks for the invite, dude. Wish I could be there. Maybe, uh, maybe next month's."

    red @happy "Yeah, maybe."

    flannery @winkbrow talkingmouth "Tell me if anything hot happens. I'm always looking for new material."

    call EndBunnyRecruit(char) from _call_EndBunnyRecruit_5

    return 

label GrushaBunnyRecruit(char):#Points you to Whitney
    red @talkingmouth "Hey, Grusha. Maybe you heard already, but we're planning a party for Saturday. A big, bunny-themed party."

    if (GetRelationshipRank("Grusha") > 0):
        grusha @upeyes angryeyebrows talking2mouth "I wore a skirt {i}one{/i} time. Is that what I'm going to be known for?"

    else:
        grusha @unamusedbrow "I hope you don't expect me to do anything with this information."

    red @sweat closedbrow talking2mouth "Alright, rolling it back. Not a fan of the bunnies, I get it."
    
    red @talkingmouth "We're also looking for help with cooking[ellipses] tailoring[ellipses] interference?"

    pause 1.0

    red @talkingmouth "Nothing?"

    grusha @talking2mouth "If you need a guy who used to be able to snowboard, I'm there. Otherwise, being surrounded by a bunch of people in bunny suits could literally kill me."
    grusha @sad2brow talking2mouth "And if it doesn't, it'll make me want to die."

    red @closedbrow talking2mouth "Noted."

    grusha @confusedbrow "Maybe Whitney can help you. She's a seamstress, and I know she'd take any excuse to put other women in bunny suits."
    
    if (HasEvent("Whitney", "BunnyRecruit")):
        red @talkingmouth "Been there, I'm afraid."

        grusha @closedbrow talking2mouth "Eh. {i}Perdón.{/i} That's all I have."

    else:
        red @talkingmouth "Huh. Yeah, alright, I'll try that. Thanks."

        grusha @talking2mouth "{i}De nada.{/i}"

    call EndBunnyRecruit(char) from _call_EndBunnyRecruit_6

    return 

label HilbertBunnyRecruit(char):#Points you to Hilda
    if (timeOfDay == "Morning"):
        redmind uniform @unamusedbrow unamusedmouth "Yeah... I was this guy's roommate. I already know how this'll play out."
    else:
        redmind @unamusedbrow unamusedmouth "Yeah... I was this guy's roommate. I already know how this'll play out."
    redmind @happy sweat "But that's no excuse not to try...!"

    red @talking2mouth closedbrow sweat "Would you ever wear a bunny suit?"

    pause 3.0

    hilbert @talking2mouth "I think I just had a stroke. What did you say?"

    red @talking2mouth sweat "Nevermind. If you were looking for someone who knew how to cook or sew, who--"

    hilbert @talking2mouth "Hilda."

    pause 1.0

    red @talking2mouth "Yep. I figured. Thanks for the talk."

    narrator "You quickly slip away, for once appreciative of Hilbert's lack of curiosity."

    pause 2.0

    hilbert @surprised "{size=30}Wait, did he {i}actually{/i} say 'bunny suit'? Is that--is that actually...?{/size}"

    call EndBunnyRecruit(char) from _call_EndBunnyRecruit_7

    return 
    
label JanineBunnyRecruit(char):#points you to Sonia
    if (IsDate(11, 6, 2004) and timeOfDay == "Night"):
        narrator "The monumental weight of what you're about to ask settles on your shoulders."

    else:
        narrator "You only get a few steps within Janine's aura of power before the monumental weight of what you're about to ask settles on your shoulders."

    pause 1.0

    narrator "You simply cannot, and decide to skip to your follow-up question."

    red @happy sweat "H-hey, Janine! Um... do you know anyone who's especially good at cooking, or tailoring, or technology?"

    janine @surprisedbrow talking2mouth "What, like my Aunt Aya?"

    red @talkingmouth "I was thinking someone closer to home. A student here, maybe?"

    janine @talking2mouth "I barely know anyone outside of the Battle Team. Best I can say is Sonia's pretty good with computers."
    janine @sadbrow talkingmouth "I[ellipses] assume. She spends enough time on them that she ought to be, in any case."
    janine @closedbrow talking2mouth "{size=30}Maybe I need to get out more.{/size}"

    red @happy "Alright, that's fair. Thanks. And..."

    narrator "...Perhaps, now, if you speak without thinking, you can break through your terror."

    menu:
        ">Quickly invite her, before you think better of it!":
            show janine surprisedbrow frownmouth lightblush with dis

            red @talking2mouth "Would you be interested in attending a bunny suit party Blue, Ethan, and I are hosting this Saturday?"

            pause 2.0

            $ ValueChange("Janine", 5)

            janine -surprisedbrow -lightblush @closedbrow talkingmouth "No. But thanks for the invite. It's been a while since I've been invited to any parties."
            janine @sad2brow talkingmouth "Apparently, I'm 'intimidating.'"

        ">Keep your tongue safe in your mouth":
            narrator "You quickly escape before any more 'brave' ideas pop into your head."

    call EndBunnyRecruit(char) from _call_EndBunnyRecruit_8

    return

label JasmineBunnyRecruit(char):#points you to Whitney
    red @talkingmouth "Hey, Jasmine. We're planning a party for Saturday. The theme is, uh, bunny suits."

    jasmine @talking2mouth "Oh? How novel. I hope you enjoy!"

    red @happy "Hey, I'm inviting you."

    jasmine @talking2mouth sadbrow "Oh? Me, in a bunny suit? I'm not sure where I'd get one that would fit me. And I don't think anyone would want to see that."

    if (HasEvent("Jasmine", "JamesBlunt")):

        show jasmine lightblush surprisedbrow 
        
        red @sadeyebrows lightblush talkingmouth "This part of 'anyone' would."

        pause 1.5
        
        jasmine -lightblush -surprisedbrow @happy "...Flatterer."

        $ ValueChange("Jasmine", 3)

        red @lightblush talkingmouth "*Ahem.* Anyway, we'll be making outfits for the guests. Custom designs, since we know they can be expensive, and it's very short notice."

    else:
        
        red @talkingmouth "We're going to be making them for the guests. Custom designs, since we know they can be expensive, and it's very short notice."

    jasmine @sadbrow talkingmouth "Clever, but whether I'd be well enough to claim the suit made for me is a bit of a coinflip. I wouldn't want someone to go through all that effort, and then have me fail to show up."
    jasmine @talking2mouth "I should especially take Saturday easy so that I'm in passable health for the Millennium Drop."
    jasmine @closedbrow talking2mouth "Even aside from all that... I tend to bring the mood of parties down after a short while. It's probably for the best that I do not."

    red @sadbrow frownmouth "[ellipses]{nw}"
    extend @sadbrow talking2mouth "Alright. If you're sure."
    red @talkingmouth "Well, uh, we're also looking for help with cooking, sewing, and if you know someone who could help us keep this all quiet, too[ellipses]"

    jasmine @sadbrow talkingmouth "I'm afraid I'm not versed in any of those particular skills."
    jasmine @talkingmouth "I appreciate the offer, though. May I suggest you also extend it to Whitney?"
    jasmine @talkingmouth "She's a very talented seamstress, and[ellipses] well, I'm sure she'd be very popular, if she chose to attend, which I'm certain she would."
    
    if (not HasEvent("Whitney", "BunnyRecruit")):
        red @talkingmouth "That's a good idea. Thanks, Jasmine."

        jasmine @talkingmouth "I'm happy to provide what little help I can."

    else:
        red @happy "Got to her already."

        jasmine @talkingmouth "Then it would seem everything's well-sorted."

    jasmine @happy "I {i}do{/i} hope you have fun!"

    call EndBunnyRecruit(char) from _call_EndBunnyRecruit_9

    return

label MistyBunnyRecruit(char):#points you to Dawn
    red @talkingmouth "Hey, Misty. We're planning a party for Saturday. The theme is, uh, bunny suits. Are you interested?"

    misty @talking2mouth "You realize how perverted that sounds, right?"

    red @closedbrow talking2mouth "'No' is fewer words."

    pause 1.0

    misty @sadbrow talking2mouth "Does this have anything to do with that one girl who wore a bunny suit and got splashed last Saturday?"

    red @talking2mouth "Yeah. We're trying to cheer her up, basically. Give her a {i}real{/i} bunny party."

    misty @closedbrow talking2mouth "Well, it still sounds gross and misogynistic, but maybe you're not doing it {i}on purpose{/i}."

    red @talking2mouth "'No' is still fewer words. {size=30}And there'll be guys, too.{/size}"
    
    if (not HasEvent("Game", "Contest3")):
        misty @talking2mouth "Whatever. I'm not interested in this, and I've gotta spend Saturday practicing for the Millennium Drop, anyway, but maybe ask Dawn."
    else:
        misty @talking2mouth "Whatever. I'm not interested in this, and I'm going to be protesting at the harbor on Saturday, anyway, but maybe ask Dawn."

    red @talking2mouth "Dawn? You really think she'd want to--"

    misty @angrybrow talking2mouth "No, she {i}obviously{/i} wouldn't want to be a bunny, but she can at least make the suits!" 
    misty @angry "I {i}know{/i} you're not forcing your guests to bring their own costumes!"
    misty @closedbrow talking2mouth "And if you are, you shouldn't be."

    if (HasEvent("Dawn", "BunnyRecruit")):
        red @talking2mouth "We're not, and I already talked to Dawn. I didn't get anything out of this besides you yelling at me."

        misty @talking2mouth "Well, maybe you'll remember that next time."

    else:
        red @closedbrow sweat talking2mouth "We're not. And[ellipses] thanks for the heads-up on Dawn. I'll go talk to her."

    pause 1.0

    misty @closedbrow talking2mouth "If you're {i}really{/i} doing this for that one girl, and not because you're a gross man, then[ellipses] you're alright, I guess."

    hide misty with dis

    redmind @happy "Hey, high praise from Misty."

    call EndBunnyRecruit(char) from _call_EndBunnyRecruit_10

    return

label RaihanBunnyRecruit(char):#points you to Nessa
    red @talkingmouth "Hey, Raihan. We're planning a party for Saturday. The theme's bunny suits. Are you interested?"

    raihan @happybrow talkingmouth "Bunnies? Pull the other one. Sounds like a killer time, mate, but that's not the sort of thing the Great Raihan can go to all willy-nilly, you know?"
    raihan @talkingmouth "Gotta keep my image squeaky-clean. Reckon I'm half too old for most of the people who'd be at your party, anyway. Don't want to be that old git who people have to turn the music down for."

    red @sweat unamusedbrow talkingmouth "Raihan, you're twenty-three."

    raihan @sadbrow talking2mouth "Don't I feel it."
    raihan @talkingmouth "Nah, mate, not for me. Ask Ness, though, reckon she'd be right up for it. Figure she's been on a bit of a dress-up withdrawal recently, since she's put her job on hold."

    if (HasEvent("Nessa", "BunnyRecruit")):
        red @talkingmouth "Right you are. In fact, I already asked her, and she's in."

    else:
        red @talkingmouth "Good idea. Thanks for the tip--I'll ask her."

    if (GetRelationshipRank("Raihan") == 0):
        raihan @happy "Aces. Stay safe, and don't sneak any liquor. I know the drinking age here's nonsense, but it's not worth getting caught."
    else:
        raihan @talkingmouth "Ace." 

        pause 1.0
        
        raihan @talking2mouth "Just between you and me, mate, some of the stuff her agency made her wear makes a bunny suit look tame. Wasn't right, given how young she was."
        raihan @closedbrow talking2mouth "Never wanted to cause a problem for her, so I didn't say anything, but[ellipses] I'm just glad to see her deciding what she wears for once. And if it's a bunny suit, more power and long ears to her."

        red @talkingmouth "Hell yeah. Everyone at this party's going to know exactly what they're getting into. No nasty surprises, this time."

        raihan @talkingmouth "Good on ya. Stay safe, and don't sneak any liquor. I know the drinking age here's nonsense, but it's not worth getting caught."

    red @sweat talkingmouth "We'll be safe, don't worry. No drinks."

    call EndBunnyRecruit(char) from _call_EndBunnyRecruit_11

    return

label KrisBunnyRecruit(char):#points you in the direction of iono or whitney
    narrator "[ellipses]"
    narrator "Obviously, you do not actually ask Professor Cherry to the party."

    hide kris with dis

    pause 1.0

    if (IsPresent("Iono") and not HasEvent("Iono", "BunnyRecruit")):
        narrator "However, it occurs to you that, if you're looking for tech support, Iono's probably the most technologically-able person in the school. It might be worth asking her for some guidance[ellipses]"
    
    elif not HasEvent("Whitney", "BunnyRecruit"):
        narrator "However, remembering how Whitney flushed like an embarrassed schoolgirl upon seeing Professor Cherry in class[ellipses]"
        narrator "You're reminded that Whitney would probably take any excuse to see women in bunny suits, including wearing one herself."
        narrator "Perhaps even making them, if that's within her capabilities. Maybe something to follow up on[ellipses]"
    else:
        narrator "You fear you may have just wasted some time[ellipses]"

    return

label SabrinaBunnyRecruit(char):#points you toward Rosa
    red @talking2mouth "Hey--"

    if (not HasEvent("Rosa", "HalfBunnyRecruit")):
        sabrina @talking2mouth "No, but ask Rosa."
    else:
        sabrina @talking2mouth "No."

    hide sabrina with dis

    pause 1.0

    red @confused "Well[ellipses] brevity's a virtue, I guess."

    call EndBunnyRecruit(char) from _call_EndBunnyRecruit_12

    return

label SerenaBunnyRecruit(char):#points you toward Calem
    red @talkingmouth "Hey, Serena. We're planning a party for Saturday. The theme is, uh, bunnies."

    serena @blush surprised "Oh my. How delightfully scandalous!"

    red @talkingmouth "Nah, it won't be anything like that. It'll be a good time. A low-key stressless environment where everyone just happens to be wearing bunny suits."

    serena @talkingmouth "How charming. May I assume this is an invitation?"

    red @talkingmouth "May I assume this is acceptance?"

    if (HasEvent("Game", "Contest3")):
        serena @sadbrow talking2mouth "Tragically, you cannot. I find myself otherwise-booked for Saturday--Misty's involved me in a rather fun-sounding bout of environmental activism."
    else:
        serena @sadbrow talking2mouth "Tragically, you cannot. I find myself otherwise-booked for Saturday--last-minute preparations for the Millennium Drop. Though I'd cancel my plans in a heartbeat if I could--this sounds {i}far{/i} more fun."

    red @sadbrow talkingmouth "Oh, well. We're also looking for help with food, costumes, and keeping the Disciplinary Committee or security from shutting things down?"

    serena @talkingmouth "Oh, then perhaps I can help in some small way, after all. Calem does not make much show of it, but he's a decent tailor--well, for artistic embellishments, in any case." 
    serena @talking2mouth "Larger garments still somewhat escape him, but Brendan's been teaching him. But for adornment of {i}this{/i} kind, I think he should be fully up-to-task."
    serena @talkingmouth "He is free this Saturday--perhaps he can help?"

    if (not HasEvent("Calem", "BunnyRecruit")):
        red @talkingmouth "Huh, I didn't know that he could sew. What a renaissance man!"

        serena @talkingmouth "He would be {i}very{/i} flattered to hear you say that, I'm sure of it."
        serena @happy "Keep me abreast of what goes on, if you please. Especially if there's any... scandal, perhaps."

    else:
        red @happy "'Fraid I already asked him. Thanks, though."

        serena @talkingmouth sadbrow "Ah, well. Perhaps I cannot help after all. Even so, do keep me abreast of what goes on, if you please. Especially if there's any... scandal, perhaps."

    red @talking2mouth "I'll keep my ear to the ground."

    call EndBunnyRecruit(char) from _call_EndBunnyRecruit_13

    return

label TiaBunnyRecruit(char):#points you toward Whitney
    red @happy "Hey, Tia! We're planning a party on Saturday. We're looking for some help with sewing, cooking, and... uh, keeping everything low-key."
    red @talkingmouth "Think you could help with any of that? Or maybe know someone who could?"

    show tia happy:
        ypos 1.2 xpos 0.5
        ease 0.2 ypos 1.25
        ease 0.2 ypos 1.2

    if (GetRelationshipRank("Tia") == 0):
        narrator "Tia nods happily, and starts signing at you rapidly... before seeming to realize that you're not getting any of it."

        show tia sadbrow with dis

        red @sadbrow talkingmouth "Sorry. Could you write something down, maybe...?"

        show tia closedeyes angryeyebrows frownmouth with dis

        narrator "Tia closes her eyes and appears deep in thought... she then holds up three fingers on her hand."

        red @talking2mouth "Three? Uh, 'W'?"

        pause 1.0

        if (not HasEvent("Whitney", "BunnyRecruit")):
            show tia happybrow -frownmouth with dis

            red @happy "Oh, Whitney! Got it, I'll ask her."

            red @talkingmouth "Thanks, Tia."

        else:
            show tia sadbrow -frownmouth with dis

            red @happy "Oh, Whitney! Sorry, I actually already asked her."

            red @talkingmouth "It was a good idea, anyway. Thanks, Tia."

    elif (GetRelationshipRank("Tia") == 1):
        narrator "Tia nods happily, and starts signing at you rapidly."

        tia "Sure! Whitney is {i}really{/i} good at [tiafont]sewing{/font}. I'm sure [tiafont]she'd be more than{/font} happy to help--[tiafont]especially{/font} if she gets to go to a [tiafont]party{/font}, as well!"

        red @happybrow talkingmouth "Well, I didn't get {i}all{/i} of that, but I did get Whitney."

        if (not HasEvent("Whitney", "BunnyRecruit")):
            show tia happybrow -frownmouth with dis

            red @happy "I'll ask her. Thanks, Tia."

        else:
            show tia sadbrow -frownmouth with dis

            red @sadbrow talkingmouth "I actually already asked her, though. It was a good idea, anyway. Thanks, Tia."

    else:
        narrator "Tia nods happily, and starts signing at you rapidly."

        tia "Sure! Whitney is {i}really{/i} good at sewing. I'm sure she'd be more than happy to help--especially if she gets to go to a party, as well!"

        red @happybrow talkingmouth "Hey, I actually got all of that! Look at me, bein' all cultured and knowing three languages and stuff."

        if (not HasEvent("Whitney", "BunnyRecruit")):
            show tia happybrow -frownmouth with dis

            red @happy "Anyway, I'll ask her. Thanks, Tia."

        else:
            show tia sadbrow -frownmouth with dis

            red @sadbrow talkingmouth "Buuuut... I actually already asked her. It was a good idea, anyway. Thanks, Tia."

    show tia happybrow with dis

    pause 0.1

    hide tia with gaussdissolve

    narrator "Tia waves goodbye, while you quickly look around, making sure nobody saw that."

    call EndBunnyRecruit(char) from _call_EndBunnyRecruit_14

    return

label BiancaBunnyRecruit(char):#points you toward May
    red @talkingmouth "Hey, Bianca. You doing alright?"

    bianca @sideeyes talking2mouth "Mmmmostly."

    red @sweat talking2mouth "Right. Well, no pressure, but we're planning a party for this Saturday[ellipses]"

    bianca @talkingmouth "Oh, yup. Yellow told me. Um, I don't think I can go, though."

    red @sadbrow talkingmouth "That's alright. You {i}did{/i} just go to Dawn's birthday a couple weeks ago."

    redmind @wince frownmouth "And, you know, the {i}other{/i} thing that happened that week[ellipses]"

    bianca @talking2mouth "You were looking for help with cooking, though, right?"

    red @talkingmouth "Oh, yeah! Do you know anyone?"

    bianca @happy "May! When we were dormies, she used to do half of the cooking, with Hilda, and everything she made was so super-scrumptious-yummy-licious. I bet she'd love to go to your party, and cook, too."

    if (HasEvent("May", "BunnyRecruit")):
        show bianca surprisedbrow frownmouth with dis

        red @closedbrow talking2mouth "I've[ellipses] already asked her, actually."

        bianca -surprisedbrow -frownmouth @talkingmouth happybrow "Oh, well. I'll keep thinking, and if I come up with any more ideas, I'll tell Yellow during our classes together."

        red @happy "Thanks, Bianca."

    else:
        red @talkingmouth "Oh, good idea. Thanks, Bianca!"

    show bianca:
        ypos 1.2 xpos 0.5
        ease 0.2 ypos 1.25
        ease 0.2 ypos 1.2
        ease 0.2 ypos 1.25
        ease 0.2 ypos 1.2
        ease 0.2 ypos 1.25
        ease 0.2 ypos 1.2

    $ ValueChange("Bianca", 1)

    bianca @happy "Happy to help!"

    hide bianca with dis

    narrator "Bianca walks away, slightly more of a spring in her step than she had before. Seems you might've done a good thing."

    call EndBunnyRecruit(char) from _call_EndBunnyRecruit_15

    return

label WallyBunnyRecruit(char):#points you toward Dawn
    show wally surprisedbrow with dis

    red @talkingmouth "Hey, Wally. We're planning a party for Saturday. Everyone'll be wearing bunny suits. Are you interested?"

    wally @sideeyes talking2mouth "Why does everyone keep trying to put me in women's clothing? {size=30}I'm small. I'm just small, I'm not... I'm not like {i}that{/i}.{/size}"

    red @closedbrow talkingmouth "Oh, yeah, you did mention how Whitney kept trying to--"

    show wally with vpunch

    wally sadbrow @dead2eyes sadeyebrows talking2mouth "Gah, no, please, don't bring it up again!"

    red @sadbrow talking2mouth "Sorry. If it's any consolation, I think people just keep trying to put you in cute outfits 'cause they think you'd look cute in them."

    wally @talking2mouth "That's {i}not{/i} a consolation. {size=30}Why don't people think I'd look cute in a suit and tie? Maybe a cape...?{/size}"

    redmind @thonk "I think I can psychically {i}hear{/i} Ethan groaning."

    red @talking2mouth "So it's a 'no' on the bunnies. Got it. We're also looking for some help with cooking, logistics, and tailoring. Don't suppose you've got a hidden talent for any of them?"

    wally @happy "If I do, it's {i}very{/i} hidden."

    wally @talking2mouth "Oh, but--tailoring, right? Pretty much all of my classmates in Fairy could probably help you with that. Dawn, I think, is probably one of the best."

    if (HasEvent("Dawn", "BunnyRecruit")):
        red @talkingmouth "Ah, sorry. Already asked her. She's a 'yes', though, so it was a good idea."

        wally @closedbrow talking2mouth "Oh. Okay. Well, I hope you, um[ellipses]"

    else:
        red @talkingmouth "Good idea. I'll chat with her."

        wally @talkingmouth "Glad I could help. I hope you, um[ellipses]"

    pause 1.0

    wally @talkingmouth "Good luck. Yeah, that's what I was trying to say. Good luck on the partying."

    red @happy "Thanks. And if you change your mind--"

    wally @unamusedbrow talking2mouth "I {i}promise{/i} I won't."

    call EndBunnyRecruit(char) from _call_EndBunnyRecruit_16

    return

label BugsyBunnyRecruit(char):#points you toward May. Did you wanna add that item reward for this fight and Morty's? Fine either way!    
    if (_return): # Do I need to add something labeling this battle somewhere?
        bugsy @happy "Darn! That was a great battle--but don't think you've squished us yet! Bug trainers never say die!"

        bugsy @talkingmouth "Anyway, a promise is a promise! I, Bugsy, hereby and forthwith declare your Pikachu..."

        bugsy @happy "An honorary Bug-type!"

        $ renpy.music.play("Audio/Pokemon/pikachu_happy2.ogg", channel="altcry", loop=None)
        libpikachu happy "Pika!"

        red @happy "He's deeply honored!"

    else:
        bugsy @happy "Mwa ha ha! I'll save you a seat in Burgh's class!"

        red @sadeyebrows talkingmouth "Okay, okay, you got me."
        
        bugsy @happy "Don't let it bug you! Your team was really amazing, and it looked like they had lots of fun!"

        red @happy "Right back atcha."

    red @talkingmouth "Hey, Bugsy--while I've got you here, would you want to come to a party this weekend? It's, uh, bunny-themed."

    bugsy @surprisedbrow talking2mouth "Bunnies? Like, we have to {i}bring{/i} bunnies? Some of Burgh's Pokémon are real good at hopping, but they're not very fuzzy."

    red @happy "Nah, don't worry--there's no bunny requirement for entry. Think more like... bunny costumes. Sexy bunny costumes."

    bugsy @surprised "OHHHHHHHHHH! {i}That{/i} kind of bunnies!"

    bugsy @sadbrow talkingmouth "Yyyeaaahhhh, that sounds a little bit... much for me. Also, I'm not sure if I[ellipses] y'know[ellipses] qualify."
    
    red @talkingmouth sadeyebrows "Of course you do. All bunnies are welcome: guys, girls, neither, both. But if that doesn't sound like your thing, no pressure at all."

    bugsy @happy "I'm still gonna pass, but I'm really happy you invited me! If you ever decide to throw a bug-themed party, I am THERE."

    bugsy @surprisedbrow talking2mouth "Ooh! You know who you oughta ask, though? May! She dresses up all the time for contests--and her cooking is sooooo good! Maybe you could get her to bring cookies!"

    bugsy @happy "Or... carrot cake...?"

    if (HasEvent("May", "BunnyRecruit")):
        red @talkingmouth "Sorry; beat you to it! I've asked May already."

        bugsy @talkingmouth "Rats! Well, I hope you have lots of fun at the party!"

        red @happy "Thanks, Bugsy. I'm sure we will."

    else:
        red @talkingmouth "Right, good idea. Should've thought of that myself."

        bugsy @talkingmouth "If you come to every Bug class, you'll never miss it when she brings snacks."

        red @happy "I'll take that under advisement."

    call EndBunnyRecruit(char) from _call_EndBunnyRecruit_17

    return

label MortyBunnyRecruit(char):
    morty @talkingmouth "Nice match."

    red @happy "Yeah, that was fun! We should do it again sometime!"

    pause 1.5

    morty @talkingmouth "Now, I don't have to be a psychic to see where this is going. You're standing around all awkward like you wanna ask me something, even though you know the answer."

    show morty surprisedbrow frownmouth with dis

    red @embarrassedeyebrows talkingmouth "Would you want to dress up as a sexy bunny for a secret party we're having to cheer up one of my friends?"

    morty @talking2mouth "Okay, {i}definitely{/i} not a psychic."
    morty -surprisedbrow @happybrow talkingmouth "Not a party guy, either--but you knock yourselves out. Show that friend of yours a good time for me."

    red @talkingmouth "Yeah, I kind of saw that coming. Any chance you're good at sewing?"

    morty @talkingmouth "Nope."

    red @talkingmouth "Tech support?"

    morty @talkingmouth "Nope."

    red @talkingmouth "Cooking?"

    morty @talkingmouth "Only if your crowd likes it {i}real{/i} spicy." # ghost peppers ba dum tss #FREUDNOTE: heh

    red @sadeyebrows talkingmouth "Dang. Got any friends who you think {i}would{/i} be interested?"

    morty "[ellipses]"

    pause 1.0

    morty @talking2mouth "Now, I'm not trying to pull your leg, here."

    red @happy "Hey, I'm open to ideas! Otherwise I wouldn't be canvassing in gym class."

    morty @talkingmouth "Fair enough."
    morty @talking2mouth "Maybe you oughta ask Melody."

    pause 1.0

    red @confused "Wait, are we talking about the same Melody? Green hat; big sunglasses? Blows more bubbles than a Popplio?"

    red @surprised "Actually, hold on--backtrack for a second. You're {i}friends{/i} with Melody?!"

    morty @talking2mouth "Dunno if I'd put it that way, but yeah, we get along. We sit at the same lunch table."

    red @surprisedbrow talking2mouth "Melody doesn't let anybody sit at her table."

    morty @talkingmouth "Maybe I let her sit at mine."
    morty @talking2mouth "I dunno. She never seemed so bad. I don't ask her any stupid questions, and nobody bothers me while I'm reading if she's around."
    morty @talkingmouth "Besides, we've got a thing or two in common. She's got a thing for old folktales, just like I do. And neither of us wants to bother anybody--we just like being left alone."

    if (GetSeenClassScenes("Water") >= 10):
        red @sadeyebrows talking2mouth "That's an... interesting take on Melody. I don't think Instructor Wallace would agree. And I {i}definitely{/i} don't think she'd come to a sexy bunny party."
    else:
        red @sadeyebrows talking2mouth "That's an... interesting take on Melody. I'm not sure everyone would agree. And I {i}definitely{/i} don't think she'd come to a sexy bunny party."
    
    morty @talkingmouth "She definitely won't. But she might like it if you asked."

    red @sadeyebrows talkingmouth "Yyyyeah, I[ellipses] I'll think about it, Morty. Thanks."

    morty @talkingmouth "Ciao."

    call EndBunnyRecruit(char) from _call_EndBunnyRecruit_18

    return

label IonoBunnyRecruit(char):#Tech Support
    show iono surprisedbrow surprisedmouth with dis

    red @talkingmouth "Hey, Iono. We're planning a party for Saturday. The theme is, uh, bunnies."

    iono neutralbrow neutralmouth @confusedbrow talking2mouth "Holy shit, chat, did our age rating just smash through T and hit M?"

    red @talkingmouth "Nah, it won't be anything lewd. I mean, no more than bunny suits are, inherently, I guess."
    red @talkingmouth "It'll be a good time. A low-key stressless environment where everyone just happens to be wearing bunny suits."

    iono @talking2mouth "Mmm... not sure I can go, though. It'd make people think I was a 'normal student', sure, but[ellipses]"
    iono @sadbrow talking2mouth "The whole 'eating food, hanging out with people, making casual physical contact[ellipses]'"
    iono @angrybrow talking2mouth "I ain't about that life, homie!"

    redmind @thonk "Is she allowed to say that?"

    iono @happybrow talkingmouth "Buuuuut, as you may recall, the hyper-genius Iono the Supercharged Streamer is not only sexy and hilarious, but also the smartest person since whoever the [[COMMUNITY STANDARDS VIOLATION] invented sliced bread!"

    red @surprisedbrow talking2mouth "How the fuck did you just say that?"

    iono @happybrow happymouth "That's right! If you've got a bunch of sexy girls--"

    red @talking2mouth "Guys, too. We're doing equal-opportunity fanservice."

    iono @shivereyes angryeyebrows talking2mouth "If you've got a bunch of sexy {i}personajes{/i}, you're going to want to make sure that there aren't any creeps around who try to record the guests!"

    red @confused "I[ellipses] I guess we {i}do{/i}, actually, have a few semi-famous people who might attend the party. I guess that's something we should actually keep in mind, yeah."

    iono @talking2mouth "Then don'tcha worry about nothing, my luddite buddy-o! I'll keep an eye on all electric activity happening within three hundred meters of the party location."

    red @thinking "Three hundred meters?"

    iono @sadbrow talking2mouth "The range of the kinds of cameras professional creepshotters use."

    red @closedeyes angryeyebrows talking2mouth "Oh, gross."

    iono @angrybrow talking2mouth "Right? But don't worry. Now you've looped me into this, I'mma have my brand-new Rotee keep an eye on any infernal machines." 
    iono @talking2mouth "I'mma be like Big Brother--full surveillance state, literally 2004."

    narrator "You start to get a painful spiking situation somewhere in your head, a clear sign a conversation with Iono is starting to wrap up."

    red @happy "Right, well, thanks a ton! You'll be working with Ethan, then, and I know he'd love the chance to meet you."

    iono @confusedbrow talking2mouth "Ethan? Givin' off big NPC energy to--"

    show iono surprisedbrow talking2mouth with dis

    red @talking2mouth "Stop."

    pause 1.0

    iono sadbrow frownmouth @sadbrow talking2mouth "Er[ellipses] sorry. I[ellipses] I didn't mean it. I'm sure Ethan's a nice guy."

    red @talkingmouth "He is. And you'll get to know him yourself, soon."

    iono neutralbrow neutralmouth @talking2mouth "Alright. Um, thanks for the invite."

    red @happy "You're a friend. I'm inviting {i}all{/i} my friends."
    red @sad2eyes sadeyebrows talkingmouth "And maybe a few people I'd struggle to call friends, but you're in the former group."
    red @happy "Anyway, seeya. I'll text you time and place soon, alright?"

    $ BecomeContacted("Iono")

    iono @happy "Alrighty-o!"

    call EndBunnyRecruit(char) from _call_EndBunnyRecruit_19

    return

label NateBunnyRecruit(char):#Tech Support, Bunny
    red @talkingmouth "Hey, Nate. We're planning a party for Saturday. The theme is bunny suits."

    nate @talkingmouth "Cool, I'm in."

    pause 1.0

    red @talking2mouth "Uh, do you want to...?"

    nate @sadbrow talking2mouth "Oh, wait. Is it girls-only?"

    red @sadbrow talkingmouth "No, there'll be guys, but--"

    nate @happy "Then I'm in. Whatever the 'but' is, save it, because I'm in, anyway."

    pause 1.0

    red @talking2mouth "Well[ellipses] cool. Hope to see you there."

    nate @playfuleyes unamusedeyebrows talkingmouth "Hope to see {i}you{/i} there."
    nate @surprisedbrow talking2mouth "Oh, wait, just realized something."
    nate @talking2mouth "I imagine this bunny-suit themed party isn't exactly sanctioned by the school?"

    red @talking2mouth "Yeah. We're not going to go off-campus, or bring any booze, but we're not exactly respecting curfew, either."

    nate @talking2mouth "So[ellipses] people are going to need to go back to their dorms without being caught by security, or the cameras[ellipses]"
    nate @happy "Got it. I can handle that part. I, uh, know a guy."

    pause 1.0

    if (GetRelationshipRank("Nate") > 0):
        red @sadbrow talkingmouth "{size=30}Nate, I gotta ask[ellipses] is this part of the role? The 'Nate' you're playing?{/size}"

        nate @sadbrow talking2mouth "{size=30}You tell me. I want to do it, so I'm doing it. Maybe I {i}am{/i} Nate. Who knows, at this point?{/size}"

        red @happy "Well, whatever the case, I like this. Thanks."

        $ ValueChange("Nate", 1)

        nate @happy "Thank {i}you{/i} for the invite! It's fun to break the rules once in a while."
        nate @playfuleyes unamusedeyebrows talkingmouth "And the bunnies[ellipses] do {i}not{/i} hurt."

    else:
        red @happy "Thanks."

    red @happy "I'll text you time and place soon, alright?"

    nate @talkingmouth "Sure. Hey, are you excited about this party? You have, uh, high expectations that it'll turn out well?"

    pause 1.0

    red @confused "Yyyyes...?"

    nate @happy "So you're hop-ful that--"

    show nate surprisedbrow frownmouth with dis

    pause 0.1

    scene blank2 with splitfadefaster

    call EndBunnyRecruit(char) from _call_EndBunnyRecruit_20

    return

label SoniaBunnyRecruit(char):#Tech Support, Cooking
    show sonia surprisedbrow frownmouth with dis

    red @talkingmouth "Hey, Sonia. We're planning a party for Saturday. Uh, people'll be dressing in bunny suits."

    sonia -surprisedbrow -frownmouth @talkingmouth "Well, that's rather[ellipses] that's a bit much for me, I'm afraid."

    red @talkingmouth "Totally fine. We're also looking for some help with food, sewing, and logistics?"

    sonia @happy "Oh, brill. I can certainly help with that, then--if you'd have me?"

    red @happy "'Course. Help with {i}what{/i}, specifically?"

    sonia @talking2mouth "Well, you mentioned needing help with logistics--if you want someone to manage a database of who's coming, who's bringing what, who can provide transportation, and whatnot, I'm fairly adept at that."
    sonia @talkingmouth "A lot of work with my gran was just organizing the contributions of her aides. A lot of spreadsheets were involved... aheh."
    sonia @happy "You mentioned sewing, too, right? Am I right in understanding that the party organizers will be making these bunny outfits for the guests?"

    red @talkingmouth "Yeah. Can you help with that?"

    sonia @sadbrow talkingmouth "Well, I've no talent whatsoever when it comes to fabric work, myself, but I can match tailors up with guests."

    red @happy "Fantastic, thanks!"

    sonia @talking2mouth "As for cooking[ellipses] well, I make a rather decent curry. I'm sure I can help with that, too."

    red @sadbrow talkingmouth "Sonia, that's {i}amazing{/i}. Thank you so much! I can't believe you're doing all this for a party you're not going to."

    sonia @sadbrow talkingmouth "You may be unsurprised to hear that this is not an altogether unfamiliar situation for me."

    if (IsContacted("Sonia")):
        red @happy "Aw. Well, next time. I can't imagine there being {i}three{/i} bunny-themed parties happening this year. Can I text you later with more details?"
    
    else:
        red @happy "Aw. Well, next time. I can't imagine there being {i}three{/i} bunny-themed parties happening this year. I'll text you later with more details, if I can have your number?"

        $ BecomeContacted("Sonia")

    sonia @happy "Certainly. And, yes, three is very unlikely[ellipses]"

    pause 1.0

    sonia @surprisedbrow talking2mouth "Pardon, {i}three{/i}?"

    call EndBunnyRecruit(char) from _call_EndBunnyRecruit_21

    return

label CalemBunnyRecruit(char):#Tailoring
    if (timeOfDay == "Noon"):
        calem @talkingmouth "Now, let me hazard a guess. You're here to discuss Saturday's plans."

    else:
        calem @talkingmouth "Hello, [first_name]. I wondered when you might approach me."

    if (timeOfDay != "Evening"):
        red uniform @talkingmouth "Hm? Oh, you already know about the party?"
    else:
        red @talkingmouth "Hm? Oh, you already know about the party?"

    calem @talkingmouth "Yes. Brendan filled me in, in broad strokes."
    calem @talking2mouth "I assure you you would have no interest in seeing myself in a bunny suit, but I'm at your disposal when it comes to {i}making{/i} them."

    red @happy "Hey, thanks, man."

    calem @talking2mouth closedbrow "It's certainly alright. The thought of what happened to Leaf leaves an ill feeling in my stomach."
    calem @sadbrow talkingmouth "I remember clearly those first few weeks of school, and how she brought so many of us together[ellipses]"
    calem @talking2mouth "The same motivation that drives Brendan to help, I warrant."
    calem @sadbrow talkingmouth "On that theme, I should warn that my skill pales in comparison to him."

    red @sadbrow talkingmouth "We're making outfits for a handful of people that we'll use for one evening. They don't need to be {i}masterpieces{/i}."

    calem @talking2mouth "Should not the paint match the canvas?"

    red @surprisedbrow frownmouth lightblush "[ellipses]"

    calem @talkingmouth sadbrow "Pardon me. It's a Kalosian's instinct to flirt obscurely when the topic of art comes around."

    red @closedbrow talkingmouth "Nnnnot {i}complaining{/i}, per se..."

    calem @talking2mouth "In any case, I trust you will contact me with further details about how I can best play my part, yes?" 

    red @talkingmouth "Yeah, that's the plan."

    calem @happy "Splendid. I will await your instructions with bated breath and handfuls of thread."

    call EndBunnyRecruit(char) from _call_EndBunnyRecruit_22

    return

label DawnBunnyRecruit(char):#Tailoring
    if (timeOfDay == "Noon"):
        red @talkingmouth "Hey, Dawn-- while I've got you, we're having a party this Saturday. Uh, the theme is bunny suits."
    elif (timeOfDay == "Morning"):
        red uniform @talkingmouth "Hey, Dawn. We're having a party this Saturday. Uh, the theme is bunny suits."
    else:   
        red @talkingmouth "Hey, Dawn. We're having a party this Saturday. Uh, the theme is bunny suits."

    pause 1.0

    redmind @thonk "Hm. She's taking this better than I thought she would."

    dawn @talking2mouth "I promised myself when I saw you walk up to me that I wouldn't freak out, no matter what you said."

    red @happy "Well done!"

    dawn @talkingmouth sadbrow "Yeah. Yeah, that[ellipses] that[ellipses] {size=30}internally, I'm screaming.{/size}"
    dawn @talking2mouth "Why bunny suits?"

    red @closedbrow talking2mouth "Ah[ellipses] okay, it's not really a big thing, so don't spread it around, but Leaf went to a party a while back. She went in a bunny suit, but, uh she was the only one there dressed up. And it wasn't actually a party, either."

    dawn sadbrow frownmouth @talking2mouth "Oh. Oh, poor Leaf[ellipses] if that happened to me, I'd[ellipses] I'd actually just die, I think."

    red @talking2mouth "There was some more to it, but that's the gist. Anyway, we're throwing a {i}real{/i} party this weekend. Keeping the bunny theme, though."

    pause 1.0

    dawn @talking2mouth "I could[ellipses] make one."

    red @happy "Could you?"

    dawn @talkingmouth "I think so. I've never made a bunny suit before, but it should be a relatively simple pattern to follow, right?"
    dawn @talkingmouth "I've made repairs to my contest outfits before, like, um, if something tore when I was backstage[ellipses] I think I could probably follow a pattern."

    red @talkingmouth "That'd be {i}great{/i}. Thanks {i}so{/i} much."

    dawn -frownmouth @sadbrow talkingmouth "It's alright. Leaf[ellipses] she threw me the best birthday I've ever had. It's nice that she gets parties thrown for her, too."

    red @sadbrow talkingmouth "This {i}might{/i} be the first. But maybe the first of many? Depends on if this one isn't an absolute disaster, I guess."

    dawn @sad2eyes talkingmouth "If it helps[ellipses] I know firsthand that having an absolute disaster of a party doesn't mean that future ones won't be better."

    red @talkingmouth "Noted. Thanks, Dawn. I'll text you more details later."

    $ BecomeContacted("Dawn")

    dawn @talkingmouth "Alright. Um[ellipses] thanks for inviting me to be part of this."

    red @happy "Of course. Thanks for {i}being{/i} part of this. I'm sure it was out of your comfort zone, but I really appreciate you went for it, anyway."

    dawn @sad2eyes sadeyebrows talkingmouth "{size=30}I think my comfort zone is located somewhere in Orre. Wherever it is, I don't remember the last time I was {i}in{/i} it.{/size}"

    call EndBunnyRecruit(char) from _call_EndBunnyRecruit_23

    return

label HildaBunnyRecruit(char):#Tailoring, Cooking
    show hilda surprisedbrow frownmouth with dis

    red @talkingmouth "Hey. Have you heard about the party on Saturday? The theme is bunny suits."

    hilda @talking2mouth "Uh, why? Springsday was a while ago, wasn't it?"

    red @closedbrow talking2mouth "Kinda a long story, but the short of it is that we're trying to make Leaf feel better."

    hilda @talking2mouth "With bunny--"
    hilda -surprisedbrow -frownmouth @closedbrow talking2mouth "Okay, actually, that makes sense, yeah, that kinda shit would probably work for her."

    hilda @talking2mouth "Alright, tell me how I can help."

    red @talkingmouth "Well, you could attend--"

    hilda @sadbrow talkingmouth "No, the fuck I can't. I'm not wearing a bunny suit, and, anyway, that kind of party is {i}not{/i} my scene."

    red @closedbrow talking2mouth "Noted, offer withdrawn. Then we're looking for help with {i}making{/i} the bunny outfits, and cooking."

    hilda @happy "I figured you probably needed something like that. I'm already on it. You'll text me with time and place details as soon as you get something ironed out, right?"

    $ BecomeContacted("Hilda")

    red @talkingmouth "Sure will."

    hilda @talkingmouth "Great. Now, sorry, I gotta run. I've gotta get started on this {i}fast{/i} if we want it done by Saturday."

    hide hilda with dis

    redmind @closedbrow frownmouth "Damn, she was {i}way{/i} more excited about the idea of setting up the party than actually {i}going{/i} to it. Different strokes, I guess[ellipses]"

    call EndBunnyRecruit(char) from _call_EndBunnyRecruit_24

    return

label WhitneyBunnyRecruit(char):#Tailoring, Bunny
    show whitney surprisedbrow frownmouth with dis

    if (timeOfDay == "Morning"):
        red uniform @talkingmouth "Hey. The Dorm 25 guys and I are throwing a party on Saturday--"

    else:
        red @talkingmouth "Hey. The Dorm 25 guys and I are throwing a party on Saturday--"

    whitney -frownmouth talkingmouth "Yes."

    red @talking2mouth "And the theme is bunny suits--"

    whitney happymouth "Yes!"

    red @sweat unamusedbrow talking2mouth "And we'd appreciate some help making them for the other guests--"

    whitney happy "YES!"

    red @wince talking2mouth "So I'll text you later with more details...?"

    $ BecomeContacted("Whitney")

    whitney happy "{size=40}YEEEEEESSSSSS!!!!{/size}"

    show whitney with dis:
        xpos 0.5 ypos 1.2 zoom 1.3
        ease 0.5 xpos 0.45 ypos 1.0 zoom 1.0
        ease 0.2 xpos 1.2

    pause 2.0

    redmind @sadbrow "I'm not sure I'll ever love anything as much as Whitney loves the chance to put herself and other women in bunny suits. It's almost intimidating."

    call EndBunnyRecruit(char) from _call_EndBunnyRecruit_25

    return

label GardeniaBunnyRecruit(char):#Tailoring, Food
    if (timeOfDay == "Noon"):
        gardenia @talkingmouth "So? Don't hold out on me -- what's this 'higher purpose' of yours?"

        red uniform @talkingmouth "Believe it or not, it's inviting people to a party on Saturday. The theme is bunny suits."

    else:
        red @talkingmouth "Hey, Gardenia. We're planning a party for Saturday. The theme is bunny suits."

    gardenia @angrybrow talkingmouth "Ooh, sexy. How many guests will you have?"

    red @talking2mouth "Not sure. We're looking in the ballpark of twenty, though?"

    gardenia @talking2mouth "Okay. I could sell you twelve-packs of bunny suits--"

    red @sweat talking2mouth "Ah, sorry. We're actually handmaking the suits. We want people to be able to express themselves, so we're having custom suits made." 
    red @talkingmouth "We're matching tailors up with guests and going from there."

    gardenia @talking2mouth "Ah, alright. I know a bit of sewing, and I'm not busy on Saturday--maybe I could help?"

    red @sweat talkingmouth "Eh... how much will it cost?"

    gardenia @talkingmouth "Just a favor. And I'm owed so many of those, maybe I'll never get around to cashing {i}yours{/i}."
    gardenia @happy "Seriously, though, take my help. I know some guys who can provide food for the party, too. You've got cooks, probably? But it can't hurt to have some cheap mass-produced stuff to fill in the gaps."
    gardenia @talkingmouth "Promise I'm not going to try and make money off of this. I just want to help. Pay back a bit."
    gardenia @flirtbrow smirkmouth "{i}My{/i} profit is the chance to see a bunch of guys in bunny suits."

    red @talking2mouth "How'd you know there'd be guys there?"

    gardenia @talking2mouth "At any place where there are women in bunny suits, there will be men wearing 'em, too, to get closer to the women. That's Bunomics 101."

    red @talking2mouth "Fair point, though I think pretty much all of the men I've invited are {i}also{/i} there for the men."

    gardenia @happy "Seriously? What a time to be alive. In the world of business, it's only love that's free, but {i}boy is it.{/i}"

    red @happy "Ironic. I'd been told that sex sells."

    gardenia @talkingmouth happybrow "What do I always say? Information, food, and bodies. Those are the only three things you can sell, and sex is two of them, depending on how hungry you are."

    red @closedbrow talking2mouth "Could be all three, depending on how much experience you have."

    gardenia @flirtbrow smirkmouth "Enough to look for something new, but not enough that I'm bored of it, yet." 
    gardenia @happy "Wear something cute to the party--that might make the difference between me calling in my favors from the guys that work at that Kalosian Restaurant in Inspira, or calling in a grocery run to the Ball-Mart."

    red @closedbrow talking2mouth "I feel like I should object, but I gotta be honest, this won't be the most undignified thing I'm going to do to make this party work."

    gardenia @happybrow smirkmouth "That's the spirit! Keep digging, 'til you hit that bottom line!"

    call EndBunnyRecruit(char) from _call_EndBunnyRecruit_26

    return

label MayBunnyRecruit(char):#Food, Bunny, but only if you have enough Food
    if (timeOfDay == "Noon"):
        may @talkingmouth "By the way, Brendan told me about your party on Saturday! I'm in!"
    
    else:
        may @talkingmouth "Heya, [first_name]. Brendan already told me about the party, and I'm in!"
    
    if (timeOfDay != "Evening"):
        red uniform @happy "Great!"
    else:
        red @happy "Great!"

    may @talkingmouth "Oh, {i}but{/i}[ellipses] I'm not going to {i}attend{/i} the actual party. I'll probably be too busy in the kitchen."

    red @talking2mouth "Oh."
    red @talkingmouth "Well, okay. No pressure. Are you sure, though? We're planning to have a good few cooks--I'll be there, Blue'll be there[ellipses]"

    may @talking2mouth "Well[ellipses] if everything is handled, {i}maybe{/i} I'll think about it, but[ellipses]"

    may @happy "I kinda have to admit that the idea of wearing a bunny suit out in public is a little embarrassing. Thrilling? Kinda. But also kinda embarrassing."

    red @happy "Hey, it's alright. I get it. Like I said, no pressure. If you decide to join the party, that's great. If you decide to just stay in the kitchen, that's fine, too. Just let us know so we can make a suit for you."

    may @closedbrow talking2mouth "Oh, that[ellipses] either way, that won't be necessary."

    red @confused "Huh? Uh, sure. Alright."

    pause 1.0

    red @talkingmouth "Anyway, I'll text you some more details about the cooking side of things. Let me know what you decide regarding actually attending the party[ellipses]"
    red @happy "Or, uh, don't. I'll know what you decided when I see what you're wearing there, I guess."

    may @happy "You sure will! I'll keep an eye on my phone."

    red @talkingmouth "Right, thanks. Talk to you later."

    call EndBunnyRecruit(char) from _call_EndBunnyRecruit_27

    return

label NessaBunnyRecruit(char):#Bunny
    red @talkingmouth "Hey. Have you heard about the party on Saturday? The theme is bunny suits."

    nessa "[ellipses]"
    nessa @talkingmouth "{i}That{/i} wasn't on my bingo card."

    red @sweat closedbrow talkingmouth "We're all trying new things."

    pause 1.0

    nessa @sadbrow talkingmouth "Does this have something to do with[ellipses] what was her name? Leaf? The girl who showed up to our study group on Saturday?"

    red @talking2mouth "Yeah. We're trying to make her feel better."

    nessa @surprisedbrow talkingmouth "By putting her in the same situation she was in before, when {i}that{/i} happened?"

    red @sadbrow talkingmouth "By giving her the opportunity to attend the fun party she worked up the courage to attend in the first place."

    nessa "[ellipses]"

    pause 1.0

    nessa @talking2mouth "Alright. I wasn't going to go, but that's a good enough reason to do this. I'll attend." 
    nessa @talkingmouth "When do I need the suit by?"

    red @talkingmouth "Don't worry about that. We're hand-making all the suits. We'll match a tailor up with you, and they'll ask you what you want."

    pause 1.0

    nessa @talkingmouth "Actually[ellipses]" 
    extend @sadbrow talkingmouth " sounds kinda fun."

    nessa @talkingmouth "I've spent a lot of time dressing up and dressing down for money. Don't think I ever got to design the outfit, though."

    pause 0.5

    nessa @talkingmouth "Text me when you have more details about time and place, or who my tailor is."

    red @talkingmouth "Sure thing."

    nessa @closedbrow talking2mouth "Thanks."
    
    call EndBunnyRecruit(char) from _call_EndBunnyRecruit_28

    return

label RosaBunnyRecruit(char):#Bunny, but only if you have enough Tech Support
    show rosa surprisedbrow frownmouth with dis

    red @talkingmouth "Hey, Rosa. You might've heard, already, but we're planning a bunny suit party for Saturday evening. I know you've got all kinds of rules you need to follow, so if you can't, no pressure[ellipses]"
    red @happy "[ellipses]but if you can, that'd be great! Any interest?"

    pause 1.0

    rosa -surprisedbrow -frownmouth @sad2eyes talking2mouth "I[ellipses] don't think I can. It sounds {i}really{/i} fun, but[ellipses] there's a {i}lot{/i} of risks involved, you know?"

    red @sadbrow talkingmouth "Yeah, I get it. Although, we're taking security {i}really{/i} seriously, if that helps."

    rosa @talkingmouth "A little bit, but what do you mean by {i}really{/i} seriously?"

    if (HasEvent("Nate", "BunnyRecruit")):
        red @talking2mouth "Well, we've made sure that no-one will be recorded on the school's cameras, and security will be kept far away from the site."

    if (HasEvent("Iono", "BunnyRecruit")):
        red @talkingmouth "We're keeping an eye on any electric activity all around the party site, too. If anyone tries to bring a camera in, or fly a Rotom phone in the area, we'll know."

    if (HasEvent("Sonia", "BunnyRecruit")):
        red @happy "We've got a database of everyone who's attending, and all the people who are helping out, too, so if something weird happens, we can hold them accountable."
        red @talkingmouth "Sonia's the one running that database, actually--your roommate, right?"

    red @talking2mouth "The only rule we plan to break is curfew. There won't be any alcohol--we aren't going to do anything weird. Just bunny suits, and a fun, chill, time."
    red @talking2mouth "And, uh, it goes without saying that the Disciplinary Committee won't be a problem."

    pause 1.0

    if (HasEvent("Nate", "BunnyRecruit") + HasEvent("Iono", "BunnyRecruit") + HasEvent("Sonia", "BunnyRecruit") + min(1, GetRelationshipRank("Rosa") / 2.0) >= 3):
        rosa @sadbrow talkingmouth "Well[ellipses] alright. It sounds like you've actually thought this through pretty thoroughly."

        red @sadbrow talkingmouth "First party I've ever been a part of planning. Yellow actually deserves most of the credit here."
        red @happy "Anyway, that's great to hear! We'll see you there. And don't worry, if anything changes, or one of our security people has to drop out, I'll let you know beforehand."
        red @sadbrow talkingmouth "Everyone's going to go into this knowing {i}exactly{/i} what they're getting into. Promise."

        rosa @happy "Aw. Thanks so much for your support!"

    else:
        rosa @sadbrow talkingmouth "I'm[ellipses] sorry. I think it's probably still too risky."

        red @talkingmouth "Hey, it's alright. Tell you what--if I loop more people into this who can guarantee the security of the party, I'll text you about it. Does that sound alright?"

        rosa @closedbrow sweat talking2mouth "Actually[ellipses] the agency monitors my phone. How about you text one of my roommates?"
        
        if (IsContacted("Raihan")):
            $ AddEvent("Rosa","PromisedRaihanText")
            red @talkingmouth "Sure, I have Raihan's number."
        elif (IsContacted("Sonia")):
            $ AddEvent("Rosa","PromisedSoniaText")
            red @talkingmouth "Sure, I have Sonia's number."
        elif (IsContacted("Sabrina")):
            $ AddEvent("Rosa","PromisedSabrinaText")
            red @talkingmouth "Sure, I can just, uh, {i}think{/i} at Sabrina."
        elif (IsContacted("Nessa")):
            $ AddEvent("Rosa","PromisedNessaText")
            red @talkingmouth "Sure, I have Nessa's number."

        rosa @talkingmouth "Alright. Thank you!"
        rosa @sadbrow talkingmouth "I really {i}do{/i} want to go, but if it's too hard to get all this security stuff in place, then that's fine. I know it's a lot of trouble[ellipses]"

        red @happy "Nah, I totally get it. Well, I don't '{i}get{/i} it', but I get that your security's really important. We'll do what we can."

        rosa @happy "Aw. Thanks so much for your support!"

        hide rosa with dis

        pause 1.0

        narrator "[bluecolor]It seems Rosa may only be willing to attend the party if you can guarantee her security[ellipses]{/color}"

        $ RemoveEvent("Rosa", "BunnyRecruit")
        $ AddEvent("Rosa", "HalfBunnyRecruit")

    call EndBunnyRecruit(char) from _call_EndBunnyRecruit_29

    return

init python: 
    """
    Bea - Recruitment -> Nate
    Cheren - Recruitment -> Gardenia
    Skyla - Recruitment -> Gardenia
    Silver - Recruitment -> Gardenia
    Erika - Recruitment -> Hilda
    Flannery - Recruitment -> Whitney
    Grusha - Recruitment -> Whitney
    Hilbert - Recruitment -> Hilda
    Janine - Recruitment -> Sonia
    Jasmine - Recruitment -> Whitney
    Misty - Recruitment -> Dawn
    Raihan - Recruitment -> Nessa
    Kris - Recruitment -> Iono or Whitney, if Iono hasn't been unlocked.
    Sabrina - Recruitment -> Rosa
    Serena - Recruitment -> Calem
    Tia - Recruitment -> Bianca
    Bianca - Recruitment -> May
    Wally - Recruitment -> Dawn

    Iono - Tech Support
    Nate - Tech Support
    Sonia - Tech Support

    Brendan - Free - Tailoring
    Calem - Tailoring
    Dawn - Tailoring
    Hilda - Tailoring
    Whitney - Tailoring
    Yellow - Free - Tailoring
    Gardenia - Tailoring

    Gardenia x2 - Food
    May - Food
    Hilda x2 - Food
    Sonia x2 - Food
    Red - Free - Food
    Blue - Free - Food

    Ethan - Free - Attendee (Only attends if you have max Tailoring, as there was an extra outfit made for him.)
    Klara - Free - Attendee
    Leaf - Free - Attendee
    May x2 - Attendee (Only attends if you have max Food, as she has time to step away from the kitchen to enjoy the party. Mallow shows up, maybe?)
    Melody - Free - Attendee
    Natex2 - Attendee
    Nessa - Attendee
    Red x2 - Free - Attendee
    Whitney x2 - Attendee
    Rosa - Attendee (Only attends if you have at least three Tech Support, or two and at least two ranks with her. She needs to be entirely sure that no-one can record her, or see her there, or—anything, really.)
    """

label BunnyRecruitRecap:

python:
    addalso = True
    recruited = 0
    specialrecruited = 0
    lastchar = ""
    recruittypes = {}
    for char in persondex:
        if GetEventDatetime(char, "BunnyRecruit") == calDate:
            recruited += 1
            lastchar = char
            for key, value in bunnypartydex.items():
                if (char in value):
                    if (key != "Recruitment"):
                        specialrecruited += 1
                    if key in recruittypes:
                        recruittypes[key].append(char)
                    else:
                        recruittypes[key] = [char]
    recruitmentcount = (0 if "Recruitment" not in recruittypes else len(recruittypes["Recruitment"]))
    techcount = (0 if "Tech" not in recruittypes else len(recruittypes["Tech"]))
    bunnycount = (0 if "Bunny" not in recruittypes else len(recruittypes["Bunny"]))
    foodcount = (0 if "Food" not in recruittypes else len(recruittypes["Food"]))
    tailorcount = (0 if "Tailor" not in recruittypes else len(recruittypes["Tailor"]))

if (recruited != 1):
    red @talkingmouth "Yeah, I talked to [IntToWord(recruited)] people about it."
elif (recruited == 1):
    red @talkingmouth "Yeah, I talked to [lastchar] about it."
else:
    red @talkingmouth "Nope."

if (recruitmentcount > 0):
    if (recruitmentcount >= 2):
        red @talking2mouth "A [('few' if recruitmentcount >= 2 else 'couple')] people weren't able to come to the party, or help out, but they pointed me towards other people."
    else:
        $ solochar = recruittypes["Recruitment"][0]
        $ pronoun = "he" if persondex[solochar]["Sex"] == Genders.Male else "she"
        red @talking2mouth "[solochar] can't come, but [pronoun] pointed me towards someone else."
    $ addalso = True

if (techcount > 0):
    if (techcount >= 3):
        red @happy "[('Also, ' if addalso else '')]I got us a ton of help with logistics. Sonia's going to make a big database of all the guests and tailors, and match 'em up together."
        red @happy "If the cooks need something, then you can probably just shoot her a message and she'll assign someone to that, too."
        red @talkingmouth "Also, Nate's got some kind of influence over security, and the school's cameras, and he basically said that those just won't be a problem for us. He's going to be attending the party, too."
        red @closedbrow talkingmouth "And Iono's got some kind of gizmo--not really sure how it works--but it sounds like she can give us advanced warning if someone tries to crash the party, or spy on us."
        $ bunnycount -= 1
        $ recruittypes["Bunny"].remove("Nate")
        $ foodcount -= 1
        $ recruittypes["Food"].remove("Sonia")
    elif (techcount == 2):
        if ("Sonia" in recruittypes["Tech"] and "Nate" in recruittypes["Tech"]):
            red @talkingmouth "[('Also, ' if addalso else '')]I got us some help with logistics and security. Sonia's going to make a big database of all the guests and tailors, and match 'em up together."
            red @talkingmouth "If the cooks need something, then you can probably just shoot her a message and she'll assign someone to that, too."
            red @closedbrow talkingmouth "Also, Nate's got some kind of influence over security, and the school's cameras, and he basically said that those just won't be a problem for us. He's going to be attending the party, too."
            $ bunnycount -= 1
            $ recruittypes["Bunny"].remove("Nate")
            $ foodcount -= 1
            $ recruittypes["Food"].remove("Sonia")
        elif ("Sonia" in recruittypes["Tech"] and "Iono" in recruittypes["Tech"]):
            red @talkingmouth "[('Also, ' if addalso else '')]I got us some help with logistics and security. Sonia's going to make a big database of all the guests and tailors, and match 'em up together."
            red @talkingmouth "If the cooks need something, then you can probably just shoot her a message and she'll assign someone to that, too."
            red @closedbrow talkingmouth "Also, Iono's got some kind of gizmo--not really sure how it works--but it sounds like she can give us advanced warning if someone tries to crash the party, or spy on us."
            $ foodcount -= 1
            $ recruittypes["Food"].remove("Sonia")
        else:
            red @talkingmouth "[('Also, ' if addalso else '')]I got two people who can help with security. Nate's got some kind of influence over security, and the school's cameras, and he basically said that those just won't be a problem for us. He'll be attending the party, too."
            red @closedbrow talkingmouth "Also, Iono's got some kind of gizmo--not really sure how it works--but it sounds like she can give us advanced warning if someone tries to crash the party, or spy on us."
            $ bunnycount -= 1
            $ recruittypes["Bunny"].remove("Nate")
    else:
        $ solochar = recruittypes["Tech"][0]
        $ pronoun = "he" if persondex[solochar]["Sex"] == Genders.Male else "she"
        red @talking2mouth "[('Also, ' if addalso else '')]I talked to [solochar]. [pronoun.title()] said [pronoun] can help."
        if (solochar == "Sonia"):
            red @happy "She's going to make a big database of all the guests and tailors, and match 'em up together. And if the cooks need something, then you can probably just shoot her a message and she'll assign someone to that, too."
            red @talkingmouth "She also said she'll help out with the food, so don't scare her off, Blue!"
            $ foodcount -= 1
            $ recruittypes["Food"].remove("Sonia")
        elif (solochar == "Nate"):
            red @happy "He's got some influence over security. Didn't specify what, but basically they won't be a problem--and neither will the school's cameras."
            red @talkingmouth "And he'll come to the party, too, so that's another bunny."
            $ bunnycount -= 1
            $ recruittypes["Bunny"].remove("Nate")
        elif (solochar == "Iono"):
            red @talking2mouth "She's got some kind of gizmo--not really sure how it works--but it sounds like she can give us advanced warning if someone tries to crash the party, or spy on us."

    $ addalso = True

if (tailorcount > 0):
    if (tailorcount >= 2):
        if (HasEvent("Sonia", "BunnyRecruit")):
            red @talkingmouth "[('Oh, that reminds me. ' if addalso else '')]A [('few' if tailorcount >= 2 else 'couple')] people said they'd be able to help make outfits. Sonia'll get in contact with them--ask her for their names and schedules, Yellow. They'll follow your lead."
        else:
            red @talkingmouth "[('Oh, that reminds me. ' if addalso else '')]A [('few' if tailorcount >= 2 else 'couple')] people said they'd be able to help make outfits. I'll start a group chat with them and you, Yellow."

    else:
        $ solochar = recruittypes["Tailor"][0]
        $ pronoun = "he" if persondex[solochar]["Sex"] == Genders.Male else "she"
        red @talkingmouth "[('Oh, that reminds me. ' if addalso else '')]I talked to [solochar]. [pronoun.title()] said [pronoun] can help with the tailoring."
        if (solochar == "Whitney"):
            red @talkingmouth "She, uh, also seemed {i}very{/i} enthusiastic about attending the party."
            $ bunnycount -= 1
            $ recruittypes["Bunny"].remove("Whitney")
        elif (solochar == "Gardenia"):
            red @talkingmouth "She's also got us a hook-up for the food. Sounds like we won't even have to pay for it."
            $ foodcount -= 1
            $ recruittypes["Food"].remove("Gardenia")
    $ addalso = True

if (foodcount > 0):
    if (foodcount >= 2):
        if (HasEvent("Sonia", "BunnyRecruit")):
            red @talkingmouth "[('On the food side of things, a' if addalso else 'a')] [('few' if foodcount >= 2 else 'couple')] people said they could help with the cooking. Sonia's already on top of it."
        else:
            red @happy "[('On the food side of things, a' if addalso else 'a')] [('few' if foodcount >= 2 else 'couple')] people said they'd be able to help with the cooking. Of course, I didn't tell them they'd be reporting to you, Blue."

    else:
        $ solochar = recruittypes["Food"][0]
        $ pronoun = "he" if persondex[solochar]["Sex"] == Genders.Male else "she"
        red @talkingmouth "[('On the food side of things, ' if addalso else '')]I talked to [solochar]. [pronoun.title()] said [pronoun] can help with that."
        if (solochar == "May"):
            red @talkingmouth "She said she'd like to attend the party--as long as she wasn't too busy in the kitchen, anyway."
            $ bunnycount -= 1
            $ recruittypes["Bunny"].remove("May")
    $ addalso = True

if (bunnycount > 0):
    if (bunnycount >= 2):
        red @happy "[('Finally, ' if addalso else '')]I got a [('few' if bunnycount >= 2 else 'couple')] people who said they'd be able to come to the party. So we'll have guests, at least!"

    else:
        $ solochar = recruittypes["Bunny"][0]
        $ pronoun = "he" if persondex[solochar]["Sex"] == Genders.Male else "she"
        red @talkingmouth "[('Finally, ' if addalso else '')]I talked to [solochar]. [pronoun.title()]'s coming to the party, and will be bunny-suited! We just gotta find the right tailor, now."
    $ addalso = True

$ totalrecruits = bp2ebfood() + bp2ebtech() + bp2ebcloth() + bp2ebparty()# 9 - 17

if (totalrecruits <= 11):
    if (specialrecruited >= 5):
        yellow @happy "That's really fantastic!"

        blue @closedbrow "Glad to see you're taking your job seriously, after all."

    elif (specialrecruited >= 3):
        yellow @talkingmouth "That's great! We're going at a good pace, I think."

        blue @talking2mouth "Could be faster, but whatever. I guess it's alright."

    elif (specialrecruited >= 1):
        yellow @closedbrow talking2mouth "[ellipses]Okay. That's a bit concerning--we might need to speed things up, if we can."

        blue @glancebrow talking2mouth "Don't tell me {i}I'll{/i} have to go out and invite people to the party[ellipses]"

        yellow @sadbrow talkingmouth "N-no, you {i}definitely{/i} don't need to do that."

    else:
        narrator "Yellow and Blue stare at you as though expecting you to say something more. Ethan coughs, and everyone decides to move on."

elif (totalrecruits < 14):
    if (specialrecruited >= 5):
        yellow @happy "That's really fantastic!"

        blue @closedbrow "Glad to see you're taking your job seriously, after all."

    elif (specialrecruited >= 3):
        yellow @talkingmouth "That's great! We're going at a good pace, I think."

        blue @talking2mouth "We've already got a bunch. Probably won't run out of time."

    elif (specialrecruited >= 1):
        yellow @closedbrow talking2mouth "Okay. We already have a fair number of people invited, so I think having a 'down day' is fine."

        blue @glancebrow talking2mouth "Don't tell me {i}I'll{/i} have to go out and invite people to the party[ellipses]"

        yellow @sadbrow talkingmouth "N-no, you {i}definitely{/i} don't need to do that."

    else:
        narrator "Yellow and Blue stare at you as though expecting you to say something more. Ethan coughs, and everyone decides to move on."

elif (totalrecruits < 17):
    if (specialrecruited >= 5):
        yellow @happy "That's really fantastic!"

        blue @closedbrow "Glad to see you're taking your job seriously, after all."

    elif (specialrecruited >= 3):
        yellow @talkingmouth "That's great! I think we almost have everyone we need now, right?"

        blue @talking2mouth "What a surprise. You didn't screw it up."

    elif (specialrecruited >= 1):
        yellow @closedbrow talkingmouth "Great. I think we almost have everyone we need now, right?"

        blue @glancebrow talking2mouth "Just don't use that as an excuse to slack off."

    else:
        narrator "Everyone seems satisfied with your recruiting efforts."
else:
    blue @talking2mouth "Yeah, yeah, you've got everyone we need already. We know."

return