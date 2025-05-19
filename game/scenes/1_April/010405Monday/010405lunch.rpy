label lunch010405:

$ timeOfDay = "Afternoon"

$ renpy.transition(dissolve)
show screen currentdate

queue music "Audio/Music/Road to Viridian City.ogg"
    
hide blank2 with splitfade

$ renpy.pause(0.5, hard=True)

show bianca uniform with dis

bianca @happy "Hey, cute guy in the red hat!"

red uniform @talkingmouth "That is my name, yes."

bianca @talkingmouth "Cheren wants to see you!"

red @confused "Already? I thought he was going to wait until after school."

bianca @happy "So did I! And so did he! And somehow we were all wrong! Isn't that weeeeeird?"

red @happy "You said it."
red @talkingmouth "Well, lead the way."

show blank2 with splitfade

hide bianca

narrator "You find your way to Cheren's table, surprised to see a few familiar faces there."
narrator "You're also surprised to see that this table, which was clearly designed to seat four, has six people crammed into it, not including yourself."
narrator "You awkwardly insert yourself in, and make small talk until Cheren clears his throat, pointedly."

cheren uniform @talkingmouth "Ladies and gentlemen. You're doubtlessly wondering why I've gathered you here today."

hide blank2 with splitfade

show cafeB_CG:
    subpixel True
    alpha 0.0 xalign 0.5 yalign 1.0 zoom 1.25
    parallel:
        ease 1.5 alpha 1.0
    parallel:
        ease 5.0 zoom 1.0

redmind "Not doing anything to dispel the 'Cheren is a mob boss' notion, then."

serena uniform @talkingmouth "May I assume you've somehow heard of my intentions towards the Student Council?"

cheren @talking2mouth "Yes, that's certainly part of it."

hide calem
hide hilda

cheren @talking2mouth "As I understand it, you, Calem, are still deciding as to whether or not to attempt election?"

calem uniform @talkingmouth "That's the short of it, yes."

hilda uniform @smirkmouth "So what are {i}we{/i} here for? Hilbert and I?"

$ BecomeNamed("Hilda")
cheren @happy "Excellent question, Hilda."
cheren @talkingmouth "You're here as representatives of the student body."
cheren @closedbrow talking2mouth "It wouldn't do to decide the future of the student body without the input of its constituents."

hilbert uniform @sadbrow talkingmouth "Pass."

hilda @angry "Hilbert!"

cheren @surprised "...I'm sorry, what?"

hilbert @talkingmouth "I don't represent anyone but myself. Besides, anyone who signs up for the Student Council is just setting themselves up for failure. This dump has way more problems than a dozen councils can solve."

cheren @angrybrow "{w=0.5}.{w=0.5}.{w=0.5}."
cheren @sad "I understand why you may feel that way. Doubtlessly, others will too. I would still appreciate your input, unenthusiastic though it may be."
cheren @happy "The 'jaded, apathetic voter' is still a demographic I'm trying to reach."

hilbert @sadbrow talkingmouth "[ellipses]Pfft. {w=0.5}{nw}" 
extend @talkingmouth "Whatever."

pause 1.0

red uniform @confused "Uh... why am I here, then?"

cheren @happy "Well, [first_name], when we spoke on Friday, you... {i}motivated{/i} me." 
cheren @talkingmouth "I thought I sensed in you something that could be very powerful if leveraged properly. A sort of... inoffensive charisma."

red @confused "Inoffensive? Thanks."

cheren @happy "It's a valuable skill!"
cheren @closedbrow talking2mouth "And I appreciate your willingness to move our scheduled meeting up. Turns out I was double-booked after school."
cheren @talkingmouth "In any case, [first_name], I invited you here because I wanted to hear your thoughts on whether you would consider running for Student Council."

if (council_campaigning):
    red @happy "Actually, I already am. I only decided this morning, but, yeah, I want to run."

else:
    menu:
        "Yeah, I think I would.":
            $ council_campaigning = True

        "No, I'll be too busy.":
            pass

if (council_campaigning):
    cheren @happy "Splendid."
    cheren @talking2mouth "That does mean there's a somewhat awkward follow-up question, though."
    cheren @talking2mouth "[first_name], Serena... and possibly Calem..."

