label flint_assetCreator:

show expression "BG/Garden.webp" as current_scene
narrator "This script is to create a portrait for a NEW character, to be added into portraits.rpy."
narrator "If you are adding new items for an existing character that already has that layer, you can simply add the file to existing image folder, and it will appear in the Asset Viewer."
narrator "Note: If it doesn't appear, add ''auto'' to the layer in portraits.rpy."

label creator_character:
$ cur_dir_express = os.path.join(os.getcwd(), "game", "images", "expressions")
$ cur_dir_output = os.getcwd()
$ testCharacter = renpy.input("What's the character name? (Note: assets must be in expression folder.)").lower()

$ character_directory = os.path.join(config.basedir, "game", "images", "expressions", testCharacter)
narrator "[character_directory]"

$ flag_issue = False

$ number_of_images = len(character_directory)
if number_of_images == 0:
    narrator "Folder is empty. Put some images in there."
    jump creator_character

python:
    file_list = os.listdir(character_directory)
    for item in file_list[:]:
        if not (item.endswith(".png") or item.endswith(".webp")):
            file_list.remove(item)
    items = list(set([x.split("_")[1].split(".")[0] for x in file_list]))

narrator "[items]"

python:
    file_name_to_output = testCharacter + ".txt"
    f = open(file_name_to_output, "w")
    f.write("    layeredimage " + testCharacter + ":\n")
    f.write("        zoom 0.5\n")
    f.write("        xalign 0.5\n")
    f.write("        yanchor 0.6\n")
    f.write("        ypos 1.0\n")

    items_filtered = [x.split(".png")[0].split(".webp")[0] for x in file_list if x.split("_")[1] == "body"] #account for png and webp

    if len(items_filtered) > 0: # Using body, and not base/hair.
        f.write('\n        group body:\n')
        if testCharacter + "_body_neutral" in items_filtered:
            f.write('            attribute neutral "' + testCharacter + '_body_neutral" default\n')
            items_filtered.remove(testCharacter + "_body_neutral")
        else:
            flag_issue = True

if flag_issue:
    narrator "No neutral body found."
    $ flag_issue = False

python:
    if len(items_filtered) > 0:
        for item in items_filtered:
            att_name = item.split("_")[2]
            f.write('            attribute ' + att_name + ' "' + item + '"\n')
        items.remove("body")
    else: # check for base/hair.
        items_filtered = [x.split(".png")[0].split(".webp")[0] for x in file_list if x.split("_")[1] == "base"]
        if len(items_filtered) > 0: # Using bases.
            f.write('\n        group base auto:\n')
            if testCharacter + "_base_neutralbase" in items_filtered:
                f.write('            attribute neutralbase "' + testCharacter + '_base_neutralbase" default\n')
                items_filtered.remove(testCharacter + "_base_neutralbase")
        for item in items_filtered:
            att_name = item.split("_")[2]
            f.write('            attribute ' + att_name + ' "' + item + '"\n')
        items.remove("base")
    

    items_filtered = [x.split(".png")[0].split(".webp")[0] for x in file_list if x.split("_")[1] == "hair"]
    if len(items_filtered) > 0: # Using hair.
        f.write('\n        group hair auto:\n')
        if testCharacter + "_hair_neutralhair" in items_filtered:
            f.write('            attribute neutralhair "' + testCharacter + '_hair_neutralhair" default\n')
            items_filtered.remove(testCharacter + "_hair_neutralhair")
        
        for item in items_filtered:
            att_name = item.split("_")[2]
            f.write('            attribute ' + att_name + ' "' + item + '"\n')
        items.remove("hair")

    items_filtered = [x.split(".png")[0].split(".webp")[0] for x in file_list if x.split("_")[1] == "clothes"]
    if len(items_filtered) > 0: # Using clothes.
        f.write('\n        group clothes auto:\n')
        if testCharacter + "_clothes_neutralclothes" in items_filtered:
            f.write('            attribute neutralclothes "' + testCharacter + '_clothes_neutralclothes" default\n')
            items_filtered.remove(testCharacter + "_clothes_neutralclothes")
        
        for item in items_filtered:
            att_name = item.split("_")[2]
            f.write('            attribute ' + att_name + ' "' + item + '"\n')
        items.remove("clothes")

    items_filtered = [x.split(".png")[0].split(".webp")[0] for x in file_list if x.split("_")[1] == "brow"]
    if len(items_filtered) > 0: # Using brows.
        f.write('\n        group brow auto:\n')
        if testCharacter + "_brow_neutralbrow" in items_filtered:
            f.write('            attribute neutralbrow "' + testCharacter + '_brow_neutralbrow" default\n')
            items_filtered.remove(testCharacter + "_brow_neutralbrow")
        
        for item in items_filtered:
            att_name = item.split("_")[2]
            f.write('            attribute ' + att_name + ' "' + item + '"\n')
        items.remove("brow")

    items_filtered = [x.split(".png")[0].split(".webp")[0] for x in file_list if x.split("_")[1] == "mouth"]

    f.write('\n        group mouth auto:\n')
    if testCharacter + "_mouth_neutralmouth" in items_filtered:
        f.write('            attribute neutralmouth "' + testCharacter + '_mouth_neutralmouth" default\n')
        items_filtered.remove(testCharacter + '_mouth_neutralmouth')
    else:
        flag_issue = True

