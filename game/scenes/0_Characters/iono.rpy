label Iono1:
$ AddEvent("Iono", "Iono1")
scene ionodoor
with Dissolve(2.0)
stop music fadeout 1.5
queue music "audio/music/mybetterworld.ogg"

pause 1.0

red @unamusedbrow unamusedmouth "[ellipses]"
red @talking2mouth "{size=30}I can't believe I'm doing this.{/size}"

pause 1.0

$ PlaySound("knock.ogg")

pause 2.0

red @talking2mouth "Iono? You in there?"

show iono with dis:
    zoom 0.0
    ease 0.5 zoom 1.0

iono poutmouth angryeyes annoyedeyebrow @angrymouth "Hey! What's the big idea? Mugging at my security cams like that! Can't a girl video-edit in privacy?"

python:
    nightestlaw = "Gardenia"
    nightestlawvalue = 0
    pronoun = "She"
    for char in ["Gardenia", "Silver", "Skyla"]:
        charvalue = GetRelationshipRank(char) * 100 + GetValue(char)
        if (charvalue > nightestlawvalue):
            nightestlawvalue = charvalue
            nightestlaw = char
            if (nightestlaw == "Silver"):
                pronoun = "He"
            else:
                pronoun = "She"

red @talking2mouth "I've been talking with [nightestlaw]. [pronoun] talked with the other Disciplinary Committee members, and {i}no-one{/i} has seen you in classes."

pause 1.5

iono confusedeyebrow confusedeyes frownmouth @confusedmouth "Well... yeah. That's kinda the point, friendo."

red @confused "We thought you were going to start showing up in classes?"

iono neutralbrow @happybrow happymouth "Nyohohoho! I {i}definitely{/i} didn't say I was going to do {i}that.{/i}"

red @talking2mouth "But you're not recording the lessons anymore, right? So[ellipses]"
red @wince talking2mouth "Don't tell me you're spending a small fortune to attend Kobukan Academy and you're just {i}not{/i} going to class."

iono @surprised "What? No, no, friendo, you've got me all wrong!"
iono @angry "The eye of Sauron sees all, young Hobbit. I'll not be deceived, distracted, or misled!"
iono neutralbrow smilemouth @winkeyes teeheemouth "It's true I'm not {i}recording{/i} the classes any more, but I still stream 'em."

pause 0.5

iono @sad "Though[ellipses] since I don't have recordings to look through any more, I can only really attend {i}one{/i} homeroom, and take {i}two{/i} electives at once[ellipses]"
iono @angry "And that's boring! You guys' rule about not recording anything is boring me to death! Death! Death!"
iono @defeatedeyes sadmouth sigheyebrow "Not to mention that I'm getting {i}way{/i} less bang for my buck..."

red @upeyes angryeyebrows talking2mouth "Firstly, we're not a 'you guys'--they do their thing, I do mine. The only reason I'm here is because I thought I could get through to you."

iono @smugeyebrow smugeyes smugmouth "Ooh, you think you can get through to me? Well, Sir Friends-A-Lot, I'm afraid that your Friendzone is no match for the power of the Iono Zone!"
iono @smilebrow battlemouth "Behold! My ultimate technique--a meter of reinforced steel!"
iono neutraleyes @teeheemouth "No Frienergy waves are getting through that, friendo. Bad luck!"

red @closedbrow talking2mouth "I wasn't going to try and 'Frienergy' you, I was going to {i}talk{/i} to you."

iono @surprised "Ah! This chad aura--this impermeable social confidence--is it possible I've met my match?! Do I have any defense against the power of 'Just Talking Like a Normal Person?!'"

pause 1.5

red @unamusedbrow talking2mouth "Iono, I realize asking this is going to come off a tiny bit rude, but can you turn that off?"

iono sad @sadbrow "Too much?"

red @closedbrow talking2mouth "A little bit. My head's spinning with a billion different questions, and I can't really figure out which one to ask first with you dropping references every five words."

iono @happybrow happymouth "Alright-y, alright-y."
iono @sadbrow talkingmouth "Sorry, buddy, pal, chum, matey, homie, homeslice, breadslice, dawg. No more references. Putting a lid on it." 
iono neutralbrow smilemouth @winkbrow happymouth "Wrapping it up, and without futher ado, I will use the absolute minimum amount of words I can to convey whatsoever meaning I doth careth to impart upon thine earholey orifices."

red @sweat talking2mouth "Uh[ellipses] okay."

red @closedbrow talking2mouth "So, the second thing I was going to say is that you're missing a {i}ton{/i} of Kobukan stuff locked up back here."
red @closedbrow talking2mouth "Cheren said he cleared it with Drayden. Whatever, he probably isn't lying. But just because you {i}can{/i} stay here doesn't mean you {i}should{/i}."

iono rolleyes frownmouth @rolleyes angryeyebrow talking2mouth "Uggggh. Look, this {i}works{/i} for me. I'm not in anyone's way, and the only people who know I'm here work for the school. You're basically my bodyguards."

red @talking2mouth "Again--{i}not{/i} a member of the Disciplinary Committee. Student government and I aren't on speaking terms. But more importantly--"
red @sadbrow talkingmouth "Iono, you were getting bullied by {i}Tinkatink{/i} before we found you."

red @talking2mouth "And[ellipses] {nw}" 

show iono surprisedbrow frownmouth with dis

extend @talking2mouth "the Disciplinary Committee and staff aren't the only people who know you're here."

iono worriedbrow frownmouth @shiverbrow talking2mouth "What? Who else knows?!"

red @surprised "Uh, well, there's me, I guess, and[ellipses] whoever Skyla tells, probably[ellipses]"

iono worriedmouth @closedeyes talking2mouth "No, no, no[ellipses] that's bad. That's real bad. Bad Times New Roman. Antipogs in the chat."

pause 0.5

iono sadbrow frownmouth @sadbrow talking2mouth "It's so Ionover. 'm going to have to pick up all my stuff and move somewhere else again[ellipses]"

red @confused "...Iono, I'm absolutely, completely, confused. Before you do anything drastic like leaving Kobukan, can we just get to know each other a bit?"

iono neutralbrow @neutralbrow talking2mouth "'Kay, but I'm packing a suitcase right now, so I might be AFK for a bit."

pause 1.0

iono @smugbrow talkingmouth "That's a joke."

iono sadbrow @sadbrow talking2mouth "My suitcase is already packed. It {i}always{/i} is."

pause 1.0

redmind @thonk "This girl... she has more energy than I've ever seen, but it's impossible to tell which direction that energy's going to go at any moment."
redmind @angrybrow "Thankfully, I've prepared."

call clearscreens() from _call_clearscreens_243
show suite at sepia
show ethan casual at sepia
show flashback
with Dissolve(2.0)

red sepia @talking2mouth "Hey, Ethan, got a question for you."

ethan surprisedbrow frownmouth @neutraleyes neutraleyebrows talkingmouth "Yeah? Shoot."

red @confused "You've heard of, uh, the streamer 'Iono', right?"

pause 1.0

ethan @talking2mouth "I swear my donations are under control. I have {i}nothing{/i} parasocial with her."

red @talking2mouth unamusedbrow "I'll take that as a 'yes.'"
red @closedbrow talking2mouth "Can you run me through what you know about her?"

ethan happy "Can I? How many hours you got?"

show blank with splitfade

pause 1.0

hide suite
hide blank
hide flashback
hide ethan
show screen currentdate
with Dissolve(2.0)

#redmind @surprisedbrow frownmouth "Wait, that reminds me--when I was looking up Iono, I learned some interesting information. Maybe asking about that'll get her to slow down?"

red -sepia @talking2mouth "Iono, hold on. You can't book plane tickets in the middle of a conversation, right? It'd be rude."

iono @rolleyes angryeyebrows frownmouth "[ellipses]"
iono @angrybrow talking2mouth "Alright, Jobbird-slayer. You've got five minutes to prevent me from beaming myself off to a different continent."
iono poutmouth @confusedbrow talking2mouth "What's your play?"

red @talking2mouth "You're Iono. The Supercharged Streamer, the Gym Leader of Levincia, and Master Engineer of the Paldean Youth Technology Convention four years running."

