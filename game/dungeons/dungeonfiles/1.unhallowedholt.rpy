#######SETUP###########

label unhallowedholt: #ghost-type dungeon, should be very easy, partners are Cheren, Skyla, and Silver

if (timeOfDay == "Night"):
    show silver at rightside, night:
        xzoom -1
    show skyla at leftside, night
    show cheren at night
    with dis

else:
    show silver at rightside:
        xzoom -1
    show skyla at leftside
    show cheren
    with dis

skyla @happy "Alright, let's go! We'll save Instructor Will, and break in the head of the big evil boss hiding in the forest!"

cheren @talking2mouth "It is unlikely any threat such as that is present... but if it is so, then so it is."

silver @closedbrow talkingmouth "Let's go. We don't need to wait around."

cheren @talking2mouth "Wait. This forest... it smells strongly of rot. We should prepare to see many Grass and Ghost types."
cheren @sad2eyes talking2mouth "Prepare accordingly, [first_name]. If the Disciplinary Committee is to embarrass itself by asking for your aid, you will be the deciding factor in our success."
cheren @talking2mouth "Now, are you ready?"

menu:
    "Yes!":
        silver @angry "We're getting Instructor Will back."

        skyla @talkingmouth "Finally... I can be a {i}real{/i} hero."

        cheren @closedbrow talking2mouth "This is how I pay my debt."

    "Not yet.":
        hide skyla
        hide silver
        hide cheren
        with dis

        if (timeOfDay == "Night"):
            jump aftersetupnight

        else:
            jump aftersetup
    
python:
    dungeon = Dungeon(name = "Unhallowed Holt",#a string
        endname = "Haunted Depths",#a string
        backgrounds = {"Night" : "midnightforest", "Default": "eveningforest"},#a dictionary of timeofdays to check against. If the current timeofday is not listed, then the "Default" value is picked.
        music = ("audio/music/duskforest.ogg"),#a tuple that contains one or two elements. If it contains two, the first is nolooped, and the second is looped. if it contains one, then it's looped
        encounterpool = {# a dictionary encounterpool, in the same format as the ones for normal wildareas
            pokedexlookupname("Pumpkaboo", DexMacros.Id): 5,
            pokedexlookupname("Phantump", DexMacros.Id): 3,
            pokedexlookupname("Rowlet", DexMacros.Id): 1,
            pokedexlookupname("Shuppet", DexMacros.Id): 7,
            pokedexlookupname("Paras", DexMacros.Id): 10,
            pokedexlookupname("Foongus", DexMacros.Id): 7,
        },
        difficulty = 16,#an int, 1-100, indicating the dungeon's difficulty. Should be roughly equivalent to AimLevel()
        floors = 5,#the number of battles you need to win to go through the level
        floorlength = 3,#the number of turns a battle will last, at max, before you find the stairs
        levelrange = range(11, 14),#a level range, set up the same way as normal wildarea level ranges
        startingmysteriosity=20,#the base chance that mysteriosity happenings will occur
        startingferocity=10,#the base chance that strong Pokémon will appear
        startinggenerosity=40,#the base chance that good things will happen
        trainers=["Silver", "Cheren", "Skyla"],# the trainers you start this dungeon with, not counting red
        cutscenefunc=UnhallowedHoltCutscenes,#the function that returns the cutscene labels you should jump to
        godmodder=None,#manually calls events and outcomes if certain conditions are met
        lootlist = {#the dictionary of loot that you should get from this
            Item.GimmighoulCoin : 20, 
            Item.RawstBerry : 10, 
            Item.OranBerry : 10, 
            Item.SitrusBerry : 5,  
            Item.OddKeystone : 1, 
            Item.SpellTag : 5, 
            Item.MiracleSeed : 5,
            Item.BlackApricorn : 3,
            Item.BlueApricorn : 3,
            Item.GreenApricorn : 3,
            Item.RedApricorn : 3,
            Item.WhiteApricorn : 3,
            Item.PinkApricorn : 3,
            Item.YellowApricorn : 3 })

call wildarea(dungeon) from _call_wildarea_10

jump AfterUnhallowedHolt

######GODMODDER & CUTSCENES###########

