label day010525:

$ timeOfDay = "Morning"

call calendar(1) from _call_calendar_50

show morning at vspaz

$ calDate = calDate.replace(day=25, month=5, year=2004)

pause 3.0

$ renpy.music.play("Audio/Morning_ambience.ogg", channel='crowd', loop=True, fadein=1.0)

scene suite
show screen currentdate
show yellow frownmouth unamusedbrow uniformlowponytail
with splitfade

$ renpy.pause(1.0, hard=True)

hide blank2

$ PlaySound("knock.ogg")

red uniform @happy "Morning, Yell'!"

yellow @talking2mouth "...Morning."

red @talkingmouth "Do something new with your hair?"

yellow -unamusedbrow @sadeyebrows sad2eyes talking2mouth "...Blue never notices."

pause 1.0

redmind @confusedeyebrows frownmouth "Okay."

red @talkingmouth "Noticed you and Ethan weren't there for game night last night. That's two weeks we've missed it, right?"

redmind @thinking "Hm. Maybe Blue and Leaf actually {i}do{/i} have something in common."

yellow @closedbrow talking2mouth "Yes... I went to bed early."
yellow @sad2eyes talking2mouth "I was watching a Coordinator club meeting. It went a bit long... and I didn't want to risk leaving while Lisia was training the coordinators, in case she thought I {i}was{/i} one, trying to escape."

red @happy "I heard she can get pretty intense."
red @talkingmouth "But I didn't know you were interested in Coordinating."

yellow @talking2mouth "I'm not, really. I was just looking for something to do."
yellow @sad2eyes talking2mouth "Normally, I spend my evenings with Blue, but... since we weren't talking..."
yellow @talking2mouth "Well, I wandered all over the school until I found the coordinators."

red @talking2mouth "Think you might try out?"

yellow @surprised "N-no! Definitely not!"
yellow @happy "They're all so pretty and graceful and confident. I wouldn't last a second in the ring with them."
yellow @blush sad2eyes sadeyebrows happymouth "Besides, the outfits the coordinators wear... they're a bit much for me."

red @talkingmouth "Hey, never know 'til you try."
red @closedbrow talking2mouth "So the Coordinator Club holds its meetings on Mondays?"

yellow @talking2mouth "Not usually. But Lisia's been holding a lot of extra meetings. There's a big contest coming up, and Lisia wants to make sure the Coordinator Club puts on the best show they can."
yellow @closedbrow talking2mouth "The contest was called the... hm..."
yellow @closedeyes angryeyebrows talking2mouth "I think it was called the [bluecolor]'Millennium Drop Water Festival Contest'{/color}?"

red @talkingmouth "Bit of a mouthful."

yellow @closedbrow talkingmouth "Yeah, they just called it the [bluecolor]Millennium Drop{/color}."

red @talkingmouth "Might be fun to watch."

yellow @talking2mouth "If you want, you can attend a Coordinator club meeting."
yellow @happy "Lisia calls them almost every other day. If there's not one today, there should be tomorrow."

red @closedbrow talking2mouth "Yeah, maybe I'll do that."

$ PlaySound("Pokemon/pikachu_confused2.ogg")
libpikachu @surprised "Pika?"

red @happy "Don't worry. I'm not going to make you participate in a contest, buddy."
red @closedbrow talking2mouth "Well, unless you want to, I guess."
red @happy "Who knows? I always said I was going to be a Pokémon Champion. Never specified what kind. Maybe I'm going to be a contest champion?"

show yellow -frownmouth happyeyes with dis

$ PlaySound("Pokemon/pikachu_happy3.ogg")
libpikachu @happy "Pika-a-a-a!"

red @unamusedbrow talking2mouth "...You didn't have to {i}laugh{/i} at me, [pika_name]."

stop music fadeout 1.5 channel "crowd"

scene blank2 with splitfade

pause 1.0

scene homeroom 
show oak 
with splitfade

narrator "Homeroom passes quickly, with Oak seeming serious and focused, hinting that the quiz coming on Thursday will involve the effects of terrains..."
narrator "The only hiccup is Melody, who abruptly leaves twenty minutes before the end of class."

show oak angrymouth with dis

narrator "Sam's lips tighten, but he otherwise doesn't react."

redmind uniform @thinking "Roxanne said no-one can touch Melody. Does Sam already know that? Or has he not tried yet?"
redmind @thinking "Well, at least she was wearing her uniform this time..."

jump homeroom1transition