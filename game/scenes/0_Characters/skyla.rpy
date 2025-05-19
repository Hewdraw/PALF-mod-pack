label Skyla1:
    if (not IsBefore(1, 5, 2004)):
        $ persondex["Skyla"]["Events"].append("Level2SceneVer2")

    scene city_B
    with Dissolve(2.0)
    stop music fadeout 1.5
    $ renpy.music.queue("Audio/Music/MistraltonCity.ogg", channel='music', loop=True, fadein=1.5, tight=None)

    show screen songsplash("Mistralton City Remastered", "Zame")

    show skyla surprisedbrow frownmouth with dis

    skyla @talkingmouth "Woah! [first_name], is that you?"

    red @talkingmouth "Huh? Oh, yeah. I was just doing some shopping. What's up?"

    skyla -surprisedbrow -frownmouth -surprised @angrybrow happymouth "Adventure's up! I'm hot on the tail of a couple of criminals!"

    red @closedbrow talking2mouth "...Criminals?"

    skyla @happy "Yeah!"

    red @talkingmouth "And these are definitely criminals, right? Because you thought a meteor was an alien invader."

    skyla @angry "Hey! I still maintain that that meteor is not entirely {i}not{/i} an alien invader."

    red @closedbrow talking2mouth "Right. Well, if you're trying to stop an actual criminal, shouldn't we leave that to the cops?"

    skyla @closedbrow talking2mouth "Cops are useless! If anyone's going to step up and be a hero, it'll be us!"

    red @confused "Okay. Just so I know what we're walking into here, these criminals are...?"

    skyla @angry "A pair of skinheads. They look real mean, too."

    red @closedbrow talking2mouth "And you know they're criminals because...?"

    skyla @closedbrow talking2mouth "Well... I mean..."
    skyla @angry "They're bald! And they were {i}skulking!{/i}"

    red @confused "Skulking."

    skyla @angrybrow happymouth "Yeah! They were...{w=0.5} kinda...{w=0.5} walking side-by-side...{w=0.5} and, uh...{w=0.5} looking shifty..."

    red @closedbrow talking2mouth "Skyla, I think you might be hot on the tail of a couple of {i}bears{/i}."

    skyla @surprised "No way! I know a human being when I see one."

    red @sadbrow talkingmouth "Alright. Well, why don't you lead me to these 'criminals,' and we'll see what mischievous deeds they're up to?"

    skyla @happy "Gladly! They just went down this alleyway."

    show skyla:
        ease 0.5 xpos 1.5

    red @surprised "Wait... {i}that{/i} alleyway?! Skyla, stop!"

    scene abandonedhouse with slideleft

    pause 1.0

    show skyla surprisedbrow frownmouth at night with dis

    skyla @talkingmouth "Look! [first_name], this is it! I was right! This must be their evil hideout!"

    show roughneck at leftside, night
    show roughneck2 at rightside, night
    with dis

    pause 2.0

    roughneck @happy "Hey, [first_name]."

    skyla @surprised "You know these rogues, [first_name]?"

    red night @sadbrow talkingmouth "Not personally?"

    skyla angry "Well, halt, evildoers! Your machiavellian schemes end today!"

    red @closedbrow talking2mouth "Oooh, boy. Okay, Skyla, these guys might not be the {i}most{/i} morally white, but the worst they'll do is steal someone's hat."

    roughneck2 @happy "Yeah, I {i}did{/i} do that once."

    roughneck @happy "Heh, me too."

    skyla surprisedbrow frownmouth @surprised "See? They admit to their... their heinous crimes!"

    red @talking2mouth "Skyla. You're massively outnumbered, there's a couple dozen guys as backup just twenty feet away in the shack, and their boss is a skilled trainer."

    show skyla -surprisedbrow -frownmouth -surprised frownmouth with dis

    red @happy "But let's ignore all that, and just play this out."
    red @closedbrow talking2mouth "Let's say you {i}did{/i} manage to beat these two in a Pokémon battle."
    red @happy "Which, let's be honest, isn't hard."

    roughneck @angry "Oi."

    roughneck2 @surprised "Yeah, we're tough as nails!"

    red @talkingmouth "So, you've beaten them now. We can assume that your Pokémon will let you make them go wherever you want to bring them. What will you do with them?"

    skyla @closedbrow talking2mouth "Um... tie them up a smidgen on the tight side, then leave them for the cops?"

    red @closedbrow talking2mouth "Didn't you say the police were useless earlier? Well, whatever."

    show skyla sad with dis

    red @confused "How are you going to tie them up? A smidgen tightly or not? Do you have any rope? And how will you let the police know that they're here? Because, if you don't, they go free."
    red @talking2mouth "Further, are you going to leave an explanation of why you beat and tied up these trainers? Do you have evidence of their crimes? Without those, the cops start looking for {i}you,{/i} and they go free."
    red @closedbrow talking2mouth "That's not even mentioning that vigilantism is illegal. So beating and tying up a criminal, even if they totally {i}did{/i} do something wrong, is probably going to let them go free."
    red @sadbrow talkingmouth "Put simply; they go free."

    pause 2.0

    roughneck @happy "So... can we go free?"

    pause 1.0

    red @confused "Skyla?"

    skyla sadbrow frownmouth @sadmouth "Yeah... I guess."

    hide roughneck
    hide roughneck2
    with dis

    pause 1.0

    skyla -sadbrow frownmouth @angry "Dang it."

    pause 1.0

    red @happy "Alright. Let's get out of this alleyway, and maybe you can tell me what this was all about, alright?"

    skyla @sad "Yeah... alright."

    scene city_A
    show skyla 
    with Dissolve(2.0)

    narrator "You spend several minutes walking together in silence until you make your way to a different part of the city, and Skyla's mood seems to improve."

    red @talkingmouth "So. What was up with that, huh?"

    skyla @talkingmouth "I... want to be a hero. I always have."

    red @happy "Straight and to the point. I like that you know what you're about."
    red @closedbrow talking2mouth "So, like, a firefighter?"

    skyla @talkingmouth "No. Like... a real hero. A superhero."

    red @surprised "Uh... a superhero? That seems a bit... out of reach."

    skyla @surprised "Does it? Really?"

    red @confused "I mean... yeah. Doesn't it? Where would you get superpowers from?"

    if (not IsBefore(1, 5, 2004)):
        skyla @talkingmouth "{i}You've{/i} got superpowers yourself, you know."

        red @closedbrow talkingmouth "Geez. Frienergy isn't a superpower, you know."

        pause 1.0

        red @sad2eyes talking2mouth "Okay, maybe it is, a little bit, but it's not {i}really.{/i}"

        skyla @talkingmouth "Anyway, since I wasn't born with superpowers, I know exactly where I could get mine from."

    skyla @talkingmouth "My Pokémon."
    skyla @talkingmouth "Pokémon can fly, turn invisible, read minds, be super-strong, be super-fast... superheroes already exist all around us. They're just called Pokémon."
    

    if (not IsBefore(1, 5, 2004)):
        skyla @talkingmouth "Sabrina can read minds. Bea can punch through brick. You can make friends with anyone. There's gotta be a way, right?"
    else:
        skyla @talkingmouth "There has to be a way for a person to have those powers, too, right?"

    red @wince talking2mouth "I... I guess? Maybe?"

    skyla @closedbrow talking2mouth "Besides, you don't need powers to be a superhero. You just need..."

    pause 1.0

    skyla @sadbrow talkingmouth "Well, I guess that's the problem. I don't know what you need to be a superhero."
    skyla @closedbrow talkingmouth "I thought that if I stopped two criminals from... I don't know. Doing what they're doing... that maybe I'd be making some progress there."

    red @talkingmouth "Tell me more. Where did this desire come from?"

    skyla @talkingmouth "Well..."

    if (not IsBefore(1, 5, 2004)):
        skyla @sad "When you were up on that stage, or when Sabrina was being harassed by those two punks... I wanted to help. I wanted {i}so desperately{/i} to help. But I had no idea what to do."

        skyla @closedbrow talkingmouth "I've always wanted to be a hero. That was my chance!"

        skyla frownmouth @sad "...And I blew it."

        pause 1.0

    if (not HasEvent("Skyla", "Backstory")):
        $ AddEvent("Skyla", "Backstory")
        skyla closedbrow talking2mouth "I'm from Mistralton City, in the West of Unova, but there's a town on the East side of the region called Lentimas, and they were, like, really isolated, so..."
        skyla happy sweat "I learned to fly so I could, uh, transport stuff over there. Food and medicine and stuff."

        pause 1.0

        red @talkingmouth "Uh... so you had family there, or something?"

        skyla -happy -sweat talkingmouth "Nope. No connection. Well, before I got my pilot's license, anyway."

        red @talkingmouth "So you just... learned to fly planes... to help out a town on the opposite side of the region? That you had no connection to?"

        skyla closedbrow sweat -talkingmouth @talkingmouth "Yyyyyep."

        red @happy "That's insane."

        skyla @talkingmouth "I've heard that before."

    skyla -frownmouth @closedbrow talking2mouth "I just... heroes are {i}it{/i}, you know? They're the best thing there is. The best kind of person."
    skyla @happy "Think about other titles. There can be bad presidents, bad cops, even bad Champions."
    skyla @talkingmouth "But there's no such thing as a bad hero."

    red @closedbrow talking2mouth "I guess that's true."

    show skyla:
        ease 0.25 ypos 1.2 zoom 1.3

    skyla @talkingmouth "I want to {i}help{/i} people, [first_name]. Really help them. And I want to punish those who hurt others."

    red @sadbrow talkingmouth "You're already the one point of contact to an extremely isolated town back in Unova. And you're still doing flights for them, right?"

    skyla @talkingmouth "Yeah. Not as often as I used to, but my family's taken over most of my flights while I'm in Kobukan."

    red @closedbrow talking2mouth "I can't help but feel like you're already helping people. Like, a {i}lot.{/i} Doesn't that mean you're already a hero?"

    skyla @talkingmouth "...I thought so, at first. Like, right after I got my pilot's license, for a few years, I really thought that was all I needed."

    pause 1.0

    skyla @sadbrow talkingmouth "But I've been doing that for a few years. And I'm kinda over it. If I'm going to be a hero, a {i}real{/i} hero, I'm going to need to do more than just transport food and medicine to people."

    red @confused "So you settled on stopping criminals."

    skyla @talkingmouth "Yeah! When I graduate, I want to become a Pokémon Ranger."

    red @surprised "Like the TV Show?"

    skyla @angry "Wha- no! Like the job!"
    skyla @talkingmouth "There's this one super-famous and super cool ranger in Fiore--well, actually, she's from Almia, but she lives in Fiore now--called Elita."
    skyla @happy "She's famous for this awesome Skarmory she flies around with, and everyone calls her the 'Steel Samurai of the Sky!'"

    red @confused "Everyone?"

    skyla @closedbrow talking2mouth "Well, the producers of {i}Pokémon Rangers{/i} call her that."

    red @confused "The producers of the job?"

    skyla @angry "Wha- no! The show!"

    pause 1.0

    skyla @sadbrow talkingmouth "Oh, wait. You were messing with me, weren't you?"

    red @happy "Maybe a little bit."

    skyla @happy "Jerk. Be serious! I'm pouring out my hopes and dreams for you here."

    red @closedbrow talking2mouth "I mean, being a Ranger is a great goal. And I support that for you, seriously. But running into the middle of a city, and looking for a fight, just seems dangerous."
    red @happy "And I can't see how that'll make you any more heroic, honestly."

    skyla sadbrow frownmouth @talking2mouth "But..."

    red @closedbrow talking2mouth "If you want to be a hero, I think the best chance you have is to {i}help{/i} people. Keep on doing what you've been doing."

    skyla @thinking "[ellipses]"

    red @sadbrow talkingmouth "No-one's going to think you're any less of a good person if you do the same good things every day."

    skyla @talkingmouth "Yeah, but would you watch a cartoon where the hero does the exact same thing in every episode?"

    red @confuse "I... didn't really watch a lot of TV. But I guess that does sound... boring."

    skyla @talkingmouth "I don't want to be a... a {i}fixture{/i}, [first_name]."
    skyla @happy "I want people to {i}cheer{/i} when they see me. Not just think 'oh, here comes Skyla, with the food again.'"

    red @sadbrow talkingmouth "Then... are you really doing it for other people? Or are you doing it for yourself?"

    skyla @sad "{w=0.5}.{w=0.5}.{w=0.5}."
    skyla -frownmouth @closedbrow talking2mouth "If I wanted to do good things for the wrong reasons, is that so bad?"

    red @closedbrow talking2mouth "I genuinely have no idea. We might need to ask a Professor that one. It's a bit too philosophical for me to figure out."

    skyla -sadbrow @talkingmouth "Well, alright, then! Let's do that."

    red @surprised "Huh? Do what?"

    skyla @happy "You suggested it! Talk to a Professor, goof."
    skyla @talkingmouth "Even if they can't answer whether selfish good is still good, maybe they can think of ways I can be a hero..."

    pause 1.0

    skyla @sad "That are less likely to end up with me unconscious in an alleyway."

    pause 1.0

    skyla @sadbrow talkingmouth "I should... probably thank you for what you did, by the way."
    skyla @closedbrow talking2mouth "I wasn't really thinking, and if I'd gone into that alley alone, and had to face down all those thugs by myself, well... I don't know what would've happened."

    red @happy "Oh, nothing {i}too{/i} bad, I'm sure. They're not really scary, just kinda... lost and bored."
    red @talkingmouth "Besides, their boss is a good person."

    skyla @surprised "Oh! Yeah, that reminds me! How do you know those people? How do you know whoever their boss is?"
    skyla @closedbrow talking2mouth "Were you secretly part of their evil team? But then you broke away, blowing up their base as you left, but not before stealing a powerful piece of forbidden technology?"

    red @talking2mouth "Yes, that's it exactly. Nailed it."

    skyla @happy "Yessss. Knew it!"

    red @surprised "Wait, you, uh... sorry, I should've made clear I was joking. Yeah, that's not actually the case."

    skyla @sad "Aw. But that was fun."

    show skyla surprisedbrow frownmouth with dis

    red @talkingmouth "Sorry to disappoint. One of those thugs stole the hat of a friend of mine. I ran after him, chased them to their hideout, and then met their boss."

    pause 1.0

    show skyla angrybrow frownmouth with dis

    skyla @angry "Oh, but when {i}I{/i} do it, suddenly you're all 'vigilantism is bad' this and 'with great power comes great responsibility' that!"

    red @confused "I can guarantee I never said that second one."

    skyla -angrybrow -frownmouth @closedbrow talkingmouth "Well... I remember you saying that."

    red @sadbrow talkingmouth "Will you at least promise me that you won't try to battle an entire gang before we have time to figure out alternate, {i}safer{/i} ways of handling your hero complex?"

    if (not IsBefore(1, 5, 2004)):
        red @sad2eyes talking2mouth "Personally, I'd think being part of the Disciplinary Committee would be enough, but if not, then..."

    skyla @angrybrow talkingmouth "God, fine. But you're being a total buzzkill."

    red @closedbrow talking2mouth "If that's the price I have to pay to keep you safe, then that's what I'll do."

    pause 1.0

    skyla @talkingmouth "Hey. It just occurred to me. Every superhero has a {color=#0048ff}sidekick{/color}, right?"

    red @talking2mouth "With the greatest amount of respect--I will not be your sidekick."

    skyla @sad "Aw..."

    red @closedbrow talking2mouth "Maybe later. How about, for now... I be your wingman?"

    skyla @happy "Alright! I'll take it! That can even be your codename--{color=#0048ff}Wingman!{/color}"

    $ RelationshipRankUp("Skyla", "Wingman", 1)

    scene blank2 with Dissolve(2.0)

    pause 2.0

    narrator "Later, back in your dorm, you discover a letter pushed underneath your door."

    if (HasEvent("Silver", "Overthrown")):
        TempCharacter("{color=#686080}???{/color}") "Thanks for handling that. With me gone, it's harder to stop her and Copycat from {i}really{/i} getting into a fight. It's getting {s}fucking{/s} {s}goddamn{/s} {s}really{/s} annoying."
        TempCharacter("{color=#686080}???{/color}") "See if you can keep pointing her in other directions. At least until I'm back in the shack, and in control again.{w=1.0} -S"

    else:
        TempCharacter("{color=#686080}???{/color}") "Thanks for handling that. She's tried to 'vanquish' my guys a couple of times. It's getting {s}fucking{/s} {s}goddamn{/s} {s}really{/s} annoying. Keep her out of my hair, and you'll be rewarded.{w=1.0} -S"

    $ ValueChange("Silver", 3)

    narrator "Your understanding of Silver increased!"

    return

