label lunch010531:

show serena uniform:
    xpos 0.33

show brendan uniform:
    xpos 0.66

serena @talkingmouth "Which of your Pokémon do you think you will be using in the Millennium Drop, Brendan?"

brendan @happy "It's gotta be my Wailmer! It's the only one that makes sense. He's from Hoenn, he's a Water-type, {i}and{/i} he's cute!"

serena @talkingmouth "Hm? You think that those attributes will help?"

brendan @talkingmouth "Totally. The Millennium Drop is based on a Hoennian festival, so the audience is going to want to see Hoennian Pokémon."
brendan @happy "The judges are a Water-type specialist, a Ghost-type specialist, and a Flying-type specialist, so the audience is going to want to see Ghost, Water, and Flying-types."
brendan @talkingmouth "Finally, Water as a type is associated with the Cute and Beautiful contest types, so the audience is going to want to see more of that!"

serena @closedbrow talking2mouth "Hm... so appealing to the audience is a necessary part of the performance as well..."

brendan sadbrow @talkingmouth "Always is. But here in Kobukan, they actually give you points based on how popular your Pokémon is with the audience."

serena sadbrow @talking2mouth "I suppose that means that this won't be my dear Rhyhorn's time to shine, then..."

$ sidemonnum = pokedexlookupname("Rhyhorn", DexMacros.Id)
$ PlaySound("pokemon/cries/{}.mp3".format(sidemonnum))
sidemon "Rhy..."

brendan happy "Don't worry, Rhyhorn! A Lairon won the '02 Meteor Smash Earth Rock Rumpus. There's a competition for every type of Pokémon... you'll get your chance one day!"

hide brendan 
hide serena
with dis

red uniform @closedbrow talking2mouth "Hm... seems like the audience is looking for some pretty specific Pokémon."

if (starterobj in playerparty):
    $ DisplayPokemon(starter_species_name)

    python:
        starter_contest_trait = pokedexlookup(starter_id, DexMacros.ContestTrait)

    red @confused "Let's see... looking at you, I think I'd say you're... [starter_contest_trait]!"

    $ HidePokemon()

narrator "[bluecolor]To view a Pokémon's contest trait, look them up in your Mental Pokédex.{/color} Every species has a different one, and they often change when they evolve!"

jump PickTable