iono neutraleyes @happybrow happymouth "Hey, you remembered! Niceu, niceu, very {i}niceu{/i} [first_name]-chan."

red @talking2mouth "I'll admit, I had to look up a {i}lot{/i} of those words, but I think I get the idea. You were a prodigy engineer in Paldea."

iono surprisedbrow frownmouth @smugbrow talkingmouth "Not just {i}a{/i} prodigy. {i}The{/i} prodigy. Molayne? Bill? Oak? Buffoons, compared to me!"

red @talking2mouth "Okay, well, Samuel Oak is one of my best friends, so maybe roll the egocentrism back a bit."

iono neutralbrow frownmouth @sadeyebrows talking2mouth "Oh. Um, sorry. I was kinda[ellipses] exaggerating, for the bit. I don't actually think I'm smarter than any of those guys."

red @sadbrow talkingmouth "It's fine, I got it."
red @talking2mouth "Anyway, you won a ton of engineering contests trying to get kids into STEM. Then you attended Naranjuva, and were top of your class every year."

iono neutralmouth @surprisedbrow talking2mouth "And the competition was {i}really{/i} stiff, too! People who say Paldean Champions are a joke obviously never fought one!"

red @talking2mouth "You graduated from Naranjuva two years early, and took on the Paldean league. You beat the Top Champion of Paldea and became a Champion."

iono @smugbrow talkingmouth "Yeah, so I'm pretty sure I could go toe-to-toe with Cynthia. You know, since we're both Champions."

red @confusedbrow talking2mouth "Then things got a bit fuzzy[ellipses] but you became a Gym Leader, right?"

iono poutmouth @angrybrow talking2mouth "In any {i}other{/i} league, I would've been the youngest Gym Leader ever."
iono @talking2mouth "But Poppy was technically a Gym Leader for a month, before La Primera promoted her, so she'd have fewer challengers, and can still take naps[ellipses]"
iono @rolleyes talking2mouth "It's so hard to be a prodigy nowadays. It used to be fine to become Champion at, like, twenty-five. That used to be {i}huge{/i}."
iono @sadbrow talking2mouth "Nowadays, unless you're throwing Poké Balls and catching legendary Pokémon out of the crib, you're already too late."

pause 2.0

iono @talking2mouth "Wait, friendo, all you're doing is reading my Rotovideo wiki page to me. Weren't you trying to prevent me from catastrophizing?"

red @talking2mouth sweat "Kinda. The bigger thing, though, is[ellipses]"
red @happy "Well, that's the end of it. That's all I know. And I can't really draw a line from super-popular streamer, prodigy engineer, Gym Leader, and {size=30}technical{/size} Champion to[ellipses]"

show iono angrybrow poutmouth with dis

red @confused "...to Kobukan student locked behind a big metal door in a part of the school no-one goes to."
red @talking2mouth sadbrow "There's gotta be a story there, right? You're thinking of throwing away your Kobukan chances on the off-chance someone else knows you're here."
red @sadbrow talkingmouth "Don't want to sound like a broken record, but this is {i}Kobukan.{/i} People don't do that, right?"

pause 2.0

iono @talking2mouth "This is what you do, isn't it? You talk to people, look at 'em with those big brown eyes and they just spill {i}all{/i} their tragic backstory over you."

red @closedbrow talking2mouth "That... {i}has{/i} been a surprisingly recurring theme, yes."

iono @angrybrow talking2mouth "Well, I ain't falling for it! No way, no how, no chance, no dance, nosferatu!"

red @closedbrow talking2mouth "Alright. Fine, fine. But before you order that ticket, let me have one more chance. Just to take a wild guess at what might be going on here."
red @talkingmouth "You don't have to tell me if I'm right, or not. Just listen to what I say, and[ellipses] do whatever feels right, after that."

iono closedeyes frownmouth @rolleyes confusedeyebrow talking2mouth "Go on...?"

red @sadbrow talkingmouth "You're scared of leaving your bunker, right? Something happened--or maybe there was some kind of {i}threat{/i} that something would happen." 

show iono magnemiteshadow closedeyes frownmouth with dis

red @talking2mouth "In Paldea, maybe because of your success as an engineer, or maybe it was your streaming career, or maybe it was your Championship--somehow, you started attracting the wrong kind of attention."
red @sad2eyes talking2mouth "And[ellipses] you're hiding from it. You're attending Kobukan because you want to increase your knowledge of Pokémon, and become the kind of Champion that {i}could{/i} challenge Cynthia one day[ellipses]"
red @talking2mouth "But also because Kobukan is very, {i}very{/i} far from Paldea."

pause 2.0

iono -magnemiteshadow neutraleyes smilemouth @talking2mouth "Oh. That's a baseball."

red @confused "What?"

iono @winkbrow talkingmouth "Where are baseballs found?"

red @confused "At a baseball field?"

iono @disgustedbrow disgustedmouth "No. {i}In the ballpark.{/i}"

red @confused "In the[ellipses]"
red @surprisedbrow talking2mouth "Oh! In the ballpark. Got it."

iono @rolleyes talking2mouth "Look, you telling me how awesome I am stopped me from booking this plane ticket for, like, two minutes, so I think I {i}may{/i} be able to consider options other than {i}nigerundayooooo{/i}, so what've you got for me?"

red @talking2mouth "...Before we do that, look, you're saying a {i}lot{/i} of things I don't understand. I can't tell if that's because you're making more references than Ethan, or if it's because my English isn't as good as my Japanese, so can we switch?"

iono sadbrow frownmouth @sadbrow talking2mouth "Oh. I, uh... I don't know Japanese."

pause 1.0

red @talking2mouth "Really? Just English?"

iono @closedbrow talking2mouth "Yyyyeah[ellipses]"

red @talking2mouth "I've been switching between Japanese and English randomly for the past fifteen minutes. Did you mean that you only understood half of what I said?"

iono poutmouth @rolleyes angryeyebrow talking2mouth "Look, I know a {i}gajillion{/i} programming languages. Meatspace languages are {i}hard!{/i} Half of the reason I came to Kobukan was because I knew most people here spoke Japanese, and I could learn through immersion."

red @unamusedbrow talking2mouth "A great idea, save the fact that you can't learn the language if you aren't talking to anyone."

iono @poutmouth angrybrow "Hmph!"
iono frownmouth @talking2mouth "Roasting my language skills isn't going to get me to leave my bunker and attend classes, friendo."

red @talking2mouth sweat "Right, sorry, I got side-tracked. I'm just thinking[ellipses] you don't want anyone to know that you're here, right? Behind this big metal door?"

iono neutraleyes frownmouth @talking2mouth "Yup. This is locked content. My firewall. No getting through here. Even Tier 3 Subs can't impregnate my fortress of solitude."

pause 1.5

red @talking2mouth "Okay, hear me out--"

iono happybrow smilemouth @happybrow happymouth "Smash!"

pause 2.0

red @wince talking2mouth "What?"

iono @talking2mouth "When someone says 'hear me out,' they're usually about to say something like 'this non-sexy thing is actually sexy.'"
iono @talking2mouth "So I was, like, pre-empting that. See, when I say 'smash', that means, yeah, I agree, and would Super Smash whatever you're hear-me-outing."

pause 1.0

red @talking2mouth "I wasn't going to say {i}anything{/i} like that, though."

pause 1.0

iono confusedeyes bravemouth calmeyebrow @shadow disgustedbrow disgustedmouth "{size=30}Goddamn {i}normies.{/i}{/size}"

red @talking2mouth "(This is the longest five-minute conversation I've ever had.)"

iono @talkingmouth "English, friendo. {i}No hablo japonesa.{/i}"

red @talking2mouth "Right. Okay, so, as I was saying--the most important thing to you is that no-one knows you're {i}here{/i}."

iono @talkingmouth "Yep."

red @confused "But if people thought you were a normal student, then[ellipses] wouldn't they have no idea that you're here? They'd think you were in a regular dorm, or something, right?"

iono @surprisedbrow talking2mouth "Wait, wait, wait, wait, wait. Chat, is this guy brilliant, or an idiot?"