label Skyla1Part2:
    $ AddEvent("Skyla", "Skyla1Part2")
    stop music fadeout 1.5
    
    $ renpy.music.queue("Audio/Music/MistraltonCity.ogg", channel='music', loop=True, fadein=1.5, tight=None)

    show screen songsplash("Mistralton City Remastered", "Zame")

    #show phone_B
    #show phone_A
    show skyla behind phone_A:
        zoom 0.8 ypos 0.9 xpos 0.53
    with fadeinbottom

    red casual night hatless @happy "Oh? Skyla, hey! I don't think I had your number?"

    skyla @talkingmouth "Nope! I just remembered I needed to reach out to you, though! Got this number from Gardenia. Hope that's alright?"

    redmind @thinking "She got this number from Gardenia... who got it from Nate. Well, when it's out there, it's out there."

    $ BecomeContacted("Skyla")

    red @talking2mouth "Totally fine, yeah. You said you needed to reach out? Right, right. We were going to ask your Professors about heroism, I think?"

    skyla @talkingmouth "Yeah. Whether doing a good thing for the wrong reason is all that bad... and how I could be a hero until I actually get superpowers."

    red @sadbrow talkingmouth "Right, and I was going to try to convince you you're already a hero."

    skyla @happy "I think we discussed {i}around{/i} that point."

    red @talking2mouth "Well, what's the plan? Are you going to do it alone, or...?"

    skyla @talking2mouth "I could, but I thought you might want to come with?"

    if (HasEvent("Instructor Winona", 2.1) and HasEvent("Burgh", 2.1)):
        red @talkingmouth "Of course! I've been to both Instructor Winona and Instructor Burgh's classes pretty often already, so it's not like I'm going out of my way."
    elif (HasEvent("Instructor Winona", 2.1)):
        red @talkingmouth "Of course! I've been Instructor Winona's classes a good few times already, so it's not like I'm going out of my way, for her, at least."
    elif (HasEvent("Burgh", 2.1)):
        red @talkingmouth "Of course! I've been Instructor Burgh's classes a good few times already, so it's not like I'm going out of my way, for him, at least."
    elif (not (IsNamed("Burgh") or IsNamed("Instructor Winona"))):
        red @talkingmouth "I don't think I know either of your type elective instructors, so this'd be a chance to meet some new members of the faculty."
    elif (not IsNamed("Burgh")):
        red @talkingmouth "I don't think I know your Bug-type elective instructor, so this'd be a chance to meet a new member of the faculty."
    elif (not IsNamed("Instructor Winona")):
        red @talkingmouth "I don't think I know your Flying-type elective instructor, so this'd be a chance to meet a new member of the faculty."
    else:
        red @talkingmouth "Of course! Can't let you go into that big, scary, classroom all by yourself."

        skyla @happy "My hero!"

    $ ValueChange("Skyla", 1)

    skyla @talkingmouth "I'll see you there, then! No rush, but I'd like to talk to both of them."

    red @talkingmouth "It's cool. I'll make time for it, at some point. Talk to you later?"

    skyla @happy "Sayonara!"

    stop music fadeout 2.0

    scene blank2 with Dissolve(2.0)

    return

