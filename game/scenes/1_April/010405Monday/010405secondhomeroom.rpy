label secondhomeroom010405:

$ timeOfDay = "Evening"

play music "Audio/Music/Oak Intro.ogg" noloop
queue music "Audio/Music/Oak Class.ogg"

scene homeroom with Dissolve(2.0)

show oakbg with dis

$ renpy.transition(dissolve)
show screen currentdate
$ renpy.pause(1.5, hard=True)

narrator "You return to homeroom as the school day draws to a close."
redmind uniform "The day didn't feel like it dragged on for that long, but all things considered, I'm ready to call it.{w=0.5} Judging by the looks on everyone's faces, they look like they're ready, too."
narrator "The final period burns through while you listen to Professor Oak talk about rather trivial matters."
redmind @thonk "It's weird. I was expecting class with the professor to be a little more--how should I put it--fulfilling?{w=0.5} At least, that's what my other classmates were making it out to be earlier in the day."
redmind @thinking "But so far I haven't taken anything out of homeroom that's especially memorable, other than the scary speech about the school's graduation rate."

hide blank2

oak @talkingmouth "I can tell by the look in your eyes that you're all quite tired of listening to me prattle on."
oak @talkingmouth "To tell you the truth, I'm tired of it, too, ha ha!"
oak @talkingmouth "But before I dismiss you, let me give you all a welcoming gift as celebration for your acceptance into Kobukan Academy."

show pokeballs_full:
    alpha 0.0 xalign 0.5 yalign 1.0
    ease 1.0 alpha 1.0

$ renpy.pause(2.0, hard=True)

redmind @surprisedbrow frownmouth "Are those what I think they are?{w=0.5} If so, then this class just got a little more exciting."

oak @talkingmouth "Today, each of you will be taking home a Pokémon for yourself, courtesy of the academy!"

$ renpy.music.play("Audio/school_crowd.ogg", channel='crowd', loop=True, fadein=1.0)

oak @talkingmouth "In each of these Poké Balls that you will receive is a random unevolved, untamed Pokémon.{w=0.5} Consider them your homework for the next year."

show pokeballs_full:
    alpha 1.0
    ease 0.5 alpha 0.0

show blue uniform with dis

blue @talkingmouth "Hey, I got plenty of Pokémon back home already.{w=0.5} I don't need any more, especially unevolved ones."

oak @talkingmouth "{color=#0048ff}Regardless of what Pokémon you may already own, these Pokémon will be required to stay on hand for the rest of your time at Kobukan Academy.{/color}"
oak @talkingmouth "{color=#0048ff}At the end of the year, this Pokémon will be reviewed along with yourself and other potential Pokémon in your party to determine whether or not you can graduate.{/color}"

blue @angry "GREAT!{w=0.6} I just {i}love{/i} being forced to take on liabilities!"
show blue surprisedbrow frownmouth with dis

oak @talkingmouth "That's the spirit, [blue_name]!"

hide blue with dis

redmind "So that's how they do it.{w=0.5} I had assumed this school wasn't going to be all about good grades, so this isn't a complete shocker."

oak @talkingmouth "I'll call you up one by one to receive your Pokémon.{w=0.5} Remember, what you get is what you get!"

red @talkingmouth "This takes me back to when I was a kid and Professor Oak gave me [pika_name]."

$ renpy.music.play("Audio/pokemon/cries/37.mp3", channel="altcry", loop=None)

Character("Excited Student") "\"I got a Vulpix?!{w=0.5} WOOHOO!\""

redmind "Nice. Vulpix are pretty rare, so I bet whoever I get has to be at least equally as rare!"

oak @talkingmouth "[first_name]!"

$ renpy.music.set_volume(0.0, delay=1.0, channel="music")

redmind "Phew! Okay."
redmind @sweat closedbrow frownmouth "Here goes.{w=0.5} The moment of truth!"

show pokeballs_emptyA:
    alpha 0.0 xalign 0.5 yalign 1.0
    ease 1.0 alpha 1.0

redmind @sadbrow sweat "Knowing my luck, I'm {i}gonna{/i} end up getting a Rattata or Bidoof."
redmind @closedbrow frownmouth "Whatever gods are out there watching me, please, don't let me down!"
redmind @thinking "[ellipses]Wait."
redmind "The Poké Balls here are marked with National ID numbers. I've memorized {i}every{/i} Pokémon and their numbers. I can just... like, pick, whatever I want!"

pause 1.0

redmind "That means... I can influence my choice here. Sam knows that I know the National ID numbers of every Pokémon, right? Maybe he was giving me a leg up here."

menu:
    ">Pick from three random balls":
        $ starter_id = renpy.call("PickPokemon", "all")

    ">Pick from three Pokémon from your elective classes":
        $ starter_id = renpy.call("PickPokemon", "electives")

    ">Pick from three Pokémon from a specific type":
        call PickType() from _call_PickType
        $ starter_id = renpy.call("PickPokemon", _return)

    ">Pick a specific Pokémon":
        $ starter_id = renpy.call("PickPokemon", "every")

$ starter_id = _return
$ starter_name = pokedexlookup(starter_id, DexMacros.Name)

show blank with dis:
    alpha 1.0

pause 0.5

$ PlaySound("Pokemon/Ball sound.ogg")

oak @talkingmouth "Hmmm..."

hide pokeballs_emptyA

pause 1.5

$ startercry = "Audio/pokemon/cries/{}.mp3".format(starter_id)
$ renpy.music.play(startercry, channel="altcry", loop=None)

show pokeballs_emptyB behind blank:
    xalign 0.5 yalign 1.0

show blank:
    alpha 1.0
    ease 1.0 alpha 0.0

pause 1.0

$ renpy.music.play("Audio/Get.ogg", channel="XYgame", loop=None, fadeout=0.5)

show starterportraitfull at pokeball:
    align (0.5, 0.5)
    zoom max(1, (ReadHeight(starter_id) / 40.0))

