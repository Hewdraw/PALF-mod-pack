label lunch010407:

$ timeOfDay = "Afternoon"

show cafe behind blank2

queue music "Audio/Music/Route 1 Anime.ogg"

$ renpy.transition(dissolve)
show screen currentdate

hide blank2 with splitfade
$ renpy.pause(0.5, hard=True)

hide afternoon

redmind uniform @closedeyes frownmouth "Hm... Looks like there are a bunch of different tables I can sit at. I know picking a table to sit at is a serious deal, though. I shouldn't take this lightly."
redmind "In order to avoid the absolute desolation of my social standing, {color=#0048ff}I should probably only sit at tables where I know, and have a positive relationship with, everyone there.{/color}"

pause 1.0

narrator "[bluecolor]To be absolutely clear, you need at least one bond point with every character at a table to sit there.{/color}" 

python:
    validtables = []
    tables = ["Angry Table", "Cheerful Table", "Busy Table", "Romantic Table", "Calm Table", "Quiet Table"]
    for table in tables:
        tablevalid = True
        for i, character in enumerate(GetCharsInTable(table)):
            value = (persondex[character]["Value"] if character in persondex.keys() and "Value" in persondex[character].keys() else 0)
            if (value < 1):
                tablevalid = False
        if (tablevalid):
            validtables.append(table)
        
    if (len(validtables) == 0):
        renpy.say(None, "{}Since you cannot currently sit at any main tables, try the Sleeping Table, with Ethan. (On the top left.){{/color}}".format(bluecolor))

jump PickTable