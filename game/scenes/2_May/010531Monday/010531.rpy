label day010531:

stop music fadeout 1.5

call calendar(1) from _call_calendar_56

python:
    calDate = calDate.replace(day=31, month=5, year=2004)
    timeOfDay = "Morning"
    renpy.pause(2.5, hard=True)
    renpy.music.queue("Audio/bigcrowdloop.ogg", channel='crowd', loop=True, fadein=0.5)
    renpy.music.queue("Audio/Music/Oak Class.ogg", channel='music', loop=None, fadein=1.5, tight=None)

scene homeroom
show screen currentdate
show oak 
with splitfade

oak @talkingmouth "Good morning, class!"

pause 2.0

stop music fadeout 2.5 channel "crowd"

oak @talking2mouth "{size=40}Ahem!{/size}{w=0.5} Good morning, class!"

pause 1.0

oak @talkingmouth "That's better. Now, what's gotten everyone so excited? I haven't seen this much movement in the Student Body since before the elections."

show may uniform with dis:
    xpos 0.25

may @talkingmouth "The Millennium Drop preliminaries are this Wednesday, Professor! We're all getting our contest routines ready for that."

oak @talking2mouth "Ah... the Millennium Drop...? Yes, I think I remember Instructor Morand saying something about that."
oak @talkingmouth "Hrm. Contests... I'm afraid I've never quite gotten the hang of them. Subjective metrics like 'style' or 'appeal'... it's much easier to tell if you've won a Pokémon battle."
oak @happy "After all, if you're winning, your opponent's Pokémon was knocked out, and if you're losing, yours was knocked out!"

may @sadbrow talking2mouth "That's true, but you can tell if you're winning in a contest, as well! If the crowd is cheering for you, or if the judges are whispering to each other while pointing at you, then you know you're standing out!"

oak @sadbrow talkingmouth "Ah, of course. I'm certain there's a science to it I simply haven't figured out. Please do not mistake my confusion for dismissal."
oak @happy "Why, as a much younger man, I had a friend who quite excelled at contests. She told me a fair bit about it, at the time. Though my memories of it are... fleeting."

may sadbrow poutmouth "[ellipses]"

oak @talkingmouth "Ah... if it helps, I believe I may be able to share some choice information about the Millennium Drop."

hide may with dis

show melody uniform on with dis:
    xpos 0.75 xzoom -1

melody @talking2mouth "Something we don't know?"

oak surprisedbrow frownmouth @talkingmouth neutralbrow "I imagine so. It seemed to have only just occurred to Instructor Waters. Or, er, Champion Wallace."

melody @surprisedbrow talking2mouth "Nevermind. If it was {i}his{/i} idea, I don't care."

hide melody with dis

pause 1.5

oak -surprisedbrow -frownmouth @closedbrow talking2mouth sweat "Er, right. Well, that being the case... I believe the number-one performer across all rounds of the Millennium Drop preliminaries will earn a special prize."
oak @talkingmouth "This prize is none other than an exceedingly rare Feebas. The offspring, I believe, of his very own Champion-level Milotic."

$ renpy.music.play("Audio/bigcrowdloop.ogg", channel='crowd2', loop=True, fadein=0.5)

pause 1.0

oak @happybrow talkingmouth "Yes, I imagined that might get you interested. As I always say, Kobukan is the best place in the world to form connections, to shake hands, and to make memories with the greats of our Pokémon world."

stop music fadeout 2.0 channel "crowd2"

pause 1.0

oak sad2eyes @closedbrow talkingmouth "That being said, we have a test to prepare for later today, so I'd like to get started on the lecture."

narrator "Sam's eyes flick towards his heavily-taped copy of 'Teaching For Geniuses.'"

oak @sad2eyes talking2mouth "{size=30}Ah, yes, here we go.{/size}"
oak -sad2eyes @talkingmouth "Right. I am going to draw a personal connection between the learning material, and something that interests you. This will enable you to associate the information with emotion, which helps recall."

leaf uniform @sadbrow talkingmouth "{size=30}He's got the spirit.{/size}"

oak @talking2mouth "Some moves that are not particularly useful in battle may have new uses in contests. Synchronoise, for example, is a move that is of rare usage."
oak @talkingmouth "It is a Psychic-type move, at 120 BP. This is considerable, but it comes with a significant drawback--it can only affect Pokémon that share at least one type with the user."
oak @talking2mouth "Given it is a Psychic-type move, learned {i}primarily{/i} by Psychic-types, one can see the issue here. It doesn't much matter how powerful it is if it will be hitting, more often than not, an enemy Psychic-type for half damage."
oak @talkingmouth "Given these circumstances, many would say the titular move of the Psychic-type, Psychic, is better in every feasible circumstance."
oak @surprisedbrow talking2mouth "Actually, come to think of it, Umbreon is capable of learning this move--a Dark-type Pokémon, who under normal circumstances cannot make use of Synchronoise whatsoever."