$ starterobj = Pokemon(starter_id, shinylock=False)
$ playerparty.append(starterobj)
$ starter_species_name = playerparty[0].GetNickname()
$ starter_preposition = ("a" if starter_species_name[0] not in ["A", "E", "I", "O", "U"] else "an")
oak @happy "Congratulations, it's [starter_preposition] [starter_name]!"
oak @talkingmouth "This Pokémon is really quite energetic!"

if (ReadHeight(starter_id) > 48):
    oak @angry "...However, it's also quite large, for a baby. Would you mind getting it off my table?"
    red @surprised "Oh, shoot, sorry Sa-- I mean, Professor Oak. I'm just..."

$ renpy.music.set_volume(1.0, delay=1.0, channel="music")

red @surprised "I--{w=0.5}Wha--"
red @happy sweat"You're not pulling my leg, are you?"

oak @talkingmouth "I am not pulling anybody's leg.{w=0.5} It's in your care now."

red @happy "ALL RIGHT!"
$ starter_preposition = ("a" if starter_species_name[0] not in ["A", "E", "I", "O", "U"] else "an").title()
redmind @closedeyes frownmouth "[starter_preposition] [starter_name]?!{w=0.5} Today is my lucky day!"
redmind @closedeyes frownmouth "I didn't know what to expect, but everything somehow turned out better than I could have imagined."
redmind happy "Thank you! I knew the gods were looking after me!"

hide pokeballs_emptyB
hide starterportraitfull
hide blank2 
with dis

$ PlaySound("BellChime.ogg")

show leaf uniform at leftside with dis:
    xzoom -1

leaf @happy "Nice Pokémon, [first_name]!"

red @happy "Thanks!{w=0.5} I actually always wanted one. Did you get a Pokémon you wanted, too?"

leaf @talkingmouth "You bet I did!{w=0.5} Say hello to Bulbasaur!"

$ DisplayPokemon("Bulbasaur")

leaf @happy "Your [starter_name] should play with my Bulbasaur sometime."
leaf @flirttalk "It's only natural that our Pokémon should be best friends like their Trainers!"

$ PlaySound("pokemon/ball sound.ogg")
show sideportraitfull at backinpokeball

red @confused "Since when were we best fri--"
show leaf surprisedbrow frownmouth with dis

hide blue
show blue uniform at rightside with dis:
    xzoom -1

$ starter_preposition = ("a" if starter_species_name[0] not in ["A", "E", "I", "O", "U"] else "an")
blue @happy "You got [starter_preposition] [starter_name], [first_name]?{w=0.5} HA! That's perfect!"

show leaf flirtbrow with dis

red @sweat talking2mouth "I'm going to regret asking this, but... {w=0.5}{nw}" 
extend @confused "What's wrong with [starter_preposition] [starter_name]?"

blue @happy "Oh, nothing really..."
show leaf angrybrow frownmouth with dis
blue @angrybrow happymouth "Except it's not nearly as rare as my {i}Eevee!{/i} Ha ha ha ha!"

red @surprised "Wha?"

blue @happy "It must be divine retribution!"
blue @closedbrow talkingmouth "You're never gonna beat me, even at random draws! Ha ha!"
blue @happy "Once this Eevee evolves, I'll be able to beat any kind of team you try to set up against me! You're powerless!"

red @closedbrow talking2mouth "I mean, sure, if you want to evolve your Eevee to beat one particular trainer's team, knock yourself out."

blue @angry "Yo! Let's check out our Pokémon!{w=0.5} Come on, I'll take you on!"
show blue surprisedbrow frownmouth with dis

oak @talkingmouth "Blue! This isn't the time or place for that!"

blue @sad2eyes talkingmouth "Psh. Whatever, my Pokémon looks a lot stronger anyway!"
show blue surprisedbrow frownmouth with dis
show leaf surprisedbrow frownmouth with dis

show may uniform angrybrow frownmouth with dis

may @angry "Hey, leave him alone!{w=0.5} It's not nice to bully others!"

blue @closedbrow sweat talkingmouth "Oh. I, uh..."

may @angry "And for your information, there's a lot more to winning battles than type advantage!"

leaf -surprisedbrow -frownmouth @talkingmouth "Just ignore him.{w=0.5} What'd you get, May?"

hide blue with dis

$ renpy.pause(1.0, hard=True)

may -angrybrow -frownmouth @happy "A Torchic!{w=0.5} I love Fire-types so she and I are gonna be best buds, I just know it!"

leaf @happy "Ha ha! A Torchic really suits you, May!{w=0.5} I mean, your bow already kinda reminds me of their fuzzy heads."

may @surprised "Hey... you're right!" 
may @happy "You hear that, Torchic? This was fate!{w=0.5} You and me were meant to be!"

$ showredonly = True

whitney uniform @smile "You guys got starters? Luckyyy!"

show may:
    xpos 0.5
    ease 0.5 xpos 0.8

show leaf:
    xpos 0.25 xzoom -1
    ease 0.5 xpos 0.6 xzoom 1

show whitney uniform:
    xpos -0.5
    ease 0.4 xpos 0.4

show flannery uniform:
    xpos -0.5
    ease 1.0 xpos 0.2

pause 1.0

$ showredonly = False

red @talkingmouth "Starters are pretty cool, but every Pokémon can be great with the right trainer.{w=0.5} What Pokémon did you guys get?"

whitney @happy "A Cleffa!{w=0.5} It's a different kinda cute compared to my Miltank, but I'll take it!"
whitney @winkbrow talkingmouth "I heard these little tykes are really rare."

flannery @happybrow talkingmouth "I got a cute li'l Numel.{w=0.5} I'm taking the Fire and Ground electives, so this is just great!"
flannery @closedbrow talkingmouth "My family back in Lavaridge had tons of these. Somehow, I never got one. Might not be the best in battle, but I still love him."

