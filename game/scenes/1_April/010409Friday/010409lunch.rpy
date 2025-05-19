label lunch010409:

############################################################################################################################################################################################################################
#### 2. LUNCH SCENE ########################################################################################################################################################################################################
############################################################################################################################################################################################################################



queue music "Audio/Music/Road to Viridian City.ogg"

scene cafe with splitfade

$ renpy.transition(dissolve)
show screen currentdate

$ renpy.pause(0.5, hard=True)

hide afternoon

show brendan uniform:
    xpos 1.0/7.0 xzoom -1
show may uniform:
    xpos 2.0/7.0
show ethan uniform:
    xpos 3.0/7.0
show leaf uniform:
    xpos 4.0/7.0
show serena uniform:
    xpos 5.0/7.0 xzoom -1
show calem uniform:
    xpos 6.0/7.0 xzoom -1
with dis

brendan @surprised "Phew, I'm beat!{w=0.5} I know I used to complain a lot about Littleroot High, but I kinda miss it now."

may @happy "That was high school, Brendan.{w=0.5} Things are meant to be a little harder in university."

ethan @sad "This is {i}way{/i} more than just a 'little harder.' This is like jumping from the kiddie pool into the middle of the ocean."

leaf @talking2mouth "So, how're classes treating you, [first_name]?{w=0.6}{nw}"

extend @flirttalk " Ready to crack yet?"

menu:
    "It's all right.":
        red uniform @talkingmouth "I think I'm managing all right.{w=0.5} It's a little tougher than high school, but that's just something to be expected."
        
        leaf @flirtbrow talkingmouth "...That was so cliché. Spoken like a real square."
        
        red @sadeyes sadeyebrows talkingmouth "Come on, I'm just telling you what I think.{w=0.5} You can't possibly rag on me for that."
        
        leaf @happybrow talking2mouth "I can, and I will.{w=0.5} Everyone has opinions, [first_name], but some are more fun to listen to than others!"
        
        red @closedbrow talking2mouth "...Geez."

    "I can't take it anymore!":            
        show brendan surprisedbrow frownmouth
        show ethan surprisedbrow frownmouth
        show calem surprisedbrow
        show may surprisedbrow frownmouth
        show leaf surprisedbrow frownmouth
        show serena surprisedbrow frownmouth
        with dis

        red uniform @sad "It's torture, I tell you!{w=0.5} I swear, making us battle {i}every{/i} day?! We haven't even had the chance to get any new Pokémon yet! We've had barely any time to train our 'mons!" 
        red @angry "There are some fights I just can't win! And besides that... what the hell's up with those battle quizzes?! My brain hurts just remembering them, never mind doing them!"
        
        pause 2.0

        show brendan happy
        show ethan happy
        show calem -surprisedbrow -frownmouth
        show may -surprisedbrow -frownmouth
        show leaf -surprisedbrow -frownmouth
        show serena -surprisedbrow -frownmouth
        with dis
        
        $ ValueChange("Brendan", 1, 1.0/7.0, False)
        $ ValueChange("Ethan", 1, 3.0/7.0)

        brendan "Man, {i}preach!{/i}"
        
        leaf @talking2mouth "Uh, aren't you being just a little melodramatic?"
        
        ethan "You just don't get it, Lozenge.{w=0.5} Some of us weren't gifted with smarts like you."

        leaf @angry "(Lozenge?!)"
        
        brendan @sad "You'll never understand us dumb people!"

        ethan "Yeah! We're the three idiots!{w=0.5} All for one and one for all!"
        
        narrator "You and the other two idiots high five each other."

        show brendan -happy
        show ethan -happy
        with dis
        
        leaf @closedbrow talking2mouth "You three are a real piece of work."
        
    ">Flatter Leaf to dodge the question":            
        show leaf surprisedbrow
        with dis
        
        red uniform @talkingmouth "What about you, Leaf? You seem smart.{w=0.5} I bet classes are no problem for someone like you."

        $ ValueChange("Leaf", 1, 4.0/7.0)
        
        leaf @talkingmouth "Aw, I had no idea you thought of me like that!{w=0.5}{nw}"
        
        extend -surprisedbrow @happy " You really think so?"
        
        brendan @angrybrow talking2mouth "Hey! You can't just dish out compliments like that!{w=0.5} That's just...{w=0.25} weird!{w=0.25} You're weird, man!"

        may @sadbrow happymouth "I wouldn't mind if you did that to me every once in a while."

        brendan @surprised "Really?{w=0.5}{nw}"
        extend @closedbrow talking2mouth " Then...{w=0.25} I guess it's fine."
        
        serena @sadbrow happymouth "Ah... Brendan, you can be a bit clueless, can't you?"

        calem @closedbrow talking2mouth "So... did anyone actually catch how [first_name] felt about his classes, or...?"
        
    "This school is too easy for a genius like me!" if GetGrade() >= 1:
        show brendan surprisedbrow frownmouth
        show ethan surprisedbrow frownmouth
        show calem surprisedbrow
        show may surprisedbrow frownmouth
        show leaf surprisedbrow frownmouth
        show serena surprisedbrow frownmouth
        with dis
        
        red uniform @talkingmouth "Pfft! What, are you kidding me?{w=0.5} Come on, the last person I battled had a Trubbish. A {i}Trubbish{/i}." 
        red @happy "And the battle quizzes? Someone who's never seen a Pokémon before could do those!"

        may @surprised "Wow, [first_name]! I had no idea you were that smart!"
        leaf @surprisedbrow talkingmouth "You're serious?"

        calem -surprisedbrow -frownmouth -surprised @closedbrow talkingmouth "Oh, yes, he's quite serious. I can vouch for him. His ability to memorize is impressive."
        calem @surprisedbrow talkingmouth "I've seen him diligently studying, too. His own motivation, in no small part, motivates me."

        show brendan -surprisedbrow -frownmouth
        show ethan -surprisedbrow -frownmouth
        show may -surprisedbrow -frownmouth
        show leaf -surprisedbrow -frownmouth
        with dis

        serena -surprisedbrow -frownmouth -surprised @surprisedbrow talkingmouth "Oh! [first_name], I did not realize that you were so studious. I'm quite glad."
        leaf @talkingmouth "Wow, I'm impressed.{w=0.5}{nw}"
        extend @flirttalk " I never took you for a bookworm, [first_name]."

        $ ValueChange("Serena", 1, 5.0/7.0, False)
        $ ValueChange("Calem", 1, 6.0/7.0, False)
        $ ValueChange("Leaf", 1, 4.0/7.0)
        
        red @happy "Yeah, well, what can I say?{w=0.5} I just do it all."
        redmind @thinking "Just don't ask me anything that doesn't involve {i}Pokémon{/i}, please."
        
        leaf @flirtbrow talking2mouth "Let's not get too ahead of ourselves, skippy."

