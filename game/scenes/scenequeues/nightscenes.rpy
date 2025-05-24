label nightscenequeue:

label natenightscene:
    if (IsAfter(17, 5, 2004) and EventAvailable("Nate", "ClassSwap")):
        scene blank2 with splitfade

        stop music fadeout 1.5

        queue music "audio/music/nuvema2_start.ogg" noloop
        queue music "audio/music/nuvema2_loop.ogg"

        narrator "Elsewhere, in an area with a thin veneer of privacy..."

        scene garden night
        show nate frownmouth sadbrow at night:
            xzoom -1
        with splitfade

        nate @talking2mouth "...It never ends. Every step requires two follow-ups. It just {i}never{/i} ends."

        show nate at night:
            xpos 0.5 xzoom -1
            ease 0.5 xpos 0.33 xzoom 1

        show rosa at night:
            xpos 1.2
            ease 0.5 xpos 0.66

        rosa @surprised "Hm? Nate?"

        nate -sadbrow -frownmouth @happy "Hey there, RW! What're you doing out so late? Curfew's at 20 hundred, you know."
        nate @winkbrow talkingmouth "Just trying to get away from the cameras? Good luck with that."

        rosa sadbrow @talkingmouth "Um... yeah, something like that."

        nate @happy "Carry on then. Don't want {i}too{/i} much exposure when making a picture, right?"

        rosa @talkingmouth "Right."

        pause 2.0

        nate surprisedbrow frownmouth @confusedeyebrows talkingmouth "Hey, uh, need stage directions? Stage left is that way."

        rosa @talkingmouth "Um... I know this is none of my business, but... I can tell you're acting. And you seemed... sad."

        pause 1.0

        nate @closedbrow talkingmouth "Ah, well, everyone has down moments, right? I mean, you must've heard about Bianca by now..."

        pause 0.5

        rosa @sadbrow talkingmouth "I have... but I feel like you're sadder about that than most people. Like you feel responsible."

        nate @sadbrow talkingmouth "Irresponsible, more like."
        nate -surprisedbrow -frownmouth @happy "Don't worry about me, RW. In fact, do your best to forget about me."

        pause 0.5

        show nate surprisedbrow frownmouth at night with dis:
            xpos 0.33

        rosa @talking2mouth "...Lying makes a good living, right?"

        pause 1.5

        nate -surprisedbrow @angrybrow talking2mouth "What do you know?"

        rosa @sadbrow talkingmouth "That you're too good at lying to not do it professionally."

        pause 2.0

        nate -frownmouth @closedbrow talkingmouth "Sharp."

        rosa @happy "Like the film-cutter's scissors."

        pause 1.0

        nate @sadbrow talkingmouth "Still, I can't tell you anything. Can't even tell you if you're right."

        rosa @sadbrow talkingmouth "There are things I can't do, too. I understand... I think."

        nate @surprised "Awfully understanding, aren't ya? Spending all that time around that mind-reader... she's rubbed off on you."

        rosa @happy "I think she'd rub off on a lot of people, if they were able to spend time with her... um, without her spending time with them."

        nate @sweat talking2mouth "Yeah, I get that."

        pause 1.0

        rosa @talking2mouth "...I should be going."

        nate "{w=0.5}.{w=0.5}.{w=0.5}."

        pause 1.0

        nate @talkingmouth "Wait."

        rosa @talkingmouth "Yeah?"

        nate @talkingmouth "All those rules they put on you... all those lies they tell you, and all those lies they make you tell..."
        nate @sadbrow talkingmouth "You don't have to put up with it."
        nate @happy "I mean, some people just need to suck it up. But you deserve better."
        nate @sad2eyes sadeyebrows talkingmouth "Ah, but what do I know? I'm just a fan. I've loved your movies ever since I saw {i}World Order: Under New Management{/i}."

        pause 0.5

        if (HasEvent("Nate", "HasToxel")):
            nate @happy "You know what? You could use this Pokémon much better than I could. I'm about to drop Electric class, anyway, so I guess we're going to be seeing a lot less of each other."

            narrator "Nate casually passes Rosa his Toxel's Poké Ball."

        else:
            nate @sadbrow talkingmouth "I'm sure I barely registered on your radar, but, uh, I'm going to drop electric classes, so I guess we're going to be seeing a lot less of each other."

        $ AddEvent("Nate", "ClassSwap")

        rosa @surprised "Huh? Why?"

        nate @sadbrow talkingmouth "...It's a lot easier to do your work quietly in the dark than be the electric spark of hope. Tried the second one. Didn't work out."

        pause 1.0

        rosa @sadbrow talkingmouth "That's from one of my movies."

        nate @talkingmouth "Yeah. Remember which one?"

        rosa @sadbrow talkingmouth "Sorry."

        nate @talkingmouth "...Memory's a precious thing. Keep it as long as you can."

        nate happy "Cheers, RW."

        hide nate with dis

        return

