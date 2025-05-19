define treatboosts = {
    Item.PlainBread: "Normal",
    Item.SpicyJerky: "Fire",
    Item.WaterBottle: "Water",
    Item.EnergyDrink: "Electric",
    Item.SaladWrap: "Grass",
    Item.IcePop: "Ice",
    Item.KnuckleSandwich: "Fighting",
    Item.FastFood: "Poison",
    Item.GroundBeef: "Ground",
    Item.BouffalantWings: "Flying",
    Item.BrainFood: "Psychic",
    Item.PicnicBasket: "Bug",
    Item.RockCakes: "Rock",
    Item.SoulFood: "Ghost",
    Item.GummyWyrms: "Dragon",
    Item.DarkChocolate: "Dark",
    Item.SteelcutOats: "Steel",
    Item.PixieSticks: "Fairy"
}

define shopitems = {
    0: (200, Item.PokeBall),
    1: (200, Item.Potion),
    2: (200, Item.Antidote),
    3: (200, Item.BurnHeal),
    4: (200, Item.IceHeal),
    5: (200, Item.Awakening),
    6: (200, Item.ParalyzeHeal),
    7: (300, Item.PokeDoll),
    8: (400, Item.FullHeal),
    9: (500, Item.Repel),
    10: (600, Item.GreatBall),
    11: (700, Item.SuperPotion),
    12: (750, Item.SuperRepel),
    13: (800, Item.UltraBall),
    14: (1500, Item.HyperPotion),
    15: (1500, Item.MaxRepel),
    16: (2000, Item.Revive),
    17: (2500, Item.MaxPotion),
    18: (3000, Item.FullRestore),
    19: (5000, Item.MaxRevive)
}

#To Update from spreadsheet:
#Find: ([0-9,]+)\t([0-9,]+)\t([A-z \-']+)\t([A-z 0-9,'.é]+)
#Replace: $1: ($2, "$3", "$4"),
#Find: ([0-9]+),([0-9]+)
#Replace: $1$2

define marketitems = {
    200: (2000, Item.OranPot),
    500: (2000, Item.ExperienceCondenser),
    1000: (500, Item.EnergyPowder),
    2000: (300, Item.HealPowder),
    3000: (200, Item.ExpCandyXS),#100:200 - 1:2
    4000: (5000, Item.OvalStone),
    5000: (700, Item.ResearchPaper),
    6000: (2500, Item.UnremarkableTeacup),
    7000: (1000, Item.ExpCandyS),#800:1000 - 4:5
    8000: (10000, Item.SecondhandLaptop),
    9000: (10000, Item.TMSoftware2000),
    10000: (1000, Item.BlankTR),
    11000: (3000, Item.BlankTM),
    12000: (5000, Item.Lawnmower),
    13000: (3000, Item.ExpCandyM),#3000:3000 - 1:1
    13337: (5000, Item.UpGrade),
    14000: (300, Item.B5),
    15000: (3000, Item.AspearPot),
    16000: (5000, Item.DeepSeaTooth),
    17000: (3000, Item.RawstPot),
    18000: (5000, Item.Protector),
    19000: (3000, Item.CheriPot),
    20000: (5000, Item.Fan),
    21000: (5000, Item.DeepSeaScale),
    22000: (3000, Item.PechaPot),
    23000: (1000, Item.TamatoSmoothie),
    24000: (3000, Item.ChestoPot),
    25000: (10000, Item.TMSoftwareXP),
    26000: (2500, Item.CrackedPot),
    27000: (5000, Item.SitrusPot),
    28000: (5000, Item.GalaricaCuff),
    29000: (6000, Item.ExpCandyL),#10000:6000 - 5:3
    30000: (5000, Item.Sachet),
    33000: (1000, Item.HondewSmoothie),
    35000: (30000, Item.ZincConcentrate),
    37000: (5000, Item.Electirizer),
    39000: (5000, Item.Refrigerator),
    40000: (5000, Item.WhippedDream),
    43000: (1000, Item.KelpsySmoothie),
    44444: (4444, Item.ReaperCloth),
    45000: (30000, Item.HPUpConcentrate),
    47000: (5000, Item.GalaricaWreath),
    49000: (10000, Item.TMSoftwareVista),
    50000: (1200, Item.EnergyRoot),
    53000: (1000, Item.PomegSmoothie),
    55000: (30000, Item.IronConcentrate),
    57000: (5000, Item.Magmarizer),
    59347: (5000, Item.DubiousDisc),
    60000: (5000, Item.Microwave),
    61000: (10000, Item.LumPot),
    63000: (1000, Item.QualotSmoothie),
    65000: (30000, Item.ProteinConcentrate),
    67000: (5000, Item.AuspiciousArmor),
    70000: (5000, Item.RazorClaw),
    73000: (1000, Item.GrepaSmoothie),
    74000: (5000, Item.DragonScale),
    75000: (30000, Item.CalciumConcentrate),
    77000: (50000, Item.MasterpieceTeacup),
    78000: (10000, Item.ExpCandyXL),#30000:10000 - 3:1
    80000: (5000, Item.WashingMchn),
    83000: (5000, Item.MaliciousArmor),
    85000: (30000, Item.CarbosConcentrate),
    87000: (50000, Item.ChippedPot),
    88000: (10000, Item.TMSoftware05),
    90000: (5000, Item.RazorFang),
    91000: (1000, Item.B5Plus),
    93000: (5000, Item.KingsRock),
    95000: (2800, Item.RevivalHerb),
    97000: (5000, Item.EscapeRope),
    99000: (5000, Item.MetalAlloy),
    100000: (10000, Item.LinkCable)
}

