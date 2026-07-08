label secondhomeroom010611:

scene blank2

play music "Audio/Music/Oak Intro.ogg" noloop
queue music "Audio/Music/Oak Class.ogg"

show homeroom behind blank2
    
$ renpy.transition(dissolve)
show screen currentdate

hide blank2 
with splitfade

show oak sadbrow frownmouth with dis

pause 2.0

redmind uniform @sadbrow frownmouth "That's a guilty-looking Sam."

oak @talking2mouth sweat closedbrow "Er[ellipses] students. I feel I must, er, apologize."
oak @talkingmouth "This morning, I was distracted. I told you I intended to speak with Professor Sycamore, yes? Well, the meeting went rather long, and[ellipses]"
oak @closedbrow sweat talking2mouth "Ah, that's just making excuses. I should not have been so late to class."

show melody on uniform with dis:
    xpos 0.75

melody @talking2mouth "It's whatever. We can study by ourselves."

oak @sadbrow talkingmouth "You can, but I'm not entirely blind to the amount of money you are spending to ensure you, er, do {i}not{/i} have to do that."

melody @bubblemouth "[ellipses]"
melody @talking2mouth "There's definitely {i}worse{/i} things you could do, as a teacher. Still, if you want to make it up to us[ellipses]"

show oak surprisedbrow frownmouth with dis

melody @bubblemouth "Someone take over, I don't know how to finish this sentence."

hide melody with dis

pause 1.0

show oak sweat closedbrow frownmouth with dis

oak @talking2mouth "Well, er, that being the case, I--"

show melody uniform on with vpunch:
    xpos 0.75

melody @talking2mouth "Nevermind, figured something out. This year's way stronger than last year. Why?"

show oak surprisedbrow frownmouth with dis

pause 1.0

oak @confusedbrow talking2mouth "What? Well, surely there are a variety of factors, including environmental and educational--"

melody @angrybrow talking2mouth "I don't want to hear that again! There has to be one {i}concrete{/i} reason even the {i}Bug{/i}-class kids are walking around with level twenties."

pause 0.5

oak -surprisedbrow -frownmouth @confused "Does there, Melody?"

melody @surprisedbrow frownmouth "[ellipses]"
melody @sadbrow talking2mouth "I mean[ellipses] yeah. It's gotta be. It {i}can't{/i} just be that I went here during the wrong year."

oak @talkingmouth "No, it's not that. Because {i}any{/i} year one can attend Kobukan is the right one."
oak @sadbrow talkingmouth "The other Professors and I {i}have{/i} noticed the level discrepancies, and are discussing possibilities, but whatever conclusion we reach is not likely to be the one, absolute, answer you seek."

pause 0.5

oak @talkingmouth "Absolutism is a very appealing--but very dangerous--philosophy. Shades of grey impose much uncertainty and doubt into one's actions."
oak @talking2mouth closedbrow "When ills befall you, it's tempting to want to blame one cause. When you come across a boon, you may try to identify its particular source, and replicate it."
oak sadbrow @closedbrow talking2mouth "Indeed, in the sciences, we love nothing more than a single cause with a single effect."

pause 1.0

oak -sadbrow @sadbrow talkingmouth "There's only one applied field where that's a reality, though, and that's math."

pause 1.0

melody @talking2mouth "Fine. What were you going to say? About the 'variety' of factors?"

oak @talkingmouth "Well, I'd love to discuss this with you in more detail, but perhaps this should be an after-class discussion? I have office hours, if you're interested."

melody @talking2mouth "I don't go to office hours."

oak @upeyes talking2mouth "Fine. Then the short version of the longer answer is that there are several students in this school year who have extraordinary aptitude, and assist in the training of their classmates through their very presence."
oak @talking2mouth "This is not a unique situation. The years in which Champions Cynthia, Steven, and Wallace attended Kobukan were notably stronger than prior years."

melody "[ellipses]{nw}"
extend @talking2mouth "A rising tide lifts all boats."

oak @talkingmouth "Quite right. Some students are able to make enough waves to {i}be{/i} the tide."

melody @talking2mouth "And some just make enough to drown everyone else."

