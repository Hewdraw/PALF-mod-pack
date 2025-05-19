label secondhomeroom010408:

$ renpy.music.queue("Audio/Music/Oak Class.ogg", channel='music', loop=True, fadein=1.0, tight=None)

scene blank2

show oakbg behind blank2
show homeroom behind oakbg

$ renpy.transition(dissolve)
show screen currentdate

hide blank2 with dis

$ renpy.music.queue("Audio/Music/Oak Class.ogg", channel='music', loop=None, fadein=1.5, tight=None)
    
show homeroom behind oakbg

oak @talkingmouth "...And that concludes our lesson for today."

redmind uniform @thinking "Finally! Sam's always fun to listen to, but my head starts swimming after just twenty minutes of lecture, never mind four hours."
redmind @thonk "Wait. We were supposed to have a quiz, weren't we?"

$ renpy.music.play("Audio/school_crowd.ogg", channel='crowd', loop=True, fadein=1.5)
narrator "Despite your hesitancy, everyone in the room starts to shuffle out of their seats."

$ renpy.music.stop(channel='crowd', fadeout=1.5)
oak @talkingmouth "Not so fast! I haven't dismissed you yet.{w=0.5} I hope you all haven't forgotten about the {color=#0048ff}quizzes every Monday and Thursday.{/color}"

show flannery uniform with dis:
    xpos 0.66

flannery @surprised "Oh... what?{w=0.6}{nw}"

extend sadbrow frownmouth @angry " Whitney! You said those were on Mondays and {i}Fridays!{/i} "

show whitney uniform with dis:
    xpos 0.33

whitney @talking2mouth "Oops, did I really?{w=0.6}{nw}"

extend happybrow @happy " Oh well! You know, if you studied, you wouldn't have anything to worry about!"

flannery @sad "Oh noooo..."

hide flannery
hide whitney
with dis
    
oak @talkingmouth "Okay, class. Clear your desks and take out your pencils." 
oak @talkingmouth "Today's quiz is pretty simple. Still, make sure you look at the status of the field, your opponent, and yourself, before you commit to any moves!"
oak @talkingmouth "Remember, {color=#0048ff}this is graded!{/color}"

$ trainer1 = Trainer("red", TrainerType.Player, [Pokemon(pokedexlookupname("Deino", DexMacros.Id), level=5, moves=[GetMove("Tackle"), GetMove("Dragon Rage"), GetMove("Focus Energy"), GetMove("Draco Meteor")])])
$ trainer2 = Trainer("oak", TrainerType.Enemy, [Pokemon(pokedexlookupname("Klink", DexMacros.Id), level=15, moves=[GetMove("Vise Grip")], ability="Plus")])

$ trainer1.GetTeam()[0].Health = 1
$ trainer2.GetTeam()[0].ChangeStats(Stats.Speed, -6, trainer2.GetTeam()[0])
$ trainer2.GetTeam()[0].Health = 40
$ trainer2.GetTeam()[0].Stats[Stats.Health] = 40

call Battle([trainer1, trainer2], clearstats=False, gainexp=False, healParty=False, uniforms=[True, False], lockbag=True) from _call_Battle_5
$ battlehistory["Oak1"] = _return

$ renpy.transition(dissolve)
show screen currentdate

if (WonBattle("Oak1")):
    red uniform @happy "Hey, that was pretty easy. Phew. Good thing that Klink was slowed down so much. Pretty much anything it did to me could've knocked me out if it went first."
else:
    red uniform @sad "Oh, man... I knew I had to knock that Klink out before it hit me, but I thought I had more time..."

oak @talkingmouth "[ellipses]"

pause 0.5

oak @talkingmouth "At a glance..."

pause 0.5

if (WonBattle("Oak1")):
    oak "It looks like everyone did quite well. It seems you understand the importance of fixed-damage moves. There are other moves that ignore defenses, too, and I look forward to seeing how you use them."
else:
    oak "I recommend everyone pay more attention to the status of the battlefield before committing to a move." 
    oak "Depending on the amount of health you have left, or the amount of stat changes on you and your opponent, you might want to battle more or less aggressively."

oak @talkingmouth "That's it for today, class.{w=0.5} Now, you're all dismissed."

show oakbg:
    alpha 1.0
    ease 0.5 alpha 0.0

$ renpy.music.play("Audio/school_crowd.ogg", channel='crowd', loop=True, fadein=1.5)

redmind @thinking "Finally, I'm about ready to drop. For the first time, I don't even care about talking to Sam, I just want to get out of here."

hide oakbg

show oak:
    xpos 450 alpha 0.0
    parallel:
        ease 0.5 alpha 1.0
    parallel:
        ease 1.5 xpos 720
    
pause 0.5

oak @talkingmouth "[first_name], it's time.{w=0.5} Come to my laboratory in the Research Center now, if you please."

show oak:
    alpha 1.0 xpos 720
    
red @talkingmouth "Uh, sure thing, Professor."

show oak:
    xpos 720 alpha 1.0
    parallel:
        ease 0.75 alpha 0.0
    parallel:
        ease 1.0 xpos 900

pause 1.5

hide oak

show blue uniform:
    alpha 0.0 xpos 400
    parallel:
        ease 0.5 alpha 1.0
    parallel:
        ease 0.75 xpos 720
    
blue @talkingmouth "Not even a week and you're already in trouble.{w=0.5} What'd you do this time?"
    
