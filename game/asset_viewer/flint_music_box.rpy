
screen music_box_menu():
    add "gui/bg_tiles/bg_tile_none_full.webp"

    add "BG/Blank.webp" pos (.03, 0.015) crop (0.05, 0.015, .185, .1)
    text "{color=#000}{b}{size=60}Music Box{/b}{/color}" pos (0.05, 0.015)
    
    viewport id "test":
            
        align (0.5, 0.0)
        area(35,75,1880,910)
        scrollbars "vertical"
        arrowkeys True
        pagekeys True
        mousewheel True
        vscrollbar_base_bar "#fff"
        vscrollbar_thumb "#363436"
        vscrollbar_top_bar "#e7e6e7"
        vscrollbar_bottom_bar "#e7e6e7"


        vpgrid:

            cols 4
            spacing 15

            $ music_options = [("Tia Theme", ("TiaTheme_start.ogg", "TiaTheme_loop.ogg")), ("The Very Best", ("TheVeryBest_start.ogg", "TheVeryBest_loop.ogg")),("Don't Ever Forget", ("DontEverForget_start.ogg", "DontEverForget_loop.ogg")),("Lavender Theme", ("lavender_start.ogg", "lavender_loop.ogg")),
            ("Nuvema", ("Nuvema2_Start.ogg", "Nuvema2_Loop.ogg")),("Kanto Gym", ("KantoGym_Start.ogg", "KantoGym_Loop.ogg")),("Rival (Blue)", ("RivalChill_start.ogg", "RivalChill_loop.ogg")),("Drought", "drought.ogg"),
            ("Hoenn Rival", ("HoennRivalStart_Rock.ogg","HoennRivalLoop_Rock.ogg")),("Legendary (Altaria)", "legendary.ogg"),("Mansion", ("mansion_start.ogg","mansion_loop.ogg")),("Relic Song", "relicsong.ogg"),
            ("Runaway, Fugitives", ("runawayfugitives_start.ogg","runawayfugitives_loop.ogg")),("Soaring Dreams", ("SoaringDreams_Start.ogg","SoaringDreams_Loop.ogg")),("Sword/Shield Gym", ("SwordShieldGym-Intro.ogg","SwordShieldGym-Loop.ogg")),
            ("Mistralton City", "MistraltonCity.ogg"),("Blue (Champion)", ("bigbluebattle_start.ogg", "bigbluebattle_loop.ogg")),("Deoxys", ("deoxys_start.ogg","deoxys_loop.ogg")),
            ("Sinis Trio (Nate)", ("natetheme_start.ogg","natetheme_loop.ogg")),("Olivine City", ("olivine_start.ogg","olivine_loop.ogg")),("Sonia's theme", ("sonia_start.ogg","sonia_loop.ogg")),
            ("BW Pokémon", ("BW_Pokemon_Start.ogg", "BW_Pokemon_Loop.ogg")), ("Celebi", ("celebi_start.ogg", "celebi_loop.ogg")),
            ("Klara's theme", ("everyonesfavoritegirl_start.ogg", "everyonesfavoritegirl_loop.ogg")), ("Join Avenue", ("joinavenue_start.ogg", "joinavenue_loop.ogg")),
            ("Trainer Encounter", ("TrainerEncounter_Start.ogg", "TrainerEncounter_Loop.ogg")), ("Unova Trainer (Rock)", ("UnovaTrainerStart_Rock.ogg", "UnovaTrainerLoop_Rock.ogg")),
            ("Victory Road", ("victory_start.ogg", "victory_loop.ogg")), ("Alolan Encounter", ("alolaencounter_intro.ogg", "alolaencounter_loop.ogg")),
            ("Anabel", ("anabel_start.ogg", "anabel_loop.ogg")), ("Celadon", ("Celadon_Start.ogg", "Celadon_Loop.ogg")),
            ("Dragon Den", ("DragonDenStart_B.ogg", "DragonDenLoop.ogg")), ("Embracing One's Duty", "embracingonesduty.ogg"),
            ("Field Theme", ("Fieldstheme_Start.ogg", "Fieldstheme_Loop.ogg")),("Goldenrod City", ("goldenrod_start.ogg", "goldenrod_loop.ogg")),
            ("Beyond", "Beyond.ogg"), ("Brand New World", "brandnewworld.ogg"), ("Chillstar", ("chillstar_start.ogg", "chillstar_loop.ogg")),
            ("Eterna", ("Eterna_Start.ogg", "Eterna_Loop.ogg")), ("Fuschia", ("fuchsia_start.ogg", "fuchsia_loop.ogg")),
            ("Game Corner", ("gamecorner_start.ogg", "gamecorner_loop.ogg")), ("G/S Bike", ("GSCBike_Start.ogg","GSCBike_Loop.ogg")),
            ("Imminence", ("imminence_start.ogg", "imminence_loop.ogg")), ("Littleroot", ("Littleroot_Start.ogg", "Littleroot_Loop.ogg")),
            ("LoFi Max Raid", ("LoFiMaxRaidBattle_start.ogg", "LoFiMaxRaidBattle_loop.ogg")), ("Mt. Pyre", ("MtPyre_start.ogg", "MtPyre_loop.ogg")),
            ("Oak Theme", ("OakTheme_Start.ogg", "OakTheme_Loop.ogg")), ("Ocean Waltz", ("Ocean Waltz_Start.ogg", "Ocean Waltz_Loop.ogg")),
            ("Pewter", ("Pewter_start.ogg", "Pewter_loop.ogg")), ("Power Plant", ("Power Plant_start.ogg", "Power Plant_loop.ogg")),
            ("RBY Wild Pokémon", ("RBY_Pokemon_Start.ogg", "RBY_Pokemon_Loop.ogg")), ("Route 1 (Anime)", "Route 1 Anime.ogg"),
            ("Hoenn Rival", ("RSE_Rival_Start.ogg", "RSE_Rival_Loop.ogg")), ("Seaport", ("seaport_start.ogg", "seaport_loop.ogg")),
            ("Silph Co.", ("silphco_intro.ogg", "silphco_loop.ogg")), ("Stow on Side", ("StowOnSide_start.ogg", "StowOnSide_loop.ogg")),
            ("Tension", ("tension_start.ogg", "tension_loop.ogg")), ("Pokémon Theme", ("theme_start.ogg", "theme_loop.ogg")),
            ("Vaniville", ("Vaniville_Start.ogg", "Vaniville_Loop.ogg")), ("Vermillion", ("Vermillion_Start.ogg", "Vermillion_Loop.ogg")),
            ("Viridian Forest", ("viridianforest_start.ogg", "viridianforest_loop.ogg")), ("Viridian City", ("ViridianCity_Start.ogg", "ViridianCity_Loop.ogg"))
            ]

            
            for music in music_options:

                frame:
                    background Solid('#070707')

                    xysize (450, 100)

                    imagebutton idle Solid('#ed7c3f') hover Solid('#ffdcca') pos (0,0) action Function(music_box_action, music)
                    
                    text "{b}[music[0]]{/b}":
                        style 'music_box_label'
                        color '#FFFFFF' xalign .5 ypos 30

                    #textbutton "{b}[music[0]]{/b}":
                    #    style 'music_box_label'
                    #    text_color '#FFFFFF' xalign .5 ypos 30
                    #    text_font "fonts/pkmndp.ttf"
                    #    # action Show("music_box_action", None, music)
                    #    action Function(music_box_action, music)
                        

    textbutton "{color=#000}Return{/color}" pos (0.1, 0.92) action [Function(music_box_exit), Hide("music_box_menu")] style "menu_choice_button" xmaximum 300
    
    add "BG/Blank2.webp" pos (.895, 0.92) crop (0.05, 0.015, .070, .05)
    text "{color=#FFF}{b}{size=30}Volume{/b}{/color}" pos (0.9, 0.94)
    bar pos (.9, .93) value Preference("music volume") style "pref_slider" ymaximum 50 yminimum 50

init python:
    def music_box_action(music):
        chosen_music = music[1]
        renpy.music.stop()

        if str(type(chosen_music)) == "<class 'str'>":
            renpy.music.queue("audio/music/" + chosen_music, channel='music', loop=True, fadein=0.1, tight=None)
        elif str(type(chosen_music)) == "<class 'tuple'>":
            renpy.music.queue("audio/music/" + chosen_music[0], channel='music', loop=False, fadein=0.1, tight=None)
            renpy.music.queue("audio/music/" + chosen_music[1], channel='music', loop=True, tight=None)

        return

    def music_box_exit():
        renpy.music.stop()
        renpy.music.queue("Audio/Music/Shelf of Memories (Prelude).ogg", channel='music', loop=True, fadein=0.1, tight=None)
        
        return


style music_box_label:
    size 35
