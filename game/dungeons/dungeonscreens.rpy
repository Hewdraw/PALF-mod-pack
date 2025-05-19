screen dungeonpartyviewer(dungeon):
    zorder -1
    if (not inbattle):
        python:
            trainers = dungeon.GetTrainers()
            num_trainers = len(trainers)
            positions = [(i + 1) / (num_trainers + 1) for i in range(num_trainers)]

        for i in range(num_trainers):
            python:
                trainer = trainers[i]
                setxpos = positions[i]
                firstmon = trainer.GetUnfaintedTeam()[0]
                charcolor = GetCharColor(trainer.GetName())
                status = firstmon.GetNormalStatus()
                status = status.title() if status else "No Status"
                ppercentage = 0
                actualpp = 0
                maxpp = 0

                for move in firstmon.GetMoves():
                    actualpp += move.PP
                    maxpp += move.MaxPP

                ppercentage = str(round(actualpp / maxpp * 100)) + "%"
            
            add firstmon.GetImage() xanchor 0.5 yanchor 1.0 pos (setxpos - 0.06, 1.01) zoom 0.3 matrixcolor TintMatrix(charcolor) * BrightnessMatrix(1.0) * ContrastMatrix(0.0)
            add (GetChibi(trainer.GetName()) if not inbattle else firstmon.GetImage()) xanchor 0.5 yanchor 1.0 pos (setxpos, 0.9) zoom 0.4
            add "gui/PaperFrame.png" xanchor 0.5 yanchor 1.0 pos (setxpos, 1.0)
            add (firstmon.GetImage() if not inbattle else GetChibi(trainer.GetName())) xanchor 0.5 yanchor 1.0 pos (setxpos - 0.06, 1.0) zoom 0.25
            
            text status xalign 0.5 yanchor 1.0 pos (setxpos, 0.945) color "#fff" font "fonts/AncientModernTales.ttf" outlines [(absolute(1), "#000000", absolute(1), absolute(1))]
            text "PP: " + str(ppercentage) xalign 0.5 yanchor 1.0 pos (setxpos, 0.99) color "#fff" font "fonts/AncientModernTales.ttf" outlines [(absolute(1), "#000000", absolute(1), absolute(1))]
            #text ppercentage xalign 0.5 yanchor 1.0 pos (setxpos + 0.04, 0.99) color "#fff" font "fonts/AncientModernTales.ttf" outlines [(absolute(1), "#000000", absolute(1), absolute(1))]

            python:
                health = firstmon.GetHealth()
                maxhealth = firstmon.GetStat(Stats.Health)
                gendersymbol = ""
                if (firstmon.GetGender(affectedByIllusion = True) == Genders.Male):
                    gendersymbol = "{color=#2b00ff}{font=fonts/pkmndp.ttf}♂{/font}"
                elif (firstmon.GetGender(affectedByIllusion = True) == Genders.Female):
                    gendersymbol = "{color=#ff00b7}{font=fonts/pkmndp.ttf}♀{/font}"
                hueshift = 0
                if (health / maxhealth <= 0.25):
                    hueshift = 240
                elif (health / maxhealth <= 0.5):
                    hueshift = 300

            hbox:
                xalign 0.5
                pos (setxpos, 0.825)
                if (not inbattle):
                    for pkmn in trainer.GetTeam():
                        add "GUI/pixelpokeball_indicator.webp" matrixcolor SaturationMatrix(pkmn.GetHealth() > 0) xalign 0.5 ypos 1.0


        add "gui/dungeontextbox.png" xalign 0.5 yanchor 0.24 zoom 0.6

        add MultiBar(2, (960, 50), (0, 0), [ Color("#800"), Color("#008") , Color("#080") ], [Color("#000"), Color("#000")], bar_range = (dungeon.GetFerocity()+dungeon.GetMysteriosity()+dungeon.GetGenerosity()), start_values = [dungeon.GetFerocity(), dungeon.GetMysteriosity(), dungeon.GetGenerosity()], sensitive=False) xalign 0.5
        text "Mysteriosity Saturation - " + dungeon.GetEventChance() ypos 57 xalign 0.5 color "#fff" font "fonts/AncientModernTales.ttf" outlines [(absolute(1), "#000000", absolute(1), absolute(1))]
        
        hbox:
            xalign 0.5
            ypos 0.1
            for i in range(1, dungeon.GetFloors() + 1):
                if (dungeon.GetCurrentFloor() >= i):
                    add "gui/Gem.png"
                else:
                    add "gui/GemUnlit.png"

