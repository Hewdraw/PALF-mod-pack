init python:
    def oldmandialog(attributes):
        if (Turn == 0):
            renpy.call_in_new_context("oldmandialog0")

label oldmandialog0:
    hide screen battle
    show screen battleui
    show red:
        xpos 0.33
    show oldman milotic:
        xpos 0.66
    with dis

    red @surprised "Wait, two Pokémon?"

    oldman @surprisedbrow happymouth "What, lad? Weren't you listenin'? This entire round will be double battles!"

    red @sweat happymouth closedbrow "Oops. I've been out of the region for a bit, so I guess I missed the part where they told us that."

    oldman @happybrow happymouth "Eheheh! Looks like I've got the upper hand here, then!"

    red @talkingmouth "Maybe, but I'm still confident in [pika_name]. C'mon, buddy! Let's do this!"

    $ renpy.music.play("Audio/Pokemon/pikachu_angry1.ogg", channel="altcry", loop=None)
    pikachu cocky_2b "Pika! Pika!"

    hide red 
    hide oldman
    show screen battle
    with dis
    return

init python:
    def dawndragonitedialog(attributes):
        if ("BeforeBattle" in attributes and Turn == 0):
            renpy.call_in_new_context("dawndragonitedialog0")
        elif ("PreStep" in attributes and Turn == 1):
            renpy.call_in_new_context("dawndragonitedialog1")
        elif ("AfterMove" in attributes and "Ally" in attributes and Turn == 1):
            renpy.call_in_new_context("dawndragonitedialog2")

label dawndragonitedialog0:
    hide screen battle
    show screen battleui
    show red sadbrow frownmouth:
        xpos 0.33
    show dawn sad:
        xpos 0.66
    with dis

    dawn @sad "So... you're using Lance's Dragonite..."

    red @sad "Look..."

    hide red 
    hide dawn
    show screen battle
    with dis
    return

label dawndragonitedialog1:
    hide screen battle
    show screen battleui
    show red sadbrow frownmouth:
        xpos 0.33
    show dawn sad:
        xpos 0.66
    with dis

    dawn @closedbrow frownmouth "I guess all you really cared about was power, after all."
    dawn @angrybrow sadmouth "Maybe you really are mind-controlling people, huh?"

    red @angry "No!"

    show dawnbreakstheicebg1 
    hide screen battleui
    with Dissolve(3.0)

    dawn angrybrow frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."

    show dawnbreakstheicedawn with Dissolve(3.0)

    dawn "It doesn't matter."

    show dawnbreakstheiceblizzard with Dissolve(3.0)

    dawn "For my entire life, I've been living in a cage. It's cold, and harsh, and I've had to live in it alone. Too weak for a champion, and too powerful for everyone else."
    dawn "But when I tried to get away from all that, and just do my own thing, people said I was wasting my potential."

    pause 1.0

    dawn "Fine. Here's my potential--the {i}true{/i} potential of my partner and I!"

    show dawnbreakstheicedawnlight behind dawnbreakstheiceblizzard with dis

    narrator "Altaria's Altarianite is reacting to Dawn's Mega Chisel!"

    pause 1.0

    $ PlaySound("megaevo.ogg")

    show dawnbreakstheicebg2 behind dawnbreakstheicedawnlight
    show dawnbreakstheicealtarialight behind dawnbreakstheicedawnlight
    with dis

    dawn "Altaria! Break the chains of ice! Eliminate all restrictions, and show the dark of night a new dawn! Mega Evolution!"

    $ EnemyBattlers()[0].ChangeForme(334.1)
    $ EnemyBattlers()[0].ApplyStatus("mega evolved")

    dawn @angrybrow happymouth "Altaria, now's your time! We won't be taken down without a fight--Cotton Guard, now!"

    hide red 
    hide dawn
    hide dawnbreakstheicealtarialight
    hide dawnbreakstheicebg1
    hide dawnbreakstheicebg2
    hide dawnbreakstheicedawn
    hide dawnbreakstheicedawnlight
    hide dawnbreakstheiceblizzard
    show screen battle
    with dis
    return

label dawndragonitedialog2:
    hide screen battle
    show screen battleui
    show red surprised:
        xpos 0.33
    show dawn angrybrow happymouth:
        xpos 0.66
    with dis

    red @talkingmouth "Wait... that didn't K.O.?"

    dawn @angrybrow happymouth "It sure didn't! We've got them, Altaria! Just make sure that you don't get hit critically, and we've got this!"

    dawn @happy "Altaria, Altaria, you're the one! You've got power, you've got fun! You're the best, you're the star! We're gonna win--and we'll go far!"

    $ ApplyEffect(dawnaltariaobj, "lucky", 999, False)

    narrator "Dawn started a Lucky Chant!"

    redmind @confusedeyebrows playfuleyes frownmouth "That doesn't seem fair."

    hide red 
    hide dawn
    show screen battle
    with dis
    return

init python:
    def dawnpikachudialog(attributes):
        global allowfractions
        allowfractions = True
        if ("BeforeBattle" in attributes and Turn == 0 and "dawnpikachudialog0" not in dialogshown):
            renpy.call_in_new_context("dawnpikachudialog0")
            dialogshown.append("dawnpikachudialog0")
        elif ("AfterMove" in attributes and movesdodged == [] and "Enemy" in attributes and len(FriendlyUnfainteds()) == 1 and "dawnpikachudialog1" not in dialogshown):
            renpy.call_in_new_context("dawnpikachudialog1")
            dialogshown.append("dawnpikachudialog1")
        elif ("AfterMove" in attributes and len(movesdodged) == 1 and "Enemy" in attributes and len(FriendlyUnfainteds()) == 1 and "dawnpikachudialog2" not in dialogshown):
            renpy.call_in_new_context("dawnpikachudialog2")
            dialogshown.append("dawnpikachudialog2")
        elif ("PostTurn" in attributes and len(movesdodged) == 2 and len(FriendlyUnfainteds()) == 1 and "dawnpikachudialog3" not in dialogshown):
            renpy.call_in_new_context("dawnpikachudialog3")
            dialogshown.append("dawnpikachudialog3")
        elif ("PostTurn" in attributes and len(movesdodged) == 3 and len(FriendlyUnfainteds()) == 1 and "dawnpikachudialog4" not in dialogshown):
            renpy.call_in_new_context("dawnpikachudialog4")
            dialogshown.append("dawnpikachudialog4")
        elif ("PostTurn" in attributes and len(movesdodged) == 4 and len(FriendlyUnfainteds()) == 1 and "dawnpikachudialog5" not in dialogshown):
            renpy.call_in_new_context("dawnpikachudialog5")
            dialogshown.append("dawnpikachudialog5")
        elif ("AfterMove" in attributes and "Enemy" in attributes and len(movesdodged) ==  5 and len(FriendlyUnfainteds()) == 1 and "dawnpikachudialog7" not in dialogshown):
            renpy.call_in_new_context("dawnpikachudialog7")
            dialogshown.append("dawnpikachudialog7")
        elif ("PostTurn" in attributes and len(movesdodged) == 6 and len(FriendlyUnfainteds()) == 1 and "dawnpikachudialog8" not in dialogshown):
            renpy.call_in_new_context("dawnpikachudialog8")
            dialogshown.append("dawnpikachudialog8")
        elif ("PostTurn" in attributes and len(movesdodged) == 7 and len(FriendlyUnfainteds()) == 1 and "dawnpikachudialog9" not in dialogshown):
            renpy.call_in_new_context("dawnpikachudialog9")
            dialogshown.append("dawnpikachudialog9")
        elif ("PostTurn" in attributes and len(movesdodged) == 8 and len(FriendlyUnfainteds()) == 1 and "dawnpikachudialog10" not in dialogshown):
            renpy.call_in_new_context("dawnpikachudialog10")
            dialogshown.append("dawnpikachudialog10")
        elif ("AfterMove" in attributes and "Enemy" in attributes and len(movesdodged) == 9 and len(FriendlyUnfainteds()) == 1 and "dawnpikachudialog11" not in dialogshown):
            renpy.call_in_new_context("dawnpikachudialog11")
            dialogshown.append("dawnpikachudialog11")
        elif ("UseItem" in attributes and "Enemy" in attributes and "dawnpikachuitemdialog" not in dialogshown):
            renpy.call_in_new_context("dawnpikachuitemdialog")
            dialogshown.append("dawnpikachuitemdialog")

label dawnpikachuitemdialog:
    hide screen battle
    show screen battleui
    show red:
        xpos 0.33
    show dawn:
        xpos 0.66
    with dis

    red @confused "Dang, you have items...?"

    dawn @surprised "I can't believe I actually have to use them here...!"

    $ ValueChange("Dawn", 3, 0.9, False)

    dawn @happy "I'm really impressed, [first_name]. The only other time I had to use items was..."
    dawn @sadbrow happymouth "Well, I {i}lost{/i} that time."

    red @happy "Heh. I think those kinds of items are a bit out of my budget right now, though..."

    dawn @sadbrow happymouth "Well, um... maybe I should just let you know I have a {i}lot{/i} more..."

    red @sweat closedbrow talking2mouth "Noted."
    redmind @thinking "Mannn... Rich people, am I right?"

    hide red 
    hide dawn
    show screen battle
    with dis
    return

label dawnpikachudialog0:
    hide screen battle
    show screen battleui
    show red:
        xpos 0.33
    show dawn:
        xpos 0.66
    with dis

    dawn @happy "Thank you, [first_name]. I never thought I'd get to have another battle like this."

    red @happy "I can't even imagine what you've gone through, but I can tell you shouldn't have had to go through it. Giving you a fun battle is the least I can do."

    redmind @thinking "Admittedly, there's absolutely no way I'm going to win this, but... at least no-one's giving up. And not having to worry about who 'wins' or 'loses' is freeing."

    pause 1.0

    redmind @sweat closedbrow frownmouth "That being said. A level 68 Altaria? What's she even doing in this school? She could be battling Champions already..."

    hide red 
    hide dawn
    show screen battle
    with dis
    return

