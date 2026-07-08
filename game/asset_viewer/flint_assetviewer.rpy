label flint_assetViewer:

python:
    from collections import OrderedDict
$ viewer_characters = OrderedDict()


$ scene_name = "garden"
$ corrupted_bgs = False
$ renpy.show("clouds")
$ renpy.show(scene_name, [Transform(zoom=.625)])
narrator "Welcome to Flintlock's asset tester, inspired by Ethan's of the same name! With special advice from Adingo."

# $ cur_dir = os.path.join(os.getcwd(), "game", "images", "expressions")

$ cur_dir = os.path.join(config.basedir, "game", "images", "expressions")

if not os.path.exists(cur_dir):
    narrator "You need to have an ''expressions'' folder."
    jump flint_assetViewer

label viewer_character:
$ testCharacter = renpy.input("What's the character name?").lower()

$ character_directory = os.path.join(cur_dir, testCharacter.lower())

$ number_of_images = len(character_directory)
$ is_valid_path = os.path.isdir(character_directory)

if number_of_images == 0:
    narrator "Folder is empty. Put some images in there."
    jump viewer_character
elif not is_valid_path or testCharacter == "":
    narrator "Character: [testCharacter] not valid entry. Please make certain character assets are fully lowercase."
    jump viewer_character


$ li = {} # li = LayeredImage
$ char_attributes = {}
$ char_cur_expressions = {}
$ yanchor_default = 0.6
$ ypos_default = 1.0

$ response = get_char_attributes(testCharacter)
$ char_attributes = response[0]
$ char_cur_expressions = response[1]
$ yanchor_default = response[3]
$ ypos_default = response[2]      

$ file_list = os.listdir(character_directory)

python:
    for file in file_list:
        if ".png" not in file and ".webp" not in file:
            file_list.remove(file)


# $ items = list(set([x.split("_")[1].split(".")[0] for x in file_list]))

$ val_xpos = .6
$ val_ypos = 1.02
$ val_zoom = 1.0
$ val_xalign = 0.5
$ val_yanchor = 0.6
$ update_character = False
$ update_character_info = ()

$ viewer_characters[testCharacter] = {"show_str": testCharacter, "tag": testCharacter, "asset_name":testCharacter, "current_expressions":char_cur_expressions, "char_attributes":char_attributes, "xpos": 0.5, "ypos": ypos_default, "yanchor": yanchor_default, "zoom": 1.0, "xzoom": 1.0, "rotate": 0}
$ selected_character = testCharacter


$ other_characters = []
$ char_levitating = False

$ interaction = ""
$ petpet_index = 0
$ headpat_counter = 0

label viewer_main_area:
        
$ scene_zoom = 1.0
$ need_extra = None

if scene_name == "garden":
    $ need_extra = "clouds"
    $ scene_zoom = 0.625
elif scene_name == "academy":
    $ scene_zoom = 0.625
elif scene_name == "fields1":
    $ need_extra = "clouds"

$ renpy.scene()
if corrupted_bgs:
    if need_extra is not None:
        $ renpy.show(need_extra, [Transform(matrixcolor=SaturationMatrix(0.0))])
    $ renpy.show(scene_name, [Transform(zoom=scene_zoom, matrixcolor=SaturationMatrix(0.0))])
else:
    if need_extra is not None:
        $ renpy.show(need_extra)
    $ renpy.show(scene_name, [Transform(zoom=scene_zoom)])

$ show_str = viewer_characters[selected_character]["asset_name"]

python:
    for key, value in viewer_characters[selected_character]["current_expressions"].items():
        if value is not None and (value[0] != "-" or selected_character == None):
            show_str += " " + value
    viewer_characters[selected_character]["show_str"] = show_str

$ char_data = viewer_characters[selected_character]


# New code for displaying every character.
# python:
#     for character in viewer_characters:
#         if character != selected_character:
#             test_item = viewer_characters[character]
#             renpy.show(test_item["show_str"], 
#             [Transform(xpos=test_item["xpos"], ypos=test_item["ypos"], yanchor=test_item["yanchor"],
#             zoom=test_item["zoom"], xzoom=test_item["xzoom"], 
#             alpha=1.0, rotate=test_item["rotate"])], 
#             tag=test_item["tag"])

show screen viewer_characters_display()

