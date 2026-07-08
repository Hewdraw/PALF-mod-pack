label lunchscenequeue:

label SilverLunchScene:
    if (EventAvailable("Silver", "RocketReboots", 3)):
        show silver uniform with dis

        pause 1.0

        red uniform @talkingmouth "Hey, red."

        silver @angrybrow talking2mouth "What the hell do you want?"

        pause 1.0

        silver @sadbrow talking2mouth "Sorry, red."

        red @sadbrow talkingmouth "I know you're working on it."
        red @happy "Anyway, when we were talking with [duplica_name], you mentioned there had been a few Rocket resurrection attempts."

        silver @talking2mouth "Too many, but keep your voice down. It's damn impossible to hear anything in this cafeteria, but we don't want to be careless."

        red @sadbrow talkingmouth "{size=30}Right.{/size} What can you tell me about them? There were four, right?"

        silver @closedbrow talking2mouth "Yeah."

        silver @talking2mouth "The first was Team Neo Rocket. If any attempt was going to succeed, it would've been them. After Kanto's Rocket disbanded, a bunch of the guys in Johto refused to believe it."
        silver @sadbrow talkingmouth "They thought Giovanni was being... {i}coerced{/i}, or it was a false flag, or something. They took a bunch of guys, the ones left over, recruited some of the Rockets left in Kanto, and tried to take over Johto."
        silver @closedbrow talking2mouth "In all fairness to them, they {i}did{/i} manage to take over the Goldenrod Radio Tower. They broadcast a nationwide announcement saying they'd taken over Johto for Giovanni, and asked him to come back."

        pause 2.0

        red @talking2mouth "I guess he didn't."

        silver @sadbrow talkingmouth "All that just to place a phone call that wasn't picked up."

        red @confused "Why did they need {i}him{/i}, though? Why not just... run the region themselves?"

        silver "[ellipses]"
        silver @talking2mouth "It's like I said with The Copycat. Rocket is {i}defined{/i} by its lack of imagination. All they can think of doing is the same thing they've always done. Steal. Hurt. Profit."
        silver @sadbrow talking2mouth "Without a strong leader like Giovanni[ellipses] they have no direction."

        pause 1.0

        silver @closedbrow talking2mouth "Well, enough direction to take over a region, but not enough to do anything with it once they did."

        pause 2.0

        silver @talking2mouth "Anyway, that was the only revival attempt that might have, in some alternate universe, succeeded. Everything else was just... dumb as hell."

        pause 1.0

        silver @closedbrow talking2mouth "Team GO Rocket thought that there was some kind of special 'Shadow' Pokémon out there that could give them the strength they needed to come back." 
        silver @talking2mouth "They went to Orre, looking for these Pokémon, met up with another group of criminals--Silence, or something--and[ellipses] disappeared. We lost contact with them. Guess {i}someone{/i} stopped 'em."

        pause 1.0

        silver @closedbrow talking2mouth "Team Great Rocket is when we started getting {i}really{/i} pathetic about it. They took over a small island West of Galar. Holed up in an old castle there." 
        silver @talkingmouth "An international card game tournament was in the area, and they intended to use those high-level players as hostages while they built up money and manpower."
        silver @sadbrow talkingmouth "Turns out being a goddamn nerd doesn't mean you're weak. The players fought off Team Great Rocket. When one of their executives turned out to be a mole, that was the last straw, and the 'King' of Great Rocket surrendered." 
        silver @talkingmouth "Guess the players enjoyed themselves--they hold 'mock invasion' events every couple years. Visited a couple times."

        red @sadbrow talkingmouth "And... Rainbow Rocket?"

        silver @angrybrow "[ellipses]"
        silver @talking2mouth "I should find this one funny, but I don't."
        silver @angrybrow talking2mouth "Someone pretending to be Giovanni showed up on TV, claiming he and his 'Team Rainbow Rocket' were now in possession of the Aether Foundation facility."

        pause 1.0

        silver @sadbrow talking2mouth "'Course, that was the last thing we heard from him. The news said that he and his executives--a bunch of schizophrenics who thought they were famous criminals--were beaten by a champion-level trainer and arrested."

        red @surprised "Woah! Who was that trainer?"

        silver @closedbrow talking2mouth "Beats me. Beats Alola, too, I guess, because they started the Alolan league just six months later. Guess they realized they couldn't rely on a mysterious 'somebody' dropping in to save them next time."

        red @sadbrow talkingmouth "Well[ellipses] if Team Rainbow Rocket was just a bunch of crazy people, does that count as a {i}real{/i} revival attempt?"

        silver @talking2mouth "It did for the grunts who left to follow that fake Giovanni. I lost a lot of guys to that impostor."

        pause 1.0

        silver @closedbrow talking2mouth "Anyway, you get why I say that {i}any{/i} attempt to bring back Rocket is going to fail, right?"

        red @sadbrow talkingmouth "Hearing your reasoning... yeah, it's pretty impossible to argue with."

        silver @talking2mouth "[ellipses]Yeah."

        pause 0.5

        silver @sadbrow talking2mouth "But a lot of people still do."

        $ ValueChange("Silver", 1, 0.5)

        silver @closedbrow talkingmouth "Thanks for not saying it's my destiny, or my duty, to try again, or whatever."

        red @confused "What? I'd never say that."

        silver @talkingmouth "Yeah, and that makes you different."
        silver @talking2mouth "Which, uh, I appreciate."

        red @happy "Buddy? Raise your standards. Right now, they're underground."

        silver @closedbrow smilemouth "Hmph."

        hide silver with dis

        return