red @sadbrow talkingmouth "Jury's still out on that one."

show iono angrybrow poutmouth with dis

red @talking2mouth "But, seriously, think about it. You've got a {i}lot{/i} of fans, right? Maybe not Rosa-level, but[ellipses]"

iono @talking2mouth "I {i}could{/i} have Rosa-level fans! But she's part of the Pokéstar elite, and I'm just a little indie streamer! She's got bodyguards and schedules and managers and jazz! All I've got is a webcam!"

red @talking2mouth "That's not really the point I'm trying to make. I'm saying that if your fans find out you're here, they'll go looking for you."
red @sadbrow talkingmouth "Hiding your existence from everyone only works if people don't know you're here at all. At this point, that cat's basically out of the bag."
red @happy "But, like, if your fans think you're just another, normal, student, then they won't try to find you, right? Because they'll see you in class."

iono @closedbrow talking2mouth "[ellipses]You actually {i}are{/i} a genius, aren't you? I thought you were just a himbo, but you've got something behind those eyes."

red @talkingmouth sadbrow "I'm {i}extremely{/i} motivated to come up with ideas that help people out."

iono @talking2mouth "Well[ellipses] alright."

pause 1.0

iono @talkingmouth "Alright! In order to not be found, I'm going to make sure {i}everyone{/i} sees me as a totally normal, average, everyday student! Yeah! Let's do this!"
iono neutralbrow smilemouth @smugbrow happymouth "Nyohohoho! Hiding in plain sight--delightfully devilish, my collabster!"

red @talking2mouth "Cool. Glad I could convince ya."
red @closedbrow talking2mouth "Now, if we're going to convince the rest of Kobukan that you're a totally normal, average, student, we're going to need to do a bunch of things, very quickly, before you need to attend your first elective."

show iono impressedbrow frownmouth with dis

red @talking2mouth "That doesn't give us a lot of time. But I've made a list of what we can do to help you out."

pause 1.0

iono @talking2mouth "You[ellipses] came here with a list?"

red @talking2mouth "Well, yeah."

pause 1.0

iono closedbrow frownmouth @closedbrow talking2mouth "So, you were {i}that{/i} confident that I'd go along with your plan[ellipses]"
iono sadbrow frownmouth @sadbrow talking2mouth "Why do I feel like I've been tricked?"

red @sadbrow talkingmouth "Promise you haven't. I can't really trick people--you know, Frienergy."

iono angrybrow poutmouth @angrybrow talking2mouth "Yeah, except the whole thing about {i}a meter of steel{/i}. I have 101%% immunity to your Frienergy!"

red @confused "Maybe. I don't know. Maybe a meter of steel isn't enough."

iono @talking2mouth "Hmph. It {i}definitely{/i} is, but I can't tell you why I know it. Just know that I'm right, you're wrong, end of story, game over, {i}fin{/i}."

red @talking2mouth unamusedbrow "I'll accept that unquestioningly."

iono @happybrow happymouth "That's what I like to hear!"

pause 1.0

iono @sadbrow talking2mouth "Wait, scratch that. Everything's awful. I just realized this plan won't work."

red @talking2mouth "What?"

iono @sadbrow talking2mouth "My holograms are the best in the entertainment biz. {i}Hatsune Miku{/i} uses them to perform. I've used 'em in my gym for ages, with no problems. But even they're not perfect. And that redheaded stripper--"

red @unamusedbrow talking2mouth "Her name is Skyla, and she's very nice."

iono @sadbrow talking2mouth "--she could see my holograms flickering. If {i}she{/i} can see them, then maybe someone else can, too."

if (HasEvent("Skyla", "Skyla2")):
    $ AddEvent("Iono", "SkylaHologram")
    red @talking2mouth "Look[ellipses] she's a special case, okay? She actually has, like, a power. It lets her see things, uh, {i}truly{/i}. She can see stuff other people can't."
    red @talkingmouth "I {i}promise{/i} there's only one person out there who can do what Skyla can, and she's not going to be a problem. She doesn't even go to Kobukan."
    red @sadbrow talkingmouth "No-one else will be able to see through your holograms. Guaranteed."

    pause 1.0

    iono @talking2mouth "Are you serious? The Hoothooters Waitress has X-Ray vision?"

    red @talking2mouth unamusedbrow "That's not {i}any{/i} part of what I said, no."

    iono @closedbrow talking2mouth "Well, if you {i}say{/i} she's a special case, I'll believe it."
    iono @angrybrow angrymouth "But if someone else comes around with their special eyes and sees through my hologram, it's on you!"

    red @sadbrow talkingmouth "It'll be fine."

    pause 1.0

    iono @angrybrow happymouth "Alright. Normal student time..."
    extend uniform happybrow smilemouth @happybrow happymouth "Go!"

elif (GetRelationshipRank("Nate") > 0):
    $ AddEvent("Iono", "NateHologram")
    red @talking2mouth "Yeah, I thought about that. You said your holograms are the best in the entertainment biz, right?"

    iono @talking2mouth "Yeah."

    red @talking2mouth "Well, I've got something that might help. It's a bit {i}outside{/i} of the biz."

    narrator "You look around quickly, then hold out a small gadget that Nate gave you. He didn't ask what you wanted it for, and he'd gotten it to you in less than half an hour."

    iono @confusedbrow talking2mouth "Huh? What's this? A fidget toy or something[ellipses]? I've got enough, thanks."

    red @talking2mouth "I don't know what it is. But I know it's used to hide things. And that {i}extremely{/i} powerful people trust it to hide things for them."

    iono @disgustedbrow disgustedmouth "Wait, that's[ellipses]"
    iono @surprisedbrow talking2mouth "Holy frijoles! This little baby's a crystalline light refractor shield! But I've never seen one {i}so{/i} tiny!"
    iono neutralbrow smilemouth @smugbrow talkingmouth "Look at that! It's got over twenty wafer-thin mirrors aligned with absolute {i}pinpoint{/i} precision--this machining is {i}insane{/i}! Who made this? The Unovan military? INTERPOL? Santa's Elves?"

    red @talking2mouth "We at the North Pole are not at liberty to discuss that."
    red @talkingmouth "Will this help make your holograms more stable?"

    iono @talkingmouth "Oh, totally, 100%%! All I need to do is swap out the lenses for my I-Balls, then I can beam a photorealistic version of myself that even my own mother wouldn't be able to tell the difference between!"

    red @talking2mouth "Cool. How long will that take?"

    iono @talking2mouth "Huh? Oh, not long. I'll be done soon."

    pause 1.5

    red @talking2mouth "Like, two hours--"

    iono @talking2mouth "Five."

    pause 1.0

    red @talking2mouth "What do you think 'soon' means?"

    iono @smugbrow talkingmouth "Friendo, I'm installing the ability to create the world's most-advanced holograms, ever, into a pair of machines that will need to trick thousands of students, every day, until the school year's over."
    iono @closedbrow talking2mouth "I'm doing this by using technology that's twenty years ahead of anything I've ever seen before, and was made by, as far as I can tell, aliens."
    iono angrybrow poutmouth @angrybrow talking2mouth "You'll give me the time I need, capiche, comprende, understando?!"

    red @closedbrow sweat talking2mouth "U-understando[ellipses]"

    narrator "You sheepishly hand over the gizmo, and pull out some textbooks--you had a feeling this might happen. Might as well get some studying in."
    
    call clearscreens() from _call_clearscreens_244
    scene blank2 with splitfade

    pause 1.0

    show asmuchtimeassheneedslater at vspaz

    pause 3.5

    show screen currentdate
    scene ionodoor
    show iono uniform
    with splitfade

