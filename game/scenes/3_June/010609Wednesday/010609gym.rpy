label gym010609:

play music "Audio/Music/Gym_Start.ogg" noloop
queue music "Audio/Music/Gym_Loop.ogg"

show screen currentdate
scene gym 
with dis

$ renpy.pause(2.0, hard=True)

show alder with dis:
    xpos 0.66

show bruno think with dis:
    xpos 0.33

alder @norm2 "Good morning, students."

redmind uniform @thinking "Hm... more subdued than usual."

alder @norm4 "I've been doing some thinking about battles. We talked yesterday about 'good battles,' and what kind of battle could be considered 'well-fought.'"

alder @talking2mouth "I'd like to tell you a story about what fighting well means to me."
alder @happy2 "It was early 2003. February, I think. I was still Champion of Unova... heh, 'Leader of the Free World,' they called me."
alder @closedbrow talking2mouth "C'mon out, Volcarona."

$ renpy.music.play("Audio/Pokemon/Volcarona_Ball.ogg", channel="altcry", loop=None)

show alder:
    xpos 0.66
    ease 0.5 xpos 0.75

show bruno:
    xpos 0.33
    ease 0.5 xpos 0.25

show volcarona at pokeball behind alder:
    xpos 0.5 ypos 1080 zoom 1.8

$ renpy.pause(1.0, hard=True)

show volcarona:
    subpixel True
    zoom 1.8 ypos 1080 xpos 0.5
    block:
        parallel:
            ease 1.0 ypos 900
            ease 1.3 ypos 1040
            ease 0.9 ypos 930
            ease 1.5 ypos 1080
            ease 1.2 ypos 905
            ease 1.4 ypos 1160
        parallel:
            ease 0.8 xpos 0.48
            ease 1.4 xpos 0.51
            ease 1.1 xpos 0.52
            ease 1.6 xpos 0.51
            ease 1.25 xpos 0.49
            ease 1.3 xpos 0.5
        repeat

alder @talkingmouth "Volcarona and I had heard stories about this challenger who was blitzing through the Unovan League."
alder @happy2 "Frankly, we didn't believe most of 'em! The stories seemed to contradict each other."
alder @talking2mouth "Some people said that the challenger was a dainty princess. Others said she was a fearsome dragon."

pause 1.0

alder @talking2mouth "Well, we were interested, but I'd walked Unova for four years, and hadn't heard anything about this challenger."
alder @happy2 "If she was defeating the league as fast as it sounded, she must've been preparing for a long time. And since I hadn't heard of her, I thought I'd slip on my sandals, grab my Pokémon, and check her out for myself."

pause 1.0

stop music fadeout 1.5

alder @sadbrow talkingmouth "Thing is, though[ellipses] we never got the chance."

$ sidemonnum = pokedexlookupname("Volcarona", DexMacros.Id) 

$ PlaySound("pokemon/cries/{}.mp3".format(sidemonnum))

sidemon "Vol! Carona!"

queue music "audio/music/aldertheme.ogg" fadein 2.5

narrator "Alder's Volcarona flaps its wings, and in the heat haze, you swear you can see images moving[ellipses]"

show screen songsplash("Alder's Theme", "Zame")

call clearscreens() from _call_clearscreens_277
scene blank with transeye2