else:
    cheren @sad "Unfortunate."
    cheren @talking2mouth "I suppose that saves us from the awkwardness of this next question, then."
    cheren @talking2mouth "Serena... and possibly Calem..."

cheren @sad "I would very much like to work with you to become elected. However, I'm not aware, yet, of your positions. It may be that we end up political enemies."
cheren @talking2mouth "Would you share some of the points you intend to run on?"

serena @talkingmouth "Certainly. There's one thing, more than anything else, that I want."
serena @blush heartbrow talkingmouth "Coed dorms."

calem @surprised "Er...?"

serena @happy "After all, we're all adults, are we not? As we do not have the freedom to live in nearby apartments, we jolly well ought to have the freedom to live how we wish on-campus."

cheren @happy "Well said. I'm certain this will be a popular position to hold, too, regardless of my personal feelings."

if (council_campaigning):
    cheren @talkingmouth "What about you, [first_name]?"

    red @talking2mouth "I'm not sure yet. But nothing either of you two said has scared me off, so..."

    cheren @closedbrow talkingmouth "...So we should be on the same page."

hilda @talkingmouth "It sounds like what you guys want to do is going to put you on the admin's shit list. Especially you, Cheren."

hilbert @closedbrow talkingmouth "Yeah. Even if you run a great campaign, if you're running on a platform the school doesn't like, they'll just shut you down."

hide bianca

cheren @closedbrow talkingmouth "That's always a concern, but Kobukan Academy's Student Council has a lot of power, and an even greater budget."
cheren @talkingmouth "As long as we can get {i}into{/i} the council, I think I can defend us from the admin."

bianca uniform @happy "I believe in you guys!"

pause 1.0
    
bianca @happy sweat "So, um, have you guys seen the garden out back yet?{w=0.5} It's so pretty~!"

redmind @closedbrow talkingmouth "Thank goodness for Bianca.{w=0.5} I guess she's the kind I can count on to change the topic to something more lighthearted."

serena @talkingmouth "I've seen it from outside, but I haven't been in there myself."
serena @happy "We should go there sometime!"

hilda @happy "Hell yeah.{w=0.5} It'd be a goddamn waste if we didn't."

hilbert @surprised "Why?{w=0.5} What do you even {i}do{/i} in a garden?"

serena @talkingmouth "I was thinking of perhaps a picnic of sorts.{w=0.5} I hear the center of the garden is a very popular spot for students during the spring and summer."

hilbert @talkingmouth "Why not just eat in the cafeteria?{w=0.5} It's cheaper, faster, and we don't have to worry about the wind blowing everything away."

hilda @closedbrow talking2mouth veins "It's not the same, Hilbert..."

hilbert @sadbrow talkingmouth "You're right, it's not."
hilbert @angry "Eating on a table is much better than eating on some dirt and grass."

hilda @angrybrow smirkmouth "Do you really think eating in a boring room surrounded by crowds of people is better than eating with your friends in a quiet garden?"

hilbert @frownmouth "[ellipses]"
hilbert @talkingmouth "Yes."

calem @talkingmouth "I have to agree with Hilbert."

serena @talkingmouth "Calem?{w=0.5} I thought that you, of all people, would prefer somewhere with less people around."

calem @talkingmouth "You're not wrong, but I don't quite like the idea of eating food that's so close to the floor.{w=0.5} Who knows what's been on the garden grounds?"

serena @talkingmouth "Well, that's just your opinion.{w=0.5} What does everyone else think?"

cheren @talking2mouth "Both sides have their merits. I see no reason to take an absolute stand on this issue."

bianca @happy "It depends on the day! Variety's the spice of life, you know!"

serena @happy "Seems the house is still split evenly, then."
serena @talkingmouth "What about you, [first_name]?"

redmind @thinking "Uh... are they really expecting me to decide this? This isn't exactly a hill I'd like to die on."

