label day010607:

stop music fadeout 1.5

call calendar(1) from _call_calendar_63

python:
    calDate = calDate.replace(day=7, month=6, year=2004)
    timeOfDay = "Morning"
    renpy.pause(2.5, hard=True)
    #renpy.music.queue("Audio/bigcrowdloop.ogg", channel='crowd', loop=True, fadein=0.5)
    renpy.music.queue("Audio/Music/Oak Class.ogg", channel='music', loop=None, fadein=1.5, tight=None)

scene homeroom
show screen currentdate
show oak 
with splitfade

oak @talkingmouth angrybrow "...hence the importance of stall strategies in competitive settings." 
oak @talkingmouth closedbrow "As the number of Pokémon on the field increases, stalling becomes less and less viable a strategy, but in single battles, there are many situations where a Pokémon can reach the point of practically infinite self-sufficiency."
oak @talkingmouth "Even if you cannot reach that stable equilibrium, though, stall is often simply a matter of using the move that will let you stay on the field just {i}one more turn{/i}. Ah, The Persistence of Memory[ellipses]"
oak @talking2mouth "You may even find that the optimal move, in a situation where your only hope is to stall, has no effect whatsoever."
oak @talking2mouth "Sometimes, every other option would deprive you of a resource you may need later. 'Nothing' is better than 'Something Bad!'"
oak @closedbrow talkingmouth "That being said, it's not as though Pokémon are helpless, even when they have no PP left for their moves."
oak @talkingmouth "You may note a couple of your classmates have a habit of bringing a pair of Cyclizar out into the fields, and using the species' 'Regenerator' ability to battle long past the point at which they have expended all their PP."
oak @happy "A bold strategy! I can only hope it works out for them."

$ PlaySound("bellchime.ogg")

pause 4.0

oak @closedbrow talkingmouth "Well, regardless of if it does or not, it certainly takes a lot of time--and it appears that {i}we{/i} are out of it. Have a good day, students."

hide oak with dis

pause 2.0

show blue uniform frownmouth with dis

pause 1.0

blue @talking2mouth "She's not here."

red uniform @talking2mouth "No."

pause 1.0

blue @talking2mouth "We should tell Yellow and Ethan, right?"

red @talking2mouth "Yeah. They'll want to know."

scene blank2 with splitfade

show screen songsplash("Pallet Town", "Zame")
stop music fadeout 1.5
queue music "audio/music/palletpiano.ogg"

pause 1.0

scene academyhall 
show ethan uniform:
    xpos 0.5
show yellow uniform:
    xpos 0.75
with splitfade

pause 0.5

show blue uniform:
    xpos 0.25

ethan @talkingmouth sadbrow "Guessing by your faces she didn't show up to class."

blue @closedbrow talking2mouth "Ugh."

yellow @talking2mouth "Well, that makes it even more important we get this party perfect, then. Does everyone remember their roles?"

blue @talking2mouth "I'm going to make some food. I'll make that sugary crap Leaf likes, but see if I can sneak some actual nutrients into it."

yellow @talking2mouth "I'll work on sewing costumes for the guests..."

ethan @closedbrow talkingmouth "And I'll figure out how to keep the Disciplinary Committee and Security off our backs, so the party doesn't get shut down early. Being a distraction is my specialty."

yellow @talkingmouth "Which leaves the most important job for you, [first_name]. We're going to need guests. And Ethan, Blue and I are going to need help with our tasks."

red uniform @talkingmouth "Right. I'm in charge of {i}recruitment{/i}."

ethan @closedbrow talkingmouth "By process of elimination, mostly. Leaf's the only other person in our dorm who could be described as anything that vaguely resembles a 'people person.'"

blue angrybrow frownmouth @angry "Hey! What do you mean by that?!"

ethan @confused "You can't honestly think that you--"

show yellow surprisedbrow frownmouth with dis

blue @angry "People {i}love{/i} Yellow!"

ethan @confused "Sure, but there's a difference between 'people liking you' and 'being able to ask people for things.'"
ethan @sadbrow talkingmouth "It's an acquired skill."

yellow -surprisedbrow -frownmouth @sadbrow talkingmouth "I... kind of agree..."

blue -angrybrow -frownmouth @glanceeyes frownmouth "Hmph."

yellow @talking2mouth "Whenever you have a moment--after classes, in-between classes, during lunch, in gym class--look around for people who might be able to help with the party."

red @talking2mouth "Got it."

blue @talking2mouth "Remember, we need people who can cook and acquire food, people who can make outfits, and people who can run interference against Security and the Disciplinary Committee."