whitney @talking2mouth "Really? Isn't it one of the few Pokémon in the world that can learn Eruption?"
whitney @surprised "I don't know all there is to know about Fire Pokémon, but isn't that move super good?"

flannery @happy "Sure!{w=0.5} But, I mean, Camerupt are {i}really{/i} slow. Still, they're super-fun to cuddle with!"

redmind @thinking "So... are we just going to overlook Flannery's 180-degree personality switch?"

show hilbert uniform sad behind leaf with dis:
    xpos 0.5 zoom 0.8

pause 2.0 

redmind @thonk "...Just going to lurk, huh?"

pause 1.0

show hilbert surprisedbrow with dis
red @happy "What about you, Hilbert?"

hilbert @surprised "Huh?"

show hilbert uniform sad behind whitney:
    xpos 0.5 zoom 0.8
    ease 0.5 zoom 1.0

show may:
    xpos 0.8
    ease 0.5 xpos 0.9

show leaf:
    xpos 0.6
    ease 0.5 xpos 0.7

show whitney uniform:
    xpos 0.4
    ease 0.5 xpos 0.3

show flannery uniform:
    xpos 0.2
    ease 0.5 xpos 0.1

hilbert @sadbrow talkingmouth "Oh...{w=0.5} I got a Cubchoo."

red @confused "Hey, a Unova 'mon.{w=0.5} Old territory for you, right?"

whitney @happy "Aw, Cubchoo are so adorable!"
whitney @talking2mouth sadbrow "...At least until they become Beartic."

whitney @sadbrow talking2mouth "Hey, are you gonna evolve your Cubchoo?"

hilbert @angrybrow talkingmouth "Probably."

whitney @sad "Aw, that's too bad..."

hide hilbert with dis

show may:
    xpos 0.9
    ease 0.5 xpos 0.8

show leaf:
    xpos 0.7
    ease 0.5 xpos 0.6

show whitney uniform:
    xpos 0.3
    ease 0.5 xpos 0.4

show flannery uniform:
    xpos 0.1
    ease 0.5 xpos 0.2


$ renpy.pause(0.6, hard=True)

may @happy "I can't wait to play with my Torchic!{w=0.5} She's gonna have so much fun with my Nincada when she gets here!"

flannery @surprised "We can bring our Pokémon here from home?"

leaf @talking2mouth "The Professor said that it doesn't matter what other Pokémon we have in our party, so yeah."
leaf @talkingmouth "I'm getting my Dratini and Helioptile sent here tomorrow morning."

leaf @closedbrow talking2mouth "It's so hard to get anything shipped into Kobukan, but I put some money aside a while ago, so we should be fine."

whitney @angrybrow talking2mouth "Tell me about it! Do you know how much it costs to find a Moon Stone in this region? It might actually be cheaper to just fly to Unova!"

may @talkingmouth "Well, the mining industry is--"

show leaf surprisedbrow frownmouth with dis
show may surprisedbrow frownmouth with dis
show whitney surprisedbrow frownmouth with dis
show flannery surprisedbrow frownmouth sweat with dis
oak @talkingmouth "What are you all still standing around for?{w=0.5} Class is over! Go on home already!"

show leaf:
    alpha 1.0 xpos 0.6
    ease 0.5 alpha 0.0

show flannery:
    alpha 1.0 xpos 0.2
    ease 0.5 alpha 0.0

show whitney:
    alpha 1.0 xpos 0.4
    ease 0.5 alpha 0.0

show may:
    alpha 1.0 xpos 0.8
    ease 0.5 alpha 0.0

$ renpy.music.stop(channel='crowd', fadeout=0.5)
$ renpy.pause(0.5, hard=True)

$ renpy.transition(dissolve)
call clearscreens from _call_clearscreens_10

window hide

stop music fadeout 2.5

scene blank2 with spinfade
$ renpy.pause(1.0, hard=True)

$ renpy.music.play("Audio/hall_crowd.ogg", channel='crowd', loop=True, fadein=1.75)
$ renpy.pause(2.0, hard=True)

scene academyhall with spinfade
$ renpy.pause(1.5, hard=True)

$ renpy.transition(dissolve)
show screen currentdate

show leaf uniform with dis

show may uniform at leftside with dis

leaf @happy "Mmm, sweet freedom!{w=0.5} What do you guys wanna do now?"
    
may @sadbrow happymouth "Sorry, I've got plans.{w=0.5} Brendan said he was hungry and wanted me to meet up with him in the cafeteria after classes."

leaf @surprised "But we just had lunch!"

leaf @flirttalk "You guys are gonna stuff your faces again?{w=0.5} You're gonna get fat!"

may @sadbrow happymouth "Well, {i}I'm{/i} not hungry, but Brendan wants me to come with him, so...{w=0.5} I mean, unless you guys want to come with me."

leaf @talkingmouth "Nah, I'm okay. {w=0.5}{nw}"
extend @flirttalk "I'm sure [first_name] and I can find something else to do!"

red uniform @confused "Huh?"
red @happy "Seems you may have just decided something for yourself again."

leaf @angrybrow talking2mouth "I dare you to tell me that you have plans today."

red @closedeyes happymouth "...Point."

show brendan uniform happybrow at rightside with dis

brendan @happymouth "Yo!{w=0.5} Let's go, May!"

may @happy "Oh, great!{w=0.5} Have fun, you two!"

show may:
    xpos 0.25
    ease 0.5 xpos 0.4

may @flirtbrow talkingmouth "Give me a call if you... {i}need anything{/i}, Leaf. {size=30}I have a massive stash in our dorm.{/size}"

leaf @flirttalk "{size=30}Good to know.{/size}"

hide may
hide brendan
with dis

leaf @happy "All right! Toodles!"

$ renpy.pause(1.5, hard=True)

leaf happybrow @happy "So, what do you wanna do?{w=0.5} I don't even really know what kind of stuff you like."

red @happy "Big fan of running."

