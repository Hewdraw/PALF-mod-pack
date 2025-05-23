label secondhomeroom010528:

scene blank2

play music "Audio/Music/Oak Intro.ogg" noloop
queue music "Audio/Music/Oak Class.ogg"

show homeroom behind blank2
    
$ renpy.transition(dissolve)
show screen currentdate

show oak 
hide blank2 
with splitfade

oak @talkingmouth "Good evening."

pause 0.5

oak @talking2mouth "It has been one week since I have returned to this classroom."
oak @closedbrow talking2mouth sweat "Well, five days, but to quibble about such details is not necessary at this time."
oak @talkingmouth "As we have some time before next Monday's quiz, which I expect shall be of similar difficulty to this Monday's quiz, as opposed to yesterday's, I would like to give a lecture on Champion Lance Tatsuhara."

pause 0.5

oak @closedbrow talking2mouth "...I understand one may see this as an irrelevancy in the grand scheme of battling, but this is a calculated move."
oak @talking2mouth "Any student of mine who wishes to become World Champion will eventually have to face him, as, if there is one truth to his existence, it is that he will not cease his attempts to become World Champion under any conditions, ever."

show may sadbrow uniform with dis:
    xpos 0.25

pause 0.5

oak @talking2mouth "Yes, Miss Birch."

may surprisedbrow frownmouth @talkingmouth "What if we aren't interested in becoming World Champion?"

show blue uniform with dis:
    xpos 0.75

blue @closedbrow talking2mouth "Then you're not in my way. Smart move."

oak @closedbrow sweat talking2mouth "Blue, sit down."

hide blue with dis

oak @talkingmouth "In the event you have no ambitions towards the slot of World Champion, or perhaps none towards battle-related fields whatsoever, I'll just ask for your patience as I deliver a very quick history of the Indigo League."

hide may with dis

oak @sadbrow talkingmouth "I'll set a timer to cut myself off. No more than ten minutes."

narrator "You take a quick glance at the clock. 1:03 PM..."

oak @talking2mouth "Champion Lance won the Kanto Championship in 1995, after thirty-four attempts. Breaking with all tradition, Lance executed many of these attempts back-to-back." 
oak @talkingmouth "On May 5th, 1995, Champion Lance launched four formal challenge attempts in a row, a record that has never been beaten before or since."
oak @closedbrow talking2mouth "Of course, the record prior was 'one challenge.' To this day, Champion Lance is the only person who has ever challenged a formal Pokémon League multiple times in a single day."
oak @talkingmouth "His efforts paid off November 11th of the same year. On his thirty-fourth attempt at the Kanto League, he finally became the Kanto champion."

show hilbert uniform with dis:
    xpos 0.75

pause 0.5

oak @talkingmouth "Yes, Mr. Von Schwarzdrachen."

hilbert uniform @sad "You don't have to say the full thing every time..."
hilbert @closedbrow talkingmouth "Anyway, looking at the battle records, it looks like Lance began his challenges in late 1994, then challenged the league multiple times a week until May 5th."

oak @talkingmouth "Yes, I believe that's correct."

hilbert @talkingmouth "But after May 5th, he took a long break. Why was that? He didn't resume his challenges until October, almost six months later."
hilbert @sadbrow talkingmouth "That seems... out-of-character."

oak @surprised sweat "Oh!"
oak @happy "Well, I'm afraid, Mr. VS, I'm not quite sure myself."
oak @talkingmouth "However, your position on the battle team privileges you with a good opportunity to ask, no?"

hilbert @closedbrow talkingmouth "He doesn't talk about himself much."

hide hilbert with dis

oak @closedbrow talking2mouth "Yes, he is rather taciturn."
oak @talkingmouth "In any case, after attaining the Kanto championship, he allowed himself to rest on that victory for a few years. In early 2001, however, he began challenging the Johto league."
oak @talkingmouth "Seventeen attempts later, on the same day he had won the Kanto championship six years earlier, he was entered into another Hall of Fame, becoming the first two-time regional Champion in history."
oak @closedbrow talking2mouth sweat "If we discount Champion Stone's reclaiming of his previous title, of course."

show dawn uniform with dis:
    xpos 0.25

oak @talkingmouth "Yes, Ms. Berlitz."

dawn @talkingmouth "Um... is that when he got rid of a bunch of the Elite Four?"