pause 1.5

may closedbrow frownmouth "[ellipses]"
may @surprisedbrow sadmouth "Aw, it always gets noisy during this time of day.{w=0.5} Can't a girl unwind in peace?"

serena @talkingmouth "If you wanted to unwind, surely your room would be more comforting...? And quieter?"

may -thinking @sadbrow happymouth "I would, but I don't have time to go all the way there and back in time for class."
may @happy "Besides, there's nothing fun to do in my room.{w=0.5} Hanging out with you guys is way more interesting!"

calem @talkingmouth "We could move somewhere else if it's too loud."

red @happy "Hey, I've got an idea! Serena, Calem, you were there for this. Some other friends mentioned the gardens. Apparently, it's a good spot for a picnic."

pause 2.0

show brendan surprisedbrow frownmouth
show ethan surprisedbrow frownmouth
show calem surprisedbrow
show may surprisedbrow frownmouth
show leaf surprisedbrow frownmouth
show serena surprisedbrow frownmouth
with dis

leaf sad "{cps=15}You... you have other friends?{/cps}"

red @wince talking2mouth "Uh..."

leaf angry "You bastard! You villain! You cur! I thought we had something special--! To take my heart, and shatter it with such cruel abandon... How could you? How dare you?"
leaf @angrybrow angrymouth "Other friends! Really. Really! My-- oh, geez--"
leaf -angry @happy "Ah, sorry, hahaha! I can't keep that up! God, I'm hilarious!"

red @closedbrow talking2mouth "A real knee-slapper you are."

leaf @sarcastic "Okay, but, for real. Who are your other friends?"

$ morefriends = ", "

if (persondex["Gardenia"]["Value"] > 0):
    $ morefriends += "Gardenia, "
if (persondex["Dawn"]["Value"] > 0):
    $ morefriends += "Dawn, "
if (persondex["Misty"]["Value"] > 0):
    $ morefriends += "Misty, "
if (persondex["Skyla"]["Value"] > 0):
    $ morefriends += "Skyla, "

show leaf surprisedbrow frownmouth with dis

red @closedbrow talking2mouth "Hm... well, there's Hilda, Bianca, Hilbert, Whitney, Flannery, Nate[morefriends]and Rosa. Oh, and Silver."

ethan @talking2mouth "Dude. You've been here five days."

brendan @closedbrow talkingmouth "I mean... maybe he's just bein' a bit loose with his definition of friend?"

show brendan -surprisedbrow -frownmouth
show ethan -surprisedbrow -frownmouth
show calem -surprisedbrow
show may -surprisedbrow -frownmouth
show leaf -surprisedbrow -frownmouth
show serena -surprisedbrow -frownmouth
with dis

leaf -surprisedbrow -frownmouth -surprised @happy "Oh, yeah, that's it, duh! I mean, have any of those, like, {i}dozens{/i} of names made an Official Friendship Pact{font=fonts/consola_0.ttf}™{/font}?"

red @closedbrow talking2mouth "...Nnnno?"

leaf @flirttalk "Then they don't count. Not friends, sorry. Those are the rules."

red @closedbrow talking2mouth "Damn. Guess I've never had any friends, ever, then."

leaf @happy "Don't worry! I'll make an Official Friendship Pact{font=fonts/consola_0.ttf}™{/font} with you right now!"

red @sadeyes sadeyebrows talkingmouth "Sorry. I'm saving myself for marriage."

leaf @angrybrow talkingmouth "We'll see about that."

pause 2.0

calem @talkingmouth "Not that this conversation isn't illuminating, but we were heading out to the garden?"

red @surprised "Oh! Right! Yes, of course."

show may at dissolveaway:
    xpos 2.0/7.0
show leaf at dissolveaway:
    xpos 4.0/7.0
show serena at dissolveaway:
    xpos 5.0/7.0
show calem at dissolveaway:
    xpos 6.0/7.0

pause 2.0

show ethan sadbrow frownmouth with dis

ethan @talkingmouth "...Hey, big man?"

brendan @talkingmouth "Huh? Yeah, Ethan?"

ethan @talkingmouth "Do you know how he's doing that?"

brendan @surprisedbrow talkingmouth "Doin' what?"

ethan @talkingmouth "Like... all those people. He makes friends so easily. And we've got a lot in common, y'know? So I should be able to do it, too." 
ethan -frownmouth @talking2mouth "But... I dunno. It kinda feels like he's got something I don't."

brendan @happy "Ethan, you're totally asking the wrong guy. From the moment I saw you two, I wanted to be a friend to {i}both{/i} you guys."

ethan @happy "Aw, thanks, big man."

brendan @thinking "[ellipses]"

brendan @talking2mouth "Are you callin' me 'big man' because you forgot my name?"

ethan @closedbrow talking2mouth "Yes, absolutely. Sorry."

brendan @happy "It's alright, bro! It's Brendan. Remember, Brendan's here for friendin'! Now c'mon, let's go catch up to the others."

hide brendan with dis

pause 2.0

ethan @closedbrow talking2mouth "It can't just be a coincidence, right?"

$ renpy.pause(1.5, hard=True)
    
stop music fadeout 1.0
$ renpy.music.stop(channel='crowd', fadeout=2.0)
$ renpy.transition(dissolve)
call clearscreens from _call_clearscreens_39
    
show blank with splitfade
$ renpy.pause(1.5, hard=True)

$ renpy.music.queue("Audio/Music/Celadon_Start.ogg", channel='music', loop=None, fadein=0.5, tight=None)
$ renpy.music.queue("Audio/Music/Celadon_Loop.ogg", channel='music', loop=True, tight=None)

hide cafe

show clouds behind ethan:
    yalign 0.5
show garden behind ethan:
    zoom 1.25 xalign 0.5 zoom 0.85
    ease 5.0 zoom 0.625