define elementitems = {
    Item.SilkScarf: "Normal",
    Item.Charcoal: "Fire",
    Item.MysticWater: "Water",
    Item.MiracleSeed: "Grass",
    Item.Magnet: "Electric",
    Item.NeverMeltIce: "Ice",
    Item.BlackBelt: "Fighting",
    Item.PoisonBarb: "Poison",
    Item.SoftSand: "Ground",
    Item.SharpBeak: "Flying",
    Item.TwistedSpoon: "Psychic",
    Item.SilverPowder: "Bug",
    Item.HardStone: "Rock",
    Item.SpellTag: "Ghost",
    Item.BlackGlasses: "Dark",
    Item.DragonFang: "Dragon",
    Item.MetalCoat: "Steel",
    Item.FairyFeather: "Fairy"
}

define treatitemspostmay = {
    0 : (800, Item.PlainBread, "Attracts Normal-types in the wild. I'm not saying you're boring, but..."),
    1 : (800, Item.SpicyJerky, "Attracts Fire-types in the wild. Will get stuck in your teeth for weeks."),
    2 : (800, Item.WaterBottle, "Attracts Water-types in the wild. A core component of a wet T-shirt contest."),
    3 : (800, Item.EnergyDrink, "Attracts Electric-types in the wild. It contains electrolytes. They're what plants crave."),
    4 : (800, Item.SaladWrap, "Attracts Grass-types in the wild. The healthy choice for people who hate themselves."),
    5 : (800, Item.IcePop, "Attracts Ice-types in the wild. Brainfreeze is obligatory, but darn it, it's worth it."),
    6 : (800, Item.KnuckleSandwich, "Attracts Fighting-types in the wild. A sandwich carved in the shape of a fist."),
    7 : (800, Item.FastFood, "Attracts Poison-types in the wild. You're pretty sure the Head Chef bought fast food and disguised it as his own cooking. Delightfully devilish."),
    8 : (800, Item.GroundBeef, "Attracts Ground-types in the wild. Does not help with grinding."),
    9 : (800, Item.BouffalantWings, "Attracts Flying-types in the wild. Does not come from actual Bouffalant."),
    10 : (800, Item.BrainFood, "Attracts Psychic-types in the wild. May also attract zombies."),
    11 : (800, Item.PicnicBasket, "Attracts Bug-types in the wild. Also comes with complimentary red-and-white checked blanket."),
    12 : (800, Item.RockCakes, "Attracts Rock-types in the wild. It looks like a grinning Geodude."),
    13 : (800, Item.SoulFood, "Attracts Ghost-types in the wild. Just like Momma used to make."),
    14 : (800, Item.GummyWyrms, "Attracts Dragon-types in the wild. Cheap and sugary candy that looks like Dratini."),
    15 : (800, Item.DarkChocolate, "Attracts Dark-types in the wild. Pretentious people will claim it's better than milk chocolate."),
    16 : (800, Item.SteelcutOats, "Attracts Steel-types in the wild. Makes a darn good porridge with some brown sugar."),
    17 : (800, Item.PixieSticks, "Attracts Fairy-types in the wild. Immediate inducer of diabetes in anyone who has a bite."),
    18 : (350, Item.LavaCookie, "Heals all status conditions. Warm and classically Hoennian. Keep away from Lance..."),
    19 : (2500, Item.SlowpokeTail, "Humanely harvested, grilled to perfection, has a soft, marshmallowy texture. A very popular gift item."),
    20 : (20, Item.OranBerry, "The most basic berry. Useful for Belch strategies, and little else.")
}

