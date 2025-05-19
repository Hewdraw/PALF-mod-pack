

label usetr:

show screen partyviewer

python:
    teachablemoves = []
    movenames = []
    for move in inventorymetadata[Item.TechnicalRecord]:
        if (move not in movenames):
            movenames.append(move)
            teachablemoves.append((move, move))
    if (len(teachablemoves) == 0):
        renpy.say(None, "You have no Technical Records with valid move data on them.")#this shouldn't show up.
        renpy.jump("exitusetr")
    else:
        renpy.say(None, "Which move would you like to teach?")
        teachablemoves.append(("Nevermind", "abort"))
        teachingmove = renpy.display_menu(teachablemoves)
        if (teachingmove == "abort"):
            renpy.jump("exitusetr")
        teachablemons = []
        for mon in playerparty:
            if (MonCanLearn(mon, teachingmove)):
                teachablemons.append((mon.GetNickname(), mon))
        if (len(teachablemons) == 0):
            renpy.say(None, "None of the Pokémon in your party can learn {}.".format(teachingmove))
        else:
            renpy.say(None, "Which Pokémon would you like to teach the move {} to?".format(teachingmove))
            teachablemons.append(("Nevermind", "abort"))
            teachablemon = renpy.display_menu(teachablemons)
            if (teachablemon != "abort"):
                teachablemon.LearnNewMove(teachingmove, fullpp = False)
            if (teachingmove in teachablemon.GetMoveNames()):
                LoseItem(Item.TechnicalRecord)

jump usetr

label exitusetr:
    return