label Skyla1Part3:
    $ AddEvent("Skyla", "Skyla1Part3")
    scene classroom
    show bugtype:
        xalign 0.5 yalign 1.0
    with dis

    $ location = "bug"

    show skyla uniform with dis:
        xpos 0.5 xzoom -1

    stop music fadeout 1.5
    
    $ renpy.music.queue("Audio/Music/MistraltonCity.ogg", channel='music', loop=True, fadein=1.5, tight=None)

    show screen songsplash("Mistralton City Remastered", "Zame")

    skyla @talking2mouth "Hey, [first_name]!"

    if (GetEventDatetime("Burgh", 1) == calDate):
        skyla @talkingmouth "This was your first Bug-type elective, right?"

        red uniform @talkingmouth "Sure was. Instruct-- sorry, {i}Burgh{/i} is an interesting guy."

        skyla @happy "Right? He's so passionate about his art, but, like, not in one of those pretentious ways where they're talking about lines and colors and how the color blue means depression."

        red @closedbrow talkingmouth "Right."

        skyla @talking2mouth "His relationship with Bugsy is pretty cute, too. Burgh doesn't show favorites--at least he tries not to--but the way those two talk is adorable. I've never seen someone who likes bugs so much!"

        red @talkingmouth "You know, I'm not sure I ever asked--what's up with bugs?"

    else:
        red uniform @talkingmouth "Hey, Skyla. You know, I'm not sure I ever asked--what's up with bugs?"

    skyla @talking2mouth "What do you mean?"
    
    red @happy "Just kinda surprised you're taking this class, I guess. There's a lot of Bug/Flying-types out there, but I'm not sure I've known too many people who learn to master {i}both{/i} types."

    skyla @talkingmouth "I just think bugs are neat. I mean, that's why Rosa, world-famous celebrity, is here!"
    skyla @angrybrow talkingmouth "They're the ultimate underdog, you know? The littlest guys, fighting with foes a hundred times their size."
    skyla @closedbrow happymouth "In the world of bugs, every single one of them is a superhero."

    red @happy "Fair enough. Now, we were going to talk to Burgh, right?"

    skyla @talkingmouth "Oh, yep."

    show burgh norm with dis:
        xpos 0.33

    show skyla with dis:
        xpos 0.5
        ease 0.5 xpos 0.66

    if (HasEvent("Burgh", 2)):
        burgh @norm2 "Ah. Hello, Skyla. Hello, [first_name]."

    else:
        burgh @norm2 "Ah. Hello, Skyla. Hello..."
        burgh sad @sad2 "Sorry, could you remind me?"

        red @happy "'Course. [first_name]."

        burgh norm @norm2 "Of course, [first_name]. Thank you, I'll remember for sure, now."

    skyla @talkingmouth "We wanted to ask you a question!"

    $ pokemonname = GetTrainerTeam("Skyla", "Ledyba").GetNickname()#could be ledian

    burgh @happy2 "I'm glad to hear it. That's what I'm here for. Is it about your [pokemonname]? Is it still posing at inopportune times in battle?"

    skyla @talkingmouth "No, it's--"
    skyla @sadbrow talkingmouth "Well, actually, yes, it is, but I think we're making progress on it."

    burgh surprised @norm2 "Okay. So, what did you want to ask?"

    skyla @angrybrow talkingmouth "It's about heroism!"

    burgh @surprised2 "I wasn't expecting that."
    burgh norm @happy2 "Sounds like a fun discussion, though. I'll do my best to answer your question."
    burgh @norm2 "What about heroism did you want to ask?"

    skyla @talking2mouth "So, hypothetically, if there was someone who did a bunch of good stuff for other people, would you call them a hero?"

    burgh @norm4 "Hm... I'd call that a good start, but not {i}necessarily{/i} heroic."
    burgh @norm2 "It's not quite so simple: what 'good stuff' did they do? Why did they do it? How did everything turn out?"
    burgh @norm4 "I don't think heroism is about acts of kindness alone. The context, I believe, is very important."
    
    skyla @closedbrow talking2mouth "You mean like... making sure the good stuff you do actually helps people? Not just {i}trying{/i} to help people?"

    burgh @norm2 "Certainly. Donations to charity, for example, are a kindness--but not always {i}heroic{/i}." 
    burgh @norm4 "It's easy enough to spare some change for a Pokémon shelter. But often, shelters need volunteers more than money--people who'll spend time to look after their charges, and to bring in Pokémon in need."
    burgh @norm2 "A truly good person reflects on their actions, before {i}and{/i} after. Is the true goal to help, or to ease one's conscience? Did good really come of their actions?" 
    burgh happy2 "Were there unintended consequences? What could they do better next time?"

    skyla @sadbrow talking2mouth "So, if someone tried to do something good and it backfired, then... they're not a hero?"

    burgh @happy2 "I wouldn't say that."
    burgh @norm2 "Some of the noblest acts are failures. What matters is that the actor's heart was in the right place, and that they learned from it."
    burgh @norm4 "One deed doesn't define a person's character. We can't define ourselves by the consequences or causes of a moment. Nor by the actions of that moment."
    burgh @happy2 "People and Pokémon alike shift, change, evolve, mutate, pupate, and discover themselves."
    burgh @norm2 "Besides, in this hypothetical, this 'something good' backfired. Surely that was an accident?"
    burgh @norm4 "The hero has a duty to be careful, so such an accident doesn't reoccur. But they have no duty to deprive themselves of the joy of helping another, simply because they failed once."
    burgh @happy2 "I know you've watched this show, haven't you? 'It is possible to commit no mistakes and still lose. That is not a weakness. That is life.'"

    skyla @sadbrow talkingmouth "Oh, true..."
    skyla @happy "Okay, great! Hypothetically, I'm really happy to hear that. But, um, follow-up question."

    burgh @norm2 "I assumed."

    skyla @talking2mouth "What if this hypothetical hero wasn't, um, so... purely-motivated? What if they just wanted to help people to..."
    skyla @sadbrow talkingmouth "Um. Stand out? Be liked? Be admired?"

    burgh @norm4 "That's a trickier question. Motives {i}do{/i} matter. If someone's doing good just to feed their own ego, it can poison the act, especially if those self-centered motives start to take precedence. I've seen how that can lead to disaster."
    burgh norm3 @norm4 "As, I'm sure, has every Unovan."

    skyla @surprised "Do you mean... um, Team--"

    burgh @sad2 "Yes. Yes, I do." 
    burgh @sad2 "At their core, a lot of their ideals had merit--helping Pokémon, standing against cruelty. But somewhere along the way, for many of them, it became about power, control, or personal gain." 
    burgh sad @sad2"Even the good things they did were tainted by those motives."

    skyla sadbrow frownmouth @sadbrow talking2mouth "So... if someone helped others but only cared about {i}looking{/i} like a hero, they wouldn't really be one?"

    burgh sad @sad2 "I would... {i}struggle{/i} to describe them as such, yes."
    burgh @norm4 "Though it's my personal opinion, I can't see {i}true{/i} heroism as directed toward applause, or toward spotlight. It's about centering others--their needs, their struggles, their well-being." 
    burgh @norm4 "And staying honest with oneself about why one is doing it."

    pause 1.0

    burgh norm @sad2 "For what it's worth, Skyla, I don't believe this mild criticism applies to you. I know what you've done for those people in Lentimas. You've helped hundreds." 
    burgh @happy2 "And, if I recall correctly, you've never asked them to name a street after you."

    skyla @sadbrow talking2mouth "I might've wanted them to, though..."

    burgh norm @norm2 "We often want things that our good sense, and true hearts, dissuade us from taking action to possess. Gain is tempting, but I don't believe this temptation has unduly shaped your priorities."

    skyla @sadbrow talkingmouth "Um... okay. Thanks."

    pause 1.0

    burgh @sad2 "I'm sorry I couldn't give you a wholly satisfactory answer."

    skyla @sadbrow talkingmouth "It's alright. Maybe this is what I needed to hear."

    burgh @norm2 "Maybe. Well, I am, after all, only one person. I am sure you have other instructors whose minds you could pick."
    burgh happy @happy2 "I have thoroughly enjoyed having you in my classes, Skyla--and look forward to seeing more of you."

    if (GetEventDatetime("Burgh", 1) == calDate):
        burgh @norm2 "[first_name], it was a pleasure to have you in class today. I hope to see more of you."

        red @happy "Same, Inst--, uh, Burgh."

    else:
        burgh @norm2 "[first_name], have a nice [timeOfDay.lower()]."

        red @happy "Same, Burgh."

    skyla happybrow -frownmouth @happy "I'll see you tomorrow, Burgh!"

    hide burgh with dis

    pause 1.0

    show skyla sadbrow with dis

    pause 0.5

    jump Skyla1PartsConclusion

