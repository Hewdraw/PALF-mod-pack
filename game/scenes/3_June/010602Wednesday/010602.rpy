label day010602:

stop music fadeout 1.5

call calendar(1) from _call_calendar_58
$ calDate = calDate.replace(day=2, month=6, year=2004)
$ renpy.music.queue("Audio/Morning_ambience.ogg", channel='music', loop=True, fadein=1.5, tight=None)
$ timeOfDay = "Morning"

call morningscenequeue() from _call_morningscenequeue

jump homeroom1transition