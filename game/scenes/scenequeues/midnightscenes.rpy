label midnightscenequeue:

label Bea2Part2Caller:
    if (GetRelationshipRank("Bea") >= 2 and not HasEvent("Bea", "Bea2Part2") and IsPresent("Bea")):
        call Bea2Part2 from _call_Bea2Part2
        return
    
label Cheren1Caller:
    if (IsAfter(25, 5, 2004) and GetCharacterLevel("Cheren") >= 2 and not HasEvent("Cheren", "Scene1") and IsWeekday() and IsPresent(["Silver", "Skyla", "Brendan", "May", "Sabrina", "Cheren"])):
        call Cheren1 from _call_Cheren1
        return

label Whitney2Part2Caller:
    if (GetRelationshipRank("Flannery") > 1 and GetRelationshipRank("Whitney") > 1 and not HasEvent("Whitney", "Whitney2Part2") and IsPresent(["Flannery", "Whitney"])):
        call Whitney2Part2 from _call_Whitney2Part2
        return

label Calem1Part2Caller:
    if (GetRelationshipRank("Calem") > 0 and not HasEvent("Calem", "Calem1Part2") and IsPresent(["Calem", "Serena"])):
        call Calem1Part2 from _call_Calem1Part2
        return
    
label Silver2Part2Caller:
    if (GetRelationshipRank("Silver") == 2 and not HasEvent("Silver", "Silver2Part2") and IsPresent("Silver") and GetEventDatetime("Silver", "Silver2") + datetime.timedelta(days=7) < calDate and GetCharacterLevel("Silver") >= 6):
        call Silver2Part2 from _call_Silver2Part2
        return