oak @closedbrow talking2mouth "Granted. Whether you lift or drown--whether you raise or ruin--all of you have the power to change everyone's futures through actions both grand and small."
oak @happy "You can't always know what shores your waves will crash against, but that's no reason not to make them! And there's no place better to make waves than Kobukan."

pause 1.0

oak @happy "A rather fitting metaphor, given tomorrow's planned events, no? But we've a lesson to attend to, and I don't intend to apologize for my absence purely through long-winded aqueous metaphors. Now, if you'll open your books[ellipses]"

scene blank2 with splitfade

pause 0.5

$ PlaySound("BellChime.ogg")

call freeroam() from _call_freeroam_49

#copy of rosafollowupbunnyrecruitscene
if (not HasEvent("Rosa", "BunnyRecruit") and HasEvent("Rosa", "HalfBunnyRecruit") and (HasEvent("Nate", "BunnyRecruit") + HasEvent("Iono", "BunnyRecruit") + HasEvent("Sonia", "BunnyRecruit") + min(1, GetRelationshipRank("Rosa") / 2.0) >= 3)):        
    scene blank2 with splitfade

    $ AddEvent("Rosa", "BunnyRecruit")

    stop music fadeout 1.5
    queue music "audio/music/joinavenue_start.ogg" noloop
    queue music "audio/music/joinavenue_loop.ogg"

    show screen songsplash("Join Avenue", "Zame")

    if (HasEvent("Rosa", "PromisedNessaText")):
        red @thinking "Hm[ellipses] after today's recruitment, I think we can make sure the party is secure for Rosa. I said I'd text Nessa, so[ellipses]"

    elif (HasEvent("Rosa", "PromisedSoniaText")):
        red @thinking "Hm[ellipses] after today's recruitment, I think we can make sure the party is secure for Rosa. I said I'd text Sonia, so[ellipses]"

    elif (HasEvent("Rosa", "PromisedRaihanText")):
        red @thinking "Hm[ellipses] after today's recruitment, I think we can make sure the party is secure for Rosa. I said I'd text Raihan, so[ellipses]"

    else:
        red @thinking "Hm[ellipses] after today's recruitment, I think we can make sure the party is secure for Rosa. I said I'd let Sabrina know, so[ellipses]"

    pause 1.0

    redmind "There, text sent."

    show rosa behind phone_A:
        zoom 0.8 ypos 0.95
    with fadeinbottom

    rosa @talkingmouth "Hey, [first_name]!"

    red @talkingmouth "Oh, hey, Rosa! I thought you couldn't use your phone?"

    if (HasEvent("Rosa", "PromisedNessaText")):
        rosa @happy "Didn't you notice? I'm using Nessa's phone! She got your text!"

    elif (HasEvent("Rosa", "PromisedSoniaText")):
        rosa @happy "Didn't you notice? I'm using Sonia's phone! She got your text!"

    elif (HasEvent("Rosa", "PromisedRaihanText")):
        rosa @happy "Didn't you notice? I'm using Raihan's phone! He got your text!"

    else:
        rosa @happy "Didn't you notice? I'm using Nessa's phone! Sabrina heard your, uh, your 'thought!'"

        if (not IsContacted("Nessa")):#should be impossible, but just in case
            $ BecomeContacted("Nessa")

    red @talkingmouth "Gotcha. So, we're good? You'll be able to go to the party, then?"

    rosa @talkingmouth "I think so. It really sounds like you thought this through pretty thoroughly."
    rosa @sadbrow talkingmouth "And[ellipses] I {i}really{/i} appreciate that. I know it's a hassle."

    $ ValueChange("Rosa", 1, 0.5)

    red @happy "Don't worry about it! I just want you to be able to have fun with us, like everyone else."
    red @talkingmouth "There won't be any fancy movie-people there, or anything, so it's probably a much more low-key party than you're used to, but I hope you still have fun."

    rosa @talkingmouth "Trust me, that sounds like the best kind of party right now. The stage lights get blinding, after a while."

    red @happy "I can imagine."
    red @talkingmouth "Anyway, that's great to hear! We'll see you there. And don't worry, if anything changes, or one of our security people has to drop out, I'll let you know beforehand."
    red @sadbrow talkingmouth "Everyone's going to go into this knowing {i}exactly{/i} what they're getting into. Promise."

    rosa @happy "Aw. Thanks so much for your support!"

