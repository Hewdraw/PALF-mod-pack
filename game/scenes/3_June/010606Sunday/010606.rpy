label day010606:

$ timeOfDay = "Morning"
call clearscreens() from _call_clearscreens_269
call calendar(1) from _call_calendar_62


$ renpy.music.queue("Audio/Music/Pallet Town A.ogg", channel='music', loop=True, fadein=1.0, tight=None)

$ calDate = calDate.replace(day=6, month=6, year=2004)

$ HealParty()

stop music

scene blank2
show morning at vspaz

scene kitchen 
show yellow:
    xpos 0.66
show blue:
    xpos 0.33
with splitfade

red @talkingmouth "Morning, guys. Any coffee left?"

blue @talking2mouth "Not sure you deserve any for waking up so late, but Leaf didn't chug it straight from the carafe today, so yeah, there's a little."

red @talking2mouth "Huh. She {i}did{/i} come home last night, right?"

yellow @talking2mouth "Yep. She came home before you did, actually."

red @confused "Huh. I guess her party wrapped up sooner than she thought."

blue @closedbrow talking2mouth "She probably just killed the mood, and they sent her home early."

red @unamusedbrow unamusedmouth "[ellipses]"
red @closedbrow talking2mouth "I'm {i}really{/i} going to need that coffee."

red @talking2mouth "Anyway, any luck finding a contest fit yesterday, Yell'?"

yellow @talkingmouth "Not yet. I think we're getting closer, though."

red @talking2mouth "Oh, yeah? What kind of design are you thinking?"

yellow @sad2eyes talking2mouth "Um... something made of at least 90%% natural materials, where the craftsperson was compensated for their work, and preferably something biodegradable, so when I grow out of it--"

red @sweat talkingmouth "I think I get the vibe."

blue @talking2mouth "You doing anything big today?"

red @talkingmouth "Nah, just got a bunch of free time. Nice change of pace!"

blue surprisedbrow frownmouth @happy "Hah! If you've got free time in Kobukan, you're doing it wrong! You should--"

red @closedbrow talking2mouth "Save it for when I get back."

blue angry "Oh, don't think I won't! Because I {i}absolutely{/i} will!"

$ removestudents = { "Leaf" }

call freeroam() from _call_freeroam_43

stop music fadeout 1.5

call clearscreens() from _call_clearscreens_270

$ renpy.music.queue("Audio/Music/Pallet Town A.ogg", channel='music', loop=True, fadein=1.0, tight=None)

scene suitenight 
show blue wistfulbrow frownmouth:
    xpos 0.8 xzoom -1
show yellow sadbrow frownmouth: 
    xpos 0.6
show ethan sad2eyes angryeyebrows frownmouth:
    xpos 0.4
show brendan sadbrow frownmouth:
    xpos 0.2 xzoom -1
with splitfade

pause 1.0

red @confused "Uh... hi, guys. Hi, Brendan. What happened? Why are you here?"

if (HasEvent("Klara", "AgreePartner")):
    blue @talking2mouth "Nice partner you chose, [first_name]. Real nice."

    red @confusedeyebrows talking2mouth "I expected you to yell at me as soon as I got back to the dorm, but I really have no idea what you're yelling at me about here."

ethan @talking2mouth "You need to hear what Brendan has to say."

red @talking2mouth "Well, sure? Go ahead."

brendan @talking2mouth "Well, bro, it's like this. Last night, Leaf came to our study session, and..."

narrator "[ellipses]As Brendan tells the story of last night, your brow furrows deeper and deeper, and your fists start to unconsciously clench."

brendan -sadbrow @talking2mouth "...And I don't fully know, but I'm kinda getting the feeling that... Klara might've tricked Leaf, then splashed her on purpose."
brendan @talking2mouth "I don't think the other girls picked up on it, but I know Leaf. And Nessa talked with me after, and said... well, she thought something was off, too."
brendan @sadbrow talking2mouth "Klara said that Leaf just made a mistake, and, y'know, maybe she did. I don't really know."

pause 1.0

