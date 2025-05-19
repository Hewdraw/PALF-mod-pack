#######SETUP###########

label windsweptwoods: #flying-type dungeon, should be hard-difficulty, partners are Rosa, Nessa, Raihan and Sonia

if (timeOfDay == "Night"):
    if (IsPresent("Raihan")):
        show rosa at night:
            xpos 0.2
        show nessa at night:
            xpos 0.4
        show raihan at night:
            xpos 0.6
        show sonia at night:
            xpos 0.8
        with dis
    else:
        show rosa at leftside, night
        show sonia at rightside, night
        show nessa at night
        with dis

else:
    if (IsPresent("Raihan")):
        show rosa:
            xpos 0.2
        show nessa:
            xpos 0.4
        show raihan:
            xpos 0.6
        show sonia:
            xpos 0.8
        with dis

    else:
        show rosa at leftside
        show sonia at rightside
        show nessa
        with dis

rosa @talkingmouth "Okay, are we all ready?"

nessa @talkingmouth "Not so fast. Sonia, what did your survey say?"

sonia @talking2mouth "Looks like this part of the forest is called the 'Windswept Woods.' The especially tall trees cause wicked air currents up top. Flying-types make this place their home, in addition to the expected Grass-types."

rosa @surprised "Huh?"

nessa @talkingmouth "We staked the place out to figure out what kind of wild Pokémon we might find. Honestly, Rosa, you could stand to think ahead a bit."
nessa @closedbrow talkingmouth "There's no stunt double to take your place. No reshoots on this stage, if anything goes wrong."

rosa @sadbrow sweat sadmouth "I'm... yeah. You're right."

nessa @closedbrow talkingmouth "You're doing the right thing. Let's just do it smartly."

if (IsPresent("Raihan")):
    raihan @happy "We don't need to do this smartly, girls. You've got The Great Raihan here. My Rock-types will make these Flying-types embarrassed to have wings!"

sonia @talking2mouth "Right, [first_name]. If you've got any Foreverals that give [pika_name] the Ice-type, now might be a good time to use them."
sonia @closedbrow talking2mouth "Or... perhaps Electric, or Rock, or Flying, or Fire...? Hm..."

menu:
    "I'm ready.":
        rosa @talkingmouth "Allllright! We're {i}totally{/i} going to write a story here! A {i}real{/i} adventure!"

        nessa @talkingmouth "...This'd all sort itself out in the end, but... why wait?"

        sonia @talking2mouth "[first_name]. Reckon you could use [pika_name] in battle a good bit? I'd like to get some more data on him."

        if (IsPresent("Raihan")):
            raihan @talking2mouth "Seconding that. I'd like to see what the slayer of Jobbird can do up-close."

            if (timeOfDay == "Night"):
                red night @closedbrow talkingmouth sweat "Maybe don't call Dawn's Altaria that anymore..."

            else:
                red @closedbrow talkingmouth sweat "Maybe don't call Dawn's Altaria that anymore..."

    "Hold on a mo'.":
        hide rosa
        hide nessa
        hide sonia
        hide raihan
        with dis

        if (timeOfDay == "Night"):
            jump aftersetupnight

        else:
            jump aftersetup

python:
    dungeon = Dungeon(name = "Windswept Woods",#a string
        endname = "Towering Arborage",#a string
        backgrounds = {"Night" : "midnightforest", "Default": "eveningforest"},#a dictionary of timeofdays to check against. If the current timeofday is not listed, then the "Default" value is picked.
        music = ("audio/music/duskforest.ogg"),#a tuple that contains one or two elements. If it contains two, the first is nolooped, and the second is looped. if it contains one, then it's looped
        encounterpool = {# a dictionary encounterpool, in the same format as the ones for normal wildareas
            pokedexlookupname("Swablu", DexMacros.Id) : 10, 
            pokedexlookupname("Rowlet", DexMacros.Id) : 1, 
            pokedexlookupname("Hoothoot", DexMacros.Id) : 5,
            pokedexlookupname("Hoppip", DexMacros.Id) : 7,
            pokedexlookupname("Paras", DexMacros.Id) : 10,
            pokedexlookupname("Foongus", DexMacros.Id): 7
        },
        difficulty = 18,#an int, 1-100, indicating the dungeon's difficulty. Should be roughly equivalent to AimLevel()
        floors = 5,#the number of battles you need to win to go through the level
        floorlength = 5,#the number of turns a battle will last, at max, before you find the stairs
        levelrange = range(13, 17),#a level range, set up the same way as normal wildarea level ranges
        startingmysteriosity=10,#the base chance that mysteriosity happenings will occur
        startingferocity=20,#the base chance that strong Pokémon will appear
        startinggenerosity=20,#the base chance that good things will happen
        trainers=["Rosa", "Nessa", "Sonia"] + (["Raihan"] if IsPresent("Raihan") else []),# the trainers you start this dungeon with, not counting red
        cutscenefunc=WindsweptWoodsCutscenes,#the function that returns the cutscene labels you should jump to
        godmodder=None,#manually calls events and outcomes if certain conditions are met
        lootlist = {#the dictionary of loot that you should get from this
            Item.GimmighoulCoin : 20, 
            Item.ChestoBerry : 10, 
            Item.OranBerry : 10, 
            Item.SitrusBerry : 9, 
            Item.SharpBeak : 5, 
            Item.MiracleSeed : 5,
            Item.BlackApricorn : 3,
            Item.BlueApricorn : 3,
            Item.GreenApricorn : 3,
            Item.RedApricorn : 3,
            Item.WhiteApricorn : 3,
            Item.PinkApricorn : 3,
            Item.YellowApricorn : 3 })

