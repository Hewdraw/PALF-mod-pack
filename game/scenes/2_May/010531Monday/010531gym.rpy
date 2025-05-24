label gym010531:

stop music fadeout 1.5
queue music "Audio/Music/Gym_Start.ogg" noloop
queue music "Audio/Music/Gym_Loop.ogg"

$ renpy.music.play("Audio/school_crowd.ogg", channel='crowd', loop=True, fadein=1.0)

$ renpy.transition(dissolve)
show screen currentdate

scene gym with dis

$ renpy.pause(2.0, hard=True)

python:
    '''
    show alder with dis:
        xpos 0.66
    
    show bruno think with dis:
        xpos 0.33
    '''

show wally uniform with dis 

wally @talking2mouth "Um... [wally_name]?"

red uniform @talkingmouth "Yeah?"

wally @sad2eyes sadeyebrows talkingmouth "Do you know where Bruno and Alder are? Class starts in three minutes, doesn't it? They should be here before us."

red @sadbrow talkingmouth "Sorry, I've got no idea."
red @closedbrow talking2mouth "Hm. Maybe Whitney will know. She usually knows most of the gossip."

wally @sad2eyes talking2mouth "I'm... not sure I want to talk with her."

red @confused "Huh? Why?"

wally @closedbrow sweat talking2mouth "She just makes me uncomfortable."

red @angrybrow frownmouth "[ellipses]"
red @angrybrow talking2mouth "Wally, if you're saying--"

wally @sad2eyes talking2mouth "I mean, I was flattered the first time she made an outfit for me, but she keeps making all these, like, {i}really{/i} girly outfits for me, and I feel like I'm being a poor sport if I don't wear them in our Fairy class."
wally @sadbrow talking2mouth "I know I'm small, but I'm trying to bulk up, and all those ribbons are... I mean, they're not stopping me..."
wally @unamusedbrow unamusedmouth "[ellipses]"
wally @closedbrow talking2mouth "They're pretty demoralizing, though."

show ethan sadbrow frownmouth uniform:
    xpos 0.33

show wally surprisedbrow frownmouth with dis:
    xpos 0.5
    ease 0.5 xpos 0.66

ethan @sadbrow talkingmouth "'For every drowning man, there is a man parched.'"

pause 1.0

wally @sadbrow talkingmouth "Sorry?"

ethan closedbrow tears frownmouth @talking2mouth "So am I."

pause 1.0

hide ethan with dis

pause 1.0

show wally surprisedbrow frownmouth with dis:
    xpos 0.66
    ease 0.5 xpos 0.5

wally -surprisedbrow -frownmouth @closedbrow talking2mouth sweat "Uh, sorry. You probably didn't need to hear that."
wally @happy sweat "I'm going to try and get some triple battle training in before the teachers arrive." 

red @confused "Triple battles?"

wally @closedbrow talking2mouth "Yeah. Last week was double battles, so I think we're probably doing triple battles this week, if we're following the same schedule we did at the start of the year."
wally @happy "That's just a guess though. Don't put any money on me."

pause 1.0

wally @talkingmouth "I'll let you get back to[ellipses] um, waiting."