if (HasEvent("Klara", "AgreePartner")):
    narrator "Your head is swimming with mixed emotions. Partnering with Klara during the tryouts, you saw a side of her that you hadn't seen before."
    narrator "She seemed to truly love the stage, the spotlight, and coordinating, and her bond with her Pokémon was strong."

    pause 1.0

    narrator "Is it {i}truly{/i} possible that she had set out, {i}on purpose{/i}, to humiliate Leaf?"
    narrator "Or maybe this was truly just an awful misunderstanding, with both sides confused and hurt...?"

    pause 1.0

    narrator "Or is it possible that the truth is somewhere in the middle...?"

pause 1.0

red @talking2mouth angrybrow "I need to talk to Klara."

ethan @talking2mouth "There's no situation in which that's the call, dude."

blue @talking2mouth "Ethan's right. Stay here and help us figure out what we're going to do about this."

red @closedbrow talking2mouth "Sorry, guys. I have to."

pause 1.0

if (mayhaslarvesta):
    brendan @sadbrow talking2mouth "Be careful out there, man. Don't make any decisions you'll regret. Gettin' angry doesn't solve anything."

else:
    brendan @sadbrow talking2mouth "Be careful out there, man. I don't know if Klara's like this, but some people will just smile in your face and pull your chair out from under you."

red @closedbrow talking2mouth "I know. Where's her dorm?"

brendan @talking2mouth "Pledge Hall. 303."

pause 1.0

red @sad2eyes talking2mouth "I'll be back."

scene blank2 with splitfade

narrator "You march firmly toward Pledge Hall, uncaring of the rapidly-approaching curfew. If Cheren wants to cause a problem, he'll have a {i}much{/i} bigger problem on his hands."

narrator "Your mind is spinning, with possibilities, frustrations, and words that you hope you manage to sift through before you arrive at the dorm door."

pause 1.0

scene door with splitfade

narrator "Your feet carry you faster than your mind can process."

$ PlaySound("knock.ogg")

$ hideside = True

klara @talking2mouth "Hm? It's almost curfew. Who is it?"

TempCharacter("???") "Go check. Maybe it's the RA?"

show dooropen with dis

pause 0.5

show klara casual makeup hairpin with dis

klara @happy "Hi! Can I--"

hide dooropen with dis

klara surprisedbrow frownmouth "[ellipses]"

klara @talkingmouth "[first_name], what are you doing here?"

$ hideside = False

if (HasEvent("Klara", "FirstBase")):
    klara @talking2mouth "Are you[ellipses] you know, in the mood? My dormmates are home, but we could see if the pool's open?"

elif (HasEvent("Klara", "AgreePartner")):
    if (HasEvent("Game", "WonMDTryouts")):
        klara @talking2mouth "Did you want to go over our routine for the Millennium Drop again?"
    else:
        klara @talking2mouth "Have you been thinking about how we lost in the Millennium Drop? Me too[ellipses]?"

red @talking2mouth "What happened with Leaf?"

klara @talking2mouth "Leaf[ellipses]? Oh, right, Leaf!"
klara sadbrow @talkingmouth "It was just an {i}awful{/i} accident. I was planning a party for next weekend. Bunny-themed, and all the girls were going to come wearing bunny suits. It would've been really cute and sexy."
klara @sadmouth "But... Leaf got the date wrong. She came yesterday, instead of next Saturday. She walked in right when I was in a study group with my Water-type classmates."
klara @talking2mouth "It was an innocent mistake--{i}I{/i} was totally willing to overlook it, but Leaf got really[ellipses]"

pause 1.0

klara @closedbrow talking2mouth "Well, {i}I{/i} didn't say it, but the people I was studying with said 'bitchy.'"

pause 1.0