call wildarea(dungeon) from _call_wildarea_12

jump AfterWindsweptWoods

######GODMODDER & CUTSCENES###########

init python:
    def WindsweptWoodsCutscenes(parameters):
        currentscene = None
        
        tiafainted = False
        for mon in FaintedMons:
            if (mon.GetId() == pokedexlookupname("Latias", DexMacros.Id)):
                tiafainted = True

        if (parameters == "DungeonTurn5"):
            currentscene = "WindsweptWoodsBossIntro"
        elif (parameters == "DungeonBattle5"):
            currentscene = "WindsweptWoodsBoss"
        elif (dungeon.GetCurrentFloor() == 5):
            if (Turn == 1):
                currentscene = "WindsweptWoods1"
            elif (Turn == 2):
                currentscene = "WindsweptWoods2"
            elif (Turn == 3):
                currentscene = "WindsweptWoods3"

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

label WindsweptWoodsBossIntro:
    stop music fadeout 1.5
    queue music "audio/music/potown_start.ogg" noloop
    queue music "audio/music/potown_loop.ogg"

    if (timeOfDay == "Night"):
        if (IsPresent("Raihan")):
            scene midnightforest
            show rosa at night:
                xpos 0.2
            show nessa at night:
                xpos 0.4
            show raihan at night:
                xpos 0.6
            show sonia at night:
                xpos 0.8
            with dis
        else:
            scene midnightforest
            show rosa at leftside, night
            show sonia at night
            show nessa at rightside, night
            with dis

    else:
        if (IsPresent("Raihan")):
            scene eveningforest
            show rosa:
                xpos 0.2
            show nessa:
                xpos 0.4
            show raihan:
                xpos 0.6
            show sonia:
                xpos 0.8
            with dis
        else:
            scene eveningforest
            show rosa at leftside
            show sonia 
            show nessa at rightside
            with dis

    rosa @sweat sadbrow talking2mouth "Oh man... we're through... I'd rather spend seven months shooting in the jungles of Fiore than do that again."

    sonia @sadbrow talkingmouth "...Brr. It's chilly."

    nessa @talkingmouth "Are you two seriously whining about this? It was just a short hike."

    if (IsPresent("Raihan")):
        raihan @happy "Yeah, I'm with Ness! That was nothing."

    rosa @angrybrow talking2mouth "Speak for yourself! I'm used to having my air-conditioned trailer whenever I'm within fifty feet of a tree!"

    nessa @closedbrow talkingmouth "What a surprise. You're more of a princess than I thought."

    rosa @surprised "P-Princess?! I-- {i}why, I never!{/i}"

    stop music fadeout 1.5

    show rosa surprised
    show nessa surprised
    show sonia surprised
    with dis

    if (IsPresent("Raihan")):
        show raihan surprised with dis

    redmind @surprised "[sabrinacolor]Help.{/color}"

    sonia sadbrow frownmouth @talking2mouth "You lot heard that, right?"

    rosa sadbrow frownmouth @talking2mouth "Yeah. That was definitely Sabrina."

    if (IsPresent("Raihan")):
        raihan @surprised "...So, this is the girl you called me to help? Alright."

    nessa angrybrow frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."

    queue music "audio/music/lavenderintense_start.ogg" noloop
    queue music "audio/music/lavenderintense_loop.ogg"

    nessa @talkingmouth "There."

    hide sonia
    hide rosa
    hide nessa
    hide raihan
    with dis

    pause 1.0

    if (timeOfDay == "Night"):
        show sabrina poweredbrow casualoldhair at night with Dissolve(1.0):
            ypos 0.9 xpos 0.5
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

    else:
        show sabrina poweredbrow casualoldhair with Dissolve(1.0):
            ypos 0.9 xpos 0.5
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

    if (timeOfDay == "Night"):
        rosa night @talkingmouth "...Sabrina!"
    else:
        rosa @talkingmouth "...Sabrina!"

    if (timeOfDay == "Night"):
        nessa night @surprised "She looks different." 
    else:
        nessa @surprised "She looks different." 

    if (timeOfDay == "Night"):
        sonia night @sadbrow talking2mouth "Did you do something new with your hair?"
    else:
        sonia @sadbrow talking2mouth "Did you do something new with your hair?"

    if (IsPresent("Raihan")):
        if (timeOfDay == "Night"):
            raihan night @closedbrow talking2mouth "Hey, I'm suddenly a {i}lot{/i} more into this rescue mission."
        else:
            raihan @closedbrow talking2mouth "Hey, I'm suddenly a {i}lot{/i} more into this rescue mission."

    rosa @angrybrow talking2mouth "Now's not the time for jokes! We have to save her!"

    nessa @talkingmouth "Granted, but from what? She looks fine... if a bit exposed."

    if (not HasEvent("Nessa", "OutfitSwap")):
        sonia @talkingmouth "{i}You're{/i} saying that, Ness?"

        nessa @closedbrow talkingmouth "It's {i}my{/i} choice. I just want to make sure that that was hers."

    if (timeOfDay == "Night"):
        red night @angrybrow talking2mouth "...Sabrina?"
    else:
        red @angrybrow talking2mouth "...Sabrina?"

    sabrina @talking2mouth "{font=fonts/alien.ttf}We come ... ... ... ... ... ... ... ... ... for ...!{/font}"

    red @surprised "What? What are you coming for...?"

    sabrina @talking2mouth "{font=fonts/alien.ttf}... ... a great treasure ... us ... ... coming for ... ... ... ... our treasure!{/font}"

    if (GetRelationshipRank("Sabrina") > 0):
        red @sad "This... isn't her. Something's controlling her."

    else:
        rosa @sad "This... isn't her. Something's controlling her."

    sonia @angrybrow talkingmouth "I reckoned. We might need to prepare for a nasty fight, then."

    red @angrybrow talking2mouth "Alright. Let's go."

    dn "Sabrina's emotions fluctuate through everyone's minds! The Mysteriosity spits out several Psychic-type Pokémon, eager to consume the fluctuating emotions!"
    dn "They're greedy opportunists, but it looks like they may flee if the strong Pokémon they're following is defeated..."

    return

