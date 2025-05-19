label Silver1:
    if (not IsBefore(1, 5, 2004)):
        $ persondex["Silver"]["Events"].append("Level2SceneVer2")

    scene abandonedhouse
    with Dissolve(2.0)
    stop music fadeout 1.5
    $ renpy.music.queue("Audio/Morning_ambience.ogg", channel='music', loop=True, fadein=1.5, tight=None)

    show roughneck at night with dis

    red night @talking2mouth "...Hey."

    roughneck @angry "You here to talk to the boss?"

    red @talkingmouth "Sure am. Mind letting him know I'm here?"

    roughneck @angry "Tch."

    hide roughneck with dis

    narrator "You've come back to the city to talk with Silver, carefully retracing your steps until you find your way to the abandoned house that Silver lives in."

    show silver angry at night with dis

    silver "The hell do you want?"

    red @confusedeyebrows talking2mouth "...Um. To talk?"

    silver -angry @sad "Right. Sorry. Force of habit."

    stop music fadeout 1.5
    queue music "audio/music/DontEverForget_start.ogg" noloop
    queue music "audio/music/DontEverForget_loop.ogg"

    pause 1.0

    silver @talkingmouth "Well. What do you want to talk about?"

    red @talkingmouth "I want to talk about you."

    pause 1.0

    silver @sad "There's nothing to say."

    if (not IsBefore(1, 5, 2004)):
        silver @talkingmouth "If it's about the mind-powers stuff... whatever. I'm obviously outnumbered when it comes to not trusting you." 
        silver @closedbrow talkingmouth "Anyway, my position in the Disciplinary Committee lets me make sure you don't get too powerful."

        pause 1.0

        silver @happymouth "Remember, if I see you trying to start your own little gang, there's a Crobat with your name on it."

        red @confused "Noted. Terrifying. But that wasn't what I wanted to talk about at all."

        silver @closedbrow talkingmouth "Yeah? What, then?"

    red @confused "Silver. You live in the city, in a run-down shack, hiding from the cops, with twenty older guys who all treat you like you're their boss."

    pause 1.0

    silver @closedbrow talkingmouth "...Yeah."

    red @happy "Can you honestly tell me there's no story there?"
    red @talkingmouth "If you say that, I'll believe you. But I don't think you're going to say that."

    pause 1.0

    silver @sad "Fine. There's a story. But I'm not telling it."

    red @confused "Why not?"

    silver @angry "Well, aren't you all goddamn nosy all of a sudden!"

    red @sad "{w=0.5}.{w=0.5}.{w=0.5}."

    silver @sad "Sorry."

    red @talking2mouth "Silver, I just want to get to know you. In a stadium of hundreds of people, you were the only person who stood up to help me when Lance was being a dick."
    red @talking2mouth "I want to know why. {i}Why{/i} you helped me. What gave you the motivation to."
    red @happy "I want to know {i}who{/i} helped me. Who the Silver that stood up and acted as my shield was...{w=0.5} {i}is.{/i}"

    silver @smilemouth "{w=0.5}.{w=0.5}.{w=0.5}."
    silver @happymouth "Well, don't you think you're important?"

    red @surprised "Huh?"

    if (IsBefore(1, 5, 2004)):
        silver @talkingmouth "I wasn't doing it for you. You seem like a nice guy. You'd probably deserve it, if I did defend you."
    else:
        silver @talkingmouth "I wasn't doing it for you. Powers aside, you're nice enough, and you'd probably deserve it if I {i}did{/i} do it for you."

    silver @angry "But I was doing it for your Pikachu."

    if (IsBefore(1, 5, 2004)):
        $ renpy.music.play("Audio/Pokemon/pikachu_question.ogg", channel="altcry", loop=None)
        pikachu neutral_4 "Pika?"

    else:
        $ renpy.music.play("Audio/Pokemon/pikachu_question.ogg", channel="altcry", loop=None)
        libpikachu @surprisedbrow talkingmouth "Pika?"

    silver @angrybrow sadmouth "My entire life, I've heard weak men blame others for their incompetence." 
    silver @sad "People just can't take any goddamn {i}responsibility{/i} for their own failure."
    silver @talking2mouth "I'm... better, now. But the life I lived before... when I lived with my Dad..."

    pause 1.0

    silver @sad "Some mistakes you can't roll back."
    silver @closedbrow talkingmouth "But I can dream. And work as hard as I can to bury my past in the new me."

    pause 1.0

    silver @sad "And... I don't want others making the same mistakes I have. So... when I see or hear a trainer blame a Pokémon for their failure..."
    silver @angry "I need to let them know what they're doing wrong."

    pause 1.0

    red @surprised "Wait, you were trying to {i}help{/i} Lance?!"

    silver @angry "I think we've established at this point that I'm not exactly the picture of eloquence! Yes, I was trying to help the bastard."

    red @talkingmouth "...You might want to work on your communication skills."

    silver @sad "If that's really all you came here to tell me, you can piss off back to the campus, now."

    red @sadbrow happymouth "C'mon, Silver. Work with me, here."

    silver @smilemouth "{w=0.5}.{w=0.5}.{w=0.5}."
    silver @talkingmouth "You're a patient guy."

    red @happy "One of my many positive qualities."

    if (IsBefore(1, 5, 2004)):
        silver @talkingmouth "How can I work with you, then? I already agreed to help you get elected. You agreed to beat up my goons. Not sure what else we can do for each other."
    
        red @talkingmouth "Well, if we're going to be on the Battle Team together, we could stand to learn a little bit more about each other, right?"

    else:
        silver @talkingmouth "How can I work with you, then? I already agreed to help you get elected. And we all know how well that worked. Not sure what else we can do for each other."

        red @talkingmouth "What you did to help me out that day... I mean, it was kinda crazy. It probably would have worked, if Cheren hadn't... you know. Where'd you come up with that? Staging an attack on the school?"

        silver @sad "{w=0.5}.{w=0.5}.{w=0.5}."

    silver @closedbrow talkingmouth "I've talked enough. Tell me more about yourself."

    red @happy "Sure! So, I'm from a little town called Pallet Town, in Southwest Kanto. My Pikachu here is called [pika_name], and he was my first friend."
    red @closedbrow talking2mouth "Um... I lived with my Mom my whole life. My father wasn't in the picture--he died when I was young. We were pretty poor. Not 'cause he died, even before that."

    pause 1.0

    silver @talkingmouth "What kind of place was Pallet Town?"

    red @happy "Small!"
    red @talkingmouth "Peaceful, though. The people were kind. The grass was green, and the ocean was just south of us. And everyone knew everyone."

    pause 1.0

    red @sad "The one bad thing was... well, everyone knew everyone. It would be pretty much impossible to get a fresh start, there. Anything you do sticks with you until you move away."

    silver @talkingmouth "Mm. I get that."
    silver @sad "I grew up in Kanto as well, actually. In Celadon."

    red @happy "Really? Huh! I would've thought Celadon would be big enough to find a new start wherever you turned."

    silver @angrybrow happymouth "Not when you never leave your... {i}house.{/i} I probably got fresh air three times for the first twelve years of my life."
    silver @talkingmouth "And one of those times was when we were evacuating the building. Alarms flashing, cops pulling up... heh."

    red @surprised "Geez! Sounds intense. Was there a fire?"

    silver @sad "Something like that."
    silver @talkingmouth "...So, your Pokémon have always trusted you, huh?"

    red @happy "Pretty much. I mean, I've had [pika_name] for a long time, but I think he trusted me when we first met."

    silver @sad "And you don't have... you don't have any skeletons in your closet? No memories you want to bury in the dark?"

    red @confused "Uh... no."

    if (not IsBefore(1, 5, 2004)):
        red @sadbrow talkingmouth "Well, there {i}was{/i} the whole Frienergy thing, but... that's off my chest now, so... besides that, I don't think so."

    silver @closedbrow talkingmouth "Damn."

    red @confused "Damn? Why?"

    silver "[ellipses]"

    silver @talkingmouth "You... are good."

    red @happy "Aw, thanks."

    silver @angry "Shut up. I mean you're {i}good.{/i}"
    silver @closedbrow talkingmouth "You're kind, you know all kinds of shit about Pokémon, you're a great battler, you're fit, and you can make friends with anyone."

    red @happy "Flatterer."

    silver @talkingmouth "Look, no-one has all that unless they're trying to make up for something. There's gotta be something in your past. {i}Something.{/i}"
    silver @angry "Like, you used to be a fatass who didn't know anything about Pokémon, and you had no friends, right?"

    red @closedbrow talking2mouth "Well... there was a time when I didn't have any friends, yeah. After that, I definitely became a lot more social."
    red @talkingmouth "Or at least a lot more willing to take risks. Socially."

    silver smilemouth @talkingmouth "Hmph. Knew it."

    red @happy "Hey, is that a smile?"

    silver @talkingmouth "Yeah. It's a hell of a relief to hear that you aren't as perfect as I thought you were. What's this all in service of, anyway?"

    red @closedbrow talking2mouth "Huh?"

    silver @sad "Why bother being everything you are? It'd be so much easier to just... hide away, right? Be mediocre. Fade into the background."

    red @closedbrow "{w=0.5}.{w=0.5}.{w=0.5}."
    red @talking2mouth "I want to be a Champion."

    silver -smilemouth @talkingmouth "...So? Not like you need friends to do that. Look at Lance. Bastard's done it twice, and what does he have going for him, besides an overcompensatory hairstyle?"

    red @sadbrow happymouth "Maybe he doesn't need friends. But I do."

    silver @closedbrow sadmouth "Psh."

    red @happy "I'm serious. I'm nothing without my friends. And I'm not being modest. I freeze up. I can't speak for myself. I can barely remember anything about Pokémon, and everything I know about battling goes out the window."
    red @closedbrow talking2mouth "I spent four years in Pallet Town without any friends, and..."
    red @sadbrow happymouth "Well, I can barely remember anything I did then. I think I was kinda just in a dull haze."

    if (not IsBefore(1, 5, 2004)):
        silver @sad "So... like up there on the stage, then..."

    silver @talkingmouth "...Well, you need to get over that."

    red @upeyes angryeyebrows talking2mouth "Oh, gee, thanks. Wish I'd thought of that."

    silver @closedbrow talkingmouth "If you can't do it for yourself, do it for your Pokémon. They're relying on you. And if you can leave this world with at least one Pokémon you haven't disappointed, then you've won."

    red @talkingmouth "What about one human?"

    silver @sad "Yeah, that's... not going to happen."

    red @happy "I dunno. I think you can do it."

    silver @happymouth "Then prepare to be disappointed."

    pause 1.0

    red @confused "Was that a joke?"

    silver @happymouth "Are you so surprised? I'm a funny guy."

    red @happy "I'm kinda surprised, yeah! I didn't know you told jokes."

    silver @talkingmouth "...Most people don't get them. My humor's a bit dry."

    red @talkingmouth "Well, what's your dream? International comedian?"

    silver @closedbrow talkingmouth "...Whenever I close my eyes at night, I only ever have one dream." 
    silver @sad "And I dream of an absolution."

    if (IsBefore(3, 6, 2004)):
        red @happy "...C'mon. You're, what, eighteen?"

        silver @talkingmouth "Seventeen."
    else:
        red @happy "...C'mon. You're eighteen."

    red @happy "What do you have to be absolved of?"

    silver @angry "Are you so privileged that you think just because you've never had a nightmare, they don't exist?"

    pause 1.0

    silver @closedbrow talkingmouth "I've got a lot of nightmares in my dream journal, red. I can't tear out those pages. I can only keep writing."

    pause 1.0

    silver @talkingmouth "So that's my dream. I'll never be able to forget what I was. But if I can outweigh it, then maybe I can die happy."

    red @closedbrow talking2mouth "Hm."
    red @talkingmouth "So, your first step in this absolution is to try and rehabilitate your father's former employees."

    silver @talkingmouth "Yeah, these idiots."

    red @confused "...That's not normally the kind of thing the son of a CEO has to do, even if his Dad's company fails {i}really{/i} hard."

    silver @happymouth "Yeah, well, my Dad's company was always a {i}family{/i} business. Like he liked to remind me."

    red @closedbrow talking2mouth "What's your end-goal with these guys?"

    silver @surprisedbrow talking2mouth "Huh?"

    red @closedbrow talking2mouth "Like, what's your rehabilitation plan? What goalposts are you setting? How long do they have? What's your exit strategy?"

    silver @angry "I yell at them when they act up."

    red @talking2mouth "Not much of a plan."

    silver @closedbrow talkingmouth "No, not much of one."
    silver @sad "I guess I'm just kinda hoping that... one day... they'll just wander away, and not be my problem anymore."
    silver @closedbrow talkingmouth "Maybe when I'm not looking, they'll get a long-term job somewhere. Maybe even buy an apartment and leave."

    pause 1.0

    silver @talkingmouth "They bring me a lot of money. I don't ask where it comes from. I just try to invest it--get it out of this house--as soon as I can."
    silver @talking2mouth "Here, take a wad."

    $ PlaySound("Get.ogg")

    $ money += 2000

    narrator "Silver tosses you a brown paper bag filled with $2,000."

    red @surprised "W-woah. I don't really like to accept money from... wait, where'd this come from?"

    silver @sad "Didn't you hear? I said I don't ask where it comes from."

    pause 1.0

    silver @sad "It's more likely they'll try to rob a cop and get put away for a couple years. Still not my problem."

    red @closedbrow talking2mouth "You've been talking a lot about how your Dad's employees are... well, criminals. And I first met them when they stole Tia's hat."

    pause 1.0

    silver @talkingmouth "Yeah."

    red @sadbrow happymouth "What... kind of business did your Dad run, exactly?"

    pause 1.0

    silver @talkingmouth "Let me put it this way."
    silver @sad "When he did well, he was the only one who was happy about it. And when he went 'out of business...' well, no-one cared."

    red @sadbrow talking2mouth "...Silver."

    silver @sad "He was a bastard, but he was the only one who knew how to handle these people. And they're disappointed in me, because I'm not as cruel or tough as he was."
    silver @talkingmouth "Isn't that fucked up?"

    red @sadbrow happymouth "...You have trouble enforcing discipline, huh?"

    silver @closedbrow talkingmouth "Yeah, you could say that."
    silver @sad "I mean, some of these guys knew me when I was in diapers. The fact they live in my house now doesn't change that."

    red @closedbrow talking2mouth "Do you think you could use some help with your job here, then?"

    silver @talkingmouth "Well, yeah. But you're already helping, by coming here to beat them up every once in a while."

    red @talkingmouth "Glad I could be your {color=#0048ff}enforcer{/color}, then!"

    silver @sad "I don't want that."

    red @confused "Come again?"

    silver @sad "Everything about my life is drenched in violence, and authority, and shouting, and being the guy with the biggest stick in every room I go into. It's all just painful memories. But at least they're memories."
    silver @talkingmouth "I've left it behind. Even if they don't want me to. I'm not going back, and I'm not bringing anyone new into it. I don't want to drag anyone--you--into that."

    pause 1.0

    silver @sad "I don't need an enforcer. I don't need {i}more{/i} people who want to beat up others on my behalf. I just need a..."

    pause 2.0

    red @sad "Silver?"

    silver @closedbrow sadmouth "{size=30}I just need a {color=#0048ff}friend.{/color}{/size}"

    pause 2.0

    silver @surprisedbrow sadmouth "{size=30}Please?{/size}"

    red @happy "Silver. Did you really need to ask? C'mon. I wouldn't have come out here if I didn't want to be your friend."

    silver @sadbrow happymouth "...Thank you."

    $ RelationshipRankUp("Silver", "Friend", 1)

    return