if (HasEvent("Klara", "AgreePartner")):
    narrator "It is {i}hard{/i} to believe that this was an accident. But[ellipses] if it was, even if there was even the {i}smallest{/i} possible chance, it's worth pursuing to the end."
    narrator "One thing you are certain of is that yelling at Klara will not make Leaf feel better, will not make Klara feel guilty, and will not make your chest stop hurting."
    narrator "There must be another way to handle this--one that results in the least amount of harm for everyone."

    show klara surprisedbrow frownmouth with dis

    red @sadbrow talking2mouth "Klara, I'm really sorry."

    pause 1.5

    klara @talking2mouth "{size=30}Wh-{/size}What?"

    red @talkingmouth "This sounds like... a {i}huge{/i} mistake. It's incredibly unlikely, and that makes it even harder to believe it really was."

    klara frightenedbrow @sadbrow talking2mouth "Oh, so you don't--"

    red @talking2mouth "But I believe you. And I'm sure you must be {i}really{/i} hurting inside, that there are people who think you'd do something like that to your friend, when you were just trying to set up a fun party."

    klara -frightenedbrow @talking2mouth "I[ellipses] yeah. Yeah, um, I'm really[ellipses] upset."

    red @sadbrow talkingmouth "I know there are a lot of hurt feelings on both sides. Leaf is {i}really{/i} upset, and I believe you when you say you are too."
    red @talking2mouth "But I promise I'll do my best to make this right--to sort these hurt feelings out for everyone."
    red @sadbrow talkingmouth "I don't know how I'll do it, but[ellipses] like you always say, you like me because I follow through when I promise something."
    red @happy "So you know what my promise means."

    klara @talking2mouth "Wait, wait, sorry, {i}stop{/i}. I'm confused. Are you--are you messing with me, right now?"

    red @confused "N-no?"
    red @sadbrow talkingmouth "No, I really {i}do{/i} promise I'll figure out how to make both of you feel better. Your friendship shouldn't end because of this awful mistake."
    red @sadbrow talkingmouth "And neither should our partnership in the Millennium Drop, you know?"

    klara poutmouth "[ellipses]"

    red @sweat talking2mouth "I think the first step is probably an apology. On both ends."

    klara @angrybrow talking2mouth "Oh, no, Leaf will {i}never{/i} apologize. She's {i}so{/i} stubborn, and she has it out for me, now."

    red @talking2mouth "I'll work on her. It'll take some time before she's ready, and I wouldn't blame you if it takes you some time, too."
    red @sadbrow talkingmouth "But I believe in both of you. I know you'll get there."

    pause 1.0

    klara restrainedbrow @shadow closedbrow talking2mouth "What is {i}happening?!{/i}"

    red @talkingmouth "We're going to rebuild this bridge, Klara. Stronger than it was before. And we'll come out of this laughing."

    pause 1.0

    red @sweat talking2mouth "There's just one thing I gotta check. You were just trying to throw a party, right? Like, that innocent desire is where this all came from?"

    klara @talking2mouth "Y-yeah."
    klara @closedbrow talking2mouth "Oh, but I cancelled next week's party. I think it would be too awkward, now."
    klara surprisedbrow frownmouth @sadbrow talkingmouth "I mean, the first person I invited freaked out at me, so--"

    red @happy "I got it. Thanks, that's all I needed to know."

    klara @talking2mouth "Y-yeah. Sure."

    if (HasEvent("Game", "WonMDTryouts")):
        red @talkingmouth "I'll see you later--we still need to go over some parts of our contest routine, right?"
    else:
        red @talkingmouth "I'll see you later. Just 'cause we didn't get into the Millennium Drop doesn't mean we can't hang out, right?"

    klara @sadbrow talkingmouth "Yeah. Um, I mean[ellipses] 'Yeppers!'"

    narrator "You leave."

    pause 1.0

    klara frightenedbrow frightenedmouth "What the hell was that? That's not how the conversation was meant to go. That's not how this was meant to go at all!"

