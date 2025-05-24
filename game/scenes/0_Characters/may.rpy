label May1:
    if (not IsBefore(1, 5, 2004)):
        $ persondex["May"]["Events"].append("Level2SceneVer2")

    scene research
    show may at leftside:
        zoom 0.8
    with Dissolve(2.0)
    stop music fadeout 1.5
    $ renpy.music.queue("Audio/Music/RSE_Rival_start.ogg", channel='music', loop=False, tight=None)
    $ renpy.music.queue("Audio/Music/RSE_Rival_loop.ogg", channel='music', loop=True, tight=None)

    red @happy "Oh, hey, May! Didn't expect to see you here. What are you up to?"

    may @happy "[first_name]! Hiya. I'm just doing some research."

    show may:
        ease 0.5 xpos 0.5 zoom 1.0

    if (not IsBefore(1, 5, 2004)):
        red @talkingmouth "Cool. Is it alright if I join you?"

        may @happy "Of course! It's not like I'm worried about you using your mind control powers on me or anything."

        red @sadbrow talkingmouth sweat "The ones I don't have."

        may @angrybrow happymouth "Yeah, those ones."

        red @closedbrow talkingmouth sweat "Alright, just making sure we're on the same page." 
        red @talkingmouth "So, you said you're doing research?"

    red @talkingmouth "What about? School stuff?"

    may @talkingmouth "Yeah, I'm trying to figure something out for Bug class." 
    may @surprisedbrow sadmouth "Burgh mentioned that the way Bug-types create their webs is more an art than a science..."
    may @happy "But my dad always says that art is just science people haven't put a formula to, yet!"

    red @closedbrow talking2mouth "Your Dad... oh, Professor Birch, right?"

    may @talkingmouth "The one and only."

    red @talkingmouth "I guess you were raised in a pretty science-y household, then?"

    may @talkingmouth "Yup. Science and research have been in the Birch family line for generations."
    may @happy "My Dad moved to Hoenn to study the biodiversity there a few years before I was born."

    red @closedbrow talking2mouth "So, is that what you want to do when you graduate?"

    may @talkingmouth "Nah. I could never do better than my Dad, anyway. I want to be a contest coordinator, with Brendan."

    red @surprised "Oh, right! I think you might've mentioned that..."
    red @closedbrow talking2mouth "How did you and Brendan end up becoming interested in coordinating, anyway?"

    may @talkingmouth "{i}Contest{/i} coordinating. Musical coordinating is a different thing."

    red @talkingmouth "Oh, right. My bad."

    may @happy "It's no problem! Anyway, contests are {i}really{/i} popular in Hoenn. Actually, that's where they were invented."
    may @talkingmouth "I guess we both just kinda grew up watching coordinators on TV, instead of trainers. So that's who we wanted to become."

    red @talkingmouth "Kinda funny that you're going to enter an arts field instead of a science field, huh?"

    may @sadbrow happymouth "I guess it is. My Dad was surprised, actually. He always thought that I'd take over the Birch Lab when he retired."
    may @closedbrow talking2mouth "Actually, I think he's a bit angry at Brendan, because he thinks Brendan made me want to be a coordinator."

    red @confused "Really? But Brendan's always talked so highly about your Dad."

    may @happy "Yeah... my Dad's a really big softie. When he's angry at someone, the worst he'll do is not offer them extra cornbread at dinner."

    red @happy "The horror!"

    may @talkingmouth "Besides, Brendan's so nice, I don't think he'd even notice if someone were {i}furious{/i} with him."

    red @sadbrow talkingmouth "I don't know what Brendan could even do to make someone furious with him."

    if (IsBefore(1, 5, 2004)):
        may @happy "Yeah. I mean, the only arguments we ever have, really, are about something I cook."

        red @closedbrow talking2mouth "Right... I kinda clued into that, actually. What's the deal there?"

    else:
        may @sadbrow frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."

        may @sad "...Well..."

    may frownmouth @talkingmouth "Oh, it's... well... hm."
    may @closedbrow talking2mouth "Hmm..."

    red @talkingmouth "Trying to decide something?"

    may @talkingmouth "Yeah. I'm wondering if I should tell you... but I guess I can? We know each other well enough, and you're friends with Brendan."

    red @talkingmouth "Well, there we go, th--"

    may -frownmouth @happy "But I think I'm going to leave it up to this coin!"

    pause 1.0

    red @confused "...Wait, for real?"

    may @talkingmouth "Yeah!"

    red @talkingmouth "Um... isn't flipping a coin to decide this kinda irresponsible? I mean, if you don't trust me, that's fine, but I wouldn't leave it up to chance."

    may @happy "It's totally irresponsible. But that's a good thing. I'm not responsible at all--the coin is!"

    red @confused "That's... an interesting interpretation of how responsibility works."

    $ PlaySound("coinflip.ogg")

    pause 1.0

    may @surprised "Okay. So that's a heads." 
    may @happy "So, sure, I guess I'll tell you!"

    red @confused "Sure."

    may @talkingmouth "So... I like to cook. I do pretty much all of the cooking for my dorm, and whenever Brendan and I have picnics or whatever, I cook for those, too."

    red @talkingmouth "With you so far."

    may @happy "I learned back home in Hoenn. Taught myself, actually. My dad's great with a grill, but... he can also, kinda, {i}only{/i} grill."
    may @talkingmouth "So I learned to cook and bake, just so we had a bit more variety in our food. And I got really, really, good at it, too."
    may @sad "But... um. Pretty much the only things I know how to make are... meat and sweets..."

    if (IsBefore(1, 5, 2004)):
        may @happy "And Brendan's a vegetarian who doesn't like sweet things."

        red @surprised "Eesh. That's unfortunate."

        may @angry "Yeah, and the weird part is that he wasn't always like that. We've been dating for years, known each other for ten, and for the first nine, he couldn't get enough of my cooking!"
        may @sadbrow talkingmouth "I know that nobody can help it if his tastes changed... but I don't know what to do, now. I can't cook nearly as often as I used to, since there's not a lot I know how to make that he can actually eat at this point."

    else:
        may frownmouth @sad "And Brendan was... well, sick of it."

        red @surprised "Huh?"

        may @sadbrow happymouth "He said he loved my cooking at first, and... I can tell he's telling the truth. I saw how his eyes sparkled for the first few years."

        redmind @confusedeyebrows frownmouth "First few {i}years?{/i}"

        may @sad "But... I drove him to the point where he felt he had to {i}lie.{/i} Lie that he was a vegetarian, lie that he didn't like sweet things!"
        may @sad "And... I mean, I was a {i}little{/i} bit mad at him for that, but I was mostly even more upset with myself..."

        may @closedbrow sadmouth "I only found out when Sabrina... you know."

        may @sadbrow happymouth "So I confronted him, and he confessed. Like, right away, he didn't try to hide it. And he said he felt really bad he lied in the first place."

        red @closedbrow talking2mouth "So... you're not sure you can trust him, now?"

        may @surprised "What?"
        may @angry "No! I can {i}absolutely{/i} trust him!"

        pause 1.0

        may @angry "Lying was wrong, but... If I hadn't..."

        pause 1.0

        may @sadmouth "I... I just don't know what to do, now. I don't want to force him into another situation where he feels like he needs to lie."

    red @closedbrow talking2mouth "Hmm... "
    red @talking2mouth "You {i}do{/i} like cooking for him, right? Like, you're not just doing it out of a sense of obligation?"

    may -frownmouth -sadbrow @happy "Of course! It's really fun. And besides, it's how I tell him I love him."

    red @happy "Cute."

    pause 1.0

    red @sadbrow talkingmouth "Forgive me for asking a dumb question, but have you considered learning some new recipes?"

    show may sad with dis

    pause 1.0

    red @sad "Oh, sorry. Did I say something I shouldn't have?"

    may -sad frownmouth @closedbrow sadmouth "No... It's just... I've known five recipes for ten years."
    may @happybrow sadmouth "And I'm good at them!"
    may @closedbrow talking2mouth "What if it turns out I'm not good at any others?"

    red @closedbrow talking2mouth "Well... then you could practice, I guess."

    may @angry "Practice on Brendan? I'm not going to give my sweetheart crappy food just so I can get better."

    if (not IsBefore(1, 5, 2004)):
        red @confusedeyebrows talking2mouth "May, trust me. As a dude, he'll probably really appreciate seeing you taking steps to improve."

        may @closedbrow talking2mouth "No. I have standards for my boyfriend."

        red @sweat closedbrow talkingmouth "Worth a shot. Well, then, alternative idea."

    red @happy "You can practice on me! I'll eat pretty much anything."

    may @closedbrow talking2mouth "Mm... maybe. Maybe I should flip a coin for this..."

    pause 2.0

    $ PlaySound("idea.ogg")

    show may surprisedbrow frownmouth with dis

    red @happy "Oh, I get it!"

    may @talkingmouth "Huh?"

    red @talkingmouth "This isn't about cooking at all."
    red @angrybrow happymouth "You're afraid of change, aren't you?"

    may -surprisedbrow -frownmouth -surprised angry "Hey! That's a bit rude!"

    red @happy "It's the only thing that makes sense. You don't want to make big decisions, so you let other people, or that coin, make them for you."
    red @talkingmouth "And you don't want to learn new recipes, because, right now, you're good at everything you make." 
    red @talkingmouth "Even if Brendan's overexposed to it, you know that the food is, objectively, good. So why change it, right?"

    show may angrybrow frownmouth with dis

    pause 1.0

    redmind @surprised "Uh-oh. Did I blow it?"

    may -angry -angrybrow frownmouth @closedbrow talking2mouth "I guess you aren't entirely wrong..."

    if (IsBefore(1, 5, 2004)):
        may @sad "But you can't tell Brendan this! He just thinks I'm really forgetful."

        red @closedbrow talking2mouth "...I don't think couples should have secrets from each other. I won't tell Brendan, but you should."

        may @sad "Yeah, you're right, {w=0.5}of course." 

    else:
        may @sad "And... on top of all this... now Brendan is walking on eggshells around me, because he thinks I'm mad. And I am. But only a little bit? I don't know..."

        pause 1.0

        may @sadmouth "I guess you're right."

    may @sad "I {i}am{/i} afraid of change."
    may @closedbrow talking2mouth "I never thought that was a bad thing, though. Everything's going fine now, so why try to fix what isn't broken?"

    red @talkingmouth "Change isn't always about fixing a broken thing. Change sometimes just lets you get better."
    red @happy "I mean, you're in the Bug-type elective. You know this, right? A bug's gotta mash all its insides up into gross goop before it can become a butterfly."

    may @angrybrow frownmouth "Are you saying I need to enter my gross goop phase?"

    red @talkingmouth "Well... yeah. A Caterpie might think its life is perfect, but I'm pretty sure there's no Butterfree that would want to go back to being a Caterpie."
    red @talkingmouth "Also, your Dad's a scientist, and you've been around science-y stuff your whole life. You know how important evolution is, right? Not just for Pokémon. People have to evolve, too."
    red @happy "But if you want to evolve, that means you need to {i}actively{/i} make the choice to. And you need to decide what you're evolving into. You can't just flip a coin on that."

    may @talkingmouth "Actually, Wurmple randomly evolve into either Silcoon or Cascoon."

    red @happy "Correct me if I'm wrong, but I don't think you're a Wurmple?"

    may @happy "I used to pretend to be one! My Dad bought me a sleeping bag that looked like a Cascoon. I loved that thing."
    may @sad "...But then I got too big for it."

    red @happy "Evolution does have its downsides--like not fitting in your cozy Cascoon sleeping bag any more. But the upsides are too big to turn down."

    if (pikachuobj.GetId() == 25):
        may -frownmouth @angrybrow happymouth "Pretty big of Mr. I'm-Never-Evolving-My-Pikachu to be lecturing {i}me{/i} on evolution."

        red @talkingmouth "Hey, I would if I could. And he wanted to evolve, of course."

    else:
        may -frownmouth @angrybrow happymouth "Pretty big of the former Mr. I'm-Never-Evolving-My-Pikachu to be lecturing {i}me{/i} on evolution."

        red @talkingmouth "Well, I've changed, too. And so has [pika_name]. 'Cause change is good."

    may @talkingmouth "It's kinda weird that I'm telling you this stuff before everyone else... but I really want Brendan to see me as better than I am." 
    may @happy "You know?"
    may @sad "I mean, the scientists' daughter and entomologist who doesn't want to go through her own metamorphosis? It sounds like a bad joke."

    red @happy "I don't think there's anything to worry about there. Brendan is the most non-judgmental guy I know. And it's obvious that he loves you just as much as you love him."
    red @talkingmouth "The fact you're so worried about making this work is proof that even if you're afraid of changing what you have, and messing up, you'd find a way to fix it."

    if (not IsBefore(1, 5, 2004)):
        red @sweat talkingmouth "Besides. You mentioned he's walking on eggshells around you, right? He probably wants to fix this just as much as you do."

    may @happy "Aw. Thanks, [first_name]. You're a good friend."

    red @talkingmouth "I try my best. But, again, the best way to fix any issues you think you might be having is to just tell Brendan everything you've told me."

    pause 2.0

    may @talkingmouth "[first_name], have you ever had a girlfriend?"

    red @happy "Hah! No, I have not." #FIX THIS: Change when Red has possibility to get girlfriend/boyfriend

    may @closedbrow talking2mouth "What about a boyfriend?"

    red @talkingmouth "Nope. Though I {i}would{/i} be open to it."

    may @angrybrow happymouth "Maybe I should be worried about how much time you're spending around Brendan, then!"

    red @happy "Nah, I'm not a homewrecker. Don't worry about me."

    may @talkingmouth "Phew. That's a relief."

    red @talkingmouth "Anyway, why do you ask? About whether I've ever had a, uh, partner, I mean?"

    may @angrybrow happymouth "It's just that you're giving a lot of advice for someone who's never actually {i}been{/i} in this situation. Where'd this come from, huh?"

    pause 1.0

    show may surprisedbrow frownmouth with dis

    red @confused "Will you be offended if I say 'common sense'?"

    may angry "A little bit, yeah!"

    red @happy "Sorry! But that's where this is coming from. I mean, communication works. And it's the {i}only{/i} thing that works. If you can't Pokémon battle it into submission, then you just gotta talk to it, and if that doesn't work, nothing will."

    show may thinking with dis

    pause 1.0

    red @angrybrow talking2mouth "No, you can't Pokémon battle away your fear of change."

    may sad "Dang it."

    show may thinking with dis

    pause 1.0

    red @closedbrow talking2mouth "You also can't Pokémon {i}contest{/i} away your fear of change."

    may sad "Double-dang it."

    if (IsBefore(1, 5, 2004)):
        red @talkingmouth "If the idea of just explaining why you make the same meals for Brendan over and over is {i}really{/i} that terrifying, though, then you can just practice your new recipes on me."
        red @closedbrow talking2mouth "Maybe a bit less spicy than you would normally do, though."

        may -sad @talkingmouth "Mm..."
        may @happy "Alright! Thank you. But {i}please{/i} don't tell Brendan about this."

        red @talkingmouth "I won't. As long as you promise you, eventually, will."

        pause 1.0

    else:
        red @talkingmouth "The way I see it, you've already handled that hardest part of this. Or... Sabrina did, anyway."

        red @sadbrow talkingmouth "Now the secret's out, and everyone can be truthful with each other. This could be a good thing, if you choose to see it that way."

    may @talkingmouth "Okay. I will."

    red @happy "Cool. Also, can I say... I'm kinda jealous?"

    may @surprised "Huh?"

    red @talkingmouth "It's really obvious how much you and Brendan care for each other. I want that someday."

    may @happy "Aw. That's sweet of you. And I'm sure you'll find someone who loves you as much as I love Brendan."

    red @happy "What do you love about the guy? I mean, I know why I like him, but what's your reason?"

    may @sadbrow happymouth "I'm not even sure I could say them all."
    may @closedbrow talking2mouth "He's so kind. If he thinks anybody is feeling lonely, or needs help with something, he's always there. Even if he's not actually good at the thing he's helping with."
    may @happy "And he's so funny. He's got such an innocent mind, and we can look at the same thing and see two completely different things. He always sees the world in a different way than I do, and I love finding out how he feels about things."
    may @talkingmouth "It's been years since we started dating, but I still learn new things about his mind every day. And I love that."

    red @confused "...Okay, but when are you going to mention that he's hot and fit as hell?"

    may @angrybrow happymouth "I was {i}getting{/i} to that! Let me fawn over my boyfriend at my own pace, please!"

    red @happy "{i}Mea culpa.{/i}"

    may @happy "Well, I don't usually mention that, because I don't want to seem shallow, but I really do love how much effort he puts into his appearance."
    may @talkingmouth "Part of it is just that Pokémon coordinators need to look good if they want to win, but he goes above and beyond."
    may @talkingmouth "He wakes up at six in the morning every day, just so he can work out, take a shower, brush his teeth, and do his hair."

    red @talkingmouth "I {i}have{/i} noticed. Brendan's pretty fastidious for such a big guy."

    may @happy "Yeah. I love that about him. He's so disciplined, and when he's got his mind on something, he'll never let go, and he works {i}so{/i} hard on anything he tries to..."

    may @thinking "[ellipses]"

    $ ValueChange("Brendan", 3, -0.5)

    narrator "Extolling Brendan's virtues with May makes you feel as though you both have a better understanding of Brendanity. You gained three points with Brendan!"

    pause 1.0

    red @confusedbrow talkingmouth "May? You with us?"

    may @sadbrow happymouth "I'm sorry, I need to go cuddle my boyfriend. I just remembered how much I love him."

    if (IsBefore(1, 5, 2004)):
        red @happy "Aw. Love him enough to tell him why you don't want to make any new meals?"

        may @sadbrow happymouth "...Maybe after I practice."

        red @talkingmouth "I'll take it. And I'm here to help. You got any noxious, steaming piles of Mystery Food X? I'll try them before they get anywhere near Brendan's delicate palate."

    else:
        red @happy "Sounds good. And remember--if you've got any noxious, steaming piles of Mystery Food X? I'll try them before they get anywhere near Brendan's delicate palate."

    may @happy "Thanks! I bet you'll be a great {color=#0048ff}taster{/color}!"

    $ RelationshipRankUp("May", "Taster", 1)

    return