hide dawn with dis

oak @talkingmouth "Well, that's a rather pointed way of putting it, but the fact of the matter is that he was condensing two Elite Four into one. Some cuts {i}did{/i} need to be made."
oak @talkingmouth "Tell me, who can name some of the members of the Indigo Elite Four?"

pause 1.0

oak @happy sweat "Oh, you can just shout it out. No hands necessary for this one."

show may uniform with dis:
    xpos 0.25

may @talkingmouth "I know Bruno's one!"

show hilbert uniform with dis:
    xpos 0.65 xzoom -1

hilbert @talkingmouth "Instructor Koga's another."

show melody uniform with dis:
    xpos 0.85

melody @talking2mouth "Karen and Will. This is easily-accessible information."

hide may
hide melody
hide hilbert
with dis

oak @talkingmouth "That's correct. Specifically, they are to be challenged in the order of Instructors Will, Koga, Bruno, and Karen."
oak @talkingmouth "However, this Elite Four is formed from unique circumstances, due to the aforementioned consolidation of the Kanto and Johto Leagues."
oak @talking2mouth "Instructors Will and Karen were members of the Johto league that elected to stay on after Lance's ascension."
oak @closedbrow talking2mouth "Elite Four Bruno is in the same position, on the Kanto side of things. And Instructor Koga was recruited from his Gym Leader position by Lance directly."

pause 1.0

oak @angrybrow talkingmouth "But what of the Elite Four that were not carried forward into the Indigo League? Analyzing their history may provide the greatest insight into Champion Lance's weaknesses, given how often..."
oak @sadbrow talkingmouth "...Well, how often they beat him, frankly."
oak @talking2mouth "The Johto league Elite Four members that were not retained were named Walker Wayne and Magnus Kobushi."
oak @closedbrow talking2mouth "Walker, a Flying-type specialist, was a former Gym Leader in Violet City." 
oak @talkingmouth "He supposedly took his defeat at Champion Lance's hands quite poorly, and immediately left Johto, swearing not to return until he could prove himself the superior Flying-type master."
oak @happy "One supposes that he mistook Champion Lance for a bird keeper, as opposed to a dragon tamer!"

may @closedbrow uniform sadmouth "{size=30}Hm... that sounds familiar... was it something Brendan told me...?{/size}"

oak @talkingmouth "Magnus was a Fighting-type specialist, and was apparently quite inspired by the spirit of competition and battle that Lance showed him." 
oak @talkingmouth "He decided that he wanted to spread that spirit of competition to all of Johto, founding the Pokéathlon dome just outside of Goldenrod City."
oak @talking2mouth "Of course, the Pokéathlon has existed for centuries, but there had never been a single home to practice all events in, that could support such a large audience."

show whitney uniform with dis:
    xpos 0.25 

whitney @happy "I have a baseball bat signed by Magnus! He was a great Pokéathlete himself, years ago."

hide whitney with dis

oak @closedbrow talkingmouth "Quite so."

pause 0.5

oak @sad2eyes talking2mouth "Now... just double-checking my notes..."
oak @happy "Ah, yes. There was no Johtonian champion at the time of Champion Lance's ascension."
oak @talkingmouth "So, let's go over to the Kanto side of things."
oak @talkingmouth "The biggest impediment to his success in his Kanto League attempts was, of course, Lorelei Kanna. Perhaps you have heard her referenced by other faculty--she is Kobukan's trustworthy legal representation."

pause 0.5

oak @talkingmouth "I believe he only had {i}one{/i} Pokémon that could resist Miss Kanna's many piercing Ice-type attacks. Indeed, the majority of his thirty-four Kanto runs started and ended at Miss Kanna's doorway."
oak @talking2mouth "...Perhaps neither could endure the other. Immediately upon Champion Lance's ascendancy, Miss Kanna left the Elite Four."
oak @closedbrow talking2mouth "Whether she left of her own will, or Champion Lance dismissed her, it is not clear."
oak @happy "But I imagine one or the other would be happy to divulge the details!"
oak @talking2mouth sweat "Though... it seems likely that one may need to talk to both to get the {i}full{/i} picture."

pause 1.0