else:
    $ AddEvent("Iono", "Tia")
    red @talking2mouth "Yeah, I thought about that. You said your holograms are the best in the entertainment biz, right?"

    iono @talking2mouth "Yeah."

    red @talking2mouth "Well, I've got something that might help. It's a bit {i}outside{/i} of the biz."

    narrator "You look around quickly, then hold out a feather that Tia gave you. Examining it closely, each barb has a semi-translucent crystalline pattern, reflecting everything around it, within itself, infinitely."

    iono @confusedbrow talking2mouth "Huh? What's this? A bird leaf?"

    red @talking2mouth "It's a feather. But look closely at it."

    narrator "You turn the feather sideways, and it seems to almost entirely disappear in your hand. Angling it a bit more, a {i}perfect{/i} reflection of the finger underneath is visible in the feather's barbs, imitating both depth and color flawlessly."

    iono @disgustedbrow disgustedmouth "Wait, that's[ellipses]"
    iono @surprisedbrow talking2mouth "Holy frijoles! This little baby's basically a crystalline light refractor shield! But I've never seen one {i}so{/i} tiny, and the fact it's a {i}feather{/i}?!"
    iono @smugbrow talkingmouth "Look at that! It's got {i}thousands{/i} of these tiny crystalline barbs--every single one of them a perfect mirror! What kind of Pokémon is this from?! Lugia? Ho-Oh?! It's {i}gotta{/i} be a big bird, right?"

    red @talking2mouth "We of the Kimono Girls are not at liberty to discuss that."
    red @talkingmouth "Can you learn anything from this? Will this help make your holograms more stable?"

    iono @talkingmouth "Oh, totally, 100%%! All I need to do is route the reflections I'm using to emit my holograms through one of these barbs, then I can beam a photorealistic version of myself that even my own mother wouldn't be able to tell the difference between!"

    red @talking2mouth "Cool. How long will that take?"

    iono @talking2mouth "Huh? Oh, not long. I'll be done soon."

    pause 1.5

    red @talking2mouth "Like, two hours--"

    iono @talking2mouth "Five."

    pause 1.0

    red @talking2mouth "What do you think 'soon' means?"

    iono @smugbrow talkingmouth "Friendo, I'm installing the ability to create the world's most-advanced holograms, ever, into a pair of machines that will need to trick thousands of students, every day, until the school year's over."
    iono @closedbrow talking2mouth "I'm doing this by using a {i}feather{/i} that belongs to a Pokémon I've never seen before, and grew on a Pokémon that, as far as I can tell, doesn't exist."
    iono angrybrow poutmouth @angrybrow talking2mouth "You'll give me the time I need, capiche, comprende, understando?!"

    red @closedbrow sweat talking2mouth "U-understando[ellipses]"

    narrator "You sheepishly hand over the feather, and pull out some textbooks--you had a feeling this might happen. Might as well get some studying in."

    call clearscreens() from _call_clearscreens_245
    scene blank2 with splitfade

    pause 1.0

    show asmuchtimeassheneedslater at vspaz

    pause 3.5

    show screen currentdate
    scene ionodoor
    show iono uniform
    with splitfade

pause 1.0

red @talking2mouth "Hey, uh, Iono?"

iono @talkingmouth "Yep?"

red @talking2mouth "You're wearing the uniform?"

iono @smugbrow smugmouth "Yeah, I modeled and textured it myself. Pretty swank, right?"

pause 1.0

show iono impressedbrow frownmouth with dis

red @unamusedbrow talkingmouth "I'm going to wait for the genius prodigy Iono to figure this out on her own."

iono @closedbrow talking2mouth "I haven't left the house in a while[ellipses] let's see[ellipses] keys? Wallet? Poké Balls?"

pause 1.0

iono @happybrow happymouth "Eureka! I got it!"
iono neutralbrow smilemouth nocoat @happybrow happymouth "There we go. No coat, and now I'm all proper-like and Kobukanian and whatnot. Ready to be a normal student, yep!"

pause 2.0

iono sadbrow frownmouth @sadbrow talking2mouth "You're still lookin' at me like I've got a big glowing weak spot somewhere[ellipses]"

pause 1.0

iono @angrybrow talking2mouth "You're really busting my I-Balls here, friendo! What is it? Did I mess up my drone alignment? Am I flickering? Did I leave a layer turned off?"

pause 1.0

red @unamusedbrow unamusedmouth "[ellipses]"

pause 1.0

iono puppyeyes defeatedeyebrow frownmouth @puppyeyes defeatedeyebrow talking2mouth "[first_name]? Please help me. I don't know what I did wrong, and I'm kinda scared."

red @surprisedbrow talking2mouth "Oh. Oh, shit, sorry, I didn't mean to take it that far."


show iono surprised blush with dis

red @talking2mouth "It's just... it's a [getRWDay(0)] [timeOfDay]. No-one's going to be wearing their uniforms right now. I mean, I'm not."

pause 1.0

iono defeatedbrow frownmouth @defeatedbrow talking2mouth "This plan is doomed. There's no way I can be a normal student. I'm too weird."

red @closedbrow talking2mouth "You gotta at least try, right?"
red @sadbrow talkingmouth "Believe me, in this year, you're... probably only top five, when it comes to weirdness."

iono @talking2mouth "...Not just sayin' that 'cause you're trying to get me to trust you so I leave my bunker and then you steal my bathwater when I'm not lookin'?"

red @unamusedbrow sweat talking2mouth "I guarantee I have absolutely no interest in your bathwater."

iono @closedbrow talking2mouth "Alright. I'll change back. Don't peek, my coatless model's only available to Tier 4 subs."

pause 1.0

show iono stream with dis

pause 1.5

show iono coat with dis

pause 1.0

red @sadbrow talkingmouth "Believe it or not, I actually have some experience helping secret hologram girls get acclimated to Kobukan. So don't worry. You're in good hands."

iono @closedbrow talking2mouth "If that's even a little bit true, you must be even weirder than me."

red @sadbrow sweat talkingmouth "Yeah, I'm easily top three. Now, come on. We need to get you a starter Pokémon."

call clearscreens() from _call_clearscreens_246
show blank2 with splitfade

stop music fadeout 2.5
queue music "audio/music/power plant_start.ogg" noloop 
queue music "audio/music/power plant_loop.ogg"

pause 1.0

show screen currentdate
scene research
show oak
with splitfade

oak @talking2mouth "Oh? Hello, lad!"

red @talking2mouth "Hey, Sam. Er, Professor Oak."

oak @talking2mouth "Who's this you've got with you? I don't recall seeing her before[ellipses]"

show iono:
    xpos 0.66 xzoom -1
show oak surprisedbrow frownmouth:
    xpos 0.5
    ease 0.5 xpos 0.33
with dis

iono @happy "Wotcher, alola, buengiorno and namaste! Iono, normal Kobukan student with nothing to hide, at your service!"

oak @talking2mouth sweat "I[ellipses] I see. Well, I'm glad to make your acquaintance, Miss Iono."

camera master at desaturate

show iono surprised behind oak with dis:
    xzoom 1 xpos 0.66

narrator "As though in slow-motion, you suddenly see Sam reach out for a handshake[ellipses]"

redmind @surprisedbrow frownmouth "Shit, we didn't think about that. Uh, excuses, excuses, {i}excuses{/i}..."

show iono behind oak:
    xpos 0.66 xzoom 1
    ease 0.2 xpos 0.85

camera master at Transform(matrixcolor=IdentityMatrix())

iono @surprisedbrow talking2mouth "Woah, there, Doctor! No touchy!"

show iono behind oak:
    xzoom -1 xpos 0.85

iono neutralbrow neutralmouth @sadbrow talkingmouth "I've[ellipses] got {i}real{/i} bad allergies, see? Even shaking someone's hand could lay me out."

redmind @thonk "Hm. She's fast on her feet."

show iono behind oak:
    xpos 0.85
    ease 0.5 xpos 0.66

oak @talking2mouth "Ah. So, that would explain the long, floppy sleeves. They serve as a form of protection. Quite sensible, then!"

iono @talking2mouth "Sharp as a tack, Doc! There's a reason they call you the Pokémon Professor."

oak @closedbrow talkingmouth "If you're trying to flatter me, I must admit it's working."
oak surprisedbrow frownmouth @sadbrow talkingmouth "It's always a pleasure to see you, lad, and meet more of your friends, but may I assume you came here to get something?"

red @talkingmouth "'Fraid so, this time. Iono here didn't pick up her starter Pokémon. We were hoping to fix that."

