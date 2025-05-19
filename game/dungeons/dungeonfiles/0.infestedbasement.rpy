#######SETUP###########

label infestedbasement:

python:
    isgame = True
    dungeon = Dungeon(name = "Infested Basement",#a string
        endname = "Griseous Cellar",#a string
        backgrounds = {"Default": "catacombs3"},#a dictionary of timeofdays to check against. If the current timeofday is not listed, then the "Default" value is picked.
        music = ("audio/music/sealedruin.ogg"),#a tuple that contains one or two elements. If it contains two, the first is nolooped, and the second is looped. if it contains one, then it's looped
        encounterpool = {# a dictionary encounterpool, in the same format as the ones for normal wildareas
            pokedexlookupname("Weedle", DexMacros.Id): 10, 
            pokedexlookupname("Paras", DexMacros.Id) : 10, 
            pokedexlookupname("Nymble", DexMacros.Id) : 10,
            pokedexlookupname("Tarountula", DexMacros.Id): 10,
            pokedexlookupname("Rattata", DexMacros.Id): 10,
            pokedexlookupname("Grimer", DexMacros.Id): 10,
            pokedexlookupname("Ekans", DexMacros.Id): 10,
            pokedexlookupname("Sandshrew", DexMacros.Id): 10,
            pokedexlookupname("Zubat", DexMacros.Id): 10,
            pokedexlookupname("Venonat", DexMacros.Id): 10,
            pokedexlookupname("Skorupi", DexMacros.Id): 10
        },
        difficulty = 14,#an int, 1-100, indicating the dungeon's difficulty. Should be roughly equivalent to AimLevel()
        floors = 4,#the number of battles you need to win to go through the level
        floorlength = 3,#the number of turns a battle will last, at max, before you find the stairs
        levelrange = range(10, 15),#a level range, set up the same way as normal wildarea level ranges
        startingmysteriosity=50,#the base chance that mysteriosity happenings will occur
        startingferocity=1,#the base chance that strong Pokémon will appear
        startinggenerosity=100,#the base chance that good things will happen
        trainers=["Leaf", "Ethan", "Yellow"],# the trainers you start this dungeon with, not counting red
        cutscenefunc=InfestedBasementCutscenes,#the function that returns the cutscene labels you should jump to
        godmodder=InfestedBasementGodmodder,#manually calls events and outcomes if certain conditions are met
        lootlist = { })#the dictionary of loot that you should get from this

call wildarea(dungeon) from _call_wildarea_9

return

######GODMODDER & CUTSCENES###########

init python:
    def InfestedBasementGodmodder(parameters):
        if ("Outcome" in parameters):
            if (dungeon.GetCurrentFloor() == 1):
                return Outcomes.Nothing#have no mysteriosity events occur in the first encounter
            elif (dungeon.GetCurrentFloor() == 2):
                if (Turn == 1 and "TutorialBuffFoes" not in dungeon.EventHistory):
                    return Outcomes.Bad#make sure the first turn has a scheduled 'buffenemies' flux
                else:
                    return Outcomes.Nothing#otherwise, nothing
            elif (dungeon.GetCurrentFloor() == 3):
                if (Turn == 1 and "TutorialGetLoot" not in dungeon.EventHistory):
                    return Outcomes.Good#make sure the first turn has a scheduled 'buffenemies' flux
                else:
                    return Outcomes.Nothing#otherwise, nothing

        elif ("Event" in parameters):
            if (dungeon.GetCurrentFloor() == 2):
                if (Turn == 1 and "TutorialBuffFoes" not in dungeon.EventHistory):#after the first allied pokemon makes its first move
                    return "TutorialBuffFoes"
            elif (dungeon.GetCurrentFloor() == 3):
                if (Turn == 1 and "TutorialGetLoot" not in dungeon.EventHistory):#after the first allied pokemon makes its first move
                    return "TutorialGetLoot"

        return None

    def InfestedBasementCutscenes(parameters):
        currentscene = None
        if (parameters == "DungeonTurn1"):
            currentscene = "InfestedBasementIntro"
        elif (parameters == "DungeonTurn2"):
            currentscene = "InfestedBasement1"
        elif (parameters == "PostDungeonEvent" and dungeon.GetCurrentFloor() == 2 and Turn >= 1):
            currentscene = "InfestedBasement2"
        elif (parameters == "DungeonTurn3"):
            currentscene = "InfestedBasement3"
        elif (parameters == "PostDungeonEvent" and dungeon.GetCurrentFloor() == 3 and Turn >= 1):
            currentscene = "InfestedBasement4"
        elif (parameters == "DungeonTurn4"):
            currentscene = "InfestedBasement5"
        elif (parameters == "DungeonBattle4"):
            currentscene = "InfestedBasement6"

        if (currentscene != None and currentscene not in seencutscenes):
            seencutscenes.append(currentscene)
            renpy.hide_screen("battle")
            renpy.hide_screen("dungeonpartyviewer")
            renpy.call(currentscene)

