label day010601:

stop music fadeout 1.5

call calendar(1) from _call_calendar_57
$ calDate = calDate.replace(day=1, month=6, year=2004)
$ renpy.music.queue("Audio/Music/Oak Class.ogg", channel='music', loop=None, fadein=1.5, tight=None)
$ timeOfDay = "Morning"

scene homeroom
show screen currentdate
show oak
with splitfade

oak @talking2mouth "Good morning, class. Today, I'd like to elaborate somewhat on the interactions of moves and abilities."
oak @talkingmouth "There are some abilities that are known to be biologically necessary for the Pokémon in question."
oak @closedbrow talking2mouth "As such, these abilities can be considered a 'mandatory part' of the Pokémon, as opposed to merely an additional feature."

pause 1.0

oak @sweat happybrow talkingmouth "Hm... I'm getting some blank looks!"
oak @talking2mouth "Let me see if I can simplify this. An ability like Static is a fairly common one. It is an ability that multiple species can hold, and is not particularly complicated."
oak @talkingmouth "If a Pokémon with Static is hit by a contact move, then there is a chance the foe becomes paralyzed, immunities notwithstanding."

pause 0.5

oak @talking2mouth "One can easily imagine how this might be 'turned off.' Simply put--if a foe makes contact with a Pokémon {i}without{/i} Static, there is no chance of paralysis."
oak @talking2mouth "Barring Synchronize, Effect Spore, or anything of that nature... but let's ignore those conditionals for now."

pause 0.5

oak @talking2mouth "However, there are some abilities that are such an inherent part of the Pokémon that they simply cannot be affected or ignored, through the effects of moves like Gastro Acid, or abilities like Mold Breaker."
oak @talkingmouth "These abilities are often referred to as 'unignorable abilities.' Many of them are tied to the ability to change forms." 
oak @talkingmouth "Zero to Hero, the signature ability of Palafin, and Shields Down, the signature ability of Minior, are examples you may have heard of."
oak @closedbrow talking2mouth "Aegislash, Dondozo, and Eiscue are also amongst this number... I'm sure you can find a full and comprehensive list in the library."

pause 0.5

oak @talking2mouth "There is much overlap between these abilities and abilities that cannot be copied onto another Pokémon, or abilities that cannot be replaced."

pause 0.5

oak @sadbrow talkingmouth sweat "In truth, there's not much one can do except memorize these lists--though, as stated previously, a good rule of thumb is that, if it is a signature ability, or a form-changing ability, it is likely one cannot affect it."
oak @happy "In scenarios where taking away an opponent's tool is not necessarily an option, simply hit them with your own!"
oak angrybrow talkingmouth "You may find that Hyper Beam is an {i}extremely{/i} effective ability-supressing move."

narrator "Professor Oak waxes philosophical on whether power or versatility is a more effective method of winning a battle..."

jump homeroom1transition