label May2:
    scene colosseum 
    with Dissolve(2.0)

    stop music fadeout 1.5

    $ PlaySound("coin.ogg")

    narrator "You're walking by the Battle Hall when you hear a pretty distinct sound echoing through the empty hall. Your ears prick up--as do [pika_name]'s."

    $ PlaySound("pokemon/pikachu_question.ogg")

    libpikachu @confusedeyes surprised2mouth "Pi-ka?"

    red @talking2mouth "Not sure, buddy. Sounds like someone dropped their wallet, maybe?"

    scene stadium_empty with splitfade

    $ renpy.music.queue("Audio/Music/RSE_Rival_start.ogg", channel='music', loop=False, tight=None)
    $ renpy.music.queue("Audio/Music/RSE_Rival_loop.ogg", channel='music', loop=True, tight=None)

    pause 1.0

    show may with dis

    red @talkingmouth "Oh, hey, May. Whatcha doing here?"

    may @talkingmouth "Not much. There were a couple of battles going on in here, and I thought I might watch them."

    red @talkingmouth "Oh, yeah? Anyone I know?"

    show bea with dis:
        xpos 0.33

    show may with dis:
        xpos 0.5
        ease 0.5 xpos 0.66

    bea @talking2mouth "I suppose that depends on whether you know me."

    red @happy "Yeah, I'd say I do. Hey there, Bea. What're you doing here?"

    bea @closedbrow talkingmouth "Training."

    if (GetRelationshipRank("Bea") > 1):
        bea @talking2mouth "With Bianca's father's death, it's become ever more apparent that our ultimate confrontation may very well occur in a public place."
        bea @closedbrow talking2mouth "I do not have the luxury of isolating myself and training alone anymore. I must acclimatize myself to the idea of battle with others around."
        bea @talking2mouth "To that end, I've been inviting non-Battle Team students to challenge me all evening."

        red @sadbrow talkingmouth "Oh... wow. Um, should May be hearing this?"

        bea @talking2mouth "I am speaking in frustratingly vague terms."

        may @angrybrow talking2mouth "It's true! And I'm incredibly curious, but Bea won't spill the beans!"

        redmind "Huh. I didn't realize Bea liked teasing people... She always has such a straight face, it's hard to tell when she's joking or teasing... but I can definitely tell she is now."

        may @sadbrow talkingmouth "The best guess I have is that she's going to try and make a championship run...?"

        bea @closedbrow talkingmouth "So close. Yet still so far."

        may angrybrow poutmouth "Grrr!"

        red @sadbrow talkingmouth "Sorry, May. I guess you two battled, then?"

    else:
        red @sweat closedbrow talkingmouth "{size=30}Ask a dumb question...{/size}"

        red @talkingmouth "I guess you and May battled, then?"

    bea @talkingmouth "We did. In my arrogance, I expected a Battle Team member's victory over a Coordinator Club member's to be absolute and crushing."

    may -angrybrow -poutmouth @sadbrow talkingmouth "Bea's... straight-to-the-point."

    bea @talking2mouth "I was surprised. May is an extremely competent battler. Her Heracross alone managed to present a formidable threat to my team, making usage of unexpected coverage moves."

    may @happy "Aw, thanks!"
    may @talkingmouth "When it comes to Bug-types, you often {i}have{/i} to look at their coverage moves, if you want to hit something hard. I guess it's a bit of an acquired skill."

    bea @talkingmouth "Perhaps."

    if (getRWDay(0) == "Friday"):
        bea @closedbrow talking2mouth "Now, please excuse me, you two. I need to change before the Battle Team meeting later."
    elif (timeOfDay == "Evening"):
        bea @closedbrow talking2mouth "Now, please excuse me, you two. I wish to meditate under my shower faucet for a while before heading to bed."
    else:
        bea @closedbrow talking2mouth "Now, please excuse me, you two. The day is young. I would like to get more training in--perhaps I will venture into the city."

    hide bea with dis

    pause 1.0

    show may:
        xpos 0.66
        ease 0.5 xpos 0.5

    may @sadbrow talkingmouth "...I'm kinda jealous of her."

    red @talkingmouth "Yeah?"

    may @closedbrow talking2mouth "She knows exactly what she wants to do, and just does it. I wish I could think like she does. She's really great in our Fighting-type elective, too. I think she's Sensei Marshal's favorite."

    if (GetRelationshipRank("Bea") > 0):
        redmind @sweat thinking "I can't tell May that Bea gets choice paralysis when she picks a cereal box in the morning..."

        $ ValueChange("Bea", 3, -0.5)

        narrator "Your understanding of Bea increased by three points!"

        redmind @thinking "Although... actually, maybe that's something they have in common. May might actually be {i}better{/i} at that than Bea is."

        red @talkingmouth "Look, she may {i}look{/i} like she's got it all figured out, but... we're all figuring it out as we go. Even her. {i}Especially her.{/i}"

    else:
        red @sadbrow talkingmouth "We all have our strengths and weaknesses. Maybe it's not as easy for her as it seems."

    pause 1.5

    red @happy "So, hey. Is there something I can help you figure out?"

    may @talkingmouth "What do you mean?"

    red @talkingmouth "While [pika_name] and I were outside, we heard a coin dropping."
    red @happy "Not to get presumptuous, but that's usually the sound of you making a decision."

    may @sadbrow talkingmouth "Oh. Yeah, actually, that might be helpful."
    may @happybrow talkingmouth "Um... the problem is I dropped my coin in the bleachers."

    red @confused "Oh, right? Not a problem, I can find it for you."
    red @talkingmouth "During Battle Team practice, we usually sit on the bleachers to watch demonstrations Janine or Lance put on. People are dropping stuff in the cracks between them all the time."
    red @happy "Come to think of it, no wonder I heard that coin so loudly. It probably fell right onto the metal base."

    may @talkingmouth "Thanks!"

    pause 0.5

    may @surprised "Oh! But don't move it before you see which side it landed on!"

    red @happy "You could flip it again, since you didn't even see how it landed the first time."

    may @closedbrow talking2mouth "That would be {i}cheating{/i}."
    may @angrybrow talkingmouth "What if I {i}subconsciously{/i} saw how it landed last time? I might be accidentally ignoring the result I secretly don't want!"
    may @talking2mouth "Re-flips aren't allowed. Never."

    red @confusedbrow talkingmouth "If there's a result you don't want, does flipping the coin matter?"

    may @talkingmouth sadbrow "...It might help me figure out what the result I don't want {i}is{/i}."

    red @sadbrow talkingmouth "Fair enough."

    may @talkingmouth "Besides, that's not just {i}any{/i} coin. It's an anniversary gift."

    red @upeyes talkingmouth "Of course it is. God, you guys are disgustingly cute."

    may @sadbrow talking2mouth "Well, as long as 'cute' is part of that..."

    red @talkingmouth "Alright, be right back with your coin."

    show blank2 with splitfade

    pause 1.0

    narrator "You eventually manage to squeeze [pika_name] through the metal scaffold on the underside of the bleachers, and, making your way through fields of dust, discarded bags of chips, and a couple loose Poké Balls, you find May's coin." 

    redmind @happy "Hey, free Poké Balls!"

    $ GetItem("Poké Ball", 2)

    narrator "There's[ellipses] only one problem."

    red @confused "Uh... May? You're not going to believe this."

    show may surprisedbrow frownmouth
    hide blank2 
    with splitfade

    pause 1.0

    red @talking2mouth "It was on its side. Looked like it had bounced off the ground and ended up leaning against one of the bars down there."

    may @talking2mouth "...Was it leaning in one direction over another?"

    red @sweat talking2mouth "No luck. It was completely vertical."

    pause 1.0

    may @talking2mouth sadbrow "Well... that's, scientifically speaking, very unlikely."

    red @closedbrow talking2mouth "Yeah, no, I'm baffled, too. I promise I didn't figure out how to lie just to tell you this coin landed on its side, though."

    may -surprisedbrow -frownmouth @closedbrow talking2mouth "I believe you. But... dang it."

    red @talkingmouth sadbrow "You could re-flip."

    may @angrybrow talking2mouth "Nononono. Re-flips aren't allowed, remember?"

    red @sweat talking2mouth "Well... damn. I dunno, maybe you could tell me what the problem is?"

    may @sadbrow talkingmouth "I guess..."

    show may:
        ypos 1.0
        ease 0.5 ypos 1.2

    narrator "You sit down on a bleacher, and lean back, waiting for May to be comfortable enough to tell you what's biting her."

    may @frownmouth closedbrow "[ellipses]"
    may @closedbrow talking2mouth "Okay."

    show may:
        ypos 1.2 zoom 1.0
        ease 0.5 zoom 1.3 ypos 1.2

    may @talkingmouth "I've been thinking about Coordinating a lot, recently."

    red @sweat talking2mouth "Yeah, from what I've heard, Lisia hasn't really given you a chance to {i}not{/i} think about it."

    may @sadbrow talkingmouth "...And I'm starting to realize that I'm just {i}not that into it.{/i}"

    red @surprised "Huh?"

    may @sadbrow talkingmouth "I know! I was surprised, too."

    red @talking2mouth "But you're on the Coordinator track, aren't you?"

    may sadbrow blush @talkingmouth "Yes... I joined because..."

    pause 1.0

    red @talkingmouth "Because Brendan did?"

    may @talking2mouth "Yeah... I know that wasn't the most responsible choice, but I wanted to spend more time with him, and I knew I'd find it fun."
    may -blush @closedbrow talking2mouth "And I know I can succeed as a Coordinator. I'm even more sure of it, now that Lisia's teaching me. I'm keeping up, even with Brendan and Dawn."

    pause 1.0

    may @sadbrow talkingmouth "I even find it fun."

    pause 0.5

    red @sad2brow talkingmouth "But... you're not passionate about it?"

    may @talking2mouth "...I guess not. It's fun. I get to spend time with Brendan, and Lisia, who is probably Hoenn's most famous person."
    may @happy "But when I see Brendan get that fire in his eyes, and he talks about how he's going to make the world {i}respect{/i} contests..."

    pause 0.5

    may @talkingmouth "I've never felt that way about contests. Or... anything, really."

    pause 0.5

    may @sadbrow talkingmouth "I think I'm just... too happy following the tracks. Doing what I've always done. And if there aren't any tracks, I flip a coin and make some for myself."
    may @happy "Brendan has dreams, but I think I only really have fantasies. Like, he {i}wants{/i} to get better--he wants to achieve things, you know?"
    may @sadbrow talkingmouth "I can't really think of anything like that for myself. Something I'm {i}really{/i} passionate about..."

    pause 0.5

    may @happy "Well, I guess I've felt that way about cooking, but we {i}all{/i} know how it turned out when I got too intense about my cooking."

    red @talkingmouth "It's alright to be passionate about it, May. C'mon. You and Brendan aren't going to let something like that hang over you forever, right?"

    may -sadbrow @happy "Of course not. We've been dating for seven years. That wasn't even the biggest thing that ever happened between us."

    pause 1.0

    may @talkingmouth flirtbrow "You're curious, aren't you?"

    red @sweat talkingmouth "Curious, but possessed of the minimal amount of self-control required to not ask."

    may @happy "Hah! Well, let me just say that when we first met, I had... a {i}very{/i} different sense of style."
    may @closedbrow talkingmouth "We argued for ages over what was '{i}proper{/i}' or '{i}decent{/i}' for a lady to wear in public."

    redmind @lightblush surprisedbrow frownmouth "[ellipses]"

    may @closedbrow talking2mouth "{size=30}Come to think of it, running around in leaves and moss every day was probably an early sign that I...{/size}"
    may @happy "Actually, nevermind, I'm not going to finish that sentence!"

    redmind @lightblush surprisedbrow frownmouth "Steady on, old boy. Move your thoughts elsewhere."

    red @talking2mouth "W-well, that aside, I think I've got an idea." 
    red @talkingmouth "With how you've been cooking for me, it's pretty clear that you're passionate about your cooking, and you want to be a better chef."
    red @happy "Not just for Brendan. Just because it's something you're proud of. Right?"

    may @talking2mouth "I... guess."

    red @talkingmouth "Well, as fun as it's been being your [bluecolor]taster{/color}, we're quickly running into the problem that I'm only one guy, with one palate."
    red @happy "And it's not a particularly refined one, either."

    may @closedbrow talking2mouth "Hmmm... So you're thinking that I should get some other people involved?"

    red @talkingmouth "Even better. I might just know someone who's already involved. In a general sense."

    may @surprisedbrow talking2mouth "...Yeah?"

    red @happy "Sure. Follow me."

    scene blank2 with splitfade

    pause 1.5

    stop music fadeout 1.5
    queue music "audio/music/alolaencounter_intro.ogg" noloop
    queue music "audio/music/alolaencounter_loop.ogg"


    scene cookingkitchen 
    show screen currentdate
    show mallow
    with splitfade

    mallow surprisedbrow frownmouth @happy "Alola! [first_name], it's so good to see y--"

    pause 1.0

    show may sadbrow with dis:
        xpos 0.66

    show mallow with dis:
        xpos 0.5
        ease 0.5 xpos 0.33

    pause 1.5

    mallow @talking2mouth "You... came back."

    may @happybrow talkingmouth "Um, I'm actually just dropping in--my friend [first_name] brought me here--"

    show mallow with dis:
        xpos 0.33
        ease 0.2 xpos 0.6

    show may surprisedbrow frownmouth with dis:
        xpos 0.66
        ease 0.5 xpos 0.75

    mallow -surprisedbrow -frownmouth @happy "This is fantastic! I'm so glad you changed your mind!"

    red @talkingmouth "I guess you already know each other, then?"

    show mallow with dis:
        xpos 0.6
        ease 1.0 xpos 0.33

    show may sadbrow -frownmouth with dis:
        xpos 0.75
        ease 0.2 xpos 0.66

    mallow @talkingmouth "Yup. When the Head Chef founded the club, he said we needed more members. I asked around for other people in Kobukan interested in cooking, and May's name kept coming up."
    mallow @happy "I knew you'd be a perfect fit for the club!"

    red @sadbrow talkingmouth "Well, hold on. May hasn't agreed to {i}join.{/i} I just wanted to bring her here to see what a club meeting looks like--to see if it's something she {i}might be{/i} interested in joining."

    mallow @talking2mouth "Oh."
    mallow @talkingmouth "Oh, well, that's okay! Sure, I can cook up a session of the Cooking Club right now."
    mallow @sadbrow talkingmouth "We were--um, I was--just kind of making a paella right now... but we could turn that into a group activity."

    pause 1.0

    mallow @closedbrow talking2mouth "Oh, no, it's in the oven right now... um, well, we could..."

    pause 1.0

    redmind @wince frownmouth "Hm... I was hoping May and Mallow would get along, given their shared interest in cooking, but Mallow might be too awkward to pull it off."

    may @talkingmouth "...How about a {i}sofrito{/i}?"

    mallow @talkingmouth "Oh! To put on top of the paella?"

    may -sadbrow @talkingmouth "Sure. The spiciness of the sauce works well with the savory paella. Right?"

    mallow @happy "Yeah, that's exactly what I was thinking!"

    may @talkingmouth "I've never made one before, though. But I think I get the theory. Do you have any Tamato berries?"

    mallow @talkingmouth "Do I? Of course! Oh, now, this is a bit controversial, but I think if we grind a few Poké Beans up and put them in the sauce, it'll thicken up the texture, which my {i}Tutu{/i} swears by."

    may @talkingmouth "Oh, you know, that's actually what I was thinking, too? I was thinking of using flour, but if you say Poké Beans work, then we should try that."
    may @happy "Don't you find it annoying when the sauce sinks into the paella too fast, making it soggy?"

    mallow @closedbrow talking2mouth "You just {i}can't{/i} keep it as leftovers like that."

    may @surprised "Exactly! So if we thicken up the sauce then we can--"

    mallow @talkingmouth "Yeah, and let's make some baguettes on the side, while we're--"

    may @talkingmouth "I'll preheat the other oven to--"

    mallow @happy "And then we--"

    red @sadbrow "[ellipses]"

    redmind @happy "My work here is done."

    hide mallow 
    hide may
    with dis

    narrator "You turn to leave the Cooking Club, when you suddenly feel two firm hands placed on your shoulders."

    redmind @thonk "Huh?"

    show may flirtbrow:
        xpos 0.66 ypos 1.2 zoom 1.3
    show mallow flirtbrow catmouth:
        xpos 0.33 ypos 1.2 zoom 1.3
    with Dissolve(2.0)

    may @talkingmouth "Hold on a minute, [bluecolor]kitchen boy{/color}. Where do you think you're going?"

    red @confused "Uh... somewhere else?"

    may @happy "Not so fast! You know how busy I am with the Coordinator Club, right?"

    red @sadbrow sweat talkingmouth "Excessively, yeah."

    may @closedbrow talking2mouth "If you're going to get me wrapped up in something I {i}really{/i} don't have time for, you need to take responsibility and help."

    red @closedbrow talking2mouth "I[ellipses] am not able to find an argument against this, unfortunately."

    mallow @talkingmouth "We won't keep you long. Sofrito barely takes any time."

    may @happy "And it'll go even faster if you're helping with the dishes."

    red @sadbrow talkingmouth "Dish duty? You know, I can cook, too. I'm not bad at it, even."

    if (IsAfter(22, 5, 2005)):
        may @talkingmouth "Oh, I know. I tasted Dawn's cake, remember?"

        show mallow surprisedbrow frownmouth with dis:
            xpos 0.33 ypos 1.2 zoom 1.3
            ease 0.5 ypos 1.0 zoom 1.0

        pause 1.0

        show may surprisedbrow frownmouth with dis:
            xpos 0.66 ypos 1.2 zoom 1.3
            ease 0.5 ypos 1.0 zoom 1.0

        red @surprisedbrow talking2mouth heavyblush "Uh... should you tell Brendan?"

        mallow @sadbrow talkingmouth "What kind of person did you bring into my Cooking Club, [first_name]?"

        may talking2mouth "Wait, wait, hold on! You've got it wrong! I'm not a pervert, I have a boyfriend! I'd never taste another woman's cake!"
        may sadbrow "{size=30}...Okay, actually, I might be a pervert, and I {i}did{/i} look at Serena's, but I {i}do{/i} have a boyfriend, and--{/size}"

    else:
        may @talkingmouth "Oh, I know. Leaf told me about your sticky buns."

        show mallow surprisedbrow frownmouth with dis:
            xpos 0.33 ypos 1.2 zoom 1.3
            ease 0.5 ypos 1.0 zoom 1.0

        pause 1.0

        show may surprisedbrow frownmouth with dis:
            xpos 0.66 ypos 1.2 zoom 1.3
            ease 0.5 ypos 1.0 zoom 1.0

        red @closedbrow sweat talking2mouth "I can't believe she did that."

        mallow @sadbrow talkingmouth "What kind of person did you bring into my Cooking Club, [first_name]?"

        may talking2mouth "Wait, wait, hold on! You've got it wrong! I'm not a pervert, I have a boyfriend!" 
        may sadbrow "I'm not interested in anyone's buns but Brendan's! Not that they're {i}bad{/i}, probably, but I {i}do{/i} have a boyfriend, and--"

    show blank2 with splitfade 

    narrator "You quickly throw on an apron and move to the sink as May flounders about, cooking up a pile of excuses that, without accounting for taste, seem pretty rotten."

    pause 2.0

    show may -sadbrow -talking2mouth 
    show mallow -surprisedbrow -frownmouth
    hide blank2
    with splitfade

    may @closedbrow talking2mouth "...Oh, really? So that's why my [GetTrainerTeam('May', 'Cutiefly').GetNickname()] seems so low-energy..."

    mallow @sadbrow talkingmouth "A lot of Bug and Grass-types from Alola need to be around Alolan flowers every once in a while. It's not just people who get homesick."

    may @closedbrow talking2mouth "Hm... I think it should probably be possible to grow those Alolan flowers in the greenhouse. My Dad's work on Pokémon environments might come in handy here..."

    mallow @happy "I still can't believe your Dad is {i}the{/i} Professor Birch. If I'd known that, I never would have let you go."

    may @talkingmouth "He's pretty humble about it. I know he seriously considered going to Alola at one point, though--the Aether Foundation is one of the best places to study Pokémon habitats."
    may @happy "I guess it's for the best he didn't, though--if he had, I might never have met Brendan! I might not have even gone to Kobukan."

    pause 1.0

    red @talkingmouth "Hey, I'm done with the dishes, and it looks like your {i}sofrito{/i} should be done in a couple minutes. Mind if I step out?"

    may @talkingmouth "Not a bit. Thanks for helping out!"
    may @sadbrow talkingmouth "Will you join us again?"

    redmind @happy "You're an 'us,' now? This worked better than I thought."

    red @talkingmouth "Sure. I'll drop by whenever I have the time."

    may @surprisedbrow talking2mouth "...Time?"

    pause 1.0

    may @closedbrow talking2mouth "Oh no... I forgot. I was supposed to be at a Coordinator Club meeting right now..."

    red @wince talking2mouth "Oh, geez. Uh, sorry about that. Maybe the head chef of the club could write you an excused absence note?"

    mallow @sadbrow talkingmouth "I'm not sure he has the authority to do that, but... I could ask?"

    may sadbrow @talkingmouth "I should probably just tell Lisia what happened. Time to face the music... and the dancing."

    red @talkingmouth "Good luck."

    hide may with dis

    pause 1.5

    red @talkingmouth "Well, she seems nice, right--"

    show mallow happy with dis:
        xpos 0.33
        ease 0.2 ypos 1.2 zoom 1.3 xpos 0.5

    show cookingkitchen with vpunch

    mallow "{gradualsize=36-60}Thank you thank you thank you thank you thank you thank you thank you!{/gradualsize}"

    red @surprised "Gah!"

    show blank2 with splitfadefaster

    narrator "Mallow wraps you up in a tight hug, and it is only through careful application of [pika_name], and a promise to come back and attend future club meetings, that you're able to free yourself from Mallow."

    pause 1.0

    narrator "Your thoughts linger on May... you hope that she doesn't get in too much trouble with Lisia, and that Brendan is as understanding as you've always known him to be."

    $ RelationshipRankUp("May", "Kitchen Boy", 2)

    narrator "[bluecolor]May is now a contributing member of the Cooking Club!{/color} As a result, the cooking Club's selection has increased, and its prices have decreased."

    return