hide leaf
hide may
hide brendan
hide ethan
hide calem
hide serena

$ renpy.transition(dissolve)
show screen currentdate

hide blank with splitfade
$ renpy.pause(5.0, hard=True)

show garden:
    zoom 0.625

show leaf uniform with dis:
    xpos 0
    pause 0.2
    ease 1.25 xpos 4.0/7.0

show serena uniform happy behind leaf with dis:
    xpos 0
    ease 0.5 xpos 3.0/7.0

show ethan uniform happy behind leaf with dis:
    xpos 0
    pause 0.25
    ease 1.0 xpos 1.0/7.0

show brendan uniform behind leaf with dis:
    xpos 0
    pause 0.3
    ease 1.5 xpos 2.0/7.0

show may uniform behind leaf with dis:
    xpos 0
    pause 0.5
    ease 1.25 xpos 5.0/7.0
    
show calem uniform behind leaf with dis:
    xpos 0 xzoom -1
    ease 3.0 xpos 6.0/7.0

$ renpy.pause(0.5, hard=True)
    
serena @talkingmouth "Ah, isn't this refreshing?{w=0.5} There's nothing quite like the great outdoors after being indoors all day."

red @talkingmouth "The great outdoors is right--this is one big garden!{w=0.5} They could fit my whole school from back home in here."
red @happy "It looks like spring is in full swing.{w=0.5} Everything's starting to bloom."
    
serena @talkingmouth "Yes, isn't it lovely?{w=0.5} Calem, doesn't it remind you of Parfum Palace gardens?"

calem @talkingmouth "Rather. {w=0.5}{nw}"
extend @sad "It's like I never left home."

leaf @happy "I heard Kalos is a really beautiful region.{w=0.5} I've always wanted to go there myself someday."

calem @talkingmouth "Well, if you ever find yourself there, you should visit Coumarine City. It has some amazing views."

serena @talkingmouth "You should see some of the paintings that Calem made of them. I have pictures of almost all of them on my phone."

calem @surprised "Ah! That might not be the, er, the best--"

serena @happy "Would you like to see them?"

leaf @happy "Really? That'd be awesome, actually!"

red @talkingmouth "What about you, May?{w=0.5} Is Hoenn anything like Kobukan?"

may @closedbrow talking2mouth "Hmmm...{w=0.5}{nw}"
extend @talkingmouth " in terms of climate, I guess Hoenn's a little warmer around this time of year, but other than that, there's nothing really jumping out at me."

may @sadbrow happymouth "I was hoping to see new Pokémon here, but since Kobukan's so urbanized, there probably aren't a ton of indigenous species here."

leaf @talking2mouth "All right then, let's take advantage of the green Kobukan {i}does{/i} have and find a nice picnic spot!"

brendan @closedbrow talkingmouth "Yeah... about that."

show brendan surprisedbrow frownmouth
show ethan surprisedbrow frownmouth
show calem surprisedbrow frownmouth
show may surprisedbrow frownmouth
show leaf surprisedbrow frownmouth
show serena surprisedbrow frownmouth
with dis

$ renpy.music.play("Audio/school_crowd.ogg", channel='crowd', loop=True, fadein=1.0)
$ renpy.music.set_volume(0.5, delay=1.0, channel="crowd")

pause 1.5

brendan @talking2mouth "Most of the good spots are already taken, from the looks of it."
ethan @angry "Geez, even out here?! Just how many people does this school {i}have?{/i}"

show brendan -surprisedbrow -frownmouth -surprised
show ethan -surprisedbrow -frownmouth -surprised
show calem -surprisedbrow -frownmouth -surprised
show may -surprisedbrow -frownmouth -surprised
show leaf -surprisedbrow -frownmouth -surprised
show serena -surprisedbrow -frownmouth -surprised
with dis

leaf @happybrow talkingmouth "Fwohohoho. There's an easy solution to this."

red @angrybrow talking2mouth "Uh-huh. Sure. What do you propose?"

show leaf at getcloser:
    xpos 4.0/7.0

show garden:
    yalign 0.0
    ease 0.03 ypos -10
    ease 0.03 ypos 10
    ease 0.03 ypos 0
    repeat 3
    
leaf happy "{size=44}All right, I'll give the first person to find a good spot $1,000!{/size}"
leaf @talking2mouth "[first_name], try not to make any new friends while you're--"

$ PlaySound("Whoosh.ogg")

show garden with vpunch

show brendan surprisedbrow frownmouth
show ethan surprisedbrow frownmouth
show calem surprisedbrow frownmouth
show may surprisedbrow frownmouth
show leaf surprisedbrow frownmouth
show serena surprisedbrow frownmouth
with dis

pause 3.0

show leaf at getfurther:
    xpos 4.0/7.0

ethan @talkingmouth "Uh... I think he's going to be the one."

serena @talkingmouth "Yes, the speed at which he ran was... astounding."

show brendan -surprisedbrow -frownmouth -surprised
show ethan -surprisedbrow -frownmouth -surprised
show calem -surprisedbrow -frownmouth -surprised
show may -surprisedbrow -frownmouth -surprised
show leaf -surprisedbrow -frownmouth -surprised
show serena -surprisedbrow -frownmouth -surprised
with dis

calem @closedbrow talking2mouth "Hm. Well, perhaps we should also fan out... but with slightly less enthusiasm."

may @happy "Yeah! I mean, clearly, he needs it more than us! Wonder what he's going to buy?"

brendan @closedbrow talkingmouth "New running shoes, maybe? The ones he wears everywhere are all old and have holes in 'em."

leaf closedbrow talkingmouth "Hmm..."

$ renpy.pause(1.0, hard=True)

hide leaf
hide brendan
hide may
hide ethan
hide calem
hide serena
with dis

redmind "Sheesh, for such a big garden, there sure are a lot of people taking up space.{w=0.5} You'd think there'd be a quiet spot somewhere in here."

show garden:
    zoom 0.625 xalign 0.5
    pause 1.5
    ease 1.25 zoom 0.75 xalign 0.23
    pause 0.25
    ease 1.3 zoom 0.82 xalign 0.9 yalign 0.72
    pause 0.5
    ease 1.0 zoom 0.76 xalign 0.16 yalign 0.9
    pause 0.5
    ease 1.0 zoom 0.625 xalign 0.5
    
redmind "[ellipses]"

