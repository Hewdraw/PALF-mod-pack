label textingscenequeue:

label rosafollowupbunnyrecruitscene:#remember there's a copy of this scene in 010611secondhomeroom.rpy
    if (not HasEvent("Rosa", "BunnyRecruit") and HasEvent("Rosa", "HalfBunnyRecruit") and (HasEvent("Nate", "BunnyRecruit") + HasEvent("Iono", "BunnyRecruit") + HasEvent("Sonia", "BunnyRecruit") + min(1, GetRelationshipRank("Rosa") / 2.0) >= 3)):        
        $ AddEvent("Rosa", "BunnyRecruit")
    
        stop music fadeout 1.5
        queue music "audio/music/joinavenue_start.ogg" noloop
        queue music "audio/music/joinavenue_loop.ogg"

        show screen songsplash("Join Avenue", "Zame")

        if (HasEvent("Rosa", "PromisedNessaText")):
            red @thinking "Hm[ellipses] after today's recruitment, I think we can make sure the party is secure for Rosa. I said I'd text Nessa, so[ellipses]"

        elif (HasEvent("Rosa", "PromisedSoniaText")):
            red @thinking "Hm[ellipses] after today's recruitment, I think we can make sure the party is secure for Rosa. I said I'd text Sonia, so[ellipses]"

        elif (HasEvent("Rosa", "PromisedRaihanText")):
            red @thinking "Hm[ellipses] after today's recruitment, I think we can make sure the party is secure for Rosa. I said I'd text Raihan, so[ellipses]"

        else:
            red @thinking "Hm[ellipses] after today's recruitment, I think we can make sure the party is secure for Rosa. I said I'd let Sabrina know, so[ellipses]"

        pause 1.0

        redmind "There, text sent."

        show rosa behind phone_A:
            zoom 0.8 ypos 0.95
        with fadeinbottom

        rosa @talkingmouth "Hey, [first_name]!"

        red @talkingmouth "Oh, hey, Rosa! I thought you couldn't use your phone?"

        if (HasEvent("Rosa", "PromisedNessaText")):
            rosa @happy "Didn't you notice? I'm using Nessa's phone! She got your text!"

        elif (HasEvent("Rosa", "PromisedSoniaText")):
            rosa @happy "Didn't you notice? I'm using Sonia's phone! She got your text!"

        elif (HasEvent("Rosa", "PromisedRaihanText")):
            rosa @happy "Didn't you notice? I'm using Raihan's phone! He got your text!"

        else:
            rosa @happy "Didn't you notice? I'm using Nessa's phone! Sabrina heard your, uh, your 'thought!'"

            if (not IsContacted("Nessa")):#should be impossible, but just in case
                $ BecomeContacted("Nessa")

        red @talkingmouth "Gotcha. So, we're good? You'll be able to go to the party, then?"

        rosa @talkingmouth "I think so. It really sounds like you thought this through pretty thoroughly."
        rosa @sadbrow talkingmouth "And[ellipses] I {i}really{/i} appreciate that. I know it's a hassle."

        $ ValueChange("Rosa", 1, 0.5)

        red @happy "Don't worry about it! I just want you to be able to have fun with us, like everyone else."
        red @talkingmouth "There won't be any fancy movie-people there, or anything, so it's probably a much more low-key party than you're used to, but I hope you still have fun."

        rosa @talkingmouth "Trust me, that sounds like the best kind of party right now. The stage lights get blinding, after a while."

        red @happy "I can imagine."
        red @talkingmouth "Anyway, that's great to hear! We'll see you there. And don't worry, if anything changes, or one of our security people has to drop out, I'll let you know beforehand."
        red @sadbrow talkingmouth "Everyone's going to go into this knowing {i}exactly{/i} what they're getting into. Promise."

        rosa @happy "Aw. Thanks so much for your support!"

        return

label gardeniatextingscene:
    if (IsAfter(24, 4, 2004) and IsPresent("Gardenia") and not HasEvent("Gardenia", "GardeniaFirstText")):
        python:
            triggergardenia = False
            for item in elementitems.keys():
                if (GetItemCount(item) > 0):
                    triggergardenia = True
                for mon in AllPokemon():
                    if (mon.Item == item):
                        triggergardenia = True
        if (triggergardenia):
            python:
                gotfromdungeon = True
                for teacher in classtaught:
                    if (HasEvent(teacher, 3.1)):
                        gotfromdungeon = False
                        break
                texted = True
                AddEvent("Gardenia", "GardeniaFirstText")
            show phone_B
            show phone_A
            show gardenia behind phone_A:
                zoom 0.95
            with fadeinbottom
            
            gardenia @happy "Hey, partner!"

            if (IsContacted("Gardenia")):
                red @talkingmouth "Hey, Gardenia. What's up?"

                if (gotfromdungeon):
                    gardenia @happy "A little birdie told me that you recently acquired a certain item in the great wilderness!"
                else:
                    gardenia @happy "A little birdie told me that you recently acquired a certain item in one of your elective classes!"

            else:
                red @confused "Huh? Gardenia? How'd you get this number?"

                gardenia @talkingmouth "Oh, I paid Nate to tell me!"

                red @closedbrow talking2mouth "I really need to have a talk with Nate about how callous he is about other people's personal information."

                gardenia @talkingmouth "Yeah, it's pretty awful of him. {w=0.5}{nw}"

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

            gardenia @happy "Do you really need to be told this one? After you hang out with someone, just hand it off."

            red @talkingmouth "Cool. Thanks for the, uh, business advice."

            $ ValueChange("Gardenia", 3, 0.5)

            gardenia @happy "Yeah, I'll be sending you my consultant's fee in the morning. Ta-ta!"

            hide phone_B
            hide phone_A
            hide gardenia
            with fadeoutbottom

            pause 1.0

            red @closedbrow talking2mouth "I really hope she's joking."

            if (not IsContacted("Gardenia")):
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