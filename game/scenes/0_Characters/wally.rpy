label Wally1:
    scene gym 
    show wally annoyedbrow
    with Dissolve(2.0)
    $ renpy.music.queue("Audio/Music/verdanturf.ogg", channel='music', fadein=0.0, tight=None)

    pause 1.5

    narrator "While walking into the Gym, you notice Wally is standing in front of the Battle Simulators." 
    narrator "Many of the trainers around him are engaged in actual battles, but he seems transfixed on the computer screen in front of him, hands quickly typing out calculations and setting up virtual scenarios."
    narrator "You watch for a moment, but he seems quite invested in his task, only pausing every once in a while to scribble something in a Flygon-themed notebook open on the desk next to him."
    narrator "Curious, you decide to approach."

    menu:
        "You know, real battles are more helpful.":
            $ AddEvent("Wally", "Condescend")
            wally -annoyedbrow @surprisedbrow frownmouth "Hm?"
            wally @closedeyes angryeyebrows talking2mouth "I know. My Pokémon are tired. I'm waiting for them to rest up--I thought I'd put some hours into the simulator in the meantime."

            red @sweat talking2mouth "Oh. Uh, sorry. Shouldn't have assumed."

        "What're you working on?":
            $ AddEvent("Wally", "Curious")
            wally -annoyedbrow @surprisedbrow frownmouth "Hm?"
            wally @happy "Oh, hi, [wally_name]."
            wally @talkingmouth "My Pokémon are tired. I'm waiting for them to rest up--I thought I'd put some hours into the simulator in the meantime."

            red @talkingmouth "Ah, I get it now."

    red @talkingmouth "Seems you take training really seriously, huh?"

    wally sad2eyes @sadbrow talkingmouth "I try to."

    pause 1.0

    redmind @thonk "Hm. He's... avoiding eye contact. He does that a lot, huh? Even though he's a friendly guy who I'm pretty sure likes me, it feels like he's always a bit uncomfortable."

    pause 1.5

    red @happy "Hey, are you near a good stopping point?"

    wally @talking2mouth "Just about. Just wrapping up some speed tie probability matrices..."

    pause 1.0

    wally -sad2eyes @talkingmouth "Okay, I'm done. What, um, what can I help you with, [wally_name]?"

    red @talkingmouth "Not sure it's something you can help me with as much as it's just... something I'd like to do together with you."

    wally surprisedbrow @neutraleyes neutraleyebrows talking2mouth "...I'm sorry?"

    red @happy "Let's go grab some food from the cafeteria."

    if (IsMorning()):
        red @talkingmouth "You know, a late breakfast. Brunch."

    elif (IsMidday()):
        red @talkingmouth "You know, an early lunch. Late breakfast, maybe. Brunch."
    
    elif (IsEvening()):
        $ AddEvent("Wally", "LunnerJoke")
        red @talkingmouth "You know, a late lunch. Early dinner, maybe. Lunner."

    $ brunchlunner = "Brunch" if IsEarlier() else "Lunner"

    wally -surprisedbrow @talking2mouth "Oh. Sure. [brunchlunner]."

    wally @talkingmouth "Let me just grab my notebooks."

    narrator "Wally closes his Flygon-themed notebook, and puts it in a small bag, which, despite its small size, you notice he visibly struggles to pick up."

    wally @sweat talking2mouth "That's... {w=0.5}{i}cough{/i}. Heavy."

    red @confused "Want a hand?"

    wally @happy "I should probably do it. 'Gotta get in my reps,' you know."

    red @happy "Hah, you sound like Brendan."

    wally @sad2eyes sweat talkingmouth "Y-yeah. I was quoting him."

    red @talking2mouth "Fair. C'mon, then."

    scene blank2 with splitfade

    pause 1.0

    narrator "You make your way to the cafeteria, Wally lagging behind somewhat as he struggles under the weight of his big bag."

    pause 1.5

    scene cafe
    show wally happybrow smilemouth 
    with dis

    narrator "A few minutes later, you're sitting across from Wally, as he happily digs into a Coba Berry parfait."
    
    wally @happymouth "I'm telling you, [wally_name], you need to try one of these. They're the best thing this cafeteria serves."

    red @talkingmouth "Call me old-fashioned, but I think you really can't go wrong with a plain old Pecha Berry. I mean, Coba berries are so dry and bitter."
    
    wally @confusedbrow talkingmouth "Well, yeah, but that's the point. The yogurt and honey glaze offsets the natural bitterness of the berry. It's, like, the {i}perfect{/i} bittersweet combination."

    red @sadbrow talkingmouth "Not sure I can agree with you there."

    wally -happybrow @talkingmouth "Well... I guess my tastes were pretty influenced by May's, and she'd eat pretty much anything she can fit into her mouth."
    wally @sweat talking2mouth "I never got her appreciation for spicy food, but... other stuff, sure."

    red @thinking "Hm."

    pause 1.0

    wally @talkingmouth "Hm?"

    red @talkingmouth "You mentioned Brendan earlier, and May just now. You're...?"

    wally -smilemouth @talking2mouth "Oh, we're dormmates."

    red @confused "Sure. Was there something more?"

    show wally sideeyes with dis

    pause 1.0

    wally @talkingmouth "There... might've been. I mean, we knew each other in Hoenn."

    red @happy "Wow! Three childhood friends all ending up in Kobukan at the same time? What're the odds of that?"

    wally -sideeyes @closedbrow sweat talkingmouth "Y-yeah. Uh, it's... pretty unlikely."
    wally @confused "Although, actually... doesn't it seem like a lot of Kobukan students joined with someone they knew when they were younger? May and Brendan, Serena and Calem, there's these two students called Hilbert and Hilda, the Galarians..."

    red @confused "...Huh. Yeah."

    wally @closedbrow talkingmouth "I guess that's 'gravity'. In, um, the metaphorical sense."

    pause 1.5

    show wally sadeyes with dis

    stop music fadeout 2.0
    queue music "audio/music/lament.ogg" fadein 10.0

    red @talkingmouth "Well, uh, tell me about your time in Hoenn. I know the gist of Brendan and May's relationship back then, but I don't think I knew you were part of it."

    wally @talking2mouth "Oh. Um, I wasn't. I mean, we knew each other, and we were friendly, but we weren't really... {i}friends{/i}."
    wally @sadbrow talkingmouth "I couldn't be, actually. I was... {w=0.5}{i}Cough{/i}."

    pause 1.0

    red @confused "What?"

    wally @angrybrow talking2mouth "Weak."

    pause 1.0

    scene blank2 with Dissolve(2.0)

    pause 1.0

    call clearscreens() from _call_clearscreens_255
    scene forest3 at sepia 
    show flashback
    with Dissolve(2.0)

    $ hideside = True

    wally "C'mon, guys, wait up for me! You're going too fast!"

    may "C'mon, Wally! Ya can't keep laggin' behind like that or we'll forget you're even with us!"

    brendan "I {i}cannot{/i} believe I allowed you to convince me to drag me into this filthy forest. Don't you know bugs could drop from the treetops at any moment? I'll need to take the {i}longest{/i} bath when I get home."

    may "Whatcha mean by that? We're here {i}for{/i} the bugs!"

    brendan "Oh, spare me the thought! You wild girl, you're intolerable! Bug Pokémon are repulsive--not cute, nor beautiful, at all!"

    may "Yeah? Well, what's the first part of Beautifly's name, then?"

    brendan "I've never heard of that Pokémon, but based on Ariados and Heracross--"

    may "Hah! You ain't got any idea what Beautifly are."

    wally "{size=30}Guys! I {i}need{/i} you to slow down!{/size}"

    may "...Huh? Didja hear something, Brendan?"

    brendan "Don't try to distract me. I know the moment I look away from here, you'll probably throw a bug at me, tear your clothes off again, and leave me stranded in this creepy forest."

    may "It ain't creepy, you posh-pantsed prick! It's gotta beauty way more than all that wax you use on your Pokémon, or that dumb hair dye you use!"

    brendan "{size=30}What?{/size} I didn't dye my... this is a {i}hat{/i}!"

    wally "{size=20}Guys-- please, I can't-- I can't breathe, I--{/size}"

    may "Oh, so you're the proper guy who's always sayin' 'wear synthetics', 'brush yer teeth', and stupid stuff like that, but you think wearin' a floppy glove on your head is fashion?"

    brendan "You phillistine! This {i}is{/i} high fashion--a custom-knit beanie made by Valerie {i}herself{/i} before she left Johto! Before she even started her fashion career! Don't you understand what that means?"

    wally "{size=20}Guys...{/size}"

    show forest3:
        matrixcolor SepiaMatrix() * SaturationMatrix(1.0)
        ease 5.0 matrixcolor SaturationMatrix(0.0)

    pause 2.0

    $ hideside = False

    wally @sadbrow talking2mouth "I was weak. I couldn't keep up with them."

    red @talking2mouth "But... you were kids, right? What were they even doing that you couldn't keep up with? Battling, or contests, or..."

    wally @sadbrow talkingmouth "[first_name], I'm being literal. I {i}physically{/i} couldn't keep up with them, because I was {i}physically{/i} weak."

    red @sadbrow talking2mouth "{size=30}What...?{/size}"

    wally @sadbrow talkingmouth "There was one time... ha. There was one time when we were all running into Petalburg forest. They were going to catch a Pokémon. I think... I think that was the day they caught Brendan's Shroomish, actually."
    wally @talkingmouth "May was strong and wild. Brendan had long legs. They both got ahead of me, as I struggled behind. And I, uh..."
    wally @sideeyes talking2mouth "I started having an attack. I couldn't breathe. And, uh, I tried to scream for help, but..."
    wally @happy "Turns out you need air in your lungs to do that. I just fell to the ground, and gasped, and... and I almost passed out. But I didn't. I stayed awake."
    wally @talking2mouth "I stayed awake, gasping for breath, trapped in the tall grass, breathing, desperately hoping someone would notice me... for two hours."

    $ hideside = True

    show forest3:
        matrixcolor SaturationMatrix(0.0)
        ease 1.0 matrixcolor SepiaMatrix()

    wally "{size=30}Help. Please... someone, help.{/size}"
    wally "{size=30}I don't want to die here. I don't want to be left behind. I don't want to be forgotten.{/size}"
    wally "{size=30}I don't want to be... weak.{/size}"
    wally "{size=30}I don't want to be weak.{/size}"

    pause 1.0

    show forest3 at vpunch

    wally "{size=50}I don't want to be WEAK!{/size}"

    scene blank2 with splitfade

    $ hideside = False

    pause 1.0

    show cafe
    show wally
    with splitfade

    wally @sadbrow talkingmouth "I couldn't move, but... I eventually got enough of my breath back that I could fill my lungs with air slowly, by working up to it. I had to train my lungs to take in more air as I was trying to breathe it out."
    wally @sad2eyes talking2mouth "I screamed. Brendan and May were long gone by that point, but... I hoped someone would hear me."

    stop music fadeout 2.5
    queue music "audio/music/verdanturf.ogg" fadein 10.0

    wally @talkingmouth "And then someone did."

    show wally:
        xpos 0.5
        ease 0.5 xpos 0.33

    $ raltsspecies = GetTrainerTeam("Wally", "Ralts").GetNickname()

    $ DisplayPokemon(raltsspecies)

    if (raltsspecies in ["Ralts", "Kirlia"]):
        red @talkingmouth sadbrow "This little guy?"
    else:
        red @talkingmouth sadbrow "This guy?"

    wally @talkingmouth "Yep."

    if (raltsspecies != "Ralts"):
        wally @talkingmouth "He was just a Ralts then, of course."

    show wally:
        xpos 0.33
        ease 0.4 xpos 0.5

    $ HidePokemon()

    wally @confused "You know, it's funny--everyone knows Ralts can sense emotions through their horns, right?"

    red @talking2mouth "Uh... most people don't know that, but I guess you and I do, sure."

    wally @closedbrow talking2mouth "Why do we specify for Ralts, specifically, that they can sense emotions {i}from their horns{/i}?"
    wally @talking2mouth "I mean, Hatterene can do it. Sylveon can do it. Blissey can do it. But no-one ever specifies {i}how{/i} they do it, right?"
    wally @confused "And why the horns, specifically? Because people say that Ralts read emotions with their horns, like that explains anything. Horns can't do that. Houndoom has horns, but it's not reading emotions with them."

    red @surprisedbrow frownmouth "[ellipses]"

    wally @closedbrow talking2mouth "There's, like, Shuppet, which is also able to read emotions through its singular horn... but that's not a horn in the traditional sense." 
    wally @talking2mouth "It's just an extrusion, it's the same ectoplasmic, fleshy, material the rest of the Pokémon is made of."
    wally @talkingmouth "I think I need to read the report where they identified Ralts' horn as the conduit for its empathy, because I'm not sure I'll ever understand, otherwise."

    pause 1.5

    show wally surprisedbrow frownmouth with dis

    red @confused "Dude, if this is what Coba berries make you think about, I think I {i}do{/i} need to try them out."

    wally -surprisedbrow @happybrow lightblush talkingmouth "Ah-ha... sorry, [wally_name]. I get kind of into Pokémon biology and history. I just wish I understood the 'training' part as well."
    wally @closedbrow talking2mouth "Anyway, where was I in this story...?"

    red @closedbrow talking2mouth "Uh, you were writhing about and choking in the grass."

    wally @sad2eyes talking2mouth "Oh. Yeah."
    wally @sadbrow talkingmouth "Well, [raltsspecies] must have sensed my panic, and my... my helplessness."
    wally @closedbrow sweat talking2mouth "{size=30}With his horn, I guess.{/size}"

    pause 1.0

    wally @closedbrow talking2mouth "It's funny, actually. Ralts are {i}never{/i} seen so far West of Petalburg. He must've sensed me panicking and freaking out from miles away."
    wally @happy "I'm glad he did. He came up to me, put his little hands on my chest, and... sat on me."

    red @confused "What?"

    wally @closedbrow talking2mouth "Yeah, it didn't help me breathe. But..."
    wally @sideeyes talkingmouth "It did help me calm down. He was chattering away a storm. I guess {i}he{/i} thought he was helping. Since I got up from the grass that day, and was able to make my way home, I guess maybe he did."
    wally @talkingmouth "He followed me home. And the next day, I went to the local Gym Leader, asked to borrow his Zigzagoon, and caught the Ralts that... more or less... 'saved me.'"
    wally @talking2mouth "I'd never thought about becoming a trainer before, but after that day... I knew it's what I had to do."

    red @talking2mouth "You just decided that after a single day?"

    wally @talkingmouth "Yeah. I... I mean, I don't blame Brendan and May. It was my own weakness that caused this."
    wally @angryeyebrows talking2mouth "But I can't be the kind of person who trails behind someone else. I can't be the kind of person too weak to keep up with my friends. I can't be forgotten behind, gasping for breath, ever again."
    wally @talking2mouth "I needed to be a Trainer. A strong trainer. Someone who can fight for himself, defend himself, and get what he wants for himself, and other people."

    pause 1.0

    wally @closedbrow talking2mouth sweat "But I was late. I mean, this only happened a few years ago. Everyone I knew had gotten into Pokémon years earlier." 
    wally @sadbrow talkingmouth "I'm playing catch-up to everyone here."

    red @sadbrow talkingmouth "I know how you feel, man. When I first showed up at Kobukan, I felt like I was being thrown in the deep end."

    wally @sadbrow talkingmouth "Really? You always seemed so confident."

    red @sad2eyes confusedeyebrows frownmouth "Hm..."
    red @confused "I guess I was, actually. Still am. Sure, I felt like I was being thrown in the deep end, but I know how to swim, and swimming in the deep end isn't any harder than swimming in the shallow end."

    wally @happy "Lucky! What's your secret?"

    red @sadbrow talkingmouth "A supportive mom and a close relationship with a world-famous Pokémon Professor."

    wally @closedbrow talking2mouth "...Might've missed the boat on that one."
    wally @closedeyes angryeyebrows talking2mouth "Wait, actually... I'm in Professor Rowan's class. He's world famous. And he..."
    wally @closedbrow talking2mouth sweat "Well, he {i}does{/i} remember my name, which is {i}basically{/i} a close relationship when it comes to him."

    red @confused "...Hey, I've got a question."

    wally surprisedbrow @neutraleyebrows neutraleyes talking2mouth "Yeah?"

    red @confused "Why did you hide during the first Quarter Qlash? When Lisia went to interview you, I mean. You don't seem like you're {i}that{/i} camera shy. "

    wally -surprisedbrow @closedbrow talking2mouth "...Can you keep a secret?"

    red @talkingmouth "Historically, no."

    wally @sadbrow talkingmouth "Alright. Then... I guess I can't tell you."

    red @closedbrow talking2mouth "Damn."

    pause 1.0

    red @sadbrow talkingmouth "What if I tried {i}really{/i} hard?"

    wally @happy "I guess that's good enough."

    wally @sadbrow talking2mouth "Well, after the incident in Petalburg woods, I was sent to Verdanturf. The air there is supposed to be really fresh and clean. A lot of people with conditions live there."
    wally @talking2mouth "Um... I was living with my cousin Wanda, before, and in Verdanturf, I was living with my Aunt and Uncle."

    redmind @sad2brow frownmouth "Hm... no parents mentioned."

    wally @closedbrow talking2mouth "But my Aunt and Uncle are going through a really messy divorce, and they split shortly after I moved there, and..."
    wally @sweat talking2mouth "They refuse to talk to each other except through me. I think you know where this is going."

    red @surprised "Oh my god, they have no idea you're here."

    wally @closedbrow talking2mouth "...Yeah."
    wally @sad2brow talking2mouth "Each of them thinks I'm with the other. Wanda thinks I'm with both of them. I took the Kobukan entrance exam behind their back, and they were none the wiser."
    wally @closedbrow talking2mouth "I think... they'll probably figure it out before I graduate, but I'm just hoping that they figure it out late enough they can't do much about it."

    pause 1.0

    red @confused "So... you just got into Kobukan? With almost no training experience?"

    wally @talking2mouth "'Kobukan is prepared to teach trainers with zero experience, or trainers who could already be champions'."
    wally @happy "That's what the website says, anyway."

    red @talking2mouth "Yeah, I've heard that. But, man, how are you going to pay for it? I mean, if your aunt and uncle don't know, and Wanda doesn't know, then who can pay for..."

    show wally sad2brow with dis

    narrator "Wally shifts uncomfortably, and coughs into his hand. Taking out a sanitary wipe, he rubs it over his hands several times, before slowly speaking, very precisely."

    wally @talking2mouth "My family has a lot of generational wealth. We're a pretty old and important family in Hoenn."
    wally @talking2mouth "The reason I, uh, never thought about becoming a trainer is because I don't, um... actually need to be a trainer. Or anything."
    wally @sadbrow talkingmouth "I could never work a day in my life and have everything I wanted."
    wally @talking2mouth "{size=30}Except my dignity...{/size}"

    red @confused "Wait, are you a Stone? Like, Steven, Devon Corporation?"

    wally @happy "Hah, no! Not {i}that{/i} important."

    red @confused "A Winstrate?"

    wally @surprisedbrow talking2mouth "Oh, that's a deep cut. But no, not a Winstrate, and not a Waters, either."
    wally @talking2mouth "We're not like that. But we have a good amount of money, and..."
    wally @sad2brow talkingmouth "Well, this is going to sound bad, but they won't really notice if a large amount of money goes missing."
    wally @sad2brow talking2mouth "I want to pay them back, of course... but I can't do that until I graduate."

    pause 1.0 

    red @talking2mouth "What do you want to do when you graduate?"

    wally sweat sad2brow frownmouth "[ellipses]"

    red @happy "C'mon. I won't laugh."

    wally -sweat -sad2brow -frownmouth @sadbrow talkingmouth "I wouldn't put money on that. Sometimes, when I take a step back and think about what I want to do, I can't help but laugh at it myself."
    wally @angrybrow talking2mouth "But... I want to make the {color=#50C878}{b}Dragon Ascent{/b}{/color}."

    red @confused "Wait... you mean, like, that tower in Hoenn?"

    wally @talking2mouth "You've heard of it? That's pretty unusual for a Kantonian. You know a {i}lot{/i} about Pokémon, huh, [wally_name]?"

    red @happy "Yeah, I'm kinda hyper-obsessed." 
    red @talkingmouth "Tell me about the Dragon Ascent, though. I think I know the gist, but there might be parts I'm missing."

    wally @talkingmouth "Sure. Um, there's a tower in Hoenn called the Sky Pillar. It was built thousands of years ago, by a tribe of native Hoennians called the Draconids."
    wally @closedbrow talking2mouth "It's got fifty floors. And it's an absolute deathtrap. Not just because it's made of thousand-year-old stone, but because it was {i}built{/i}, on purpose, to be full of traps and puzzles."
    wally @talking2mouth "We have to assume that {i}someone{/i} has successfully climbed it, but we don't have any records of it."
    wally @talking2mouth "Making it trickier, is, for the safety of people, it's been closed off to the public for centuries, with only Draconid and Sootopolitan descendants being permitted on the island it's on, for heritage and pilgrimage reasons."
    wally @sweat talking2mouth "And they're not climbing it, of course. Just worshipping, usually."

    pause 1.0

    wally @talkingmouth "If I can make it to the top, then... I'll be the first person in recorded history to do so. And there's a legend that if you reach the top, you can claim a kind of power that no-one's ever seen before."
    wally @closedbrow talking2mouth "From the descriptions, it sounds like some kind of powerful mythical Pokémon with a unique transformation--it seems similar to Mega Evolution, but not {i}exactly{/i} the same."

    red @talking2mouth "Wally... that sounds {i}really{/i} ambitious. "

    wally @sadbrow talkingmouth "Yeah. It is. It's insane. It would be insane if anyone else wanted to do it. And... it's even more insane that {i}I{/i} want to do it."
    wally @angrybrow talking2mouth "But I {i}do{/i}. And I'm going to."

    pause 2.0

    red @happy "Okay."

    wally surprisedbrow @confused "Wait, [wally_name], what do you mean 'okay?'"

    red @sadbrow talkingmouth "I mean I believe you. I think you can make the Dragon Ascent."

    pause 1.0

    wally -surprisedbrow @sad2brow lightblush talking2mouth "[wally_name[0]]-[wally_name]... C'mon. You're just humoring me. I mean, I haven't even shown you my notebooks."

    red @talking2mouth "Your notebooks? Oh, is that what was in them? That's why you have so many?"

    wally @happybrow happymouth "Heh heh. Yep. I've been taking notes on the Sky Pillar, and planning my Dragon Ascent for almost six years now."
    wally @sad2brow talking2mouth "I... should probably have spent that time training."
    wally @angrybrow talking2mouth "But it doesn't matter. I'm going to climb that tower before I graduate."

    red @surprised "Woah, what? Before you graduate? Isn't that cutting it a bit tight?"

    wally @sadbrow talkingmouth "...Yeah. But it's necessary. Like I said, I need to pay my family back. If I took that money, snuck off to Kobukan, and didn't do something to make it all worth it, then..."
    wally @angrybrow talking2mouth "Then I'd just be a thief. I hate thieves."

    pause 1.0

    wally @talking2mouth "And so did the Draconid people, because they built all these traps to keep thieves out of the tower, keep them away from getting to the treasure at the top."
    
    wally @talkingmouth "Here, take a look at some of my notes."

    show screen book_mixed_text(dragonascentnotes7) with Dissolve(3.0)

    pause

    red @surprised "Wow. You really put a lot of thought into this. And, uh... you {i}were{/i} really looking for a shortcut, weren't you?"

    wally @closedbrow talking2mouth "Believe me, I tried {i}so{/i} hard. I thought if I just looked hard enough, I'd figure out some way to get in that no-one's thought of, but..."
    wally @sadbrow talking2mouth "I guess, over the last 3,000 years, everyone else has had those thoughts, too."
    wally @closedbrow talking2mouth "The biggest problem is just that area of 'dead air', after about 500 meters."
    wally @angrybrow talking2mouth "I thought that I could just take a tank of air and a breathing mask up there... like I was going deep-sea diving... but I guess those ancient Draconids thought of that, too."
    wally @closedbrow talking2mouth "It's not just that the air is thin up there. It's that the air is {i}drained{/i} from everything that goes up there. A tank of air would empty in minutes. Lungs would empty in seconds."
    wally @angrybrow talking2mouth "It's like a giant vacuum, that leaves you breathless, no matter what you do. No matter who you get help from, unless you can figure out how to climb a third of the tower without needing to breathe, then..."

    red @confused "Wait. If the air is being sucked out of your lungs, then... doesn't that kinda... make you crumple? And die?"

    wally @sadbrow talkingmouth "If it was a regular vacuum, then yeah. But there's nothing regular about this place. It's made of three-thousand-year-old stone, but resists jackhammers."
    wally @closedbrow talking2mouth "The Draconids didn't want anyone getting to the top unless they were using {i}their{/i} method." 
    wally @talkingmouth "Two people, a Lorekeeper and a Loremaker, a Draconid Priestess and Priest, who would beseech the Lord Dragon to grant their wish..."
    wally @sadbrow talkingmouth "On the bright side, at least it's just trying to keep out the 'unworthy', not actually trying to {i}bury{/i} anyone who goes in."

    red @closedbrow talking2mouth "I feel like the floors where it's pulling the breath out of your lungs are pretty lethal."

    wally @unamusedbrow talking2mouth "It's survivable. Not fun, but survivable."

    red @surprisedbrow frownmouth "[ellipses]"
    red @closedbrow talkingmouth "Man, I say dumbass things sometimes."

    wally @happy "Nah. It's fine, [wally_name]."
    wally @sadbrow talkingmouth "To tell you the truth... this is actually the first time I've told anyone this plan."
    wally @closedbrow talking2mouth "Saying it out loud really makes it sound stupid, huh?"

    red @confused "What? No, it's not stupid."

    wally @sad2brow talking2mouth "...I take it seriously. But... I don't think anyone else ever could. I mean, maybe {i}you{/i} can't even take it seriously." 
    wally @sadbrow talkingmouth "It just feels like a big dream from a small guy. Like I'm trying to overcompensate for my lack of... {i}everything{/i} with ambition."

    red @sad2brow frownmouth "[ellipses]"

    wally @closedbrow talking2mouth "Well..."
    wally @sadbrow talkingmouth "Even if it's stupid, even if it's silly, I've spent too much time making this mistake to stop now. Six years, you know?"

    pause 1.0

    wally @happy "Thanks for hanging out with me, [first_name]."

    red @sadbrow talkingmouth "It wasn't a charity case. I enjoyed it."
    red @talking2mouth "I'm assuming that you're interested in looping me into this plan?"

    wally @sad2brow talking2mouth "I... don't know. A lot of the puzzles can only be solved by two people at once. A big guy and a small guy. It was meant to be a man and a woman, but..."
    wally sad2brow embarrassedmouth @sweat talking2mouth "Well, I'm a lot smaller than most guys. And you're kinda the perfect size for the 'big guy' role..."

    pause 2.0

    wally -embarrassedmouth@talking2mouth "It makes sense, but... I don't think so."

    red @confused "Huh? Why?"

    wally -sad2brow @sadbrow talkingmouth "I'm just not sure I can take it seriously. I mean, it's my own plan, and I'm not sure I can even believe that I'm actually planning it. That's gotta be a bad sign, right?"

    red @sadbrow talking2mouth "I think that just means that you're not confident. It doesn't necessarily mean it's not a good plan."

    wally @closedbrow talking2mouth "Well, it's not a plan, yet. It's barely a concept of a plan. I mean, I don't even know what the treasure at the top of the Sky Pillar is, yet. I have my theories, but I need to do some more research."
    
    red @talkingmouth "Sure. Keep me updated."

    wally @talking2mouth "Um... okay."

    if (not persondex["Wally"]["Contact"]):
        red @talkingmouth "You have a phone?"

        wally @surprisedbrow talking2mouth "O-oh! Yes, one second--"

        $ BecomeContacted("Wally")

    red @talkingmouth "Cool. Call me as soon as you make any progress on this, alright?"

    wally @talking2mouth "O... okay. What are you going to do?"

    red @happy "I'm going to do some research of my own. After all, if I'm going to be [bluecolor]the big guy{/color} climbing the tower with you, I should probably know a bit about the tower."

    wally @sad2brow talkingmouth lightblush "You... don't have to be, you know."

    red @happy "Yeah, I know. But I want to be. Sorry to be stubborn about this."

    wally @sadbrow talkingmouth "...Thanks, [wally_name]."

    red @talkingmouth "Chin up, Wally. We'll climb that tower and change the world. Count on it. The first person who has to take you seriously is yourself--and the rest of the world is right behind."
    red @winkbrow talkingmouth "Seeya."

    hide wally with dis

    pause 1.0

    $ RelationshipRankUp("Wally", "The Big Guy")

    return