# The display of the current draggable character.
# if selected_character != None:
#     show screen draggable(show_str=char_data["show_str"], tag=char_data["tag"], x_pos=char_data["xpos"], y_pos=char_data["ypos"], zoom=char_data["zoom"], rotate=char_data["rotate"]) onlayer master


# if char_levitating is True:
#     $ renpy.show(show_str, [Transform(xpos=.5, ypos=val_ypos, zoom=val_zoom, alpha=1.0, rotate=0)], tag="mc")
#     # $ renpy.show(show_str, [Transform(xpos=.5, ypos=val_ypos, zoom=val_zoom, alpha=1.0, rotate=0), levitate], tag="mc")
# else:
#     $ renpy.show(show_str, [Transform(xpos=.5, ypos=val_ypos, zoom=val_zoom, alpha=1.0, rotate=0)], tag="mc")


python:
    for key, value in viewer_characters[selected_character]["current_expressions"].items():
        if value is not None and value[0] == "-":
            viewer_characters[selected_character]["current_expressions"][key] = None


call screen viewer_topGUI

$ test_item = [("dorm", Return("dorm_A"), False), ("research", Return("research"), False)]
$ interaction = _return
if interaction == "scenes":

    # scene_opt is grabbed from flint_configurations.rpy now
    $ scene_select = renpy.display_menu(scene_opt)

    if not isinstance(scene_select, bool): # There was a mistake, this'll prevent an error.
        $ scene_name = scene_select
    
# This code is no longer in use. TODO remove?
elif interaction == "manual_change":
    $ renpy.scene()
    if corrupted_bgs:
        if need_extra is not None:
            $ renpy.show(need_extra, [Transform(matrixcolor=SaturationMatrix(0.0))])
        $ renpy.show(scene_name, [Transform(zoom=scene_zoom, matrixcolor=SaturationMatrix(0.0))])
    else:
        if need_extra is not None:
            $ renpy.show(need_extra)
        $ renpy.show(scene_name, [Transform(zoom=scene_zoom)])

    python:
        for char in other_characters:
            renpy.hide(char)
    $ other_characters = []
    $ char_cur_expressions.clear()
    $ char_cur_expressions = {}
    
    jump viewer_character
elif interaction == "animations":
    python:
        for char in viewer_characters:
            renpy.hide(char)
    jump viewer_animation_list
elif interaction == "characters":
    
    $ character_options = [("Back", "back"), ("Add Custom", "custom"), ("Remove All Nonselected", "none")]
    python:
        for item in viewer_characters:
            if item != selected_character:
                character_options.append(("Remove " + item.title(), "remove_" + item))
    
    # normal_character_options is grabbed from flint_configurations.rpy now
    $ chosen_character = renpy.display_menu(character_options + normal_character_options)
    
    if isinstance(chosen_character, bool): # There was a mistake, this'll prevent an error.
        pass
    elif chosen_character is "none":
        python:
            char_removed = []
            for char in viewer_characters:
                if char != selected_character:
                    renpy.hide(char)
                    char_removed.append(char)
            
            for char in char_removed:
                del viewer_characters[char]

    elif "remove_" in chosen_character: # Needs to remove character from list.
        python:
            remove_char = chosen_character.split("remove_")[1]
            char_removed = []
            for char in viewer_characters:
                if char == remove_char:
                    renpy.hide(char)
                    char_removed.append(char)
            
            for char in char_removed:
                del viewer_characters[char]

    elif "back" in chosen_character: # Do nothing.
        pass

    else:
        if "custom" == chosen_character:
            $ result = view_custom_character()

            if result != False:
                $ chosen_character = result
            else:
                $ chosen_character = None

        if chosen_character is not None:

            $ char_info = get_char_attributes(chosen_character)

            $ custom_name = chosen_character
            # Version of character already exists. Make a new dict item for them.
            if chosen_character in viewer_characters:
                python:
                    attempt = 1
                    while True:
                        str_attempt = chosen_character + "_" + str(attempt)

                        if str_attempt not in viewer_characters:
                            custom_name = str_attempt
                            break

                        attempt += 1


            $ placement_positions = [.5, .325, .675, .125, .875]
            $ default_x = placement_positions[len(viewer_characters) % 5]
            $ viewer_characters[custom_name] = {"show_str": chosen_character, "tag": custom_name, "asset_name":chosen_character, "current_expressions": char_info[1], "char_attributes":char_info[0], "xpos": default_x, "ypos": char_info[2], "yanchor":char_info[3], "zoom": 1.0, "xzoom": 1.0, "rotate": 0}

            $ renpy.notify(f"Selected character: {custom_name}")
            $ selected_character = custom_name