label wallynightscene:
    if (EventAvailable("Wally", "NightScene")):
        scene blank2 with splitfade

        stop music fadeout 1.5

        $ renpy.music.queue("audio/music/Eterna_Start.ogg", channel='music', loop=False, fadein=1.5, tight=None)
        $ renpy.music.queue("audio/music/Eterna_Loop.ogg", channel='music', loop=True)

        narrator "While walking back to your dorm..."

        scene cafenight
        show wally angrybrow frownmouth
        with splitfade

        redmind @thonk "Hm? That's... Wally, right? What's he doing in the cafeteria so late at night?"

        pause 1.5

        narrator "You watch Wally for a bit longer, unsure if you should speak up. He seems deep in concentration, scribbling notes into a Ludicolo-themed notepad."

        redmind @thonk "Studying? I admire his commitment, but it's getting pretty darn late. Shouldn't he be getting back to his dorm soon?"

        wally -angrybrow "[ellipses]"

        pause 1.0

        $ PlaySound("!.ogg")

        wally @surprised "Oh! [wally_name]!"

        red @talking2mouth "Hey, Wally. Sorry, I was just walking past and noticed you were still here. It's pretty late, you know!"

        wally @happybrow lightblush talkingmouth "Yeah... I was just really focused on what I was writing here. Um, sorry, I know I should be going to my dorm--"

        red @talkingmouth "It's fine. I mean, I'm not part of the Disciplinary Committee."

        wally @happybrow talkingmouth "Eh... thanks. And, um, thanks for... pointing out the time. I think I probably would've kept writing until the sun came up if you hadn't walked in here."

        red @talkingmouth "Nah, I'm sure Chef Katy would've nudged you when the cooks go home."
        red @talkingmouth "Anyway, what were you writing? Something for school?"

        wally @sadbrow talkingmouth "K-kinda. Um... it's actually... kinda like research. But not for an assignment?"

        red @thonk "Hm?"

        narrator "You take a peek over Wally's shoulder at the Ludicolo notebook. Written on the front are the words 'Mirage Research #4.'"

        red @talking2mouth "What're you figuring out?"

        wally sad2eyes frownmouth "[ellipses]"

        wally -sad2eyes -frownmouth @sadbrow talkingmouth "Promise you won't laugh?"

        red @happy "I mean, I can't {i}promise{/i}, but I'll do my best."

        wally @sweat talking2mouth "Okay. I, um... I think there's a special Pokémon hidden somewhere in this school."

        pause 1.0

        red @sweat surprisedbrow talking2mouth "...Oh."

        wally @closedbrow talking2mouth "Yes. I think it's probably a Psychic-type. And it's not matching any descriptions of any Pokémon I've heard of before."
        wally @sadbrow talkingmouth "I know it's silly, but... I kinda have this crazy idea it might be a Mythical?"
        wally @sad2eyes sadeyebrows talkingmouth "I know, I know, it's ridiculous. But... if there's even a chance that I can put myself in the right place, at the right time, to find this Mythical Pokémon..."
        wally @sadbrow talking2mouth "I have to try, you know? If I could just find a {i}single{/i} Mythical Pokémon, that would prove[ellipses]"

        pause 1.0

        wally sadbrow frownmouth @closedbrow talking2mouth "Well, I'd at least have a pretty good shot at landing that Birch internship."

        red @closedbrow talking2mouth "Uh,{w=0.5} wow,{w=0.5} okay,{w=0.5} that's,{w=0.5} um,{w=0.5} yeah,{w=0.5} you,{w=0.5} huh."

        wally @sad2eyes talking2mouth "I knew it. You think I'm crazy. Or... stupid."

        red @closedbrow talking2mouth "N-no, no, it's, uh, it's definitely not that."

        wally @surprisedbrow frownmouth "Hm?"
        wally -sadbrow -frownmouth @talking2mouth "So, you... um. You think there might actually be a Mythical Pokémon in this school?"

        red @sadbrow sweat talkingmouth "Anything's possible in Kobukan!"

        pause 0.5

        wally unamusedmouth unamusedbrow "[ellipses]"

        wally @closedbrow talking2mouth "That's a very noncommittal answer."

        red @closedbrow sweat talking2mouth "Sorry. I'm just not really sure I can contribute much to this kind of conversation."

        wally "[ellipses]"

        wally @angrybrow talking2mouth "You know something."

        red @surprisedbrow frownmouth "Hm?!"

        wally @talking2mouth "I know you--{w=0.5}okay, well, I don't {i}actually{/i} know you, mostly, but I think I know enough about you to be pretty sure of this."
        wally @talking2mouth "You're always so confident. You talk, and even if you don't know {i}exactly{/i} what you're talking about, you sound confident enough that I believe it."

        pause 1.0

        wally @talking2mouth "So, if you're just saying 'nothing,' here... then that must mean..."

        pause 2.0

        wally @sweat closedbrow talking2mouth "That there's a good reason for you not to tell me."
        wally -unamusedbrow -unamusedmouth @sadbrow talkingmouth "Alright. I'll drop it. Won't look into this anymore."

        $ ValueChange("Wally", 3)

        wally @happy "Sorry if I worried you for a moment!"

        red @talking2mouth "No, no, it's fine. Um..."
        red @wince talking2mouth "Okay, I realize I should just leave this be, while you're doing exactly what I want you to, but are you sure you want to drop this that easily? I mean, I didn't even ask you to stop."

        wally @sadbrow talkingmouth "You don't have to. I can tell this is important, and if I end up hurting someone else by looking into this, I should just stop."
        wally @sad2eyes talking2mouth "I {i}will{/i} wonder, but... maybe you can tell me one day, if you ever can."

        red @sadbrow talkingmouth "Sure. Thanks a bunch, man."

        wally @happy "Anytime, [wally_name]!"

        pause 1.5

        red @talking2mouth "Um, sorry, I gotta ask--why did you think a mythical Pokémon was in this school?"

        wally @talking2mouth "Oh... just a bunch of pieces of circumstantial evidence. Nothing concrete. I was hoping to build them up into something bigger, but I was missing something that would tie this last piece of evidence into my theory."

        red @talkingmouth "What kind of evidence?"

        wally @talkingmouth "Um, a few things. Apparently, people in the school have felt, like, the tips of wings brushing the tops of their heads. A few people have mentioned bumping into something invisible for half a second."
        wally @surprised "Oh! One person reported that some sort of big Pokémon broke into the kitchen and stole a bunch of the synthesized Arrokuda!"
        wally @closedbrow sweat talking2mouth "I'm thinking that there's probably some sort of big, Flying-type bird Pokémon that can turn invisible in the school." 
        wally @confusedeyebrows talking2mouth "I'm not sure how it's avoided being detected yet, though. There are a bunch of places only a student can get into."
        wally @sadbrow talkingmouth "That's why I think it's a Psychic-type. Maybe it's some trainer's Pokémon? Maybe someone else knows about this, but is hiding it?"
        wally @talking2mouth "The one thing that's kinda confusing me just doesn't fit into that idea, though."

        redmind @wince "Yep... that's Tia."

        pause 1.0

        red @talking2mouth "What was that {i}last{/i} piece of evidence you mentioned?"

        wally @closedbrow talking2mouth "Right, I'm sorry, I feel like it's probably not even worth mentioning. But..."
        wally @closedbrow sweat talking2mouth "Uh... some students have been reporting they've been seeing Will-O-Wisps floating around the school."

        red @confused "Huh?"

        wally @confused "I know, it's confusing, right? That means it should be a Ghost-type, or maybe a Fire-type. But there aren't many Psychic-types that know that move."

        red @closedbrow talking2mouth "Hold on. What kind of Will-O-Wisps?"
        red @closedbrow talking2mouth "I mean, that's a pretty specific thing to call them."

        wally @talking2mouth "Hm... just, like, big, floating, glowing balls. Like, blue flames, pink flames, I guess. I haven't seen them myself."

        red @confused "That's... not at all what I expected to hear. Yeah, I have {i}no{/i} idea what that could be about."

        wally @happy sweat "Right?"

        wally @closedbrow talking2mouth "I... guess I don't need this anymore, so maybe you should take it. Maybe my notes would be helpful in finding this mythical!"

        red @sadbrow talkingmouth "Sure."

        redmind @thonk "I'm not sure how useful these notes will be in finding Tia. I mean, I already know where she is. But I {i}do{/i} wonder about these so-called Will-O-Wisps."

        $ GetItem("Mirage Research #4", 1)

        red @talkingmouth "Thanks." 
        red @sadbrow talkingmouth "And, uh, good luck on... everything else."

        wally @talkingmouth "You too. Get back to your dorm safely!"

        return