python:
    calDate = calDate.replace(day=17, month=2, year=2003)
    timeOfDay = "Evening"
    playercharacter = "Alder"
    oldinventory = copy.copy(inventory)
    oldpersonalstats = copy.copy(personalstats)
    oldparty = copy.copy(playerparty)
    oldpersondex = copy.copy(persondex)
    oldclassstats = copy.copy(classstats)

    inventory = {
        Item.PokeBallGarland : 1,
        Item.SacredAshes : 1,
        Item.TheRedButton : 1,
        Item.HikingStick : 1,
        Item.AnkleBrace : 1,
        Item.SparePoncho : 1,
        Item.MacaroniArt : 1
    }

    personalstats = {
        "Charm" : 76,
        "Knowledge" : 7,
        "Courage" : 17,
        "Wit" : 1,
        "Patience" : 77
    }
    playerparty = GetTrainerTeam("Young Alder")

    persondex = copy.deepcopy(defaultpersondex)
    persondex["Sensei Marshal"] = {"Named" : True, "Value" : 0, "Contact": True, "Sex": Genders.Male, "Relationship": "Sensei", "RelationshipRank": 0, "Events": [] }
    persondex["Alder"] = {"Named" : True, "Value" : 0, "Contact": True, "Sex": Genders.Male, "Relationship": "Self", "RelationshipRank": 0, "Events": [] }
    persondex["Shauntal"] = {"Named" : True, "Value" : 77, "Contact": True, "Sex": Genders.Female, "Relationship": "Champion", "RelationshipRank": 0, "Events": [] }
    persondex["Marshal"] = {"Named" : True, "Value" : 176, "Contact": True, "Sex": Genders.Male, "Relationship": "Sensei", "RelationshipRank": 0, "Events": [] }
    persondex["Grimsley"] = {"Named" : True, "Value" : 17, "Contact": True, "Sex": Genders.Male, "Relationship": "Sufferer", "RelationshipRank": 0, "Events": [] }
    persondex["Caitlin"] = {"Named" : True, "Value" : 76, "Contact": True, "Sex": Genders.Female, "Relationship": "Champion", "RelationshipRank": 0, "Events": [] }
    
    classstats = { 
        "Normal" : 94,
        "Fire" : 87,
        "Water" : 54,
        "Grass" : 34,
        "Electric" : 10,
        "Ice" : 86,
        "Fighting" : 86,
        "Poison" : 43,
        "Ground" : 78,
        "Flying" : 56,
        "Psychic" : 89,
        "Bug" : 97,
        "Rock" : 75,
        "Ghost" : 72,
        "Dark" : 74,
        "Dragon" : 90,
        "Steel" : 11,
        "Fairy" : 2
    }

scene championhall
show caitlin
show marshal sad:
    xpos 0.25 xanchor 0.5
show shauntal surprisedbrow frownmouth:
    xpos 0.75 xzoom -1
show flashback
show screen currentdate
with Dissolve(2.0)

alder @talkingmouth "Well, now, what do we have here? I heard a lot of yelling out there in the oval room. Did our Fairy Tale challenger make her way here sooner than we thought?"

marshal @sad2 "Apologies, Alder-{i}sensei!{/i} I could not hold her back! She roars like a dragon--she is fearsome beyond measure!"

caitlin @talking2mouth "What Marshal means is that the challenger's strength has not been exaggerated."
caitlin @talking2mouth "She and her Pokémon are of one mind. They cannot be swayed from their path."

shauntal @angrybrow happymouth "She had {i}fire{/i} in her eyes, Alder! The way she battled--it was like she and her Pokémon shared a single soul."
shauntal @happy "Oh, what a delightful story she must have to tell! 'The delicate flower who dances with dragons.'~"
shauntal -surprisedbrow -frownmouth @angrybrow talkingmouth "Yes, I'm quite certain, I need to write about her! Immediately!"

alder @winkbrow happymouth "Hold your horses there, Shauntal. If this woman's all you're cracking her up to be, then you're going to want to be {i}here{/i}, to write about our battle."

narrator "You lift your Poké Ball, and can feel your Volcarona inside vibrate with excitement. You feel it, too. Something about this challenger[ellipses] it was different."

marshal @sad2 "Er[ellipses] Sensei, 'woman' might not be the right word to describe her."

alder @surprisedbrow talking2mouth "Oh, sorry, I thought Shauntal said 'she.'"

marshal @sad2 "She did, but[ellipses]"

pause 1.0

show marshal surprised with dis

alder @surprisedbrow talking2mouth "Something you aren't telling me, Marshal?"

