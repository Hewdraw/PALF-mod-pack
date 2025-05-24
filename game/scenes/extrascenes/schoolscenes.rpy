label combeefrenzy:
    scene baseball
    show whitney
    with splitfade

    if (activetreat in [Item.PicnicBasket, Item.BouffalantWings]):
        $ AddEvent("Whitney", "FrenzBee")
        whitney @talking2mouth "Oh, hey! [first_name], perfect timing!"

        red @confusedeyebrows talkingmouth "What, you're saying the jazz-loving bee that hit on you is here?"

        whitney surprised "Uh, yeah!"

        red @surprised "What?"

        stop music fadeout 1.5
        $ renpy.music.queue("Audio/Music/RelicCastle_Start.ogg", channel='music', loop=False, tight=None, fadein=3.0)
        $ renpy.music.queue("Audio/Music/RelicCastle_Loop.ogg", channel='music', loop=True, tight=None)

        whitney @sad "Ah! It's coming back! And I'm allergic to bee stings!"

        show whitney:
            xpos 0.5
            ease 0.3 xpos -0.5

        red @surprised "Wait, really?"

        $ sidemonnum = 415

        $ PlaySound("pokemon/cries/415.mp3")

        sidemon "Hot! Hot! Hot!"

        show sideportraitfull:
            xpos 1.1 zoom 0.0 ypos 0.0 yanchor 1.0 xanchor 0.5
            ease 1.0 xpos 0.5 zoom 2.0 ypos 1.0
            ease 1.0 xpos 0.2 zoom 0.5 ypos 0.3
            easeout 1.0 xpos 0.5 zoom 1.0 ypos 0.4
            easein 1.0 zoom 3.0 ypos 1.2

        red @surprised "What? It really {i}is{/i} a Combee! But... there's something different about it...?"

        show sideportraitfull:
            ease 0.3 zoom 2.0 align (0.5, 0.5) alpha 1.0

        sidemon "Hot! Hot! Hot!"

        python:
            trainer1 = Trainer("red", TrainerType.Player, playerparty, number=3)

            vespiquenobj = Pokemon("Vespiquen", level=33.3, moves=[GetMove("Attack Order"), GetMove("Defend Order"), GetMove("Heal Order"), GetMove("Acrobatics")], gender=Genders.Female, item="Sitrus Berry", foreverals=["Vespiquen Uneveral"], frenzynerf=(21, ["Slash", "Bug Bite", "Defend Order", "Power Gem"]), intelligence=3)
            vespiquenobj.ApplyStatus("frenzied")
            vespiquenobj.Image = "pokemon/415.webp"
            vespiquenobj.Nickname = "Combee"
            trainer2 = Trainer("sideportraitfull", TrainerType.Enemy, [vespiquenobj], isPokemon=True)

        call Battle([trainer1, trainer2], healParty = False, specialmusic="Nothing", custombrain=combeebrain) from _call_Battle_168
        $ RecordBattle("Combee1")

        stop music fadeout 1.5

        pause 2.0

        queue music "audio/music/goldenrod_start.ogg" noloop
        queue music "audio/music/goldenrod_loop.ogg"

        show whitney:
            xpos -0.2
            ease 2.0 xpos 0.0 rotate 25

        pause 0.5

        whitney sadbrow @talking2mouth "Is it gone?"

        red @talkingmouth sweat "Yeah, it's gone."

        $ ValueChange("Whitney", 3, 0.05)

        show whitney:
            xpos 0 rotate 25
            ease 0.5 xpos 0.5 rotate 0

        whitney -sadbrow @talking2mouth "Phew! Thanks for that!"
        whitney @surprised "But, wait, how could it speak Japanese?"

        red @talkingmouth "I don't think it was speaking Japanese at all."
        red @closedbrow talking2mouth "When I was battling it, it had a Foreveral on it."
        red @sideeyes talking2mouth "It's concerning, but I've seen something like that before." 
        red @talking2mouth "But this one... it looks like it was choking on it."
        red @sadbrow talkingmouth "That choking sound was probably what you heard. It sounded like it was saying 'Hot! Hot! Hot!'"

        whitney sadbrow frownmouth @sad "Oh no! The poor thing...! Does it need medical attention?"

        if (vespiquenobj in AllPokemon()):
            red @talking2mouth "Nah. Capturing it broke the Foreveral."

        elif (WonBattle("Combee1")):
            red @closedbrow talking2mouth "Nah. It seemed fine after I defeated it. I think battling it enough broke the Foreveral."

        else:
            red @sweat sadbrow talkingmouth "I mean, you saw how it kicked my ass, right? I'm pretty sure it's doing fine. It got the Foreveral out before it flew away, anyway. It shattered before it even hit the ground, though."

        whitney -sadbrow -frownmouth @talkingmouth "...Okay. That's good. But there's one more question..."

        red @confused "Yeah?"

        whitney @confusedbrow talkingmouth "How did it ask me if I liked jazz?"

        red @closedbrow talking2mouth "Cripes, I forgot about that part. Okay, I don't actually know that one. Maybe there was a radio nearby or something?"

        whitney @confusedeyebrows talking2mouth "[first_name], it's 2004. There aren't any radios {i}left.{/i}"

        red @closedbrow talkingmouth "Yeah, alright. You can lord your technological superiority over me later. I need to go."

        whitney @happy "Thanks again for clearing out the baseball field!"

        red @talkingmouth "Any time."

        scene blank2 with splitfade

        pause 2.0

        call clearscreens() from _call_clearscreens_234
        scene baseball
        show flannery at leftside:
            xpos 0.33 xzoom -1
        with splitfade

        Character("???") "\"Ya like jazz?\""

        show flannery:
            xpos 0.33
            ease 0.5 xzoom 1

        flannery @talking2mouth "Huh? Jazz? I mean, sure, it's fine. I don't think I recognize you...?"

        show brock:
            xpos 1.2 xzoom -1
            ease 0.5 xpos 0.66

        brock @talkingmouth "Probably not. I'm a candle on the wind, Li'l Sis."
        brock @happymouth "A flame one moment... aflame the next."

        flannery @confusedbrow talking2mouth "Um... are you meant to be here?"

        brock @talkingmouth "Are any of us really meant to be anywhere?"

        pause 1.0

        brock surprised @happy "Eh-heh. Anyway, I noticed you've got an Onix. Pretty solid. I've got an Onix, too."

        pause 1.0

        flannery tired @tiredbrow talking2mouth "I swear to God, if you take your pants off, I'm having my Numel burn off whatever's underneath."

        brock sadbrow @sad "Wo-hoh! You've got the wrong idea, Li'l Sis. I'm just... uh, just asking questions."

        pause 1.0

        brock sadbrow happymouth "Ya like ska?"

        scene blank2 with splitfade

    else:
        red @talkingmouth "Hey, Whitney. Is that Combee you were talking about around?"

        whitney @talking2mouth "Not right now. But it keeps coming back to the field--and I {i}swear{/i} it's calling me hot!"

        red @closedbrow talkingmouth "We'll see."

        whitney @upeyes talking2mouth "Anyway, if we want it to show up... hm. I think it shows up more often when Flan and I try to picnic here..."
        whitney @sadbrow talking2mouth "Maybe that helps?"

        red @closedbrow talking2mouth "Yeah, it just might. I think I know what to do."

        redmind @thinking "If I were to come here smelling like a Pokétreat Combee would like, then..."
            
        if (GetItemCount(Item.PicnicBasket) > 0 or GetItemCount(Item.BouffalantWings) > 0):
            redmind @thonk "Hold, on, don't I have something like that on me, already?"

    return