label Skyla1Part4:
    $ AddEvent("Skyla", "Skyla1Part4")
    scene classroom 
    show flytype:
        xalign 0.5 yalign 1.0
    with dis

    $ location = "flying"

    show skyla uniform with dis:
        xpos 0.5

    stop music fadeout 1.5
    
    $ renpy.music.queue("Audio/Music/MistraltonCity.ogg", channel='music', loop=True, fadein=1.5, tight=None)

    show screen songsplash("Mistralton City Remastered", "Zame")

    skyla @talking2mouth "[first_name]! Thanks for being here."

    if (GetEventDatetime("Instructor Winona", 1) == calDate):
        skyla @talkingmouth "This was your first Flying-type elective, right?"

        red uniform @talkingmouth "Yep. It's cool to see a Kobukan Instructor who's so young."

        if (IsNamed("Professor Cherry")):
            red @talkingmouth "'Course, Professor Cherry's even younger, but it's not a competition."

        skyla @closedbrow talkingmouth "Instructor Winona's one of those people who realized, early, that they can do whatever they set themselves to, even if they've never seen anyone else do it!"

        red @talkingmouth "Like you, Ms. Pilot?"

        skyla @sadbrow talkingmouth "Well... I'm not sure I'd call {i}myself{/i} that."
        skyla @happy "But I don't think Instructor Winona would call herself that, either. She tends to get a bit nervous in classes."

    else:
        red uniform @talkingmouth "I've been here before. It's not an issue."

    skyla @happy "Anyway, let's talk to Instructor Winona!"

    show winona with dis:
        xpos 0.33 xzoom -1

    show skyla with dis:
        xpos 0.66 xzoom -1

    if (HasEvent("Instructor Winona", 2)):
        winona @talking2mouth "Skyla? [first_name]?"

    else:
        winona @talking2mouth "Skyla? And, um, your friend...?"

        red @happy "[first_name]."

        winona @sadbrow talkingmouth "Right! Right, of course. [first_name]."

    skyla @talkingmouth "We wanted to ask you a question!"

    $ pokemonname = GetTrainerTeam("Skyla", "Ledyba").GetNickname()#could be ledian

    winona @surprised "Oh. Your [pokemonname], again? Is it still striking poses in the middle of battle?"

    skyla @happy "A little bit, but that's not what I'm asking about {i}this{/i} time."

    winona @talking2mouth "Oh! Okay. Good. I'm not sure what else we could do about that, because, y'know... Bugs. Not birds."
    winona @surprised "N-not that there's anything wrong with bugs! I'm sure most of them are, uh, {i}great{/i}, and don't lay eggs in your ears at all!"
    winona surprisedbrow @surprisedbrow talking2mouth "Oh, but, sorry, you had a question! Um, what is it?"

    skyla @angrybrow talkingmouth "It's about heroism!"

    winona -surprisedbrow -frownmouth @talking2mouth "Heroism? Oh... okay. Sure. Heroism. I'm, um, not the best person to ask about this, I don't think, but I'll do my best."
    winona @talkingmouth "What about heroism?"

    skyla @talking2mouth "So, hypothetically, if there was someone who did a bunch of good stuff for other people, would you call them a hero?"

    winona @talkingmouth "I... guess so? Yes? Well, not {i}just{/i} good stuff. There are plenty of people who do good things, but aren't heroes."
    winona surprisedbrow @sadbrow talkingmouth "You know, important people, people who are necessary, but... not heroes. Like, um, mailmen, and farmers, and... teachers..."

    skyla @closedbrow talking2mouth "Hm. What would make them heroes, then...?"

    winona -surprisedbrow -frownmouth @surprisedbrow talking2mouth "Make them heroes? I guess... if they did something really big? Something that changed somebody's life? Maybe?"
    winona @closedbrow talking2mouth "For example, if a, um, a taxi driver went to work and... just drove his taxi every day... that wouldn't make him a hero."
    winona @sadbrow talkingmouth "But if he brought someone sick to the hospital, and then the doctors saved them, then he {i}would{/i} be a hero, right?"
    winona @sadbrow talking2mouth "Or maybe the doctors would be the heroes? Are {i}all{/i} doctors heroes?"
    winona @surprised "M-maybe all taxi drivers are heroes, too, because they drive lots of people around, and sometimes to the hospital?! But--wait--what about ambulances?!"
    winona @talking2mouth "I guess what I'm saying is... it's all kind of relative?"

    redmind @sadbrow "Winona seems to have more questions than answers, here..."

    show skyla sadbrow frownmouth with dis

    redmind @sadbrow frownmouth "And Skyla doesn't seem to like hearing that heroes can't just do everyday stuff and still be heroes."
    redmind @closedbrow frownmouth "I guess that {i}is{/i} the exact opposite of my opinion."
    redmind @sadbrow "Well, that's the thing about opinions. Everyone's got 'em, and they won't always line up."

    winona @sadbrow talking2mouth "Did I say something wrong?"

    skyla @happybrow talkingmouth "N-no, not at all! I'm um, just thinking about my follow-up question."

    winona @surprisedbrow talking2mouth "{size=30}There's more?{/size}"
    winona @happy "Oh, okay! Sure. More questions. I can handle that. Yup!"

    skyla @closedbrow talking2mouth "So... being a hero really is about doing something big. Something extraordinary. I thought so."
    skyla @sadbrow talkingmouth "But... what about {i}why{/i} the hero does it? Like, what if their motivation is, um... not ideal?"

    winona @talking2mouth "What do you mean? Heroes can be motivated by all sorts of things. Belief in a higher purpose, necessity, the desire to challenge themselves... even fear."

    skyla @sadbrow talkingmouth "Okay. But what if their motivation, is, um... wanting to stand out? Be admired? Be, well, cool? Is that selfish?"

    winona @surprisedbrow talking2mouth "Selfish? Oh, no, no, I don't think so, Skyla. I mean, um, people are... people are supposed to feel good about helping others, aren't they?"

    skyla @sadbrow talking2mouth "I don't know. Wouldn't it be wrong to enjoy it too much? I think that's a sign that, um, the hero isn't doing it for the right reason. I could see {i}someone{/i} feeling guilty over that."

    winona @closedbrow talking2mouth "Well... guilt can be good. It helps us, uh, notice when we've done something wrong. But, um... this? This hypothetical? I really don't think there's anything wrong with being motivated by... by praise, or thanks, or adoration."
    winona @happy "I think... feeling happy because you've made someone else happy--that's normal. That's good--it's {i}right{/i}! That's why so many teachers become teachers, after all."

    skyla @closedbrow talking2mouth "But what if a person just... thrives on that? Like, on gratitude and feeling loved? Doesn't that kinda make it seem like this person would stop if the thanks dried up?"

    winona @sadbrow talkingmouth "I think I'd need to know the person to know for sure." 
    winona @closedbrow talkingmouth "But, since this is a hypothetical, we could pretend we're talking about you?"

    skyla @closedbrow talkingmouth "Sure."

    winona @sadbrow talkingmouth "Well, if it {i}was{/i} you, I think I'd say that... I don't think there's a wrong reason for being kind. And if there is, I don't think wanting to be appreciated for it is it."
    winona @closedbrow talking2mouth "M-maybe I'm not the right person to say this, but, um, you might be overthinking this, Skyla. The way you care so much, and how hard you work... it just seems like you're a good person!"
    winona @talkingmouth "I mean, that's what makes sense to me, anyway. If you did 'big stuff,' you could definitely be a hero. For whatever reason you wanted. That's what I think."

    skyla @sadbrow talkingmouth "Well... thanks. I think."

    winona @talking2mouth "I, um, really hope I didn't say anything wrong!"

    skyla @sadbrow talkingmouth "It's alright. Maybe this is what I needed to hear."

    winona sadbrow smilemouth @talkingmouth "Oh. Um, well, you can definitely ask someone else. Actually, yeah! You should definitely do that! {size=30}And if someone says something different, j-just ignore everything I told you, okay...?{/size}"
   
    hide winona with dis

    if (GetEventDatetime("Instructor Winona", 1) == calDate):
        narrator "Instructor Winona quickly absconds, her relative confidence quickly departing."

    else:
        narrator "Instructor Winona quickly absconds, as her uncharacteristic confidence abandons her."

    pause 1.0

    show skyla sadbrow with dis

    pause 0.5

    jump Skyla1PartsConclusion