elif interaction == "select_character":
    $ character_options = [("Back", "none")]

    python:
        for item in reversed(viewer_characters):
            #if item != selected_character:
            character_options.append((item.title(), item))

    # Selects the new character
     
    $ chosen_option = renpy.display_menu(character_options)

    if chosen_option != "none" and not isinstance(chosen_option, bool):
        # FLINTLOCK Should this be changed?
        $ selected_character = chosen_option
        $ char_attributes = viewer_characters[selected_character]["char_attributes"]
        $ char_cur_expressions = viewer_characters[selected_character]["current_expressions"]
        $ viewer_characters.move_to_end(selected_character)

        $ renpy.notify(f"Selected character: {chosen_option}")
        $ renpy.redraw("viewer_topGUI", 0)
        $ renpy.redraw("viewer_quick_expressions", 0)
        $ renpy.redraw("viewer_quick_expressions_item", 0)

elif interaction == "advanced":
    $ advanced_options = [("Play Music", "music"), ("{glitch=10.0}Corrupted World{/glitch} Background Toggle", "corrupted_world"), ("Credits", "credits"), ("Return", "return")]
    # ("rotate", "rotate"),
    $ chosen_advanced = renpy.display_menu(advanced_options)

    if chosen_advanced is "ypos":
        $ val_ypos_new = renpy.input("{color=#e70000}Enter ypos. Default: 1.0, Current: " + str(val_ypos) + ". Suggested range: 1.0 to 0.0.{/color}", length=6, allow="1234567890.")
        $ val_test = len(val_ypos_new.split("."))
        python:
            if val_test < 3:
                val_ypos = float(val_ypos_new)
    
    # TODO not implemented yet. Possibly remove?
    elif chosen_advanced is "yanchor":
        $ val_yanchor_new = renpy.input("{color=#e70000}Enter yanchor. Default: 0.6, Current: " + str(val_yanchor) + ". Suggested range: 1.0 to 0.0.{/color}", length=6, allow="1234567890.")
        $ val_test = len(val_yanchor_new.split("."))
        python:
            if val_test < 3:
                val_yanchor = float(val_yanchor_new)
    
    elif chosen_advanced is "zoom":
        $ val_zoom_new = renpy.input("{color=#e70000}Enter zoom. Default: 0.5, Current: " + str(val_zoom) + ". Suggested range: 1.0 to 0.0.{/color}", length=6, allow="1234567890.")
        $ val_test = len(val_zoom_new.split("."))
        python:
            if val_test < 3:
                val_zoom = float(val_zoom_new)
    
    elif chosen_advanced is "music":
    
        # music_options declaration moved to flint_configurables.rpy.
        $ chosen_music = renpy.display_menu(music_options)
        $ renpy.music.stop()

        if str(type(chosen_music)) == "<class 'str'>":
            $ renpy.music.queue("audio/music/" + chosen_music, channel='music', loop=True, fadein=0.1, tight=None)
        elif str(type(chosen_music)) == "<class 'tuple'>":
            $ renpy.music.queue("audio/music/" + chosen_music[0], channel='music', loop=False, fadein=0.1, tight=None)
            $ renpy.music.queue("audio/music/" + chosen_music[1], channel='music', loop=True, tight=None)

    elif chosen_advanced is "corrupted_world":
        $ corrupted_bgs = not corrupted_bgs

    elif chosen_advanced is "credits":
        narrator "This tool was created by Flintlock, based upon the original version made by Ethan."
        narrator "Special thanks to Adingo for his investigations and advice!"
        narrator "I hope this tool is useful to you! :D"