oak @talking2mouth "What? But it's the [getRDay(0)] of [calendar.month_name[calDate.month]]! Your starter Pokémon will, surely, be {i}terribly{/i} behind if you're only picking it up {i}now{/i}."
oak @confusedbrow talking2mouth "Perhaps more importantly, who's your homeroom teacher? Not giving you a starter Pokémon is a glaring oversight on their part. When Melody joined my class late, I immediately made sure to give her a new starter."
oak @sad2eyes talking2mouth "{size=30}Though[ellipses] I haven't seen her use it. It's a shame, too, Horsea are quite rare in the Kobukan area. I thought she'd be appreciative[ellipses]{/size}"

iono @sadbrow talking2mouth "I[ellipses] forgot."

pause 1.0

oak frownmouth @confused "I beg your pardon?"

iono @talking2mouth "I was late to class when the starters were given out, and[ellipses] forgot to pick it up."

pause 2.0

oak -surprisedbrow @sadbrow talking2mouth "Miss Iono, please tell me the truth."

iono embarrassedmouth @embarrassedeyebrow talking2mouth "I[ellipses] was too embarrassed to pick it up."

oak @talking2mouth "Well, that makes slightly more sense."
oak @talkingmouth closedbrow "But you mustn't let embarrassment rob you of opportunity! Self-awareness is a wonderful thing, but, perhaps, too {i}much{/i} may represent more of a shackle than a wing."
oak @sadbrow talking2mouth "That being said, unless you're looking for vaguely-inspiring quotes, I'm afraid I can be of little help in this regard."
oak -frownmouth @talkingmouth "You'll want to ask your homeroom teacher. They'll likely have your starter Pokémon on-hand, still, assuming it has not been released into the wild."

red @talking2mouth "Who's your homeroom teacher?"

show oak confusedeyebrows with dis

iono neutralbrow @talking2mouth "Well, like I said, I took a buncha homerooms."

red @talking2mouth "Sure. A {i}normal{/i} student wouldn't, though--so which was your {i}official{/i} homeroom?"

iono @rolleyes talking2mouth "Uh[ellipses] Cherry. Yeah, Doc Cherry."

show oak -confusedeyebrows with dis

red @happy "Oh, great."

redmind @thinking "She was the one who handled Tia, as well[ellipses] I almost feel bad dumping {i}another{/i} odd Ducklett on her, but if any Professor can take it in stride, I bet it's her."

red @happy "Thanks, Sam. I'll see you in class."

oak @talkingmouth "Certainly. Take care, lad! Be safe, Iono!"

hide iono with dis

pause 2.0

oak @confused "She took 'multiple homerooms?' What did she mean by that?"
oak @sad2eyes talking2mouth "I, certainly, never saw her[ellipses]"
oak @closedbrow sweat talking2mouth "I suppose I've still not quite shed my reputation[ellipses]"

stop music fadeout 1.5

call clearscreens() from _call_clearscreens_247
show blank2 with splitfade

queue music "audio/music/celebi_start.ogg" noloop
queue music "audio/music/celebi_loop.ogg"

pause 1.0

show screen currentdate
scene newhomeroom
show kris
with splitfade

red @talkingmouth "Oh, Doctor, you're here! Great."
red @happy "Is now a good time?"

kris @talking2mouth "Generally, my students sign up for office hours, if they want to discuss something."
kris @sadbrow talkingmouth "But if it's nothing too lengthy, I have some time."

show iono:
    xpos 0.66 xzoom -1
show kris surprisedbrow frownmouth:
    xpos 0.5
    ease 0.5 xpos 0.33
with dis

iono @happy "Yo, yo, yo! It's Io-no-no-no in the house! Pleasure to meetcha, Doc!"

kris @talking2mouth "Iono? That's--"

show iono confusedbrow confusedmouth with dis:
    xpos 0.66 
    ease 2.0 xpos 0.7

show kris angrybrow frownmouth with dis:
    xpos 0.33
    ease 0.5 xpos 0.5

narrator "Kris gets very, {i}very{/i} close to Iono, squinting and looking at her with uncomfortable intensity."

pause 1.0

kris @talking2mouth "[ellipses]Huh."

show iono confusedbrow confusedmouth with dis:
    xpos 0.7
    ease 0.5 xpos 0.66

show kris -angrybrow -frownmouth with dis:
    xpos 0.5
    ease 0.5 xpos 0.33

kris @talking2mouth "Your cosplay's {i}really{/i} impressive. You've even got her I-Balls. I don't think anyone could tell you're not actually her unless they were looking {i}really{/i} closely."

iono @surprised "Huh? What? I'm not Iono?! What do you mean?"

kris @happy "Iono has pink hair on her left, and teal on her right. You've got it flipped. Amazing effort, though!"

iono @talking2mouth "Oh. Right."

narrator "Iono looks at you, and mouths a word."

iono @disgustedbrow disgustedmouth "{size=30}Mirrors.{/size}"

kris @talking2mouth "It's a shame, because I know one of my students, Ethan, would {i}die{/i} to meet the real Iono. Maybe you should say 'hi' to him anyway? You must be a {i}really{/i} big fan to get your cosplay so close. I bet the two of you would get along well!"

iono winkbrow smilemouth @winkbrow talkingmouth "What if I told you I {i}was{/i} the real Iono?"

kris @sadbrow talkingmouth "I'm afraid I'd have to gently chastise you for lying."

iono @happy "Fair! Counterpoint: Rotonono, come out here, will you?"

show iono surprisedbrow frownmouth rotom rotombrowneutral rotommouthhappy with dis

TempCharacter("{gradient=#f00-#00f}Rotonono{/gradient}") "Bzzt! Ready to serve, happy to serve! What's your bidding, Genius Gym Leader Electrical ★ Streamer Master Engineer Fairest-of-Them-All Iono?"

show iono rotommouthneutral with dis

redmind @thinking sweat "She[ellipses] trained her Rotom to call her that?"

iono @sadbrow talking2mouth "I[ellipses] forgot that that's what I asked Rotonono to call me."
iono neutralbrow @winkbrow talkingmouth "Rotonono, how about you shorten that to {i}just{/i} Iono?"

show iono rolleyes frownmouth rotommouthhappy with dis

TempCharacter("{gradient=#f00-#00f}Rotonono{/gradient}") "Bzzt! Sure thing, Just Iono! Ready to serve, happy to serve!"

iono rotommouthneutral @rolleyes talking2mouth "Sarcastic little cuss."

kris @sadbrow talkingmouth "This is a {i}very{/i} elaborate cosplay."
kris @talking2mouth "Um, [first_name], and... 'Iono', this is taking a bit long. Can we pick this up later?"

iono @angrybrow talking2mouth rotombrowwonder rotommouthfrown "Hold it, hold it! Just gimme a second!"
iono -frownmouth @talkingmouth "Rotonono, snap a picture of us. Caption it 'Here at {color=#377CAB}#Kobukan{/color}, w/ Homeroom teach Cherry.\n{color=#377CAB}#IonoZone #RightHere #Blessed #PhysicallyHere #SmartWomen{/color}."

$ PlaySound("photo.ogg")

show blank

pause 1.0

hide blank with Dissolve(3.0)

iono @winkbrow talkingmouth "Now, post it to {i}all{/i} my socials."

show iono rotombrowwonder rotommouthhappy with dis

TempCharacter("{gradient=#f00-#00f}Rotonono{/gradient}") "Bzzt! Content generated and posted, Just Iono! Task complete in: 0.02 seconds!"

iono -rotommouthhappy -rotombrowwonder norotom @talkingmouth "Thankee muchly, Rotonono."
iono teeheemouth @winkbrow teeheemouth "Now, Doc Cherry, why don't you pop on over to @TheRealIono?"

kris surprisedbrow frownmouth @angrybrow talking2mouth "I already follow Iono, and I get alerts whenever she posts. Now, I'm actually getting a bit cross. Please--"

$ PlaySound("vibrate.ogg")

pause 1.0

kris @closedbrow talking2mouth "Please excuse me. It's probably a faculty email, or--"

pause 1.0