leaf @happy "Great!{w=0.5} I won't be doing that."
leaf @closedbrow talking2mouth "Umm... {w=0.5}{nw}"
extend -happybrow @talking2mouth "Wanna hang out in the lobby while we think of a place to go?"

show leaf surprisedbrow frownmouth with dis

red @sadbrow talkingmouth "Sure, but I don't really know any place to go around here."

leaf @surprised "What are you talking about?"
leaf @happybrow talkingmouth"We can go to {color=#0048ff}the garden, the Recreation Center, the Research Center,{/color} or..."

pause 1.5

leaf -surprisedbrow -frownmouth @sarcastic "...Does any of this sound familiar to you?"

red @confused "A few friends of mine brought up the garden earlier, but for the rest... {w=0.5}{nw}"
extend @closedbrow talking2mouth sweat "Look, my research into Kobukan was more about academics and history than geography."

leaf @happy "Hmmm, I would've thought that maybe you wised up since the last time, but maybe your sense of direction is innately hopeless."
leaf @flirttalk "Luckily, you have me!{w=0.5} Let's break out the ol' map and take a look around the area."

$ renpy.music.play("Audio/Music/Show Me Around.ogg", channel='music', loop=True, fadein=1.0)

show academyhall_blur 
show mapdemo 
with dis

$ renpy.pause(1.5, hard=True)

leaf @talking2mouth "We're right here, over at the main building above the Student Center."
leaf @flirttalk "Now you see all the paths on the map?{w=0.5} Those are paths that we can take to get to the other--"

red @unamusedbrow talking2mouth "Look, despite the evidence to the contrary, I {i}do{/i} know how to read a map."

leaf @happy "All right, but if you have any questions about the area in general, just let me know!"

jump map_tutorial

label map_tutorial:

menu:
    extend ""
    "Which buildings are open to students?":
        leaf @talkingmouth "Well, right now all of them, more or less. With the exception of the Battle Hall, {color=#0048ff}they're all open to students throughout the day, but they close down at night.{w=0.5} After that, you'll need special permits.{/color}"

        red @talkingmouth "So basically once they're closed, I'll have to wait until the next day to get in."

        leaf @talking2mouth "Yeah, it's kinda lame, but {color=#0048ff}once they're closed, your activities will be limited to your dorm.{/color}{w=0.5} You should really try to make the most out of your day before that."
        leaf @talkingmouth "Anything else you'd like to know?"

        jump map_tutorial

    "What activities are there to do around here?":
        red @talkingmouth "Is there anything in particular that everyone enjoys?"

        leaf @talking2mouth "Not that I can think of.{w=0.5}"

        leaf @talkingmouth "There's plenty of stuff to do, but {color=#0048ff}it all depends on where you decide to visit.{/color}"
        leaf @talking2mouth "{color=#0048ff}Depending on what you do, some activities may take a little bit of time out of your day, or it may take up your entire day.{/color}{w=0.5} Try to manage your time well and plan ahead what you're going to be doing."

        leaf @flirttalk "Or if you're tired or just feeling lazy, you can {color=#0048ff}go back to your dorm after classes and just kill the rest of your time there.{/color}"
        leaf @surprised "I mean, that's only if you {i}really{/i} can't think of anything to do...{w=0.5} or if you have no friends."
        leaf @talking2mouth "Personally, I'd love to go out and do stuff, but this school has a strict curfew.{w=0.5}{nw}"
        extend @talking2mouth " So {color=#0048ff}once it's night, you can't leave the dorms.{/color}"
        
        red @talkingmouth "Yeah, I remember hearing about that on orientation day."

        leaf @talkingmouth "Anything else you'd like to know?"

        jump map_tutorial

    "What can you tell me about Inspira City?":
        red @talkingmouth "What can you tell me about Inspira City?"

        leaf @happy "It's got all these cool shops and markets to visit!"
        leaf @talking2mouth "It's every girl's paradise."

        leaf @flirttalk "But for someone like you...{w=0.5} I'd go {color=#0048ff}after I've become familiar enough with the campus.{/color}"
        
        red @closedbrow talking2mouth "I can't think of any reason to go to the city right now anyway."

        leaf @talking2mouth "Anything else you'd like to know?"

        jump map_tutorial

    "I'm good.":
        red @talkingmouth "All right, I got it.{w=0.5} Thanks for the help."

        leaf @happy "No problem!"

hide academyhall_blur
hide mapdemo
with dis

$ renpy.pause(1.5, hard=True)

leaf @talking2mouth "So, now that we got that all sorted out, where do you want to go?"

red @confused "Me?{w=0.25} I didn't say anything about going anywhere."

leaf @flirttalk "Oh, don't be shy! Come on, come on, let's go somewhere fun!"  
leaf @happy "It's not like you have any other plans right now anyway!"

red @talkingmouth "Oh, why not? You lead the way."

leaf @happy "Awesome!"
leaf @closedbrow talking2mouth "Let's see...{w=0.5} how about the gym?{w=0.5} Since the Battle Hall requires permission to battle there, I bet we can catch some cool battles in the gym!"
leaf @flirttalk blush "Besides, you look like you could use a good workout."

red @upeyes angryeyebrows talking2mouth "Hey!"

leaf @happy "I'm kidding!{w=0.5} It's obvious that you stay in shape. Probably go to the gym every day, right? And get all gross and sweaty, huffing and puffing like an overexerted Slowpoke?"

pause 2.0

red @closedbrow talking2mouth sweat "Leaf, I'm begging you, whoever taught you how to flirt, you need to stop listening to them."

leaf @happy "Hey, I don't get this from {i}anyone!{/i} My technique is 100\% a Leaf original! Homegrown and homemade! Fresh from the garden."

red @unamusedbrow talking2mouth "Your 'technique' puts me in the mood for fast food."

pause 1.0

leaf @sad "...What's fast food in this context?"

red @sigh "Let's not--"

leaf happy "Doesn't matter. Let's go!"