stop music fadeout 3.0

scene stadium_empty
show screen currentdate
with Dissolve(2.0)

$ HealParty()

pause 0.5

show blue battleteam:
    xpos 1.0/8.0
show sonia battleteam:
    xpos 7.0/8.0
show erika battleteam:
    xpos 5.0/8.0
show ethan battleteam:
    xpos 4.0/8.0
show silver battleteam:
    xpos 2.0/8.0
show bea battleteam behind ethan:
    xpos 3.0/8.0
show hilbert battleteam behind sonia:
    xpos 6.0/8.0
with dis

pause 1.0

show smoke:
    animation
    alpha 0.0 yalign 3.0 xalign 0.5
    parallel:
        ease 3.0 yalign 0.5
    parallel:
        ease 0.5 alpha 1.0
        pause 0.5
        ease 3.0 alpha 0.0 

pause 2.0

stop music
show screen songsplash("Fuchsia City", "Zame")

queue music "Audio/Music/fuchsia_start.ogg" noloop
queue music "audio/music/fuchsia_loop.ogg"

pause 1.0

show blank
show janine behind blank

pause 0.1

hide smoke
hide blank

show lance:
    xpos 1.1 ypos 1.0
    ease 0.5 xpos 0.66

show janine behind lance:
    ease 0.5 xpos 0.33

pause 1.0

janine @closedbrow talking2mouth "You know what to do."

show blue:
    ease 0.8 xpos 1.5
show erika:
    ease 1.0 xpos 1.5
show ethan:
    ease 0.4 xpos 1.5
    pause 0.2
    ease 0.4 xpos -0.5
show silver:
    ease 0.5 xpos -0.5
show bea:
    ease 0.5 xpos 1.5
show sonia:
    ease 0.5 xpos 1.5
show hilbert:
    ease 0.5 xpos -0.5

pause 1.0

hide blue
hide erika
hide silver
hide bea
hide sonia
hide hilbert

janine surprisedbrow frownmouth @neutraleyes neutraleyebrows talking2mouth "Alright. I'm going to step down now, and let Blue lead this Battle Team meeting."

show lance sadeyes angryeyebrows with dis

red battleteam @surprisedbrow talking2mouth "{i}WHAT.{/i}"

pause 1.0

show janine happybrow talkingmouth with dis

red @wince talking2mouth "Crap, I said that out loud, didn't I?"

pause 1.0

show janine:
    xpos 0.33
    ease 0.5 xpos -0.2
show lance:
    xpos 0.66
    ease 0.5 xpos 1.2
show blue battleteam 
with dis

blue @talking2mouth "So, uh, Battle Team."
blue @closedbrow talking2mouth "You all saw my battle with Sycamore this morning, right? I asked Janine to call all the Battle Team out to the Battle Hall. And in exchange I'd[ellipses] do this."

bea battleteam @talking2mouth "What is {w=0.5}'this?'"

blue @talking2mouth "I'm going to share my tips for training Pokémon."

show blue surprisedbrow frownmouth with dis

silver battleteam @angrybrow talking2mouth "I'm pretty sure I don't need to know how you train your Pokémon."

show blue:
    xpos 0.5
    ease 0.5 xpos 0.33

blue -surprisedbrow @angrybrow talking2mouth "Hey, what did you mean by that?"

show silver battleteam with dis:
    xpos 0.66

silver @sadbrow frownmouth "[ellipses]"
silver @closedbrow talking2mouth "Forget it."

blue angrybrow frownmouth @angry "I sure as hell will {i}not!{/i} What did you mean by that? You trying to imply something, second-place?"

silver @angry "All I'm {i}implying{/i} is that your Pokémon seem a little {i}too{/i} strong, and given your personality, I'm pretty sure I know how you got them there."

hide ethan

