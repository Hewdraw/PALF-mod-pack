init python:
    def linspace(start, stop, num, decrease=True):
        step = (stop - start) / (num-1) # Set step size according to limit and desired size.
        ls = [start + i * step for i in range(num)] # Generate list [start, start + step, start + 2*step, ..., stop]

        return ls if not decrease else ls[::-1] # Reverse to descending if needed.

    # Gradually changes the font size from one size to the other, by character.
    # Arguments are separated by dashes.
    # Arguments:
    # 'start' (int): The starting font size.
    # 'stop' (int): The final font size.
    # Example: {gradualsize=36-5}Text{/gradualsize}
    # Example: {gradualsize=5-36}Text{/gradualsize}
    def gradualsize_tag(tag, argument, contents):
        args = [int(a) for a in argument.split("-")]
        start, stop, decrease = min(args), max(args), args[0] > args[1]
        num = 0

        for kind, txt in contents:
            if kind == renpy.TEXT_TEXT: # Actual text - sum over to get needed steps.
                num += len(txt)
        
        linsp = linspace(start, stop, num, decrease)
        currsizeind = 0

        rv = []
        
        for kind, txt in contents:
            if kind == renpy.TEXT_TEXT: # Do we manipulate the tags?
                for char in txt:
                    rv.append((renpy.TEXT_TAG, u"size={}".format(round(linsp[currsizeind]))))
                    rv.append((renpy.TEXT_TEXT, char))
                    rv.append((renpy.TEXT_TAG, u"/size"))
                    currsizeind += 1

            else: # Keep other stuff untouched.
                rv.append((kind, txt))



        return rv

    config.custom_text_tags["gradualsize"] = gradualsize_tag