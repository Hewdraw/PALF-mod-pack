label nopikachu:
    if (pikachudenial == 0):
        red @angry "Boxing [pika_name] is the one thing I'll {i}never{/i} do."
        if (IsBefore(1, 5, 2004)):
            red @sad "It's bad enough I can't take my little buddy with me to gym class..."

    elif (pikachudenial == 1):
        red @angry "No means no. Get it? [pika_name] was there for me when I was alone."

    elif (pikachudenial == 2):
        red @angry "Boxing [pika_name] is the one thing I'll {i}never{/i} do."
        red @angry "He was there when I lost all my friends, and before I even had any."

    elif (pikachudenial == 3):
        red @angry "Boxing [pika_name] is the one thing I'll {i}never{/i} do."
        red @angry "He was there when my Mom and I had to skip meals."

    elif (pikachudenial == 4):
        red @angry "Boxing [pika_name] is the one thing I'll {i}never{/i} do."
        red @angry "He was there when I got in fights with the other kids for making fun of my mom."

    elif (pikachudenial == 5):
        red @angry "Boxing [pika_name] is the one thing I'll {i}never{/i} do."
        red @angry "He was there when I got my first human friend, Blue. And he was there when I lost him, too."
        
    elif (pikachudenial == 6):
        red @sad "...I feel sad for you. Haven't you ever had a friend that you never wanted to be parted from?"
        red @sad "Someone you'd move heaven and hell for? Someone you'd spit in the eye of god to keep by your side?"
        red @sad "[ellipses]"
        red @happy "I hope you do, someday. But [pika_name]'s staying. That's non-negotiable."

    else:
        red @talkingmouth "Nah."   

    $ pikachudenial += 1

    if (location == "city"):
        jump citysetup

    else:
        jump aftersetup