label Skyla1PartsConclusion:
    red @sadbrow talkingmouth "Thoughts...?"

    if (not (HasEvent("Skyla", "Skyla1Part4") and HasEvent("Skyla", "Skyla1Part3"))):
        skyla -sadbrow @sadbrow talkingmouth "Well, I definitely want that second opinion the Instructor mentioned."
        
        if (HasEvent("Skyla", "Skyla1Part3")):
            skyla @talkingmouth "You'll come with me to Instructor Winona's class, right?"

        elif (HasEvent("Skyla", "Skyla1Part4")):
            skyla @talkingmouth "You'll come with me to Instructor Burgh's class, right?"
            
        red @happy "Yeah, sure thing."

        if (timeOfDay != "Afternoon"):
            skyla @talkingmouth "Alright. I'll be there this afternoon!"

    else:
        $ AddEvent("Skyla", "TalkedBothProfessors")

        skyla @angrybrow talking2mouth "...I didn't get the answers I wanted."

        red @sweat closedbrow talking2mouth "Yeah, that'll happen, sometimes."

        red @sadbrow talkingmouth "Want to talk about it?"

        skyla @talking2mouth "...I guess. Eventually."

        if (HasLocation("Cafe")):
            red @talking2mouth "Alright. Let's go out to the city at some point. Drown your troubles in sugar at the Inspira Pokécafe. We'll chat then."
        else:
            red @talking2mouth "Alright. Let's go out to the city at some point. Drown your troubles in sugar at a cafe somewhere. We'll chat then."

        skyla sadbrow frownmouth "[ellipses]"

        red @sadbrow talkingmouth "Unless you'd rather do something else?"

        skyla @sadbrow talking2mouth "No, that's fine... I guess."

        red @happy "Alright. Talk to you later."

        skyla @sadbrow talkingmouth "Yeah. Seeya."

    $ location = "school"

    return