hide leaf with dis

pause 0.5

window hide

show blank2 with dis

$ renpy.transition(dissolve)
call clearscreens from _call_clearscreens_11
$ renpy.music.stop(channel='crowd', fadeout=1.5)
stop music fadeout 1.5
$ renpy.pause(2.0, hard=True)

############################################################################################################################################################################################################################
#### KORRINA INTRO #########################################################################################################################################################################################################
############################################################################################################################################################################################################################
#### NO IT ISN'T ###########################################################################################################################################################################################################
############################################################################################################################################################################################################################

play music "Audio/Music/Gym_Start.ogg" noloop
queue music "Audio/Music/Gym_Loop.ogg"

$ renpy.music.play("Audio/school_crowd.ogg", channel='crowd', loop=True, fadein=1.0)

$ renpy.transition(dissolve)
show screen currentdate

scene gym with Dissolve(2.0)

hide blank2

$ renpy.pause(1.0, hard=True)

show leaf uniform with dis

leaf @talkingmouth "Wow. Looooots of people here." 

red uniform @talkingmouth "Guess it makes sense. It's a good place to battle {i}and{/i} work out. All kinds would come here."

leaf @closedbrow talkingmouth "It's a bit crowded.{w=0.5} Maybe we should try somewhere..."
show leaf surprisedbrow frownmouth with dis

pause 1.5

red @confused "Hm? What's up?"

leaf surprisedbrow frownmouth @surprised "Hold the front door. Is that freakin' {i}ROSA?{/i}"

$ rosanamed = IsNamed("Rosa")

if (rosanamed):
    if (classstats["Electric"] > 0):
        red @confused "Huh? {w=0.5}{nw}" 
        extend @talkingmouth "Oh, yeah, it is. I mean, we took the Electric elective together before, right?"

        leaf @angry "What! That's a lie! There's {i}no way{/i} I didn't notice her."

    else:
        red @confused "Huh? {w=0.5}{nw}" 
        red @talkingmouth "Oh, yeah, it is. I met her earlier, in my elective class."

        leaf @angry "Shut {i}up!{/i} You did {i}not!{/i}"

    red @happy "Totally did."

    leaf @angry "Well... whatever! I'm going to talk to her!"

    red @confused "How do you know her?"

else:
    red @confused "Who's that?"

leaf @surprised "You're kidding me! You don't know Rosa? The Queen of Pokéstar Studios? One of the most talented actresses {i}ever?{/i}"

red @talking2mouth "Well, I didn't watch many movies back in Pallet Town. And most of what I watched was on VHS, which I'm guessing is a bit older than her."

leaf -surprisedbrow -frownmouth @happy "Oh my god, I have {i}so{/i} many movies to show you. She's legendary. There's one scene where her character in {i}Timegate Traveler{/i} gets buried under rubble, and her arm is torn off--"
leaf @happy "--and she screams and cries {i}so realistically{/i} that if the volume on your TV is too high, your neighbors will call the cops on you!"

red @confused "That's... that's great?"

leaf @embarrassedbrow talkingmouth "Oh, and this one time, when she was filming {i}Love and Battles{/i}, the guy who played her love interest {i}actually fell in love with her!{/i} He even proposed!"
leaf @happy "I read about it in a magazine."

red @confused "Huh."

pause 1.0

leaf @talking2mouth angrybrow "I better get more than a 'huh' for introducing you to the best actress who ever lived."

red @talking2mouth "It's just... I tend to prefer flicks like Diantha's more, you know?"

leaf surprisedbrow frownmouth @surprised "{w=0.5}.{w=0.5}.{w=0.5}."
leaf surprisedbrow @talking2mouth "Like... old black and white films?"

red @confused "How old do you think she is? No, modern stuff."
red @closedbrow talkingmouth "Although I guess I do like Brycen's old snowball westerns, too."

leaf "{w=0.5}.{w=0.5}.{w=0.5}."
leaf -surprisedbrow -frownmouth @closedbrow talking2mouth "I'm going to be the bigger woman here and let you have awful taste."
leaf @happy "Oh! That's another one of her films! 'The Giant Woman!'"

red @wince talking2mouth "Even without having seen it, I can tell that's the director's barely-disguised fetish."

leaf @closedbrow talkingmouth "Yeah, it really was..."

pause 2.0

leaf @happy "Well, whatever! I'm going to go talk to Rosa! And then we'll be best friends, and she'll cast me as an extra in her movies!"

red @happy "How mercenary."

show rosa with dis:
    xpos 0.66

show leaf:
    xpos 0.5 xzoom 1
    ease 0.5 xpos 0.33 xzoom -1

leaf @happy "Rosa!"

$ BecomeNamed("Rosa")

show leaf:
    xpos 0.33 xzoom -1

show rosa:
    xpos 0.66

rosa @surprised "Huh?"
rosa @talkingmouth "Oh, hi! You must be a fan."

leaf @surprised "I totally am! Your biggest fan! Oh, my gosh! It's Rosa!{w=0.25} It's really you!"

leaf @happy "[first_name], can you believe it?!"

red @happy "Sure can't!"

show rosa happybrow sweat with dis

leaf @embarrassedbrow talkingmouth "I've seen {i}all{/i} your interviews! You're amazing! Is it really true that when you were filming {i}Full Metal Cop{/i}, the International Police visited the studio, because they thought you {i}actually were{/i} an infamous jewel thief?"

rosa @talkingmouth "Ha ha! Maybe!"
rosa @closedbrow sweat talking2mouth "...But, for legal reasons, no."

leaf @happy "I'm like, your biggest fan {i}ever{/i}! Did I say that? Whatever, it's still true."

if (not rosanamed):
    leaf @happy "What are you doing here? Are you a guest speaker? Are you being hired to teach a class?"

    rosa @happy "Hah hah, what? No? I'm only twenty, you know. I'm just attending--"

    leaf @surprised "{i}*GASP*{/i} You're enrolled here?!{w=0.5} Pinch me, I'm dreaming!"
    
