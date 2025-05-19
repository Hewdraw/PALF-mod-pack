init python:
    def GetDialog(speaker):
        if (speaker == "Leaf"):
            if (IsBefore(5, 5, 2004)):
                if (HasEvent("Leaf", "RejectedConfession")):
                    return "hey, [first_name]. still hitting me up late at night? knew you couldnt leave me"
                elif (HasEvent("Leaf", "AcceptedConfession")):
                    return "looking forward to our date! i hope youre ready for my date outfit. might be a bit too scandalous, but idc. ;3"
                else:
                    return "hitting me up late at night? ;3 im onto you."
            else:
                if (GetMood("Leaf") < 0):
                    return "you could just yell, you know. im right here."
                else:
                    if (HasEvent("Leaf", "RejectedConfession")):
                        return "dude, what? im literally outside your room. i think u might be a tiny bit obsessive, ngl.\njk"
                    elif (HasEvent("Leaf", "AcceptedConfession")):
                        return "dude, what? im literally outside your room. i think u might be a tiny bit obsessive, ngl.\n(xox)"
        elif (speaker == "Serena"):
            if (IsBefore(5, 5, 2004)):
                if (GetRelationship("Serena") == "Conspirator"):
                    return "Oh, delightful. You've come to update me on your mission regarding Calem, yes? Please, do tell."
                else:
                    return "What a splendid surprise. To what do I owe this pleasure?"
            else:
                if (GetMood("Serena") < 0):
                    return "Apologies, I don't think I can be very entertaining right now."
                else:
                    return "What a splendid surprise. To what do I owe this pleasure?"
        elif (speaker == "Calem"):
            if (IsBefore(5, 5, 2004)):
                return "Why are you texting me, [first_name]?\nI'm literally right here."
            else:
                if (GetMood("Calem") < 0):
                    return "[first_name]. I'm very sorry to say this, but I can't spend too much time talking. Serena is trying to discuss something."
                else:
                    return "[first_name]. Good to hear from you. This reminds me of when we were roommates."
        elif (speaker == "Brendan"):
            if (IsBefore(5, 5, 2004)):
                return "BRO YOUR TEXTNG ME WHILE WERE IN THE SAME ROOM??? WACK"
            else:
                if (GetMood("Brendan") < 0):
                    return "NGL DUDE BAD TIME. TALK LATER???"
                else:
                    return "HEY BRO LONG TIME NO TALK MAYBE. I DONT REMEMBER"
        elif (speaker == "May"):
            lowername = first_name.lower()
            if (IsBefore(5, 5, 2004)):
                return "{}? its pretty late. whats up???".format(lowername)
            else:
                if (GetMood("May") < 0):
                    return "sorry, im kinda talking with Brendan right now... mind waiting a bit???"
                else:
                    return "{}? its pretty late. whats up???".format(lowername)
        elif (speaker == "Nate"):
            if (IsBefore(5, 5, 2004)):
                return "Heya, {}! It's past 2200! L8 to bed 2nite? Just touching base?".format(nate_name)
            else:
                if (GetRelationshipRank("Nate") > 0):
                    return "{}, we shouldn't talk 2 much on civvy lines. There's basically no encryption here.".format(nate_name)
                else:
                    if (GetMood("Nate") < 0):
                        return "{}, sorry, don't really have time 2 talk rn. Got some stuff 2do. Catch u l8r?".format(nate_name)
                    else:
                        return "Heya, {}! It's past 2200! L8 to bed 2nite? Just touching base?".format(nate_name)    
        elif (speaker == "Nessa"):#Nessa is not affected by mood at night
            if (GetRelationship("Nessa") == "Good Friend"):
                return "hi, [first_name]. kinda sleepy. still good to hear from you, tho. got anything you wanna talk about, or just listen to me whine?"
            elif (GetRelationship("Nessa") == "Friend"):
                return "hi, [first_name]. pretty late. should let you know i dont give out 'spicy' texts before the second date, but if you just wanna chat, im down."
            else:
                return "sorry, i dont text before the first date. hurry up and take me out, k?"
        elif (speaker == "Sabrina"):
            if (IsBefore(5, 5, 2004)):
                return "It's nice to hear from you again. How was your day?"
            else:
                if (GetMood("Sabrina") < 0):
                    return "...I asked to be left alone."
                else:
                    return "...Hello."
        elif (speaker == "Blue"):
            if (IsBefore(5, 5, 2004)):
                return "wat the hel's your PROLBEM? I was IN THE MIDLDE of trainin! you were probly gonna BEG me for tips, huh? tough! ill BLOKC this number!\n*PROBLEM"
            else:
                return "I'm in the other goddamn room, you idiot! Just {i}yell!{/i}"
        elif (speaker == "Hilda"):
            if (GetRelationshipRank("Hilda") > 1):
                if (GetMood("Hilda") < 0):
                    return "Busy as hell right now. Not much time; what's up?"
                else:
                    return "Got to get some running in today. Almost as good as riding my old bike. Miss that thing."
            else:
                if (GetMood("Hilda") < 0 or GetRelationshipRank("Hilda") == 0):
                    return "orz, bz. ttyl, k?"
                else:
                    return "So, got some free time. Thanks to you. But you better quit that spit! I can handle myself!\n*shit!"
        elif (speaker == "Misty"):#always moody
            if (GetRelationshipRank("Misty") > 1):
                if (GetMood("Misty") > 0):
                    return "hi. whatre you doing up so late? not that i care. jsut wondering.\n*just"
                else:
                    return "you woke me up. this better be good"
            else:
                return "yeah so i kinda just want to be left alone rn.\ni guess we can text, but don't send/ask for any pics, perv."
        elif (speaker == "Bea"):#always stoic
            if (GetRelationshipRank("Bea") > 0):
                if (GetRelationshipRank("Bea") > 1):
                    return "{cps=15}'Lo.{w=1.0} I have been training hard.{w=1.0} You should too.{w=1.0} We need to be prepared for what's about to come.{/cps}"
                else:
                    return "{cps=15}'Lo.{w=1.0} I followed another one of your plans today.{w=1.0} It went well.{w=1.0} I am most grateful.{/cps}"
            else:
                return "{cps=15}Hi.{w=1.0} How are you?{w=1.0} What do you mean, {w=1.0}I text slowly?{/cps}"
        elif (speaker == "Bianca"):#always cheerful
            if (GetMood("Bianca") < 0 or (IsAfter(17, 5, 2004) and IsBefore(21, 5, 2004))):
                return "...hii. Im sorry, Im a bit sleepy. I think Im going to bed early."
            else:
                if (IsWeekend()):
                    return "hiiii!!!~ how was your day??? today was so fun for me!!! I went out into the fields---oh but i had breakfast first, and then i went to class,,, and---"
                else:
                    return "hiiii!!!~ how was your day??? today was so fun for me!!! I got up and then went to class---oh but i had breakfast first, and then i went to class,,, and---"
        elif (speaker == "Gardenia"):#always business
            return "What're you looking for? Big deals? Massive savings? Hot singles in your area? I got it all!\nOh, just to chat? Sure, I can do that, too!"
        elif (speaker == "Whitney"):
            if (GetMood("Whitney") < 0):
                return "<U_U> Kinda in a bad mood rn... don't want to talk about it..."
            else:
                return "Heya! ^U^ What's up? You'll never believe what I just heard. O_O"
        elif (speaker == "Flannery"):
            if (IsDate(18, 5, 2004) or IsDate(19, 5, 2004)):
                return "Hey! I'm going to bed early. Don't want to be all tired for Doc Cherry's test, you know? You should go to bed too!"
            elif (GetMood("Flannery") < 0):
                return "im not doing super great. mind if we talk later? probably not tomorrow morning, though..."
            else:
                return "Hey, man! You're up late! Don't stay up too-- what, me? Hey, I'm going to bed in a few hours!"
        elif (speaker == "Wally"):
            if (GetMood("Wally") < 0):
                return "Hi, [wally_name]. I'm studying. And I'm a bit tired from training earlier. Will this take long?"
            else:
                return "Hi, [wally_name]. What are you doing? Did you study anything great recently? And, um, do you have any more tips for me?"
        elif (speaker == "Raihan"):
            if (GetMood("Raihan") < 0):
                return "Sorry, mate. Just got off the phone with Rose. Not up for it right now."
            else:
                return "[last_name]! How are ya? What've you got for me?"
        elif (speaker == "Dawn"):
            if (GetMood("Dawn") < 0):
                return "asdfghjkl ur calling me now sry sry sry cant talk cant talk cant talk!!!!"
            else:
                return "hi hi hi!! whats up!! how are you!! how have you been doing!! i wasnt sleeping!! we can talk!! if you still want to!! no worries if not!! i can hang up!!"
        elif (speaker == "Hilbert"):
            if (GetMood("Hilbert") < 0):
                return "I do not want to talk. Goodnight."
            else:
                return "I have rounded another corner in my mission. The sword of justice draws ever closer to its target.\n...No, I'm not being dramatic. Be quiet."
        elif (speaker == "Grusha"):
            if (GetMood("Grusha") < 0):
                return "been a bad day, amigo. need some space. little prince is doing fine"
            else:
                return "how've you been, amigo? little prince is doing fine. thought i saw him rocking--probably just a trick of the light"
        elif (speaker == "Jasmine"):
            if (GetMood("Jasmine") < 0):
                return "I'm sorry. Not right now. I'm too tired. I'll talk"
            else:
                return "Good evening, [first_name]! Work continues in earnest on the Ironsides case. I'll let you know immediately if I get any leads!"
        elif (speaker == "Skyla"):
            if (HasEvent("Skyla", "Skyla2")):
                if (GetMood("Skyla") < 0 and GetRelationshipRank("Skyla") >= 2):
                    return "Talking with WES!!! Need to focus on MISSIONS!!! Talk LATER???!!!"
                else:
                    return "Don't tell WES I kept my PHONE!!! I just wanted to be able to CHAT with YOU!!!"
            else:
                if (GetMood("Skyla") < 0):
                    return "Marathoning Pokémon Rangers and eating ICE CREAM!!! This is GREAT!!! I am doing FINE!!!"
                else:
                    return "Hey, [GetRelationship('Skyla')]!!! Got any spicy MISSIONS for us???!!!"
        elif (speaker == "Silver"):
            if (GetMood("Silver") < 0):
                return "✔️✔️ Read"
            else:
                return "gd 2 her frm u. no updts. jst wnt 2 tlk? fn, fine. How was your day, or whatever?"
        else:
            return "THIS IS AN ERROR. PLEASE SCREENSHOT THIS AND REPORT ON THE DISCORD. [speaker], [calDate], [GetRelationshipRank(speaker)], [GetMood(speaker)]"