menu:
    "Eating indoors is the way to go.":
        $ ValueChange("Calem", 1, (448/1920, 641/1080), False)
        $ ValueChange("Hilbert", 1, (1579/1920, 281/1080))
        
        hilbert @closedbrow talkingmouth "Exactly."
        hilbert @talkingmouth "What if you forgot something in your room?{w=0.5} Then you'd have to walk all the way back and get it.{w=0.5} It'd just be a lot of work for a lot of nothing."
        
        hilda @sad "All right, we get it, Hilbert.{w=0.5} You don't have to beat a dead horse."
        
        serena @poutmouth "Well, {i}I{/i} still think that a picnic is a good idea."
        
        calem @closedbrow talking2mouth "And I still think that not eating off the ground is better.{w=0.5} We're allowed to have our own opinions."
        
        serena @angrybrow talkingmouth "Yes, I know.{w=0.5} It was just an idea."
    
    "A picnic sounds great.":
        $ ValueChange("Serena", 1, (112/1920, 426/1080), False)
        $ ValueChange("Hilda", 1, (1455/1920, 650/1080))

        serena @happy "Yes! Having a light meal surrounded by nothing but green nature and the blue sky...{w=0.5} it sounds so romantic!"

        calem @sadmouth "One can be overexposed to romance."
        
        hilda @smirkmouth "Whatever.{w=0.5} It's about the, y'know, atmosphere, not the actual meal."
        hilda @closedbrow talkingmouth "The cherry blossoms are in full bloom around this time of year, yeah? We didn't get that in Unova."
        
        hilbert @angrybrow talkingmouth "Then you can go outside and eat in the trees if you want."
        hilbert @closedbrow talkingmouth "Everyone who doesn't like a handful of dirt in their sandwich can stay here."

        hilda @sadbrow talking2mouth "It was just a suggestion!"
        
        calem @closedbrow talkingmouth "I still prefer eating on stable ground, but to each their own."
    
    "It really doesn't matter where you eat.":
        red @talkingmouth "What's important is the meal itself, not the setting."
        red @happy "You can put me in the bathroom for all I care, as long as I have food."
        
        $ ValueChange("Cheren", 1, (914/1920, 197/1080), False)
        $ ValueChange("Bianca", 1, (1326/1920, 285/1080))
        
        cheren @closedbrow talkingmouth "That was a crude way of putting it, but I agree."
        
        bianca @happy "Yeah! As long as the food ends up in my tummy, I'm good to go!"
        
        serena @sadbrow talkingmouth "So we're still at an impasse."
        
        hilbert @angry "Who cares?{w=0.5} You all can go and eat wherever you want. I'm done with this conversation."
    
bianca @talkingmouth "Well, if you wanted to go to the garden anyway, it's free access to students all day, every day!"
bianca @happy "I was planning on going to get a head start on my Psychic and Normal classes."

cheren @confused "In what way did you plan on getting a head start?"

bianca @talkingmouth "I dunno, but I thought maybe I can take a closer look at any Pokémon that I can find there so I have something to compare to in class. Is that weird?"

cheren @happy "No, that is a good idea.{w=0.5} I was planning on doing something similar."

bianca @happy "Hehe, thanks!"

cheren @closedbrow talkingmouth "Even I fall into the trap so many others do of underestimating you, Bianca. I ought to know by now that you're an extremely diligent student."
cheren @happy "In many ways, your focus surpasses mine."

bianca @happy "Aw, thanks! I knew I'd have to take this seriously after that big brouhaha with my Dad, though."

cheren @sadbrow talkingmouth "Er... yes. That was quite a 'brouhaha.'"

serena @talkingmouth "Speaking of classes, how do you all plan on handling your studies?{w=0.5} Do you think we should hold some kind of study group?"

calem @closedbrow talkingmouth "Are you concerned about what the professors said about the graduation rate? A fixed eighty percent is... concerning."

serena @sadbrow happymouth "Mm... just a little."

cheren @closedbrow talkingmouth "There's no need to fret about something like graduating."
cheren @happy "I have confidence that everyone sitting here at this table will have no trouble graduating on time."
cheren @talkingmouth "What you should be concerned with is how you should spend your time {i}outside{/i} of class.{w=0.5} Have any of you decided on your extracurricular activities yet?"

bianca @surprised "Oh, clubs? {w=0.5}{nw}" 
extend talkingmouth "I was looking at the gardening club, but I wanted to think about it a little more."
bianca @happy "Have you decided on a club yet, Cheren?"

cheren @talking2mouth "I see no need.{w=0.5} I will have my hands full preparing for the Student Council elections, and I'll be even busier if I succeed."