ethan battleteam @talking2mouth "{size=30}[ellipses]The boys are fighting again. Popcorn?{/size}"

redmind @wince frownmouth "Janine, what are you doing? C'mon, break them up already."

blue @talking2mouth "You think I'm pushing my Pokémon too hard? Is that what you're trying to get at?"

silver @talking2mouth "You tell me how else you've got a level [IntToWord(GetTrainerTeam('Blue', 'Magikarp').GetLevel())] Gyarados already."

blue @talking2mouth "So you've got a problem with my Gyarados, but don't have a problem with [first_name]'s level [IntToWord(GetHighestLevel())] [GetHighestLevelMon().GetSpeciesName()]?"

silver @talking2mouth "Yeah, actually, I {i}don't{/i}."

pause 1.0

blue @talking2mouth "You know, I should battle you into the floor for that. But let me do something else, instead."

python:
    place = Transform(xcenter = 0.7, xpos=0.0, yalign=0.5, xzoom=-1)
    global sidemonnum
    global sidemonnew
    PlaySound("Pokemon/ball sound.ogg")
    PlaySound("pokemon/cries/130.mp3")
    renpy.show("fullgyarados", [pokeball, place])

hide blue
show blue battleteam angrybrow frownmouth:
    xpos 0.33

blue @talking2mouth "Hey, Gyarados! This asshole thinks I've been training you too hard. What do you think of that?"

$ PlaySound("pokemon/cries/130.mp3")

blue @closedbrow talking2mouth "[ellipses]Uh-huh, okay."
blue @talkingmouth "So why don't we prove it?"

silver @surprisedbrow talking2mouth "Prove{w=0.5}--what? Don't do anything reckless."

blue @talking2mouth "Oh, we're {i}way{/i} past that. Gyarados are supposed to be crazy violent and destructive, right? Like, the S.S. Anne {i}sank{/i} because of a bad trainer whose Magikarp evolved early."

silver @talking2mouth "Y-yeah. Where are you going with this?"

blue @closedbrow happymouth "Heh."

show silver surprised with dis

blue angry "Gyarados. {w=0.5}{i}Bite my head.{/i}"

call clearscreens() from _call_clearscreens_281
show blank2 with splitfadedownfaster

redmind @surprisedbrow frownmouth "WHAT?!"

narrator "Before anyone can react, Blue's Gyarados immediately closes its mouth around Blue's head."

red @surprisedeyebrows deadeyes frownmouth "[ellipses]"
redmind @wince frownmouth "Shit, what am I going to tell Daisy?"

blue @talking2mouth "{size=30}I can't see all your faces, but I assume you've all got dumb looks of shock?{/size}"

pause 1.0

redmind @sad2eyes surprisedeyebrows poutmouth "On the other hand, if Gyarados wants to bite down[ellipses]"

hide blank2 
show silver -surprised 
with dis

blue @talking2mouth "Gyarados bit my head. But he didn't close his mouth all the way. He brought me to the very edge of serious injury, but I never actually got hurt."
blue @talking2mouth "Get it, Silver? I trust him not to hurt me. He trusts me not to hurt him. What we do isn't easy, and there's always a risk when you train like a Champion. We bring each other to the edge, over and over."
blue @talking2mouth closedbrow "That's {i}almost{/i} enough. But there's one more step."
blue frownmouth @angrybrow talking2mouth "You need to trust {i}yourself{/i} not to hurt your Pokémon. That's when you can {i}really{/i} start training."

pause 0.5

silver "[ellipses]"
silver @talking2mouth "Yeah, I[ellipses] sorry. Maybe I was projecting."

show blue surprisedbrow frownmouth with dis

silver @sadbrow talking2mouth "Are we cool?"

pause 1.0

blue -surprisedbrow -frownmouth @happymouth surprisedbrow "What? No. I'm going to hold a grudge over this forever, and when I kick you out of the Quarter Qlashes, I'll remind you about it."

silver @closedbrow talking2mouth "Ugh[ellipses]"

$ renpy.show("fullgyarados", [backinpokeball, Transform(xcenter = 0.7, xpos=0.0, yalign=0.5, xzoom=-1)])