pause 1.0

oak @closedbrow talkingmouth "In contests, however, Synchronoise is a 'Clever' move, which allows you to stay in the back of the performance during the next round, avoiding any issues that may arise from being disrupted by your fellow performers."

pause 1.0

oak @happy "Of course, my job is to teach you about the intricacies and interactions of {i}battle{/i}, not contests. If you have any interest in the latter, I suggest taking Instructor Wallace or Instructrice Fantina's electives."
oak @closedbrow talking2mouth "Hm... I seem to recall my friend had a sister that seemed to draw Coordinators to her as well... though the name escapes me at the moment."

pause 0.5

oak @talkingmouth "Moving on, then. How can we possibly make Synchronoise useful? Well, there's a variety of different ways." 
oak @winkbrow talkingmouth "The paradigm of 'being a Psychic-type, using Synchronoise, and hitting an enemy Psychic-type for half damage' is not the only one accessible to you."
oak @happybrow talkingmouth "There are several non-Psychic Pokémon that have access to Synchronoise, including every one of the so-called 'Eeveelutions.' This is because of the great versatility of Eevee, as emblematic of Normal-types in general."
oak @talking2mouth "Other non-Psychic users of Synchronoise include Psyduck, Chatot, and Whismur's line. Indeed, it is learnable by many Pokémon that have the ability to utilize sound in an offensive capacity."

pause 1.5

oak @talking2mouth sweat "That being said... Synchronoise is not, in actuality, a sound-based move, despite the word 'noise' being in it." 
oak @closedbrow talking2mouth "Terribly confusing, I know, but as it attacks through the psychic link between two Pokémon of corresponding types, and {i}not{/i} by moving air through sound waves, an argument could be made by the pedants who classified it."
oak @sad2eyes sadeyebrows talkingmouth "Not that I'm one to talk, when it comes to accusing others of pedantry. Why, I once debated if a Tamato Berry was a fruit or vegetable for several hours with my college girlfriend, which... er..."
oak @closedbrow talking2mouth sweat "I see now where I went wrong. Let's move on."

pause 1.5

oak @talkingmouth "So, I've now established that Synchronoise can be used by non-Psychic types." 
oak @happybrow talkingmouth "As such, I've also established that it can be used {i}against{/i} non-Psychic-types, and it's worth mentioning it can hit all adjacent Pokémon, both foes and allies."
oak surprisedbrow frownmouth @talking2mouth "You can control the team you bring to the bout--you can control the Pokémon you give Synchronoise too. However, you {i}cannot{/i} control the Pokémon your opponent brings to the match."
oak @talkingmouth angrybrow "What if, after all this, there's still no way to make Synchronoise deal even a single point of damage?"

$ PlaySound("bellchime.ogg")

pause 4.0

oak -surprisedbrow confusedeyebrows frownmouth @confused "...Eh? That's... surely that can't be right."

hide oak with dis

red uniform @surprisedbrow frownmouth "[ellipses]"
red @confused "Wait... class is over?"

show leaf uniform:
    xpos 0.33 xzoom -1

leaf @talkingmouth "Uh, yeah. C'mon, grab your bag."

red @talking2mouth "But that was... it was so fast? Sam actually lectured that whole time, and it {i}didn't{/i} feel..."

pause 1.0

leaf @sarcastic "Exhausting?"

red @sad2eyes sadeyebrows talkingmouth "I mean, {i}I{/i} never had a problem with his lessons, but... huh. I guess when he's teaching us relevant material, or stuff we didn't know, class does actually pass by way faster."

show leaf angrybrow frownmouth uniform:
    xpos 0.33 xzoom -1

show melody uniform on:
    xpos 0.66 xzoom -1

melody uniform @talking2mouth "Wow. He's hit 'bare minimum.' Man's on a rocketship."

#redmind @sadbrow "He's come a long, {i}long{/i} way since that first day of class."

leaf @angrybrow talking2mouth "No-one asked you, Melody."

melody @surprisedbrow talking2mouth "What? What's {i}your{/i} beef? Are you still mad about last Wednesday?"

leaf @angrybrow talking2mouth "Get over it. Klara's told me {i}plenty{/i} about you."

melody @sadbrow talking2mouth "Oh.{w=0.5} Her."

pause 1.0

melody @talking2mouth "Yeah, okay. That's fine. Sure. {i}Klara{/i}."

pause 1.0

show leaf surprisedbrow frownmouth with dis

melody @sadbrow bubblemouth "Genuinely disappointed in you."

hide melody with dis

pause 1.0

leaf @closedbrow talking2mouth "{size=30}What? What does she mean by... what?{/size}"

hide leaf with dis

pause 1.0

show oak happy sweat with dis

oak @happy "Well, I'll finish this lecture before the quiz later today. I'll see you then!"

$ renpy.transition(dissolve)
call clearscreens from _call_clearscreens_258

show blank2 with splitfade

jump PickElective