menu:
    "Alright, good luck.":
        pass

    "Let me join you.":
        wally @surprised "W-woah, really? You'd battle me?"

        red @happy "Sure. If Alder walks in in a minute, we can just end the battle, say whoever has the most Pokémon left is the winner."

        $ ValueChange("Wally")

        wally @happy "That's great! Thank you so much, [wally_name]. I'm sure battling the ace of the Battle Team will give me tons of experience."

        red @talkingmouth "I'll do my best to point out anywhere I think you can improve."
        red @winkbrow happymouth "Show me what you've got!"

        $ trainer1 = MakeRed(number=3)
        $ trainer2 = MakeTrainer("Wally", number=3)

        call Battle([trainer1, trainer2], uniforms=[True, True]) from _call_Battle_172
        $ RecordBattle("Wally2")

        if (WonBattle("Wally2")):
            show wally uniform closedeyes angryeyebrows frownmouth with dis

            wally "[ellipses]"

            wally @talking2mouth "Gosh darn it."

            pause 1.0

            $ ValueChange("Wally", 3)

            wally -closedeyes -angryeyebrows smilemouth @happy "[wally_name], thanks for that battle. I learned a ton, and I can tell my Pokémon have too. I really appreciate you taking the time to help me here."

            red uniform @sadbrow talkingmouth "It's completely alright."

            wally @talkingmouth "Do you have any tips?"

            red @closedbrow talking2mouth "Well, I see you're focusing on two types now, which is good. Fighting and Fairy are a strong combination."
            red @talking2mouth "Your Pokémon still seem pretty underleveled, though. And it didn't look like any of them knew the instructors' special moves."

            wally @sweat closedbrow talking2mouth "Sorry. After our last battle, I caught a bunch of new Pokémon, but haven't really had time to train them up."

            red @happy "It's alright. You know what to work on now. You just gotta make your numbers bigger."

            wally @angrybrow happymouth "Alright. I'll do that! Thank you. Thank you very much! I'll definitely do better next time!"

        else:
            show wally uniform surprisedbrow frownmouth with dis

            wally @talking2mouth "...Um, [wally_name], are you feeling alright?"
            wally @sadbrow talking2mouth "Did you cramp something? Do you have a tummyache?"

            red uniform @closedbrow talking2mouth "No, I just... ugh. Everyone has off days."

            wally @surprisedbrow surprisedmouth "Oh. Of course!" 
            wally -surprisedbrow -frownmouth @happy sweat "I know you normally do much better."

            red @sadbrow talkingmouth "Yeah... well, I'll {i}have{/i} to do better next time."

        queue music "Audio/Music/Gym_Start.ogg" noloop
        queue music "Audio/Music/Gym_Loop.ogg"

wally @surprisedbrow talking2mouth "Oh! There's Elite Four Bruno!"

red @confused "Huh? Why didn't I notice him before? He's pretty recognizable, so--"

pause 1.0

hide wally with dis

stop music fadeout 4.0


$ renpy.music.play("Audio/school_crowd.ogg", channel='crowd', loop=True, fadein=4.0)

show bruno professor with Dissolve(2.0):
    xpos -0.1 
    ease 2.0 xpos 0.5

pause 2.0

redmind @unamusedbrow unamusedmouth "Come on, what the hell is this?"

bruno @talkingmouth "Students, Gym Class will now commence. I--"
bruno surprisedbrow "[ellipses]"
bruno @talking2mouth "Why are you whispering? What is happening?"

serena uniform @talking2mouth sadbrow "{size=30}It is as though a beautiful star was snuffed from the sky.{/size}"

hilda uniform @sadbrow sadmouth "{size=30}I never thought I'd be {i}unhappy{/i} to see a guy in a long coat, but...{/size}"

bea uniform @sadbrow talking2mouth "{size=30}I fear Sir Bruno has left us. What stands there now is... something else.{/size}"

narrator "In spite of the general consensus that Bruno's new shirted appearance is deeply unsetting, no-one seems willing to mention it to him."

stop music fadeout 4.0 channel "crowd"

bruno -surprisedbrow @closedbrow talking2mouth "Hm. Please settle down."

queue music "Audio/Music/Gym_Start.ogg" noloop fadein 4.0
queue music "Audio/Music/Gym_Loop.ogg"

bruno "[ellipses]"

show bruno:
    xzoom 1.0
    ease 1.0 xzoom -1
    pause 1.0
    ease 1.0 xzoom 1

bruno @talking2mouth "Hm. Is Alder not here?"

sabrina uniform @poweredbrow frownmouth "[ellipses]"

show bruno surprisedbrow frownmouth with dis

sabrina @talking2mouth "He is not on-campus."

bruno -surprisedbrow @closedbrow frownmouth "Hm.{w=0.5}{nw}"
extend @talking2mouth closedbrow " This is concerning. Please allow me to place a phone call."

