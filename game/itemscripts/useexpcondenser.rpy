label useexpcondenser:

$ expcount = math.floor(inventorymetadata[Item.ExperienceCondenser][1])
$ onoff = "on" if inventorymetadata[Item.ExperienceCondenser][0] else "off"

narrator "The Experience Condenser is currently turned [onoff] and contains [expcount] EXP."

menu:
    ">Toggle on" if onoff == "off":
        $ inventorymetadata[Item.ExperienceCondenser][0] = True

    ">Toggle off" if onoff == "on":
        $ inventorymetadata[Item.ExperienceCondenser][0] = False

    ">Create candy":
        if (expcount < 100):
            narrator "The Experience Condenser does not have enough Experience to create candies--it needs at least 100!"

        else:
            python:
                candy_values = {Item.ExpCandyXL: 30000, Item.ExpCandyL: 10000, Item.ExpCandyM: 3000, Item.ExpCandyS: 800, Item.ExpCandyXS: 100}
                candy_count = {Item.ExpCandyXL: 0, Item.ExpCandyL: 0, Item.ExpCandyM: 0, Item.ExpCandyS: 0, Item.ExpCandyXS: 0}
                
                for candy, value in candy_values.items():
                    while expcount >= value:
                        expcount -= value
                        candy_count[candy] += 1
                
                inventorymetadata[Item.ExperienceCondenser][1] = expcount

                for candy, count in candy_count.items():
                    if (count > 0):
                        GetItem(candy, count, text="You created [count]x [GetItemName(candy)]!")

    ">Stop using":
        return

jump useexpcondenser