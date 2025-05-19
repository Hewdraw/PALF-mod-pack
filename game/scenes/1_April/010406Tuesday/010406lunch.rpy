label lunch010406:

$ timeOfDay = "Afternoon"

show cafe behind blank2

queue music "Audio/Music/Route 1 Anime.ogg"

$ renpy.transition(dissolve)
show screen currentdate

hide blank2 with splitfade
$ renpy.pause(0.5, hard=True)

hide afternoon

redmind uniform @wince frownmouth "Phew!"

redmind @thinking "I'm beat.{w=0.5} Maybe it's the added pressure of having the whole class watch me during my battle, but I feel like I'm way more tired than I should be."
redmind @thinking "I mean, I'm not even doing any of the real battling, [starter_name] is.{w=0.5} So why am I so worn out?"

show cafe at vpunch

show hilda uniform angry at rightside

hilda @talkingmouth "Hey! [first_name]. What the hell was that?"

red @confused "Uh... Hi, Hilda?"

hilda sad "Yeah, hi, whatever.{w=0.5}{nw}"
extend angry @talkingmouth " What the hell was that?"

red @happy "You're going to have to be way more specific."

show brendan uniform at leftside with dis:
    xzoom -1

show may uniform at centerside with dis

may @talkingmouth "Hey, [first_name]! Is something wrong?"

red @happy "Nah, just talking with Hilda. She's got some questions? I think?"

hilda -angry @talkingmouth "Don't pretend you have no idea what just happened."

red @talking2mouth "I will continue to not pretend to have no idea what just happened."

$ startergenderfragment = "'im"
if (playerparty[0].GetGender() == Genders.Unknown):
    $ startergenderfragment = "it"
elif (playerparty[0].GetGender() == Genders.Female):
    $ startergenderfragment = "'er"
brendan @talking2mouth "Uh... bro, I think she's talkin' about how [starter_name] just did exactly what you told [startergenderfragment] to."

red @confused "Huh?"

may @happy "Brendan told me that you let your Pokémon out in the dorm, and it was completely still! I wasn't sure I believed him, but now I do!"

hilda @talkingmouth "Seriously. That was a brand new Pokémon. You can't train them to be that obedient. Literally, you {i}can't train them.{/i}"

show cheren uniform at midleftside with dis

cheren @closedbrow talkingmouth "I must say, I noticed your Pokémon's peculiar behavior, too. I was hoping to inquire as to how you manage to do that..."

show gardenia uniform at midrightside with dis

show may surprisedbrow frownmouth
show brendan surprisedbrow frownmouth
show hilda surprisedbrow frownmouth 
show cheren surprisedbrow
with dis

gardenia @happy "Yeah, that was so weird! If I didn't know any better, I'd think that you'd been training that Pokémon for months!"

if (not IsNamed("Gardenia")):
    pause 1.5

    red @confused "Er... do I know you?"
    gardenia @surprised "Oh, I guess not.{w=0.5}{nw}"
    $ BecomeNamed("Gardenia")
    extend @happy " I'm Gardenia! Anyway, what's up with how you battle, friend?"

else:
    red @sweat unamusedbrow talking2mouth "Hey, Gardenia."

show may -surprisedbrow -frownmouth
show hilda -surprisedbrow -frownmouth
show cheren -surprisedbrow
show brendan -surprisedbrow -frownmouth
with dis

brendan -surprisedbrow -frownmouth -surprised @closedbrow talking2mouth "You, uh, you picked up a lot of friends pretty quickly, huh, [first_name]?"

cheren @happy "Like I said. 'Inoffensive charisma.'"

show calem uniform at farleftside with dis

calem @talkingmouth "[first_name], I--"

pause 1.0

calem @sad "Hm. Rather too crowded here. We'll chat later."

hide calem at farleftside with dis

show hilbert uniform at farleftside with dis:
    xzoom -1

hilbert @talkingmouth "I'll take his place. You need to answer a couple questions."