label LeafMagnetGet:
    scene relichall_A
    show leaf
    with splitfade

    leaf @talkingmouth "Heya, [first_name]. What's up?"

    red @talking2mouth "Just had a question for you. Since you're in the Electric elective, do you have any spare magnets?"

    leaf @talkingmouth "Oh, sure. Want one?"

    red @talkingmouth "Yep."

    leaf @closedbrow talkingmouth "Hehehe... you're {i}asking{/i} me to give you something, now. This is definitely a change of pace."

    red @sadbrow talkingmouth "I'll admit, it's not something I'm used to."

    leaf @closedbrow talkingmouth "Well, in my magnanimousness, I am fully willing to give you this magnet, as long as you do something for me."

    red @talkingmouth "Name it."

    show leaf surprisedbrow frownmouth with dis

    red @talking2mouth sweat "As long as it doesn't involve tongues or marzipan, because I can't handle that."

    pause 1.0

    leaf -surprisedbrow -frownmouth @sadbrow talkingmouth "It's so great that even after all this time we've known each other, you can still say stuff that throws me completely off-balance, skippy."

    red @sadbrow talkingmouth "Same to you, you lunatic."

    $ ValueChange("Leaf", 3)

    leaf @happy "God, you just {i}get{/i} me."
    leaf @flirtbrow talkingmouth "So I bet you know what I want in exchange, don't you?"

    red @winkbrow talkingmouth "Already getting out my Poké Balls."

    leaf angrybrow happymouth "That's my dormie!"

    python: 
        trainer1 = MakeRed()
        trainer2 = MakeTrainer("Leaf")

    call Battle([trainer1, trainer2]) from _call_Battle_184
    $ RecordBattle("Leaf2")

    show leaf happybrow with dis

    if (WonBattle("Leaf2")):
        $ ValueChange("Leaf", 3)

    leaf @happy "You are just the {i}best{/i} at that, you know?"

    if (WonBattle("Leaf2")):
        red @closedbrow talkingmouth "I bet you say that to everyone you battle with."

    else:
        red @closedbrow talkingmouth "I didn't even win. I bet you say that to everyone you battle with."

    leaf @flirtbrow talkingmouth "Sure, but I {i}mean it{/i} with you."

    red @happy "Imagine how special I feel."

    $ GetItem(Item.Magnet)

    leaf surprisedbrow frownmouth @closedbrow talkingmouth "Yeah, you're blessed. Anyway, here's your magnet, as promised. Don't do anything weird with it."

    red @sadbrow talkingmouth "Leaf, you have {i}no idea{/i} how weird the things I'm going to do with it are."

    return