label GrushaLunchScene:
    if (EventAvailable("Grusha", "LunchScene", 1)):
        show grusha uniform with dis

        grusha @closedbrow "Hmm[ellipses]"

        red uniform @talking2mouth "Hey, Grusha. You look like you're deep in thought?"

        grusha @talkingmouth "[first_name]. {i}Hola, amigo{/i}. Yeah, trying to figure out what to eat."

        red @confused "Where's the Little Prince?"

        grusha @talking2mouth "Got a bowl of warm water back in my dorm. Go there between classes to switch it out."
        grusha @sad2brow talking2mouth "{size=30}Just between you and me, I think I caught one of my roommates trying to sit on him. I'm starting to think there's something off about her.{/size}"

        red @happy "You're really taking care of him, aren't you?"

        grusha @sadbrow talkingmouth "Doing the best I can. I got a full life before I cracked like an egg. {i}Huevito{/i} should have the same chance, no?"

        red @sadbrow talkingmouth "You're a good guy, Grusha."

        grusha @closedbrow talking2mouth "Eh. Do my best."
        grusha @talking2mouth "Whenever I'm carrying him, or moving him, or... replacing his water... I pay a lot more attention to the world around me. I need to make sure I don't trip, or bump into something, you know? He could fall."
        grusha @sad2eyes talking2mouth "Even when he's not around, I'm keeping an eye out for safe places to bring him, making sure I don't injure myself, so I can go back to him for his water-change..."
        grusha @talking2mouth "The world seems a bit more colorful with him around. Sharper edges. Brighter hues. I'm just noticing it more, though."

        pause 2.0

        grusha @closedbrow talking2mouth "[ellipses]Is it weird that after this conversation, I kinda want eggs?"

        red @sadbrow talkingmouth "Maybe a little bit, but I won't tell him if you don't."

        $ ValueChange("Grusha", 1)

        grusha @winkbrow talkingmouth "I'll hold you to that."

        hide grusha with dis

        return