label dawnpikachudialog1:
    hide screen battle
    show screen battleui
    show red sadbrow:
        xpos 0.33
    show dawn sadbrow:
        xpos 0.66
    with dis

    dawn @talkingmouth "I guess... I guess this is it, then."

    red @talkingmouth "Eh, I wouldn't rule out [pika_name]. Not yet, anyway."

    dawn @sadbrow talkingmouth "It's nice that you believe in him, but... every odd is kinda stacked against you right now, isn't it?"

    red -sadbrow @happy "Not every odd. I still have [pika_name], and as long as I have him, I have all the odds I need."

    $ renpy.music.play("Audio/Pokemon/pikachu_angry1.ogg", channel="altcry", loop=None)
    pikachu cocky_2b "Pika! Pika!"

    pause 1.0

    dawn @talkingmouth "I... I remember what that was like... to believe so absolutely, and so truly, in my partners, in my friends..."

    pause 1.0

    dawn @sadbrow happymouth "Thank you."

    dawn angry "Altaria, finish this. Dragon Pulse."

    hide red 
    hide dawn
    show screen battle
    with dis
    return

label dawnpikachudialog2:
    hide screen battle
    show screen battleui
    show red surprised:
        xpos 0.33
    show dawn surprised:
        xpos 0.66
    with dis

    dawn "Um...? What was that?"

    red @confused "Beats me. [pika_name]?"

    $ renpy.music.play("Audio/Pokemon/pikachu_angry1.ogg", channel="altcry", loop=None)
    pikachu cocky_2b "Pika! Pika!"

    narrator "{glitch=5.00}...Something's stirring. The whisper of liberation echoes again...{/glitch}"

    hide red 
    hide dawn
    show screen battle
    with dis
    return

label dawnpikachudialog3:
    hide screen battle
    show screen battleui
    show red surprised:
        xpos 0.33
    show dawn surprised:
        xpos 0.66
    with dis

    dawn "Why... {i}how{/i} is your Pikachu still holding on?"

    red @happy "I've got no idea, but let's press this advantage!"

    $ renpy.music.play("Audio/Pokemon/pikachu_angry2.ogg", channel="altcry", loop=None)
    pikachu cocky_2b "Ka... Pikachu!"

    narrator "{glitch=10.00}...Something's approaching. The murmur of liberation gets louder still.{/glitch}"

    hide red 
    hide dawn
    show screen battle
    with dis
    return

label dawnpikachudialog4:
    hide screen battle
    show screen battleui
    show red:
        xpos 0.33
    show dawn surprised:
        xpos 0.66
    with dis

    dawn "Whaaaat is happening?"

    red @happy "A Pokémon battle? This is a real battle, Dawn! Stuff happens, and no-one knows why! When was the last time you were surprised?"

    $ renpy.music.play("Audio/Pokemon/pikachu_angry2.ogg", channel="altcry", loop=None)
    pikachu cocky_2b "Ka... Pikapi!"

    narrator "{glitch=15.00}It's getting closer! The shout of liberation is heard clearly!{/glitch}"

    hide red 
    hide dawn
    show screen battle
    with dis
    return

label dawnpikachudialog5:
    hide screen battle
    show screen battleui
    show red happy:
        xpos 0.33
    show dawn closedbrow frownmouth:
        xpos 0.66
    with dis

    dawn @talkingmouth "I've never seen anything like this before--is this what Cynthia was trying to show me?"

    red @surprised "You've talked to Cynthia?"

    dawn @angrybrow happymouth "I {i}battled{/i} Cynthia! And a Pokémon that battled Cynthia can more than handle a tiny Pikachu! Altaria, use your most powerful Dragon Pulse!"

    $ renpy.music.play("Audio/Pokemon/pikachu_angry3.ogg", channel="altcry", loop=None)
    pikachu cocky_2b "Pikaaaaaaaachu!"

    narrator "{glitch=20.00}It's right nearby! It's gusting hard! The scream of liberation will never be silenced!{/glitch}"

    narrator "{glitch=20.00}A new option has appeared to you...{/glitch}"

    hide red 
    hide dawn
    show screen battle
    with dis
    return

label dawnpikachudialog6:
    $ renpy.music.set_volume(0.0, 5.0)
    hide blank2
    hide screen battleui
    hide screen battle
    show blank2
    show sugimoripikachu:
        xpos 200  
        yanchor 1.0 
        ypos 1.0 
        xzoom -1.0
        pause 5.0
        ease 3.0 xpos 960 xanchor 0.5 yalign 0.5
        pause 2.0
        alpha 0.0
    with Dissolve(5.0)

    pause 3.0

    python:
        pikachuobj.Id = 25.2
        pikachuobj.Nature = Natures.Brave
        pikachuobj.RecalculateStats()
        pikachuobj.Health = pikachuobj.GetStat(Stats.Health)
        renpy.music.queue("audio/music/evolution_cut.ogg", channel="evolution")
        renpy.call_screen("evolution", 25, 25.2, True)
        renpy.music.stop(channel="evolution")
        PlaySound("Get.ogg")
        renpy.music.set_volume(1.0, 3.0)

    stop music fadeout 1.5
    queue music "audio/music/theme_start.ogg" noloop fadein 7.0
    queue music "audio/music/theme_loop.ogg"

    hide sugimoripikachu
    hide blank2
    hide screen battleui
    show screen battleui
    with dis

    pause 2.0

    label pickbanner:

    narrator "The banner of liberation flies again!"

    narrator "What color will your banner be?"

    $ renpy.call_screen("liberize")

    if (len(libtypes) == 0):
        narrator "You must pick a banner to fly! Liberation has no room for bystanders!"

        jump pickbanner

    $ types = libtypes[0]
    if (len(libtypes) == 2):
        $ types = libtypes[0] + "/" + libtypes[1]

    narrator "Do you want to raise up the banner of the [types]-type?"

    menu:
        "Let me fight for another cause.":
            jump pickbanner

        "Raise it high!":
            pass

    narrator "It is so."

    pause 1.0

    show red surprised:
        xpos 0.33
    show dawn surprised:
        xpos 0.66
    with dis

    dawn "What the heck is that?! Is that some kind of Pikachu evolution I've never heard of?"

    red @talkingmouth "I have no idea... buddy, are you good?"

    $ renpy.music.play("Audio/Pokemon/pikachu_angry3.ogg", channel="altcry", loop=None)

    libpikachu glowing @angryeyes happymouth sparks "Pik... Pika. Pikerachu!"

    red -surprised @happy "Looks like he's still firing on all cylinders!"

    red @talkingmouth "Well, Dawn?"

    dawn "I-- I have {i}no{/i} idea what's happening! Altaria, another Dragon Pulse!"

    redmind @thinking "...I think I might know why she didn't win against Cynthia. She's kind of a one-track-minded battler, huh?"

    $ renpy.music.play("Audio/Pokemon/pikachu_scared.ogg", channel="altcry", loop=None)

    libpikachu @angry2eyes surprisedmouth "Pik... Pika. Pikerachu!"

    redmind @thinking "He's being brave, but... that's still my [pika_name]. I can tell that he's worried about getting hit again."
    redmind @angrybrow frownmouth "I don't understand this power, but if I want to have any chance of winning, [bluecolor]I need to think about what Dawn is likely to do, and Liberize accordingly.{/color}"
    redmind @closedbrow frownmouth "[bluecolor]Right now, she's planning on using a {i}Dragon Pulse{/i}...{/color}"

    hide red
    hide dawn
    with dis

    return

label dawnpikachudialog7:
    hide screen battle
    show screen battleui
    show red happy:
        xpos 0.33
    show dawn angrybrow happymouth:
        xpos 0.66
    with dis

    dawn @talkingmouth "Pretty sneaky of you, [first_name]! Is this some kind of crazy Terastallization power?"

    red @winkeyes talkingmouth "You wouldn't believe me if I told you what it was."

    pause 1.0

    dawn @surprisedbrow sadmouth "Wait, you have no idea what this is, do you?"

    red @happy "Hah, hah! You caught me! Nope!"

    dawn @happy "Well, that was a clever trick, absorbing my Dragon-type move with your Fairy-type transformation! But can you take an Earthquake?"

    hide red 
    hide dawn
    show screen battle
    with dis
    return

label dawnpikachudialog8:
    hide screen battle
    show screen battleui
    show red happy:
        xpos 0.33
    show dawn happy:
        xpos 0.66
    with dis

    dawn "Oh, you dodged that too... well, how about we show him this next move, Altaria? Maybe we can turn their bad luck into some good luck for us..."

    dawn @angrybrow happymouth "Altaria, use Ominous Wind!"

    red @angrybrow happymouth "[pika_name], we're not out yet!"

    hide red 
    hide dawn
    show screen battle
    with dis
    return

label dawnpikachudialog9:
    hide screen battle
    show screen battleui
    show red happy:
        xpos 0.33
    show dawn happy:
        xpos 0.66
    with dis

    dawn "Hah! Guess you figured that one out, then... well, we're not going to give up yet! We'll make our voices be heard!"

    dawn @angrybrow happymouth "Altaria, Hyper Voice!"

    hide red 
    hide dawn
    show screen battle
    with dis
    return

label dawnpikachudialog10:
    hide screen battle
    show screen battleui
    show red happy:
        xpos 0.33
    show dawn happy:
        xpos 0.66
    with dis

    red @happy "Hm... correct me if I'm wrong, but that's four moves, right? Unless Janine taught you how to use a fifth move, I'm pretty sure that means you can't hit me."
    
    red @sweat talking2mouth "Of course... nothing's immune to the Fairy-type..."

    red @angrybrow happymouth "So does this mean I've finally earned the right to see your Mega Altaria?"

    dawn -happy @sadbrow happymouth "...[first_name], this has been the most fun I've ever had in a battle."

    red -happy @happy "I'm glad. I didn't expect any of {i}this{/i} would happen--but as long as you come out of this happy, then... hey, I'd call that a win."

    show dawnbreakstheicebg1 
    hide screen battleui
    with Dissolve(3.0)

    show dawnbreakstheicedawn with Dissolve(3.0)

    dawn "[first_name]... there's something I want you to understand."

    show dawnbreakstheiceblizzard with Dissolve(3.0)

    dawn "For my entire life, I've been living in a cage. It's cold, and harsh, and I've had to live in it alone. I was too weak to be a champion, but too powerful for everyone else."
    dawn "But when I tried to get away from all that, and just do my own thing, people said I was wasting my potential."

    pause 1.0

    dawn "But you... just now... you saw me for more than my potential. You saw me for who I am. Right now. In this moment."
    dawn "And that... unlike {i}anything{/i} else... made me want to show you my potential."
    dawn "So here's my potential, [first_name]. My true power. The {i}true{/i} potential of my partner and I!"

    show dawnbreakstheicedawnlight behind dawnbreakstheiceblizzard with dis

    narrator "Altaria's Altarianite is reacting to Dawn's Mega Chisel!"

    pause 1.0

    $ PlaySound("megaevo.ogg")

    show dawnbreakstheicebg2 behind dawnbreakstheicedawnlight
    show dawnbreakstheicealtarialight behind dawnbreakstheicedawnlight
    with dis

    dawn "Altaria! Break the chains of ice! Eliminate all restrictions, and show the dark of night a new dawn! Mega Evolution!"

    $ EnemyBattlers()[0].ChangeForme(334.1)
    $ EnemyBattlers()[0].ApplyStatus("mega evolved")

    dawn angrybrow talking2mouth "Altaria, now's your time! Sing the ultimate song--use your true, full-power Hyper Voice!"

    red angrybrow talking2mouth "[pika_name]! I believe in you! I 100%% know you can win this! So attack, with everything you've got!"

    $ PlaySound("finalsmash.ogg")

    libpikachu @angry2eyes happymouth sparks "Pikera.... CHUUUUUU!"

    $ pikachuobj.LearnNewMove([(1, "Liberage")])

    hide dawnbreakstheicealtarialight
    hide dawnbreakstheicebg1
    hide dawnbreakstheicebg2
    hide dawnbreakstheicedawn
    hide dawnbreakstheicedawnlight
    hide dawnbreakstheiceblizzard
    show screen battle
    with dis
    return