oak @talkingmouth "The fourth Elite Four member was an Alolan girl, actually. Mina. Though quite young, she had prodigious skill, and was a master of the Fairy-type, which has seen {i}very{/i} little success in Kanto, historically."
oak @confused "And she... well, after Lance won against her... she just wandered off. It seems that the third Elite Four member simply hired a child to fill that empty 'strongest Elite Four' position slot as way to 'mock' Champion Lance."
oak @talkingmouth "This was before the Paldean league debuted an even {i}younger{/i} child as a core member of their Elite Four, of course." 
oak @sweat closedbrow talking2mouth "Perhaps it wouldn't have been considered as humorous to lose to an Elite Four containing a child twenty times if such a thing had already been common in another region."

pause 2.0

show blue uniform frownmouth:
    xpos 0.75

blue @talkingmouth "Uh, Gramps? What about Kanto Elite #3?"

oak @surprised "Oh? Didn't I mention? That was Bruno."

blue @closedbrow talkingmouth "No, Bruno was #2. You know, #3? I met her once, right?"

pause 1.0

show oak noshine with Dissolve(2.0)

pause 0.5

oak @talking2mouth "I'm... afraid I have no memory of this person."

blue surprisedbrow frownmouth @surprised "What?"

pause 1.0

blue sadbrow talkingmouth "C'mon, Gramps! Weren't you, like rivals, back in the day? You mentioned her on Wednesday! Agatha!"

oak shadow closedbrow frownmouth @talking2mouth "...I'm sorry. I can't recall anything about... about that person. The third Elite Four member."

pause 1.0

blue wistful "...Sorry. Guess I was wrong."

hide blue with dis

pause 2.0

show oak surprisedbrow frownmouth -shadow -noshine with vpunch

oak @talkingmouth "Wait! I remember! It was her! I--"

$ PlaySound("alarm.ogg")

pause 1.0

oak frownmouth @closedbrow talking2mouth "Drat."

pause 1.0

oak @happy "Well, that's that. Please pardon this little historical tangent. Perhaps I'll give more mini-lectures on the challenge attempts of various other champions--though few are as interesting as Champion Lance's."

scene blank2 with splitfade

narrator "Professor Oak continues to teach about practical battle matters for the rest of the lesson."

$ PlaySound("BellChime.ogg")

narrator "You have some time before your Battle Team meeting... what would you like to do?"

call freeroam from _call_freeroam_33

$ HealParty()

stop music
show screen songsplash("Fuchsia City", "Zame")

queue music "Audio/Music/fuchsia_start.ogg" noloop
queue music "audio/music/fuchsia_loop.ogg"

scene stadium_empty
show screen currentdate
show janine: 
    xpos 0.33
show lance:
    xpos 0.66
with Dissolve(2.0)

janine @talking2mouth "The first match of the second round of the Quarter Qlashes begins on August eighteenth. Slightly under three months."
janine @closedbrow talking2mouth "Naturally, we will encounter no problems."

ethan battleteam unamusedbrow talking2mouth "Just like in Round 1, right?"

janine @talking2mouth "Unnecessary, Ethan."

ethan @closedbrow talking2mouth sweat "Sorry."

janine @talking2mouth "Our training now should be looking ahead, past Round Two. I fully believe everyone can get past Round Two as we are now, so we should be training for the sorts of opponents we'll see in Round Three."
janine @closedbrow talking2mouth "Unfortunately, I'm not sure what battle format Round Two will take, but--"

stop music fadeout 3.33

janine surprisedbrow @talking2mouth "Hm?"

$ PlaySound("clap.ogg")

TempCharacter("???", False) "{w=0.333}*Clap.*" 

$ PlaySound("clap.ogg")

TempCharacter("???", False) "*Clap.*{fast} {w=0.333}*Clap.*"

$ PlaySound("clap.ogg")

TempCharacter("???", False) "*Clap.* *Clap.*{fast} {w=0.333}*Clap.*"

queue music "audio/music/lawrencetheme_start.ogg" noloop
queue music "audio/music/lawrencetheme_loop.ogg" 

show phobos happy with dis:
    xpos 1.333
    ease 0.999 xpos 0.75 #(3 * .25)

show janine:
    xpos 0.33
    ease 0.5 xpos 0.25

show lance:
    xpos 0.66
    ease 0.5 xpos 0.5

lance @talking2mouth "Lawrence."