$ renpy.music.stop(channel='crowd', fadeout=3.0)

pause 1.5

redmind "[ellipses]"
redmind "Hey, here's a pretty good spot. Took long enough.{w=0.5} I can't just keep wandering around in this maze."
redmind "Let me just give the group a call..."
        
show phone_B 
show phone_A
with fadeinbottom

$ calledleaf = False

menu:
    ">Give Calem a call" if persondex["Calem"]["Contact"]:
        show calem uniform behind phone_A:
            alpha 1.0 xalign 0.5 zoom 0.9

        $ ValueChange("Calem", 1, 0.5)
            
        calem @talkingmouth "{i}Calling me to report? I'm flattered. May I assume you found a spot?{/i}"
            
        red @talkingmouth "Yeah, it's nice and quiet here.{w=0.5} Let's get everyone here quick before lunch period ends."
        
        calem @talkingmouth "{i}Great, where are you?{/i}"
        
        red @surprised "Uh..."
        redmind @thinking "Oh, awesome.{w=0.5} I was so focused that I have no idea how I ended up here."
        
        red @happyeyes happyeyebrows talkingmouth "I'm next to...{w=0.5} these hedges with lots of flowers on it.{w=0.5}{nw}"
        
        show calem thinking with dis
        extend @wince talking2mouth " And I see some of the benches. Made of wood, I think."

        calem @closedbrow talking2mouth "{i}Um, that... doesn't help.{/i}"
        
        calem @talkingmouth "{i}Which section are you in?{/i}"
        
        red @wince talking2mouth "{size=30}...Maybe I should've brought a map with me.{/size}"
        
        calem @talkingmouth "{i}I can't hear you clearly, [first_name].{/i}"
        
        red @happy "{i}Yeah, uh, hold on.{w=0.5} Let me ask somebody around here and I'll call you right back.{/i}"
        
        calem @talkingmouth "{i}All right. Talk to you soon...{/i}{w=0.5}{nw}"
        
        extend happy " {i}hopefully.{/i}"
        
        show calem:
            parallel:
                ypos 1.0
                ease 1.0 ypos 3.0
            parallel:
                alpha 1.0
                ease 0.4 alpha 0.0
    
    ">Give Brendan a call" if persondex["Brendan"]["Contact"]:
        show brendan uniform behind phone_A:
            alpha 1.0 xalign 0.5 zoom 0.9

        $ ValueChange("Brendan", 1, 0.5)
    
        brendan @talking2mouth "{i}Yo, no way, [first_name]!{w=0.5} You're calling me up? Thanks! Guess you found a spot?{/i}"
        
        red @talkingmouth "Yeah, it's nice and quiet here.{w=0.5} Let's get everyone here quick before lunch period ends."
        
        brendan @happy "{i}Cool, cool. So where are you?{/i}"
        
        red @surprised "Uh..."
        redmind @thinking "Oh, awesome.{w=0.5} I was so focused that I have no idea how I ended up here."
        
        red @happyeyes happyeyebrows talkingmouth "I'm next to...{w=0.5} these hedges with lots of flowers on it.{w=0.5}{nw}"
        
        show brendan thinking with dis
        extend @wince talking2mouth " And I see some of the benches. Made of wood, I think."
        
        brendan @talking2mouth "{i}Uh, y'know...{w=0.5} you pretty much just described the garden.{/i}"
        
        brendan @talking2mouth "{i}You know which section?{/i}"
        
        red @wince talking2mouth "{size=30}...Maybe I should've brought a map with me.{/size}"
        
        brendan @happy "{i}Sorry, I didn't catch that.{/i}"
        
        red @happy "Yeah, uh, hold on.{w=0.5} Let me ask somebody around here and I'll call you right back."
        
        brendan happy "{i}Okay, no prob. Gimme a call back when you figure it out!{/i}"
            
        show brendan:
            parallel:
                ypos 1.0
                ease 1.0 ypos 3.0
            parallel:
                alpha 1.0
                ease 0.4 alpha 0.0

    ">Give May a call" if persondex["May"]["Contact"]:
        show may uniform behind phone_A:
            alpha 1.0 xalign 0.5 zoom 0.8 ypos 0.95

        $ ValueChange("May", 1, 0.5)
    
        may @talkingmouth "{i}Oh, you're calling me, [first_name]?{w=0.5} Right, I forgot that you have this number! Then that means you found a spot?{/i}"
        
        red @talkingmouth "Yeah, it's nice and quiet here.{w=0.5} Let's get everyone here quick before lunch period ends."
        
        may @happy "{i}Great! So, where are you?{/i}"
        
        red @surprised "Uh..."
        redmind @thinking "Oh, awesome.{w=0.5} I was so focused that I have no idea how I ended up here."
        
        red @happyeyes happyeyebrows talkingmouth "I'm next to...{w=0.5} these hedges with lots of flowers on it.{w=0.5}{nw}"
        
        show may thinking with dis
        extend @wince talking2mouth " And I see some of the benches. Made of wood, I think."
        
        may @talkingmouth "{i}Well...{w=0.5} it sounds pretty! But I'm not sure I could find it from that.{/i}"
        
        may @happy "{i}Do you know which section you're in?{/i}"
        
        red @wince talking2mouth "{size=30}...Maybe I should've brought a map with me.{/size}"
        
        may @happy "{i}Could you raise your voice a bit? I didn't hear that!{/i}"
        
        red @happy "Yeah, uh, hold on.{w=0.5} Let me ask somebody around here and I'll call you right back."
        
        may happy "{i}Ok-ay! I'll let Brendan know, in the meantime.{/i}"
            
        show may:
            parallel:
                ypos 1.0
                ease 1.0 ypos 3.0
            parallel:
                alpha 1.0
                ease 0.4 alpha 0.0
    
    ">Give Serena a call" if persondex["Serena"]["Contact"]:
        show serena uniform behind phone_A:
            alpha 1.0 xalign 0.5 zoom 0.9

        $ ValueChange("Serena", 1, 0.5)
    
        serena @talkingmouth "{i}Oh, you're calling me, [first_name]?{w=0.5} Of course. I remember now, we exchanged information a while ago. Then, do I understand that you've found a spot?{/i}"
        
        red @talkingmouth "Yeah, it's nice and quiet here.{w=0.5} Let's get everyone here quick before lunch period ends."
        
        serena @happy "{i}Fantastique! So, where are you?{/i}"
        
        red @surprised "Uh..."
        redmind @thinking "Oh, awesome.{w=0.5} I was so focused that I have no idea how I ended up here."
        
        red @happyeyes happyeyebrows talkingmouth "I'm next to...{w=0.5} these hedges with lots of flowers on it.{w=0.5}{nw}"
        
        show serena thinking with dis
        extend @wince talking2mouth " And I see some of the benches. Made of wood, I think."
        
        serena @talkingmouth "{i}Beautiful, I am sure.{w=0.5} But do you have anything more concrete in terms of direction?{/i}"
        
        serena @happy "{i}For example, do you know which section you're in?{/i}"
        
        red @talkingmouth "{size=30}Man, my sense of direction is so poor I barely know which region I'm in.{/size}"
        
        serena @happy "{i}Pardon? You were a bit quiet there.{/i}"
        
        red @happy "Yeah, uh, hold on.{w=0.5} Let me ask somebody around here and I'll call you right back."
        
        serena happy "{i}Very well! I'll inform Calem, and keep him updated, then.{/i}"
            
        show serena:
            parallel:
                ypos 1.0
                ease 1.0 ypos 3.0
            parallel:
                alpha 1.0
                ease 0.4 alpha 0.0
    
    ">Give Leaf a call" if persondex["Leaf"]["Contact"]:
        $ calledleaf = True

        show leaf uniform behind phone_A:
            alpha 1.0 xalign 0.5 zoom 0.9
    
        leaf "{i}[ellipses]{/i}"

        red @surprised "Uh... hi? Are you there?"

        pause 2.0

        show leaf flirt bigblush with dis

        $ ValueChange("Leaf", 1, 0.5)

        leaf @flirttalk "{i}Hehehe. You're calling me on my phone.{/i}"

        red @closedeyes talkingmouth "Ah, geez. Look, I just found a place. It's nice and quiet.{w=0.5} Let's get everyone here quick before lunch period ends."
        
        leaf -flirt -bigblush @happy "{i}Alright, alright! Where are you, then?{/i}"
        
        red @surprised "Uh..."
        redmind @thinking "Oh, awesome.{w=0.5} I was so focused that I have no idea how I ended up here."
        
        red @happyeyes happyeyebrows talkingmouth "I'm next to...{w=0.5} these hedges with lots of flowers on it.{w=0.5}{nw}"
        
        show leaf thinking with dis
        extend @wince talking2mouth " And I see some of the benches. Made of wood, I think."
        
        leaf @sarcastic "{i}So...{w=0.5} you have no clue?{/i}"
        
        red @talkingmouth "{size=30}I mean, I know I'm in the garden...{/size}"
        
        leaf @happy "{i}Speak up! Can't hear your mumbling.{/i}"
        
        red @happy "Yeah, uh, hold on.{w=0.5} Let me ask somebody around here and I'll call you right back."
        
        leaf @sarcastic "{i}You better. $1,500 is riding on this!{/i}"
            
        hide leaf with dis

        pause 2.0

        redmind @thinking "$1,500? I thought it was $1,000{w=0.5}.{w=0.5}.{w=0.5}."