label Silver2:
    $ AddEvent("Silver", "Silver2")
    stop music fadeout 1.5
    show relichall_A with Dissolve(1.5)
    
    queue music "audio/music/DontEverForget_start.ogg" noloop
    queue music "audio/music/DontEverForget_loop.ogg"

    redmind @thinking "Hm. Let's see, what should I do...? I've got some time, so..."

    show silver winter with vpunch 

    silver @talkingmouth "Red."

    red @talkingmouth "Red."

    silver @closedbrow talkingmouth "Need you to come with me."

    red @confused "Uh... sure. Is that about the Disciplinary Committee?"

    silver @closedbrow talkingmouth "Only that I'm about to jump into the harbor if I have to listen to one more of Cheren's 'duty' and 'responsibility' speeches."
    silver @sad "And that airhead's always nodding along, hanging on his every word, like he isn't just forcing us to listen to ten minutes of self-flagellation."

    red @confused "Huh?"

    silver @sad "Means 'punishment.' Swear he goes out of his way to embarrass himself as much as he can."

    $ ValueChange("Cheren", 2, 0.75, False)
    $ ValueChange("Skyla", 2, 0.25)

    narrator "Your understanding of Skyla increased! ...And your understanding of Cheren is further muddied."

    silver @closedbrow talkingmouth "But unlike that guy, I'm not going to sit in a dark room writing emo poetry."
    silver @talkingmouth "Got something to do. And I could use you to do it."

    red @sadbrow talkingmouth "...Does that mean you trust me again?"

    silver @closedbrow talkingmouth "Not even close, red. But if you're going to use that power anyway, I want to put it toward something good."

    pause 1.0

    show silver sadbrow with dis

    red @sadbrow talkingmouth "I do too, man."

    silver @talkingmouth "Well, I'm giving you a chance to prove it."

    pause 0.5

    silver -sadbrow @talkingmouth "We're going up the mountain. Will you be warm enough in that?"

    red @talkingmouth "Uh, should be, I think."

    silver @angrybrow talkingmouth "...Don't try to act tough. You can't 'friend' your way out of a cold."
    silver @talkingmouth "Come with me."

    hide silver with dis

    pause 0.3

    redmind @thinking "Hm? He's not heading towards the mountain... are we going somewhere else first?"

    scene blank2 with splitfade

    pause 0.5

    narrator "You follow Silver closely, though he doesn't look back at all. You soon realize that you're heading toward the Disciplinary Committee's office, and start to pull back a bit."

    red @confused "Hold on--"

    silver winter @talkingmouth "This doesn't have anything to do with the Committee. It's just where lost and found is."

    red @sadbrow talking2mouth "...Alright."

    scene studentcouncil 
    show silver winter closedbrow 
    with splitfade

    silver @talkingmouth "...Right. Bunch of clothes here, left over. Take something warm. Take a whole outfit, if you want."

    red @surprised "Oh. Uh, is that alright?"

    silver @talkingmouth "This box has been here since last year."
    silver @sad "Whoever this shit belonged to doesn't remember it exists anymore. They're not coming back. It's just lost, not found."

    pause 0.5

    silver @angry "So take something!"

    red @sadbrow talkingmouth "Uh... I don't want to sound ungrateful, but if this stuff has been sitting here for a year, shouldn't I probably wash it before putting it on?"

    silver @talkingmouth "Already done. Put it in with the washing at the shack."

    red @surprised "!"

    silver @angry "What?"
    silver @sad "You think any of those idiots I live with are the kind to wash their own damn clothes? I'm their landlord, but sometimes I feel more like their mother, they're so hopeless."

    red @closedbrow talkingmouth sweat "Alright. I'll find something, then..."

    narrator "You rummage through the clothing for a while, until you find a coat you like the look of."

    red @talkingmouth "Awesome! These'll work."

    silver @talkingmouth "Alright. Bathroom in the corner. Get changed there, then we can go."

    red @talkingmouth "Sure."

    narrator "You lean down to put the box of clothing away, then notice something strange. A black shirt with a big red \"R\" on it is folded within the clothing."

    show silver surprisedbrow with dis

    red @confused "Huh, what's--"

    show silver:
        xpos 0.5
        ease 0.2 ypos 1.2 zoom 1.3

    silver angry "It's {i}nothing.{/i}"

    pause 1.0

    show silver:
        ypos 1.2 zoom 1.3
        ease 0.5 ypos 1.0 zoom 1.0

    silver -angry @talkingmouth "Just some trash. One of my tenants' old clothes must've gotten mixed in."

    pause 0.5

    silver @sad "Go on. Get changed."

    red @sad "Okay."

    scene blank2 with splitfade

    narrator "You walk into the bathroom, and put your new change of clothes on the floor next to you, taking a look at yourself in the mirror."

    pause 0.5
    
    redmind swimsuithatless @thinking "Well, that definitely explains a couple things. {i}Rocket{/i}, huh...?"
    redmind @sad2eyes frownmouth "I might be a Pallet Town boy, but even I recognize their logo. So, if that was one of Silver's goons' clothes, and that goon was a member of Team Rocket, then that means Silver must have been..."

    pause 0.5

    redmind @closedbrow frownmouth "Well, he was definitely involved, somehow."

    scene studentcouncil 
    show silver winter 
    with splitfade

    silver @talkingmouth "You're back."
    silver @closedbrow talkingmouth "Something up? You look like you've seen a ghost."

    red winter @talkingmouth "Not really."

    silver @talkingmouth "Right. Let's go."
    silver @talking2mouth "I'll cover the Ride Cyclizar fee."

    python:
        hascyclizar = False
        for mon in playerparty:
            if (mon.GetId() == pokedexlookupname("Cyclizar", DexMacros.Id)):
                hascyclizar = True
                break

    if (hascyclizar):
        red @happy "It's fine. I've got one."

        silver @talkingmouth "Alright."

        python:
            rideable = None
            for mon in playerparty:
                if (pokedexlookupname("Cyclizar", DexMacros.Id) == mon.Id):
                    rideable = mon
                    break

        $ PlaySound("pokemon/ball sound.ogg")
        $ sidemonnum = pokedexlookup("Cyclizar", DexMacros.Id)
        $ sidemonoverride = rideable.GetNickname()
        $ PlaySound("pokemon/cries/{}.mp3".format(sidemonnum))
        
        sidemon "Cyc! Lizar!"

        $ sidemonoverride = None

    else:
        red @talkingmouth "Thanks."

        silver @talkingmouth "Don't mention it."

    scene icepath with splitfade

    pause 0.5

    show silver winter with dis

    red winter @talkingmouth "So, uh, what're we doing here?"

    silver @talkingmouth "One of my tenants told me about an Absol she spotted out here. Looked like a really tough one, she said, too."

    $ absolinparty = absolobj in playerparty
    $ caughtabsol = absolinparty or absolobj in box
    $ absolsex = "him" if absolobj.Gender == Genders.Male else "her"

    if (caughtabsol):
        red @talkingmouth "Oh, was that a while ago? Because I caught that Absol."
        if (absolinparty):
            red @happy "I've got [absolsex] with me now, actually."

            $ PlaySound("pokemon/ball sound.ogg")
            $ sidemonnum = pokedexlookup("Absol", DexMacros.Id)
            $ sidemonoverride = absolobj.GetNickname()
            
            $ PlaySound("pokemon/cries/{}.mp3".format(sidemonnum))
            sidemon "Absoooool."

            $ sidemonoverride = None

        silver @talkingmouth "Nice. They're good Pokémon. But no, this was more recent."

    else:
        red @talkingmouth "Oh, was that a while ago? Because I fought that Absol."

        silver @talkingmouth "Nah. More recent."

    silver @talkingmouth "Lot of trainers out there... don't respect Absol."
    silver @closedbrow talkingmouth "Either they're superstitious idiots that think Absol {i}bring{/i} disaster, or they're even bigger idiots trying to monetize their ability to sense disasters."
    silver @talking2mouth "You get a lot of trainers trying to use them, or 'cheat' their disaster sense for some kinda profit."
    silver @sadbrow talking2mouth "They're living creatures. Not smoke detectors, not earthquake sirens..."
    silver angry "Scum."

    pause 1.0
            
    silver -angry @sad "Since Absol don't let themselves be exploited, the trainers call 'em 'difficult to train', and just drop them. Or... {i}worse.{/i}"

    pause 0.5

    silver sadbrow @talkingmouth "I had one once."

    red @happy "Cool! Is it with your Crobat?"

    silver sadbrow "{w=0.5}.{w=0.5}.{w=0.5}."
    silver @sadmouth "It was difficult to train."

    pause 1.5

    silver @talkingmouth "Now you see why you're here."
    silver @closedbrow talkingmouth "We're not here to catch the Absol. My tenant told me the Absol looked like it was wounded. It'd be dangerous for {i}anyone{/i} to try and catch it right now."
    silver @talkingmouth "I can't calm it down. Not like I am. That's what I need you for."

    red @sadbrow talkingmouth "...Alright."

    scene blank2 with splitfade

    pause 1.0

    $ sidemonnum = pokedexlookup("Absol", DexMacros.Id)
    $ PlaySound("pokemon/cries/{}.mp3".format(sidemonnum))

    if (caughtabsol):
        red winter @talking2mouth "Yeah, I definitely recognize that cry. The Absol's this way. Sounds like it's wounded, like you said."

        silver winter @talkingmouth "We should hurry."

    else:
        silver winter @talkingmouth "Yeah, I recognize that cry. The Absol's this way."
        silver @sad "Sounds... pained."

    scene icecave with splitfade

    narrator "You emerge into a cave, where you see an Absol shivering up against a wall. It moves dizzily, and sweat pours down its forehead, slicking its softly lucent fur."

    if (not caughtabsol):
        red winter @surprised "Wait... that's the Absol! The one Skyla, Brendan, and I fought!"

        show silver winter angry with vpunch

        silver "And you left it like this?!"

        red @sadbrow talking2mouth "No. I promise. It just ran away after the battle. It didn't look injured then, at all."

        silver -angrymouth angrybrow "{w=0.5}.{w=0.5}.{w=0.5}."
        silver -angrybrow @sadbrow talkingmouth "Fine. Let's just help it."

    else:
        show silver winter angry with dis
        
        silver "Some trainer... just left it like this. Look, they battled it way past the point at which you should just call it quits on trying to catch it."
        silver "I swear, if I got my hands on that worthless shithead, I'd... I'd..."

        pause 1.0

        red winter @confused "What?"

        silver -angry @sad "Nevermind. Let's just help it."

    show silver:
        xpos 0.5
        ease 0.5 xpos 0.25

    narrator "You cautiously approach the Absol, who seems to calm down at your presence."

    red @sadbrow talkingmouth "Hey, big man. Big girl? Not sure. Don't worry--we're here to help. We've got some medicines that should make you feel better."

    narrator "Silver pulls a ball of red thread and a couple of bandages out of his coat."

    silver @talkingmouth "Doesn't look like you're going to need stitches, but you'd probably appreciate a Full Restore, and a bandage for that leg."

    $ sidemonnum = pokedexlookup("Absol", DexMacros.Id)
    $ PlaySound("pokemon/cries/{}.mp3".format(sidemonnum))

    sidemon "Absol... sol!"

    pause 1.5

    silver @talkingmouth "Alright. Looks like we're done here."

    red @confused "That's all?"

    silver @talkingmouth "That's all."

    red @talkingmouth "Aren't... you going to catch it?"

    silver @closedbrow talkingmouth "I don't catch Pokémon. Not anymore. Especially not an Absol."

    red @surprised "Really? But you have so many of them!"

    silver @sad "Told you. They're my tenants'. Haven't thrown a Poké Ball since I lived in Kanto."
    silver @closedbrow talkingmouth "You need Pokémon in this world, just to exist, but I ain't catching any more."
    silver @sadbrow talkingmouth "That's one thing my tenants are good for, I guess."

    pause 0.5

    red @sadbrow talkingmouth "Where {i}is{/i} your Crobat, Silver?"

    silver @closedbrow talkingmouth "Safe. Away from me."

    pause 1.0

    red @sadbrow talkingmouth "You know, I heard that Golbat won't evolve unless they have a strong bond with their trainer."

    silver @angry "Yeah? Well, {i}I{/i} heard being a shit judge of character isn't something exclusive to humans."

    red @sadbrow frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."
    red @talking2mouth "I don't know a lot of... your story."

    silver @talkingmouth "That's right. You don't."

    red @talkingmouth "But I feel like you need to forgive yourself."

    silver @sadbrow happymouth "Oh, I have. That's why I don't go near waterfalls anymore."
    silver @sadbrow talkingmouth "Everything else, though... that's not mine to forgive."

    pause 1.0

    silver @angrybrow talkingmouth "Hey, what're you still doing here? Go on. We're done."

    narrator "Silver turns his attention to the Absol, which is standing steadfastly in front of you two. A small red string tying down a bandage on its foreleg is the only sign that you had ever interacted."
    narrator "Your eyes trace the string's path, and realize with a start it leads to Silver's hand."

    red @happy "Hey, red. You forgot to cut the string."

    silver @surprisedbrow talking2mouth "Hm?"
    silver @talkingmouth "Oh. No wonder it's still here, then." 
    
    narrator "Silver reaches into his boot, and pulls out a small switchblade. You cock an eyebrow, but don't question it. He raises the knife towards the red string, and..."

    silver @sad "{w=0.5}.{w=0.5}.{w=0.5}."

    narrator "Hesitates."

    silver @closedbrow talkingmouth "Looks familiar."
    silver @sadbrow talkingmouth "Just in my head, though. No way."

    narrator "Silver swings the knife down, and..."

    show silver surprisedbrow with dis

    $ sidemonnum = pokedexlookup("Absol", DexMacros.Id)
    $ PlaySound("pokemon/cries/{}.mp3".format(sidemonnum))

    sidemon "Ab!"

    narrator "Absol blocks the blade, deflecting it with its own bladed horn."

    silver @sadbrow talkingmouth "C'mon. What are you trying to say, Absol?"

    red @sadbrow talkingmouth "I think it's pretty obvious what it's saying, Silver."
    red @happy "It's not a very subtle metaphor."

    silver closedbrow angrymouth "{size=30}Damn it.{/size}"

    pause 1.0

    silver @angry "Go on. {i}Leave.{/i} You don't want this. I don't want this. {i}Anyone{/i} else would be better."

    sidemon "{w=0.5}.{w=0.5}.{w=0.5}."

    silver sadbrow -angrymouth @talkingmouth "[first_name]. Get out of here. I need to show this Absol what's what, and I can't have you staring at me with those moon eyes."

    red @sadbrow talkingmouth "...Alright."

    pause 0.5

    red @sadbrow talkingmouth "I know you voted to keep me on the Battle Team, when Erika was trying to kick me out. And I appreciate that."
    red @talkingmouth "I don't know what you were thinking, then... but maybe you were thinking I deserved another chance?"

    pause 0.5

    red @talkingmouth "If I had the ability to, I'd give you another [bluecolor]chance{/color}, too."

    pause 1.0

    red @sadbrow talkingmouth "I don't, though."

    pause 1.0

    red @happy "But maybe there's someone here who {i}does{/i}."
    
    $ sidemonnum = pokedexlookup("Absol", DexMacros.Id)
    $ PlaySound("pokemon/cries/{}.mp3".format(sidemonnum))

    sidemon "Sol!"

    pause 1.0

    silver @angrybrow talkingmouth "Out."

    scene blank2 with splitfadefast

    pause 1.0

    narrator "You leave the cave, and a few minutes later, you hear the sound of battle."

    scene icepath with splitfade

    pause 1.0

    show silver winter with dis

    silver @talkingmouth "We're done here. Let's go back."

    narrator "Your eyes flit down to Silver's waistline, and notice a Luxury Ball that was not there before."

    red winter @talkingmouth "A Luxury Ball?"

    silver @sadbrow talkingmouth "Had one lying around."

    red @closedbrow talking2mouth "Hm."

    show silver sadbrow with dis

    red @talkingmouth "Looks good on you."

    scene blank2 with splitfade 

    red winter @talkingmouth "Oh, about the clothes--"

    silver winter @talkingmouth "Keep 'em."

    pause 1.0

    silver @closedbrow talkingmouth "They look good on you."

    $ RelationshipRankUp("Silver", "Chance", 2)

    return