leaf @flirttalk "Hey, what dorm do you live in? Can I see your room sometime? Like, right now, maybe?"

redmind @unamusedbrow unamusedmouth "Alright, {b}now{/b} it's time to intervene."

show leaf surprisedbrow frownmouth with dis

red @sadbrow talkingmouth "Leaf.{w=0.5} Be cool."
    
leaf @surprised "But--"

rosa -sweat -happybrow @talkingmouth "Nah, it's okay.{w=0.5} I appreciate the enthusiasm, but I'm just a student here, like you!"
rosa @happy "If I'm not in front of a green screen, there's no reason to treat me any differently to anyone else."

leaf @sadbrow talkingmouth "Oh gosh, I'm sorry." 
leaf -surprisedbrow -frownmouth @happy "I just never thought my idol would wind up so close to me, and talking to me face-to-face no less..."

rosa @happy "Don't worry about it!"

pause 0.75

if (rosanamed):
    rosa @talkingmouth "...Hi, [first_name]."

    red @happy "Hey."

    rosa @sadbrow talkingmouth "I guess you get why I was a bit weird in class before, huh?"

    red @happy "I wouldn't say that, but it {i}does{/i} explain a couple things."
    
rosa @talkingmouth "Well, Miss, I don't think I caught your name.{w=0.5} Refresh me?"

leaf surprisedbrow frownmouth @surprised "Oh, I'm Leaf! Leaf's my name. And this is [first_name]! You can call him [first_name]. Kinda a silly name, right?"
      
rosa @surprised sweat "Silly? Um, I wouldn't-- I mean, that's not the first thing I would say..."

leaf @happy "I know! {i}Soooo{/i} silly! Hahahahaha? Ha!"

show leaf surprisedbrow frownmouth with dis

red @closedeyes talkingmouth "It's an unspoken rule to not throw your friends under the bus, Leaf. {w=0.5}{cps=*0.2}{nw}" 
extend @noeyes shadow frownmouth "{color=#f00}I'll remember this.{/color}"

show leaf sadbrow -frownmouth with dis

pause 1.5
    
rosa @surprisedbrow talking2mouth sweat "Whoa, look at the time!{w=0.5}{nw}" 
extend @sadbrow talkingmouth " Break's over. I need to get back to my workout! Every ounce of extra weight is an extra five weeks for the CGI team."
rosa @happy "Sorry, guys, I gotta run...{w=0.5} literally!"

show rosa happybrow sweat with dis
    
leaf -sadbrow @happy "Ha! That's a good one, Rosa!{w=0.5} Ha ha ha! My sides!"

rosa @talkingmouth "All right, nice meeting you, Leaf.{w=0.5} Catch you later!"

hide rosa at rightside with dis

pause 1.0

hide rosa

red @happy "She seems nice."

leaf -happy @talkingmouth "She is {i}so{/i} nice!"
leaf @happy "I've heard all these horror stories about actors being huge jerks offscreen, but Rosa obviously isn't anything like that!"

leaf @talkingmouth "If I could just end up being friends with Rosa by the time I graduate, I would be so happy."

red @talkingmouth "You guys seem like you'd get along well."

leaf @surprised "You really think so?"

red @happy "Sure. Just maybe lay off the brown-nosing a little."

leaf thinking @angrybrow talking2mouth "Excuse me?! I don't--"

pause 2.0

leaf -thinking @sadbrow talkingmouth "[ellipses]I'll try to keep it under control."

red @confused "So, do you still want to stay here?{w=0.5} This place looks packed."

leaf @talking2mouth "Yeah, definitely not."
leaf @talkingmouth "Let's try somewhere else."

hide leaf with dis

window hide

show blank2 with Dissolve(1.5)

$ renpy.transition(dissolve)
call clearscreens from _call_clearscreens_12
$ renpy.music.stop(channel='crowd', fadeout=1.5)
stop music fadeout 1.5
$ renpy.pause(2.5, hard=True)

show night at vspaz

pause 3.5

############################################################################################################################################################################################################################
#### END OF DAY ############################################################################################################################################################################################################
############################################################################################################################################################################################################################

play music "Audio/Music/SoaringIllusions_Intro.ogg" noloop
queue music "Audio/Music/SoaringIllusions.ogg"

$ renpy.transition(dissolve)
show screen currentdate

$ timeOfDay = "Night"

scene relichall_B with Dissolve(2.0)

hide blank2
hide night

show leaf uniform happy at night with dis

narrator "You end up wandering around the campus for a while, talking about nothing in particular."
narrator "Under the cover of idle chatter, night descends."

leaf frownmouth @surprised "Is it that time of day already?{w=0.5} Shoot, we need to head back to the dorms before we get in trouble."

red night uniform @sigh "I was wondering... is it that big a deal if we're caught outside after dark?"

leaf -surprisedbrow -frownmouth -surprised @sarcastic "Do it too often, and the Academy could suspend or even expel you.{w=0.5} Personally, I'd love to go out and do stuff, but with so much time and money at stake, it's just not worth it."
leaf @talking2mouth "Anyway, Kobukan's super-classy and junk, but Inspira's full of delinquents and thugs that wander over at night sometimes."
leaf -frownmouth @happy "Of course, my elite battling skills are more than enough to beat up anyone who tries something, but you might want to stay clear."

red @talking2mouth "I am very delicate, yes."

leaf @surprised "...Whoops! I didn't mean to ramble on for so long about that."
leaf @happy "It was fun while it lasted, but we should really head back in."

red @sadbrow talkingmouth "That's fine with me. Thanks for the tour, and, uh, tutorial on how to use maps."

leaf happy "G'night!"

hide leaf at night with dis

pause 2.0

redmind @thinking "Leaf wasn't kidding.{w=0.5} This place is like a ghost town once it gets close to curfew."

window hide