define treatitems = {
    0  : (1000, Item.PlainBread),
    1  : (1000, Item.SpicyJerky),
    2  : (1000, Item.WaterBottle),
    3  : (1000, Item.EnergyDrink),
    4  : (1000, Item.SaladWrap),
    5  : (1000, Item.IcePop),
    6  : (1000, Item.KnuckleSandwich),
    7  : (1000, Item.FastFood),
    8  : (1000, Item.GroundBeef),
    9  : (1000, Item.BouffalantWings),
    10 : (1000, Item.BrainFood),
    11 : (1000, Item.PicnicBasket),
    12 : (1000, Item.RockCakes),
    13 : (1000, Item.SoulFood),
    14 : (1000, Item.GummyWyrms),
    15 : (1000, Item.DarkChocolate),
    16 : (1000, Item.SteelcutOats),
    17 : (1000, Item.PixieSticks)
}

init python:
    def GetItem(itemid, count = 1, text = None, audio = True, hidefanfare=False):
        if isinstance(itemid, str):
            itemname = itemid
            itemid = GetItemEntryFromName(itemname)[0]
        else:
            itemname = GetItemEntry(itemid)[1]
        
        if (not hidefanfare):
            if (audio):
                PlaySound("item_get.ogg")
            DisplayGetItem(itemid)

        if (itemid in inventory.keys()):
            inventory[itemid] += count
        else:
            inventory[itemid] = count

        if (not (hidefanfare or text == None)):
            if (text.lower() != "default"):
                renpy.say(None, text)
            elif (text.lower() == "default"):
                preposition = "an" if itemname[0].lower() in ["a", "e", "i", "o", "u"] else "a"
                renpy.say(None, "You got {} {}!".format(preposition, itemname))

    def LoseItem(item, count = 1):
        if isinstance(item, str):
            item = GetItemEntryFromName(item)[0]
        
        if (item in inventory and inventory[item] >= count):
            inventory[item] -= count

            if (inventory[item] <= 0):
                del inventory[item]
                if (item in inventorymetadata):
                    del inventorymetadata[item]
            
            return True

        return False

    def RemoveItem(pkmn):
        if (inbattle):
            renpy.invoke_in_new_context(renpy.say, None, "Please wait until the battle is over to unequip items.")
        else:
            GetItem(pkmn.Item, 1, audio = False, hidefanfare=True)
            pkmn.Item = None

    def GetItemCount(item):
        if isinstance(item, str):
            item = GetItemEntryFromName(item)[0]
        
        for otheritem, amount in inventory.items():
            if (item == otheritem):
                return amount
        return 0

    def GiveItem(partymon, item):
        global activemon
        global invoverwrite
        activemon = partymon
        monnickname = partymon.GetNickname()
        olditem = partymon.GetItem()
        if (olditem == None):
            if (LoseItem(item)):
                partymon.GiveItem(item)
                invoverwrite = "{} was given the {}.".format(monnickname, GetItemName(item))
        else:
            invoverwrite = "{} is already holding the {}. Swap it for the {}?".format(monnickname, GetItemName(olditem), GetItemName(item))

    def SwapItems(item):
        global invoverwrite
        olditem = activemon.GetItem()
        if (LoseItem(item)):
            GetItem(olditem, hidefanfare = True)
            activemon.TakeItem()
            activemon.GiveItem(item)
            invoverwrite = "{} was given the {}, and you put the {} in your bag.".format(activemon.GetNickname(), GetItemName(item), GetItemName(olditem))
    
    def GetGiftValue(character, item):
        global giftedmysterygift

        if (item == "Premier Ball"):
            return 7
        elif (item in ["Mystery Gift", "Slowpoke Tail"]):
            return 10
        elif (character == "Leaf"):
            if (item == Item.MysticWater):
                return -1
            elif (item == Item.LavaCookie):
                return 5
        elif (character == "Misty" and item == Item.SilverPowder):
            return -1
        elif (character == "Gardenia" and item == Item.SpellTag):
            return -1
        elif (character == "Brendan" and item == Item.LavaCookie):
            return -1
        elif (item == Item.FeebasEgg):
            AddEvent(character, "GaveFeebas")
            if (character == "Klara"):
                return 30
            elif (character == "Brendan"):
                return 15
            elif (character == "Nessa"):
                return 10
            elif (character == "Misty"):
                return 7
            elif (character == "Melody"):
                return -1
        elif (item in [Item.ResearchPaper, Item.CelebiWing] and character == "Professor Cherry"):
            return 7
        elif (ItemHasTag(item, "software") or item == Item.SecondhandLaptop and character in ["Iono", "Professor Cherry", "Sonia"]):
            return 7
            
        if (character in classdex):
            if item in elementitems and elementitems[item] in GetCharTypes(character):
                return 5

            if item in treatboosts and treatboosts[item] in GetCharTypes(character):
                return 5

        if (character == "Janine"):
            if (ItemHasTag(item, "likedByJanine")):
                return 5
        elif (character in ["Professor Cherry", "Iono"]):
            if ItemHasTag(item, "rotom catalog"):
                return 20
            if character == "Professor Cherry" and ItemHasTag(item, "move boost item"):
                return 5
        elif (character == "Ethan"):
            return 5

        for shopitem in AllMarkets():
            if (item == shopitem[1]):
                if (shopitem[0] < 500):
                    return 2
                elif (shopitem[0] < 800):
                    return 3
                elif (shopitem[0] < 1001):
                    return 4
                elif (shopitem[0] < 5001):
                    return 5
                else:
                    return 10

        return GetItemEntry(item)[7]

    def IsPerishable(item):
        return ItemHasCategory(item, "berry") or ItemHasCategory(item, "exp item") or ItemHasCategory(item, "treat boost") or ItemHasCategory(item, "apricorn")

    def GetItemSellValue(item):
        global soldmysterygift
        returnvalue = 100
        for shopitem in AllMarkets():
            if (item == shopitem[1]):
                return math.floor(shopitem[0] / 4.0)
                break
        if (IsPerishable(item)):
            return 10
        elif (item == Item.GimmighoulCoin):
            return 1
        elif (item in elementitems.keys()):
            return 100
        elif (item in [Item.CelebiWing, Item.MysteryGift]):
            return 2000
        return math.floor(returnvalue)

    def HasItem(item):
        if isinstance(item, str):
            item = GetItemEntryFromName(item)[ItemdexMacros.Id]
        return item in inventory.keys()

    def AllMarkets():
        return list(shopitems.values()) + list(marketitems.values()) + list(treatitems.values()) + list(treatitemspostmay.values())

    def ValidateBlankTMTRUsage():
        if (not inbattle):
            return False
        elif (Item.SecondhandLaptop not in inventory):
            renpy.say(None, "You cannot use a Blank TM/TR without the appropriate software, and a device to run it on!")
            return False
        elif (Item.TMSoftware2000 not in inventory and Item.TMSoftwareXP not in inventory and Item.TMSoftwareVista not in inventory and Item.TMSoftware05 not in inventory):
            renpy.say(None, "You cannot use a Blank TM/TR without the appropriate software!")
            return False
        elif (Item.BlankTR in inventorymetadata or Item.BlankTM in inventorymetadata):
            renpy.say(None, "You are already recording a move!")
            return False
        else:
            softwaretype = Item.TMSoftware2000
            if (Item.TMSoftware05 in inventory):
                softwaretype = Item.TMSoftware05
            elif (Item.TMSoftwareVista in inventory):
                softwaretype = Item.TMSoftwareVista
            elif (Item.TMSoftwareXP in inventory):
                softwaretype = Item.TMSoftwareXP
            copyablemoves = []
            for mon in (Battlers() if (softwaretype in [Item.TMSoftware05, Item.TMSoftwareVista]) else FriendlyBattlers()):
                lastmove = GetLastMove(ActionLog, mon)
                if (lastmove != None and not IsCustomMove(lastmove)):
                    copyablemoves.append((mon.GetNickname() + " - " + lastmove.Name, lastmove.Name))
            if (len(copyablemoves) == 0):
                if (softwaretype in [Item.TMSoftware2000, Item.TMSoftwareXP]):
                    renpy.say(None, "None of your Pokémon have used moves that can be recorded!")
                    return False
                else:
                    renpy.say(None, "No active Pokémon have used moves that can be recorded!")
                    return False
        
        return True