label raihannightscene:
    if (EventAvailable("Raihan", "NightScene")):
        scene blank2 with splitfade

        stop music fadeout 1.5
        
        queue music "audio/music/brandnewworld_start.ogg" fadein 1.5
        queue music "audio/music/brandnewworld_loop.ogg"

        narrator "While walking back to your dorm..."

        scene library2 night
        show raihan angrybrow frownmouth
        with splitfade

        redmind @thonk "Hm? What's Raihan doing in the library so late? He knows curfew's in a few minutes, right?"

        show raihan -angrybrow -frownmouth with dis

        red @talking2mouth "Hey, Raihan. What's up?"

        raihan @talkingmouth "Hey, [first_name]! Good seeing you, mate."

        red @talking2mouth "It's pretty late. Still hitting the books?"

        raihan @closedbrow talking2mouth "Nah, yeah. Well, yeah, but 'nah' in the sense I don't want anyone knowing I'm studying late."
        raihan @happy "Got a reputation to maintain, after all."

        red @talking2mouth "What're you looking up?"

        narrator "Looking past Raihan's very broad shoulder, you notice a stack of books on topics you wouldn't generally expect Raihan to be overly interested in."

        redmind @thonk "Electrical engineering? Rotom care?"

        raihan @talking2mouth "Got this odd problem with my Rotom here. Picking up some sort of signal I can't make heads nor tails of."
        raihan @closedbrow talking2mouth "Now, I'm not a Rotom trainer, by any stretch of the imagination, but I'm fairly certain I can reckon when my Rotom's doing something it really ought not to."

        red @talking2mouth "Oh, you're talking about your Rotom phone, right?"

        raihan @talking2mouth "That's it, yeah. Li'l guy is actin' up recently. Saying stuff that I can't make heads or tails of. Weird clips of... messages, kinda?"
        raihan @closedbrow talking2mouth "Honestly, reminds me of some of the stuff I say whenever I write up posts for RotoPhotos."

        red @confused "What do you mean? Like, what kinds of stuff is it saying?"

        raihan @sadmouth "Stuff like thanking people who don't exist, greeting newcomers I've never heard of, saying that it's going offline, even when it isn't."

        red @confused "That's weird. I know that Rotom can communicate through phones made for them, but... it's just saying nonsense?"

        raihan @sadmouth "Yeah, never had this issue before. Wish I could just talk to him, flat out, and hash this out. Unfortunately, he's saying that he doesn't know what I'm talking about."
        raihan @surprisedbrow talkingmouth "Hold on..."
        raihan @surprised "Can Rotom develop dementia?!"

        red @wince talking2mouth "Not to my knowledge..."

        raihan @closedbrow sadmouth "Well, that idea's nothing, then. Guess I'm full stumped."
        raihan @talking2mouth "If it's not that my Rotom's getting a bit long in the tooth, then I don't know what else it could be. Maybe my phone's old? I mean, it's not, I bought it a couple months ago, but..."

        if (starter_id == 479):
            red @closedbrow talking2mouth "Well... my starter Pokémon at Kobukan is a Rotom. So, maybe, I have an idea of what's going on?"
        else:
            red @sweat sadbrow talkingmouth "Well... I'm not an expert on Rotom, by any stretch of the imagination, but I know a bit about them. I might have a {i}little{/i} bit of an idea of what's going on?"

        raihan @talking2mouth "Right, then, share what you've got."

        red @closedbrow talking2mouth "So, Rotom is a Ghost and Electric-type, right?"
        
        red @talkingmouth "But when Rotom possesses something with a motor, like a microwave, a lawnmower, or a specially-made Rotom phone, it loses that ghostly aspect of itself, taking on the attributes of whatever it's possessing."

        raihan @talkingmouth "Sure. A real 'Ghost in the Machine' kinda Pokémon." 
        raihan @talking2mouth "When they possess a special phone, made right for Rotom, they can make the phone pull off some cracking stunts." 
        raihan @talkingmouth "Paldean models can even fly. Best part for me is that you can place calls from pretty much anywhere, even if you don't have data coverage."
        raihan @happy "Saves a parcel on data plans, and practically mandatory if you're going overseas. Just a damn shame they burn out after a year or two."
        raihan @sad "But, being real about it, normal phones are in such a bad way nowadays that they die almost as fast."

        red @happy "I wouldn't know. My old phone is still ticking, after eight full years!"

        raihan @happy "Ah, Kanto-made phones. Silph, probably?"

        red @talkingmouth "Yep."

        raihan @sadbrow talkingmouth "They don't make them like that anymore. I'd love to get my hands on a genuine 1996 Silphone. I'd pay a parcel for it, too."

        red @confused "Um, I--"

        raihan @closedbrow talkingmouth "Ah, sorry, 'lightly used'. Should've put that on the billing. It's for collecting purposes."

        red @sweat closedbrow talking2mouth "Worth a shot."
        red @talking2mouth "Anyway, about your Rotom, maybe it's picking up some sort of ghostly signal it shouldn't?"
        red @talking2mouth "Rotom doesn't stop being a Ghost-type, at heart, even when it's possessing something."
        red @closedbrow sweat talking2mouth "Since Rotom's a Ghost-type, maybe it's receiving some kind of ghostly transmission, like the antenna on the top of Dusknoir's head gets."

        raihan @closedbrow talking2mouth "Maybe. Like that EVP thing, yeah?"

        red @confused "Hm? Electric Voice Phenomena?"

        raihan @talkingmouth "That's the one."

        red @talking2mouth "Well, yeah, I guess it could be that. I was just thinking, since Rotom Phones are really good at receiving signals, maybe it's picking up some ghostly ones, in addition to, you know, phone calls."

        raihan @closedbrow talking2mouth "Maybe."
        raihan @sad "But... I don't reckon I have any idea what the kinds of stuff it's saying would be, if they really are coming from ghosts. Do the ghosts really care about the kind of stuff my Rotom's talking about?"

        red @sadbrow talkingmouth "Hard to say. I've never talked to one myself."

        raihan @happy "Hah! Fairly said. I don't think I have either, though there was one codger in my Gym who'd been there since before Mustard, and I figured he might be a ghost."

        pause 1.0

        raihan @sad "Actually, come to think of it, that {i}would{/i} explain how he kept getting into the Gym after we asked him to retire."
        raihan sad "Huh. Might need to look into the Galarian league's policy on hiring undead. Not sure I gave him the right level of accommodations for that."

        hide raihan with Dissolve(2.0)

        narrator "Raihan wanders off, deep in thought, seemingly very concerned he may have inadvertently treated the ghost he employed unfairly."

        $ ValueChange("Raihan", 3)

        return

