label day010603:

stop music fadeout 1.5

call calendar(1) from _call_calendar_59
$ calDate = calDate.replace(day=3, month=6, year=2004)
$ renpy.music.queue("Audio/Music/Oak Class.ogg", channel='music', loop=None, fadein=1.5, tight=None)
$ timeOfDay = "Morning"

scene homeroom
show screen currentdate
show blue happybrow uniform:
    xpos 0.33
show leaf uniform flirtbrow frownmouth:
    xpos 0.66
with splitfade

blue @happy "...But did you {i}see{/i} her?!"

leaf @sarcastic "Yes, Blue. I saw her. I saw her the last three times you asked, as well."

blue @angrybrow talkingmouth "She was on fire! She was--it was like something out of one of Diantha's movies! Who the hell taught her to dance?"

leaf @closedbrow talking2mouth "I figured she learned it from trying to avoid stepping on your land mines all the time."

blue @happy "Man, I don't even care what you say. She was the best damn coordinator last night!"

show leaf -flirtbrow -frownmouth with dis

if (HasEvent("Yellow", "AcceptPartner")):
    red uniform @confused "Uh, yeah, hi. Also here. I was also there last night?"

    if (HasEvent("Professor Oak", "WonMDTryouts")):
        blue -happybrow @talking2mouth "What, you want a medal? Yellow carried you. You looked stupid as hell, standing there like a lump in that ratty old vest."
    else:
        blue -happybrow @angrybrow angrymouth "It was {i}your{/i} half of the performance that made you lose. You looked stupid as hell, standing there like a lump in that ratty old vest."

elif (HasEvent("Professor Oak", "ParticipateMDTryouts")):
    red uniform @confused "Uh, yeah, hi. Also here. I was also there last night?"

    blue -happybrow @talking2mouth "Yeah, so what? You should just be happy you weren't in the same round as Yellow. You would've lost, hard. You looked stupid as hell, standing there like a lump in that ratty old vest."

    if (HasEvent("Professor Oak", "WonMDTryouts")):
        red @talking2mouth "I won my round."

        blue @closedbrow talking2mouth "Against a bunch of fat old men, great job."

elif (HasEvent("Professor Oak", "WatchMDTryouts")):
    red uniform @happy "Nice to hear you being so invested in someone else's interests for once, Blue."

    blue -happybrow @talking2mouth "Pssht. I'm always positive. For example, I'm {i}positive{/i} that it was a good idea for you to not join--because if you had, Yellow would have crushed you!"
    blue @happy "Can you imagine yourself standing up there? You'd look stupid as hell, standing there like a lump in that ratty old vest."

else:
    red uniform @happy "Sounds like I missed quite the show."

    blue -happybrow @happy "Hah! You don't even know. It was a good idea for you to not join--because if you had, Yellow would have crushed you!"
    blue @happy "Can you imagine yourself standing up there? You'd look stupid as hell, standing there like a lump in that ratty old vest."

red @upeyes angryeyebrows talking2mouth "Why does every tiny bit of positivity you show have to come at my expense?"

blue @talking2mouth closedbrow "Whatever. You'll deal with it, and pull some bullshit that makes you leap ahead later. Like always."

hide blue with dis

if (not (HasEvent("Yellow", "AcceptPartner") or HasEvent("Professor Oak", "ParticipateMDTryouts") or HasEvent("Professor Oak", "WatchMDTryouts"))):
    red @confused "Was Yellow really that good?"

    leaf @sadbrow talkingmouth "Blue might've been overselling her a bit."

    pause 1.0

    leaf @happy "But... I think she was having fun. And that's what matters, right?"

show leaf:
    xpos 0.66
    ease 0.5 xpos 0.5

pause 1.0

leaf @closedbrow frownmouth "Hm."

red @confusedbrow talkingmouth "Something up?"

leaf @closedbrow talking2mouth "I'm just thinking, what Blue said about your vest..."

red @closedbrow sweat talking2mouth "It's not actually ratty. He calls it that because [pika_name]'s fur gets on it. And [pika_name]'s a mouse, so, you know, it's a bit of a pun, but--"

leaf angrybrow angrysmilemouth @sadbrow talkingmouth "Skippy? Shush. I'm going into my mind palace."

red @happy "Mind funhouse, more like."

leaf -angrybrow -angrysmilemouth @closedbrow frownmouth "[ellipses]"

show blank

pause 0.1

hide blank

$ PlaySound("idea.ogg")

leaf @surprisedbrow happymouth "Ellipses!"

red @confused "Pretty sure it's 'eureka.'"

leaf @talkingmouth "Yeah, I thought I'd start doing that thing you do, where you pretend you get simple phrases wrong."