show phone_B:
    ypos 1080
    ease 1.0 ypos 3000
        
show phone_A:
    ypos 1080
    ease 1.0 ypos 3000
    
redmind @thinking "Okay, I need to dash fast."
redmind @angry "Of course, the {i}one{/i} time I need somebody around, the place is empty.{w=0.5} There's gotta be someone I can talk to..."

pause 1.5

show erikaintro:
    alpha 0.0 zoom 1.0
    parallel:
        ease 1.0 alpha 1.0
    parallel:
        ease 5.0 zoom 1.05
show erikaCG awake:
    alpha 0.0 zoom 1.0
    ease 5.0 zoom 1.05
        
$ renpy.pause(2.0, hard=True)

redmind @confusedeyebrows frownmouth "Hm, looks like somebody had the right idea finding a quiet place to nap.{w=0.5} But in the middle of a school day?"
redmind @thinking "I'd ask her for some directions, but I really don't want to wake some random stranger."
redmind "Then again, I don't see or hear anyone else around..."

show erikaintro:
    alpha 1.0 zoom 1.05
show erikaCG awake:
    alpha 0.0 zoom 1.05

redmind @thinking "I suppose I could just wake her up and ask her, but I wonder if she'll be mad at me for disturbing her beauty sleep..."

hide garden

menu:
    ">Nudge her and wake her up":
        redmind "Beggars can't be choosers."
        redmind "Who knows where the nearest person is in this maze?{w=0.5} I'll try and handle this as delicately as I can."
        
        show erikaintro:
            zoom 1.05
            ease 0.7 zoom 1.1
            ease 0.4 zoom 1.05
            ease 0.5 zoom 1.12
            ease 0.5 zoom 1.05
            
        redmind "I'll just...{w=0.5} gently...{w=0.5} nudge her until she wakes up..."
        
        erika uniform closedbrow talking2mouth "...Mm."

        show erikaintro:
            zoom 1.05
        
        redmind "Hey, I think it's working!"
        
    ">Leave her alone":
        
        redmind @thinking "Nah, I'll just ask someone else.{w=0.5} With a garden this big, I'm bound to bump into someone else soon."
        
        redmind @thinking "Or maybe I should just keep running in a straight line until I reach the center?{w=0.5} But what if one of the other guys finds a spot first? Then--"
        
pause 1.0
        
show erikaCG awake with dis

$ renpy.pause(1.5, hard=True)

erika uniform "[ellipses]"

red @happy "Hi!"

show erikaintro:
    zoom 1.05
    ease 0.2 zoom 1.0
show erikaCG sad:
    zoom 1.05
    ease 0.2 zoom 1.0

erika surprisedbrow frownmouth @surprised "EEK!"

hide erikaintro
hide erikaCG sad
with dis

show garden behind erikaintro:
    zoom 0.84781 xalign 0.5
    parallel:
        ease 0.03 xalign 0.49
        ease 0.03 xalign 0.51
        ease 0.03 xalign 0.5
        repeat 3
    parallel:
        ease 0.031
        ease 0.03 yalign 0.99
        ease 0.03
        repeat 3
        
show erika surprisedbrow frownmouth with dis:
    xpos 720 ypos 2.0 zoom 1.3565
    ease 0.75 ypos 1.0
    
