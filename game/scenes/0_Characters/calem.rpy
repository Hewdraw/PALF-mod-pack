label Calem1:
    scene hall_B 
    show calem annoyedbrow
    with Dissolve(2.0)
    stop music fadeout 1.5
    $ renpy.music.queue("Audio/Music/lumiose.ogg", channel='music', fadein=0.0, tight=None)

    red @talkingmouth "Oh, hey, Cal-"

    calem @talking2mouth "[first_name] [last_name], have you and Serena engaged in a conspiracy to get me a date?"

    pause 2.0

    red @surprisedbrow frownmouth "[ellipses]"
    red @sweat closedbrow talkingmouth "Well[ellipses] shit."

    calem @closedbrow talking2mouth "I know I need not tell you why that's incredibly silly."

    red @sadbrow talkingmouth "I'm right there with you, man. Serena kinda... force-of-will'd me into it."

    calem @closedbrow talking2mouth "Yes... I know exactly what you mean."

    pause 1.0

    calem -annoyedbrow @talkingmouth "[first_name], I understand your intentions were benign, but... you must also understand that this was a bit condescending, no?"

    red @sadbrow talkingmouth "Yeah, I get that."

    calem @closedbrow talking2mouth "I am no wide-eyed schoolboy fresh from the Kalos countryside, I assure you."
    calem @talkingmouth "I am more than capable of handling my own romantic pursuits, or lack thereof."

    red @sadbrow talkingmouth "Calem, I promise, I know. You're preaching to the choir. It's Serena who needs to be told this."

    calem @closedbrow talking2mouth "Which I very much intend to, possibly tonight. But you are the man in front of me, right now."

    red @closedbrow talking2mouth "Okay, well, like I said--I'm sorry. It won't happen again."

    calem @closedbrow talking2mouth "Thank you."

    pause 1.5

    calem smilemouth @sadbrow talkingmouth "I apologize for my brusqueness."

    red @sweat talking2mouth "It was probably deserved."

    calem @talkingmouth "Nonsense. Good manners are the bare minimum you should be able to expect in return for your efforts."

    red @wince talking2mouth "...Eh. Not sure {i}these{/i} particular efforts warrant it, but... thanks anyway."
    red @confused "Although, now feels like the best time to ask, and I kind of have to. What's your situation with Serena?"

    pause 1.0

    calem @closedbrow talking2mouth "At the present? Or in the past?"

    red @sweat talkingmouth sadbrow "Both, I guess."

    calem @thinking "Hm."
    calem @annoyedbrow talkingmouth "I am loath to answer a question with a question, but I suppose I must ask if you're asking because you have an interest in her."
    
    pause 1.0

    calem @closedbrow talkingmouth "In a romantic sense, that is."

    menu:
        "Yes.":
            $ AddEvent("Calem", "SerenaCrush")
            $ calemknown = GetCrossKnown("Calem", True)
            if (calemknown != ""):
                $ AddEvent("Calem", "CheaterIntent")
                show calem surprisedbrow with dis

                pause 2.0

                calem annoyedbrow @talking2mouth "Oh."

                red @happy "Hey, Calem, what's wrong? Are you jealous?"

                pause 1.0

                $ ValueChange("Calem", -5)

                calem @talking2mouth "I was under the impression you were intimate with [calemknown]."

                red @surprisedbrow frownmouth "[ellipses]"

                calem @talking2mouth "I'm not fond of this stunned silence. It does not cast you in a good light. Please explain this misunderstanding."

                red @closedbrow talking2mouth "Uh... I kinda..."

                calem @talking2mouth "I am aware that polyamorous relationships exist. However, I do not believe you have discussed this possibility with [calemknown]. Have you?"

                red @closedbrow talking2mouth "I... yeah, sorry. I got a bit ahead of myself."

                calem -annoyedbrow @closedbrow talking2mouth "I do not know the particulars of your relationships. But the best way to avoid strife is clear and open communication amongst all parties--{i}beforehand{/i}."

                calem @talking2mouth "As a show of good faith, and a sign of my trust that you will make the decisions that cause the greatest amount of good, I will tell you this story. I ask you use this knowledge for positive means."
            
            else:
                calem @talkingmouth "Noted. I assure you I will not be an obstacle."

        "No.":
            $ AddEvent("Calem", "SerenaLike")
            calem @talking2mouth "Hm. Very well."

        "Don't worry about that. Just tell me.":
            $ AddEvent("Calem", "SerenaAvoid")
            calem @talking2mouth "Hm. Very well."

    calem @talking2mouth "...I met her when I moved to Vaniville Town when my art mentor's health began to fail, and city life became too much for her. This was in, oh, late 2001, I believe."
    calem @talkingmouth "I didn't know much about her. As I understood it, she was another Kalosian, someone I had simply never seen before. I lived in Lumiose City for many years... it was definitely possible I'd overlooked her as a child."
    
    pause 1.0
    
    calem @blush sadbrow talkingmouth "As a man, though... it was impossible to overlook her."
    calem @closedbrow talking2mouth "She was--{i}is{/i} gorgeous, intelligent, generous, funny, and so dreadfully ambitious. I worried that if I looked away for a moment, I would look back to see her occupying the Prime Ministership."
    calem @sadbrow talkingmouth "'Smitten' does not begin to cover my thoughts. I had loved before... but when I saw her, for the first time, I {i}fell{/i} in love."
    calem @closedbrow talkingmouth "I could not begin to tell her how ardently I admired and loved her. I thought of her first thing in the morning, when I woke. She was my last thought before I laid my head to rest."

    red @lightblush frownmouth "[ellipses]"

    red @talkingmouth "Uh... wow. I just learned more about her {i}and{/i} you than I think I ever knew before."

    $ ValueChange("Calem", 2, 0.33, False)
    $ ValueChange("Serena", 2, 0.66)

    narrator "Your understanding of Serena and Calem increased!"

    red @talking2mouth "But, like, dude. I thought you didn't like her?"

    calem @sadbrow talkingmouth "And yet, between the two of us, I'm considered the weaker actor."

    pause 1.0

    red @talkingmouth sadbrow "What happened, man?"

    calem @talking2mouth "...I grew up. I saw what sorts of priorities I needed to dedicate my life to, and knew that I could not address them within the same lifetime that I would devote myself to Serena."

    red @confused "C'mon. What do you mean by that?"

    if (HasEvent("Calem", "SerenaCrush")):
        calem @sadbrow talkingmouth "You said yourself you are interested in romance with her. You understand, surely? I cannot live a life where I claim to love her, but she does not receive all the love I wish to give her."
    else:
        calem @sadbrow talkingmouth "You've met her. You understand, surely? I cannot live a life where I claim to love her, but she does not receive all the love I wish to give her."

    red @closedbrow talking2mouth "It's not an all-or-nothing thing, man. She likes you--she'd be happy to have whatever you can give."

    calem @sadbrow talkingmouth "I trust your counsel and know your intentions are good, but you cannot speak for her."

    pause 1.5

    red @sad2brow talking2mouth "What would keep you so busy, anyway? So busy you couldn't pay attention to this woman you love more than anything?"

    calem @talking2mouth "...Not more than anything. There is one thing I love more."
    calem @closedbrow talking2mouth "Kalos, my home. {i}Belle terre{/i}. To preserve it is my greatest goal, and it will take a lifetime--or at least half of one."

    pause 1.0

    calem -smilemouth @talking2mouth "Are you familiar with the {i}Lysandre Labs{/i} incident?"

    red @talking2mouth "Doesn't ring a bell."

    calem @talking2mouth "In 2002, a businessman of some prominence in the region--Lysandre Fuladari--announced his intention to destroy the region."
    
    red @surprised "What? The whole region?"
    
    calem @sad "And much of the surrounding area, including Galar and Paldea. He claimed he would use some sort of... 'weapon' to do this. Something from history's pages, long forgotten."

    if (GetRelationshipRank("Hilbert") > 1):
        redmind @thinking "Yeah... I know what this is about. This is that Ultimate Weapon that I read about with Hilbert, isn't it? The cannon."

    calem @closedbrow talking2mouth "Clearly, he was quite mad. Nothing he promised came to pass, and he was arrested very shortly after his proclamation."

    red @talkingmouth sadbrow "I'm sensing a 'however.'"

    calem @sadbrow talkingmouth "Acute of you, I'm afraid."

    pause 1.0

    calem @annoyedbrow talking2mouth "...However, Lysandre was a very involved public figure. He was seen talking with our champion at length. He invented the Holo Caster, the primary method of communication in Kalos."
    calem @annoyedbrow talking2mouth "Far worse is that his second-in-command was one of our Elite Four. Her position still has yet to be filled--Diantha has received much heat for that."
    calem @sad "People have lost faith in the government, in the people that we relied on and respected. The region is on edge, and a push in either direction could decide its fate."
    calem @closedbrow angrymouth "At the same time, there are opportunists from other regions attempting to warp the narrative and influence the media in our country, breaking down order and trust."
    calem @annoyedbrow talking2mouth "At the risk of losing my apolitical veneer--far too much of the Kalosian populace's opinions on their government is formed by Galarian television."

    pause 0.5

    calem @closedbrow talking2mouth "I believe my countrymen can handle the clean-up efforts from within. I do not seek to be a politician. But this sense of isolation, of relying too greatly on internal strongmen, is what caused this."
    calem @talkingmouth "To do right, we must look outwards."
    calem @closedbrow talking2mouth "Kalos cannot recover from this state alone. Strong bonds, alliances, and friendships between people who may think, speak, and look entirely differently are the key."
    calem @talking2mouth "To save the region I love, I must forsake my..."

    pause 1.0

    red @confused "My?"

    pause 1.5

    calem @sad "Me."

    pause 1.0

    calem @annoyedbrow talking2mouth "I will be on call at all hours of the night. I will shake hands with those whose hands have never felt dirt, and those whose hands are bloody." 
    calem @closedbrow talking2mouth "I will say what I need to bring people together. All for the sake of getting them to the same table." 
    calem @sadbrow talking2mouth "I will be the mouthpiece for hundreds of arrogant, egocentric, avaricious politicians who would rather their people starve than admit fault."
    calem @talkingmouth sadbrow "Do you understand, [first_name]? This is what I have devoted my life to. Sacrifice and sublimation of the self."
    calem sadbrow smilemouth @closedbrow talking2mouth "Serena deserves better than to love a non-entity... and one who could rarely attend to her, in any case."

    pause 1.5

    red @talkingmouth sadbrow "I understand. I'm not sure I agree, but only you can decide what your priorities are, so..."
    red @talking2mouth "If this is the only path that you can be satisfied with, then that's that."

    calem @sadbrow talkingmouth "Bless you, [first_name]. I, myself, am blessed to have in my company {i}two{/i} individuals so charming and empathic."

    red @happy lightblush "Flatterer."

    pause 2.0

    calem @talkingmouth "'Sacrifice is art.'"

    red @thonk "Hm?"

    calem @talkingmouth "'Art is sacrifice.'"

    red @talking2mouth "I guess that's implied by the last thing, yeah."

    calem @closedbrow talkingmouth "The words of my art mentor. A brilliant painter. I suspected, as did my parents, that I would go to art school. When I elected to pursue a career in diplomacy... ha! They were quite upset."
    calem @talkingmouth "I'm sure you can see the irony. The prodigal son veering off the path of artistry laid before him to pursue international relations? Seems rather the inverse of the common theme."

    red @talking2mouth "Are your parents artists?"

    calem @talking2mouth "Aggressively so. They're part of an artist commune that has... very liberal views on relationships. And intellectual rights, incidentally."
    calem @talking2mouth "There are, of course, two parents that I can trace my lineage to, but it would not be wholly incorrect to say I had at least seven parents."

    red @surprised "Woah. Kalos is, uh..."

    calem @sad "Please do not attribute this to Kalos as a whole. My parents are... very much a special sort."
    calem @closedbrow talking2mouth "Come to think of it, given their anti-societal views, I suppose I've always played the role of the rebellious teenage son, with my keen interest in governmental work."
    calem @talking2mouth "Even in my art, I was somewhat of a black sheep. I became quite blasé to nude portraiture {i}very{/i} early. I preferred landscapes--buildings--manmade marvels."
    calem @happy "Ha! When the rest of my playgroup were painting Galarian Rapidash, Florges, and other fantastic sights, I wanted to paint the coffee shop I passed by every day on the way to my lessons."

    red @happy "Dude. This is hilarious. And adorable. You're the edgy goth kid, except you went counter-counter-culture."

    calem surprisedbrow bigblush @talking2mouth "{size=30}Adorable?{/size}"

    pause 1.5

    calem -surprisedbrow blush @closedbrow talking2mouth "W-well, be that as it may, my, er, counter-counter-culturality was certainly not a {i}conscious{/i} choice."
    calem @closedbrow talkingmouth "Perhaps it is simply the nature of children to think their parents are absolute dorks, and strive for something else."

    pause 1.0

    calem -blush @talkingmouth "What about you, [first_name]? Are you the apple that fell far from the tree?"

    red @sadbrow talkingmouth "In the sense that I'm still alive, while my Dad is, uh pretty bad at that."

    calem @sad "My sympathies. I'm sure he was a good man."

    red @talkingmouth "As far as I know. He went down with Cinnabar."

    calem @closedbrow talking2mouth "Hm. That disaster... yes, I'm familiar with it."
    calem @talkingmouth "What of your mother?"

    red @winkbrow happymouth "Wow, you {i}just{/i} learned my Dad's dead, and you're asking me about my mother? I heard Kalosians move fast, but--"

    calem @closedbrow talking2mouth "That is a vicious stereotype[ellipses] {nw}"
    extend @closedbrow talkingmouth "that is accurate too often for me to wholly dismiss. Ah, it is the air of Kalos. It simply makes you believe in love. What can I say?"

    pause 1.0

    red @talkingmouth "A lot, and you say it pretty well, too."

    pause 1.0

    calem @closedbrow "Hm."

    pause 1.5

    show calem -smilemouth sadbrow with dis

    red @talkingmouth "Hey, bud. If you could somehow spend the time with Serena that you think she deserves, {i}and{/i} be on-call in case Cynthia needs you to talk to Lance, would you do it?"

    pause 1.0
    
    calem @closedbrow talking2mouth "I'm not sure there's much worth in pursuing this fantasy, [first_name]. I am quite simply one man, with one lifetime."
    calem @sadbrow talkingmouth "I've dedicated myself to one thing over another. I must prioritize."
    calem @closedbrow talking2mouth "What's that Unovan expression, again? 'Never half-ass two things...?'"

    red @sadbrow talkingmouth "'Whole-ass one thing'."

    calem @happy "Crude but truthful!"

    red @talkingmouth "Well, maybe it's not 'worth pursuing this fantasy.' We might not be able to change anything. But I guess I'm just interested in what your true thoughts are."
    red @sadbrow talkingmouth "You're a really interesting guy, Calem. I've never seen someone with such a strong sense of responsibility. And if you're putting aside your feelings to help other people, that's fine, I guess..."
    red @happy "But I don't want you to forget what they {i}are{/i}, you know?"

    calem smilemouth @sadbrow talkingmouth "Hm. I'm unsure what I did to deserve this level of care and consideration... but I suppose that's the second time I've thought that."
    calem @closedbrow talking2mouth "Very well. In a perfect world, a world where time is free and love is boundless, where I can give to everyone everything they need at no cost to myself..."
    calem @talkingmouth "I suppose I would love it all with reckless abandon. My nation, you, Serena, my art, my Pokémon, my parents, my--"

    red @confused lightblush "Sorry, what was that second one?"

    calem @talkingmouth "Oh. You."

    pause 1.5

    red @sweat blush confused "Like, uh, platonically...?"

    calem @sadbrow talkingmouth "...[first_name], my dear friend, this is not a conversation we should have. The 'would haves' and 'could haves' have no good reason to be discussed when no actionable course can be followed to claim them."

    red lightblush @talking2mouth "Uh... Sorry."

    calem @surprisedbrow talking2mouth "Whatever for?"

    red @sad2brow talkingmouth "I wasn't really properly respecting how you felt about... the sacrifices you need to make."
    red @talkingmouth sweat closedbrow "It was a lot easier to talk about this when I wasn't part of it."

    calem @talkingmouth "The abstract artist is, often, somewhat removed from his piece."

    red @closedbrow talking2mouth "Alright, deep breaths..."
    red -lightblush @happy sweat "Hey, let's, uh, let's move the conversation back to Serena, okay?"

    calem @talkingmouth "As you wish."

    red @sad2brow talking2mouth "So, uh, about where she's really from..."

    calem @sadbrow talkingmouth "Oh. Yes. That."

    pause 1.0

    calem @closedbrow talking2mouth "In retrospect, perhaps I should have seen the signs." 
    calem @sadbrow talkingmouth "Her Kalosian accent got a lot stronger towards the end of the time we knew each other. And she always had a strange store of knowledge that didn't seem to match the history she provided me."
    calem @annoyedbrow talking2mouth "But... love is blind, or so it's said. Blind {i}and{/i} a fool, to boot."
    calem @talking2mouth "In a way, it's comforting, I suppose, that the woman I loved so dearly doesn't actually exist. I can hardly lose her now."

    red @surprised "What?"

    calem @sad "Come now. She told me she was a Kalosian Coordinator, showed me forged educational transcripts--which I did not ask for, of course--and had a tremendous interest in the Kalosian art scene."
    calem @talkingmouth "Given what has come out about her origins, I find it hard to believe that she knew of Édouard Monet for any reason but to get closer to me."#intentional renaming

    pause 1.0

    show calem surprisedbrow -smilemouth with dis

    red @confused "Isn't that better...?"

    calem @surprisedmouth "Er..."

    red @closedbrow talking2mouth "Okay, not the lying about where she comes from, or who she is, part."
    red @sadbrow sweat talkingmouth "I agree that was a bit crazy."
    red @talkingmouth "But... if she became this new person, to be the perfect person for {i}you{/i}, and it worked, then... isn't that a sign you're perfect for each other?"

    calem @closedbrow talking2mouth "The Serena I knew was. But she is not the real Serena."
    calem @sadbrow talkingmouth "I was incorrect. I do not blame her for lying. I blame myself for believing it."
    calem -surprisedbrow @happy "Besides, what would you have me do? Ask her to put on a show for the rest of her life? Hide that who she is? She may very well do it, but I would die before asking such a thing."

    pause 2.0

    calem @closedbrow talking2mouth "[first_name], of all your attributes, I find myself appreciating your straightforward and earnest nature most."
    calem @sadbrow talkingmouth "I doubt it's escaped your attention that Serena and I have a habit, perhaps, of overcomplicating matters."

    red @happy "Maybe a little bit."

    calem @talkingmouth "In Lumiose, one often gets lost without a [bluecolor]map{/color}. I feel as though talking with you provides the same sense of relief--the sense of direction I've been lacking ever since the Student Council fiasco."
    calem @talking2mouth "My thoughts are far less muddied, and I think I can finally put this {i}fausse{/i} romance far behind me. Now, at last, I can focus on my priorities, as they exist now."

    red @talking2mouth "Which are?"

    calem @talkingmouth "Step one. Continue to fulfill my campaign promises. Failure to win election is no excuse not to try my hardest."
    calem @talkingmouth "Step two. Work hard as a Kobukan student, and live an uncomplicated and uneventful school life until I graduate."
    calem @talking2mouth annoyedbrow "Step three. Make this Flabébé of mine respect me, or possibly die trying. Either result will be a relief."

    red @sadbrow talkingmouth "Still having trouble there?"

    calem @annoyedbrow talking2mouth "So much. Quite unlike any of the Fairy-types I grew up around. The 'fairest' type, my foot."

    red @sweat happy "You know, sometimes small, young Pokémon refuse to evolve because they want to learn a move that'll take more time if they {i}do{/i} evolve. Only way to snap them out of that is to make them stronger." 
    red @talkingmouth "I've got some time. I mean, for you. Want to train together?"

    calem sadbrow talkingmouth "I will gladly take you up on that. My thanks, as ever, are many."

    hide calem with dis

    $ RelationshipRankUp("Calem", "Map")

    return

