
init python:
    def get_char_attributes(name):
        
        character_directory = os.path.join(cur_dir, name)

        number_of_images = len(character_directory)
        is_valid_path = os.path.isdir(character_directory)
        # TODO add error checking here.

        li = {} # li = LayeredImage
        char_attributes = {}
        char_cur_expressions = {}
        for key, val in renpy.display.image.images.items():
            if isinstance(val, LayeredImage): # This one actually works without a full prefix
                li[key]=val # Can do val.layers if you don't care about the entire object instead, of course

        for lay in li[(name,)].layers:
            if isinstance(lay, store.layeredimage.Attribute): # This and the Always class do need the full prefix
                if lay.group in char_attributes:
                    pass
                else: # Newly seen group

                    # This is a quick and DIRTY way to hide these problematic makeup layers from sight. It's not permanent, but hey, at least it'll prevent crashes.
                    if testCharacter == "leaf":
                        bad_items = ["makeup", "makeupmouth", "makeupbrow"]
                        if lay.group in bad_items:
                            continue
                    elif testCharacter == "klara":
                        bad_items = ["makeup", "browmakeup", "lipstick"]
                        if lay.group in bad_items:
                            continue

                    if testCharacter == "iono" and lay.group == "body":
                        char_cur_expressions[lay.group] = "body1"
                    else:
                        char_cur_expressions[lay.group] = None
                    char_attributes[lay.group] = []

        fixed_args = li[(testCharacter,)].fixed_args
        if "yanchor" in fixed_args:
            yanchor_default = fixed_args["yanchor"]
        if "ypos" in fixed_args:
            ypos_default = fixed_args["ypos"] + 0.03


        file_list = os.listdir(character_directory)

        for file in file_list:
            if ".png" not in file and ".webp" not in file:
                file_list.remove(file)


        #items = list(set([x.split("_")[1].split(".")[0] for x in file_list]))

        items = [
            x.split("_")[1].split(".")[0]
            for x in file_list
            if "_" in x and "." in x  # optional: also ensure there's an extension
        ]
        items = list(set(items))

        for keys, value in char_attributes.items():
            items_filtered = [x.split(".png")[0].split(".webp")[0] for x in file_list if "_" in x and x.split("_")[1] == keys]
            for item in items_filtered:
                att_name = item.split("_")[2]
                value.append(att_name)

        return [char_attributes, char_cur_expressions, ypos_default, yanchor_default]
    
    def view_custom_character():
        char_name = renpy.input("What's the character name?").lower()

        character_directory = os.path.join(cur_dir, char_name.lower())

        number_of_images = len(character_directory)
        is_valid_path = os.path.isdir(character_directory)

        if char_name == "iono":
            error_string = "Sorry, Iono doesn't work well with the Asset Viewer. If you want to use her, try it when you first open the Viewer."
            renpy.notify(error_string)

        #     return False

        if number_of_images == 0:
            error_string = "Folder is empty. Put some images in there."
            renpy.notify(error_string)

            return False

        elif not is_valid_path or char_name == "":
            error_string = f"Character: {char_name} not valid entry. Please make certain character assets are fully lowercase."
            renpy.notify(error_string)
            return False

        return char_name

    def save_position(drags, drop):
        #return True
        if drags:
            drag = drags[0]
            tag = viewer_characters[selected_character]["tag"]

            # Anchors (hardcode or pass/store; assume 0.5/0.6)
            x_anchor = 0.5
            y_anchor = viewer_characters[selected_character]["yanchor"]
            
            # Final top-left pixels
            final_tl_x = drag.x
            final_tl_y = drag.y
            
            # Anchor offset pixels (from child's rendered size)
            anchor_offset_x = drag.w * x_anchor
            anchor_offset_y = drag.h * y_anchor
            
            # Final anchor pixels = top-left + offset
            final_anchor_x = final_tl_x + anchor_offset_x
            final_anchor_y = final_tl_y + anchor_offset_y

            new_x = final_anchor_x / renpy.config.screen_width
            new_y = final_anchor_y / renpy.config.screen_height
            
            # Optional: Notify
            renpy.notify("{} saved at x={:.5f}, y={:.5f}".format(tag, new_x, new_y))

            viewer_characters[selected_character]["xpos"] = new_x
            viewer_characters[selected_character]["ypos"] = new_y

        return True  # Allow free drop