label melodynightscene:
    if (IsAfter(28, 5, 2004) and IsNamed("Melody") and not HasEvent("Melody", "NightScene")):
        $ AddEvent("Melody", "NightScene")
        scene blank2 with splitfade

        stop music fadeout 1.5

        $ renpy.music.queue("audio/music/Eterna_Start.ogg", channel='music', loop=False, fadein=1.5, tight=None)
        $ renpy.music.queue("audio/music/Eterna_Loop.ogg", channel='music', loop=True)

        narrator "While walking back to your dorm..."

        scene concerthallnight 
        show melody noglasses at night
        with splitfade

        redmind night @surprisedbrow frownmouth "Oh, crap. It's Melody."
        redmind @sad2eyes frownmouth sadeyebrows "Okay, I just need to walk past, and she won't notice me, right?"

        pause 2.0

        melody @talking2mouth "Hey."

        redmind @sweat frownmouth closedbrow "I tempted the universe."

        red @wince talking2mouth "Hi, Melody. It's pretty late. Shouldn't we get to our dorms?"

        melody @talking2mouth "Yeah, that's the problem. Pretty girl out here, all alone, late at night. Aren't you going to be a gentleman and walk me back?"

        red @unamusedbrow talking2mouth "I really don't think that you need my protection. You were a student here last year."

        melody @talking2mouth "Right. And you kicked my ass. And everyone has, like, way higher levels than last year, because I guess the cafeteria staff is just grinding up Rare Candy and putting it in the food now."

        pause 1.0

        red @talking2mouth "That seems to have really bothered you, when we battled."

        melody @talking2mouth "Yep."

        pause 2.0

        melody @closedbrow talking2mouth "Nevermind, I don't want you to walk me back. I'm just going to stay out here tonight."

        red @closedbrow talking2mouth "...Here? All night?"

        melody @talking2mouth "Infer."

        pause 1.0

        red @upeyes angryeyebrows talking2mouth "Curfew is in, like, ten minutes."

        melody @talking2mouth "Oh no. Now the Disciplinary Committee will yell at me."
        melody @sadbrow talking2mouth "Seriously, have you been paying attention at all?"

        red @sad2eyes angryeyebrows talking2mouth "To {i}some{/i} things. Important things."

        melody @sadbrow talking2mouth "Oh no, my feelings. {w=0.5}{nw}"
        extend @talking2mouth "Anyway, you should probably get out of here before someone sees us and thinks that I know your name."

        red @upeyes talking2mouth "You {i}do.{/i}"

        if (melody_name == first_name):
            if (first_name not in ["Jon", "John", "Jonny", "Johnny", "Jonathon", "Jonathan", "Johnathon", "Johnathan"]):
                $ melody_name = "John" 
            else:
                $ melody_name = "Steve" 

        melody @talking2mouth "Do I, [melody_name]?"

        red @upeyes angryeyebrows frownmouth "[ellipses]"

        red @talking2mouth "I'm not rising to the bait."

        melody @talking2mouth "Boo."

        pause 2.0

        red @sad2eyes angryeyebrows talking2mouth "Ugh. I know I should just leave, but I'm curious. Why are you staying out here all night? It's cold."

        melody @surprised "Uh, it's [calendar.month_name[calDate.month]]."

        red @talking2mouth "Fine. I'm leaving."

        hide melody with dis

        pause 2.0

        $ showredonly = True

        melody "{size=30}...singing.{/size}"

        red @upeyes angryeyebrows frownmouth "[ellipses]"

        show melody noglasses at night with dis 

        red @confused "What?"

        $ showredonly = False

        melody @talking2mouth "Singing. The Contest Hall is haunted. And, sometimes, the ghosts sing."
        melody @talking2mouth "I like to join in."

        pause 1.0

        red @unamusedbrow talking2mouth "You didn't need to lie to me {i}that{/i} hard."

        melody @talking2mouth "Whatever."
        melody @closedbrow talking2mouth "You'll know I'm right by the end of the year, assuming you make it that long."

        pause 1.0

        melody @talking2mouth "This school has a lot of ghosts. I hope you run into the ones who were victims. The other ones suck. And there's nothing you can do about them."
        melody @talking2mouth "You can't touch a ghost, you know."

        hide melody with Dissolve(4.0)

        narrator "Melody steps into the shadows of the contest hall, seemingly fading away into the very darkness itself. She no longer seems interested in conversation."

        pause 1.0

        red @closedbrow sweat talking2mouth "Brr. All this talk of ghosts is giving me the creeps. I should get back to my dorm before the DC sees me."

        return