phobos @sadbrow talkingmouth "Ah, ah, ah. Lance, Lance, Lance, must we get off on the wrong foot so soon? I'd certainly never disrespect you in such a fashion. Baron{w=0.333} Lawrence{w=0.333} Phobos{w=0.333} III, if you please."

show phobos surprisedbrow frownmouth with dis

lance @talking2mouth "I have no interest in pleasing you, Phobos, nor in entertaining your delusions of grandeur."

phobos -surprisedbrow -frownmouth @happy "My, my, my! Such an attitude you have, Lancey-boy."

phobos @closedbrow talkingmouth "Ah, but that's just how your prodiginiousal instructor is, Battle Teamites."
phobos @happy "You'll grow to love him... I'm sure."

janine @talking2mouth "Baron Phobos. Why-"

phobos @happy "To what do you owe this great, extravagant, immaculate, pleasure? Why, only my extreme interest in your development!"

phobos @closedbrow talking2mouth "As you may have heard, the Coordinator Club, my own beloved coordinator club, the one and only, has had a certain uptick in potential recently."
phobos @shadow angrybrow talkingmouth "Is it not fascinating how much more success a group may encounter when they receive an adequate amount of investment? And apparently I have a student to thank for this matter!"
phobos @happy "I'm here only to check on your competency, in comparison. Please, ignore me. Consider me a fly on the wall, a mere annoyance, nothing to be acknowledged!"

lance @sadbrow talking2mouth "I cannot imagine that will be difficult to do."

phobos @happy "Ah-ha-ha! He's so witty. Isn't he hilarious, Battlers? Ah, Advisor Lance... as a board member, I'm very much kept abreast of your status here in this school."
phobos @closedbrow talking2mouth "Supposedly, you've only made a {i}single{/i} student cry this year? Perhaps you're going soft! This time of year, I would have thought you'd hit at least three."

show janine surprisedbrow
show phobos surprisedbrow frownmouth
with dis

sonia battleteam @sad "Advisor Lance... comforted me. When I was crying. He did not cause it."

pause 1.0

show janine -surprisedbrow with dis

phobos -surprisedbrow -frownmouth @happy "That's absolutely lovely, but I think you might be oversharing a bit, no? Rather embarrassing, 'innit?' Don't think we really needed to know that one, did we?"

pause 0.5

janine @angry "Baron Phobos. If you want to-"

phobos @talkingmouth "Talking? Wasn't it clear I was talking? Could you not {i}hear{/i} me talking?"

lance @talking2mouth "Lawrence, you will not speak to my goddaughter that way."

pause 1.0

phobos @noshine talking2mouth "Or what, Lancey?"

lance @closedbrow frownmouth shadow "[ellipses]"

pause 1.0

phobos @talkingmouth "Come now, Battle Teamsters. I think we've all gotten off on the wrong foot. Everyone said a lot of things that I think you'll come to regret, but why should we let that get in the way of our cooperation?"
phobos @happy "I'm a Coordinator--a lover, not a fighter! I even came here with a gift."

leaf battleteam @sadbrow talking2mouth "I have an awful feeling I know what this 'gift' is..."

phobos @happy "Meeeelody!~"

show phobos with dis:
    xpos 0.75
    ease 0.25 xpos 0.6 #(3 * .25)

show janine:
    xpos 0.25
    ease 0.5 xpos 0.2

show lance:
    xpos 0.5
    ease 0.5 xpos 0.4

show melody on bubblemouth:
    xpos 1.2 xzoom -1
    ease 1.0 xpos 0.8

pause 0.5

phobos surprisedbrow frownmouth @happy "Mel-"

lance @talking2mouth "Absolutely not."

phobos @happy "Now, now, there's lots of other factors to consider. Let's not let any of those {i}nasty{/i}, {i}awful{/i}, {i}distracting{/i} prejudices interfere with our good judgment."
phobos -surprisedbrow -frownmouth @talkingmouth "Nor your pride, Lancey-boy."

lance @talking2mouth "I have neither pride nor prejudice."

redmind battleteam @unamusedbrow unamusedmouth "Having difficulty believing that one."

show melody surprisedbrow with dis

lance @talking2mouth "Melody brings nothing worthwhile to the team we do not already possess."

show melody sadbrow with dis

janine @talking2mouth "This is true. We will not consider adding {i}anyone{/i} to the team."
janine @angrybrow talking2mouth "Though, if I {i}was{/i} going to, it would not be Melody, it would be Raihan--a Gym Leader strong enough to beat some champions."