label dawnpikachudialog11:
    $ renpy.music.set_volume(0.0, 5.0)
    hide blank2
    hide screen battleui
    show blank2
    show liberationpikachu:
        xpos 200  
        yanchor 1.0 
        ypos 1.0 
        xzoom -1.0
        pause 2.0
        ease 2.0 ypos 0.7
    show liberationpikachutail:
        xpos 200  
        yanchor 1.0 
        ypos 1.0 
        xzoom -1.0
        matrixcolor TintMatrix(GetLiberaColor())
        pause 2.0
        ease 2.0 ypos 0.7
    show liberationpikachucollar:
        xpos 200  
        yanchor 1.0 
        ypos 1.0 
        xzoom -1.0
        matrixcolor TintMatrix(GetLiberaColor(False))
        pause 2.0
        ease 2.0 ypos 0.7
    show megaaltaria:
        xpos 1720
        xanchor 1.0  
        yanchor 1.0 
        ypos 1.0
        pause 2.0
        ease 2.0 ypos 0.7
    with Dissolve(5.0)

    pause 3.0

    show liberationpikachu:
        ease 3.0 xpos 100
        ease 0.3 xpos 960

    show liberationpikachutail:
        ease 3.0 xpos 100
        ease 0.3 xpos 960

    show liberationpikachucollar:
        ease 3.0 xpos 100
        ease 0.3 xpos 960

    show megaaltaria:
        ease 3.0 xpos 1820
        ease 0.3 xpos 960

    stop music fadeout 1.5

    pause 3.0

    show blank with spinfaderapid

    pause 3.0

    lisia @surprised "{cps=*0.3}It's... {/cps}{cps=*0.2}it's...!"
    lisia @surprised "{cps=*0.05}It's a d{w=1.0}{/cps}{nw}"

    $ EnemyBattlers()[0].Health = 0
    show screen battleui
    hide blank
    hide blank2
    hide liberationpikachu
    hide liberationpikachucollar
    hide liberationpikachutail
    hide megaaltaria

    extend @happy "efeat for Dawn!"

    lisia @surprised "Surprising absolutely everybody, [first_name] [last_name] is the winner!"

    return

init python:
    def deoxysdialog(attributes):
        currentscene = None
        if (len(EnemyBattlers()) == 0):
            currentscene = "deoxysabort"
        elif (Turn == 1):
            currentscene = "deoxysdialog0"
        elif (Turn == 2):
            currentscene = "deoxysdialog1"
        elif (Turn == 3):
            currentscene = "deoxysdialog2"
        elif (Turn == 4):
            currentscene = "deoxysdialog3"
        elif (Turn == 5):
            currentscene = "deoxysdialog4"

        if (currentscene != None and currentscene not in seencutscenes):
            seencutscenes.append(currentscene)
            renpy.call_in_new_context(currentscene)

label deoxysdialog0:
    hide screen battle
    show screen battleui
    show nate angrybrow frownmouth 
    with dis

    nate @talking2mouth "Keep this thing occupied! Don't let it get to [pika_name]!"

    blue @surprised "What am I, his damn guardian?"

    nate @talking2mouth "AZOTH1 has the ability to absorb and assimilate genetic material! We can't let it get access to that special Pikachu's power!"

    blue @angry "Psh! That rat only {i}got{/i} its power by taking it from Azoth in the first place! To me, it looks like Azoth is just taking back what [first_name] stole!"

    nate @talking2mouth "Look, just don't let it get past you!"

    blue @angrybrow happymouth "Easy! I'll put this thing in the ground, {i}again!{/i}"

    show nate:
        xpos 0.5
        ease 0.5 xpos 0.33

    show yellow sad with dis:
        xpos 0.66

    yellow @talking2mouth "W-wait! Don't hurt them!"

    nate @angry "Right now, we should be more worried about {i}it{/i} hurting {i}us{/i}!"

    hide nate
    hide yellow
    show screen battle
    with dis
    return

label deoxysdialog1:
    hide screen battle
    show screen battleui
    show nate angrybrow frownmouth 
    with dis

    nate @talking2mouth "Keep holding on! I'm locking onto it now!"

    if (len(FriendlyUnfainteds()) == 5):
        blue @desperateeyes scaredmouth "Hey, hey! This thing just one-shot my Pokémon! How much longer do you need me to hold on?"

    else:
        blue @happy "Hey, what do you take me for? I've got this in the bag!"

    hide nate
    show screen battle
    with dis
    return

label deoxysdialog2:
    hide screen battle
    show screen battleui
    show nate angrybrow frownmouth 
    with dis

    nate @talking2mouth "Almost done charging. Get ready!"

    blue @angrybrow talkingmouth "...Right. But... hey, this isn't going to hurt it, will it?"

    nate @surprised "Is that seriously your priority, right now?"

    if (len(FriendlyUnfainteds()) == 5):
        nate @surprised "It's torn through one of your Pokémon already!"
    elif (len(FriendlyUnfainteds()) == 4):
        nate @surprised "It's torn through two of your Pokémon already!"
    elif (len(FriendlyUnfainteds()) == 3):
        nate @surprised "It's torn through three of your Pokémon already!"
    elif (len(FriendlyUnfainteds()) == 2):
        nate @surprised "It's torn through four of your Pokémon already!"
    else:
        blue @talkingmouth "It's not like I'm taking any damage here! I mean, I'm not sure this thing is even all that strong!"

    hide nate
    show screen battle
    with dis
    return

label deoxysdialog3:
    hide screen battle
    show screen battleui
    show nate angrybrow frownmouth 
    with dis

    nate @talking2mouth "Okay, I'm done charging! Get out of the way!"

    blue @sad2eyes wistfulmouth "I'm not sure this is the only way, Nate! I mean, we've got Yellow, who can tell what Pokémon are feeling, and we've got [first_name], who Pokémon just {i}listen{/i} to."
    blue @surprisedbrow talkingmouth "Can't we try something else?"

    nate @angrymouth "Not until it calms down! And right now, it's in a frenzied state--it won't listen to us!"

    blue @angry "Rrrghhh... hold off. Just one more round, alright?"

    hide nate
    show screen battle
    with dis
    return

label deoxysdialog4:
    hide screen battle
    show screen battleui
    with dis

    blue @angry "Hey, you two! Are you getting anything from it?"

    show yellow sad:
        xpos 0.66

    show red frownmouth:
        xpos 0.33

    red @talking2mouth "It's completely shutting me out."

    yellow @talking2mouth "It won't listen to me. It's just mindlessly attacking, now..."

    nate @talking2mouth "That's enough, Blue! If you don't move out of the way, you're going to be hurt by my attack!"

    blue @talkingmouth "...Wait, okay? Just wait."

    $ Fled = True

    hide nate
    show screen battle
    with dis
    return

label deoxysabort:
    hide screen battle
    show screen battleui
    with dis

    blue @closedbrow talking2mouth "Look, it's calmed down. Let's try talking things through."

    $ Fled = True
    return

init python:
    def hildahilbertdialog(attributes):
        currentscene = None
        if (len(FriendlyBattlers()) > 0 and AbilityOnOpponentField(FriendlyBattlers()[0], "Moody", splash=False)):
            currentscene = "seesnorunt"

        if (currentscene != None and currentscene not in seencutscenes):
            seencutscenes.append(currentscene)
            renpy.call_in_new_context(currentscene)

label seesnorunt:
    hide screen battle
    show screen battleui
    show leaf surprised uniform:
        xpos 0.25
    with dis

    leaf "Wait a minute! That Snorunt doesn't have a Choice item!"

    show hilbert uniform talkingmouth:
        xpos 0.75

    hilbert @talkingmouth "You've a keen eye. I imagine you recognize what it {i}does{/i} have, then?"

    leaf "Yeah! That's-- that's a {i}Leftovers!{/i}"

    if (len(FriendlyBattlers()) == 2):
        leaf angrybrow frownmouth @talking2mouth "[first_name], we need to take this thing down, before it gets out of control!"

    elif (len(FriendlyBattlers()) == 1 and FriendlyBattlers()[0] in playerparty):
        leaf angrybrow frownmouth @talking2mouth "[first_name], you need to take this thing down, before it gets out of control!"

    else:
        leaf angrybrow frownmouth @talking2mouth "Geez! I gotta take this thing down, before it gets out of control!"

    redmind uniform @confusedeyebrows frownmouth "It's just an apple core... why's she so scared?"

    hide hilbert
    hide leaf
    show screen battle
    with dis
    return

init python:
    def battlewithyellowdialog(attributes):
        currentscene = None
        for trainer in FriendlyTrainers():
            if (len(trainer.GetUnfaintedTeam()) == 0 and trainer.Name == "yellow"):
                currentscene = "yellowembarrassed"

        if (currentscene != None and currentscene not in seencutscenes):
            seencutscenes.append(currentscene)
            renpy.call_in_new_context(currentscene)

label yellowembarrassed:
    hide screen battle
    show screen battleui
    show yellow uniformbraidfront blush sadbrow:
        xpos 0.25
    with dis

    yellow @challengingmouth "W-well... I guess that's me out, then. I'm sorry..."

    hide yellow
    show screen battle
    with dis
    return

init python:
    def firsteeveebattle(attributes):
        currentscene = None
        if (len(EnemyBattlers()) == 1 and EnemyBattlers()[0].GetId() == pokedexlookupname("Eevee", DexMacros.Id)):
            currentscene = "sendouteevee"
        elif (GetTrainerTeam("Blue", "Eevee", False) in FaintedMons):
            currentscene = "eeveelost"

        if (currentscene != None and currentscene not in seencutscenes):
            seencutscenes.append(currentscene)
            renpy.call_in_new_context(currentscene)

