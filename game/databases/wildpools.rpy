init 2 python:
    class Wildpool:
        def __init__(self, encounterpool, levelrange, dexbackground, evopool = {}):
            self.encounterpool = encounterpool
            self.levelrange = levelrange
            self.dexbackground = dexbackground
            self.evopool = evopool
        
        def GetEncounterPool(self):
            return self.encounterpool

        def GetEvoPool(self):
            return self.evopool

        def GetLevelRange(self):
            return self.levelrange

        def GetDexBackground(self):
            return self.dexbackground
        
        def GrabFromEncounterPool(self):
            encounterlist = []
            encountermax = 0
            for entry, odds in self.GetEncounterPool().items():
                if (activerepel == None
                or activerepel == "Repel" and odds < 10
                or activerepel == "Super Repel" and odds < 7
                or activerepel == "Max Repel" and odds < 5):
                    encounterlist.append((encountermax, entry))
                    encountermax += (odds * GetTreatBoost(entry))

            if (len(encounterlist) == 0):#if your current repel prevents any Pokémon from showing up at all, ignore repels
                for entry, odds in self.GetEncounterPool().items():
                    encounterlist.append((encountermax, entry))
                    encountermax += (odds * GetTreatBoost(entry))

            encounterlist.append((9999, 0))
            
            randnum = RandInt(0, encountermax)
            for i in range(len(encounterlist)):
                if (randnum <= encounterlist[i + 1][0]):
                    return encounterlist[i][1]

    wildpools = {
        "fields" : Wildpool({
            pokedexlookupname("Zigzagoon", DexMacros.Id): 10,
            pokedexlookupname("Cyndaquil", DexMacros.Id): 3,
            pokedexlookupname("Bidoof", DexMacros.Id): 10,
            pokedexlookupname("Sunkern", DexMacros.Id): 10,
            pokedexlookupname("Yamper", DexMacros.Id): 10,
            pokedexlookupname("Eevee", DexMacros.Id): 1,
            pokedexlookupname("Nymble", DexMacros.Id): 10,
            pokedexlookupname("Budew", DexMacros.Id): 7,
            pokedexlookupname("Nidoran♀", DexMacros.Id): 5,
            pokedexlookupname("Nidoran♂", DexMacros.Id): 5,
            pokedexlookupname("Swablu", DexMacros.Id): 7,
            pokedexlookupname("Meditite", DexMacros.Id): 7,
            pokedexlookupname("Kricketot", DexMacros.Id): 10,
            pokedexlookupname("Rhyhorn", DexMacros.Id): 5,
            pokedexlookupname("Pumpkaboo", DexMacros.Id): 5,
            pokedexlookupname("Bunnelby", DexMacros.Id): 10,
            pokedexlookupname("Cyclizar", DexMacros.Id): 3,
            pokedexlookupname("Togedemaru", DexMacros.Id): 7,
            pokedexlookupname("Comfey", DexMacros.Id): 7
        }, range(3, 11), "fieldstatic"),

        "alley" : Wildpool({
            pokedexlookupname("Glameow", DexMacros.Id): 10,
            pokedexlookupname("Litten", DexMacros.Id): 1,
            pokedexlookupname("Wimpod", DexMacros.Id): 10,
            412.2: 10,#Burmy Trash Cloak
            pokedexlookupname("Magnemite", DexMacros.Id): 10,
            pokedexlookupname("Castform", DexMacros.Id): 5,
            pokedexlookupname("Scraggy", DexMacros.Id): 7,
            pokedexlookupname("Trubbish", DexMacros.Id): 10,
            pokedexlookupname("Cubone", DexMacros.Id): 7,
            pokedexlookupname("Vullaby", DexMacros.Id): 7,
            pokedexlookupname("Espurr", DexMacros.Id): 7,
            pokedexlookupname("Tarountula", DexMacros.Id): 10,
            pokedexlookupname("Rockruff", DexMacros.Id): 3,
            pokedexlookupname("Shuppet", DexMacros.Id): 10,
            88.1: 10,#Alolan Grimer
            pokedexlookupname("Duraludon", DexMacros.Id): 1,
            pokedexlookupname("Varoom", DexMacros.Id): 5,
            pokedexlookupname("Mime Jr.", DexMacros.Id): 5
        }, range(6, 13), "hideout"),

        "seaport" : Wildpool({
            190: 10,
            58: 7,
            223: 10,
            781: 1,
            602: 3,
            131: 1,
            852: 7,
            690: 7,
            194.1: 10,
            580: 10,
            976: 5,
            595: 7,
            688: 10,
            592: 5,
            592.1: 5,
            318: 7,
            885: 3,
            393: 3,
            298: 10
        }, range(9, 16), "seaport"),

        "infested basement" : Wildpool({
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
        }, range(10, 15), "catacombs3"),

        "unhallowed holt" : Wildpool({
            pokedexlookupname("Pumpkaboo", DexMacros.Id): 5,
            pokedexlookupname("Phantump", DexMacros.Id): 3,
            pokedexlookupname("Rowlet", DexMacros.Id): 1,
            pokedexlookupname("Shuppet", DexMacros.Id): 7,
            pokedexlookupname("Paras", DexMacros.Id): 10,
            pokedexlookupname("Foongus", DexMacros.Id): 7,
        }, range(11, 14), "eveningforest"),

        "shattered glades" : Wildpool({
            pokedexlookupname("Makuhita", DexMacros.Id) : 5, 
            pokedexlookupname("Mankey", DexMacros.Id) : 10, 
            pokedexlookupname("Rowlet", DexMacros.Id) : 1,
            pokedexlookupname("Meditite", DexMacros.Id) : 7,
            pokedexlookupname("Paras", DexMacros.Id): 10,
            pokedexlookupname("Foongus", DexMacros.Id): 7
        }, range(12, 16), "eveningforest"),

        "windswept woods" : Wildpool({
            pokedexlookupname("Swablu", DexMacros.Id) : 10, 
            pokedexlookupname("Rowlet", DexMacros.Id) : 1, 
            pokedexlookupname("Hoothoot", DexMacros.Id) : 5,
            pokedexlookupname("Hoppip", DexMacros.Id) : 7,
            pokedexlookupname("Paras", DexMacros.Id) : 10,
            pokedexlookupname("Foongus", DexMacros.Id): 7
        }, range(13, 17), "eveningforest"),

        "mountain" : Wildpool({
            234: 3,
            776: 1,
            86: 10,
            459: 10,
            74.1: 10,
            712: 7,
            739: 7,
            757: 7,
            220: 10,
            225: 7,
            337: 5,
            338: 5,
            872: 7,
            932: 10,
            425: 10,
            624: 3,
            996: 1,
            27.1: 7,
            703: 5
        }, range(14, 21), "mountain"),

        "catacombs" : Wildpool({
            19.1 : 10,
            935 : 3,
            874 : 5,
            854 : 7,
            736 : 10,
            971 : 7,
            453 : 10,
            92 : 10,
            50.1 : 10,
            83.1 : 7,
            856 : 5,
            622 : 7,
            95 : 7,
            562.1 : 7,
            859 : 5,
            443 : 1,
            52.2 : 10,
            957 : 7,
            109 : 10,
            207 : 7
        }, range(19, 26), "catacombs1", {
            19.1 : (20, 20.1),
            736 : (20, 737),
            92 : (25, 93),
            443 : (24, 444),
            957 : (24, 958)
        })
    }

    habitatorder = {hab: i for i, hab in enumerate(wildpools.keys())}

default knownareas = [] # the first time a wild zone or a dungeon is accessed, it will be marked as known and players can view pokémon from that habitat in the dex