elif interaction == "headpat":
    $ petpet_index = (petpet_index + 1) % 10
    $ rand_xpos = float(random.randrange(37, 57))/100
    $ rand_ypos = float(random.randrange(22, 37))/100
    $ headpat_counter += 1
    $ renpy.show("petpet" + str(petpet_index), at_list=[tranform_petpet(rand_xpos, rand_ypos)], zorder=4, what="petpet")
    #$ headpatdialog("serena")
    #$ petpet_index = 0
    #$ renpy.show("misty uniform surprised")
    #$ renpy.say(misty, "Uh, what do you think you're doing?")
elif interaction == "copyexp":
    python:
        modified_clip = show_str.split(" ")
        full_clip = ""
        for item in modified_clip:
            if item[0] != "-":
                full_clip += item + " "
    $ renpy.notify(f"Expressions saved to clipboard.")
    $ CopyToClipboard(full_clip)()

elif interaction == "renderfile":
    python:

        asset_name = viewer_characters[selected_character]["asset_name"] # The actual character
        
        import glob
        import os

        if not os.path.isdir(os.path.join(config.basedir, "viewer_images")):
            os.mkdir(os.path.join(config.basedir, "viewer_images"))

        pattern = os.path.join(os.path.join(config.basedir, "viewer_images"), asset_name + "*" + ".png")
        files = glob.glob(pattern)

        max_num = 0
        for file in files:
            if os.path.isfile(file):
                filename = os.path.basename(file)
                middle = filename[len(asset_name):-len(".png")]
                if middle.isdigit():
                    num = int(middle)
                    if num > max_num:
                        max_num = num
        next_num = max_num + 1

        
        screenshot_filename = os.path.join(os.path.join(config.basedir, "viewer_images"), f"{asset_name}{next_num}.png")

        renpy.render_to_file(Transform(viewer_characters[selected_character]["show_str"], zoom=2.0), screenshot_filename)
        renpy.notify(f"Expressions saved to file: {screenshot_filename}")

elif interaction == "renderallfile":
    $ renpy.notify(f"Expressions saving to files...")
    python:
        for character in viewer_characters:
            
            asset_name = viewer_characters[character]["asset_name"] # The actual character
            
            import glob
            import os

            if not os.path.isdir(os.path.join(config.basedir, "viewer_images")):
                os.mkdir(os.path.join(config.basedir, "viewer_images"))

            pattern = os.path.join(os.path.join(config.basedir, "viewer_images"), asset_name + "*" + ".png")
            files = glob.glob(pattern)

            max_num = 0
            for file in files:
                if os.path.isfile(file):
                    filename = os.path.basename(file)
                    middle = filename[len(asset_name):-len(".png")]
                    if middle.isdigit():
                        num = int(middle)
                        if num > max_num:
                            max_num = num
            next_num = max_num + 1

            
            screenshot_filename = os.path.join(os.path.join(config.basedir, "viewer_images"), f"{asset_name}{next_num}.png")

            renpy.render_to_file(Transform(viewer_characters[character]["show_str"], zoom=2.0), screenshot_filename)

    $ renpy.notify(f"Expressions saved to files.")

elif interaction == "saveloc":

    python:
        import datetime
        now = datetime.datetime.now()
        msg = f"Images saved at: {now}.\n"
        with open("saved_locations.txt", "a") as f:
            f.write(msg)
            for character in viewer_characters:
                save_show_str = viewer_characters[character]["show_str"]
                save_xpos = round(viewer_characters[character]["xpos"], 5)
                save_ypos = round(viewer_characters[character]["ypos"] - 0.03, 5)  # Small adjustment for the other case.
                save_zoom = round(viewer_characters[character]["zoom"], 2)
                save_xzoom = round(viewer_characters[character]["xzoom"], 1)
                save_rotate = viewer_characters[character]["rotate"]
                save_tag = viewer_characters[character]["tag"]

                msg = f"show {save_show_str} as {save_tag}:\n"
                f.write(msg)
                msg = f"    xpos {save_xpos} ypos {save_ypos}\n"
                f.write(msg)
                msg = f"    "
                if save_xzoom != 1.0:
                    msg += f"xzoom {save_xzoom} "
                if save_rotate != 0:
                    msg += f"rotate {save_rotate} "
                if save_zoom != 1.0:
                    msg += f"zoom {save_zoom}"
                if len(msg) > 4:
                    msg += "\n"
                f.write(msg)
                f.write("\n")

    $ renpy.notify(f"locations & expressions saved to: saved_locations.txt")

elif interaction == "main_menu":
    $ MainMenu(confirm=True)()
    