hide silver with dis

blue @talking2mouth "Alright, now I've spouted a bunch of bullshit about how training should {i}feel.{/i} Let's talk about what you actually {i}do{/i}."

blue @angry "First step! What you fight really doesn't matter. Stronger Pokémon give you more experience, but you should never train to defeat an opponent, you train {i}yourself{/i} to defeat {i}all{/i} your opponents."
blue @closedbrow talking2mouth "Unless your opponent is [first_name], then you can train to defeat just him, that's fine."

red @upeyes angryeyebrows talking2mouth "Thanks, neighbor."

blue @talking2mouth "Can't take a joke[ellipses]"

blue @angrybrow talking2mouth "Second step. What you fight doesn't matter, but {i}where{/i} you fight does."
blue @talking2mouth "Always go to the most difficult place you can go to train. If you got comfortable training in the fields, go to the seaport. If you're comfortable there, go to the mountains!"

erika battleteam @talking2mouth surprisedbrow "Oh? But I have seen you in the garden with Yellow[ellipses] training, of a sort."

blue surprisedbrow frownmouth @neutraleyes neutraleyebrows talking2mouth "Yeah, so what? I'm good enough I don't need to follow that 'always,' but {i}you{/i} do."

hide janine

janine @talking2mouth "{size=30}Tone it down.{/size}"

blue -surprisedbrow @closedbrow talking2mouth "{size=30}Right, sorry.{/size}"

blue @talking2mouth "Step three. Never defeat less than twenty Pokémon in a single training session. In a row! No breaks! No water! No repels!"
blue @angrybrow talking2mouth "If you lose your momentum, then it's not a {i}real{/i} training session. If you've battled nineteen Pokémon and number twenty roars at you and your Pokémon runs away, get back in there and do all twenty again!"
blue @closedbrow talking2mouth "And just[ellipses] make sure the roaring thing can't happen again. Bring a Pokémon that can knock out that species before it can roar. Or use Taunt, or Suction Cups, or... whatever! I'm here to teach training, not battling."
blue @talking2mouth "Obviously, the Pokémon doing the actual battling gets the most experience, but that'll probably {i}pale{/i} to the amount of experience the whole party gets at the end of a streak." 
blue @happymouth "So use whoever makes training easiest--your other Pokémon will watch and learn."

pause 1.0

blue @talking2mouth "So[ellipses] yeah. Those are my tips."

pause 0.5

blue @surprisedbrow talking2mouth "Janine? We done?"

show janine with dis:
    xpos 0.25

show blue surprisedbrow frownmouth with dis

janine @talking2mouth "Good question. Professor?"

redmind @surprisedbrow "Oh! Is that Sam--"

play music "audio/music/sycamore.ogg"

show sycamore:
    xpos 1.2
    ease 0.3 xpos 0.66

sycamore @happy "Ah, ah, magnifique! A remarkable demonstration of student-driven study, backed by such passion!"
sycamore @sadbrow talking2mouth "Oh, it is a {i}terrible{/i} unkindness that you were not placed into my class. I am so jealous of Samuel--yes, {i}so{/i} jealous!"
sycamore @talkingmouth "But, Monsieur Oak, I must beg of you to transfer! I understand love of family is strong, but my class direly needs someone with your--your--{i}sentiments enflammés.{/i}"

pause 0.5

blue @talking2mouth closedbrow "Wait, hold on. You're asking me to {i}transfer?{/i} From Gramps' class to yours?"

sycamore @talkingmouth "{i}Oui!{/i} In my class, I strive to have students teach each other. You have shown such proficiency just now!"
sycamore @talkingmouth "And more--your passion this morning--our battle--ah, it has kept me from sleep!"

blue @surprisedbrow talking2mouth "It's been like eight hours. When would you even sleep? It's a schoolday."

sycamore @talking2mouth "Oh, I take a midday nap. Normally."

blue @talking2mouth closedbrow "Huh."

pause 1.0

show sycamore surprisedbrow frownmouth
with dis

