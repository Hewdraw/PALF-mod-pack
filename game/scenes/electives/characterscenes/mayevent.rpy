label mayevent:

if (IsPresent("May", "Bug") and IsAfter(24, 4, 2004) and not HasEvent("Bugsy", "GuiltTrip") and HasEvent("Burgh", 2)):
    $ AddEvent("Bugsy", "GuiltTrip")
    if (mayhaslarvesta):
        show bugsy uniform with dis:
            xpos 0.33
        show may uniform with dis:
            xpos 0.66
        bugsy uniform @happy "Ohmygosh {i}look{/i} at him!! He's so {i}CUTE{/i}!!"
        may uniform @happy "I know, right? I have to thank Alder, like, fifty times for telling me about his egg!"
        bugsy @talkingmouth "I'm so happy for you, May! You've been looking for a Larvesta for ages!"
        bugsy @surprised "Hold on--your Larvesta's mom is Alder's Volcarona. That means Burgh's Volcarona is your little guy's brother!"
        bugsy @happy "And, waitasec, Burgh's Volcarona is Poppy's dad, so... I guess yours is Poppy's uncle? That's kinda weird!"
        may @happy "Does that make us in-laws? I hope Brendan won't be jealous!"
        redmind thinking "Seeing May so happy, I'm sure I did the right thing."
        hide bugsy with dis
        hide may with dis
    
    else:
        show bugsy uniform with dis
        bugsy frownmouth @sad "Hey, [first_name]. Is it true that you took the Larvesta egg May found?"
        red uniform @surprised "I--uhh--wait, that sounds really bad! That's not how I saw it at all!"
        red @sadeyebrows talking2mouth "Look, Volcarona is an amazing Pokémon. We {i}both{/i} wanted one for our teams. Isn't a battle the fairest way to decide?"
        bugsy @angrybrow talking2mouth "But Volcarona isn't just a strong Pokémon. It's May's {i}favorite{/i} Pokémon, and now that you took that egg, she's really sad!"
        red @angryeyebrows talking2mouth "What if it's my favorite Pokémon, too?"
        bugsy @angrybrow talking2mouth "I--"
        pause 0.5
        bugsy @sad "{size=30}Is it?{/size}"
        red @sad2brow frownmouth "[ellipses]"
        bugsy @sadbrow talking2mouth "...I guess I didn't think of that."
        pause 1.0
        bugsy @sadbrow talking2mouth "Sorry, [first_name]. It just sucks seeing May so down. She {i}really{/i} wanted that egg, y'know?"
        red @closedeyes talking2mouth "I know."
        bugsy @sadbrow talkingmouth "Well... I bet our Larvestas will be really good friends! I'm sure Poppy would love to train with yours!" 
        bugsy @sadbrow talkingmouth "And--and maybe we'll find another one sometime, so May can have one too!"
        red @sadeyebrows talkingmouth "That'd be great. If I see another Larvesta egg, she's definitely got dibs."
        hide bugsy with dis

return