yellow @talking2mouth "But the most important thing is that we have guests, of course. But some guests probably won't want to come if we can't promise them something--an outfit, security, or maybe just food."
yellow @talkingmouth "Whatever brings people in the door."

red @happy "You know, I can cook. I can help with the cooking."

yellow @talkingmouth "If it comes to that, that'll be really helpful. But bringing people {i}into{/i} the party is the most important thing we can have you doing right now."

red @talking2mouth "Got it."

ethan @talking2mouth "I wrote some logistical stuff down in this notebook. Here."

$ GetItem(Item.BunnyParty2ElectricPikachu)

red @talking2mouth "'Bunny Part 2: Electric Pikachu'?"

ethan @talkingmouth "Yeah, it's a meme. Anyway, I wrote down a list of roles we need to fulfill, and... {i}roughly{/i}, how many people we're going to want to help with each role."

yellow @talking2mouth "I've[ellipses] never actually planned a party before, and neither has Blue. Leaf obviously wasn't able to answer our questions. So[ellipses]"

ethan @closedbrow talking2mouth "Yeah, somehow, I'm the one who's planned parties the most of this crowd. That was, like, a decade ago, when I was in grade school, but I still remember some stuff."
ethan @talking2mouth "Anyway, make sure to write in that book whenever you loop someone in. [bluecolor]If you do that, you can always check it to remind yourself who you've talked to, and who still needs to be talked to.{/color}"

red @talking2mouth "Alright. We'll check in later today, right?"

ethan @talking2mouth "Yeah."

blue @angrybrow talking2mouth "We've all got a lot of work to do. I don't really care that we're doing it, but if we're going to do it, we need to do it {i}right{/i}. No-one's allowed to slack off or screw up. Got it?"

red @unamusedbrow talkingmouth "Are you sure {i}you{/i} can do your part? Party food needs to actually look good, not just give you enough nutrients to go three days without eating."

blue @closedbrow talking2mouth "Pah. Cooking is the only thing I'd ever admit you're better than me in, and even then, barely. Anything I make is delicious."

pause 1.0

red @talking2mouth "Okay, but it {i}does{/i} need to look good."

blue @surprised "What're you saying?!"

red @closedbrow talking2mouth "You remember that meatloaf that you--"

blue @lightblush angry "That meatloaf fed Daisy and I for three weeks! Our skin was {i}glowing{/i} by the end!"

red @talking2mouth "I'm not saying it wasn't edible. It even tasted great. But it needs to {i}look{/i} good, too."

blue @closedbrow talking2mouth "Pssh. Who gives a damn if it looks awful? It's tastier and healthier than anything they could make, anyway. If they can't get past how it looks, then they're just missing out."

red @closedbrow talking2mouth "Alright. You've got 'til Saturday to get your recipe plans in order, anyway. Maybe something'll change by then."

blue @talking2mouth "Whatever. {i}I{/i} won't be the one letting Dorm 25 down."

show blue:
    xpos 0.25
    xzoom 1
    ease 0.5 xzoom -1

blue @angrybrow talking2mouth "C'mon, Yellow, let's get out of here. No training this week--we're spending every spare second at the dorm, preparing for the party."
blue @angrybrow happymouth "Smell ya later!"

show blue:
    xpos 0.25
    ease 0.5 xpos -0.25

pause 1.0

show yellow happy with dis

yellow "Good luck, Ethan. Good luck, [first_name]. We're really counting on you!"

show yellow:
    xpos 0.75
    ease 0.5 xpos -0.2

pause 0.5

ethan @closedbrow talking2mouth "Alright... running interference. Physical lookouts are so '90s--we need cameras."
ethan @confused "Although... Kobukan has its own cameras, and we're going to need to make sure that we aren't caught on {i}those{/i}, either[ellipses]"

red @sweat closedeyes angryeyebrows talking2mouth "Yeah, we don't want a repeat of what happened with the elections. Not one bunny suit can show up on-camera. It's a big task, but you're up to it, right?"

ethan @happy "Not sure, but we'll find out! Talk to you later, man?"

red @talking2mouth "Probably talk to you immediately. It's time for our first elective, right? Might as well just head there together."

ethan @closedbrow sweat talking2mouth "Oh, yeah. Damn, I've gotten so used to it I even forget it happens."

red @sadbrow talkingmouth "We'll add 'unpacking that' to the list."

ethan @happy "That list's going to take some {i}serious{/i} unpacking when we get around to it in 2047."

$ renpy.transition(dissolve)
call clearscreens from _call_clearscreens_276

show blank2 with splitfade

jump PickElective