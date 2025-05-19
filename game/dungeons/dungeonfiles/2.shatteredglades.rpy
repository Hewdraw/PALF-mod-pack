#######SETUP###########

label shatteredglades: #fighting-type dungeon, should be medium-difficulty, partners are Leaf, Flannery, and Whitney

if (timeOfDay == "Night"):
    show leaf at rightside, night
    show flannery at leftside, night
    show whitney at night
    with dis

else:
    show leaf at rightside
    show flannery at leftside
    show whitney
    with dis

leaf @happy "Alright, let's go! The Tia untrapment team is ready to roll out!"

if (timeOfDay == "Night"):
    red night @confused "'Untrapment'?"

else:
    red @confused "Untrapment?"

leaf @sarcastic "You try coming up with a word that means 'rescue' and begins with 'T.'"

whitney @talkingmouth "Does everyone have everything they need? I've got some bandages and antiseptics, in case we get bonked by anything in there, but we should still be careful."

flannery @talking2mouth "I looked ahead. According to this old forum post from a former student, this part of the forest is called the 'Shattered Glades.'"

leaf @surprised "Woah, edgy name. Why?"

flannery @closedbrow talking2mouth "There's a bunch of really hard ironwood trees in this part of the forest. Fighting-types gather to train here by punching the trees, and they end up smashing trees all over the place."
flannery @talkingmouth "Of course, there's also a bunch of Grass-types. It {i}is{/i} a forest."

leaf @closedbrow talking2mouth "Hm. Alright. Sounds like Flying-types would be useful in here, then..."

whitney @angry "Alright, enough standing around! Are we going to {i}do{/i} this thing?"

menu:
    "Hell yeah!":
        leaf @happy "She helped us out, [first_name]--now it's our turn!"

        whitney @talkingmouth "I'm responsible for Tia. So I've gotta pull her out of whatever trouble she's in!"

        flannery @closedbrow talkingmouth "She's our little sister. And we gotta take care of her. Time to wake up and smell the coffee."
        flannery @sadbrow talkingmouth "Although, to be honest, I'm still having some difficulty believing she's a dragon."

    "Just one moment.":
        hide whitney
        hide leaf
        hide flannery
        with dis

        if (timeOfDay == "Night"):
            jump aftersetupnight

        else:
            jump aftersetup

python:
    dungeon = Dungeon(name = "Shattered Glades",#a string
        endname = "Splintered Copse",#a string
        backgrounds = {"Night" : "midnightforest", "Default": "eveningforest"},#a dictionary of timeofdays to check against. If the current timeofday is not listed, then the "Default" value is picked.
        music = ("audio/music/duskforest.ogg"),#a tuple that contains one or two elements. If it contains two, the first is nolooped, and the second is looped. if it contains one, then it's looped
        encounterpool = {# a dictionary encounterpool, in the same format as the ones for normal wildareas
            pokedexlookupname("Makuhita", DexMacros.Id) : 5, 
            pokedexlookupname("Mankey", DexMacros.Id) : 10, 
            pokedexlookupname("Rowlet", DexMacros.Id) : 1,
            pokedexlookupname("Meditite", DexMacros.Id) : 7,
            pokedexlookupname("Paras", DexMacros.Id): 10,
            pokedexlookupname("Foongus", DexMacros.Id): 7
        },
        difficulty = 17,#an int, 1-100, indicating the dungeon's difficulty. Should be roughly equivalent to AimLevel()
        floors = 4,#the number of battles you need to win to go through the level
        floorlength = 5,#the number of turns a battle will last, at max, before you find the stairs
        levelrange = range(12, 16),#a level range, set up the same way as normal wildarea level ranges
        startingmysteriosity=5,#the base chance that mysteriosity happenings will occur
        startingferocity=30,#the base chance that strong Pokémon will appear
        startinggenerosity=60,#the base chance that good things will happen
        trainers=["Leaf", "Whitney", "Flannery"],# the trainers you start this dungeon with, not counting red
        cutscenefunc=ShatteredGladesCutscenes,#the function that returns the cutscene labels you should jump to
        godmodder=None,#manually calls events and outcomes if certain conditions are met
        lootlist = {#the dictionary of loot that you should get from this
            Item.GimmighoulCoin : 20, 
            Item.CheriBerry : 10, 
            Item.OranBerry : 10, 
            Item.SitrusBerry : 7, 
            Item.BlackBelt : 5, 
            Item.MiracleSeed : 5,
            Item.BlackApricorn : 3,
            Item.BlueApricorn : 3,
            Item.GreenApricorn : 3,
            Item.RedApricorn : 3,
            Item.WhiteApricorn : 3,
            Item.PinkApricorn : 3,
            Item.YellowApricorn : 3 })