label ErikaBadMoodLunchScene:
    if (GetMood("Erika") < 0 and GetNature("Erika") == TrainerNature.Distant and HasEvent("Gardenia", "OpenMarket") and EventAvailable("Gardenia", "ErikaBadMoodLunchScene")):
        $ removelunchstudents = removelunchstudents | { "Gardenia", "Erika" }
        
        show erika uniform happybrow happymouth with dis

        pause 1.0

        show erika uniform surprisedbrow frownmouth with dis

        erika sadbrow frownmouth @talking2mouth "Oh. I beg your pardon."

        hide erika with dis

        red uniform @confused "Huh? Sorry, did I miss something?"

        redmind @thinking "That was weird. Erika's usually a bit tense around me, but this time it looked like[ellipses] she was actively avoiding me."
        redmind @thinking "I know it's none of my business, but[ellipses]"

        show gardenia uniform:
            xpos 1.2 
            ease 0.5 xpos 0.75

        gardenia @talkingmouth "Heya, Partner."

        red @surprised "What?! I didn't even say it out loud this time!"

        show gardenia uniform:
            xpos 0.75
            ease 0.5 xpos 0.5

        gardenia @happy "You didn't need to. My business instincts run deep--seriously deep."

        pause 1.0

        red @talking2mouth unamusedbrow "Okay, I'm going to ask flat-out. Are you an Esper?"

        gardenia @talkingmouth "Nope! Think I'd be able to make half as many deals as I do if I was? People'd turn me away because they'd think I was pulling one over on them."
        gardenia @happy "Just got really good instincts, partner."
        gardenia @talkingmouth "And what my instincts are telling {i}me{/i} is that you're worried about Erika."

        menu:
            "I really don't care about her at all.":
                $ AddEvent("Gardenia", "ErikaLunchSceneDontCare")
                show gardenia uniform surprisedbrow frownmouth with dis

                pause 0.5

                gardenia -surprisedbrow -frownmouth @talking2mouth sadbrow "Oh. Well, uh, I guess we can't always get to the handshake."
                gardenia @talking2mouth "Still, you should try to think from a bit higher of an angle."
                gardenia @talking2mouth "Maybe you don't care about Erika, but I bet you care about what she can make happen--or, if sticks are more of a motivator than carrots, what letting her stay in that funk might cause."

                red @confused "I really didn't think {i}you{/i} were the person who'd go to bat for Erika."

                gardenia @talking2mouth rollbrow "I didn't either, but spending an hour a day with her in our Grass-elective class kinda made me see her a bit differently."

                gardenia surprisedbrow frownmouth @happybrow talkingmouth "At least listen to why I think you {i}should{/i} care about her--at least a little bit, alright?"

                red @closedbrow talking2mouth "Alright, but go into this with the understanding she tried to get me kicked from the Battle Team, and also told me to drop out of Kobukan {i}right{/i} after the Student Council elections."
                red @sad2eyes angryeyebrows talking2mouth "Like, literally {i}immediately{/i} after."
                red @sad2brow talking2mouth "{size=30}I hadn't even left the auditorium.{/size}"

                gardenia @talking2mouth "Oh.{w=1.0} Oh my god, I'm sorry. I had no idea. I thought you guys were just a bit rough because she's filthy rich and you're[ellipses] not."

                red @upeyes sadeyebrows talkingmouth "{i}Everyone{/i} in this school is filthy rich, by my standards."
                red @sadbrow sweat talkingmouth "That wouldn't make me dislike someone. And for what it's worth, I don't think me being poor is what makes her dislike me."

                gardenia sadbrow -frownmouth @talking2mouth "Well[ellipses] I guess, since that's your relationship[ellipses] maybe you don't need to hear my spiel after all."

                menu:
                    "Yeah, I don't.":
                        gardenia @talkingmouth "Right. Um[ellipses] sorry, partner."

                        hide gardenia with Dissolve(1.0)

                        narrator "Gardenia wanders away awkwardly."

                        return

                    "Nah, go ahead.":
                        show gardenia -sadbrow with dis 

                        gardenia @talkingmouth "Hey. That's big of you, you know."

                        red @happy "Gas me up like that and I'll get a big head."

            "Maybe a tiny bit.":
                $ AddEvent("Gardenia", "ErikaLunchSceneTinyCare")

                gardenia -happy @happy "Knew it! Well, then, partner, you're in luck."

            "Moreso confused. She seems to be in a {i}really{/i} bad mood.":
                $ AddEvent("Gardenia", "ErikaLunchSceneConfused")

                gardenia @talkingmouth "I can work with that. And if that's the deal, I've got some good news for you!"

        gardenia @talking2mouth "So, here's the thing. Erika is really easily influenced. That can be a good thing, but also a bad thing, depending on which way the wind blows her."
        gardenia @talkingmouth "It's like Newton's first law of motion. An Erika in motion stays in motion, unless acted on by an outside force."

        red @sweat talking2mouth "And if she's heading down, then[ellipses]"

        gardenia @sadbrow talking2mouth "She'll keep heading down. That's right."
        gardenia @talkingmouth "But the thing is, it's not just {i}her{/i} that'll head down. If she's in a bad mood, she'll probably be less willing to go out and do fun things, or talk to other people."
        gardenia @happy "I mean, she's not just going to stay indoors and watch the cooking channel all day, but she probably isn't going to be part of any big happenings around campus! 'Cept mandatory ones, of course."
        gardenia @talkingmouth "But there's more consequences to this than just having Erika closed-off to you. Erika's got other friends."
        gardenia @talkingmouth "They might want to talk with her, or do something with her, but if she's moping in her room, they might never get the chance."
        gardenia @talking2mouth "Who knows? Maybe the conversation those two other students would have had would have helped you in some way, or led to something else down the road that {i}would{/i} directly affect you."

        narrator "In game terms, [bluecolor]characters who are in bad moods will not be able to show up for some events. If a character is mandatory for an event, and the character is in a bad mood, the event will likely not happen!{/color}"
        narrator "[bluecolor]The event will almost never be permanently missable, though--as soon as all the criteria for the event are fulfilled, the event will trigger in the first available timeslot.{/color}"
        narrator "It's in your best interest to keep as many characters in a positive mood as possible!"

        red @unamusedbrow unamusedmouth "[ellipses]"

        gardenia @surprised "What? What's that look for?"

        red @talking2mouth unamusedbrow "You've convinced me there's a problem. Now, I assume, you're going to sell me the solution?"

        gardenia @happy blush "Heh heh! Am I that obvious?"

        red @closedbrow talking2mouth "How much is it?"

        gardenia @talkingmouth "Hold on. I'm not going to say there's a single thing you can do to get back in the black. Even I have to acknowledge you can't just buy someone's feelings."
        gardenia @happybrow smirkmouth "You're going to want to practice a long-term investment strategy."
        gardenia @talkingmouth "This can include spending time with her in classes, seeking her out outside of classes, studying with her at lunch, or[ellipses]"

        redmind @closedbrow sweat "{i}Here{/i} we go."

        gardenia @talkingmouth "Gifting her a few choice items, only {i}some{/i} of which can be found in Gardenia's modern antiques collection, available by investing in my market!"

        red @talking2mouth "Yeah? You know of a gift that'll really knock her diamond-encrusted, silk socks off?"

        gardenia @talkingmouth "I sure do. She takes Grass and Poison classes, so, like every student, she'll like gifts that help her find or train Pokémon of those types. But, outside of that universal law of gift-lovin', she's got a secret vice."

        red @talkingmouth "Uh-huh?"

        show gardenia flirtbrow with dis:
            xpos 0.5 ypos 1.0 zoom 1.0
            ease 0.5 ypos 1.1 zoom 1.2

        gardenia @smirkmouth "Teacups."

        red @confused "You're shitting me."

        gardenia @happy "I'm sure as shit, actually!"

        show gardenia -flirtbrow with dis:
            xpos 0.5 ypos 1.1 zoom 1.2
            ease 0.5 ypos 1.0 zoom 1.0

        gardenia @talkingmouth "Seriously, the girl goes gaga for teacups. Doesn't matter how unremarkable they are, she'll put them in a little glass cabinet in her room and proudly show 'em off to anyone who comes over. She can't get enough of them!"
        gardenia @talkingmouth "And if you give her a teacup that's a real masterpiece? Better watch out! You might find the Tamamushi fortune shoved in your back pocket when you wake up the next day!"
        gardenia @happy "Of course, you'd probably {i}need{/i} that fortune to buy one of those fancy-schmancy teacups in the first place."

        red @talking2mouth "I'll[ellipses] keep that in mind."

        if (investment < 6000):
            gardenia @talkingmouth "Once you've invested, say, $6,000 in my market, I think I could probably start selling them to you... and then it's easy street to being Erika's best friend."
        else:
            gardenia @talkingmouth "Buy one every once in a while, then it's easy street to being Erika's best friend."

        gardenia @happy "I bet once you hang out with her a bit--you know, get a chance to {i}really{/i} talk with her--she'll warm up to you. Easily influenced, you know? That can be a good thing, if you want."

        red @talking2mouth "[ellipses]You know, I used to think that advertising doesn't work on me."

        gardenia @talkingmouth flirtbrow "{i}Everyone{/i} thinks that. The fact you said you 'used to' means you're ahead of the curve."
        gardenia @happy "Pleasure doing business with you!"

        hide gardenia with dis

        return