screen dungeonbattlefieldstatus(dungeon):
    zorder 1
    modal True

    imagebutton idle Null() xysize (1920, 1080) action Hide("dungeonbattlefieldstatus")

    add "BG/Blank2.webp" alpha 0.6
    add "gui/dungeonscroll1.png" align (0.5, 0.5)
    vbox:
        align (0.5, 0.5)
        if (inbattle):
            text "{color=#FFD700}{font=fonts/DejaVuSans.ttf}♣{/font}{/color} Progress {color=#FFD700}{font=fonts/DejaVuSans.ttf}♣{/font}{/color}" xalign 0.5 font "fonts/AncientModernTales.ttf" color "#fff" outlines [(absolute(1), "#000000", absolute(1), absolute(1))]
            text "You have explored " + str(dungeon.GetProgress()) + " " + cp(dungeon.GetProgress(), "room") + " on this floor." xalign 0.5 font "fonts/AncientModernTales.ttf" color "#fff" outlines [(absolute(1), "#000000", absolute(1), absolute(1))]
            null height 40
        text "{color=#008}{font=fonts/DejaVuSans.ttf}♦{/font}{/color} Mysteriosity {color=#008}{font=fonts/DejaVuSans.ttf}♦{/font}{/color}" xalign 0.5 font "fonts/AncientModernTales.ttf" color "#fff" outlines [(absolute(1), "#000000", absolute(1), absolute(1))]
        text dungeon.GetEventChance() + " chance of a Mysterious Flux after an ally's turn." xalign 0.5 font "fonts/AncientModernTales.ttf" color "#fff" outlines [(absolute(1), "#000000", absolute(1), absolute(1))]
        null height 40
        text "{color=#080}{font=fonts/DejaVuSans.ttf}♥{/font}{/color} Generosity {color=#080}{font=fonts/DejaVuSans.ttf}♥{/font}{/color}" xalign 0.5 font "fonts/AncientModernTales.ttf" color "#fff" outlines [(absolute(1), "#000000", absolute(1), absolute(1))] 
        text str(dungeon.GoodOdds()) + "% chance that Mysterious Fluxes will turn out well." xalign 0.5 font "fonts/AncientModernTales.ttf" color "#fff" outlines [(absolute(1), "#000000", absolute(1), absolute(1))]
        null height 40
        text "{color=#800}{font=fonts/DejaVuSans.ttf}♠{/font}{/color} Ferocity {color=#800}{font=fonts/DejaVuSans.ttf}♠{/font}{/color}" xalign 0.5 font "fonts/AncientModernTales.ttf" color "#fff" outlines [(absolute(1), "#000000", absolute(1), absolute(1))] 
        text str(dungeon.BadOdds()) + "% chance that Mysterious Fluxes will turn out poorly." xalign 0.5 font "fonts/AncientModernTales.ttf" color "#fff" outlines [(absolute(1), "#000000", absolute(1), absolute(1))]
        if (inbattle):
            if (len(BattlefieldEffects) > 0 or CurrentWeather != None):
                null height 40
                text "~ Effects on the Entire Battlefield ~" xalign 0.5 font "fonts/AncientModernTales.ttf" color "#fff" outlines [(absolute(1), "#000000", absolute(1), absolute(1))]
                if (CurrentWeather != None):
                    text CurrentWeather[0].title() xalign 0.5 font "fonts/AncientModernTales.ttf" color "#fff" outlines [(absolute(1), "#000000", absolute(1), absolute(1))]
                for effect in BattlefieldEffects:
                    text effect.title() xalign 0.5 font "fonts/AncientModernTales.ttf" color "#fff" outlines [(absolute(1), "#000000", absolute(1), absolute(1))]
            if (len(FriendlyEffects) > 0):
                null height 40
                text "~ Effects on all Allies ~" xalign 0.5 font "fonts/AncientModernTales.ttf" color "#fff" outlines [(absolute(1), "#000000", absolute(1), absolute(1))] 
                for effect in FriendlyEffects:
                    text effect.title() xalign 0.5 font "fonts/AncientModernTales.ttf" color "#fff" outlines [(absolute(1), "#000000", absolute(1), absolute(1))]
            if (len(EnemyEffects) > 0):
                null height 40
                text "~ Effects on all Foes ~" xalign 0.5 font "fonts/AncientModernTales.ttf" color "#fff" outlines [(absolute(1), "#000000", absolute(1), absolute(1))] 
                for effect in EnemyEffects:
                    text effect.title() xalign 0.5 font "fonts/AncientModernTales.ttf" color "#fff" outlines [(absolute(1), "#000000", absolute(1), absolute(1))]