marshal think2 @surprised "No, Alder! I tell you everything! My life is yours! {gradualsize=36-20}I would never keep anything from you, not after you granted me life with your generosity! I am honorbound to--{/gradualsize}"

show marshal behind caitlin

narrator "You tune Marshal out as Caitlin steps forward."

alder @talking2mouth "Level with me, Caitlin. Does Cyrano have any chance of beating her?"

caitlin @talking2mouth "None."

alder @spunky2 "Spoken like a true Esper. You didn't have a moment of hesitation, huh?"

caitlin @talking2mouth "One doesn't need clairvoyance to divine her fate. I doubt that, even if Grimsley were still with us, he would have fared much better."

shauntal @talking2mouth "It's true. I loved the romance of her story, from what I'd read in the newspapers chronicling her league challenge, but never dreamed that those stories I'd read could have so much {i}truth{/i} to them."

alder @frownmouth "Hm[ellipses]"

narrator "You look at your Volcarona's Poké Ball again. Inside, you know she's staring back at you."

alder @talking2mouth "Is this it, Volcarona? I've only been here for four years. Sometimes that was a lifetime, and sometimes I blinked and a year had passed."
alder @talkingmouth sadbrow "This nation needs a strong champion. Maybe I'm not as young as I used to be, but I reckon I could keep going a bit longer."

show caitlin behind marshal
show marshal neutral 
with dis

alder @happy2 "'Course, I know you'd never forgive me if I didn't put everything I had into this."
alder @winkbrow talkingmouth "And neither would you three, eh?"

caitlin @closedbrow talkingmouth "The outcome you choose will be the correct one."

marshal @neutral2 "You will fight with honor and conquer this upstart {i}gaijin.{/i}"

shauntal @happy "Oh, whatever happens, it'll be a {i}fantastic{/i} story. I haven't been this excited since your last challenge, two years ago."

alder @happy2 "Alright, you guys. Come on, bring it in, group hug time. You've been the best Elite Four this sad old man could ask for. And if I can't defeat this challenger, I want you to know nothing between us will change."

show marshal sad with dis

alder @talking2mouth "Marshal, I'll still be there for you. I'll help you recover everything you lost. We're friends, and I'll never leave you to hang out to dry."
alder @closedbrow talking2mouth "You're a good man. I'd say you might even be a great one. Just don't do anything reckless, and reach out to me for help--even if you don't think you need it."

marshal @sad2 "Sensei."

pause 1.0

show caitlin sadbrow with dis

alder @talkingmouth "Caitlin, I don't care what the newspapers say about Cynthia--{i}you're{/i} the strongest woman in the world."
alder @happy2 "If I, or anyone else, had to put up with half of what you do, we'd be real jerks. You keeping your good heart was a miracle, and it's always been worth it to know you."

caitlin @talking2mouth "My butler, Darach, minded me decently, but I never felt like I'd had a true family. Until you accepted me, a tormented and troublesome foreigner."
caitlin @happybrow talkingmouth "If you see any good heart in me, it is one I learned from you."

pause 1.0

show shauntal surprisedbrow frownmouth heavyblush with dis

alder @spunky2 "And Shauntal[ellipses] when are you going to tie the knot with that girl you're seeing? Romance novels {i}do{/i} have an end, right?"

shauntal lightblush @surprisedmouth "Y-y-you {i}knew{/i} about her? Us? ME?! Being-- I mean, how I'm--"

alder @happy2 "How old do you think I am? I know what your salary is--I {i}pay{/i} it! It's not like you {i}need{/i} a roommate to afford that tiny apartment of yours."

shauntal sweat @sad2brow talkingmouth "{size=30}Oh, well[ellipses]{/size} I'm just waiting for the right time, really, so[ellipses]"

alder @talking2mouth "Take it from your senior, Shauntal. The right time was {i}yesterday{/i}. Second-best time is now."

