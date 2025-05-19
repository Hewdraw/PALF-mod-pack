label lunch010602:

show klara uniform:
    xpos 0.66

show leaf uniform:
    xpos 0.33 xzoom -1

leaf @sadbrow talkingmouth "{gradualsize=20-36}N-no, that'd be great!{/gradualsize} I'd love that!"

klara @sadbrow talkingmouth "Are you sure? Because I don't want you to feel uncomfortable. I know you're not really used to parties, so--"

leaf @happy "What? No, I'm--{w=0.5}I'm totally down to party! I'm a total party girl. They called me the party queen back in Goldenrod. I mean, I {i}just{/i} planned a party, and--"

klara surprisedbrow frownmouth @surprisedbrow talking2mouth "You... planned a party?"

leaf frownmouth @surprisedbrow talking2mouth "Oh. Um, yeah."

klara sadbrow frownmouth @sadbrow talkingmouth "I... guess I wasn't invited? I mean, you were the first person I invited to {i}this{/i} party..."

leaf surprisedbrow frownmouth @surprised "Oh, well, it was, like, um, kinda a private thing, and it was a birthday, but also kinda a 'sorry your father was killed' party, and that kinda had a very specific vibe, and[ellipses] and[ellipses]"

pause 1.0

leaf -surprisedbrow -frownmouth @happy "Hey, [first_name]!"

show klara surprisedbrow with dis

pause 0.2

show klara:
    xpos 0.66
    ease 0.5 xpos 1.1

red uniform @talkingmouth "Hey, Leaf. What's up?"

leaf surprisedbrow frownmouth @happy "Oh, Klara just invited me to her sorority's party, and--"

pause 1.0

leaf -surprisedbrow -frownmouth @sadbrow talkingmouth "I swear Klara was right here."

red @happy "I believe you."
red @talkingmouth "So, a party, huh? That's big. Must be nice to be invited to something {i}you{/i} didn't plan, for once."

leaf @sadbrow talkingmouth "It actually kind of is, yeah."
leaf @happy "Not that I mind being the planner, but, you know, even tailors need clothes."

red @talkingmouth "Not nudist tailors."

leaf @flirtbrow talkingmouth "I need you to think {i}hard{/i} about who the clientele for a nudist tailor would be."

red @frownmouth upeyes "Hmm..."
red @closedbrow happymouth "Got it. A foolish emperor who needs new clothes."

leaf @talkingmouth "Oh, damn, that's clever."

red @winkbrow talkingmouth "Mama [first_name] didn't raise no fool."

leaf @happy "Yeah, but she {i}did{/i} raise a massive dork."

red @talkingmouth "Interested in bringing a dork as your plus one to the party, then?"

leaf @winkbrow talkingmouth "You'd have to get surgery pretty quickly. It's girls-only."

red @surprisedbrow frownmouth lightblush "[ellipses]"

leaf @talkingmouth "Now, {i}that's{/i} a fun expression. What I'd give to be able to read your mind right now..."

if (GetRelationshipRank("Sabrina") > 0):
    redmind @surprisedbrow frownmouth "[sabrinacolor]It's not as pleasant as one might think.{/color}"

red @closedbrow talking2mouth sweat "So, yeah, girls-only party. I assume you're going to have pillow fights in your underwear, eat soft cheeses, and talk about boys?"

leaf @flirtbrow talkingmouth "Duh. What else do girls do?"

red @talkingmouth "Curse my pick of the genetic lottery. I'm just one chromosome away from heaven."

leaf @talkingmouth "Yeah, lactose intolerance is a bitch. No soft cheese for you."
leaf @sadbrow talkingmouth "Genetics, though. What can you do?"

red @happy "Now {i}that's{/i} a surgery I'd get."

leaf @talkingmouth "Sign me up, first!"

hide leaf with dis

jump PickTable