label WindsweptWoodsBoss:
    python:
        dungeon.Reinforcing = False
        sabrinaparty = GetTrainerTeam("Sabrina")
        goodguys = dungeon.GetTrainers()
        badguys = []
        for mon in sabrinaparty:
            mon.ApplyStatus("tyrannic")
            mon.ApplyStatus(".keystone")#if they're knocked out, the entire trainer is knocked out
            badguys.append(Trainer("sabrina", TrainerType.Enemy, [mon] + [Pokemon("Drowzee")] * 3, number=1))

    call Battle(goodguys + badguys, uniforms=False, customoutfits=False, healParty=False, specialmusic="Nothing", canBeDitto=False, dungeon=dungeon) from _call_Battle_127

    return

label WindsweptWoods1:
    if (timeOfDay == "Night"):
        hide screen battle
        show screen battleui
        show sabrina casualoldhair poweredbrow at night
        with dis
    else:
        hide screen battle
        show screen battleui
        show sabrina casualoldhair poweredbrow
        with dis

    sabrina @angrymouth "{font=fonts/alien.ttf}We come ... ...\n... ... ... ...\n... ... ... for ...{/font}"

    show screen battleui
    hide sabrina
    with dis
    return

label WindsweptWoods2:
    if (timeOfDay == "Night"):
        hide screen battle
        show screen battleui
        show sabrina casualoldhair poweredbrow at night
        with dis
    else:
        hide screen battle
        show screen battleui
        show sabrina casualoldhair poweredbrow
        with dis

    sabrina @angrymouth "{font=fonts/alien.ttf}... ... a great treasure ... us\n... ... coming for ...\n... ... ... our treasure{/font}"

    show screen battleui
    hide sabrina
    with dis
    return

label WindsweptWoods3:
    if (timeOfDay == "Night"):
        hide screen battle
        show screen battleui
        show sabrina casualoldhair poweredbrow at night
        with dis
    else:
        hide screen battle
        show screen battleui
        show sabrina casualoldhair poweredbrow
        with dis

    sabrina @angrymouth "{font=fonts/alien.ttf}Beware\n... ...\nBeware ... man clad ... ...{/font}"

    show screen battleui
    hide sabrina
    with dis
    return