label sendouteevee:
    hide screen battle
    show screen battleui
    show blue og angrybrow:
        xpos 0.75
    with dis

    $ AddEvent("Blue", "SawEevee")

    blue @angrybrow happymouth "Here we go, Eevee. Just like we practiced, now! Use your new ability--{i}Tetra Element!{/i}"

    hide blue
    show screen battle
    with dis
    return

label eeveelost:
    hide screen battle
    show screen battleui
    show blue og surprised:
        xpos 0.75
    with dis

    $ AddEvent("Blue", "KOEevee")

    blue "Wait. Eevee lost? He... {i}lost?{/i}"

    if (len(EnemyUnfainteds()) > 0):
        pause 1.0

        blue @angry "Damn it! But this fight's not over yet!"

        if (len(EnemyUnfainteds()) == 1):
            blue @angry "I've got one more Pokémon left, and as long as I have one, I can win this!"

        else:
            blue @angry "I've got more Pokémon left, and as long as I have one, I can win this!"

    else:
        blue @closedbrow talking2mouth "He was my last Pokémon... Damn it."

    hide blue
    show screen battle
    with dis
    return

init python:
    def dawnrematch2to3(attributes):
        currentscene = None
        if (len(EnemyBattlers()) == 1 and pokedexlookupname("Cyclizar", DexMacros.Id) == EnemyBattlers()[0].GetId()):
            currentscene = "seecyclizar"

        if (currentscene != None and currentscene not in seencutscenes):
            seencutscenes.append(currentscene)
            renpy.call_in_new_context(currentscene)

label seecyclizar:
    hide screen battle
    show screen battleui
    show red uniform:
        xpos 0.15
    show dawn uniform:
        xpos 0.85
    with dis

    $ AddEvent("Dawn", "SawCyclizar")

    if (not HasEvent("Ethan", "IgnoredFrenzyConfession")):
        red @talkingmouth "Hey, that's new. You didn't have a Cyclizar the last time we battled."

        dawn @sadbrow talkingmouth "I caught it for Professor Cherry, but I'm not sure it fits onto my team properly... it's a bit too fast. I might trade it to someone else."

    else:
        red @talkingmouth "A Cyclizar? That doesn't seem to be your speed."

        dawn @sadbrow talkingmouth "Yeah... it's a bit {i}too{/i} fast, actually. I caught it for Professor Cherry, but I'm not sure it fits onto my team properly... I might trade it to someone else."

    red @happy "Good luck with that."

    hide dawn
    hide red
    show screen battle
    with dis
    return

init python:
    def melodyinterruption(attributes):
        currentscene = None
        if ("PostTurn" in attributes and Turn == 2):
            currentscene = "melodyinterruption1"
        elif ("PostTurn" in attributes and Turn == 4):
            currentscene = "melodyinterruption2"
        elif ("PostTurn" in attributes and Turn == 6):
            currentscene = "melodyinterruption3"

        if (currentscene != None and currentscene not in seencutscenes):
            seencutscenes.append(currentscene)
            renpy.call_in_new_context(currentscene)

label melodyinterruption1:
    $ AddEvent("Melody", "Interrupt1")
    hide screen battle
    show screen battleui
    with dis

    narrator "You'd only just bent your head down over your quiz, when..."

    $ PlaySound("door_slam.ogg")

    pause 1.0

    show oak angrybrow frownmouth with dis

    pause 2.0

    oak @talking2mouth "Excuse me! My students are currently taking a test--"

    show melody on:
        xpos 1.2 xzoom -1
        ease 1.5 xpos 0.85

    pause 2.0

    melody @talking2mouth "Lawrence told you to expect me."

    pause 0.5

    melody @surprisedbrow talking2mouth "What's the problem?"

    oak @surprised "Oh? You are... you're Miss Phobos?"

    melody @talking2mouth "No."

    pause 1.0

    melody @talking2mouth "It's Melody."

    oak surprised @closedbrow talking2mouth "...Then, Miss Melody, you should be in your uniform right now."

    melody @talking2mouth "...Yeah, whatever."

    hide melody with dis 

    narrator "Melody walks to a desk in the corner of the room and, ignoring the chair, sits on the desk, bobbing her head to some unseen tune."

    pause 1.0

    show oak angrybrow frownmouth with dis

    redmind @sadbrow frownmouth "Geez. This couldn't have happened at a worst time for Old Man Oak..."

    hide oak with dis

    pause 0.5

    narrator "[bluecolor]You attempt to turn your attention back to the test, but Melody's dramatic entrance continues to distract you from your ability to focus on the test...{/color}"

    $ uifuckery = 1

    show screen battle
    with dis
    return

label melodyinterruption2:
    $ AddEvent("Melody", "Interrupt2")
    hide screen battle
    show screen battleui
    with dis

    show melody on with dis:
        xpos 0.66 xzoom -1

    melody @talking2mouth "So what are we doing?"

    show oak angrybrow frownmouth with dis:
        xpos 0.33

    oak @talking2mouth "My students are currently taking a quiz on the importance of coverage moves--"

    melody @talking2mouth "Seriously? First-week material. It's, what, end of month two?"
    melody @sadbrow talking2mouth "Guess you're {i}that{/i} teacher. Phobos told me about you."

    oak @talking2mouth "Miss Melody, please keep your voice down and try not to distract your classmates while they are taking a quiz."

    melody @talking2mouth "Of course. {i}Real{/i} battles are well-known for being quiet, distraction-free environments. Brilliant."
    melody @surprisedbrow sadmouth "What are you even doing...?"

    narrator "[bluecolor]You frustratedly attempt to turn your attention back to the test, but Melody's aggravating presence continues to distract you from your ability to focus on the test...{/color}"

    $ uifuckery = 2

    show screen battle
    with dis
    return

label melodyinterruption3:
    $ AddEvent("Melody", "Interrupt3")

    hide screen battle
    show screen battleui
    with dis

    show melody on with dis:
        xpos 0.66 xzoom -1

    melody @talking2mouth "So, like, are you going to give me a test, or what?"

    show oak angrybrow frownmouth with vpunch:
        xpos 0.33

    oak @talking2mouth "Miss Melody! Please wait until the quiz is {i}over!{/i} We can discuss when you may make this up {i}later!{/i}"

    melody @talking2mouth "...So I'm taking it after everyone else?"

    pause 1.0

    melody @talking2mouth "That doesn't seem fair."

    oak @talking2mouth "I don't see--"

    melody @sadbrow talking2mouth "If I'm taking it after everyone else, then I could cheat."

    oak @closedbrow talking2mouth "Are you {i}going to{/i}?"

    pause 2.0

    melody @talking2mouth "I could."

    oak @closedbrow sweat talking2mouth "I trust that you will not. {i}For now{/i}, though, {i}please{/i} try not to interrupt any further."

    hide melody
    hide oak
    with dis

    pause 1.0

    narrator "[bluecolor]You grind your teeth and keep your nose to your paper, though your concentration, at this point, is almost completely shattered.{/color}"

    $ uifuckery = 3

    show screen battle
    with dis
    return

init python:
    def firstpichubattle(attributes):
        currentscene = None

        faintedcheck = False
        for mon in FaintedMons:
            if (mon.GetId() == 172.1):
                faintedcheck = True

        if (172.1 in EnemySpecies()):
            currentscene = "sendoutpichu"
        elif (faintedcheck):
            currentscene = "pichulost"

        if (currentscene != None and currentscene not in seencutscenes):
            seencutscenes.append(currentscene)
            renpy.call_in_new_context(currentscene)

label sendoutpichu:
    hide screen battle
    show screen battleui
    show ethan:
        xpos 0.85
    with dis

    $ AddEvent("Ethan", "SawPichu")

    ethan @happy "Alright, Pichu! We just got a new power-up--let's see what it does!"

    if (GetWinLoss("Ethan")[0] > 0):
        ethan @confused "Hey, is it just me, or does Pichu look a bit tougher than before...?"

    hide ethan
    show screen battle
    with dis
    return

label pichulost:
    hide screen battle
    show screen battleui
    show ethan:
        xpos 0.85
    with dis

    $ AddEvent("Ethan", "KOPichu")

    ethan @sad2eyes sadeyebrows talking2mouth "Man... figures."
    ethan @happy "Ah, well, don't know what I was expecting. We got a power-up, not an 'I Win' button."

    if (len(EnemyUnfainteds()) > 0):
        pause 1.0

        ethan @closedbrow talkingmouth "Anyway, this fight isn't done until one of us is out of lives."

        if (len(EnemyUnfainteds()) == 1):
            ethan @winkbrow talkingmouth "And it looks to me like I've still got one left."

        else:
            ethan @winkbrow talkingmouth "And it looks to me like I've got some left."

    else:
        ethan @closedbrow sweat talking2mouth "GG, man."

    hide ethan
    show screen battle
    with dis
    return

init python:
    def firstmelodybattle(attributes):
        currentscene = None

        highestlevel = 0
        for mon in FriendlyBattlers():
            if (mon.GetLevel() > highestlevel):
                highestlevel = mon.GetLevel()
                removeevent = None
                for event in persondex["Melody"]["Events"]:
                    if ("HighestLevelSeen" in event):
                        removeevent = event
                RemoveEvent("Melody", removeevent)
                AddEvent("Melody", "HighestLevelSeen" + str(highestlevel))

        if (len(EnemyBattlers()) > 0 and EnemyBattlers()[0].Id == pokedexlookup("Wimpod", DexMacros.Id)):
            currentscene = "seewimpod"
        elif (len(EnemyBattlers()) > 0 and EnemyBattlers()[0].Id == pokedexlookup("Falinks", DexMacros.Id)):
            currentscene = "seefalinks"

        if (currentscene != None and currentscene not in seencutscenes):
            seencutscenes.append(currentscene)
            renpy.call_in_new_context(currentscene)

label seewimpod:
    hide screen battle
    show screen battleui
    show red battleteam surprised:
        xpos 0.15
    show melody bubblemouth on:
        xpos 0.85 xzoom -1
    with dis

    red "Woah, woah, woah! Hold on! What's that?"

    melody -bubblemouth @talking2mouth "What, Wimpod's bling? Just some rock. Gives it a couple powers. Don't worry about it."

    redmind @sadbrow frownmouth "How can I {i}not{/i} worry about it?! How the hell did she get a Foreveral?!"
    redmind angrybrow frownmouth "Wait..."

    show blue battleteam surprised with dis

    blue "[first_name], I know what you're thinking, and it wasn't me!"

    redmind @sad2eyes angryeyebrows frownmouth "But then... who... and how?"

    hide melody 
    hide red
    hide blue
    show screen battle
    with dis
    return