$ PlaySound("Body Roll.ogg")

red @surprised "Waugh!"
    
hide erikaintro
hide erikaCG
    
erika sad @sadbrow surprised2mouth "Please, stay away! I promise I have nothing worth stealing!{w=0.5} D-don't hurt me! It's too public here!"

red @surprised "Ee-!{w=0.25} Wait, I wasn't trying to...{w=0.25} Let me expl--"

$ PlaySound("Slap.ogg")
pause 0.1

show erika angry:
    xpos 620 ypos 1.0 zoom 1.3565 rotate 0
    ease 0.1 xpos 520 ypos 1.2 zoom 1.44 rotate -3

show garden at garden_move1

pause 0.25

$ ValueChange("Erika", -1, 620/1920)

red @closedeyes surprisedmouth "Ow, my pride."

show erika:
    xpos 520 ypos 1.2 zoom 1.44 rotate -3
    ease 0.2 xpos 360 ypos 1.1 zoom 1.3565 rotate 0

show garden at garden_move2

erika sad @surprisedmouth "S-stay back! There's a professor right around the corner! And I have Pokémon!"

show garden:
    xpos 960 zoom 0.84781 rotate 0

redmind @frownmouth "I very much doubt both of those claims."

show garden:
    zoom 0.84781
    ease 0.5 zoom 0.625

show erika angry:
    xpos 360 ypos 1.1 zoom 1.3565 rotate 0
    ease 0.5 zoom 1.0 xpos 500 ypos 1.0
    
red @closedeyes talking2mouth "Look, slow down. I'm not attacking you, or robbing you, or anything."
red @sad "I was just trying to ask you something. I'm a good guy, really."

show garden:
    zoom 0.625 xalign 0.5

show erika:
    xpos 500 zoom 1.0
    ease 0.5 xpos 940
    
erika @angry "'Self-evident is goodness in the heart of the man who speaks not of his own.'"

show erika surprisedbrow frownmouth with dis

red @happy "Er... Is that from a book?"
red @thinking "[ellipses]"
red @surprised "W-wait! Wait, I know that one! {i}Pride's Pariah!{/i} I, uh, fell asleep reading it, but, um... I know that reference!"

erika @talking2mouth "You... {i}fell asleep{/i} reading {i}Pride's Pariah{/i}? One of the great romance novels of our time?"

red @happy "I mean, it's a great book, but, uh, doesn't have anything to do with Pokémon, y'know? I wasn't the best at school."

red @closedbrow talking2mouth "I was at the bottom of my class in Pallet, actually. So... yeah, I haven't done a whole lot of book-learnin'."

erika -surprisedbrow -frownmouth @sadbrow talking2mouth "Oh, you're from Pallet Town? In Kanto?"

red @surprised "Wait, you've actually heard of Pallet?"

erika @talkingmouth "Yes, rather. My tutors ensured I had a thorough grounding in my academics, including the geography of my home region."

erika @talkingmouth "I lived in Celadon City, you see, before I was sent here."

redmind @thinking "[ellipses]I think I may have found my complete opposite. I'm from a tiny town, she's from the second-biggest city in Kanto." 

if (calledleaf):
    redmind @thinking "I'm running around a garden for $1,500, and her parents paid for tutors."
else:
    redmind @thinking "I'm running around a garden for $1,000, and her parents paid for tutors."

red @talking2mouth "Well, see? We're both Kantonian. Even with that shaky start, we can find some common ground."

erika sad @talking2mouth "Yes, you're right. I jumped to conclusions, and thought you were acting with wicked intent. I apologize."

red @happy "Hey, don't worry about it. It was my bad, too."

show erika at getcloser:
    xpos 940

erika -sad @talkingmouth "How is your eye? Are you injured? I know a little first aid..."

red @happy "Ah, don't worry about it. I've taken worse before."

show erika at getfurther:
    xpos 940

erika @surprised "Truly? You must be quite the street tough."

redmind @thinking "It's more like you have the wrist strength of a Wynaut, but sure."

red @talkingmouth "Anyway, sorry about waking you up, again. I was actually just trying to figure out where in the garden I am."

erika @surprised "Where...?"

red @closedbrow talking2mouth "Yeah. Like, the section we're in, or maybe how to get here from the main area?"

erika sad @sadbrow talkingmouth "Oh... I'm afraid I don't know. I simply told the Professor I'd like a nap, and she brought me here."

red @surprised "Oh, so there {i}really{/i} was a professor around the corner?"

show erika:
    xpos 940.0/1920.0
    ease 0.5 xpos .75

show kris at leftside with dis

kris @talkingmouth "Sure is! How can I help you, kiddo?"

red @confusedeyebrows talking2mouth "[ellipses]{nw}"
extend @talking2mouth "Very funny. Where's the {i}actual{/i} Professor?"

show erika surprisedbrow frownmouth
show kris surprisedbrow frownmouth
with dis

pause 2.0

kris angrybrow @surprisedmouth "Ex-{i}cuse{/i} me?"

red @happy "I mean, glasses and a crop-top lab coat don't really make you a Professor."

show garden at vpunch
show kris at getcloser, leftside

kris @pissedbrow pissedmouth "No, but my {i}doctorate{/i} does! Would you like me to bring you to my office and show it to you?!"

red @surprised "Wait... you actually {i}are{/i} a Professor?"

show kris closedbrow angrymouth at getfurther, leftside with dis

kris @poutmouth "Hmph."

$ BecomeNamed("Professor Cherry")

erika -surprisedbrow -frownmouth @talkingmouth "Er... this is Professor Cherry, my mentor."

red @surprised "Oh, crap. Uh, sorry, miss--Doctor. Professor? Doctor Professor Cherry. I know who you are now. I just didn't see you on the faculty page."

red @sad "And, uh, you look {i}really{/i} young to have a doctorate."

kris "{w=0.5}.{w=0.5}.{w=0.5}."

kris @angrybrow talking2mouth "What's your name?"

red @sad "Um, [first_name] [last_name]. I'm Ethan's dormmate. I think you might know him?"

kris "{w=0.5}.{w=0.5}.{w=0.5}."

kris -closedbrow -angrymouth -angrybrow @talkingmouth "Alright, I'm over it. Yes, I'm a professor, and yes, I'm the youngest professor that Kobukan's ever had."