narrator "Bruno takes out an ancient-looking flip phone, and with great precision, punches in some numbers, his massive fingers dwarfing the tiny phone in his palm."

bruno @closedbrow talking2mouth "Alder? What is your location?"

pause 2.0

bruno @surprised2 "Unova?"
bruno @angrybrow talking2mouth "A week-long meeting with national champions in Castelia... I understand. You needed to accompany Champion Blanc."
bruno angrybrow @angrymouth "That being said, you know you are required to submit a PTO request for such things."

pause 2.0

bruno @angrybrow talking2mouth "You {i}cannot{/i} drop an edited calendar in Dean Drayden's mailbox. You must submit a PTO request through the instructor portal on the staff website."

pause 2.0

bruno @angry2 "Of course we have a website! I trained atop a mountain, under waterfalls, in rural Kanto, for ten years--there is no reason you should be struggling with this more than I!"

pause 2.0

bruno @closedbrow talking2mouth "Apologies, Champion. My temper got the better of me. I must meditate to re-attune myself."

pause 2.0

bruno -angrybrow @talking2mouth "You do not need to apologize, my friend. But[ellipses] I would not resent a case of Casteliacones."

pause 2.0

bruno closedbrow @talking2mouth "Goodbye."

narrator "Bruno closes his phone and sighs deeply."

bruno @talking2mouth "It seems, for the next week, I will be instructing this class alone. This is fine."

pause 2.0

bruno @talkingmouth "Students, sit down. Cross-legged. I will begin the lecture on focusing one's composure, so that you cannot be thrown off in battle."
bruno -closedbrow @closedbrow talking2mouth "Discipline is key in battle, as in life. Motivation is the weaker substitute for discipline. Duty is the weaker substitute for discipline."
bruno @closedbrow talkingmouth "You must ensure that once you have a plan, you follow it through to the very end. There is no plan that is benefited through the altering."

redmind @wince frownmouth "That's... not only demonstrably untrue, but also awful advice."
redmind @wince frownmouth "I think I know why Alder gives the lectures now."

bruno @talking2mouth "I apologize, that's hyperbole. That is not what I meant to say. Rather, I was trying to convey the idea that sticking to one's strategy is a key part of succeeding in the use of the strategy."
bruno @talking2mouth "Forethought is a valuable martial art, but it is ever better at defeating the past. I..."

pause 1.0

bruno @closedbrow talking2mouth "That makes no sense. Allow me to restart."

pause 1.0

bruno @talkingmouth "To battle with six Pokémon, you must learn to win with one. A battle is won on the back of the battles you do not partake in."

bea uniform @closedbrow talkingmouth "Bruno is incredibly wise."

bruno @closedbrow talking2mouth "No. No, I'm afraid that was nonsense. I have many talents, but public speaking is not one."
bruno @sadbrow talking2mouth "I have found myself entirely out-of-my-depth here--however, I believe I know how to address this. I will call another Professor to co-run this class for me for the rest of the week." 
bruno @talking2mouth "For the rest of today's lesson, though, I ask that you simply battle amongst yourselves."
bruno @sadbrow talking2mouth "I will assign partners, as is customary. And then I am going to stop talking." 
bruno @sadbrow talking2mouth "{size=30}My throat is sore.{/size}"

pause 1.0

bruno @talkingmouth "[first_name], your partner for this match will be... Klara. {size=30}Triple battle, please.{/size}"

hide bruno with dis

pause 1.5

show klara makeup hairpin uniform with dis

klara @happy "Hey, [first_name]!~ It's been so long!"

red @talkingmouth "Not really, but good to see you again, too!"