###########CUSTOM EVENTS CALLED BY GODMODDER############

# None


##########WRAP-UP SCENE##########

label AfterWindsweptWoods:

stop music fadeout 1.5
queue music "audio/music/lavender_start.ogg" noloop
queue music "audio/music/lavender_loop.ogg"

if (IsPresent("Raihan")):
    if (timeOfDay == "Evening"):
        scene eveningforest
        show rosa frownmouth:
            xpos 1.0/6.0
        show sabrina casualoldhair closedbrow:
            xpos 2.0/6.0
        show sonia frownmouth:
            xpos 3.0/6.0
        show nessa frownmouth: 
            xpos 4.0/6.0
        show raihan frownmouth:
            xpos 5.0/6.0
        with dis
    else:
        scene midnightforest
        show rosa frownmouth at night:
            xpos 1.0/6.0
        show sabrina casualoldhair closedbrow at night:
            xpos 2.0/6.0
        show sonia frownmouth at night:
            xpos 3.0/6.0
        show nessa frownmouth at night: 
            xpos 4.0/6.0
        show raihan frownmouth at night:
            xpos 5.0/6.0
        with dis

else:
    if (timeOfDay == "Evening"):
        scene eveningforest
        show rosa frownmouth: 
            xpos 0.2
        show sabrina casualoldhair closedbrow: 
            xpos 0.4
        show sonia frownmouth: 
            xpos 0.6
        show nessa frownmouth: 
            xpos 0.8
        with dis
    else:
        scene midnightforest
        show rosa frownmouth at night: 
            xpos 0.2
        show sabrina casualoldhair closedbrow at night: 
            xpos 0.4
        show sonia frownmouth at night: 
            xpos 0.6
        show nessa frownmouth at night: 
            xpos 0.8
        with dis

pause 1.0

rosa @sadmouth "...Sabrina?"

if (IsPresent("Raihan")):
    if (timeOfDay == "Evening"):
        show sabrina:
            xpos 0.4
            block:
                ease 0.02 xpos 2.0/6.0 - 0.01
                ease 0.02 xpos 2.0/6.0
                ease 0.02 xpos 2.0/6.0 + 0.01
                ease 0.02 xpos 2.0/6.0
                repeat 5
    else:
        show sabrina at night:
            xpos 0.4
            block:
                ease 0.02 xpos 2.0/6.0 - 0.01
                ease 0.02 xpos 2.0/6.0
                ease 0.02 xpos 2.0/6.0 + 0.01
                ease 0.02 xpos 2.0/6.0
                repeat 5

else:
    if (timeOfDay == "Evening"):
        show sabrina:
            xpos 0.4
            block:
                ease 0.02 xpos 0.39
                ease 0.02 xpos 0.4
                ease 0.02 xpos 0.41
                ease 0.02 xpos 0.4
                repeat 5
    else:
        show sabrina at night:
            xpos 0.4
            block:
                ease 0.02 xpos 0.39
                ease 0.02 xpos 0.4
                ease 0.02 xpos 0.41
                ease 0.02 xpos 0.4
                repeat 5

sabrina "{size=30}Nngh.{/size}"

sonia @happy "She's snapping out of it!"

sabrina -closedbrow @sadbrow talking2mouth "Where..."

if (IsPresent("Raihan")):
    if (timeOfDay == "Evening"):
        show raihan surprisedbrow:
            xpos 5.0/6.0
        show nessa surprisedbrow:
            xpos 4.0/6.0
        show rosa surprisedbrow:
            xpos 1.0/6.0
        show sonia surprisedbrow:
            xpos 3.0/6.0
        with dis

    else:
        show raihan surprisedbrow at night:
            xpos 5.0/6.0
        show nessa surprisedbrow at night:
            xpos 4.0/6.0
        show rosa surprisedbrow at night:
            xpos 1.0/6.0
        show sonia surprisedbrow at night:
            xpos 3.0/6.0
        with dis

else:
    if (timeOfDay == "Evening"):
        show nessa surprisedbrow:
            xpos 0.8
        show rosa surprisedbrow:
            xpos 0.2
        show sonia surprisedbrow:
            xpos 0.6
        with dis

    else:
        show nessa surprisedbrow at night:
            xpos 0.8
        show rosa surprisedbrow at night:
            xpos 0.2
        show sonia surprisedbrow at night:
            xpos 0.6
        with dis

sabrina @closedbrow angrymouth "Ah! My head, ow...{w=0.5} ow...{w=0.5}"