red @happy "Well, uh... hi! Sorry, I really didn't mean to offend you."

redmind @thinking "Geez, I'm really off my game today. That news yesterday really threw me off."

kris -angrymouth @talkingmouth "You said you were dormmates with Ethan?"

red @talkingmouth "Yeah, that's right."

kris @happy "Hah! That's cute. What do you think of him?"

red @surprised "What do I think of him? Uh... well, he's a cool, friendly guy. Though there's this weird thing happening where we keep ending up in the same places, and doing the same things."

kris @happy "Did he tell you about me?"

red @closedeyes talking2mouth "Not so much. Just mentioned your name, and said you were his homeroom teacher. It seems like you had some sort of history?"

kris @talkingmouth "That's one way to put it. I actually used to be his babysitter. Since his Dad was always at work, he was basically like my little brother."

red @surprised "{w=0.5}.{w=0.5}.{w=0.5}."

red @angrybrow happymouth "Oh my god. You can tell me embarrassing Ethan stories, right?"

kris @angrybrow happymouth "Can I?"

pause 1.0

red @closedbrow talking2mouth "Ah... damn. Sorry, Doctor, I'd love to hear more about Ethan, but I've gotta find a place for the rest of my friends to eat."

kris @talkingmouth "Oh, you're having a picnic out here? That's a nice idea. Do you want to use this area? Erika and I were just about to leave."

$ BecomeNamed("Erika")
$ persondex["Erika"]["Value"] = -1

redmind @thinking "Erika, huh? Okay, got it."

red @closedeyes talking2mouth "Yeah, that'd be great, actually. Uh... do you know how to get here? Or what section this is?"

kris @talkingmouth "Sure, it's the area with the {i}Oranomi sinesis{/i} trees."

pause 2.0

red @wince talking2mouth "Uh... despite my accent, I'm not actually a farmer. I don't know what those are."

kris @surprised "Oh. Right. 'Oran Berry' trees."

red @closedbrow talking2mouth "Oh, okay. I think I saw some signs pointing to the 'Oran Grove' a while back, so everyone else should be able to find their way here."

red @happy "Thank you very much, Doctor!"

kris @happy "Just 'Professor' is fine."

erika @sadbrow talkingmouth "I'd like to, um, apologize again for jumping to conclusions."

red @talking2mouth "It's alright. It was sensible, given the situation."

erika @happy "Farewell, then. 'Then, I do grant thee permission to depart, 'tis only to enhance the joy of our eventual reunion.'"

red @talkingmouth "And an old book quote to you too, Erika."

$ ValueChange("Erika", 2, 0.75, False)
$ ValueChange("Professor Cherry", 1, 0.25)

hide erika
hide kris 
with dis
        
$ renpy.pause(2.5, hard=True)

redmind "All right, time to give the group another call."

show blank2 with splitfade
$ renpy.pause(1.5, hard=True)

stop music fadeout 1.5

show text "{color=#ffffff}.{/color}" as text1:
    alpha 1.0
    pause 0.5
    ease 0.0 alpha 0.0
show text "{color=#ffffff}..{/color}" as text2:
    alpha 0.0
    pause 0.5
    block:
        ease 0.0 alpha 1.0
        pause 0.5
        ease 0.0 alpha 0.0
show text "{color=#ffffff}...{/color}" as text3:
    alpha 0.0
    pause 1.0
    block:
        ease 0.0 alpha 1.0
        pause 1.5
        ease 1.0 alpha 0.0

$ renpy.pause(3.0, hard=True)

hide brendan
hide ethan
hide calem
hide leaf
hide serena
hide may

show brendan uniform at dissolvein behind blank2:
    xpos 1.0/7.0 xzoom -1
show ethan uniform at dissolvein behind blank2:
    xpos 2.0/7.0
show calem uniform at dissolvein behind blank2:
    xpos 3.0/7.0
show may uniform at dissolvein behind blank2:
    xpos 4.0/7.0
show leaf uniform at dissolvein behind blank2:
    xpos 5.0/7.0
show serena uniform at dissolvein behind blank2:
    xpos 6.0/7.0 xzoom -1

$ renpy.music.play("Audio/Morning_ambience.ogg", channel='crowd', loop=True, fadein=1.0)

hide blank2 with splitfade
$ renpy.pause(1.5, hard=True)

hide text
hide text1
hide text2
hide text3

red @happy "Well, we're all here now, but we'd better eat fast.{w=0.5} Lunch period's gonna be ending pretty soon."

ethan @happy "Aha! I already ate mine while we were walking here.{w=0.5} See? Thinking ahead."

red @surprisedeyes talking2mouth "I... guess that's one way to put it."

show brendan surprisedbrow frownmouth
show ethan surprisedbrow frownmouth
show calem surprisedbrow frownmouth
show may surprisedbrow frownmouth
show leaf surprisedbrow frownmouth
show serena surprisedbrow frownmouth
with dis

$ renpy.music.play("Audio/pokemon/cries/48.mp3", channel="altcry", loop=None)

pause 1.0

ethan @talkingmouth "Woah, what was that?"

pause 2.0

redmind @surprised "Wait, they're looking at me?"

show brendan -surprisedbrow -frownmouth -surprised
show ethan -surprisedbrow -frownmouth -surprised
show calem -surprisedbrow -frownmouth -surprised
show may -surprisedbrow -frownmouth -surprised
show leaf -surprisedbrow -frownmouth -surprised
show serena -surprisedbrow -frownmouth -surprised
with dis

red @happy "Sorry, guys! I learned my Pokémon from books. Kinda hard to convey what a Pokémon cry sounds like through text."

may @closedbrow talking2mouth "Wait, wait, I know this one..."

brendan @happy "That's my girl!"

may @happy "Yeah, that's right! It's Venonat! I knew it had to be a Bug-type!"

brendan angrybrow happymouth "C'mon, babe, let's catch it for you!"

may angrybrow happymouth "Let's go!"

hide may
hide brendan 
with dis

pause 2.0
    
leaf @talking2mouth "So, completely unrelated, you think the National Tournament this year's going to be an Academy sweep?{w=0.5}{nw}"
extend @surprised " With what I saw at the exhibition match, I can't imagine it not being one."

calem @talkingmouth "Hm... I'm unsure. Janine's skills are impressive, and there's no doubt she's a powerful trainer at her level. But her ace {i}is{/i} a Venomoth."

