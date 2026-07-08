init 3 python:
    bunnyparty2electricpikachu = Book("notebook")
    bunnyparty2electricpikachu.Add_Page([
        "{b}Food: [bp2ebfood()]/6{/b}",
        "",
        "Blue",
        "[PlayerName()]",
        "<HasEvent('May', 'BunnyRecruit')|May|{color=#ddd}Unknown{/color}>",
        "<HasEvent('Hilda', 'BunnyRecruit')|Hilda|{color=#ddd}Unknown{/color}>",
        "<HasEvent('Sonia', 'BunnyRecruit')|Sonia|{color=#ddd}Unknown{/color}>",
        "<HasEvent('Gardenia', 'BunnyRecruit')|Gardenia|{color=#ddd}Unknown{/color}>",
        "",
        "{b}Clothing: [bp2ebcloth()]/7{/b}",
        "",
        "Yellow",
        "Brendan",
        "<HasEvent('Whitney', 'BunnyRecruit')|Whitney|{color=#ddd}Unknown{/color}>",
        "<HasEvent('Calem', 'BunnyRecruit')|Calem|{color=#ddd}Unknown{/color}>",
        "<HasEvent('Dawn', 'BunnyRecruit')|Dawn|{color=#ddd}Unknown{/color}>",
        "<HasEvent('Hilda', 'BunnyRecruit')|Hilda|{color=#ddd}Unknown{/color}>",
        "<HasEvent('Gardenia', 'BunnyRecruit')|Gardenia|{color=#ddd}Unknown{/color}>"], include_para_tab=False)
    bunnyparty2electricpikachu.Add_Page([
        "{b}Interference/Tech Support:{/b} [bp2ebtech()]/4",
        "",
        "Ethan",
        "<HasEvent('Iono', 'BunnyRecruit')|Iono|{color=#ddd}Unknown{/color}>",
        "<HasEvent('Nate', 'BunnyRecruit')|Nate|{color=#ddd}Unknown{/color}>",
        "<HasEvent('Sonia', 'BunnyRecruit')|Sonia|{color=#ddd}Unknown{/color}>",
        "",
        "{b}Bunnies: ~[bp2ebparty()]{/b}",
        "",
        "first_name (Go on, do it do it do it do it)",
        "<HasEvent('Leaf', 'BunnyRecruit')|Leaf|Leaf (unconfirmed)>",
        "Blue (I mean, we can dream, right?)",
        "Ethan (haha jk. unless...?)",
        "<HasEvent('May', 'BunnyRecruit')|May|{color=#ddd}Unknown{/color}>",
        "<HasEvent('Nate', 'BunnyRecruit')|Nate|{color=#ddd}Unknown{/color}>",
        "<HasEvent('Nessa', 'BunnyRecruit')|Nessa|{color=#ddd}Unknown{/color}>",
        "<HasEvent('Whitney', 'BunnyRecruit')|Whitney|{color=#ddd}Unknown{/color}>",
        "<HasEvent('Rosa', 'BunnyRecruit')|Rosa|{color=#ddd}Unknown{/color}>",
        "Maybe some others...?"], include_para_tab=False)

    bunnyparty2electricpikachu.Add_Page([
        "{b}Talked to:{/b} ",
        "",
        "[TalkedToList(0, 5)]",
        "[TalkedToList(5, 10)]",
        "[TalkedToList(10, 15)]",
        "[TalkedToList(15, 20)]",
        "[TalkedToList(20, 25)]",
        "[TalkedToList(25, 30)]"], include_para_tab=False)

    def PlayerName():
        return first_name

    def TalkedToList(segmentstart, segementend):
        recruitlist = set()

        for characters in bunnypartydex.values():
            for character in characters:
                if (character not in ["Silver", "Skyla", "Cheren"]):
                    recruitlist.add(character)

        formatlist = []

        for character in sorted(recruitlist):
            if not IsNamed(character):
                formatlist.append("{color=#ddd}???{/color}")
            elif BunRecruit(character):
                formatlist.append(f"{{color=#ddd}}{{s}}{character}{{/s}}{{/color}}")
            else:
                formatlist.append(character)

        return "   ".join(formatlist[segmentstart:segementend])

    def bp2ebfood():
        return 2 + HasEvent('May', 'BunnyRecruit') + HasEvent('Hilda', 'BunnyRecruit') + HasEvent('Sonia', 'BunnyRecruit') + HasEvent('Gardenia', 'BunnyRecruit')

    def bp2ebtech():
        return 1 + HasEvent('Iono', 'BunnyRecruit') + HasEvent('Nate', 'BunnyRecruit') + HasEvent('Sonia', 'BunnyRecruit')

    def bp2ebcloth():
        return 2 + HasEvent('Whitney', 'BunnyRecruit') + HasEvent('Calem', 'BunnyRecruit') + HasEvent('Dawn', 'BunnyRecruit') + HasEvent('Hilda', 'BunnyRecruit')  + HasEvent('Gardenia', 'BunnyRecruit')

    def bp2ebparty():
        return 4 + HasEvent('May', 'BunnyRecruit') + HasEvent('Nate', 'BunnyRecruit') + HasEvent('Nessa', 'BunnyRecruit') + HasEvent('Whitney', 'BunnyRecruit') + HasEvent('Rosa', 'BunnyRecruit')