label cramorantscene:
    scene seaport with splitfade

    pause 1.0

    if (not seencramorant):
        red @closedbrow talking2mouth "Hm... looks like the seaport isn't super-busy right now. I don't see any signs of a Frenzied Pokémon around, either..."
        
        $ PlaySound("Pokemon/pikachu_norm1.ogg")

        pikachu neutral_2 "Pika?"

        red @talkingmouth "Right."

        red @happy "Well, whatever it is, it's got to be weak to you, buddy. There's plenty of Flying-types and Water-types around here, so you've probably got the advantage."

        if (pikachuobj in playerparty):
            $ playerparty.remove(pikachuobj)

        red @closedbrow talking2mouth "Of course, that Absol and Lopunny were both pretty far out of their territory. I guess there's no guarantee that whatever stole Tia's hat came from this area."

        red @confused "On the other hand, this is still a pretty industrial area. There's a power plant over there, and dumpsters all around. The sewers lead out here, too, I think."

        red @talking2mouth "And with all the ships around here, it could've been something even brought over from a different region..."

        if (GetRelationship("Bea") == "Planner"):
            red @happy "Ah, geez. I'm sounding like Bea, now, trying to figure out every possibility."

        red @talkingmouth "What do you think, buddy?"

    else:
        red @closedbrow talking2mouth "Okay. We need to make sure that Cramorant doesn't get the drop on us again. With your electric-type moves, it wouldn't stand a chance. Ready, buddy?"

        if (pikachuobj in playerparty):
            $ playerparty.remove(pikachuobj)

    $ seencramorant = True

    pause 1.0

    $ PlaySound("idea.ogg")

    red @confused "Buddy?"

    pause 1.0

    stop music

    $ renpy.music.queue("Audio/Music/RelicCastle_Start.ogg", channel='music', loop=None, tight=None)
    $ renpy.music.queue("Audio/Music/RelicCastle_Loop.ogg", channel='music', loop=True, tight=None)

    $ PlaySound("pokemon/cries/845.2.mp3")

    show cramorantthroatgoat:
        xpos 1.1 zoom 0.0 ypos 0.0 yanchor 1.0 xanchor 0.5
        ease 1.0 xpos 0.5 zoom 2.0 ypos 1.0
        ease 1.0 xpos 0.2 zoom 0.5 ypos 0.3
        easeout 1.0 xpos 0.5 zoom 1.0 ypos 0.4
        easein 1.0 zoom 3.0 ypos 1.2

    pause 3.0

    red @surprised "Buddy?! Get out of there!"

    $ PlaySound("Pokemon/pikachu_confused2.ogg")
    $ PlaySound("Pokemon/pikachu_scared.ogg")

    pikachu swallowed "Pika?! Pikapikapika!"

    red @sweat closedbrow talkingmouth "Right... I guess you're trying, huh?"

    redmind @sad "It looks like the wild Cramorant really wants to chow down on [pika_name]! [bluecolor]Even if I get the Cramorant to spit him back up, he'll probably just try to gobble him down again.{/color}"

    python:
        trainer1 = Trainer("red", TrainerType.Player, playerparty, number=3)

        cramorantobj = Pokemon("Cramorant", level=25, moves=[GetMove("Surf"), GetMove("Dive"), GetMove("Fly"), GetMove("Roost")], frenzynerf=(12, ["Stockpile", "Swallow", "Spit Up", "Water Gun"]), shinylock=False)
        cramorantobj.ApplyStatus("frenzied")
        cramorantobj.ApplyStatus("gorging")
        trainer2 = Trainer("sideportraitfull", TrainerType.Enemy, [cramorantobj], isPokemon=True)
        sidemonnum = 845.2

    hide cramorantthroatgoat with dis

    call Battle([trainer1, trainer2], healParty = False, specialmusic="Nothing") from _call_Battle_38
    $ battlehistory["Cramorant1"]  = _return

    $ AddPikachu()

    if (cramorantobj in (AllPokemon())):
        python:
            seaportunlocked = True
            cramorantobj.Level = 12
            cramorantobj.Moves = [GetMove("Stockpile"), GetMove("Swallow"), GetMove("Spit Up"), GetMove("Water Gun")]
            cramorantobj.Experience = cramorantobj.CalculateAllExperienceNeededForLevel(12)
            cramorantobj.ClearStatus("all", True)
            cramorantobj.RecalculateStats()

            pronoun = "him" if cramorantobj.GetGender() == Genders.Male else "her"
            pronoun2 = "he" if cramorantobj.GetGender() == Genders.Male else "she"

        red @happy "Yes! I caught [pronoun]."
        
        $ PlaySound("Pokemon/pikachu_angry1.ogg")

        pikachu angry "Pika."

        red @sadbrow happymouth "Oh, cheer up, buddy. I'm sure you'll warm up to [pronoun]." 
        if (cramorantobj in playerparty):
            red @happy "Look, [pronoun2]'s calmer already."
        elif (absolobj in (AllPokemon()) or lopunnyobj in (AllPokemon())):
            red @happy "I bet [pronoun2]'ll probably stop trying to eat you. These Frenzied Pokémon always calm down after a while."
        else:
            red @closedbrow talking2mouth "As long as [pronoun2] stops trying to eat you, anyway."

        $ PlaySound("Pokemon/pikachu_angry2.ogg")

        pikachu angry "Pika!"

        $ cramorantname = cramorantobj.GetNickname()

        red @closedbrow talking2mouth "I get the feeling that [pika_name] would rather not hang out around [cramorantname] any more than absolutely necessary..."   

        narrator "{color=#0048ff}You discovered the seaport!{/color} In the seaport, you'll be able to find new Pokémon, and battle for as long as you want."
        narrator "However, leaving will cause this period of free time to end."

    elif (WonBattle("Cramorant1")):
        $ seaportunlocked = True
        red @talkingmouth "Phew! That was tough. But that big, bad, bird won't be bothering anyone else anytime soon."

        red @happy "Well? How did it feel to be a missile?"

        $ PlaySound("Pokemon/pikachu_angry2.ogg")

        pikachu angry "Pika!"

        narrator "{color=#0048ff}You discovered the seaport!{/color} In the seaport, you'll be able to find new Pokémon, and battle for as long as you want."
        narrator "However, leaving will cause this period of free time to end."

    else:
        red @surprised "Crap! It's too strong! Retreat, [pika_name]!"

    $ PlaySound("Pokemon/pikachu_angry2.ogg")

    pikachu angry "Pika!"

    return