label Calem1Part2:
    $ AddEvent("Calem", "Calem1Part2")
    stop music fadeout 1.5
    $ renpy.music.queue("Audio/Music/lumiose.ogg", channel='music', fadein=0.0, tight=None)
    call clearscreens() from _call_clearscreens_239
    scene blank2 with splitfade

    show midnight at vspaz    

    python:
        timeOfDay = "Midnight"
        playercharacter = "Serena"
        oldinventory = copy.copy(inventory)
        oldpersonalstats = copy.copy(personalstats)
        oldparty = copy.copy(playerparty)
        oldpersondex = copy.copy(persondex)
        oldclassstats = copy.copy(classstats)

        inventory = {
            Item.RhyhornReins : 1,
            Item.CoordinatorKit : 1,
            Item.TouristsGuidetoKalos : 1,
            Item.OUTRAGEMagazine : 1,
            Item.LoveLetters : 7,
            Item.BlueHandkerchief : 1,
            Item.TicketStubs : 2
        }
        
        personalstats = {
            "Charm" : 32,
            "Knowledge" : 15,
            "Courage" : 5,
            "Wit" : 64,
            "Patience" : 12
        }
        playerparty = GetTrainerTeam("Serena")
        persondex = copy.deepcopy(defaultpersondex)
        
        #serena
        persondex = copy.deepcopy(defaultpersondex)
        persondex["Calem"] = {"Named" : True, "Value" : 1, "Contact": True, "Sex": Genders.Male, "Relationship": "...?", "RelationshipRank": 0, "Events": [] }
        persondex[first_name] = {"Named" : True, "Value" : oldpersondex["Serena"]["Value"], "Contact": True, "Sex": Genders.Male, "Relationship": "Solute", "RelationshipRank": 0, "Events": [] }
        persondex["Leaf"] = {"Named" : True, "Value" : 24, "Contact": True, "Sex": Genders.Female, "Relationship": "Former Dormmate", "RelationshipRank": 0, "Events": [] }
        persondex["May"] = {"Named" : True, "Value" : 32, "Contact": True, "Sex": Genders.Female, "Relationship": "Dormmate", "RelationshipRank": 0, "Events": [] }
        persondex["Bianca"] = {"Named" : True, "Value" : 16, "Contact": True, "Sex": Genders.Female, "Relationship": "Former Dormmate", "RelationshipRank": 0, "Events": [] }
        persondex["Hilda"] = {"Named" : True, "Value" : 23, "Contact": True, "Sex": Genders.Female, "Relationship": "Former Dormmate", "RelationshipRank": 0, "Events": [] }
        persondex["Serena"] = {"Named" : True, "Value" : 28, "Contact": True, "Sex": Genders.Female, "Relationship": "Self", "RelationshipRank": 0, "Events": [] }
        persondex["Brendan"] = {"Named" : True, "Value" : 16, "Contact": True, "Sex": Genders.Male, "Relationship": "Dormmate", "RelationshipRank": 0, "Events": [] }
        persondex["Cheren"] = {"Named" : True, "Value" : 2, "Contact": True, "Sex": Genders.Male, "Relationship": "Betrayed", "RelationshipRank": 0, "Events": [] }
        
        persondex["Dawn"] = {"Named" : True, "Value" : 43, "Contact": True, "Sex": Genders.Female, "Relationship": "Clubmate", "RelationshipRank": 0, "Events": [] }
        persondex["Klara"] = {"Named" : True, "Value" : 2, "Contact": True, "Sex": Genders.Female, "Relationship": "Clubmate", "RelationshipRank": 0, "Events": [] }
        persondex["Tia"] = {"Named" : True, "Value" : 3, "Contact": True, "Sex": Genders.Female, "Relationship": "Clubmate", "RelationshipRank": 0, "Events": [] }
        persondex["Misty"] = {"Named" : True, "Value" : 26, "Contact": True, "Sex": Genders.Female, "Relationship": "Clubmate", "RelationshipRank": 0, "Events": [] }
        persondex["Brendan"] = {"Named" : True, "Value" : 56, "Contact": True, "Sex": Genders.Female, "Relationship": "Clubmate", "RelationshipRank": 0, "Events": [] }
        persondex["Jasmine"] = {"Named" : True, "Value" : 35, "Contact": True, "Sex": Genders.Female, "Relationship": "Clubmate", "RelationshipRank": 0, "Events": [] }
        
        classstats = { 
            "Normal" : 0,
            "Fire" : GetTrainerTeam("Serena", "Houndour").GetLevel() + 5,
            "Water" : 0,
            "Grass" : 0,
            "Electric" : 7,
            "Ice" : 0,
            "Fighting" : 3,
            "Poison" : 0,
            "Ground" : GetTrainerTeam("Serena", "Rhyhorn").GetLevel() + 2,
            "Flying" : 2,
            "Psychic" : 0,
            "Bug" : 0,
            "Rock" : 0,
            "Ghost" : 17,
            "Dark" : GetTrainerTeam("Serena", "Houndour").GetLevel() + 3,
            "Dragon" : 0,
            "Steel" : 0,
            "Fairy" : 7
        }

    pause 3.5

    scene dorm_B norm 
    show screen currentdate
    with splitfade

    serena pajama sadbrow frownmouth "[ellipses]"

    pause 2.0

    narrator "You are sitting on your bed, nervously waiting for the sound of the doorknob to turn."

    pause 1.0

    narrator "You're reminded forcefully of one of the many times you would be sitting outside the headmistress' office, waiting for your mother to finish speaking with her."

    scene serenaschool at sepia
    show flashback
    with Dissolve(2.0)

    narrator "'She lies,' the headmistress would say. 'Blatant, compulsive lies, about things she has no clear reason to lie about.'"
    narrator "'She has an active imagination,' your mother would respond, tight-lipped. 'She is very creative.'"
    narrator "'At Sienna Academy, we recognize and reward creativity. We cannot do so for deception.'"

    pause 1.0

    narrator "There would be a big pause, and your mother would sigh, defeated."

    pause 1.0

    narrator "'I don't know why...', she would mutter, trailing off, quiet enough you could not hear her."

    pause 1.0

    narrator "She didn't know why. She couldn't. How could {i}the{/i} Grace Umaoka, legendary Rhyhorn Racer, idol of Southwest Kanto, possibly understand?"
    narrator "You loved your mother. She loved you. Of this you were certain. But love did not grant the glory--the spotlight--the {i}grace{/i} you so desperately sought."
    narrator "Was it foolishness that you envied your own mother, wishing for the benefits of her accomplishments, without any of the effort taken to claim them?"
    narrator "Was it naivety to believe there was a glory for you that did not exist in the mud where your mother found gold?"

    pause 1.0

    narrator "The headmistress' voice cuts back in. 'Grace, given this repeated pattern of behavior, there aren't a lot of options left to us. It's not fair to the other children.'"
    
    pause 1.0

    narrator "'There is a school in Viridian, just West of here--an older man, Hoennian, runs it. They have a strong Ground-type program, that sets students well on the road to become trainers.'"
    narrator "'They're associated with the Viridian Gym, and have a history of taking on students with... {i}diverse{/i} histories. If the therapy is not working, then perhaps she would be more well-received there.'"

    pause 1.0

    narrator "Your mother's voice, cold, level, and quiet, cuts through the implication like a knife."
    narrator "'You think she will be well-received because the Viridian gym was run by a criminal. That's what you're saying.'"

    pause 1.0

    narrator "The headmistress did not flinch."
    narrator "'She is a talented, intelligent, and ambitious young woman. Unfortunately, we do not have the tools to equip her for success.'"

    pause 1.0

    narrator "The sound of a chair moving back, scraping on linoleum, then someone standing. A moment later, another chair moves, and another person stands."
    narrator "'I'm sorry about this,' a voice says. 'I love her. I do, really. I just... don't know why...'"

    pause 1.0

    narrator "You're not sure who said that one."

    scene blank2 with transeye

    pause 2.0

    $ hideside = True

    calem "{size=30}Serena?{/size}"

    pause 1.0

    calem "[ellipses]"
    calem "My dear, I know you're not asleep."

    pause 1.0

    $ hideside = False

    scene dorm_B norm
    show calem sadbrow:
        ypos 1.2 zoom 1.3
    with transeye2

    serena pajama @sad2brow poutmouth "[ellipses]"
    serena @talking2mouth sadbrow "I was at first."

    show calem:
        ypos 1.2 zoom 1.3
        ease 0.5 ypos 1.0 zoom 1.0

    calem @talkingmouth "I believe you."

    narrator "He shouldn't."

    show calem closedbrow with dis 

    calem @talkingmouth "We need to talk."

    serena @sadbrow talkingmouth "I assumed."

    pause 1.0

    calem -closedbrow @talking2mouth "Can we switch to Kalosian? I fear I may forget the language if I don't use it every once in a while."

    serena @talkingmouth "{i}Oui{/i}."

    pause 1.5

    narrator "Calem takes a deep breath, rubs his hands together, then looks down at {i}your{/i} hands, reacting with surprise at the sight."
    narrator "The words that follow are the same refined, chocolatey-sweet dulcet tones you fell in love with so many years ago."
    narrator "A painter Calem might be, but when speaking the language of his home, he is a poet."

    calem @sad "Poor girl. You've rubbed your knuckles raw with worry."
    calem @sadbrow talkingmouth "I trust you did not think me the sort of brute who would rage or scream over this misguided, but well-meaning gesture?"

    serena @sadbrow talkingmouth "N-no. Of course not."

    pause 1.0

    calem @talking2mouth "Serena, I understand your intentions were good--"
    calem @talkingmouth "And I understand you only want what is best for me--"
    calem @sadbrow talkingmouth "But you, of all people, should know that I am perfectly capable of getting myself a date under my own power."
    calem @talkingmouth "After all... I was not 'unpopular', in Kalos. There was a time when I even had to shut myself up in my room for a while to get away from it."

    pause 1.5

    calem @talking2mouth "Perhaps this plan was a plan within a plan? In your inimitable style, of course."
    calem @closedbrow talking2mouth "If I were to guess that the plan here was not, in actuality, to get me a partner, but to have me discover this plan, which you made little attempt to hide..."
    calem @closedbrow talking2mouth "Then I would have to wonder why. In which case my mind would naturally be left wandering, and in my egocentricity, assume it has something to do with your feelings for me."
    calem @sadbrow talkingmouth "If you were attempting to get me a date, a feat of which I am plenty capable, then one reason you might try to do this is so that I am no longer 'an option' for... well, anyone else."

    pause 1.0

    calem @annoyedbrow talking2mouth "Among that number of 'anyone else' is you."
    calem @sadbrow talkingmouth "And... as I've expressed my inability to commit to you wholly..." 
    calem @sadbrow talkingmouth "Offering me 'another', some form of substitute, would be something I would be immensely grateful for, and convey your respect and acknowledgement for my choices and preferences."
    calem @closedbrow talking2mouth "This appreciation may then result in me changing my mind."

    pause 1.5

    narrator "Calem studies your face, looking for any sign of a reaction. His eyebrows begin to arch with worry."

    calem sadbrow smilemouth @talkingmouth "Er... if I {i}am{/i} entirely incorrect, this will be possibly the vainest thing I've ever said."
    calem @closedbrow talkingmouth "{size=30}Though perhaps the vanity lies in the consideration, moreso than the veracity.{/size}"
    calem @sad "Well, not much that can be done on that count now. I've said my piece, and wait for your response."

    pause 2.0

    narrator "It would be so very easy to deny this. To deny every part of it. Calem will certainly believe you."

    pause 1.0
    
    narrator "So you do."

    show calem surprisedbrow -smilemouth with dis

    serena @sadbrow talkingmouth "Calem, my dear, there's no truth to that whatsoever."

    pause 1.0

    calem sadbrow smilemouth @annoyedbrow talking2mouth "Well, I certainly look like a prat now, don't I?"

    serena @happy "A very handsome prat, granted, but it's rather improper to attribute {i}my{/i} every action to attempting to claim a man's affection, is it not?"

    calem @closedbrow talking2mouth "Indeed it is. I'm quite embarrassed. I pray you forgive this impropriety of mine?"

    serena @talkingmouth "There's nothing to forgive. And if there were, it would be granted immediately upon conclusion of the offending act."

    calem @saddownbrow talking2mouth "I appreciate your mercy. If you told my parents of this matter, I'd probably be sentenced to read five volumes of queer feminist literature."
    calem @closedbrow talkingmouth "Fascinating prose, naturally, but there's only so many times one can read the word 'systemic' in one sitting before one becomes heavily inclined to remove {i}themselves{/i} from the system."

    pause 1.0

    calem @annoyedbrow talking2mouth "Come to think of it, that's actually {i}exactly{/i} what my parents did. Hm."

    pause 1.5

    calem @sadbrow talkingmouth "Well, that's not an option for me."
    calem @closedbrow talking2mouth "In any case, I hope now that I'm no longer suffering from these self-important delusions, we might bring things back to the way they were before."
    calem @sadbrow talkingmouth "Our conversation, perhaps, could become more... light."
    calem @talkingmouth "To that end, do you have any plans in the immediate future?"

    serena @sadbrow talkingmouth "I believe I've lost a bet to [first_name], so I'll be inviting him to a Rhyhorn race shortly. Beyond that, there's various activities planned with the Coordinator Club..."

    calem @closedbrow talking2mouth "Lovely. I'm quite pleased to hear you're spending time with [first_name], especially."
    calem @talkingmouth "He's a man of tremendously decent character. Kind and upright."

    serena @talkingmouth "Yes... he is. A good man."

    $ ValueChange("Serena", 3, 0.33, False, adjustoldpersondex=True)
    $ ValueChange("calem", 3, 0.66, adjustoldpersondex=True)

    narrator "Your trust in [first_name], shared with Calem, is absolute. You understand and appreciate [first_name] in ways you cannot quite form."

    calem @talking2mouth "I sometimes wonder[ellipses] in a different life, of course[ellipses]"
    calem @talkingmouth closedbrow "Oh, nevermind that."

    pause 1.5

    if (HasEvent("Calem", "SerenaCrush") and not HasEvent("Calem", "CheaterIntent")):
        calem @talking2mouth "Ah. Something occurs to me."

        calem @talkingmouth "During the course of our conversation, the topic of you came up, as it naturally does, given our mutual fondness for you."
        calem @closedbrow talkingmouth "He expressed... interest in you, my dear. Of a variety that I believe you may be receptive to, if you follow my drift."

        serena @surprisedbrow talking2mouth "Him? He... fancies me?"

        calem @sadbrow talkingmouth "In an uncomplicated and unrestrained way. Which I imagine makes a nice change of pace!"

        serena @surprisedbrow frownmouth "[ellipses]"

        calem @happy "I'll leave you to that thought."
        calem @talkingmouth "'There's always time for true love'... a phrase you're fond of. Not one I can necessarily agree with, given time's unchanging nature, but a lovely sentiment."
        calem @closedbrow talkingmouth "I believe he is worth looking into. I would myself, save that..."

        pause 1.5

        calem @sadbrow talkingmouth "Well, there's a multitude of factors, of which I'm quite certain further elaboration would provide no benefit."

    calem @talking2mouth "Regarding [first_name]... you are friends already. Close. Perhaps, something, to consider."

    serena @sadbrow talkingmouth "Calem... {i}we{/i} are friends already. {i}We{/i} are close."

    calem @talkingmouth sadbrow "This is true."
    calem @talking2mouth "But that man has something I do not have, and can never have."
    calem sadbrow @talkingmouth "You know I love you. But I cannot love you as you wish, nor as I wish. His heart may have the strength mine lacks."

    serena @sadbrow talkingmouth "You lack nothing I want."

    pause 1.5

    calem sadbrow -smilemouth @sad "Then why are there tears in your eyes, my dear?"

    pause 2.0

    serena sad tear "There are not."

    pause 1.0

    show calem:
        ypos 1.0 zoom 1.0
        ease 2.0 zoom 1.3 ypos 1.2

    calem @sad "I believe you."

    pause 1.0

    call clearscreens() from _call_clearscreens_240
    scene blank2 with transeye

    narrator "He shouldn't."

    python:
        inventory = oldinventory
        personalstats = oldpersonalstats
        playerparty = oldparty
        persondex = oldpersondex
        classstats = oldclassstats
        playercharacter = None

    pause 2.0

    scene bedroommidnight with splitfade

    $ PlaySound("vibrate.ogg")

    red casual hatless night @tired unamusedbrow talking2mouth "{size=30}Wha...{/size} Too early for this, who's... texting...?"

    show phone_B behind blank2
    show phone_A behind blank2
    with fadeinbottom

    show serena neutralbrow behind phone_A with fadeinbottom 

    serena "Hello. I hope I did not wake you. You'll probably see this text in the morning."

    red @closedbrow tired talking2mouth "Yeah, no luck."

    serena "I'm afraid the conspiracy has been rumbled. Your part, thus, ends."
    serena "No longer are you a necessary part of this machiavellian machinery. We are [bluecolor]friends{/color}."
    serena "And that is what Calem and I have arrived at. Friendship. Simple. It is for, I believe, the best. We can move on, and... and forget."
    serena "We would both like to extend our sincere and deep thanks for your patience and companionship. You have been an excellent friend to both of us. Better, perhaps, than we deserved."
    serena "I hope your dreams are sweet and uncomplicated. And I bid you good morning."

    pause 1.0

    serena poutmouth sad2brow "...also i owe you two rhyhorn race tickets now i guess"

    pause 1.0

    hide phone_A
    hide phone_B
    hide serena 
    with fadeoutbottom

    redmind @thonk tired "Well... I hope they're both happy with this. Not sure if they can really put aside these feelings they've had for so long, but..."
    redmind @thinking tired "At least they're trying. Maybe I can just be a friend to them now, instead of this weird chess piece." 
    redmind @sadbrow tired "Good luck."
    
    scene blank2 with splitfade

    $ RelationshipRankUp("Serena", "Friend", 2)
    $ RelationshipRankUp("Calem", "Friend", 1)

return