if (IsPresent("Raihan")):
    if (timeOfDay == "Evening"):
        show raihan -surprisedbrow:
            xpos 5.0/6.0
        show nessa -surprisedbrow:
            xpos 4.0/6.0
        show rosa -surprisedbrow:
            xpos 1.0/6.0
        show sonia -surprisedbrow:
            xpos 3.0/6.0
        with dis

    else:
        show raihan -surprisedbrow at night:
            xpos 5.0/6.0
        show nessa -surprisedbrow at night:
            xpos 4.0/6.0
        show rosa -surprisedbrow at night:
            xpos 1.0/6.0
        show sonia -surprisedbrow at night:
            xpos 3.0/6.0
        with dis

else:
    if (timeOfDay == "Evening"):
        show nessa -surprisedbrow:
            xpos 0.8
        show rosa -surprisedbrow:
            xpos 0.2
        show sonia -surprisedbrow:
            xpos 0.6
        with dis

    else:
        show nessa -surprisedbrow at night:
            xpos 0.8
        show rosa -surprisedbrow at night:
            xpos 0.2
        show sonia -surprisedbrow at night:
            xpos 0.6
        with dis

rosa @talking2mouth "Sabrina? You're safe, now. We came here to get you back."

sabrina @sadbrow talking2mouth "Get... get me back? What do you...? No, I came out here on purpose..."
sabrina @sadbrow talking2mouth "This... this was all part of the plan, but then... headaches, and... I was attacked. But... the plan..."

nessa @talkingmouth "Was being out here for almost a week part of your plan?"

sonia @confusedbrow talkingmouth "What have you been {i}eating?{/i}"

sabrina @sadbrow talking2mouth "I... I..."

if (IsPresent("Raihan")):
    sabrina @surprisedbrow talking2mouth "Wait, {i}Raihan?{/i}"

    raihan @happy "Hey, another fan. Yeah, it's Raihan. You one of the Fang Gang?"

    $ ValueChange("Sabrina", 10, 2.0/6.0)

    sabrina @talking2mouth "I... follow your RotoPhoto stories..."

    nessa @talkingmouth "Sabrina. Don't blow up his head any more than it already is, okay? I need you to think back. What do you remember?"

pause 2.0

sabrina @closedbrow talking2mouth "I don't... remember. I remember the yelling, and the anger, then running out here, and... nothing."

if (GetRelationshipRank("Sabrina") > 0):

    sabrina @surprised "Wait... [first_name]?"

    if (timeOfDay == "Night"):
        red @happy "'Bout time you noticed. Just cause I'm not a supermodel doesn't mean I'm not here."

    else:
        red night @happy "'Bout time you noticed. Just cause I'm not a supermodel doesn't mean I'm not here."

    sabrina @talking2mouth "I... I thought you were leaving... I read--I heard--"

    red @happy "Yeah, I did leave. And then I came back. What'd I say? You can't trust people's thoughts."

    sabrina @closedbrow talking2mouth "I'm... glad."

if (IsPresent("Raihan")):
    if (timeOfDay == "Evening"):
        show raihan surprised:
            xpos 5.0/6.0
        show nessa surprised:
            xpos 4.0/6.0
        show sonia surprised:
            xpos 3.0/6.0
        with dis

    else:
        show raihan surprised at night:
            xpos 5.0/6.0
        show nessa surprised at night:
            xpos 4.0/6.0
        show sonia surprised at night:
            xpos 3.0/6.0
        with dis

else:
    if (timeOfDay == "Evening"):
        show nessa surprised:
            xpos 0.8
        show sonia surprised:
            xpos 0.6
        with dis

    else:
        show nessa surprised at night:
            xpos 0.8
        show sonia surprised at night:
            xpos 0.6
        with dis

rosa @angry "Hold on! We've got something serious to discuss before we take you one step further, Sabrina!"

sabrina @sad "I... I know. I'm so sorry. I didn't mean to reveal everyone's secrets. I shouldn't have snapped at-"

if (IsPresent("Raihan")):
    if (timeOfDay == "Evening"):
        show raihan -surprised:
            xpos 5.0/6.0
        show nessa -surprised:
            xpos 4.0/6.0
        show sonia -surprised:
            xpos 3.0/6.0
        with dis

    else:
        show raihan -surprised at night:
            xpos 5.0/6.0
        show nessa -surprised at night:
            xpos 4.0/6.0
        show sonia -surprised at night:
            xpos 3.0/6.0
        with dis