ethan @surprised "What do you mean, Calamari?"

calem @talkingmouth "Well, Venomoth isn't a very strong Pokémon, is all."

red @closedbrow talking2mouth "You're sounding a bit like Lance, there."

calem @surprised "[ellipses]Oh, dear, I am. Please excuse me. Old habits."

serena @talkingmouth "Regardless of the strength of her Pokémon, Janine {i}is{/i} very young. She still attends this Academy, after all. I just can't see her as Champion material."

leaf @angrybrow talking2mouth "What, just 'cause she's young? The National Champion of Unova is, like, six."

ethan @talkingmouth "Twelve, actually."

leaf @sarcastic "You can remember that, but can't remember a name."

ethan @closedbrow talking2mouth "What's this about a national tournament, though?"

leaf @sarcastic "Uh... It's, like, only the most important event any student Trainer looks forward to.{w=0.5} Or at least any Trainer worth their salt."

#red @talking2mouth "I'd like a large explanation with a side of context. Hold the sarcasm, please."

#leaf @happy "Oh, coming right up. Careful, it's hot!"

leaf @closedbrow talkingmouth "Basically, the Kobukan region isn't large enough to support a traditional eight-Gym challenge. Four times a year, roughly every three months, everyone in Kobukan has a week to compete in the Quarter Qlashes."

ethan @closedbrow talking2mouth "Quarter Qlashes?"

leaf @sarcastic "Yeah, with two 'Qs.' It's very dumb. Anyway, the QQs are a bunch of single-elimination mini-tournaments all held at the same time. You have to win three times."

calem @talkingmouth "If you win, you eliminate seven other people."

serena @talkingmouth "{i}Personally{/i} eliminating three, of course."

redmind @thinking "Maybe it's just their accents, but the way those two say eliminate, it sounds like they mean 'kill.'"

leaf @talkingmouth "Yeah, so if you're a finalist in all four Quarter Qlashes in a year, you're allowed to participate in the National Tournament at the end of the year."

ethan @closedbrow talking2mouth "And the winner of that gets to fight the Champion for the title?"

calem @closedbrow talking2mouth "This year, the winner will just {i}become{/i} Champion. Kobukan's current Champion abdicated around this time last year."

red @closedbrow talking2mouth "Hm... just spitballing here, but has an academy student ever become Champion?"

serena @surprised "A student? No, not to my knowledge. Though the majority of Kobukan Champions have been alumni."

red @closedbrow talking2mouth "Huh."

leaf @sarcastic "Hey, I know what you're thinking. And no, absolutely not, that's impossible."

red @happy "That obvious, huh?"

leaf @closedbrow talkingmouth "Like a book."

pause 1.0

narrator "You make small talk as you shove sandwiches in your mouth before you're called back to class."

hide serena
hide calem
with dis

stop music fadeout 8.0

narrator "Eventually, Serena and Calem leave, briskly speedwalking to their next class."

pause 2.0

show leaf angrybrow
show ethan surprisedbrow frownmouth 
with dis

pause 2.0

hide ethan
show leaf -angrybrow 
with dis

narrator "Finally, following a particularly nasty glare from Leaf, Ethan leaves you and Leaf alone."

pause 1.0

show leaf at getcloser:
    xpos 5.0/7.0

leaf blush embarrassed "Hey. Um, we don't have much time..."

redmind @surprisedbrow frownmouth sweat "?"

leaf -blush flirtbrow bigblush @talking2mouth  "And, well, I know you've been waiting for this. That you {i}need{/i} this. So..."

redmind surprisedbrow frownmouth @surprised "Wait, holy shit, what's she--"

$ PlaySound("Get.ogg")

leaf -bigblush -flirtbrow @happy "Here's your $2,000!"

$ money = 2000

narrator "Leaf shoves $2,000 into your sweaty hands."

red @talkingmouth "Oh."

pause 1.0

red -surprisedbrow -frownmouth -surprised @closedbrow talking2mouth "Wait, no, Leaf, you didn't need to... I mean, I could tell you were joking."

pause 1.0

leaf sadbrow @talkingmouth "Hey.{w=0.5} It's alright. Just take it, okay?"

red @sad "...How? I mean, how did you...?"

pause 1.0

leaf @talkingmouth "Only someone who really needs it would have run {i}that{/i} fast."
leaf @talking2mouth "Besides... you never answered me when I asked if you could afford to evolve [pika_name] now."

red @sad "...I'm not too proud to reject this, but..."
red @closedbrow talking2mouth "I have to figure this out by myself. I rely on my friends too much already."

leaf @surprised "What? No, you don't."

red @sadeyes sadeyebrows talking2mouth "I really do. You've never seen it before, but if I don't have someone backing me up, I just...{nw}" 
extend @closedbrow talking2mouth " shut down."

leaf @happy "Well, hey, you'll always have {i}someone{/i} backing you up. You're way too popular to not have that, right?"

red @talking2mouth "I hope so! For a while, Blue was my only friend in Pallet. When he stopped being my friend, I..."
red @talkingmouth "Well, anyway. I decided I was never going to let that happen again."

leaf @closedbrow talkingmouth "Oh, right?"

red @happy "Yeah. I was going to get fit, read everything I could get my hands on, and make friends with {i}everyone{/i} I talked to. I'd do everything I could to make sure I never lost all my friends again."

leaf @flirttalk "Well, I think you're probably safe. The only thing that could wipe out all your friends now would be, like, a meteor."

red @happy "I'll keep an eye on the forecast."

leaf @talking2mouth "Alright. So what are you going to spend that money on? Maybe you could get some new running shoes?"

red @happy "Oh, no, I keep these things on purpose. I could totally get new ones, I just like the smell."

leaf @happy "Hahaha!{w=0.5} Gross!"

show blank2 
hide red
hide leaf
with splitfade

pause 2.0

red uniform @happy "Hey, did I tell you that I made two new friends while I was off running? And one's a professor!"
leaf uniform @surprised "Jeez louise, [first_name]! We need to get you on a twelve-step program! Your friend addiction is tearing this family apart!"
red uniform @angry "These are choices, Leaf! I can quit any time!"

pause 2.0

show blue uniform thinking behind blank2
hide blank2 
with dis

blue @talkingmouth "...A meteor, huh?"

show blank2
with dis

pause 2.0

jump PickElective