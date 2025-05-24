label Cheren1:
    call clearscreens() from _call_clearscreens_165
    scene blank2 with splitfade

    pause 1.0 

    "{color=#ff0000}You are no longer you.{/color}"

    stop music fadeout 1.5
    queue music "Audio/Music/eterna_start.ogg" noloop
    queue music "Audio/Music/eterna_loop.ogg"
    call clearscreens() from _call_clearscreens_225
    scene blank2 with splitfade

    show midnight at vspaz    

    python:
        timeOfDay = "Midnight"
        playercharacter = "Cheren"
        oldinventory = copy.copy(inventory)
        oldpersonalstats = copy.copy(personalstats)
        oldparty = copy.copy(playerparty)
        oldpersondex = copy.copy(persondex)
        oldclassstats = copy.copy(classstats)

        inventory = {
            Item.Notepad : 1,
            Item.SparePens : 7,
            Item.BrokenGlasses : 1,
            Item.TapeRoll: 1,
            Item.ToDoList : 1,
            Item.MusicPlayer : 1,
            Item.SpareTieClip : 1,
            184 : 1 # Paper with [first_name]'s Face
        }
        personalstats = {
            "Charm" : -7,
            "Knowledge" : 24,
            "Courage" : 71,
            "Wit" : 13,
            "Patience" : 3
        }
        playerparty = GetTrainerTeam("Cheren")
        persondex = copy.deepcopy(defaultpersondex)
        #battle teammates
        persondex["Cheren"] = {"Named" : True, "Value" : 0, "Contact": True, "Sex": Genders.Male, "Relationship": "Self", "RelationshipRank": 0, "Events": [] }
        persondex["Bianca"] = {"Named" : True, "Value" : 113, "Contact": True, "Sex": Genders.Female, "Relationship": "Disappointment", "RelationshipRank": 0, "Events": [] }
        persondex["Falkner"] = {"Named" : True, "Value" : 9, "Contact": False, "Sex": Genders.Male, "Relationship": "Underling", "RelationshipRank": 0, "Events": [] }
        persondex["Blue"] = {"Named" : True, "Value" : 17, "Contact": False, "Sex": Genders.Male, "Relationship": "Memory", "RelationshipRank": 0, "Events": [] }
        persondex["Nate"] = {"Named" : True, "Value" : 2, "Contact": False, "Sex": Genders.Male, "Relationship": "Memory", "RelationshipRank": 0, "Events": [] }
        persondex["Sabrina"] = {"Named" : True, "Value" : 34, "Contact": False, "Sex": Genders.Female, "Relationship": "Beggar", "RelationshipRank": 0, "Events": [] }
        persondex[first_name] = {"Named" : True, "Value" : oldpersondex["Cheren"]["Value"], "Contact": True, "Sex": Genders.Male, "Relationship": "Anathema", "RelationshipRank": 0, "Events": [], "Mood": 0 }
        persondex["Roxanne"] = {"Named" : True, "Value" : 14, "Contact": False, "Sex": Genders.Female, "Relationship": "Underling", "RelationshipRank": 0, "Events": [] }
        persondex["Brawly"] = {"Named" : True, "Value" : 8, "Contact": True, "Sex": Genders.Male, "Relationship": "Underling", "RelationshipRank": 0, "Events": [] }   
        persondex["Calem"] = {"Named" : True, "Value" : 28, "Contact": True, "Sex": Genders.Male, "Relationship": "Traitor", "RelationshipRank": 0, "Events": [] }
        persondex["Serena"] = {"Named" : True, "Value" : 24, "Contact": False, "Sex": Genders.Female, "Relationship": "Traitor", "RelationshipRank": 0, "Events": [] }
        persondex["Silver"] = {"Named" : True, "Value" : 68, "Contact": False, "Sex": Genders.Male, "Relationship": "Co-Worker", "RelationshipRank": 0, "Events": [] }
        persondex["Jasmine"] = {"Named" : True, "Value" : 22, "Contact": False, "Sex": Genders.Female, "Relationship": "Traitor", "RelationshipRank": 0, "Events": [] }
        persondex["Grusha"] = {"Named" : True, "Value" : 11, "Contact": False, "Sex": Genders.Male, "Relationship": "Traitor", "RelationshipRank": 0, "Events": [] }
        persondex["Gardenia"] = {"Named" : True, "Value" : 38, "Contact": True, "Sex": Genders.Female, "Relationship": "Target", "RelationshipRank": 0, "Events": [] }
        persondex["Skyla"] = {"Named" : True, "Value" : 53, "Contact": True, "Sex": Genders.Female, "Relationship": "Co-Worker", "RelationshipRank": 0, "Events": [] }
        persondex["Brendan"] = {"Named" : True, "Value" : 5, "Contact": False, "Sex": Genders.Male, "Relationship": "Schoolmate", "RelationshipRank": 0, "Events": [] }
        persondex["May"] = {"Named" : True, "Value" : 4, "Contact": False, "Sex": Genders.Female, "Relationship": "Schoolmate", "RelationshipRank": 0, "Events": [] }
        persondex["Melody"] = {"Named" : True, "Value" : 3, "Contact": False, "Sex": Genders.Female, "Relationship": "Dickless", "RelationshipRank": 0, "Events": [] }

        classstats = { 
            "Normal" : AimLevel() - 2,
            "Fire" : 1,
            "Water" : 1,
            "Grass" : 1,
            "Electric" : 1,
            "Ice" : 1,
            "Fighting" : 1,
            "Poison" : 1,
            "Ground" : 1,
            "Flying" : 1,
            "Psychic" : 1,
            "Bug" : 1,
            "Rock" : 1,
            "Ghost" : 0,
            "Dark" : AimLevel() - 1,
            "Dragon" : 1,
            "Steel" : 1,
            "Fairy" : 1
        }

    pause 3.5

    scene bedroommidnight 
    show screen currentdate
    with splitfade

    pause 2.0

    narrator "{color=#1f67df}But you have not been you for a while.{/color}"

    pause 1.0

    cherenmind night shirtless tired "...I'm so tired."
    cherenmind "Why can't I sleep...?"

    show phone_B 
    show brokenphone
    with fadeinbottom

    cherenmind "I'll call Dad. He's probably still up writing, anyway."

    $ PlaySound("vibrate.ogg")

    pause 3.0

    hide brokenphone
    show brokenphoneperson
    with Dissolve(1.0)

    dad "Heya, kiddo! I haven't heard from you in a while!"
    dad "{w=0.5}.{w=0.5}.{w=0.5}."
    dad "Hey, what's this? I can't see you, kid."

    cheren @sad2eyes talkingmouth "I... fell. My phone broke a little bit."

    dad "{w=0.5}.{w=0.5}.{w=0.5}."
    dad "Well, alright then, kiddo. Just let me know if you need a replacement!"

    cheren @talking2mouth "...Alright."

    pause 0.5

    cheren @talking2mouth sadbrow "I hope I didn't wake you up."

    dad "Not a chance! You know your old man. I've been working on this massive article--an exposé on the construction of the PWT!"
    dad "You'd never believe what those Driftveil contractors are doing. Get this--they're actually hiring illegal immigrants {i}on purpose{/i}, so they can blackmail them and force them to work for lower wages!"
    dad "Well, I won't stand for it! I don't care how many billions they're saving--no amount of money is worth the price of human dignity! As soon as I publish this article, their whole operation will crack like an egg!"
    dad "I tell ya, kiddo! This article will be bigger than the Bronius interview!"

    cheren @sad2brow talking2mouth "...Stay safe. An article like that will make you enemies."

    dad "Hah! Kiddo, {i}way{/i} too late for that one. I was running away from corporate thugs with Sawk on their belts since I was younger than you!"
    dad "And you know what? I'd do the whole thing again!"
    dad "Gahahahaha!"

    pause 1.0

    dad "Hey, Cheren. What's up? You're all quiet."

    cheren @talking2mouth "I'm... just tired."

    dad "C'mon, kiddo. I'm a journalist. I find truth. Besides that, you're my son--I know when you're upset."

    pause 1.0

    cheren @talking2mouth "It's... a deeper tiredness. Today was exhausting."

    dad @talkingmouth "Oh, yeah? Well, tell me about it."

    pause 1.0

    cheren @talking2mouth "Okay."

    stop music fadeout 1.5

    call clearscreens() from _call_clearscreens_226
    scene blank2 with splitfade

    pause 1.0

    show morning at vspaz

    $ timeOfDay = "Morning"

    pause 3.5

    show screen songsplash("Embracing One's Duty", "Zame")
    queue music "audio/music/embracingonesduty.ogg"

    scene studentcouncil
    show silver uniform:
        xpos 0.33
    show skyla uniform:
        xpos 0.66 xzoom -1
    show flashback
    show screen currentdate
    with splitfade

    cheren uniform @talkingmouth "Good morning, you two. I trust your patrols were uneventful. Damage report?"

    skyla @happy "All clear skies and smooth seas, Captain!"

    silver @talkingmouth "Someone set fire to a dumpster, Melody made two different girls (and one guy) cry, Brendan and May were caught in the janitor's closet again..."
    silver @closedbrow talkingmouth "On the faculty side of things, Siebold, Kofu, and Katy are fighting. Since they can't agree on what to cook, they're demanding a doubled kitchen budget to make two meals a day."

    pause 1.0

    skyla @happy "All clear skies and smooth seas, Captain!"

    silver @sadbrow talkingmouth "Oh, and someone made an effigy of you and hung it in the auditorium."

    cheren @confusedeyebrows talking2mouth "Oh? That's a new one."
    cheren @closedbrow talking2mouth "...Was it you?"

    silver @angrybrow happymouth "Well, I didn't stop them."

    cheren @tired talkingmouth "Ah... we have fun."

    pause 0.5

    cheren @talkingmouth "Well, I suppose I had better resolve some of these issues..."

    show gardenia uniform angrybrow frownmouth behind silver:
        xpos 1.2 ypos 1.0
        parallel:
            easein 0.3 ypos 0.7
            easeout 0.3 ypos 1.0
        parallel:
            ease 0.3 xpos 0.25
        parallel:
            pause 0.3
            ease 0.5 xzoom -1

    show skyla surprisedbrow frownmouth:
        xpos 0.66
        ease 0.5 xpos 0.75

    show silver surprisedbrow:
        xpos 0.33 xzoom 1
        ease 0.5 xpos 0.5 xzoom -1

    gardenia @angrymouth "Hey!"

    cheren @closedbrow talking2mouth "Good morning again, Gardenia. No, no-one said 'business.'"

    gardenia @talking2mouth "That's not it. I finally have it--{i}undeniable{/i} proof that this school is haunted!"

    cheren @closedbrow talking2mouth "We've talked about this. There's no such thing as ghosts, and your nagging that the Disciplinary Committee drop the important work we're doing to chase phantoms continues to grate on our limited time and patience."

    silver @sad "Important work? That's a laugh. I didn't sign up with you to actually {i}do{/i} Disciplinary Committee work, and even {i}I{/i} feel annoyed at how little we can actually do."

    skyla @angrybrow talkingmouth "We totally do important work! Just yesterday, we helped find a student's lost Poké Ball! Remember? We spent {i}all day{/i} on that."

    gardenia @surprised "A single Poké Ball? They cost, like, $200."

    silver @angry "That's what {i}I{/i} said! It didn't even have a Pokémon in it!"

    cheren @closedbrow talking2mouth "We're getting off-topic. Gardenia, we will not be participating in your ghost hunt. Please take this request to the Occult Club."

    gardenia @angry "I told you, that {i}won't{/i} work. Only people who don't believe in ghosts can get rid of them. The Occult Club is full of believers."

    cheren @sadbrow talkingmouth "And I suppose the instant we find these ghosts, we'd be helpless to 'exorcise' them? Presumably, finding them would make it quite clear that they are, in fact, real."

    show silver sad
    show skyla sad
    with dis

    gardenia @sad "...Just seeing isn't believing. Like how you can {i}see{/i} [first_name] isn't evil, but can't believe it. That stubbornness--that refusal to believe--is what's needed to {i}really{/i} get rid of a ghost."

    cheren shadow sadbrow noshine talking2mouth  "{w=0.5}.{w=0.5}.{w=0.5}."
    cheren @talkingmouth "If you won't leave, then I will. I have {i}real{/i} work to do."

    $ renpy.music.set_volume(0.8, 10)

    scene blank2 with splitfade

    dad "Hah! Every time you tell me about those two, they crack me up. Silver and Skyla, right? I'm pretty sure I know Skyla's Dad. Never heard of this Silver guy, but if he's a Johtonian, he's off my beat."

    cheren tired night shirtless @sadbrow talking2mouth "They tolerate me, which is more than can be said about most people."

    dad "I'd be careful about that Gardenia girl, though. I get a dangerous vibe from her. I feel like she knows exactly what she wants, and she's not going to take no for an answer."

    cheren @sad2brow talkingmouth "You're very right. Anyway, later in the day..."

    call clearscreens() from _call_clearscreens_227

    pause 1.0

    show noon at vspaz

    $ timeOfDay = "Noon"

    pause 3.5

    scene studentcouncil
    show flashback
    show screen currentdate
    with splitfade

    $ PlaySound("knock.ogg")

    pause 0.5

    cheren uniform @downeyes talking2mouth "Come in."

    show melody uniform on behind flashback with Dissolve(2.0)

    melody @talking2mouth "Yo, dickless."

    cheren @talking2mouth "My name is Cheren."

    melody @talking2mouth "Course it is."

    pause 1.0

    melody @talkingmouth "So, third time today, right? Do I get a prize?"

    cheren @talking2mouth "No."

    pause 1.0

    melody @talking2mouth "You're boring me."

    cheren @angrybrow talking2mouth "I am not here to entertain. You are here to think on what you have done wrong, in silence."

    melody @talking2mouth "Uh-huh. 'Cause I'm pretty sure Ex-Champion Wallace sent me here expecting you to punish me."

    cheren @closedbrow uniform "{w=0.5}.{w=0.5}.{w=0.5}."

    melody @talking2mouth "But you can't do that, can you?"

    cheren @talking2mouth "I will elevate this incident to the Student Council, as I have been instructed to do in matters concerning you."

    narrator "You write a note on a piece of paper, placing it on the stack next to you. The stack is already quite large."

    melody @talking2mouth "So dickless..."

    pause 1.0

    melody @talking2mouth "You know, if I'm going to be here so often, you could at least put a beanbag in here. Maybe hook a Wii up on that wall there. Do you do Mario Party? Mario Party co-op?"

    pause 1.0

    melody @sadbrow talking2mouth "Oh, no, of course you don't. Because that would require friends."

    pause 1.0

    melody @talking2mouth "{size=30}And a dick.{/size}"

    $ renpy.music.set_volume(0.6, 10)

    call clearscreens() from _call_clearscreens_228
    show blank2 with transeye 

    cherenmind @sad2brow talkingmouth "I'd almost prefer it were [first_name] who kept getting sent here..."

    pause 0.5

    dad "That Melody... what a piece of work! You said she was Lawrence Phobos' niece? Odd, I don't recall him having any siblings... but that guy's a real piece of work, too."
    dad "A coworker wrote an article about alleged illegal acts happening in Phobos' mansion, the 'Phobosphere'--what a tacky name--and he lost his job the next day. I'm not calling that a coincidence!"

    pause 0.5

    dad "Anyway, what happened next?"

    pause 1.0

    show afternoon at vspaz

    $ timeOfDay = "Afternoon"

    pause 3.5

    scene studentcouncil
    show flashback
    show screen currentdate
    with splitfade

    $ PlaySound("knock.ogg")

    pause 0.5

    cheren uniform @downeyes talking2mouth "Come in."

    show brendan sadbrow uniform behind flashback:
        xpos 0.33
    show may sadbrow uniform behind flashback:
        xpos 0.66
    with dis

    cheren @surprised "Oh? You two? What..."
    cheren @sadbrow talkingmouth "Oh. Was it the janitor's closet again?"

    brendan @talking2mouth "Empty classroom."

    may @talkingmouth "Well, we {i}thought{/i} it was empty."

    cheren @closedbrow sweat talking2mouth "You're putting me in an exceedingly awkward position."
    cheren @sad2brow talkingmouth "Obviously, a little physical affection between consenting adults is not exactly something I wish to punish..."
    cheren @upeyes talking2mouth "But at this point, you've been warned to tone it down so many times, it truly feels like direct rebellion."

    brendan @surprised "I... I swear, it wasn't, man! It's just, when we're together... I mean..."

    may @talkingmouth "Come on. We just love each other so much, Cheren. You {i}must{/i} love someone that much, too, right? Surely you understand."

    cheren @sad2brow talking2mouth "...I do."

    pause 0.5

    show may angrybrow frownmouth
    show brendan angrybrow frownmouth
    with dis

    cheren @closedbrow talking2mouth "But I cannot simply let you off with a warning, this time. You've had enough chances."

    brendan @talking2mouth "Tch."

    may @angry "Great job keeping the school safe from seeing a healthy relationship, Cheren. Thank goodness you're here to save us from that."

    $ renpy.music.set_volume(0.4, 10)

    call clearscreens() from _call_clearscreens_229
    show blank2 with transeye 

    narrator "You scribble a note, and add it to the pile on your desk. The pile bulges, and seems as though it is about to topple."
    narrator "The note you just added slides off the top, into the trashcan next to your desk. You pretend not to notice."

    cherenmind @sad2brow talkingmouth "...I really do understand. Brendan, May... I understand more than you ever could."

    pause 0.5

    dad "Hah hah! College PDA. Classic, kiddo. Hey, you aren't getting into anything you shouldn't, are you? But if you are, well, college is the time for it. Just remember to wear protection!"

    pause 0.5

    dad "Ah, you probably don't want to hear your old man saying that, huh? My bad. How about the rest of your day?"

    pause 1.0

    show evening at vspaz

    $ timeOfDay = "Evening"

    pause 3.5

    scene library
    show flashback
    show screen currentdate
    with splitfade

    pause 0.5

    cherenmind uniform @closedbrow talking2mouth "Alright. I've put this off long enough. I need to do this now."

    show sabrina casualoldhair behind flashback with dis

    pause 1.0

    cheren @talkingmouth "Sabrina, I--"

    sabrina @closedbrow talking2mouth "You wish to apologize."

    cheren @sad2brow talking2mouth "...Yes."

    pause 1.0

    cheren @talking2mouth "I truly--"

    sabrina @closedbrow talking2mouth "You truly never meant any harm to anyone except [first_name]. And even then, you only wanted to bring him down to everyone else's level."
    sabrina @sad2brow talking2mouth "But your passion got the better of you, and you saw how dire the situation was when the school was 'invaded'. You believed drastic measures were necessary."
    sabrina @talking2mouth "You feared meeting with him one-on-one and accusing him directly, as, if he was morally bankrupt, as you feared, he may remove your ability to tell others."
    sabrina @talking2mouth "You left your 'allies' without oversight, believing that they would simply talk to other students and gain compromising information, as you had done. You never meant for me to hurt."
    sabrina @talking2mouth "I know."

    pause 1.0

    show sabrina casualoldhair psychicangryeyes gen1aura: 
        ypos 1.0
        ease 2.0 ypos 0.8
        parallel:
            ease 2.0 ypos 0.85
            ease 2.0 ypos 0.8
            repeat

        parallel:
            ease 2.0 xpos 0.52
            ease 2.0 xpos 0.5
            ease 2.0 xpos 0.48
            ease 2.0 xpos 0.5
            repeat

    sabrina @angryeyebrows psychicfuriouseyes angrymouth "I've had to hear you rehearsing this speech in your head for {i}weeks.{/i} Over and over... just {i}waiting{/i} for you to finally say the words."

    cheren @surprisedbrow talking2mouth "I... my intentions were only ever good..."

    sabrina @talking2mouth "I {i}know{/i}."
    sabrina @talking2mouth "And because I cannot help but know your intentions, you feel entitled to my empathy."
    sabrina psychicfuriouseyes angryeyebrows angrymouth "You will not get it. Take nothing but my scorn. Take it, leave with it, and stay gone."

    cheren @sadbrow "{w=0.5}.{w=0.5}.{w=0.5}."

    cheren @shadow closedbrow talking2mouth "As you wish."

    $ renpy.music.set_volume(0.2, 10)

    call clearscreens() from _call_clearscreens_230
    show blank2 with transeye 

    dad "{w=0.5}.{w=0.5}.{w=0.5}."
    dad "Are you alright, kiddo?"

    show night at vspaz

    $ timeOfDay = "Night"

    pause 3.5

    scene studentcouncilnight
    show flashback
    show screen currentdate
    with splitfade

    pause 0.5

    cherenmind night uniform @closedbrow talkingmouth "Finally. Almost time to go back to the dorm..."
    cherenmind @sad2brow smilemouth "Where I can be surrounded by people who may hate me, but at least don't talk to me."

    queue sound "audio/knock.ogg"

    pause 1.5

    cheren @surprised "Huh? Who is it? The Disciplinary Committee is closed for today--"

    show falkner behind flashback at night with Dissolve(2.0)

    falkner @talking2mouth "Cheren."

    cheren @closedbrow talkingmouth "*{i}Sigh.{/i}*"
    cheren @talkingmouth "Thank goodness, it's just you. I thought it was a late-night complaint, or..."

    pause 0.5

    cheren @sad2brow talking2mouth "You don't look happy."

    falkner @talking2mouth "I'm not, Cheren. That pile of reports you gave us this afternoon--why wasn't Brendan and May's PDA reported there?"

    cheren @sadbrow talking2mouth "...What?"

    falkner @talking2mouth "We know they were caught, and reported here, as instructed."
    falkner @angrybrow talking2mouth "Brendan told us later, to apologize for giving us more work."
    falkner @talking2mouth "But we didn't have any work, because we were never told."

    pause 1.0

    cherenmind @sadbrow "No good deed goes unpunished."

    cheren @shadow sad2brow talking2mouth "It's a foolish rule. A relic of Kobukan's past. We are not children. This is not a high school. Brendan and May did nothing wrong."

    falkner @angry "That is not for you to decide. You had your chance to change the law when you were running for Student Council. You now exist to {i}serve{/i} the law, not debate it."

    cheren @sad2brow shadow "{w=0.5}.{w=0.5}.{w=0.5}."

    falkner @talking2mouth "Roxanne will tell Drayden about this. I imagine he'll have words for you. Remember, you are a member of the Disciplinary Committee as a {i}punishment{/i}."

    cheren @shadow sad2brow talking2mouth "This is not justice."

    falkner @closedbrow talking2mouth "Justice is an ephemeral--a convenient spirit that means only what the speaker says."
    falkner @talking2mouth "What we want, concretely, is a school where the Student Council can rely on the Disciplinary Committee to follow the established rules laid out, until such a time as they're changed."

    pause 1.0

    falkner @talking2mouth "'Justice' is a ghost."
    falkner @talking2mouth "Do what you said you would do."
    falkner closedbrow talking2mouth "Stop chasing ghosts."

    hide falkner with Dissolve(2.0)

    stop music fadeout 2.0

    call clearscreens() from _call_clearscreens_231
    show blank2 with transeye 

    pause 0.5

    show midnight at vspaz

    $ timeOfDay = "Midnight"

    pause 3.5

    scene bedroommidnight
    show phone_B 
    show brokenphoneperson
    show screen currentdate
    with splitfade

    dad "{w=0.5}.{w=0.5}.{w=0.5}."
    dad "There are bad days, kiddo. There will always be bad days. Things'll turn around."

    cheren night shirtless @sadbrow tears talking2mouth "...I hope you're right."
    cheren @sadbrow talking2mouth "But... what if I don't deserve for them to turn around? What if this, forever, is what I deserve?"

    pause 1.0

    dad "I can't believe that."

    pause 0.5

    dad "It's easy to give up. Every time I bust out the typewriter, I have to consider if I'm okay ruining my life over what I'm about to write."
    dad "And people have promised all sorts of things in retaliation. If I had a nickel for every time someone said 'I'd regret this', I coulda sent you to Kobukan {i}twice.{/i}"
    dad "And you know what? Sometimes, I did. Sometimes I {i}did{/i} regret it. But even when I thought I'd done something wrong, I knew I {i}meant{/i} to do the right thing."
    dad "That's all anyone can do. Besides, call it my bias, but I don't think you did anything wrong."

    cheren @sad2brow talking2mouth "I hurt hundreds of innocent people. I... I may have only managed to expose a {i}single{/i} person who actually deserved it."

    dad "Kid... you're my boy, Cheren. From the first moment I held you in my arms, I knew I would love, trust, and believe in you, no matter who or what you became."
    dad "My only fear when you left Unova was that you'd come back thinking you had to be like {i}them{/i} to win. And everything you're telling me tells me that you're as far from that as you ever were."

    cheren @closedbrow angrymouth cry "Dad..."

    dad "Keep your head up, kiddo."
    dad "And call me more often. I miss you. It's lonely here without you."

    pause 0.5

    dad "...Remember, kid. Even when your Mom left us, I knew I'd done the right thing."
    dad "If I can still hold my head high and believe in justice after that, you can too."

    pause 1.0

    dad "Maybe justice {i}is{/i} a ghost."
    dad "But is there really anything so wrong with chasing ghosts?"

    pause 0.5

    dad "Love you."

    hide phone_B 
    hide brokenphoneperson
    with fadeoutbottom

    pause 2.0

    cherenmind @sad2brow talking2mouth "...It seems that positively affecting reality absolutely eludes me."
    cherenmind @sad2brow smilemouth "Perhaps it is only in fiction, then, that my influence can be found."

    stop music
    $ renpy.music.set_volume(1)
  
    queue music "audio/music/potown_start.ogg" noloop fadein 2.5
    queue music "audio/music/potown_loop.ogg"

    show phone_B
    show brokenphone
    with fadeinbottom

    show phone_C behind brokenphone with dis

    show phone_msg1 behind brokenphone with dis:
        xzoom -1
        
    $ title = Text("Gardenia Natane",size=30,font="fonts/consola_0.ttf",color="#313131")

    image msg6 = Text("Fine.\nRemind me, what was that poem you held\nso much stock in? The cause of all\nthose early-morning interruptions?",size=21,color="#ffffff",line_spacing=5,text_align=0.0)

    show text title behind brokenphone:
        xalign 0.51 yalign 0.34 
    show msg6 behind brokenphone:
        xpos .41 ypos .4 
    with dis

    pause

    call clearscreens() from _call_clearscreens_232
    scene blank2 with Dissolve(2.0)

    image poemline1 = Text("In hallowed halls, old with wear",size=30,color="#fff")
    image poemline2 = Text("Shadows call to those who dare",size=30,color="#fff")
    image poemline3 = Text("One Living, Ghost in mortal shell",size=30,color="#fff")
    image poemline4 = Text("One Changed, Ghost back from hell",size=30,color="#fff")
    image poemline5 = Text("One Dead, Ghost here further more",size=30,color="#fff")
    image poemline6 = Text("Two Unfed, Ghosts once adored",size=30,color="#fff")
    image poemline7 = Text("By day they hide, by night they roam",size=30,color="#fff")
    image poemline8 = Text("Haunted spectres far from home",size=30,color="#fff")
    image poemline9 = Text("Disaster comes with undrawn breath",size=30,color="#fff")
    image poemline10 = Text("{gradient=#fff-#f00}If not freed, naught else comes but death{/gradient}",size=30,color="#fff")

    show poemline1 with gaussdissolve:
        ypos 1/13 xalign 0.5 yanchor 0.5

    pause 0.5

    show poemline2 with gaussdissolve:
        ypos 2/13 xalign 0.5 yanchor 0.5

    pause 0.5

    show poemline3 with gaussdissolve:
        ypos 3/13 xalign 0.5 yanchor 0.5

    pause 0.5

    show poemline4 with gaussdissolve:
        ypos 4/13 xalign 0.5 yanchor 0.5

    pause 0.5

    show poemline5 with gaussdissolve:
        ypos 5/13 xalign 0.5 yanchor 0.5

    pause 0.5

    show poemline6 with gaussdissolve:
        ypos 6/13 xalign 0.5 yanchor 0.5

    pause 0.5

    show poemline7 with gaussdissolve:
        ypos 7/13 xalign 0.5 yanchor 0.5

    pause 0.5

    show poemline8 with gaussdissolve:
        ypos 8/13 xalign 0.5 yanchor 0.5

    pause 0.5

    show poemline9 with gaussdissolve:
        ypos 9/13 xalign 0.5 yanchor 0.5

    pause 0.5

    show poemline10 with gaussdissolve:
        ypos 10/13 xalign 0.5 yanchor 0.5

    pause

    python:
        inventory = oldinventory
        personalstats = oldpersonalstats
        playerparty = oldparty
        persondex = oldpersondex
        classstats = oldclassstats
        playercharacter = None
        AddEvent("Cheren", "Scene1")
        persondex["Cheren"]["RelationshipRank"] = 1
        maxliberationlimit += 20

    scene blank2 with splitfade

    narrator "As the enemy forces gather in the night, the banner of liberation flies higher, readying for the fight! Your resolve resonates through [pika_name]."
    narrator "[pika_name]'s Liberation Limit increased by [bluecolor]twenty{/color}!"

    return

