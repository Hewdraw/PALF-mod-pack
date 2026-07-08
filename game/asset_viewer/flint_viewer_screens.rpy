default quick_expressions_toggle = False
default presets_toggle = False
default tools_toggle = False

screen viewer_topGUI():
    # $ tooltip = GetTooltip()
    if quick_expressions_toggle:
        textbutton "{color=#000000}Expression Menu" text_xalign 0.5 xalign 0.0 pos (0, 0) action [SetVariable("quick_expressions_toggle", False), Hide("viewer_quick_expressions"), Hide("viewer_quick_expressions_item")] text_font "fonts/pkmndp.ttf" style "menu_choice_button" xmaximum 300 ymaximum 100 yminimum 100
    else:
        textbutton "{color=#000000}Expression Menu" text_xalign 0.5 xalign 0.0 pos (0, 0) action [SetVariable("quick_expressions_toggle", True), Show("viewer_quick_expressions")] text_font "fonts/pkmndp.ttf" style "menu_choice_button" xmaximum 300 ymaximum 100 yminimum 100
    textbutton "{color=#000000}Scene Select" text_xalign 0.5 xalign 0.0 pos (300, 0) action [Return("scenes"), Hide("viewer_quick_expressions"), Hide("viewer_quick_expressions_item"), Hide("viewer_presets_screen")] text_font "fonts/pkmndp.ttf" style "menu_choice_button" xmaximum 270 ymaximum 100 yminimum 100
    textbutton "{color=#000000}Add Character" text_xalign 0.5 xalign 0.0 pos (570, 0) action [Return("characters"), Hide("viewer_quick_expressions"), Hide("viewer_quick_expressions_item"), Hide("viewer_presets_screen")] text_font "fonts/pkmndp.ttf" style "menu_choice_button" xmaximum 270 ymaximum 100 yminimum 100
    textbutton "{color=#000000}Select Character" text_xalign 0.5 xalign 0.0 pos (840, 0) action [Return("select_character"), Hide("viewer_quick_expressions"), Hide("viewer_quick_expressions_item"), Hide("viewer_presets_screen")] text_font "fonts/pkmndp.ttf" style "menu_choice_button" xmaximum 270 ymaximum 100 yminimum 100
    # textbutton "{color=#000000}Animations" text_xalign 0.5 xalign 0.0 pos (840, 0) action [Return("animations"), Hide("viewer_quick_expressions"), Hide("viewer_quick_expressions_item"), Hide("viewer_presets_screen")] text_font "fonts/pkmndp.ttf" style "menu_choice_button" xmaximum 270 ymaximum 100 yminimum 100
    #textbutton "{color=#000000}Change Character" text_xalign 0.5 xalign 0.0 pos (1110, 0) action [Return("manual_change"), Hide("viewer_quick_expressions"), Hide("viewer_quick_expressions_item"), Hide("viewer_presets_screen")] text_font "fonts/pkmndp.ttf" style "menu_choice_button" xmaximum 270 ymaximum 100 yminimum 100
    
    textbutton "{color=#000000}Tools Display" text_xalign 0.5 xalign 0.0 pos (1110, 0) action [SetVariable("tools_toggle", not tools_toggle)] text_font "fonts/pkmndp.ttf" style "menu_choice_button" xmaximum 270 ymaximum 100 yminimum 100
    if presets_toggle:
        textbutton "{color=#000000}Presets" text_xalign 0.5 xalign 0.0 pos (1380, 0) action [SetVariable("presets_toggle", False), Hide("viewer_presets_screen")] text_font "fonts/pkmndp.ttf" style "menu_choice_button" xmaximum 270 ymaximum 100 yminimum 100
    else:
        textbutton "{color=#000000}Presets" text_xalign 0.5 xalign 0.0 pos (1380, 0) action [SetVariable("presets_toggle", True), Show("viewer_presets_screen")] text_font "fonts/pkmndp.ttf" style "menu_choice_button" xmaximum 270 ymaximum 100 yminimum 100
    textbutton "{color=#000000}Extra Options" text_xalign 0.5 xalign 0.0 pos (1650, 0) action [Return("advanced"), Hide("viewer_quick_expressions"), Hide("viewer_quick_expressions_item"), Hide("viewer_presets_screen")] text_font "fonts/pkmndp.ttf" style "menu_choice_button" xmaximum 270 ymaximum 100 yminimum 100

    #textbutton "{color=#000000}Petpet." text_xalign 0.5 xalign 0.5 pos (1250, 900) action [Return("headpat")] text_font "fonts/pkmndp.ttf" style "menu_choice_button" xmaximum 270 ymaximum 100 yminimum 100
    if tools_toggle:
        textbutton "{color=#000000}Save Location." text_xalign 0.5 xalign .5 pos (690, 900) action [Return("saveloc")] text_font "fonts/pkmndp.ttf" style "menu_choice_button" xmaximum 270 ymaximum 100 yminimum 100 tooltip "Saves the current coordinates/expressions of ALL \ncharacters to a file, named saved_locations.txt."
        textbutton "{color=#000000}Clip Expression." text_xalign 0.5 xalign .5 pos (960, 900) action [Return("copyexp")] text_font "fonts/pkmndp.ttf" style "menu_choice_button" xmaximum 270 ymaximum 100 yminimum 100 tooltip "This will clip the selected character's \nexpression to your clipboard."
        textbutton "{color=#000000}Save Image." text_xalign 0.5 xalign .5 pos (1230, 900) action [Return("renderfile")] text_font "fonts/pkmndp.ttf" style "menu_choice_button" xmaximum 270 ymaximum 50 yminimum 50 tooltip "Saves the selected character's expressions as \nan image, found in the folder ''viewer_images.''"
        textbutton "{color=#000000}Save ALL Images." text_xalign 0.5 xalign .5 pos (1230, 950) action [Return("renderallfile")] text_font "fonts/pkmndp.ttf" style "menu_choice_button" xmaximum 270 ymaximum 50 yminimum 50 tooltip "Saves ALL characters expressions as \nimages, found in the folder ''viewer_images.''"
        
    textbutton "{color=#000000}Main Menu" text_xalign 0.5 xalign 0.0 pos (1650, 980) action [Return("main_menu")] text_font "fonts/pkmndp.ttf" style "menu_choice_button" xmaximum 270 ymaximum 100 yminimum 100
    #text "Headpat Counter: " + str(headpat_counter) pos(1100, 1000)

    $ tooltip = GetTooltip()
    if tooltip:
            nearrect:
                focus "tooltip"
                prefer_top False

                frame:
                    xanchor 0.0
                    xpos 0.0
                    text "{size=30}" + tooltip