label SoniaMagnetGet:
    $ location = "laboratory"
    scene research
    show sonia
    with splitfade

    sonia @talkingmouth "Oh? [first_name]? Is there something I can do for you?"

    red @talking2mouth "Just had a question for you. Since you're in the Electric elective, do you have any spare magnets?"

    sonia @talkingmouth "Rather few, yes."
    sonia @sadbrow talking2mouth "Although... they're not {i}exactly{/i} spare. I somewhat need them. I use them in experiments, and sell the excess, so..."

    red @talkingmouth "Oh, I understand. Totally fine. Can I buy one off of you?"

    sonia @talking2mouth "Certainly. How does... hm. How would $500 sound?"

    menu:
        "Sure. Here you go." if money >= 500:
            $ money -= 500
            $ ValueChange("Sonia", 6)

            sonia @talkingmouth "Here's your magnet. Ah, thank you for... well, to put a rather fine point on it, the money."

            $ GetItem(Item.Magnet, text="You bought the magnet for $500!")

        "Sorry, that's a bit much.":
            sonia @confusedbrow talking2mouth "Oh, terribly sorry. Er... I should've remembered, you're also... my mistake. Please, take the magnet, free of charge."

            red @sadbrow talkingmouth "Aw, Sonia, you don't have to do that. I'm fine paying a little bit, really."

            sonia @sadbrow talkingmouth "N-no, I mustn't be greedy. Gran wouldn't approve. Again, very sorry."

            $ ValueChange("Sonia", 3)

            $ GetItem(Item.Magnet, text="You got the magnet, and some guilt! But guilt isn't a tracked stat, so there's no mechanical repercussions for taking this option.{w=1.5}\nYou monster.")

        "I don't have that much on me." if money < 500:
            sonia @confusedbrow talking2mouth "Oh, terribly sorry. Er... I should've remembered, you're also... my mistake. Please, take the magnet, free of charge."

            red @sadbrow talkingmouth "Aw, Sonia, you don't have to do that. I'm fine paying a little bit, really."

            sonia @sadbrow talkingmouth "N-no, I mustn't be greedy. Gran wouldn't approve. Again, very sorry."
            
            $ ValueChange("Sonia", 3)

            $ GetItem(Item.Magnet, text="You got the magnet, and some guilt! But guilt isn't a tracked stat, so there's no mechanical repercussions for taking this option.{w=1.5}\nYou monster.")

        "I don't have that much on me, but you can ask Gardenia to pay you." if money < 500 and bank >= 500:
            sonia @talkingmouth "Oh! Right, yes. Gardenia's got some of my money in storage, as well. How are you finding it?"

            red @closedbrow sweat talking2mouth "To be honest, I'm not exactly sure what she's doing with my money, but she's adding a little bit to it every day, so... I guess it's fine?"

            sonia @sadbrow talkingmouth "Fair enough. She jolly well ought to be more reliable than the banks in Galar, in any case. They're {i}never{/i} open."
            sonia @talking2mouth "Oh, please excuse my dithering."

            red @happy "Totally fine, Sonia."

            $ ValueChange("Sonia", 6)

            sonia @talkingmouth "Here's your magnet. Ah, thank you for... well, to put a rather fine point on it, the money."

            $ bank -= 500
            $ GetItem(Item.Magnet, text="You gained the magnet! Gardenia will give Sonia $500 from your bank account.")

    sonia @talkingmouth "Good luck with... whatever enterprise you have planned with that magnet, then."

    red @happy "Thanks. Seeya!"

    return