bianca @surprised "Oh, yeah, that's right!{w=0.5} You guys are gonna be so busy!"

calem @sad "I'm still on the fence about the Student Council myself, but... as a backup plan, I plan on joining the art club.{w=0.5} It'd be a good way to pass the time and unwind."

serena @talkingmouth "I've heard from my parents that Kobukan Academy's musicals are so impressive, they can be compared to professional ones."
serena @happy "If possible, I'd like to be able to join their pit orchestra with my violin."

calem @talkingmouth "I am {i}beyond{/i} certain that if Brendan learned of your skills with the violin, he would do his best to swipe you into the Coordinator Club."

serena @happy "Then perhaps I will let him do so!"

hilda @sadbrow smirkmouth "It must be nice being able to play a musical instrument."
hilda @happy "All I can play is tennis."

serena @surprised "Then are you joining the tennis team?"

hilda @sadbrow smirkmouth "This school has a tennis team?"

pause 1.0

hilda @smirkmouth "I can't even imagine joining a club. I'll be way too busy.{w=0.5} What about you, Hilbert?"

hilbert @closedbrow talkingmouth"I can't play tennis."

hilda @talkingmouth "No, I'm talking about if there are any clubs you're interested in."

hilbert @talkingmouth "Hm.{w=0.25}.{w=0.25}."
hilbert @talkingmouth "I'll be joining the Battle Team."

calem @closedbrow talkingmouth "Do you have any clubs in mind, [first_name]?"

if council_campaigning:
    calem @talkingmouth "Even if you're confident that you'll be elected into the Student Council, it's still a good idea to have a Plan B."

red @closedbrow talking2mouth "Clubs, huh?{w=0.5} Right now I'm leaning towards..."

menu:
    "The art club.":
        red @talkingmouth "I've always thought it'd be cool to learn how to draw and paint.{w=0.5} I've never used a pencil for anything other than writing words and numbers."
        
        $ ValueChange("Calem", 1, (448/1920, 641/1080))
        
        calem @happy "Looking to add new skills to your repertoire?{w=0.5} That's a good attitude you have, [first_name]."
        calem @closedbrow talkingmouth "If you think you'd like a crash course in fine arts, give me a call.{w=0.5} My parents practically forced me to take art lessons when I was a child."
        
        serena @happy "Calem is quite a talented painter, you know?{w=0.5} You should see some of the pieces he's created. They're utterly beautiful."
        
        calem @sadbrow talkingmouth "You flatter me unduly."
    
    "The gardening club.":
        red @talkingmouth "It sounds like a place where I can really chill out and relax for a couple of hours."
        
        $ ValueChange("Bianca", 1, (1326/1920, 285/1080))       
        
        bianca @happy "{i}Right???{/i} It'd be soooo soothing winding down after a long day of classes!"
        
        hilda @happy "Yeah, sounds relaxing as hell. Wish I had the time to drop by."
        
        bianca @puppyeyes happymouth "I heard that they take care of Pokémon, too!{w=0.5} I wonder if they'd let us bring some home for ourselves?"
    
    "The theatre club.":     
        red @talkingmouth "Back home in Pallet Town, {i}battling{/i} with Pokémon was considered pretty fancy. I can't even imagine how you'd set up a musical with them."
        red @happy "I'd love to find out, though."

        $ ValueChange("Serena", 1, (112/1920, 426/1080)) 
        
        serena @happy "Oh, how splendid! I am certain you would make a fine addition to any musical you took up an instrument in."
        serena @talkingmouth "Which department are you thinking of joining?"

        red @confused "Department?{w=0.5} You mean like sanitation or...?"
        
        serena @sadbrow happymouth "...No. Like the stage crew, choreographers, pit orchestra... did you not know about this?"

        red @closedbrow talking2mouth "Not even a twinge."

        pause 1.0

        serena @talkingmouth "It doesn't matter.{w=0.5} What's important is your decision to join the club at all."
    
    "The tennis team.":
        red @talkingmouth "I wasn't a great player--only knew the very basics, but I was pretty fast on my feet, so that helped. Maybe I can get in?"

        $ ValueChange("Hilda", 1, 1290/1920)

        hilda @happy "No shit? Go for it, dude. What kind of player were you?"
        
        red @talkingmouth "Uh, I was pretty average, I think.{w=0.5} Nothing really special."
        
        hilda @smirkmouth "No, I mean like were you a pusher?{w=0.3} A baseliner?{w=0.3} Or were you perhaps an all-rounder?"
        
        red @confused "{w=0.25}.{w=0.25}.{w=0.5}.I have absolutely no idea. I hit the ball, and it went over the net."
        
        hilda @happy "Eh, that's fine. Only fancy word you need to know to actually play is that love means nothing."

        serena @sad "[ellipses]"
        calem @sad "[ellipses]"

        redmind @thinking "Hm."

        hilda @smirkmouth "Anyway, if you want to learn some of the terminology, or just practice a bit, find me when I'm free." 
        hilda @sadbrow smirkmouth "That'll probably be harder than mastering tennis, honestly."
    "The Battle Team.":
        red @talkingmouth "The Battle Team."
        red @talkingmouth "I'm going to be a Champion someday, and I know a lot of the Champions from Kobukan joined the Battle Team."

        $ ValueChange("Hilbert", -1, 1690/1920)
        
        hilbert @closedbrow talkingmouth "Do you have any experience in Pokémon battling?"
        
        red @talkingmouth "I wouldn't call myself a master, but I know a thing or two. As a kid I participated in scrimmages with others and the Pokémon we had around town."

        hilbert @talkingmouth "But have you ever battled competitively?{w=0.5} You can hardly call yourself a Pokémon Trainer until you've experienced an official match."
    
        red @closedbrow talking2mouth "Well... no."

        hilbert @sadbrow talkingmouth "And yet you claim that you'll be a Champion someday... with absolutely no proof. No evidence. Not a shred of {i}reason.{/i}"

        red @angrybrow  talkingmouth "Yeah. Because there's {i}nothing{/i} I won't do to become Champion."