label InfestedBasementIntro:
    pause 3.0
    
    show blue with Dissolve(1.0)

    blue @talkingmouth "What're you gawking at?"

    red @surprised "This is more in-depth than I expected. Like, wow, you put a lot more effort into this than I thought you would."

    blue @happy "Heh. {i}Pokémon Mystery Dungeons & Dragons{/i} is one of the most hardcore military strategy games out there. Just wait until we get to the grappling rules."

    show yellow at rightside with dis

    yellow @talking2mouth "Whenever I GM, I tend to go a bit more rules-light, but..."

    blue @angrybrow talkingmouth "But the rules {i}exist for a reason{/i}."

    yellow happy "You're right."

    hide yellow with dis

    pause 1.5

    blue @talkingmouth "Alright."

    pause 0.5

    blue @closedbrow talkingmouth "You awake in a musty dungeon. Your head throbs and your breath is visible in the dank air."

    ethan @closedbrow talkingmouth "{size=30}Heh.{/size}"

    blue @talking2mouth "The mossy stone that your environs are made of is wet and clingy to the touch--your head is pounding, and memory escapes you."

    leaf @closedbrow talkingmouth "Sounds like last night was a good time."

    ethan @sadeyebrows talkingmouth "Guess we couldn't hold our ye olde ale."

    blue @talkingmouth "The last thing you remember is hearing a woman screaming for help."
    blue @closedbrow happymouth "Bereft of other clues, you decide you need to figure out how to get out of here."
    blue @angrybrow talkingmouth "One path presents itself to you immediately... {i}forward{/i}."

    hide blue with dis

    return

label InfestedBasement1:
    red @talkingmouth "Neat. I've never been in a battle with four to a side before. Range becomes even more important in that kind of battle, huh?"

    show blue with dis

    blue @closedbrow talkingmouth "{i}Now{/i} you get it. Positioning is {i}everything{/i} when you're out on a {i}real{/i} battlefield. Superior forces can get totally wiped out if they don't have room to maneuver."

    leaf @sarcastic "Yeah, alright, Instructor Surge. Save the war stories, I know you came from the boonies, like [first_name]."

    ethan @talking2mouth "...Hey, what are those other options? The one about surveying your surroundings, and checking in with your party?"

    blue @talking2mouth "They're more mechanics. We'll talk about 'taking stock of your environment' later, but for now I'll just tell you about 'checking in on your party.'" 
    blue @talking2mouth "Between battles, you can reorganize your party--change the order of the Pokémon in your party members' teams, and shift party members' positions."
    blue surprisedbrow frownmouth @neutraleyes talking2mouth "Marching order matters a ton. You want Pokémon that can handle a lot of damage to be in the center of your formation, since they're the ones who will be hit the most often."

    ethan @talking2mouth "Tanks up front, deeps on the wings. Got it."

    blue @talking2mouth "Y-yeah... yeah, you actually {i}did{/i} get it. Huh."

    hide blue with dis

    return

label InfestedBasement2:
    hide screen battle
    hide screen battleui

    show blue with dis

    red @surprised "Woah, woah, hold on! Reinforcements will have their attack increased one stage... what do you mean by that?"

    blue @closedbrow talking2mouth "Exactly what it says on the tin. The enemy Pokémon that show up next will hit harder."

    red @confused "Okay. Follow-up question: why?"

    blue @talkingmouth "Because I rolled a seven. Look, the longer you stay on a floor, the tougher the opponents will get." 
    blue @talking2mouth "Your Pokémon will start to get tired out, your opponents will get stronger, and it becomes more likely that something bad will happen to you."

    show yellow with dis:
        xpos 0.75

    yellow @talking2mouth "Dungeons have lots of rewards in them. Potentially {i}infinite{/i} rewards. But... if you wipe out in one, then that's it." 
    
    ethan @closedbrow talking2mouth "{color=#f00}Game over...{/color}" 
    
    blue @talking2mouth "It's never worth going too far for one more lousy coin."

    ethan @talking2mouth "Got it. Here's another question for you--it looks like moves get weaker the more we use them. Is that right?"
    
    blue @closedbrow "Yeah, it's based on the percentage of PP you've got left for that move. You can try spamming the same move over and over, but if it's your most powerful move, by the time you hit the boss, you'll have nothing left."
    blue @talking2mouth "Bring ethers, elixirs, whatever, if you want to use the same move over and over. Or just use your whole party, if you're a cheapass like [first_name]."

    red @upeyes angryeyebrows frownmouth "[ellipses]"

    yellow @talking2mouth "Because it's based on percentage, moves with high PP will keep their power for a lot longer. And status moves aren't affected, of course." 
    yellow @happy "Many people forget the old reliable moves, like Tackle, as soon as they get something better, but... sometimes, Tackle's the best."

    hide blue
    hide yellow
    show screen battleui
    with dis
    return