red @angrybrow talking2mouth "Oh, shove off. I'm sure it's nothing."

show blue happy:
    alpha 1.0 xpos 720
    ease 0.5 alpha 0.0 xpos 500
    
redmind @thinking "...Suddenly, all my tiredness has just disappeared."
redmind @happy "Anyway, he said the Research Center, right?{w=0.5} So, if I start running now, I should be able to cover the entire campus in--"

show hall_A2b at sepia with dis

$ renpy.pause(1.0, hard=True)

show leaf angrybrow angrysmilemouth at sepia, dissolvein behind flashback

pause 0.5

leaf @talking2mouth "Use. The. Brochure. It's got a map on it!"

show blank with splitfade

hide leaf
hide hall_A2b
hide flashback
hide blank with dis

pause 1.5

redmind @happy "...Yeah, you're right, head-Leaf. "

redmind @thinking "[ellipses]"
redmind @thinking "Actually, Leaf's always been inviting me to go out since school started. Maybe I should invite her, this time?"

menu:
    ">Invite Leaf":        
        show leaf uniform with dis:
            xpos 700
            
        red @talkingmouth "Hey."

        leaf @happy "[first_name]! Hi!{w=0.5} What's up?"
        
        red @talkingmouth "I'm dropping by the Research Center. I was going to take a look around, then have a chat with Sam."

        show leaf surprisedbrow frownmouth with dis

        red @happy "A while ago, you seemed surprised by how close he and I are, so I thought maybe you'd want to hear us chat."
        
        leaf -surprisedbrow -frownmouth @happy "Aw, I'd love to go!{w=0.5}{nw}"
        
        show leaf:
            xpos 700
            ease 0.5 xpos 750
            
        extend @talkingmouth " Did you know I used to be super into science stuff when I was a kid?{w=0.5}{nw}"
    
        show leaf:
            xpos 750
            ease 0.5 xpos 700
        
        extend @happy " Mostly paleobiology, but I bet the other 'ologies' are just as cool!"
        
        red @happy "Cool. So, you good to go?"
        
        leaf @embarrassedbrow talkingmouth "I would be, buuut, just not today.{w=0.5}{nw}"
        extend @blush embarrassedbrow talking2mouth " I kinda asked to study with May after I bombed the quiz. I knew Instructor Clair said something about Dragon Rage, but... I'm really sorry!"
        
        red @talkingmouth "Hey, no problem. We'll do it another time."
        
        leaf @flirttalk "Yeah we will.{w=0.5} I'll come next time, I promise!"
        
        $ ValueChange("Leaf", 1, 700/1920)
        $ BecomeContacted("Leaf")

        leaf @happy "And now, next time you want to invite me somewhere, you can just call me."
        leaf @flirttalk blush "Aren't you a lucky guy?{w=0.5} See you later, [first_name]!"
        
        hide leaf with dis
            
        pause 1.0
        
        redmind @happy "Heh, she probably didn't invite me out in the first place because she had things to do.{w=0.5} Well, can't say I didn't try."
        redmind "Anyway, I should get going."       
        
        hide leaf
        
    ">On second thought...":        
        redmind @thinking "Nah. I'm going to be talking with Sam about serious stuff. Like, how I even got into this school."
        redmind @thinking "Frankly... I'm not sure I want her hearing that."

window hide

show blank2:
    alpha 0.0
    pause 0.5
    ease 1.5 alpha 1.0

$ renpy.transition(dissolve)
call clearscreens from _call_clearscreens_36
$ renpy.music.stop(channel='crowd', fadeout=1.5)
stop music fadeout 1.5
$ renpy.pause(2.5, hard=True)

############################################################################################################################################################################################################################
#### 2. RESEARCH CENTER ####################################################################################################################################################################################################
############################################################################################################################################################################################################################

queue music "audio/music/power plant_start.ogg" noloop fadein 1.0
queue music "audio/music/power plant_loop.ogg"

$ renpy.transition(dissolve)
show screen currentdate

scene research with Dissolve(2.0)

hide blank2

pause 0.5

redmind uniform "I'm impressed! It's like Professor Oak's lab back home, except ten times bigger and cleaner.{w=0.5} Makes me wonder why Professor Oak would even bother coming back to Pallet Town."

show bianca uniform happy:
    alpha 0.0 xpos -250 ypos 1.1 zoom 1.0
    ease 0.3 alpha 1.0 xpos 740
    ease 0.2 zoom 1.2 xpos 700 ypos 1.0

bianca @talkingmouth "[first_name]!{w=0.5} Is that you?"

show bianca happy:
    xpos 700 zoom 1.2 alpha 1.0
    
red @talkingmouth "The one and only.{w=0.5} I didn't expect to see you here."

bianca -happy @talkingmouth "Me, too!{w=0.5} Well, I mean, I didn't expect to see {i}you{/i} here!{w=0.5} I'm always here to help Nate around the lab! I mean, if I'm not helping Cheren!"
$ natenamed = IsNamed("Nate")
if (natenamed):
    red @talkingmouth "Oh, Nate's here?"

    show bianca:
        xpos 700 zoom 1.2
        ease 0.5 xpos 720 zoom 1.0

    bianca @talkingmouth "Yeah!"