init python:
    def UnhallowedHoltCutscenes(parameters):
        currentscene = None
        if (parameters == "DungeonTurn5"):
            currentscene = "UnhallowedHoltBossIntro"
        elif (parameters == "DungeonBattle5"):
            currentscene = "UnhallowedHoltBoss"
        elif (dungeon.GetCurrentFloor() == 5 and Turn == 1):
            currentscene = "UnhallowedHolt1"
        elif (dungeon.GetCurrentFloor() == 5 and Turn == 2):
            currentscene = "UnhallowedHolt2"
        elif (dungeon.GetCurrentFloor() == 5 and Turn == 3):
            currentscene = "UnhallowedHolt3"

        if (currentscene != None and currentscene not in seencutscenes):
            seencutscenes.append(currentscene)
            renpy.hide_screen("battle")
            renpy.hide_screen("dungeonpartyviewer")
            renpy.call(currentscene)
            if (inbattle):
                renpy.show_screen("battle")
            else:
                renpy.show_screen("dungeonpartyviewer", dungeon)
            return True
        return False

label UnhallowedHoltBossIntro:
    stop music fadeout 1.5
    queue music "audio/music/potown_start.ogg" noloop
    queue music "audio/music/potown_loop.ogg"

    if (timeOfDay == "Night"):
        scene midnightforest
        show silver at rightside, night:
            xzoom -1
        show skyla at leftside, night
        show cheren at night
        with dis

    else:
        scene eveningforest
        show silver at rightside:
            xzoom -1
        show skyla at leftside
        show cheren
        with dis

    silver @talkingmouth "Did... we do it?"

    cheren @talking2mouth "We... {i}do{/i} appear to be in the deepest part of the forest, but I don't see..."

    show skyla surprised
    show silver surprised
    with dis

    skyla surprised "Ah! There, look!"

    hide skyla
    hide silver
    hide cheren
    with dis

    pause 1.0

    show will frownmouth poweredsadbrow with Dissolve(2.0):
        ypos 1.2 rotate 10

    narrator "You see Instructor Will slumped against a tree. His eyes are glowing faintly, and he's muttering something."

    will poweredbrow talking2mouth "{font=fonts/alien.ttf}We ... ... ... ... are ... danger!{/font}"

    if (timeOfDay == "Night"):
        cheren night @angrybrow talking2mouth "Be on your guard. There's something wrong here."
    else:
        cheren @angrybrow talking2mouth "Be on your guard. There's something wrong here."

    stop music fadeout 1.5
    queue music "audio/music/reliccastle_start.ogg" noloop fadein 1.0
    queue music "audio/music/reliccastle_loop.ogg"

    show will powered with Dissolve(1.0):
        ypos 1.2 rotate 10
        ease 2.0 ypos 0.9 rotate 0
        parallel:
            ease 2.0 ypos 0.95
            ease 2.0 ypos 0.9
            repeat

        parallel:
            ease 2.0 xpos 0.52
            ease 2.0 xpos 0.5
            ease 2.0 xpos 0.48
            ease 2.0 xpos 0.5
            repeat

    will poweredangrybrow angrymouth "{font=fonts/alien.ttf}We ... a great treasure within ... ... ... coming ... us ... will take ... treasure!{/font}"

    if (timeOfDay == "Night"):
        silver night @surprised "Woah, woah, is he going to try and fight us? We can't beat a teacher!"
    else:
        silver @surprised "Woah, woah, is he going to try and fight us? We can't beat a teacher!"

    $ PlaySound("pokemon/cries/708.mp3")
    $ PlaySound("pokemon/cries/723.mp3")
    $ PlaySound("pokemon/cries/46.mp3")

    cheren @angrybrow talking2mouth "No... look, with his psychic powers, he's controlling the wild Pokémon around him!"

    pause 1.0

    cheren @upeyes talking2mouth "Well, this is ironic."

    if (timeOfDay == "Night"):
        skyla night @angry "Come on! If we all fight together, we should be able to beat them!"
    else:
        skyla @angry "Come on! If we all fight together, we should be able to beat them!"    

    cheren @closedbrow talking2mouth "True. I've faith in your abilities."
    cheren shadow noshine surprisedeyes surprisedmouth "Disciplinary committee. Assist [first_name].{w=0.5} {i}Enforce order.{/i}"

    return