show leaf uniform at farrightside with dis

leaf @talkingmouth "Hey, what's up with the crowd?"

show may surprisedbrow frownmouth
show brendan surprisedbrow frownmouth
show hilda surprisedbrow frownmouth 
show cheren surprisedbrow frownmouth 
show leaf surprisedbrow frownmouth 
show gardenia surprisedbrow frownmouth
show hilbert surprisedbrow frownmouth
with dis
red @surprised "Guys! I really don't have any answers. I just ask my Pokémon to do something, and they do it."


show may -surprisedbrow -frownmouth -surprised
show brendan thinking 
show hilda sad 
show cheren thinking
show leaf flirt
show gardenia happy
show hilbert sad
with dis

red @talking2mouth closedbrow "I mean, that's just what Pokémon trainers {i}do{/i}, right?"

hilda @talkingmouth "I mean... I guess."
brendan @talking2mouth "Yeah, but, bro, you make it look so easy..."
cheren @sadmouth "Perhaps you're subconsciously applying some strategy that we haven't yet discovered."
hilbert @talkingmouth "That's bullshit, and I do not believe you."

show hilbert:
    xpos 0.12
    ease 0.5 xpos -0.2

redmind @thinking "...Sigh. They're not really listening, huh?"

hide may at centerside with dis
hide brendan at leftside, dissolveaway 
hide hilda at rightside with dis
hide cheren at midleftside with dis
hide leaf at farrightside with dis
hide gardenia at midrightside with dis

redmind @thinking "I think Sam might be the only one who could answer this question for me... but I swear he's trying to avoid me."
redmind @thinking "Maybe I'll be able to track him down after my next elective."

pause 2.0

if (not WonBattle("Blue1")):
    red @surprised "Wait... I {i}lost{/i} that battle. Did all these guys come here to... cheer me up?"
    pause 1.0
    red @happy "Dorks."
    pause 1.0

show ethan uniform at centerside with dis

ethan @talking2mouth "Hey, bud."

red @talkingmouth "Hey!"

ethan @happy "Good battling. Since we've got the same Pokémon, I can figure out how to battle better by watching you!"

red @angrybrow happymouth "What, like, I'm some sort of crash-test dummy?"

ethan @closedbrow talkingmouth "Well, not a dummy. But a crash-test {i}something{/i}, yeah."

red @talkingmouth "Well, maybe don't follow my example exactly."

if (not WonBattle("Blue1")):
    red @sad "I didn't win, after all."

    ethan @happybrow talkingmouth "Yeah, but that's not cause [blue_name] is any better."

else:
    ethan @happybrow talkingmouth "Why not? You won!"

    ethan @closedbrow talking2mouth "Though I guess that wasn't exactly entirely on you..."

ethan @angrybrow talkingmouth "You know just as much as I do that [blue_name]'s Eevee wasn't listening to a single word he said."

red @talking2mouth "Yeah, I can't deny that. I guess it makes sense that he'd get such a willful and stubborn Pokémon, though. Like trainer, like 'mon."

ethan @closedbrow talking2mouth "I wonder..."

red @confused "Hm? What about?"

ethan @closedbrow talking2mouth "It's just that conversation in the dorm last night. And a few things Professor Cherry said."

red @confused "Are you also getting the vibe that people think training Pokémon is a lot harder than it's felt so far?"

ethan @surprised "Yeah! That's it exactly!"

red @closedbrow talking2mouth "Then I guess we're either very good at it..."

ethan @closedbrow talking2mouth "Or we're about to see why everyone else thinks it's so hard."

red @happy "Let's hope it's the first thing."

ethan @happy "Crossing my fingers!"

show blank2 with dis
    
$ renpy.pause(1.0, hard=True)

stop music fadeout 1.0
$ renpy.music.stop(channel='crowd', fadeout=1.5)

$ renpy.transition(dissolve)
call clearscreens from _call_clearscreens_24

$ renpy.pause(2.0, hard=True)

jump PickElective