else:
    red @talkingmouth "Oh, really? Uh... who's Nate?"

    show bianca:
        xpos 700 zoom 1.2
        ease 0.5 xpos 720 zoom 1.0
    
    bianca @talkingmouth "He's a friend from Unova.{w=0.5} He's real smart!"

show bianca:
    xpos 720 zoom 1.0
    
bianca @talkingmouth "Anyway, what made you want to visit the Research Center all of a sudden?"

red @talkingmouth "Well, Sam asked me to come here to talk about something. Uh, Professor Oak, I mean."

bianca @talkingmouth "Oh, neat!{w=0.5}{nw}"

show bianca happybrow talkingmouth:
    subpixel True
    
    block:
        ease 0.12 ypos 1.12 xpos 650
        ease 0.1 ypos 1.0
        repeat

extend @talkingmouth " {cps=140}{size=30}I'm here 'cause today the Research Center brought in Magnemite and Voltorb and we're gonna see how much energy they can store in a light bulb, oh, but we're not gonna use them for slave labor or anything, gosh, no, that'd be awful--{/size}{/cps}"

redmind "[ellipses]"

bianca @talkingmouth "{cps=140}{size=30}You can think of this as like some kind of conditioning or workout routine for Pokémon like Magnemite or Voltorb and I heard somewhere that since they technically don't have any muscle fibers or whatever, using up their electricity builds up their natural affinity to their--{/size}{/cps}"

show bianca -happybrow -talkingmouth:
    xpos 650 ypos 1.0
    ease 0.5 xpos 720 zoom 1.0

$ showredonly = True
    
nate uniform "Yo, B! Are you running the ears off another guest?"

#### Nate INTRO ################################################################################################

show bianca:
    xpos 720 zoom 1.0
    ease 0.5 xpos 900

show nate uniform with dis:
    xpos -100
    ease 1.25 xpos 450

nate @happy "You gotta slow it down, B! I'm never going to get another assistant if you keeping blocking off the door with your wall of text!"

$ showredonly = False

bianca @happy "You don't need another assistant, though! You have me!"

nate @talking2mouth "You're part-time." 
nate @winkbrow talkingmouth "Much as I'd love to have all your attention to myself, I know you've got a thing going on with Cheren."
nate @happy "Now, {i}I{/i} don't mind sharing, but I think Cheren might."

pause 2.0

show bianca surprisedbrow frownmouth
show nate surprisedbrow frownmouth
with dis

red @talkingmouth "Ahem."

show bianca -surprisedbrow -frownmouth -surprised
show nate -surprisedbrow -frownmouth -surprised
with dis

$ name_fragment = first_name[0]
if (IsNamed("Nate")):
    nate @talkingmouth "Hey! [first_name], right?"

else:
    $ BecomeNamed("Nate")

    nate @talkingmouth "Hey! Sorry, what am I doing? Names, right? I'm Nate. What's up?"

    red @talkingmouth "[first_name]. Pleasure."

nate @happy "Good to have ya here! I see you and Bianca know each other already."

red @closedbrow talking2mouth "Yeah, Bianca's grabbed me a couple times for Cheren."

nate @talkingmouth "Cool, cool. Anyway, let me welcome you to the Research Center."
nate @happy "There's not much here for the average student, though. But if you're trying to do something big with computers, or run an experiment, this is the place."

show nate surprisedbrow frownmouth with dis

red @confused "Well, which of those categories are you in?"

pause 1.0

nate -surprisedbrow -frownmouth @closedbrow talking2mouth "Observant, huh? Yeah, I'm here just to, uh... use the computers, basically. Networking stuff."
nate @happy "Think of me like Kobukan's unpaid, unknown, IT guy!"

show bianca:
    subpixel True xpos 900
    block:
        ease 0.15 ypos 1.12
        ease 0.1 ypos 1.0
        repeat 3

bianca @talkingmouth "Yeah! Nate's a super genius!{w=0.5} He knows how to code and hack and slash and debug and defrag and defibrillate and defenestrate and--"

nate sweat @angrybrow talking2mouth "B, let's not talk too much more, alright?"

bianca @happy "O-kay!~"

nate -sweat surprisedbrow frownmouth @neutraleyes talkingmouth "Sorry about that, [name_fragment]. Really, I'm just a simple tech guy. So if you have a toaster that needs fixing, {i}that's{/i} the kind of stuff I can do."

$ PlaySound("vibrate.ogg")
pause 1.5

nate @surprised "Oh, that's for me. Sorry, gotta step out for a sec, [name_fragment] and B!"
show nate happy with dis

red @talkingmouth "See you around."

show nate at dissolveaway:
    xpos 450

pause 2.0

nate @closedbrow talking2mouth "{gradualsize=36-20}Yes? Of, course, Sir, it's all on...{/gradualsize}"

pause 2.0

bianca @happy "Nate's always being pulled off by phone calls!" 
bianca @surprised "Then he gets super serious for a couple minutes."
bianca -happy @happy "Then he's back to normal!"

pause 1.0

red @talkingmouth "So how'd you meet? I figured you and Cheren were childhood friends, but now it looks like you and Nate are, too?"

bianca @talkingmouth "Yep! Actually, Cheren and I are from Nuvema Town. Then we moved to Aspertia, and met Nate!"
bianca @surprised "Nate was barely ever home, though! I think I've talked to him more in the last four days than I ever had before!"

red @closedeyes talkingmouth "So... you don't actually know him all that well? But you're helping him with his ambiguous 'computer stuff?'"