call wildarea(dungeon) from _call_wildarea_11

jump AfterShatteredGlades

######GODMODDER & CUTSCENES###########

init python:
    def ShatteredGladesCutscenes(parameters):
        currentscene = None
        
        tiafainted = False
        for mon in FaintedMons:
            if (mon.GetId() == pokedexlookupname("Latias", DexMacros.Id)):
                tiafainted = True

        if (parameters == "DungeonTurn4"):
            currentscene = "ShatteredGladesBossIntro"
        elif (parameters == "DungeonBattle4"):
            currentscene = "ShatteredGladesBoss"
        elif (len(EnemyBattlers()) == 1 and EnemyBattlers()[0].Id == 380):
            currentscene = "ShatteredGlades1"
        elif (tiafainted):
            currentscene = "ShatteredGlades2"

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

label ShatteredGladesBossIntro:
    stop music fadeout 1.5
    queue music "audio/music/potown_start.ogg" noloop
    queue music "audio/music/potown_loop.ogg"

    if (timeOfDay == "Night"):
        scene midnightforest
        show leaf at rightside, night
        show flannery at leftside, night
        show whitney sadbrow frownmouth at night
        with dis

    else:
        scene eveningforest
        show leaf at rightside
        show flannery at leftside
        show whitney sadbrow frownmouth
        with dis

    flannery @happy "Wow! We made it through! Wasn't that {i}great?!{/i}"

    whitney @sad "Noooo! I never want to do that again! My feet hurt, and I'm all sweaty, and a million different branches poked me, and I hate the wild!"

    leaf @talking2mouth "Whitney, I'm not the biggest fan of the outdoors, either, but aren't you being a bit tough on mother nature?"

    whitney @closedbrow surprisedmouth "No! Mother Nature's a bitch! I never want to see her, ever again!"

    flannery @sweat talkingmouth "I mean... we still need to get back out after we find Tia..."

    whitney @sadeyebrows sad2eyes talking2mouth "...Right. For Tia. Mmmrgrrgrr..."

    if (timeOfDay == "Night"):
        show flannery surprised:
            xpos 0.25
        show whitney surprised at night
        with dis
    else:
        show flannery surprised:
            xpos 0.25
        show whitney surprised
        with dis

    leaf surprised "Wait... oh, wow, our job just got a lot easier!"

    flannery @angryeyebrows talking2mouth "Wait, do you mean..."

    stop music fadeout 1.5
    queue music "audio/music/reliccastle_start.ogg" noloop fadein 1.0
    queue music "audio/music/reliccastle_loop.ogg"

    hide flannery
    hide whitney
    hide leaf
    with dis

    pause 1.0

    if (timeOfDay == "Night"):
        show latias poweredangryeyes powered angrymouth at night with Dissolve(1.0):
            ypos 1.0 xpos 0.5
            parallel:
                ease 2.0 ypos 1.05
                ease 2.0 ypos 1.0
                repeat

            parallel:
                ease 2.0 xpos 0.52
                ease 2.0 xpos 0.5
                ease 2.0 xpos 0.48
                ease 2.0 xpos 0.5
                repeat

    else:
        show latias poweredangryeyes powered angrymouth with Dissolve(1.0):
            ypos 1.0 xpos 0.5
            parallel:
                ease 2.0 ypos 1.05
                ease 2.0 ypos 1.0
                repeat

            parallel:
                ease 2.0 xpos 0.52
                ease 2.0 xpos 0.5
                ease 2.0 xpos 0.48
                ease 2.0 xpos 0.5
                repeat

    $ PlaySound("pokemon/cries/380.mp3")

    latias "...Ra! Rati, lati, tiiii-AS!"

    pause 1.0

    if (timeOfDay == "Night"):
        leaf night @sadbrow surprisedmouth "Oh, no, what's happening to her?! Why's she screaming like that?"

        whitney night @sad "It's like she's been possessed!"

        red night @sad "Tia...!"

        flannery night @surprised "Holy shit, she actually {i}is{/i} a dragon?!"

    else:
        leaf @sadbrow surprisedmouth "Oh, no, what's happening to her?! Why's she screaming like that?"

        whitney @sad "It's like she's been possessed!"

        red @sad "Tia...!"

        flannery @surprised "Holy shit, she actually {i}is{/i} a dragon?!"

    latias @closedeyes "Laaaat... ti, {i}ti{/i}, TI!"

    pause 1.0

    latias soullesseyes talking2mouth "{i}Latias.{/i}"

    leaf @surprised "Uh-uh-uh-- she's coming right for us!"

    flannery @angry "Dragon or not, let's save our friend!"

    whitney @angry "[bluecolor]Tia doesn't know any attacking moves...{/color} so don't worry about her! Just beat down her team!"
    whitney @sadbrow talking2mouth "Although... just stating {i}all{/i} our options here... but if we knock her out, her other Pokémon will probably give up."

    flannery @furious "Whitney!"

    hide tia 
    hide whitney 
    hide leaf
    hide flannery
    with dis

    return

