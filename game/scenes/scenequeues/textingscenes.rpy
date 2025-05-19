label textingscenequeue:

label gardeniatextingscene:
    if (not IsContacted("Gardenia") and IsAfter(24, 4, 2004) and IsPresent("Gardenia")):
        python:
            triggergardenia = False
            for item in elementitems.keys():
                if (GetItemCount(item) > 0):
                    triggergardenia = True
                for mon in AllPokemon():
                    if (mon.Item == item):
                        triggergardenia = True
        if (triggergardenia):
            $ texted = True
            show phone_B
            show phone_A
            show gardenia behind phone_A:
                zoom 0.95
            with fadeinbottom

            gardenia @happy "Hey, partner!"

            red @confused "Huh? Gardenia? How'd you get this number?"

            gardenia @talkingmouth "Oh, I paid Nate to tell me!"

            red @closedbrow talking2mouth "I really need to have a talk with Nate about how callous he is about other people's personal information."

            gardenia @talkingmouth "Yeah, it's pretty awful of him. {w=0.5}{nw}"

            python:
                gotfromdungeon = True
                for teacher in classtaught:
                    if (HasEvent(teacher, 3.1)):
                        gotfromdungeon = False
                        break

            if (gotfromdungeon):
                extend @happy "Anyway! A little birdie told me that you recently acquired a certain item in the great wilderness!"
            else:
                extend @happy "Anyway! A little birdie told me that you recently acquired a certain item in one of your elective classes!"

            gardenia @angrybrow happymouth "And that set off my 'ooh, business opportunity' sense."
            
            red @confused "Is this about investing in your junk shop?"

            if (investment == 0):
                gardenia @talking2mouth "No, but you {i}should{/i} do that."
            else:
                gardenia @happy "No, but I appreciate your support in that regard!"

            gardenia @talkingmouth "I've got some 'independent merchants' in the city who sell official Pokémon League items under the table."
            gardenia @talking2mouth "Nothing wrong with them--they just don't pass inspection, or fall off trucks, or are surplus goods, or whatever."
            
            if (gotfromdungeon):
                gardenia @happy "Anyway, those guys have been looking to expand their product lines to some less mass-produced items, the kind we can get in the wild pretty easily."

                red @talkingmouth "[bluecolor]So you want me to find more of these items in dangerous places outside the school and sell them to you,{/color} so you can re-sell them to some shady black market people?"
            else:
                gardenia @happy "Anyway, those guys have been looking to expand their product lines to some less mass-produced items, the kind we can get in our elective classes pretty easily."

                red @talkingmouth "[bluecolor]So you want me to make these items in my elective classes and sell them to you,{/color} so you can re-sell them to some shady black market people?"

            gardenia @talkingmouth "Pretty much, yup!"

            red @confused "Do you have... {i}any{/i} money-making plans that aren't some flavor of illegal?"

            if (not HasEvent("Gardenia", "Gardenia1")):
                gardenia @angrybrow happymouth "Uh, yeah. My yoga classes. But you aren't signing up for them!"

                red @sweat closedbrow happymouth "Fair enough."

            else:
                gardenia @angrybrow happymouth "Uh, yeah. My yoga classes. But you only showed up once!"

            gardenia @talking2mouth "So, I obviously {i}want{/i} you to sell this stuff to me, but, in the interest of fair play, I should probably tell you what else you can do with 'em."

            red @confused "Just... like, give them to my Pokémon in battle, right?"

            gardenia @talkingmouth "That's one thing. [bluecolor]But don't forget you can gift them to people, as well.{/color}"

            red @closedbrow talking2mouth "Huh."

            gardenia @happy "Giving people gifts to make them like you! Classic. Never fails."
            gardenia @talking2mouth "[bluecolor]Oh, but don't give anyone more than one gift a week.{/color} That'll just seem desperate, and people can smell desperation."

            red @confused "Noted."
            red @closedbrow talking2mouth "[bluecolor]So, if I wanted to sell items, I should meet up with you in the Baseball field, right?{/color}"

            gardenia @talkingmouth "That's right. Same place you'd go to make investments."

            red @talkingmouth "And what about if I wanted to give these items as gifts?"

            gardenia @happy "Just find whoever you're trying to give the gift to during your free time and hand it off. Quick and easy. Doesn't even take any time."

            red @talkingmouth "Cool. Thanks for the, uh, business advice."

            $ ValueChange("Gardenia", 3, 0.5)

            gardenia @happy "Yeah, I'll be sending you my consultant's fee in the morning. Ta-ta!"

            hide phone_B
            hide phone_A
            hide gardenia
            with fadeoutbottom

            pause 1.0

            red @closedbrow talking2mouth "I really hope she's joking."

            $ BecomeContacted("Gardenia")

            show blank2 with Dissolve(2.0)

            return

label wallytextingscene:
    if (GetRelationshipRank("Wally") > 0 and not HasEvent("Wally", "Wally1Part2") and IsPresent(["Brendan", "May", "Serena", "Calem", "Silver", "Skyla", "Cheren", "Wally"])):
        call Wally1Part2() from _call_Wally1Part2

        return

label skylatextingscene:
    if (GetRelationshipRank("Skyla") > 0 and not HasEvent("Skyla", "Skyla1Part2") and IsContacted("Gardenia")):
        call Skyla1Part2() from _call_Skyla1Part2

        return

$ textingscenetriggered = False
return