label wallyellowscene:
    $ sawwallyellow = True
    scene citycafe with splitfade

    show screen songsplash("Relic Song", "Zame")
    play music "audio/music/relicsong.ogg"

    pause 1.0

    narrator "You walk into an unfamiliar cafe. You actually remember this cafe from the impromptu restaurant tour that Leaf dragged you on a while ago, though you're looking forward to enjoying it at your own pace."
    narrator "In the corner, you see a familiar woman talking with someone slightly less-familiar, though still recognizable."

    show wally:
        xpos 0.33
    show yellow:
        xpos 0.66

    yellow @talking2mouth "...And how were your Quarter Qlash matches?"

    wally @sideeyes talkingmouth "Fine. I wasn't... it wasn't easy, though. I only barely scraped out a win on my third match."
    wally @sadeyes talkingmouth "I think I made a mistake coming here."

    pause 1.0

    yellow @talking2mouth "Why?"

    wally @surprised2eyes surprisedeyebrows surprisedmouth "Why?"
    wally @closedeyes angryeyebrows angrymouth "Because I only barely won!"

    yellow @happy "I didn't win, though. Does that mean I made a mistake coming here, Wally?"

    $ BecomeNamed("Wally")

    wally @sideeyes talkingmouth "N-no, of course not. But... you want to be a Pokémon nurse, right? You don't {i}need{/i} to be a strong battler."
    wally @talkingmouth "I do. If I'm going to... {w=0.5}{nw}"

    show yellow sadbrow frownmouth with dis

    extend @sideeyes talkingmouth "{i}cough.{/i}"

    pause 1.0

    wally @talkingmouth "Sorry. I meant I need to get stronger if I'm going to... to get what I want."

    pause 1.0

    yellow @sadbrow talking2mouth "It looks like your cough's getting worse."

    wally @sadbrow happymouth "It's just... a little bug going around. That time of year, you know?"

    yellow @angrybrow talking2mouth "It's May."

    show citycafe with vpunch

    wally @surprisedeyes talkingmouth "What about her?!"

    yellow -sadbrow -frownmouth @surprised "What?"

    wally @talkingmouth "What?"

    pause 1.0

    wally @closedeyes talkingmouth "Sorry. I thought you were saying something about May."

    yellow @talking2mouth "I don't know who that is. Is she in the nursing course?"

    wally @sideeyes talkingmouth "No, she wants to be a coordinator."

    yellow @talking2mouth "Oh."

    pause 1.0

    yellow @closedbrow talkingmouth "Actually... I think Leaf might have mentioned one of her old roommates was named May..."
    yellow @talking2mouth "Is May Brendan's girlfriend?"

    wally @talkingmouth "...Yes. Last I checked."
    wally @sideeyes talkingmouth "Actually, I dorm with those two. May, Brendan, and I were all friends back in Hoenn, but... as they became a couple, you know... there wasn't really room for me."

    wally @sideeyes talkingmouth "I hoped we could reconnect here in Kobukan, but it looks like they're still a thing. And their thing... {w=0.5}{nw}"

    show yellow sadbrow frownmouth with dis

    extend @sideeyes talkingmouth "{i}cough.{/i}"

    pause 1.0

    show yellow surprisedbrow frownmouth blush with dis

    wally @lightblush sadbrow talkingmouth "It gets loud at night, if you catch my drift."

    yellow @sadbrow talking2mouth "Oh... oh! I, ha, I see..."
    yellow @happy "My dorm also gets pretty loud, too..."

    wally @closedbrow talkingmouth "Ugh. I don't get why the Student Council decided to let men and women dorm together. I was perfectly happy with the old arrangement."

    yellow -surprisedbrow -frownmouth -blush @surprised "Oh-oh! I didn't mean it like that. I meant, um, Leaf snores really loudly, and Blue sneaks out of the dorm at midnight, and... um... well, I think it's better if I don't mention the noises I hear from Ethan's room..."

    wally @talkingmouth "...Gotcha. You dorm with [first_name], too, right? The one who gave that big speech in front of everyone? I've heard some weird stories about him."

    if (not mayhaslarvesta):
        wally @talkingmouth "It sounded like he did something that really pissed off Brendan. I don't know what that was, though..."

    yellow @talking2mouth "Yes. But he's really nice in-person. He even tolerates Blue."

    wally @happy "Hah! You've told me how hard {i}that{/i} is. Maybe I'd like to meet this guy."

    pause 1.0

    wally @sideeyes talkingmouth "Hey... he's not, like, a blabbermouth, is he? He won't tell anyone about me being here? I've been trying to stay pretty unnoticed so far."
    wally @closedbrow angrymouth "That thing with Lisia was too close. If someone back home saw me on TV, then..."

    yellow @sadbrow talking2mouth "I haven't had a whole lot of time to talk to him, but I don't think he's like that."

    wally @talkingmouth "Alright."

    pause 1.0

    show yellow sadbrow frownmouth with dis

    wally @closedbrow talkingmouth "{i}Cough.{/i}"

    pause 2.0

    wally @happy "Cheer up, Yellow."
    wally @talkingmouth "It was just all the excitement of the Quarter Qlashes. As soon as we go back to classes, I should be fine again."
    wally @sideeyes talkingmouth "...Maybe I should wear a mask."

    yellow @sadbrow talking2mouth "I wish I could heal you..."

    wally @sadeyebrows talkingmouth "It's not that bad. It's really just a cough." 
    wally @sadeyebrows happymouth "Every time I walk into the infirmary and see Grusha laid out on the table, or Jasmine shivering under her blankets, I gotta ask myself if I should even be there."

    yellow -sadbrow -frownmouth @closedbrow talking2mouth "Pain isn't a competition. The existence of others' hurt doesn't invalidate yours."

    show yellow happy with dis

    wally happy "Ha-{i}cough{/i}-ha! Which fortune cookie did you get {i}that one{/i} off of?"

    $ ValueChange("Wally", 3, 0.33)

    return

