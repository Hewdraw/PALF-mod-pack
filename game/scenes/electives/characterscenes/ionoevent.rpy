label ionoevent:

if (IsAbsent("Iono", location.title()) or HasEvent("Iono", "ClassIntro")):
    return

$ AddEvent("Iono", "ClassIntro")

narrator "The absolute {i}instant{/i} you step into the classroom..."

show iono uniform nocoat surprisedbrow with vpunch

iono "[first_name]!"

red uniform @happy "Hey, good to see you here."

iono sadbrow frownmouth @sadbrow talking2mouth "I'm freaking out. Freak-out levels are critical. Hull is damaged, shields are at 10%%. Normal students don't freak out, right? I'm about to blow it--about to go 'pop', like an Electrode!"

red @upeyes frownmouth "Hm[ellipses]"
red @talking2mouth "I think they do, actually. Freak out, I mean. What are you freaking out about, though?"

if (GetEventDatetime("Iono", "Iono1") == calDate + datetime.timedelta(days=-1)):
    iono @talking2mouth "This is my first time actually showin' up at [location.title()]-type class. I don't know what to say to the Instructor."

else:
    iono @talking2mouth "I need to figure out a way to explain why I was absent from class for so long. I just[ellipses] don't know how to answer, and I was tryin' to avoid it, but[ellipses]"

$ instructor = altclasstaught[location.title()]

if (IsNamed(instructor)):
    red @closedbrow talking2mouth "Just tell [instructor] what you told Professor Cherry. You transferred in late. Any other explanation would just be overly-complicated, right?"
else:
    $ BecomeNamed(instructor)
    red @closedbrow talking2mouth "Just tell the instructor what you told Professor Cherry. You transferred in late. Any other explanation would just be overly-complicated, right?"

iono @angrybrow talking2mouth "But what if [instructor] asks how I already know all the material that was covered in class?"

red @talking2mouth "Well, you're a Champion and Gym Leader, so[ellipses] you can probably just say you learned it at Naranjuva, and no-one will question you."

pause 1.0

iono @talking2mouth "I don't want to be told my catastrophizing isn't valid, I want unquestioning agreement, and to be told that it's probably even worse than I imagined."

#there are some classes where this won't work, because the professor arrives later, as part of the actual scene. 
#I don't think we need to create, like, a variable, just to track that, though, because that's a _ton_ of effort for a _very_ small consistency update. 
#We'll just address any reports people make. 
#Fair enough -- but if you wanted, I could very easily note down which Ghost & Electric classes have the instructor arrive later. You could just reference them by number? BUT - only if you think it's worthwhile; I don't want to waste your time.

red @happy "Sorry. That's not how I work. Now, c'mon, let's go to the Instructor before class."

show iono surprised with dis:
    xpos 0.5 
    ease 0.5 xpos 0.33

iono "Wait, wait, wait, wait--!"

if (location == "electric"):
    show surge with dis:
        xpos 0.66

    surge @talking2mouth "You're in the wrong place, kid. The bimbos in Fairy class'll fix your damn haircut."

    iono @happybrow talking2mouth "H-hi! I just, uh, I just wanted to, um, apologize for ghosting you and not showing up in class until now--"

    surge @talking2mouth "You're mistaking me for someone who has a goddamn clue who you are. The hell do I care if you show up?"
    
    iono @talking2mouth "Oh. Um, Iono, Sir. Gym Leader of the Levincia Gym and Paldean Champion."
    iono @happybrow happymouth "Supercharged Streamer and Content Creator extraordinaire! Happy to be here, Instructor Lieutenant Surge!"

    surge @talkingmouth "Well, well. Guess you're new around here. Lemme give you a li'l orientation."
    surge @happy "First off, I don't give a shit about your participation trophy. Your 'treasure hunt' sent you down the wrong rabbit hole, cupcake."
    surge @talkingmouth "In the real world, we play by {i}Unovan{/i} rules. You get what you earn--and so far you've earned a 'Z-minus-minus', on account of not showing up."
    surge @talkingmouth "'Course, this is Kobukan, so I'm not allowed to fail you yet."
    surge @happy "Try to keep up, and maybe someday you'll trade those Girl Scout ribbons for a {i}real{/i} badge. GAHAHAHAHAHAHA!"

    hide surge with dis

    pause 1.0

    iono disgustedbrow frownmouth @disgustedbrow disgustedmouth "{i}Wow{/i}. Literally {i}so{/i} not okay. I've been cancelled before for {i}way{/i} less."

    red @sadbrow talkingmouth "But was it as bad as it {i}could{/i} have been?"

    iono neutralbrow neutralmouth @closedbrow talking2mouth "Iunno. Could've been worse, I guess. I only lost, like, {i}two{/i} lives."

    hide iono with dis

