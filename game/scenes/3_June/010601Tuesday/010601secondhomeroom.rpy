label secondhomeroom010601:

scene blank2 with splitfade

pause 1.0

play music "Audio/Music/Oak Intro.ogg" noloop
queue music "Audio/Music/Oak Class.ogg"
$ renpy.music.queue("Audio/bigcrowdloop.ogg", channel='crowd', loop=True, fadein=0.5)

show homeroom behind blank2
    
$ renpy.transition(dissolve)
show screen currentdate

show oak 
hide blank2 
with splitfade

pause 1.0

oak @talkingmouth "Hmm, seems everyone's still talking quite excitedly about that upcoming contest..."

stop music channel "crowd" fadeout 2.5

oak @talking2mouth "Perhaps I can deliver a quick lecture on contest strategies, then, before we get into preparations for Thursday's quiz."
oak @talking2mouth "As I'm sure you've noticed, every Pokémon performs better in certain categories of contests, based on what the audience want to see."
oak @talkingmouth "Additionally, moves may have greater or lesser effects when used to enhance the effect of a coordinator's routine, based on what the {i}judges{/i} want to see."
oak @talkingmouth "These categories are the same--I believe the common criteria are Toughness, Coolness, Cuteness, Beauty, and Cleverness."
oak @sweat closedbrow talking2mouth "It irks me to no end that 'beauty' is the only word that does not end in 'ness,' but I suppose that's a frustration I'll just have to deal with."

may uniform @surprisedbrow frownmouth "[ellipses]"
may @angrybrow talking2mouth "{size=30}Actually, that's a good point. Why {i}did{/i} they do that? Dawn, do you know?{/size}"

dawn uniform @sadbrow talkingmouth "{size=30}I don't actually know much about contests, or their history. Just, um, how to win them...{/size}"

oak @talking2mouth "In any case, these categories could be considered 'Contest Types'. Now, I imagine any of you with a passing interest in contests have noticed the 'energy' evaluation that judges give to Pokémon during a contest?"

may @talkingmouth "Right. It's a way to tell how much fun it looks the Pokémon's having, how much effort they're putting in!"

oak @talkingmouth "Which is a very positive sentiment, being rewarded for having fun."
oak @talking2mouth "Pokémon that show these traits generally make stronger appeals. Further, this 'energy' can be expended for an all-out appeal to grab attention--a 'grand finale', if you will."

may @talkingmouth "Most people wait until rounds five or ten to do that, since you get extra points in those rounds!"

oak @closedbrow talkingmouth "Sensible and strategic!"
oak @talking2mouth "There {i}is{/i} a concern, though. Remember that a Pokémon-coordinator pair's rhythm can be thrown off." 
oak @talking2mouth "Perhaps they were shocked by a surprising move used by a fellow performer. In this case, they can instantly lose {i}all{/i} their energy, leaving them stumbling about onstage until they recover their footing."
oak @talkingmouth "Conserving resources until the most efficient moment to use it is definitely a sensible option, but be careful not to hoard them too much! A basket overflowing with eggs is of no use to you if you can't carry it anymore."
oak @closedbrow talking2mouth "Now, I think we should go back to your regularly-scheduled lecturing, unless there's any more questions?"

pause 1.0

oak @confusedbrow talking2mouth "Yes, Melody?"

melody uniform on @talking2mouth "Some people here probably don't know how to get energy in the first place. Seems kind of important?"

oak @confusedbrow talking2mouth "Well... yes, I suppose so."
oak @talking2mouth "If a Pokémon uses a move of one of its own types, it is expressing itself fully, embracing the purest and strongest energy within." 
oak @talkingmouth "From what I have seen in the research I performed last night, that usually causes the judges to bump up a Pokémon's energy rating."
oak @talking2mouth "These would be the same moves that, in-battle, provide STAB--Same Type Attack Bonus, or the 50%% boost in power that Pokémon get when using moves of their own type."
oak @closedbrow talkingmouth "Yes, in contests and battles alike, both trainer and Pokémon thrive most when being true to themselves!"
oak @happy "I'll leave the examination of that metaphor to you and your free time."

pause 0.5

oak @closedbrow talkingmouth "Now, really, we {i}must{/i} get back to the lessons. You students can't keep distracting me like this! I really {i}am{/i} trying to be better."

hide oak with dis

pause 0.5

show oakbg with dis

pause 0.5

melody sadmouth "[ellipses]" 
melody bubblemouth "[ellipses]" 
melody smilemouth "[ellipses]" 

redmind uniform "Hm. Seems like Professor Oak's actually having fun learning about something he didn't know about before."
redmind happy "Besides Foreverals, and Frienergy, and the Mysteriosity in the forest, and [pika_name]'s special form, and--"

scene blank2 with splitfade

$ PlaySound("bellchime.ogg")

pause 1.0

call freeroam from _call_freeroam_39

stop music fadeout 1.5

$ renpy.music.queue("Audio/Music/Cinnabar_Start.ogg", channel='music', loop=None, fadein=0.0, tight=None)
$ renpy.music.queue("Audio/Music/Cinnabar_Loop.ogg", channel='music', loop=True, tight=None)

scene suitenight
show yellow closedbrow frownmouth
with splitfade

yellow @closedbrow talking2mouth "Cool, Beautiful, Cute, Clever, Tough. Cool opposes Clever and Cute. Beautiful opposes Clever and Tough. Cute opposes Cool and Tough. Clever opposes Beautiful and Cool. And, um... Tough opposes Beautiful and Cute."
yellow surprisedbrow @closedbrow talking2mouth "Okay. Again. Cool, Beautiful, Cute, Clever, Tou--"

red @happy "Hey, Yell'."

yellow @talkingmouth "Oh. Hello."

red @talkingmouth "Change your mind about the Millennium Drop Tryouts?"

yellow -surprisedbrow -frownmouth @talking2mouth "N-no, no. No, definitely not."
yellow @sad2eyes talking2mouth "I, um, I just want to be able to follow along. I'm planning on going to watch the other coordinators. I don't... no. Just watch."

pause 0.5

red @sadbrow talkingmouth "Alright. But, hey, maybe I'm completely wrong here, but I think... you know, just make sure you don't do something you'll regret."
red @happy "Or {i}don't{/i} do someting you'll regret, I guess. Kobukan has a lot of opportunities. Once-in-a-lifetime kinda things, you know?"

yellow @sadbrow talking2mouth "...Yeah. Yeah, I know."

pause 1.0

yellow @talking2mouth "Will you be participating in the tryouts?"

red @sadbrow talkingmouth "Guess we'll find out tomorrow. Still got one more day to decide!"

yellow @talkingmouth "True."
yellow @sadbrow talkingmouth "{size=30}Still one more day to decide.{/size}"

pause 0.5 

yellow @closedbrow talkingmouth "Are you going to bed now?"

red @sadbrow talking2mouth "That's between me and whatever emergency pops up on my phone as soon I as I lie down."

yellow @happy "Don't push yourself too hard."

red @happy "Same to you. G'night!"

yellow @happybrow happymouth "Goodnight!"

pause 1.0

yellow sad2brow frownmouth @talkingmouth "Still one more day to decide."

call texting from _call_texting_18

jump day010602