label SabrinaBadMoodLunchScene:
    if (GetMood("Sabrina") < 0 and GetNature("Sabrina") == TrainerNature.Distant and EventAvailable("Nessa", "SabrinaBadMoodLunchScene")):
        $ removelunchstudents = removelunchstudents | { "Nessa", "Sabrina" }

        show nessa uniform with dis

        nessa @talkingmouth "Hey."

        red uniform @talkingmouth "Oh, hey, Nessa. What's up?"

        nessa @talkingmouth "What's going on between you and Sabrina?"

        red @surprisedbrow frownmouth "[ellipses]"
        red @talking2mouth "Uh[ellipses] nothing, to my knowledge. Why not ask Rosa?"

        nessa @talkingmouth "She's been in a bad mood for a while now. Sabrina, I mean, not Rosa." 
        nessa @closedbrow talkingmouth "Sabrina gets teed off if we think about her, so I didn't want to drag Rosa into this. I figured you'd be the second-best person to ask."

        red @wince talking2mouth "[ellipses]I mean, she'll still know that you're asking about her, right?"

        nessa @talkingmouth "Yeah. But she won't take it out on Rosa."

        red @unamusedbrow talking2mouth "But you're fine with her taking it out on me?"

        nessa @talking2mouth "You're a big, strong, man. You can take it."

        red @upeyes angryeyebrows poutmouth "[ellipses]"
        red @confused "Well, like I said, if there {i}is{/i} something going on between us, I don't know what it is."

        nessa @closedbrow talkingmouth "Yeah, I guess it's not your problem."
        nessa @talkingmouth "Not that Sab's a {i}problem{/i}, of course, but[ellipses]"
        nessa @talking2mouth "Maybe you should try to hang out with her a bit more? Just between you, me, and Sabrina, she seems to like your company. Even if she doesn't show it."

        red @confused "Huh? Where are you getting that from?"

        nessa @sadbrow talking2mouth "Well, Rosa's kinda her best friend right now, but Rosa is very[ellipses] high-energy. Talking with her requires investment. You're a bit more mellow--I think Sabrina likes relaxing around you."

        red @happy "If we're talking about mellow, aren't you the queen of it? I mean, you're like a walking Zen garden."

        nessa @talking2mouth closedbrow "Hah. I'm trying, too, don't worry. Couldn't let Rosa handle this alone."
        
        pause 0.5

        nessa @sadbrow talking2mouth "And[ellipses] well, I guess I care about her a little. More than just as a dormmate, or as Rosa's friend. I also want her to be my friend. Only so long I can tolerate Raihan, you know?"
        nessa @talkingmouth sadbrow "I don't like seeing her moping around in her room. There are a lot of people who want to talk to her, and things she could be doing, but if she's in a bad mood, she'll probably just stay in her room and[ellipses]"
        nessa @talkingmouth "Anyway, bad moods lead to missed opportunities. Staying indoors all day is a whatever choice, as long as it's {i}actually{/i} a choice."

        narrator "In game terms, [bluecolor]characters who are in bad moods will not be able to show up for some events. If a character is mandatory for an event, and the character is in a bad mood, the event will likely not happen!{/color}"
        narrator "[bluecolor]The event will almost never be permanently missable, though--as soon as all the criteria for the event are fulfilled, the event will trigger in the first available timeslot.{/color}"
        narrator "It's in your best interest to keep as many characters in a positive mood as possible!"

        red @talkingmouth "I getcha. I'll try to hang out with her more."

        nessa @talkingmouth "And if all else fails, you can always try to give her a gift." 
        nessa @talking2mouth "She trains Psychic-type and Ghost-type Pokémon, so maybe something that helps her find or train them."
        nessa @sadbrow talking2mouth "Oh, but, word of warning: don't give her books. I made that mistake. I thought she hung out around the library because she liked reading--turns out she hangs out there because no-one else does."
        
        red @talking2mouth "No books, huh? Alright. Thanks for the heads-up."

        nessa @talkingmouth "No problem. See you later. Hope Sabrina doesn't get too mad at us for talking about her."

        red @wince talking2mouth "Yeah, me too."

        hide nessa with dis

        if (IsContacted("Sabrina")):
            pause 2.0

            redmind @sadbrow "Sabrina?"

            redmind @wince frownmouth "[sabrinacolor]I have nothing to say.{/color}"

        return