if (GetRelationshipRank("Klara") > 0):
    if (not HasEvent("Klara", "FirstBase")):
        red @sadbrow talkingmouth "Thanks for being cool about... you know. How our date ended."

        klara @happy "Hah, what? Don't be silly, [first_name]. I wouldn't hold that against you. I mean, you said no, and I totally respect that."
        klara @sadbrow talkingmouth "What kind of desperate loser would keep trying if you said no?"

        red @wince talking2mouth "Well, uh..."

    else:
        red @talkingmouth "I can't stop thinking about our date."

        klara @talking2mouth flirtbrow "Well, you can do a {i}lot{/i} more than just think about it, if you're interested."
        klara @winkbrow talkingmouth "I'm down for a second one any time. Or we could just cut to the chase. Whatever you want. I'm {i}very{/i} flexible."

        red @closedbrow lightblush talking2mouth "Ah... I'll keep that in mind."

else:
    klara @sadbrow talkingmouth "Really? With the way you keep avoiding going on that date with me, I kinda thought you hated me."

    red @sweat talking2mouth "No, it's not that, really, I just--"

    klara @sadbrow talkingmouth "It's fine. I get it. I know you have other friends. You can't pay attention to {i}all{/i} of them, all the time."
    klara @happy "Just remember that I'll always be there for {i}you{/i}!"

    red @sadbrow talkingmouth "Of course. Can't forget!"

klara @happy "Alright! Now, we'll battle! I'll show you in this battle that I'm the perfect partner for the Millennium Drop!"

red @sadbrow talkingmouth "I'm not sure I'm even going to join it yet. And, anyway, how's a battle going to prove that you're a good {i}contest{/i} partner?"

klara @happy "You'll see!~ Just keep your eyes on me and my adorable Pokémon!"

python:
    trainer1 = MakeRed(number=3)
    trainer2 = MakeTrainer("Klara", number=3)

call Battle([trainer1, trainer2], uniforms=[True, True], customoutfits=["", "hairpin makeup"]) from _call_Battle_173
$ RecordBattle("Klara1")

if (WonBattle("Klara1")):
    show klara shadow angrybrow frownmouth uniform makeup hairpin with dis

    pause 0.2

    $ ValueChange("Klara", 30)

    klara -angrybrow -shadow -frownmouth @happy "Wow! [first_name], you're really incredible. Such a strong battler {i}and{/i} such an amazing coordinator. You're really just the perfect guy, huh? I can't believe I found you first."

else:
    show klara surprised uniform makeup hairpin with dis

    klara -surprised @talkingmouth "Oh, wow! I[ellipses] won?"
    klara @happy sweat "I really wasn't expecting that!"

    red @closedbrow talking2mouth "Really? But your Pokémon were seriously strong. Give yourself some credit. You can definitely win with what you've got, even against Battle Team members."

    klara @restrainedbrow talking2mouth "...I'm glad {i}you{/i} can tell."
    klara @winkbrow talkingmouth "Don't worry about it, though. I know battling is your 'thing', and I'm sure it's super-embarrassing getting beaten by a Coordinator like me, but I bet you'll be even better as a Coordinator!"

red uniform @happy "Klara, I've literally never been in a contest before. Don't gas me up like that! I'll get a big head."

if (HasEvent("Klara", "FirstBase")):
    klara @flirtbrow talkingmouth "{size=30}That's not the only thing that's big...{/size}"
    klara @talkingmouth "Anyway, I can just {i}tell{/i} when someone has what they need to make it big as a Coordinator. And I can tell, beyond a shadow of a doubt, you do!"
else:
    klara @talkingmouth "I can just {i}tell{/i} when someone has what they need to make it big as a Coordinator. And I can tell, beyond a shadow of a doubt, you do!"

klara @talking2mouth "It would be a {i}really{/i} big waste if you didn't take advantage of that. You might regret not making the most of your time at Kobukan, even!"

red @closedbrow sweat talkingmouth "You... {i}really{/i} want me to do this, huh?"

klara @puppybrow talkingmouth "I want to watch you become World Contest Champion one day, [first_name]. Why should it always be a Hoennian? I bet you can do it, without even trying."

red @closedbrow lightblush talkingmouth "Geez, that's embarrassing."
red @happy "But, uh, thanks. I appreciate it. I'm still not sure if I'm going to participate, but your faith means a lot."

