label PickPokemon(choices):#can be a list of ids, or the string "all", or a string of a "Type", or a string of "electives"
    $ beenthrough = False
    hide blank2
    show blank2 with dis:
        alpha 0.8

    label startchoice:

    python:
        alllist = [
            pokedexlookupname("Lillipup", DexMacros.Id),
            pokedexlookupname("Dunsparce", DexMacros.Id),
            pokedexlookupname("Audino", DexMacros.Id),
            
            pokedexlookupname("Charmander", DexMacros.Id),
            pokedexlookupname("Darumaka", DexMacros.Id),
            pokedexlookupname("Heatmor", DexMacros.Id),
            
            pokedexlookupname("Mudkip", DexMacros.Id),
            pokedexlookupname("Buizel", DexMacros.Id),
            pokedexlookupname("Wishiwashi", DexMacros.Id),
            
            pokedexlookupname("Turtwig", DexMacros.Id),
            pokedexlookupname("Petilil", DexMacros.Id),
            pokedexlookupname("Maractus", DexMacros.Id),
            
            pokedexlookupname("Mareep", DexMacros.Id),
            pokedexlookupname("Chinchou", DexMacros.Id),
            pokedexlookupname("Rotom", DexMacros.Id),
            
            pokedexlookupname("Spheal", DexMacros.Id),
            pokedexlookupname("Snorunt", DexMacros.Id),
            pokedexlookupname("Cryogonal", DexMacros.Id),
            
            pokedexlookupname("Timburr", DexMacros.Id),
            pokedexlookupname("Riolu", DexMacros.Id),
            pokedexlookupname("Heracross", DexMacros.Id),
            
            pokedexlookupname("Zubat", DexMacros.Id),
            pokedexlookupname("Mareanie", DexMacros.Id),
            pokedexlookupname("Seviper", DexMacros.Id),
            
            pokedexlookupname("Trapinch", DexMacros.Id),
            pokedexlookupname("Drilbur", DexMacros.Id),
            pokedexlookupname("Stunfisk", DexMacros.Id),
            
            pokedexlookupname("Starly", DexMacros.Id),
            pokedexlookupname("Murkrow", DexMacros.Id),
            pokedexlookupname("Tropius", DexMacros.Id),
            
            pokedexlookupname("Ralts", DexMacros.Id),
            pokedexlookupname("Slowpoke", DexMacros.Id),
            pokedexlookupname("Sigilyph", DexMacros.Id),
            
            pokedexlookupname("Sewaddle", DexMacros.Id),
            pokedexlookupname("Nincada", DexMacros.Id),
            pokedexlookupname("Shuckle", DexMacros.Id),
            
            pokedexlookupname("Larvitar", DexMacros.Id),
            pokedexlookupname("Dwebble", DexMacros.Id),
            pokedexlookupname("Minior", DexMacros.Id),
            
            pokedexlookupname("Litwick", DexMacros.Id),
            pokedexlookupname("Misdreavus", DexMacros.Id),
            pokedexlookupname("Mimikyu", DexMacros.Id),
            
            pokedexlookupname("Sandile", DexMacros.Id),
            pokedexlookupname("Sneasel", DexMacros.Id),
            pokedexlookupname("Sableye", DexMacros.Id),
            
            pokedexlookupname("Bagon", DexMacros.Id),
            pokedexlookupname("Noibat", DexMacros.Id),
            pokedexlookupname("Drampa", DexMacros.Id),
            
            pokedexlookupname("Aron", DexMacros.Id),
            pokedexlookupname("Ferroseed", DexMacros.Id),
            pokedexlookupname("Skarmory", DexMacros.Id),
            
            pokedexlookupname("Flabébé", DexMacros.Id),
            pokedexlookupname("Cutiefly", DexMacros.Id),
            pokedexlookupname("Mawile", DexMacros.Id)
        ]
        
        if (choices != "every"):
            if (not beenthrough):
                if (choices == "all"):
                    choices = alllist
                elif (choices in starters.keys()):#if a "Type" string is passed in
                    choices = starters[choices]
                elif (choices == "electives"):
                    choices = list(starters[GetStatRank(0)]) + list(starters[GetStatRank(1)])
            
                random.shuffle(choices)
                choices = choices[0:3]
        else:
            choices = alllist

        beenthrough = True

    call screen pickpokemon(choices, _with_none=False) with dissolve
    $ pkmnid = _return
    with dissolve
    hide blackground
    $ pkmnname = pokedexlookup(pkmnid, DexMacros.Name)
    "You chose [pkmnname]?"

    menu:
        ">Yes":
            return pkmnid

        ">No":
            jump startchoice