show blank2 with dis

$ renpy.transition(dissolve)
call clearscreens from _call_clearscreens_13

$ renpy.pause(2.0, hard=True)

$ renpy.transition(dissolve)
show screen currentdate

$ PlaySound("Door_Open1.ogg")
scene dorm_B norm with Dissolve(2.0)

hide blank2
hide relichall_B

red uniform @talkingmouth "Phew!"

$ PlaySound("Door_Close1.ogg")

red @happy "Finally back.{w=0.5} It's only the first day of class and I'm already feeling like sleeping the rest of the week away."
red @happy "Hey, guys!"

$ renpy.music.play("Audio/Pokemon/pikachu_norm1.ogg", channel="altcry", loop=None)

pikachu happy_3 "Pi-KA-chu!"

red @happy "Hey, [pika_name]! Did ya miss me?"

$ renpy.music.play("Audio/Pokemon/pikachu_norm4.ogg", channel="altcry", loop=None)

pikachu happy_3 "Pika-pika."

show calem at leftside with dis

calem @talkingmouth "I'd say he missed you.{w=0.5} Ever since I got back, he hasn't stopped staring at the door."

show brendan at rightside with dis

brendan @happy "He's like a little robot!"

calem @closedbrow talkingmouth "It's very endearing to watch, albeit a little unsettling."
calem smilemouth @talkingmouth "Anyway, how'd the day go for you, overall?"

red @happy "All things considered, it was all right.{w=0.5} I got a new Pokémon, so that was pretty cool."

calem @surprised "Oh? A new Pokémon? Fantastic!" 
calem @happy "I, myself, received a Fletchling in my homeroom with Professor Sycamore."

brendan @happy "Professor Birch gave me a Mudkip! When this li'l guy evolves into a Swampert, it'll be one of the best ground types from Hoenn!"

red @talkingmouth "I have homeroom with Hilbert, and he said he got a Cubchoo. Pretty sure he'll be beelining it into a Beartic, though."

show ethan with dis

ethan @happy "Well, what did you get?"

show ethan surprisedbrow frownmouth with dis
show calem surprisedbrow with dis
show brendan surprisedbrow frownmouth with dis
$ starter_preposition = ("a" if starter_species_name[0] not in ["A", "E", "I", "O", "U"] else "an")
red @happy "I got [starter_preposition] [starter_name]! Which is kinda crazy, because I always wanted one when I was a kid."
if (starter_name == "Mudkip"):
    red @happy "Looks like we've got two Mudkip in this dorm, now!"

pause 2.0

red @confused "What?"

show calem happy with dis
show brendan happy with dis
$ starter_preposition = ("a" if starter_species_name[0] not in ["A", "E", "I", "O", "U"] else "an")
ethan happy "Dude, I got [starter_preposition] [starter_name] as well!"

show brendan -happy with dis
show calem -happy with dis
red @happy "No shit? Huh! The coincidences just keep piling up between us."
if (starter_name == "Mudkip"):
    red @talkingmouth "I can't believe that three of the five of us ended up with Mudkip! Crazy."

ethan @talkingmouth "So true."
ethan @happy "Hey, you guys, the craziest thing happened. We both picked the same electives today! Same order and everything!"

calem @closedbrow talkingmouth "Hm... the odds of that are quite low."

if (GetStatRank(0) in classdex["Calem"] and GetStatRank(1) in classdex["Calem"]):
    calem @happy "Although [first_name] and I actually had the same electives, as well."
elif (GetStatRank(0) in classdex["Brendan"] and GetStatRank(1) in classdex["Brendan"]):
    brendan @surprised "Huh, what're the odds that Ethan, [first_name] and I all had the same electives?"

    calem @happy "Even lower."

red @talkingmouth "Well, how are you all feeling about classes?"

calem @closedbrow talking2mouth "It's been fairly uneventful thus far.{w=0.5} Not all that different from high school, to be honest."
calem @happy "But a lot of people say change isn't always a good thing, so perhaps I should count my blessings."

brendan @sadbrow talking2mouth "Man, I just know that these classes are gonna kill me."
brendan @closedbrow sweat talking2mouth "I've never felt so much academic pressure in my life!"

calem @sad "Truly? It {i}is{/i} only the first day of class.{w=0.5} Don't you think that it's a bit too early to decry the insurmountable wall?"

brendan @sad "Hey man, I'm not the sharpest tool in the shed, so any class from this place is tough for me at this point, you know?"

ethan @confused "I basically feel... well, like nothing's actually started yet!"
ethan @happy "I mean, the classes haven't had any tests, we haven't had any battles, we haven't had to catch any new Pokémon...! It's like we're still in the tutorial!"

brendan frownmouth sadbrow @sad "Aw, man, I'm having trouble in the {i}tutorial{/i}? I'm doomed, man..."

narrator "You and your roommates spend a while assuring Brendan that he is not, in fact, doomed."

show brendan -frownmouth -sadbrow with dis

narrator "Eventually, the conversation wraps back around to your new Pokémon, and..."

$ starter_name = pokedexlookup(starter_id, DexMacros.Name)
red @happy "Come on out, [starter_name]!"

$ PlaySound("Pokemon/Ball sound.ogg")

show starterportraitfull at pokeball, dormdesk
show calem:
    xpos 0.25
    ease 0.5 xpos 0.1

show ethan:
    xpos 0.5
    ease 0.5 xpos 0.25

show brendan:
    xpos 0.75
    ease 0.5 xpos 0.8

$ renpy.pause(0.5, hard=True)
$ renpy.music.play("Audio/pokemon/cries/{}.mp3".format(starter_id), channel="altcry", loop=None)

$ startercrop = starter_name[:3]
starter @talkingmouth "[startercrop]!"

redmind "Hmm. Now that I think about it, should I give you a nickname?"

label nicknamestarter:

$ starter_name = renpy.input("{color=#e70000}Your starter's nickname? (Press Enter for the default){/color}", length=12, exclude="{}[[]%<>",)
$ starter_name = starter_name.strip()

if starter_name == "" or starter_name == pokedexlookup(starter_id, DexMacros.Name).lower():
    $ starter_name = pokedexlookup(starter_id, DexMacros.Name)

red @closedbrow talking2mouth "Hm... I think [starter_name] would suit you just fine."

menu:
    "Yeah, that'll do, [starter_name].":
        pass

    "Wait, I've got a better idea.":
        jump nicknamestarter

$ playerparty[0].Nickname = starter_name

red @talkingmouth "Welcome to the team, [starter_name]!"
    
$ renpy.music.play("Audio/pokemon/cries/{}.mp3".format(starter_id), channel="altcry", loop=None)

$ species_name = pokedexlookup(starter_id, DexMacros.Name)
starter @talkingmouth "[species_name]!"

$ startergender = "he" 
if (playerparty[0].GetGender() == Genders.Female):
    $ startergender = "she"
elif (playerparty[0].GetGender() == Genders.Unknown):
    $ startergender = "it"

brendan @happy "Wow! Look at that, [startergender] likes you already!"
brendan @talking2mouth "It's not too often you find a Pokémon that gets chummy with its Trainer so soon after meetin' him."

red @confused "Really?{w=0.5} Huh. I never noticed. [starter_name]'s acting basically the same as [pika_name] did all those years ago."

brendan @surprised "R-really? Huh...{w=0.5} Maybe my Pokémon just don't trust me, then?"

calem @closedbrow talkingmouth "No, I don't think that's it. I was actually quite surprised when you let [starter_name] out in this room, [first_name]. I thought we'd have to duck for cover."

$ startergendercap = startergender.capitalize()
red @confused "What do you mean? [startergendercap]'s a baby Pokémon. [startergendercap] can't cause {i}that{/i} much damage."

calem @sad "True, but, more to the point... [startergender]'s not causing {i}any{/i} damage."

$ startergenderpronoun = "him" 
if (playerparty[0].GetGender() == Genders.Female):
    $ startergenderpronoun = "her"
elif (playerparty[0].GetGender() == Genders.Unknown):
    $ startergenderpronoun = "them"

ethan @confused "Hold on, I'm confused, now. You guys are acting like you expected [first_name]'s buddy to just go berserk as soon as he let [startergenderpronoun] out."

calem @surprised "Why, were you not? [startergendercap]'s a baby Pokémon, as you've said. [startergendercap] hasn't received even a modicum of training. But [startergender]'s just... {i}being{/i} there, patiently."

ethan @happy "Calem, you're pulling our leg, right? That's literally just how Pokémon are."

calem @angrybrow talking2mouth "I assure you, the numerous baby starter Pokémon Professor Sycamore foisted on me during my internship would beg to disagree."

brendan @closedbrow talkingmouth "Man, I dunno what to think now. Every Pokémon I've ever had took weeks to feel comfortable around me." 
brendan frownmouth @sad "I thought that was normal, but with you two saying the opposite, maybe I'm just bad at Pokémon."

show brendan:
    xpos 0.8
    ease 0.5 xpos 0.7

show hilbert at dissolvein:
    xpos 0.8

hilbert @talkingmouth "You probably are."

calem @angry "Hilbert!"

hilbert @talkingmouth "Let me finish."

hilbert @talkingmouth "Whether anyone here is good or bad at Pokémon, Ethan and [first_name]'s experience is not typical." 
hilbert @talkingmouth "If we were to all let our new Pokémon out right now, this room would become a disaster."
hilbert @talkingmouth "...So you are not one of the odd ones out here, Brendan."

brendan happy "Hah, sweet!"

pause 1.0

brendan -happy @closedbrow talking2mouth "Hey, wait, isn't being one of the odd ones out a good thing, here?"

red @confused "Maybe we can ask Professor Oak about it. I wanted to ask him some questions earlier, anyway."

red @surprised "Actually... Ethan, which homeroom do you have? Given we got the same starter and electives, I'm really surprised we don't have the same homeroom."

ethan @surprised "Oh, yeah! I'm, uh... with Kr--{w=0.5} I mean,{w=0.25} uh,{w=0.25} Professor Cherry."

red @closedbrow talking2mouth "Hm. I don't remember that name from the faculty page."

ethan @happy "Yeah, she was a new hire. And she's... well, she's a lot."

red @talkingmouth "Anyway, I'll see if I can get to homeroom early tomorrow, and ask Old Man--{w=0.5} I mean,{w=0.25} Professor Oak,{w=0.25} about why our Pokémon are weird."

redmind @thinking "Or not weird, I guess."

ethan @happy "Sounds like a plan! Now, I'm going to turn in. Night, all!"

hide hilbert
hide brendan
hide calem
hide ethan
with dis

red @talkingmouth "Sounds good.{w=0.5} What about you two? Ready for bed?"

$ renpy.music.play("Audio/Pokemon/pikachu_norm3.ogg", channel="altcry", loop=None)

pikachu happy "Pika."

$ renpy.music.play("Audio/pokemon/cries/{}.mp3".format(starter_id), channel="altcry", loop=None)

$ starter_fragment = pokedexlookup(starter_id, DexMacros.Name)[:3]
starter @talkingmouth "[starter_fragment]!"

window hide

$ PlaySound("Pokemon/Ball sound.ogg")

show starterportraitfull at backinpokeball, dormdesk

pause 1.0

show dorm_B lightsout

pause 1.0

$ renpy.transition(dissolve)
call clearscreens from _call_clearscreens_14

show blank2 with transeye

narrator "As you crawl into bed, you do not even have time to realize just how exhausted you are.{w=0.5} Not even a minute after your head hits the pillow, you fall into a deep sleep."

window hide

stop music fadeout 1.0
$ renpy.pause(1.0, hard=True)

hide dorm_empty_B
hide blank2

jump day010406