bianca @happy "I guess not! And I guess so!"

red @confusedeyebrows talkingmouth "And the whole thing about being here every day is...?"

bianca @happy "I've been here every day of the school year so far!"

red @closedbrow talking2mouth "Hm. Well, uh, {w=0.5}{nw}" 
extend @happy "I look forward to seeing you again!"
    
bianca @talkingmouth "Yay!"
bianca @surprised "Ooh! You said you wanted to see Professor Oak, right? He's down the hallway, to the left!"

red @happy "Hey, thanks."

bianca @happy "No problem!~♪"

show bianca happy:
    alpha 1.0 xpos 900
    ease 0.5 alpha 0.0 xpos 300

pause 0.5

show blank2 with splitfade

$ renpy.pause(1.5, hard=True)

stop music fadeout 1.0

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

hide nate
hide bianca

hide text
hide text1
hide text2
hide text3

$ renpy.music.queue("Audio/Music/OakTheme_Start.ogg", channel='music', loop=None, tight=None)
$ renpy.music.queue("Audio/Music/OakTheme_Loop.ogg", channel='music', loop=True, tight=None)

hide blank2 with splitfade

#### MEET OAK ################################################################################################

show oak with dis:
    xpos 0.5

oak @talkingmouth "Ah, [first_name].{w=0.5} Good, you're here."

red @talking2mouth "Hey, Sam.{w=0.5}{nw}" 
extend @talkingmouth " I'm glad we're finally getting to talk. Now, what did you want to talk about?"

oak @happy "Let me answer that question with a question, lad.{w=0.5} What do you think we {i}have{/i} to talk about?"

red frownmouth @talking2mouth "...My place in this academy."

oak @closedeyes talkingmouth "Yes, I can imagine that you would think it would be necessary for us to discuss this."

red @talking2mouth "Sam, please, just give me a straight answer. Why am I here? Why didn't you tell me you'd be here?"

oak @angrybrow frownmouth "[ellipses]"

oak @talking2mouth "I'll give you an answer, [first_name] [last_name]. But you're going to have to work for it."

red @angrybrow frownmouth "[ellipses]"

red @happy "Yeah, alright. Classic Samuel Oak move right there. You never just hand anything over, do you?"

oak @closedeyes talkingmouth "No. No, I do not."

show flashback with dis

red @closedbrow talking2mouth "Okay. Here are the facts. I'm in Kobukan Academy. And you teach here. You didn't tell me, even though you would've had plenty of time to."
red @closedbrow talking2mouth "So you didn't {i}want{/i} me to know. However, you knew how much getting into Kobukan Academy meant to me."
red @closedbrow talking2mouth "And you knew that if I knew you were working here, I'd ask for your help getting in."
red @closedbrow talking2mouth "So, you didn't want me to ask for your help. That means you either didn't want to help me, or... you didn't want me to ask for help."

pause 1.0

$ PlaySound("idea.ogg")

hide flashback with dis

red @happy "Oh, duh, now I get it!"

show oak surprisedbrow frownmouth with dis

red @talkingmouth "You didn't want me to ask for your help getting in because then you'd have to choose between recommending Blue or me."

pause 2.0

oak -surprisedbrow -frownmouth -surprised @closedeyes talkingmouth "...Completely wrong, actually."

red @surprised "What?"

oak angrymouth @talking2mouth "Lad, I never had any intention of recommending my grandson to this school."

red @surprised "WHAT?! But... why... why not?"

oak @angrybrow frownmouth "[ellipses]"
oak @angrybrow talking2mouth "Do your best to answer that question. Then I will give you my answer."

redmind @thinking "Ugh, this again..."

red @closedeyes talking2mouth "Well... You figured he could get into this school without your help? And you wanted to give him confidence, let him know that he doesn't need to rely on your name?"

oak @closedeyes talking2mouth "Once again, entirely incorrect."

red @sad "Then... why?"

oak @closedeyes talkingmouth "Why don't you try to answer that, then--"

show oak surprisedbrow frownmouth with dis

red @angry "Just answer the question, Sam!"

pause 1.0

show oak angry with dis

pause 2.0

red @sad "Well?"

oak angrybrow angrymouth @talking2mouth "I do not believe my grandson deserves his spot in this school."

red @surprised "What?"

oak @talking2mouth "He is arrogant, cruel, and utterly refuses to learn, even from his betters."
oak @closedeyes talking2mouth "Further, though I've tried, I barely have a relationship with the boy. He calls me on holidays where I'm expected to send him money, and that's it."
oak @talking2mouth "His skill at training Pokémon is undeniable, but that does not excuse his callous disregard for everyone but himself."

oak @sad "Unfortunately, I know all too well where he got these traits from. I was not the best father to {i}his{/i} father... but even so."

oak -angrybrow -angrymouth @closedeyes talking2mouth "In any case, lad, Blue was not a consideration in my silence on this matter."

red @surprised "Then... you didn't tell me... because you were going to recommend me anyway."

oak @happy "There we go!"

red @sad "But Sam, I spent so much time writing those letters, and applying, and worrying about whether I'd get in..."

oak @happy "Well, if I'd told you that I was going to recommend you, perhaps you wouldn't have tried so hard." 
oak @angrybrow happymouth "In any case, you're eighteen, out of school, and unemployed. I can't imagine that wasted time would have been put to good use. Did I make you miss a daily run or two?"