label KrisBadMoodLunchScene:
    if (GetMood("Professor Cherry") < 0 and GetNature("Professor Cherry") == TrainerNature.Distant and EventAvailable("Ethan", "KrisBadMoodLunchScene")):
        show ethan uniform with dis

        ethan @talkingmouth "Hey, [first_name]. Got a second?"

        red uniform @talkingmouth "Sure. What's up?"

        ethan @talking2mouth "It's Kris. Uh, Professor Cherry. She's been kinda cranky recently. I think the stress of teaching at Kobukan is getting to her."

        red @sadbrow talkingmouth "Oh, man. Yeah, being a student here is hard enough. I can't imagine what it's like to be a professor."

        ethan @talking2mouth "Anyway, I was hoping you might be able to help her out a bit."

        red @confused "Me? How? She's your professor. And, you know, your babysitter."

        ethan @closedbrow talking2mouth "Yeah, but that's the problem. She sees me as too much of a kid--{i}her{/i} kid, you know? Always putting on the smiley face, even when it'd probably be better for her to just yell and rant for a bit."

        red @talking2mouth "I don't know, man. I don't really know a ton about her. And I'm not sure it's[ellipses] well, {i}appropriate{/i} for me to try to help her out."

        ethan @talkingmouth "I get that. And I'm not saying you should try to 'hang out' with her or anything. I mean, I get it, she's a professor."
        ethan @happy "Just let her be a professor, that'll cheer her right up. You could sit at her table at lunch, or ask her to tutor you--I know she really loves that."

        ethan @closedbrow talking2mouth "Or, just between you and me, giving her a gift is pretty much a cheat code. She goes crazy for research papers, old electronics, software--you know, nerd stuff."

        red @confused "Aren't you a nerd, too?"

        ethan @talkingmouth "Yeah, but I'm not a smart nerd, like she is. I'm a 'media' nerd. You know, the kind who can recite the entire plot of every video game I've ever played (and most I haven't), but couldn't give you directions to the nearest Poké Mart."

        red @closedbrow talkingmouth "Alright, man. I'll keep it in mind--if I see a chance to help her out without getting too personal, I'll do it."

        ethan @talkingmouth "Thanks, man. And, y'know, it's not {i}just{/i} for her. Being a professor, she's got a lot of responsibilities. If she's in a bad mood, she might not be able to help you, or her other students, out as much as she could if she was doing fine."

        narrator "In game terms, [bluecolor]characters who are in bad moods will not be able to show up for some events. If a character is mandatory for an event, and the character is in a bad mood, the event will likely not happen!{/color}"
        narrator "[bluecolor]The event will almost never be permanently missable, though--as soon as all the criteria for the event are fulfilled, the event will trigger in the first available timeslot.{/color}"
        narrator "It's in your best interest to keep as many characters in a positive mood as possible!"

        ethan @talking2mouth "Yeah, the narrator got what I was going for. Anyway, thanks for helping."

        red @confused sweat "N-no problem[ellipses]?"

        hide ethan with dis

        return

