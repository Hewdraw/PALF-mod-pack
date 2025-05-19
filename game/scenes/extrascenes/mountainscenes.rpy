label bluetalkmountainfieldtrip:
    $ AddEvent("Blue", "MountainTalk")
    show blue uniform wistfulbrow glancemouth with dis

    red uniform @talkingmouth "Hey, Blue."

    blue @glancebrow wistfulmouth "Oh. Hi."

    $ ValueChange("Blue", 1, 0.5)

    pause 1.0

    red @talkingmouth "Talk to your grandpa yesterday?"

    pause 1.0

    blue @talkingmouth "Not yet."

    pause 0.5

    blue "{w=0.5}.{w=0.5}.{w=0.5}."

    blue @wistfulmouth "I don't want him to pay attention to me {i}just{/i} because I've got this Eevee."

    hide blue with dis

    pause 1.0

    red @closedbrow talking2mouth "Good talk."

    return

label dawntalkmountainfieldtrip:
    $ AddEvent("Dawn", "MountainTalk")
    show dawn uniform with dis

    red uniform @talkingmouth "Hi, Dawn."

    dawn @happy "O-oh! Hi, [first_name]."

    $ ValueChange("Dawn", 1, 0.5)

    red @talkingmouth "You seem to be in high spirits. Does this place remind you of home?"

    dawn @talkingmouth "A little bit."
    dawn @sadbrow talkingmouth "If I'd known we were taking a class trip out here so soon, though, I wouldn't have gone out here alone last Wednesday."

    red @happy "Think of it like an early advantage. You're the Veteran, now, who can guide all us rookie trainers to the best spots on the mountain."

    dawn @talkingmouth "I guess. Actually, it's nice that I don't need to rush around like everyone else. I can just look at the mountain and enjoy the scenery for a while. {i}Sigh...{/i}"
    dawn @happy "This is actually some great inspiration for that ice sculpture I was making. I wasn't sure what kind of pedestal I wanted..."

    pause 0.5

    dawn happy @sadbrow talkingmouth "I don't suppose it'd be weird if I asked you to pose for me just so I can sketch out some ideas?"

    red @happy "Might be a little weird, but it's the kind of weird I like. Let's do it."

    narrator "You pose for a bit. You feel ridiculous, but Dawn seems very enthusiastic about her sketches, so you try to avoid laughing."

    dawn @talkingmouth "This is great!"

    pause 1.0

    dawn -happy @sadbrow talkingmouth "Um... j-just out of curiosity, I'm not planning anything, but, um... do you have plans this Saturday?"

    red @talkingmouth "Hm? Not that I know of."

    dawn @closedbrow talkingmouth "W-well, it's my birthday this Saturday, so, um, if you were interested... then... maybe we could... do a thing...?"

    red @happy "Hey, are you inviting me to a birthday party?"

    dawn @sadbrow talkingmouth "M-more or less."

    red @talkingmouth "That sounds great. I'd love to come, Dawn. When and where?"

    dawn @surprised "O-oh. I, um, I don't know. I don't actually have anything planned. I wasn't planning on celebrating, or anything... until very recently."

    red @talkingmouth "Well... we don't have a lot of time. How about you give me a call when you have the deets?"

    dawn surprised "C-c-c-call?!"

    red @closedbrow talkingmouth "A text is fine too."

    dawn -surprised @sadmouth closedbrow "Y-yes, please."
    dawn @closedbrow sadmouth "I... I guess I should ask for your phone number, then... and give you mine."

    red @winkeyes talkingmouth "Yeah, it'd make calling me a bit easier."

    dawn @closedbrow "A-alright, then..."

    $ BecomeContacted("Dawn")

    hide dawn with dis

    return