red @angry "Yes, actually!"

oak @closedeyes talking2mouth "Hardly something worth caring about at this junction, I imagine."

red @closedeyes talking2mouth "[ellipses]You could be a bit more empathetic."

oak @talking2mouth "Not with how limited {i}my{/i} time is."
oak @talkingmouth "Speaking of, you now have enough evidence, I believe, to answer your first question. 'Why are you here?'"
oak @talking2mouth "Think it through."

red @thinking "[ellipses]{nw}"
extend @talkingmouth " I'm here because you recommended me. But, wait..." 
red @closedbrow talking2mouth "Kobukan is prepared to teach a complete newbie to Pokémon training, but it still demands that you have high grades when it comes to math, science, literature... and a life outside school, too."
red @talkingmouth "I don't. There's no way I could have gotten in with {i}just{/i} your recommendation."
red @surprised "You... forced me in, somehow."

oak @closedeyes talkingmouth "Yes, and the 'how' is not something that will be relevant, so you can end your train of thought there."

red @sad "Then... why? {w=0.5}{nw}"
extend @closedeyes talking2mouth "Nevermind, you'll just tell me to figure it out."

oak @happy "True."

red @closedeyes talking2mouth "So... there had to be some reason you wanted me here at the school. If it's not grades, not extracurriculars... what do I have?"
red @surprisedeyes talking2mouth "Oh! It's my memory, right? Being able to memorize every Pokémon, and all their stats and moves and stuff?"

oak @talking2mouth "No. It's related, but most of the professors at this school have done that. Further, it's nothing that anyone with a Pokédex couldn't do."
oak @talkingmouth "Of course, your aptitude at memorization, of all things, is rather impressive. Most people have to use a Pokédex for that, so having it all memorized is convenient... though I seem to recall that wasn't your choice?"

red @sad "Yeah... I really wanted a Pokédex, but neither my Mom nor I were trainers, so it didn't seem worth it to drop the money on it."

oak @talkingmouth "Well, I take your memorization as proof my decision not to give you a Pokédex was the right one."

red @surprised "Wait, you didn't give me a Pokédex on purpose?!"

oak @happy "Now, lad, next guess?"

red @closedbrow talking2mouth "Hm..."
red @surprised "Oh! It's the Pokémon thing, isn't it? Like, the way they're all calm around me."

oak @talkingmouth "Ah, so you've picked up on that. Well, that's partially correct, but it's more a symptom of a larger reason."

pause 2.0

redmind @unamusedbrow unamusedmouth "This conversation could have been an email."

pause 2.0

oak @talking2mouth "Well, lad?"

red @closedeyes talking2mouth "Please, Sam. I get that you're smart. Everyone else does, too. You're literally world-famous for it. Please, just tell me..."

pause 1.0

oak @talkingmouth "Very well. You are aware that the focus of my research has been Pokémon and human relationships, yes?" 
oak @talking2mouth "Well, you represent a breakthrough--something that could further the bonds between Pokémon and human more than ever before." 
oak @angrybrow talkingmouth "Lad, I believe you may possess a special ability."

red @surprised "Huh? Like, a Pokémon ability?"

oak @talkingmouth "Very much like that, yes. My colleague in Sinnoh has some interesting theories about the commonalities of human and Pokémon ancestry, incidentally... {w=0.5}but that's neither here nor there."

red @confusedeyebrows talkingmouth "Okay, am I taking crazy pills, or... humans can't have abilities. That's just not a thing. Right? I mean, am I wrong?"

oak @talkingmouth "The answer to that question has been the subject of my research for almost two decades. Certainly, there are many documented cases of human beings with Psychic powers." 
oak @closedeyes talkingmouth "Some have been known to talk to Pokémon, or heal their injuries with a touch."
oak @talkingmouth "Others demonstrate extreme physical strength beyond the norm, and others have brainpower that exceeds our understanding of anatomy. The answer I'm arriving at is... well, {i}yes{/i}, [first_name]."
oak @angrybrow talking2mouth "[first_name], people and Pokémon like you. Instantly. From the moment they lock eyes with you, they want to know you. I call this ability 'Frienergy.'"

red @surprised "...Isn't that just normal?"

oak @sadeyes sadeyebrows talking2mouth "It's hard to say. In my reclusive life as an academic, then researcher, I can certainly say people don't tend to initiate conversations with me. But that could easily be my own failing."

red @closedeyes talking2mouth "...I'm sorry, Professor. I don't think you're right about this. I don't have some kind of... superpower. Some kind of aura. I just go up to people, introduce myself, then ask their name. It's really that simple."

oak @talking2mouth "Lad, the difference between you and other people is far greater than can be explained by simple extroversion. No, I maintain my hypothesis is correct, and unless the data proves me wrong, I intend to maintain it."

red @confusedeyebrows talking2mouth "The data? What do you--"
red @surprised "That's why!"

show oak surprisedbrow frownmouth with dis

red @angry "You brought me here just to test your theory?! Not because of anything I can do, or what I deserve, just because you wanted to prove yourself right?"

oak sad "Er... yes. I don't understand. Why are you upset with me?"

red @angry "Why am I upset?! I'm upset because--"

redmind @thinking "Woah, there. Slow down, [first_name]. You know you need to be patient with Sam."

red @closedeyes talking2mouth "I'm upset, Sam, because it sounds like you don't think I deserve to be here. That you just brought me here so you could answer your own, personal, questions."

