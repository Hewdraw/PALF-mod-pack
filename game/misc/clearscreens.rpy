label clearscreens:
    call clearcontestscreens() from _call_clearcontestscreens

    hide screen dungeonbattleui
    hide screen dungeonpartyviewer
    hide screen dungeonbattlefieldstatus
    hide screen DungeonHelp
    hide screen currentdate
    hide screen movedata
    hide screen mondata
    hide screen nonbattlemoves
    hide screen fieldinventory
    hide screen partyviewerpopup
    scene onlayer arrowlayer
    scene onlayer undermaster
    with dis
return

label silence:
    stop music fadeout 1.5
    stop music fadeout 1.5 channel "crowd"
    stop music fadeout 1.5 channel "crowd2"
    stop music fadeout 1.5 channel "crowd3"
    stop music fadeout 1.5 channel "misc"
    stop music fadeout 1.5 channel "ctc"
    stop music fadeout 1.5 channel "altcry"
    stop music fadeout 1.5 channel "XYgame"
    stop music fadeout 1.5 channel "points"
return