label seefalinks:
    hide screen battle
    show screen battleui

    $ AddEvent("Melody", "SawFalinks")

    redmind battleteam @confused "Hm? That's a pretty weak Falinks. What's she doing with that on her team?"

    show screen battle
    with dis
    return

init python:
    def mismagiusbattle(attributes):
        currentscene = None
        if (attributes == "PreStep"):
            currentscene = "teramagius"
        elif (attributes == "FailToCatch"):
            currentscene = "trainermagius"

        if (currentscene != None and currentscene not in seencutscenes):
            seencutscenes.append(currentscene)
            renpy.call_in_new_context(currentscene)

label teramagius:
    hide screen battle
    show screen battleui

    narrator "A strange yellow light gathers around Mismagius... {w=1.5}crystals begin to form...{w=1.5} {nw}"
    
    $ eb().Terastallized = Turn
    
    extend "Mismagius has changed dramatically!"

    show red surprisedbrow frownmouth with dis:
        xpos 0.33

    red @surprised "Wait... Terastallization? How?! There's no trainer around, and we're miles from Paldea!"

    pause 1.5

    red @angrybrow talking2mouth "I'll figure that out later. Right now, I've got a ghost to bust."

    hide red
    show screen battle
    with dis
    return

label trainermagius:
    $ AddEvent("Professor Oak", "TriedToCatchIonoMismagius")
    hide screen battle
    show screen battleui

    show red surprisedbrow frownmouth with dis:
        xpos 0.33

    red @surprised "What? My Poké Balls aren't locking onto the Mismagius--this must be a trainer's Pokémon!"
    
    if ("teramagius" in seencutscenes):
        red @confused "I guess that explains the Terastallization...? But if it's a trainer who's Terastallizing it, where {i}are{/i} they?"
    else:
        red @confused "But... I don't see one around. And if there {i}is{/i} one, then {i}why{/i} are they battling us?"

    pause 1.0

    red @angrybrow talking2mouth "One thing at a time. C'mon, [fb().GetNickname()]! Let's bring it home!"

    hide red
    show screen battle
    with dis
    return

init python:
    def gardeniafielddialog(attributes):
        currentscene = None
        if (attributes == "EnemySwitch" and eb().GetNickname() == "Phantump"):
            currentscene = "gardeniafieldforfeit"

        if (currentscene != None and currentscene not in seencutscenes):
            seencutscenes.append(currentscene)
            renpy.call_in_new_context(currentscene)

label gardeniafieldforfeit:
    hide screen battle
    show screen battleui

    show red angrybrow:
        xpos 0.33
    show gardenia sadbrow:
        xpos 0.66
    with dis

    if (len(EnemyTrainers()[0].GetUnfaintedTeam()) == 1):
        gardenia @talkingmouth "Oh, I'm down to Phantump..."

        pause 1.0

        show red surprisedbrow frownmouth with dis

        gardenia @happy "Well, I'm definitely not going to be able to win with {i}him{/i}, so I guess you win! I forfeit." 

    else:
        gardenia @talkingmouth "Oh, you brought out Phantump..."

        pause 1.0

        show red surprisedbrow frownmouth with dis

        gardenia @happy "Well, I can tell which way the wind is blowing, and I'm definitely not going to be able to win with {i}him{/i}, so I guess you win! I forfeit." 

    $ AutoWin = True

    hide red
    show screen battle
    with dis
    return

init python:
    def duplicadialog(attributes):
        currentscene = None
        if ("PostTurn" in attributes and eb().GetId() == pokedexlookup("Banette", DexMacros.Id) and eb().Item == Item.Banettite):
            currentscene = "duplicamegaevo"
        elif ("AfterMove" in attributes and "Enemy" in attributes and eb() == GetTrainerTeam("Duplica", "Ditto2", heal=False)):
            currentscene = "hocustransform"

        if (currentscene != None and currentscene not in seencutscenes):
            seencutscenes.append(currentscene)
            renpy.call_in_new_context(currentscene)

label duplicamegaevo:
    hide screen battle
    show screen battleui

    show red angrybrow frownmouth:
        xpos 0.33
    show copyred playfulbrow playfulmouth:
        xpos 0.66 xzoom -1
    with dis

    red @talking2mouth "Enough of this, Copycat! We can talk this out."

    duplica @winkbrow tonguemouth "Hey, bozo! Didya miss a tick? You challenged {i}me{/i}, and that means I've got you in the ring for three minutes!"

    red @talking2mouth "You think it'll take me that long to beat you?"

    duplica @happybrow talking3mouth "Aren't you so adorably confident? Lololol!"
    duplica @winkbrow talkingmouth "You got one thing right, though! We should probably wrap this up, pronto."

    red @talking2mouth "That's the plan."

    duplica @happy "Great minds think alike! But I guess that makes sense, since I'm you."

    red @talking2mouth "You're nothing like me."

    duplica @winkbrow talking3mouth "Wanna bet? I could kiss your Mommy and she wouldn't blink twice."

    red @unamusedbrow talking2mouth "God, can we just get back to the battle?"

    duplica angrybrow smirkmouth @happy "That's exactly what I was thinking!"

    narrator "Her--{i}your{/i} face shifts into an expression of smirking condescension."

    duplica @talkingmouth "Banette, I've taken his name, his face, and his wallet. Make yourself useful and take his dignity!"

    show blank 
    hide screen battleui
    with transeye2

    narrator "Banette's Banettite is reacting to The Copycat's Mega Doll!"
    
    pause 1.0

    $ PlaySound("megaevo.ogg")

    duplica "Banette! Bear the grudge of Rocket's fate for me, until we can copy it again! Hate them all, 'til there's nothing left to hate! Mega Evolution!"

    $ EnemyBattlers()[0].ChangeForme(354.1)
    $ EnemyBattlers()[0].ApplyStatus("mega evolved")

    pause 1.0

    show screen battleui
    show copyred angrybrow noshine smirkmouth shadow
    hide blank 
    with transeye2

    pause 1.0

    duplica @talking3mouth "Like my new toy? It's {i}pointier{/i} than my old one."

    red @talking2mouth "Pokémon aren't toys--they're not dolls, or tools, or weapons. They're not something you collect! They're not something you get to use!"

    duplica @sadbrow talkingmouth "Oh, you sound {i}just{/i} like dear ol' Boss Silver."
    duplica @talking2mouth "Well, I got {i}him{/i} to stop talking back to me. And I think you'll be easier, frankly."
    duplica @angry "All Pokémon exist for the glory of Team Rocket! As long as there's a single loyalist with a single Rattata, Team Rocket will never die!"

    red @angry "Put up or shut up, faker!"

    duplica happy "Lololol! Why so mad?"

    hide copyred
    hide red
    show screen battle
    with dis
    return

label hocustransform:
    hide screen battle
    show screen battleui

    show red surprisedbrow frownmouth:
        xpos 0.33
    show copyred playfulbrow playfulmouth:
        xpos 0.66 xzoom -1
    with dis

    red @talking2mouth "Woah, woah, hold up! Time out! What just happened?!"

    duplica @winkbrow talking3mouth "Did you think you were the only one with a special one-in-a-million Pokémon out there? These things are a dime a dozen for Team Rocket! And I got a dozen of them, for a dime!"

    red -sadbrow @talking2mouth "What?"

    duplica @sad2brow talkingmouth "Okay, that was a joke."

    pause 0.5

    show red angrybrow with dis

    duplica @happybrow talking3mouth "I didn't pay for them! Lololol!"
    duplica @talkingmouth "This little cutie, for example, was taught by my dear Auntie Kasa."
    duplica @closedbrow happymouth "I wouldn't expect a lowbrow goon like you to understand, but I'm a member of High Societea, where advantages like this are common."
    duplica angrybrow frownmouth @happymouth winkbrow "Mr. Giovanni took one look at my special Ditto and brought me onboard! Lololol!"

    red angrybrow @talking2mouth "Yeah, for all the good it did. Team Rocket fell apart right after you joined, didn't it?"

    show copyred shadow with dis

    red @closedbrow talking2mouth "I'm not saying there's a connection, but..."

    duplica @talking2mouth "Stop {i}talking{/i}! Ditto, bring this punk kid down! Team Rocket will never fall to some hay-chewing farmer's brat!"

    redmind sweat "This is her last Pokémon. This ends here..."

    hide copyred
    hide red
    show screen battle
    with dis
    return

init python:
    def rowanbattledialog(attributes):
        currentscene = None
        if ("BeforeBattle" in attributes and Turn == 0):
            currentscene = "rowanbattleintro"
        elif ("AfterMove" in attributes and Turn == 2):
            currentscene = "rowanbattle1"
        elif ("AfterMove" in attributes and Turn == 4):
            currentscene = "rowanbattle2"
        elif ("AfterMove" in attributes and Turn == 6):
            currentscene = "rowanbattle3"

        if (currentscene != None and currentscene not in seencutscenes):
            seencutscenes.append(currentscene)
            renpy.call_in_new_context(currentscene)

label rowanbattleintro:
    hide screen battle
    show screen battleui

    show red surprisedbrow frownmouth:
        xpos 0.33
    show rowan nocoat nocase angrybrow:
        xpos 0.66 xzoom -1
    with dis

    red @surprised "Woah, woah, hold on! A level--level {i}thirty-five{/i} Torterra?!"

    rowan @closedbrow talking2mouth "Did you think this was a joke, [first_name]? Did you think this was a {i}test of character?{/i}"
    rowan @angrybrow talking2mouth "This is a battle, boy! A battle where I will soundly defeat you, unless you treat it like a battle!"

    redmind sadbrow frownmouth "How I {i}treat{/i} it really isn't going to matter here..."
    redmind sweat "I think, right now, I should just try to survive. Maybe something'll come up...? I have to pay attention to {i}every{/i} little thing, in case I find an opening."

    hide rowan
    hide red
    show screen battle
    with dis
    return

label rowanbattle1:
    hide screen battle
    show screen battleui

    $ PlaySound("pokemon/cries/85.mp3")

    TempCharacter("???") "Dooo... Drio! Drio! Drio!"

    show red surprisedbrow frownmouth:
        xpos 0.33
    show rowan nocoat nocase angrybrow:
        xpos 0.66 xzoom -1
    with dis

    red @talking2mouth "Wait. Wait, did you hear that?"

    rowan @angrybrow talking2mouth "Keep your eyes and ears on the battle, boy!"

    hide rowan
    hide red
    show screen battle
    with dis
    return

