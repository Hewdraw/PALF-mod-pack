label day010530:

$ timeOfDay = "Morning"
call clearscreens() from _call_clearscreens_221
call calendar(1) from _call_calendar_55

$ calDate = calDate.replace(day=30, month=5, year=2004)

$ HealParty()

stop music

scene blank2
show morning at vspaz

narrator "You wake up with no particular plans for the day."
narrator "What a nice change of pace! You are free to spend Sunday however you want."
narrator "Keep in mind that, if you have any interest in participating in the [bluecolor]Millennium Drop Water Festival Contest{/color}, you should increase your [contestcolor]Coordinating Knowledge{/color} before the preliminaries on [bluecolor]Wednesday.{/color}"
narrator "Joining the Millennium Drop will be a significant time commitment. However, passing up this opportunity means you may never have any success as a Coordinator, for the rest of your life. [bluecolor]The choice is yours.{/color} Think carefully."

call freeroam() from _call_freeroam_37

stop music fadeout 1.5

call clearscreens() from _call_clearscreens_222

$ renpy.music.queue("Audio/Music/Pallet Town A.ogg", channel='music', loop=True, fadein=1.0, tight=None)

scene suitenight 
show leaf hatless:
    xpos 0.2 xzoom -1
show yellow: 
    xpos 0.6
show ethan casual:
    xpos 0.4
show blue og:
    xpos 0.8 xzoom -1
with splitfade

leaf @talking2mouth "Meeting time, everybody."

blue @talkingmouth "I see your mouth moving, and I {i}already{/i} know that--"

yellow @angrybrow frownmouth "Ahem."

blue @wistfulbrow talkingmouth "--I am willing to hear you out."

leaf @happy "Awesome! Because I have come up with--"

show leaf surprisedbrow frownmouth
show yellow happy
show ethan happy
show blue happy
with vpunch

Character("Dorm 25 Sans Leaf") "\"A plan?\""

show yellow -happy
show ethan -happy
show blue -happy
with dis

pause 0.5

leaf -surprisedbrow -frownmouth -surprised @flirtbrow talkingmouth "It seems my reputation as a master strategist precedes me. Yes, my generals, I have come up with a plan."

ethan @unamusedbrow talking2mouth "Do we have to go into the forest?"

leaf @talkingmouth "Nope."

blue @sad2eyes talkingmouth "Is it something that benefits {i}only{/i} you?"

leaf @flirtbrow talking2mouth "No."

red @talkingmouth "Is it something that--"

leaf @angry "You are all assholes."

yellow @sadbrow talkingmouth "Um."

leaf @sadbrow talkingmouth "Not you, sweetheart, you're an angel."
leaf @talkingmouth "It's just a movie, guys. A movie and popcorn."

pause 1.0

yellow @happy "That sounds lovely."
yellow @talking2mouth "Do you have one in mind?"

leaf @closedbrow talkingmouth "Yep. {i}151 Things I Hate About You.{/i} It's this teen romantic comedy that came out five or six years ago."

blue @closedbrow talkingmouth "...I'm fine with this, but don't blame me if I start snoring."

ethan @talking2mouth "Eh, alright. I'll give it a shot."

leaf @happy "Great! I've already bought the popcorn, so you guys just get cozy on the couch. I'll be right back."

hide leaf with dis

pause 1.0

ethan @sweat closedbrow talking2mouth "Hey, do you think one of us should go with Loaf? Make sure she doesn't... uh... you know?"

show leaf:
    xpos -1.0

leaf @talking2mouth "It's just popcorn, Ethan! I know how to make it!"

pause 1.0

leaf @talking2mouth "Okay, how many times do I press the popcorn button?"

yellow @sadbrow talking2mouth "Oh, Leaf, no..."

scene blank2 with Dissolve(2.0)

pause 2.0

show makingmemoriesofafuture with Dissolve(2.0)

$ hideside = True

Character("Actor Lars") "\"Hello, Katarina. Make anyone cry today?\""
rosa @talkingmouth "Sadly, no. But it's only 4:30!"

pause 1.0

rosa @talkingmouth "I don't like to do what people expect. Why should I live up to other people's expectations instead of my own?"
Character("Actor Fabio") "\"So you disappoint them from the start and then you're covered, right?\""
rosa @talkingmouth "Something like that."
Character("Actor Fabio") "\"Then you screwed up.\""
rosa @talkingmouth "How?"
Character("Actor Fabio") "\"You never disappointed me.\""

pause 1.0