screen viewer_quick_expressions():

    $ show_scroll = 19  < len(viewer_characters[selected_character]["char_attributes"])
    viewport id "expression_type":
        area(000,100,300,980)

        if show_scroll:
            scrollbars "vertical"
            arrowkeys True
            pagekeys True
            mousewheel True
            vscrollbar_base_bar "#fff"
            vscrollbar_thumb "#363436"
            vscrollbar_top_bar "#e7e6e7"
            vscrollbar_bottom_bar "#e7e6e7"
            child_size (300, 50 * len(viewer_characters[selected_character]["char_attributes"]) + 10)

        $ yval = 0
        $ expression_index = 0
        # if "body" in char_attributes: # TODO Replace this char_attributes with the currently selected character's attributes!
        #     pass
        # elif "base" in char_attributes and "clothes" in char_attributes:
        #     pass

        # TODO Flintlock
        # Temporarily remove the makeup layers from Leaf and Klara.
        # Permanent solution is likely here, if I can figure it out.

        for keys, value in viewer_characters[selected_character]["char_attributes"].items():
            textbutton "{color=#000000}" + keys text_xalign 0.5 xalign 0.0 pos (0, yval) action Show("viewer_quick_expressions_item", expression_index_item=expression_index, layer_key=keys) text_font "fonts/pkmndp.ttf" style "menu_choice_button" maximum (300,75) minimum (300,50)
            $ yval += 50
            $ expression_index += 1