screen dungeonbattleui(dungeon):
    python:
        numfoes = len(EnemyBattlers())
        numallies = len(FriendlyBattlers())
            
    for i, enemymon in enumerate(EnemyBattlers()):
            #FIX THIS: ADDRESS THIS: Make Tyrannic Pokémon have health bars that cover the entire top of the screen
            python:
                ylevels = 0
                xbase = ((i * 2 + 1) / (numfoes * 2))
                zoombase = (0.75 if numfoes > 4 else 1.0)
                trainer = enemymon.GetTrainer()
                reinforcementlist = list(trainer.GetUnfaintedTeam())
                if (enemymon in reinforcementlist):
                    reinforcementlist.remove(enemymon)
                maxyoffset = enemymon.IsTerad() + len(enemymon.GetVisibleStatusKeys()) + len(enemymon.GetAllStatChanges()) + (len(reinforcementlist) > 0)
    
            add enemymon.GetImage() xcenter xbase ypos 0.5 yanchor 1.0 zoom zoombase xzoom (1 if (i + 1) > numfoes / 2.0 else -1) 
            
            hbox:
                xcenter xbase ypos 0.65 yanchor 1.0 spacing -40
                for j, mon in enumerate(reinforcementlist[:3]):
                    add mon.GetImage() yanchor (0.8 if len(reinforcementlist[:3]) % 2 == 0 or j % 2 == 0 else 0.5) zoom zoombase * 0.5 xzoom (1 if (i + 1) > numfoes / 2.0 else -1) matrixcolor TintMatrix("#00000088")
    
            if (maxyoffset > 0):
                add "gui/dungeonscroll1.png" zoom 0.35 xcenter xbase ypos 140 + 30 * maxyoffset yanchor 1.0
    
            imagebutton:
                xanchor 0.5 xpos xbase
                idle Transform("gui/LongPaperFrame.png", matrixcolor=InvertMatrix(0), zoom=0.75)
                hover Transform("gui/LongPaperFrame.png", matrixcolor=InvertMatrix(), zoom=0.75)
                if uifuckery < 1:
                    action ([Show("pokedexdata", dexid = None, formid = enemymon.GetId() if enemymon.Id != 25.2 else 25.2, outOfContextDex = True)] if enemymon.Id not in unknownmons else NullAction())
    
            if (maxyoffset > 0):
                if (enemymon.IsTerad()):
                    text "{gradient2=3-#f00-#0f0-11-#0f0-#00f-11-#00f-#f00-11}Terastallized {/gradient2}" + enemymon.GetTeraType() xcenter xbase ypos 90 + 30 * ylevels font "fonts/DungeonFont.ttf"
                    $ ylevels += 1
    
                if (len(reinforcementlist)):
                    text "Reinforced x" + str(len(reinforcementlist)) xcenter xbase ypos 90 + 30 * ylevels font "fonts/DungeonFont.ttf"
                    $ ylevels += 1
    
                for status in enemymon.GetStatusKeys():
                    if (status[0] != ".") and (status != "illusion"):
                        if (status in ["diveralized", "mega evolved", "minigigamaxed"]):
                            text "{gradient2=3-#f00-#0f0-11-#0f0-#00f-11-#00f-#f00-11}" + status.title() + "{/gradient2}" xcenter xbase ypos 90 + 30 * ylevels font "fonts/DungeonFont.ttf"
                        else:
                            text status.title() xcenter xbase ypos 90 + 30 * ylevels font "fonts/DungeonFont.ttf"
                        $ ylevels += 1
    
                for change in enemymon.GetAllStatChanges().keys():
                    text StatToString(change) + ("+" if enemymon.GetStatChanges(change) > 0 else "" ) + str(enemymon.GetStatChanges(change)) xcenter xbase ypos 90 + 30 * ylevels font "fonts/DungeonFont.ttf"
                    $ ylevels += 1
            
            python:
                health = enemymon.GetHealth()
                maxhealth = enemymon.GetStat(Stats.Health)
                gendersymbol = ""
                if (enemymon.GetGender(affectedByIllusion = True) == Genders.Male):
                    gendersymbol = "{color=#2b00ff}{font=fonts/pkmndp.ttf}♂{/font}"
                elif (enemymon.GetGender(affectedByIllusion = True) == Genders.Female):
                    gendersymbol = "{color=#ff00b7}{font=fonts/pkmndp.ttf}♀{/font}"
                hueshift = 0
                if (health / maxhealth <= 0.25):
                    hueshift = 240
                elif (health / maxhealth <= 0.5):
                    hueshift = 300
    
            vbox:
                xcenter xbase ypos 0.01
                hbox:
                    spacing 20 xalign 0.5
                    text enemymon.GetNickname() font "fonts/AncientModernTales.ttf" color "#fff" outlines [(absolute(1), "#000000", absolute(1), absolute(1))]
                    text gendersymbol + "{color=#000000}Lv." + str(enemymon.GetLevel()) font "fonts/AncientModernTales.ttf"
    
                bar range maxhealth value health xmaximum 250 ymaximum 10 right_bar Frame("GUI/bar_empty.webp", 0, 0) left_bar Frame("GUI/bar_full.webp", 0, 0) xalign 0.5 at Transform(yzoom=0.5, matrixcolor=HueMatrix(hueshift))
                #FIX THIS: ADDRESS THIS: Add another bar over the previous one indicating how much damage you can actually do in one instance of damage, for tyrannic pokemon

    for i, allymon in enumerate(FriendlyBattlers()):
            python:
                ylevels = 0
                xbase = ((i * 2 + 1) / (numallies * 2))
                zoombase = (0.75 if numallies > 4 else 1.0)
                trainer = allymon.GetTrainer()
                charcolor = GetCharColor(trainer.GetFormatName())
                maxyoffset = allymon.IsTerad() + len(allymon.GetVisibleStatusKeys()) + len(allymon.GetAllStatChanges())
                originali = i
    
            add allymon.GetImage() at (hovering if originali == BattlerIndex and len(FriendlyBattlers()) > 1 else None) yanchor 0.96 ypos 1040 - (80 if maxyoffset > 0 else 0) - 30 * maxyoffset zoom 0.55 xcenter xbase xzoom (1 if (i + 1) > numallies / 2.0 else -1) matrixcolor TintMatrix(charcolor) * BrightnessMatrix(1.0) * ContrastMatrix(0.0)
            add allymon.GetImage() at (hovering if originali == BattlerIndex and len(FriendlyBattlers()) > 1 else None) yanchor 0.95 ypos 1040 - (80 if maxyoffset > 0 else 0) - 30 * maxyoffset zoom 0.5 xcenter xbase xzoom (1 if (i + 1) > numallies / 2.0 else -1)
            
            if (maxyoffset > 0):
                add "gui/dungeonscroll1.png" zoom 0.35 xcenter xbase ypos 1080 - 140 - 30 * maxyoffset
            
            imagebutton:
                yalign 1.0 
                xcenter xbase
                idle Transform("gui/LongPaperFrame.png", matrixcolor=InvertMatrix(0), zoom=0.75)
                hover Transform("gui/LongPaperFrame.png", matrixcolor=InvertMatrix(), zoom=0.75)
                hovered [Show("mondata", None, allymon, False, False), Show("nonbattlemoves", None, allymon)]
                unhovered [Hide("mondata"), Hide("nonbattlemoves"), Hide("movedata")]
                if uifuckery < 1:
                    action ([Show("pokedexdata", dexid = None, formid = allymon.GetId() if allymon.Id != 25.2 else 25.2, outOfContextDex = True)] if allymon.Id not in unknownmons else NullAction())
    
            python:
                reinforcementstring = "{font=fonts/icons.ttf}{size=45}{color=#00f}s{/color}{/size}{/font} " + str(len(trainer.GetUnfaintedTeam())) + "/" + str(len(trainer.GetTeam()))
    
            text reinforcementstring yanchor 1.0 xcenter xbase ypos 995 - (50 if maxyoffset > 0 else 0) - 30 * maxyoffset color "#fff" font "fonts/AncientModernTales.ttf" outlines [(absolute(1), "#000000", absolute(1), absolute(1))]
    
            if (maxyoffset > 0):
                if (allymon.IsTerad()):
                    text "{gradient2=3-#f00-#0f0-11-#0f0-#00f-11-#00f-#f00-11}Terastallized {/gradient2}" + allymon.GetTeraType() xcenter xbase ypos 1080 - 120 - 30 * ylevels font "fonts/DungeonFont.ttf"
                    $ ylevels += 1
    
                for status in allymon.GetStatusKeys():
                    if (status[0] != ".") and (status != "illusion"):
                        if (status in ["diveralized", "mega evolved", "minigigamaxed"]):
                            text "{gradient2=3-#f00-#0f0-11-#0f0-#00f-11-#00f-#f00-11}" + status.title() + "{/gradient2}" xcenter xbase ypos 1080 - 120 - 30 * ylevels font "fonts/DungeonFont.ttf"
                        else:
                            text status.title() xcenter xbase ypos 1080 - 120 - 30 * ylevels font "fonts/DungeonFont.ttf"
                        $ ylevels += 1
    
                for change in allymon.GetAllStatChanges().keys():
                    text StatToString(change) + ("+" if allymon.GetStatChanges(change) > 0 else "" ) + str(allymon.GetStatChanges(change)) xcenter xbase ypos 1080 - 120 - 30 * ylevels font "fonts/DungeonFont.ttf"
                    $ ylevels += 1
            
            
            python:
                health = allymon.GetHealth()
                maxhealth = allymon.GetStat(Stats.Health)
                gendersymbol = ""
                if (allymon.GetGender(affectedByIllusion = True) == Genders.Male):
                    gendersymbol = "{color=#2b00ff}{font=fonts/pkmndp.ttf}♂{/font}"
                elif (allymon.GetGender(affectedByIllusion = True) == Genders.Female):
                    gendersymbol = "{color=#ff00b7}{font=fonts/pkmndp.ttf}♀{/font}"
                hueshift = 0
                if (health / maxhealth <= 0.25):
                    hueshift = 240
                elif (health / maxhealth <= 0.5):
                    hueshift = 300
    
            vbox:
                xcenter xbase ypos 0.99 yanchor 1.0
                hbox:
                    spacing 20 xalign 0.5
                    text allymon.GetNickname() font "fonts/AncientModernTales.ttf" color "#fff" outlines [(absolute(1), "#000000", absolute(1), absolute(1))]
                    text gendersymbol + "{color=#000000}Lv." + str(allymon.GetLevel()) font "fonts/AncientModernTales.ttf"
    
                bar range maxhealth value health xmaximum 250 ymaximum 10 right_bar Frame("GUI/bar_empty.webp", 0, 0) left_bar Frame("GUI/bar_full.webp", 0, 0) xalign 0.5 at Transform(yzoom=0.5, matrixcolor=HueMatrix(hueshift))