label IonoBadMoodLunchScene:
    if (GetMood("Iono") < 0 and GetNature("Iono") == TrainerNature.Distant and HasEvent("Rosa", "RosaSabrinaNightScene") and GetEventDatetime("Rosa", "RosaSabrinaNightScene") + datetime.timedelta(days=2) < calDate and EventAvailable("Rosa", "IonoBadMoodLunchScene")):
        $ removelunchstudents = removelunchstudents | { "Iono", "Rosa" }
        
        show rosa uniform with dis

        rosa @talkingmouth "Heya, [first_name]! Mind if I ask you a favor?"

        red uniform @talking2mouth "Huh? Sure. What is it?"

        rosa @sadbrow talkingmouth "Could you hang out with Iono a bit more? She's been in a bad mood for a while now, and I think she could use a friend." 
        rosa surprisedbrow frownmouth @wince talking2mouth "I know you're, um, really important to her, and Sabrina and Iono are arguing a lot, and it's kinda driving me crazy having to keep those two away from each other's throats."

        red @talking2mouth "Sure? What do you mean by a bad mood, though? She's[ellipses] I mean, her bad moods usually last for, like, a single textbox."
        
        pause 1.0

        red @wince talking2mouth "Great, now {i}I'm{/i} doing it."

        rosa -surprisedbrow -frownmouth @talkingmouth "Well, I don't know about that, but I know she's kinda retreating into herself right now. She's not, um, spending time with other people as much, and she's skipping some events--even a couple classes."
        
        narrator "In game terms, [bluecolor]characters who are in bad moods will not be able to show up for some events. If a character is mandatory for an event, and the character is in a bad mood, the event will likely not happen!{/color}"
        narrator "[bluecolor]The event will almost never be permanently missable, though--as soon as all the criteria for the event are fulfilled, the event will trigger in the first available timeslot.{/color}"
        narrator "It's in your best interest to keep as many characters in a positive mood as possible!"
        
        rosa @happy "I think she just needs a little reminder that she's got friends in this school, and I know you're one of 'em."

        red @talkingmouth "Alright. I'll see if I can find some time to hang out with her."

        rosa @talkingmouth "Thanks, [first_name]."
        rosa @talking2mouth "And[ellipses] just in case just 'hanging out' doesn't work--she's been not-so-subtly hinting she'd like some new software or hardware for her computers." 
        rosa @talkingmouth "If you could get her something mechanical--machines or software--I think she'd be really appreciative."

        red @happy "Noted. I'll keep that in mind."
        
        rosa @talkingmouth "Awesome! Thanks for your support. See you later, then!"

        hide rosa with dis

        return