else:
    if (timeOfDay == "Evening"):
        show nessa -surprised:
            xpos 0.8
        show sonia -surprised:
            xpos 0.6
        with dis

    else:
        show nessa -surprised at night:
            xpos 0.8
        show sonia -surprised at night:
            xpos 0.6
        with dis

rosa @happy "Where did you get that {i}adorable{/i} tank top?"

sabrina surprised "Huh?"

nessa @talkingmouth "Seriously, a crop/tank-top with low-rise jeans? That's fashion, if I've ever seen it. You're more daring than I thought."

sabrina sadbrow surprisedmouth "I... it's just... a grocery store..."

sonia @confused "Hold on, you're telling me you picked out {i}that{/i} cute outfit at a grocery store? What could you do in an actual clothes store?!"

nessa @closedbrow talkingmouth "I don't know, but I want to find out."

rosa @happy "Sounds like a trip to Forever 151 is in order!"
rosa @sadbrow talkingmouth "I... can't buy anything, but I can lend an eye, and--"

if (IsPresent("Raihan")):
    if (timeOfDay == "Evening"):
        show eveningforest with vpunch
        show sabrina poweredbrow angrymouth with dis:
            xpos 1.0/3.0
    else:
        show midnightforest with vpunch
        show sabrina poweredbrow angrymouth at night with dis:
            xpos 1.0/3.0
else:
    if (timeOfDay == "Evening"):
        show eveningforest with vpunch
        show sabrina poweredbrow angrymouth with dis:
            xpos 0.4
    else:
        show midnightforest with vpunch
        show sabrina poweredbrow angrymouth at night with dis:
            xpos 0.4

sabrina "N-no! You don't understand! I'm a witch--a curse! I'll only hurt you if you try to get closer to me! I'll expose everything about you!"

pause 1.0

if (GetRelationshipRank("Sabrina") > 0):
    red @talkingmouth "Sabrina."

    if (timeOfDay == "Evening"):
        show sabrina sadbrow with dis:
            xpos (0.4 if IsAbsent("Raihan") else 1.0/3.0)
    else:
        show sabrina sadbrow at night with dis:
            xpos (0.4 if IsAbsent("Raihan") else 1.0/3.0)

    red @talkingmouth "Yeah, you exposed me. But it wasn't your fault. And, in the long run, I think you did me a favor."

rosa @talking2mouth "Sabrina. You know what my darkest secret is?"

if (timeOfDay == "Evening"):
    show sabrina sadbrow -angrymouth with dis:
        xpos (0.4 if IsAbsent("Raihan") else 1.0/3.0)
else:
    show sabrina sadbrow -angrymouth at night with dis:
        xpos (0.4 if IsAbsent("Raihan") else 1.0/3.0)

sabrina @sadbrow talking2mouth "...Yes."

rosa @happy "And so does everyone else. It's literally on every single one of my wiki pages."

nessa @talkingmouth "I've made a couple of mistakes. Most of them involving Raihan. And he told {i}everyone.{/i} He didn't even have Esper powers as an excuse."

if (IsPresent("Raihan")):
    raihan @sad "Guilty as charged. Not proud of it, though. I just have trouble keeping my mouth shut when something great happens."

sonia @talkingmouth "I'm not quite sure I have anything like a 'secret,' but... well, I reckon I've already done the most embarrassing thing that could happen to me this year, what with begging Janine to let me back into the Battle Team."

sabrina @talking2mouth "I... maybe, then, but..."

nessa @talkingmouth "Come on. You don't need to make any decisions right now. The thing we need to do now is get you back to the school."

if (IsAbsent("Raihan")):
    if (timeOfDay == "Evening"):
        show nessa:
            xpos 0.8
            ease 0.2 xpos 0.85
        show rosa:
            xpos 0.2
            ease 0.2 xpos 0.05
        show sonia:
            xpos 0.6
            ease 0.2 xpos 0.75
        with dis

    else:
        show nessa at night:
            xpos 0.8
            ease 0.2 xpos 0.85
        show rosa at night:
            xpos 0.2
            ease 0.2 xpos 0.05
        show sonia at night:
            xpos 0.6
            ease 0.2 xpos 0.75
        with dis

    pause 1.0

    red @confusedeyebrows frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."

    red @talkingmouth "Oh, so just because I'm the only guy here, I'm the one who has to carry her."

    nessa @talkingmouth "Go on. Be a gentleman."

else:
    sonia @talking2mouth "Rai, could you give her a hand?"

    if (GetRelationshipRank("Sabrina") > 0):
        raihan @closedbrow talking2mouth "Sure, but... I dunno... [last_name], maybe I'm being presumptuous, but I get the feeling you'd rather do it?"

    else:
        raihan phone @talking2mouth "Sorry. Gotta keep my hands free for this victory selfie I'm about to snap. [last_name], think you've got a hand free for a pretty girl?"

        nessa @closedbrow talking2mouth "{size=30}Ugh. The only thing worse than Raihan's flirting is when he tries to wingman for you.{/size}"

        show raihan -phone with dis