red @happy "Ah, right. {w=0.5}{i}Pretend{/i}."

leaf @talkingmouth "Anyway, I figured it out, I'm a genius, and other things you already know."

red @happy "Standing by to deliver praise, ma'am."

if (HasEvent("Professor Oak", "ParticipateMDTryouts")):
    leaf @happy "I need to go shopping to pick up an outfit for Klara's party on Saturday. Why don't we all go to Inspira Friday evening to pick out coordinator outfits for you and Yellow?"
    
    if (not HasEvent("Game", "WonMDTryouts")):
        if (HasEvent("Yellow", "AcceptPartner")):
            redmind @sadbrow "Even though we didn't win our tryouts, she still wants to get outfits for us...?"

        else:
            redmind @sadbrow "Even though I didn't win my tryout, she still wants to get an outfit for me...?"

else:
    leaf @happy "I need to go shopping to pick up an outfit for Klara's party on Saturday. Why don't we all go to Inspira Friday evening to pick out a coordinator outfit for Yellow, too?"

if (HasEvent("Klara", "BrokeBond")):
    pause 1.0

    leaf surprisedbrow frownmouth @talking2mouth "Wait. What's wrong?"

    red @closedbrow talking2mouth "It's... ah, it's nothing."

    leaf @sadbrow talkingmouth "C'mon, Skippy. Friendship pact. It's never 'nothing' between us."

    red @sad2brow frownmouth "[ellipses]"
    red @sad2brow talking2mouth "Okay. Look, I'm not--I don't think she did anything wrong. I'm not saying that."
    red @closedbrow talking2mouth "But Klara and I met yesterday, and... she said some really weird stuff. It made me pretty uncomfortable."
    red @closedbrow talking2mouth "You know, she wanted me to be her partner in the tryouts, right? And I... well, I think she kinda tried to blackmail me into it when I said no."

    leaf @surprisedbrow talking2mouth "{i}Klara{/i} did this?"

    red @closedbrow sweat talking2mouth "Well, maybe? It might just be in my mind. I might be imagining it, you know? But..."
    red @wince talking2mouth "Well, final answer, yes."

    pause 1.0

    show leaf angrybrow frownmouth with dis

    leaf @talking2mouth "I trust you. I don't know why she'd do that, but I believe you."

    red @sadbrow talkingmouth "Thanks. I'm not sure I believe it myself, so having {i}you{/i} believe me means a lot."

    leaf @talking2mouth "I'll talk to her at the party. I'll figure out what was going on, and why she did this."
    leaf -angrybrow -frownmouth @sadbrow talkingmouth "It might be an awful misunderstanding, you know?"

    red @sadbrow talkingmouth "I hope so. I don't think she's, like, trying to do what Cheren did, but[ellipses]"
    red @closedbrow talking2mouth "Well, like I said, I felt a bit uncomfortable."

    leaf @talkingmouth "I gotcha, Skippy. I'll figure this out. And if it turns out she was just being a meanie-pants, we cut ties and move on."

    red @happy "Spoken like a true kindergarten teacher."

    pause 1.0

    red @talking2mouth "Oh, there's one more problem, though."

else:
    red @talking2mouth "There's a problem with that plan, Generalissimo."

leaf @surprisedbrow talking2mouth "What? My flawless stratagem has a flaw? Say it ain't so."

red @happy "We've got something Friday evening. Remember? That little 'Battle Team meeting' thing we do sometimes?"

leaf @surprised "Oh my god, I can't believe I forgot that."

leaf @closedbrow talking2mouth "Well... shoot. I guess I'll just have to pick something up by myself. Maybe Saturday morning."

pause 1.0

red @sadbrow "[ellipses]"

leaf surprisedbrow frownmouth @surprisedbrow talking2mouth "What? What's that face for?"

red @talkingmouth "It holds a bunch of my organs in place, but the main thing is, well, is there any real reason to push this back?"

leaf @talking2mouth "Um. I guess not...?"

red @happy "Why don't we just do it this evening, then?"

leaf @talking2mouth "Uh. Yeah. Yeah, that would work."

pause 1.0

leaf @sadbrow talkingmouth "I swear I'm getting better at carpe-ing my diems. I just need a bit more practice."

red @happy "It's alright. I'm here for ya until you figure it out."

show leaf angrysmilemouth angrybrow fullblush with dis

red @winkbrow talkingmouth "Which, you know, if you keep putting it off, might be a while."

show oakbg behind leaf with dis

pause 0.5

red @happy "Yell at me later, dormie. Sam's here."

scene blank2 with splitfade

jump homeroom1transition