label hilberttalkmountainfieldtrip:
    $ AddEvent("Hilbert", "MountainTalk")
    show hilbert uniform with dis

    red uniform @talkingmouth "Hey, Hilbert. You looked like you were struggling up the hill, a bit."

    hilbert @closedbrow talkingmouth "Apparently Cyclizar riding takes more grip strength and coordination than I possess."

    pause 0.5

    hilbert @talkingmouth "At least it'll be easy to go back down. Even if I fall off, I'm going the right way."

    pause 2.0

    show hilbert sadbrow with dis

    red @surprised "Was that a joke?"

    hilbert @angrybrow talkingmouth "It was a mistake. Just like coming up here was. I hate the cold. I hate the ice. I hate everything about this."

    pause 1.0

    red @confusedeyebrows frownmouth "{w=0.5}.{w=0.5}.{w=0.5}."

    show hilbert surprised with dis

    red @happy "We could huddle together for warmth."

    $ ValueChange("Hilbert", 1, 0.5)

    hilbert @closedbrow "D-don't... say ridiculous things like that."
    hilbert @angrybrow talkingmouth "Not unless your words are true."

    red @playfulbrow smirkmouth "Oh, so {i}now{/i} you care about truth?"

    hilbert @sadbrow talkingmouth "I'm leaving."

    hide hilbert with dis

    return

label ethantalkmountainfieldtrip:
    $ AddEvent("Ethan", "MountainTalk")

    show icecave with dis

    narrator "You follow Ethan into an icy cave."
    narrator "However, as soon as you step in, you don't see him anywhere."

    if (IsWeekend()):
        red @talkingmouth "Ethan, bud? You around?"

        show ethan with dis

    else:
        red uniform @talkingmouth "Ethan, bud? You around?"

        show ethan uniform with dis

    ethan @talkingmouth "Oh, hey. Yeah, I came up here to train. I was just checking out the echo in this cave." 

    $ ValueChange("Ethan", 1, 0.5)
    
    ethan @happy "Check this out."

    ethan @happy "{size=40}I'm here!{/size}"

    TempCharacter("Echo") "{size=30}I'm here!{/size}"
    TempCharacter("Echo") "{size=20}I'm here.{/size}"
    TempCharacter("Echo") "{size=10}I'm here...{/size}"
    
    ethan @talkingmouth "Neat, huh? And all the ice makes it kinda pretty, too."

    red @happy "Pretty as a Pecharunt."

    ethan @confused "What?"

    red @talkingmouth "It's a Pokémon from Kitakami. Um, creates Mochi zombies. That's what I've heard, anyway. They're meant to be extremely rare."

    ethan @talkingmouth "Gotcha."

    pause 1.0

    ethan @sad2eyes talking2mouth "Welp, I'm outsies. Looks like there aren't any Pokémon in this cave, now, so we should probably head to the main path."

    red @talkingmouth "Sure. I'll spend just a little bit more time in here. You go on ahead."

    ethan @talking2mouth "Sounds good, man. Don't spend too long in here, though. You'll go crazy talking to the echoes."

    red @happy "I'll keep that in mind."

    hide ethan with dis

    pause 2.0

    narrator "You spend a bit more time looking around the cave, but besides a large rock that seems somewhat out-of-place in the cave, nothing grabs your attention."
    narrator "Every few minutes, a single droplet of water lands on the rock, very, {i}very{/i} slowly covering it in ice. Perhaps, a long time in the future, this rock will be fully frozen."
    narrator "Or perhaps the frozen water will worm its way into the rock's cracks, and just shatter it to pieces. We must pray that the rock can endure."

    redmind @thinking "...Ethan's right, this place {i}does{/i} make you go crazy."

    pause 0.5

    red @talkingmouth "Alright, let's get out of here."

    pause 1.0

    show kris angrymouth with dis:
        xpos 0.25

    pause 1.0

    kris @sadbrow talking2mouth "Oh, Ethan... what happened to you...?"

    pause 0.5

    kris sadbrow @talkingmouth "Thank goodness you've got that [first_name] to watch out for you, at least..."

    $ ValueChange("Kris", 1, 0.5)

    kris angrybrow talking2mouth "I'll figure this out, Ethan. Don't worry."

    hide kris 
    hide icecave
    with dis

    return