label Skyla2:
    $ location = "city"
    $ AddEvent("Skyla", "Skyla2")
    
    scene citycafe 
    with Dissolve(2.0)
    show screen songsplash("Relic Song", "Zame")
    $ renpy.music.play("Audio/bigcrowdloop.ogg", channel='crowd', loop=True, fadein=0.5)
    play music "audio/music/relicsong.ogg"

    if HasLocation("Cafe"):
        narrator "You're sitting back in a booth at the Inspira Pokécafé, sipping on some kind of sugar mixture that purports to be coffee."
    else:
        $ RecordKnownLocations("Skyla", "Cafe")
        narrator "You vaguely remembered a cafe that you briefly encountered during Leaf's whirlwind shopping trip, and, through some insistence on your part, managed to drag Skyla there."

    if IsWeekday():
        if GetRelationshipRank("Tia") > 1:
            narrator "In the background, Tia smiles merrily as she dances from table to table, serving drinks and food to the hungry patrons and their Pokémon."
        else:
            narrator "In the background, a waitress smiles merrily as she dances from table to table, serving drinks and food to the hungry patrons and their Pokémon."
    else:
        narrator "In the background, a waitress smiles merrily as she dances from table to table, serving drinks and food to the hungry patrons and their Pokémon."

    if (IsAfter(26, 5, 2004)):
        narrator "Even Melody, who is also here (and not wearing the uniform) seems to be in a fairly decent mood."

    narrator "Generally, everyone's having a good time. Everyone except[ellipses]"

    show skyla angrybrow frownmouth with Dissolve(2.0):
        ypos 1.2 zoom 1.3

    skyla "[ellipses]"

    narrator "She glares at your drink like she's trying to drill a hole in it with laser vision."

    redmind @thinking "Knowing her, she just might be."

    red @poutmouth "[ellipses]"
    red @poutmouth "{i}Sipppppp.{/i}"

    skyla @talking2mouth "Do you have to drink so loudly?"

    red @sweat talking2mouth "I'm just sitting here, Skyla."

    pause 1.0

    skyla sadbrow frownmouth @talking2mouth "This sucks."

    pause 1.0

    show skyla angrybrow with dis

    red @confused "You didn't really think that either of your instructors were going to tell you to go out and pick a fight with the incarnation of evil, did you?"

    skyla @talking2mouth "Don't make fun of me, [first_name]. I'm actually upset."

    red @sadbrow "[ellipses]"

    show skyla sadbrow with dis

    red @talking2mouth sadbrow "Sorry."

    pause 1.0

    red @talking2mouth "You know, I think you'd be a great hero. I think you're already a hero, but I think, you know, if you had the {i}chance{/i}, if the moment to do something {i}really{/i} extraordinary fell into your lap, you'd be great at it."

    pause 0.5

    skyla sadbrow -frownmouth  @talking2mouth "You're sweet."

    red @closedbrow talking2mouth "What's {i}sweet{/i} is this drink. I'm about to go into cardiac arrest if I take one more sip from it."
    red @sad2brow talking2mouth "We should probably get back to campus, now."

    $ RecordKnownLocations("Skyla", "JoinAvenue")

    red @sadbrow talkingmouth "Would it make you feel better if we dropped by Join Avenue on the way back? You could yell at that nose cream salesmen for harassing preteens again."

    skyla @sadbrow talkingmouth "I {i}do{/i} like that[ellipses] I think we should probably just go home, though. I've got some studying to do. Studying to prepare for my boring life as a boring ol' pilot and Gym Leader."

    red @closedbrow sweat talking2mouth "Skyla, I sympathize--really--but where I come from, most people's career ambitions topped out at 'spam caller.' Being a pilot is amazing. Being a Gym Leader is even better."
    red @sadbrow talkingmouth "The sky's the limit. Just, y'know, the opposite way people normally mean that."

    skyla @sadbrow talking2mouth "Guess so."

    show skyla:
        ypos 1.2 zoom 1.3
        ease 0.5 ypos 1.0 zoom 1.0

    show wes paintlesshood cloakhood nogoggles:
        xpos 1.2 xzoom -1
        ease 0.5 xpos 0.85

    stop music fadeout 1.5

    skyla @closedbrow talking2mouth "Alright. I guess it's time we--"
    skyla "[ellipses]"

    pause 2.0

    skyla @talking2mouth "Um, hi?"
    skyla @closedbrow talking2mouth "[first_name], this guy's staring at me, not moving, and is wearing a black cloak. Bad-guy vibes, right?"

    red @wince talking2mouth "Skyla, you gotta stop judging people based on their appearance."

    redmind @thonk "That being said... what {i}is{/i} this guy's deal?"

    red @happy "Hey, my name's [first_name]. What's up?"

    show skyla surprisedbrow frownmouth:
        xpos 0.5
        ease 0.5 xpos 0.33

    $ renpy.music.queue("Audio/Music/theonlyshadowleft.ogg", channel='music', loop=True, fadein=1.5, tight=None)

    show screen songsplash("Colosseum Battle Remastered", "Zame")

    wes @talking2mouth "Not you. Her..."

    show wes:
        xpos 0.85
        ease 0.5 xpos 0.8

    redmind @angrybrow frownmouth "Oh, that was weird. I'm getting bad-guy vibes now, too."

    pause 1.0

    show skyla angrybrow with dis

    red @talking2mouth "Hey, man. Why don't you tell us what you're talking about, before you step any closer?"

    pause 1.0

    wes @talking2mouth "Red hair."

    show wes:
        xpos 0.8
        ease 0.5 xpos 0.75

    wes @talking2mouth "Blue eyes."

    show wes:
        xpos 0.75
        ease 0.5 xpos 0.66

    wes @sadbrow talking2mouth "But... not {i}her{/i} eyes."

    pause 1.0

    wes @sad "I'm sorry. I thought you were someone I knew."
    wes @closedbrow talking2mouth "I apologize for taking your time."

    pause 1.0

    redmind @thonk "Is this some sort of really bizarre negging strategy? This isn't the first weirdo who's approached Skyla while we've been hanging out, but he's..."
    redmind @sad2eyes poutmouth "Well, he's one of the better-looking ones."

    skyla surprisedbrow frownmouth @happy "Oh, that's totally alright. I just have one of those faces, you know? I look like a lot of people."

    wes @sadbrow talking2mouth "If that were true, this world would be a much more beautiful one."

    pause 1.0

    redmind @unamusedbrow unamusedmouth "Is this guy serious?"

    skyla @talking2mouth "Oh. Um. Well, I'm, um, Skyla. So, hi. What's your name?"

    wes @talking2mouth "It doesn't matter. I'll be a memory to you in a minute--and to this region in a year."

    show wes:
        xpos 0.66 xzoom -1
        ease 0.5 xpos 0.66 xzoom 1

    wes pokeball @talkingmouth "Stay safe."

    show skyla surprised with dis

    show sideportraitfull:
        xpos 5.0 xzoom -1

    $ DisplayPokemon("Togetic")

    pause 1.0

    wes surprisedbrow frownmouth @closedbrow talking2mouth "Togetic, let's fly. Our quarry is somewhere in this city, and--"

    stop music fadeout 3.0 channel "crowd"

    show citycafe with vpunch

    $ PlaySound("!.ogg")

    skyla @surprised "What's wrong with that Togetic?!"

    show wes:
        xpos 0.66 xzoom 1
        ease 0.5 xpos 0.66 xzoom -1

    show sideportraitfull:
        pause 0.3 xzoom -1
        ease 0.5 xzoom 1

    pause 1.0

    TempCharacter("Barista") "Ma'am? Yes, you, the one dressed like a stripper, with tall, dark and gruesome over there. You're upsetting the other customers."

    skyla surprisedbrow frownmouth @sad "Oh, uh, sorry, it's just... this Togetic, it's...?"

    TempCharacter("Barista") "{size=30}Arceus, another one of those Kobukan students tripping on Joy Dust. There ought to be a law...{/size}"

    skyla @sadbrow talking2mouth "[first_name]? You see it, right? You see why this Togetic looks[ellipses] wrong?"

    narrator "You examine the Togetic carefully. But, any way you look at it, it comes out looking like an ordinary Togetic."

    red @sadbrow talking2mouth "Sorry."

    $ HidePokemon()

    wes -pokeball @talking2mouth "You can see it?"

    skyla @talking2mouth "Wait, you can, too?"

    show skyla:
        xpos 0.33
        ease 0.5 xpos 0.3

    show wes behind skyla:
        xpos 0.66
        ease 0.5 xpos 0.5

    wes @angrybrow talking2mouth "No. I've never been able to. There was one girl who could, though. Hair like fire, eyes like the sea, a heart of gold."

    show skyla:
        xpos 0.3
        ease 0.5 xpos 0.27

    show wes behind skyla:
        xpos 0.5
        ease 0.5 xpos 0.4

    wes sad "Rui?"

    pause 1.0

    skyla -surprisedbrow @sadbrow talkingmouth "Skyla."

    pause 1.0

    show wes:
        xpos 0.4 xzoom -1
        ease 0.5 xpos 0.43
        ease 0.5 xzoom 1
        ease 0.5 xpos 0.66
        ease 0.5 xzoom -1

    show skyla:
        xpos 0.27
        pause 1.0
        ease 0.5 xpos 0.33

    wes -sad @closedbrow talking2mouth "...Right. You said."

    pause 1.0

    red @talking2mouth "I'm so lost. There's something about this Togetic that only Skyla can see?"

    skyla @talking2mouth "I've always been told I had amazing vision... maybe that's it?"

    wes @talking2mouth "This is more than just vision. If your eyes can pierce the darkness, there may be a hope for the shadows that threaten destruction to this region yet."

    pause 1.0

    skyla @talking2mouth "You mean... I could be a hero?"

    wes @talking2mouth "You would be more than a hero. You would be the greatest Unovan hero."
    wes surprisedbrow @sadbrow talking2mouth "This is a heavy burden I place on you. If you--"

    skyla @angrybrow talking2mouth "I'll do it."

    wes "..."
    wes -surprisedbrow @sadbrow talking2mouth "Rui threw herself at the shadows, unarmed and defenseless, to bring some justice to this wretched world."
    wes @angrybrow talking2mouth "Perhaps there is a chance, after all, there is another Rui to take up the fight."

    pause 1.0

    show wes surprisedbrow with dis

    skyla @talking2mouth "I'm... I'm 100%% up for this saving-the-world thing, but I'm not Rui. I'm Skyla. Skyla Huuro."

    wes -surprisedbrow @talking2mouth "Right. Of course.{w=0.5} You mentioned."

    pause 1.0

    red @sadbrow talkingmouth "Please tell me what's going on?"

    pause 0.5

    narrator "The man jerks his head in your direction, not even bothering to look at you."

    wes @talking2mouth "This is your sidekick?"

    skyla @talking2mouth "Oh. Um, well, no. He's my, uh, my[ellipses]"
    skyla @happy "Wingman. [first_name] [last_name]."

    wes @talking2mouth "Bring him."

    skyla @talking2mouth "Bring him? Bring him where?"

    wes @talking2mouth "This is no place to discuss our justice. We need to meet up somewhere more privately."

    skyla @talking2mouth "Oh, okay. Like, um, where...?"

    wes @talking2mouth "The streets of Inspira contain many shadows at night. Some must be eliminated. Others provide useful occlusion. We'll meet there."

    skyla @talking2mouth "When? Should we, um, like, exchange phone numbers or--"

    wes @angrybrow talking2mouth "No. They can track you with those. You should throw away your phone. Don't say anything to anyone you can't see right in front of you."
    wes @closedbrow talking2mouth "Watch the sky at night. You'll see my mark. It is then you must come."

    skyla surprisedbrow frownmouth @surprisedbrow talking2mouth "O-okay..."

    show wes:
        xpos 0.66 xzoom -1
        ease 0.5 xzoom 1

    $ BecomeNamed("Wes")

    wes @talking2mouth "It's Wes."
    wes @sadbrow talking2mouth "You're now responsible for the fate of the entire world, Skyla Huuro."
    wes sadbrow @talking2mouth "{size=30}Forgive me.{/size}"

    show wes:
        xpos 0.66
        ease 0.5 xpos 1.3

    pause 2.0

    red @confused "We're not buying that, are we?"

    $ autoquote = False

    skyla happy "\"Oh my god, oh my god, oh my god, oh my god, oh my god, oh my god, oh my god, it's happening, it's finally happening, oh my god, oh my god, oh my god,"

    $ autoquote = True

    redmind @unamusedbrow unamusedmouth "Hook, line, and sinker."

    call clearscreens() from _call_clearscreens_254
    scene blank2 with splitfade

    narrator "This is a concerning development indeed! What does this mysterious man want with Skyla? What are these so-called Shadows? {i}What{/i}, exactly, was wrong with that Togetic?" 
    narrator "[bluecolor]Find out next time on Skyla's Bond Scene 2, Part 2, viewable starting tomorrow, any time you would normally text someone!{/color}"

    return