label InfestedBasement3:
    ethan @talking2mouth "Alright, I was promised exposition on the other mechanics. Mysteriosity? Ferocity? Generosity? At least two of those aren't real words."

    show blue with dis

    blue @talking2mouth "It's simple. The higher your Mysteriosity is, the more likely it is that {i}something{/i} will happen after an ally's turn. Could be good, could be bad--all that matters is that it's something."

    red @talking2mouth "So Ferocity is the chance of a bad thing happening, and Generosity is the chance of a good thing happening?"

    blue @talking2mouth "And the degree of those effects, too. Higher Ferocity makes your bads worse. Higher Generosity makes your goods better."

    leaf @closedbrow talking2mouth "{size=30}Thus perishes the Japanese language.{/size}"

    ethan @talking2mouth "Okay, how do we change these values?"

    blue @talking2mouth "Mostly, you can't. Knocking out opponents increases the dungeon's Ferocity, and enduring Negative Mysterious Fluxes increases the dungeon's Generosity." 
    blue @talkingmouth "So it'll balance out, somewhat, but in the long run, things'll just keep getting worse, no matter what you do."

    ethan @closedbrow talking2mouth "Mood."

    show yellow with dis:
        xpos 0.75

    yellow @talking2mouth "It's not all bad, though. When you go to a new floor in a dungeon, the dungeon's Ferocity is cut in half, no matter how big it was before."
    yellow @talking2mouth "And, um, the dungeon's Generosity gets a little bump, as well. So the start of every floor should be, relatively, easier."

    blue @talking2mouth "Mysteriosity, though... it goes up constantly. And it'll go up faster and faster with every floor." 
    blue @talkingmouth "Even though high Mysteriosity means you have a greater chance of Positive Mysterious Fluxes, a good situation can become a bad one, {i}very{/i} fast, if you're getting Mysterious Fluxes every single turn."

    ethan @talking2mouth "With all this talk about how we shouldn't dawdle on floors, I'm getting the idea that you {i}really{/i} don't want us to try and grind out rewards."

    blue @frownmouth "[ellipses]"
    blue @closedbrow "I mean, I would. But that's just because I'm built different."

    yellow @angrybrow talking2mouth "And because you've got a pocket cleric whenever we take on a dungeon boss."

    hide yellow
    hide blue
    with dis

    return

label InfestedBasement4:
    hide screen battle
    hide screen battleui

    red @talkingmouth "Wait, you {i}actually{/i} gave us Gimmighoul coins? Like, for real?"

    show blue with dis

    blue @closedbrow "Sure. They're a dime a dozen out in the forest. Pretty much anywhere where Pokémon hide out. Don't pretend {i}you{/i} don't know that, [first_name]."

    leaf @surprised "Are Gimmighoul actually that common?"

    show yellow frownmouth at rightside with dis

    yellow @talking2mouth "No, but other Pokémon like to raid their chests."
    yellow @closedbrow talking2mouth "But since they can't do anything with the coins... they end up just carrying the coins to random places and leaving them behind."

    ethan @confused "Wait, is this in the game, or real life?"

    yellow @sadbrow talking2mouth "Real life. It's sad..."

    blue @talkingmouth "If they didn't want their chests to be raided, they'd lock them up better. You see a chest, you take whatever's inside. That's just the rule."

    ethan @sadbrow talking2mouth "Bit harsh."

    blue @angry "Can we {i}move on{/i} from sobbing over nature?"

    yellow -frownmouth @closedbrow talking2mouth "Okay, okay..."

    pause 0.5

    yellow -frownmouth @talking2mouth "Let's talk about the stairs, and reinforcements. As you get further in the dungeon, the chance of finding the stairs at the end of the round increases."
    yellow @talkingmouth "But you can only find them once you've explored at least 50%% of the floor. So if the floor has a length of 'three' then you need to explore at least 'twice' before there's a chance of finding them."

    blue @talkingmouth "Exploring takes one round of combat, obviously. A clean six seconds."
    blue @talking2mouth "If you {i}don't{/i} find the stairs at the end of the round, then more reinforcements will show up for the enemy. They'll start to fill their side of the field, up to six Pokémon at once."
    blue @happy "But if there's already six on the opposing side, then you're {i}really{/i} sunk! Then the wild Pokémon will become {b}reinforced{/b}."

    leaf @sarcastic "Does the power of friendship make them stronger?"

    blue @talkingmouth "Sure does. Knocking them out will replace them with one of their reinforcements immediately, and their stats will increase."
    blue @talkingmouth "If you see the enemy Pokémon gathering enough that they're starting to get reinforcements, you should probably just take the stairs."

    ethan @closedbrow talkingmouth "We'll see. That just sounds like a challenge, to me."

    hide blue
    hide yellow
    show screen battleui
    with dis
    return