sabrina @sadbrow talking2mouth "I... I can walk by myself..."

menu:
    "Take my hand.":
        $ ValueChange("Sabrina", -3, (0.4 if IsAbsent("Raihan") else 1.0/3.0))

    "You don't need to, though.":
        pass

    "Alright.":
        $ ValueChange("Sabrina", 3, (0.4 if IsAbsent("Raihan") else 1.0/3.0))

        sabrina @closedbrow talking2mouth "Thank you, but..."

pause 1.0

sabrina @sadbrow talking2mouth "No."

pause 1.0

red @confused "No?"

sabrina @talking2mouth "They... those students... they targeted me {i}because of you.{/i}"

sonia sad "Steady on, Sabrina." 

nessa sad "That wasn't his fault."

sabrina @closedbrow angrymouth "I know! It wasn't anyone's fault but my own. But I... I..."

if (GetRelationshipRank("Sabrina") > 0):
    sabrina @closedbrow angrymouth "I {i}told{/i} you to stay away from me! The very first time we met, that was {i}all{/i} I asked for!"

    sabrina @sad "Why... why didn't you...?"

    red @sadbrow frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."

    redmind @sadbrow frownmouth "...She did, didn't she...?"
    redmind @sadbrow frownmouth "I... I guess I thought... that I could make you happier than leaving you alone would make you."

    pause 2.0

    rosa sad "I understand you're upset, Sabrina. [first_name] does, too. Don't take it out on him. You two were friends, right? You told me about him in our classes together." 

    sabrina @talking2mouth "I didn't think through the consequences. I thought... I thought I knew what kinds of heartbreak the future held. {size=30}I couldn't have predicted this.{/size}"

else:
    sabrina @closedbrow sadmouth "I know."

    sabrina @sadbrow talking2mouth "You did everything right."

    $ ValueChange("Sabrina", 10, (0.4 if IsAbsent("Raihan") else 1.0/3.0))

    sabrina @closedbrow angrymouth "You even stayed away from me, which was all I asked for. If I can't keep people safe when they do everything right, when {i}I{/i} do everything right, then what can I..."

    rosa sad "I understand you're upset, Sabrina. [first_name] does, too. Don't take it out on him, or yourself."

menu:
    "It was Cheren's fault.":
        $ AddEvent("Sabrina", "CherenFault")
        $ ValueChange("Sabrina", -1, (0.4 if IsAbsent("Raihan") else 1.0/3.0))

        sabrina @talking2mouth "...Not wholly."

        if (timeOfDay == "Evening"):
            show sabrina sad with dis:
                xpos (0.4 if IsAbsent("Raihan") else 1.0/3.0)
        else:
            show sabrina sad at night with dis:
                xpos (0.4 if IsAbsent("Raihan") else 1.0/3.0)

        redmind @sadbrow frownmouth "[sabrinacolor]I'm sorry. I need... I need space. And time.{/color}"

    "It was those two students' fault.":
        $ AddEvent("Sabrina", "AceFault")
        $ ValueChange("Sabrina", -1, (0.4 if IsAbsent("Raihan") else 1.0/3.0))

        sabrina @talking2mouth "...Not wholly."

        if (timeOfDay == "Evening"):
            show sabrina sad with dis:
                xpos (0.4 if IsAbsent("Raihan") else 1.0/3.0)
        else:
            show sabrina sad at night with dis:
                xpos (0.4 if IsAbsent("Raihan") else 1.0/3.0)

        redmind @sadbrow frownmouth "[sabrinacolor]I'm sorry. I need... I need space. And time.{/color}"

    "It was your fault.":
        $ AddEvent("Sabrina", "YourFault")
        $ ValueChange("Sabrina", -5, (0.4 if IsAbsent("Raihan") else 1.0/3.0))

        sabrina @talking2mouth "...Not wholly."

        if (timeOfDay == "Evening"):
            show sabrina sad with dis:
                xpos (0.4 if IsAbsent("Raihan") else 1.0/3.0)
        else:
            show sabrina sad at night with dis:
                xpos (0.4 if IsAbsent("Raihan") else 1.0/3.0)

        redmind @sadbrow frownmouth "[sabrinacolor]I'm sorry. I need... I need space. And time.{/color}"

    "It was my fault.":
        $ AddEvent("Sabrina", "MyFault")
        $ ValueChange("Sabrina", 3, (0.4 if IsAbsent("Raihan") else 1.0/3.0))
        if (GetRelationshipRank("Sabrina") > 0):
            redmind sadbrow frownmouth "I'm sorry, Sabrina. You're right. I should have listened. But now the damage has been done, and I don't want to stop being friends with you."

            redmind "[sabrinacolor]Have you considered what {i}I{/i} want?{/color}"

            redmind "Do {i}you{/i} want to stop being friends?"

            if (timeOfDay == "Evening"):
                show sabrina sad with dis:
                    xpos (0.4 if IsAbsent("Raihan") else 1.0/3.0)
            else:
                show sabrina sad at night with dis:
                    xpos (0.4 if IsAbsent("Raihan") else 1.0/3.0)

            redmind "[sabrinacolor]...No. Maybe. I don't know. I just need... I need space. And time.{/color}"
        else:
            sabrina @talking2mouth "...Not wholly."