label JasmineGrushaTiaMidnightScene:
    if (GetEventDatetime("Grusha", "Grusha1Part2") + datetime.timedelta(days=7) < calDate and EventAvailable(["Jasmine", "Grusha", "Tia"], "JasmineGrushaTiaMidnightScene", [0, 1, 0])):
        call clearscreens() from _call_clearscreens_273
        scene suitenight 
        show jasmine glasses sleepwear downeyes:
            xpos 0.33 xzoom -1
        show tia surprisedbrow frownmouth sleepwear:
            xpos 0.66
        with Dissolve(2.0)

        jasmine frownmouth @talking2mouth "{gradualsize=20-36}...thus I write these words in steel,{/gradualsize} for anything not set in metal cannot be trusted."

        pause 1.0

        jasmine surprisedbrow frownmouth @talking2mouth "Oh my gosh."

        pause 0.5

        jasmine surprisedbrow frownmouth @surprised "Oh my {i}gosh!{/i}"
        jasmine @happy "It makes sense now! Oh my gosh, {i}that's{/i} what he meant! That's why he wrote in metal! Oh my gosh!"

        show tia happy:
            ypos 1.0 xpos 0.66
            ease 0.2 ypos 1.05
            ease 0.2 ypos 1.0

        pause 0.5

        jasmine @closedbrow talking2mouth "I did {i}not{/i} see that coming. Oh, but in hindsight, it's {i}so{/i} obvious. {i}So{/i} obvious. I can't believe it. He {i}truly{/i} did it again!"

        show tia:
            ypos 1.0 xpos 0.66
            ease 0.2 ypos 1.05
            ease 0.2 ypos 1.0

        pause 0.5

        jasmine @happy "Well, we {i}must{/i} buy the next book, musn't we?"
        jasmine @angrybrow talking2mouth "Why, I'd say I'm quite cross at this author for leaving us on such a cliffhanger!"
        jasmine @closedbrow sweat talking2mouth "Not cross enough to stop reading, though[ellipses]"

        tia "[tiafont]I could fly out to the bookstore now? If I hide myself, no-one will see me.{/font}"

        jasmine @sadbrow talkingmouth "Ah... I'm sorry. I still can't understand. Whitney's been teaching me a bit, but[ellipses]"

        show tia poutmouth sad2eyes with dis

        jasmine @talkingmouth "I'm sure you want to continue reading--I'd like little more than to dash out and get the next book right now--but I'm afraid we fallible humans need to sleep." 
        jasmine @happy sweat "I, {i}especially{/i}, need to."

        show tia frownmouth confusedbrow with dis

        pause 0.5

        jasmine @talking2mouth "Oh? You'd like to try reading again?"

        show tia angrybrow frownmouth with dis:
            ypos 1.0 xpos 0.66
            ease 0.2 ypos 1.05
            ease 0.2 ypos 1.0

        pause 0.5

        show tia -angrybrow -frownmouth with dis

        jasmine @closedbrow talkingmouth "Well, alright. You can borrow the book, but please be careful with it."

        show tia lightblush sad2eyes with dis

        jasmine @sadbrow talkingmouth "If you become frustrated again... um, try not to bite {i}this{/i} one."

        show tia -lightblush -sad2eyes with dis

        pause 0.5

        show tia:
            xpos 0.66
            ease 0.5 xpos 0.4
            pause 0.5
            ease 0.5 xpos 0.75

        pause 2.0

        show tia glasses with gaussdissolve

        narrator "The around Tia shifts, and a pair of glasses forms on her brow--ornamental, of course, and nonfunctional--but crafted in imitation of Jasmine's."
        narrator "Dragon see, dragon do."

        jasmine @sadbrow talking2mouth "Careful. Grusha's not back yet. If he sees you transform before we've managed to tell him about you, it could come as quite a shock."
        jasmine @talkingmouth sadbrow "It doesn't hurt to be too careful, if it costs us nothing."

        show tia poutmouth sad2eyes with dis:
            xpos 0.75
            pause 1.0 
            ease 0.5 xpos 1.2

        pause 2.0

        jasmine closedbrow sweat frownmouth @talking2mouth "{size=30}Although... I suppose it {i}could{/i} cost Tia something. If expressing herself through her illusions is as much a part of her as reading is for me, then, perhaps asking her to[ellipses]{/size}"

        pause 1.0

        show grusha:
            xpos 1.2
            ease 0.5 xpos 0.66

        show jasmine surprisedbrow frownmouth with dis

        grusha "{i}Hola{/i}."
        grusha @confusedbrow "You look like you're trying to shoulder the world again. Heavy thoughts?" 

        jasmine -surprisedbrow -frownmouth -sweat @talkingmouth "Lighter than some others. Today was a good day."

        grusha @happy "{i}Igual{/i}. Since I didn't have to pop my head into the infirmary every five minutes, I took the extra time off to take the Little Prince out for a walk."

        jasmine @talkingmouth "I trust you weren't egg-rolling?"

        grusha @sad2brow "What kind of parent do you think I am? No, I strapped him to the back of a Cyclizar and slapped it on the butt. Little Prince should be three regions away by now."

        jasmine @talking2mouth unamusedbrow "So if I open the door to our bedroom, I'm not going to see it sitting in that bowl of warm water you've put on the dresser."

        grusha @talking2mouth "Absolutely not."

        jasmine @closedbrow talking2mouth "Hm. Well, I was just about to turn in for the night, so[ellipses]"

        grusha @happy "{i}Un momento, por favor.{/i} I need to go throw my pajamas on. And do nothing else, naturally."

        show grusha:
            xpos 0.66
            ease 0.5 xpos -0.2

        pause 1.0

        show jasmine unamusedbrow unamusedmouth with dis

        pause 2.0

        show grusha sleepwear noscarf:
            xpos -0.2 xzoom -1
            ease 0.5 xpos 0.66
            ease 0.5 xzoom 1

        pause 1.0

        grusha @talkingmouth "Right, you were saying something? Oh, did you want to check on the Little Prince?"

        jasmine @closedbrow talkingmouth sweat "No, I trust you."

        pause 1.0

        grusha @sad2eyes talking2mouth "Well, now you're just going to make me feel bad."
        grusha @talkingmouth "Change of topic. Finish that book you were reading?"

        jasmine surprisedbrow frownmouth @talkingmouth "Oh, yes! Right before you came back, actually."

        grusha @talking2mouth "Cool. I bought you the sequel."

        jasmine @surprised "Y-you did?!"

        grusha @talking2mouth sadbrow "Yep. Couple weeks ago, when you picked up {i}Metal Maidens{/i}."

        jasmine -surprisedbrow -frownmouth @talking2mouth "{i}Metal Magic{/i}, but[ellipses] thank you!"
        jasmine @talkingmouth "What's the occasion?"

        grusha @talking2mouth "Eh[ellipses] nothing in particular. I just wanted to get you something nice, and I know you've been really into that book, recently."
        grusha @closedbrow talkingmouth "Heh, with you reading it out loud to Venetia all the time, I started to get a tiny bit invested as well."

        jasmine @talking2mouth "If you want, you can borrow it after Tia's done." 
        
        grusha @confusedbrow talking2mouth "Assuming she doesn't bite through {i}this{/i} book."

        jasmine @sad2brow talking2mouth "She was[ellipses] {i}very{/i} apologetic. It's just hard for her to read, you know[ellipses]"

        grusha @talking2mouth "Jaz, I've met people with dyslexia. I've met people whose eyes hurt from looking at screens. I've never met someone who was so frustrated they were moved to tears by it."
        grusha @sad2eyes talking2mouth "Look, be straight with me. Are you and the other girls hiding something from me? Is this something I'm too male to be privy to? Because, frankly, I think I'm {i}very{/i} close to straddling that line."

        jasmine @sadbrow talking2mouth "Hiding? Well[ellipses] we, um[ellipses] if we {i}were{/i} hiding something, it would be up to Tia to tell you, right?"

        grusha @talking2mouth "Huh. So you are. Kinda surprised. You're not in any danger, are you?"

        jasmine @sadbrow talkingmouth "No, no, definitely not."

        pause 1.0

        show jasmine surprisedbrow frownmouth with dis

        grusha @closedbrow talking2mouth "I'm going to just chalk this up to her being illiterate, then."

        pause 1.0

        jasmine -surprisedbrow @surprisedbrow talking2mouth "That's[ellipses] a possibility."

        grusha @sad2eyes talking2mouth "Mute, illiterate, {i}and{/i} stunted. If Whitney and Flannery didn't exist in this dorm, I'd think Dorm 721 was some kind of dumping ground for genetic failures."
        
        jasmine @talking2mouth "We {i}chose{/i} to dorm together. We even had to get special accommodations for you to dorm with me before the dorms were allowed to be co-ed."

        grusha @closedbrow talkingmouth "Sure, and I'm {i}pretty{/i} sure that was our idea. But all sorts of ideas have been popping into my head recently that I am {i}pretty{/i} sure I didn't think up."

        pause 1.0

        jasmine @talking2mouth "Are you talking about the Little Prince?"

        pause 1.0

        grusha @talking2mouth "I don't even start new book series. I'm {i}that{/i} scared of committing to something I might not be able to finish. And I decided to look after an egg of a {i}really{/i} rare Pokémon? I didn't think of that."
        grusha @closedbrow talkingmouth "I don't remember who, exactly, came up with the idea, but I blame [first_name] for this."

        jasmine @closedbrow talking2mouth "Yes, yes, I know you do. You've muttered his name to yourself quite enough recently."

        grusha @talking2mouth sad2eyes lightblush "Have I? That's embarrassing. I thought my scarf would have muffled that[ellipses]"

        jasmine -frownmouth @talkingmouth "Well, you've been wearing your scarf a lot less, too."

        grusha frownmouth downeyes sadeyebrows "Hmm."

        show jasmine confusedeyebrows with dis

        narrator "Grusha's hand traces the jagged line that unconsciously crawls up his chest, terminating a centimeter above his upper lip. Jasmine's eyebrow raises, asking a silent question."

        pause 1.0

        show jasmine -confusedeyebrows with dis

        grusha -frownmouth -downeyes -sadeyebrows @talking2mouth "Not yet. I still get people coming up to me every couple days asking about the Student Council election. 'Hey, are you the guy who fell off the stage?'"
        grusha @sad2eyes talkingmouth "Never thought I'd be infamous for {i}two{/i} falls. Just my luck that I've survived two, I guess."

        jasmine @talkingmouth "My world is a better place that you have."

        grusha @talking2mouth "Hm. Being part of your world is probably the only reason I did."

        jasmine @talking2mouth "Nonsense. I had nothing to do with your recovery from that first fall. That was your own strong spirit."

        grusha @talking2mouth "Your back was the first thing I saw when I woke up after surgery. I'd say you get a fair amount of credit."
        grusha @talkingmouth "I'm pretty sure I never thanked you for being a nosy busybody and keeping the paparazzi away from me while I recovered, by the way."

        jasmine @talking2mouth angrybrow "Oh, they were so {i}awful!{/i} All of them just trying to get you to say something damning about the race organizers, or[ellipses] or[ellipses] your competition, or[ellipses]"
        jasmine @talking2mouth "I didn't intend to stay there so long, but every time I tried to leave, they'd start to swarm in. I had to physically plant myself in the doorway to stop them from getting past."
        jasmine @closedbrow talkingmouth "After all, no-one's willing to shove aside a 'sick girl.' Hmph. Perhaps they should have."

        grusha @upeyes talking2mouth "Yes, and in classic Jasmine fashion, you overexerted yourself protecting someone else, and ended up collapsing, so then {i}I{/i} was on the hook for watching over you."
        grusha @talking2mouth "Kept me out of my own mind, at least. A bit."

        pause 1.0

        jasmine @talkingmouth "That was years ago. A lot of time."

        grusha @talkingmouth "Every second since has been a miracle."

        pause 0.5

        grusha @closedbrow talkingmouth "Even better, some of them have been {i}enjoyable{/i}."
        grusha @winkeyes sadeyebrows talkingmouth "Sometimes even at the same time you were there."

        jasmine @closedbrow talking2mouth "Oh, you[ellipses] {i}buffoon{/i}."

        grusha @unamusedbrow talkingmouth "Language, Jaz. Little ears around."

        pause 1.0

        grusha @talking2mouth "Speaking of which, you should probably make sure Venetia's not making a meal out of your metals. The sequel's in my bag--I'll give it to you if you help me hook myself up to the machine?"

        jasmine @talking2mouth "I'll see you in a moment, then."

        show jasmine:
            xpos 0.33
            ease 0.5 xpos 1.2

        pause 2.0

        grusha @sad2eyes tired talkingmouth "{size=30}I hope you do. Only takes me a second to drop dead.{/size}"
        grusha @angrybrow tired talking2mouth "{size=30}Of course, [first_name] would say[ellipses]{/size}"

        pause 0.5

        grusha @upeyes angryeyebrows angrymouth "{i}¡Vete!{/i} I did it again."

        show grusha:
            xpos 0.66
            ease 0.5 xpos -0.2

        scene blank2 with splitfade

        narrator "As Grusha argues with you in his head, and Tia tries to conceal the suspiciously beak-shaped marks now adorning Jasmine's copy of {i}Metal Magic{/i}..."

        python:
            ValueChange("Jasmine", 3, 0.25, False)
            ValueChange("Tia", 3, 0.5, False)
            ValueChange("Grusha", 3, 0.75)

        narrator "Your understanding of Jasmine, Grusha, and Tia goes up!"

        return







        


        
return