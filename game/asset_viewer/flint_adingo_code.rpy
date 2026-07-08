screen main_menu_modbtn:
    textbutton "{color=#000000}Music Box" text_xalign 0.5 anchor (1.0, 0) pos (0.995, 0.8) action Show("music_box_menu") text_font "fonts/pkmndp.ttf" style "menu_choice_button" xmaximum 300
    textbutton "{color=#000000}Asset Viewer" text_xalign 0.5 anchor (1.0, 1.0) pos (0.995, 0.68) action Start("flint_assetViewer") text_font "fonts/pkmndp.ttf" style "menu_choice_button" xmaximum 300
    textbutton "{color=#000000}Asset Creator" text_xalign 0.5 anchor (1.0, 1.0) pos (0.995, 0.76) action Start("flint_assetCreator") text_font "fonts/pkmndp.ttf" style "menu_choice_button" xmaximum 300

    #textbutton "Mods" text_xalign 0.5 anchor (1.0, 1.0) pos (0.995, 0.86) action Show("adingo_mod_screen", transition=dissolve) text_font "fonts/pkmndp.ttf" style "menu_choice_button" xmaximum 300

init 1 python:
    def asset_viewer():
        if renpy.get_screen("main_menu"):
            renpy.show_screen("main_menu_modbtn")
    
    config.interact_callbacks.append(asset_viewer)