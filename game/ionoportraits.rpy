init:
    layeredimage ionojustteal:
        zoom 0.5
        xalign 0.5
        yanchor 0.65
        ypos 1.0

        group expressions:
            attribute surprised "iono_teal_front7_surprisedteal7"
            attribute closed "iono_teal_down_closedteal5"
            attribute happy2 "iono_teal_down_happyteal3"
            attribute impressed "iono_teal_down_impressedteal3"
            attribute neutral "iono_teal_down_neutralteal2"
            attribute angry "iono_teal_front_angryteal4"
            attribute happy "iono_teal_front_happyteal1"
            attribute sad "iono_teal_front_sadteal6"
            attribute smug "iono_teal_front_smugteal1"

    layeredimage ionojustpink:
        zoom 0.5
        xalign 0.5
        yanchor 0.65
        ypos 1.0

        group expressions:
            attribute angry "iono_pink_down_angrypink4"
            attribute happy "iono_pink_down_happypink1"
            attribute sad "iono_pink_down_sadpink6"
            attribute smug "iono_pink_down_smugpink1"
            attribute closed "iono_pink_front_closedpink5"
            attribute happy2 "iono_pink_front_happypink3"
            attribute neutral "iono_pink_front_neutralpink2"
            attribute impressed "iono_pink_front_impressedpink3"

    layeredimage iono:
        zoom 0.5
        xalign 0.5
        yanchor 0.65
        ypos 1.0

        group pink variant "down" auto:
            attribute nomagnemite null

        group teal variant "down" auto:
            attribute nomagnemite null

        group downmagnemiteshadow5 auto if_all ["body5"] if_not ["nomagnemite"]
        
        group downmagnemiteblush1 auto if_all ["body1"] if_not ["nomagnemite"]

        group body auto:
            attribute nobody null
            attribute neutralpose null
            attribute sneaky null
            attribute happy null
            attribute angry null
            attribute thinking null
            attribute sad null
            attribute surprised null

        group blush1 auto if_all ["body1"] 
        group blush7 auto if_all ["body7"] 

        always "iono_over7_bodyhand" if_all ["body7"] if_not ["uniform"]

        group shadow4 auto if_all "body4"
        group shadow5 auto if_all "body5"
        group shadow7 auto if_all "body7"

        group eyebrow1 auto if_all "body1" if_not "nobody"
        group eyebrow2 auto if_all "body2" if_not "nobody"
        group eyebrow3 auto if_all "body3" if_not "nobody":
            attribute winkeyebrow "iono_eyebrow3_happyeyebrow"
            attribute sadeyebrow "iono_eyebrow3_teeheeeyebrow"
        group eyebrow4 auto if_all "body4" if_not "nobody"
        group eyebrow5 auto if_all "body5" if_not "nobody":
            attribute angryeyebrow "iono_eyebrow5_concentratedeyebrow"
            attribute closedeyebrow "iono_eyebrow5_calmeyebrow"
        group eyebrow6 auto if_all "body6" if_not "nobody":
            attribute sadeyebrow "iono_eyebrow6_sigheyebrow"
        group eyebrow7 auto if_all "body7" if_not "nobody"

        group hair1 auto if_all "body1" if_not "nobody":
            attribute twintail default
        group hair2 auto if_all "body2" if_not "nobody":
            attribute twintail default
        group hair3 auto if_all "body3" if_not "nobody":
            attribute twintail default
        group hair4 auto if_all "body4" if_not "nobody":
            attribute twintail default
        group hair5 auto if_all "body5" if_not "nobody":
            attribute twintail default
        group hair6 auto if_all "body6" if_not "nobody":
            attribute twintail default
        group hair7 auto if_all "body7" if_not "nobody":
            attribute twintail default

        group mouth1 auto if_all "body1" if_not "nobody":
            attribute talkingmouth "iono_mouth1_smugmouth"
            attribute talking2mouth "iono_mouth1_uneasymouth"
            attribute happymouth "iono_mouth1_grinmouth"
            attribute sadmouth "iono_mouth1_uneasymouth"
            attribute frownmouth "iono_mouth1_embarrassedmouth"
            attribute smilemouth "iono_mouth2_catmouth"

        group mouth2 auto if_all "body2" if_not "nobody":
            attribute talkingmouth "iono_mouth2_talkingmouth"
            attribute talking2mouth "iono_mouth2_talking2mouth"
            attribute happymouth "iono_mouth2_talkingmouth"
            attribute sadmouth "iono_mouth2_disappointedmouth"
            attribute frownmouth "iono_mouth2_disappointedmouth"
            attribute smilemouth "iono_mouth2_neutralmouth"

        group mouth3 auto if_all "body3" if_not "nobody":
            attribute happymouth default
            attribute talkingmouth "iono_mouth3_happymouth"
            attribute talking2mouth "iono_mouth3_impressedmouth"
            attribute happymouth "iono_mouth3_happymouth"
            attribute sadmouth "iono_mouth3_impressedmouth"
            attribute frownmouth "iono_mouth3_impressedmouth"
            attribute smilemouth "iono_mouth3_teeheemouth"

        group mouth4 auto if_all "body4" if_not "nobody":
            attribute angrymouth default
            attribute talkingmouth "iono_mouth4_battlemouth"
            attribute talking2mouth "iono_mouth4_angrymouth"
            attribute happymouth "iono_mouth4_battlemouth"
            attribute sadmouth "iono_mouth4_angrymouth"
            attribute frownmouth "iono_mouth4_poutmouth"
            attribute smilemouth "iono_mouth4_challengemouth"

        group mouth5 auto if_all "body5" if_not "nobody":
            attribute frownmouth default
            attribute talkingmouth "iono_mouth5_confusedmouth"
            attribute talking2mouth "iono_mouth5_scaredmouth"
            attribute happymouth "iono_mouth5_talkingmouth"
            attribute sadmouth "iono_mouth5_scaredmouth"
            attribute frownmouth "iono_mouth5_frownmouth"
            attribute smilemouth "iono_mouth5_bravemouthmouth"
            
        group mouth6 auto if_all "body6" if_not "nobody":
            attribute talkingmouth "iono_mouth6_defeatmouth"
            attribute talking2mouth "iono_mouth6_defeatmouth"
            attribute happymouth "iono_mouth6_defeatmouth"
            attribute sadmouth "iono_mouth6_sadmouth"
            attribute frownmouth "iono_mouth6_helplessmouth"
            attribute smilemouth "iono_mouth6_helplessmouth"

        group mouth7 auto if_all "body7" if_not "nobody":
            attribute surprisedmouth default

        group eyes1 auto if_all "body1" if_not "nobody"
        group eyes2 auto if_all "body2" if_not "nobody"
        group eyes3 auto if_all "body3" if_not "nobody"
        group eyes4 auto if_all "body4" if_not "nobody"
        group eyes5 auto if_all "body5" if_not "nobody":
            attribute worriedeyes "iono_eyes5_confusedeyes"
        group eyes6 auto if_all "body6" if_not "nobody"
        group eyes7 auto if_all "body7" if_not "nobody"

        always "iono_over1_eyepony" if_all ["body1", "ponytail"]

        always "iono_over2_eyepony" if_all ["body2", "ponytail"]

        always "iono_over3_eyepony" if_all ["body3", "ponytail"]

        always "iono_over6_eyepony" if_all ["body6", "ponytail"]
        always "iono_over6_eyetwin" if_all ["body6", "twintail"]


        group cloth1 auto if_all "body1" if_not "nobody":
            attribute stream default
        group cloth2 auto if_all "body2" if_not "nobody":
            attribute stream default
        group cloth3 auto if_all "body3" if_not "nobody":
            attribute stream default
        group cloth4 auto if_all "body4" if_not "nobody":
            attribute stream default
        group cloth5 auto if_all "body5" if_not "nobody":
            attribute stream default
        group cloth6 auto if_all "body6" if_not "nobody":
            attribute stream default
        group cloth7 auto if_all "body7" if_not "nobody":
            attribute stream default

        always "iono_over1_clothbikinitwin" if_all ["body1", "bikini", "twintail"]
        always "iono_over1_clothpony" if_all ["body1", "ponytail"]
        always "iono_over1_clothuniformtwin" if_all ["body1", "stream", "twintail"]
        always "iono_over1_clothuniformtwin" if_all ["body1", "uniform", "twintail"]

        always "iono_over3_clothpony" if_all ["body3", "ponytail"]
        always "iono_over3_clothtwin" if_all ["body3", "twintail"]

        always "iono_over4_clothpony" if_all ["body4", "ponytail"]

        always "iono_over5_clothpony" if_all ["body5", "ponytail"]
        
        always "iono_over6_clothpony" if_all ["body6", "ponytail"]
        always "iono_over6_clothtwin" if_all ["body6", "twintail"]

        always "iono_over7_clothpony" if_all ["body7", "ponytail"]

        group pink variant "front" auto:
            attribute nomagnemite null

        group teal variant "front" auto:
            attribute nomagnemite null

        group frontmagnemiteshadow5 auto if_all ["body5"] if_not ["nomagnemite"]

        group frontmagnemiteblush1 auto if_all ["body1"] if_not ["nomagnemite"]

        always "iono_over3_magnemitehand" if_all ["body3"] if_not ["stream", "uniform"]

        group coat1 auto if_all "body1" if_any ["stream", "uniform"]:
            attribute coat default
            attribute nocoat null
        group coat2 auto if_all "body2" if_any ["stream", "uniform"]:
            attribute coat default
            attribute nocoat null
        group coat3 auto if_all "body3" if_any ["stream", "uniform"]:
            attribute coat default
            attribute nocoat null
        group coat4 auto if_all "body4" if_any ["stream", "uniform"]:
            attribute coat default
            attribute nocoat null
        group coat5 auto if_all "body5" if_any ["stream", "uniform"]:
            attribute coat default
            attribute nocoat null
        group coat6 auto if_all "body6" if_any ["stream", "uniform"]:
            attribute coat default
            attribute nocoat null
        group coat7 auto if_all "body7" if_any ["stream", "uniform"]:
            attribute coat default
            attribute nocoat null

        always "iono_over1_coatstream" if_all ["body1", "stream", "coat"]
        always "iono_over1_coatuniform" if_all ["body1", "uniform", "coat"]

        always "iono_over2_coatstream" if_all ["body2", "stream", "coat"]
        always "iono_over2_coatuniform" if_all ["body2", "uniform", "coat"]

        always "iono_over3_coatstream" if_all ["body3", "stream", "coat"]
        always "iono_over3_coatuniform" if_all ["body3", "uniform", "coat"]

        always "iono_over4_coatstream" if_all ["body4", "stream", "coat"]
        always "iono_over4_coatuniform" if_all ["body4", "uniform", "coat"]

        always "iono_over5_coatstream" if_all ["body5", "stream", "coat"]
        always "iono_over5_coatuniform" if_all ["body5", "uniform", "coat"]
        
        always "iono_over6_coatstream" if_all ["body6", "stream", "coat"]
        always "iono_over6_coatuniform" if_all ["body6", "uniform", "coat"]
        
        always "iono_over7_coatstream" if_all ["body7", "stream", "coat"]
        always "iono_over7_coatuniform" if_all ["body7", "uniform", "coat"]

        #-----------------------------------------------------------

        always "iono_over1_overcoatstreampony" if_all ["body1", "stream", "ponytail", "coat"]
        always "iono_over1_overcoattwin" if_all ["body1", "twintail", "coat"]
        always "iono_over1_overcoatuniformpony" if_all ["body1", "uniform", "ponytail", "coat"]

        always "iono_over2_overcoatpony" if_all ["body2", "ponytail", "coat"]
        always "iono_over2_overcoattwin" if_all ["body2", "twintail", "coat"]

        always "iono_over3_overcoatpony" if_all ["body3", "ponytail", "coat"]
        always "iono_over3_overcoattwin" if_all ["body3", "twintail", "coat"]

        always "iono_over4_overcoatpony" if_all ["body4", "ponytail", "coat"]
        always "iono_over4_overcoattwin" if_all ["body4", "twintail", "coat"]
        
        always "iono_over5_overcoatpony" if_all ["body5", "ponytail", "coat"]
        always "iono_over5_overcoattwin" if_all ["body5", "twintail", "coat"]
        
        always "iono_over6_overcoatpony" if_all ["body6", "ponytail", "coat"]
        always "iono_over6_overcoattwin" if_all ["body6", "twintail", "coat"]
        
        always "iono_over7_overcoatpony" if_all ["body7", "ponytail", "coat"]
        always "iono_over7_overcoattwin" if_all ["body7", "twintail", "coat"]

        group pink variant "front7" auto:
            attribute nomagnemite null

        group teal variant "front7" auto:
            attribute nomagnemite null

        group leftmagnemiteblush7 auto if_all ["body7"] if_not ["nomagnemite"]
        
        group rightmagnemiteblush7 auto if_all ["body7"] if_not ["nomagnemite"]

        group anger4 auto if_all "body4"

        group rotombody auto:
            attribute norotom null

        group rotombrow auto

        group rotommouth auto

    image side iono = LayeredImageProxy("iono", Transform(xpos=0.08, yanchor=0.55))