label ShatteredGladesBoss:
    python:
        dungeon.Reinforcing = False
        goodguys = dungeon.GetTrainers()
        tiaobj = Pokemon("Latias", nickname = "Tia", level=70, item="Soul Dew", ivs=[15, 15, 15, 15, 15, 15], gender=Genders.Female, moves=[GetMove("Sweet Kiss"), GetMove("Light Screen"), GetMove("Reflect"), GetMove("Heal Pulse")], nature=Natures.Bashful, intelligence = 1)
        tiaobj.ApplyStatus("tyrannic")
        tiaparty = GetTrainerTeam("Tia")
        tiaparty.insert(2, tiaobj)
        
        badguys = []
        for mon in tiaparty:
            badguys.append(Trainer("latias", TrainerType.Enemy, [mon], number=1))

    call Battle(goodguys + badguys, uniforms=False, customoutfits=False, healParty=False, specialmusic="Nothing", canBeDitto=False, dungeon=dungeon) from _call_Battle_126

    return

label ShatteredGlades1:
    hide screen battle
    show screen battleui
    hide latias
    with dis

    narrator "Tia is out of useable Pokémon... Tia blacked out!"

    $ EnemyBattlers()[0].Health = 0

    show screen battleui with dis
    with dis
    return

label ShatteredGlades2:
    hide screen battle
    show screen battleui
    hide latias
    with dis

    narrator "Tia's Pokémon are trainerless... without direction, it's easy to defeat them!"

    python:
        for mon in EnemyTrainers()[0].GetTeam():
            mon.Health = 0

    show screen battleui with dis
    with dis
    return

###########CUSTOM EVENTS CALLED BY GODMODDER############

# None


##########WRAP-UP SCENE##########

label AfterShatteredGlades:

stop music fadeout 1.5
queue music "audio/music/TiaTheme_start.ogg" noloop 
queue music "audio/music/TiaTheme_loop.ogg"

if (timeOfDay == "Night"):
    scene midnightforest
    show leaf sadbrow frownmouth at night:
        xpos 0.8 ypos 1.0 zoom 1.0 rotate 0
    show latias closedbrow frownmouth behind leaf at night:
        xpos 0.6
    show whitney frownmouth at night:
        xpos 0.4
    show flannery frownmouth at night:
        xpos 0.2
    with dis

else:
    scene eveningforest
    show leaf sadbrow frownmouth:
        xpos 0.8 ypos 1.0 zoom 1.0 rotate 0
    show latias closedbrow frownmouth behind leaf:
        xpos 0.6
    show whitney frownmouth:
        xpos 0.4
    show flannery frownmouth:
        xpos 0.2
    with dis

pause 1.0

leaf -sadbrow @talkingmouth "Did we... did we hit her too hard...?"

whitney @talking2mouth "Nah, she's fine. She's just fainted, same as any other Pokémon."
whitney -frownmouth @happy "A revive should fix this right up!"