screen viewer_quick_expressions_item(expression_index_item, layer_key):
    $ yval = 0
    # This is old code, but I'm keeping it here just so you can see how HELL the first version was.
    #$ temp_full_string = [x for num, x in enumerate(full_str.split("_")) if num != 2 + expression_index_item]
    #$ temp_before_str = ''.join([x + "_" for num, x in enumerate(temp_full_string) if num < 2 + expression_index_item])
    #$ temp_after_str = ''.join(["_" + x for num, x in enumerate(temp_full_string) if num >= 2 + expression_index_item])
    #$ item_list = [x.split("_")[2 + expression_index_item].split(".webp")[0] for x in os.listdir(character_directory) if len(x.split("_")) == len(layers) + 2 and temp_before_str in x and temp_after_str in x]
    

    $ show_scroll = 19 - expression_index_item < len(viewer_characters[selected_character]["char_attributes"][layer_key])
    viewport id "expression_type_item":
        if expression_index_item < 20:
            area(300,100+expression_index_item*50,300,980-expression_index_item*50)
        else:
            area(300,100,300,980)

        if show_scroll:
            scrollbars "vertical"
            arrowkeys True
            pagekeys True
            mousewheel True
            vscrollbar_base_bar "#fff"
            vscrollbar_thumb "#363436"
            vscrollbar_top_bar "#e7e6e7"
            vscrollbar_bottom_bar "#e7e6e7"
            child_size (300, 50 * len(viewer_characters[selected_character]["char_attributes"][layer_key]) + 10)

        $ layer_key_test = layer_key
        if layer_key in ["eyebrows", "eyesparkles", "costume", "clothes"]:
            if viewer_characters[selected_character]["current_expressions"][layer_key] is not None:
                $ remove_item = "-" + str(viewer_characters[selected_character]["current_expressions"][layer_key])  
                $ item_return_val = (layer_key, remove_item)           
                textbutton "{color=#000000}Default" text_xalign 0.5 xalign 0.0 pos (0, yval) action [Return("expression_change"), SetVariable("quick_expressions_toggle", False), SetVariable("update_character", True), SetVariable("update_character_info", item_return_val)] text_font "fonts/pkmndp.ttf" style "menu_choice_button" maximum (300,50) minimum (300,50)
                $ yval += 50
        elif layer_key not in ["body", "eyes", "mouth", "base"]:
            if viewer_characters[selected_character]["current_expressions"][layer_key] is not None:
                $ remove_item = "-" + str(viewer_characters[selected_character]["current_expressions"][layer_key])  
                $ item_return_val = (layer_key, remove_item)           
                textbutton "{color=#000000}None" text_xalign 0.5 xalign 0.0 pos (0, yval) action [Return("expression_change"), SetVariable("quick_expressions_toggle", False), SetVariable("update_character", True), SetVariable("update_character_info", item_return_val)] text_font "fonts/pkmndp.ttf" style "menu_choice_button" maximum (300,50) minimum (300,50)
                $ yval += 50
        
        for item in viewer_characters[selected_character]["char_attributes"][layer_key]:
            $ item_return_val = (layer_key, item)
            textbutton "{color=#000000}" + item text_xalign 0.5 xalign 0.0 pos (0, yval) action [Return("expression_change"), SetVariable("quick_expressions_toggle", False), SetVariable("update_character", True), SetVariable("update_character_info", item_return_val)] text_font "fonts/pkmndp.ttf" style "menu_choice_button" maximum (300,50) minimum (300,50)
            $ yval += 50

init python:
    def preset_setter(new_xpos=None, new_ypos=None, new_zoom=None, new_rotate=None):
        if new_xpos != None:
            viewer_characters[selected_character]["xpos"] = new_xpos
        if new_ypos != None:
            viewer_characters[selected_character]["ypos"] = new_ypos
        if new_zoom != None:
            viewer_characters[selected_character]["zoom"] = new_zoom
        if new_rotate != None:
            viewer_characters[selected_character]["rotate"] = new_rotate

# Function(preset_setter, new_xpos=0.5),

# SetVariable(SetVariable(viewer_characters[selected_character]["xpos"], 0.5), viewer_characters[selected_character]["ypos"], 1.03), SetVariable(viewer_characters[selected_character]["zoom"], 1.0), SetVariable(viewer_characters[selected_character]["rotate"], 0),
screen viewer_presets_screen():
    viewport id "preset_screen":
        area(1380,100,270,980)        
        textbutton "{color=#000000}Reset Position" text_xalign 0.5 xalign 0.0 pos (0, 0) action [Return("preset"), 
        Function(preset_setter, new_xpos=0.5, new_ypos=1.03, new_zoom=1.0, new_rotate=0), 
        SetVariable("presets_toggle", False), SetVariable("char_levitating", False)] text_font "fonts/pkmndp.ttf" style "menu_choice_button" maximum (270,100) minimum (270,100)

        textbutton "{color=#000000}Large Image (.25)" text_xalign 0.5 xalign 0.0 pos (0, 100) action [Return("preset"), 
        Function(preset_setter, new_xpos=0.5, new_ypos=1.03, new_zoom=0.5, new_rotate=0),
        SetVariable("presets_toggle", False)] text_font "fonts/pkmndp.ttf" style "menu_choice_button" maximum (270,100) minimum (270,100)
        
        # Below two no longer necessary with recent change.
        # textbutton "{color=#000000}Short" text_xalign 0.5 xalign 0.0 pos (0, 200) action [Return("preset"), 
        # SetVariable("val_ypos", 1.0), SetVariable("val_xalign", 0.5), SetVariable("val_yanchor", 0.63), 
        # SetVariable("presets_toggle", False), SetVariable("char_levitating", False)] text_font "fonts/pkmndp.ttf" style "menu_choice_button" maximum (270,100) minimum (270,100)
        
        # textbutton "{color=#000000}Tall" text_xalign 0.5 xalign 0.0 pos (0, 300) action [Return("preset"), 
        # SetVariable("val_ypos", 1.0), SetVariable("val_xalign", 0.5), SetVariable("val_yanchor", 0.57), 
        # SetVariable("presets_toggle", False), SetVariable("char_levitating", False)] text_font "fonts/pkmndp.ttf" style "menu_choice_button" maximum (270,100) minimum (270,100)
        
        textbutton "{color=#000000}Levitating" text_xalign 0.5 xalign 0.0 pos (0, 200) action [Return("preset"), 
        Function(preset_setter, new_xpos=0.5, new_ypos=0.5, new_zoom=1.0, new_rotate=0),
        SetVariable("presets_toggle", False), SetVariable("char_levitating", True)] text_font "fonts/pkmndp.ttf" style "menu_choice_button" maximum (270,100) minimum (270,100)

