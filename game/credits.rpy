transform credits_scroll():
    yalign 0.0
    linear 50 yalign 1.0

label credits:
    $ renpy.movie_cutscene('images/videos/Credits.webm')

    show screen credits

    pause 60

    hide screen credits

    call screen main_menu()

screen credits():
    add "BG/Blank2.webp"
    vbox at credits_scroll:
        xalign 0.5
        yalign 0.1
        spacing 50
        null height 1080

        vbox:
            text "Project Recreator" size 80 color "#fff"
            text "Freudian Creations" size 40 color "#fff"

        $ writers = ["MMCC"]
        vbox:
            text "Writing Assistance" size 80 color "#fff"
            for name in writers:
                text name size 40 color "#fff"

        $ coders = ["🟧 Flintlock 🟧", "Hewdraw", "Adingo", "Gaslighter 〚Bianca's protecctor〛", "IndexClone", "MrCrabClaw"]
        vbox:
            text "Programming Assistance" size 80 color "#fff"
            for name in coders:
                text name size 40 color "#fff"

        $ artists = ["Iustinus Tempus", "KBunink", "Dantalion", "Anthos", "SquishyBird22", "jadespring", "Ken Sugimori", "codygon z", "Dreamcloud1283", "Dahlia Wilder", "Strife", "Mint", "scarletspecter", "Glazed"]
        vbox:
            text "Artists" size 80 color "#fff"
            for name in artists:
                text name size 40 color "#fff"

        $ audioengineers = ["Achroma"]
        vbox:
            text "Audio Assistance" size 80 color "#fff"
            for name in audioengineers:
                text name size 40 color "#fff"

        $ singers = ["OnesieBanette", "On Off Music", "Marcus Gonda Music"]
        vbox:
            text "Original Songs" size 80 color "#fff"
            for name in singers:
                text name size 40 color "#fff"

        $ specialthanks = ["imainmeleekirby", "JumboXtraLarge", "Bartre God Dio", "Novemball", "Lexel", "Eyen [[Capo Eternal]", "Ghost", "NathanRose", "Mint", "Enigmatic Passerby", "Leirbag15"]
        vbox:
            text "Special Thanks" size 80 color "#fff"
            for name in specialthanks:
                text name size 40 color "#fff"
        
        $ teachingassistants = ["naototogo", "Monarchist MISSINGNO.", "Smokey", "variaqlty", "exalt5420", "caerulight", "seanmac317", "cinnaburh", "inferno6703", "Kay『 Mr. PAL:Friday 』", "supernick64", "kingrajesh", "Farzalou, #1 Whitney challenger", "propoke24", "nmorrow", "Leirbag15 (Pikmin Trainer)", "swf11", "hope_devourer"]
        vbox:
            text "Teaching Assistants" size 80 color "#fff"
            for name in teachingassistants:
                text name size 40 color "#fff"
        
        $ topstudents = ["lastskylord", "naototogo", "hufcok74", "redrevan.", "vander86", "sweetdr3am", "Girll", "Monarchist MISSINGNO.", "alurayune", "Smokey", "buggybluejay", "Adamthenoob1 (#1 simp for Hilda)", "Q1justin [[Blue Deserves Love]", "variaqlty", "oniiboro", "Silver Phoenix", "himdave", "Canary", "exalt5420", "Bartre God Dio", "Midnight @ Sundown", "Solvalou (AKA Fenty)", "Darugus (skyver is okay)", "Lexel", "caerulight", ".jacattac", "toasty_._", "Cobra - #1 Leaf Fan", "Enigmatic Passerby (Yellow Fan)", "ikai210", "Revan Noct - Follower of Helix", "marco (leaf’s husband)", "Misheavous", "🌈JXL- Tia's ICE/Astrid Superego", "Shepurd", "rhaykou", "Justin #1 Ethan Vanguard", "bigfan0510", "carpe_0", "seanmac317", "mirrorabyss", "#1 Leaf simp~", "darksea99", "Ajinho", "cinnaburh", "Horny, MILF Enjoyer", "luisilly6", "inferno6703", "AJ", "Kay『 Mr. PAL:Friday 』", "Orion", "Alm•Misty's Husband", "pesto0903", "chyson", "Guest the (NOT) Rat", "microe", "tgasf", "FlanneryHildaAreMY#1's", "mmcc_94868", "Sikoh", "myname_jonas", "nathanrose115", "supernick64", "Ren", "review10", "kingrajesh", "carpechaz", "The Hilbert Gremlin", "Farzalou, #1 Whitney challenger", "chaoticly_vee_ttv", "byakuya7758", "ralz-[[leader of dawn protectors]", "Eyen [[Capo Eternal]", "haxixe1995", "tiggyxtaggy", "signofnature_eevee", "Adingo [[I AM PUN]", "Viva〚#1 Peak Shipping Meister〛", "Raion [[Lyra and Serena Simp]", "Bill4123", "FunkyLittleDude(Melodys Husband)", "Claire Redfield", "weez1ng", "denial___", "kogasaka", "propoke24", "Spreem - Grusha’s Husband", "MysticHobo", "nicksaulnier", "iustinustempus", "Based King 🤴🏾 (Christian)", "prettymiggy", "mrrjc", "the_pickle_man.", "nmorrow", "velmidos9021", "andrewwz", "Leirbag15 (Pikmin Trainer)", "primename", "pestofettuccine", "kingslayer3765", "soluxisofficial", "Krok [[Hibernating till week 10]", "swf11", "shinzeka", "hetasear", "hope_devourer", "rufusthered_13354", "lordmichaeltm", "bacon8en", "Scotch the Bro Route Advocate", "thatoneowl", "pabloxdreams", "NStar", "sharky2254", "KingSting"]
        vbox:
            text "Top Students" size 80 color "#fff"
            for name in topstudents:
                text name size 40 color "#fff"
        
        $ commissioners = ["Dolphin - Pokemon Concierge Fan", "vander86", "🟧 Flintlock 🟧", "tektonik", "crippledjoe", "Canary", "exalt5420", "#1 Blue stan", "Bartre God Dio", "Lexel", "caerulight", ".dmstorm", "a 6:30 AM Meeting", "Viva〚#1 Peak Shipping Meister〛", "🌈JXL- Tia's ICE/Astrid Superego", "The Aura Ranger", "AjanisApprentice (#1 Dawn simp)", "Horny, MILF Enjoyer", "queenduplica", "etherious55", "CAnon || Team Yell", "Gaslighter〚🍵MorBid🍹 apologist〛", "Sikoh", "nathanrose115", "#1 Leon S. Kennedy", "Banned for level up", "jman7403", "byakuya7758", "Night Fury (PALF YouTuber)", "Orange (Erika Glazer)", "Eyen [[Capo Eternal]", "zum1udontno", "JWill", "Adingo [[I AM PUN]", "mgear", "Polaris", "denial___", "Leirbag15 (Pikmin Trainer)", "Flynn Stone", "kinporte", "NStar", "KingSting"]
        vbox:
            text "Commissioners" size 80 color "#fff"
            for name in commissioners:
                text name size 40 color "#fff"

        vbox:
            text "Shaders by Feniks (https://feniksdev.com)"

        vbox:
            text "Fashion Design" size 80 color "#fff"

            text "ポケ垢" size 40 color "#fff"
            text "VIK_Works" size 40 color "#fff"
            text 'Crys (u/Epee_Prisme)' size 40 color "#fff"
        
            null height 80

            text "Backgrounds" size 80 color "#fff"

            text "@scarletspecter" size 40 color "#fff"
            text "Backgrounds by Sai Gakai/Kimagure After (きまぐれアフター)" size 40 color "#fff"
            text "Background Material Shop" size 40 color "#fff"
            text "QUUN PLANT Co., Ltd." size 40 color "#fff"
            text "KNT Graphics:Yagaminiso" size 40 color "#fff"
            text "Shounensha" size 40 color "#fff"
            text "BG Spot"size 40 color "#fff"
            text "Backgrounds by Min-Chi (みんちり)" size 40 color "#fff"
            text "Taken from みんちりえ (https://min-chi.material.jp/) and みんちりのfanbox (https://min-chi.fanbox.cc/)" size 25 color "#fff"
 
            null height 80

            text "Extra Art" size 80 color "#fff"

            text "nelsini0s" size 40 color "#fff"
            text "Brumirage" size 40 color "#fff"

            null height 80

            text "Battle Music Credits" size 80 color "#fff"

            text "StevenMix - Johto, Paldea and Kitakami Trainer Battle Themes" size 40 color "#fff"
            text "Zame - Hoenn, Orre, and Kalos Trainer Battle Themes" size 40 color "#fff"
            text "Pokestir - Sinnoh and Galar Trainer Battle Themes" size 40 color "#fff"
            text "Kunning Fox - Unova and Alola Trainer Battle Themes" size 40 color "#fff"

        null height 1080