label Skyla2Part2:
    $ AddEvent("Skyla", "Skyla2Part2")
    stop music fadeout 1.5
    queue music "audio/music/potown_start.ogg" noloop
    queue music "audio/music/potown_loop.ogg"

    scene blank2 with splitfade

    narrator "You quickly change back into your regular clothes, and prepare to sneak out into the city."

    scene nightmap with splitfade

    redmind night @thinking "Man... breaking the rules to sneak out to the city {i}with a member of the disciplinary committee?{/i} No-one takes this curfew seriously..."

    if (HasLocation("Shady Nightclub")):
        narrator "You sneak off-campus without incident, and meet up with Skyla outside of a familiar-looking shady nightclub." 
    else:
        narrator "You sneak off-campus without incident, and meet up with Skyla outside of a shady nightclub." 

    if (GetRelationshipRank("Klara") > 0):
        narrator "The strong smell of Lombrero-Schweiß lager wafts out from inside, rekindling memories of a dubious wholesomeness."

    scene citystreetnight with splitfade

    $ location = "city"

    show wes painthood cloakhood nogoggles with dis

    $ renpy.music.queue("Audio/Music/theonlyshadowleft.ogg", channel='music', loop=True, fadein=1.5, tight=None)

    show screen songsplash("Colosseum Battle Remastered", "Zame")

    pause 1.0

    wes @talking2mouth "You came."

    skyla @talking2mouth "We did. I mean, we {i}had{/i} to. The fate of the world is at stake, here! Right?"

    wes @angrybrow talking2mouth "More than you can know."

    red @sadbrow talking2mouth "Please tell us what's going on here, man. I'm confused, worried, and frankly a little bit suspicious."

    wes @closedbrow talking2mouth "Understandable."

    pause 1.0

    show wes -painthood cloak goggles with dis 

    wes @talking2mouth "I am Wenceslaus of Nojave, Hero of Orre. I fought for Orre since childhood, fought against a poison that sought to corrupt the minds and hearts of its people."

    pause 1.0

    wes @sadbrow talking2mouth "I am here because I lost that fight."

    pause 0.5

    wes @talking2mouth "I believed that I had rescued and purified every Shadow Pokémon. I believed I had destroyed all the monsters making them."
    wes @angrybrow angrymouth "I let {i}one{/i} roach slip away from me. Just one."
    wes @angrybrow furiousmouth "And from that singular roach grew an infestation that ate the very foundations of the structure I had sacrificed so much to build!"

    pause 1.0

    wes @sadbrow talking2mouth "My partners... my Espeon and Umbreon... they were taken, and their own hearts were turned to darkness. They became weapons of the very shadows we had fought against."
    
    pause 0.5

    wes @talking2mouth "The Shadow Pokémon tore across the land, leaving dust where there once was grass--ash where there once was life."
    wes @sadbrow talking2mouth "Orre is lost. I wander the world, now, fighting to make sure what happened to my home cannot happen to others."

    pause 1.0

    show wes sadbrow with dis

    skyla @talking2mouth "Who was Rui?"

    wes @talking2mouth "Everything. She was everything to me. The light against shadow. My path and my map. My cause and my future."
    wes @angrybrow talking2mouth "Without her, I am... nothing. But I am a 'nothing' that will cut through the Shadows until the very end of my path."

    pause 0.5

    wes -sadbrow @sadbrow talking2mouth "In a more literal sense, she had a power--as do you, I believe--that let her see the shadows that surround a Pokémon's heart. We used this power to find and rescue Shadow Pokémon."

    skyla @surprisedbrow talking2mouth "A power?"

    wes @talking2mouth "No other word for it."

    skyla @surprisedbrow talking2mouth "I have a superpower."

    wes @talking2mouth "A rare and valuable one. One that proves you are in the right place, at the right time. I can guide this power--help you sharpen it, hone it."
    wes @talking2mouth "This power is the {i}only{/i} way Kobukan's fate can be averted from disaster. You are our only hope. You are our only hero."

    pause 1.0

    skyla @talking2mouth angrybrow "I'll do it. I'll do anything."

    red @talking2mouth "Hold on. What, exactly, are we fighting here? 'Shadow Pokémon?' You said that a couple of times. Are those like Frenzied Pokémon?"

    wes @talking2mouth "I don't know what Frenzied Pokémon are. But I suspect they are dissimilar."
    wes @angry "Shadow Pokémon have had the doors to their hearts shut, through cruel science, and acts unmentionable."

    red @talking2mouth "What does that... what does that {i}mean{/i}? 'Shut the doors to their heart?'"

    wes @sad "They can no longer form happy memories. They cannot think positively of another living being. Their basest instinct, joy through battle, is closed to them--yet fighting becomes all they are good for."
    wes @sadbrow talking2mouth "With time, they even forget what memories and bonds they possessed before the shadowification."

    skyla @sadbrow talking2mouth "That's awful! Who would do that?!"

    wes @talking2mouth "Cipher. They were evil incarnate. But I destroyed them. I destroyed them all. Every last peon. Every last laboratory. Every last candy bar in every last vending machine in every last cafeteria."

    pause 1.0

    redmind @surprisedbrow frownmouth "It sounds like a joke, but he's saying it with such a straight face, I think he means it..."

    wes @talking2mouth "Rui, Espeon, Umbreon, and I returned Cipher to the sand it sprang from. Our strength could not be outmatched, when we worked together."
    wes @sad "I had dozens of Pokémon partners... now I have only Togetic left."

    wes @talking2mouth "But I do not take my weakness as an excuse to stop The Work. It is only temporary, after all."

    skyla @sadbrow talking2mouth "Every superhero has an arc where they lose their powers..."

    wes @talking2mouth "I came to Kobukan, because I heard reports that Shadow Pokémon have been seen here. Pokémon from Unova, Kalos, even Paldea. Cipher's technology--their cruelty--must have escaped with that last roach."
    wes @talking2mouth "If I still have a reason to breathe, it's to make sure that whatever brought it {i}into{/i} this region doesn't bring it back out."

    wes @talking2mouth "While I'm tracking down Cipher's remnants, though... there is a greater task for you."

    skyla @talking2mouth surprisedbrow "Yeah?"

    wes @talking2mouth "You must find and capture the Shadow Pokémon. They are suffering. I know of a way to purify them, back in Orre--that ally, at least, has not abandoned me--but my name and face is too well-known to my enemies."
    wes @angry "With you, Ru-- Huuro, as the eyes that pierce Shadow, your companion as the fist that may break it asunder, and I as the insurance it shall never again rise, we may yet save this region."
    wes @talking2mouth "This task, I charge you with."

    pause 1.0

    skyla @surprisedbrow talking2mouth "{size=30}Y-yeah. Okay.{/size}"

    pause 1.0

    skyla @angrybrow talking2mouth "Yes! Yes, I'll do it! We'll do it! We'll rescue all the Shadow Pokémon and make those monsters who are creating them pay!"

    wes "[ellipses]"
    wes @talkingmouth "And so a glimmer of hope pierces the shadow."
    wes -cloak @talkingmouth "You will need this."

    pause 2.0

    show wes surprisedbrow with dis

    skyla @surprised "Holy crap, you look so absolutely amazing! You've got a super-suit! An actual, real-life, 100%% genuine super-suit, and you use it to fight crime!"

    wes -surprisedbrow @closedbrow talkingmouth "It {i}does{/i} contain a number of 'gimmicks' I have found useful in my pursuit of The Work, yes."
    wes @talking2mouth "The most important is this machine affixed to my arm--the [bluecolor]Snag Machine.{/color}"

    pause 1.0

    wes @talkingmouth sadbrow "I stole it from a laboratory, leaving nothing but rubble in my wake... hmph. They got what they deserved. They wanted to use it for stealing Pokémon from good trainers. Unjust conduct gets just rewards."

    skyla @surprisedbrow frownmouth "[ellipses]"

    redmind @thinking "I think I just {i}heard{/i} Skyla's heartbeat go up by, like, thirty beats per minute."

    wes @talking2mouth "This device allows one to transform ordinary Poké Balls into Snag Balls, which can be used to capture Pokémon that are already captured."
    wes @angry "An unfortunate side-effect of Shadow Pokémon is that they, even invisibly, stand out. They are captured quickly, and used for their extreme skill in battle, even if the trainer is oblivious to the harm they're causing."
    wes @sadbrow talking2mouth "Though they very often are not."
    wes @talking2mouth "In cases such as these, being able to capture an opposing trainer's Pokémon is a necessity. {i}Explaining{/i} the necessity of it can come later--keeping the Pokémon safe and in good hands is your first priority."

    pause 1.0

    wes @talking2mouth "...It occurs to me that my gauntlet is perhaps a bit bulky for you or your companion's use, Skyla."

    skyla @sadbrow talking2mouth "Yeah, I, um, I think it's really cool, but I also think the other guys in my class would probably ask me what it is a bit too often, especially if you're trying to keep it secret."

    pause 1.0

    wes @closedbrow talking2mouth "...I can work on making a more discreet version. The version I have now is equipped with... well, as I said, 'gimmicks.'"
    wes @talking2mouth "Though I would recommend letting [first_name] use it, while you identify the Shadow Pokémon, and direct his actions."
    wes @sadbrow talking2mouth "This was an arrangement that worked well for Rui and I."

    skyla @talking2mouth "Oh."
    skyla @happy "Well, sure! Sure, I'm fine with that. He's got his friend-superpower, and I've got my eyes-superpower. We stay in our lanes."

    wes @surprisedbrow talking2mouth "Friend-superpower?"

    red @talking2mouth "It's kind of a long and complicated story. How much time do you have?"

    wes @sadbrow talking2mouth "Not enough. Though this is a curious addendum. It raises a question about purification I had not yet considered..."
    wes @closedbrow talking2mouth "We will stay in communication. Keep an eye on the night sky. I'll alert you when I have made the necessary modifications to my Snag Machine, and when I have your first target for you."

    skyla @surprisedbrow happymouth "Oh my god, we get {i}targets{/i}? You're assigning us targets, like mission control?"

    wes @talking2mouth "I will, yes."

    skyla @happy "This is even cooler than what Gardenia is having us do!"

    pause 1.5

    wes @talking2mouth "...I thank you. As will Kobukan."

    pause 1.0

    wes @sadbrow talking2mouth "Huuro, may [first_name] and I have a word in private?"

    skyla @talking2mouth "Oh? Uh, sure. I'll just... go over here."

    show wes:
        ypos 1.0
        ease 0.5 ypos 1.2 zoom 1.3

    narrator "Wes looks at you closely, and carefully."

    wes @talking2mouth "If the Shadowseer trusts you, then I must also trust you."

    pause 1.0

    red @talking2mouth "But you don't?"

    wes @talking2mouth "I wonder if you understand the tremendous responsibility Skyla has been saddled with."

    red @unamusedbrow talking2mouth "I {i}definitely{/i} do not."

    wes "[ellipses]{nw}"
    extend @talking2mouth "There is time to learn. Not much. But, perhaps, enough."

    wes @talking2mouth "As the Shadowseer's Shadowhunter, it will be your duty to protect her. To preserve her. Save her, even at cost to yourself."

    pause 1.0

    red @talking2mouth "Shadowhunter? Is that who I am, now?"

    wes @talking2mouth "Remember, The Work cannot be done without her. We are disposable--any man can wear a glove and throw a Poké Ball. {i}She{/i} is not, for eyes and heart like her come once in a lifetime." 
    wes @sadbrow talking2mouth "Perhaps this is a sign I am already dead, that I have encountered two..."
    wes @talking2mouth "I failed to protect my Shadowseer. You must not. You will not."

    red @talking2mouth "I'll keep her safe. From Shadow Pokémon, from herself, and, if I need to, from you."

    wes @talking2mouth "[ellipses]I will say that I have more trust for you than it appears you do for me."

    show wes:
        ypos 1.2 zoom 1.3
        ease 0.5 zoom 1.0 ypos 1.0

    wes @talking2mouth "Shadowseer, we are finished."

    skyla @surprisedbrow talking2mouth "Wait, Shadowseer? Is that--is that me? Is that my hero name?!"

    red @talking2mouth "{size=30}Yeah, apparently I'm Shadowhunter.{/size}"

    wes @closedbrow smilemouth "Hmph."
    wes @closedbrow talkingmouth "I would venture a guess that your 'hero name' is Skyla Huuro."
    wes @talkingmouth "Goodnight, warriors of light. I appreciate your alliance. Together, we will rescue everyone man and Pokémon--purge the shadows from this land--and, perhaps, remove the need for The Work to continue."

    pause 0.5

    wes @talkingmouth "Untold billions are counting on me, whether they know it or not."
    wes @talking2mouth "And I am counting on you."

    hide wes with Dissolve(3.0)

    narrator "A dramatic turn of events! Wenceslaus of Nojave, a former hero, has tasked Skyla and [first_name] [last_name] with the rescue of Shadow Pokémon! Will they prevail? Or are they doomed to fail? Find out--"

    red @talking2mouth "Seriously, Skyla, cut that out."

    skyla @winkbrow talkingmouth "Don't be boring, [bluecolor]Shadowhunter{/color}."

    red @upeyes talkingmouth "I am {i}not{/i} calling you Shadowseer."

    skyla @angrybrow talkingmouth "Boo!"

    $ RelationshipRankUp("Skyla", "Shadowhunter", 2)

    return