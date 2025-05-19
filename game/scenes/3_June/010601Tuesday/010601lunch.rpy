label lunch010601:

narrator "As students trail from the gym class into the cafeteria, you notice many of them seem exhausted from the gym class, far more than usual."

show nessa sadbrow frownmouth uniform with dis:
    xpos 0.33 xzoom -1

show sonia sadbrow uniform with dis:
    xpos 0.66

nessa @talking2mouth "Battling always takes a lot out of my Pokémon, and even me, but it's different under Professor Rowan, somehow."

sonia @talking2mouth "That's just the way he is. He pushes his students hard, harder, and even harder."

menu:
    "[bluecolor][[Nessa Rank 2]{/color} >Listen in" if GetRelationshipRank("Nessa") > 1:
        jump nessasoniarowanconvo
    "[bluecolor][[Sonia Rank 2]{/color} >Listen in" if GetRelationshipRank("Sonia") > 1:
        jump nessasoniarowanconvo
    ">Mind your own business":
        jump afternessasoniarowanconvo

label nessasoniarowanconvo:
    $ AddEvent("Nessa", "ListenToNessaSoniaConvo")
    sonia @sadbrow talkingmouth "Last year, I was in his class. I[ellipses]"

    if (GetRelationshipRank("Sonia") > 1):
        redmind uniform @frownmouth "Hm... she mentioned that she had a nervous breakdown last year. I'm sure being in Rowan's class didn't help..."

        $ ValueChange("Sonia", 1, 0.66)

        narrator "Your understanding of, and sympathy for, Sonia increased!"

    sonia -sadbrow @closedbrow talkingmouth "All I can say is I'm really rather thankful that I was placed in Professor Cherry's class this year."

    nessa -sadbrow @closedbrow talking2mouth "Is Rowan worth it?"

    sonia @confused "Wot? Are you considering a transfer?"

    nessa @talkingmouth "Didn't know that was a thing I could do."
    nessa @sadbrow talkingmouth "But not really, Sunny. Working that hard[ellipses] not up my alley. I'm just interested in your thoughts."

    sonia @sadbrow talkingmouth "Well, there's no doubt that he's a fantastic trainer, an incredibly intelligent man, and taught the strongest woman in the world."

    pause 1.0

    sonia @closedbrow talking2mouth "But is he {i}worth it?{/i} That's a tricky question to answer."
    sonia @talking2mouth "He's a bit like my Gran. Very severe. But he goes a step further. He's... well, there's no beating around the bush. He can be mean."

    nessa @talking2mouth "Picked up on that."

    sonia @talking2mouth "A lot of people thrive when challenged. A lot of people need to be pushed down to spring back up. Some people's karma rewards them if they're in a hard time."
    sonia @sadbrow talkingmouth "People like Lee and Raihan. They could flourish under him, jumping back up. Springs. Or like Cynthia, of course."
    sonia sadbrow frownmouth @talking2mouth "But... people like me, Ness? I wasn't a spring. I was a paper crane. And I just crumpled."

    pause 1.0

    nessa @talking2mouth "Could I do it?"

    sonia @sadbrow talkingmouth "Ness, you can do anything you set your mind to."

    nessa @talking2mouth "Sunny."

    show nessa:
        xpos 0.33
        ease .5 xpos 0.4

    pause 1.0

    nessa -frownmouth @talkingmouth "Could I do it?"

    pause 1.0

    sonia sadbrow @closedbrow talking2mouth "Well, it'd be a very uphill battle, so--"

    nessa @talkingmouth "Sunny."

    show nessa:
        xpos 0.4
        ease .5 xpos 0.5

    pause 1.0

    nessa @talkingmouth "Could I do it?"

    show sonia sadbrow -frownmouth  with dis

    pause 1.0

    sonia -sadbrow -frownmouth @closedbrow talking2mouth "No, Ness. He'd sense your attitude, zero in on you, and keep smashing himself against you until you were just rubble."

    nessa "Hm."

    show nessa:
        xpos 0.5
        ease 0.5 xpos 0.33

    nessa -sadbrow @closedbrow talkingmouth "Don't think you have any proper reason to beat yourself up over it, then."
    nessa @happy "After all, if I couldn't do it, then--"

    show nessa:
        xpos 0.33
        ease 0.5 xpos 0.25

    show sonia:
        xpos 0.66
        ease 0.5 xpos 0.75

    show raihan uniform behind nessa with vpunch

    raihan @happy "Oi, ladies, you two coming to the table? Sabrina and Rosa are talkin' about Leon. Thought you might want to be part of that."

    nessa @angrybrow talkingmouth "I wouldn't mind talking about something {i}other{/i} than Leon once in a while. We're not in Galar anymore."

    raihan @talkingmouth closedbrow "See where you're coming from, but it's a bit of cultural outreach, you know? More fans Leon's got in the colonies, the bigger and better Galar gets."

    nessa @closedbrow talkingmouth "'The colonies'? I have {i}no{/i} idea how you've avoided being cancelled for so long. {i}I{/i} get more hate for being hot and quiet."

    raihan happybrow smilemouth @talkingmouth "That'd be you, Ness, pulling on my ear before I post something daft."

    nessa @closedbrow talkingmouth "True. I don't know what you'd do without me, honestly."

    sonia happybrow @talkingmouth "Whatever it is, it wouldn't be nearly as fun."

    nessa sadbrow talkingmouth "Yeah, I'm a regular life of the party."

    $ ValueChange("Sonia", 1, 0.33, False)
    $ ValueChange("Raihan", 1, 0.5, False)
    $ ValueChange("Nessa", 1, 0.66)

label afternessasoniarowanconvo:

hide sonia 
hide nessa 
hide raihan
with dis

jump PickTable