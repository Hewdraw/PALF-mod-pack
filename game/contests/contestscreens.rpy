label clearcontestscreens:
hide screen ContestUI
hide screen ContestUIAbove
hide screen ContestChoices
hide screen energyupleft
hide screen energyupright
scene onlayer arrowlayer
with dis
$ RealignTextbox()
return

screen ContestUI():
    layer "master"
    $ ljudges = len(Judges)
    for i, judge in enumerate(Judges):
        $ cutout_y = (i+.5)/ljudges - 0.139
        add Transform("images/GUI/contest/judges_bar.webp", crop=(32, round(cutout_y * 1080), 300, 300)) xpos (0.825) ypos cutout_y
        add Transform(judge.GetImage(), crop=(0, 0, 1000, 800 if judge.GetName() != "Lawrence" else 918)) zoom 0.35 ypos (i+.5)/ljudges + 0.035 xalign (0.98 if judge.GetName() == "Instructor Wallace" else 1.0)
        add Transform("images/GUI/contest/judges_frame.webp", matrixcolor=TintMatrix(GetCharColor(judge.GetName()))) xpos (0.825) ypos cutout_y
        add judge.GetSeekingImage() ypos (i+.5)/ljudges - 0.15 xalign 0.953 zoom 0.7
        
        add "GUI/contest/stars_banner.webp" ypos (i+.5)/ljudges + 0.045 xpos 0.8355 zoom 0.9
        add Transform("GUI/contest/stars_empty.webp", crop=(0, 0, 289 - (45 + (5 - judge.GetJackpotLimit()) * 40), 129)) ypos (i+.5)/ljudges + 0.045 xpos 0.8355 zoom 0.9
        if judge.GetSparks() > 0:
            add Transform("GUI/contest/stars_full.webp", crop=(0, 0, 45 + (judge.GetSparks()) * 40, 129)) xpos 0.8355 zoom 0.9 ypos (i+.5)/ljudges + 0.045

    fixed:
        xmaximum 1552
        add "gui/contest/hint.webp" xalign 0.99 yalign 0.01

        if showround:
            hbox:
                xalign 0.5
                ypos 0.0
                add "contest_round_text"
                null width 5
                for digit in str(Turn):
                    add "contest_round_" + digit yalign 0.5

screen ContestUIAbove(showEnergy=True):
    for i, coord in enumerate(Coordinators):
        vbox:
            yalign 1.0
            xcenter ((i + 1) / 7) - 0.01
            fixed:
                if InActiveContestRound:
                    text str(coord.GetCurrentPoints()) + " Pts" xalign 0.5 size 70 color "#fff" outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ] font "fonts/Delfino.ttf" yalign 0.9
                if showEnergy:
                    add "GUI/contest/energy_empty.webp" xpos 0.45 yalign 0.985
                    if coord.GetEnergy() > 0:
                        add Transform("GUI/contest/energy_full.webp", crop=(0, 0, 38 + coord.GetEnergy()*40, 99)) xpos 0.45 yalign 0.985

screen energyupleft(coordname):
    zorder 100
    add "GUI/double-arrow.webp" yalign 0.5 at swipeinleft, Transform(yzoom = 0.3, xzoom=-0.3)
    text "{size=60}" + coordname + "'s{/size}\nenergy increased!" color "#fff" yalign 0.5 size 80 outlines [ (absolute(10), "#000", absolute(0), absolute(0)) ] at swipeinleft
    timer 2.0 action Hide("energyupleft")

screen energyupright(coordname):
    zorder 100
    add "GUI/double-arrow.webp" yalign 0.5 xalign 1.0 at swipeinright, Transform(zoom = 0.3)
    text"{size=60}" + coordname + "'s{/size}\nenergy increased!" color "#fff" yalign 0.5 size 80 xalign 1.0 outlines [ (absolute(10), "#000", absolute(0), absolute(0)) ] at swipeinright
    timer 2.0 action Hide("energyupright")

