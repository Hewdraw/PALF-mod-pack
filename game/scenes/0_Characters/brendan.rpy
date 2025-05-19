label Brendan1:
    scene concerthallback
    with Dissolve(2.0)
    stop music fadeout 1.5
    $ renpy.music.queue("Audio/Music/SoaringIllusions_Intro.ogg", channel='music', loop=None, tight=None)
    $ renpy.music.queue("Audio/Music/SoaringIllusions.ogg", channel='music', loop=True, tight=None)

    narrator "You're walking back to the main academy building when you hear something echoing from the Contest Coliseum."

    redmind @thonk "Hm? That sounds like Brendan's singing. What's he doing in there...?"

    scene blank2 with splitfade

    pause 1.0

    scene concerthallhallway with splitfade

    narrator "As you make your way through the winding, dusty, hallways of the Contest Coliseum--decrepit and unimpressive, despite its immense size--Brendan's voice echoes around you."

    show blank2 as blank2two with dis:
        alpha 0.5

    image songline1 = Text("Glory won in battle has a color pale",size=30,color="#fff")
    image songline2 = Text("For what artistry is there in what lacks power but to ail?",size=30,color="#fff")
    image songline3 = Text("In pursuit of power, unending, wholly mad",size=30,color="#fff")
    image songline4 = Text("A family's love, a son's respect, every glory that you had",size=30,color="#fff")
    image songline5 = Text("Was taken from you, victim, powerless to keep your grasp",size=30,color="#fff")
    image songline6 = Text("Dismissing love and art and beauty as burdens from the past",size=30,color="#fff")
    image songline7 = Text("I forgive you, father. I beg that you forgive",size=30,color="#fff")
    image songline8 = Text("for this descent into ambition",size=30,color="#fff")
    image songline9 = Text("is no damn way to live.",size=30,color="#fff")

    show songline1 with splitfadereverse:
        ypos 1/11 xalign 0.5 yanchor 0.5

    pause 1.5

    show songline2 with splitfadereverse:
        ypos 2/11 xalign 0.5 yanchor 0.5

    pause 1.5

    show songline3 with splitfadereverse:
        ypos 3/11 xalign 0.5 yanchor 0.5

    pause 1.5

    show songline4 with splitfadereverse:
        ypos 4/11 xalign 0.5 yanchor 0.5

    pause 1.5

    show songline5 with splitfadereverse:
        ypos 5/11 xalign 0.5 yanchor 0.5

    pause 1.5

    show songline6 with splitfadereverse:
        ypos 6/11 xalign 0.5 yanchor 0.5

    pause 2.5

    show songline7 with splitfadereverse:
        ypos 7/11 xalign 0.5 yanchor 0.5

    pause 2.5

    show songline8 with splitfadereverse:
        ypos 8/11 xalign 0.5 yanchor 0.5

    pause 2.5

    show songline9 with splitfadereverse:
        ypos 9/11 xalign 0.5 yanchor 0.5

    pause

    scene concerthallhallway with Dissolve(2.0)

    red @sadbrow frownmouth "[ellipses]"
    redmind @frownmouth sadbrow "Is[ellipses] he alright?"

    pause 2.0

    show concerthallhallway with vpunch

    $ PlaySound("pianoslam.ogg")

    pause 1.0

    redmind @closedbrow sweat frownmouth "Guess not."

    scene blank2 with splitfade 

    pause 1.0

    scene concerthallstage 
    show brendan angrybrow frownmouth angrywrinkles
    with splitfade

    pause 2.0

    show brendan surprisedbrow -angrywrinkles with dis

    red @talking2mouth "...Hey, Brendan."

    brendan @talkingmouth "Oh. Hey, bro."

    pause 1.0

    brendan -surprisedbrow @sadbrow talkingmouth "Uh, guess you heard that."

    red @sadbrow talkingmouth "Kinda hard to miss."

    brendan surprisedbrow @closedbrow talking2mouth "Eesh. Sorry about that, man. My voice kinda carries."

    red @sadbrow talkingmouth "Not just your voice. I heard you pound that piano hard enough that May would be jealous."

    brendan -surprisedbrow @closedbrow sweat sadmouth "...Not the time, man."

    red @sadbrow talkingmouth "Sorry."

    pause 1.0

    red @sadbrow talkingmouth "Want to talk about it?"

    brendan @talking2mouth "It's just some family drama, bro. Don't worry about it."

    red @happy "Brendan, if I can drag you into {i}my{/i} drama, then you can definitely drag me into yours."

    brendan -frownmouth @sadbrow "[ellipses]"
    brendan @talkingmouth "Alright, bro. Thanks."

    show brendan:
        ypos 1.0
        ease 0.5 ypos 1.2

    brendan @talkingmouth "C'mon, sit down with me. I've been standing on that stage, spittin' on the microphone for way too long."

    show brendan:
        ypos 1.2 zoom 1.0
        ease 0.5 zoom 1.3 ypos 1.2

    red @happy "Oh, {i}that's{/i} how I heard you from outside."

    brendan @closedbrow talking2mouth "Nah, it's not plugged in. I was just really shouting."

    pause 0.5

    redmind @surprisedbrow frownmouth "Woah."

    pause 1.0

    brendan @closedbrow talking2mouth "Okay. I don't remember if I told you this, bro, but I'm originally from Johto."

    red @closedbrow talking2mouth "I'm not sure you ever told me directly, but you mentioned it to Calem, yeah."

    brendan @talkingmouth "Well, my dad wanted to start a Gym there. But the league was already full-up. They denied his application over and over."
    brendan @sadbrow talkingmouth "So, uh... this is gonna make him sound bad, but keep an open mind... he left my mom and I and moved to Hoenn."

    red @angrybrow talking2mouth "That {i}does{/i} sound bad."

    brendan @sadbrow talkingmouth "He didn't, like, ghost us or abandon us or anything. He just literally left."
    brendan @closedbrow talking2mouth "I was just a kid at the time, so I didn't really get to know him until we moved to Hoenn ourselves, when I was eleven."

    red @confused "Hm? You moved to Hoenn, like he did? I mean, I knew you were from Hoenn, but now I'm wondering {i}why{/i}. Did you move to Hoenn {i}because{/i} your dad did? Or... did your mother move you, I guess?"

    brendan @talking2mouth "Yeah."
    brendan @talkingmouth sadbrow "Like I said, he didn't cut ties or anything. He just moved somewhere else. So we followed him a few years later."

    pause 1.0

    red @sad2brow frownmouth "[ellipses]"

    brendan @talking2mouth "I was pretty angry at him. Even though I'd never met him."
    brendan @talking2mouth "Probably {i}because{/i} I'd never met him, actually... so I was a bit of a brat. I tried to be everything he wasn't."

    pause 1.0

    brendan @happy "Guy was a battler? Well, I'd do contests. Guy was a plain and down-to-Earth? I'd be fashionable, stand out, and reach for the stars."

    red @sadbrow talkingmouth "Brendan, I think we all have rebellious teenage phases, but yours kinda just sounds like it was a good thing."

    brendan @sadbrow talkingmouth "Eh... it's easy to think that in retrospect, but I hurt a lot of people besides him. I mean, it was my mom who had to put up with that for more than a decade."
    brendan @sadbrow talkingmouth "I refused to use Pokémon that looked tough--refused to even allow my clothes to get dirty. I'd do anything to be the opposite of him."

    pause 1.0

    brendan @closedbrow talking2mouth "Then we moved to Hoenn, and... I kinda got it."

    red @confused "What?"

    brendan @annoyedbrow talking2mouth "Look, I'm not saying the guy was flawless, but it's {i}really{/i} hard to stand out as a Normal-type Gym Leader. He always had to work twice--three times as hard as anyone else."
    brendan @closedbrow talking2mouth "The guy gave my Mom and I most of what he earned at his job. He didn't want to cut ties. In fact... he wanted me to take over the gym. I mean, once I was old enough."

    pause 1.0

    brendan @closedbrow talking2mouth "But that didn't work out."

    red @sad2eyes angryeyebrows talking2mouth "He didn't want a Coordinator running his gym? After all that?"

    brendan @talking2mouth sadbrow "Wasn't that, bro."
    #brendan @talkingmouth sadbrow "Meeting May was the best thing I could've done. She really mellowed me out. And even if the sight of cookies makes me a bit sick now, it's only 'cause of her I learned to be as happy as I am."

    brendan @closedbrow talking2mouth "Nah. The reason I didn't get that gym is..."

    pause 1.0

    brendan @closedbrow talking2mouth "I'd spent over a decade trying to avoid battling, thinking about battling, doing {i}anythin'{/i} that would involve battlin'."
    brendan @sadbrow talkingmouth "I sucked, man. I kinda still do, but I'm gettin' better at it."

    red @happy "What? Come on! You got into Kobukan. You can't be {i}that{/i} bad."

    brendan @sadbrow talkingmouth "I'm as confused about that one as you are. I was pretty sure I'd blown the admittance exam."

    brendan @talking2mouth "But, even if I'm not great now, I {i}really{/i} sucked when I was a kid. I mean, I was using Ground-type moves on Flying-types. That's how bad it was."

    pause 1.5

    brendan @sadbrow talkingmouth "We were both kinda surprised. I was surprised because I was a dumb kid, and always thought not being a good battler was a choice."
    brendan @closedbrow talking2mouth "But, yeah, turns out you need to practice at something to be good at it. You can't go out of your way to avoid doing something your entire life and secretly still be amazing at it."
    brendan @happy "Who knew, right?"

    pause 0.5

    red @talkingmouth "You said your Dad was surprised, too."

    brendan @sadbrow talkingmouth "...Yyyeah. He thought that all he needed to do to get his 'Brendan takes over the gym' fantasy fulfilled was get through my teenage rebellion."
    brendan @talking2mouth "Guess he {i}also{/i} didn't really think this through. All these plans, and counter-plans, and we all forgot that I just needed to be good at battling in the first place."

    pause 1.0

    brendan @talking2mouth "And that's how it's been for about five years. I'm just kinda all-in on contests, and he's... disappointed, but, y'know, looking for other successors." 
    brendan @closedbrow sweat talkingmouth "He gave Wally his first Pokémon, the Normal-type Zigzagoon. He caught his Ralts with it."

    if (HasEvent("Wally", "Wally1Part2")):
        brendan @closedbrow talking2mouth "I dunno, though. I don't think Wally's all that interested in a Gym Leader position. I mean, bro's trying to make the Dragon Ascent. That takes a life, you know?"
        
        brendan @closedbrow angrymouth sweat "Man, I hope it {i}doesn't{/i} take a life, though. I'm not going to tell Wanda, but I'm seriously worried about Wally."

    else:
        brendan @closedbrow talking2mouth "I dunno, though. I don't think Wally's all that interested in a Gym Leader position. He's got something else going on--something big. Not sure what."

        if (GetRelationshipRank("Wally") > 0):
            redmind @happy "I do!"

    pause 1.0

    red @talkingmouth "I see. I guess there's just one question I have, then."

    brendan surprisedbrow frownmouth @neutralbrow talkingmouth "Yeah?"

    red @happy "Why were you singing an angsty power ballad to him, five years after all this was supposed to be settled?"

    pause 1.0

    brendan @happy "Ah, yeah, that... uh..."

    pause 1.0

    brendan -surprisedbrow @closedbrow talking2mouth sweat "He's coming here."

    red @surprisedbrow talking2mouth "What? Really?"

    brendan @talking2mouth "Yeah. He wants to watch a contest I'm going to participate in."
    brendan @annoyedbrow talking2mouth shadow angrywrinkles "For the first time. Ever."

    pause 1.0

    red @sadbrow talkingmouth "Is that not[ellipses] good?"

    pause 1.0

    brendan @sadbrow talkingmouth "Man, you tell me. It took a lot to get over my Dad issues, y'know? Even went to therapy and junk. I'd accepted that I couldn't make him proud. That I couldn't even make him interested."
    
    pause 1.0

    brendan annoyedbrow frownmouth @talking2mouth "But now he's showing up, after years of not caring about what I'm actually {i}good{/i} at, and that just... that..."

    red @sadbrow talkingmouth "Pisses you off?"

    pause 1.0

    brendan -annoyedbrow @sadbrow talkingmouth "It gives me hope, bro. Hope that I didn't need, or want, until I got this phone call two hours ago."
    
    pause 1.0

    brendan @sadbrow talkingmouth "But now... I've got this hope, and no amount of closure I thought I had can get rid of it, y'know?"

    red @sadbrow talkingmouth "I get you. And I'm sorry, man. Hope sucks, sometimes."

    pause 1.5

    red @confused "Well, what are you going to do?"

    brendan @closedbrow talking2mouth "...All I can do, I guess. Just do the contest, do it really damn well. Win, obviously. Maybe winning will impress him."
    brendan @happy "I mean, if he thinks I'm as bad at contests as I am at battles, no wonder he's never been impressed. Heck, I'm not sure he even knows I can sew."

    pause 1.0

    red @talkingmouth "Buddy... I seriously think you need to give yourself a bit more credit. You don't need to put in all the legwork here. He's your father. He should be trying harder to reach out to you."

    narrator "Brendan holds his phone out, shrugging."

    brendan @sadbrow talkingmouth "Bro, as of two hours ago, he kinda has."

    red @closedbrow talking2mouth "Okay, so, yeah, that's great, but that's not {i}everything{/i}. Based on what you've just told me, he probably needs to do a lot more."

    pause 0.5

    brendan @sadbrow talking2mouth "Maybe."

    pause 1.0

    red @sadbrow talkingmouth "{i}Not being good at something{/i} isn't something you need to apologize for. Whether it's taking tests, or battling, or... hell, I dunno, dancing."

    brendan @talking2mouth "I'm great at dancing, though."

    red @talkingmouth "I don't doubt that. But if you were bad at it... I mean, you don't have any obligation to be good at {i}anything{/i}. Even the stuff your Dad wants you to be."

    brendan @talking2mouth "I know that. And I'm not tryin' to be good at battling. I mean, that ship's sailed."
    brendan @talkingmouth "But... if I could show him {i}how good{/i} I am at contests... if I could get him to {i}understand{/i} contests are worth my time, and are a kind of power themselves..."

    pause 1.0

    brendan @sadbrow talkingmouth "Did I mention I was {i}really{/i} okay without this hope?"

    red @sadbrow talkingmouth "Sorry, man. Hope springs eternal... even when you don't want it to."

    brendan @closedbrow talking2mouth "Yeah, I guess. I should probably start thinking about what I'll do for the contest, then..."

    red @talkingmouth "What do you mean? You're going to win, right?"

    brendan @talkingmouth "Oh, for sure. But I need to figure out {i}how{/i} I'm going to win. I can't just put on a show-winnin' performance this time. I gotta put on a heart-winnin' one."

    pause 1.0

    brendan @talking2mouth "...Yeah, I'm going to need to practice my tenor for this. Best way to crack ice is with high notes."
    brendan @talkingmouth "Alright."
    brendan -frownmouth @happy "Alright! I feel good about this, actually. We're going to put on a rocking performance--we'll knock my Dad back in his seat!"

    pause 1.0

    brendan @sadbrow talkingmouth "Hey, thanks, bro. Appreciate you bein' a sounding board for me."

    red @talkingmouth "I appreciate you telling me about this." 
    red @happy "And I'm sure you'll put on the best contest performance ever!"

    brendan @talkingmouth "Appreciate it, bro. Seriously. We're [bluecolor]tight{/color}, right?"

    red @talkingmouth "Thick as thieves."

    show brendan:
        ypos 1.2 zoom 1.3
        ease 0.5 ypos 1.0 zoom 1.0

    brendan @talkingmouth "Sick. Alright. I'm going to head to the music room and get composin', then!"

    red @happy "Godspeed."

    hide brendan with Dissolve(1.5)

    pause 1.0

    redmind @sad2eyes angryeyebrows frownmouth "[ellipses]"
    redmind @sad2eyes angryeyebrows frownmouth "Brendan's father, huh... sounds like a real piece of work."

    $ RelationshipRankUp("Brendan", "Tight", 1)

    return