klara @closedbrow talkingmouth "Right. Of course!"
klara @happy "Well, when you decide to, just pick me as a partner, and everything will be fine, okay? We'll get those scholarships!"

pause 1.0

klara @talkingmouth winkbrow "Trust me. You'll have a good time if you partner with me."

pause 1.0

klara frownmouth @surprisedbrow talking2mouth "Hey, what's wrong? Why aren't you agreeing?"

red @closedbrow talking2mouth "Sorry, I kinda spaced out. It's a small thing, but I'm a bit confused about your team. You're... in the Bug and Water electives, right?"

klara "[ellipses]"
klara @talking2mouth "Yeppers."

red @confused "Okay, so, all your Pokémon are Bug and Water-type. Except for Slowpoke. It evolves into a Poison-type. And, when your Skorupi evolves, it'll still be a Poison-type, but it won't be Bug anymore." 
red @closedeyes confusedeyebrows sweat talking2mouth "Come to think of it, more of your team is--"

klara -frownmouth @happy "[first_name]? Earth to [first_name]? You're wrong, silly-billy!"

red @happybrow talkingmouth "Probably, but what am I wrong about?"

klara @happy "Slowpoke is a {i}Water{/i}/Psychic-type, cutie. You should know that, you're from Kanto, just like they are."

red @thonk "[ellipses]"

red @closedbrow talking2mouth "Sorry, I {i}really{/i} don't want to argue with you, but[ellipses] you have a Galarian Slowpoke."
red @sadbrow talkingmouth "They're pure Psychic-type."

klara @talkingmouth "Oh, I can think why you'd think that, because they don't spend as much time near water, but they're not. They're actually--"

show klara surprisedbrow frownmouth with dis:
    xpos 0.5 ypos 1.0 zoom 1.0
    ease 0.5 ypos 0.9 zoom 0.9

red @talking2mouth "Klara."

pause 1.0

red @talking2mouth "They're Psychic-type. They can evolve into Galarian Slowbro, or Galarian Slowking, which are both Poison/Psychic-type."

pause 0.5

red @sadbrow talkingmouth "I {i}promise{/i} I know this."

pause 1.0

klara @sadbrow talking2mouth "...Oh."

show klara surprisedbrow frownmouth with dis:
    xpos 0.5 ypos 0.9 zoom 0.9
    ease 0.5 ypos 1.0 zoom 1.0

klara puppybrow @closedbrow sadmouth "Yes, you're right. You're so right. I'm sorry, I shouldn't have lied. I just didn't want anyone thinking I used Poison-types."

red @surprised "What? Why? What's wrong with them?"

klara @talkingmouth "Nothing, of course. But... oh, it's so sad. I just have such a sad story about loving Poison-types."
klara @closedbrow sadmouth "I'm sorry. I don't think I can get into it right now. It hurts too much."
klara @puppybrow talkingmouth "I'll tell you when we team up for the Millennium Drop, okay? I'm really looking forward to telling you, actually..."
if (GetRelationship("Klara") != "L'Amour"):
    klara @happy "You might be the only one that can heal my aching heart. You won't leave your best friend hanging, right? You're better than that, no matter what Leaf said."
else:
    klara @happy "You might be the only one that can heal my aching heart. You won't leave your best friend hanging again, right? You're better than that, no matter what Leaf said."

hide klara with dis

pause 1.0

redmind @thonk "...Huh? What Leaf said? Did she say something?"

if (HasEvent("Leaf", "AcceptedConfession")):
    redmind @thinking "I didn't think the date went {i}that{/i} badly..."

else:
    redmind @thinking "I didn't think that trip to the Café went {i}that{/i} badly..."

show bruno professor think:
    xpos 0.5
with dis

pause 2.0

bruno -think @talking2mouth "It's the new outfit, isn't it?"

$ PlaySound("Complaining.ogg")

pause 2.0