pause 1.0

melody -sadbrow -bubblemouth @talking2mouth "Yeah, that's fair. I'd pick him, too."
melody @talking2mouth "Alright. We tried. No luck. Let's bounce."

phobos @happy anger sweat "Now, now, now. Let's not throw in the towel just yet."
phobos @closedbrow talkingmouth "Perhaps Melody's prodigious talent in the nobler art of Coordinating means she isn't the {i}strongest{/i} battler, but I imagine she's stronger than your weakest Battle Team Member. Perhaps not an addition..." 
phobos @winkbrow talkingmouth "But a substitution?"

janine @talking2mouth "All my Battle Team Members have potential exceeding Melody's."

melody @talking2mouth "{size=30}Ow.{/size}"

phobos @talkingmouth "Potential? Come now, the Battle Team has never cared about potential. Not even back in my day. You want strength, yes? Well, pit her strength against yours!"
phobos @happy "Surely you're not afraid of a little friendly competition from a 'Coordinator.'"

janine @talking2mouth "I will {i}not{/i} be changing the composition of the Battle Team."

phobos @closedbrow talkingmouth "Such... {i}inflexible{/i} thinking. Battlers really are a separate breed, aren't they, niece?"

melody @talking2mouth "I... look. She said no. We don't need this. Let's just go."

phobos @talkingmouth "No, no, no! That simply can't happen. We need to give it the old Kobukan try, at the very least."

phobos @talking2mouth "Tell you what, oh Captain of the Battle Team. If you graciously permit my champion to fight yours, then, assuming she loses, we'll say no more of the matter." 
phobos @happy "And... if she wins... then I simply must insist that you allow her to join the team."
phobos @talkingmouth sadbrow "I do {i}hate{/i} to play this card, but please remember I {i}am{/i} a Kobukan board member."

lance @talking2mouth "One of many."

phobos @closedbrow talkingmouth "Granted, but we are often of one mind about... various topics."

lance @closedbrow talking2mouth "Not when it comes to the Battle Team. If you were, I've no doubt you would have hastened its closure."
lance @sadeyes talking2mouth "Janine, you have nothing to fear from Lawrence's insubstantial bluff."

janine closedbrow "{w=0.5}.{w=0.5}.{w=0.5}."

redmind battleteam @thinking "She... seems conflicted."
redmind @thinking "I guess she doesn't want to give into Lawrence's implied threat... but at the same time, she doesn't want to {i}not{/i} let the Battle Team battle..."

menu:
    ">Volunteer to battle":
        $ AddEvent("Janine", "VolunteerBattle")
        
        pause 1.0

        redmind @thinking "Hm? Did she hear me...?"

        show janine smilemouth -closedbrow with dis

        $ ValueChange("Janine", 10, 0.2)

        janine @talking2mouth "Jeez, [first_name]... so reckless. Always getting in fights."

        show melody surprisedbrow with dis

        janine -closedbrow @talking2mouth "Sorry about this guy. I can't control him. If he wants to battle, he will."
        janine @closedbrow talking2mouth "Personally, I'd be against it, of course..."

        show melody -surprisedbrow with dis

        phobos @shadow happy "Oh, of course! Battle Teamaggots. So headstrong. So... passionate. Just like I remember."

    ">Stay silent":
        janine @confusedbrow talking2mouth "...Ugh. Fine. I'll make someone battle Melody."

        phobos @happy "Of course you will."

        janine @sad "{w=0.5}.{w=0.5}.{w=0.5}."
        janine -closedbrow @talking2mouth "[first_name]. You're up."

        red @talking2mouth "Alright."

janine @talking2mouth "A single battle. One round. No funny business."

melody @talking2mouth "...You. [melody_name], right?"

if (melody_name != first_name):
    red @talking2mouth "You know it's not."

melody @talking2mouth "...I should let you know, I don't make a good first impression in battle."
melody @talking2mouth "Of course, I don't make a good first impression, period."
melody @angrybrow talking2mouth "And the really sad part is..."
melody angry "You won't be around for the second impression."

redmind @angrybrow frownmouth "{i}We'll see.{/i}"

python:
    trainer1 = MakeRed()
    trainer2 = MakeTrainer("Melody")

