init python:
    def GetGymClassCandidates():
        global week10gymbattles
        
        candidates = []

        if ('week10gymbattles' not in globals()):
            week10gymbattles = []

        for key, value in persondex.items():
            if (key not in week10gymbattles 
                and value["Role"] == "Student" 
                and IsNamed(key) 
                and value["Nature"] != TrainerNature.Special
                and IsPresent(key) 
                and GetTrainerTeam(key) != None 
                and key != "Klara"):
                candidates.append(key)
            elif (not (value["Role"] != "Student" or not IsNamed(key) or value["Nature"] == TrainerNature.Special or not IsPresent(key)) and GetTrainerTeam(key) == None):
                prnt(key, "omitted because they have no trainerteams entry")
        
        if (GetSeenClassScenes("Bug") >= 10 and "Bugsy" not in week10gymbattles):
            candidates.append("Bugsy")
        if (GetSeenClassScenes("Psychic") >= 10 and "Morty" not in week10gymbattles):
            candidates.append("Morty")
        
        return candidates

    def pick_opponent_make_type_composite(char, right):
        types = []
        color = "#111"
        if char:
            if char == "Morty":
                types = ["Psychic", "Ghost"]
            elif char == "Bugsy":
                types = ["Bug"]
            else:
                types = GetCharTypes(char) if char.lower() != "red" else [GetStatRank(0), GetStatRank(1), GetStatRank(2)]

            color = GetCharColor(char)
        
        type_disps = []
        if types:
            type_width = (config.screen_width // 2) // len(types) # Allows for an arbitrary number of types.
            for i in range(len(types)):
                if right:
                    if i == 0: # Lopside everything to the right - long first section.
                        type_disps += [(0, 0), Crop((0, 0, config.screen_width // 2 + type_width, config.screen_height // 2), "GUI/bg_tiles/bg_tile_" + types[i] + "_full.webp")]
                    else:
                        type_disps += [(config.screen_width // 2 + i * type_width, 0), Crop(((config.screen_width // 2 + i * type_width) % 135, 0, type_width, config.screen_height // 2), "GUI/bg_tiles/bg_tile_" + types[i] + "_full.webp")]
                else:
                    if i == len(types) - 1: # Lopside everything to the left - long last section.
                        type_disps += [(i * type_width, 0), Crop(((i * type_width) % 135, 0, config.screen_width // 2 + i * type_width, config.screen_height // 2), "GUI/bg_tiles/bg_tile_" + types[i] + "_full.webp")]
                    else:
                        type_disps += [(i * type_width, 0), Crop(((i * type_width) % 135, 0, type_width, config.screen_height // 2), "GUI/bg_tiles/bg_tile_" + types[i] + "_full.webp")]
        
        else: # No character is set.
            type_disps += [(0, 0), Crop((0, 0, config.screen_width, config.screen_height // 2), "GUI/bg_tiles/bg_tile_unknown_full.webp")]
        
        if right:
            if (char == "Iono"):
                type_disps += [(0, 0), AlphaMask(GradientDisplayable(["#EE8FB5", "#1d8fc5"], center=(0.25, 0.5), kind="linear"), "GUI/pick_opponent/halftype_overlay.webp")]
            else:
                type_disps += [(0, 0), Transform("GUI/pick_opponent/halftype_overlay.webp", matrixcolor=TintMatrix(color))]
        else: # Since the images have a cut-off chevron on the right, we have to offset a bit when lopsiding to the left. This saves the space of another, near-identical image.
            type_disps += [(-30, 0), Transform("GUI/pick_opponent/halftype_overlay.webp", matrixcolor=TintMatrix(color), xzoom=-1)]
            type_disps += [(config.screen_width - 30, 0), Solid(color, xsize=30, ysize=config.screen_height // 2)]

        d = Composite((config.screen_width, config.screen_height // 2), *type_disps)
        return d

transform pick_opponent_trans(shown_xpos):
    on replace: # No show, as the transform won't be played on anything visible on show.
        xpos shown_xpos + 0.1 alpha 0.0
        linear 0.5 xpos shown_xpos alpha 1.0
    on replaced: # No hide, as that also triggers on returning of the screen
        xpos shown_xpos alpha 1.0
        linear 0.5 xpos shown_xpos - 0.1 alpha 0.0

screen pick_opponent(custom_outfits=["uniform", "uniform"], candidate_function=GetGymClassCandidates):
    modal True
    zorder 1 # 1 higher than lower_pick_opponent

    default candidates = candidate_function()
    default chosen_candidate = None
    default chibi_count = 8
    default pick_page = 0
    default red_bg = pick_opponent_make_type_composite("Red", False)

    # Setting _dismiss_pause to False ensures rapid clicking can't accidentally skip the transition.
    on "show" action [SetVariable("_dismiss_pause", False), ShowTransient("lower_pick_opponent", chosen_candidate=None, custom_outfit=None)]
    on "hide" action SetVariable("_dismiss_pause", True)

    frame:
        ypos 0.0
        ysize config.screen_height // 2
        background red_bg
        xfill True
        yfill True

        viewport:
            add GetCharacterSprite("Red", 1, custom_outfits[0] == "uniform", (custom_outfits[0] if custom_outfits and custom_outfits[0] != "uniform" else "") + " angrybrow happymouth"):
                ypos 1.7
                xpos 0.13
                zoom 0.98
                matrixcolor TintMatrix("#000")
            
            add GetCharacterSprite("Red", 1, custom_outfits[0] == "uniform", (custom_outfits[0] if custom_outfits and custom_outfits[0] != "uniform" else "") + " angrybrow happymouth"):
                ypos 1.7
                xpos 0.15
        
        frame:
            background Frame("GUI/frame_pbattlestat.webp", 10, 32)
            xycenter (0.75, 0.3)
            xysize (610, 132) # (600 + xoffset, 100 + yoffset)
            
            grid 6 1:
                xycenter (0.5, 0.5)
                for i in range(6):
                    add "GFX/pokeball.webp" xysize (100, 100) matrixcolor (IdentityMatrix() if i < len(playerparty) else SaturationMatrix(0.0))
    
    if chosen_candidate:
        imagebutton:
            idle "GUI/pick_opponent/pick_opponent_confirm.webp"
            hover Transform("GUI/pick_opponent/pick_opponent_confirm.webp", matrixcolor=BrightnessMatrix(0.1))
            action ([With(Dissolve(1.0)), Return(chosen_candidate)] if chosen_candidate else None)
            focus_mask True
            align (0.5, 1.0)
            yoffset -30
    transform:
        rotate -5
        subpixel True
        frame:
            padding (0, 0)
            xycenter (0.5, 0.5)
            ysize 200
            xsize config.screen_width + 30
            background "#333"
            xfill True
            yfill True

            hbox:
                xcenter 0.5

                imagebutton:
                    idle "GUI/pick_opponent/pick_opponent_page_prev_idle.webp"
                    hover Transform("GUI/pick_opponent/pick_opponent_page_prev_idle.webp", matrixcolor=BrightnessMatrix(0.1))
                    action CycleScreenVariable("pick_page", range(len(candidates) // chibi_count + bool(len(candidates) % chibi_count)), reverse=True) # `req. pages - 1` if candidates % chibi_count != 0, `req. pages` otherwise
                    keysym "viewport_leftarrow"
                    xysize (72, 200) # For trapezoid

                for i in range(chibi_count // 2):
                    if pick_page * chibi_count + i < len(candidates):
                        imagebutton:
                            xysize (180, 200)
                            insensitive Transform(GetChibi(candidates[pick_page * chibi_count + i]), ysize=150, fit="contain", xycenter=(0.5, 0.5), matrixcolor=SaturationMatrix(0.0))
                            idle Transform(GetChibi(candidates[pick_page * chibi_count + i]), ysize=150, fit="contain", xycenter=(0.5, 0.5), matrixcolor=IdentityMatrix())
                            hover Transform(GetChibi(candidates[pick_page * chibi_count + i]), ysize=150, fit="contain", xycenter=(0.5, 0.5), matrixcolor=BrightnessMatrix(0.1))
                            action [ShowTransient("lower_pick_opponent", Dissolve(0.5), candidates[pick_page * chibi_count + i], custom_outfits[1]), SetScreenVariable("chosen_candidate", candidates[pick_page * chibi_count + i])]
                            focus_mask True
                            sensitive chosen_candidate != candidates[pick_page * chibi_count + i]

                    else:
                        null width 180 height 200
                
                null width 360 height 200

                for i in range(chibi_count // 2, chibi_count):
                    if pick_page * chibi_count + i < len(candidates):
                        imagebutton:
                            xysize (180, 200)
                            insensitive Transform(GetChibi(candidates[pick_page * chibi_count + i]), ysize=150, fit="contain", xycenter=(0.5, 0.5), matrixcolor=SaturationMatrix(0.0))
                            idle Transform(GetChibi(candidates[pick_page * chibi_count + i]), ysize=150, fit="contain", xycenter=(0.5, 0.5), matrixcolor=IdentityMatrix())
                            hover Transform(GetChibi(candidates[pick_page * chibi_count + i]), ysize=150, fit="contain", xycenter=(0.5, 0.5), matrixcolor=BrightnessMatrix(0.1))
                            action [ShowTransient("lower_pick_opponent", Dissolve(0.5), candidates[pick_page * chibi_count + i], custom_outfits[1]), SetScreenVariable("chosen_candidate", candidates[pick_page * chibi_count + i])]
                            focus_mask True
                            sensitive chosen_candidate != candidates[pick_page * chibi_count + i]
                    else:
                        null width 180 height 200

                imagebutton:
                    idle "GUI/pick_opponent/pick_opponent_page_next_idle.webp"
                    hover Transform("GUI/pick_opponent/pick_opponent_page_next_idle.webp", matrixcolor=BrightnessMatrix(0.1))
                    action CycleScreenVariable("pick_page", range(len(candidates) // chibi_count + bool(len(candidates) % chibi_count))) # `req. pages - 1` if candidates % chibi_count != 0, `req. pages` otherwise
                    keysym "viewport_rightarrow"
                    xysize (72, 200)

    add "GUI/versus.webp" xycenter (0.5, 0.5) xsize 350 fit "contain"
   
screen lower_pick_opponent(chosen_candidate, custom_outfit):
    modal True

    default chosen_bg = pick_opponent_make_type_composite(chosen_candidate, True)

    add chosen_bg:
        ypos 0.5
        yanchor 0.0
    
    if chosen_candidate:
        frame:
            background Frame("GUI/frame_pbattlestat.webp", 10, 32)
            xycenter (0.25, 0.8)
            xysize (610, 132) # (600 + xoffset, 100 + yoffset)
            grid 6 1:
                xycenter (0.5, 0.5)
                for i in range(6):
                    add "GFX/pokeball.webp" xysize (100, 100) matrixcolor (IdentityMatrix() if i < len(GetTrainerTeam(chosen_candidate)) else SaturationMatrix(0.0))
        
        if (chosen_candidate != "Iono"):
            text chosen_candidate:
                size 80
                color GetCharColor(chosen_candidate)
                outlines [(absolute(10), "#000", absolute(0), absolute(0))]
                xycenter (0.25, position(-85, 0.8))
    
        else:
            text "{gradient=#EE8FB5-#1d8fc5}Iono{/gradient}":
                size 80
                outlines [(absolute(10), "#000", absolute(0), absolute(0))]
                xycenter (0.25, position(-85, 0.8))
    
    add (GetCharacterSprite(chosen_candidate, 1, custom_outfit == "uniform", (custom_outfit if custom_outfit and custom_outfit != "uniform" else "") + " angrybrow happymouth") if chosen_candidate else None):
        ypos 1.3
        zoom 0.98
        matrixcolor TintMatrix("#000")
        at pick_opponent_trans(0.87)

    add (GetCharacterSprite(chosen_candidate, 1, custom_outfit == "uniform", (custom_outfit if custom_outfit and custom_outfit != "uniform" else "") + " angrybrow happymouth") if chosen_candidate else None):
        ypos 1.3
        at pick_opponent_trans(0.85)
            

label pickgympartner:

"Who do you want to battle?"

call screen pick_opponent() with Dissolve(1.0)

$ battlechar = _return

$ renpy.show(GetCharacterSprite(battlechar, None, True))

"You want to battle [battlechar]?"

menu:
    "Yes.":
        $ week10gymbattles.append(battlechar)
        
        call Week10GymDialogs(battlechar) from _call_Week10GymDialogs

        return battlechar

    "No.":
        $ renpy.hide(battlechar.lower())

        jump pickgympartner

label Week10GymDialogs(character):
if (character == "Bea"):
    bea uniform @talking2mouth "[first_name]. Battle me."
    red uniform @surprisedeyebrows surprisedeyes talking2mouth "Whoa. You could at least take me out for dinner first."
    bea @talkingmouth "I fail to see how one can have dinner before lunch."
    red @sadeyebrows talkingmouth "You know what, Bea? Never mind. Let's do this."

elif (character == "Bianca"):
    bianca uniform @happy "Oh! You really {i}did{/i} pick me--I'll have to tell Professor Fennel!"
    red uniform @confused "Okay, you've lost me. What does Professor Fennel have to do with gym class?"
    bianca @surprisedeyebrows talking2mouth "Well, last night I dreamed that we had a battle. Persistently accurate dreams can be a sign of psionic abilities!"
    red @surprisedeyebrows talking2mouth "Whoa! So, who won in your dream?"
    bianca @happy "I did, using a giant floofy dragon that spit out blue fire!!"
    red @unamusedeyebrows talking2mouth "Right. If one of those shows up, you'd better get checked out by Instructor Will."

elif (character == "Blue"):
    blue uniform @angryeyebrows talkingmouth "Alright, {i}yes{/i}."
    blue @talking2mouth "This 'all cooking, no training' plan is hitting my Pokémon like a fat load of Kelpsy berries. They could use a punching bag."
    red uniform @angryeyebrows talkingmouth "Careful, buddy. This punching bag strikes back harder than a Wobbuffet."
    red @closedbrow sweat talking2mouth "[ellipses]{i}Boy{/i} that sounded cooler in my head."

elif (character == "Brendan"):
    brendan uniform @happy "Bro! It's been a while since we've had the chance to rumble!"
    if (IsCoordinator() and not HasEvent("Game", "Contest2")):
        brendan @talkingmouth "Couldn't wait for the Millennium Drop?"
        red uniform @talkingmouth "Never was the patient type."
        brendan @talkingmouth "Well, that's fine by me. No pain, no gains!"
    elif (IsCoordinator() and HasEvent("Game", "Contest2")):
        brendan @sadbrow talkingmouth "Bummed we won't get a {i}real{/i} chance in the Millennium Drop?"
        red uniform @sadbrow talkingmouth "Yeah. You'd have been one hell of a rival."
        brendan @talkingmouth "Hey, it's water under the bridge. Let's get you in top shape, so you can stick it to Phobos for both of us!"
    else:
        brendan @talkingmouth "Don't get it twisted: I haven't forgotten how to battle just 'cause the Millennium Drop is around the corner!"
        red uniform @talkingmouth "Never dreamed you would. Let's go!"

elif (character == "Bugsy"):
    bugsy uniform @surprised "Whoaaaa!!"
    bugsy @happy "I just realized--this is our first battle! That's totally momentous! We should have a special challenge to make this extra-super-unforgettable!"
    red uniform @sadbrow talkingmouth "And--let me get this straight--you {i}only{/i} train Bug-types? Nothing else?"
    bugsy @happy "Um, yeah? I didn't name myself 'Rocky' or 'Ghosty!'"
    red @confused "Don't you think that makes you a little predictable?"
    bugsy @angrybrow talkingmouth "Oh, ye of little faith! That settles it. We're definitely doing a special challenge!"
    if (getRWDay(0) != "Friday"):
        bugsy @happy "If you win, I'll declare your Pikachu an honorary Bug-type! If I win, I better see you in Burgh's class next week!"

    else:
        bugsy @happy "If you win, I'll declare your Pikachu an honorary Bug-type! If I win, I better see you in Burgh's class tomorrow!"

elif (character == "Calem"):
    calem uniform @talkingmouth "I must say, there's something pleasantly anarchic about choosing one's own opponents."
    calem @talkingmouth "Endless opportunities lie before me: to connect with classmates to whom I've never spoken, and to experience battling styles from half a dozen regions."
    if IsDate(7, 6, 2004) or (week10gymbattles[-2] == "Serena" and not IsDate(11, 6, 2004)):
        red uniform @talkingmouth "So, who are you picking tomorrow?"
    elif (week10gymbattles[-2] == "Serena" and IsDate(11, 6, 2004)):
        red uniform "So, who'd you pick on Monday?"
    else:
        red uniform @talkingmouth "So, who'd you pick yesterday?"
    calem @closedbrow talking2mouth "{size=30}[ellipses]Serena.{/size}"

elif (character == "Cheren"):
    cheren uniform @closedbrow talking2mouth "[first_name]."
    cheren uniform @sadbrow talking2mouth "I suppose that, were I to point out how petty this looks, you'd profess no idea what I'm talking about."
    red uniform @angrybrow talking2mouth "Is it that hard to believe I just wanted to talk to you about something?"
    cheren uniform @angrybrow talking2mouth "Talk with your Pokémon."

elif (character == "Dawn"):
    red uniform @talkingmouth "Hey there, rival. Looks like we meet again."
    dawn uniform @apprehensiveeyebrows sadeyes talkingmouth "{size=30}Not so loud[ellipses]{/size} Whenever you call me that, Blue yells at me until Yellow drags him away."
    red @playfuleyebrows talkingmouth "Just remind him how your last battle went."
    dawn uniform @sad "But then he'll challenge me again[ellipses]"
    red @playfuleyebrows talkingmouth "Right now {i}I'm{/i} challenging you. Unless you wanna chicken out."
    dawn @angryeyebrows talkingmouth "Not a chance, {size=30}rival!{/size}! I hope you're ready!"

elif (character == "Erika"):
    erika uniform @talkingmouth "So you've thrown down your gauntlet. As a member of the Battle Team, I am honor-bound to take it up."
    if GetRelationshipRank("Erika") == 0 and HasEvent("Erika", "RejectApology"):
        red uniform @unamusedeyebrows unamusedeyes talking2mouth "As a {i}fellow{/i} member of the Battle Team, I'm not going to go easy on you. Bring it."
    else:
        red uniform @happy "Nice to see you too, Erika! Nice weather, huh? Enjoying our newfound freedom of choice? Got a new page-turner to recommend?"
        
        show erika surprisedbrow frownmouth with dis
        
        pause 2.0
        
        red uniform @unamusedbrow talkingmouth "Nothing? Gotcha. We can save the pleasantries for {i}after{/i} I kick your butt."
        erika @angryeyebrows talkingmouth "{i}En garde!{/i}"

elif (character == "Ethan"):
    ethan uniform @sadeyebrows talking2mouth "Dude, you know {i}I'm{/i} coming to the party. What's the point of picking me?"
    show ethan uniform surprised with dis
    red uniform @happyeyebrows happyeyes talkingmouth "How about 'you're my best friend and I wanna hang out with you?'"
    pause 1.0

    python:
        highestbond = "Leaf"
        highestbondvalue = GetCharValue("Leaf")
        for char in persondex.keys():
            val = GetCharValue(char)

            if (val > highestbondvalue and char != "Ethan"):
                highestbond = char
                highestbondvalue = val

    ethan -surprised @sadeyebrows talkingmouth "You had me there for a minute. Then I remembered that [highestbond] exists."
    ethan @happy "Thanks for lying, though. I needed that kick of dopamine."

elif (character == "Flannery"):
    red uniform @talkingmouth "Not pairing up with Whitney today?"
    flannery uniform @talkingmouth "Our Pokémon know each other too well. Half the time they just play around instead of battling."
    flannery @angrybrow talkingmouth "You and Leaf better watch out, too. Your Pikachu does a lot of fraternizing with the enemy."
    $ renpy.music.play("Audio/Pokemon/pikachu_happy2.ogg", channel="altcry", loop=None)
    libpikachu happy "Pika!"
    red @happy "He says 'guilty as charged.'"

elif (character == "Gardenia"):
    gardenia uniform @talkingmouth "[first_name]! Just the man I wanted to see! I've got a business proposition for you."
    red uniform @unamusedbrow talking2mouth "I'm not fixing any matches, no matter how much you pay me."
    gardenia @surprisedbrow talking2mouth "Match-fixing?! What do you take me for?"
    gardenia @talkingmouth "I'm talking about match-{i}making{/i}. You're a famous face around campus. I could advertise an open challenge {size=30}for a very reasonable commission{/size} and we'd make a killing on tickets."
    red @sadeyebrows talkingmouth "Sorry, Gardenia. This week I'm battling for a higher purpose."
    gardenia @flirtbrow talkingmouth "Oh? Color me intrigued."

elif (character == "Grusha"):
    grusha uniform "{i}Oye.{/i} Today, let's {i}not{/i} take it easy."
    red uniform @surprisedbrow talking2mouth "What's got you fired up?"
    grusha angryeyebrows angryeyes "The {i}pendejo{/i} taking over the Coordinators' Club."
    red @sadeyebrows sadeyes talking2mouth "Oh, no. What did he say?"
    grusha @angryeyebrows angryeyes "To me? Nothing. To Jasmine, {i}no sé{/i}. She won't tell me, which tells me more than enough."
    grusha @angryeyebrows talking2mouth "I'd rather cool off here than leave the Millennium Drop on a stretcher."
    red @angryeyebrows talkingmouth "Fair enough. Let's do this."

elif (character == "Hilbert"):
    hilbert uniform @talking2mouth "[first_name]. Good."
    if IsBefore(8, 6, 2004):
        hilbert @closedbrow talking2mouth "Without Professor Rowan, I fear the level of challenge in this class will drop significantly."
    else:
        hilbert @closedbrow talking2mouth "Since Professor Rowan left us, the level of challenge in this class has dropped significantly."
    red uniform @surprisedbrow talking2mouth "Wait, are you saying you miss Rowan?"
    hilbert @talking2mouth "I meant exactly what I said. And I wonder, had Professors Cherry and Rowan taught us the full year, how much stronger I would be."
    hilbert @closedbrow talking2mouth "For now, you'll have to do."

elif (character == "Hilda"):
    hilda uniform @angrybrow blush talking2mouth "[first_name]--there you are! Please tell me you don't have a partner yet."
    red uniform @surprisedbrow talking2mouth "Nope: free as a Delibird. What's the matter?"
    hilda @angrybrow talkingmouth "Because {i}Hilbert{/i} just turned {i}me{/i} down. Can you believe that shit?"
    hilda @closedbrow angrymouth "I was just trying to do him a favor, but no! Mr. Battle Team has 'nothing to learn' from training with me!"
    hilda @blush talking2mouth "Anyway, I told him I already had a partner, so[ellipses]"
    red @playfuleyebrows talkingmouth "So you need an accomplice to cover up your lie."
    hilda @angry "It's not a {i}lie{/i}! It just wasn't true {i}yet{/i}!"

elif (character == "Iono"):
    red uniform @talkingmouth "You know, Terastallization is cool and everything, but[ellipses]"
    if (GetRelationshipRank("Iono") == 0):#not actually possible to see this...?
        red uniform @confused "If you need an Electric-type with Ghost attacks, couldn't you just catch a Rotom?"
    else:
        red uniform @confused "If you need an Electric-type with Ghost attacks, couldn't you just use Rotee?"

    iono uniform @surprised "¿QUÉ? QUOI? NANI?!"
    iono uniform @angry "It sounds to me like you wanna fight, friendo! I'll take you down like a DDOS!"
    redmind @thonk "Is Lt. Surge rubbing off on her already?"

elif (character == "Jasmine"):
    red uniform @happy "Hey, Jasmine! Glad to have Alder back this week?"
    jasmine uniform @talking2mouth "Hmm[ellipses] I suppose so, for the most part."
    red @surprisedbrow talking2mouth "Huh--I thought you, of all people, would be happier! 'Lift up everybody, not just the strong' was your whole Student Council platform. Rowan's kind of the opposite of that."
    jasmine @sadbrow talkingmouth "Oh, I know. My reluctance is more selfish than philosophical."
    jasmine @sadbrow talkingmouth "Last week, when Rowan was assigning partners, I faced a difficult battle every class. Just like every other student."
    jasmine @sadbrow talking2mouth "This week, we're free to pick our own partners. Yet out of consideration, nobody has chosen me."
    jasmine @sadbrow talkingmouth "Maybe I shouldn't complain. I'm sure I sound a bit hypocritical."
    red @sadbrow talkingmouth "No, I think I get what you mean. There's gotta be a middle ground between putting you in a bubble and throwing you to the Mightyena."
    red @angrybrow talkingmouth "If it helps, I'm not gonna treat you with kid gloves. You'd better be ready!"
    jasmine @angrybrow talkingmouth "I'd expect nothing less!"

elif (character == "May"):
    may uniform @sadbrow talkingmouth "[first_name]! You have {i}no idea{/i} how glad I am to see you."
    may @sadbrow talking2mouth "For weeks my whole life has been contests, contests, contests! Which is, um, {i}great{/i}--but my Pokémon want to battle, too!"
    may @sadbrow talking2mouth "Normally I'd just ask Brendan, but[ellipses] y'know[ellipses]"
    red uniform @talkingmouth "Say no more. I think I can help you take the edge off."
    may @angrybrow talkingmouth "That's exactly what I wanted to hear."

elif (character == "Melody"):
    melody uniform on @talking2mouth "What."
    red uniform @talking2mouth "What do you think? I want to battle you."
    melody @talking2mouth "Right. Gotta get your Pikachu to level fifty by the Millennium Drop."
    melody @bubblemouth "{w=0.5}.{w=0.5}.{w=0.5}."
    melody @talking2mouth "You know what? Fine. I've got time to kill."

elif (character == "Misty"):
    if (IsCoordinator() and HasEvent("Game", "Contest3")):
        misty uniform @sadbrow talking2mouth "Oh. Hey."
        red uniform @sadbrow talking2mouth "Look[ellipses] I get it. The Millennium Drop meant a lot to you, and I know you were practicing like crazy."
        red @sadbrow talkingmouth "But if it helps, that was the most badass thing I've seen all week. And I just saw Raihan bench-pressing his Cyclizar."
        misty uniform @sadbrow talkingmouth "Tch[ellipses]"
        red @playfuleyebrows talkingmouth "C'mon, that was a laugh. You know I saw it."
        misty uniform @sadbrow talkingmouth "Just battle me, you chowderhead."
    else:
        misty uniform @closedbrow talking2mouth "([ellipses]Then a half-turn on the high note, with my foot placed here[ellipses])"
        red uniform @embarrassedeyebrows talkingmouth "Um, Misty?"
        misty uniform @closedbrow talking2mouth "(Will he think I'm sucking up? Healing Spring is his own move[ellipses] No; who am I kidding. It's Wallace.)"
        red uniform @unamusedbrow talking2mouth "Earth to Misty. Ground Control requests a battle partner."
        misty uniform @surprised "Huh?!"
        red @embarrassedeyebrows talkingmouth "We're, uh, in gym class. Picking our own opponents. And you're[ellipses] lip-synching into the void."
        misty @sadbrow talkingmouth "Sure, let's battle; whatever[ellipses]"
        redmind @thonk "Wow, nothing? she's {i}really{/i} fixated on the Millennium Drop[ellipses]"

elif (character == "Morty"):
    red uniform @surprisedeyebrows surprisedeyes talking2mouth "Whoa. How come I never noticed we're in the same class?"
    morty uniform @talkingmouth "I like to keep a low profile. Pretty sure Rowan didn't notice me, either."
    red @happyeyebrows happyeyes talkingmouth "You know what? I can see the upside."
    red @confused "Come to think of it, I have no idea what Pokémon you train, either."
    morty @talkingmouth "Isn't that something. Ready to find out whether curiosity kills the cat?"

elif (character == "Nate"):
    red uniform @happy "You know, I like this kind of gym class! The power of free choice is really growing on me."
    if GetRelationshipRank("Nate") == 0:
        nate uniform @happy "Ha, yeah. Sure is nice!"
        red @angrybrow talkingmouth "We're agents of our own destines, battling for the noblest of all reasons: just 'cause we feel like it!"
    else:
        nate uniform @happy "Ha. Yeah. Must be nice."
        red @playfuleyes playfuleyebrows talkingmouth "Oh, c'mon. You can't pretend you aren't enjoying this a {i}little{/i} bit. Today, at least, we're agents of our own destinies!"
    nate @surprisedbrow talking2mouth "So, am I more aware than you of your own ulterior motives, or does an honest component disguise a system's ulteriority? Frienergy sure keeps me asking the big questions."
    red @unamusedeyebrows unamusedmouth "What."
    nate @happy "Don't worry your pretty little head about it."

elif (character == "Nessa"):
    if (IsCoordinator()):
        nessa uniform @talking2mouth "Uh-uh. I talk first."
        nessa @angrybrow talking2mouth "I'll only battle you if you're {i}not{/i} gonna talk to me about coordinating."
        red uniform @uniform playfuleyebrows playfuleyes talkingmouth "Getting too much of that from Instructor Wallace?"
        nessa @closedbrow talking2mouth "Not just from him. Water-type class lives up to {i}every{/i} stereotype."
        if (GetSeenClassScenes("Water") <= 10):
            red @playfuleyebrows talkingmouth "So it's full of hot gay men? I should spend more time there."
        else:
            red @happy "You're telling me! It's got more coordinators and hot gay dudes than the YMCA!" #YMKA? (Kyogrist)
    else:
        nessa uniform @talkingmouth "[first_name]! You're not a coordinator. I should've thought of you first."
        red uniform @talkingmouth "Hey, I'm just glad you thought of me last!"
        nessa @angrybrow talkingmouth "Talk to me about {i}battling{/i}. Please. Anything that doesn't involve 'jams' and 'appeals' and comparisons between me and Lisia."
        red @sadeyebrows talking2mouth "Instructor Wallace laying it on a little thick?"
        nessa @closedbrow talking2mouth "You have {i}no{/i} idea."

elif (character == "Raihan"):
    if ("Dragon Badge" in badgeslist):
        raihan uniform @happy "Haven't lost that Dragon Badge, have you?"
        show raihan uniform surprised
        red uniform @surprisedbrow talking2mouth "Dude, of course not! I bought a whole second toothbrush to keep it polished! Why do you ask?"
        raihan -surprised @happy "You're not a 'challenger' anymore, mate. Back in Galar, that'd qualify you to battle my {i}real{/i} team. But maybe we oughta take it easy, yeah?"
        red @embarrassedeyebrows talkingmouth "Hate to admit it, but you're probably right. You're the world's maybe-strongest-trainer's best frenemy, and by the associative property of battling, I don't think I'm ready for that." 
        red @angrybrow talkingmouth "At least, not yet."
        raihan @happy "Aces. We'll keep it sporting, then!"
    else:
        raihan uniform @talkingmouth "Thought I might see you here, mate."
        raihan @talking2mouth "I can see it in your peepers: you've got a score to settle."
        raihan @happy "Or maybe I'm projecting, an' you can tell me to sod off."
        red uniform @embarrassedeyebrows talkingmouth "Nah, you got me. If I'm picking my own opponent[ellipses] I want the guy I couldn't beat. That's how I'll learn, right?"
        raihan @happy "Couldn'ta put it better myself. Challenge accepted." # Another possible chance to give Red the Dragon Badge? Or not. Not sure how missable you want it to be.

elif (character == "Rosa"):
    rosa uniform @closedbrow talking2mouth "I'm {i}so{/i} sorry; I wish I could battle every one of my fans, but there's already a line fiftee--"
    rosa @surprisedbrow talking2mouth "--Oh, [first_name]! It's you!"
    rosa @happy "Forget I said anything. Let's battle!"
    red uniform @surprisedbrow talking2mouth "What about the fifteen people ahead of me?"
    rosa @talkingmouth "Are {i}you{/i} going to pester me for autographs afterwards?"
    red @talkingmouth "Wasn't planning on it."
    rosa @happy "Then you're on my express pass."

elif (character == "Sabrina"):
    show sabrina uniform closedbrow with dis
    redmind uniform "[sabrinacolor]Stop thinking so hard.{/color}"
    redmind @thonk "What?"
    redmind "[sabrinacolor]About who you're going to challenge. It's not like you, and it's making my head hurt.{/color}"
    redmind "[sabrinacolor]I'll make it easy. Get over here and battle me.{/color}"
    redmind @unamusedeyebrows "Yes, ma'am[ellipses]"

elif (character == "Serena"):
    serena uniform @talkingmouth "May I have the pleasure of this dance?"
    red uniform @talkingmouth "It'd be my honor, Your Ladyness."
    serena @talkingmouth "So close, and yet so far. Full points for effort, {i}mon ami{/i}."
    if (GetRelationshipRank("Serena") <1):
        red uniform @sad "Oh, just let me eat my cake."
        serena @angrybrow poutmouth "[ellipses]"
    else:
        red @playfuleyebrows talkingmouth "{size=30}Rhyhornwranglersayswhat?{/size}"

elif (character == "Silver"):
    if HasEvent("Silver", "Overthrown"):
        silver uniform @talking2mouth "Right on time. Absol needs to burn off some frustration."
        red uniform @sadeyebrows talking2mouth "Um[ellipses] Right[ellipses]"
        pause 1.0
        red @sadeyebrows talkingmouth "You know, Silver, if there's anything you want to talk abou--"
        silver @angry "No."
        pause 1.0
        silver @closedbrow talking2mouth "...Not {i}now.{/i}"
    else:
        silver uniform @talkingmouth "Right on time. One of today's Pokémon has a bone to pick with you."
        red uniform @surprisedbrow talking2mouth "What? Why? I've met plenty of trainers who don't like me, but I usually get along with Pokémon!"
        silver @talkingmouth "Don't take it personal. You kicked her ass a few weeks ago, when you were training with my[ellipses] associates in Inspira."
        silver @angrybrow talkingmouth "Now she's about ten levels higher and ready to settle the score."
        red @angrybrow talkingmouth "Well, I'm looking forward to the rematch! Bring it on!"

elif (character == "Skyla"):
    skyla uniform @happy "The wings of justice are in full feath--{size=30}wait, no.{/size}"
    skyla @angrybrow talkingmouth "Get ready, because I'll BEAK-oming for vict--{size=30}shoot.{/size}"
    skyla @embarrassedeyes embarrassedeyebrows talking2mouth "{size=30}Uh.{/size} No wishbones about it, the hero is here to[ellipses] hero[ellipses] here[ellipses]"
    pause 3.0
    red uniform @embarrassedeyebrows talkingmouth "You know, maybe we should just--"
    skyla @angrybrow happymouth "{i}OWL{/i} FOR {i}HERON'S{/i} SAKE LET'S JUST {i}WING{/i} IT!!!"

elif (character == "Sonia"):
    red uniform @talkingmouth "Hey, Sonia. Up for a battle?"
    sonia uniform @surprised "Oh! Yes, of course!"
    sonia @sadeyebrows talkingmouth "But, ah--we train together every Friday, in Battle Team. You know I'm hardly the strongest one there, and given the range of possible opponents, are you quite sure it's {i}me{/i} you'd like to challenge?"
    red @sadeyebrows talkingmouth "Hey, Sonia? Listen to yourself for a second. Half this room would give an arm to be the {i}worst{/i} member of the Battle Team. Which you aren't."
    red @talkingmouth "So, yeah. It's you I want to challenge."
    sonia @blush talkingmouth "Right-o, then. I accept!"

elif (character == "Tia"):
    if (GetRelationshipRank("Tia") == 0):
        red uniform @talkingmouth "You down for a battle, Tia?"
        show tia happy with dis
        narrator "You understand only one of Tia's signs[ellipses] the thumbs-up at the end."
    elif (GetRelationshipRank("Tia") == 1):
        tia uniform @happy "[first_name]! We made [tiafont]eye contact{/font}, so that means we have to battle!"
        red uniform @confused "Sorry, we did what?"
        tia uniform @sad "You know! When my [tiafont]eyes{/font} and your [tiafont]eyes stare{/font} into each other!"
        red uniform @surprisedbrow lightblush "Uh, I don't know what you're talking about! L-let's just forget about it!"
    else:
        tia uniform @happy "[first_name]! We made eye contact, so that means we have to battle!"
        red uniform @confused "[ellipses]Does it?"
        tia uniform @surprised "Well, I guess we don't {i}have{/i} to! But it's an ancient tradition among Alpha Pokémon!"
        red uniform @sadbrow talking2mouth "Yeesh. No wonder they get so tough."

elif (character == "Wally"):
    wally uniform @surprisedbrow talking2mouth "[wally_name][ellipses]"
    wally uniform @sad "You chose me."
    red uniform @surprisedbrow talking2mouth "Uh, sorry? Is that a bad thing?"
    wally @sadeyebrows talkingmouth "No. It's just[ellipses] I wanted to challenge you first."
    red @happy "Oh! Great minds think alike, I guess!"
    wally @angryeyebrows talkingmouth "This[ellipses] is how I'm going to get stronger."

elif (character == "Whitney"):
    red uniform @playfuleyes playfuleyebrows talkingmouth "Pop quiz, Whitney. What level's your Clefairy now?"
    whitney uniform @angryeyebrows poutmouth "You know what, mister? I'm {i}working{/i} on it."
    whitney @angryeyebrows talkingmouth "Greatness takes time. Do you know how many hours I've put into training Milty?"
    red @playfuleyes playfuleyebrows talkingmouth "I can guess. But isn't that the problem?"
    whitney @angryeyebrows talkingmouth "It's about to be {i}your{/i} problem!"

else:
    pass

return