screen ContestTooltip(hint):
    frame:
        ypadding 10
        xpadding 15
        background Frame("GFX/DateTimeBanner.webp", 4, 4, 12, 8)
        hbox:
            text "Hint: {} ".format(hint) size 28 color "#1c1c1c" alt ""
    timer 4.0 action [Hide("ContestTooltip", moveoutleft)]

init -2 python:
    def ContestNotify(hint):
        if hint not in shownhints:
            shownhints.append(hint)
            renpy.sound.play("audio/idea.ogg")
            renpy.transition(dissolve)
            renpy.show_screen("ContestTooltip", hint=hint)

screen contestmovedata(move):
    zorder 5
    frame:
        background Frame("GUI/character_frame.webp", 10, 10)
        xsize 1150
        ysize 175
        xalign 0.26
        ypos 0.1
        text move.Name xminimum 550 xalign 0.5 yalign .05 size 100
        text ParseContestEffects(move)[10:] size 40 xmaximum 1100 xalign 0.5 yalign .95

screen ContestChoices(coordinator, startingmon):
    default spendingenergy = False
    $ currentMon = coordinator.GetMon()
    if startingmon != currentMon:
        add "GUI/contest/switched_indicator.webp"

    #$ showteraoption = False
    #if (currentMon != None and Item.TeraOrb in inventory.keys()):
    #    $ showteraoption = True
    #    for allymon in currentMon.GetTrainer().GetTeam():
    #        if (allymon.IsTerad() and (allymon != currentMon or allymon == currentMon and allymon.GetTerastallized() != Turn)):
    #            $ showteraoption = False

    #$ hasdiveral = False
    #if (currentMon != None):
    #    for fvl in currentMon.GetForeverals():
    #        if (lookupforeveraldata(fvl, FVLMacros.FVLType) == ForeveralTypes.FormSwap):
    #            $ hasdiveral = True

    fixed:
        xmaximum 1552
        if contestaction == None:
            hbox:
                xalign 0.5
                yalign 0.5
                imagebutton idle Transform("GUI/contest/performbutton_idle.webp", zoom=0.65) hover Transform("GUI/contest/performbutton_hover.webp", zoom=0.65) action [Hide("ContestUIAbove"), SetVariable("contestaction", "Perform"), SetVariable("contestmove", None), (Function(ContestNotify, "Your points are doubled this round!") if Turn == 5 else NullAction()), (Function(ContestNotify, "Your points are tripled this round!") if Turn == 10 else NullAction()), (Function(ContestNotify, "Spend energy for a big boost, or keep it for a smaller increase!") if coordinator.GetEnergy() > 0 else NullAction()), SetScreenVariable("spentenergy", 0)]
                null width 20
                imagebutton idle Transform("GUI/contest/switchbutton_idle.webp", zoom=0.65) hover Transform("GUI/contest/switchbutton_hover.webp", zoom=0.65) action [Hide("ContestUIAbove"), SetVariable("contestaction", "Switch"), SetVariable("contestmon", None)] hovered Function(ContestNotify, "You can switch without penalty before your first performance!")
        
        # Perform
        elif (contestaction == "Perform"):
            vbox:
                xalign 0.5
                yalign 0.5
                null height 225
                fixed:
                    xmaximum 600
                    ymaximum 67
                    xalign 0.5
                    # Spend energy
                    button:
                        if not spendingenergy:
                            background Transform("GUI/contest/contestmove_idle.webp", zoom=0.65, matrixcolor=TintMatrix(GetDimContestTypeColor(currentMon.GetContestTrait())))
                            idle_background Transform("GUI/contest/contestmove_idle.webp", zoom=0.65, matrixcolor=TintMatrix(GetContestTypeColor(currentMon.GetContestTrait())))
                            hover_background Transform("GUI/contest/contestmove_hover.webp", zoom=0.65, matrixcolor=TintMatrix(GetContestTypeColor(currentMon.GetContestTrait())))
                        else:
                            idle_background Transform("GUI/contest/contestmove_active_idle.webp", zoom=0.65, matrixcolor=TintMatrix(GetContestTypeColor(currentMon.GetContestTrait())))
                            hover_background Transform("GUI/contest/contestmove_active_hover.webp", zoom=0.65, matrixcolor=TintMatrix(GetContestTypeColor(currentMon.GetContestTrait())))
                        sensitive (coordinator.GetEnergy()) action ToggleScreenVariable("spendingenergy") xysize(368, 133) xalign 0.5
                        vbox:
                            align (0.5, 0.5)
                            if not spendingenergy:
                                text "Not spending energy" font "fonts/Delfino.ttf" color ("#fff" if spendingenergy else "#000") size 40 xmaximum 300 textalign 0.5 xalign 0.5
                            else:
                                text "Giving it all!" font "fonts/Delfino.ttf" color ("#fff" if spendingenergy else "#000") size 40 xmaximum 300 textalign 0.5 xalign 0.5
                                text "★"*coordinator.GetEnergy() font "fonts/DejaVuSans.ttf" color ("#fff" if spendingenergy else "#000") size 40 xmaximum 300 textalign 0.5 xalign 0.5
                null height 95
                # Moves
                grid 2 2:
                    spacing 50
                    for move in currentMon.GetMoves():
                        button:
                            if contestmove != move:
                                idle_background Transform("GUI/contest/contestmove_idle.webp", zoom=0.65, matrixcolor=TintMatrix(GetContestTypeColor(move.Contest))) hover_background Transform("GUI/contest/contestmove_hover.webp", zoom=0.65, matrixcolor=TintMatrix(GetContestTypeColor(move.Contest)))
                            else:
                                background Transform("GUI/contest/contestmove_active_idle.webp", zoom=0.65, matrixcolor=TintMatrix(GetContestTypeColor(move.Contest)))
                            action SetVariable("contestmove", move) hovered Show("contestmovedata", move = move) unhovered (Show("contestmovedata", move = contestmove) if contestmove != None else Hide("contestmovedata"))
                            xysize(368, 133)
                            text move.Name font "fonts/Delfino.ttf" color ("#000" if contestmove != move else "#fff") align(0.5, 0.5) size 55 xmaximum 300
                null height 70
                if contestmove != None:
                    imagebutton idle Transform("GUI/contest/confirmperformbutton_idle.webp", zoom=0.65) hover Transform("GUI/contest/confirmperformbutton_hover.webp", zoom=0.65) action [Hide("contestmovedata", dissolve), Return((1, contestmove, startingmon != currentMon, spendingenergy*coordinator.GetEnergy()))] xalign 0.5
                else:
                    null height 133
                
            # Pokédex shortcut
            button:
                idle_background Transform("GUI/contest/pokemondata_switchmon_idle.webp", zoom=0.66, matrixcolor=TintMatrix(GetContestTypeColor(currentMon.GetContestTrait()))) hover_background Transform("GUI/contest/pokemondata_switchmon_hover.webp", zoom=0.66, matrixcolor=TintMatrix(GetContestTypeColor(currentMon.GetContestTrait()))) xysize(158, 135)
                action Show("pokedexdata", dexid=None, formid=currentMon.GetId(), outOfContextDex=True)
                xalign 0.01 yalign 0.99
                add currentMon.GetImage() zoom 0.2 yalign (0.35 if mon.GetId() != 25.2 else 0.32) xalign 0.5
        
        # Switching
        elif (contestaction == "Switch"):
            # Before selecting Pokémon
            if contestmon == None:
                vbox:
                    xalign 0.5
                    yalign 0.5
                    $ rows = math.ceil(len(coordinator.GetTeam()) / 3)
                    grid 3 rows:
                        spacing 50
                        for mon in coordinator.GetTeam():
                            button:
                                idle_background Transform("GUI/contest/contestmove_idle.webp", zoom=0.65, matrixcolor=TintMatrix(GetContestTypeColor(mon.GetContestTrait()))) hover_background Transform("GUI/contest/contestmove_hover.webp", zoom=0.65, matrixcolor=TintMatrix(GetContestTypeColor(mon.GetContestTrait()))) xysize(368, 133) action SetVariable("contestmon", mon)
                                hbox:
                                    xalign 0.5
                                    yalign 0.5
                                    add mon.GetImage() zoom 0.1 yalign 0.55
                                    null width 20
                                    text mon.GetNickname() font "fonts/Delfino.ttf" color "#000" size 55 xmaximum 300
            
            # After selecting Pokémon
            else:
                add "GUI/contest/pokemondata_switchscreen.webp" align(0.5, 0.1)
                hbox:
                    xalign 0.5
                    yalign 0.06
                    add contestmon.GetImage() zoom 0.2 yalign (0.35 if mon.GetId() != 25.2 else 0.32)
                    null width 20
                    text contestmon.GetNickname() font "fonts/Delfino.ttf" color "#000" size 80 xmaximum 300
                add ("GUI/contest/contestcategory_" + contestmon.GetContestTrait().lower() + ".webp") xalign 0.5 yalign 0.22
                grid 2 2:
                    xalign 0.5
                    yalign 0.545
                    xmaximum 1040
                    ymaximum 430
                    spacing 70
                    for move in contestmon.GetMoves():
                        button:
                            idle_background Transform("GUI/contest/pokemondata_move.webp", matrixcolor=TintMatrix(GetContestTypeColor(move.Contest)))
                            hover_background Transform("GUI/contest/pokemondata_move.webp", matrixcolor=TintMatrix(GetBrightContestTypeColor(move.Contest))) xysize(416, 161)
                            action NullAction() hovered Show("contestmovedata", move = move) unhovered Hide("contestmovedata")
                            text move.Name font "fonts/Delfino.ttf" color ("#000" if contestmove != move else "#fff") align(0.5, 0.5) size 55 xmaximum 300 textalign 0.5
                if contestmon != currentMon:
                    imagebutton idle Transform("GUI/contest/confirmswitchbutton_idle.webp", zoom=0.65) hover Transform("GUI/contest/confirmswitchbutton_hover.webp", zoom=0.65) action [Function(coordinator.ResetEnergy), Function(coordinator.Reorder, contestmon), Function(renpy.invoke_in_new_context, renpy.say, None, "You switched your Pokémon to {}{}!".format(contestmon.GetNickname(), (", but lost all your accumulated energy" if coord.GetEnergy() > 0 else ""))), SetVariable("contestaction", None), SetVariable("contestmon", None)] xalign 0.5 ypos 0.8

                # Side buttons to easily switch
                $ partyindex = coordinator.GetTeam().index(contestmon)
                if partyindex - 1 >= 0:
                    $ prevmon = coordinator.GetTeam()[partyindex - 1]
                    button:
                        idle_background Transform("GUI/contest/pokemondata_switchmon_idle.webp", zoom=0.66, matrixcolor=TintMatrix(GetContestTypeColor(prevmon.GetContestTrait()))) hover_background Transform("GUI/contest/pokemondata_switchmon_hover.webp", zoom=0.66, matrixcolor=TintMatrix(GetContestTypeColor(prevmon.GetContestTrait()))) action SetVariable("contestmon", prevmon) xysize(158, 135)
                        yalign 0.5
                        xalign 0.025
                        add prevmon.GetImage() zoom 0.2 yalign (0.35 if mon.GetId() != 25.2 else 0.32) xalign 0.5
                        keysym "mousedown_4"
                if partyindex + 1 <= len(coordinator.GetTeam()) - 1:
                    $ nextmon = coordinator.GetTeam()[partyindex + 1]
                    button:
                        idle_background Transform("GUI/contest/pokemondata_switchmon_idle.webp", zoom=0.66, matrixcolor=TintMatrix(GetContestTypeColor(nextmon.GetContestTrait()))) hover_background Transform("GUI/contest/pokemondata_switchmon_hover.webp", zoom=0.66, matrixcolor=TintMatrix(GetContestTypeColor(nextmon.GetContestTrait()))) action SetVariable("contestmon", nextmon) xysize(158, 135)
                        yalign 0.5
                        xalign 0.975
                        add nextmon.GetImage() zoom 0.2 yalign (0.35 if mon.GetId() != 25.2 else 0.32) xalign 0.5
                        keysym "mousedown_5"
                
    if contestaction != None:
        imagebutton idle Transform("GUI/contest/backbutton_idle.webp", zoom=0.65) hover Transform("GUI/contest/backbutton_hover.webp", zoom=0.65) action ([SetVariable("contestaction", None), SetVariable("contestmove", None), Hide("contestmovedata"), Show("ContestUIAbove", dissolve)] if contestmon == None else SetVariable("contestmon", None)) xalign 0.78 yalign 0.99