call Battle([trainer1, trainer2], customexpressions=["red battleteam angrybrow frownmouth", "red battleteam angrybrow frownmouth", "melody on", "melody on bubblemouth"], dialogfunc=firstmelodybattle) from _call_Battle_166
$ RecordBattle("Melody1")

stop music
show screen songsplash("Fuchsia City", "Zame")

queue music "Audio/Music/fuchsia_start.ogg" noloop
queue music "audio/music/fuchsia_loop.ogg"

if (not WonBattle("Melody1")):
    show janine sad with dis
    show lance angrybrow with dis
    show phobos happy with dis
    show melody on sadbrow with dis:
        xpos 0.8

    melody @talking2mouth "{size=30}What...?{/size}"

    phobos shadow @talkingmouth "Now, Janine... I believe we had an agreement, no?"

    jump gameover

show janine closedbrow with dis
show lance sad2eyes with dis
show phobos angrybrow frownmouth with dis
show melody on surprisedbrow with dis:
    xpos 0.8 xzoom -1

phobos @sweat closedbrow talking2mouth "Ah, well... that's a bit unfortunlamentable, but..."

melody @talking2mouth "Excuse me."

lance @talking2mouth "You are not excused."

python:
    highestlevel = 13
    for event in persondex["Melody"]["Events"]:
        if (isinstance(event, str)):
            if ("HighestLevelSeen" in event):
                highestlevel = int(event.replace("HighestLevelSeen", ""))
        elif (isinstance(event, tuple)): 
            if ("HighestLevelSeen" in event[0]):
                highestlevel = int(event[0].replace("HighestLevelSeen", ""))

    totalhighestlevel = GetHighestLevel()

if (highestlevel > 16):
    melody @talking2mouth "Talking. You, [melody_name]. What the eff? You have a level [highestlevel] Pokémon?"

    if (totalhighestlevel > highestlevel):
        red battleteam @confused "Uh... yeah? I actually have a level [totalhighestlevel] Pokémon, too. Why, is that weird?"
    else:
        red battleteam @confused "Uh... yeah? Why, is that weird?"

    melody -surprisedbrow -frownmouth -surprised @talking2mouth "No, it's totally normal, except that it's {i}May{/i}."

    red @confused "I don't get it. I mean, I'm a member of the Battle Team. That's pretty normal, right?"

    melody @talking2mouth "Yeah, except that at this time last year, even the Battle Team members had, like, level {i}thirteens{/i}."

    pause 1.0

    red @talking2mouth "Uh... Sonia?"

    sonia battleteam @talking2mouth "Come to think of it, that's a bit true, yes. I suppose I hadn't really noticed."

    show melody surprisedbrow with dis

    melody surprisedbrow @surprisedmouth "Hadn't noticed? You {i}hadn't noticed?!{/i}"
    melody @talking2mouth "Janny, what are you feeding these kids?!"

    janine -closedbrow @angrybrow talking2mouth "Get out of my Battle Hall."

    melody @surprisedbrow surprisedmouth "No, I'm serious. Can anyone tell me? This is just the Battle Team, right? There isn't anyone else who's got these crazy levels, do they?"

    red @confused "What, haven't you battled in gym class?"

    melody @surprisedmouth "Uh, no, I always got kicked out to my pad in the DC's office before then. Are you telling me--"

    red @talking2mouth "Yyyeah. I just battled Misty earlier today. Uh, level twenty-twos. One level twenty-three."

    pause 1.0

    melody surprised up "What the ess?"

else:
    melody @talking2mouth "Sucks to be me, then."

red @angrybrow talking2mouth "Hold on. I have a question for {i}you.{/i} Where did your Wimpod get its{nw}"

hide melody with dis

extend @unamusedbrow talking2mouth " and you're walking away now, fantastic, that's awesome. It's not like my ability to pay for this school depends on knowing the answer to that question."

phobos closedbrow frownmouth @talkingmouth "A good coordinator always knows when to leave the stage. That being said..."
phobos @happy "I'm... so {i}happy.{/i} You've all proven that the Battle Team is {i}even stronger{/i} than it used to be. Which is... {i}so...{/i} fantastic."
phobos @talkingmouth anger "You're doing a fantastic job, Janininine."

janine -closedbrow @talking2mouth "You're clenching your teeth so hard your eyes are bloodshot."