blue @talking2mouth "Look, I'm flattered, I guess, but Gramps is... I mean, he's my Gramps. I can't just leave his class."

janine "[ellipses]{nw}"
extend @talking2mouth "You know, Kobukan evaluates your entrance exam and places you in the class of the homeroom teacher where we think you'll succeed most. Your result {i}was{/i} Sycamore."

blue @surprisedbrow talking2mouth "What? Then why'd I end up with Gramps?"

hide lance
show lance behind sycamore with dis:
    xpos 0.75

lance @talking2mouth "This is neither the time nor the place to discuss this matter. We will move on. Augustine, we will discuss this matter later--for now, allow Janine's battler to focus on the Battle Team meeting that is currently happening."

sycamore @talking2mouth "Ah. {i}Je suis désolé.{/i}"

hide lance with dis

pause 1.0

blue @closedbrow talking2mouth "Ugh. {i}Hell.{/i} What does that mean, that I was {i}supposed{/i} to be with Sycamore?"

sycamore -surprisedbrow -frownmouth @sadbrow talkingmouth "Perhaps now, then, is not the time for my pursuit--but be warned, monsieur Oak! There is little as persistent as a Kalosian who chases another's passion!"

blue @talking2mouth closedbrow "Sure. Whatever."

pause 1.0

show sycamore surprisedbrow frownmouth with dis

janine -surprisedbrow -frownmouth @talking2mouth "Well[ellipses] since you're here, Professor Sycamore, could you handle the move tutoring?"

sycamore -surprisedbrow -frownmouth @happy "But of course. Monsieur Oak, do you--"

show blue behind sycamore:
    xpos 0.33
    ease 0.5 xpos 1.2

show sycamore surprisedbrow frownmouth with dis

blue @closedbrow talking2mouth "Pass."

pause 1.0

sycamore -surprisedbrow -frownmouth @sadbrow talking2mouth "[ellipses]Oh."

pause 1.0

sycamore @happy "Well then, Monsieur [last_name]! Monsieur Oak's very best friend, {i}non?{/i} Yes, I can feel the burning bonds of brotherhood--{nw}"
extend @winkbrow talkingmouth "or perhaps there is something less fraternal and more fanciful?"

redmind @wince frownmouth "Oh, god."

label movetutor611:

call screen SelectMon
$ tutormon = _return

if (tutormon == 'back'):
    sycamore @closedbrow talking2mouth "Ah, you will not avail yourself of my techniques?"

    menu:
        "I don't want to teach any of my Pokémon a new move.":
            sycamore @closedbrow talking2mouth "{i}C'est la vie.{/i}"

        "On second thought...":
            jump movetutor611

elif (tutormon == pikachuobj):
    sycamore @talkingmouth "Alas, I do not know how to teach your Pikachu. I would be delighted if you might bring him by my laboratory for study, though!"
    sycamore @sadbrow talking2mouth "Though I fear, like with Monsieur Oak, Doctor Samuel has--how do you say--'called dibs.'"

    jump movetutor611

else:
    $ tutormon = _return
    $ tutormonname = pokedexlookup(tutormon.GetId(), DexMacros.Name)

    sycamore @happy "Your [tutormonname]? Wonderful!"
    
    $ rememberablemoves = GetRememberableMoves(tutormon)

    if (len(rememberablemoves) == 0):
        sycamore @talking2mouth "Oh... actually... this Pokémon does not seem to have any moves it is inclined to learn."

        jump movetutor611

    else:        
        sycamore @talking2mouth "Now we know the restaurant, what will be the entree?"

        $ learnmove = renpy.call_screen("rememberablemoves", tutormon)

        if (learnmove == "Back"):
            sycamore @talkingmouth "There is no rush."

            jump movetutor611

        else:
            $ tutormon.LearnNewMove([(0, learnmove)])

            if (learnmove not in tutormon.GetMoveNames()):
                jump movetutor611

sycamore @talkingmouth "A pleasure, Monsieur [last_name]."

hide sycamore

pause 1.0

show janine with dis