if update_character is True:
    $ viewer_characters[selected_character]["current_expressions"][update_character_info[0]] = update_character_info[1]
    $ update_character = False


jump viewer_main_area

label viewer_animation_list:

$ animation_options = [("All", "all"), ("Walk out", "walk_out"), ("Walk in", "walk_in"), ("Hop Around", "hop_around"), ("RIP Headphones.", "rip")]
$ chosen_animation = renpy.display_menu(animation_options)

$ val_xpos = viewer_characters[selected_character]["xpos"]
$ val_ypos = viewer_characters[selected_character]["ypos"]
$ val_zoom = viewer_characters[selected_character]["zoom"]
$ val_tag =  viewer_characters[selected_character]["tag"]

if chosen_animation is "all" or chosen_animation is "walk_out":
    $ renpy.show(show_str, [Transform(xpos=val_xpos, ypos=val_ypos, zoom=val_zoom, alpha=1.0), walk_out_anim], tag=val_tag)
    pause 1.0

if chosen_animation is "all" or chosen_animation is "walk_in":
    $ renpy.show(show_str, [Transform(xpos=val_xpos, ypos=val_ypos, zoom=val_zoom, alpha=1.0), walk_in_anim], tag=val_tag)
    pause 1

if chosen_animation is "all" or chosen_animation is "hop_around":
    $ renpy.show(show_str, [Transform(xpos=val_xpos, ypos=val_ypos, zoom=val_zoom, alpha=1.0), hop_around_anim], tag=val_tag)
    pause 6

if chosen_animation is "all" or chosen_animation is "rip":
    stop music

    play sound "Audio/Mic_Feedback.ogg"
    $ renpy.music.stop(channel='crowd', fadeout=0.5)

    $ renpy.show(show_str, [Transform(xpos=val_xpos, ypos=val_ypos, zoom=val_zoom, alpha=1.0), monochrome, rip_anim], tag=val_tag)

    pause 3.6
    play sound "Audio/Thud2.ogg"
    play sound "Audio/Thud.ogg"
    pause 1.0


jump viewer_main_area

transform walk_out_anim:
    xpos val_xpos - .1 ypos val_ypos
    ease 1.0 xpos 1.2

transform walk_in_anim:
    xpos -.2 ypos val_ypos
    zoom val_zoom
    yanchor val_yanchor
    ease 1.0 xpos val_xpos -.1

transform hop_around_anim:
    parallel:
        linear 0.2 xpos val_xpos + .1
        pause .6
        linear .4 xpos val_xpos - .2
        pause .6
        linear .2 xpos val_xpos
        repeat
    parallel:
        ease 0.3 ypos val_ypos + .1
        ease 0.3 ypos val_ypos
        repeat

transform rip_anim:
    
    parallel:
        xpos val_xpos
        ease 0.04 xpos val_xpos + .04
        ease 0.04 xpos val_xpos - .04
        ease 0.04 xpos val_xpos
        repeat 10
    parallel:
        ease 0.04 ypos val_ypos + .04
        ease 0.04 ypos val_ypos - .04
        ease 0.04 ypos val_ypos + 0
        repeat 10

    pause 1.2

    ease 0.5 xpos val_xpos - .02 ypos val_ypos + .1 rotate -10.0
    pause 0.5
    ease 0.5 xpos val_xpos ypos val_ypos + .2 rotate 10.0

transform levitate:
    rotate 0 ypos val_ypos
    parallel:
        ease 0.18 ypos val_ypos
        ease 0.18 ypos val_ypos - 0.01
        ease 0.18 ypos val_ypos
        ease 0.18 ypos val_ypos + 0.01
        repeat


# TODO Everything that needs doing:

# Optional, maybe future roadmap.
# Fixing animations, porting to new code.
# Improve selection of scenes?
# Statically order important fields (mouth, eyes) at the top of the selection.
# Fixing keys to make it go faster based on holding the key. PARTIAL.
# Fixing leaf/klara. HID THE ISSUE FROM SIGHT. GOOD ENOUGH FOR NOW.
# manual setting of fields like ypos.

# 5.0.1 fixes needed:
# Fix game crashing if no _. Make sure there are three portions.
# Add feature to make character blank. For brows/eyes/mouth/etc.