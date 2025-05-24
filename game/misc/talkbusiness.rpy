label talkbusiness:

show baseball
show gardenia 
with dis
gardenia @happy "Heya! You're looking good. Ready to talk business?"
label beginbusiness:

if (bank > 0 and not HasEvent("Gardenia", "DepositedFirstTime")):
    $ AddEvent("Gardenia", "DepositedFirstTime")
    gardenia @surprised "Thanks for depositing your money! I'll make sure to keep it nice and safe."
    gardenia @talking2mouth "You can now look forward to earning a nice $[min(1000, math.floor(bank / 100))] every day from now 'til the end of the year."
    gardenia @happy "I look forward to many more economic encounters, my thrifty friend!"
    
    red @sadbrow talkingmouth "Uh... yeah... I can't help but feel like no matter how much I bank, it'll be small potatoes compared to your empire, though."

    gardenia @talking2mouth "Maybe a bit. But, hey, you know how many potatoes it takes to bring {i}down{/i} an empire?"

    red @confused "Uh, how many?"

    gardenia @sadbrow talking2mouth "Zero. Just ask the Galarians."

    red @closedbrow talking2mouth "Eesh. Point taken."

    gardenia @happy "I cherish {i}every{/i} potato entrusted to me, no matter how small."

    red @happy "It's nice to be appreciated."

    gardenia @happy "Besides, you know what you can make with potatoes?"

    pause 1.0

    red @confused "Mashed potatoes?"

    gardenia @talkingmouth "A {i}field{/i} of potatoes, partner. Yeah, you might only be earning $[min(1000, math.floor(bank / 100))] right now, but you know how long it'll take you to {i}double{/i} your money, with my compound, everyday interest?"

    red @talking2mouth "No idea. I guess this is a math thing?"

    gardenia @talkingmouth "Partner, it'll only take you {i}seventy{/i} days. That's {i}barely{/i} over two months."
    
    red @surprised "Woah!"

    gardenia @sad2brow talking2mouth "At a 1%% rate of interest, I might be giving you unrealistic expectations for what you can expect from banks outside of, you know, my hobbies[ellipses]"
    gardenia @happy "But don't worry. If you ever get to the point that you're making more than a $1,000 per day from me in interest, I'll give you a special prize for being my best customer."
    gardenia @happy "Aaaaand, hopefully, that'll soothe the injury of being told you're being cut off."

    red @sadbrow talkingmouth "You cap interest at $1,000?"

    gardenia @talkingmouth "You have to cut the eyes off of your potatoes, or they'll kill the potato, {i}and{/i} whoever eats it. But don't worry--by the time you're making a thousand per day from interest, you won't even feel the cutoff."

    red @happy "Alright. I'll take your word for it. Sounds like you're giving me a pretty good deal, so, y'know, thanks."

    $ ValueChange("Gardenia", 3)

    gardenia @happy "Thank {i}you{/i}! And don't worry if you're only a fraction of a fraction of a fraction of my enterprise. I appreciate it all the same."
        
elif (bank > 1000 and not HasEvent("Gardenia", "OpenMarket")):
    $ AddEvent("Gardenia", "OpenMarket")
    gardenia @surprised "Oh, that reminds me! Since my bank's earning you a bit of money every day, now, I thought I'd tell you about something you might be interested in spending it on."

    red @closedbrow talkingmouth "Classic Gardenia. You give me a way to earn money, {i}and{/i} a way to spend it."

    gardenia @talkingmouth "Horizontal integration, partner."
    gardenia @talking2mouth "There are a bunch of items that you'll never find sold in stores run by the Pokémon League." 
    gardenia @talkingmouth "I'm talking powerful items like Vitamin Concentrates that make EV Training a cinch, herbal medicine way more effective than anything the League sells..."
    gardenia @happy "Oh, and evolution items. Protectors, Razor Claws, even imported foreign stuff like those armors from Paldea that Charcadet go crazy for."

    red @closedbrow talkingmouth "There's a catch here."

    gardenia @sadbrow talkingmouth "Afraid so. It's not worth the time or money for me to get my hands on those items until I know there's interest in them." 
    gardenia @talkingmouth "If you invest in my shipping efforts, I can open up a little market here--the 'Junk Shop'--that sells those kinds of items."

    red @closedbrow talking2mouth "You want me to pay you to sell me stuff?"

    gardenia @happy "Given the palms I need to grease to get around the Kobukanian import tariffs, I could ask for a lot more!"

    red @sweat talkingmouth "Guess I should be grateful, then."

    $ ValueChange("Gardenia", 3)

    gardenia @talking2mouth "Now you get it! [bluecolor]If you want me to expand my selection of items, just talk to me here and ask about investing money.{/color} I'll always accept it!"