label Silver2Part2:
    $ AddEvent("Silver", "Silver2Part2")
    $ AddEvent("Silver", "Overthrown")
    stop music fadeout 1.5
    queue music "Audio/Music/eterna_start.ogg" noloop
    queue music "Audio/Music/eterna_loop.ogg"
    call clearscreens() from _call_clearscreens_251
    scene blank2 with splitfade

    pause 1.0

    show midnight at vspaz

    pause 3.5

    scene bedroommidnight with splitfade

    narrator "Thmp."

    pause 1.0

    narrator "Thmp."

    pause 1.0

    narrator "Thmp."

    red night casual hatless @tired unamusedbrow talking2mouth "What's making that noise...? Why are--who's...?"

    $ PlaySound("pokemon/pikachu_sad.ogg")

    libpikachu night @closedeyes sadmouth "Piiiikaaaa."

    red @closedbrow tired talking2mouth "No, it's fine, I'll get it."

    narrator "You unsteadily shuffle out of bed, and fumble around for the light."

    show bedroomnight with dis

    red @closedbrow talking2mouth "Crap, that's bright. Okay, what's going on here? Who's making that noise? Is...?"

    narrator "You turn to the window, and see, with some surprise, a small pebble hit the glass, then fall out of sight."

    pause 1.5

    red -night @confused "That's concerning." 
    
    narrator "You open up the window, and, looking down onto the campus, you see..."

    scene relichall_B 
    show silver surprisedbrow frownmouth winter at night
    with splitfade

    redmind casual hatless @thonk "Silver?"

    red @confused "Dude, what the fuck are you doing up? It's like midnight o'thirty. Is this a Disciplinary Committee thing?"

    narrator "...You mouth silently to him, given you don't want to disturb the quiet night air by shouting."

    silver @angrybrow talking2mouth "It doesn't matter. Just get down here. I'm in a lot of trouble, and didn't know who else--{i}where{/i} else to go."

    narrator "...He mouths silently back at you. Both of you are suitably impressed by your ability to understand lip movements, in the dark, across such a large distance."

    pause 1.0

    red @closedbrow talking2mouth sweat "Alright, I'll be right down. Just give me a second. I need to put on a jacket or something."

    pause 1.0

    silver @talking2mouth "In effervescence comes celery of thirteen explode twulpy."

    pause 1.0

    narrator "It seems apparent that your magical powers of lip-reading across dark distances has left you."
    narrator "Either that or Silver's having a stroke."

    redmind @thinking sweat "Either way, I should definitely head down there quickly..."

    red @talking2mouth "Come with me, [pika_name]. Might be trouble."

    $ PlaySound("pokemon/pikachu_excite2.ogg")

    libpikachu @angryeyes happymouth "Pika!"

    stop music fadeout 1.5
    
    queue music "audio/music/DontEverForget_start.ogg" noloop
    queue music "audio/music/DontEverForget_loop.ogg"

    scene blank2 with splitfade

    pause 1.0

    scene relichall_B 
    show silver winter surprisedbrow frownmouth at night
    with splitfade

    red night winter hatless @closedbrow talking2mouth "Silver, what's[ellipses]{nw}" 
    extend @surprisedbrow talking2mouth " Oh, shit, are you alright?"

    silver @talking2mouth "What? Why? Why are you asking?"

    red @wince talking2mouth "I mean, you're throwing pebbles at my window in the middle of the night, but, more than that, you're shaking like you just ran a marathon."

    pause 1.0

    red @surprised "Wait, what are you even doing here? You live in Inspira. Did you--holy {i}shit{/i}, did you run from Inspira?"

    silver -surprisedbrow @closedbrow talking2mouth "...Yeah."

    red @talking2mouth "Tell me what happened."

    silver @talking2mouth surprisedbrow "It's... shit, it's bad. It's really bad. I shouldn't be here, I just didn't know what to do, you were the first person I thought of, and--"

    show silver surprisedbrow frownmouth at night:
        ypos 1.0 zoom 1.0
        ease 0.2 ypos 0.9 zoom 0.8

    red @angrybrow talking2mouth "Silver!"

    narrator "Silver flinches. It's only for a moment, but when he turns back, his expression is unreadable. Is it anger? Shame?"

    show silver -surprisedbrow at night:
        ypos 0.9 zoom 0.8
        ease 0.5 ypos 1.0 zoom 1.0

    red @talking2mouth "Sorry, man. I didn't mean to yell. I just... I need to know. Are you in danger?"

    silver @sadbrow talking2mouth "No. No, I'm not in danger. But Inspira might be. Kobukan might be. My... my damn tenants... {i}definitely{/i} are."

    red @sadbrow talking2mouth "What happened?"

    silver @talking2mouth "...I got overthrown."

    red @surprised "What?!"

    silver @sadbrow talking2mouth "I... all the Pokémon we use go into a big pile in the shack. People grab whatever they need. I train 'em up, but we don't--{i}I{/i} don't have personal Pokémon."
    silver @surprisedbrow talking2mouth "But then I got this Absol, and... and I didn't want to give it up to them, and... some of them started saying that wasn't fair, and it spiraled into this huge argument, and then--"
    silver @closedbrow talking2mouth "One of them took over. Said I wasn't trying to resurrect Team Rocket at all. That I was just waiting for them all to disappear one-by-one."

    pause 1.0

    red @sadbrow talkingmouth "You're trying to resurrect Team Rocket?"

    silver @angry "No, dumbass! I--I never said that! They just believe it because the boss was {i}my Dad!{/i}"

    pause 1.0

    red @sadbrow talking2mouth "I thought so. Giovanni Sakaki. The Gym Leader of Viridian, right? And the leader of Team Rocket."

    silver @talking2mouth "He had a lot of bastards. I'm not special. But I was the only one he kept with him in Celadon."
    silver @talking2mouth sadbrow "His 'favorite', I guess. Lucky fucking me."

    pause 1.0

    red @talking2mouth "What are you going to do about your... your tenants?"

    silver angrybrow @angry "Why the hell do you think I'm here? I'm here because {i}I don't know{/i}, and I thought you would!"

    red @sadbrow talking2mouth "Why would I know? It's not like I've ever had a terrorist's son ask me how to get his father's minions to calm down before!"

    pause 1.0

    show silver sadbrow frownmouth with dis

    silver @talking2mouth "They're so screwed. It's been hard enough trying to keep them under the radar. We've had INTERPOL sweeping across the globe trying to get the last of us, especially after those idiots in Johto made their play."
    silver @closedbrow talking2mouth "The last of us in Unova were captured six months ago. They found him buried somewhere in Icirrus. Swept in in the dead of winter." 
    silver @talking2mouth closedbrow "That place is a swampy shithole in the middle of nowhere--if they could find him {i}there{/i}, what chance do {i}we{/i} have in the middle of a big fucking city?!"
    silver @sadbrow talking2mouth "I thought Kobukan would be safe! I thought if I got a proper Kobukan education, didn't stand out, we can stay under the radar, and I could emerge as a legitimate Dark-type Gym Leader, or something, somewhere."
    silver @closedbrow talkingmouth "But then Lance spouted that shit during the orientation match, and I saw red, then I... I encouraged my grunts to go to the school on election day, and that just made things worse, and..."
    silver @angrybrow talking2mouth "And I'm trying to protect these assholes, protect what little life they've got left, and they just keep fucking it up for themselves! I'm {i}trying{/i} to help them!"
    silver angry "Why won't they stop {i}hurting{/i} people?! Why is that the only thing these worthless bastards can do right is lie, cheat, and steal?! Why is it whenever any one of us tries to make a change, it {i}always{/i} ends up like this?!"

    pause 1.5

    silver @angrybrow talking2mouth "I wanted to leave it behind. I didn't want to fight anymore. I wanted to climb out of that basement forever, and make a new life. And I thought I could bring someone with me."

    pause 1.0

    silver @closedbrow angrymouth "I can't. Can't fucking help {i}anyone{/i}. {w=0.5}Lie. {w=0.5}Cheat. {w=0.5}Steal. {w=0.5}Hurt. That's all I can do. And when I don't do it, I still hurt the people I'm trying to help."

    pause 1.0

    red @talking2mouth sadbrow "Silver, reviving Team Rocket isn't the answer."

    silver sadbrow @talking2mouth "Then what fucking is? That's what they want me to do. That's what anyone who knows I exist wants me to do."

    red @talking2mouth sadbrow "I know you exist. And I don't want you to revive Team Rocket."

    silver @talking2mouth "Yeah? What do you want me to do, then? Just stay in a holding pattern? Stay underground in that little shack, scared to stick our heads out and get hit, like some kind of goddamn criminal Diglett?"

    pause 1.0

    red @sweat talking2mouth "I... I don't know what the answer is, but... I know what it {i}isn't{/i}."

    silver @sadbrow talking2mouth "Yeah, well, you're in the same boat as me, then. And apparently if you don't know the answer for long enough, they take the reigns away from you."

    pause 1.0

    silver @closedbrow talking2mouth "God, I'm so stupid. One of the things they said was that I'm not spending enough time around them--that I'm spending too much time with you. What do I do after they kick me out? Go right to you. Guess they were right."

    pause 1.0

    red @talking2mouth sadbrow "We're friends, Silver. There's nothing wrong with coming to me when you're in trouble. Look, we can work this through together."
    red @talking2mouth wince "We'll figure something out. I don't know. I don't have the answers right now, but... but we'll... we'll do {i}something{/i}, and it'll... it'll work."

    silver sadbrow @talking2mouth "My Dad left a trail of people who went in 'planning to plan.' We can't just go in without a solution. We need to know exactly what we're doing, {i}now.{/i}"

    red @sadbrow talking2mouth "Isn't that what your tenants said to you? That you needed a plan, that you couldn't just figure something out?"

    pause 1.0

    silver @talking2mouth "But look how well 'figuring it out' has worked out for me. I spent too long 'figuring it out.' They lost their patience, and now, I'm... I'm..."

    pause 1.0

    silver @talking2mouth "{i}Shit{/i}."

    red @closedbrow talking2mouth "No, Silver, you're not shit."

    silver @angrybrow talking2mouth "I wasn't saying that {i}I{/i} was shit, I'm just saying this whole shitty situation is {i}shit{/i}! It's all shit, and it's {i}shit{/i} on top of {i}shit{/i}, and I'm sick to death of all this {i}shit!{/i}"

    pause 2.0

    silver -sadbrow @closedbrow talking2mouth "...I feel better."

    pause 1.0

    red @sadbrow talkingmouth "Great."

    silver @closedbrow talking2mouth "I need to talk to them. Make them see reason. Maybe I can negotiate with {i}her{/i}."

    red @talking2mouth "Her?"

    silver @sadbrow talking2mouth "The one who took over, who pushed for the mutiny. She's a fanatic. She's never stopped drinking the Rocket Kool-Aid. I knew she was trouble when I brought her with me, but I thought..."
    silver @sadbrow talking2mouth "I thought I'd figure something out."

    pause 1.5

    silver @sadbrow talking2mouth "I'm sorry. I need you for this."

    red @sadbrow talkingmouth "You didn't have to ask."

    silver @talking2mouth "I only have Absol with me right now, so if we have to battle, I'll be counting on you. Okay?"

    red @talking2mouth "Alright. Next time I go to the city, I'll text you, and we can drop by the alley."

    if (not IsContacted("Silver")):
        silver @sadbrow talking2mouth "You don't have my phone, do you?"

        red @talking2mouth surprisedbrow "Oh. Guess not."

        $ BecomeContacted("Silver")

        silver @talking2mouth "Thanks."

    red @talking2mouth "Wait, where--where will you stay? You don't have a dorm, right?"

    silver @talking2mouth "I've got one, officially. Never used it, but I guess tonight's the night to start."

    red @talking2mouth "Geez, Silver. You can't knock on the door of a dorm you've never been to before and just ask to be let in. They'll probably call the Disciplinary Committee on you."

    silver @talking2mouth "I {i}am{/i} the Disciplinary Committee."

    red @unamusedbrow talking2mouth "Then they'll call campus security, who'll probably just call the cops."
    red @talking2mouth "Come to my dorm, alright? You can stay the night. Tomorrow, talk to Cheren, figure out a place to dorm. Maybe it's your old dorm, maybe not." 
    red @closedbrow talking2mouth sweat "Then, when we both have time, we'll go to the city and see if we can talk some sense into them."

    if (HasEvent("Silver", "SilverBirthday1")):
        red @sadbrow talkingmouth "Remember your birthday, Silver? I told you that you could use my dorm. You said you'd only use it in an emergency. I think this qualifies."

    pause 1.0

    silver @sadbrow talking2mouth "...Yeah. Yeah, okay. Fine."

    pause 1.0

    narrator "Silver's breath is visible in the cold night air. He stumbles over his words as he tries to add something."

    silver @talking2mouth "Look, I... thanks. I dragged you into my mess, and I'm sorry for it. But you've been... you've been a great friend. You gave me a chance. I, uh, really appreciate what you've done for me."

    pause 0.5

    silver @sadbrow talking2mouth "So, I just want to say, you know, if you're inviting me to your dorm..."

    red @sadbrow talking2mouth "I promise it doesn't mean anything. I'm just trying to get you out of the cold, give you a place to crash for the night while you work things out."
    red @sadbrow talking2mouth "I wouldn't try anything while you're... you know."

    pause 1.5

    silver @talking2mouth "Oh."

    pause 0.5

    silver @sadbrow talking2mouth "Yeah, I was coming at this from the complete opposite direction."

    red @surprisedbrow talking2mouth "Wait, what?"

    silver @sadbrow talking2mouth "I lived underground with a bunch of criminals that thought my Dad could walk on water, where promotions were based mainly on how happy my Dad was at any given moment. And there was nothing to do down there. We had {i}five{/i} books."
    silver @sadbrow happymouth "See what I'm saying? If I told you the amount of action I got, you'd have to come up with a harsher word than 'manwhore.'"
    silver @closedbrow talking2mouth "It doesn't mean anything to me. So, if you wanted me to, uh, pay you back..."

    red @surprised "Oh, god, no, abort, rewind. This is {i}not{/i} a transactional thing. No way. I'm doing this because you're my friend, not because I expect you to pay me. In {i}any{/i} way."

    if (IsBefore(3, 6, 2004)):
        pause 1.0

        red @wince talking2mouth "Wait, you're seventeen."

        silver @closedbrow talking2mouth "Oh. Yeah. Forgot some people care about that."

    pause 1.0

    silver @closedbrow talking2mouth "Thanks.{w=0.5} {i}That{/i}, uh, means a lot."

    pause 1.0

    silver @closedbrow talking2mouth "You're still gay, right?"

    red @talking2mouth "I like men, yes. But not just men."

    silver @sadbrow happymouth "Well, nobody's perfect."

    red @closedbrow talkingmouth "Alright, Silver. C'mon, let's get you to my dorm. Careful for the loose tile near the entryway, it clicks when you step on it."

    scene blank2 with splitfade

    narrator "You bring Silver back to your dorm, where, after throwing his jacket on the floor, the evening's drama overwhelms him, and he falls asleep, with you following soon after."

    pause 1.0

    narrator "When you awake, Silver is gone, but you find a small purple orb on your nightstand, with a note attached."

    TempCharacter("Note") "Thanks. Don't forget to [bluecolor]meet me in the city.{/color}"

    $ GetItem(Item.ToxicOrb, text="You put the Toxic Orb in your bag! The purple liquid inside swirls around malevolently.")

    return