label krisnightscene:
    if (IsAfter(21, 5, 2004) and EventAvailable("Professor Cherry", "NightScene")):
        scene blank2 with splitfade

        stop music fadeout 1.5

        queue music "audio/music/celebi_start.ogg" noloop
        queue music "audio/music/celebi_loop.ogg"

        narrator "While walking back to your dorm..."

        scene garden night
        show kris surprisedbrow frownmouth at night
        with splitfade

        kris @talking2mouth "[first_name]? What are you--"
        kris @sadbrow frownmouth "[ellipses]"
        kris -surprisedbrow -frownmouth @sadbrow talkingmouth "You know you shouldn't be out this late. I'll just say I didn't see you, if you scuttle back to your dorm, okay?"

        red night @talkingmouth "Thanks, but I've got a couple more minutes. I can run back to the dorm. No need to say anything."

        kris @surprisedbrow talking2mouth "Oh? Is it actually...?"

        pause 1.0

        kris @happy "Oh, wow. It's {i}way{/i} earlier than I thought it was."
        kris @happy "Gosh, I'm {i}so{/i} terrible at keeping track of time. It always gets away from me."#THIS IS THE CLEVEREST FUCKING PUN, PRAISE ME IN ~6 MONTHS WHEN IT MAKES SENSE

        red @talkingmouth "It's alright. But what are you doing?"

        kris @talking2mouth "Oh, I just... I heard rumors that some students have seen flickering, bright images around the school. Silhouettes of a person wearing long robes..."

        red @surprisedbrow frownmouth "[ellipses]"
        red @talking2mouth "Woah. Really? What do you think it is? Some kind of Pokémon illusion?"

        kris @surprisedbrow talking2mouth "Hm? A Pokémon that makes illusions? No, definitely not. There's nothing like that at this school."

        red @unamusedbrow frownmouth "[ellipses]"

        redmind @thinking sweat "Okay, I'm pretty sure that Kris knows about Tia. But if she's trying to keep it a secret, too, I guess there's no reason to press the issue."

        pause 1.5

        redmind @smirkmouth unamusedbrow "On the other hand... it could be fun to tease a Professor a little bit."

        red @talkingmouth "Well, if it's not illusions from a Pokémon, what do you think it could be?"

        kris @sadbrow talking2mouth "Oh... I don't know. I have a few things I hoped for."
        kris @closedbrow talking2mouth "Could be a powerful Ghost-type's aura manifesting, or perhaps a Mismagius' cry."
        kris @sadbrow talking2mouth "Or... temporal fractures. That was the least likely one, though."

        red @confused "Come again? Temporal fractures? I think I missed that lesson."

        kris @talking2mouth sadbrow "No, they don't teach about that sort of thing in Kobukan. It's not really relevant."
        kris @angrybrow talkingmouth "But I can give an impromptu lecture, if you'd like!"

        red @happy "Sure, but it can't go for too long Doctor. Curfew, remember!"

        kris @happy "Of course. I'll make it short."
        kris @closedbrow talking2mouth "{i}*Ahem.*{/i}"
        kris @talkingmouth "Temporal fractures are areas, people, or Pokémon that exist in multiple 'places' in time at once."
        kris @talking2mouth "The settlers to Hisui--Sinnoh, now--referenced them as a frequent occurrence. They called them 'Dimensional Rifts', which we now recognize as a collection of several Temporal Fractures in a small area." 
        kris @talkingmouth "Given the relative unsettledness of the land, they're strongly associated with Mysteriosity, which is equally, seemingly, repelled, by urbanization." 
        kris @sadbrow talking2mouth "And humans in general."
        kris @talkingmouth "We definitely don't get any reports from Sinnoh about them appearing in the quantities they did back then, in any case."

        pause 1.0

        kris @talkingmouth "When a person appears as a Temporal Fracture, they're often described as a glowing silhouette that fades in and out with increasing frequency over a period of anything from minutes to centuries."
        kris @talking2mouth "These silhouettes appear more and more frequently, until eventually the person themselves appears in the place their 'silhouette' was manifesting."
        kris surprisedbrow @neutralbrow talking2mouth "This phenomenon is {i}very{/i} similar to the Ultra Wormholes of Alola, and the 'Fallers' that come from there. But Temporal Fractures don't travel through space. Only time. And only through one universe, which..."

        pause 2.0

        kris -surprisedbrow @happy "Oh, I'm sorry. It's way too early to be dropping multiverse theory on you!"

        red @sadbrow talkingmouth "With the greatest amount of respect, thank you for sparing me. I could already feel my brain starting to melt after the fourth definition of 'time' you dropped."

        kris @talking2mouth "Ah, I got a bit carried away. At least we still have plenty of time before--"

        show garden night 
        show kris surprised
        with vpunch

        kris @surprised "AH! Curfew was five minutes ago!"

        red @closedbrow talking2mouth "Ah, crap."

        pause 1.0

        red @confused "Wait, why are you worried?"

        kris sadbrow frownmouth @talking2mouth "That means I had a staff meeting {i}fifteen{/i} minutes ago!"

        red @wince talking2mouth "Oof, sorry. Guess I distracted you."

        kris @sadbrow talkingmouth "It's fine. Just... um..."

        red @sadbrow talkingmouth "Run?"

        kris sadbrow talkingmouth "Please!"

        show kris:
            xpos 0.5
            ease 1.0 xpos 0.35
            ease 0.2 xpos 1.2

        narrator "Your mutual terror forges the bonds of understanding between the two of you!"

        $ ValueChange("Professor Cherry", 5)

        return