label texting():

$ texted = False
$ texting = True

call clearscreens() from _call_clearscreens_176
if (IsBefore(5, 5, 2004)):
    scene dorm_B norm with Dissolve(2.0)
else:
    scene bedroommidnight with Dissolve(2.0)
    
stop music fadeout 2.5

queue music "Audio/Music/Road to Viridian City.ogg"

if (IsBefore(5, 5, 2004)):
    redmind hatless casual "...I should text someone before I head to bed."
else:
    redmind hatless casual night "...I should text someone before I head to bed."

label afterroomsetuptexting():

show phone_B behind blank2
show phone_A behind blank2
with fadeinbottom

if (not skiptextingscenes):
    $ textingscenetriggered = True
    call textingscenequeue() from _call_textingscenequeue
else:
    $ textingscenetriggered = False

if (not textingscenetriggered):
    call screen database(calling=True, _with_none=False) with Dissolve(1.0)
    with dissolve

    $ interaction = _return
    $ hasevent = []
    $ cancelmessage = "You don't want to text anyone? Going to sleep early will confer no benefit right now."

    if (HasEvent("Grusha", "Scene1Part1") and GetRelationshipRank("Grusha") < 1 and IsPresent("Grusha", ignoreabsences=True)):
        $ hasevent.append("GrushaScene1Part2")
    if (HasEvent("Skyla", "Skyla2") and GetRelationshipRank("Skyla") < 2 and IsPresent("Skyla")):
        $ hasevent.append("Skyla2Part2")
        
    if (hasevent):    
        $ cancelmessage = "You don't want to text anyone? There are other events that you could engage in right now."

    if (interaction == "Back"):
        narrator "[cancelmessage]"

        menu:
            "Yes, just go to sleep." if (not hasevent):
                pass
            
            "Yes, I want to check on Grusha." if ("GrushaScene1Part2" in hasevent):
                jump Grusha1Part2

            "Yes, I want to go with Skyla into the city." if ("Skyla2Part2" in hasevent):
                jump Skyla2Part2

            "No, I want to text someone.":
                jump texting

    elif (IsAbsent(interaction)):
        narrator "[ellipses]"
        narrator "No response. Seems [('he' if persondex[interaction]['Sex'] == Genders.Male else 'she')]'s otherwise occupied."

        jump texting

    elif (interaction == "Klara" and GetRelationshipRank("Klara") == 0):
        show klara behind phone_A with fadeinbottom 

        klara @happy "Hiiiiiiiiiiiii! I can't really sleep. What about you? Want to go out somewhere?"
        klara @restrainedbrow happymouth "Maybe somewhere new? Somewhere... {i}really{/i} fun?"
        klara @happy "Like, I'm totally down right now. C'mon! Let's make it a date."
        klara puppybrow talkingmouth "Please?"

        menu:
            ">Accept her offer":
                klara @happy "That's great! I'll meet you in front of Relic Hall!"

                scene blank2 with splitfade

                call Klara1 from _call_Klara1

            ">Deny her plaintive plea":
                klara sad "Oh... okay..."

                hide klara with dis

                jump texting

    elif (interaction == "Misty" and GetRelationshipRank("Misty") < 2 and HasEvent("Misty", "Scene2Part1")):
        $ texted = True
        call Misty2Part2() from _call_Misty2Part2        

    else:
        if (interaction != "Sabrina"):
            $ interactionsprite = GetCharacterSprite(interaction, overridemood=min(GetMood(interaction), 0))
            if (interaction == "Professor Cherry"):
                $ interactionsprite = "kris"
            
            $ transforms = [flattener(interactionsprite), Transform(zoom=0.8, ypos=0.95)]
            if (interaction == "Raihan"):
                $ transforms.append(Transform(zoom=0.8, xalign=0.5, ypos=0.85))
            elif (interaction == "Nessa"):
                $ transforms.append(Transform(xalign=0.48))
            elif (interaction == "Skyla"):
                $ transforms.append(Transform(xalign=0.55))
            
            $ renpy.transition(dis)
            $ renpy.show(interactionsprite, at_list=transforms, behind=["phone_A"])

            narrator "You want to text [interaction]?"

            menu:
                "Yes, text [interaction].":
                    if (interaction in ["Blue", "Leaf", "Yellow", "Ethan"] and (IsDate(10, 5, 2004) or IsDate(31, 5, 2004))
                        or interaction == "Leaf" and IsAfter(4, 6, 2004) and IsBefore(12, 6, 2004)):
                        
                        narrator "You do not get a response, though you hear a phone go off in the other room."

                        jump texting

                    elif (interaction == "Blue" and not IsBefore(1, 5, 2004)):
                        pause 1.0

                        narrator "Silence, at first, and then..."

                        show bedroommidnight with vpunch

                        blue night @angry "I'm in the other goddamn room, you idiot! Just yell!"

                        $ ValueChange(interaction, 1, 0.5)

                        if (IsDate(6, 5, 2004)):
                            narrator "You spent some time yelling at Blue, but then..."

                        else:
                            narrator "You spent some time yelling at [interaction] before drifting off to sleep."

                        call clearscreens from _call_clearscreens_84

                        hide phone_A
                        hide phone_B
                        hide phone_C
                        $ renpy.hide(interactionsprite)
                        with dis

                    else:
                        $ texted = True
                        $ renpy.show(GetCharacterSprite(interaction))

                        red @happy "Just thought I'd text. How're you doing?"

                        python:
                            if (interaction == "Klara"):
                                renpy.say(None, "Klara's response is not one that can be recounted in any manner approximating decent. Though it {i}is{/i} enjoyable, by most metrics.")
                            else:
                                renpy.say("{color=" + GetCharColor(interaction) + "}" + interaction, GetDialog(interaction))
                            
                            ValueChange(interaction, 1, 0.5)

                        if (IsDate(6, 5, 2004) or IsDate(18, 5, 2004)):
                            narrator "You spent some time texting [interaction], but then..."

                        else:
                            narrator "You spent some time texting [interaction] before drifting off to sleep."

                        hide phone_A
                        hide phone_B
                        hide phone_C
                        $ renpy.hide(interactionsprite)
                        with dis

                        call clearscreens from _call_clearscreens_52

                "Nevermind.":
                    python:
                        renpy.hide(interactionsprite)
                        renpy.jump("texting")

        else:
            narrator "You want to think about Sabrina?"

            menu:
                "Yes, open your mind to her.":
                    if (IsAfter(1, 5, 2004) and IsBefore(16, 5, 2004) and not rescuedsabrina):
                        narrator "The comforting whisper of Sabrina's telepathy, which you've gotten so used to..."

                        pause 1.0

                        narrator "Is completely absent."

                        jump texting

                    hide phone_B
                    hide phone_A
                    with fadeoutbottom

                    $ dialog = GetDialog("Sabrina")
                    redmind @happy "Just thought I'd check in. How're you doing?"
                    redmind "{color=#600080}[dialog]{/color}"

                    $ ValueChange("Sabrina", 1, 0.5)

                    if (IsDate(18, 5, 2004)):
                        "You spent some time thinking back and forth with Sabrina, but then..."
                    else:
                        narrator "You spent some time thinking back and forth with Sabrina before drifting off to sleep."
                    
                "Nevermind.":
                    python:
                        renpy.hide(interactionsprite)
                        renpy.jump("texting")

    if (not skiptextingscenes):
        call midnightscenequeue from _call_midnightscenequeue

$ skiptextingscenes = False

return