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
        silver @talkingmouth "Guess the players enjoyed themselves--they hold 'mock invasion' events every couple years. Visited a couple times. Picked up a bit of an accent."

        red @sadbrowt talkingmouth "And... Rainbow Rocket?"

        silver @angrybrow "[ellipses]"
        silver @talking2mouth "I should find this one funny, but I don't."
        silver @angrybrow talking2mouth "Someone pretending to be Giovanni showed up on TV, claiming he and his 'Team Rainbow Rocket' were now in possession of the Aether Foundation facility."

        pause 1.0

        silver @sadbrow talking2mouth "'Course, that was the last thing we heard from him. The news said that he and his executives--a bunch of schizophrenics who thought they were famous criminals--were beaten by a champion-level trainer and arrested."

        red @surprised "Woah! Who was that trainer?"

        silver @closedbrow talking2mouth "Beats me. Beats Alola, too, I guess, because they started the Alolan league just six months later. Guess they realized couldn't rely on a mysterious 'somebody' dropping in to save them next time."

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

#no need for generic dialog for this--just go directly to PickTable

return