label cherennightscene:
    if (HasEvent("Wally", "NightScene") and HasEvent("Raihan", "NightScene") and HasEvent("Melody", "NightScene") and HasEvent("Professor Cherry", "NightScene") and IsPresent(["Silver", "Skyla", "Cheren", "Gardenia"]) and GetCharacterLevel("Cheren") >= 3 and EventAvailable("Cheren", "Cheren2", 1)):
        call Cheren2() from _call_Cheren2

        return

label natenightscene2:
    if (IsAfter(26, 5, 2004) and EventAvailable("Nate", "NightScene2", 1)):
        $ AddEvent("Nate", "NightScene2")

        scene blank2 with splitfade

        stop music fadeout 1.5

        queue music "audio/music/nuvema2_start.ogg" noloop
        queue music "audio/music/nuvema2_loop.ogg"

        narrator "On the way back to the dorm..."

        scene garden night
        show nate frownmouth sadbrow at night
        with splitfade

        pause 2.0

        show nate surprisedbrow frownmouth with dis

        red night @talking2mouth "Huh? Nate? What're you doing here? Curfew's in a couple minutes."

        nate @talking2mouth "Oh, hey, [nate_name]."

        pause 0.5

        nate -surprisedbrow @closedbrow talking2mouth "Just thinking, I guess."

        pause 1.0

        nate @sad2eyes talking2mouth "It hasn't been that long since Bianca's father was[ellipses] you know."

        red @sadbrow talking2mouth "Oh. Yeah."

        nate @sadbrow talkingmouth "But everyone's stopped talking about it. They've stopped {i}thinking{/i} about it."

        pause 1.5

        nate @sad2eyes talking2mouth "That's good. Because, you know, if you think {i}too{/i} hard about that kind of thing, then[ellipses]"
        nate @sadbrow talkingmouth "You go crazy, [first_name]. You can't stop thinking about it."
        nate @sad2brow talking2mouth "It's for the best that we have a world that can move on from these kinds of things."

        pause 1.0

        nate @sad2brow talking2mouth "But where does that leave the victims? Where does that leave Bianca? How's she supposed to live in the world I'll make tomorrow, where no-one can even understand what happened to her?"

        red @talking2mouth "'A world where people forget they have fists.'"

        nate @talking2mouth "That's the dream.{w=0.5} That's the mission."

        pause 1.0

        nate @talking2mouth "At least[ellipses] at least {i}we're{/i} there for Bianca."

        red @sadbrow talkingmouth "Sometimes all it takes is one person. She's got more than that."

        nate @talkingmouth closedbrow "Yeah."

        pause 1.0

        red @sadbrow talkingmouth "You're not going back to your dorm, are you?"

        nate @sad2brow talking2mouth "There's been some criminal activity in Inspira I should probably check out. An international fugitive we've chased across a couple regions."

        red @sadbrow talking2mouth "Not related to {i}our{/i} thing?"

        nate @sadbrow talkingmouth "No, a different thing that threatens peace as we know it, and could end the happy lives of billions."
        nate surprisedbrow frownmouth @sad2eyes sadeyebrows talkingmouth "{size=30}It never ends. It just {i}never{/i} ends.{/size}"

        red @talking2mouth "Maybe it won't. But... I grew up peacefully."

        red @sadbrow talkingmouth "So, y'know, that's one person who didn't know about {i}any{/i} of this for the entire time he was a kid."
        red @wince talking2mouth "Maybe I still learned {i}eventually{/i}, but[ellipses]"
        red @sadbrow talkingmouth "I guess you're probably doing a better job than not?"

        pause 1.0

        $ ValueChange("Nate", 3)

        nate sadbrow frownmouth @talkingmouth "Maybe I {i}can{/i} defend another night, then."

        pause 2.0

        red @confused "Hey, do you sleep?"

        nate @talking2mouth "Rarely."
        nate @closedbrow talking2mouth "Agency's got a special kind of pill that removes the ability to feel tiredness."
        nate @talking2mouth closedbrow sweat "After about three days, whether I feel tired or not, I usually drop, but I've got those 'drops' on a cycle."

        red @talking2mouth "Wait, you mean you can stay awake for almost 72 hours? And you feel completely fine?!"
        red @happy "That pill's amazing! Why is it kept a secret?"

        nate unamusedbrow @talkingmouth "Imagine your boss knows you can stay awake for seventy-two hours."

        red @talking2mouth "I immediately see what you mean, and this must {i}never{/i} get out."

        nate -unamusedbrow -frownmouth @closedbrow talkingmouth "Hah. Sleep well, [nate_name]. I've got a world to make."

        red @happy "Stay safe."

        call clearscreens() from _call_clearscreens_271
        scene blank2 with splitfade

        pause 2.0

        scene garden night
        show anabel at night
        with splitfade

        pause 1.0

        anabel @talking2mouth "Reporting in."
        anabel sadbrow @talking2mouth "Black No. 2 is[ellipses]"

        pause 0.5

        anabel -sadbrow @closedbrow talking2mouth "Black No. 2 is operating within assigned parameters. Will continue to monitor."

        pause 0.5

        anabel angrybrow frownmouth @talking2mouth "Out."

        scene blank2 with splitfade

        return