phobos -closedbrow -frownmouth @talkingmouth "Nonsense. I'm just possessed of a very firm jawline."
phobos @talkingmouth "But I've other matters to attend to. [melody_name], was it?"

if (melody_name != first_name):
    red @talking2mouth "No."

phobos @talkingmouth "I couldn't help but notice you may have offhandedly mentioned a certain difficulty in paying for Kobukan?"

red @closedbrow talkingmouth "Yes, but--"

phobos @happy "Fantastic! Glad to hear that our tuition continues to be competitive."
phobos @talkingmouth "But there is {i}one{/i} offer that I believe may interest you, given your monetarility issue."

red @confused "...Hm?"

phobos @talkingmouth "Perhaps you've heard of an upcoming contest that Kobukan has the honor of hosting? The Millennium Drop Water Festival Contest?"

red @talking2mouth "I've heard the name a couple times, yes."

phobos @talkingmouth "Ah, well, since you haven't, let me tell you. It's based on an old Hoennian tradition. Supposedly, every one thousand years, the sky would be lit aglow by a most miraculous of celestial bodies."
phobos @happy "But this star was not one of only beauty--but also coolness, intelligence, cleverness, and, indeed, toughness."

janine @closedbrow talking2mouth "{size=30}He's forcing it.{/size}"

phobos @talkingmouth "To celebrate the appearance of this star, the citizens of olden Hoenn would throw a massive festival of beauty and performance."
phobos @winkbrow talkingmouth "And then--and follow this--it is so said that, one year, their performances so thrilled and excited the star that, in order to show its gratitude to the brilliant coordinators, it granted one wish to each of the top performers."
phobos @talking2mouth "Ah ha! You see now how this connects to your very own sorry situation!"

red @unamusedbrow talking2mouth "It literally doesn't matter what I say here, does it?"

phobos @surprised "Oh, you still fail to make the connection? Ah, the Battle Team is so... {i}reliable{/i}."
phobos @winkbrow talkingmouth "Allow me to make this fully plain, then. The top three performers in the Millennium Drop Water Festival will have their own wishes, of a sort, made true."
phobos @talking2mouth "Yes, each winner will receive the [bluecolor]Droplet Scholarship for Wonderful Water Students!{/color}"

sonia @talkingmouth "{size=30}Hm... a scholarship would {i}definitely{/i} help patch over some of my money concerns...{/size}"

lance @talking2mouth "I am not fooled for an instant, Lawrence. Why are you telling the Battle Team this?"

phobos @happy "Oh, my champion friend, you've really too much suspicion. This is purely for my own amusement."
phobos @talkingmouth "After all..."
phobos @shadow happy "It will be very amusing to pit your wonderful Battle Teamidgets against a challenge that requires a {i}modicum{/i} of class, and cannot be purely brutalized through, no?"
phobos happy "But that's all I have to say today. Ta-ta, Battle Teamorons!~"

hide phobos with dis

pause 2.0

show lance:
    xpos 0.4
    ease 0.5 xpos 0.66

show janine:
    xpos 0.2
    ease 0.5 xpos 0.33

silver battleteam @closedbrow talkingmouth "Fuck that guy."

ethan battleteam @closedbrow talking2mouth "Seconded."

janine -smilemouth @closedbrow "{w=0.5}.{w=0.5}.{w=0.5}."
janine -closedbrow @talking2mouth "Lance, what are our options?"

lance @sadeyes talking2mouth "He and his niece both hate the Battle Team with a passion. However, he is only one boardmember, and none of the others would authorize him to take any action against it."
lance @closedbrow talking2mouth "'Melody' is a different consideration... but as Phobos' pawn, she has no agency that Phobos does not."
lance @talking2mouth "They cannot be safely ignored, but a wary eye should be adequate response at this time." 
lance @sadeyes talking2mouth "His coordinating interest in the school is in far more danger than anything involving the Battle Team, so he has more to lose through rash action."

pause 0.5

janine @talking2mouth "Alright. Everyone, stay away from Melody and Lawrence, if you can. We don't want to piss them off--even if they can't do anything to us, we don't want them to try."

erika battleteam @sadbrow talkingmouth "...What if I were to have already entered into a conflict with Melody?"

janine @closedbrow talking2mouth "Just... don't do it again."
janine @talking2mouth "We wasted a lot of time on that, so let's get the tutoring over with, so we can get as much training in as possible."