if flag_issue:
    narrator "No neutral mouth found."
    $ flag_issue = False

python:
    for item in items_filtered:
        att_name = item.split("_")[2]
        f.write('            attribute ' + att_name + ' "' + item + '"\n')
    items.remove("mouth")

    items_filtered = [x.split(".png")[0].split(".webp")[0] for x in file_list if x.split("_")[1] == "eyes" and not x.split("_")[1] == "eyesparkles"]

    if len(items_filtered) > 0:
        f.write('\n        group eyes auto:\n')
        if testCharacter + "_eyes_neutraleyes" in items_filtered:
            f.write('            attribute neutral "' + testCharacter + '_mouth_neutraleyes" default\n')
            items_filtered.remove(testCharacter + '_eyes_neutraleyes')
        else:
            flag_issue = True

if flag_issue:
    narrator "No neutral eyes found."
    $ flag_issue = False

python:
    if len(items_filtered) > 0:
        for item in items_filtered:
            att_name = item.split("_")[2].split("eyes")[0]
            f.write('            attribute ' + att_name + ' "' + item + '"\n')
        items.remove("eyes")

    if "eyesparkles" in items: # We know this is one of Iusti's. This is likely incomplete.
        items_filtered = [x.split(".png")[0].split(".webp")[0] for x in file_list if "eyesparkles" in x.split("_")[1]]
        print(items_filtered)
        #f.write()
        f.write("\n        group eyesparkles auto:\n")
        f.write('            attribute eyesparkles "' + testCharacter + '_eyesparkles" default\n')
        """items_filtered.remove(char_name_r + '_eyesparkles')

        for item in items_filtered:
            att_name = item.split("_")[2].split("eyesparkles")[0]
            f.write('            attribute ' + att_name + ' "' + item + '"\n')"""
        items.remove("eyesparkles")
        if "eyesparkles2" in items:
            items.remove("eyesparkles2")

    for i in items:
        f.write('\n        group ' + i + ' auto:\n')
        items_filtered = [x.split(".png")[0].split(".webp")[0] for x in file_list if i in x.split("_")[1]]
        for item in items_filtered:
            att_name = item.split("_")[2].split("eyes")[0]
            f.write('            attribute ' + att_name + ' "' + item + '"\n')

    f.close()

narrator "portraits code has been autogenerated for character. You will find the text file in the folder you launched the game."
narrator "You will need to put it in the portraits.rpy file (or elsewhere), and reload the game."

