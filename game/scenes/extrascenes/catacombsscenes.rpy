label CatacombsIntro:
    $ AddEvent("Professor Oak", "FoundCatacombs")

    show cheren at night 
    show silver at night:
        xpos 0.75 xzoom -1
    show skyla at night:
        xpos 0.25

    cheren @talking2mouth "Seems I-Balls wasn't lying. These tunnels really do exist."

    silver @sadbrow talking2mouth "Like I said."

    cheren @angryeyebrows closedeyes talking2mouth "You did. You said these tunnels link into the city's sewers?"

    silver @talking2mouth "Yeah."
    silver @angrybrow talking2mouth "But no-one's going to be using 'em. Not anymore."

    cheren @talking2mouth "Please ensure it."

    pause 1.0

    show cheren:
        xzoom 1
        ease 0.5 xzoom -1
        pause 1.0
        ease 0.5 xzoom 1

    pause 2.0

    cheren @talking2mouth "The architecture here is... quite old."
    cheren @closedbrow talking2mouth "Galarian in style, if I'm not mistaken."

    skyla @talking2mouth "Not just Galarian architecture. There's a lot of Galarian Pokémon down here, in addition to those Tinkatink from Paldea."
    skyla @talkingmouth "Look, you can see them moving in the shadows out there."
    skyla @happy "Aren't Pokémon amazing? They can find their way into pretty much {i}anywhere{/i}!"

    silver @sadbrow talking2mouth "Ugh. I hate being underground. Let's get this job done and get out of here."

    cheren @talkingmouth "Galar. The nation that once held Unova by a leash..."
    cheren @closedbrow smilemouth "Hmph."
    cheren @talkingmouth "Seems there's more than one kind of ghost down here."

    pause 1.0

    cheren @talking2mouth "It's of no account. Let's focus; we're here to find Tinkatitanium."

    skyla @angrybrow talkingmouth "Alright! We'll find a Tinkatink, take its rattle, and be out of here before anyone knows it!"

    show skyla surprisedbrow frownmouth
    show cheren surprisedbrow frownmouth
    with dis

    silver @closedbrow talking2mouth "We're not picking on a Tinkatink."

    pause 2.0

    silver @surprisedbrow talking2mouth "Wait, are you guys seriously {i}surprised{/i} that I'd be against taking a rattle from a baby?"
    silver @sadbrow talkingmouth "Damn. I thought {i}I{/i} had problems. I should {i}never{/i} be the most moral person in the room."

    cheren @closedbrow sweat talking2mouth "Er... I suppose the immorality of taking a Tinkatink's rattle hadn't {i}quite{/i} occurred to either of us."

    show skyla sadbrow -frownmouth with dis

    cheren -surprisedbrow @talking2mouth "But now that you've pointed out the, {w=0.5}er, {w=0.5}{i}error{/i} in that plan, we'll figure something else out."

    silver @closedbrow talking2mouth "{size=30}Maybe I really {i}do{/i} have a reason to be here, after all...{/size}"

    if (not HasEvent("Cheren", "JoinCatacombs")):
        cheren @talking2mouth "Let's proceed. Skyla, please take the rear, and watch our backs. Silver, please take the vanguard, and prepare to handle whatever might jump out at us."

        silver @closedbrow talking2mouth "Yeah, fine."

        skyla @happy "Got it!"

        menu:
            "Hold on. I want to join.":
                $ AddEvent("Cheren", "JoinCatacombs")
                $ AddEvent("Cheren", "JoinCatacombsLater")
                show cheren surprisedbrow frownmouth
                show silver surprisedbrow frownmouth
                show skyla surprisedbrow frownmouth
                with dis

                silver @surprised "Gah! How long were you standing there?!"

                skyla @talkingmouth "Wait, you didn't notice?"

                silver @sadbrow talking2mouth "Obviously not..."

                show cheren -surprisedbrow -frownmouth
                show silver -surprisedbrow -frownmouth
                show skyla -surprisedbrow -frownmouth
                with dis

                cheren @closedbrow talking2mouth "You want to... okay. Fine. We'll change the plan, then."

                cheren @sad2brow talking2mouth "Skyla, please go with [first_name]. I will take Silver."

                silver @closedbrow talking2mouth "{size=30}Probably for the best.{/size}"

                skyla @happy "Sure thing."

                cheren @talking2mouth "Stay in contact--let us know if you run into any trouble, or if you find some Tinkatitanium without an owner."

                red night @talking2mouth "We will."

                pause 1.0

                cheren @sad2brow talking2mouth "I... appreciate your assistance. As, I'm sure, do Skyla and Silver."

                $ ValueChange("Skyla", 1, 0.25, False)
                $ ValueChange("Silver", 1, 0.75)

                red @talking2mouth "It's whatever. There's new Pokémon here, and it's a dark, unexplored, place beneath the school. If you guys are exploring it, I might as well, too."

                cheren @closedbrow talking2mouth "Sensible."

                skyla @happy "Alright, [GetRelationship('Skyla')]! Let's fly!"

                hide skyla
                hide cheren
                hide silver
                with dis

            ">Stay silent":
                hide skyla
                hide cheren
                hide silver
                with dis

                narrator "The disciplinary committee walks out of sight..."

    else:
        cheren @talking2mouth "Let's proceed. Skyla, please go with [first_name]. I will take Silver."

        silver @closedbrow talking2mouth "Yeah, fine."

        skyla @happy "Got it!"

        cheren @talking2mouth "Stay in contact--let us know if you run into any trouble, or if you find some Tinkatitanium without an owner."

        hide skyla
        hide cheren
        hide silver
        with dis
    
    $ AddEvent("Professor Oak", "LeftCatacombs")

    return