oak -sad @angrybrow angrymouth "[ellipses]"
oak @angrybrow talking2mouth "I don't know if you deserve to be here. Neither do you. No-one does, until you graduate or fail."

red @closedeyes talking2mouth "{i}Sigh...{/i} Yeah, alright. You're right, of course."
red @talkingmouth "Well, how can I help you in your research, then?"

oak @happy "Graduate! In four days, you've been introduced to more people than you knew in your entire life in Pallet Town."
oak @happy "If my hypothesis is correct, by the time you graduate, you should have a great many friends, and a team of strong, loyal, Pokémon."

pause 2.0

red @angrybrow talking2mouth "...Sam. If you're right, does that mean I'm mind-controlling people to like me?"

oak @closedeyes talking2mouth "I thought you might be concerned about that, so I made sure to discover the answer to that before there was ever the chance I'd tell you about my theory."
oak @talkingmouth "No, lad, far from it. Rather, your true feelings become apparent to anyone you talk with. It's more than wearing your heart on your sleeve. It's giving your heart to another."
oak @talkingmouth "People and Pokémon subconsciously know how you're feeling, and even what you're thinking, to a certain degree. And because of that, they know you're just a friendly boy that's safe to be around."
oak @closedeyes talking2mouth "In any case, I hypothesize this is an ability that would be actively detrimental in the hands of anyone who wasn't as kind as you. And useless to anyone who wasn't as outgoing." 
oak @angrybrow talking2mouth "I repeat, this is not mind control, nor does it {i}make{/i} people like you. It just means your intentions won't be misunderstood. And when you tell the truth, people believe it."
oak @sad "In a world where everyone wants something out of someone else, and no-one says what they mean, being able to know the intentions of the person you're talking to is... reassuring."

red @talking2mouth "Wow. So... my Pokémon don't freak out because they know I'm not going to try and control them, or abuse them, or... be a jerk, basically?"

oak @talkingmouth "That's my theory. Based on that special Pikachu I gave you, and how I've seen wild Pokémon interact with you, the effect seems especially pronounced on Pokémon."

red @sad "What if... like, what if I were to lie to someone, then? Would they believe me then, too?"

oak @happybrow "[ellipses]{nw}"
extend @talking2mouth "Lad, when was the last time you lied to anyone? About anything?"

red @closedeyes talkingmouth "Fair enough."

oak @talking2mouth "Don't worry about things that won't happen. Though if you must, I theorize that people are far more likely to {i}disbelieve{/i} your lies."

red @closedbrow talking2mouth "I guess... it still feels kinda uncomfortable, though. Like I'm getting an unfair advantage in life."

oak @closedeyes talkingmouth "Then feel free to put it out of your mind. Ignore my ramblings, assume you're a bog-standard student, and just do your best at this school that you got into fairly and squarely."

red @happy "Can't really do that, now."

oak @happy "Well, there you have it, then. Now, I really must be getting back to work."

show oak:
    xpos 720
    ease 1.0 xpos 200

red @surprised "Wait!"

show oak surprisedbrow frownmouth with dis:
    xpos 200
    ease 0.5 xpos 960

oak -surprisedbrow -frownmouth -surprised @surprisedeyes surprisedeyebrows talking2mouth "Yes, lad?"

red @talking2mouth "Not everyone likes me. I met a couple of trainers on my first day here. I told them about my... circumstances here, and they pretty clearly lost interest. But that's not all."

oak @surprised "Oh?"

if (IsNamed("Sabrina")):
    red @talkingmouth "Yeah, there's a girl in one of my elective classes. Sabrina. She told me to stay away from her."

    oak @closedeyes talkingmouth "Mm, that makes sense. I'm familiar with her. The Esper, yes?"
    oak @talkingmouth "I believe that her situation is unique. She probably doesn't even notice your own subtle empathic ability, given how much stronger her own telepathy is."

    red @talking2mouth "Okay. Well, that's one explanation. But there's another person."

red @closedbrow talking2mouth "There's Lance.{w=0.5} Uh,{w=0.25} Mr. Lance,{w=0.25} I guess? He got seriously angry at me."

oak @happy "Oh? Now, I'm sure that's not true. Lance is stern, and stubborn, but I'm sure it's far from his ability to dislike a promising young student such as yourself."

redmind @thinking "...Guess Sam wasn't there for the Battle Exhibition, then."

red @talking2mouth "Well, there's one more."

red @closedeyes talking2mouth "Blue. He hates me. Always has."

oak @closedeyes talking2mouth "My grandson is...{w=0.75} a statistical anomaly. Well within the margin of error. And, if I'm to prove my hypothesis of eighteen years correct, not worth considering."

red @frownmouth "Hmm..."

redmind @thinking "I feel kinda bad for Blue, whenever I hear how his grandfather talks about him... but it's not like he doesn't deserve it."

red @closedeyes talkingmouth "Well, I guess I've got one more question, then."

show oak surprisedbrow frownmouth with dis

red happy "How am I going to pay for Kobukan? My first tuition payment is due in six months."

stop music

pause 2.0

hide red
oak sad "{cps=10}Er... to be honest, lad, I didn't think of that...{/cps}"

pause 2.0

show research 
show red surprisedmouth deadeyes surprisedeyebrows at Transform(xpos=0.08, yanchor=0.35), monochrome
with vpunch