janine @talking2mouth "Sparring time. You all know the drill. Pick a partner and get down to it. For this match, try bringing your opponents down to as close as possible to 1 HP without knocking them out."
janine @talkingmouth "Control is key. Control over your Pokémon's strengths, your opponent's strengths, and the pace of the battle."

hide janine with dis

redmind @thinking "Alright. I should partner with[ellipses]"

show janine with dis

janine @talking2mouth "Come with me."

red @confused "Sure?"

narrator "Janine leads you to a secluded corner of the Battle Hall."

janine @talking2mouth "Where's Leaf?"

red @happy sweat "Oh, {i}that's{/i} what this is about."
red @talking2mouth "Um[ellipses] she's in a hotel. She hasn't been feeling well for a while now--trying to sleep it off."

janine @talking2mouth "She understands these Battle Team meetings are mandatory, right? Like, you can't pick and choose when you attend. We're not the Coordinator Club."

red @talking2mouth "Yeah, she gets it. I know she'd be here if she could be--she {i}loves{/i} battles, and loves the Battle Team, too."

janine "[ellipses]"
janine @talking2mouth "Tell her that as soon as she's up for it, I need her to reach out to me."

red @sadbrow talkingmouth "So she's {i}not{/i} in trouble?"

janine @angrybrow talking2mouth "She {i}will{/i} be."
janine @sadbrow talking2mouth "But she's not yet, no. We all have down days. I guess I can imagine a down week, too."

pause 1.0

menu:
    ">Ask about Blue":
        red @talking2mouth "Sorry if this is, uh, crossing any lines, but[ellipses] what's up with Blue?"

        janine @talking2mouth "What do you mean?"

        red @closedbrow talking2mouth sweat "I just[ellipses] you called everyone to the Battle Hall because he asked you to, right?"
        red @talking2mouth "And in exchange, he gave a lecture? And I'm pretty sure you invited--or at least allowed--Sycamore to be here for this meeting."
        red @talking2mouth "It kinda feels like you're trying to help Blue out, somehow."

        pause 1.0

        janine @talking2mouth "Uh, yeah."
        janine @talkingmouth "I am. I'm the Battle Team Captain. That's what I do."

        pause 1.0

        janine @talkingmouth "Don't tell me you're jealous, [first_name]."

        red @surprisedbrow lightblush surprisedmouth "Wha--no! No, of course not!"

        $ ValueChange("Janine", 5, 0.5)

        janine @smilemouth "Hmph."
        janine @closedbrow talkingmouth "I can't believe it. I {i}actually{/i} spoiled you."

        pause 1.0

        redmind @upeyes sadeyebrows frownmouth "Wait[ellipses] am I? Was that actually it? I was just jealous of him?"
        redmind @closedbrow frownmouth "If that's it, I should cut it out. Janine's done way more for me than she has for Blue, anyway."

    ">Stay quiet":
        pass

janine @talking2mouth "We've wasted enough time. Go pick out a partner and spar."

red @happy "Yes, Captain."

pause 0.5

janine @closedbrow talkingmouth "I feel like you were more fun when you were terrified of me[ellipses] *{i}Sigh.{/i}*"

if (CanBunnyRecruit("Janine")):
    narrator "Now seems like it might be a good time to mention the party on Saturday[ellipses] do you want to bring it up?"

    menu:
        "Yes.":
            call BunnyRecruit("Janine", False) from _call_BunnyRecruit_14

        "No.":
            pass
  
call clearscreens() from _call_clearscreens_282 
scene blank2 with splitfade

$ BattleTeamTraining()

ethan battleteam sweat @closedbrow talking2mouth "Man, I'm beat. {i}Barely{/i} knocking out your opponents is way harder than just plain-ol' knocking them out."

red battleteam sweat @talking2mouth "Seriously. I'm looking forward to a nice hot shower."

ethan @talkingmouth "Hey, Blue! You coming with us? Campus gets scaa~aary at night."

blue battleteam @talking2mouth "Uh[ellipses] go on ahead. I'm going to talk to Sycamore again."

ethan @talking2mouth "Alright, man. Don't think too hard about twisting the knife in your gramps' back."

blue @angrybrow talking2mouth "Oh, piss off."

jump day010612