init python:
    lastionoattributes = []
    ionobodyassociations = { }

    for asset in os.scandir(os.path.join(config.searchpath[0], "images", "expressions", "iono")):
        bodystring = asset.name
        if ("eyebrow" in bodystring or "eyes" in bodystring or "mouth" in bodystring and bodystring):
            match = re.search(r'\d+', bodystring)
            if match:
                bodytype = "body" + match.group()
            else:
                continue
            parts = bodystring.split('_', 2)
            if len(parts) > 2:
                ionobodyassociations[parts[2][:-5]] = bodytype

    def find_string_with_any_substring(strings, substrings):
        """
        Scans a list of strings and returns the first string that contains any of the provided substrings.
        If substrings is a single string, it checks for that string. 
        Returns None if no such string exists.

        :param strings: List of strings to scan.
        :param substrings: A single string or a list of substrings to search for.
        :return: The first string containing any of the substrings, or None.
        """
        # Ensure substrings is a list for consistent processing
        if isinstance(substrings, str):
            substrings = [substrings]

        for string in strings:
            if any(substring in string for substring in substrings):
                return string
        return None

    def iono_adjuster(names):
        global lastionoattributes

        atts = list(names[1:])
        getattributescall = renpy.get_attributes("iono")
        oldatts = (list(getattributescall) if getattributescall != None else [])

        bodystring = True
        while (bodystring):
            bodystring = find_string_with_any_substring(atts, "body")
            if (bodystring == "nobody"):
                break
            if (bodystring in atts):
                atts.remove(bodystring)

        skipbodyassignment = True
        if ("sneaky" in atts):
            atts.remove("sneaky")
            atts.append("body1")
        elif ("neutralpose" in atts):
            atts.remove("neutralpose")
            atts.append("body2")
        elif ("happy" in atts):
            atts.remove("happy")
            atts.append("body3")
        elif ("angry" in atts):
            atts.remove("angry")
            atts.append("body4")
        elif ("thinking" in atts):
            atts.remove("thinking")
            atts.append("body5")
        elif ("sad" in atts):
            atts.remove("sad")
            atts.append("body6")
        elif ("surprised" in atts):
            atts.remove("surprised")
            atts.append("body7")
        elif ("nobody" not in atts):
            skipbodyassignment = False

        splitbrows = []
        fixbrows = []
        for att in atts:
            if (att.endswith("brow") and not att.endswith("eyebrow")):
                splitbrows.append(att)
            elif (att.endswith("eyebrows")):
                fixbrows.append(att)
        for att in fixbrows:
            atts.remove(att)
            atts.insert(0, att[:-1])
        for att in splitbrows:
            atts.remove(att)
            atts.insert(0, att[:-4] + "eyes")
            atts.insert(0, att[:-4] + "eyebrow")

        allatts = atts + oldatts

        clothstring = find_string_with_any_substring(allatts, ["stream", "bikini", "uniform"])
        hairstring = find_string_with_any_substring(allatts, ["twintail", "ponytail"])
        coatstring = find_string_with_any_substring(allatts, "coat")
        pinkstring = find_string_with_any_substring(atts, "pink")
        if (pinkstring == None and "nomagnemite" in atts):
            pinkstring = "nomagnemite"
        tealstring = find_string_with_any_substring(atts, "teal")
        if (tealstring == None and "nomagnemite" in atts):
            tealstring = "nomagnemite"
        mouthstring = find_string_with_any_substring(atts, "mouth")
        eyestring = find_string_with_any_substring(atts, "eyes")
        eyebrowstring = find_string_with_any_substring(atts, "eyebrow")

        
        if (eyestring == "impressedeyes" and pinkstring == tealstring == None):
            pinkstring = "impressedpink3"
            tealstring = "impressedteal3"
            atts.append("impressedpink3")
            atts.append("impressedteal3")

        if (not skipbodyassignment):
            bodystring = None
            firstmover = None
            for att in atts:
                if (att in ionobodyassociations):
                    if (firstmover == None):
                        firstmover = att
                    #if (bodystring != None and bodystring != ionobodyassociations[att]):
                    #    renpy.notify("iono asset conflict: " + att + " is associated with " + bodystring + ", but " + firstmover + " is associated with " + ionobodyassociations[att])
                    #    print("iono asset conflict: " + att + " is associated with " + bodystring + ", but " + firstmover + " is associated with " + ionobodyassociations[att])
                    bodystring = ionobodyassociations[att]
                    break
            
            if (bodystring == None):
                bodystring = "body2"

            #print("auto-setting body " + bodystring)
            secondbodystring = True
            while (secondbodystring):
                secondbodystring = find_string_with_any_substring(atts, "body")
                if (secondbodystring in atts):
                    atts.remove(secondbodystring)
            atts.append(bodystring)

        if (clothstring == None):
            atts.append("stream")

        if (hairstring == None):
            atts.append("twintail")

        if (coatstring == None):
            atts.append("coat")

        if (pinkstring == None):
            body_to_pink = {
                "body1": "happypink1",
                "body2": "neutralpink2",
                "body3": "happypink3",
                "body4": "angrypink4",
                "body5": "closedpink5",
                "body6": "sadpink6",
                "body7": "surprisedpink7",
            }
            
            for body, pink in body_to_pink.items():
                if body in atts:
                    atts.append(pink)
                    break

        if (tealstring == None):
            body_to_teal = {
                "body1": "happyteal1",
                "body2": "neutralteal2",
                "body3": "happyteal3",
                "body4": "angryteal4",
                "body5": "closedteal5",
                "body6": "sadteal6",
                "body7": "surprisedteal7",
            }
            
            for body, teal in body_to_teal.items():
                if body in atts:
                    atts.append(teal)
                    break

        if mouthstring == None:
            body_to_mouth = {
                "body1": "catmouth",
                "body2": "neutralmouth",
                "body3": "happymouth",
                "body4": "angrymouth",
                "body5": "frownmouth",
                "body6": "sadmouth",
                "body7": "surprisedmouth",
            }
            
            for body, mouth in body_to_mouth.items():
                if body in atts:
                    atts.append(mouth)
                    break

        if eyestring == None:
            body_to_eyes = {
                "body1": "grineyes",
                "body2": "neutraleyes",
                "body3": "happyeyes",
                "body4": "angryeyes",
                "body5": "closedeyes",
                "body6": "sadeyes",
                "body7": "surprisedeyes",
            }
            
            for body, eyes in body_to_eyes.items():
                if body in atts:
                    atts.append(eyes)
                    break

        if eyebrowstring == None:
            body_to_eyebrow = {
                "body1": "grineyebrow",
                "body2": "neutraleyebrow",
                "body3": "happyeyebrow",
                "body4": "annoyedeyebrow",
                "body5": "calmeyebrow",
                "body6": "sigheyebrow",
                "body7": "surprisedeyebrow",
            }
            
            for body, eyebrow in body_to_eyebrow.items():
                if body in atts:
                    atts.append(eyebrow)
                    break 

        #print(atts)

        lastionoattributes = copy.copy(atts)
        #print(lastionoattributes)

        return names[0], *atts

define config.adjust_attributes["iono"] = iono_adjuster