else:
    narrator "It is {i}hard{/i} to believe that this was an accident. Given what Klara said at the tryouts, a grain silo's worth of red flags that you had adamantly denied the existence of begin to pop up, forcing themselves into your sight."
     
    pause 1.0

    narrator "You sigh, and prepare to say a series of words that taste strange, and unfamiliar, in your mouth."

    pause 1.0

    show klara surprisedbrow frownmouth with dis

    red @angrybrow talking2mouth "I do not believe you."

    pause 1.0

    klara sadbrow @talkingmouth "{size=30}I guess even the perfect boy has a limit[ellipses]{/size}"
    klara @talking2mouth "Well[ellipses] I'm really sorry to hear you have those trust issues, [first_name]. I just trust everyone. Which is why it hurt me so much when you said you weren't going to be my Millennium Drop partner."
    klara @talking2mouth "I was relying on you, you know? If you don't keep your promises to people, they won't want to be your friend."

    red @talking2mouth "Is that why you did this? Because I didn't partner with you?"

    klara @sadbrow talkingmouth "[first_name], I didn't do {i}anything{/i}. Leaf did this. It was {i}her{/i} mistake. That's what happens when you don't listen to the people around you--you make embarrassing mistakes like this."

    pause 1.0

    red @angrybrow talking2mouth "Stop blaming Leaf."

    pause 1.0

    klara @shadow talking2mouth "Then maybe it was {i}you{/i}. Maybe I was so upset that you ditched me that I told her the wrong time, just once. {i}Maybe{/i} that's what she heard, which is why she thought it was a week early."
    klara @shadow angrybrow talkingmouth "Maybe if you'd just played along with me, if you'd just stood there and let your power win us the tryouts, maybe this awful mistake wouldn't have happened. I don't really know."
    klara @happy "All I know is that I don't think {i}either{/i} of you two are as good friends as I thought you were."

    red @talking2mouth "Why?"

    pause 1.0

    klara surprisedbrow frownmouth @talkingmouth "Why?"

    red @talking2mouth "This isn't just because I didn't partner with you. It {i}can't{/i} just be that. So why?"

    pause 2.0

    klara -surprisedbrow @talking2mouth "Partner with me in the Millennium Drop. I passed the tryouts, even without your help. You can get us to the end. If you let me take the scholarship, I'll give you your 'why.'"
    klara @closedbrow talking2mouth "Leaf's mistake doesn't have to get between us working together."

    pause 2.0

    red @talking2mouth "There's no chance in hell I'm working with you."

    if (HasEvent("Game", "WonMDTryouts")):
        if (HasEvent("Yellow", "AcceptPartner")):
            red @talking2mouth "Yellow and I are going to win the Millennium Drop--and we're going to be the one preventing you from getting any one of those scholarships."
        else:
            red @talking2mouth "I'm going to win the Millennium Drop--and I'm going to be the one preventing you from getting any one of those scholarships."
    elif (not HasEvent("Yellow", "AcceptPartner")):
        red @talking2mouth "Yellow's going to win the Millennium Drop--and she's going to be the one preventing you from getting any one of those scholarships."
    else:
        red @talking2mouth "Someone else is going to win the Millennium Drop. I don't know who, and I don't know how, but I know you're not going to get any one of those scholarships."

    red @talking2mouth "Keep that 'why' until you're {i}really{/i} desperate. Because I promise you will be."

    klara "[ellipses]"

    klara @talking2mouth "I just don't understand why you're being {i}so mean{/i} to me. I'm just a sweet and innocent girl[ellipses]"

    red @angrybrow shadow frownmouth "[ellipses]"

    narrator "You leave."

    if (GetValue("Klara") != 0):
        $ AnimateValueChange(-GetValue("Klara"), 0.5, True)

    klara sadbrow poutmouth "Aw, now {i}he's{/i} made a mistake, too[ellipses]"
    
scene blank2 with splitfade

if (not (HasEvent("Klara", "BrokeBond") or HasEvent("Klara", "AgreePartner"))):
    narrator "You're confused and hurt. The one thing you {i}can{/i} understand, though, is that your understanding of Klara was entirely incorrect."
    narrator "[bluecolor]Your bond with Klara has been revealed to be fake.{/color}"

    python:
        AddEvent("Klara", "FormerBond" + str(GetValue("Klara")))
        AddEvent("Klara", "BrokeBond")
        persondex["Klara"]["Mood"] = 0
        persondex["Klara"]["Value"] = 0
        persondex["Klara"]["Nature"] = TrainerNature.Special

pause 2.0

scene suitenight 
show blue wistfulbrow frownmouth:
    xpos 0.8 xzoom -1
show yellow sadbrow frownmouth: 
    xpos 0.6
show ethan sad2eyes angryeyebrows frownmouth:
    xpos 0.4
show brendan sadbrow frownmouth:
    xpos 0.2 xzoom -1
with splitfade

yellow @talking2mouth "You're back?"

if (HasEvent("Klara", "AgreePartner")):
    red @sadbrow talkingmouth "Yeah."

    yellow @talking2mouth "What did you learn?"

    pause 1.0

    red @talking2mouth "Bear with me, guys. I {i}really{/i} think there's at least a chance that this was just an {i}awful{/i} mistake."
    red @closedbrow talking2mouth "It might be that Klara mis-said the date once, or maybe Leaf misremembered[ellipses] either way, I don't think we want to do anything rash."

    ethan angrybrow @closedbrow talking2mouth "Dude, a mistake? A misunderstanding? C'mon, man, there's seeing the best in everyone, there's what Yellow does, and then there's what {i}you're{/i} doing. That's way too far. Klara's a psycho."

    yellow @talking2mouth "That's not the term I'd use, but... Ethan might be right."
    yellow @sadbrow talkingmouth "I try to see the best in everyone, but[ellipses] even I can't really see how this could {i}genuinely{/i} be an accident."