kris @talking2mouth "Wait."

show kris:
    xpos 0.33
    ease 1.5 xpos 0.3

kris @talking2mouth "Wait. {i}Wait{/i}. You're[ellipses] you're the {i}real{/i} Iono? The actual, {i}real{/i}, Iono?"

iono @talkingmouth "Sure am, Doc! Transferred in late. Had some Paldean league duties that kept me super busy. Champion stuff, yanno."
iono @winkbrow talkingmouth "Lucky you, though, you get to be my homeroom teacher!"

kris @talking2mouth "You're the real, actual, Iono, and you're actually, physically, right in front of me."

iono @winkbrow "I've never been more present than I am right now! Nyohoho! The Iono Zone's come to {i}your{/i} classroom, Doc! What do you think about that?"

kris @talking2mouth "I don't understand. I[ellipses] I'm just a brand-new teacher. You're a Gym Leader--a Champion--a sensation! Why are {i}you{/i} in Kobukan?"

iono @grinmouth smugbrow "Because I'm a lifelong learner. Education is my passion!"

kris @talking2mouth "Iono[ellipses] in my class[ellipses] Iono[ellipses]"

iono @disgustedbrow talking2mouth "Y-yeah[ellipses]"

pause 1.5

show kris:
    xpos 0.33
    ease 0.5 xpos 0.5

show iono surprisedbrow surprisedmouth with dis:
    xpos 0.66 xzoom 1
    ease 0.2 xpos 0.85

kris happybrow @happy "Iono!"

iono @surprisedmouth "Woah, yes, hello, welcome to my personal space, can I help you?! C'mon, Iono Zoner, you know the rules! No touchy!"

show kris:
    xpos 0.5
    ease 3.0 xpos 0.33

kris -frownmouth -happybrow @happy "No, this is[ellipses] this is just such an honor. I'm sorry, I couldn't control myself."

iono @talking2mouth "It's alright!"
iono neutralbrow neutralmouth @disgustedbrow disgustedmouth "I am aware of the effect I have on women."

show iono behind kris with dis:
    xpos 0.85 xzoom 1
    ease 0.5 xpos 0.66 xzoom -1

iono @talkingmouth "I guess you're a big fan of my streaming career, then?"

kris @talking2mouth "Oh, well[ellipses] I think I'm a bit older than your target demo, but your engineering work is a {i}massive{/i} inspiration to me."
kris @happy "You made a better Poké Ball than the industry standard when your were {i}fourteen!{/i} I handcraft all my Poké Balls, and I still follow {i}your{/i} method."

pause 1.0

kris @talking2mouth "You've got a rare mind, Iono. You may be the next Bill--maybe even the next Professor Oak."

pause 1.0

kris @surprisedbrow talking2mouth "Wait, no[ellipses]"
kris @happy "You'll be the {i}first{/i} Iono."

iono embarrassedeyebrow embarrassedmouth blush @embarrassedeyebrow talking2mouth blush "Whozawatzit[ellipses]? You're talking like I was some kind of childhood inspiration to you. You're probably older than me."

kris @happy "Maybe not a {i}childhood{/i} inspiration. But who says only children can be inspired? I'm definitely an adult now, but I'm still inspired by you."

pause 1.0

redmind @sadbrow "She seems speechless[ellipses]"

red @talkingmouth "Hey, Iono, you wanted to ask Professor Cherry something, right?"

iono @surprisedbrow talking2mouth "Oh. Oh, right!"
iono neutralbrow neutralmouth -blush @grinbrow grinmouth "Doc, since I'm transferring in late, I need a starter Pokémon! You got any bzzt-y buddies for me?"

#FIX THIS IF/WHEN TIA AND SILVER GET THEIR STARTERS

kris @talkingmouth "Oh[ellipses] I {i}do{/i} have a couple. One of them was unclaimed, and the other just reappeared in my lab suddenly, but I'm not sure how well they'd work for you."
kris @closedbrow talking2mouth "I have an Oricorio here, but it's Pa'u Style, not Pom-Pom. The other one is a Totodile."

red @confused "Wait, sorry, 'reappeared'?"

kris @surprisedbrow talking2mouth "Yes, it was {i}really{/i} strange. My lab was broken into, but nothing was taken. Instead, this Totodile's Poké Ball was just sitting on my desk."

red @confused "Someone broke into your lab to[ellipses] leave a Pokémon behind?"

kris @sadbrow talkingmouth "I can't understand it, either. Perhaps they {i}really{/i} don't like Totodile? Or thought they couldn't raise it themselves[ellipses]?"

if (GetRelationshipRank("Silver") > 2):
    narrator "You suddenly remember Silver's policy of not catching or owning any new Pokémon, and wonder if there's a connection there[ellipses]"

    $ ValueChange("Silver", 3, 0.1)

iono @sadbrow talking2mouth "That's[ellipses] 'm I gonna have to learn to train a Totodile, then?"

kris @talking2mouth "No, I don't think so. I've held onto it for a while, hoping whoever its true trainer is comes back. I think we can work out something better."

pause 1.0

kris @talkingmouth "See, I have a Rotom of my own. 'Rotee.'"
kris @happy "It's very energetic, and very smart, too. Plus, it's about level [AimLevel()], which is right on-track for this year of overachieving {i}wunderkinds{/i}."
kris @sadbrow talkingmouth "Though I suppose I can't make fun, given my own situation."

pause 1.0

show iono surprisedbrow surprisedmouth with dis

kris @talking2mouth "So, what do you think, Iono? Would you trade your Rotonono for my Rotee?"

iono @talking2mouth "Woah, that's allowed?!"

kris @happy "Sure. I'm a teacher at Kobukan. It follows that Rotee is a Kobukan Pokémon. I'm giving you a Kobukan Pokémon to raise and train as your own, just like any other student."
kris @talkingmouth "And it's not favoritism, because we're trading."

iono puppyeyes smilemouth @puppyeyes talking2mouth "Thanks, doc. I, uh[ellipses] I wasn't expecting this at all. I'm, uh, {i}really{/i} grateful. I don't normally use giftmons, but--"

kris @talking2mouth "Not a giftmon. Because it's a {i}trade{/i}. That's something else entirely."

iono @talking2mouth "Yeah[ellipses] Yeah[ellipses]"
iono rotom rotombrowneutral rotommouthneutral angrybrow smilemouth @angrybrow happymouth rotom rotombrowneutral rotommouthhappy "Yeah! Let's do it! Rotonono, you down with this?"

TempCharacter("{gradient=#f00-#00f}Rotonono{/gradient}") "Bzzt! Down like gravity, Just Iono!"

kris @happy "I'll take {i}very{/i} good care of your Rotonono, don't worry! And I know you'll take {i}just as good{/i} care of my Rotee."

iono happy "You gotcha, Doc! We'll both be able to keep track of 'em, anyway, since I'm going to be showing up in classes every day from now on."

kris happy "I can't wait!"

$ PlaySound("audio/07_fanfare.ogg")

pause 1.0

narrator "Iono and Professor Cherry have traded Rotom!"
narrator "[ellipses]or have agreed to, at least. They'll still have to go the trade machine, and sign some paperwork, and stuff. It's a whole process."

scene blank2 with splitfade

pause 2.0

scene hall_B
show iono closedbrow frownmouth 
with splitfade

pause 1.0

red @talking2mouth "You look like you're deep in thought."

iono @talking2mouth "Deeper than a fourteen-year-old's poetry, friendo."
iono neutralbrow frownmouth @talking2mouth "We're going back to the bunker, now?"

red @talking2mouth "Sorry. There's one more thing we need to handle first, if you want to have any chance of graduating."

iono @surprisedbrow talking2mouth "What? Same-turn reinforcements?! Bullshit!"

red @talking2mouth "Neither bull, nor shit. You can't just blow off the Quarter Qlashes and expect to graduate like anyone else."

iono @sadbrow talking2mouth "Wot? Like, that's a rule? Certified, stamped, notarized, branded in red?"

red @closedbrow talking2mouth "'Fraid so. The bright side is Dean Drayden has made a {i}lot{/i} of exceptions to this rule. I'm sure he's got one more in him."