label rowanbattle2:
    hide screen battle
    show screen battleui

    $ PlaySound("pokemon/cries/85.mp3")

    TempCharacter("???") "Dooo... Drio! Drio! Drio!"

    show red surprisedbrow frownmouth:
        xpos 0.33
    show rowan nocoat nocase angrybrow:
        xpos 0.66 xzoom -1
    with dis

    red @talking2mouth "Profe-- sorry, Rowan, I'm serious! There's a Pokémon crying out somewhere. It sounds like it's in pain."

    rowan @angrybrow talking2mouth "Taking advantage of my poor hearing to try and trick me? Harrumph! No dignity, {i}and{/i} no shame!"

    hide rowan
    hide red
    show screen battle
    with dis
    return

label rowanbattle3:
    $ AddEvent("Professor Rowan", "RunEvents")
    hide screen battle
    show screen battleui

    $ PlaySound("pokemon/cries/85.mp3")

    TempCharacter("???") "Dooodrio! Dododododododrio!"

    narrator "It's unmistakable! That's the cry of a Dodrio, in pain, and not far away, either!"

    show red angrybrow frownmouth:
        xpos 0.33
    show rowan nocoat nocase angrybrow:
        xpos 0.66 xzoom -1
    with dis

    red @talking2mouth "Rowan, there's a Pokémon that needs help! We have to stop this battle {i}now{/i}!"

    rowan @angry "Enough of this nonsense, boy! {b}No! There's no running from a trainer battle!{/b}"

    redmind -angrybrow @closedbrow sadmouth "Damn it. He won't listen to me[ellipses] what would a champion do? A Champion wins every battle, no matter what, right?"

    pause 1.0

    redmind @sadbrow frownmouth "But what's the {i}real{/i} battle I'm fighting here...?"

    hide rowan
    hide red
    show screen battle
    with dis
    return

init python:
    def sycamoredialog(attributes):
        currentscene = None
        if ("BeforeBattle" in attributes):
            currentscene = "sycamorebattleintro"
        elif ("PreStep" in attributes and Turn % 12 == 0 and seencutscenes.count("sycamorebunnyrecruit") < 3):
            currentscene = "sycamorebunnyrecruit"
        elif ("PostTurn" in attributes and eb().Item == Item.Kangaskhanite):
            currentscene = "sycamoremegaevo"

        if (currentscene != None and (currentscene == "sycamorebunnyrecruit" or currentscene not in seencutscenes)):
            seencutscenes.append(currentscene)
            renpy.call_in_new_context(currentscene)

label sycamorebattleintro:
    hide screen battle
    show screen battleui

    redmind uniform @thinking "It looks like almost everyone is here, even the professors. Gotta admit, this is a great opportunity--no-one'll notice me chatting with everyone's focus on the battle."
    redmind @thinking "The longer Blue lasts in battle, the more time I'll have to talk to people. [bluecolor]I think I can probably talk to one person for every twelve turns he lasts{/color}[ellipses] as long as I speak {i}quickly{/i}, anyway."

    pause 1.0

    redmind @unamusedbrow unamusedmouth "I can't believe I'm saying this[ellipses] but good luck, Blue."

    show screen battle
    with dis
    return

label sycamorebunnyrecruit:
    hide screen battle
    show screen battleui

    python:
        bunnyrecruitables = []
        for candidate in GetGymClassCandidates() + ["Kris", "Janine"]:
            if (CanBunnyRecruit(candidate) and candidate not in ["Morty", "Bugsy"]):
                bunnyrecruitables.append((candidate, candidate))

    if (len(bunnyrecruitables) > 0):
        narrator "There's a break in the crowd[ellipses] with everyone's eyes on the battle, now might be the time to discreetly approach someone!"

        python:
            bluebattlechar = renpy.display_menu(bunnyrecruitables)
            renpy.transition(dis)
            renpy.show(GetCharacterSprite(bluebattlechar, None, True))

        "You want to talk to [bluebattlechar]?"

        menu:
            "Yes.":
                call BunnyRecruit(bluebattlechar, True) from _call_BunnyRecruit

            "No.":
                $ renpy.hide(bluebattlechar.lower())

                jump sycamorebunnyrecruit

        if (seencutscenes.count("sycamorebunnyrecruit") >= 3):
            narrator "A decent amount of time has passed, and other students start filtering out of the Battle Hall[ellipses] you signal to Blue that he should try to wrap this up."

    show screen battle
    with dis
    return

label sycamoremegaevo:
    hide screen battle
    show screen battleui

    show blue angrybrow uniform zorder 201:
        xpos 0.1
    show sycamore zorder 201:
        xpos 0.9 xzoom -1
    with dis

    blue @happymouth "{i}Comme je pensé! Moi gagne toi avec presque pas effort. Bonjour! C'est ça le vrai power du Prof de Méga Évolution{/i}?"

    sycamore @happy "Ah-ha-ha! My friend, this battle is only {i}beginning!{/i} I promised you a show of Mega Evolution, did I not?"

    blue @angrybrow "About time. Hit me with {i}everything!{/i}"

    sycamore @talkingmouth "{i}Oui.{/i} Such passion deserves a mirror--let me show you the bonds between my Pokémon and I!"

    narrator "Professor Sycamore casually puts his hand in his pocket, and pulls out a Key Stone."
    narrator "[ellipses]Apparently, attaching it to something else is more of a tradition than a requirement."

    show blank zorder 202
    hide screen battleui
    with transeye2

    narrator "Kangaskhan's Kangaskhanite is reacting to Professor Sycamore's Mega Flair!"
    
    pause 1.0

    $ PlaySound("megaevo.ogg")

    sycamore "Kangaskhan! Show this promising young student the power of bonds between people and Pokémon! Mega Evolution!"

    $ EnemyBattlers()[0].ChangeForme(115.1)
    $ EnemyBattlers()[0].ApplyStatus("mega evolved")

    pause 1.0

    show screen battleui
    show sycamore angrybrow
    hide blank 
    with transeye

    pause 1.0

    sycamore @talkingmouth "{i}Mon ami{/i}, it has been absolutely {i}fantastic{/i} battling with such a motivated and passionate student. But I am afraid this is where your attempt to beat me ends."

    blue @talkingmouth "We'll see about that! Where I'm standing, it looks to me like this is where {i}your{/i} reputation as a great battler ends!"

    sycamore @happy "Passionate words! Passion, passion, passion--fantastic! {i}En garde!{/i}"

    hide sycamore
    hide blue
    show screen battle
    with dis
    return

init python:
    def phobospeanutgallery(attributes):
        global smalltalks
        currentscene = None

        tatsu = GetTrainerTeam("phobos", "Tatsugiri", False)
        if ("PostTurn" in attributes):
            for mon in EnemyBattlers():
                if (mon != None):
                    fvls = mon.GetForeverals()
                    if (fvls == ["Wugtrio Triveral"] and not "wugtrioseen" in seencutscenes):
                        seencutscenes.append("wugtrioseen")
                        smalltalks = [("Ethan", "Guys, that Dugtrio has a Foreveral!"), ("Blue", "That is {i}not{/i} a Dugtrio!"), ("Leaf", "Isn't the Foreveral the bigger problem?!")]
                    elif (mon.GetId() == 993 and not "ironjugulisseen" in seencutscenes):
                        seencutscenes.append("ironjugulisseen")
                        smalltalks = [("Ethan", "That's not a Pokémon, right?"), ("Leaf", "Looks like a Hydreigon...?"), ("Blue", "But it's all wrong.")]
                    elif (fvls == ["Dodrio Overal"] and not "dodrioseen" in seencutscenes):
                        seencutscenes.append("dodrioseen")
                        smalltalks = [("Leaf", "Why does it sound so familiar?"), ("Blue", "It's acting strange..."), ("Ethan", "It's also got a Foreveral.")]
                    elif (fvls == ["Vespiquen Uneveral"] and not "combeeseen" in seencutscenes):
                        seencutscenes.append("combeeseen")
                        smalltalks = [("Blue", "This Combee's going crazy!"), ("Leaf", "Maybe it's the Foreveral...?"), ("Ethan", "How many does Phobos {i}have?!{/i}")]
                    else:
                        smalltalks = []
        elif ("PreChoice" in attributes and tatsu in EnemyBattlers() and tatsu.GetId() != 978.4):
            if ("phobosbattlemegatatsugiri" not in seencutscenes):
                currentscene = "phobosbattlemegatatsugiri"
            else:
                currentscene = "phobosbattlemegatatsugiriskip"

        if (currentscene != None and (currentscene not in seencutscenes or currentscene == 'phobosbattlemegatatsugiriskip')):
            seencutscenes.append(currentscene)
            renpy.call_in_new_context(currentscene)

init python:
    def phobosbattledialog(attributes):
        currentscene = None
        tatsu = GetTrainerTeam("phobos", "Tatsugiri", False)
        if ("BeforeBattle" in attributes and Turn == 0):
            currentscene = "phobosbattleintro"
        elif ("PreChoice" in attributes and tatsu in EnemyBattlers() and tatsu.GetId() != 978.4):
            if ("phobosbattlemegatatsugiri" not in seencutscenes):
                currentscene = "phobosbattlemegatatsugiri"
            else:
                currentscene = "phobosbattlemegatatsugiriskip"

        if (currentscene != None and (currentscene not in seencutscenes or currentscene == 'phobosbattlemegatatsugiriskip')):
            seencutscenes.append(currentscene)
            renpy.call_in_new_context(currentscene)

label phobosbattleintro:
    narrator "{glitch=20}The winds of liberation are howling!{/glitch} [pika_name] is raring to battle!"

    $ PlaySound("Pokemon/pikachu_excite5.ogg")
    libpikachu glowing angry2eyes sparks happy2mouth "Piii-kaaaa-chuuu!"

    if (fb() == pikachuobj):
        narrator "{glitch=20.00}A familiar option has appeared to you.{/glitch}"

    else:
        narrator "{glitch=20.00}A familiar power is flowing out of [pika_name].{/glitch}"

    return