else:
    red @angryeyebrows closedeyes talking2mouth "Yeah."
    red @angrybrow talking2mouth "It's because I didn't partner with her in the Millennium Drop Tryouts. Not entirely, but[ellipses] that was definitely part of it. This is my fault."

    ethan angrybrow @closedbrow talking2mouth "No, dude, it's not your fault. Klara's just a psycho."

    yellow @talking2mouth "That's not the term I'd use, but... Ethan's right--it's not your fault."

pause 1.5

yellow @talking2mouth "About midday, I noticed that Leaf was still in her room. I knocked on the door, but... she's not answering, and it's locked."

blue @talking2mouth "We sure she's still in there?"

yellow @talking2mouth "I... eventually got her to speak when I said I was going to call Nurse Miriam in case she was having a medical emergency, but all she said was 'Don't. I'm fine.'"

ethan @talking2mouth "I hear water splashing every once in a while--and I think she's run out to the bathroom a couple times. I never saw her, though."

brendan @talking2mouth "That makeup she was using--that stuff's notorious for being {i}really{/i} hard to get off. It's great for contests, because no matter how much you sweat, it won't ever run, but..." 
brendan @sadbrow talking2mouth "You kinda need to scrub it with water for hours to even make a dent, and if it's on your face, then that's... I mean, I kinda get the idea that Leaf wouldn't want to do that?"

blue @closedbrow talking2mouth "As much as I hate to say this, maybe you should talk to her? I mean, of all of us..."

red @sadbrow talkingmouth "I can try."

show door with Dissolve(2.0)

$ PlaySound("knock.ogg")

pause 1.0

red @talking2mouth "Leaf?"

pause 2.0

if (HasEvent("Leaf", "AcceptedConfession")):
    red @talkingmouth sadbrow "Fael?"

pause 2.0

hide door with dis

red @closedbrow talking2mouth "It's really bad, guys. Normally, if she's feeling bad, she'll say she wants to die, or is going to leave the country, or something."
red @sadbrow talking2mouth "But... nothing but sniffles."

pause 2.0

if (HasEvent("Klara", "AcceptPartner")):
    red @talking2mouth "I'm trying to think of a way we can patch this up. Both of their feelings are really hurt[ellipses] there's gotta be a way we can mend that bridge, right?"

    narrator "The rest of the dorm shifts uncomfortably, avoiding eye contact."

    ethan @talking2mouth "I'm with you all the way, man, but, frankly, I kinda want to just do Blue's plan. What if you're wrong? What if Klara just wanted Leaf to feel really shitty for a week, and have to waterboard herself to get her makeup off?"

    red @talking2mouth "Then we don't lose anything by assuming the best out of everyone involved."

    ethan @sadbrow talking2mouth "Like I said, I'll support you, but I'm going to go ahead and say Leaf's going to be pissed to hear this."
    ethan @unamusedbrow talking2mouth "And it's kinda messed up that {i}I{/i} have to be Leaf's advocate here. Yellow, Baton Pass?"

    yellow @sadbrow talkingmouth "You[ellipses] I would've just said what you said."

    red @closedbrow talking2mouth "I promise that my plan will work out best for {i}everyone{/i}, if it works. Everyone--even Klara."

    pause 1.0

    brendan @talking2mouth "What's your plan, dude?"

    red @wince talking2mouth "My plan is to figure out a way to fix this situation in a way that works out best for everyone."

else:
    blue @angrybrow talking2mouth "I am going to battle the {i}shit{/i} out of Klara."

    ethan @talking2mouth "Form a queue, buddy."

    red @confused "Wait, you two--"

    ethan @closedbrow talking2mouth "We argue all the time, yeah, but this? {i}This?{/i} This was fucked up, man."

    show brendan sadbrow frownmouth with dis

    blue @talking2mouth "Klara can't treat a member of the Battle Team like that. Dumbass coordinator needs to remember her place."

    brendan @talking2mouth "Blue, I'm right here."

    ethan @talking2mouth "Don't take it personally, Branthony. Blue's incapable of saying something that might be considered 'nice' without getting a dozen other people caught in the crossfire."

    pause 2.0