label NateMagnetGet:
    $ location = "laboratory"
    scene research
    show nate
    with splitfade

    nate @talkingmouth "Hey, [nate_name]. Something up?"

    red @talking2mouth "Oh, I just remembered that you were in the Electric elective, right? I wondered if you had any leftover Magnets from your time in there."

    nate sad2brow @talkingmouth "Oh... yeah."

    pause 1.0

    nate @sadbrow talkingmouth "I do. It's just, I'm kinda..."

    pause 1.0

    red @sadbrow talkingmouth "Hey, man, if you want to keep it, you can. It's not a big thing."

    nate @closedbrow talking2mouth "Nah, it's... someone should take it. I've got other, more powerful, ones anyway."
    nate @sadbrow talkingmouth "It's just always a bit melancholy when you give away the last piece of something you left behind, you know?"

    redmind @sadbrow frownmouth "...He's talking about the identities he's had to leave behind as an agent, isn't he?"

    nate @happy "Anyway, here's the magnet, man. Thanks for remembering that I used to be the Electric elective."
    nate @sad2brow talkingmouth "Knowing there's someone who remembers 'past mes' is... nice, I guess."

    $ ValueChange("Nate", 6)
    $ GetItem(Item.Magnet, text="You get the magnet! You grip it firmly in your hand.")

    pause 2.0

    nate @surprised "Hey, you're holding the magnet. And I'm not. That's weird."

    red @confused "What? What do you mean?"

    nate @sadbrow talkingmouth "It's just that you're holding a magnet, and I'm not, so[ellipses]"
    nate winkbrow @happymouth "Why am I so attracted to you?"

    pause 2.0

    red tired unamusedbrow unamusedmouth "[ellipses]"

    show nate sadbrow frownmouth with dis

    red @closedbrow talking2mouth "That was repulsive."

    nate sadbrow frownmouth @talking2mouth "Man, if you just liked puns, you'd be perfect."

    red @upeyes angryeyebrows talking2mouth "I like {i}good{/i} puns."

    nate happy "Then you're missing the point, [nate_name]!"

    return