shauntal @sad2brow talkingmouth "Okay, okay, you know, maybe we should talk about something else." 
shauntal @happy "Like, if Grimsley were still here, what would you say to {i}him{/i}?"

alder @frownmouth "[ellipses]"
alder @closedbrow talkingmouth "With all due respect to my former Elite, and keeping in mind that he was your teacher at Kobukan, Shauntal[ellipses]"

show marshal surprised
show caitlin surprisedbrow frownmouth
show shauntal -lightblush -sweat
with dis

alder @angrybrow talking2mouth "I'd tell that bum to come back to Unova and pay his taxes.{w=0.5} They go into {i}our{/i} salaries."

shauntal @talking2mouth "Er[ellipses] maybe I {i}won't{/i} write that part down."

alder @spunky2 "Good call."

pause 2.0

alder @talking2mouth "Hey[ellipses] I don't hear battling anymore."
alder @happy2 "This woman might get through us fast enough that it's all over before the press gets here."

$ PlaySound("Door_Open1.ogg")

pause 1.0

alder @talkingmouth "That's her. Alright, you three. Clear off. See if you can delay the press."
alder @spunky2 "Last thing a new champion wants is a camera shoved in their face and someone screaming at them to 'do something' about Orre."

show shauntal:
    xpos 0.75
    ease 0.5 xpos -0.25

show caitlin:
    xpos 0.5
    ease 0.5 xpos 1.5

marshal @neutral2 "You will prevail with honor, Sensei."

alder @spunky2 "Or maybe I'll lose with honor? I guess we'll find out."

show marshal:
    xpos 0.25 xanchor 0.5
    ease 0.5 xpos 1.25

pause 0.5

show iris with Dissolve(2.0):
    matrixcolor BrightnessMatrix(-1)

alder @angrybrow frownmouth "[ellipses]"
alder @talkingmouth "Challenger, I congratulate you for the strength and determination you have shown to make it here. Welcome to the Champion's Room, your last stop before the Hall of Fame."
alder @talking2mouth "I stand before you as Champion Alder Acothley, representing the Great Nation of Unova. You stand before me as a challenger, unnamed, representing what may one day be."
alder @angrybrow talking2mouth "We will now battle to determine the future of this nation--whether we will continue to tread the path we have found to be true, or head off to a new ideal."
alder @angrybrow talking2mouth "Do you--"

show iris:
    matrixcolor BrightnessMatrix(-1)
    ease 0.5 matrixcolor BrightnessMatrix(0)

pause 1.0

alder @surprisedbrow talking2mouth "Wait. Uh, you're[ellipses]"

narrator "A child. Just a child. An innocent child. What was she doing here? Who let her get this far?"

pause 1.0

$ persondex["Iris"]["Named"] = True

alder @closedbrow talking2mouth "Iris, right? Drayden's kid?"

iris @talkingmouth "Yep. Drayden's my daddy."

pause 0.5

iris sadeyebrows downeyes frownmouth @surprisedbrow talking2mouth "Oh, no, wait! I didn't say what I was s'posed to!"

narrator "Iris quickly whips out a piece of paper from her simple-looking clothes, and scans it, panickedly."

pause 0.5

iris -downeyes @talking2mouth "Mr. Champion, I didn't say the right thing. Does that mean I can't be Champion, now?"

alder @frownmouth "[ellipses]"

narrator "You try to imagine this tiny girl sitting all alone on the big, marble, throne behind you." 
narrator "You try to imagine this tiny girl going out into the ruined streets of Opelucid and shaking hands, and comforting a nation, like your predecessor did."
narrator "You try to imagine this tiny girl signing documents that will change the course of the world[ellipses]"

pause 1.0

narrator "And you can't."

alder @closedbrow talking2mouth "{size=30}But there's a lot of stuff I can't imagine. Not going to stop someone from doing their best just 'cause I'm an old fogey who can't figure out computers.{/size}"

iris @talking2mouth "Mr. Champion...?"