label UnhallowedHoltBoss:
    python:
        phantumpobj = Pokemon(708, level=23, moves=[GetMove("Will-O-Wisp"), GetMove("Hex"), GetMove("Leech Seed"), GetMove("Branch Poke")], frenzynerf=(18, ["Will-O-Wisp", "Hex", "Leech Seed", "Branch Poke"]))
        dartrixobj = Pokemon(723, level=23, moves=[GetMove("Razor Leaf"), GetMove("Shadow Sneak"), GetMove("Peck"), GetMove("Giga Drain")], frenzynerf=(18, ["Razor Leaf", "Shadow Sneak", "Peck", "Leafage"]))
        parasobj = Pokemon(46, level=23, moves=[GetMove("Fury Cutter"), GetMove("Spore"), GetMove("Poison Powder"), GetMove("Stun Spore")], frenzynerf=(18, ["Fury Cutter", "Spore", "Poison Powder", "Stun Spore"]))

        phantumpobj.ApplyStatus("controlled")
        dartrixobj.ApplyStatus("tyrannic")
        dartrixobj.ApplyStatus("controlled")
        parasobj.ApplyStatus("controlled")

        reinforcements = [Pokemon("Rowlet", AimLevel())] * 5
        
        goodguys = dungeon.GetTrainers()
        sidemonnum = 723
        badguys = []
        badguys.append(Trainer("sideportraitfull", TrainerType.Enemy, [phantumpobj], number=1, isPokemon=True))
        badguys.append(Trainer("sideportraitfull", TrainerType.Enemy, [dartrixobj] + reinforcements, number=1, isPokemon=True))
        badguys.append(Trainer("sideportraitfull", TrainerType.Enemy, [parasobj], number=1, isPokemon=True))

    call Battle(goodguys + badguys, uniforms=False, customoutfits=False, healParty=False, specialmusic="Nothing", canBeDitto=False, dungeon=dungeon) from _call_Battle_125

    return

label UnhallowedHolt1:
    hide screen battle
    hide screen battleui
    with dis

    will @poweredangrybrow angrymouth "{font=fonts/alien.ttf}We ... ... ...\n... are ... danger\n... ... ... ... ...{/font}"

    show screen battleui with dis
    return

label UnhallowedHolt2:
    hide screen battle
    hide screen battleui
    with dis

    will @poweredangrybrow angrymouth "{font=fonts/alien.ttf}We ... ... great treasure within ...\n... ... coming ... us\n... will take ... treasure{/font}"

    show screen battleui with dis
    return

label UnhallowedHolt3:
    hide screen battle
    hide screen battleui
    with dis

    will @poweredangrybrow angrymouth "{font=fonts/alien.ttf}Beware\n... us\n... ... man ... ... ...!{/font}"

    show screen battleui with dis
    return

###########CUSTOM EVENTS CALLED BY GODMODDER############

# None


##########WRAP-UP SCENE##########

label AfterUnhallowedHolt:

hide will with Dissolve(1.0)

if (timeOfDay == "Evening"):
    scene eveningforest
    show silver: 
        xzoom -1 xpos 0.8
    show will closedbrow frownmouth: 
        xpos 0.6
    show cheren: 
        xpos 0.4
    show skyla: 
        xpos 0.2
    with dis
else:
    scene midnightforest
    show silver at night: 
        xzoom -1 xpos 0.8
    show will closedbrow frownmouth at night: 
        xpos 0.6
    show cheren at night: 
        xpos 0.4
    show skyla at night: 
        xpos 0.2
    with dis

queue music "audio/music/lavender_start.ogg" noloop
queue music "audio/music/lavender_loop.ogg"

pause 1.0

cheren -shadow -noshine -surprisedmouth -surprisedeyes @talking2mouth "Instructor Will?"

if (timeOfDay == "Evening"):
    show will:
        xpos 0.6
        block:
            ease 0.02 xpos 0.59
            ease 0.02 xpos 0.6
            ease 0.02 xpos 0.61
            ease 0.02 xpos 0.6
            repeat 5
else:
    show will at night:
        xpos 0.6
        block:
            ease 0.02 xpos 0.59
            ease 0.02 xpos 0.6
            ease 0.02 xpos 0.61
            ease 0.02 xpos 0.6
            repeat 5

will "{size=30}Nngh.{/size}"

skyla @happy "He's waking up!"

will -closedbrow @sadbrow talkingmouth "...Who..."