bruno @talking2mouth "Understood. Tomorrow, things will go back to normal. I will be in my regular attire, and there will be a second instructor to handle the lion's share of the talking."

$ PlaySound("BellChime.ogg")

pause 2.0

show blank2 with dis

stop music fadeout 1.5

$ renpy.transition(dissolve)
call clearscreens() from _call_clearscreens_259

$ renpy.pause(2.0, hard=True)

$ HealParty()

scene blank2

$ renpy.music.queue("Audio/Music/DragonDenStart_B.ogg", channel='music', loop=False, fadein=6.0, tight=None)
$ renpy.music.queue("Audio/Music/DragonDenLoop.ogg", channel='music', loop=True, fadein=0.0, tight=None)

pause 2.0

scene gym 
show bruno professor:
    xpos 0.33
show rowan:
    xpos 0.66 xzoom -1
with Dissolve(2.0)

pause 1.0

bruno @talking2mouth "Doctor Nanakamado. Thank you for coming."

rowan @talking2mouth "Harrrumph! Bruno, it's quite right that you called me. And none of this 'Doctor Nanakamado' business, Rowan is quite fine. There's no man worth the time it takes to say his title."
rowan @angrybrow talking2mouth "That blasted ear doctor says I'm half-deaf already, so I don't want my ears filled with anything that wastes my time. And speak up!"

bruno @talking2mouth "Yes, Rowan."

pause 0.5

rowan @closedbrow talking2mouth "Now, there are a few things I noticed that will definitely need to be fixed, but not to worry. I'll get these kids right as rain by the end of the week."
rowan @angrybrow talking2mouth "That being said... very unreliable for Alder to just leave without warning us. That's not how a Champion should bandy about. Champion Cynthia would certainly never do such a thing."
rowan @closedbrow talking2mouth "Well, it's of no matter. It's been a while since I've been able to flex the old bones in gym class."
rowan @happy "Ah, makes me feel young again. How long ago was it that you took my job?"

bruno @closedbrow talking2mouth "Ten years, I believe."

rowan @surprisedbrow talking2mouth "Oh? That's right!"
rowan @closedbrow talking2mouth "Yes, I believe I taught Champion Cynthia in my last year as a Gym Instructor..."
rowan @happy "Wohoho! Not much reason to stick around after that, no? I'd peaked!"

bruno @closedbrow talking2mouth "This class may surprise you, Rowan."
bruno @closedbrow talking2mouth "I'm sure you've noticed in your homeroom, but this year's students are remarkably strong. Alder is keeping a special eye on Dawn Berlitz, [first_name] [last_name], and Wally Mitsuru."

rowan @surprisedbrow talking2mouth "Blast it, Bruno, why on Earth would you tell me that? Have we that time to burn?"
rowan @closedbrow talking2mouth "I don't give a bleeding Bidoof who Alder's keeping an eye on. I've got two eyes of my own, don't I?"
rowan @talking2mouth "I'll keep an eye on these students and make sure that they're living up to Kobukan's standards. And if there's anyone who stands out to me, I'll ensure they're fairly rewarded."
rowan @angrybrow talking2mouth "But if they do {i}not{/i} live up to this academy's standards, I will let them know in short order."
rowan angrybrow @talking2mouth "Until I see their performance with my own eyes, though, they're all the same--students who {i}aren't{/i} Champion Cynthia."

pause 1.0

rowan surprised "Now, a different matter--why are you wearing a shirt?"

scene blank2

pause 2.0
    
show afternoon at vspaz
    
pause 3.5

$ timeOfDay = "Afternoon"

show cafe behind blank2
$ renpy.music.play("Audio/bigcrowdloop.ogg", channel='crowd', loop=True, fadein=0.5)

stop music fadeout 1.5

queue music "Audio/Music/Route 1 Anime.ogg"

$ renpy.transition(dissolve)
show screen currentdate

hide blank2 with splitfade
$ renpy.pause(0.5, hard=True)

hide afternoon

jump lunch010531