label IonoRosaSabrinaNightScene:
    if (GetEventDatetime("Iono", "Iono1") != calDate and EventAvailable(["Iono", "Rosa", "Sabrina"], "RosaSabrinaNightScene", [1, 0, 0])):
        scene blank2 with splitfade

        stop music fadeout 1.5

        queue music "audio/music/lavender_start.ogg" noloop
        queue music "audio/music/lavender_loop.ogg"

        scene garden night
        show iono frownmouth sadbrow at night
        with splitfade

        iono @sadbrow talking2mouth "Brr[ellipses] it's chilly out here[ellipses]"
        iono @talking2mouth "I need to get back to my bunker, quickly[ellipses] where it's nice and safe[ellipses] nice and dark[ellipses]"

        TempCharacter("{color=#ff5a73}???{/color}") "Excuse me!"

        iono @surprisedbrow talking2mouth "Gah!"
        iono angrybrow frownmouth @angrybrow talking2mouth "Back off, antifriendos! I've got mad battling skills! No-one's getting my bathwater without paying top dollar for it!"

        show sabrina at night with dis:
            xpos 0.75

        show rosa at night with dis:
            xpos 0.25 xzoom -1

        stop music fadeout 1.5

        queue music "audio/music/joinavenue_start.ogg" noloop
        queue music "audio/music/joinavenue_loop.ogg"

        rosa @surprisedbrow talking2mouth "Wait[ellipses] you {i}are{/i}! Sabrina and I saw you in class, but I couldn't be sure--it's actually you, Iono!"

        iono neutralbrow smilemouth @neutralbrow talkingmouth "Wait, you're[ellipses] Rosa? {i}Rosa?!{/i}"

        rosa @happy "Oh my {i}gosh{/i}, Iono, it is {i}so{/i} good to see you again. Remember {i}Everlasting Memories?{/i}"

        iono @happy "Of course! I was the cutest, most marketable little robot anyone ever saw. F-00."
        iono @sadbrow talking2mouth "I was really sad when they killed him..."
        iono @talking2mouth "But it made sense for his character, at least."

        pause 1.0

        show iono surprisedbrow behind sabrina with dis

        rosa @closedbrow talking2mouth sweat "They, um, brought him back for every sequel. And killed him off in every sequel, too."

        iono @angrybrow talking2mouth "What?! How dare they! Narrative integrity aside, they didn't even {i}ask{/i} me if I wanted to reprise my role!"
        iono @rolleyes talking2mouth "And I totally would've, too, because screw narrative integrity, I made {i}bank{/i} from that movie."

        rosa @closedbrow talkingmouth "I think Director Deeoh mentioned you were... 'difficult to work with.'"

        iono angrybrow poutmouth @angrybrow poutmouth "Hmph! He'll be sorry for that."

        rosa @happy "It's great to see you, though, Iono. We {i}need{/i} to catch up. Let's sit together in Electric class tomorrow! I've got {i}so{/i} much to ask you."

        iono @talking2mouth "Oh! R-really? You want to put me in your party? You're recruiting {i}me{/i}?"

        rosa @talkingmouth "Well[ellipses] sure. It's been a long time since we talked, right? I bet you want to catch up, too."

        iono @talking2mouth "Y-yeah."

        pause 1.0

        iono @talkingmouth "Yeah! Yeah, I'd love to! Talking with my normal student friend like a normal student would! Yeah, let's do it! Mission a-chat-chat is a-go-go!"

        pause 1.0

        show iono:
            xpos 0.5
            ease 0.5 xpos 0.4

        iono @disgustedbrow disgustedmouth "So what's the skinny on My Chemical Romance over there?"

        rosa @talkingmouth "Oh, that's Sabrina. She's normally much more talkative. Um, Sabrina, is something up?"

        pause 1.0

        sabrina @sadeyes talking2mouth "Why[ellipses] why can't I {i}hear{/i} you?"

        pause 1.0

        iono @talking2mouth "Iunno. Do you need me to {i}project?!{/i}{w=1.0} {size=40}I can {i}project{/i} my voice!{/size}"

        show rosa sweat closedbrow frownmouth
        show sabrina sadeyes judgingeyebrows
        with dis

        iono angrybrow happymouth '{size=50}IS THIS BETTER?! CAN YOU HEAR ME {i}NOW{/i}?! I AM {i}PROJECTING{/i} MYSELF!!!{/size}'

        scene blank2 with splitfade

        return

return