narrator "The five of you all look at each other, helplessly. You shift your weight from foot to foot, and you scratch your necks. Someone coughs."

pause 1.0

ethan @talking2mouth "Well, what do we do?"

if (not HasEvent("Klara", "AcceptPartner")):
    blue @angry "We battle--"

    ethan @talking2mouth "Okay, yeah, we battle Klara, but what do we do {i}for Leaf{/i}? Because battling Klara won't make Leaf feel any better."

    blue @sad2brow talking2mouth "It'd make {i}me{/i} feel better."

pause 1.5

yellow @sad2brow talking2mouth "{size=30}Even she was embarrassed...{/size}"

blue @glancebrow talking2mouth "Huh? What was that, Amarillo?"

yellow @talking2mouth "I'm just... surprised. Surprised that Leaf, of all people, would be embarrassed to wear... well, {i}anything.{/i}"

brendan @talking2mouth "Well, it's, y'know, context. At an {i}actual{/i} bunny party, it would've been fine. Looked great--storebought, obviously, but it was a good fit, cute colors."

yellow @sad2brow talking2mouth "I thought she was... confident enough that she'd never feel embarrassed, though. Especially about something she was wearing. She's so beautiful..."

red @sadbrow talkingmouth "Nah. In fact, she gets embarrassed probably more than you do."

pause 1.0

yellow "[ellipses]"

pause 1.0

yellow angrybrow frownmouth @talking2mouth "Okay, we need to help her."

if (HasEvent("Klara", "AcceptPartner")):
    yellow @talking2mouth "Maybe... Klara, too."

    red @sadbrow talking2mouth "Thanks, Yellow. And, yeah, that's what we want to do. I just... we need a plan."

else:
    red @sadbrow talkingmouth "That's what we want to do, Yellow, but... I mean, how could we even...? We need a plan."

ethan @talking2mouth "Yeah, well, we don't have one. Leaf's the planner. We're just her little minions."

yellow @talking2mouth "Wait. You're... you're right, actually."

ethan -angrybrow @confused "What? I am?"

yellow @talkingmouth "Leaf plans for us. She's {i}always{/i} the one making the plan, and organizing us, bringing us together, leading us to some--{i}something{/i}."
yellow @angrybrow talking2mouth "But... the tailor needs clothes, too."
yellow @closedeyes talking2mouth "She's out. That means we need to step up. We need to plan without her--{i}for{/i} her."
yellow @angryeyebrows closedeyes talking2mouth "Come on. If we put our heads together, we can figure something out."

pause 1.0

ethan @frownmouth "[ellipses]"

brendan @closedbrow "[ellipses]"

red @thinking "[ellipses]"

blue -sad2brow -wistfulbrow @sad2eyes frownmouth "[ellipses]"

pause 1.0

yellow @closedbrow talking2mouth "The[ellipses] tailor[ellipses] needs clothes."

pause 1.0

yellow surprisedbrow @talking2mouth closedeyes angryeyebrows  "Whitney, in the Nurse course... she makes clothing. I can do some sewing as well, so that's two. But is that enough?"

brendan @talking2mouth "I'm not really sure what you're gettin' at, but if we're listing tailors, I make my own clothes, and my girlfriend's, too."

blue surprised "Wait, what {i}are{/i} you getting at?"

ethan @confused "Yeah, I'm lost."

yellow @closedbrow talking2mouth "The tailor needs clothes."

pause 1.0

show ethan surprisedbrow frownmouth 
show brendan surprisedbrow frownmouth
with dis

yellow -frownmouth angryeyebrows @challengingmouth "And the tailor needs a {i}lot{/i} of clothes, and she needs them before next Sunday."

pause 1.0

ethan @talking2mouth "Yellow, I am so {i}confused{/i}. What's going on?"

yellow @closedbrow challengingmouth "Let me answer your question with a question, in the style of the inimitable Professor Oak."

yellow @challengingmouth angrybrow "How comfortable are you with crossdressing?"

pause 2.0

ethan angrybrow happymouth "My time has come."

pause 3.0

scene blank2

pause 2.0

jump enddemo
jump demoend