label day010409:

$ timeOfDay = "Morning"
call calendar(1) from _call_calendar_5
$ calDate = calDate.replace(day=9, month=4, year=2004)

show morning at vspaz

$ renpy.music.queue("Audio/Music/Oak Class.ogg", channel='music', loop=None, fadein=1.5, tight=None)

show homeroom behind oakbg

$ renpy.transition(dissolve)
show screen currentdate

hide blank2 with splitfade    
hide morning

show oakbg with dis

$ renpy.pause(0.6, hard=True)

redmind uniform @thinking "Despite the bombshell yesterday, Sam seems as casual as ever. I guess he figures his part in this is done, now. He's just waiting for the data to roll in... "
oak @talkingmouth "Now, does anyone remember what the reading said about the origins of Fairy-type Pokémon? [first_name], it looks like you're paying attention! Why don't you give it a stab?"
redmind @surprised "Oh, crap! What did he just say? Something about the reading, and Fairy-types? Ugh, what should {i}I{/i} say?"

menu:
    "{color=#66b77d}[[Knowledge]{/color} >Just recite the entire reading":

        red @closedeyes talking2mouth "Well, Professor, in order to make clear the origins of Fairy-type Pokémon, you need to first understand the obvious importance of reclassification, as defined in page 347, where the 'Fairy' type, previously considered to be..."

        $ TraitChange("Knowledge")

        $ PlaySound("class_groan.ogg")

        narrator "Your classmates are annoyed at you, and Flannery falls asleep, but you manage to answer the question over the course of fifteen minutes."

    "{color=#60c2f8}[[Wit]{/color} >Give a vague, but correct, answer":
        red @closedeyes talking2mouth "The answer to that is simple. The reading's opinion exactly parallels that of the well-known Fairy researcher, Professor Peach."

        redmind @thinking "Yeah, because she was a consultant on the book..."

        $ TraitChange("Wit")

        narrator "Perplexingly, Professor Oak seems pleased with this answer."

redmind @thinking "Ugh. It's exactly stuff like that--that dozing off--that made my grades so bad in Pallet Town. I've really gotta focus up."

jump homeroom1transition