red "WHAT."

show red at Transform(xpos=0.08, yanchor=0.35):
    xpos 0.08 ypos 1.0
    parallel:
        ease 2.0 ypos 1.5
    parallel:
        ease 0.5 xpos 0.12
        ease 0.5 xpos 0.04
        repeat 5

pause 3.0

show research with vpunch

pause 2.0

hide red
redmind uniform @thinking "{cps=10}...Shit.{/cps}"

pause 1.0

show blank2 with dis:
    alpha 1.0

show oak:
    xpos 960 alpha 1.0
    ease 0.5 xpos 0 alpha 0.0

$ renpy.pause(1.5, hard=True)

hide oak

redmind @thinking "[ellipses]"
redmind @thinking "Is what Professor Oak said really true?{w=0.5} Do I really have some sort of... ability?"
redmind "Cheren said I had... 'inoffensive charisma.' Is that what he meant?"
redmind "And... is there some way I can use it to not get kicked out of Kobukan in six months?"

window hide

stop music fadeout 1.5

$ renpy.transition(dissolve)
call clearscreens from _call_clearscreens_37

$ renpy.pause(3.0, hard=True)

show night at vspaz

pause 3.5

hide night

############################################################################################################################################################################################################################
#### 3. END OF DAY #########################################################################################################################################################################################################
############################################################################################################################################################################################################################

play music "Audio/Music/SoaringIllusions_Intro.ogg" noloop
queue music "Audio/Music/SoaringIllusions.ogg"

$ renpy.transition(dissolve)
show screen currentdate

$ PlaySound("Door_Open1.ogg")
scene dorm_B norm with Dissolve(2.0)

show dorm_table

hide blank2

redmind uniform @thinking "Good, no-one's back yet.{w=0.5} I want to talk to [pika_name] about my[ellipses] condition."

$ renpy.music.play("Audio/Pokemon/pikachu_excite2.ogg", channel="altcry", loop=None)

pikachu neutral_2 "Pika!"

red @talkingmouth "Hey there, buddy!{w=0.5} Did you miss me?"

$ renpy.music.play("Audio/Pokemon/pikachu_sad.ogg", channel="altcry", loop=None)

pikachu angry_2 "Pikaaaa."

red @talkingmouth "Yeah, sorry, but you'll have to get used to it.{w=0.5} I've got to keep this up for the rest of the year, remember?"

$ renpy.music.play("Audio/Pokemon/pikachu_angry2.ogg", channel="altcry", loop=None)

pikachu angry_3 "Pi!"

red @sadbrow talkingmouth "Aw, come on, lighten up!"
red @talkingmouth "Once my schoolwork starts clearing up, you won't even notice that I'm gone!{w=0.5} It'll be just like high school!"

$ renpy.music.play("Audio/Pokemon/pikachu_norm3.ogg", channel="altcry", loop=None)

pikachu happy_2 "Pika."

redmind @thinking "I'm saying that, but if Professor Oak is right, I need to start reevaluating myself as a Pokémon Trainer...{w=0.5} And myself as a person."

$ renpy.music.play("Audio/Pokemon/pikachu_question.ogg", channel="altcry", loop=None)

pikachu "Pika?"

red @closedbrow talking2mouth "Yeah, I got some news. Really big news. Just give me a second to sit down.{w=0.5} It's been a long day."

show dorm_B behind dorm_table:
    yalign 0.0
    ease 0.04 ypos -10
    ease 0.04 ypos 10
    ease 0.04 ypos 0
show dorm_table:
    yalign 0.0
    ease 0.04 ypos -10
    ease 0.04 ypos 10
    ease 0.04 ypos 0

pause 0.1
$ PlaySound("Thud2.ogg")

pause 1.5

redmind hatless casual @thinking "I feel like I could just sink right through this bed right now..."
red @closedbrow talking2mouth "{i}*Sigh*...{/i}"

pikachu neutral_3 "[ellipses]"

redmind @thinking "[ellipses]"
redmind @angry "Ugh, what the hell!{w=0.5} I can't sit still after all that!"

$ renpy.music.play("Audio/Pokemon/pikachu_pikapika1.ogg", channel="altcry", loop=None)

pikachu neutral_4 "Pika pika?"

red @wince talkingmouth "Look... Sam thinks that I have some kind of 'ability' that makes people... {i}like{/i} me."

$ renpy.music.play("Audio/Pokemon/pikachu_confused.ogg", channel="altcry", loop=None)

pikachu neutral_4 "Piiika...?"

red @talking2mouth "Okay, fine, he explicitly said it {i}wasn't{/i} an ability that makes people like me, but, still! It really feels like it."

$ renpy.music.play("Audio/Pokemon/pikachu_confused2.ogg", channel="altcry", loop=None)

pikachu surprisedbrow frownmouth @surprised "Piii-KA?!"

pause 2.0

red @talking2mouth ".{w=0.25}.{w=0.25}.Hey. Buddy. Are you, like, actually... my friend? Like, I'm not forcing you into this because of mind powers, right?"

$ renpy.music.play("Audio/Pokemon/pikachu_happy2.ogg", channel="altcry", loop=None)

pikachu happy_2 "Piiiikaaaa.~"

red @thinking "[ellipses]"
red @happy "Yeah. Okay. I trust you, buddy. And if Sam's right... and I've never known him to be wrong... then there's nothing shady or evil about this." 
red @talking2mouth "...Maybe the best strategy is really to just assume he's wrong and carry on as I was before."