image petpet:
    "petpet/petpet0.webp"
    .08
    "petpet/petpet1.webp"
    .08
    "petpet/petpet2.webp"
    .08
    "petpet/petpet3.webp"
    .08
    "petpet/petpet4.webp"
    .08
    repeat

transform tranform_petpet(xval, yval):
    xpos xval ypos yval
    pause 3.0
    linear 2.0 alpha 0.5
    xpos 2.0 ypos 2.0 alpha 1

screen draggable(show_str, tag, x_pos, y_pos, zoom, rotate):

    key "anyrepeat_K_RIGHT"action Function(update_zoom_rotate, direction="rotate_cw")  # Clockwise
    key "anyrepeat_K_LEFT" action Function(update_zoom_rotate, direction="rotate_ccw") 
    key "anyrepeat_K_UP" action Function(update_zoom_rotate, direction="zoom_in")
    key "anyrepeat_K_DOWN" action Function(update_zoom_rotate, direction="zoom_out")
    key "anyrepeat_K_p" action Function(update_zoom_rotate, direction="xzoom")
    key "anyrepeat_K_a" action Function(update_zoom_rotate, direction="left")
    key "anyrepeat_K_w" action Function(update_zoom_rotate, direction="up")
    key "anyrepeat_K_s" action Function(update_zoom_rotate, direction="down")
    key "anyrepeat_K_d" action Function(update_zoom_rotate, direction="right")
    key "K_h" action Function(toggle_gui)
    key "K_i" action Screenshot()
 
    drag:
        
        xanchor 0.5 yanchor viewer_characters[selected_character]["yanchor"] 
        xpos viewer_characters[selected_character]["xpos"] ypos viewer_characters[selected_character]["ypos"]
        drag_raise True
        draggable True
        drag_offscreen True

        # drag_handle (0, 0, 1.0, 1.0)

        focus_mask True

        add Transform(show_str, zoom=viewer_characters[selected_character]["zoom"], xzoom=viewer_characters[selected_character]["xzoom"], alpha=1.0, rotate=viewer_characters[selected_character]["rotate"], xanchor=0.5, yanchor=0.6 )

        dragged save_position

# screen viewer_characters_display():
#     for character in viewer_characters:
#         if character != selected_character:
#             $ test_item = viewer_characters[character]
#             button:
#                 xpos test_item["xpos"]
#                 ypos test_item["ypos"]
#                 xanchor 0.5
#                 yanchor test_item["yanchor"]
#                 focus_mask True
#                 background None
#                 # action Function(your_function, character)
                
#                 add Transform(test_item["show_str"],
#                     zoom=test_item["zoom"],
#                     xzoom=test_item["xzoom"],
#                     alpha=1.0,
#                     rotate=test_item["rotate"],
#                     xanchor=0.5#,
#                     #yanchor=test_item["yanchor"]
#                     )

screen viewer_character_inactive(character):
    $ test_item = viewer_characters[character]
    
    drag:
        xanchor 0.5 yanchor test_item["yanchor"]
        xpos test_item["xpos"] ypos test_item["ypos"]
        draggable False
        drag_offscreen True

        focus_mask True

        add Transform(test_item["show_str"], 
            zoom=test_item["zoom"], 
            xzoom=test_item["xzoom"], 
            alpha=1.0, 
            rotate=test_item["rotate"], 
            xanchor=0.5, 
            yanchor=0.6)

        clicked Function(select_character, character)

screen viewer_characters_display():
    for character in viewer_characters:
        if character != selected_character:
            use viewer_character_inactive(character)
        else:
            $ char_data = viewer_characters[selected_character]

            use draggable(show_str=char_data["show_str"], tag=char_data["tag"], x_pos=char_data["xpos"], y_pos=char_data["ypos"], zoom=char_data["zoom"], rotate=char_data["rotate"])
