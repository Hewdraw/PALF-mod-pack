label day010604:

stop music fadeout 1.5

call calendar(1) from _call_calendar_60
$ calDate = calDate.replace(day=4, month=6, year=2004)
$ renpy.music.queue("Audio/Music/Oak Class.ogg", channel='music', loop=None, fadein=1.5, tight=None)
$ timeOfDay = "Morning"

scene homeroom
show oakbg
with splitfade

oak @talking2mouth "{gradualsize=20-36}...which brings to our discussion of One-Hit Knockout Moves, or 'Oh-Kos'.{/gradualsize} Though typically not used in competitive settings, there was a notable Paldean tournament where{nw}" 

$ PlaySound("knock.ogg")

extend " Sheer Cold was--{w=0.5} Hm?"

flannery uniform @tiredbrow talking2mouth "{size=30}Who's knocking on the door this early?{/size}"

leaf uniform @angrybrow talking2mouth "{size=30}It {i}better{/i} not be that Phobos guy again.{/size}"

oak @talkingmouth "Er, yes, {size=40}come in!{/size}"

show wallace :
    xpos -0.1
    ease 0.5 xpos 0.5

wallace @talkingmouth happybrow "Hello, darlings! So, this is Samuel's class? I see a few familiar faces here. Miss Birch, Miss Berlitz, and[ellipses]"
wallace frownmouth @talking2mouth "Melody."

show wallace:
    xpos 0.5
    ease 0.5 xpos 0.33

show melody on uniform with dis:
    xpos 0.66 xzoom -1

melody @bubblemouth "[ellipses]"
melody @talking2mouth "Ex-champion."

pause 1.0

melody @talking2mouth "You're here for me."

wallace @angrybrow talkingmouth "Here for {i}you{/i}? Au contraire. I'm here for the winner of the Millennium Drop Water Festival Contest Tryouts."
wallace @angrybrow "[ellipses]"
wallace @talking2mouth "Which just so {i}happens{/i} to be you."

melody @talking2mouth "Must burn you to have been outvoted so hard."

wallace @talking2mouth "As it happens, your performance... {i}also{/i} impressed me."

melody @talking2mouth "Oh, so you're not as petty as I thought."
melody @bubblemouth "[ellipses]"
melody @talking2mouth "Still a perv, though."

pause 1.0

wallace angrybrow @talking2mouth "Per the rules of the Millennium Drop Water Festival Contest Tryouts, you are entitled to the egg of a Champion's Milotic."
wallace @talking2mouth "This is a prize many coordinators would sacrifice a limb for. You surely recognize the significance."

narrator "Wallace places a carefully-wrapped egg in Melody's hands."

melody @talking2mouth "Yeah."

pause 1.0

melody @talking2mouth "So, it's mine, now? I can do whatever with it...?"

wallace angrybrow talking2mouth "Do not {i}dare{/i}."

if (HasEvent("Professor Oak", "ParticipateMDTryouts")):
    show melody:
        xpos 0.66 ypos 1.0 zoom 1.0
        ease 0.5 ypos 1.2 zoom 1.3

    melody @talking2mouth "Here, hold this for me."

    red uniform @surprised "What?!"

    blue uniform @angry "Oh, come {i}on!{/i}"

    $ GetItem(Item.FeebasEgg, 1, "Melody drops the Feebas egg into your hands before you can even think about rejecting it.")

    show melody:
        xpos 0.66 ypos 1.2 zoom 1.3
        ease 0.5 ypos 1.0 zoom 1.0

    wallace "He {i}may{/i} be a coordinator, but..."

    if (not HasEvent("Instructor Wallace", 1)):
        wallace "You do not {i}re-gift{/i} the favor of a Champion! He has not, even {i}once{/i}, attended my Water-type class! He cannot even train it!"
    elif (classstats["Water"] < 11):
        wallace "You do not {i}re-gift{/i} the favor of a Champion! He has {i}barely{/i} attended my Water-type class! Do you expect him to train it?"
    else:
        wallace "You do not {i}re-gift{/i} the favor of a Champion! {i}You{/i} will train my Lucy's daughter, not him!"

    show wallace frownmouth with dis

    melody @talking2mouth "I don't care if he trains it or not. He can give the egg to someone else, or maybe wait for it to hatch, toss it into his PC forever. I don't know. Don't care."

    melody angry "I just don't want to have anything to do with you. And that includes your 'favor.' {i}Ex{/i}-champion."

else:
    melody @talking2mouth "Nah, I dare. I'm dropping this in the hands of the first person I see who's halfway decent at contests."

    wallace "You do not {i}re-gift{/i} the favor of a champion! {i}You{/i} will train my Lucy's daughter, not some--some unpicked unknown!"  

    melody angry "I don't want to have anything to do with you. And that includes your 'favor.' {i}Ex{/i}-champion." 

pause 1.0

narrator "Wallace glares at Melody with seething fury. It's impossible to tell how Melody is looking at him in response behind her sunglasses, but the curl of her lip implies her expression is quite the same."

wallace @talking2mouth "You will rue this."

melody @angrybrow talking2mouth "You can leave now. This isn't your class."

pause 2.0

show wallace:
    xpos 0.33 xzoom 1
    ease 0.5 xzoom -1
    pause 0.5
    ease 0.5 xpos -0.2

pause 2.0

show melody -angry with dis

melody @talking2mouth "Sorry, Professor Oak. I try to keep my feuds with prettyboy manchildren out of your class."

hide melody with dis

oak "[ellipses]"
oak @talking2mouth "{size=30}Try teaching, they said. It's fulfilling and easy, they said.{/size}"

jump homeroom1transition