screen DungeonHelp():
    modal True

    vbox:
        align (0.5, 0.5)
        frame:
            # pokémon list
            background "pokedex_background"
            xsize 1500
            ysize 700
            padding (20, 20)

            viewport id "dungeonhelpport":
                draggable True
                mousewheel True
                scrollbars "vertical"

                vbox:
                    spacing 50
                    text "{b}{color=#008}Mysteriosity{/color}{/b}: A basic measure of how unstable the dungeon is becoming. The longer you stay in the dungeon, the more random and impactful the events that can occur will be. It goes up a small amount every turn." color "#000"
                    text "{b}{color=#800}Ferocity{/color}{/b}: A measure of how dangerous the dungeon is getting. The more enemy Pokémon you battle, the higher this will become, providing random buffs to opponents, and debuffs to you. It goes up by a small amount every time you knock out an opponent, but halves every time you go up a floor." color "#000"
                    text "{b}{color=#080}Generosity{/color}{/b}: A measure of how safe the dungeon is. The higher it is, the more likely positive events will occur for you--including loot, bond gains, and battle buffs. It goes up by a small amount every time you go up a floor, or a Ferocity event triggers." color "#000"
                    text "{b}Loot{/b}: Knocking out enemy Pokémon will cause them to drop items you can pick up automatically. Items can also be gotten from Mysterious Fluxes. Be careful, though! Don't get greedy--a dungeon with high Ferocity isn't worth the loot." color "#000"
                    text "{b}Stairs{/b}: As you battle through dungeons, you'll eventually encounter the stairs, possibly through a Mysterious Flux, or possibly just from exploring enough. When you see the stairs, take them to leave the battle!" color "#000"
                    text "{b}Reinforcements{/b}: Enemy Pokémon can team up against you, up to six on a side. If the opposing side is already full of Pokémon, though, Pokémon can start to become 'Reinforced'. Reinforced Pokémon get a boost to their stats, and are replaced immediately when knocked out." color "#000"
                    text "{b}Tyrannic Pokémon{/b}: Tyrannic Pokémon usually show up as the bosses of dungeons. Their reinforcements prevent you from doing more than a percentage of their health in a single hit. However, hitting them super-effectively will chip away at their reinforcements. Most Tyrannic Pokémon will block you from the stairs, so you just have to beat them to progress!" color "#000"
                    
        textbutton "Back to the dungeon!" action Hide("DungeonHelp") padding (30, 10) xminimum 200 text_xalign .5 xalign 0.5 text_size 60 text_color "#000" text_hover_color "#f0f" style "menu_choice_button" text_font "fonts/pkmndp.ttf"