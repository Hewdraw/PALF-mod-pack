init python:
    def BeginKaraokeBattle(song):
        global karaoketrack
        karaoketrack = song
        AddEvent("Game", "ContestShowcase")

        config.allow_skipping = False
        preferences.text_cps = 90

    def EndKaraokeBattle():
        RemoveEvent("Game", "ContestShowcase")
        config.allow_skipping = True

    KARAOKE_REDRAW = 0.03
    KARAOKE_TRANSITION_TIME = 0.35

    KARAOKE_CURRENT_Y = 0.2
    KARAOKE_PREVIOUS_Y = 0.12 #-.08
    KARAOKE_OLDER_Y = 0.04 #-.16
    KARAOKE_ENTRY_Y = 0.28#+ .08

    def clamp(value, low, high):
        return max(low, min(high, value))

    def lerp(a, b, t):
        return a + (b - a) * t

    def get_karaoke_time():
        pos = renpy.music.get_pos("music")
        if pos is None:
            return 0.0
        return pos

    def get_line_start(line):
        return line["words"][0]["start"]

    def get_line_end(karaoke_lines, index):
        line = karaoke_lines[index]

        if index < len(karaoke_lines) - 1:
            return karaoke_lines[index + 1]["words"][0]["start"]

        last_word = line["words"][-1]
        return last_word.get("end", 999999.0)

    def get_karaoke_state():
        if karaoketrack:
            karaoke_lines = karaoke_dict[karaoketrack]
        else:
            return {
                "time": 0.0,
                "index": None,
                "current": None,
                "previous": None,
                "older": None,
                "current_start": None,
                "current_end": None,
            }

        t = get_karaoke_time()

        current_index = None
        current_line = None
        current_start = None
        current_end = None

        for i, line in enumerate(karaoke_lines):
            line_start = get_line_start(line)
            line_end = get_line_end(karaoke_lines, i)

            if line_start <= t < line_end:
                current_index = i
                current_line = line
                current_start = line_start
                current_end = line_end
                break

        if current_line is None:
            return {
                "time": t,
                "index": None,
                "current": None,
                "previous": None,
                "older": None,
                "current_start": None,
                "current_end": None,
            }

        previous_line = karaoke_lines[current_index - 1] if current_index > 0 else None
        older_line = karaoke_lines[current_index - 2] if current_index > 1 else None

        return {
            "time": t,
            "index": current_index,
            "current": current_line,
            "previous": previous_line,
            "older": older_line,
            "current_start": current_start,
            "current_end": current_end,
        }

    def build_word_progress_text(line, t):
        if not line or not line.get("words"):
            return ""

        parts = []
        words = line["words"]

        for i, word in enumerate(words):
            word_start = word["start"]

            if i < len(words) - 1:
                word_end = words[i + 1]["start"]
            else:
                word_end = word.get("end", 999999.0)

            if t >= word_end:
                parts.append("{color=#ffd54f}%s{/color}" % word["text"])
            elif word_start <= t < word_end:
                duration = max(word_end - word_start, 0.001)
                progress = clamp((t - word_start) / duration * 1.2, 0.0, 1.0)

                txt = word["text"]
                lit_chars = int(len(txt) * progress)
                past_text = txt[:lit_chars]
                future_text = txt[lit_chars:]

                parts.append("{color=#ffd54f}%s{/color}{color=#666666}%s{/color}" % (past_text, future_text))
            else:
                parts.append("{color=#666666}%s{/color}" % word["text"])

        return " ".join(parts)

    def build_finished_line_text(line):
        if not line or not line.get("words"):
            return ""

        full_text = " ".join(word["text"] for word in line["words"])
        return "{color=#ffd54f}%s{/color}" % full_text

    def make_karaoke_text(txt, ypos, alpha):
        return Transform(
            Text(
                txt,
                text_align=0.5,
                size=42,
                outlines=[(2, "#000000", 0, 0)],
                xalign=0.5,
            ),
            xalign=0.5,
            yalign=0.0,
            ypos=ypos,
            alpha=alpha,
        )

    def karaoke_displayable(st, at):
        state = get_karaoke_state()
        current_line = state["current"]

        if not current_line:
            return Null(width=1, height=1), KARAOKE_REDRAW

        t = state["time"]
        current_start = state["current_start"]

        transition_progress = clamp((t - current_start) / KARAOKE_TRANSITION_TIME, 0.0, 1.0)

        current_txt = build_word_progress_text(current_line, t)

        root = Fixed()

        older_line = state["older"]
        if older_line:
            older_y = lerp(KARAOKE_PREVIOUS_Y, KARAOKE_OLDER_Y, transition_progress)
            older_alpha = 1.0 - transition_progress
            if older_alpha > 0.0:
                root.add(
                    make_karaoke_text(
                        build_finished_line_text(older_line),
                        older_y,
                        older_alpha,
                    )
                )

        previous_line = state["previous"]
        if previous_line:
            previous_y = lerp(KARAOKE_CURRENT_Y, KARAOKE_PREVIOUS_Y, transition_progress)
            root.add(
                make_karaoke_text(
                    build_finished_line_text(previous_line),
                    previous_y,
                    1.0,
                )
            )

        current_y = lerp(KARAOKE_ENTRY_Y, KARAOKE_CURRENT_Y, transition_progress)
        current_alpha = transition_progress
        root.add(
            make_karaoke_text(
                current_txt,
                current_y,
                current_alpha,
            )
        )

        return root, KARAOKE_REDRAW