iono @sadbrow frownmouth "[ellipses]"

pause 1.0

iono @talking2mouth "I[ellipses] don't have an excuse."

red @confused "Maybe not, but you probably have an explanation, right?"

iono @sad2eyes embarrassedeyebrow talking2mouth "Not a {i}good{/i} one[ellipses]"

red @sadbrow talkingmouth "Well, I've got some good news. Whether you think it's a good explanation or not doesn't matter. It's up to Drayden, and I've never known him to--"

scene draydenoffice
show iono surprisedbrow:
    xpos 0.33 xzoom -1
show drayden:
    xpos 0.66

drayden "That is a terrible explanation."

iono @surprisedbrow "[ellipses]"

red @talking2mouth sweat "Yeah, no, I'm kinda with Dean Drayden here. Sorry."

iono sadbrow frownmouth @sadbrow talkingmouth "Okay, I {i}know{/i} it's not a good one, but[ellipses] I promised Lisia I'd co-MC with her! But I[ellipses] couldn't[ellipses] make it out[ellipses] because[ellipses] you know. My condition."

pause 1.0

drayden "You believed you could not fulfill your duties as a Kobukan student and a co-MC for the Quarter Qlashes at the same time. So you 'bailed' on both of them, as Iris might say."
drayden @sadbrow "And, in this situation, you did not seek to ask Nurse Miriam or I for help."

iono @embarrassedeyebrow sad2eyes talking2mouth "I[ellipses] y'know, didn't want to cause any trouble[ellipses]"

if (IsDate(month=6)):
    drayden @closedbrow "And in your avoidance of immediate conflict, you find yourself in the unenviable position of a {i}far more dire{/i} one a month later, asking me to make an exception to the rules with, frankly, little justification."
elif (IsDate(month=5)):
    drayden @closedbrow "And in your avoidance of immediate conflict, you find yourself in the unenviable position of a {i}far more dire{/i} less than a month later, asking me to make an exception to the rules with, frankly, little justification."
else:
    drayden @closedbrow "And in your avoidance of immediate conflict, you find yourself in the unenviable position of a {i}far more dire{/i} months later, asking me to make an exception to the rules with, frankly, little justification."

drayden "You are aware, of course, I cannot admit you into the Quarter Qlashes. That is under the Kobukan Region's jurisdiction." 
drayden "All I can do is waive the graduation requirement that you participate in as many rounds as your competence allows."

iono @sadbrow talking2mouth "Yeah, I know."

pause 1.0

drayden "Mr. [last_name], do you believe Miss Iono here deserves another chance?"
drayden @angrybrow "Consider leniency here will doubtlessly push one other student, who may have tried harder, who may have studied harder, and may have {i}needed{/i} Kobukan more, out of the ranks of your graduating class."
drayden "Iono's graduation could harm a friend. It could even harm {i}you.{/i}"
drayden @unamusedeyebrows "And[ellipses] one may be forced to ask what a Champion and Gym Leader needs with a degree from Kobukan. Perhaps that 'graduation slot' will better serve someone else."

pause 2.0

iono @sadbrow talking2mouth "{i}Señor{/i}, please. I[ellipses] I want to be normal. I want to be a normal student. Nothing weird about me. No special accommodations, no special circumstances, just[ellipses] a normal Iono."
iono @talking2mouth "I can't be a normal student if I know there's no way I'm graduating."

red @talking2mouth sweat "I'll be honest, Sir, I hadn't really thought about what giving Iono the chance to graduate would mean for me or my friends. And you've given me a lot to think about it."
red @sweat sadbrow talkingmouth "But at least, before I change my mind, I think[ellipses] since Bianca Vongole, Sonia, Raihan, Sabrina, Cheren, Melody, and, y'know, {i}I{/i} got a second chance, in so many different ways[ellipses]"
red @talking2mouth "I think Iono should have one too."

pause 1.0

drayden @closedbrow "It's exactly this recurrent softheartedness of mine that aggrieves the board to no end."

pause 1.5

drayden @angrybrow "I am unprepared to make a decision at this time, Miss Iono."

iono @sadbrow frownmouth "[ellipses]"

pause 1.0

drayden @closedbrow "However. My answer will undoubtedly be an adamant 'no', unless you fulfill a very specific condition."

iono @impressedbrow talking2mouth "Huh? Oh, of course, Sir! Whatever you want! Rope? Bombs? It's yours, my friend!"

drayden @sadbrow "[ellipses]"
drayden "I would have you apologize to Miss Lisia. Being forced to handle the announcing of the first Quarter Qlashes alone, on such short notice[ellipses]"
drayden @sadbrow "She may have had less control over her interviews than she normally maintains, and the consequences of that, though indirect, were[ellipses] impactful."

redmind @surprisedbrow frownmouth "Oh, shit. Iono doesn't know about Bianca's interview, right? Is she responsible for--"
redmind @closedbrow sweat frownmouth "No. No, she isn't. That's not her fault at all."
redmind @sad2eyes sadeyebrows frownmouth "...Very, {i}very{/i} indirectly at fault, at worst."

iono deadeyes surprisedeyebrows surprisedmouth deadpink7 deadteal7 "[ellipses]"

pause 1.0

red @closedbrow talking2mouth "Oh, shit, she broke while I was thinking to myself."

iono @sadbrow talking2mouth "Wait, apologize? Like, face-to-face? No script, no ukulele, no plain white background, no Lillipup?"

drayden @angrybrow "That is {i}exactly{/i} what I mean, Miss Iono."
drayden @closedbrow "I believe Miss Lisia is at the Contest Coliseum at present--so it's on your way."

iono closedbrow frownmouth @talking2mouth sadbrow "Wait, that'd[ellipses] that'd blow my cover, right? 'Normal students' don't have conversations with the World Contest Champion."

red @talking2mouth "Calem jumped off the bleachers to talk to her, and offer her a job. No-one's given that a second thought. You'll be fine."

drayden @angrybrow "On that note, I'd like to make clear I'm a tad miffed at that. He very much did not have the authority to do what he did." 
drayden @sadbrow "On the other hand, he cut through what would doubtlessly have been a year's worth of background checks and tense salary negotiation. The boy has a talent. I should have HR reach out to him[ellipses]"

red @talking2mouth "Thanks for meeting with us, Dean Drayden. I'm sure Iono will do her best to prove she's worth giving a second chance to."

drayden "My mind is open, and I expect this proof is obtainable through the course of being... 'a normal student.'"
drayden @happybrow "I'll be chatting with Lisia somewhat soon. I expect she'll mention you."

iono @talkingmouth "I'll show you I'm worth it. Thanks, Daddy-o."

hide iono
show drayden sad 
call clearscreens() from _call_clearscreens_248
with dis

narrator "You and Iono depart."

TempCharacter("{color=#583C68}Daddy-o{/color}") "Please do not call me that."

show drayden -sad with dis:
    xpos 0.66
    ease 0.5 xpos 0.33

pause 2.5

show anabel with Dissolve(2.0):
    xpos 0.66 matrixcolor BrightnessMatrix(-1) blur 3.0

pause 1.0

drayden "Anabel."

show anabel:
    matrixcolor BrightnessMatrix(-1) xpos 0.66 blur 3.0
    ease 0.5 matrixcolor BrightnessMatrix(0) blur 0

if (HasEvent("Iono", "NateHologram")):
    anabel @talking2mouth "That girl has the agency's technology."

    drayden "I imagine she has a great many things she should not."

else:
    anabel @talking2mouth "You are aware of that girl's status?"

    drayden "I believe myself to be."

    anabel @talking2mouth "She is lying about her very presence."

    drayden @closedbrow "I imagine she is lying about a great many things--more than she, I, or even {i}you{/i} are aware of."

anabel @talking2mouth "You'll extend a chance to her, regardless?"

drayden "To her, I'll extend the chance to {i}earn{/i} her {i}own{/i} chance."
drayden @closedbrow "Her struggles are internal--I can, at the least, not interfere by threatening to withhold her graduation."
drayden @sadbrow "Though I've no mind to {i}reveal{/i} that to her, just yet."