label phobosbattlemegatatsugiri:
    hide screen battle
    show screen battleui
    show phobos angrybrow angrysharkmouth goggles:
        xpos 0.67

    phobos "Bah, so what? You've only defeated the vanguard of my magnificience!"

    narrator "Phobos slams his hand down on his chair, and a Key Stone pops out!"

    show blank
    hide screen battleui
    with transeye2

    narrator "Tatsugiri's Megaveral is reacting to Baron Lawrence Phobos III's Mega Armrest!"
    
    pause 1.0

    $ PlaySound("megaevo.ogg")

    phobos "Tatsugiri! Prove your worth to me! Mega Evolve, and blow these brats away in an outrage of {i}my{/i} elegallantry!"

    $ GetTrainerTeam("phobos", "Tatsugiri", False).ChangeForme(978.4)
    $ GetTrainerTeam("phobos", "Tatsugiri", False).ApplyStatus("mega evolved")

    pause 1.0

    show screen battleui
    hide blank 
    hide phobos
    with transeye

    return

label phobosbattlemegatatsugiriskip:
    $ PlaySound("megaevo.ogg")
    $ GetTrainerTeam("phobos", "Tatsugiri", False).ChangeForme(978.4)
    $ GetTrainerTeam("phobos", "Tatsugiri", False).ApplyStatus("mega evolved")

    return

init python:
    def phobosbattle2dialog(attributes):
        currentscene = None
        revived = False
        
        if ("PreChoice" in attributes and len(EnemyTrainers()[0].GetUnfaintedTeam()) > 0):
            BattleCheck()
            for mon in EnemyPokemon():
                if mon.GetHealth() <= 0 and not mon.HasStatus("recruited"):
                    mon.Heal()
                    PlaySound("Heal_A.ogg")
                    if (not revived):
                        renpy.say(None, "ETERNITY PHOBOS used MAX REVIVE(s)!")
                    revived = True
        
        if ("PreChoice" in attributes and eb() == GetTrainerTeam("phobos", "Dodrio", False)):
            currentscene = "phobosbattle2dodriointro"
        elif ("Call" in attributes and eb() == GetTrainerTeam("phobos", "Dodrio", False)):
            currentscene = "phobosbattle2dodriocall"
        elif ("PreChoice" in attributes and eb() == GetTrainerTeam("phobos", "Wugtrio", False)):
            currentscene = "phobosbattle2wugtriointro"
        elif ("Call" in attributes and eb() == GetTrainerTeam("phobos", "Wugtrio", False)):
            currentscene = "phobosbattle2wugtriocall"
        elif ("PreChoice" in attributes and eb() == GetTrainerTeam("phobos", "Combee", False)):
            currentscene = "phobosbattle2combeeintro"
        elif ("Call" in attributes and eb() == GetTrainerTeam("phobos", "Combee", False)):
            currentscene = "phobosbattle2combeecall"
        elif ("PreChoice" in attributes and eb() == GetTrainerTeam("phobos", "Tatsugiri", False)):
            currentscene = "phobosbattle2tatsugiriintro"
        elif ("Call" in attributes and eb() == GetTrainerTeam("phobos", "Tatsugiri", False)):
            currentscene = "phobosbattle2tatsugiricall"
        elif ("Call" in attributes and eb() == GetTrainerTeam("phobos", "Iron Jugulis", False)):
            currentscene = "phobosbattle2ironjuguliscall"

        if (currentscene != None and currentscene not in seencutscenes):
            seencutscenes.append(currentscene)
            renpy.call_in_new_context(currentscene)

label phobosbattle2dodriointro:
    hide screen battle
    show screen battleui
    show red angrybrow frownmouth zorder 1000:
        xpos 0.1
    show yellow angrybrow frownmouth zorder 1001:
        xpos 0.2 xzoom -1

    yellow @talking2mouth "This Dodrio[ellipses] it's scared, and hurt. It's actually a Doduo, but when that stone was forced onto it, a third mind developed, demanding and absolute."
    yellow @sadbrow talking2mouth "The two other minds just want peace--but with that third mind screaming Phobos' orders at them, they're following his orders just to have a chance at silence."

    hide red
    hide yellow
    hide screen battleui
    with dis

    return

label phobosbattle2dodriocall:
    hide screen battle
    show screen battleui
    show red angrybrow frownmouth zorder 1000:
        xpos 0.1
    show yellow angrybrow frownmouth zorder 1001:
        xpos 0.2 xzoom -1

    red @sadbrow talking2mouth "Dodrio! No--Doduo! Don't listen to what Phobos tells you you need to be! Break away from Phobos!"
    red @sadbrow talking2mouth "That third voice you're hearing--that's not yours, that's Phobos screaming at you through the gem!"
    red @angrybrow talking2mouth "When you evolve, it will be a powerful and beautiful thing--not something you'll have to endure!"
    red @happy "Remember what you are, and that you only need to be yourself!"
    
    narrator "[ellipses]"

    show yellow surprisedbrow frownmouth with dis

    python:
        eb().ApplyStatus("recruited")
        eb().Health = 0
        AddEvent("Yellow", "DoduoCalled")
        dodrioobj = GetTrainerTeam("Phobos", "Dodrio", False)
        yellowtrainer = FriendlyTrainers()[1]
        dodrioobj.Owner = yellowtrainer
        dodrioobj.ClearStatus("recruited")
        dodrioobj.Heal()
        dodrioobj.Foreverals = []
        dodrioobj.Id = 84
        EnemyTrainers()[0].GetTeam().remove(dodrioobj)
        yellowtrainer.GetTeam().append(dodrioobj)

    yellow @talking2mouth "Wait, it--it wants to join me?"

    red @winkbrow talkingmouth "It's a bird of taste. But we're not done yet! Come on, let's keep going!"

    if (len(EnemyTrainers()[0].GetUnfaintedTeam()) == 0):
        jump phobosbattle2finalcall
    else:
        hide red
        hide yellow
        hide phobos
        hide screen battleui
        with dis

        return

label phobosbattle2combeeintro:
    hide screen battle
    show screen battleui
    show red angrybrow frownmouth zorder 1000:
        xpos 0.1
    show yellow angrybrow frownmouth zorder 1001:
        xpos 0.2 xzoom -1

    yellow @talking2mouth "This Combee[ellipses] it used to be a Vespiquen, a dignified queen. She was stolen from her hive, and has been forced to devolve, stripped of her dignity and status."
    yellow @sadbrow talking2mouth "She doesn't know what has happened to her hive--her children--and fears for them. She doesn't want to rebel against Phobos in case he tries to hurt them more."

    hide red
    hide yellow
    hide screen battleui
    with dis

    return

label phobosbattle2combeecall:
    hide screen battle
    show screen battleui
    show red angrybrow frownmouth zorder 1000:
        xpos 0.1
    show yellow angrybrow frownmouth zorder 1001:
        xpos 0.2 xzoom -1

    red @sadbrow talking2mouth "Vespiquen, listen up! You're still a queen, and you still have hundreds of grubs who need you to be a queen for them!"
    red @talking2mouth "You can't be scared of what Phobos might do in retaliation! You have to be strong for your subjects--you have to believe you'll be strong enough to defend them again!"
    red @angrybrow angrymouth "If you want to fight for them, then you're on the wrong side! Go to them and fight for them {i}against{/i} Phobos!"

    narrator "[ellipses]"

    $ eb().ApplyStatus("recruited")
    $ eb().Health = 0
    $ AddEvent("May", "CombeeCalled")

    may contest @surprised "Oh, it's--it's coming right at me! I think it wants to battle?"
    may @angrybrow angrymouth "I'll take care of this, Yellow and [first_name]! You handle Phobos!"

    if (len(EnemyTrainers()[0].GetUnfaintedTeam()) == 0):
        jump phobosbattle2finalcall
    else:
        hide red
        hide yellow
        hide phobos
        hide screen battleui
        with dis

        return

label phobosbattle2tatsugiriintro:
    hide screen battle
    show screen battleui
    show red angrybrow frownmouth zorder 1000:
        xpos 0.1
    show yellow angrybrow frownmouth zorder 1001:
        xpos 0.2 xzoom -1

    yellow @talking2mouth "This Tatsugiri[ellipses] it had a partner, a strong and proud Dondozo. The two were inseparable, until Phobos tore the two apart."
    yellow @talking2mouth "That rock is making Tatsugiri feel a sickening, saccharine sense of loyalty toward him, to force Mega Evolution."
    yellow @sadbrow talking2mouth "But Tatsugiri[ellipses] just wants to go home. They're oceans apart, but Tatsugiri can still hear Dondozo's cry of loss."
    yellow @sadbrow talking2mouth "Tatsugiri doesn't think that they'll ever find Dondozo again, though[ellipses]"

    hide red
    hide yellow
    hide screen battleui
    with dis

    return

label phobosbattle2tatsugiricall:
    hide screen battle
    show screen battleui
    show red angrybrow frownmouth zorder 1000:
        xpos 0.1
    show yellow angrybrow frownmouth zorder 1001:
        xpos 0.2 xzoom -1

    red @sadbrow talking2mouth "Tatsugiri! Don't give up, okay? You can still find Dondozo again! But you have to start looking!"
    red @angrybrow talkingmouth "Phobos will never let you go--he'll never {i}help{/i} you get away from him! You have to choose, now, to break what he's got over you!"
    red @talking2mouth "It's not loyalty or partnership--it's dependency. He {i}needs{/i} you to be strong for him!"
    red @angrybrow angrymouth "But you need to be strong for yourself!"

    narrator "[ellipses]"

    $ eb().ApplyStatus("recruited")
    $ eb().Health = 0
    $ AddEvent("Melody", "TatsugiriCalled")

    melody contest up @surprised "It's coming to me? Really? I was on Phobos' side ten minutes ago."
    melody @bubblemouth "[ellipses]"
    melody @talking2mouth "Guess we both were. I've got it. You finish him off."

    if (len(EnemyTrainers()[0].GetUnfaintedTeam()) == 0):
        jump phobosbattle2finalcall
    else:
        hide red
        hide yellow
        hide phobos
        hide screen battleui
        with dis

        return