label FoundTinkatitaniumLode:
    if (HasEvent("Cheren", "JoinCatacombs")):
        $ AddEvent("Professor Oak", "ClearedCatacombs")

        show skyla at night:
            xpos 0.5

        skyla @surprised "Oh--oh! Look, there! A massive lump of Tinkatitanium! Wait... it's not just one, there's a bunch of them!"

        red night @confused "I see them, but... what {i}are{/i} they? They're all misshapen, and lumpy, and... it looks a little bit pink and blue, right? That's not just me?"

        skyla surprisedbrow frownmouth @talking2mouth angrybrow "No, it's definitely pink and blue. Even in this low light, I can see--"

        pause 1.0

        red @closedbrow sweat talking2mouth "Oh... I think I see what happened here."

        skyla @sweat talking2mouth "Me too. Tinkatuff and Tinkaton smack rocks up into the sky to try and make things--Corviknight, low-flying planes, drones--crash into the ground."
        skyla @angrybrow talking2mouth sweat -surprisedbrow "Then they gather up the metal from the crash and convert it into more Tinkatitanium."
        skyla angrybrow @angry "They're a serious pain for pilots."

        red @sweat closedbrow talking2mouth "And for our drone-flying friend, I bet. It's kinda hard to make 'em out, they've been hammered so much, but these definitely {i}used{/i} to be I-Balls."

        skyla -angrybrow -sadbrow @talkingmouth "Looking around here... I think she's probably lost at least seven to the Tinkatuff that live around here."

        red @closedbrow talking2mouth "No wonder the ones she has now are in such poor condition."

        skyla -angrybrow -frownmouth @sadbrow talkingmouth "Seriously. Anyway, I'll take as many of these as I can carry and head back. Do you want to stay here a bit longer?"

        red @talking2mouth "I might. There's a lot of new Pokémon down here--I'm not sure I've seen them all."

        skyla @talkingmouth "Alright! I'll talk with the rest of the DC and tell them what we found. Meet up with us at the Battle Hall when you have time! We'll bring all this stuff back to I-Balls, and receive a hero's welcome for a job well done!"

        red @happy "Sure. Seeya later!"

        hide skyla with dis

        narrator "Skyla waves goodbye, and heads out into the darkness alone, unbothered by the lack of visibility."

    else:
        narrator "You suddenly see a large pile of warped metal. It is unmistakably Tinkatitanium."
        narrator "However, it's colored pink and blue... or at least it was, before most of the paint was hammered off."
        narrator "It seems this room is a graveyard for many of I-Ball's drones, which were presumably smacked down by the Metalsmith Pokémon."
        narrator "Given the size of the metal, and the fact that these drones used to belong to I-Balls anyway, you don't feel overly bad about taking some back with you."

    return