red @talkingmouth "Hmm..."
red @talkingmouth "Say, [pika_name]. You haven't spent much time with [starter_name], right?{w=0.5} Would you like to?"

$ renpy.music.play("Audio/Pokemon/pikachu_norm1.ogg", channel="altcry", loop=None)

pikachu neutral_2b "Pi Pikachu!"

red @talkingmouth "All right, come on out, [starter_name]!"

$ PlaySound("Pokemon/Ball sound.ogg")

$ renpy.pause(0.5, hard=True)
$ renpy.music.play(startercry, channel="altcry", loop=None)

starter @talkingmouth "[starter_species_name]!"

redmind "Now that I think of it, this is the first Pokémon that I've kept in a Poké Ball." 
redmind "I know they're perfectly comfortable, but I think living with [pika_name] for so long makes me feel bad keeping a 'mon in a Poké Ball..."

$ startergenderpronoun = "he" 
if (playerparty[0].GetGender() == Genders.Female):
    $ startergenderpronoun = "she"
elif (playerparty[0].GetGender() == Genders.Unknown):
    $ startergenderpronoun = "it"
redmind "In any case, [startergenderpronoun] sure looks happy to get out of that ball for some fresh air."

$ renpy.music.play("Audio/Pokemon/pikachu_norm1.ogg", channel="altcry", loop=None)
pikachu neutral_2 "Pika! Pi Pikachu!{w=0.5}{nw}"

extend pikachu " Pi pikachu pi...?"

$ renpy.music.play(startercry, channel="altcry", loop=None)

$ starter_species_name = pokedexlookup(starter_id, DexMacros.Name)
$ starter_fragment = starter_species_name[:3]
starter @talkingmouth "[starter_fragment]! [starter_species_name]!"

$ renpy.music.play("Audio/Pokemon/pikachu_excite2.ogg", channel="altcry", loop=None)

pikachu happy_2 "Pika!"

redmind "Riveting dialogue."
redmind "At least [pika_name] looks happy to have another Pokémon to hang out with.{w=0.5} That's a relief."
redmind "I was worried that [pika_name] would have trouble meeting new Pokémon.{w=0.5} Or that he'd get jealous over being 'replaced' or something."

$ renpy.music.play("Audio/Pokemon/pikachu_happy3.ogg", channel="altcry", loop=None)

pikachu happy_3 "Pipipi... Pika!"

show starterportraitfull behind dorm_table:
    subpixel True
    alpha 0.0 xzoom -0.4 yzoom 0.4 ypos 575 xpos 330
    parallel:
        ease 0.5 alpha 1.0
    parallel:
        pause 0.12
        block:
            parallel:
                ease 0.25 ypos 565
                ease 0.1 ypos 575
                repeat
            parallel:
                ease 0.25 xpos 320
                ease 0.1 xpos 315
                ease 0.25 xpos 320
                ease 0.10 xpos 330
                repeat
    
show pikachu happy_3 behind dorm_table:
    subpixel True
    alpha 0.0 xzoom -0.45 yzoom 0.45 ypos 650 xpos 640
    parallel:
        ease 0.5 alpha 1.0
    parallel:
        pause 0.1
        block:
            parallel:
                ease 0.32 ypos 640
                ease 0.15 ypos 650
                repeat
            parallel:
                ease 0.32 xpos 630
                ease 0.15 xpos 630
                ease 0.32 xpos 630
                ease 0.15 xpos 640
                repeat

redmind "I wonder what Mom would think of this scene.{w=0.5} She'd probably think they're just babbling, but I can tell that they're definitely talking to each other."
redmind "Come to think of it, Mom could never understand what [pika_name] was saying."
redmind "She just throws wild guesses based on whether [pika_name] sounded happy, sad, or angry at the time.{w=0.5} Sometimes she gets it right... but more often not."
redmind "...Can this really just be because [pika_name] and [starter_name] trust me? Are other trainers so busy trying to get their Pokémon to {i}obey{/i}, they never learn to listen?"

show starterportraitfull:
    ease 0.2 ypos 575 xpos 330
    pause 0.5
    ease 0.5 alpha 0.0
    
show pikachu:
    ease 0.15 ypos 650 xpos 640 alpha 1.0
    pause 0.25
    ease 0.5 alpha 0.0

$ renpy.pause(0.75, hard=True)

red @talkingmouth "All right, it's time to hit the hay, guys.{w=0.5} I've got a busy day of pretending everything's normal tomorrow, so I should get to sleep early. And I want to go for a run when I wake up--clear my head."
red @happy "Come on back, [starter_name]."

$ PlaySound("Pokemon/Ball sound.ogg")

pause 1.0

red @talkingmouth "You, too, [pika_name]. Get some sleep.{w=0.5} You can play with [starter_name] tomorrow, okay?"

hide pikachu

pikachu neutral_2b "Pika!"

red @talkingmouth "Good night!"

window hide

pause 1.0

hide dorm_table
show dorm_B lightsout

pause 1.0

$ renpy.transition(dissolve)
call clearscreens from _call_clearscreens_38

show blank2 with transeye

stop music fadeout 1.0
$ renpy.pause(1.0, hard=True)

hide pikachu
hide starterportraitfull

hide dorm_empty_B
hide blank2

jump day010409