label Cheren2:
    show screen songsplash("Embracing One's Duty", "Zame")
    stop music fadeout 1.5
    queue music "audio/music/embracingonesduty.ogg"

    scene lobby_night with splitfade

    show cheren og with dis

    cheren @talking2mouth "[last_name]."

    red @unamusedbrow talking2mouth "Oh, we're doing that thing where we call each other by our last names, now?"
    red @angrybrow talking2mouth "You're not cool, you know."

    cheren @confusedbrow "[ellipses]"
    cheren @closedbrow talking2mouth "It was the first thing that came to mind. I assure you, coolness is not a factor in any part of my presentation to you."

    red @talking2mouth "You're wearing new clothes."

    cheren @talking2mouth "I've been out and about at night quite a bit for the last couple weeks. The jacket was a practical choice."
    cheren @sad2brow talkingmouth "The plunging v-neck is because a man occasionally likes to feel sexy. Melody certainly had thoughts to share on the matter."

    red @closedbrow talking2mouth "Whatever. I'm still just calling you Cheren. What do you want?"

    cheren @talking2mouth "What I want is immeasurate. What I expect to achieve is within much smaller boundaries."

    red @unamusedbrow unamusedmouth "[ellipses]"
    redmind @upbrow frownmouth "This guy is {i}exhausting{/i} to talk to."

    cheren @sad2brow talkingmouth "In any case, I'm here to deliver your punishment."

    red @closedbrow talking2mouth "If you take your clothes off, I swear to god--"

    cheren @upeyes talking2mouth "Oh, don't you have a high opinion of yourself? Perhaps I need remind you that--"

    show cheren surprisedbrow frownmouth with dis

    show silver:
        xpos 1.2 xzoom -1
        ease 0.5 xpos 0.75

    show skyla sadbrow:
        xpos -0.2 
        ease 0.5 xpos 0.25

    silver @angry "God almighty, could you two get a goddamn room to hate each other in where we don't have to see it?"

    skyla @sadbrow talkingmouth "Sorry, Cheren, but I {i}did{/i} say you should let me recruit him."

    cheren -surprisedbrow @sad2brow talking2mouth "...In retrospect, that might have been a good idea. But, as I stated, this is not a matter of recruitment. It's a matter of compulsion."

    red @talking2mouth "What the hell kinds of grounds do you have to compel me to do {i}anything{/i}?"

    cheren @closedbrow talkingmouth "Can you really not think of {i}anything{/i}?"

    #FIX THIS: Add more nighttime scenes here, when they're written.
    if (GetRelationshipRank("Klara") > 0 or GetRelationshipRank("Grusha") > 0 or HasEvent("Wally", "Wally1Part2")):
        if (GetRelationshipRank("Klara") > 0):
            cheren @talking2mouth "You went out into Inspira with Klara, after curfew, did you not?"

        if (GetRelationshipRank("Grusha") > 0):
            extend @talking2mouth " Didn't you follow Grusha into Inspira after curfew?"

        if (GetRelationshipRank("Klara") > 0 or GetRelationshipRank("Grusha") > 0):
            red @talking2mouth "How do you know that?"

            cheren @talking2mouth "People are ever-so-willing to talk about you. Especially if they think what they say will give me more work."

            red @angryeyebrows sad2eyes talking2mouth "Well, did these 'people' tell you I had a good reason to go out?"

        if (HasEvent("Wally", "Wally2Part2")):
            cheren @closedbrow talking2mouth "It's a pattern of behavior, [first_name]."

            cheren @talking2mouth "You were well aware that curfew was in place shortly after Wally was robbed--and though we recruited you, then, I think we can all agree that event was not, perhaps, by the books."

    cheren @confusedbrow talking2mouth "Why, you'd even do it directly in front of faculty. You were, after all, out after curfew not long ago. Professor Cherry can testify to that."

    red @angry "We both lost track of time!"

    cheren @angrybrow talking2mouth "So did many others who were rightly punished. In a school of thousands, why should there be an exception for you?"

    red @angry "You got one! You're still here, instead of being kicked out!"

    cheren @angry "{i}That{/i} was an exceptional {i}punishment{/i}! I wished to be expelled for the hurt I caused, but Dean Drayden refused to let me--the {i}opposite{/i} of what he did for you, who he let drop out {i}and{/i} rejoin without fanfare!"

    red @angryeyebrows sad2eyes talking2mouth "That's ridiculous. How could he 'refuse' to let you drop out? You make your own choices."

    cheren @sad2brow talking2mouth "Never have I ever."

    pause 1.5

    silver @talking2mouth "Right. New rule. You two don't get to talk to each other anymore."

    cheren @confused "What?"

    red @confused "What?"

    skyla @closedbrow talking2mouth "Silver's right. If you can't think of something nice to say, don't say anything at all."

    redmind @frownmouth "Fine. If he shuts up, then I've got nothing to say to him."

    show cheren upeyes frownmouth with dis

    silver @talking2mouth "Cheren's making a big deal about this because he doesn't want to admit that we'd like your help."

    show cheren -upeyes with dis

    skyla @closedbrow talkingmouth "We on the disciplinary committee have a mission! And we think you'd be the best person to help us with it."

    red @talking2mouth "What, do you want me patrolling the hallways to yell at people out of their dorms late?"

    silver @talking2mouth "Not exactly."

    skyla @talking2mouth "We should probably let you talk to 'Commissioner G' first."

    red @confused "Who?"

    silver @talkingmouth "It's just Gardenia. She's 'hiring' us to investigate a bunch of rumors about ghosts around the school."
    silver @sadbrow talking2mouth "It'll be a small job, probably--find the ghosts, I battle them, Cheren catches them--but we're having trouble even getting started."

    skyla @sadbrow talking2mouth "We know the citizens know {i}something{/i} about the mysterious happenings, but they're all tight-lipped."

    silver @sad "Yeah, I... scare them off, and they don't want to talk to Cheren."

    cheren @talking2mouth "Skyla's had the most luck... and frankly, we're not sure how much of what she's reported is accurate, and how much is creative embellishment."

    skyla angrybrow frownmouth @talking2mouth "Boss!"

    silver @sadbrow talking2mouth "It doesn't help that she's reporting {i}everything{/i} she finds as gospel." 
    silver @closedbrow talking2mouth "We were trying to find a couple of Ghost-type Pokémon, but if we took Skyla seriously, we'd be finding demons, supervillains, and aliens around every corner."

    skyla @closedbrow talking2mouth "You {i}should{/i} take my reports seriously. I'm the only one who knows what we're looking for. For example, Gardenia doesn't want us to find Ghost-type Pokémon--she says there's {i}actual{/i} ghosts in the school."

    cheren @closedbrow talking2mouth "Which is obviously insane."

    silver @talking2mouth closedbrow "We can agree on that one. {w=0.5}Ghosts exist, but not at this school."

    cheren @surprisedbrow "[ellipses]"
    cheren @sad2brow talking2mouth "{size=30}Oh, dear.{/size}"

    skyla @talking2mouth "So, um, since the boys are so grumpy and mean, I guess I've got to ask nicely--"
    skyla @winkbrow talkingmouth "We were {i}really{/i} hoping you could help us gather some clues!"

    red @unamusedbrow unamusedmouth "[ellipses]"

    show skyla surprisedbrow frownmouth
    show silver surprisedbrow
    show cheren surprisedbrow
    with dis

    red @closedbrow talking2mouth "The only reason I'm even considering saying yes is because I'm pretty sure I already have the information you want."

    pause 1.5

    silver @talking2mouth "You're shitting us?"

    show skyla -surprisedbrow -frownmouth
    show silver -surprisedbrow
    show cheren -surprisedbrow
    with dis

    red @sadbrow talkingmouth "No shit here. A few students--and even Professor Cherry--mentioned some weird stuff they've seen around campus at night."

    skyla @angrybrow happymouth "Incredible! As expected of my [GetRelationship('Skyla')]!"

    silver @talking2mouth "Well, what is it? What did they say?"

    scene garden night at sepia
    show kris at night, sepia
    show flashback
    with splitfade

    kris @talking2mouth "Oh, I just... I heard rumors that some students have seen flickering, bright images around the school. Silhouettes of a person wearing long robes..."

    scene concerthallnight at sepia
    show melody noglasses at night, sepia
    show flashback
    with splitfade

    melody @talking2mouth "Singing. The Contest Hall is haunted. And, sometimes, the ghosts sing."

    scene library2 night at sepia
    show raihan at sepia
    show flashback
    with splitfade
    
    raihan @talking2mouth "Got this odd problem with my Rotom here. Picking up some sort of signal I can't make heads nor tails of."

    scene cafenight at sepia
    show wally at sepia
    show flashback
    with splitfade

    wally @talking2mouth "Hm... just, like, big, floating, glowing balls. Like, blue flames, pink flames, I guess. I haven't seen them myself."

    show blank with splitfade

    pause 2.0

    scene lobby_night 
    show skyla:
        xpos 0.25
    show cheren og
    show silver:
        xpos 0.75 xzoom -1
    with splitfade

    skyla @happy "Wow! You're like... the world's greatest detective or something!"

    silver @closedbrow talking2mouth "I gotta admit, I'm impressed, too."

    show cheren angryeyebrows with dis

    red @sadbrow talking2mouth "...To be honest, I didn't even know I was looking for clues. People just kinda told me stuff, and..."

    pause 1.0

    redmind @closedbrow frownmouth "'I guess that's another example of you getting what you want without trying for it.' I know that's what you're thinking, Cheren."

    show cheren -angryeyebrows with dis

    if (HasEvent("Klara", "AcceptCoordinatorClub")):
        red @talking2mouth "There was also a weird moment when I was in the Contest Coliseum a while ago. I thought I went into a changing room for, like, one or two minutes." 
        red @confused "The lights flickered, and when I left, a friend told me that I'd been gone for more than half an hour."

    cheren @talking2mouth "It seems apparent that our quarry is in the Contest Coliseum, then. A Ghost-type creating brightly-lit Will-o-Wisps, singing, and causing visions of robed figures..."
    cheren smilemouth @sad2brow talkingmouth "It's almost too easy."

    skyla @talkingmouth "Boss? Do you know what it is?"

    cheren @closedbrow talking2mouth "Absolutely."

    silver @sadbrow talking2mouth "This'll be good. What do you think it is, then?"

    $ AddEvent("Professor Oak", "LearnedAboutContestColiseum")

    cheren @talking2mouth "Come with me. We're going to the Contest Coliseum."

    red @closedbrow talking2mouth "Do I--"

    show cheren:
        xpos 0.5 xzoom 1
        ease 0.5 xzoom -1
        ease 0.5 xpos -0.25

    show skyla:
        xpos 0.25 xzoom 1
        ease 0.5 xzoom -1
        ease 0.5 xpos -0.5

    show silver:
        xpos 0.75
        pause 0.5
        ease 0.5 xpos -0.25

    pause 2.0

    redmind @angrybrow frownmouth "...As much as I hate to admit this, I'm madly curious as to what this 'ghost' actually is."

    scene blank2 with splitfade

    pause 1.0

    scene concerthallnight with splitfade

    narrator "'You and the Disciplinary Committee stealthily sneak through the pitch black. Your heart beats to an unfamiliar rhythm as the spectral whispers around you surround, suggest, and imply actions both terrible and great.'"
    narrator "'Skyla marches ahead, leading the nervous expedition with great vigor and bravery. The moonlight shone on her toned bod in a way that was both alluring and approved by the Comics Code Authority.'"
    narrator "'You are filled with admiration at her bravery as she grips her Poké Balls, knuckles white with heroic passion. She gives each team member a swift nod, and--'"

    show cheren og sadbrow at night with dis

    cheren @talking2mouth "Skyla, please stop that."

    show skyla at night with dis:
        xpos 0.25 

    skyla @talkingmouth "Just trying to keep the mood up."

    show silver at night with dis:
        xpos 0.75 xzoom -1

    silver @closedbrow talking2mouth "{size=30}And my blood pressure.{/size}"

    cheren angrybrow @neutralbody talking2mouth "Now, there's one thing you should all understand before we go in here. We are almost certainly going to be facing a--"

    red night @talking2mouth "Mismagius."

    pause 2.0

    cheren -angrybrow @talking2mouth "Yes, a Mismagius. They are the only Pokémon I know of that is known to sing, create illusions--hallucinations, rather--and can learn Will-O-Wisp. It even has a robed form, to boot."

    silver @talking2mouth "What about that weird signal that Raihan's Rotom was getting?"

    cheren @talking2mouth closedbrow "I am unsure. Perhaps Rotom is especially receptive to Mismagius' songs?"

    red @talking2mouth "That's the best I've got right now, too."

    cheren @talking2mouth "In any case, this should not be a difficult battle, unless this particular Mismagius is extremely powerful."
    cheren @talkingmouth "Keep in mind that whatever you are fighting may not be real. Mismagius is known to conjure illusions of even legendary Pokémon, such as Rayquaza, to intimidate foes."
    
    red @talking2mouth "It's a pure Ghost-type, so just keep hitting it with the same Dark-type attacks you'd normally use, Silver and Cheren."
    red @sweat talking2mouth "Skyla, I'm not sure if you have any Pokémon with Ghost or Dark moves, but try to hit it physically, and fast, if you can. It has low physical defense, and if you use priority moves, its high speed doesn't matter."

    cheren @talking2mouth "It's hardly a problem for the four of us."

    red @talking2mouth "Four... oh, right. How come Gardenia isn't coming?"

    skyla @sadbrow talkingmouth "She's... {i}really{/i} scared of the ghosts here. That's why she wanted us to track these rumors down and get rid of them."

    cheren @talkingmouth sadbrow "Technically, she only asked us to verify their existence... but it would be nice to exceed expectations for once."

    cheren @talking2mouth "I have a plan. We will form, perhaps, groups of two. To minimize animous pairings, Silver, if you would go with [first_name], then--"

    stop music

    show cheren surprisedbrow
    show skyla surprisedbrow frownmouth
    show silver surprisedbrow
    with vpunch

    Character("{color=#00712b}???{/color}") "\"{size=40}Aaaaaaaaaaaaaaaaaaaaaaaaah!{/size}\""

    skyla @surprised "Someone's screaming! Should we--"

    cheren @angrybrow talking2mouth "Scrap the plan. We go now, together."

    show cheren:
        xpos 0.5
        ease 0.7 xpos 0.4
        ease 0.2 xpos 1.5

    show skyla at night:
        xpos 0.25
        pause 0.3
        ease 0.7 xpos 0.15
        ease 0.2 xpos 1.5

    show silver at night:
        xpos 0.75 xzoom -1
        ease 0.5 xzoom 1
        ease 0.7 xpos 0.65
        ease 0.2 xpos 1.5

    pause 2.0

    scene blank2 with splitfadefast

    pause 1.0

    scene concerthallhallwaynight with splitfadefast

    queue music "audio/music/potown_start.ogg" fadein 10.0
    queue music "audio/music/potown_loop.ogg"

    narrator "You find yourself in a hallway, alone. It seems you ran too fast, and outpaced the rest of the Disciplinary Committee by a fair margin."

    red @closedbrow talking2mouth sweat "I really gotta stop doing that."

    pause 1.0

    red @angrybrow talking2mouth "But since I'm here..."
    red @angrybrow frownmouth "[ellipses]"

    narrator "You search the hallway, briefly, but don't see anything out of the ordinary. Whoever--{i}what{/i}ever let out that scream earlier isn't here now."

    red @talking2mouth "Hey, is anyone there? I'm here to help. {w=0.5}...Whatever way the situation needs."

    pause 0.5 

    narrator "Silence for a moment, then..."

    show gardenia sadbrow frownmouth:
        ypos 0.0
        linear 0.2 ypos 1.0

    pause 0.2

    show concerthallhallwaynight with vpunch

    red @surprised "Woah!"
    red @happy "That was pretty cool. How did you--"

    python:
        vowels = "aeiouyAEIOUY"
        vowelfound = False
        
        for i, char in enumerate(first_name):
            if char in vowels:
                # Split into three parts
                before = first_name[:i + 1]
                vowel = char
                after = first_name[i:]
                vowelfound = True
                break

    if (vowelfound):
        gardenia tear @scaredmouth sadbrow "[before]-[vowel]-[vowel]-[vowel]-[after]!"
    else: 
        gardenia tear @scaredmouth sadbrow "[first_name]!"

    show gardenia:
        ypos 1.0 zoom 1.0
        ease 0.5 ypos 1.2 zoom 1.3

    gardenia @sadbrow scaredmouth "I thought I could find the ghosts, I thought I could be brave, but I {i}can't{/i}, I just {i}can't{/i}, and now they're going to get me and they're going to steal me away, and I'm too young to become a ghost, and I haven't spent all my money yet!"

    narrator "Gardenia clings to your vest, hands trembling. Though clearly scared out of her mind, it's almost an amusing scene, seeing the fast-talking Gardenia scared of... what, exactly?"

    red @sadbrow talkingmouth "Gardenia, calm down. What happened? What's wrong?"

    gardenia @sadbrow scaredmouth "The ghost is here. It's {i}here!{/i} I've got all the information that proves it. The flickering, robed figure, the 'Will-O-Wisps', the singing and signals--I came out here to try and handle it myself, but the ghost--the ghost--!"

    red @sadbrow talkingmouth "Gardenia, come on. It's just a Pokémon. All those things you described are things Mismagius can do."

    show gardenia:
        ypos 1.2 zoom 1.3
        ease 0.5 ypos 1.0 zoom 1.0

    gardenia @angrybrow scaredmouth "What? No, it's {i}not{/i}! It's not just a Pokémon!"

    cheren og @talking2mouth "Ahem."

    gardenia -tear @surprised "Oh! You guys are here, too?"

    show gardenia:
        xpos 0.5 ypos 1.0 zoom 1.0
        ease 0.5 xpos 0.8

    show silver:
        xpos -0.1 xzoom -1
        ease 0.5 xpos 0.6

    show cheren og:
        xpos -0.1 
        ease 0.5 xpos 0.4

    show skyla:
        xpos -0.1 
        ease 0.5 xpos 0.2

    cheren @talking2mouth "Seemingly. Though I wonder to what end, given our client is here as well?"
    cheren @sad2brow talking2mouth "Far be it from me to question what you spend your money on, but does this not make us a bit redundant?"

    gardenia @sadbrow talking2mouth "Er, wait, I--"

    show skyla sadbrow frownmouth with dis

    silver @angry "I get it. We were distractions, huh? By paying us to 'look for ghosts', ghost-hunting became Disciplinary Committee business. So now you can go out after curfew, because you're 'assisting in disciplinary committee business.'"
    silver @closedbrow talking2mouth "We got played."

    gardenia @surprised "Wait, wait, that's not it at all! There really is, absolutely, a ghost in here! I just saw it--it flew right at me! It was this shimmering, kind of, blue person wearing a long robe, and--"

    cheren @talking2mouth sad2brow "It's a Mismagius."

    gardenia @angrybrow talking2mouth "It's {i}not{/i}!"

    skyla @talking2mouth "I think it kinda is."

    gardenia @sadbrow talking2mouth "What? Even you? Why?"

    play music "<from 29>audio/music/ionozone.ogg"

    skyla @talking2mouth "Because I can see it. It's right there."

    show gardenia with vpunch:
        xpos 0.8 
        ease 0.1 xpos 0.95

    gardenia @surprised "Agh!"

    pause 1.0

    gardenia @talking2mouth "Wait... where?"

    skyla @talking2mouth "It's staying hidden, but there, behind that pillar. You just kinda have to squint at--"

    show cheren surprisedbrow 
    show silver surprisedbrow
    show skyla surprisedbrow frownmouth
    show gardenia surprisedbrow frownmouth
    with dis

    skyla @surprised "Wait, nevermind, here it comes! Boss, code F!"

    show mismagius:
        xanchor 0.5 yanchor 0.5 xpos 1.2 ypos -0.2 zoom 0.3
        ease 0.5 xpos 0.5 ypos 0.5 zoom 1.5

    cheren angrybrow @talking2mouth "Hold on, [first_name]--do not engage! It's--"

    red @angrybrow talking2mouth "Screw that!"

    python:
        trainer1 = MakeRed()
        mismagius = GetTrainerTeam("Iono", "Mismagius")
        sidemonnum = pokedexlookupname("Mismagius", DexMacros.Id)
        trainer2 = Trainer("sideportraitfull", TrainerType.Enemy, [mismagius], number=1, isPokemon=False)

    show gardenia behind cheren:
        xpos 0.8 ypos 1.0 zoom 1.0
        block:
            ease 0.5 xpos -0.2
            pause 4.0
            xzoom -1
            ease 0.5 xpos 1.2
            pause 4.0
            xzoom 1
            repeat

    hide mismagius

    call Battle([trainer1, trainer2], dialogfunc=mismagiusbattle, customexpressions=["red angrybrow frownmouth", "red angrybrow happymouth", "sideportraitfull", "sideportraitfull"], stopmusic=False, specialmusic="Nothing") from _call_Battle_91
    $ RecordBattle("Iono1")

    if (not WonBattle("Iono1")):
        jump gameover
        
    show screen songsplash("Embracing One's Duty", "Zame")
    stop music fadeout 1.5
    queue music "audio/music/embracingonesduty.ogg" fadein 2.0

    cheren @talking2mouth "Well done."

    silver @closedbrow talking2mouth "So it really was a Mismagius. I guess you two knew what you were talking about."

    skyla @sadbrow talkingmouth "Um, Gardenia, you can stop running now."

    show gardenia:
        zoom 1.0 ypos 1.0
        ease 0.5 xpos 0.8 xzoom 1

    gardenia @sadbrow talkingmouth "Thanks..."

    cheren @talking2mouth "Of course, defeating this Mismagius only raises further mysteries."

    if (HasEvent("Professor Oak", 'TriedToCatchIonoMismagius')):
        red @talking2mouth "That was a trainer's Pokémon. It Terastallized, {i}and{/i} my Poké Balls didn't lock onto it."
    else:
        red @talking2mouth "That was a trainer's Pokémon. It Terastallized."

    cheren @talking2mouth "I agree. Terastallization has a range of...?"

    red @talking2mouth "Twenty meters."

    cheren @closedbrow talking2mouth "It's blocked by metal and concrete, but not by glass or crystal. We are on the second floor, and there's clearly no-one floating outside the window."

    red @talking2mouth "Meaning that the trainer who Terastallized this Mismagius must be right here. I didn't see the Tera Orb, though, did you?"

    cheren @talking2mouth "I would have said if I did. I suspect--"

    show skyla angrybrow frownmouth with dis

    silver @surprisedbrow talking2mouth "Skyla? What do you see?"

    pause 2.0

    skyla @talking2mouth "...Hologram-emitting UFOs."

    silver @closedbrow sadmouth "Why the hell did I ask..."
    silver @surprised "Wait, you mean you {i}see{/i} them? Right now?"

    skyla angry "Evildoer, stop!"

    show skyla:
        xpos 0.2
        ease 0.3 xpos 0.1
        easein 0.2 xpos 0.7 ypos 0.8

    pause 0.3

    show cheren surprised:
        xpos 0.4
        ease 0.2 xpos -0.1 rotate -40 ypos 1.2

    show silver surprised:
        xpos 0.6
        ease 0.2 xpos 1.1 rotate 40 ypos 1.2

    show gardenia surprised:
        xpos 0.8 zoom 1.0 ypos 1.0
        ease 0.2 xpos 1.5 rotate 40 ypos 1.2

    pause 0.5

    show concerthallhallwaynight with hpunch

    $ PlaySound("thud.ogg")

    show skyla surprisedbrow frownmouth with dis

    redmind @surprisedbrow frownmouth "Wait. Did Skyla just... slam into the air?"

    show skyla winkbrow sweat sadmouth with dis:
        ypos 0.8 xpos 0.7
        linear 2.0 ypos 0.83

    skyla @talking2mouth "This UFO is... pretty slippery...!"

    show skyla surprised with dis:
        ypos 0.83 xpos 0.7
        linear 0.3 ypos 2.0 rotate 40

    pause 0.2

    show concerthallhallwaynight with vpunch

    skyla "Ack!"

    pause 2.0

    show ionojustteal surprised with gaussdissolve:
        xzoom -1 xpos 0.75 ypos 1.0
        parallel:
            ease 2.0 ypos 0.98
            linear 0.3 ypos 1.01
            ease 1.0 ypos 1.0
            ease 1.0 ypos 1.05
            repeat
        parallel:
            ease 2.0 xpos 0.75
            ease 2.0 xpos 0.77
            ease 2.0 xpos 0.75
            ease 2.0 xpos 0.73
            repeat
    
    Character("{color=#C9E4E4}???{/color}") "{glitch=5.00}\"Eep!\"{/glitch}"

    show ionojustteal angry with dis

    Character("{color=#C9E4E4}???{/color}") "{glitch=5.00}\"That bikini'd bimbo just cracked my lens. Hold on, why can't I fly out of\nthere...?\"{/glitch}"

    show skyla angry:
        ease 0.2 ypos 1.0 xpos 0.25 rotate 0

    show ionojustteal surprised with dis

    skyla "What did you call me, you rude alien?! This isn't a bikini, this is my battle body!"

    show silver sadbrow behind skyla:
        xzoom 1
        ease 0.7 xpos .15 ypos 1.0 rotate 0
    
    silver @sad "{size=30}Not denying the other thing, though...{/size}"

    Character("{color=#1d8fc5}???{/color}") "{glitch=5.00}\"Wait, they're responding? Why are they responding? They shouldn't be able to\nhear me!\"{/glitch}"

    show cheren behind skyla:
        ease 0.7 xpos .35 ypos 1.0 rotate 0

    cheren -surprised @talking2mouth "And yet, we can. Who are you?"

    Character("{color=#1d8fc5}???{/color}") "{glitch=5.00}\"...Why can they hear me? They can't hear me! I--\"{/glitch}"

    show ionojustteal with vpunch

    Character("{color=#1d8fc5}???{/color}") "{glitch=5.00}\"Oh,{/glitch} {glitch=200.00}shit{/glitch}, {glitch=5.00}I hit 'broadcast!'\"{/glitch}"
    Character("{color=#1d8fc5}???{/color}") "{glitch=5.00}\"{/glitch}{glitch=200.00}Shit, shit, shit{/glitch}, {glitch=5.00}this isn't supposed to happen... okay, I-Ball 2, get in there!\"{/glitch}"

    show ionojustteal angry with Dissolve(0.5)

    pause 0.01

    show ionojustpink neutral with gaussdissolve:
        xpos 0.85 ypos 1.0
        parallel:
            ease 1.0 ypos 1.0
            ease 1.0 ypos 1.05
            ease 1.0 ypos 1.0
            ease 1.0 ypos 0.95
            repeat
        parallel:
            ease 2.0 xpos 0.85
            ease 2.0 xpos 0.87
            ease 2.0 xpos 0.85
            ease 2.0 xpos 0.83
            repeat

    Character("{gradient=#EE8FB5-#1d8fc5}???{/gradient}") "{glitch=5.00}\"Alright, busters! You step away from the Mismagius, nice and easy--there's two of me, now, and you didn't want to mess with one of me!\"{/glitch}"

    redmind @thonk "The Mismagius? Oh, this must be the Mismagius' trainer... somehow."
    redmind @sweat closedbrow frownmouth "I'm not qualified to handle whatever the hell this is."

    show skyla angrybrow frownmouth
    show silver -sadbrow
    show ionojustteal surprised
    show ionojustpink impressed
    with dis

    cheren @talking2mouth "We have no intention of taking your Mismagius. If you wish, take it back."

    Character("{gradient=#EE8FB5-#1d8fc5}???{/gradient}") "{glitch=5.00}\"Oh. Really?\"{/glitch}"

    pause 2.0

    show ionojustteal closed
    show ionojustpink closed
    with dis
    
    $ PlaySound("pokemon/ball sound.ogg")

    show mismagius:
        xpos 0.5 ypos 1.5 zoom 1.0 matrixcolor IdentityMatrix()
        ease 2.0 xpos 0.75 ypos 0.4 zoom 0.0 matrixcolor BrightnessMatrix(1.0) * ContrastMatrix(0.0)
    
    Character("{gradient=#EE8FB5-#1d8fc5}???{/gradient}") "{glitch=5.00}\"Well, okay, then.\"{/glitch}"

    redmind @thinking "...The Mismagius went back to those things? What, are they giant Poké Balls?"
    redmind @thonk "They look like Magnemite, but I don't think they're {i}real{/i} Magnemite..."

    show ionojustteal neutral
    show ionojustpink neutral
    with dis

    pause 2.0

    show ionojustteal closed
    show ionojustpink closed
    with dis

    Character("{gradient=#EE8FB5-#1d8fc5}???{/gradient}") "{glitch=5.00}\"So...\"{/glitch}"

    pause 1.0

    show ionojustteal happy
    show ionojustpink happy
    show cheren surprisedbrow frownmouth
    show skyla surprisedbrow frownmouth
    show silver surprisedbrow frownmouth
    with dis

    Character("{gradient=#EE8FB5-#1d8fc5}???{/gradient}") "{glitch=5.00}\"Can you leave, now?\"{/glitch}"

    pause 2.0

    cheren @talking2mouth "N-{w=0.5} No."
    cheren @closedbrow sweat talking2mouth "Please excuse my manners. Who are you?"

    show ionojustteal happy
    show ionojustpink neutral
    with dis

    Character("{gradient=#EE8FB5-#1d8fc5}???{/gradient}") "{glitch=5.00}\"Oh, I'm a student here at Kobukan.\"{/glitch}"

    show ionojustteal neutral
    show ionojustpink neutral
    with dis

    Character("{gradient=#EE8FB5-#1d8fc5}???{/gradient}") "{glitch=5.00}\"Don't worry, I'm not like one of those bald beefcakes who broke in the barrier back in January. I'm a licensed, professional, full-time, registered, tuition-paying Kobukan student.\"{/glitch}"

    cheren @sad2brow tired talking2mouth "...So you're not a ghost."

    show ionojustteal happy
    show ionojustpink happy
    with dis

    Character("{gradient=#EE8FB5-#1d8fc5}???{/gradient}") "{glitch=5.00}\"Mortal as hell! Just a bit of a ghost in the machine, for fun.\"{/glitch}"

    show ionojustteal surprised
    show ionojustpink impressed
    with dis

    show gardenia angrybrow frownmouth:
        ease 0.5 ypos 1.0 xpos 0.5 xzoom -1 rotate 0 zoom 1.0

    gardenia @talking2mouth "I don't believe you!"

    pause 2.0

    show gardenia:
        ypos 1.0 xpos 0.5 xzoom -1 rotate 0 zoom 1.0

    show ionojustteal angry
    show ionojustpink closed
    with dis

    Character("{gradient=#EE8FB5-#1d8fc5}???{/gradient}") "{glitch=5.00}\"You... don't believe I'm not a ghost.\"{/glitch}"

    show cheren -surprisedbrow
    show skyla -frownmouth -surprisedbrow
    show silver -surprisedbrow
    with dis

    gardenia @talking2mouth "Yeah! What about the singing? The flickering lights? The Will-O-Wisps? The weird signals? And the other stuff?"

    pause 1.0
    
    Character("{gradient=#EE8FB5-#1d8fc5}???{/gradient}") "{glitch=5.00}\"...Um. I think the Will-O-Wisps are just these. My I-Balls.\"{/glitch}"

    gardenia @sadbrow talking2mouth "Eyeballs...?"

    Character("{gradient=#EE8FB5-#1d8fc5}???{/gradient}") "{glitch=5.00}\"No, I-Balls. Capital 'I' hyphen balls.\"{/glitch}"

    show ionojustteal happy
    show ionojustpink happy
    with dis
    
    Character("{gradient=#EE8FB5-#1d8fc5}???{/gradient}") "{glitch=5.00}\"They're a pair of genius drones that use electromagnetism and infinity energy to handle my meatspace stuff for me! They can carry Pokémon, Tera Orbs, small amounts of groceries, they have cameras built in, they--\"{/glitch}"

    red @confused "Meatspace?"

    show ionojustteal neutral
    show ionojustpink neutral
    with dis

    Character("{gradient=#EE8FB5-#1d8fc5}???{/gradient}") "{glitch=5.00}\"Internet joke. It means where {i}you{/i} people live.\"{/glitch}"

    show ionojustteal surprised
    show ionojustpink impressed
    with dis

    skyla @talking2mouth "Unova?"
    
    silver @talking2mouth sadbrow "Underground?"
    
    gardenia @talking2mouth sadbrow "A haunted mansion?"

    cheren @talking2mouth sad2brow "A constant state of denial?"

    show ionojustteal sad
    show ionojustpink sad
    with dis

    Character("{gradient=#EE8FB5-#1d8fc5}???{/gradient}") "{glitch=5.00}\"...You know, if you use my special code ZAPTHEBADFEELINGS03, you can get twenty percent off your first three months of an online therapy subscription.\"{/glitch}"
 
    show ionojustteal happy
    show ionojustpink happy
    with dis
 
    Character("{gradient=#EE8FB5-#1d8fc5}???{/gradient}") "{glitch=5.00}\"I've used them myself, they're great!\"{/glitch}"

    show ionojustteal neutral
    show ionojustpink neutral
    with dis

    gardenia @talking2mouth "We'll talk about that deal later, I'm interested. But who {i}are{/i} you?"

    show ionojustteal closed
    show ionojustpink closed
    with dis
 
    Character("{gradient=#EE8FB5-#1d8fc5}???{/gradient}") "{glitch=5.00}\"Like I said. A Kobukan student.\"{/glitch}"

    cheren @talking2mouth "You've provided no proof of this. Further, if you are a student, then you are..."
    cheren @upeyes angryeyebrows talking2mouth "{size=30}I can't believe I'm about to say this.{/size}"
    cheren @sad2brow talkingmouth "Then you are in violation of curfew. Unless you expect us to believe your dorm is somewhere in Pledge, Aura, or Relic Halls, but you've decided to 'haunt' the Contest Coliseum."
    
    show ionojustteal angry
    show ionojustpink angry
    with dis
 
    Character("{gradient=#EE8FB5-#1d8fc5}???{/gradient}") "{glitch=5.00}\"¿Qué? Che cosa? Nani? I'm in my dorm, here in the Contest Coliseum, friendo! I'm eating Chinese food right now. What is the charge? Eating a meal? A succulent Chinese meal?\"{/glitch}"
    
    cheren @angrybrow talking2mouth "There are no dorms in this building."

    show ionojustteal surprised
    show ionojustpink impressed
    with dis

    Character("{gradient=#EE8FB5-#1d8fc5}???{/gradient}") "{glitch=25.00}\"Bzzzt!\"{/glitch}"

    show ionojustteal closed
    show ionojustpink closed
    with dis

    Character("{gradient=#EE8FB5-#1d8fc5}???{/gradient}") "{glitch=5.00}\"Oh, I am sorry, ladies and gentlemens, but looks like Cheren missed that one! The correct answer was:\"{/glitch}"   
    
    show ionojustteal happy
    show ionojustpink happy
    with dis
    
    Character("{gradient=#EE8FB5-#1d8fc5}???{/gradient}") "{glitch=5.00}\"There is 'one' dorm in the Contest Coliseum, and it's mine, all mine! Mi casa, watashinoie, ko'u hale.\"{/glitch}"

    show ionojustteal surprised
    show ionojustpink impressed
    with dis

    cheren @talking2mouth closedbrow "May I assume, then, that if I were to go to the Student Council, they would corroborate your story, and {i}not{/i} say they have no idea who's flying drones around the Contest Coliseum?"

    show ionojustteal closed
    show ionojustpink closed
    with dis

    Character("{gradient=#EE8FB5-#1d8fc5}???{/gradient}") "{glitch=5.00}\"Ummm... they probably wouldn't know. But Dean Drayden does, and so does Nurse Miriam!\"{/glitch}"

    cheren @closedbrow talking2mouth "Hm."

    pause 1.0

    cheren @talking2mouth "I will verify this story."

    show ionojustteal angry
    show ionojustpink angry
    with dis

    Character("{gradient=#EE8FB5-#1d8fc5}???{/gradient}") "{glitch=5.00}\"F-fine! Do that! Good!\"{/glitch}"

    cheren @confusedbrow talking2mouth "Although... the speed at which I do so may change based on how you answer a couple of questions I would ask."

    pause 1.0

    show ionojustteal happy
    show ionojustpink happy
    with dis

    Character("{gradient=#EE8FB5-#1d8fc5}???{/gradient}") "{glitch=5.00}\"Ooooookay. Ask away, friendo, I'm an open book!\"{/glitch}"

    show ionojustteal neutral
    show ionojustpink neutral
    with dis

    cheren @talking2mouth "What is your name?"

    show ionojustteal surprised
    show ionojustpink impressed
    with dis

    pause 1.5

    Character("{gradient=#EE8FB5-#1d8fc5}???{/gradient}") "{glitch=5.00}\"Geezy louisey, you're really coming out fast with the hard-hittin' questions, aren't you? Like a bolt from the blue.\"{/glitch}"

    silver @angrybrow talking2mouth "Don't jerk us around, eyeballs."

    show ionojustteal angry
    show ionojustpink angry
    with dis

    Character("{gradient=#EE8FB5-#1d8fc5}???{/gradient}") "{glitch=5.00}\"Hey, it's I-Balls! With the hyphen! I can tell you weren't using the hyphen.\"{/glitch}"

    silver @angry "Whatever. Just answer the damn question!"

    gardenia @talking2mouth "Yeah! I'm onto you, Casper--I'm not buying that you're a Kobukan student, not for a second."

    cheren @angrybrow talking2mouth "Your name, {i}please{/i}."

    show ionojustteal sad
    show ionojustpink sad
    with dis

    Character("{gradient=#EE8FB5-#1d8fc5}???{/gradient}") "{glitch=5.00}\"...Look, I want to, but I don't know if I can trust you. I really wasn't meant to be found--no-one was even meant to know I was here.\"{/glitch}"
    
    show ionojustteal closed
    show ionojustpink closed
    with dis
    
    Character("{gradient=#EE8FB5-#1d8fc5}???{/gradient}") "{glitch=5.00}\"I thought if I hid in a part of the school where nobody goes, some place big and unfilled, that I could stay hidden all year... but then Calem got Lisia to join the Coordinator Club, and everyone became interested in contests.\"{/glitch}" 
    
    show ionojustteal angry
    show ionojustpink angry
    with dis

    Character("{gradient=#EE8FB5-#1d8fc5}???{/gradient}") "{glitch=5.00}\"This place has gotten way too busy!\"{/glitch}" 

    cheren @talking2mouth "Be that as it may, I need your name. If I am to ask Dean Drayden about the truth of your claim, I should at least be able to name the specific student I'm asking about."

    show ionojustteal sad
    show ionojustpink sad
    with dis

    Character("{gradient=#EE8FB5-#1d8fc5}???{/gradient}") "{glitch=5.00}\"I... Ummm...\"{/glitch}"

    pause 1.0

    skyla @talkingmouth "Hey, friendo."
   
    show ionojustteal surprised
    show ionojustpink impressed
    show cheren surprisedbrow
    show gardenia surprisedbrow
    show silver surprisedbrow
    with dis

    skyla @talkingmouth "Is there something we can do for you?"
    skyla @happy "If the issue's just that you can't trust us, then maybe we can earn your trust!"

    pause 1.5

    show gardenia -surprisedbrow
    show silver -surprisedbrow
    with dis

    cheren -surprisedbrow @talking2mouth "Oh. Um, well done, Skyla. That's a good idea."

    silver @sad "Why... why did none of us think of that?"

    skyla @talkingmouth "Don't feel bad, guys. With everyone yelling at us all the time, it can get hard for even {i}me{/i} to remember that we can still just offer to help people."

    cheren upeyes angryeyebrows @talking2mouth sad2brow "I'm... sorry. Neither of you deserve your association with me. If you wish, then..."

    silver @closedbrow talking2mouth "Oh, shut up."

    show cheren -upeyes -angryeyebrows with dis

    red @talkingmouth "So, eyeballs, {i}is{/i} there something we can do to earn your trust?"

    show ionojustteal neutral
    show ionojustpink neutral
    with dis

    Character("{gradient=#EE8FB5-#1d8fc5}???{/gradient}") "{glitch=5.00}\"Um... yeah, a little bit.\"{/glitch}"

    show ionojustteal sad
    show ionojustpink sad
    with dis

    Character("{gradient=#EE8FB5-#1d8fc5}???{/gradient}") "{glitch=5.00}\"My I-Balls are broken.\"{/glitch}"

    skyla @surprised "What? How do you look?"

    show ionojustteal happy
    show ionojustpink happy
    show skyla surprisedbrow frownmouth
    with dis

    Character("{gradient=#EE8FB5-#1d8fc5}???{/gradient}") "{glitch=5.00}\"Amazing! Nyohoho!\"{/glitch}"

    show ionojustteal closed
    show ionojustpink closed
    with dis

    Character("{gradient=#EE8FB5-#1d8fc5}???{/gradient}") "{glitch=5.00}\"But... it's actually a huge pain.\"{/glitch}"

    show ionojustteal angry
    show ionojustpink angry
    with dis

    Character("{gradient=#EE8FB5-#1d8fc5}???{/gradient}") "{glitch=5.00}\"I can only send out one Pokémon at a time, I-Ball 2 won't charge up to full, the hologram emitters are broken, the self-camo features are fritzing like a cat...\"{/glitch}"
    Character("{gradient=#EE8FB5-#1d8fc5}???{/gradient}") "{glitch=5.00}\"...and there's some jerky mcjerkface on campus with a roided-out Rotom who keeps jacking my signals, so even the stuff they can do, they sometimes forget!\"{/glitch}"
    Character("{gradient=#EE8FB5-#1d8fc5}???{/gradient}") "{glitch=5.00}\"Oh, and...\"{/glitch}"

    show cheren surprisedbrow
    show gardenia surprisedbrow
    show silver surprisedbrow
    show skyla surprisedbrow frownmouth
    with dis

    show concerthallhallwaynight with vpunch

    TempCharacter("{gradient=#EE8FB5-#1d8fc5}???{/gradient}", False) "{i}*BANG*{/i}"

    show concerthallhallwaynight with vpunch

    TempCharacter("{gradient=#EE8FB5-#1d8fc5}???{/gradient}", False) "{i}*BANG*{/i}"

    show concerthallhallwaynight with vpunch

    TempCharacter("{gradient=#EE8FB5-#1d8fc5}???{/gradient}", False) "{i}*BANG*{/i}"

    show ionojustteal closed
    show ionojustpink closed
    show cheren -surprisedbrow
    show gardenia -surprisedbrow
    show silver -surprisedbrow
    show skyla -surprisedbrow -frownmouth
    with dis

    Character("{gradient=#EE8FB5-#1d8fc5}???{/gradient}") "{glitch=5.00}\"Either I'm not hitting my keyboard hard enough, or the microphone's 'broadcast' function is stuck on 'on.'\"{/glitch}"

    gardenia @angrybrow talking2mouth "Alright, Beetlejuice. So what you're asking for is for us to bring you seven unholy sigils that will break the curse on your haunted prison, and leave you free to cause panic among the living, and kidnap innocent businessmen?"

    show ionojustteal closed
    show ionojustpink closed
    with dis

    Character("{gradient=#EE8FB5-#1d8fc5}???{/gradient}") "{glitch=5.00}\"Bzzzt. That's a nopesies, chat. Couldn't be more wrong if you tried.\"{/glitch}"
    
    show ionojustteal neutral
    show ionojustpink neutral
    with dis

    show gardenia surprisedbrow frownmouth with dis
    
    Character("{gradient=#EE8FB5-#1d8fc5}???{/gradient}") "{glitch=5.00}\"I just need some common parts. You can find them at any Radioshock store. They should be pretty much around any street corner.\"{/glitch}"

    pause 1.0

    show ionojustteal surprised
    show ionojustpink impressed
    with dis

    gardenia @sadbrow talking2mouth "Radioshock went out of business five years ago. They filed for Chapter 11 bankruptcy--everything left was absorbed into Silph Co."

    show ionojustteal closed
    show ionojustpink closed
    with dis

    Character("{gradient=#EE8FB5-#1d8fc5}???{/gradient}") "{glitch=5.00}\"...Well, it's been a bit since I've done my own hardware maintenance.\"{/glitch}"
    
    show ionojustteal neutral
    show ionojustpink neutral
    with dis

    gardenia @angrybrow talking2mouth "You know who else wouldn't know that a company went out of business years ago?"

    cheren @talking2mouth "I am begging you, do not say--"

    gardenia @angry "A ghost! Don't try to pull a fast one on me, Marley, I know only the undead could be so out-of-date when it comes to the state of the market!"

    show ionojustteal angry
    show ionojustpink angry
    with dis

    Character("{gradient=#EE8FB5-#1d8fc5}???{/gradient}") "{glitch=5.00}\"[ellipses]\"{/glitch}"

    show ionojustteal happy
    show ionojustpink happy
    with dis

    Character("{gradient=#EE8FB5-#1d8fc5}???{/gradient}") "{glitch=5.00}\"Nyohohoho! Looks like you found me out, Gardenia! I really am a ghost!\"{/glitch}"

    show gardenia surprisedbrow frownmouth with dis
    show ionojustteal angry
    show ionojustpink angry
    with dis

    Character("{gradient=#EE8FB5-#1d8fc5}???{/gradient}") "{glitch=5.00}\"Beware and behold my terrible power! With only a flick of my finger on this here keyboard-y, I will make a most monstrous sight manifest--a ghoul beyond grotesque, a spectre most spooky, a hag so haunting!\"{/glitch}"

    show gardenia:
        xpos 0.5
        ease 2.0 xpos 0.45

    gardenia sadbrow @talking2mouth "W-wait, hold on..."

    show ionojustteal happy
    show ionojustpink happy
    with dis

    Character("{gradient=#EE8FB5-#1d8fc5}???{/gradient}") "{glitch=5.00}\"Toooooooo late!~~~\"{/glitch}"

    show ionojustteal angry 
    show ionojustpink angry
    with dis

    show blank with transeye2fast

    Character("{gradient=#EE8FB5-#1d8fc5}???{/gradient}") "{size=60}{glitch=15.00}\"Boo!\"{/glitch}{/size}"

    show iono behind ionojustteal at Glitch(_fps=300., color_range1="FCC5E6", color_range2="BFF0F0", glitch_strength=0.02):#
        xpos 0.75 zoom 0.7 xzoom -1 xanchor 0.5

    hide blank with Dissolve(3.0)

    pause 3.0

    show ionojustteal surprised
    show ionojustpink impressed
    with dis

    Character("{gradient=#EE8FB5-#1d8fc5}???{/gradient}") "{glitch=5.00}\"...Whoops.\"{/glitch}"

    show ionojustteal neutral
    show ionojustpink neutral
    hide iono
    with dis
    
    Character("{gradient=#EE8FB5-#1d8fc5}???{/gradient}") "{glitch=5.00}\"Looks like my holograms are completely, totally, one-hundred-percentedly busted. Sorry for blinding you.\"{/glitch}"
    Character("{gradient=#EE8FB5-#1d8fc5}???{/gradient}") "{glitch=5.00}\"They haven't been working great for a while... best I could get out of them was a flicker of myself, and I kinda looked like La Llorona. Probably this big coat I wear.\"{/glitch}"

    silver @talking2mouth "The flickering, robed woman... hmph. So you're a girl."
    
    show ionojustteal angry 
    show ionojustpink angry
    with dis

    Character("{gradient=#EE8FB5-#1d8fc5}???{/gradient}") "{glitch=5.00}\"Hey, hey, hey! What do you mean by that? What's that 'hmphing' about, 'friendo?'\"{/glitch}"

    show gardenia angrybrow frownmouth
    show skyla angrybrow frownmouth
    with dis

    silver @sad "{size=30}{i}Definitely{/i} a girl. You're noisy enough for one.{/size}"

    gardenia @angrybrow talking2mouth "I'm going to pretend I didn't hear that."

    silver @closedbrow talking2mouth "Whatever."

    show gardenia -angrybrow -frownmouth
    show skyla sadbrow frownmouth
    with dis

    gardenia @angrybrow talking2mouth "Alright, Slimer, let's imagine you {i}aren't{/i} a ghost. Let's imagine you're actually a Kobukan student that somehow got permission to live in the Contest Coliseum."
    gardenia @talking2mouth "What would you need to repair your I-Balls? Mareep blood? Candles made of red wax? A handmade Galarica wreath of genuine Galarian holly, acquired at a decent price from my market?"

    show ionojustteal neutral
    show ionojustpink neutral
    with dis

    Character("{gradient=#EE8FB5-#1d8fc5}???{/gradient}") "{glitch=5.00}\"Nothing like that. Although that gives me an idea for later[ellipses]\"{/glitch}"
    Character("{gradient=#EE8FB5-#1d8fc5}???{/gradient}") "{glitch=5.00}\"If Radioshock doesn't exist anymore, then it might be trickier to find these, but I need a shed Varoom Chassis, a lode of Tinkatitanium, a Magnet, an Ultra Ball, and a bottle of some kind of fizzy energy drink.\"{/glitch}"
    Character("{gradient=#EE8FB5-#1d8fc5}???{/gradient}") "{glitch=5.00}\"I'll also need a low-altitude hover engine, 200D Grade.\"{/glitch}"
    
    show ionojustteal angry
    show ionojustpink angry
    show skyla angrybrow frownmouth
    with dis
    
    Character("{gradient=#EE8FB5-#1d8fc5}???{/gradient}") "{glitch=5.00}\"Oh, and a pair of regular glasses to fix the lens that supertits broke.\"{/glitch}"

    skyla @talking2mouth "I do {i}not{/i} like you."

    show ionojustteal closed
    show ionojustpink closed
    with dis
    
    Character("{gradient=#EE8FB5-#1d8fc5}???{/gradient}") "{glitch=5.00}\"Join the hate club.\"{/glitch}"

    show ionojustteal neutral
    show ionojustpink neutral
    with dis
    
    Character("{gradient=#EE8FB5-#1d8fc5}???{/gradient}") "{glitch=5.00}\"They send out bi-monthly bulletins. I've read some of them. Their articles are actually pre-e-e-e-tty interesting.\"{/glitch}"

    show ionojustteal surprised
    show ionojustpink impressed
    show skyla surprisedbrow frownmouth
    with dis

    cheren @talking2mouth "Kindly refrain from insulting members of the Disciplinary Committee."

    show skyla sadbrow -frownmouth
    with dis

    cheren @angrybrow talking2mouth "Skyla is just as valuable and appreciated a member of the Disciplinary Committee as any one of us. Further, she is the one who offered to help you. To repay her kindness with casual insults seems ungrateful."

    pause 1.0

    show ionojustteal closed
    show ionojustpink closed
    with dis

    Character("{gradient=#EE8FB5-#1d8fc5}???{/gradient}") "{glitch=5.00}\"[ellipses]Sorry.\"{/glitch}"

    show ionojustteal neutral
    show ionojustpink neutral
    with dis

    skyla -sadbrow @closedbrow talkingmouth "No harm done, I-Balls."

    silver @talking2mouth "About the shed Varoom chassis... I'm pretty sure I can get one. There's always a bunch lying around outside my..." 
    silver @sadbrow talking2mouth "Uh, my dorm."

    cheren @talking2mouth "I could order another pair of glasses. I have a pair--it should not be difficult to order another pair of the same make from my optometrist."

    skyla @talking2mouth "I know where to get a 200D from. There's a junker who sells me aviation parts sometimes. He's kinda pricey, though..."

    gardenia @talkingmouth "Don't worry about that, I'll cover the cost for a big thing like that. The other three things seems to be pretty small, though."
    gardenia @talking2mouth "I'm pretty sure there's a club somewhere in the school that makes and sells food. You can probably buy the energy drink from there."

    if (GetItemCount("Energy Drink") > 0):
        red @talkingmouth "I've got one on me, actually."

        gardenia @talkingmouth "Nice! Prepared, aren't you?"

    elif (GetRelationshipRank("May") > 1):
        $ AddEvent("May", "AskEnergyDrink")
        redmind @thinking "Hm... if I say it's for a good cause, I bet May can get me one. Maybe even at a discount..."

    gardenia @talking2mouth "Besides that, I know Lt. Surge teaches his students how to handmake magnets. If you don't attend his class, maybe you can buy one off of another student who {i}does{/i} attend his class?"

    if (GetItemCount("Magnet") > 0):
        red @talkingmouth "Just a regular U-shaped Magnet? Sure, I've got a spare one."

        skyla @happy "Nice! That's another gadget on our utility belt we don't have to go out searching for, then."

    gardenia @sad "Oh, but I don't have any idea where you could find Tinkatitanium."

    cheren @talking2mouth "Hm... Tinkatitanium is the metal that Tinkatink and its evolutionary family use for their hammers, yes?"

    show ionojustteal sad
    show ionojustpink sad
    with dis

    Character("{gradient=#EE8FB5-#1d8fc5}???{/gradient}") "{glitch=5.00}\"Yep-ep! It starts out as plain ol' iron, but as they use their hammers, it condenses and hardens, becoming incredibly durable.\"{/glitch}"

    show ionojustteal neutral
    show ionojustpink neutral
    with dis

    cheren @upeyes confusedeyebrows talking2mouth "Hm... I suppose we could simply purchase some online...?"

    silver @surprisedbrow talking2mouth "On our budget?"

    cheren @talking2mouth "Perhaps not. Gardenia, would you be willing to open your wallet again?"

    gardenia @sadbrow talking2mouth "I... would prefer {i}not{/i} to..."

    show ionojustteal happy
    show ionojustpink happy
    with dis

    Character("{gradient=#EE8FB5-#1d8fc5}???{/gradient}") "{glitch=5.00}\"Don't worry about it! There's actually a few Tinkatink, and even a couple Tinkatuff, right here!\"{/glitch}"

    show ionojustteal neutral
    show ionojustpink neutral
    with dis

    cheren @confusedeyebrows talking2mouth "Right here? Gardenia, do you have any idea what that means?"

    gardenia @sadbrow talking2mouth "...I do, but I don't like it."

    skyla @talkingmouth "What is it, Gardenia?"

    gardenia @sadbrow talking2mouth "This school's supposed to have a series of tunnels underneath it. Long, dark, tunnels where ghosts live."

    cheren @talking2mouth "Obviously an urban myth. But why would this help us fix our Tinkatitanium problem?"

    gardenia @talking2mouth "The Kobukan tunnels are said to have Tinkatink living in them by the hundreds. You know those banging sounds you sometimes hear at night? Those are Tinkatink under the school."
    
    show skyla surprisedbrow frownmouth
    show cheren surprisedbrow frownmouth
    show silver surprisedbrow frownmouth
    show ionojustteal surprised
    show ionojustpink impressed
    with dis

    gardenia @sadbrow talking2mouth "But... there's also meant to be hundreds of ghosts down there." 
    gardenia angrybrow @angry "Those creepy ghosts are trying to suck up all the life essence from Kobukan students! Then they'll reveal themselves, burst out from underground, and try to take over the school!"

    pause 2.0

    show gardenia sadbrow frownmouth with dis

    cheren @confusedbrow talking2mouth "Gardenia, what do you have against ghosts?"

    gardenia @talking2mouth "You wouldn't understand."

    pause 1.0

    show skyla -surprisedbrow frownmouth
    show cheren -surprisedbrow frownmouth
    show silver -surprisedbrow frownmouth
    show ionojustteal neutral
    show ionojustpink neutral
    with dis

    gardenia -sadbrow @talking2mouth "Anyway, I'm not paying you to understand. We just need to find these tunnels, grab the Tinkatitanium, and bring it back to Bloody Mary here. Two Pidgey, one Smack Down." 

    cheren @talking2mouth "Yes, an easy task, save for the fact these tunnels are entirely fictitious."

    show ionojustteal happy
    show ionojustpink happy
    with dis

    Character("{gradient=#EE8FB5-#1d8fc5}???{/gradient}") "{glitch=5.00}\"Bzzzt! Wrong answer. The tunnels are, actually, real, friendo!\"{/glitch}"

    gardenia @angry "{size=30}Of course the ghost would know that.{/size}"

    show ionojustteal neutral
    show ionojustpink neutral
    with dis

    Character("{gradient=#EE8FB5-#1d8fc5}???{/gradient}") "{glitch=5.00}\"In fact, one of the entrances is right here, in the Contest Coliseum. It's just behind the backstage, behind a fake brick wall.\"{/glitch}"
    
    cheren @talking2mouth "That beggars belief."

    silver @talking2mouth "...She's right. Remember when the school was attacked earlier this year?"

    cheren @closedbrow talking2mouth "Of course. You know I do."

    silver @sad "Yeah, some of those guys... came up through the tunnels. They link into Inspira's sewer system."

    show gardenia sadbrow with dis

    cheren @closedbrow talking2mouth "Delightful. I hope no-one here is squeamish, then."

    pause 2.0

    gardenia -sadbrow @happy "I'm paying you for a reason."

    cheren @talking2mouth "Just the three of us, then, I suppose."

    menu:
        "You mean the four of us.":
            $ AddEvent("Cheren", "JoinCatacombs")
            show cheren surprisedbrow frownmouth with dis

            $ ValueChange("Silver", 2, 0.15, False)
            $ ValueChange("Skyla", 2, 0.25, False)
            $ ValueChange("Cheren", 2, 0.35, False)
            $ ValueChange("Gardenia", 2, 0.45, True)

            cheren -surprisedbrow @sad2brow talking2mouth "I... don't understand. If you despise me so much, why do you continually insist on joining our efforts?"

            red @unamusedbrow talking2mouth "I'm only here because you failed to blackmail me into joining you in the first place. I could ask you the exact same thing."

            cheren @angrybrow talking2mouth "And I could ask {i}you{/i}--"

            silver @angry "[ellipses]Grrrrr[ellipses]"

            pause 1.5

            redmind @surprisedbrow frownmouth "Did Silver just {i}growl{/i}?"
            redmind @sad2eyes sadeyebrows frownmouth "Well, it definitely lowered my attack..."

            cheren @talking2mouth "Right. Well, if you insist on joining, I am, as always, powerless to stop you."

            show ionojustteal happy
            show ionojustpink happy
            with dis

            Character("{gradient=#EE8FB5-#1d8fc5}???{/gradient}") "{glitch=5.00}\"Good luck!\"{/glitch}"

            show ionojustteal neutral
            show ionojustpink neutral
            with dis

        "Good luck.":
            pass

    cheren @talking2mouth "I'm sure we'll need it."

    cheren @sad2brow talking2mouth "[ellipses]It's getting late. We should head back to the main body of campus soon. We need to get our own sleep before classes begin... hand the patrolling of curfew over to security, for what good they are."
    cheren @talking2mouth confusedbrow "I don't suppose security has any idea you're here?"

    show ionojustteal closed
    show ionojustpink closed
    with dis

    Character("{gradient=#EE8FB5-#1d8fc5}???{/gradient}") "{glitch=5.00}\"Less than a clue.\"{/glitch}"

    show ionojustteal neutral
    show ionojustpink neutral
    with dis

    cheren @talkingmouth sad2brow "Of course. Why should I be surprised?"
    cheren @talking2mouth "When we are all available, let us meet up at the Battle Hall, as it's the closest building to the Contest Coliseum on the main campus."
    cheren @talking2mouth "We should gather all the other materials, first, then descend into the tunnels. Hopefully, we can emerge from them unscathed and go directly to you... Ms...?"

    show ionojustteal closed
    show ionojustpink closed
    with dis

    Character("{gradient=#EE8FB5-#1d8fc5}???{/gradient}") "{glitch=5.00}\"Iunno, call me whatever you want.\"{/glitch}"

    show ionojustteal surprised
    show ionojustpink impressed
    with dis

    cheren @talkingmouth sad2brow "Iono it is, then."

    Character("{gradient=#EE8FB5-#1d8fc5}???{/gradient}") "{glitch=5.00}\"[ellipses]\"{/glitch}"
    Character("{gradient=#EE8FB5-#1d8fc5}???{/gradient}") "{glitch=5.00}\"¿Qué?\"{/glitch}"

    cheren @closedbrow talking2mouth "Apologies, it was simple wordplay. You said 'Iunno', so I thought it would be amusing to literally take that as your name."

    Character("{gradient=#EE8FB5-#1d8fc5}???{/gradient}") "{glitch=5.00}\"Oh.\"{/glitch}"

    pause 1.5

    show ionojustteal happy
    show ionojustpink happy
    with dis

    Character("{gradient=#EE8FB5-#1d8fc5}I-Balls{/gradient}") "{glitch=5.00}\"Nyohohoho! That's a good one! But, actually, how about you just call me I-Balls? At least for now.\"{/glitch}"

    show ionojustteal neutral
    show ionojustpink neutral
    with dis

    cheren @talking2mouth "Very well."
    cheren @talking2mouth "Remember, we need the shed varoom chassis, the glasses, the engine, [bluecolor]the magnet, the energy drink, and an Ultra Ball{/color}."

    pause 1.0

    cheren @talkingmouth "Skyla, would you like me to write that down?"

    skyla @sadbrow talkingmouth "Please."

    cheren @talking2mouth "Alright. I've made some notes already--I'll just make some quick copies."

    show screen book_mixed_text(ghostjournal) with Dissolve(2.0)

    $ GetItem("Ghost Journal", text="You gained the ghost journal! If you're ever having difficulty remembering what your next step is in uncovering this mystery, just consult the Ghost Journal!")

    red @talking2mouth "Alright. We'll meet up at the Battle Hall, you said, right?"

    cheren @talking2mouth "At your leisure."

    Character("{gradient=#EE8FB5-#1d8fc5}I-Balls{/gradient}") "{glitch=5.00}\"Thanks, guys... I really appreciate you helping me with this. Trust me, I'll make it worth your while!\"{/glitch}"
    
    show silver sadbrow 
    show skyla happybrow sweat
    with dis

    gardenia @angrybrow talking2mouth "Oh, you will. Because if you're not a ghost, you're helping us find the {i}real{/i} ghosts."

    cheren @tired talkingmouth sad2eyes "That's definitely a sign that we've all been up too late." 
    cheren @talking2mouth "Goodnight, everyone. Good luck."

    scene blank2 with splitfade

    python:
        AddEvent("Cheren", "Scene2")
        persondex["Cheren"]["RelationshipRank"] = 2

    return