rosa @talkingmouth "I hate the way you talk to me, and the way you cut your hair. I hate the way you drive my car. I hate it when you stare."
rosa @talkingmouth "I hate your big dumb combat boots, and the way you read my mind. I hate you so much it makes me sick; it even makes me rhyme."
rosa @talkingmouth "I hate it, I hate the way you're always right. I hate it when you lie. I hate it when you make me laugh, even worse when you make me cry."
rosa @talkingmouth "I hate it when you're not around, and the fact that you didn't call."
rosa @talkingmouth "But mostly I hate the way I don't hate you. Not even close, not even a little bit, not even at all."

pause 1.0

$ hideside = False

ethan casual @closedbrow talkingmouth "Oh, now I get why the movie's called that."

yellow @sadbrow frownmouth blush "{i}Sniff.{/i} {i}Sniff.{/i}"

blue og @closedbrow tears lightblush angrymouth "Just a buncha... melodrama. {i}Shoulda talked to each other sooner...{/i}"

redmind casual hatless @sadbrow "...This is nice."
redmind @happy "Just watching a movie together with a group of friends... and Blue."
redmind "Reminds me of how it was years ago, back in Pallet Town."

stop music fadeout 3.33
queue music "audio/music/lawrencetheme_start.ogg" noloop
queue music "audio/music/lawrencetheme_loop.ogg" 

pause 1.0

narrator "While you and your dormmates watch this show, however... another show is playing out in a different part of campus."

scene blank2
show phobosface 
with Dissolve(3.33)

Character("???") "\"{w=0.333}Heh heh heh... {w=0.333}heh heh heh... {w=0.333}heh heh heh!!!\""
Character("???") "\"Of course, of course, of course! What do you take me for? Trust me, J, everything is going {i}exactly{/i} according to plan.\"" 
Character("???") "\"[bluecolor]The Millennium Drop Water Festival Contest{/color} will proceed under the conditions I have constructerated, and my pawn will claim the trophy exactly as commanded.\""
Character("???") "\"Oh? That little Battle Hall diversion? Forgive me my amusements. I wanted to see if those stones you acquired were the {i}actual{/i} deal, after all.\""
Character("???") "\"Wasting time? Hah hah hah! No, definitely not. But if I were... is this not our time to waste? Where is the rush?\""
Character("???") "\"After all... we have {i}Eternity.{/i}\""
Character("???") "\"*Click.*\""
Character("???") "\"Ahahahaha... Ahahahahah... Ahahahah--\""

hide phobosface
show phobosoffice
show phobos surprisedbrow frownmouth goggles 
show melody on:
    xpos 0.75 xzoom -1
with vpunch

melody @talking2mouth "You done with your dorky evil conference call?"

phobos angrybrow @closedbrow sweat talkingsharkmouth "Melody, you aren't supposed to come in here when I'm {i}talking{/i} with my {i}associates{/i}."

melody @talking2mouth "It's not like I don't know about it. Evil plan, yadda yadda, secret council, codenames and stuff. You know I don't care about any of that."

phobos @sad2eyes talking2sharkmouth "You do not treat my machinamations with the respect they deserve. And we're not {i}evil.{/i} We're a group of dedicated fighters for a higher cause that--"

melody @talking2mouth "You're sitting in a dark room, plotting against a bunch of kids, wearing dork-butt goggles that make you look like a Shroodle. You're evil."

phobos -goggles @angry "My goggles are not dork-butt! They are highly-sophisticated analyticritical gear! And we're not plotting against Kobukan, but against {i}society!{/i}"

melody @sadbrow talking2mouth "The more I hear about this plan, the lamer it sounds."

phobos @angrysharkmouth "Leave me! I have more... more planning to do!"

melody @talking2mouth "Hold on. I've got another favor to ask."

phobos @confusedeyebrows talking2sharkmouth "Another one? Was it not enough I brought you back into this school? Do you realize {i}how much{/i} money that took?"

melody @talking2mouth "You didn't do that part for me. I know how important I am to your 'schemes.'"
melody @closedbrow talking2mouth "And as long as I know that... I know that you'll be a good 'uncle' and give me another favor."

phobos @angrybrow angrysharkmouth "You... you... you...!"

melody @talking2mouth "The Battle Team is way more powerful this year than last year. Most students are. I want to know why."

show phobos surprisedbrow with dis

pause 1.0

phobos @talkingsharkmouth "What? Well, surely there are a variety of factors, including environmental and educational--"

melody @talking2mouth "No, it's never that. {i}Something{/i} or someone caused it. Find out what."

pause 1.0

phobos @angrybrow angrysharkmouth "I don't see how this relates to your plan at all."

melody @talking2mouth "Planning? No, that's your thing. That's what that useless Drayden does. That's what that pervert Wallace does."

melody @talking2mouth "I don't plan."

show melody angry:
    xzoom -1 xpos 0.75
    ease 0.5 xzoom 1

pause 0.6

stop music

melody "I ruin."

scene blank2 

pause 3.33

jump day010531