label cramorantscene2:
    pause 0.5

    $ PlaySound("pokemon/cries/845.mp3")
    $ sidemonnum = 845
    sidemon "Craw! Cram!"

    red @surprised "Hm? Wait, is that...?"

    libpikachu @angrybrow happymouth glowing "Pi-i-i-ka!"

    red @surprised "Looks like a Cramorant! They're pretty rare around here... this might be an important opportunity! Alright, [pika_name], let's go!"

    python:
        trainer1 = Trainer("red", TrainerType.Player, playerparty, number=3)
        cramorantobj = Pokemon("Cramorant", level=15)
        trainer2 = Trainer("sideportraitfull", TrainerType.Enemy, [cramorantobj], isPokemon=True)

    call Battle([trainer1, trainer2], healParty = False, specialmusic="Nothing") from _call_Battle_167
    $ RecordBattle("Cramorant1")

label SilverBirthday1:
    $ AddEvent("Silver", "SilverBirthday1")
    $ location = "alley"

    stop music fadeout 1.6
    queue music "audio/music/alley_start.ogg" noloop
    queue music "audio/music/alley_loop.ogg"
    scene abandonedhouse:
        yalign 0.5
    with Dissolve(2.0)

    pause 0.5

    show silver sadbrow at night with dis

    red night @surprised "Silver?"

    silver @surprisedbrow "Hm?"
    silver @talkingmouth "Oh, hey, red."

    if (HasEvent("Silver", "Overthrown")):
        red @sadbrow talkingmouth "Silver, is it safe for you to be here? What about [duplica_name]?"

        silver @talking2mouth "She's leading the goons, yeah. But... I'm still the 'big boss's son.' I'm safe. For now."

        silver @closedbrow talking2mouth "I was just visiting. Feeling nostalgic."

    else:
        red @sadbrow talking2mouth "Is there something wrong?"

        silver @talking2mouth "Feeling nostalgic."

    stop music fadeout 1.5

    queue music "audio/music/DontEverForget_start.ogg" noloop
    queue music "audio/music/DontEverForget_loop.ogg"

    silver @talking2mouth "Remembering how we ended up here. Remembered how... {i}lucky{/i} I felt to find this house. Something dark, and hidden[ellipses]"
    silver @talking2mouth "Where we could hide from anyone and anything we needed to."
    silver -sadbrow @happymouth "Never thought that I'd end up hating it after just a year."

    red @talking2mouth "You know, my dorm's open."

    if (HasEvent("Silver", "Silver2Part2")):
        silver @talking2mouth "Already took you up on that once before. Can't do it too often; people'll talk."

    else:
        silver @sadbrow talking2mouth "Yeah, maybe in an emergency."

    pause 1.0

    show silver sadbrow with dis

    red @talking2mouth "Um. I don't mean to pry, but... is there something else?"

    silver @talking2mouth "You think there might be?"

    red @sadbrow talkingmouth "I've got a vague suspicion, yeah."

    silver "[ellipses]"

    silver @talking2mouth "It's, uh, my birthday."

    if (GetRelationshipRank("Silver") == 0):
        show silver surprisedbrow with dis

        red @happy "Wow! Twenty?"

        silver -surprisedbrow @sadbrow talking2mouth "Do I look that bad? No, I'm eighteen."

        red @surprised "Oh. I'm sorry, it's just... you seem, uh, way more mature than that...?"

        silver @sadbrow talkingmouth "Heard that before. Not usually in that context, though."

    else:
        red @happy "Wow! Eighteen?"

        silver @talking2mouth "Eighteen."

    red @talkingmouth "How does it feel?"

    silver @talking2mouth "Nothing's changed. Guess I can join the military, if I ever hit my head and decide I really want to join some other group of jackbooted thugs."

    pause 1.0

    red @sadbrow talking2mouth "Sorry."

    silver @sadbrow "[ellipses]{nw}"
    extend @talking2mouth "I shouldn't complain. At least I can see the sky this year."

    pause 1.0

    if (GetRelationshipRank("Silver") >= 3):
        silver @sadbrow talkingmouth "Even with all this Copycat stuff, I guess[ellipses] all things considered[ellipses] things are better now."

    else:
        silver @sadbrow talkingmouth "I guess[ellipses] all things considered[ellipses] things are better now."

    silver smilemouth @happy "Maybe worth sticking around for the next year."

    red @talkingmouth "Definitely. I'd miss you. I know I'm not the only one."

    pause 1.0

    red @sadbrow talkingmouth "Hey, Happy Birthday, red."

    $ ValueChange("Silver", 3)

    silver @sadbrow happymouth "Thanks."

    red @confused "Are you going anywhere?"

    silver @closedbrow talking2mouth "Nah, just hanging out here for a while longer."

    red @happybrow talkingmouth "Alright. See you later."

    return