label InfestedBasement5:
    show blue with dis

    stop music fadeout 3.0
    queue music "audio/music/reliccastle_start.ogg" noloop fadein 5.0
    queue music "audio/music/reliccastle_loop.ogg"

    blue @talkingmouth "As you make your way through the dungeon, you encounter a snarling, bug-like beast. Its eyes are milky and unfocused, and large fungi seem to be sprouting from its back."
    blue @talkingmouth "This dread beast seems to be at death's door, but it still seems to be trying to pick a fight with you."
    blue @talking2mouth "You notice that it has a great many of its festering brood at its feet... it seems {i}very{/i} strongly reinforced."

    show yellow with dis:
        xpos 0.75

    yellow @talking2mouth "Most dungeons have a 'boss' at the end. If a boss is blocking your way, you can't take the stairs, even if you can find them."
    yellow @angrybrow talkingmouth "Bosses also tend to come with a lot of reinforcements, meaning even with a lot of type advantage, you can't beat them easily!"

    ethan @confused "Hold on. Didn't you say that reinforcements buff an enemy's stats, too? If it comes in with, like, 20 reinforcements, won't it have absolutely {i}insane{/i} stats?"

    yellow @talking2mouth "Not for bosses. They don't get the massive stat boost, just a smaller one. However, the amount of damage you can do to them at one time is capped, based on the number of reinforcements."

    blue @closedbrow talking2mouth "One-shotting a big boss is lame. You gotta {i}work{/i} for that shit."

    yellow @happy "Landing super-effective hits on bosses will break away their reinforcements, though. It's not much, but it helps... a bit."

    yellow @talkingmouth "Bosses also have a bunch of other benefits... they can clean themselves of status conditions, become invulnerable for a while, move twice a turn, or other things..."
    
    blue @closedbrow "But this is a tutorial boss. I'm not going to wipe a bunch of first-timers in a one-shot."

    hide blue
    hide yellow
    with dis

    return

label InfestedBasement6:
    python:
        goodguys = dungeon.GetTrainers()
        parasectboss = Pokemon("Parasect", 25, moves=["Spore", "Cross Poison", "Leech Life", "Leech Seed"])
        parasectboss.Status["tyrannic"] = 1
        sidemonnum = pokedexlookupname("Parasect", DexMacros.Id)
        reinforcements = [Pokemon("Paras", 15)] * 10
        badguys = [Trainer("sideportraitfull", TrainerType.Enemy, [parasectboss] + reinforcements, 1, isPokemon=True)]

        renpy.call("Battle", goodguys + badguys, uniforms=False, customoutfits=False, healParty=False, specialmusic="Nothing", canBeDitto=False, dungeon=dungeon)

    return

###########CUSTOM EVENTS CALLED BY GODMODDER############

label TutorialBuffFoes:
    python:
        stat = RandInt(Stats.Attack, Stats.Attack)
        stages, stagesstr = dungeon.BadMagnitude(1, 1)
        dungeon.AddFloorEvent(stat, stages + dungeon.GetEventValue(stat))

    dn "The wild Pokémon grow more feral! Reinforcements will have their [StatToString(stat)] increased [stagesstr] [cp(stages, 'stage')]!"

    return

label TutorialGetLoot:
    python:
        coinsfound, coinsfoundstr = dungeon.GoodMagnitude(10, 10)
        GetItem(Item.GimmighoulCoin, coinsfound, hidefanfare=True)
    
    dn "You stumbled upon [coinsfoundstr] Gimmighoul Coins!"

    return