label Silver3:
    $ location = "city"
    stop music fadeout 1.5
    queue music "Audio/Music/silphco_intro.ogg" noloop
    queue music "Audio/Music/silphco_loop.ogg"
    call clearscreens() from _call_clearscreens_252
    scene city_A with splitfade

    show silver angrybrow frownmouth with dis

    silver @talking2mouth "Ready?"

    red @talking2mouth "As I'll ever be."

    silver @talking2mouth "Alright. Remember, no battling. We need to make this work without fighting them, or else... I mean, that just beats the entire purpose of trying {i}not{/i} to use force to get everything we want."

    red @talking2mouth "Right. Though... if we {i}have{/i} to battle..."

    silver @talking2mouth "If we have to, we have to. Just try to avoid it."
    silver @talking2mouth "And... don't underestimate her. She acts like a dumb, smug, princess, but she's one of the strongest battlers I've ever met."

    if (GetHighestLevel() > 50):
        $ AddEvent("Silver", "DuplicaTooStrong")
        silver @talking2mouth "You can definitely beat her, but she doesn't need to Pokémon battle to win. So don't get any funny ideas about showing off."

    elif (GetHighestLevel() > 44):
        $ AddEvent("Silver", "DuplicaStrong")
        silver @talking2mouth "Maybe you could beat her, but, still, try to avoid it. Beating her wouldn't do much for us, anyway."

    elif (GetHighestLevel() > 25):
        $ AddEvent("Silver", "DuplicaWeak")
        silver @talking2mouth "Battling her as you are now... not a good idea. It'd be a very uphill battle."

    else:
        $ AddEvent("Silver", "DuplicaTooWeak")
        silver @talking2mouth "Sorry, red, but you aren't beating her at your current levels. Talking should be our first option... 'cause it's the only one that'll work."

    red @talking2mouth "What can you tell me about her?"

    silver @talking2mouth "Nothing. She's a Rocket, and that's all there is to her. She lives and breathes every word my Dad ever said."
    silver @talking2mouth "She only joined shortly before Team Rocket disbanded, but... she never acknowledged it when it did."
    silver @closedbrow talking2mouth "So I guess it wasn't {i}every{/i} word. Just most of them."

    red @talking2mouth "Is that really everything?"

    silver @closedbrow talking2mouth "[ellipses]She's a master of disguise. When Rocket was on its last legs, when we were gasping for breath, she infiltrated the Celadon police. Helped us avoid their probes."
    silver @talking2mouth "Not that it mattered. Saffron PD was on our tail, too, at that point. Celadon was happy to let them take point, and that was even before INTERPOL got involved."
    silver @closedbrow talking2mouth "Oh, and she's a Genwunner."

    red @confused "A what?"

    silver @talking2mouth "You know, she supports Genwun. The most right-wing party in the Kantonian Diet. Xenophobic, regressive, segregationist. Pushing for a foreign-Pokémon exclusion act, like what they've got in Galar."
    silver @talking2mouth "You should be fine, since you're from Kanto. Just don't say anything too complimentary about any other region."
    silver @closedbrow talking2mouth "{size=30}Except Johto, I guess. {i}Sometimes{/i} Johto is fine.{/size}"

    pause 1.0

    red @talking2mouth unamusedbrow "Good to know she's a bigot, I guess? I was kinda angling for a {i}name{/i}."

    silver @closedbrow frownmouth "..."
    silver @talking2mouth "I would've told you if I knew it. She's nameless, a ghost. She might not know herself. She calls herself 'The Magical Mimi.' Sometimes 'Lady Imite.' Sometimes 'Queen Rocket.'"

    $ PlaySound("pokemon/pikachu_angry3.ogg")

    libpikachu @angry "Pika!"

    red @confused "You said it, buddy. Sounds like she's got an ego."

    silver @talking2mouth "My father called her The Copycat. Still just a nickname, of course, but I guess it's probably the 'truest' one."

    $ BecomeNamed("Duplica")

    red @angrybrow talking2mouth "...Copycat, huh? Alright. Let's handle her."

    silver @sadbrow happymouth "{size=30}If only it were so easy.{/size}"
    silver @sadbrow talking2mouth "Word of advice. Don't let her put words in your mouth."

    red @confused "Hm?"

    silver @closedbrow talking2mouth "You'll see."

    scene blank2 with splitfade

    pause 1.0

    $ duplicacopying = "Red"
    scene abandonedhouse
    show copyred at night
    with dis

    pause 1.0

    $ location = "alley"

    pause 2.0

    red night @talking2mouth "I'm seeing double."

    duplica @winkbrow happymouth "Double the trouble, double the fun!~"
    duplica @happy "Hi, I'm [first_name] [last_name]. What's your name? Want to be friends?"

    red @unamusedbrow talking2mouth "I don't sound like that."

    silver night @sadbrow happymouth "{size=30}Kinda do.{/size}"
    
    red @talking2mouth "Who are you?"

    duplica @happy "Weren't you listening? I'm you!"

    red @closedbrow talking2mouth "No, you're not."

    duplica @winkbrow tonguemouth "Oh, you seem {i}confident{/i}. Well, if you know who I {i}amn't{/i}, you must also know who I {i}am{/i}, right?"

    redmind @thonk "Amn't?"

    duplica @talkingmouth "Go on, guess! Guess my name!"

    label duplicaguessname:

    python:
        duplica_name = renpy.input("What do you think The Copycat's true name is? (Enter for default.)", exclude="{}[[]%<>p", length=12)

        if (duplica_name == ""):
            duplica_name = "The Copycat"

    narrator "You believe The Copycat's true name is [duplica_name]?"

    menu:
        "Yes.":
            pass

        "No.":
            jump duplicaguessname

        "Obviously not, but I can't really Put the right oPtion, can I?" if (duplica_name == "DuPlica"):
            pass

    duplica @happy "Wrongamundo, little nobody! Who'd name their kid that? Guess I'm you after all, Slick!"

    duplica @talkingmouth "Want to say 'hi' to my super-rare, one-of-a-kind, hot-off-the-presses Pikachu? I never go anywhere without him. Say hi, [pika_name]."

    libpikachu night dittoeyes dittomouth "[ellipses]"

    pause 1.0

    duplica @angrybrow noshine talking2mouth "Speak, [pika_name]."

    libpikachu dittoeyes talkingmouth "Dittochu."

    duplica angrybrow frownmouth @talking2mouth "That's not what we practiced, is it? It's 'Pikachu.' 'Peek-a-chew.'"

    libpikachu dittoeyes dittomouth "[ellipses]"

    libpikachu dittoeyes talkingmouth "Pikadit."

    show abandonedhouse with vpunch

    duplica surprisedbrow @angrybrow talking2mouth "Stupid jelly! Of all my Ditto, you are by {i}far{/i} the worst!"

    red @angrybrow talking2mouth "Hey! Don't talk to your Pokémon like that!"

    show copyred playfulbrow playfulmouth with dis

    silver night @talking2mouth sadbrow "[first_name], I agree with you, but you need to back down[ellipses]"

    menu:
        ">Back down":
            $ AddEvent("Duplica", "DoNotChallengeDuplica")
            red @closedbrow frownmouth "[ellipses]{nw}"
            extend @closedbrow talking2mouth "Fine. We're here to talk, not battle."

            red @talking2mouth "I've got a question, though. Silver said you're a strong trainer--one of the strongest he's ever met."

            duplica @winkbrow talkingmouth "Aw! You flatterer, Silver. {i}About time{/i} you recognized my magnificence. What's your question, me?"
            
            red @talking2mouth "What is a trainer as powerful as Silver says you are doing working with Team Rocket?"

            jump negotationintro

        ">Make {i}her{/i} back down":
            $ AddEvent("Duplica", "ChallengeDuplica")
            red @talking2mouth "You were willing to go toe-to-toe with a champion for stealing [pika_name]'s cookie. What has this faker got over Lance?"

            duplica @winkbrow tonguemouth "Faker? I think you're the fake around here. You're comparing yourself to me? Ha. You're not even good enough to be my f--"

            red @angry "I'll make you eat those words!"

            python:
                trainer1 = MakeRed()
                trainer2 = MakeTrainer("Duplica")

            hide copyred
            call Battle([trainer1, trainer2], customexpressions=["red angrybrow frownmouth", "red angrybrow frownmouth", "copyred playfulbrow playfulmouth", "copyred winkbrow tonguemouth"], specialmusic="Nothing", dialogfunc=duplicadialog, stopmusic=False, customswitchbrain=duplicaswitchbrain) from _call_Battle_171
            $ RecordBattle("Duplica1")

            if (WonBattle("Duplica1")):
                show copyred surprisedbrow frownmouth at night with dis

                pause 1.5

                duplica @talking2mouth "You... beat me?"

                red @talking2mouth "I did. Now get out of here. Give Silver back his shack, his tenants, his... everything."

                pause 1.0

                $ ValueChange("Silver", 1, 0.25)

                silver @sadbrow talking2mouth "Look, [first_name], I appreciate what you did here. And it was nice seeing Copycat humbled for once."
                silver @closedbrow talking2mouth "But beating people up to get what we want is how my Dad operated. I don't want to 'rule' these guys by being bigger and tougher than them. Even if, you know, I {i}could{/i}."

                pause 1.0

                silver @sadbrow talking2mouth "And... right now, I can't. It was {i}you{/i} who beat her."

                red @sad2eyes talking2mouth "...I get it. Fine. But we have leverage now."
                
                $ duplicacopying = None

                red @talking2mouth "Copycat. Drop the disguise. We're negotiating now, got it?"

                show duplica rocket surprisedbrow frownmouth at night:
                    xpos 0.5
                    matrixcolor nightmatrix
                hide copyred surprisedbrow frownmouth
                with dis

                narrator "A couple of Ditto slough off of the figure in front of you, until all that's left is a very surprised-looking pigtailed woman."

                duplica @talking2mouth "Um. Okay."

                silver @sadbrow "[ellipses]"

                narrator "Silver seems to be looking at you with some concern[ellipses] you wonder if you made the right move, by fighting Copycat on his behalf."

                pause 1.0

                narrator "Whatever. You felt powerful, and it was pretty gratifying, forcing that smug brat into stunned silence."

                show duplica -surprisedbrow with dis

                jump negotiationsecondpart

            else:
                show copyred happybrow happymouth at night with dis

                silver @closedbrow talking2mouth "Damn. For a moment there, I thought..."

                $ ValueChange("Silver", 3, 0.25)

                silver @sadbrow happymouth "Well, whatever. Uh, thanks."

                red @sadbrow talkingmouth "You're welcome, but are we not going to address the elephant in the room?"

                silver @talking2mouth "I said she was strong."

                red @wince talking2mouth "'Strong' might have been underselling it, Silver."

                red @talking2mouth "What the hell is a trainer as powerful as you doing working with Team Rocket?"

            label negotationintro:

            duplica -happybrow smirkmouth @winkbrow tonguemouth "You might as well ask Scion Silver there the same thing!"

            silver @sadbrow talking2mouth "It's not the same. I was born into Rocket. Molded by it. I didn't get out of that basement until I was already a man."

            duplica @happy "Then I guess you never actually left, because you're still a little kid to me!"

            silver @angrybrow "[ellipses]"

            silver @talking2mouth "I'm not rising to your bait. You want me to get angry, want me to break something, want me to threaten or--"

            duplica @talking2mouth "I want you to {i}lead{/i}."

            silver @angrybrow talking2mouth "Yeah, well, I want you to drop dead."
            silver @sadbrow talking2mouth "Guess we're both disappointed."

            pause 1.0

            red @upeyes angryeyebrows talking2mouth "Oh my God, are you two exes?"

            duplica @happy "He wishes! I'm probably the only person in that basement who he didn't make a pass at! Probably knew I was out of his league, lololol."

            red @sweat talking2mouth unamusedbrow "{size=30}Please don't say that with my face.{/size}"

            if (HasEvent("Duplica", "ChallengeDuplica")):
                silver @talking2mouth "Enough bullshitting around. We're here to negotiate. You beat us, so obviously we can't force you into anything. Not that we'd try."

                duplica @winkbrow tonguemouth "Lololol. It's kinda wimpy saying you want to negotiate after I've kicked {i}both{/i} your butts, but maybe you can make this fun."

            else:
                silver @talking2mouth "Enough bullshitting around. We're here to negotiate. You beat me, so obviously I can't force you into anything. Not that I'd try."

                duplica @winkbrow tonguemouth "Lololol. It's kinda wimpy saying you want to negotiate after I've already kicked your booty, but maybe you can make this fun."

            silver @closedbrow talking2mouth "Just... stop looking like [first_name]."

            hide copyred
            show copysilver at night
            with dis

            $ duplicacopying = "Silver"

            narrator "A couple of Ditto slough off of the figure in front of you, reforming and re-joining to make a perfect copy of Silver."

            pause 2.0

            show copysilver happy with dis

            silver @angrybrow talking2mouth "That's not what I fucking meant."

            duplica smilemouth @happy "Lololol! I {i}love{/i} doing you, though. 'Grrr, I have feelings, I don't like being good at stuff, Pokémon are friends, Daddy issues, grrrrrrr.'"

            silver @angrybrow "[ellipses]"

            narrator "Silver's hands are clenched tightly enough the skin on his knuckles is starting to split... but he stays calm, speaking in a measured, level, voice."

            $ duplicacopying = None

            silver @talking2mouth "Copycat. Drop the disguises, and let us talk to you face-to-face."
            
            show duplica rocket flirtbrow smugmouth at night:
                xpos 0.5
                matrixcolor nightmatrix
            hide copysilver
            with dis

            duplica talkingmouth "Well, since you're so {i}desperate{/i}. First time you're seeing me, right, [first_name]? Ain't I a beaut?"

            show duplica angrybrow frownmouth with dis

            red @talking2mouth "Passable."

            duplica @talking2mouth "That's not a good start to the negotiations."

    label negotiationsecondpart:

    show silver at night with dis:
        xpos 0.33

    show duplica at night with dis:
        xpos 0.66

    silver @talking2mouth "You know what we want. What do {i}you{/i} want?"

    duplica @talking2mouth "You to come back, lead us, and revive Team Rocket."

    silver @talking2mouth "No."

    duplica @happy "Then we've got nothing to negotiate about!"

    silver @talking2mouth "Get creative. You want to make this work, trust me."

    duplica @sadbrow talkingmouth "Are you threatening me, Dear Scion Silver?"

    silver @angrybrow talking2mouth "I could go scorched earth. Blow the whistle on us to the cops. Take all of us down at once."

    duplica @talking2mouth "Mmm... yeah, the cops would probably get the grunts. But they'd never catch me, and you know it."
    duplica @talking2mouth "The only reason I'm staying here is because you and these grunts are my best chance of bringing Team Rocket back. If all the goons go away, there's no reason to stay here--I'll just go back to Kanto and try it again there."

    silver @angrybrow talking2mouth "Really. Ground zero. Where Rocket's logo shows up in kid's picture books as the emblem of {i}the bad guy?{/i} That's where you think you can make a comeback?"

    duplica angrybrow frownmouth @talking2mouth "Stop saying 'you!' It's 'us!' It's 'we!' After Johto, they're not expecting us to try Kanto again!"

    silver @angrybrow talking2mouth "But Johto {i}failed{/i}, and it failed miserably! There have been {i}four{/i} Rocket revival efforts, and {i}all of them{/i} failed!"
    silver @talking2mouth "Team Neo Rocket? Team GO Rocket? Team Great Rocket? Team Rainbow Rocket? You see what the goddamn common thread here is, right? It's Rocket!"
    silver @angrybrow talking2mouth "We will never succeed, we will never win, we will never come back, and it doesn't matter what stupid word you put between 'Team' and 'Rocket'! It's still just Rocket."
    silver @angry "Rocket is dead, and every time {i}you{/i} try to revive it, we just lose more of our people! People who could've turned things around!"

    duplica @closedbrow talking2mouth "The people don't matter, Scion Silver. All that matters is Rocket."

    silver @angrybrow talking2mouth "You're trying to bring back a ghost. No-one wants this."

    duplica @talking2mouth "If that's true, then why did the grunts side with me when I kicked you out?"

    silver @sadbrow talking2mouth "They... ugh. They side with whoever's strongest. You're not winning anyone over with your 'moral' arguments."

    duplica @talking2mouth "Psssh. So, even if I had a surefire, foolproof, plan to resurrect Team Rocket, you still wouldn't try it?"

    pause 1.0

    silver @sadbrow "[ellipses]"

    red @talking2mouth "No."
    
    silver @closedbrow talking2mouth "No."

    duplica @talking2mouth "So now this farmer's brat is speaking for you? What happened to {i}Giovanni's{/i} son?"

    silver @talking2mouth "He never had a son. Just a bunch of bastards."

    duplica @talking2mouth "Hmph. Daddy issues. For as much as you moan and complain about how he treated you, you're not doing any better."

    silver sadbrow @surprisedbrow talking2mouth "What?"

    duplica @talking2mouth "You ignore us on a good day. You hate us on a bad day. We've been hiding in this tiny shack, decomposing, for a {i}year!{/i} Maybe if you had some kind of plan, I wouldn't have been forced to coup you!"

    silver @angrybrow "[ellipses]"

    duplica @talking2mouth "It's so easy to get it all back, Scion Silver. All you have to do is say you're going to bring back Team Rocket. All I need is you to confess that. Because I know it's true! C'mon, just confess!"

    silver @talking2mouth "You've been trying to get me to say that for just as long as we've been hiding in this shack. Read my fucking lips."
    silver -sadbrow @angry "Rocket. {w=0.5}Is. {w=0.5}A. {w=0.5}Ghost."
    silver @talking2mouth "Rocket's dead, our dreams are dead, my Dad's dead, and my Dad personally killed all of them. This is what he wanted, and it's the one good thing he ever did."

    duplica @angrybrow talking2mouth "...Then you're never getting this shack back. And these grunts are mine. Before the end of the year, we'll be resurrected, and we'll have taken over this city."

    silver @angrybrow talking2mouth "You'll be curbstomped by Kobukan's students before you get out of this alley. Matori, Petrel, Sham--they'll all be arrested. Even the ones who are trying to be better."
    silver @sadbrow talking2mouth "Don't do it. Christopher's got a damn noodle shop. He's not a criminal. Not anymore."

    duplica @angrybrow talking2mouth "You want to stop this? {i}Take over{/i}."

    silver @angrybrow talking2mouth "No."

    pause 2.0

    show duplica at night:
        xzoom 1 xpos 0.66
        ease 0.5 xzoom -1

    duplica @talking2mouth "You have until the end of the year to change your mind, Scion. Then we move, and I don't care what happens to the grunts, as long as Team Rocket doesn't die quietly."

    pause 1.0

    duplica angrybrow talking2mouth "I'll be watching you. Don't trust anyone. If you try to double-cross me, I'll have already double-crossed you."

    hide duplica with dis

    pause 2.0

    silver @talking2mouth "Negotiations suck."

    red @sweat closedbrow talking2mouth "Yeah, I prefer battles, too."

    stop music fadeout 1.5
    queue music "audio/music/DontEverForget_start.ogg" noloop
    queue music "audio/music/DontEverForget_loop.ogg"

    call clearscreens() from _call_clearscreens_253
    scene blank2 with splitfade

    pause 1.0

    show screen currentdate
    scene city_A 
    with splitfade 

    pause 1.0

    show silver sadbrow with dis

    pause 1.0

    red @confused "Well, what do we do?"

    silver @closedbrow talking2mouth "I don't know. I need to stop her. She's smart--she won't do something suicidal like those guys in Johto did."
    silver @sadbrow talking2mouth "I don't know if she's really planning a full-scale assault on Inspira, since I doubt even {i}she{/i} could get away from that, but..."

    if (WonBattle("Duplica1")):
        red @sadbrow talking2mouth "I beat her, though."

        show silver:
            ypos 1.0 zoom 1.0
            ease 0.5 ypos 1.2 zoom 1.3

        narrator "Silver sighs and looks off in the distance. He pats your back, affectionately."

        silver @talking2mouth "You did. But I fought my way into this problem. I can't fight my way out of it, and you can't fight my way out of it, either."

    else:
        show silver:
            ypos 1.0 zoom 1.0
            ease 0.5 ypos 1.2 zoom 1.3

        narrator "Silver sighs and looks off in the distance. He pats your back, affectionately."

        silver @talking2mouth "You did good, red. Thanks. I don't know what we'll do next, but I'm glad you're there with me."
        silver @talking2mouth "I fought my way into this problem. I can't fight my way out of it, and you can't fight my way out of it, either."

    silver -sadbrow @closedbrow talking2mouth "There's one thing I know for sure, though. I need to get stronger."

    red @confused "What? I thought--"

    silver @talking2mouth "Not to beat her. Just to be strong enough {i}she{/i} can't beat {i}me{/i}."

    red @talking2mouth "Well, we can train harder, I guess..."

    silver @talking2mouth "That won't be enough."
    silver @sadbrow talking2mouth "I need my old Pokémon back. Absol can't carry me through this alone. Neither can you."

    pause 1.0

    silver @sadbrow talkingmouth "We're in this together, now. Sorry."

    red @talkingmouth sadbrow "Partners in crime?"

    silver @talking2mouth "Just [bluecolor]partners{/color}. No crime. {i}For once{/i}, no crime."

    red @sadbrow talkingmouth "Partners."

    silver @sadbrow smilemouth "Hm."
    silver @closedbrow talking2mouth "See ya around."

    hide silver with dis

    $ RelationshipRankUp("Silver", "Partner", 3)

    return