alder @happy2 "Don't worry about the speeches, kid. They were written fifteen hundred years ago, anyway."
alder @sadbrow talkingmouth "{size=30}Technically, we shouldn't even be battling with more than one Pokémon.{/size}"

iris -sadeyebrows -frownmouth @talkingmouth "Oh! Phew. I was really worried I'd messed somethin' up there."

alder @talkingmouth "Nah, the only thing keeping you from being champion now are my Pokémon."
alder @talkingmouth "So, you know, since I'm not giving that big speech about how this battle'll change the world, lemme think of something else to say."
alder @closedbrow "[ellipses]"

pause 1.0

alder @happy2 "Got it."
alder @talkingmouth "I am grateful for the journey you've taken. You saw people and places that you can never see except when you're on foot, around people, swimming in Unova's rivers, crossing its bridges, jumping off its cliffs."
alder @talkingmouth "I don't know what you're thinking now, but I'm sure you realize that different people and Pokémon have their own paths to follow. Unova's followed mine for long enough. Maybe it really {i}is{/i} your turn." 
alder @happy2 "Say now, how about a match with the strongest Trainer in the Unova region?"

pause 0.1

$ renpy.transition(dissolve)
call clearscreens() from _call_clearscreens_278

show blank with dis

# FAKE BATTLE
window hide

$ renpy.music.queue("Audio/Music/KantoTrainerStart_Rock.ogg", channel='music', loop=None, fadein=1.0, tight=None)
$ renpy.music.queue("Audio/Music/KantoTrainerLoop_Rock.ogg", channel='music', loop=True, tight=None)

call CreateSplash(["alder"], ["iris"]) from _call_CreateSplash_9

pause 2.0

stop music fadeout 0.25

python:
    calDate = calDate.replace(day=9, month=6, year=2004)
    timeOfDay = "Noon"
    inventory = oldinventory
    personalstats = oldpersonalstats
    playerparty = oldparty
    persondex = oldpersondex
    classstats = oldclassstats
    playercharacter = None

scene gym 
show alder:
    xpos 0.66
show bruno think:
    xpos 0.33
show screen currentdate
show screen currentdate
with dis

play music "Audio/Music/Gym_Start.ogg" noloop
queue music "Audio/Music/Gym_Loop.ogg"

alder @talkingmouth "[ellipses]well, that was a good battle. I'll be frank, I didn't want to battle her at first."
alder @sadbrow talkingmouth "Who'd want to put that much responsibility in the hands of a kid?"
alder @talking2mouth "But there's something more important to her than just how old she is."
alder @happy2 "She's a Pokémon Trainer, first and foremost. And a kid second."
alder @spunky2 "Sometimes I think that we should just give kids Pokémon when they turn ten."

bruno @talking2mouth "That would be {i}very{/i} irresponsible."

alder @talking2mouth "Maybe. Maybe still worth a shot? Who knows, maybe they'd do things we can't imagine. It's happened once, right?"

pause 1.0

alder @happy2 "Alright, you've heard me talk about how I got my butt whooped by a pre-teen long enough. Go ahead, pair off. And try to have some {i}good{/i} battles."

hide alder
hide bruno 
with dis

call pickgympartner() from _call_pickgympartner_2

python:
    battlechar = _return
    trainer1 = MakeRed()
    trainer2 = MakeTrainer(battlechar)

call Battle([trainer1, trainer2], uniforms = [True, True]) from _call_Battle_189

python:
    renpy.transition(dis)
    renpy.show(GetCharacterSprite(battlechar, 1, True))

$ RecordBattle("Week10WednesdayGym")
if (WonBattle("Week10WednesdayGym")):
    $ ValueChange(battlechar, 3)

    narrator "[battlechar] seems impressed!"

if (CanBunnyRecruit(battlechar)):
    redmind uniform @thinking "Maybe now would be a good time to bring up Saturday's party...?"
    call BunnyRecruit(battlechar, True) from _call_BunnyRecruit_9 

scene gym with dis

jump lunchtransition