screen ContestHelp():
    modal True

    vbox:
        align (0.5, 0.5)
        frame:
            # pokémon list
            background "pokedex_background"
            xsize 1500
            ysize 700
            padding (20, 20)

            viewport id "contesthelpport":
                draggable True
                mousewheel True
                scrollbars "vertical"

                vbox:
                    spacing 50
                    $ beautiful = "{color=" + GetContestTypeColor("Beautiful") + "}Beautiful" + "{/color}"
                    $ cute = "{color=" + GetContestTypeColor("Cute") + "}Cute" + "{/color}"
                    $ tough = "{color=" + GetContestTypeColor("Tough") + "}Tough" + "{/color}"
                    $ clever = "{color=" + GetContestTypeColor("Clever") + "}Clever" + "{/color}"
                    $ cool = "{color=" + GetContestTypeColor("Cool") + "}Cool" + "{/color}"
                    text "{b}Condition{/b}: At the beginning of each Contest, the Coordinator-Pokémon pair that is in the best visual condition will earn 50 points, with runners-up winning linearly fewer. This is tied to [contestcolor]Coordinating Knowledge.{/color}" color "#000"
                    text "{b}Popularity{/b}: Every turn, a Coordinator-Pokémon pair can earn one, three, or five points depending on the popularity of the Pokémon. This popularity is based on whether the Pokémon has one of three types, whether the Pokémon is from a specific region, and whether the Pokémon has a certain Contest Trait. But beware! A Pokémon that meets {i}none{/i} of those conditions can cause you to {i}lose{/i} points, instead! ([pika_name] will always be considered an Electric-type from Unova, with the {b}[cool]{/b} contest type.)" color "#000"
                    text "{b}Contest Move Types{/b}: The five kinds of Contest Move Types are [cute], [clever], [cool], [beautiful], and [tough]. Every move falls into one of these categories." color "#000"
                    text "{b}Appealing Moves{/b}: If you use a move with a Contest Move Type a Judge wants to see, they will award you an extra point, and they will become more excited." color "#000"
                    text "{b}Jackpots{/b}: If a move makes a Judge as excited as they can possibly be, they will award the user of the move a bonus 13 points! They will then start looking for something else--and be permanently easier to excite." color "#000"
                    text "{b}Energy{/b}: Using a move that is the same type as the Coordinator performing grants a Coordinator 'Energy'. Every point of Energy a Coordinator has increases the value of their appeals. When the moment feels appropriate, you can spend all your energy for a big score boost. However, switching out your Pokémon will cause you to lose that energy, and make you unable to gain any on that turn!" color "#000"
                    text "{b}Jamming Moves{/b}: Some moves are capable of 'jamming' a competitor who moved prior, or moves after. If jammed, they will lose a third of their points (min 1), and lose all their energy." color "#000"
                    text "{b}Special Rounds{/b}: On round five, after all points are tallied up, including points from energy and jamming, your score for the round is doubled. On round ten, your score for the round is tripled. Make sure to make those rounds count!" color "#000"

        textbutton "Back to the show!" action Hide("ContestHelp") padding (30, 10) xminimum 200 text_xalign .5 xalign 0.5 text_size 60 text_color "#000" text_hover_color "#f0f" style "menu_choice_button" text_font "fonts/pkmndp.ttf"