label BlueBadMoodLunchScene:
    if (GetMood("Blue") < 0 and GetNature("Blue") == TrainerNature.Distant and EventAvailable("Leaf", "BlueBadMoodLunchScene")):
        $ removelunchstudents = removelunchstudents | { "Blue", "Leaf" }

        show leaf uniform with dis

        leaf @talkingmouth "Hey, Skippy. I've got a mission for you."

        red @talking2mouth "Lay it on me."

        leaf @talking2mouth "It's Blue. He's being a dick again."

        red @closedbrow talking2mouth "Yeah, he's been in a bad mood recently."

        leaf @talking2mouth "Could you do something about that?"

        pause 1.0

        red @confused "You're smiling like you don't realize how insane that sounds."

        leaf @talkingmouth closedbrow "You do the insane every day. You can handle it."

        red @wince talking2mouth "I guess, but[ellipses]"

        leaf @sadbrow talkingmouth "C'mon, at least do it for me and our other dormies! With him being in a bad mood, it's driving the rest of us crazy, too."
        leaf @closedbrow talking2mouth "If we're busy arguing with him over stupid stuff, then we can't show up to {i}our{/i} commitments, and it's just a huge pain all around."

        narrator "In game terms, [bluecolor]characters who are in bad moods will not be able to show up for some events. If a character is mandatory for an event, and the character is in a bad mood, the event will likely not happen!{/color}"
        narrator "[bluecolor]The event will almost never be permanently missable, though--as soon as all the criteria for the event are fulfilled, the event will trigger in the first available timeslot.{/color}"
        narrator "It's in your best interest to keep as many characters in a positive mood as possible!"

        pause 1.0

        red @closedbrow talking2mouth "I'll see what I can do, but make absolutely {i}no{/i} promises."

        leaf happy "Thanks, Skippy! I'm {cps=*0.5}coooounting{/cps} on {cps=*0.5}yooooou!{/cps}~"

        hide leaf with dis

        return

#no need for generic dialog for this--just go directly to PickTable

return