latias @sadeyes "{w=0.5}.{w=0.5}.{w=0.5}."

latias surprised "!"

if (timeOfDay == "Evening"):
    hide latias
    show tia surprised:
        xpos 0.6
    with gaussdissolve
else:
    hide latias
    show tia surprised at night:
        xpos 0.6
    with gaussdissolve

tia "Hi, Whitney, Flannery! I must've... um... fallen asleep."

flannery @tiredbrow talking2mouth "You... fell asleep."

tia sadbrow "Yep. I fell asleep under my very realistic dragon blanket."

if (timeOfDay == "Evening"):
    redmind @confusedeyebrows frownmouth "I'm going to assume Tia {i}just{/i} learned about lying."

    show tia angrybrow frownmouth with dis:
        xpos 0.6
else:
    redmind night @confusedeyebrows frownmouth "I'm going to assume Tia {i}just{/i} learned about lying."

    show tia angrybrow frownmouth at night with dis:
        xpos 0.6

flannery @talkingmouth "...Looked more like a bird."

tia @angry "I'm not a bird! Don't call me a bird! I'm--Whitney, I know you're leaving something out, translate {i}everything{/i} I'm saying!"

whitney @talking2mouth "Relax, Tia. It's alright. Flan knows about you."

flannery @sad2eyes angryeyebrows talking2mouth "{size=30}Yeah, but I was the last one to learn, {i}again.{/i}{/size}"

tia surprised "What?"

whitney @talkingmouth "Pretty much the entire nurse program knows, too."

tia "Oh."

pause 1.0

tia sadbrow frownmouth "Oh."

flannery @sad "What's wrong? What {i}really{/i} happened?"

tia @closedeyes angrymouth "I don't... I don't remember exactly what happened, but... I think I started getting a headache, and then... someone attacked me! Yeah, I was attacked!"
tia @downeyes talking2mouth "And when I was attacked... I lost my hat."

whitney @sadbrow happymouth "Again?"

leaf @sadbrow happymouth "It's alright, sweetie. I'll buy you another."

tia @sadbrow talking2mouth "Thanks..."

flannery @talking2mouth "Before we go shopping, though, we need to get back to the school."

whitney @happy "Don't worry! I've got tons of potions. We'll be fine."

red @confused "Um... Couldn't Tia just fly us out of here?"

tia @talkingmouth "...Yes. I could."

red @talkingmouth "Got enough energy for it?"

tia @happy "Sure do!"

pause 2.0

tia frownmouth @confusedeyebrows "Am I flying?"

leaf @sarcastic "No."

tia @sadbrow -frownmouth "Oh. I guess I don't."

flannery @happy "The old-fashioned way it is, then. Good! I've got more than enough energy left to burn! This reminds me of hikes down the east side of Lavaridge."

whitney sad tears "Noooo! I haaaate the wiiiiiild!"
    
whitney -sad -tears @talkingmouth "...Although, um, serious time. My feet are really sore, and I can't just spray a potion on myself. [first_name], you were a massive help. Do you think you could do just one more thing and--" 

$ ValueChange("Whitney", 5, 0.4)

red @closedbrow sweat talkingmouth "Not a chance."

whitney sad tears "Ah, boo!"

flannery -frownmouth @talking2mouth "Man, I forgot how good it feels... I should {i}really{/i} get out like this more. Thanks Whit, Leaf, [first_name]."

$ ValueChange("Flannery", 5, 0.2)

leaf -frownmouth @talkingmouth "Hey, we got the mission done, together, just like I said. I'm two for two on rescue missions right now! Not bad, if I say so myself."

$ ValueChange("Leaf", 3, 0.8)

red @talkingmouth sweat closedbrow "Yeah, yeah, pat yourself on the back a bit harder. C'mon, let's get back to the school."

call clearscreens() from _call_clearscreens_153
show blank2 with splitfade

pause 1.0

narrator "Everyone makes their way back to the infirmary, battered and bruised."

$ AddEvent("Tia", "Rescued")
$ rescuedtia = True
$ lastsaved = "Tia"
$ _rollback = True
$ renpy.block_rollback()

jump infirmary