anabel @talking2mouth "You bend yourself backwards for these children. From the point of view of a risk-assessment analyst[ellipses]"
anabel @talking2mouth "You'll burn yourself out before but a handful of your investments mature."

drayden @closedbrow "Certainly. But as my flame burns to nothing, I know so many others will take it up in my stead."

pause 1.0

anabel @sadbrow talkingmouth "You are frustratingly high-minded."

drayden @happy "Comes with the territory, I'm afraid. One doesn't ascend to Kobukan's deanship without the ability to spout more quasi-wise sayings than the average sack of fortune cookies."
drayden "On that note, business as usual, tonight? Or may I finally tempt you to Inspira's sushi scene?"

anabel talking2mouth "Business as usual tonight, Dean Drayden."

show anabel:
    matrixcolor BrightnessMatrix(0) xpos 0.66 blur 0.0
    ease 0.5 matrixcolor BrightnessMatrix(-1) blur 3.0

anabel @talking2mouth "But {i}do{/i} keep asking."

scene blank2 with splitfade

pause 2.0

show concerthallstage
show iono frownmouth:
    xpos 0.33
show lisia incognito:
    xpos 0.66
with splitfade

lisia @talkingmouth "Nah, it's fine, Io."

iono @talking2mouth "Uh[ellipses] you're not mad? Like, not even a l'il bit? Not even a teeny-weenie itsy-bitsy little-bitty mad?"

lisia @sadbrow talkingmouth "I wasn't really happy at the time, but I understand. Sometimes everyone just needs to disappear from everyone who knows them and be a ghost for a while, right?"

redmind @closedbrow frownmouth "I think that might be a very {i}specific{/i} point of commonality, but[ellipses] hey, at least she's not mad."

lisia @happybrow happymouth "I mean, look what I'm wearing! I'm hiding from a {i}lot{/i} of people right now. I can't be a hypocrite about this, right?"

pause 1.0

lisia @talkingmouth "Hey, Io. You haven't been beating yourself up over this ever since the first round of the QQs, have you?"

iono @rolleyes worriedeyebrow talking2mouth "No. 'Course not."

lisia @talkingmouth "I'm glad. So, you're a Kobukan student now. That's {i}huge{/i}. Since you're on-campus, you'll join me for announcing the other QQ rounds, right?"

iono neutralbrow neutralmouth @sad2eyes talking2mouth "Er, well[ellipses] maybe[ellipses] no promises?"

lisia @talkingmouth "Alright. I'll ask again later."
lisia @happybrow happymouth "I'd love to stay and chat, but--"

iono @happybrow talking2mouth "Completely fine, I talked to {i}four{/i} people today, and I'm exhausted. I'm going to bed early, and I'm going to sleep for a {i}week!{/i}"

lisia @talkingmouth "Alright. We'll catch up later."

pause 1.0

lisia @sadbrow talkingmouth "Oh, and, Io[ellipses] you can delete all those emails from me. I was just checking on you. I don't need a response, now that I know you're alright."

iono sadbrow frownmouth @sadbrow talking2mouth "I[ellipses] alright[ellipses]"

redmind @thonk "Huh. Iono's flagging fast. We should get back to the bunker soon."

call clearscreens() from _call_clearscreens_249
scene blank2 with splitfade

pause 1.0

scene concerthallhallway
show iono closedbrow frownmouth
with splitfade

pause 1.0

iono @closedbrow talking2mouth "Mmmmrpmph. Carry me, [first_name]."

red @talking2mouth unamusedbrow "I'm not doing that."

iono @angrybrow talking2mouth "I'm so light, though. I'm {i}literally{/i} light."

red @talking2mouth "Yeah, I bet you are, but your tiredness shouldn't affect how hard it is for you to get to your bunker."

pause 1.0

red @confused "Hey. When we brought that stuff to repair your I-Balls, you[ellipses] led us {i}right{/i} to your bunker. But preventing people from knowing where you {i}are{/i} is[ellipses] like, your number-one thing, right?"

pause 1.0

iono confusedbrow frownmouth @talking2mouth confusedbrow "Yeah[ellipses]"

red @talking2mouth "But you led us {i}right{/i} to where you, physically, are."

pause 1.0

red @unamusedbrow talking2mouth "Unless you didn't."

pause 2.0

red @sadbrow talkingmouth "Don't tell me you built a decoy bunker."

iono @winkbrow teeheemouth "{i}I{/i} didn't {i}build{/i} {i}a{/i} {i}decoy{/i} {i}bunker{/i}."

red @talking2mouth "The only word in that sentence you did not suspiciously enunciate was 'didn't.'"

iono @winkbrow talking2mouth "I'll de-emphasize another one if you carry me."

red @unamusedbrow talking2mouth "What would you get out of it? Good an engineer as you are, I'm pretty sure your I-Balls don't have a sense of touch."

pause 1.0

iono @closedeyes worriedeyebrow talking2mouth "[ellipses]No. But I like to pretend."

pause 1.5

iono neutralbrow neutralmouth @talkingmouth "Thanks for taking me around the school today."

red @sadbrow talkingmouth "Thanks for being brave enough to[ellipses] well, not exactly {i}leave{/i} your comfort zone, but[ellipses] y'know."

pause 1.0

iono @closedbrow talking2mouth "Professor Oak, Doc Cherry, Dean Drayden, Lisia[ellipses]"
iono @talking2mouth "All of them were so nice to me."

red @talkingmouth "I know a lot of people who would {i}really{/i} argue with me about this, but[ellipses] I think people are nice."
red @sad2eyes sadeyebrows talkingmouth "I can't tell you your fears aren't real. I don't know what they are. But the people here--and, I think, the people wherever you find yourself--won't be as bad as they could be."

pause 1.0

iono @talking2mouth "Meatspace is[ellipses] not as bad as I thought it was. It {i}was{/i} exhausting, though. I need a save point[ellipses]"

red @happy "Well, no denying that. But it's the kind of tiredness that comes at the end of accomplishing something. Maybe[ellipses] sleepy, instead of tired, you know? Different vibes."

iono "[ellipses]"

pause 1.0

iono @talkingmouth "Thank you, [first_name]."

red @confusedbrow talkingmouth "What?"

iono @sad2eyes smugeyebrow talkingmouth "I'm still pretty sure you're trickin' me somehow, but... being your escort quest NPC made me feel normal, for once. And[ellipses] I dunno, but I feel like maybe everyone was so nice to me 'cause you were there."

pause 1.0

iono @talkingmouth "You've shown me your world. And meatspace doesn't suck."
iono angrybrow smilemouth @angrybrow talkingmouth "But you better butter up your beefy butt, because as thanks, I'm going to show you {i}my{/i} world. And you're never going to want to go into meatspace again, once you see what {i}I've{/i} got for you."

red @talking2mouth "Hm? What do you mean?"

iono @winkbrow happymouth "I mean that you are being cordially, formally, officially, professionally, and entirely invited to join me for my stream--{w=0.5}I INTERVIEWED THE SLAYER OF THE JOBBIRD?! SHOCKING SECRETS?!"

red @talkingmouth "Maybe work on the title."

iono @rolleyes talking2mouth "Yeah, I should definitely put the word 'drama' in there, somewhere. Drama's trending right now."

red @closedbrow talking2mouth sweat "{size=30}When {i}isn't{/i} it?{/size}"

iono @winkbrow happymouth "Alright-y. It's been super-fun collabing with you, [bluecolor]friendo{/color}. Drop by my bunker again! I'll want to chat and stuff."

red @sadbrow talkingmouth "You can also just[ellipses] you know, {i}leave{/i} your bunker. And maybe {i}you{/i} visit {i}me?{/i}"

iono puppyeyes frownmouth "[ellipses]"

red @wince talkingmouth "Well[ellipses] baby steps."

iono neutralbrow smilemouth @happybrow talkingmouth "Um[ellipses] bye. Friendo."

red @happy "See you in classes."
red @sadbrow talkingmouth "And, hey--{i}my{/i} door's always open."

hide iono with dis

$ RelationshipRankUp("Iono", "Friendo", 1)

return