hide janine with dis

pause 0.5

show lance:
    xpos 0.66
    ease 0.5 xpos 0.5

narrator "Lance approaches you immediately."

red @happy "I don't look as bad now, do I?"

lance @talking2mouth "Melody--and more importantly, Phobos--has access to those ridiculous Pikachu rocks you use."
lance @talking2mouth "Further, I see Ethan and Blue do as well."
lance @sadeyes talking2mouth "Your teammates would appreciate if you were to keep a lid on your {i}unique advantage{/i} going forward."

red @talkingmouth sadbrow "I haven't given {i}anyone{/i} one of those stones. Promise."

lance @closedbrow talking2mouth "I believe this, but this does not mean you do not have a duty to prevent them from spreading."

redmind @confusedeyebrows frownmouth "...How the hell am I supposed to do that?"

lance @talking2mouth "Now, if you require tutoring, I am obligated to provide that service."

label movetutor528:

call screen SelectMon
$ tutormon = _return

if (tutormon == 'back'):
    lance @closedbrow talking2mouth "Are you certain?"

    menu:
        "I don't want to teach any of my Pokémon one of their old moves.":
            lance @closedbrow talking2mouth "Very well."

        "On second thought...":
            jump movetutor528

elif (tutormon == pikachuobj):
    lance @talking2mouth "I am unable to teach this... creature. I cannot begin to determine what skills it may have possessed in the past."

    jump movetutor528

else:
    $ tutormon = _return
    $ tutormonname = pokedexlookup(tutormon.GetId(), DexMacros.Name)

    lance @talking2mouth "Your [tutormonname]. Very well."
    
    $ rememberablemoves = GetRememberableMoves(tutormon)

    if (len(rememberablemoves) == 0):
        lance @talking2mouth "This Pokémon has no moves it can remember. Avoid wasting my time."

        jump movetutor528

    else:        
        lance @talking2mouth "Fine. What do you want me to re-teach this Pokémon?"

        $ learnmove = renpy.call_screen("rememberablemoves", tutormon)

        if (learnmove == "Back"):
            lance @talking2mouth "Avoid wasting my time."

            jump movetutor528

        else:
            $ tutormon.LearnNewMove([(0, learnmove)])

            if (learnmove not in tutormon.GetMoveNames()):
                jump movetutor528


lance @talking2mouth "We are finished. I take my leave of you."

hide lance with dis

pause 0.5

show janine with dis

janine @talking2mouth "Lance talked with you about the stones?"

red @talkingmouth "Foreverals."

janine @talking2mouth "Got it. Who came from who?"

red @sweat talking2mouth "Uh, Blue's, Ethan's, and Yellow's stones come from Blue's Eevee. Mine come from [pika_name]. I don't know where Melody's came from, though..."

janine @talking2mouth "I understand."

pause 1.0

janine @talking2mouth "You find out, you tell me."

red @sadbrow talkingmouth "Of course."

janine @talking2mouth "Thank you."
janine @talking2mouth "Oh, yeah. Good job kicking Melody's ass."

$ ValueChange("Janine", 5)

janine @sadbrow talking2mouth "Don't want to imagine what the team would be like with her on it..."

red @confused "Why, what happened last year?"

janine @closedbrow talking2mouth "She broke the team apart. And she wasn't even on it."

pause 0.5

janine @talking2mouth "That's all you need to know."
janine @closedbrow talking2mouth "Now get in line. We're doing some horn drills."

red @confused "...Okay, I know what a drill is, but a 'Horn Drill'?"

janine @talking2mouth "It's an exercise that's supposed to knock you out in one hit."

red @unamusedbrow talking2mouth "I don't see how this is productive."

janine @talking2mouth "If you survive, it means you're a higher level."

red @closedbrow talking2mouth "Oh, clever. It's a pun. Ha."

call clearscreens() from _call_clearscreens_219 
scene blank2 with splitfade

$ BattleTeamTraining()

narrator "Tired and sore, you return to your dorm."

leaf battleteam @sad "Ew... my hair's, like, five pounds heavier, just from sweat."

ethan battleteam @talkingmouth "Yeah, my hat, too..."

red battleteam @happy "You guys want to join me in my morning runs? If you get used to it, it might make Battle Team training less sweaty."

pause 1.0

narrator "Your roommates' silence is deafening."

jump day010529