if (GetRelationshipRank("Sabrina") > 0):
    $ AddEvent("Sabrina", "WasFriend")
    $ RelationshipRankUp("Sabrina", "...?", 0)
    $ persondex["Sabrina"]["RelationshipRank"] = 0

pause 1.0

rosa @talkingmouth "I think we could all do with some space. And some time. Let's head back to the campus grounds, alright?"

sabrina -sad @closedbrow talking2mouth "Alright."

pause 1.0

sabrina @sad "I... I don't want to seem ungrateful."

sonia -sad @talking2mouth "You've been through a lot. Anyone would get it."

nessa @talkingmouth "I'm sure I'd feel the same."

if (IsPresent("Raihan")):
    raihan @talkingmouth "I just joined up to help a friend."
    raihan @closedbrow talking2mouth "I'm not really sure what your deal is, but we've got no beef. I don't expect any thanks. Just doing what I do."

sabrina @closedbrow sadmouth "I... I really am... I..."

rosa @sadbrow talkingmouth "Hey. It's alright. We understand."

pause 1.0

$ ValueChange("Sabrina", 3, (0.4 if IsAbsent("Raihan") else 1.0/3.0))

pause 1.0
    
if (timeOfDay == "Evening"):
    show eveningforest with vpunch
else:
    show midnightforest with vpunch

rosa @happy "Yahahaha!"

rosa -sad @talkingmouth "Oh, man, I can't believe we pulled that off! This was so risky, but so exciting, but so dangerous, but so {i}fun!{/i} This could be a new movie!"

if (IsAbsent("Raihan")):
    $ ValueChange("Rosa", 5, 0.05)

else:
    $ ValueChange("Rosa", 5, 1.0/6.0)

nessa -sad @talkingmouth "...I'm not going to say you were right, Rosa, but maybe doing the proactive thing was the right call. {i}This{/i} time."

if (IsAbsent("Raihan")):
    $ ValueChange("Nessa", 5, 0.85)

else:
    $ ValueChange("Nessa", 5, 4.0/6.0)

if (IsAbsent("Raihan")):
    $ ValueChange("Sonia", 5, 0.75)
else:
    $ ValueChange("Sonia", 5, 3.0/6.0)

sonia -sad @happy "The important thing is that we succeeded. Worse for wear or not, we set up a plan, and saw it through to the end. No quitting mid-way."

sonia @sadbrow talkingmouth "Kinda reminds you of the Galarian Stars, Ness?"

nessa @closedbrow talkingmouth "Hm."

if (IsPresent("Raihan")):
    $ ValueChange("Raihan", 5, 5.0/6.0)

    raihan @happy "So, uh, I'm glad that I got to be part of this wicked adventure and all. Really does remind me of the Galarian Stars, and how we all were in the beginning..."
    raihan @surprised "But could someone explain what this was all about? Who are you, Sabrina? Why did you run out here? What did you mean, exposing secrets?"
    raihan @closedbrow sadmouth "I kinda got the idea that you're a Mental, but--"

    nessa @talkingmouth "Uh, ixnay on the ental-May. They call them 'Espers' in this region."

    raihan @talking2mouth "Okay. ...Context?"

    sonia @sadbrow talkingmouth "Oh, where do we start...?"

call clearscreens() from _call_clearscreens_152
show blank2 with splitfade

pause 1.0

narrator "Everyone makes their way back to the infirmary, battered and bruised."

$ AddEvent("Sabrina", "Rescued")

if (IsPresent("Raihan")):
    $ AddEvent("Raihan", "WasRescueTeam")

$ rescuedsabrina = True
$ lastsaved = "Sabrina"
$ _rollback = True
$ renpy.block_rollback()

jump infirmary