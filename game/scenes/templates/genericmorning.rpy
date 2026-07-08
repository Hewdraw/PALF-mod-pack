label genericmorning:

stop music fadeout 1.5

call calendar(1) from _call_calendar_67

python:
    day, month, year = daytuple
    calDate = calDate.replace(day=day, month=month, year=year)
    renpy.music.queue("Audio/Morning_ambience.ogg", channel='music', loop=True, fadein=1.5, tight=None)
    timeOfDay = "Morning"

pause 0.5

show screen currentdate with dis

call morningscenequeue() from _call_morningscenequeue_1

stop music fadeout 1.5

jump homeroom1transition