screen karaoke_overlay():
    add DynamicDisplayable(karaoke_displayable)

init python:
        karaoke_dict = {
        "brendan.wav" : [
            {
                "words": [
                    {"start": 9.54, "text": "In"},
                    {"start": 9.88, "text": "this"},
                    {"start": 10.26, "text": "academy,"},
                    {"start": 12.30, "text": "learning"},
                    {"start": 12.74, "text": "every"},
                    {"start": 13.12, "text": "day,", "end": 14.88},
                ]
            },
            {
                "words": [
                    {"start": 14.88, "text": "Battlefronts"},
                    {"start": 15.48, "text": "and"},
                    {"start": 15.78, "text": "strategy,"},
                    {"start": 17.44, "text": "that's"},
                    {"start": 17.76, "text": "what"},
                    {"start": 17.94, "text": "they"},
                    {"start": 18.22, "text": "say", "end": 19.96},
                ]
            },
            {
                "words": [
                    {"start": 19.96, "text": "But"},
                    {"start": 20.28, "text": "deep"},
                    {"start": 20.64, "text": "inside"},
                    {"start": 21.24, "text": "of"},
                    {"start": 21.40, "text": "me,", "end": 22.48},
                ]
            },
            {
                "words": [
                    {"start": 22.48, "text": "shining"},
                    {"start": 22.78, "text": "clear"},
                    {"start": 23.18, "text": "and"},
                    {"start": 23.44, "text": "bright,", "end": 25.10},
                ]
            },
            {
                "words": [
                    {"start": 25.10, "text": "I"},
                    {"start": 25.42, "text": "dream"},
                    {"start": 25.90, "text": "to"},
                    {"start": 26.08, "text": "be"},
                    {"start": 26.50, "text": "free", "end": 27.64},
                ]
            },
            {
                "words": [
                    {"start": 27.64, "text": "in"},
                    {"start": 27.78, "text": "the"},
                    {"start": 27.92, "text": "contest"},
                    {"start": 28.60, "text": "light", "end": 31.64},
                ]
            },
            {
                "words": [
                    {"start": 31.64, "text": "Gotta"},
                    {"start": 32.00, "text": "chase"},
                    {"start": 32.34, "text": "that"},
                    {"start": 32.64, "text": "dream,", "end": 34.26},
                ]
            },
            {
                "words": [
                    {"start": 34.26, "text": "gotta"},
                    {"start": 34.58, "text": "take"},
                    {"start": 34.78, "text": "that"},
                    {"start": 35.00, "text": "stage,", "end": 36.80},
                ]
            },
            {
                "words": [
                    {"start": 36.80, "text": "colors"},
                    {"start": 37.14, "text": "flow"},
                    {"start": 37.38, "text": "and"},
                    {"start": 37.60, "text": "gleam,", "end": 39.23},
                ]
            },
            {
                "words": [
                    {"start": 39.23, "text": "turn"},
                    {"start": 39.50, "text": "a"},
                    {"start": 39.62, "text": "brand"},
                    {"start": 39.96, "text": "new"},
                    {"start": 40.30, "text": "page", "end": 41.88},
                ]
            },
            {
                "words": [
                    {"start": 41.88, "text": "Guess"},
                    {"start": 42.10, "text": "I"},
                    {"start": 42.24, "text": "battled"},
                    {"start": 42.70, "text": "hard,", "end": 44.30},
                ]
            },
            {
                "words": [
                    {"start": 44.30, "text": "played"},
                    {"start": 44.52, "text": "the"},
                    {"start": 44.70, "text": "toughest"},
                    {"start": 45.22, "text": "game,", "end": 47.00},
                ]
            },
            {
                "words": [
                    {"start": 47.00, "text": "but"},
                    {"start": 47.20, "text": "I"},
                    {"start": 47.34, "text": "want"},
                    {"start": 47.62, "text": "the"},
                    {"start": 47.94, "text": "art"},
                    {"start": 48.36, "text": "and"},
                    {"start": 48.64, "text": "not"},
                    {"start": 48.88, "text": "just"},
                    {"start": 49.24, "text": "glory's"},
                    {"start": 50.36, "text": "name", "end": 52.70},
                ]
            },
            {
                "words": [
                    {"start": 52.70, "text": "We'll"},
                    {"start": 53.02, "text": "fly"},
                    {"start": 53.42, "text": "away", "end": 55.16},
                ]
            },
            {
                "words": [
                    {"start": 55.16, "text": "to"},
                    {"start": 55.42, "text": "a"},
                    {"start": 55.54, "text": "flashy"},
                    {"start": 56.06, "text": "place,", "end": 57.94},
                ]
            },
            {
                "words": [
                    {"start": 57.94, "text": "where"},
                    {"start": 58.10, "text": "I'll"},
                    {"start": 58.32, "text": "have"},
                    {"start": 58.54, "text": "the"},
                    {"start": 58.66, "text": "strength", "end": 60.32},
                ]
            },
            {
                "words": [
                    {"start": 60.32, "text": "to"},
                    {"start": 60.46, "text": "hold"},
                    {"start": 60.80, "text": "your"},
                    {"start": 61.16, "text": "embrace", "end": 63.22},
                ]
            },
            {
                "words": [
                    {"start": 63.22, "text": "We'll"},
                    {"start": 63.54, "text": "make"},
                    {"start": 63.84, "text": "the"},
                    {"start": 64.00, "text": "cut,", "end": 65.72},
                ]
            },
            {
                "words": [
                    {"start": 65.72, "text": "we'll"},
                    {"start": 66.08, "text": "rise"},
                    {"start": 66.44, "text": "above", "end": 67.92},
                ]
            },
            {
                "words": [
                    {"start": 67.92, "text": "these"},
                    {"start": 68.78, "text": "waterfalls", "end": 69.72},
                ]
            },
            {
                "words": [
                    {"start": 69.72, "text": "and"},
                    {"start": 70.02, "text": "dive"},
                    {"start": 70.36, "text": "right"},
                    {"start": 70.70, "text": "into"},
                    {"start": 71.34, "text": "our"},
                    {"start": 71.64, "text": "love", "end": 73.60},
                ]
            },
            {
                "words": [
                    {"start": 73.60, "text": "I"},
                    {"start": 74.68, "text": "won't"},
                    {"start": 75.34, "text": "let"},
                    {"start": 75.96, "text": "go"},
                    {"start": 76.66, "text": "of"},
                    {"start": 77.24, "text": "all"},
                    {"start": 77.84, "text": "the"},
                    {"start": 78.34, "text": "dreams", "end": 79.50},
                ]
            },
            {
                "words": [
                    {"start": 79.50, "text": "I"},
                    {"start": 79.72, "text": "have"},
                    {"start": 80.06, "text": "because"},
                    {"start": 80.82, "text": "of"},
                    {"start": 81.18, "text": "a"},
                    {"start": 81.64, "text": "few"},
                    {"start": 82.26, "text": "problems", "end": 83.26},
                ]
            },
            {
                "words": [
                    {"start": 83.26, "text": "It's"},
                    {"start": 83.52, "text": "frustrating"},
                    {"start": 84.86, "text": "how", "end": 85.84},
                ]
            },
            {
                "words": [
                    {"start": 85.84, "text": "these"},
                    {"start": 86.14, "text": "doubts"},
                    {"start": 86.64, "text": "seem"},
                    {"start": 87.18, "text": "to"},
                    {"start": 87.44, "text": "weigh", "end": 88.44},
                ]
            },
            {
                "words": [
                    {"start": 88.44, "text": "me"},
                    {"start": 88.74, "text": "down", "end": 90.70},
                ]
            },
            {
                "words": [
                    {"start": 90.70, "text": "But"},
                    {"start": 91.02, "text": "I'm"},
                    {"start": 91.28, "text": "standing"},
                    {"start": 92.72, "text": "up"},
                    {"start": 93.10, "text": "to"},
                    {"start": 93.54, "text": "them"},
                    {"start": 94.00, "text": "now", "end": 96.34},
                ]
            },
            {
                "words": [
                    {"start": 96.34, "text": "I'll"},
                    {"start": 96.72, "text": "muster"},
                    {"start": 98.18, "text": "up"},
                    {"start": 98.92, "text": "the"},
                    {"start": 99.20, "text": "strength", "end": 103.64},
                ]
            },
            {
                "words": [
                    {"start": 103.64, "text": "somehow,"},
                    {"start": 106.24, "text": "and"},
                    {"start": 106.56, "text": "I'll"},
                    {"start": 106.84, "text": "let"},
                    {"start": 107.28, "text": "go"},
                    {"start": 107.80, "text": "of"},
                    {"start": 108.18, "text": "my"},
                    {"start": 108.82, "text": "mistakes,", "end": 111.50},
                ]
            },
            {
                "words": [
                    {"start": 111.50, "text": "'cause"},
                    {"start": 112.02, "text": "I'm"},
                    {"start": 112.28, "text": "standing"},
                    {"start": 113.84, "text": "up"},
                    {"start": 114.28, "text": "to"},
                    {"start": 114.80, "text": "them"},
                    {"start": 115.42, "text": "now", "end": 115.71},
                ]
            },
            {
                "words": [
                    {"start": 115.71, "text": "I"},
                    {"start": 115.86, "text": "don't"},
                    {"start": 116.24, "text": "wanna"},
                    {"start": 116.84, "text": "fight"},
                    {"start": 117.18, "text": "no"},
                    {"start": 117.50, "text": "more,", "end": 118.12},
                ]
            },
            {
                "words": [
                    {"start": 118.12, "text": "dreams"},
                    {"start": 118.56, "text": "of"},
                    {"start": 118.84, "text": "beauty"},
                    {"start": 119.64, "text": "I"},
                    {"start": 119.90, "text": "implore", "end": 120.92},
                ]
            },
            {
                "words": [
                    {"start": 120.92, "text": "Colors"},
                    {"start": 121.62, "text": "bright"},
                    {"start": 122.04, "text": "and"},
                    {"start": 122.32, "text": "dances"},
                    {"start": 122.94, "text": "grand,", "end": 123.44},
                ]
            },
            {
                "words": [
                    {"start": 123.44, "text": "I'll"},
                    {"start": 123.64, "text": "make"},
                    {"start": 123.96, "text": "my"},
                    {"start": 124.28, "text": "mark,"},
                    {"start": 124.76, "text": "alone"},
                    {"start": 125.40, "text": "I"},
                    {"start": 125.62, "text": "stand", "end": 126.26},
                ]
            },
            {
                "words": [
                    {"start": 126.26, "text": "Told"},
                    {"start": 126.70, "text": "my"},
                    {"start": 127.08, "text": "teacher"},
                    {"start": 127.76, "text": "and"},
                    {"start": 128.06, "text": "my"},
                    {"start": 128.42, "text": "friends,", "end": 129.08},
                ]
            },
            {
                "words": [
                    {"start": 129.08, "text": "\"I"},
                    {"start": 129.42, "text": "won't"},
                    {"start": 129.76, "text": "battle"},
                    {"start": 130.36, "text": "till"},
                    {"start": 130.78, "text": "the"},
                    {"start": 131.12, "text": "end.\"", "end": 131.76},
                ]
            },
            {
                "words": [
                    {"start": 131.76, "text": "They"},
                    {"start": 132.18, "text": "all"},
                    {"start": 132.49, "text": "laughed,"},
                    {"start": 132.82, "text": "but"},
                    {"start": 133.22, "text": "I"},
                    {"start": 133.36, "text": "stood"},
                    {"start": 133.82, "text": "tall,", "end": 134.22},
                ]
            },
            {
                "words": [
                    {"start": 134.22, "text": "I'll"},
                    {"start": 134.44, "text": "prove"},
                    {"start": 134.88, "text": "them"},
                    {"start": 135.22, "text": "wrong,", "end": 135.66},
                ]
            },
            {
                "words": [
                    {"start": 135.66, "text": "I'll"},
                    {"start": 135.98, "text": "have"},
                    {"start": 136.34, "text": "it"},
                    {"start": 136.64, "text": "all", "end": 137.44},
                ]
            },
            {
                "words": [
                    {"start": 137.44, "text": "I"},
                    {"start": 137.68, "text": "will"},
                    {"start": 137.96, "text": "rise", "end": 139.50},
                ]
            },
            {
                "words": [
                    {"start": 139.50, "text": "and"},
                    {"start": 140.00, "text": "I"},
                    {"start": 140.20, "text": "will"},
                    {"start": 140.48, "text": "fly", "end": 142.12},
                ]
            },
            {
                "words": [
                    {"start": 142.12, "text": "in"},
                    {"start": 142.40, "text": "contests"},
                    {"start": 143.66, "text": "where"},
                    {"start": 144.30, "text": "my"},
                    {"start": 144.88, "text": "dreams"},
                    {"start": 145.56, "text": "won't"},
                    {"start": 146.24, "text": "die", "end": 147.48},
                ]
            },
            {
                "words": [
                    {"start": 147.48, "text": "Step"},
                    {"start": 147.90, "text": "away", "end": 149.70},
                ]
            },
            {
                "words": [
                    {"start": 149.70, "text": "from"},
                    {"start": 150.00, "text": "duels"},
                    {"start": 150.38, "text": "of"},
                    {"start": 150.64, "text": "might", "end": 152.50},
                ]
            },
            {
                "words": [
                    {"start": 152.50, "text": "to"},
                    {"start": 153.24, "text": "where"},
                    {"start": 153.94, "text": "beauty"},
                    {"start": 155.14, "text": "takes"},
                    {"start": 155.88, "text": "its"},
                    {"start": 156.48, "text": "flight", "end": 160.30},
                ]
            },
            {
                "words": [
                    {"start": 160.30, "text": "Now"},
                    {"start": 162.22, "text": "you"},
                    {"start": 162.72, "text": "see"},
                    {"start": 164.74, "text": "the"},
                    {"start": 165.28, "text": "spark"},
                    {"start": 167.64, "text": "in"},
                    {"start": 169.06, "text": "me", "end": 176.0},
                ]
            },
        ],
        "coldmetal.ogg" : [
            {
                "words": [
                    {"start": 30.47, "text": "We"},
                    {"start": 31.46, "text": "hold"},
                    {"start": 32.49, "text": "on"},
                    {"start": 32.54, "text": "tight"},
                    {"start": 33.42, "text": "for"},
                    {"start": 34.12, "text": "another"},
                    {"start": 34.92, "text": "day", "end": 37.68},
                ]
            },
            {
                "words": [
                    {"start": 37.68, "text": "Like"},
                    {"start": 38.04, "text": "a"},
                    {"start": 39.22, "text": "gentle"},
                    {"start": 39.72, "text": "light"},
                    {"start": 40.60, "text": "serving"},
                    {"start": 41.52, "text": "love"},
                    {"start": 41.86, "text": "and"},
                    {"start": 42.18, "text": "grace", "end": 45.30},
                ]
            },
            {
                "words": [
                    {"start": 45.30, "text": "I"},
                    {"start": 46.40, "text": "know"},
                    {"start": 46.68, "text": "they"},
                    {"start": 46.98, "text": "can't"},
                    {"start": 48.32, "text": "see"},
                    {"start": 48.52, "text": "our"},
                    {"start": 48.74, "text": "heart"},
                    {"start": 49.10, "text": "and"},
                    {"start": 49.40, "text": "faith", "end": 52.12},
                ]
            },
            {
                "words": [
                    {"start": 52.12, "text": "We"},
                    {"start": 52.34, "text": "rise"},
                    {"start": 53.68, "text": "and"},
                    {"start": 53.92, "text": "we"},
                    {"start": 54.16, "text": "fall"},
                    {"start": 55.50, "text": "in"},
                    {"start": 55.92, "text": "fleeting"},
                    {"start": 56.42, "text": "ways", "end": 61.84},
                ]
            },
            {
                "words": [
                    {"start": 61.84, "text": "They"},
                    {"start": 64.50, "text": "cannot"},
                    {"start": 64.98, "text": "know"},
                    {"start": 65.86, "text": "the"},
                    {"start": 66.80, "text": "fire"},
                    {"start": 67.46, "text": "within", "end": 70.16},
                ]
            },
            {
                "words": [
                    {"start": 70.16, "text": "The"},
                    {"start": 70.38, "text": "dreams"},
                    {"start": 71.76, "text": "we"},
                    {"start": 72.20, "text": "hold,"},
                    {"start": 73.14, "text": "where"},
                    {"start": 73.98, "text": "hope"},
                    {"start": 74.70, "text": "can"},
                    {"start": 74.98, "text": "win", "end": 77.40},
                ]
            },
            {
                "words": [
                    {"start": 77.40, "text": "We"},
                    {"start": 77.70, "text": "rise,"},
                    {"start": 79.00, "text": "we"},
                    {"start": 79.42, "text": "fall", "end": 80.82},
                ]
            },
            {
                "words": [
                    {"start": 80.82, "text": "We"},
                    {"start": 81.22, "text": "rise"},
                    {"start": 81.56, "text": "once"},
                    {"start": 81.84, "text": "more", "end": 84.64},
                ]
            },
            {
                "words": [
                    {"start": 84.64, "text": "A"},
                    {"start": 84.86, "text": "fragile"},
                    {"start": 86.68, "text": "heart,"},
                    {"start": 88.00, "text": "forever"},
                    {"start": 89.00, "text": "sore", "end": 91.15},
                ]
            },
            {
                "words": [
                    {"start": 124.50, "text": "They"},
                    {"start": 125.86, "text": "try"},
                    {"start": 126.08, "text": "to"},
                    {"start": 126.34, "text": "steal"},
                    {"start": 127.30, "text": "your"},
                    {"start": 128.08, "text": "shining"},
                    {"start": 128.82, "text": "chance", "end": 131.50},
                ]
            },
            {
                "words": [
                    {"start": 131.50, "text": "But"},
                    {"start": 131.74, "text": "truth"},
                    {"start": 133.10, "text": "will"},
                    {"start": 133.38, "text": "appear"},
                    {"start": 134.56, "text": "and"},
                    {"start": 135.40, "text": "we"},
                    {"start": 135.70, "text": "will"},
                    {"start": 136.04, "text": "dance", "end": 139.00},
                ]
            },
            {
                "words": [
                    {"start": 139.00, "text": "You"},
                    {"start": 140.30, "text": "gave"},
                    {"start": 140.56, "text": "your"},
                    {"start": 140.80, "text": "heart,"},
                    {"start": 142.18, "text": "you"},
                    {"start": 142.56, "text": "gave"},
                    {"start": 142.84, "text": "your"},
                    {"start": 143.02, "text": "soul", "end": 146.10},
                ]
            },
            {
                "words": [
                    {"start": 146.10, "text": "Now"},
                    {"start": 147.54, "text": "watch"},
                    {"start": 147.78, "text": "your"},
                    {"start": 147.98, "text": "story"},
                    {"start": 149.78, "text": "take"},
                    {"start": 150.10, "text": "control", "end": 156.76},
                ]
            },
            {
                "words": [
                    {"start": 156.76, "text": "Your"},
                    {"start": 157.04, "text": "voice,"},
                    {"start": 158.46, "text": "a"},
                    {"start": 158.70, "text": "storm,"},
                    {"start": 159.76, "text": "a"},
                    {"start": 160.66, "text": "raging"},
                    {"start": 161.56, "text": "sea", "end": 163.94},
                ]
            },
            {
                "words": [
                    {"start": 163.94, "text": "Will"},
                    {"start": 164.22, "text": "shatter"},
                    {"start": 166.04, "text": "chains"},
                    {"start": 167.12, "text": "and"},
                    {"start": 167.88, "text": "set"},
                    {"start": 168.58, "text": "us"},
                    {"start": 168.78, "text": "free", "end": 171.42},
                ]
            },
            {
                "words": [
                    {"start": 171.42, "text": "No"},
                    {"start": 172.70, "text": "more"},
                    {"start": 173.30, "text": "whispers,"},
                    {"start": 175.10, "text": "no"},
                    {"start": 175.34, "text": "more"},
                    {"start": 175.66, "text": "fear", "end": 178.38},
                ]
            },
            {
                "words": [
                    {"start": 178.38, "text": "Your"},
                    {"start": 178.64, "text": "triumph"},
                    {"start": 180.68, "text": "rings"},
                    {"start": 181.80, "text": "for"},
                    {"start": 182.34, "text": "all"},
                    {"start": 182.58, "text": "to"},
                    {"start": 182.76, "text": "hear", "end": 184.50},
                ]
            },
            {
                "words": [
                    {"start": 184.50, "text": "Your"},
                    {"start": 184.92, "text": "triumph"},
                    {"start": 185.82, "text": "rings", "end": 187.50},
                ]
            }
        ],
        "melody.ogg" : [
            {
                "words": [
                    {"start": 0.44, "text": "They"},
                    {"start": 0.84, "text": "tore"},
                    {"start": 1.78, "text": "at"},
                    {"start": 2.18, "text": "my"},
                    {"start": 2.60, "text": "name"},
                    {"start": 3.46, "text": "with"},
                    {"start": 4.26, "text": "hands"},
                    {"start": 4.80, "text": "unclean", "end": 7.16},
                ]
            },
            {
                "words": [
                    {"start": 7.16, "text": "Spreading"},
                    {"start": 7.68, "text": "shadows"},
                    {"start": 9.34, "text": "where"},
                    {"start": 10.14, "text": "light"},
                    {"start": 10.68, "text": "had"},
                    {"start": 11.46, "text": "been", "end": 13.94},
                ]
            },
            {
                "words": [
                    {"start": 13.94, "text": "They"},
                    {"start": 14.44, "text": "mocked"},
                    {"start": 15.26, "text": "my"},
                    {"start": 15.90, "text": "stride", "end": 17.32},
                ]
            },
            {
                "words": [
                    {"start": 17.32, "text": "They"},
                    {"start": 17.72, "text": "cursed"},
                    {"start": 18.68, "text": "my"},
                    {"start": 19.38, "text": "stand", "end": 20.72},
                ]
            },
            {
                "words": [
                    {"start": 20.72, "text": "But"},
                    {"start": 21.20, "text": "this"},
                    {"start": 22.00, "text": "sacred"},
                    {"start": 22.76, "text": "ground,"},
                    {"start": 23.70, "text": "is"},
                    {"start": 24.56, "text": "where"},
                    {"start": 25.02, "text": "I"},
                    {"start": 25.40, "text": "land", "end": 27.90},
                ]
            },
            {
                "words": [
                    {"start": 27.90, "text": "Let"},
                    {"start": 28.58, "text": "the"},
                    {"start": 28.74, "text": "thunder"},
                    {"start": 29.52, "text": "crash,"},
                    {"start": 31.36, "text": "let"},
                    {"start": 32.00, "text": "their"},
                    {"start": 32.20, "text": "fury"},
                    {"start": 33.12, "text": "rise", "end": 34.64},
                ]
            },
            {
                "words": [
                    {"start": 34.64, "text": "The"},
                    {"start": 34.90, "text": "stars"},
                    {"start": 35.80, "text": "bear"},
                    {"start": 36.18, "text": "witness,"},
                    {"start": 37.94, "text": "truth"},
                    {"start": 38.40, "text": "never"},
                    {"start": 39.22, "text": "lies", "end": 41.94},
                ]
            },
            {
                "words": [
                    {"start": 41.94, "text": "Though"},
                    {"start": 42.60, "text": "they"},
                    {"start": 42.76, "text": "scream"},
                    {"start": 43.26, "text": "to"},
                    {"start": 43.62, "text": "drown"},
                    {"start": 45.48, "text": "my"},
                    {"start": 46.36, "text": "voice"},
                    {"start": 46.94, "text": "away", "end": 48.64},
                ]
            },
            {
                "words": [
                    {"start": 48.64, "text": "I"},
                    {"start": 48.72, "text": "will"},
                    {"start": 48.90, "text": "sing"},
                    {"start": 49.92, "text": "out"},
                    {"start": 50.68, "text": "louder,"},
                    {"start": 51.94, "text": "come"},
                    {"start": 52.38, "text": "what"},
                    {"start": 52.88, "text": "may", "end": 55.68},
                ]
            },
            {
                "words": [
                    {"start": 55.68, "text": "I"},
                    {"start": 56.00, "text": "wear"},
                    {"start": 56.44, "text": "my"},
                    {"start": 56.76, "text": "scars"},
                    {"start": 58.68, "text": "on"},
                    {"start": 59.04, "text": "my"},
                    {"start": 59.46, "text": "heart"},
                    {"start": 60.04, "text": "of"},
                    {"start": 60.38, "text": "gold", "end": 62.52},
                ]
            },
            {
                "words": [
                    {"start": 62.52, "text": "But"},
                    {"start": 62.92, "text": "you"},
                    {"start": 63.46, "text": "can't"},
                    {"start": 63.90, "text": "tarnish,"},
                    {"start": 65.32, "text": "the"},
                    {"start": 65.52, "text": "silver"},
                    {"start": 66.48, "text": "of"},
                    {"start": 66.90, "text": "my"},
                    {"start": 67.36, "text": "soul", "end": 69.46},
                ]
            },
            {
                "words": [
                    {"start": 69.46, "text": "No"},
                    {"start": 69.84, "text": "chains,"},
                    {"start": 71.24, "text": "no"},
                    {"start": 71.74, "text": "power,"},
                    {"start": 73.06, "text": "no"},
                    {"start": 73.42, "text": "cruel"},
                    {"start": 74.78, "text": "embrace", "end": 76.56},
                ]
            },
            {
                "words": [
                    {"start": 76.56, "text": "Can"},
                    {"start": 76.94, "text": "strip"},
                    {"start": 77.60, "text": "away"},
                    {"start": 78.24, "text": "my"},
                    {"start": 78.82, "text": "unbroken"},
                    {"start": 80.44, "text": "grace", "end": 83.52},
                ]
            },
            {
                "words": [
                    {"start": 83.52, "text": "They"},
                    {"start": 84.06, "text": "built"},
                    {"start": 84.86, "text": "their"},
                    {"start": 85.70, "text": "towers"},
                    {"start": 87.04, "text": "on"},
                    {"start": 87.34, "text": "shifting"},
                    {"start": 88.14, "text": "sand", "end": 90.30},
                ]
            },
            {
                "words": [
                    {"start": 90.30, "text": "While"},
                    {"start": 90.49, "text": "I"},
                    {"start": 90.70, "text": "stood"},
                    {"start": 91.60, "text": "firm"},
                    {"start": 92.52, "text": "on"},
                    {"start": 92.85, "text": "this"},
                    {"start": 93.28, "text": "solid"},
                    {"start": 94.56, "text": "land", "end": 97.06},
                ]
            },
            {
                "words": [
                    {"start": 97.06, "text": "Their"},
                    {"start": 97.44, "text": "tempests"},
                    {"start": 98.34, "text": "howl,"},
                    {"start": 100.42, "text": "their"},
                    {"start": 100.90, "text": "tempests"},
                    {"start": 101.74, "text": "cry", "end": 103.78},
                ]
            },
            {
                "words": [
                    {"start": 103.78, "text": "Yet"},
                    {"start": 104.02, "text": "my"},
                    {"start": 104.30, "text": "soul"},
                    {"start": 105.14, "text": "soars"},
                    {"start": 106.02, "text": "where"},
                    {"start": 106.86, "text": "legends"},
                    {"start": 107.98, "text": "fly", "end": 110.98},
                ]
            },
            {
                "words": [
                    {"start": 110.98, "text": "Let"},
                    {"start": 111.66, "text": "their"},
                    {"start": 111.86, "text": "fires"},
                    {"start": 112.68, "text": "rage,"},
                    {"start": 114.34, "text": "let"},
                    {"start": 115.04, "text": "their"},
                    {"start": 115.28, "text": "arrows"},
                    {"start": 116.10, "text": "fall", "end": 117.80},
                ]
            },
            {
                "words": [
                    {"start": 117.80, "text": "My"},
                    {"start": 118.14, "text": "spirit"},
                    {"start": 119.02, "text": "stands"},
                    {"start": 119.42, "text": "stronger"},
                    {"start": 120.34, "text": "than"},
                    {"start": 120.80, "text": "them"},
                    {"start": 121.66, "text": "all", "end": 124.10},
                ]
            },
            {
                "words": [
                    {"start": 124.10, "text": "Though"},
                    {"start": 124.32, "text": "the"},
                    {"start": 124.56, "text": "winds"},
                    {"start": 125.42, "text": "may"},
                    {"start": 126.14, "text": "scream,"},
                    {"start": 127.52, "text": "though"},
                    {"start": 127.74, "text": "the"},
                    {"start": 127.96, "text": "earth"},
                    {"start": 128.78, "text": "may"},
                    {"start": 129.64, "text": "quake", "end": 130.88},
                ]
            },
            {
                "words": [
                    {"start": 130.88, "text": "There's"},
                    {"start": 131.34, "text": "nothing"},
                    {"start": 131.96, "text": "within"},
                    {"start": 132.56, "text": "me"},
                    {"start": 133.02, "text": "they"},
                    {"start": 133.86, "text": "can"},
                    {"start": 134.58, "text": "break", "end": 137.64},
                ]
            },
            {
                "words": [
                    {"start": 137.64, "text": "I"},
                    {"start": 138.04, "text": "wear"},
                    {"start": 138.50, "text": "my"},
                    {"start": 138.82, "text": "scars"},
                    {"start": 140.74, "text": "on"},
                    {"start": 141.10, "text": "my"},
                    {"start": 141.54, "text": "heart"},
                    {"start": 142.12, "text": "of"},
                    {"start": 142.40, "text": "gold", "end": 144.60},
                ]
            },
            {
                "words": [
                    {"start": 144.60, "text": "But"},
                    {"start": 144.80, "text": "you"},
                    {"start": 145.58, "text": "can't"},
                    {"start": 145.98, "text": "tarnish"},
                    {"start": 147.38, "text": "the"},
                    {"start": 147.56, "text": "silver"},
                    {"start": 148.60, "text": "of"},
                    {"start": 149.00, "text": "my"},
                    {"start": 149.42, "text": "soul", "end": 151.42},
                ]
            },
            {
                "words": [
                    {"start": 151.42, "text": "No"},
                    {"start": 151.96, "text": "chains,"},
                    {"start": 153.32, "text": "no"},
                    {"start": 153.84, "text": "power,"},
                    {"start": 155.16, "text": "no"},
                    {"start": 155.48, "text": "cruel"},
                    {"start": 157.12, "text": "embrace", "end": 158.64},
                ]
            },
            {
                "words": [
                    {"start": 158.64, "text": "Can"},
                    {"start": 159.00, "text": "strip"},
                    {"start": 159.62, "text": "away"},
                    {"start": 160.40, "text": "my"},
                    {"start": 160.86, "text": "unbroken"},
                    {"start": 162.52, "text": "grace", "end": 167.32},
                ]
            },
            {
                "words": [
                    {"start": 167.32, "text": "I'll"},
                    {"start": 167.74, "text": "hear"},
                    {"start": 168.42, "text": "the"},
                    {"start": 168.58, "text": "voice"},
                    {"start": 169.26, "text": "that"},
                    {"start": 169.48, "text": "whispers"},
                    {"start": 170.26, "text": "still", "end": 174.16},
                ]
            },
            {
                "words": [
                    {"start": 174.16, "text": "A"},
                    {"start": 174.52, "text": "quiet"},
                    {"start": 175.30, "text": "strength"},
                    {"start": 176.04, "text": "an"},
                    {"start": 176.28, "text": "iron"},
                    {"start": 177.02, "text": "will", "end": 179.49},
                ]
            },
            {
                "words": [
                    {"start": 179.49, "text": "Through"},
                    {"start": 180.08, "text": "icy"},
                    {"start": 180.78, "text": "storms,"},
                    {"start": 182.10, "text": "through"},
                    {"start": 182.96, "text": "blizzard's"},
                    {"start": 183.80, "text": "sting", "end": 185.92},
                ]
            },
            {
                "words": [
                    {"start": 185.92, "text": "My"},
                    {"start": 186.28, "text": "fire"},
                    {"start": 186.74, "text": "will"},
                    {"start": 187.20, "text": "burn,"},
                    {"start": 188.46, "text": "my"},
                    {"start": 188.82, "text": "soul"},
                    {"start": 189.34, "text": "will"},
                    {"start": 190.12, "text": "sing", "end": 192.76},
                ]
            },
            {
                "words": [
                    {"start": 192.76, "text": "I"},
                    {"start": 193.14, "text": "rise"},
                    {"start": 193.64, "text": "untouched"},
                    {"start": 195.70, "text": "by"},
                    {"start": 196.40, "text": "their"},
                    {"start": 197.06, "text": "disgrace", "end": 199.66},
                ]
            },
            {
                "words": [
                    {"start": 199.66, "text": "Their"},
                    {"start": 200.14, "text": "empty"},
                    {"start": 201.00, "text": "words,"},
                    {"start": 202.78, "text": "their"},
                    {"start": 203.30, "text": "fleeting"},
                    {"start": 204.40, "text": "chase", "end": 206.64},
                ]
            },
            {
                "words": [
                    {"start": 206.64, "text": "No"},
                    {"start": 206.96, "text": "crown,"},
                    {"start": 208.04, "text": "no"},
                    {"start": 208.86, "text": "throne,"},
                    {"start": 210.18, "text": "no"},
                    {"start": 210.54, "text": "fleeting"},
                    {"start": 212.42, "text": "praise", "end": 213.72},
                ]
            },
            {
                "words": [
                    {"start": 213.72, "text": "Can"},
                    {"start": 214.10, "text": "steal"},
                    {"start": 214.58, "text": "from"},
                    {"start": 214.98, "text": "me"},
                    {"start": 215.40, "text": "my"},
                    {"start": 215.81, "text": "unbroken"},
                    {"start": 217.90, "text": "grace", "end": 220.58},
                ]
            },
            {
                "words": [
                    {"start": 220.58, "text": "Let"},
                    {"start": 220.92, "text": "them"},
                    {"start": 221.10, "text": "carve"},
                    {"start": 222.06, "text": "their"},
                    {"start": 222.94, "text": "names"},
                    {"start": 223.86, "text": "in"},
                    {"start": 224.66, "text": "fading"},
                    {"start": 225.42, "text": "stone", "end": 227.78},
                ]
            },
            {
                "words": [
                    {"start": 227.78, "text": "But"},
                    {"start": 228.24, "text": "dignity's"},
                    {"start": 229.94, "text": "mine"},
                    {"start": 231.52, "text": "alone", "end": 234.80},
                ]
            },
            {
                "words": [
                    {"start": 234.80, "text": "No"},
                    {"start": 235.18, "text": "storms,"},
                    {"start": 236.50, "text": "no"},
                    {"start": 236.96, "text": "shadows,"},
                    {"start": 238.32, "text": "no"},
                    {"start": 238.68, "text": "time's"},
                    {"start": 240.22, "text": "embrace", "end": 241.86},
                ]
            },
            {
                "words": [
                    {"start": 241.86, "text": "Can"},
                    {"start": 242.32, "text": "ever"},
                    {"start": 242.76, "text": "dim"},
                    {"start": 243.64, "text": "this"},
                    {"start": 243.94, "text": "flame,"},
                    {"start": 245.40, "text": "my"},
                    {"start": 245.80, "text": "unbroken"},
                    {"start": 247.34, "text": "grace", "end": 257.0},
                ]
            },
        ]
    }