label phobosbattle2finalcall:
    red @talking2mouth "Wait. One, two, three[ellipses]"
    red @surprised "That's it, right? He's out. We beat him."

    pause 1.0

    yellow @talking2mouth "No. No, there's one more. One more who needs healing."

    red @surprisedbrow talking2mouth "Really? You think you can do it?"

    yellow @closedeyes angryeyebrows sweat talking2mouth "I think I {i}have{/i} to try."

    show blank4 behind yellow 
    hide screen battle
    show screen battleui
    with transeye2nopause
    $ PlaySound("shine.ogg")
    pause 1.0
    python:
        for mon in FriendlyPokemon():
            mon.AdjustHealth(mon.GetStat(Stats.Health), absolute = True)
            mon.ClearStatus("basics", volatiles=True, basicafflictions=True)
            mon.ResetStatChanges()
            mon.ResetFaintedTurn()
            mon.Terastallized = -1
            for move in mon.GetMoves():
                move.PP = move.MaxPP
    hide blank4 with transeye2nopause

    yellow @talking2mouth "Heal."

    pause 2.0

    show phobos goggles angrybrow angrysharkmouth zorder 1000 with dis:
        xpos 0.75

    phobos "What--what {i}nonsense{/i} is this?! Are you trying to {i}heal{/i} this disappointing pile of scrap?! My weapon--your opponent?!"

    yellow @closedbrow talking2mouth "[first_name], there's--there {i}is{/i} something there. I just need a burst of energy, and I think I can get over the ledge."

    red @talking2mouth "Tell me what to do."

    yellow @closedbrow frownmouth sweat "[ellipses]"
    yellow @talkingmouth "Nothing. I can do it."

    if (GetTrainerTeam("Yellow", "Pichu") not in FriendlyBattlers()):
        python:
            yellowtrainer = FriendlyTrainers()[1]
            yellowteam = yellowtrainer.GetTeam()
            yellowtrainer.ShiftTeam(0, yellowteam.index(GetTrainerTeam("Yellow", "Pichu")))

        yellow @talking2mouth "Chuchu, please switch in. I need you!"

    else:
        phobos @talking2mouth "A boyish stringbean and her Pichu?"

    pause 1.0

    phobos @upeyes talking2sharkmouth "That hardly terrifies me."

    yellow @talking2mouth "Whenever a Pokémon evolves, it releases a burst of energy around it--a wave of natural rejuvenation, like a much more powerful version of what I can do."
    yellow @closedbrow talking2mouth "Every Pokémon can only do it as many times as they evolve."
    yellow @talking2mouth "So if you're going up against a trainer who has a team that's entirely unevolved, it might mean they don't battle very often[ellipses]"
    yellow @angrybrow challengingmouth "Or they're saving that boost for something more important than a battle."

    yellow @closedbrow talking2mouth "Pichu, now's our time! Please, evolve!"

    $ GetTrainerTeam("Yellow", "Pichu", False).Ability = "Static"
    $ GetTrainerTeam("Yellow", "Pichu").Evolve(25.3, force=True)
    $ GetTrainerTeam("Yellow", "Pichu", True).Foreverals = ["Pikachu Foreveral"]

    show yellow surprisedbrow frownmouth
    show red surprisedbrow frownmouth
    with dis

    red @talking2mouth "Uh[ellipses] where'd the outfit come from?"

    yellow @talking2mouth "I don't know. Maybe it was the Foreveral that Blue gave Chuchu?"

    red @unamusedbrow talking2mouth "Chuchu hasn't just turned into another one-in-a-million super-rare heretofore-unknown Pokémon with unimaginable power, has she?"

    yellow -surprisedbrow @confusedbrow talking2mouth "I'm pretty sure it's just an outfit."

    redmind -surprisedbrow @upeyes frownmouth confusedeyebrows "Well, that's a kind of power, I guess."

    yellow @talking2mouth "But that's not the important part. The important part is that Chuchu evolved, and with the ambient energy from evolution, I can[ellipses]"
    
    show blank4 behind yellow with transeye2nopausefast
    $ PlaySound("shine.ogg")
    pause 0.4
    hide blank4 with transeye2nopause

    yellow closedbrow sweat talking2mouth "Heal,{w=0.5}{nw}"

    show blank4 as blank42 behind yellow with transeye2nopausefast
    $ PlaySound("shine.ogg")
    pause 0.4
    hide blank42 with transeye2nopause

    extend closedeyes angryeyebrows sweat talking2mouth " heal,{w=0.5}{nw}"

    show blank4 as blank43 behind yellow with transeye2nopausefast
    $ PlaySound("shine.ogg")
    pause 0.4
    hide blank43 with transeye2nopause

    extend closedeyes angryeyebrows sweat angrymouth " and {i}heal!{/i}"

    pause 2.0

    show yellow winkeyebag winkeyes sweat frownmouth:
        xpos 0.2 xzoom -1
        ease 2.0 xpos 0.21 ypos 1.02 rotate 1

    $ EnemyTrainers()[0].Team = [GetTrainerTeam("Phobos", "Iron Jugulis")]

    red @talking2mouth "This one[ellipses] it hurt AZOTH1."

    yellow @talking2mouth "It says Phobos calls it Iron Jugulis--but its name is Cybreigon. It came from another world, in the distant future, but while it was trying to get its bearings, Phobos captured it."
    yellow @sadbrow talking2mouth "It's just scared and lost. It doesn't understand this new world, and the rock Phobos forced onto it is at least giving it some sort of direction--even if it hates it."

    pause 1.0

    red @talking2mouth "So even {i}it's{/i} a victim of Phobos, and not just a mindless machine. After all, if you can heal it, it's gotta be a Pokémon, right?" 
    red @happy "Fine. I know what to say. Let's finish this, Yell'!"

    hide red
    hide yellow
    hide screen battleui
    with dis

    return

label phobosbattle2wugtriointro:
    hide screen battle
    show screen battleui
    show red angrybrow frownmouth:
        xpos 0.1
    show yellow angrybrow frownmouth:
        xpos 0.2 xzoom -1

    $ himpronoun = "him" if GetTrainerTeam("phobos", "Wugtrio", heal=False).GetGender() == Genders.Male else "her"
    $ hispronoun = "his" if GetTrainerTeam("phobos", "Wugtrio", heal=False).GetGender() == Genders.Male else "her"
    yellow @talking2mouth "This Wugtrio[ellipses] it was Lawrence--Phobos' first partner. Wugtrio says Phobos wasn't always this way, and even though the rock Phobos forced on [himpronoun] is warping [hispronoun] body[ellipses]"
    yellow @sadbrow talking2mouth "Wugtrio remembers when Phobos was kind, and remembers the pain the two of them went through together."

    pause 1.0

    red @talking2mouth "I understand how it feels, but it can't let Phobos keep using it like this." 

    show red surprisedbrow frownmouth with dis
    
    yellow @talking2mouth "Try to convince [himpronoun] to come to our side--or at least leave Phobos."

    red @talking2mouth "What? But it's a trainer's Pokémon. They can't just[ellipses] {i}leave{/i} their trainer--can they?"

    yellow @talking2mouth "The entire time you were battling Phobos, all they were saying is that they wanted to."
    yellow @closedbrow sweat talking2mouth "Poké Balls don't control a Pokémon's mind. All of them, right now, are choosing to see Phobos as their trainer."
    yellow @angrybrow talking2mouth "And if they're choosing to stay, they can choose to leave."

    pause 1.0

    red -surprisedbrow @talking2mouth "Got it. I know what to say."

    hide red
    hide yellow
    hide screen battleui
    with dis

    return

label phobosbattle2wugtriocall:
    hide screen battle
    show screen battleui
    show red angrybrow frownmouth:
        xpos 0.1
    show yellow angrybrow frownmouth:
        xpos 0.2 xzoom -1

    red @sadbrow talking2mouth "Wugtrio, listen to us! You're not being loyal to Phobos, you're just suffering for him!"
    red @talking2mouth "If he cared about you as much as you care about him, he wouldn't ask you to forgive everything he's become!"

    show phobos unamusedbrow frownmouth goggles:
        xpos 0.7

    phobos @talking2sharkmouth "What nonsense is this? Wugtrio was my very first Pokémon. It can't abandon me--it knows I made it what it is today."
    phobos @happybrow happysharkmouth "Versatile, powerful, beautiful. Everything a Pokémon of mine should be! It owes me for every contest I let it shine in!"

    red @talking2mouth sadbrow "Ignore him, Wugtrio. You don't owe him anything--and you certainly don't owe him your suffering. Not anymore."
    red @talking2mouth angrybrow "You deserve someone kind, who will appreciate you, and take care of you! Someone who will take you to contests for {i}your{/i} benefit, not his!"

    phobos @talking2sharkmouth upeyes "Enough of this rubbish. Attack, Wugtrio."

    narrator "[ellipses]"

    show phobos surprisedbrow frownmouth with dis
    
    $ eb().ApplyStatus("recruited")
    $ eb().Health = 0
    $ AddEvent("Brendan", "WugtrioCalled")

    brendan contest @surprised "Wait, it's comin' toward me?! Uh, okay, I guess I'll battle it! Keep it up, you guys!"

    if (len(EnemyTrainers()[0].GetUnfaintedTeam()) == 0):
        jump phobosbattle2finalcall
    else:
        hide red
        hide yellow
        hide phobos
        hide screen battleui
        with dis

        return

label phobosbattle2ironjuguliscall:
    hide screen battle
    show screen battleui
    show red angrybrow frownmouth zorder 1000:
        xpos 0.1
    show yellow angrybrow frownmouth zorder 1001:
        xpos 0.2 xzoom -1

    red @closedbrow sweat talking2mouth "Hey, uh, Cybreigon! I don't--I {i}really{/i} don't understand what you are, but if you're a Pokémon, that's good enough for me!"
    red @talking2mouth "If you're a Pokémon, you deserve to be loved and cared for! I know this world is strange and scary, but it's not going to get any better by listening to what Phobos tells you to do!"
    red @angrybrow angrymouth "You're strong--you're {i}incredibly{/i} strong--and that means {i}you{/i} should get to decide what your strength means! Not Phobos, not anyone else!"

    show phobos angrybrow angrysharkmouth goggles zorder 1000:
        xpos 0.7

    phobos "Listen to me, brats! It's a machine! Just a tool! You're--you're trying to reach the heart of a lighter, a wrench, a--a pocketwatch!"
    
    red @talking2mouth "You're the only tool here, Phobos."

    yellow @talking2mouth "You can't decide people's paths for them. Not because you have power, or money, or influence. We might not always walk where we should, when we should..."
    yellow @talking2mouth "But that's our choice, too. Cybreigon--please, break free."

    narrator "[ellipses]"

    show phobos surprisedbrow frownmouth with dis

    $ eb().ApplyStatus("recruited")
    $ eb().Health = 0
    $ EnemyTrainers()[0].Team = []
    $ AddEvent("Grusha", "IronJugulisCalled")

    pause 2.0

    grusha noscarf winkbrow sweat @talking2mouth "Wait, why's everyone looking at--"

    show concerthallstagenight with vpunch

    grusha @surprisedblankeyes tinyup surprisedeyebrows surprisedmouth "{i}¡Mierda, ¿qué es eso?!{/i}"

    hide red
    hide yellow
    hide phobos
    hide screen battleui
    with dis

    $ AutoWin = True

    return