calem @surprised "Of course, when picking a club, it's important to remember the opportunity cost that comes with it."

hilbert @closedbrow talkingmouth "It's not like there's any consequences for skipping."

bianca @happy "But if you feel like dropping into another club, I'm sure they'll welcome you with open arms!"

cheren @closedbrow talkingmouth "Well, except for the Battle Team. But they're very demanding, and rightly so."

hilda @smirkmouth "Thank god. If these clubs had mandatory attendance, I wouldn't be able to attend any of 'em."

bianca @happy "Kobukan's clubs are nice because they don't care when you come in, just as long as when you {i}do{/i}, you have a good time~!"

cheren @happy "It's unsurprising, given how rigorous our academics are. Extracurriculars are a much-needed break."

bianca @surprisedbrow talking2mouth "Mmm, all this talk about clubs is making my head hurt."
bianca @happy "Let's talk about something fun, like how amazing the food is here~!"
bianca @talkingmouth "Have you guys ever had anything like this back at home?"

calem @happy "I'm Kalosian. Of course.{w=0.5} ...Though the food here is {i}rather{/i} good."

hilda @smirkmouth "Yeah, alright, fancypants. For the rest of us, this shit's incredible. They must've hired some stupid expensive chefs...{w=0.5} How much funding is this school getting, anyway?"

cheren @talkingmouth "You can thank the results and reputation of this school.{w=0.5} Numerous alumni historically become some of the most renowned Trainers and researchers in the world."

serena @sadmouth closedbrow "I believe Diantha actually dropped out of Kobukan to focus on her movie career."
serena @sadbrow happymouth "Perhaps that's a bad example. As for non-dropout Alumni..."

hilda @talkingmouth "Let's see, there's Alder and Bruno teaching our gym class.{w=0.5} Instructor Koga, Steven Stone... uh..."

bianca @happy "Don't forget Cynthia~!"

narrator "You casually talk about celebrities as lunch draws to a close."

$ renpy.music.set_volume(0.1, delay=1.0, channel="music")

show blank2 with dis

$ PlaySound("BellChime.ogg")
$ renpy.music.set_volume(1.0, delay=4.0, channel="music")

$ renpy.transition(dissolve)
call clearscreens from _call_clearscreens_9

$ renpy.pause(1.0, hard=True)

narrator "It's time to go to your next class."

window hide
scene blank2
$ renpy.music.stop(channel='crowd', fadeout=1.0)

jump PickElective