label SilverBirthday2:
    $ AddEvent("Silver", "SilverBirthday2")
    $ location = "alley"

    stop music fadeout 1.5
    queue music "audio/music/DontEverForget_start.ogg" noloop
    queue music "audio/music/DontEverForget_loop.ogg"
    scene abandonedhouse:
        yalign 0.5
    with Dissolve(2.0)

    pause 0.5

    show silver surprisedbrow at night with dis

    silver @talking2mouth "When you said 'see you later', I didn't expect, like, ten minutes later."

    red night @happy "It's your birthday, man. I've got a present for you."

    silver @talking2mouth "A p-present? Uh, what...?"

    menu silverbirthdaymenu:
        ">Give him an item":
            python:
                itemkeys = []
                for item, amount in inventory.items():
                    itemname = GetItemName(item)
                    # Use an f-string to format the display string
                    display_text = f"1x {itemname} (Total Held: {amount})"
                    # Append a tuple with unique values
                    itemkeys.append((display_text, item))
                itemkeys.append((">Give him a battle", "Battle"))
                item = renpy.display_menu(itemkeys)

            if (item == "Battle"):
                jump battlesilverbirthday

            elif (LoseItem(item)):
                $ itemname = GetItemName(item)
                $ itemvalue = GetGiftValue(character, item)

                if (itemvalue >= 7):
                    silver @surprised "[first_name]? Are you--are you serious? For me? That's..."
                    silver happy "You've made me a very happy man, red. I'll remember this."
                    $ ValueChange("Silver", itemvalue * 3)
                    narrator "You give Silver the [itemname], which he holds gently and reverently, seemingly unable to tear his eyes away from it."

                elif (itemvalue >= 5):
                    silver @surprised "Really? You're {i}giving{/i} me that? No strings?"
                    silver happybrow smilemouth @happymouth "Thanks, red. I'll remember this."
                    $ ValueChange("Silver", itemvalue * 2)
                    narrator "You give Silver the [itemname], which he looks at affectionately, before pocketing it."

                elif (itemvalue >= 3):
                    silver @surprised "Really? A birthday gift?"
                    silver smilemouth -surprisedbrow @happymouth "Thanks, red. I'll remember this."
                    $ ValueChange("Silver", itemvalue * 2)
                    narrator "You give Silver the [itemname], which he tosses to himself, then pockets."

                elif (itemvalue >= 1):
                    silver "Hm."
                    silver smilemouth -surprisedbrow @sadbrow happymouth "Thanks, red. I'll remember this."
                    $ ValueChange("Silver", 3)
                    narrator "You give Silver the [itemname], which he immediately pockets."

                else:
                    silver @closedbrow talking2mouth "Well... it's the thought that counts."
                    silver smilemouth -surprisedbrow @sadbrow happymouth "Thanks, red. I'll remember this."
                    $ ValueChange("Silver", 1)
                    narrator "You give Silver the [itemname], which he holds at a distance, before pocketing it."

            else:
                jump silverbirthdaymenu

            red @happy "That's not all, though."

            silver @surprisedbrow talking2mouth "There's more?"

        ">Give him a battle":
            jump battlesilverbirthday

    label battlesilverbirthday:

    red @talkingmouth "A battle. For fun. Not one where you have to fight for anything, or defend against anything--not for a grade, or because you have to. Just for fun."

    silver -surprisedbrow "[ellipses]"
    silver @closedbrow talking2mouth "Yeah, I'd like that."
    silver @sadbrow happymouth "Though, even if this is a casual battle, with no stakes... you're still going down like a lead rocket."

    red @winkbrow talkingmouth "We'll see."

    python:
        trainer1 = MakeRed()
        trainer2 = MakeTrainer("Silver")

    call Battle([trainer1, trainer2], specialmusic="Nothing", stopmusic=False) from _call_Battle_183
    $ RecordBattle("Silver5")

    show silver smilemouth at night with dis

    if (WonBattle("Silver5")):
        $ ValueChange("Silver", 9)

    else:
        $ ValueChange("Silver", 3)

    silver @talkingmouth "You're strong. Real strong."

    if (not WonBattle("Silver5")):
        red night @sadbrow talkingmouth "I lost, though."

    else:
        red @talking2mouth "You are, too, man."

    silver @sadbrow talkingmouth "...Maybe 'real strong's' the wrong words. I never was great at putting words together the right way."
    silver @talking2mouth "I mean, uh... your strength is {i}real{/i}."

    red @talkingmouth "What's {i}real{/i} strength, to you?"

    silver @sadbrow happymouth "Strength you don't need to use."

    red @talkingmouth "If that's what strength is to you, then... you'll get there."

    silver @sadbrow talkingmouth "Yeah."
    silver @closedbrow happymouth "I'm a year closer."

    return