label RosaMagnetGet:
    scene relichall_A
    show rosa
    with splitfade

    red @talkingmouth "Hey, Rosa! I have a question for you."

    rosa @happy "Sure thing! What's up?"

    red @talking2mouth "You're in the Electric elective, right?"

    rosa @talking2mouth "Hm? Yeah."

    red @talkingmouth "Do you have any spare magnets from your time there?"

    rosa @closedbrow sweat talking2mouth "I... do. Um, do you want one?"

    red @talking2mouth "I did, but you look concerned. Are you not allowed to give out gifts?"

    rosa @sad2brow talkingmouth "Not usually. Especially not to men my age. It's bad for optics..."

    if (GetRelationshipRank("Rosa") > 1):
        red @happy "C'mon. We hang out a bunch already. That hasn't been a problem, has it?"

        rosa @closedbrow sweat talking2mouth "We've gotten lucky, but..."

    red @sadbrow talkingmouth "Oh, I get it. Maybe I could give you something, so it's more or less a trade, instead of just a gift?"

    rosa @confusedeyebrows talking2mouth "What kind of thing?"

    red @talking2mouth "Hm... looking in my bag right now, how about..."

    label starttrade:

    python:
        itemkeys = []
        for item, amount in inventory.items():
            itemname = GetItemName(item)
            # Use an f-string to format the display string
            display_text = f"1x {itemname} (Total Held: {amount})"
            # Append a tuple with unique values
            itemkeys.append((display_text, item))
        itemkeys.append(("Nevermind", "Nothing"))
        item = renpy.display_menu(itemkeys)

    if (item == Item.Magnet):
        red @closedbrow talking2mouth "Wait. That's silly. I'm not going to trade a Magnet for a Magnet."
        jump starttrade

    elif (item == "Nothing"):
        red @wince talking2mouth "Uh... sorry, nevermind. I'm not sure I {i}can{/i} actually trade anything away right now."

        rosa @closedbrow sweat talking2mouth "Oh. Well... I guess there {i}probably{/i} isn't anyone around right now, so... as long as we're fast..."
        
        $ GetItem(Item.Magnet, text="You got the Magnet! Rosa quickly passes it to you, while looking over her shoulder.")

        jump afterrosamagnettrade

    elif (LoseItem(item)):
        $ itemname = GetItemName(item)
        $ itemvalue = GetGiftValue(character, item)
        
        if (itemvalue >= 7):
            rosa @surprised "Woah, really?! That's way more valuable than this Magnet... thank you so much! I really, {i}really{/i} mean it!"
            $ ValueChange("Rosa", itemvalue + 3)
            $ GetItem(Item.Magnet, text="You trade the Magnet for the [itemname], which Rosa giddily accepts.")

        elif (itemvalue >= 5):
            rosa @surprised "Wow! That's a very fair trade. Thank you so much for your support!"
            $ ValueChange("Rosa", itemvalue + 3)
            $ GetItem(Item.Magnet, text="You trade the Magnet for the [itemname], which Rosa happily accepts.")

        elif (itemvalue >= 3):
            rosa @talkingmouth "Sure! That's a fair trade. Thank you very much."
            $ ValueChange("Rosa", itemvalue + 3)
            $ GetItem(Item.Magnet, text="You trade the Magnet for the [itemname], which Rosa accepts.")

        else:
            rosa @talkingmouth "Suuuure. That, um, that kinda works."
            $ ValueChange("Rosa", itemvalue + 3)
            $ GetItem(Item.Magnet, text="You trade the Magnet for the [itemname], which Rosa good-naturedly accepts.")

    else:
        jump starttrade

    label afterrosamagnettrade:

    red @happy "Thanks!"

    rosa @talkingmouth "Not a problem! Now, sorry, I gotta run."

    red @talkingmouth "Take care."

    return