else:#ghost
    show fantina with dis:
        xpos 0.66

    fantina @surprisedbrow talkingmouth "Oh? I am seeing new face, but not a strange one. You wish to speak with me?"

    if (GetEventDatetime("Iono", "Iono1") == calDate + datetime.timedelta(days=-1)):
        iono @happybrow talking2mouth "H-hi! I just, uh, I just wanted to, um, apologize for ghosting you and not showing up in class until now."

        fantina @happy "Ohohohoho! Fret not, {i}ma cherie{/i}--where better is place for 'ghosting'?" 
        fantina @surprisedbrow talking2mouth "But--tell me, dear. For why am I feeling {i}déjà vu?{/i} Perhaps our paths have crossed, in another life?"

        iono @talking2mouth "Oh. Um, my name's Iono, and I'm the Gym Leader of the Levincia Gym. And um, a Champion."

        fantina @talkingmouth "Oh~? So young, and so very impressive! But our neighbors have no short of Champions. Surely I do not know them all?"

        iono @happybrow happymouth "Well, I'm also the Supercharged Streamer, catcher of eyeballs in my Electroweb!"

        fantina @happy "Aaahh, {i}très bien{/i}! Performance, then, is no stranger!"
        fantina @talkingmouth "A strong foundation, perhaps, on up to build toward contests? We will have much to discuss!"

    else:
        iono @happybrow talking2mouth "H-hi! I just, uh, I just wanted to, um, apologize for ghosting you and not showing up in class a bunch at the beginning of the year."

        fantina @talkingmouth "Nothing to worry, Miss Iono! I am merely curious, not blameful."
        fantina @happy "After all, are you not the ninety-fourth Champion of Paldea? The Plucker of Eyeballs in your Electroweb?"
        fantina @talkingmouth "Surely, what reason kept us apart must be good: I, too, know the price of fame."
        fantina @happy "{i}En plus{/i}, I sense you have always been here... in spirit! Ohohohohoho~!"

        iono @sadbrow talkingmouth "Thanks, Instructrice Fantina. You're a lot more reasonable than Instructor Surge was[ellipses]"
        iono @sad2eyes talking2mouth "He kinda just made fun of me when I tried to apologize to {i}him{/i}. And he said Paldea wasn't a {i}real{/i} league[ellipses]"

        fantina @angry "I have no surprise, {i}ma voisine{/i}. The good Lieutenant's world is small, and his mind smaller."

        iono @talking2mouth "And it's so frustrating, because I don't really understand Japanese, but almost everyone here speaks it--but since Instructor Surge refuses to speak in {i}anything{/i} but English, I thought he'd at least back me up!"
        iono @rolleyes talking2mouth "He's making me grow a spine and I {i}hate{/i} it."

        fantina @surprised "Oh? But your English--its sound is very smooth! Surely it will be small problem?"
        fantina @sadbrow talkingmouth "Four years have I spent in Galar and Kobukan--and still my words fall short."
        fantina @angry "And the spelling! {i}Ça me rend fou!{/i}"

    redmind @closedbrow smilemouth "[ellipses]There. That wasn't not so bad, is it?"

    narrator "The conversation between the two seems like it might go on for a while[ellipses] you go back to your seat."

    hide fantina
    hide iono
    with dis

return