label Cheren2Part2:
    $ AddEvent("Cheren", "Cheren2Part2")
    narrator "You remember that I-Balls wanted an Energy Drink, a Magnet, an Ultra Ball, and a lode of Tinkatitanium."

    python:
        missing_items = []
        if Item.EnergyDrink not in inventory:
            missing_items.append("an Energy Drink")
        if Item.Magnet not in inventory:
            missing_items.append("a Magnet")
        if Item.UltraBall not in inventory:
            missing_items.append("an Ultra Ball")
        if HasEvent("Professor Oak", "ClearedCatacombs") and not HasEvent("Cheren", "JoinCatacombs"):
            missing_items.append("any Tinkatitanium")

    if missing_items:
        $ formatted_missing = ", ".join(missing_items[:-1]) + (" and " + missing_items[-1] if len(missing_items) > 1 else missing_items[0])
        narrator "You currently do not have [formatted_missing]. Are you sure you want to talk to I-Balls now?"

        menu:
            "Yep.":
                pass

            "On second thought...":
                if sceneviewer:
                    return

                $ renpy.pop_call()
                $ RemoveEvent("Cheren", "Cheren2Part2")
                jump freeroam

    stop music fadeout 1.5
    show screen songsplash("Embracing One's Duty", "Zame")
    queue music "audio/music/embracingonesduty.ogg"
    show concerthallhallway with splitfade

    show cheren og:
        xpos 0.2
    show silver:
        xpos 0.8 xzoom -1
    show skyla behind silver:
        xpos 0.6 xzoom -1
    show gardenia behind cheren:
        xpos 0.4

    gardenia @talkingmouth "Alright... we're all here, right?"

    skyla @talkingmouth "Yep! Disciplinary committee, check. [first_name], check. You, check."

    silver @talking2mouth "Guess the only one we're missing is I-Balls, then."

    pause 1.0

    cheren @confusedeyebrows talking2mouth "I don't suppose anyone has a phone number?"

    gardenia @angrybrow talking2mouth "A Ouija board would probably be more useful."

    cheren @upeyes talking2mouth "We've been over this. I-Balls is not a ghost."

    silver @talking2mouth "Yeah. That tunnel underneath the school is full of them, but I-Balls? She's just some weirdo with a couple of drones and a remote control."

    gardenia @talkingmouth "We'll see."

    pause 1.0

    gardenia @sadbrow talkingmouth "U-u-um... I-Balls...?"

    pause 2.0

    red @sadbrow talkingmouth "I mean, we could yell, right?"

    skyla angrybrow frownmouth @happy "Oh, let me! I'm great at shouting!"

    silver @talking2mouth "She's not kidding. She doesn't even need a radio in her plane. Just empties her lungs out and shrieks at ground control."

    pause 1.0

    show cheren sad2brow with dis

    pause 1.0

    cheren @talkingmouth "Silver."

    silver @talking2mouth "Huh?"

    show skyla sadbrow -frownmouth with dis

    cheren @closedbrow talking2mouth "I've stopped picking fights with [first_name]. I'd ask that you return the favor and stop picking fights with Skyla."

    silver @closedbrow talking2mouth "...You picked us out {i}because{/i} we didn't get along."

    cheren @closedbrow talking2mouth "I picked you out because I can tell that you have a kind heart that genuinely wants to protect people."
    cheren @talking2mouth "Protect them from me, from the consequences of my stupid, {i}stupid{/i}, actions. But I really don't think there's any call to protect them from Skyla, is there?"

    silver @sadbrow talking2mouth "...Ugh."

    pause 1.0

    show skyla surprisedbrow frownmouth:
        xpos 0.6 xzoom -1
        ease 0.5 xpos 0.8

    show silver surprisedbrow frownmouth:
        xpos 0.8 xzoom -1
        ease 0.5 xpos 0.9
    
    show gardenia surprisedbrow frownmouth behind skyla:
        xpos 0.4
        ease 0.5 xpos 0.7

    show cheren surprisedbrow frownmouth behind gardenia:
        xpos 0.2 xzoom 1
        ease 0.5 xpos 0.6 xzoom -1

    show ionojustteal happy:
        xpos -0.2 ypos 1.0 xzoom -1
        ease 0.5 xpos 0.25 ypos 1.05
        parallel:
            ease 1.0 ypos 1.0
            ease 1.0 ypos 1.05
            ease 1.0 ypos 1.0
            ease 1.0 ypos 0.95
            repeat
        parallel:
            ease 2.0 xpos 0.25
            ease 2.0 xpos 0.27
            ease 2.0 xpos 0.25
            ease 2.0 xpos 0.23
            repeat
    show ionojustpink happy:
        xpos -0.2 ypos 1.0 xzoom -1
        ease 0.5 xpos 0.25 ypos 1.05
        parallel:
            ease 1.0 ypos 1.0
            ease 1.0 ypos 1.05
            ease 1.0 ypos 1.0
            ease 1.0 ypos 0.95
            repeat
        parallel:
            ease 2.0 xpos 0.25
            ease 2.0 xpos 0.27
            ease 2.0 xpos 0.25
            ease 2.0 xpos 0.23
            repeat
    
    Character("{gradient=#EE8FB5-#1d8fc5}I-Balls{/gradient}") "{glitch=5.00}\"Wowowowow. You guys are a capital 'M' {i}mess{/i}.\"{/glitch}"

    show ionojustteal neutral
    show ionojustpink neutral
    with dis

    gardenia @surprised "Ah!"

    show skyla -surprisedbrow -frownmouth:
        xpos 0.8 xzoom -1

    show silver -surprisedbrow frownmouth:
        xpos 0.9 xzoom -1
    
    show gardenia -surprisedbrow frownmouth behind skyla:
        xpos 0.7

    show cheren -surprisedbrow smilemouth behind gardenia:
        xpos 0.6 xzoom -1

    cheren @talking2mouth "I-Balls. We've obtained what you wanted."

    show ionojustteal surprised
    show ionojustpink impressed
    with dis

    Character("{gradient=#EE8FB5-#1d8fc5}I-Balls{/gradient}") "{glitch=5.00}\"For realsies?! That's totally rad!\"{/glitch}"

    show ionojustteal happy
    show ionojustpink happy
    with dis

    Character("{gradient=#EE8FB5-#1d8fc5}I-Balls{/gradient}") "{glitch=5.00}\"C'mon, c'mon, c'mon! Fork it over!\"{/glitch}"

    cheren @confusedeyebrows talking2mouth "Certainly, but... how? You don't appear to have hands."

    show ionojustteal neutral
    show ionojustpink neutral
    with dis

    Character("{gradient=#EE8FB5-#1d8fc5}I-Balls{/gradient}") "{glitch=5.00}\"It's okie-dokey. My I-Balls can carry Poké Balls in them, and my Pokémon can bring the materials to me.\"{/glitch}"

    cheren @talking2mouth "Or we could save some unnecessary effort, and just deliver them to you directly, no?"

    pause 0.5

    Character("{gradient=#EE8FB5-#1d8fc5}I-Balls{/gradient}") "{glitch=5.00}\"...\"{/glitch}"

    show gardenia angrybrow frownmouth with dis

    Character("{gradient=#EE8FB5-#1d8fc5}I-Balls{/gradient}") "{glitch=5.00}\"Nnnno. No, let's do the thing I said.\"{/glitch}"

    cheren @talking2mouth sweat closedbrow "Fine. Let's put everything in a pile here."

    narrator "Silver puts a shed Varoom chassis, Skyla puts a Hover Engine, and Cheren puts a pair of glasses in the pile."

    Character("{gradient=#EE8FB5-#1d8fc5}I-Balls{/gradient}") "{glitch=5.00}\"Great, great! And what about the Ultra Ball?\"{/glitch}"

    $ ionogiftsgiven = 0

    if (Item.UltraBall in inventory):
        menu:
            ">Give I-Balls one Ultra Ball":
                if (LoseItem(Item.UltraBall)):
                    $ AddEvent("Iono", "GaveUltraBall")
                    $ ionogiftsgiven += 1
                    red @talkingmouth "Here you go."

                    show ionojustteal happy
                    show ionojustpink happy
                    with dis

                    if (GetRelationshipRank("Silver") > 1):
                        show silver angrybrow frownmouth with dis

                    Character("{gradient=#EE8FB5-#1d8fc5}I-Balls{/gradient}") "{glitch=5.00}\"Oh, you got me something, too? I thought you were here just to stand around and look pretty!\"{/glitch}"

                    red @happy "Hey, I can multitask."

                    show silver -angrybrow with dis
                else:
                    jump noultraballforiono

            ">Keep it.":
                jump noultraballforiono

    else:
        label noultraballforiono:

        gardenia @talking2mouth "I've got one. I was planning on reselling this bundle later, but... I have eleven, and people never want to buy more than ten at a time."

        silver @closedbrow talking2mouth "Those free Premier Balls make all the difference, sometimes. If you're watching your wallet, you gotta make every coin count."

        redmind @thinking sweat "True."

    Character("{gradient=#EE8FB5-#1d8fc5}I-Balls{/gradient}") "{glitch=5.00}\"Cool, cool, cool! What about the Magnet?\"{/glitch}"

    if (Item.Magnet in inventory):
        menu:
            ">Give I-Balls one Magnet":
                if (LoseItem(Item.Magnet)):
                    $ AddEvent("Iono", "GaveMagnet")
                    $ ionogiftsgiven += 1
                    red @talkingmouth "Here you go."

                    if (ionogiftsgiven == 0):
                        show ionojustteal happy
                        show ionojustpink happy
                        with dis

                        if (GetRelationshipRank("Silver") > 1):
                            show silver angrybrow frownmouth with dis

                        Character("{gradient=#EE8FB5-#1d8fc5}I-Balls{/gradient}") "{glitch=5.00}\"Oh, you got me something, too? I thought you were here just to stand around and look pretty!\"{/glitch}"

                        show silver -angrybrow with dis

                    else:
                        show ionojustteal surprised
                        show ionojustpink impressed
                        with dis

                        Character("{gradient=#EE8FB5-#1d8fc5}I-Balls{/gradient}") "{glitch=5.00}\"Woah-woah-woah! You got me two things?! Everyone else only got me one! You going for a new high score?\"{/glitch}"

                        skyla @sadbrow talkingmouth "Wait, this was a competition? I would have gotten you more stuff if I knew there were scores involved!"

                        red @sadbrow talkingmouth "{i}Pretty{/i} sure she's joking."

                else:
                    jump nomagnetforiono

            ">Keep it.":
                jump nomagnetforiono

    else:
        label nomagnetforiono:

        skyla @talking2mouth "I've got one. When I was buying this engine from the Inspira junker, he also had some magnets lying around. I figured I should grab one, just in case."

        cheren @talkingmouth "Good thinking, Skyla."

    show ionojustteal happy
    show ionojustpink happy
    with dis

    Character("{gradient=#EE8FB5-#1d8fc5}I-Balls{/gradient}") "{glitch=5.00}\"Rad, radder, raddest! Okay, what about the energy drink?\"{/glitch}"

    if (Item.EnergyDrink in inventory):
        menu:
            ">Give I-Balls one Energy Drink":
                if (LoseItem(Item.EnergyDrink)):
                    $ AddEvent("Iono", "GaveEnergyDrink")
                    $ ionogiftsgiven += 1
                    red @talkingmouth "Here you go."

                    if (ionogiftsgiven == 0):
                        show ionojustteal happy
                        show ionojustpink happy
                        with dis

                        if (GetRelationshipRank("Silver") > 1):
                            show silver angrybrow frownmouth with dis

                        Character("{gradient=#EE8FB5-#1d8fc5}I-Balls{/gradient}") "{glitch=5.00}\"Oh, you got me something, too? I thought you were here just to stand around and look pretty!\"{/glitch}"

                        show silver -angrybrow with dis

                    elif (ionogiftsgiven == 1):
                        show ionojustteal surprised
                        show ionojustpink impressed
                        with dis

                        Character("{gradient=#EE8FB5-#1d8fc5}I-Balls{/gradient}") "{glitch=5.00}\"Woah-woah-woah! You got me two things?! Everyone else only got me one! You going for a new high score?\"{/glitch}"

                        skyla @sadbrow talkingmouth "Wait, this was a competition? I would have gotten you more stuff if I knew there were scores involved!"

                        red @sadbrow talkingmouth "{i}Pretty{/i} sure she's joking."

                    else:
                        show ionojustteal surprised
                        show ionojustpink impressed
                        with dis

                        Character("{gradient=#EE8FB5-#1d8fc5}I-Balls{/gradient}") "{glitch=5.00}\"Hold up! Did you get me all three things I asked for? What are you, like, the king of fetch quests?!\"{/glitch}"
                        Character("{gradient=#EE8FB5-#1d8fc5}I-Balls{/gradient}") "{glitch=5.00}\"I should've guessed you'd pull through! You've got massive protag energy. I bet your backpack was already full of half of the stuff I asked for!\"{/glitch}"

                        red @sad2eyes sadeyebrows talkingmouth "I take the sixth."

                        skyla @happy sweat "It's 'take the fifth,' and you can't do that, you're Kantonian."

                        red @talking2mouth closedbrow sweat "Damn."

                        show ionojustteal happy
                        show ionojustpink happy
                        with dis

                        Character("{gradient=#EE8FB5-#1d8fc5}I-Balls{/gradient}") "{glitch=5.00}\"For realsies, though, thank you {i}so{/i} much! This is great!\"{/glitch}"

                        red @sadbrow talkingmouth "Happy to help. It really wasn't much of a problem."

                else:
                    jump noenergydrinkforiono

            ">Keep it.":
                jump noenergydrinkforiono

    else:
        label noenergydrinkforiono:

        silver @closedbrow talking2mouth "Ugh... I've got one, I guess."

        skyla @talking2mouth "Hm? You sound embarrassed."

        if (HasEvent("Silver", "Overthrown")):
            silver @closedbrow talking2mouth "It's just cheap sugar water. I shouldn't drink that crap."

        else:
            silver @closedbrow talking2mouth "It's just cheap sugar water. I shouldn't drink that crap. I just carry a couple around in case my dormmates have an argument at night and I need to break it up. Can't look tired..."

            gardenia @sadbrow talkingmouth "It sounds like you're the only thing keeping your dorm running!"

            silver @closedbrow talking2mouth "You have no idea."

        cheren @talkingmouth "Whatever the case, thank you, Silver."

    show ionojustteal happy
    show ionojustpink happy
    with dis

    Character("{gradient=#EE8FB5-#1d8fc5}I-Balls{/gradient}") "{glitch=5.00}\"Okie-dokey! That leaves only one thing. The big lode of Tinkatitanium.\"{/glitch}"

    if (HasEvent("Professor Oak", "ClearedCatacombs")):
        narrator "You drop the piles of smashed, hammered, busted metal into the pile of junk in front of the group."

    else:
        narrator "Cheren wordlessly drops a pile of smashed, hammered, busted metal into the pile of junk in front of the group."

    show ionojustteal angry
    show ionojustpink angry
    show skyla surprisedbrow frownmouth
    show silver surprisedbrow frownmouth
    show gardenia surprisedbrow frownmouth
    show cheren surprisedbrow frownmouth 
    with vpunch 

    Character("{gradient=#EE8FB5-#1d8fc5}I-Balls{/gradient}") "{glitch=15.00}\"WHAAAAT?! My-- my--!\"{/glitch}"
    Character("{gradient=#EE8FB5-#1d8fc5}I-Balls{/gradient}") "{glitch=5.00}\"That pink {i}puta{/i}! That little{/glitch} {glitch=200.00}shit{/glitch}{glitch=5.00}! She smashed up my I-Balls! These are--were--precision\nelectronics! Does that{/glitch} {glitch=200.00}terrorist{/glitch} {glitch=5.0}have any idea how much time and money it'll take to fix\nthese?!\"{/glitch}"

    show gardenia -surprisedbrow 
    show skyla -surprisedbrow -frownmouth
    show silver -surprisedbrow -frownmouth 
    with dis

    cheren -surprisedbrow @sadbrow talkingmouth "At the risk of sounding unsympathetic, surely you must have known what was happening to your drones when they kept disappearing?"

    Character("{gradient=#EE8FB5-#1d8fc5}I-Balls{/gradient}") "{glitch=5.00}\"I had my theories, but you try figuring out exactly what's happening when someone Fastball Specials a rock into the back of your head every time you try to do a grocery run!\"{/glitch}"

    cheren @closedbrow talking2mouth "I can imagine that's very difficult."

    Character("{gradient=#EE8FB5-#1d8fc5}I-Balls{/gradient}") "{glitch=5.00}\"When I asked you to get the Tinkatitanium, I kinda just expected you to steal that Tinkaton Tinkaterrorist's hammer...\"{/glitch}"

    silver -surprisedbrow @talking2mouth "We're not doin' that. Smacking big metal things out of the sky is just what they do. Can't blame them for nature."

    Character("{gradient=#EE8FB5-#1d8fc5}I-Balls{/gradient}") "{glitch=5.00}\"I {i}can{/i} and I {i}will!{/i}\"{/glitch}"

    skyla @talking2mouth "We didn't actually see any Tinkaton down in the tunnels... though there were a few Tinkatink and Tinkatuff. Maybe the Tinkaton's left...?"

    cheren @talking2mouth "Unlikely. Though if it's older and stronger than the others, perhaps it's more intelligent, too, and didn't want to be captured."

    show ionojustteal neutral
    show ionojustpink neutral
    with dis

    gardenia surprisedbrow frownmouth @neutralbrow talking2mouth "You know... Tinkatitanium goes for a pretty penny. If you sell these lumps, you can probably recoup the cost of repairs for your I-Balls."

    Character("{gradient=#EE8FB5-#1d8fc5}I-Balls{/gradient}") "{glitch=5.00}\"Really? Maybe I'll do that, then. Oh, and you're entitled to a portion of the revenue I got from this, since you helped me out by telling me!\"{/glitch}"

    pause 1.0

    gardenia @talking2mouth sad2brow blush "Okay, so I-Balls {i}isn't{/i} a ghost, but there's definitely {i}other{/i} ghosts out there."

    cheren @closedbrow talkingmouth "As long as you keep paying us to find them, there certainly will be."

    show ionojustteal happy
    show ionojustpink happy
    with dis

    Character("{gradient=#EE8FB5-#1d8fc5}I-Balls{/gradient}") "{glitch=5.00}\"Alright. Friendos, stand behind the yellow line. I'll get my Pokémon to bring this stuff to me in a jiffy!\"{/glitch}"

    show ionojustteal neutral
    show ionojustpink neutral
    with dis

    pause 1.5

    red @thonk "[ellipses]"

    skyla @talkingmouth "How long's a jiffy?"

    show ionojustteal angry
    show ionojustpink angry
    with dis

    pause 1.5

    Character("{gradient=#EE8FB5-#1d8fc5}I-Balls{/gradient}") "{glitch=5.00}\"Piece of junk... {i}dios mio{/i}, my body's falling apart.\"{/glitch}"

    show ionojustteal sad
    show ionojustpink sad
    with dis

    Character("{gradient=#EE8FB5-#1d8fc5}I-Balls{/gradient}") "{glitch=5.00}\"Okay, change of plans. As thanks for bringing me these gifts of the magi, I, most graciously, will grant you the highest privilege of bringing them... to my front door!\"{/glitch}"

    silver @closedbrow talking2mouth "Our reward is more chores."

    show ionojustteal closed
    show ionojustpink closed
    with dis

    Character("{gradient=#EE8FB5-#1d8fc5}I-Balls{/gradient}") "{glitch=5.00}\"That's how fetch quests work, friendo.\"{/glitch}"

    silver @closedbrow talking2mouth "Ugh."

    narrator "Silver grumpily gathers up all the collected items, muscles straining against the heavy load, though he seems unbothered."

    redmind @sad2eyes poutmouth lightblush "[ellipses]"

    silver @talking2mouth "Alright. Where are we taking this?"
    
    show ionojustteal happy
    show ionojustpink happy
    with dis

    Character("{gradient=#EE8FB5-#1d8fc5}I-Balls{/gradient}") "{glitch=5.00}\"Um... just follow me!\"{/glitch}"

    call clearscreens() from _call_clearscreens_241
    scene blank2 with splitfade 

    pause 1.0

    narrator "You all follow I-Balls' two drones, which make their way through the Contest Coliseum's hallways, unsteadily bumping into each other and the walls. It seems that they've become even more broken since the last time you saw them."

    skyla @sadbrow talkingmouth "Those drones don't have much airtime left in them..."

    silver @talking2mouth "Yeah. That's why we're getting them the help they need."

    pause 1.0

    skyla @talkingmouth winkbrow "Being a hero feels good, doesn't it?"

    silver @closedbrow talking2mouth "Still fifty-fifty on if we're actually working for the bad guy here."

    gardenia @talkingmouth "You're working for {i}me{/i}. I'm not the bad guy!"

    silver @talking2mouth "Yeah? Because you've got a bit too much money for me to believe that easily."

    gardenia @surprisedbrow talking2mouth "What? But... I mean, you're in Kobukan, too..."
    gardenia @angrybrow talking2mouth "And, hey, I earned my money!"

    pause 1.0

    silver @talking2mouth "People say that all the time, like that justifies anything. I'm sure you earned it, and I don't care if you didn't."
    silver @talking2mouth "What I'm wondering is what you {i}did{/i} to earn it. Because I'm pretty sure you don't become a billionaire off of yoga classes and hunting ghosts."

    pause 1.0

    gardenia @sadbrow frownmouth "[ellipses]"

    silver @sadbrow talking2mouth "I know you haven't done anything wrong to {i}us{/i}. I'm just..."
    silver @closedbrow talking2mouth "Ugh, forget it. I can't start a conversation without picking a fight."
    silver @talking2mouth "I'm going on ahead. I need to put this junk down soon. I-Balls, hurry it up."

    pause 1.0

    cheren og @smilemouth "[ellipses]"

    skyla @talking2mouth "Boss? What are you smiling about?"

    cheren @talkingmouth "Oh, not much."
    cheren @closedbrow talkingmouth "It's just... Silver, referring to the Disciplinary Committee, said 'us.'"
    cheren @talkingmouth "A milestone, perhaps."

    pause 1.0

    skyla frownmouth "[ellipses]"
    skyla -frownmouth "Hm."
    skyla @talkingmouth "But whose milestone?"

    pause 2.0

    narrator "You follow I-Balls' drones deep into the bowels of the Contest Coliseum, discovering that it has at least two more basement levels than you were expecting."
    
    if (HasEvent("Professor Oak", "ClearedCatacombs")):
        narrator "In fact, you suspect the path you're taking to get here may just reconnect with the very tunnels that you found the Tinkatitanium in."
    
    scene ionodoor with splitfade

    narrator "You walk up to a big metal door embedded in a wall. The door itself is padlocked, chained, and covered in an intimidating series of mechanisms." 
    narrator "It reminds you, somewhat disconcertingly, of a cross between a survivalist's bunker, and a mausoleum."
    narrator "Something one goes into... then is never followed into, nor permitted to leave."

    pause 1.0

    scene streamstartingsoon1 with Dissolve(2.0)

    narrator "Perhaps the air down here is a bit thin. Your mental monologue doesn't normally wax so poetic."

    cheren og @talking2mouth "Silver? Where'd I-Balls go?"

    silver @talking2mouth "Right in here. The drones flew through that little door. I just pushed the rest of the junk in after them."

    Character("{gradient=#EE8FB5-#1d8fc5}I-Balls{/gradient}") "\"Just give me a second! I'm about to make my big meatspace debut. Just need to fix up {i}these things{/i} first.\""

    pause 1.0

    skyla @talking2mouth "Will that take a while? Hover engines are pretty tricky pieces of machinery."

    Character("{gradient=#EE8FB5-#1d8fc5}I-Balls{/gradient}") "\"Nyohoho! What do you take me for?! I'll have you know I am a {i}master{/i} engineer! A job like this is as easy as speedrunning 1-1, for me!\""

    pause 1.0

    Character("{gradient=#EE8FB5-#1d8fc5}I-Balls{/gradient}") "\"Yeah, this'll probably take about three hours.\""

    show streamstartingsoon6 with dis

    silver @closedbrow talking2mouth "Gimme a break!"

    cheren @sad2brow talkingmouth "Well, there goes my [timeOfDay.lower()]."

    Character("{gradient=#EE8FB5-#1d8fc5}I-Balls{/gradient}") "\"Sorry, lovelies! Technical difficulties. Need to make sure all my gadgets and gizmos are stream-ready, yanno!\""

    hide streamstartingsoon6 with dis

    skyla @talking2mouth "Well, it's alright. I don't have anywhere to be right now."
    
    cheren @talkingmouth "Nor I. Perhaps we could just... sit together and chat?"

    silver @surprisedbrow frownmouth "[ellipses]"

    gardenia @surprisedbrow frownmouth "[ellipses]"

    skyla @surprisedbrow frownmouth "[ellipses]"

    cheren @sad2brow talkingmouth "Just a thought. Perhaps we could play cards, instead. Silver, you carry a pack with you, don't you...?"

    narrator "Silver awkwardly pulls out a pack of well-used playing cards, and the five of you play a couple rounds of Pokér." 
    narrator "It is mostly silent, save for the frequent sound of banging metal, and hurled expletives coming from the vaultlike door next to you."

    pause 2.0

    narrator "After approximately three hours, three minutes, and the amusing revelation that Gardenia, in spite of expectation, is {i}awful{/i} at Pokér, you hear a triumphant shout of victory."

    Character("{gradient=#EE8FB5-#1d8fc5}I-Balls{/gradient}") "\"Nyohohoho! Ladies and gentlemens, we have something!\""

    silver @closedbrow talking2mouth "Finally."

    Character("{gradient=#EE8FB5-#1d8fc5}I-Balls{/gradient}") "\"Ladies and gentlemens, please ready your pogs, because it's time for the meatspace debut of the {i}one{/i}--the {i}only{/i}--the inimitable and un-copyright strike-able {nw}"
    TempCharacter("{gradient=#EE8FB5-#1d8fc5}Iono{/gradient}") "Ladies and gentlemens, please ready your pogs, because it's time for the meatspace debut of the {i}one{/i}--the {i}only{/i}--the inimitable and un-copyright strike-able {fast}{cps=*0.25}{i}Iooooooooono{/i}!"

    show officialiono with gaussdissolve

    pause 1.0

    show streamstartingsoon6 behind officialiono with dis

    pause 2.0

    skyla @talking2mouth "Oh. So, this is, like, a placeholder, right?"

    Character("{gradient=#EE8FB5-#1d8fc5}Iono{/gradient}") "\"A placeholder? What do you[ellipses]!\""
    Character("{gradient=#EE8FB5-#1d8fc5}Iono{/gradient}") "{glitch=200.0}\"Shit!\"{/glitch}"

    hide officialiono 

    pause 0.5
    
    scene streamstartingsoon1 with dis

    Character("{gradient=#EE8FB5-#1d8fc5}Maybe Iono, you forgot{/gradient}") "\"Hold on, hold on! Forget about that! Forget that I did a name reveal! My real debut is happening in three minutes. I just have to fix some bugs!\""

    redmind @thonk "...Iono, she said?"

    if (GetRelationshipRank("Rosa") > 2):
        redmind @thinking "Didn't Rosa say that Iono's the person who voiced F-00 in {i}Everlasting Memories{/i}?"

    else:
        redmind @thinking sweat "Never heard of her."

    pause 1.0

    $ BecomeNamed("Iono")
    $ PlaySound("crowd_cheer.ogg")

    scene streamstartingsoon2 with gaussdis

    Character("{gradient=#EE8FB5-#1d8fc5}Iono{/gradient}") "\"Okay, okay! We're so back, chat, we're so back. You don't even know. Yadda yadda, meatspace debut, it's the one and ooooooooonly[ellipses] Iono!\""

    show blank

    pause 0.1

    scene streamstartingsoon3

    Character("{gradient=#EE8FB5-#1d8fc5}Iono{/gradient}") "\"Lights! Camera! Viewer interaction! The supercharged streamer from Levincia is here to steal your eyeballs in my Electroweb! Whozawatzit? You already know!\""

    pause 2.0

    scene streamstartingsoon4 with dis

    pause 2.0

    Character("{gradient=#EE8FB5-#1d8fc5}Iono{/gradient}") "\"Geez, tough crowd. Haven't seen chat this dead since I did that twenty-four hour graveyard stream.\""

    scene streamstartingsoon5 with slowdis

    narrator "You and the disciplinary committee stare at this bundle of colors, energy, and phrases you are {i}very{/i} far from understanding, utterly nonplussed, and unsure how to react."

    scene blank2 with splitfade

    pause 1.0

    scene ionodoor
    show silver:
        xpos 1/6
    show skyla:
        xpos 2/6
    show iono sneaky behind skyla:
        xpos 3/6
    show gardenia:
        xpos 4/6
    show cheren og:
        xpos 5/6 xzoom -1
    with splitfade

    silver @talking2mouth "...Iono?"

    iono smugeyebrow smugeyes catmouth @smugmouth "You know it! Now, aren't you overwhelmed to be in the actual presence of the real life Iono herself?"

    pause 1.0

    show iono surprised with dis

    silver @talking2mouth "I have no idea who you are."

    iono angrybrow frownmouth @angrybrow angrymouth "What? C'mon, you know! Iono! Of the Iono Zone? The Supercharged Streamer? The Gym Leader of Levincia?! Master Engineer of the Paldean Youth Technology Convention four years running?"

    skyla @sadbrow talkingmouth "...Sorry. I know where Levincia is, at least!"

    iono body5 concentratedeyebrow frownmouth @closedeyes talking2mouth "Boo. You guys need to get yourselves cultured. You're missing out on some incredible memes. You know, I was the one who made Jobbird go viral!"
    iono @angry angrymouth "That meathead Raihan got all the credit, but all he did was quote-post me and bold the text! There's no justice in this world, I tells ya!"

    red @confused "Wait... you were the one who made Dawn's Altaria into a meme?"

    iono happy @winkeyes happyeyebrow happymouth "Sure was! Like a bolt from the blue, my memetic magic zapped this July's hottest meme into existence. I got so many clickthroughs from videos reacting to my reaction to the Jobbird!"

    pause 1.0

    $ beter = ("B" + first_name[1:] if first_name[0] not in ["B", 'b'] else "D" + first_name[1:])
    $ biffin = ("B" + last_name[1:] if last_name[0] not in ["B", 'b'] else "D" + last_name[1:])

    iono -happy @happy impressedeyes impressedeyebrow impressedmouth "Wait a minute... you're [beter] [biffin], aren't you?!"

    red @unamusedbrow talking2mouth "[first_name] [last_name], actually."

    iono @happy "Yeah, yeah, yeah! That's incredible! My luck has totally turned around! No more hiding in a basement from evil Tinkaton for me--I've got an interview with the Jobbird slayer!"

    red @confused "You do?"

    iono body2 @sneaky smugmouth "Duh've course? I made you famous, friendo! Imagine what I could do for you if I was actually {i}trying{/i}!"

    cheren @upeyes talking2mouth "If I may step in for a moment, before [first_name] gets yet {i}another{/i} extremely unlikely boon handed to him--this was a group effort."

    iono happy @winkeyes happyeyebrow happymouth "Don'tcha worry about that! I've got watchtime rewards for {i}all{/i} my loyal subs. And I'm talkin' {i}way{/i} better than bathwater, here."
    iono thinking bravemouth @calmeyebrow talking2mouth "You guys are on a mission to hunt down the ghosts of Kobukan, right?" 
    
    show cheren sad2brow shadow smilemouth with dis
    
    iono happy @winkeyes happyeyebrow happymouth "You've got the money, the muscle, the heart, the hot, and the Cheren."
    iono @happymouth "But you know what you don't have? The guy in the chair! Mission control, the one manning the screens, the button-pusher! You know, Hackerman,{w=0.2} Mr. Universe,{w=0.4} Oracle,{w=0.6} that other Oracle,{w=0.8} or Otacon!"

    show cheren -sad2brow -shadow -smilemouth with dis

    pause 1.5

    iono sad sadmouth @defeatmouth sadeyes defeatedeyebrow "...There's no recognition here. I'm talking to normies, aren't I?"

    redmind @thinking "Not sure what that means, but I'm pretty sure I should be insulted."

    iono thinking bravemouth @calmeyebrow talking2mouth "Well, that's fine. I'll get y'all right up and educated for what's hot on the internet. Open up your earholes and get ready for an educationing!" 
    iono surprised @body2 talkingmouth "Chapter one: Dadaism and the Selfish Gene. Memes are--"

    silver @talkingmouth "No. We're not doing this. We have questions, and you better have answers."

    iono body2 @talkingmouth "...We'll come back to that, then!"

    gardenia @talkingmouth "Silver's right. I guess you're {i}not{/i} a ghost. But if you're not a ghost, then what about all the evidence I've gathered that says there {i}are{/i} ghosts here?"

    cheren @talking2mouth confusedeyebrows "Hasn't all our evidence pointed towards Iono, though?"

    cheren @talking2mouth "We saw flickering, distorted images... which ended up being Iono's hologram emitters failing."
    cheren @talking2mouth "We heard singing at night, and strange signals from Raihan's Rotom phone."

    iono @happy "Oh, I do karaoke streams sometimes! The signal recently has been pretty bad... I guess Raihan's Rotom is as roided-out as its trainer, because it should {i}not{/i} have been able to get those signals."

    cheren @talking2mouth "The last piece of 'ghost evidence' was the Will-'o'-Wisps, which ended up being nothing more than Iono's drones."
    cheren @sadbrow talkingmouth "I mean, Gardenia, we even went down into the tunnels." 
    cheren @talking2mouth "Yes, there were plenty of ghost Pokémon there, and I admit I was wrong about the tunnels themselves not existing, but during this entire time, we haven't gotten a single hint of an actual ghost."

    pause 1.0

    gardenia @talking2mouth "...Wait, did you guys not know about the other ghost evidence?"

    cheren @confusedbrow talking2mouth "There's more?"

    gardenia @sadbrow talkingmouth "Yeah. People have been reporting these weird dreams of a woman talking to them, and... and... people go into rooms in the Contest Coliseum, black out and come out a long time later, without even noticing!"

    pause 1.0

    if (HasEvent("Klara", "AcceptCoordinatorClub")):
        cheren @talking2mouth "I believe [first_name] mentioned that last one."
        cheren @talking2mouth "But one isolated report of strange behavior is not nearly enough evidence to take action on. And I've heard no reports of that other information you mentioned."

    else:
        cheren @talking2mouth "I haven't heard anything like that reported."

    gardenia sadbrow frownmouth @talkingmouth "But... it's true. I mean, I haven't seen it myself, but I... people {i}have{/i} told me that's happened to them!"

    cheren sadbrow frownmouth @smilemouth "[ellipses]"

    gardenia @angrybrow talking2mouth "Don't look at me like that. Why can't you accept that you {i}might{/i} be wrong?"

    cheren @talking2mouth "It's not logical. There's no credible evidence for the existence of ghosts."
    cheren @sadbrow talkingmouth "Believe me, if ghosts existed, then I[ellipses]"
    cheren @sad2brow talking2mouth "[ellipses]It's simply Occam's Razor. There's no evidence to support the existence of ghosts. There's plenty to support their fictionality."
    cheren @sadbrow talkingmouth "In light of that, what would you have me believe?"

    show gardenia -sadbrow -frownmouth with dis

    silver @sadbrow talking2mouth "...Look, sometimes, even if all the evidence in the world is pointing one way, you just have to close your eyes, plug your nose, cover your ears, and {i}choose{/i} to believe something else."

    cheren shadow @talking2mouth "That requires a strength I do not believe I have."

    silver @closedbrow talking2mouth "Well, work on it. Before it's too late."

    pause 2.0

    iono body2 @talkingmouth "So... we're all gucci, right? I can go back to my room, and you won't tell anyone about my little pad here?"

    show iono surprised:
        xzoom -1
        ease 0.5 xzoom 1

    skyla @talkingmouth "Um, I don't mean to be rude, but... you realize you're a little bit... flickery, right?"

    iono "Woah! Good eye!"
    iono thinking bravemouth @closedeyes calmeyebrow talking2mouth "But ya got me. I'm here, but I'm here as a hologram from my I-Balls. See, I can do this!"
    iono @nobody neutralpink2 neutralteal2 "See? No body! This technology lets me go wherever I want without worrying about germs or stalkers or clout-chasers trying to get a snap of my big, bouncy, I-Balls."
    iono -thinking @sneaky "Pretty snazzy, right? All manufactured by the one and only Iono, of course! Nyohohoho!"

    cheren -sadbrow -shadow @talking2mouth "Are you permitted to attend class virtually?"

    iono @scaredmouth "Sure. Daddy Drayden was chill with it."

    cheren @talking2mouth "...I hesitate to ask, but it's the [getRDay(0)] of [calendar.month_name[calDate.month]]. School started on the 5th of April. You haven't been hiding here, not attending classes, this entire time, have you?"

    iono @happy "Whaaaat? No, of course not! I just..."

    show cheren angrybrow with dis
    
    iono sad sadmouth @defeatmouth "{size=30}...hacked into the school's camera feed and watched the classes that way.{/size}"

    cheren @talking2mouth "That definitely wasn't permitted."

    iono angry poutmouth @angrymouth "Yo, what's with the trial? The school has recordings of classes for people who can't attend anyway, right? So what's wrong with using my mad skillz to get my own recordings?!"

    cheren @sadbrow talking2mouth "Firstly, the school does {i}not{/i} have recordings of classes available."
    cheren @sad2brow talking2mouth "Privately, I think they should--it requires very little effort on their part, and could help students who need it tremendously. But that's neither here nor there."
    
    show iono sad sadmouth with dis
    
    cheren @talking2mouth "Secondly, you were recording {i}hundreds{/i} of students without their consent. I know very little about you, but I understand that your privacy is quite important to you, no?"

    iono @defeatmouth "[ellipses]'m I goin' to need to make another apology vid for this...?"

    skyla @sadbrow talkingmouth "I don't think you need to do that. Just don't do it anymore!"

    silver @closedbrow talking2mouth "And delete those old videos, obviously."

    show cheren -angrybrow with dis

    iono body2 @happy "Oh, sure! I can do that, no problemo. In facto, I'm deletin' 'em right now! To the Shadow Realm, I banish thee!"

    #cheren -angrybrow @talking2mouth "You'll attend class from now on? In-person?"
    #cheren @talkingmouth sad2brow "[ellipses]In a manner of speaking."

    #iono @talkingmouth "Sure thing. I'll be right there in class, taking notes on my laptop and stuff. Bet most people won't even know I'm a hologram!"

    gardenia @talking2mouth "And when you're {i}not{/i} in class, you'll help us find the ghosts of Kobukan, right?"

    iono @body3 winkeyes happyeyebrow "Sure will! I might even have some hints on that front already."

    gardenia @talking2mouth "...Great."

    #why is iono here

    cheren @talking2mouth "I have some more questions for you, but perhaps we'll ask them later. Mainly logistical concerns."
    cheren @talking2mouth "[first_name]? Perhaps you'd be interested in handling that side of things?"

    red @confused "What?"

    cheren @talkingmouth "Well, none of us are exactly {i}people persons{/i}, and it seems Iono already wishes to collaborate with you in some manner."

    if (ionogiftsgiven > 0 or HasEvent("Professor Oak", "ClearedCatacombs")):
        cheren @closedbrow talking2mouth "Besides which, she has a lot to thank you for."

    if (ionogiftsgiven == 3):
        $ AddEvent("Iono", "ThreeGiftsGiven")
        iono @happy "No kidding! All that stuff you brought me...? I'd be a limping target for that evil Tinkaton without that!"

        $ ValueChange("Iono", value=21, position=0.5)
        narrator "Iono is clearly extremely grateful for all the items you brought her!"
    
    elif (ionogiftsgiven == 2):
        $ AddEvent("Iono", "TwoGiftsGiven")
        iono @happy "No kidding! That stuff you brought me...? I'd be a limping target for that evil Tinkaton without that!"
        $ ValueChange("Iono", value=14, position=0.5)
        narrator "Iono is clearly grateful for the items you brought her!"

    elif (ionogiftsgiven == 1):
        $ AddEvent("Iono", "OneGiftGiven")
        iono @happy "No kidding! That thing you brought me...? I'd be a limping target for that evil Tinkaton without that!"
        $ ValueChange("Iono", value=7, position=0.5)
        narrator "Iono is grateful for the item you brought her!"

    if (HasEvent("Professor Oak", "ClearedCatacombs")):
        $ AddEvent("Iono", "ClearedCatacombsBeforeIono")
        iono @happy "I mean, that Tinkatitanium you got me was {i}great!{/i} Now I can build my I-Balls out of Tinkatitanium, and make them more Smack Down-proof!"
        $ ValueChange("Iono", value=9, position=0.5)

    iono @happy "So, yeah, totally down to collab, and do a little AMA with you!"
    iono sneaky @smugmouth "Just be warned that when I do an 'AMA,' it's a two-way street. I'mma get {i}all{/i} your deets, [beter]."

    red @sadbrow talkingmouth "Sure. But, uh, just a heads-up. There's not really that many deets to learn."

    show iono body2 with dis

    silver @closedbrow happymouth "{size=30}Hah.{/size}"

    cheren "[ellipses]"

    cheren @talking2mouth "Something just occurred to me. We've all been pursuing you, and your name, but I don't believe any of us properly introduced ourselves."
    cheren @talkingmouth "Though you've probably gathered our names from us yelling at each other..."

    show skyla surprisedbrow frownmouth with dis

    cheren surprisedbrow @closedbrow talking2mouth "Skyla Huuro, Silver Sakaki, Gardenia Natane, [first_name] [last_name], and Cheren Younger, at your service."

    show silver surprisedbrow frownmouth
    show gardenia surprisedbrow frownmouth
    show iono surprised
    with dis

    skyla @talking2mouth "{i}Younger{/i}?! Like the terrorist?!"

    pause 1.0

    show silver sadbrow
    show gardenia sadbrow frownmouth
    show iono sad sadmouth
    with dis

    cheren -surprisedbrow @tired sad2brow talking2mouth "...There was surely a better way to ask that."

    skyla sadbrow frownmouth @talking2mouth "I... I'm sorry, I just remembered seeing something on the news, and..."
    skyla @talking2mouth "I'm sorry. That must have been really hard for you."

    if (IsAfter(6, 6, 2004)):
        cheren @sad2brow talking2mouth "It was over eight years ago."
    elif (IsDate(6, 6, 2004)):
        cheren @sad2brow talking2mouth "It was exactly eight years ago."
    else:
        cheren @sad2brow talking2mouth "It was over seven years ago."

    cheren sad2brow noshine frownmouth @talking2mouth "June 6th, 1996."

    pause 2.0 

    cheren -sad2brow -noshine @talking2mouth "I can hardly remember it."
    cheren @talking2mouth "My mother made some poor choices, and accepted the consequences she suffered. It's of no account; not years later, not to us, and certainly no longer to her."

    pause 1.5

    cheren @sadbrow talkingmouth "C'mon. Cheer up, everyone. I'm sure we all have family connections that we're less than enthused about."

    silver @closedbrow talking2mouth "{size=30}You can say that again.{/size}"
    silver @talking2mouth "Cheren's right. We did it. I mean, we didn't do the thing we thought we were doing, but we {i}did{/i} do something, and that[ellipses]"
    
    show silver -sadbrow
    show gardenia -sadbrow -frownmouth
    show iono -sad sadmouth
    with dis
    
    silver @closedbrow happymouth "Well, it's something, at least."

    cheren @talking2mouth "True. Now, it seems we've made contact with the 'ghost', and at least disproven this first set of supernatural phenomena."

    skyla neutralbrow neutralmouth @surprised "Oh! Oh! I can say the thing, then! Hold on, let me--"

    narrator "Skyla strikes a heroic pose, pointing up at the sky."

    show silver smilemouth
    show gardenia happy
    show cheren sad2brow smilemouth
    show iono happy
    with dis
    
    skyla happy "{size=40}Mission complete!{/size}"

    $ PlaySound("audio/07_fanfare.ogg")

    pause 2.0

    show blank2 as newblank2 with Dissolve(2.0)
    scene blank2

    cheren og @sad2brow talkingmouth "...Perhaps there's some merit to continuing the search."

    gardenia @sad2brow talkingmouth "Even though ghosts don't exist?"

    cheren @talkingmouth "Even though."

    call clearscreens() from _call_clearscreens_224

    pause 2.0

    narrator "[bluecolor]You have formed a bond with Iono!{/color} If you want to visit her in your free time, go to the Battle Hall, then find your way to the Contest Coliseum from there."
    if (GetValue("Iono") > 9):
        narrator "You suspect that after making such a strong first impression, she would like to collaborate with you soon... perhaps, when you have some free time, you should visit her."

    pause 2.0

    scene ionodoor at night 
    show flashback
    with Dissolve(5.0)

    TempCharacter("{color=#383381}???{/color}") "{glitch=5.0}So, you're looking for ghosts...?{/glitch}"

    pause 1.0

    scene ionodoor with vpunch

    TempCharacter("{color=#383381}???{/color}") "What a load of shit! What kind of idiot would believe in something like that? {cps=3}{size=40}Kekekeh!{/size}{/cps}"
    
    scene blank2 with Dissolve(2.0)

    return