show cheren surprisedbrow
show silver surprisedbrow
show skyla surprisedbrow
with dis

will @closedbrow angrymouth "Ah, my head! Oh, that {i}smarts{/i}!"

show cheren -surprisedbrow
show silver -surprisedbrow
show skyla -surprisedbrow
with dis

silver @talkingmouth "Instructor Will? What happened?"

will @angry "Why... I remember now, yes! I went into the forest to rescue my darling Bri and Bianca, when..."

will @closedbrow talking2mouth "Oh... I was attacked! Assaulted! Impugned!"

will @angrybrow talking2mouth "Who would do such a thing? To me, the Great Will? Never in my life, have I..."

pause 1.0

will @sadbrow talking2mouth "Wait... where is Sabrina? Where is Bianca? Are they safe?"

if (rescuedsabrina and rescuedtia):
    cheren @happy "Sabrina and Bianca have been safely returned to campus grounds."

    will -frownmouth @closedbrow talkingmouth "Oh, thank the heavens."

    will @angrybrow talking2mouth "Then we must give chase! The beast who did this to my precious students is still at large!"

elif (rescuedsabrina):
    cheren @happy "Sabrina has been safely returned to campus grounds."

    will @closedbrow talkingmouth "Oh, thank the heavens."

    cheren @closedbrow talking2mouth "We're... still attempting to ascertain Bianca's whereabouts, though. We hoped you may be able to assist in our efforts to do so."

    will @sadbrow talking2mouth "I... will certainly try. But it seems that my last attempt was an utter failure..."

elif (rescuedtia):
    cheren @happy "Bianca has been safely returned to campus grounds."

    will @closedbrow talkingmouth "Oh, thank the heavens."

    cheren @closedbrow talking2mouth "We're... still attempting to ascertain Sabrina's whereabouts, though. We hoped you may be able to assist in our efforts to do so."

    will @sadbrow talking2mouth "I... will certainly try. But it seems that my last attempt was an utter failure..."

else:
    cheren @closedbrow talking2mouth "We're... still attempting to ascertain their whereabouts. We hoped you may be able to assist in our efforts to do so."

    will @sadbrow talking2mouth "I... will certainly try. But it seems that my last attempt was an utter failure..."

cheren @talking2mouth "There will be time to discuss our plans for the future later."

skyla @talkingmouth "Right now, we need to check you into the infirmary. You're banged up pretty bad, and I bet you haven't been eating or drinking right since you disappeared."

will @closedbrow poutmouth "Oh... now I know how Bri must have felt. I despise this, but... you're right. I feel quite faint right now..."

if (timeOfDay == "Evening"):
    show silver:
        xpos 0.8
        ease 0.5 xpos 0.75

    show will sadbrow:
        xpos 0.6 rotate 0
        ease 0.5 rotate 5
else:
    show silver at night:
        xpos 0.8
        ease 0.5 xpos 0.75

    show will sadbrow at night:
        xpos 0.6 rotate 0
        ease 0.5 rotate 5 

silver @closedbrow talkingmouth "...C'mon, Instructor. Lean on me. Let's get you out of here."

cheren @talking2mouth "[first_name]. I cannot understand, for the life of me, why you would aid the Disciplinary Committee, your enemy, in these duties."

$ ValueChange("Cheren", -10, 0.4)

cheren @sad2eyes talking2mouth "However, perhaps understanding is not required here. Your means were benign, as were your ends. Motivation perhaps does not matter. I offer my thanks. Do with it what you will."

skyla @happy "Thanks, [first_name]! You've kinda got a knack for this superhero stuff."

$ ValueChange("Skyla", 10, 0.2)

silver @closedbrow talkingmouth "{size=30}Airhead.{/size}"
silver @talkingmouth "But, yeah, thanks, [first_name]. This was an actual good thing we did."

$ ValueChange("Silver", 10, 0.75)

silver @closedbrow happymouth "...So that's one."

call clearscreens() from _call_clearscreens_151
show blank2 with splitfade

pause 1.0

narrator "Everyone makes their way back to the infirmary, battered and bruised."

$ AddEvent("Instructor Will", "Rescued")
$ rescuedwill = True
$ lastsaved = "Will"
$ _rollback = True
$ renpy.block_rollback()

jump infirmary