label Wally1Part2:
    stop music fadeout 1.5
    queue music "audio/music/verdanturf.ogg"

    $ AddEvent("Wally", "Wally1Part2")

    show wally smilemouth headphones behind phone_A
    with fadeinbottom

    wally @happy "[wally_name]! I've made a {i}massive{/i} breakthrough!"
   
    red casual hatless @happy "Woah! I can tell. You seem to be in high spirits."

    wally @angrybrow talkingmouth "I {i}am{/i}."

    wally @surprised "I think I know what's on top of Sky Pillar. The Draconid writings I've been using for reference were frustratingly vague, but I think I just realized why!"

    red @confusedbrow talkingmouth "Shoot."

    wally @angrybrow talking2mouth "They consistently refer to it as DE. Third-party accounts of the Draconids refer to their worship of 'the Dragon Lord', though they rarely speak of their worship to outsiders."
    wally @closedbrow talking2mouth "Now, here's what I'm thinking. DE feels a lot like a term used to refer to a divine figure without saying their name explicitly, right?"

    red @confused "Sure?"

    wally @happy "Yeah, it does! A bunch of old religions used to avoid saying their god's name, out of respect. Like, Arceus used to be called Sinnoh before Hisui was renamed Sinnoh."
    wally @closedbrow talking2mouth "Groudon and Kyogre used to be referred to as the 'Ore's Ruler' and the 'Aqueous Sultan.' But in the writings of the early Stone and Waters clans, they would always refer to these 'gods' as OR and AS."
    wally @happy "Get it?! DE is written the exact same way that OR and AS is."
    wally @angrybrow talkingmouth "I don't know what DE means, but I'm pretty sure I know exactly who it refers to--the third of the Super-Ancient Pokémon, the dragon of the sky, Rayquaza!"

    red @surprised "What?!"

    wally @angrybrow talking2mouth "It makes perfect sense! Rayquaza isn't just some ordinary Flying-type--it's been worshipped for centuries, it's said to be able to control the very air itself, in all its forms!"
    wally @happy "Clear skies, gale winds, even just air at rest! Doesn't that sound {i}exactly{/i} like the kind of thing that could suck the very air from your lungs while climbing the tower?"

    red @surprised "Holy shit, it does!"

    wally @angrybrow talking2mouth "It's probably a defense mechanism--a way to make sure it isn't bothered when it's sleeping. Legends say Rayquaza lives in the ozone layer, and though Sky Pillar isn't {i}quite{/i} that tall, it's as tall as a manmade structure can get!"

    red @surprised "Oh my god."

    if (IsDate(year=2004)):
        wally @angrybrow talking2mouth "Wait, wait, there's {i}one{/i} more thing, and it's the biggest thing. When the Super-Ancient Pokémon were fighting in Sootopolis four years ago, reports said Rayquaza flew from the {i}Southwest{/i}."

    else:
        wally @angrybrow talking2mouth "Wait, wait, there's {i}one{/i} more thing, and it's the biggest thing. When the Super-Ancient Pokémon were fighting in Sootopolis five years ago, reports said Rayquaza flew from the {i}Southwest{/i}."

    red @surprisedbrow frownmouth "[ellipses]"

    wally @confusedbrow "[ellipses]"

    pause 1.0

    wally @closedbrow talking2mouth "Oh, wait, you're not good with geography, are you?"

    red @closedbrow talking2mouth "Admittedly crap."

    wally @happy "[wally_name], Sky Pillar {i}is to the Southwest{/i} of Sootopolis! It's directly, {i}immediately{/i}, Southwest!"
    wally @angrybrow talking2mouth "If Rayquaza was flying from {i}anywhere{/i} else, then it would have been seen by people in Pacifidlog, but it didn't make an appearance {i}anywhere{/i} but Sootopolis."

    pause 1.0

    wally @closedbrow sweat talking2mouth "...Now, I guess, if Rayquaza can teleport, then this part doesn't matter much, and I might be wrong."
    wally @talking2mouth "But the scientists who analyzed the footage of the 2000 disaster are pretty sure it's a Dragon/Flying-type. {i}They{/i} usually can't teleport."
    wally @sadbrow talkingmouth "[wally_name], this is huge! You get it, right? {i}I{/i} know where a legendary Pokémon is. I could even catch it. All I need to do is climb a tower that people have barely been able to enter for thousands of years!"

    pause 2.0

    wally @sweat talking2mouth "...Okay, that sounds bad, but I think this is still a tremendous step. At least I know what's causing the air lock, now. Maybe that'll help me figure out a way to get through it."

    red @talkingmouth "I'm proud of you, man. How did you even learn this stuff, though?"

    wally @closedbrow talking2mouth "I read a lot of history books. And I take notes on everything, of course."
    wally @talkingmouth "The biggest thing, though, was when I managed to talk to a Draconid Lorekeeper. Most of the information I have about the inside of the tower comes from her... and an interview Champion Wallace gave."
    wally @closedbrow talking2mouth "Anyway, I think our next step is--"

    stop music

    hide wally
    show blank2 behind phone_A:
        xzoom 0.26 yzoom 0.47 xalign 0.5 yalign 0.5
    with vpunch

    $ PlaySound("shatter.ogg")
    $ PlaySound("body crash.ogg")
    $ PlaySound("body roll.ogg")
    $ PlaySound("body punch.ogg")

    pause 0.5

    red @surprised "Wait, Wally?"

    queue music "audio/music/tension_start.ogg" noloop
    queue music "audio/music/tension_loop.ogg"

    pause 1.0

    red @surprised "{size=40}Wally?!{/size}"

    redmind @surprisedbrow frownmouth "Shit, what happened? It sounded like something broke a window, then he dropped his phone, and... is he alright? Maybe a Pokémon flew through the window."

    redmind @sad2brow frownmouth "...I might get in trouble for this, but, damn it, I need to make sure he's okay. I mean, it might be a frenzied Pokémon!"

    scene blank2 with splitfadefast

    narrator "You throw on some pants and your hat and quickly run outside, but immediately run into..."

    stop music fadeout 1.5
    show screen songsplash("Embracing One's Duty", "Zame")
    queue music "audio/music/embracingonesduty.ogg"

    scene hall_A2b 
    show skyla surprisedbrow frownmouth:
        xpos 0.25 ypos 1.0 zoom 1.0
        ease 0.8 ypos 1.2 zoom 1.3
    show silver surprisedbrow frownmouth:
        xpos 0.75 ypos 1.0 zoom 1.0 xzoom -1
        ease 0.8 ypos 1.2 zoom 1.3
    show cheren surprisedbrow:
        xpos 0.5 ypos 1.0 zoom 1.0
        ease 0.8 ypos 1.2 zoom 1.3
    with vpunch
    
    $ PlaySound("body punch.ogg")

    silver @sadbrow talking2mouth "Shit, sorry. Are you alright?"

    show skyla:
        xpos 0.25 ypos 1.2 zoom 1.3
        ease 0.5 ypos 1.0 zoom 1.0
    show silver:
        xpos 0.75 ypos 1.2 zoom 1.3
        ease 0.5 ypos 1.0 zoom 1.0
    show cheren sadbrow:
        xpos 0.5 ypos 1.2 zoom 1.3
        ease 0.5 ypos 1.0 zoom 1.0
    with splitfadefast

    red casual @wince talking2mouth "Yeah, sorry. I was just in a rush. I..."

    cheren @shadow "[ellipses]"
    cheren surprisedbrow @neutraleyes neutraleyebrows talking2mouth "How disappointing it is to find you in flagrant violation of the rules. You're normally more subtle."

    red @angrybrow talking2mouth "Can it, Cheren. I think Wally's in trouble. I was talking with him on the phone, and something just smashed through his window. He's not answering his phone."

    narrator "Cheren's standoffish attitude immediately shifts, and he nods, curtly, but understandingly."

    cheren -surprisedbrow @talking2mouth "I understand. Disciplinary Committee, come with me. [first_name], you may go back to your room. We will--"

    red @unamusedbrow talking2mouth "Did you think for even a second I would do that?"

    cheren upeyes angryeyebrows @talking2mouth "I entertained the thought. Fine, come with us. To avoid breaking the rules, I'll call you a temporary Disciplinary Committee member."

    red @closedbrow talking2mouth "Call me whatever you like. I'm doing this because Wally's my friend."

    scene blank2 with splitfadefast

    pause 1.0

    narrator "You and the Disciplinary Committee hurry to Wally's dorm--Dorm 151, the one you previously occupied."

    scene hall_A2b with splitfadefast

    skyla @angrybrow talking2mouth "There's the door. No signs of forced entry or recent exit from this side. Whatever's going on is still going on inside."
    skyla @angrybrow happymouth "C'mon, let's bust it open!"

    silver @closedbrow talking2mouth "Look, he might've just fallen through the window and dropped his phone, then. There aren't any sounds coming from inside right now, so whatever happened, it's over. We should come back in the morning."

    cheren "[ellipses]"

    narrator "Cheren gives you an uninterpretable look."

    scene door with Dissolve(2.0)

    cheren @talking2mouth "We will knock."

    $ PlaySound("knock.ogg")

    pause 2.0

    cheren @talking2mouth "This is the Disciplinary Committee. We heard there was some sort of disturbance."

    narrator "From inside, you hear the sound of whispered, muffled voices, and furniture being shoved. And then... a sob."

    pause 2.0

    $ hideside = True

    brendan "Hey, man, it's nothing. We just... {size=30}crap, there's glass everywhere{/size}... we need some space, okay?"

    $ hideside = False

    pause 0.2

    silver @talking2mouth "{size=30}There, like I said. May and Brendan probably just... y'know. Broke something. Not the first time this year.{/size}"

    cheren @sad2brow talking2mouth "{size=30}I know doing your duty in this job is not particularly an interest of yours, but ignoring the obvious signs of {i}something{/i} happening here makes me rather suspicious.{/size}"

    silver @sad "[ellipses]"

    cheren @talking2mouth "We apologize. We need to come in and see for ourselves. Is everyone decent? We would like you to unlock the door."

    $ hideside = True

    serena "Oh, no! No, I am afraid I am terribly {i}indecent{/i}! Yes, not a scrap of thread on me! Isn't that right, Calem?"

    pause 1.5

    calem "...I am not looking at Serena, so I could not say for certain."

    may "I am! And this girl's not wearing anything that Mother Nature didn't give her!"

    brendan "Wait, really?!"

    pause 1.0

    brendan "Oh. Right, this is part of... yeah, I get it."

    pause 1.0

    brendan "Yeah, naked."

    $ hideside = False

    pause 0.2

    skyla @closedbrow talking2mouth "{size=30}Alright. I'm a girl, so I'll go in to confirm.{/size}"

    cheren @upbrow talking2mouth "{size=30}Your sacrifice is as noble as it is unnecessary.{/size}"

    cheren @talking2mouth "I understand. Would you be able to find some clothes, perhaps, if I told you that [first_name] is with us?"

    narrator "Whispered discussion is heard from behind the door."
    
    $ hideside = True

    brendan "Yeah, we can do that."

    $ hideside = False

    pause 0.2
    
    cheren @upbrow talking2mouth "{size=30}I {i}detest{/i} how effective that is.{/size}"
    cheren @sadbrow talking2mouth "Nevertheless, we can go in now. Perhaps, [first_name], you should lead the vanguard."

    red casual @talking2mouth "Okay."

    scene dooropen with dis

    red casual @talking2mouth "I'm coming in. Everyone, be decent, or be okay with being indecent around me."

    call clearscreens() from _call_clearscreens_256
    scene blank2 with splitfade 

    stop music fadeout 1.5
    queue music "audio/music/lament.ogg"

    narrator "You walk into a sorry scene. The small dorm has clearly been ransacked. The window is shattered and notebooks and backpacks are tossed around. And on the floor, knees up to his chin, a blank expression on his face..."

    wally soullesseyes neckphones "[ellipses]"

    red casual @sadbrow talking2mouth "Wally?"

    may casual @sadbrow talking2mouth "Someone just came through the window and... snatched Wally's bag. Grabbed a couple random books off the bookshelf, too, then left the way they came."

    serena pajama @angrybrow talking2mouth "It was like some sort of wild beast! It behaved like... like an aggressive Primeape!"

    calem @sadbrow talking2mouth "Or Passimian, perhaps. Whatever the case, it was a very truculent monkey."

    red @sadbrow talkingmouth "Wally, buddy? Are you with us?"

    pause 1.0

    narrator "Wally's chest is rising and falling rhythmically, but you can't see any life behind his eyes."

    wally @talking2mouth "...They took it."

    pause 1.0

    red @sadbrow talking2mouth "Your notes?"

    wally @talking2mouth "Everything. Every notebook. Every-- everything."

    pause 1.0

    wally @talking2mouth "Six years."
    wally tearfuleyes sadeyebrows tears @talking2mouth "{i}Six years.{/i}"

    pause 2.0

    red @sadbrow talking2mouth "C'mon, buddy. Get up. You should probably go to the infirmary."

    narrator "Wally numbly stands up, taking your proffered hand. He wobbles slightly."
    narrator "He seems perfectly fine, physically... but you, and everyone else in the dorm, can feel his heartbreak."

    scene blank2 with splitfade

    narrator "You make your way to the infirmary in silence. The residents of Dorm 151 awkwardly look at each other, unsure how to console Wally, unsure what was even stolen."
    narrator "The Disciplinary Committee, for its part, does its job dispassionately, and ensures that no-one is breaking curfew by escorting the six people breaking curfew."

    scene lobby_night 
    show calem sadbrow:
        xpos 0.9 xzoom -1
    show serena hatless sadbrow frownmouth behind calem:
        xpos 0.8 xzoom -1
    show brendan casual sadbrow frownmouth behind serena:
        xpos 0.7
    show may casual sadbrow frownmouth:
        xpos 0.6

    show wally:
        xpos 0.45

    show silver sadbrow:
        xpos 0.1
    show skyla sadbrow frownmouth behind wally:
        xpos 0.3
    show cheren sadbrow:
        xpos 0.2
    show screen currentdate
    with splitfade

    wally tears @talking2mouth "Wait."

    red casual @talking2mouth "...Yeah, bud?"

    pause 1.5

    wally @talking2mouth "...They took six years of my notes. Of my research. Of my preparations."

    red @talking2mouth "Yeah. They did."

    wally @closedbrow talking2mouth "They just... snatched it from the floor, before I could even think to throw a Poké Ball out."
    wally @sadbrow talking2mouth "And... I probably wouldn't have been strong enough to stop them, anyway."

    red @talking2mouth "I'm sorry."

    wally -tears @closedeyes angryeyebrows talking2mouth "No, no, that's not what I mean."

    wally confusedbrow @talking2mouth "What I mean is... why did they steal it?"

    pause 1.0

    red @confused "I... guess they wanted your notes?"

    wally @closedbrow talking2mouth "That makes sense. But if they were just trying to get my school notes, then... they didn't have to break into my dorm."
    
    show brendan surprisedbrow
    show may surprisedbrow
    with dis
    
    wally -confusedbrow @angrybrow talking2mouth "They wanted to steal my notes on the Dragon Ascent."

    brendan @talkingmouth "Wait, Wally, you aren't plannin' to make one, are you?"

    wally @closedbrow talking2mouth "Yes, I have been. For six years."

    may @surprised "But, Wally, that's... that's, like, the most dangerous thing you can do, right?"

    wally @closedbrow talking2mouth sweat "Well, no-one's died..."

    brendan @talking2mouth "Yeah, but, dude, that's because no-one's {i}done it{/i}."

    wally @angrybrow talking2mouth "Look, that's not the point. Think about it. They wanted to steal my notes. You see what that means, right...?"

    pause 2.0

    $ PlaySound("idea.ogg")

    show calem surprisedbrow 
    show serena surprisedbrow
    show silver surprisedbrow
    show skyla surprisedbrow
    show cheren surprisedbrow
    with dis

    stop music fadeout 1.5
    queue music "audio/music/verdanturf.ogg"

    red @surprised "Holy shit, you did it!"

    wally @sadbrow talking2mouth "And if I didn't, then the thief at least {i}thinks{/i} I did."

    skyla -surprisedbrow @talking2mouth "Um... why are we happy now?"

    silver -surprisedbrow @talking2mouth "Think about it. Why do people steal?"

    # FIX THIS: Change this if/when Skyla gets a bit more of an enlightened attitude
    skyla @talking2mouth "Because they're evildoers who want to cause pain!"

    silver @angry "No, airhead. Sometimes it's to survive, sometimes they're forced into it, but they only steal things that they think are worth stealing, right?"

    skyla @surprised "Oh!"

    wally @talkingmouth "Whoever stole my notes... thought they were worth stealing. That means I {i}must{/i} have been onto something."
    wally @sadbrow talking2mouth "That means... maybe... they took me seriously." 

    show cheren smilemouth sadbrow
    show silver closedbrow smilemouth
    show skyla neutralbrow neutralmouth
    show calem neutralbrow smilemouth
    show serena neutralbrow neutralmouth
    show brendan neutralbrow neutralmouth
    show may neutralbrow neutralmouth
    with dis

    wally @sadbrow talkingmouth "Maybe now I can too."

    red @happy "Seems like the thief might've just done you a favor, then."

    wally @closedbrow talking2mouth sweat "Well... I wouldn't go that far. After all, I {i}do{/i} still need those books."
    wally @sad2brow talking2mouth "I've been thinking about this for six years, so I've got a lot of it memorized. But I definitely can't try to scale the tower without them."
    wally @angrybrow talking2mouth "We still need to find the thief. But we've got a lead."

    red @confused "We do?"

    wally @sadbrow talkingmouth "You're the first person I ever told about my plan to make the Dragon Ascent, [wally_name]. Immediately after I told you, my notebooks were stolen? There's a connection there."
    wally @talking2mouth angrybrow "The thief has to be a Kobukan student. They're the only person who could've been listening in on our conversation in the cafeteria."
    wally @closedeyes angryeyebrows talking2mouth "It wasn't even that busy... if I think really hard, I'm sure I can remember who was around us then..."

    silver @closedbrow talking2mouth "{size=30}Oh, thank god. I thought it was one of my guys...{/size}"

    cheren @closedbrow talking2mouth "I must step in and say that the Disciplinary Committee cannot approve of any sort of vigilante justice."

    skyla @sadbrow talkingmouth "{size=30}Unless you've got a really good reason...{/size}"

    cheren @talking2mouth "We will report this incident to the Student Council, who will elevate it to Dean Drayden. If you happen to find the thief, do not attempt to confront them, nor to apprehend them. Just let us know."

    pause 2.0

    calem @closedbrow talking2mouth "Realistically, Cheren, do you think there's any chance of that?"

    cheren @talking2mouth sad2brow "Hope springs eternal."
    cheren @talking2mouth "Now, I believe that the mood has been somewhat restored, so there is little reason to continue bringing this entire menagerie to the infirmary."
    cheren @talking2mouth "The Disciplinary Committee can bring Wally to Nurse Miriam. Everyone else... please return to your dorms."

    wally @sadbrow talking2mouth "I'm not sure I really need to go any more, but... I probably should."
    wally @closedbrow talking2mouth "Darn it. I want to write about this..."
    wally @sadbrow talkingmouth "But I probably should check in with Nurse Miriam, just in case."

    red @talking2mouth "Alright."
    red @sadbrow talkingmouth "Talk to you later, buddy?"

    wally @angrybrow talking2mouth "Yeah. Talk to you later. This thief might've been trying to stop me from climbing that tower, or maybe they want to climb it first themselves, but..."
    wally angrybrow talkingmouth "Whatever they had planned, they messed with the wrong wimp."

    $ ValueChange("Calem", 1, 0.9, False)
    $ ValueChange("Serena", 1, 0.8, False)
    $ ValueChange("Brendan", 1, 0.7, False)
    $ ValueChange("May", 1, 0.6, False)
    $ ValueChange("Silver", 1, 0.1, False)
    $ ValueChange("Cheren", 1, 0.2, False)
    $ ValueChange("Skyla", 1, 0.3)

    stop music fadeout 3.0

    call clearscreens() from _call_clearscreens_257
    scene blank2 with Dissolve(3.0)

    pause 2.0

    scene lobby_night with splitfade

    pause 1.0

    $ hideside = True

    zinnia "'Wimp' is right. That little kid thinks he can make the Dragon Ascent?"

    queue music "audio/music/theonlyhero.ogg"

    show zinnia poutmouth angrybrow:
        xpos -0.1 
        ease 0.5 xpos 0.5

    pause 2.0

    $ hideside = False

    zinnia @talking2mouth "But, phew, that was too close. His entire dorm showing up, the Disciplinary Committee, {i}and{/i} [first_name] [last_name]?"
    zinnia @happy "Didn't expect that! Now it's almost getting a bit exciting!"

    $ sidemonnum = pokedexlookupname("Whismur", DexMacros.Id)
    $ PlaySound("pokemon/cries/{}.mp3".format(sidemonnum))

    sidemon "Mum..."

    zinnia @sadbrow talkingmouth "Aw, don't cry, li'l Aster. You're too cute for that. It's fine, it's fine! We couldn't let that kid disrespect our heritage, could we? Besides, with his noodley arms, he'd probably just hurt himself."
    zinnia @starbrow yanderemouth "Think about it like that! We're {i}heroes{/i}!"

    $ PlaySound("pokemon/cries/{}.mp3".format(sidemonnum))

    sidemon "Mum."

    zinnia @happy "Ahahahaha! And did you see his expression? He was so sad and heartbroken, and was all 'oh, no, please don't steal my stupid little notebooks that I write my stupid little notes in!'"
    zinnia angrybrow frownmouth @angrymouth "It serves him right! Only a Draconid deserves to climb the tower! Only a Draconid Lorekeeper! I'm doing this for {i}Aster{/i}, and he's just doing it because he's a kid who doesn't {i}get{/i} it!"

    $ PlaySound("pokemon/cries/{}.mp3".format(sidemonnum))

    sidemon "Whis... Mum?"

    zinnia @closedbrow talking2mouth "No, not you, sweetheart, I'm doing it for {i}big{/i} Aster."
    zinnia @starbrow talkingmouth "But also you! And every Lorekeeper who existed before me! Some green-haired wimp doesn't get to stand in the way of {i}that{/i}!"

    pause 1.0

    zinnia sad2brow poutmouth @talking2mouth "His notes are probably just all wrong, anyway. He has no idea what he's talking about. And Aster wouldn't {i}have{/i} {i}really{/i} told him anything important."

    pause 1.0

    zinnia @yanderebrow yanderemouth "It doesn't matter. It doesn't matter! It doesn't matter!!! He's not a Draconid, he doesn't get to climb the tower! He doesn't get anything! That's my job!"

    zinnia @talking2mouth "Lord Dragon hasn't been seen in four years, and... Aster... when the Super-Ancient Pokémon attacked..."

    pause 1.0

    zinnia @angrybrow angrymouth "If Aster couldn't make the climb, there's NO WAY this stupid little green-haired kid can make it! No-o-o-o-o way!"

    pause 1.0

    $ PlaySound("pokemon/cries/{}.mp3".format(sidemonnum))

    sidemon "Whismur..."

    zinnia -sad2brow -poutmouth @surprised "Oh! Of course, what am I thinking? It's time for your dessert!"
    zinnia @closedbrow talking2mouth "Such a spoiled girl you are, Aster... So what would like, hmm, sweetie?"

    pause 1.0

    zinnia @closedbrow talking2mouth "That stupid little kid... He's {i}not{/i} a Draconid. I'm saving him, really. After all, he couldn't make his way to the top of the tower, even if he did everything else right. So I'm saving him, just like I'll save everyone else."
    zinnia @angrybrow talking2mouth "Yeah. I'm the hero. {i}I'm{/i} the hero! Not him. Not anyone else."

    $ autoquote = False

    zinnia yanderebrow yanderemouth "\"Me!"

    show zinnia with vpunch:
        ypos 1.05 zoom 1.1

    $ BecomeNamed("Zinnia")

    extend " Zinnia!"

    show zinnia with vpunch:
        ypos 1.1 zoom 1.2

    extend " Lorekeeper of the Draconids!"

    show zinnia with vpunch:
        ypos 1.15 zoom 1.3

    extend " {size=50}{b}Me!{/b}\"{/size}"

    show zinnia with vpunch:
        ypos 1.3 zoom 1.5

    scene blank2 with Dissolve(2.0)

    $ autoquote = True

    return