menu:
    ">Manage money in the bank":
        gardenia @happy "Thank you for banking with us! {w=0.5}...And by us I mean 'me!' You've currently got $[bank] stored with me."
        if (bank == 0):
            gardenia @talkingmouth "Why don't you fix that?"

        $ interest = min(1000, math.floor(bank / 100))

        if (interest not in [0, 1000]):
            gardenia @talking2mouth "You're currently earning $[interest] from interest every day. That's a nice number--could be better, though, right?"
        elif (interest == 0):
            gardenia @sadbrow talkingmouth "You can't earn any interest if you don't have any money in the bank!"
        else:
            gardenia @talkingmouth "You're currently earning $[interest] from interest every day. You're maxed out! Truth be told, I started losing money on you a while ago... but there are lots of different kinds of investments, and I think you're one worth making."

        menu:
            ">Deposit money in the bank" if (money > 0):
                gardenia @talking2mouth "{i}Now{/i} we're in business! How much do you want to deposit?"
                
                $ newinvestment = renpy.input("How much would you like to deposit?", default=money, length=7, allow="1234567890")
                if (not newinvestment.isdigit()):
                    $ newinvestment = 0
                else:
                    $ newinvestment = int(newinvestment)

                if (newinvestment > money):
                    gardenia @angry "Watch it, partner. You better not be trying to give me a check that'll bounce when it's time to cash in."

                    red @sweat closedbrow talking2mouth "Oops. Miscounted."

                elif (newinvestment == 0):
                    pass

                else:
                    $ money -= newinvestment
                    $ bank += newinvestment

                    gardenia @angrybrow talking2mouth "Depositing $[newinvestment], for a total of $[bank]. Very good. I'll guard it jealously..."

            ">Withdraw money" if (bank > 0):
                gardenia @sadbrow talking2mouth "Ah... 'withdraw.' My least favorite word."
                $ withdrawal = renpy.input("How much would you like to withdraw?", default=bank, length=7, allow="1234567890")
                if (not withdrawal.isdigit()):
                    $ withdrawal = 0
                else:
                    $ withdrawal = int(withdrawal)

                if (withdrawal > bank):
                    gardenia @happy "Sorry, partner! You don't have that much banked with me."
                    gardenia @angrybrow talkingmouth "I'd give you a loan, but I'll tell you right now I'm a shark when it comes to debt."

                    red @sweat happy "Tempting offer. I'll pass!"
                
                elif (withdrawal == 0):
                    pass

                else:
                    $ money += withdrawal
                    $ bank -= withdrawal

                    gardenia @angrybrow talking2mouth "Here's your $[withdrawal]. {w=0.5}...I'll take it back any time you want!"

            "Nevermind.":
                pass
                
        jump beginbusiness

    ">Invest money" if (not investment >= 100000 and HasEvent("Gardenia", "OpenMarket")):
        $ cost, purchaseprice, itemid, description = GetNextInvestmentPrize()
        $ name = GetItemName(itemid)
        $ moretoinvest = cost - investment
        $ formatdescription = description[0].lower() + description[1:]
        gardenia @happy "That's the kind of forward-thinking attitude I like to hear, partner!"
        gardenia @talking2mouth "Once you've invested $[moretoinvest] more, bringing it up to $[cost], I think I should be able to get my hands on a [name] or two. I'll sell 'em back to you for $[purchaseprice]."
        gardenia @talkingmouth "I think that item [formatdescription] Anyway, buy it and find out if I'm right!"
        gardenia @talking2mouth "So, how much would you like to invest?"
        $ investing = renpy.input("How much would you like to invest?", default=money, length=6, allow="1234567890")
        if (not investing.isdigit()):
            $ investing = 0
        else:
            $ investing = int(investing)

        if (investing > money):
            if (investing > bank):
                gardenia @sadbrow talkingmouth "Sorry. I don't think you've got the money for that kind of investment, and I don't deal in cryptocurrencies."
            else:
                gardenia @talking2mouth "You don't have the money on-hand for that, but I'll take it out of your bank. Sound good?"

                menu:
                    "Sure.":
                        $ bank -= investing
                        $ investment += investing

                        gardenia @happy "You might not have the wallet of an angel investor, but you've sure got the heart of one. Thanks, [first_name]!"

                    "Nevermind.":
                        pass

        elif (investing == 0):
            pass

        else:
            $ money -= investing
            $ investment += investing

            gardenia @happy "You might not have the wallet of an angel investor, but you've sure got the heart of one. Thanks, [first_name]!"

        if (investment >= 100000):
            gardenia @surprised "W-woah! These numbers... looks like the market shifted at the perfect time!"
            gardenia @happy "[first_name], you've completely maxed out my investment track! And made a {i}lot{/i} of shady moving guys in Inspira happy."

            red @sadbrow talkingmouth "G-great...?"

            if (investment > 100000):
                gardenia  @talkingmouth "Here, I'll give you back a bit. I like working with round numbers--so I'll cap off your investment in me at a nice 100k."

                $ money += (investment - 100000)

                narrator "Gardenia returned some money."

            gardenia @happy "Yep, that's right--I'm now selling you {i}every{/i} single product I can get my hands on."
            gardenia @talking2mouth "Ah... I guess that means I'll have to come up with something new, something {i}way{/i} bigger, for you to invest in, then."

            red @sadbrow talkingmouth "Maybe reach out to me next year about that."

            gardenia @angrybrow talkingmouth "I {i}definitely{/i} will. Get that wallet ready for me, [first_name]."

            red @happy "You got it!"

        jump beginbusiness

    ">Go shopping ([witcolor]Wit{/color} Discount: [math.floor(personalstats['Wit'] / 3)]%%)" if (investment >= 200):
        call screen shopkeep(marketitems, market=True)
        $ boughtitem = _return
        if (boughtitem == "Back"):
            gardenia @sadbrow talking2mouth "Why do you hate the economy, [first_name]?"
            jump beginbusiness
        else:
            $ totalcost = math.floor(boughtitem[0] * (1 - personalstats['Wit'] / 300) * boughtitems)
            if (totalcost > money + bank):
                narrator "You can't afford that!"
            else:
                python:
                    itemname = GetItemName(boughtitem[1])
                    money -= totalcost 
                    usedbank = 0
                    if (money < 0):
                        usedbank = abs(money)
                        bank += money
                        money = 0
                if (usedbank != 0):
                    narrator "You withdrew $[usedbank] from the bank, and..."
                if (boughtitems > 1):
                    narrator "You bought [boughtitems] [itemname]s for $[totalcost]!"
                else:
                    $ preposition = ("an" if itemname[0].lower() in ["a", "e", "i", "o", "u"] else "a")
                    narrator "You bought [preposition] [itemname] for $[totalcost]!"
                $ GetItem(itemname, boughtitems)
                $ boughtitems = 1

            jump beginbusiness

    ">Sell items ([witcolor]Wit{/color} Bonus: [math.floor(personalstats['Wit'] / 3)]%%)" if (persondex["Gardenia"]["Contact"]):
        gardenia @happy "Sure, I'll buy something off of you. What're ya sellin'?"

        label selling:

        python:
            global invoverwrite
            global itemdesc
            invoverwrite = None
            itemdesc = " "
            item = renpy.call_screen("fieldinventory", True)
        if (item == "back"):
            gardenia @angrybrow happymouth "Ah, boo!"
            jump beginbusiness
        else:
            if (IsPerishable(item)):
                gardenia @happy "Sorry, partner! I can't buy perishables. That means no berries, no candy, no foods. No shelf-life, you know? I don't move this stuff fast, so it needs to last a while."
                jump beginbusiness

            $ itemvalue = math.floor(GetItemSellValue(item) * (1 + personalstats['Wit'] / 300))
            $ itemvalueformat = "{:,}".format(itemvalue)
            gardenia @talking2mouth "Hm... not a lot of demand for that item. Best I can do is $[itemvalueformat]."

            $ itemcount = GetItemCount(item)
            $ halfitem = math.floor(itemcount / 2.0)

            menu:
                ">Sell one":
                    if (LoseItem(item)):
                        $ money += itemvalue
                        gardenia @happy "Pleasure doing business with ya!"

                ">Sell half ([halfitem])" if (itemcount >= 3):
                    if (LoseItem(item, halfitem)):
                        $ money += itemvalue * halfitem 
                        gardenia @happy "Pleasure doing business with ya!"

                ">Sell all ([itemcount])" if (itemcount > 1):
                    if (LoseItem(item, itemcount)):
                        $ money += itemvalue * itemcount
                        gardenia @happy "Pleasure doing business with ya!"

                "Nevermind.":
                    pass

            jump selling

    "Nevermind.":
        gardenia @angrybrow happymouth "Ah, boo!"

hide baseball
hide gardenia 
with dis
jump aftersetup