label cyclizarhunt:
    $ AddEvent("Dawn", "CyclizarHunt")
    $ renpy.music.queue("audio/music/Fieldstheme_Start.ogg", channel='music', loop=None, fadein=1.0, tight=None)
    $ renpy.music.queue("audio/music/Fieldstheme_Loop.ogg", channel='music', loop=True)
    show clouds:
        yalign 0.5
    show fields1 :
        yalign 0.33 xalign 0.95
    with Dissolve(2.0)
    show blank2 as blackground behind map

    show leaf with dis:
        xpos 0.66

    show dawn with dis:
        xpos 0.33

    dawn @talkingmouth "{gradualsize=21-31}...so I thought I might try to help her{/gradualsize} out."

    leaf @talkingmouth "That's a good idea! I bet an awesome trainer like you could also catch a {i}ton{/i} of Cyclizar."
    leaf @angrybrow talking2mouth "Ooh, maybe we can make it so she doesn't have to pay a single Pokécent out of her own pocket!"

    dawn @sadbrow talkingmouth "Th-that'd be... cool... but, um, some people probably won't be able to ride an untrained Cyclizar without a {i}lot{/i} of practice..."

    leaf @talking2mouth "Well, we'll give it our best! Better to have the tools and not need them than to leave Professor Cherry hanging!"
    leaf @sadbrow talking2mouth "After all... if what she said about how we've been taught so far is true... then she {i}seriously{/i} deserves some thanks for this. It's the least we can do to show we're grateful."

    dawn @talkingmouth "R-right."

    pause 1.0

    if (not HasEvent("Ethan", "IgnoredFrenzyConfession")):
        dawn @surprised "O-oh! Rival!"

        red @talkingmouth "That's my name."

        leaf @talking2mouth "You two are rivals now?"

        dawn @talkingmouth "Y-yeah. We, um, decided it last Wednesday."

        red @talkingmouth sweat "More like you decided it."

        dawn @sadbrow "Oh. I'm sorry..."

        red @happy "No, you don't get it. That's {i}great!{/i} I'm {i}glad{/i} you decided it. Good for you."

        red @talkingmouth "I fully support whatever you're passionate about."

        if (GetRelationship("Dawn") == "Muse"):
            red @happy "That's why I'm your muse, you know?"

            $ ValueChange("Dawn", 2, 0.33, False)

        else:
            $ ValueChange("Dawn", 1, 0.33, False)
    
        leaf @happy "Aw. You are both, honestly, too cute."

        $ ValueChange("Leaf", 1, 0.66)
    
    else:
        leaf @happy "Oh, hey, I didn't see you there!"

    red @talkingmouth "Thought I'd show up and see if there are any Cyclizar I can snag for the Professor. Mind if I join you guys?"

    dawn @talkingmouth "No! That'd be, um, great! The more the merrier."

    red @talkingmouth "Cool. Let's get started."

    leaf @surprised "...Oh, wait. There's one problem. I'm not sure I have enough Poké Balls."

    show gardenia angrybrow happymouth:
        xpos 1.2 
        ease 0.3 xpos 0.75

    show dawn surprisedbrow frownmouth:
        xpos 0.33
        ease 0.5 xpos 0.25

    show leaf surprisedbrow frownmouth:
        xpos 0.66
        ease 0.5 xpos 0.5 xzoom -1

    gardenia "And {i}that's{/i} where I come in!"

    pause 1.0

    dawn "{size=30}Oh, god, it's her again.{/size}"

    gardenia -angrybrow -happymouth @happybrow talkingmouth "Please, hold your applause."

    red @talking2mouth confusedeyebrows "Sorry, what exactly is happening here?"

    gardenia @talking2mouth "I heard that you were in the market for some Poké Balls."
    gardenia @happybrow talking2mouth "I've also got some Repels, which should make it easier to find the Cyclizar you're hunting for faster--all at very reasonable prices, of course!"

    leaf @sarcastic "Were you, just, like, following us and waiting until someone said they needed something?"

    gardenia @talking2mouth "Funny question! Now, I can't stick around for long--there are some other customers who want my business, I think--but do any of these splendid capture packages interest you?"

    $ discountask = False
    $ priceone = 1000
    $ pricetwo = 3000
    $ pricethree = 6000

    label gardeniafieldshustle:

    menu:
        "5 Poké Balls & 1 Repel for $[priceone]":
            if (money >= priceone):
                $ money -= priceone
                $ GetItem("Poké Ball", 5)
                $ GetItem("Repel", 1)
                $ ValueChange("Gardenia", 1, 0.75)

                gardenia @happy "Pleasure doing business with you!~ Anything else?"

            else:
                gardenia @sadbrow talkingmouth "Sorry, [first_name]. I can't give credit. Come back when you're a little... mmm... richer!"

            jump gardeniafieldshustle

        "5 Great Balls & 1 Super Repel for $[pricetwo]":
            if (money >= pricetwo):
                $ money -= pricetwo
                $ GetItem("Great Ball", 5)
                $ GetItem("Super Repel", 1)
                $ ValueChange("Gardenia", 2, 0.75)

                gardenia @happy "Pleasure doing business with you!~ Anything else?"

            else:
                gardenia @sadbrow talkingmouth "Sorry, [first_name]. I can't give credit. Come back when you're a little... mmm... richer!"

            jump gardeniafieldshustle

        "5 Ultra Balls & 1 Max Repel for $[pricethree]":
            if (money >= pricethree):
                $ money -= pricethree
                $ GetItem("Ultra Ball", 5)
                $ GetItem("Max Repel", 1)
                $ ValueChange("Gardenia", 3, 0.75)

                gardenia @happy "Pleasure doing business with you!~ Anything else?"

            else:
                gardenia @sadbrow talkingmouth "Sorry, [first_name]. I can't give credit. Come back when you're a little... mmm... richer!"

            jump gardeniafieldshustle

        "What do the repels do?":
            gardenia @happy "Good question!"
            gardenia @talking2mouth "Repels have two functionalities."
            gardenia @talking2mouth "{i}All{/i} Repels allow you to automatically escape from battle."
            gardenia @happy "And you don't have to use them {i}in-battle{/i}, either. Use repels outside of battle, and they'll last for a while... about twenty encounters."

            gardenia @talking2mouth "Anyway, every kind of Repel keeps away Pokémon of a certain strength."
            gardenia @talking2mouth "Normal repels keep weaker Pokémon away, so only the stronger Pokémon will show up. This means the Pokémon that appear most commonly in an area, uh, won't!"
            gardenia @happy "Super Repels keep all weaker Pokémon away, so only the strongest Pokémon in each area will try to attack. That means both common and uncommon Pokémon won't show up."
            gardenia @talking2mouth "Finally... and this is where the {i}real{/i} power is, if you want my opinion..."
            gardenia @happy "Max Repels make only the absolute strongest Pokémon show up. The alphas of each herd, the elders of the swarm. The big kahunas, you know?"
            gardenia @talking2mouth "That means only the most powerful Pokémon in any area will show up, the stuff you might have to spend hours looking for, otherwise. They're very powerful Repels!"
            gardenia @angrybrow happymouth "And my {i}personal{/i} recommendation, if you happen to be in the market."

            jump gardeniafieldshustle

        "Can I have a discount?" if (not discountask):
            $ discountask = True
            show gardenia surprisedbrow frownmouth with dis

            pause 0.5

            gardenia @talking2mouth "Hm. That's ballsy."

            if (investment == 0):
                gardenia @talking2mouth "Sorry, though, friend. I usually only give discounts to established business partners."
                gardenia @talking2mouth "Come visit me in the baseball field sometime, though, and we can talk business."

            elif (investment < 4000):
                $ priceone = 800
                $ pricetwo = 2800
                $ pricethree = 5800
                gardenia -surprisedbrow -frownmouth @happy "You know what? Why not! I'll knock $200 off the asking price. As a token of my appreciation for our business relationship."

            else:
                $ priceone = 500
                $ pricetwo = 2500
                $ pricethree = 5500
                gardenia -surprisedbrow -frownmouth @happy "You know what? Why not! I'll knock a whole $500 off the asking price. As a token of my appreciation for our business relationship."

            jump gardeniafieldshustle

        "Away with ye, harbinger of capitalism!":
            gardenia @happy "Fair enough!"

    gardenia @angrybrow talking2mouth "Now, what about {i}you{/i} fine ladies...?"

    show blank2 with dis

    narrator "Gardenia pressures Dawn into buying a ludicrous amount of merchandise until Leaf rather sharply sends her on her way."

    show leaf -surprisedbrow -frownmouth:
        xpos 0.66 xzoom 1
    show dawn:
        xpos 0.33
    hide blank2 
    hide gardenia
    with dis

    dawn -surprisedbrow frownmouth @sadbrow talkingmouth "I'm... not good at saying no when people try to sell me something..."

    leaf @talkingmouth "Clearly. We'd better make sure you stay far away from {i}Join.{/i} There's a nose cream salesman there who'd eat you alive."

    return

label cyclizarhuntpart2:
    $ AddEvent("Dawn", "UsedGummyWyrms")
    show leaf angrybrow frownmouth with dis:
        xpos 0.66

    show dawn with dis:
        xpos 0.33

    dawn @sadbrow talkingmouth "I-is... is something wrong, Leaf?"

    leaf @talkingmouth "Yeah. My feet hurt, and I'm all tired and sweaty, and these Cyclizar are {i}way{/i} rarer than I thought they'd be."

    dawn @closedbrow "H-hold on... I think I know what to do here. Um, a staff member... I think he's staff anyway... gave me these."
    dawn @talkingmouth "They're called 'PokéTreats', and they, um, they're meant to attract certain wild Pokémon to your location."

    dawn @talkingmouth "Let's see... this one's the 'Gummy Wyrms', I think. It should make Dragon-types more common."

    $ activetreat = Item.GummyWyrms

    narrator "[bluecolor]Dawn used the Gummy Wyrms.{/color} Now, for every consecutive win, your chances of encountering a Dragon-type Pokémon will increase."

    return