init python:
    def update_zoom_rotate(direction):
        char_data = viewer_characters[selected_character]
        if direction == "zoom_in":
            viewer_characters[selected_character]["zoom"] = min(char_data["zoom"] + 0.05, 3.0)  # Cap at 3x
        elif direction == "zoom_out":
            viewer_characters[selected_character]["zoom"] = max(char_data["zoom"] - 0.05, 0.1)  # Floor at 0.1x
        elif direction == "rotate_cw":
            viewer_characters[selected_character]["rotate"] = (char_data["rotate"] + 5) % 360
        elif direction == "rotate_ccw":
            viewer_characters[selected_character]["rotate"] = (char_data["rotate"] - 5) % 360
        elif direction == "xzoom":
            viewer_characters[selected_character]["xzoom"] = viewer_characters[selected_character]["xzoom"] * -1.0
        elif direction == "left":
            viewer_characters[selected_character]["xpos"] = viewer_characters[selected_character]["xpos"] - 0.01
        elif direction == "right":
            viewer_characters[selected_character]["xpos"] = viewer_characters[selected_character]["xpos"] + 0.01
        elif direction == "up":
            viewer_characters[selected_character]["ypos"] = viewer_characters[selected_character]["ypos"] - 0.01
        elif direction == "down":
            viewer_characters[selected_character]["ypos"] = viewer_characters[selected_character]["ypos"] + 0.01

        if direction in ["zoom_in", "zoom_out", "rotate_cw", "rotate_ccw"]:
            renpy.notify("Zoom: {:.2f}x, Rotate: {}°".format(char_data["zoom"], char_data["rotate"]))
        elif direction == "xzoom":
            pass
        else: 
            renpy.notify("xpos: {:.2f}, ypos: {:.2f},".format(viewer_characters[selected_character]["xpos"], viewer_characters[selected_character]["ypos"]))
        renpy.restart_interaction()  # Updates Transform live

    def select_character(character):
        renpy.notify("Selected character: {}".format(character))
        global selected_character, quick_expressions_toggle

        selected_character = character
        char_attributes = viewer_characters[selected_character]["char_attributes"]
        char_cur_expressions = viewer_characters[selected_character]["current_expressions"]
        viewer_characters.move_to_end(selected_character)

        renpy.hide_screen("viewer_quick_expressions_item")

        if quick_expressions_toggle:
            renpy.show_screen("viewer_quick_expressions")

        renpy.hide_screen("viewer_topGUI")
        renpy.show_screen("viewer_topGUI")
        renpy.restart_interaction()  # Updates Transform live

    def toggle_gui():
        if renpy.get_screen("viewer_topGUI"):
            renpy.hide_screen("viewer_topGUI")
            renpy.hide_screen("viewer_quick_expressions")
            renpy.hide_screen("viewer_quick_expressions_item")
            # renpy.hide_screen("quick_menu") # Why can't I hide this?
        else:
            renpy.show_screen("viewer_topGUI")
            if quick_expressions_toggle:
                renpy.show_screen("viewer_quick_expressions")
                # renpy.hide_screen("quick_menu")
        
        renpy.restart_interaction()


# Useful code for checking fields.
# with open("fields.txt", "a") as f:
#     transform_props = {}
#     li_obj = li[(testCharacter,)]

#     all_attrs = dir(li_obj)

#     instance_vars = vars(li_obj)
#     f.write("=== Instance vars for '{}' ({} total) ===".format(testCharacter, len(instance_vars)))
#     for var_name, var_val in sorted(instance_vars.items()):
#         # For transform props, try .value(0) if expression
#         val = var_val
#         if hasattr(var_val, 'value'):
#             val = var_val.value(0)  # Evaluate constant (e.g., Constant(0.5) → 0.5)
#         f.write("  - {}: {} (type: {})\n\n".format(var_name, val, type(var_val)))
    
#     testing = li_obj.fixed_args
#     f.write("fixed args are these: " + str(testing))