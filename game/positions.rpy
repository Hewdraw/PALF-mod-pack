define dip_white = Fade(1.0, 1.0, 0.5, color="#ffffff")

transform farleftside:
    xcenter 0.12

transform leftside:
    xcenter 0.25

transform midleftside:
    xcenter 0.37

transform centerside:
    xcenter 0.5

transform midrightside:
    xcenter 0.63

transform rightside:
    xcenter 0.75

transform farrightside:
    xcenter 0.88

transform dissolvein:
    alpha 0.0
    ease 1.0 alpha 1.0

transform moveinleft:
    xcenter 1.5
    ease 1.0 xcenter 0.5

transform hovering:
    animation
    0.2
    yoffset 10
    0.2
    yoffset -10
    repeat

transform itemhover:
    subpixel True
    alpha 0.0 xalign 0.5 yalign 0.5 zoom 0.0 rotate 10
    block:
        parallel:
            ease 0.25 alpha 1.0 zoom 1.0 yalign 0.3
        parallel:
            ease 0.25 rotate -10
            ease 0.25 rotate 10
            repeat 4
    ease 0.25 rotate 0 zoom 0.75

transform itemhide:
    subpixel True
    rotate 0 zoom 0.75 yalign 0.3
    ease 0.25 zoom 0.4 xalign 0.98 yalign 0.88
    pause 0.75
    ease 0.25 zoom 0.0

transform itemgive:
    alpha 1.0 yalign 0.97 xalign 0.98 zoom 0.0
    pause 0.25
    ease 0.5 zoom 0.5 xalign 0.5 yalign 0.5

transform highlightmove(xloc, start_xpos, orientation):
    ease 0.5 ypos 1.2 zoom 1.3 xpos xloc xzoom (-1 if (((xloc if xloc != 0.5 else start_xpos) < 0.5 and orientation == "Left") or ((xloc if xloc != 0.5 else start_xpos) > 0.5 and orientation == "Right")) else 1)


transform getcloser:
    ypos 1.0 zoom 1.0
    ease 0.5 zoom 1.3 ypos 1.2

transform getfurther:
    ypos 1.2 zoom 1.3
    ease 0.5 zoom 1.0 ypos 1.0

transform sepia:
    matrixcolor SepiaMatrix()

transform grayscale:
    matrixcolor SaturationMatrix(0.0)

transform monochrome:
    matrixcolor SaturationMatrix(0.0) * ContrastMatrix(2.0)

transform night:
    matrixcolor nightmatrix

transform morning:
    matrixcolor TintMatrix(Color(rgb=(.95,.80,.75))) * BrightnessMatrix(-0.10) * ContrastMatrix(1.2)

transform pointsup(oldpos):
    subpixel True
    xpos oldpos[0] ypos oldpos[1] zoom 0.0 rotate 360
    parallel:
        ease 0.25 zoom 1.0 rotate 0
        #pause 0.25
        #ease 1.0 alpha 0.0
    parallel:
        pause 1.6
        ease 0.3 rotate 360 ypos 1.02 xpos 0.5
    parallel:
        ease 1.5 xpos (oldpos[0] + 0.04) ypos oldpos[1] - 0.11

transform hall_move1:
    transform_anchor True
    rotate_pad True
    anchor (0.5,1.0)
    xpos 960 yalign 1.0 rotate 0
    linear 0.1 xpos 1160 yalign 0.85 zoom 1.1 rotate -3

transform hall_move2:
    transform_anchor True
    rotate_pad True
    anchor (0.5,1.0)
    xpos 1160 yalign 0.85 zoom 1.1 rotate -3
    linear 0.1 xpos 960 yalign 1.0 zoom 1.0 rotate 0

transform vspaz:
    subpixel True
    alpha 0.0 xalign 0.5 yalign 0.0
    ease 0.1 alpha 1.0 yalign 0.65
    ease 0.02 yalign 0.35
    ease 0.01 yalign 0.6
    ease 0.01 yalign 0.4
    ease 0.02 yalign 0.55
    ease 0.01 yalign 0.45
    ease 0.01 yalign 0.53
    ease 0.01 yalign 0.48
    ease 0.02 yalign 0.5
    pause 2.0
    ease 0.5 alpha 0.0

transform dormdesk:
    xpos 0.5 ypos 0.78

transform pokeball:
    animation
    matrixcolor BrightnessMatrix(1.0) * ContrastMatrix(0.0) zoom 0.0 xanchor 0.5 yanchor 0.95
    parallel:
        ease 0.2 zoom 1.0
    parallel:
        ease 2.0 matrixcolor BrightnessMatrix(0.0) * ContrastMatrix(1.0)

transform backinpokeball:
    matrixcolor BrightnessMatrix(0.0) * ContrastMatrix(1.0) zoom 1.0 xanchor 0.5 yanchor 0.95
    parallel:
        pause 1.8
        ease 0.2 zoom 0.0
    parallel:
        ease 2.0 matrixcolor BrightnessMatrix(1.0) * ContrastMatrix(0.0)

transform choicefade:
    subpixel True
    alpha 0.0
    ease 0.5 alpha 1.0
    on hide:
        ease 0.5 alpha 0.0

transform fadeinleft(finalpos):
    alpha 0.0 xpos 0.0
    ease 0.7 xpos finalpos alpha 1.0

transform fadeinright(finalpos):
    alpha 0.0 xpos 1.0
    ease 0.7 xpos finalpos alpha 1.0

transform scrollfadein:
    alpha 0.0
    pause 0.1
    ease 0.3 alpha 1.0

transform varfadein(time):
    alpha 0.0
    pause time
    ease 0.3 alpha 1.0

transform fadechibis:
    alpha 0.0
    ease 0.3 alpha 1.0

transform dicerolltrans:
    xpos 1.0 ypos -0.3
    parallel:
        ease 2.0 xpos 0.14 + 160 / 1920
    parallel:
        easein_bounce 2.0 ypos 0.25 + 160 / 1080

transform collide(startingpos, firstoffset, collisionpoint):
    pause 4.0
    xpos startingpos
    ease 0.3 xpos firstoffset
    pause 0.1
    ease 0.1 xpos collisionpoint
    alpha 0.0

transform totalnum:
    alpha 0.0 zoom 0.0 rotate 0
    pause 4.5
    parallel:
        ease 0.3 alpha 1.0
    parallel: 
        ease 0.2 rotate 359
        rotate 0
    parallel:
        ease 0.3 zoom 1.0

transform swipeinleft:
    alpha 0.0 ypos 0.2 xpos -500
    ease 0.4 ypos 0.35 alpha 1.0 xpos 50
    linear 1.2 ypos 0.45 xpos 100
    ease 0.6 ypos 1.0 xpos -2000

transform swipeinleftslow:
    alpha 0.0 ypos 0.1 xpos -500
    ease 1.0 ypos 0.17 alpha 1.0 xpos 50
    linear 3.0 ypos 0.23 xpos 100
    ease 1.5 ypos 1.0 xpos -2000

transform swipeinright:
    alpha 0.0 ypos 0.2 xpos 1920 + 500
    ease 0.4 ypos 0.35 alpha 1.0 xpos 1920 - 50
    linear 1.2 ypos 0.45 xpos 1920 - 100
    ease 0.6 ypos 1.0 xpos 1920 + 2000

transform garden_move1:
    transform_anchor True
    rotate_pad True
    anchor (0.5,1.0)
    xpos 960 rotate 0
    linear 0.1 xpos 1160 yalign 0.85 zoom 1.1 rotate -3
    
transform garden_move2:
    transform_anchor True
    rotate_pad True
    anchor (0.5,1.0)
    xpos 1160 yalign 0.85 zoom 1.1 rotate -3
    linear 0.1 xpos 960 zoom 0.84781 rotate 0

transform evolveaway:
    align (0.5, 0.5) alpha 0.0 zoom 0.0 matrixcolor BrightnessMatrix(0)
    ease 1.0 zoom 1.0 alpha 1.0 
    pause 2.0
    ease 0.6 zoom 0.9 matrixcolor BrightnessMatrix(0.1)
    ease 0.6 zoom 0.8 matrixcolor BrightnessMatrix(0.2)
    ease 0.6 zoom 0.9 matrixcolor BrightnessMatrix(0.3)
    ease 0.6 zoom 0.7 matrixcolor BrightnessMatrix(0.4)
    ease 0.6 zoom 0.9 matrixcolor BrightnessMatrix(0.5)
    ease 0.6 zoom 0.6 matrixcolor BrightnessMatrix(0.6)
    ease 0.6 zoom 0.9 matrixcolor BrightnessMatrix(0.7)
    ease 0.6 zoom 0.5 matrixcolor BrightnessMatrix(0.8)
    ease 0.6 zoom 0.9 matrixcolor BrightnessMatrix(0.9)
    ease 0.6 zoom 0.3 matrixcolor BrightnessMatrix(1.0)
    ease 0.6 zoom 0.9 matrixcolor BrightnessMatrix(1.0)
    ease 0.6 zoom 0.3 matrixcolor BrightnessMatrix(1.0)
    ease 0.6 zoom 0.9 matrixcolor BrightnessMatrix(1.0)
    ease 0.6 zoom 0.3 matrixcolor BrightnessMatrix(1.0)
    ease 0.6 zoom 0.9 matrixcolor BrightnessMatrix(1.0)
    ease 0.6 zoom 0.3 matrixcolor BrightnessMatrix(1.0)
    ease 0.6 zoom 0.9 matrixcolor BrightnessMatrix(1.0)
    ease 0.6 zoom 0.3 matrixcolor BrightnessMatrix(1.0)
    ease 0.6 zoom 0.9 matrixcolor BrightnessMatrix(1.0)
    ease 0.6 zoom 0.2 matrixcolor BrightnessMatrix(1.0)
    ease 0.6 zoom 0.9 matrixcolor BrightnessMatrix(1.0)
    ease 0.6 zoom 0.1 matrixcolor BrightnessMatrix(1.0)
    ease 0.6 zoom 0.9 matrixcolor BrightnessMatrix(1.0)
    ease 0.6 zoom 0.0 matrixcolor BrightnessMatrix(1.0)

transform evolvein:
    align (0.5, 0.5) zoom 0.0 matrixcolor BrightnessMatrix(0)
    pause 2.4
    ease 0.6 zoom 0.1 matrixcolor BrightnessMatrix(1.0)
    ease 0.6 zoom 0.0 matrixcolor BrightnessMatrix(1.0)
    ease 0.6 zoom 0.2 matrixcolor BrightnessMatrix(1.0)
    ease 0.6 zoom 0.0 matrixcolor BrightnessMatrix(1.0)
    ease 0.6 zoom 0.3 matrixcolor BrightnessMatrix(1.0)
    ease 0.6 zoom 0.0 matrixcolor BrightnessMatrix(1.0)
    ease 0.6 zoom 0.4 matrixcolor BrightnessMatrix(1.0)
    ease 0.6 zoom 0.0 matrixcolor BrightnessMatrix(1.0)
    ease 0.6 zoom 0.5 matrixcolor BrightnessMatrix(1.0)
    ease 0.6 zoom 0.0 matrixcolor BrightnessMatrix(1.0)
    ease 0.6 zoom 0.6 matrixcolor BrightnessMatrix(1.0)
    ease 0.6 zoom 0.0 matrixcolor BrightnessMatrix(1.0)
    ease 0.6 zoom 0.7 matrixcolor BrightnessMatrix(1.0)
    ease 0.6 zoom 0.0 matrixcolor BrightnessMatrix(1.0)
    ease 0.6 zoom 0.7 matrixcolor BrightnessMatrix(1.0)
    ease 0.6 zoom 0.0 matrixcolor BrightnessMatrix(1.0)
    ease 0.6 zoom 0.7 matrixcolor BrightnessMatrix(1.0)
    ease 0.6 zoom 0.0 matrixcolor BrightnessMatrix(1.0)
    ease 0.6 zoom 0.7 matrixcolor BrightnessMatrix(1.0)
    ease 0.6 zoom 0.0 matrixcolor BrightnessMatrix(1.0)
    ease 0.6 zoom 0.8 matrixcolor BrightnessMatrix(1.0)
    ease 0.6 zoom 0.0 matrixcolor BrightnessMatrix(1.0)
    ease 0.6 zoom 0.9 matrixcolor BrightnessMatrix(1.0)
    ease 0.6 zoom 0.0 matrixcolor BrightnessMatrix(1.0)
    ease 0.6 zoom 1.0 matrixcolor BrightnessMatrix(1.0)
    ease 5.0 zoom 1.2 matrixcolor BrightnessMatrix(0)

transform ditto:
    zoom 0
    ease 3 zoom 1.2

transform speedlines:
    yalign 0.5 xalign 0.5 alpha 0.0 zoom 3.25 rotate 0
    parallel:
        pause 1.0
        ease 3.0 alpha 1.0
        pause 17.5
        easeout_circ 0.5 alpha 0.0
    parallel:
        ease 5.5 zoom 1.5
        pause 15
        easeout_circ 0.5 zoom 5.0
    parallel:
        easeout_circ 22 rotate 3600

transform liberizemovein: 
    xpos 2.0 ypos 2.0
    ease 0.5 xpos 1.0 ypos 1.0 xanchor 1.0 yanchor 1.0

transform liberizefadein:
    xpos 2.0 ypos 2.0 alpha 0.0
    ease 0.5 xpos 1.0 ypos 1.0 xanchor 1.0 yanchor 1.0 alpha 1.0

transform liberizeactivefadein:
    alpha 0.0
    ease 0.5 alpha 1.0

transform shinystrobe:
    animation
    matrixcolor SaturationMatrix(1.3) * HueMatrix(0.2 * 360.0)
    block:
        ease 5.0 matrixcolor SaturationMatrix(1.3) * HueMatrix(0.8 * 360.0)
        ease 5.0 matrixcolor SaturationMatrix(1.3) * HueMatrix(0.2 * 360.0)
        repeat

transform tintstrobe:
    animation
    block:
        ease 2.0 matrixcolor TintMatrix("#fc8c8c")
        ease 2.0 matrixcolor TintMatrix("#8cfc8c")
        ease 2.0 matrixcolor TintMatrix("#8c8cfc")
        repeat

transform hoverfloat:
    yanchor 1.0 xanchor 0.0 blur 3.0
    parallel:
            ease 2.0 yanchor 0.98
            ease 2.0 yanchor 1.0
            repeat
    parallel:
        ease 2.0 xanchor 0.02
        ease 2.0 xanchor 0.0
        ease 2.0 xanchor -0.02
        ease 2.0 xanchor 0.0
        repeat

transform pausethendis(pausetime):
    alpha 0.0
    pause pausetime
    ease 0.5 alpha 1.0

transform outofscreenleft:
    xpos -0.5

transform contestcenter:
    xpos 0.53 ypos 0.7

transform slideincontest(endpoint, grouppos, groupsize):
    xpos -0.3
    ease 0.5 xpos endpoint + ((grouppos - (groupsize - 1) / 2) * 0.1)

transform slideoutcontest(timeoffset):
    ease 0.5 + timeoffset xpos -0.3

transform slideinmoncontest(endpoint=0.55):
    anchor (0.5, 0.5) pos (-0.3, 0.5) xzoom -1.0
    ease 0.5 xpos endpoint

transform slideoutmoncontest(startpoint=0.55):
    xpos startpoint ypos 0.5
    ease 0.5 ypos 2.5

transform contestmoveanimation(energy = False, xend=0.55, yend = 0.5):
    pos (xend, yend) anchor (0.5, 0.5) rotate 0
    ease 0.5 pos (xend-0.05, yend-0.05) rotate (10 if not energy else 360)
    ease 0.1 pos (xend+0.05, yend+0.05) rotate (-10 if not energy else 370)
    ease 0.1 pos (xend, yend) rotate (0 if not energy else 360)

transform moveincontest(xlocation, grouppos, groupsize, ystart, yend=1.35):
    xpos xlocation + ((grouppos - (groupsize - 1) / 2) * 0.1) ypos ystart
    ease 0.5 xpos xlocation + ((grouppos - (groupsize - 1) / 2) * 0.1) ypos yend

transform coordposswitch(startpoint, endpoint, grouppos, groupsize, yend = 1.35):
    xpos startpoint + ((grouppos - (groupsize - 1) / 2) * 0.1) ypos yend
    ease 0.5 xpos endpoint + ((grouppos - (groupsize - 1) / 2) * 0.1)

transform contestwinner(grouppos, groupsize):
    zoom 0.3 xpos -1.5 matrixcolor BrightnessMatrix(-1) ypos 0.55
    ease 4 xpos 0.5 + ((grouppos - (groupsize - 1) / 2) * 0.1)

transform contestwinnerreveal(grouppos, groupsize):
    zoom 0.3 xpos 0.5 + ((grouppos - (groupsize - 1) / 2) * 0.1) matrixcolor None ypos 0.55

transform sidebarcontest:
    xpos -0.1 yanchor 0
    ease 0.3 xpos 0.08 yanchor 0.35
    pause 2.0
    ease 1.0 xpos -0.1 yanchor 0

transform desaturate:
    animation 
    matrixcolor SaturationMatrix(1.0)
    ease 3.0 matrixcolor SaturationMatrix(0.0)

transform loff:
    xpos -0.2

transform roff:
    xpos 1.2

transform flip:
    xzoom -1

transform closecenter:
    ease 0.5 xpos 0.5 ypos 1.2 zoom 1.3

define fadeinbottom = ComposeTransition(Dissolve(0.5), after=easeinbottom)
define fadeoutbottom = ComposeTransition(Dissolve(0.5), after=easeoutbottom)

define dis = { "master" : Dissolve(0.25) }
define slowdis = { "master" : Dissolve(3.0) }
define superslowdis = { "master" : Dissolve(6.0) }
define gaussdis = { "master" : ImageDissolve(im.Tile("GFX/gauss.webp"), 3.0, 90) }

init python:
    splitfadeslow = ImageDissolve(im.Tile("GFX/TransMask.webp"), 2.5, 64)
    splitfade = ImageDissolve("GFX/TransMask.webp", 1.5, 64)
    splitfadereverse = ImageDissolve("GFX/TransMask.webp", 1.5, 64, reverse=True)
    splitfadefast = ImageDissolve(im.Tile("GFX/TransMask.webp"), 0.8, 64)
    splitfadefaster = ImageDissolve(im.Tile("GFX/TransMask.webp"), 0.4, 64)
    splitfadedown = ImageDissolve(im.Tile("GFX/VertTransMask.webp"), 1.5, 64)
    splitfadedownfaster = ImageDissolve(im.Tile("GFX/VertTransMask.webp"), 0.4, 64)
    spinfade = ImageDissolve(im.Tile("GFX/TransTwirl.webp"), 1.5, 64)
    spinfaderapid = ImageDissolve(im.Tile("GFX/TransTwirl.webp"), 0.3, 64)
    transball = ImageDissolve(im.Tile("GFX/TransBall.webp"), 2.0, 90)
    transeye = ImageDissolve(im.Tile("GFX/TransEye.webp"), 1.0, 90)
    transeyefast = ImageDissolve(im.Tile("GFX/TransEye.webp"), 0.4, 90)
    transeye2 = ImageDissolve(im.Tile("GFX/TransEye2.webp"), 1.0, 90)
    transeye2fast = ImageDissolve(im.Tile("GFX/TransEye2.webp"), 0.4, 90)
    transeye2slow = ImageDissolve(im.Tile("GFX/TransEye2.webp"), 5.0, 90)
    gaussdissolve = ImageDissolve(im.Tile("GFX/gauss.webp"), 3.0, 90)

    transeye2nopause = { "master" : ImageDissolve(im.Tile("GFX/TransEye2.webp"), 1.0, 90) }
    transeye2nopausefast = { "master" : ImageDissolve(im.Tile("GFX/TransEye2.webp"), 0.4, 90) }

    def _even_positions(n, left=None, right=None):
        # Equal-gaps by default: k/(n+1), k=1..n
        if n <= 1:
            return [0.5]
        if left is None or right is None:
            gap = 1.0 / (n + 1.0)
            return [gap * (i + 1) for i in range(n)]
        step = (right - left) / float(n - 1)
        return [left + i * step for i in range(n)]

    def _visual_xzoom(tag, layer="master"):
        """
        Best-effort estimate of the current on-screen horizontal position of `tag`.
        Uses placement (xpos + normalized xoffset). Falls back to style/xalign if needed.
        """
        try:
            d = renpy.scene_lists().get_displayable_by_tag(layer, tag)
            
            if d is None:
                return 1

            xzoom = d.xzoom

            if (xzoom is None):
                return 1

            if (isinstance(xzoom, int) or isinstance(xzoom, float)):
                return xzoom

            return 1

        except Exception:
            return 1

    def _visual_x(tag, layer="master"):
        """
        Best-effort estimate of the current on-screen horizontal position of `tag`.
        Uses placement (xpos + normalized xoffset). Falls back to style/xalign if needed.
        """
        try:
            d = renpy.scene_lists().get_displayable_by_tag(layer, tag)
            
            if d is None:
                return 0.5

            xpos = renpy.get_placement(d).xpos

            if (xpos is None):
                return 0.5

            if (isinstance(xpos, float)):
                return xpos

            return xpos.absolute + xpos.relative

        except Exception:
            return 0.5

    def LineUp(duration=0.5, layer="master", left=None, right=None, exclude=None, prefilled=None, inner_band=None, considerexcludes=True, atlist=[]):
        global lastmovein
        """
        Evenly space shown sprites (by tag) on `layer`, easing into targets.

        Behavior summary:
        - All currently shown portrait sprites are considered for alignment.
        - Always maintains an outer margin (no sprites on exact left/right edges).
        - Always preserves current left→right visual order.
        - If inner_band > 0, forbids the exclusive central band (0.5 - inner_band, 0.5 + inner_band).

        prefilled:
        - Float or iterable of floats in [0.0, 1.0] treated as already-occupied slots.

        inner_band:
        - Half-width around 0.5. For example, 0.08 forbids (0.42, 0.58) exclusively.
        """

        # Collect tags currently showing (limit to known portrait asset tags).
        try:
            showing = list(renpy.get_showing_tags(layer))
        except Exception:
            showing = []
        showing = [t for t in showing if t in portraitassetlist]

        # Normalize exclude -> set
        ex = set()
        if exclude:
            if isinstance(exclude, str):
                exclude = [exclude]
            exclude = [item.lower() for item in exclude]
            ex |= set(exclude)

        # Determine movable/excluded tags
        movable = [t for t in showing if t.lower() not in ex]
        excluded_considered = [t for t in showing if t.lower() in ex] if considerexcludes else []

        # Nothing to do?
        if not movable and not excluded_considered and not prefilled:
            return

        # Combined on-screen tags (movable first, then excluded), always preserve order
        combined = movable + excluded_considered
        if len(combined) > 1:
            combined.sort(key=lambda t: _visual_x(t, layer))

        # --- normalize prefilled ---
        if prefilled is None:
            prefilled_list = []
        elif isinstance(prefilled, (int, float)):
            prefilled_list = [float(prefilled)]
        else:
            prefilled_list = [float(p) for p in prefilled]
        prefilled_list = [min(1.0, max(0.0, p)) for p in prefilled_list]

        # Determine global bounds
        L_bound = 0.0 if left is None else float(left)
        R_bound = 1.0 if right is None else float(right)
        if L_bound > R_bound:
            L_bound, R_bound = R_bound, L_bound  # swap if misordered

        # --- helpers (outer margins always active) ---
        def _even_positions_open(n, a, b):
            """Evenly space n points in (a, b) — one gap off each outer edge."""
            if n <= 0:
                return []
            if b <= a:
                mid = (a + b) / 2.0
                return [mid] * n
            denom = n + 1  # open on both outer ends
            step = (b - a) / float(denom)
            start_k = 1
            return [a + (start_k + i) * step for i in range(n)]

        def _even_positions_two_intervals_open(n, a1, b1, a2, b2):
            len1 = max(0.0, b1 - a1)
            len2 = max(0.0, b2 - a2)
            if n <= 0:
                return []
            if len1 <= 0 and len2 <= 0:
                mid = (L_bound + R_bound) / 2.0
                return [mid] * n
            if len1 <= 0:
                return _even_positions_open(n, a2, b2)
            if len2 <= 0:
                return _even_positions_open(n, a1, b1)
            if n == 1:
                return _even_positions_open(1, a1, b1) if len1 >= len2 else _even_positions_open(1, a2, b2)

            n1 = int(round(n * (len1 / (len1 + len2))))
            n1 = max(0, min(n, n1))
            n2 = n - n1
            if n >= 2:
                if n1 == 0 and len1 > 0:
                    n1, n2 = 1, n - 1
                if n2 == 0 and len2 > 0:
                    n2, n1 = 1, n - 1

            left_slots  = _even_positions_open(n1, a1, b1) if n1 > 0 else []
            right_slots = _even_positions_open(n2, a2, b2) if n2 > 0 else []
            return left_slots + right_slots

        # Compute exclusive inner barriers from inner_band (half-width around 0.5)
        use_barriers = inner_band is not None and float(inner_band) > 0.0
        if use_barriers:
            halfw = float(inner_band)
            il = 0.5 - halfw
            ir = 0.5 + halfw
            # Clamp barriers to global bounds and ensure order
            il = max(L_bound, min(R_bound, il))
            ir = max(L_bound, min(R_bound, ir))
            if il > ir:
                il, ir = ir, il
        else:
            il = ir = None

        # Total slots to generate
        total_slots = len(combined) + len(prefilled_list)
        if total_slots <= 0:
            return

        # Build targets with permanent outer margins and exclusive inner edges
        if use_barriers and il is not None and ir is not None and il < ir:
            # Allowed intervals: [L_bound, il) and (ir, R_bound]
            targets = _even_positions_two_intervals_open(total_slots, L_bound, il, ir, R_bound)
        else:
            # Single allowed interval: (L_bound, R_bound)
            targets = _even_positions_open(total_slots, L_bound, R_bound)

        # Reserved positions: excluded tags' current x (if considered) + explicit prefilled positions
        reserved_positions = ([_visual_x(t, layer) for t in excluded_considered] if considerexcludes else [])
        if prefilled_list:
            reserved_positions.extend(prefilled_list)

        # Remove nearest targets to each reserved position
        for rp in reserved_positions:
            if not targets:
                break
            min_idx = min(range(len(targets)), key=lambda i: abs(targets[i] - rp))
            targets.pop(min_idx)

        # Apply movement only to movable tags; excluded ones keep their current placement.
        exclusionoffset = 0
        for i, tag in enumerate(combined):
            if tag not in movable:
                exclusionoffset -= 1
                continue

            try:
                attrs = renpy.get_attributes(tag, layer=layer)
            except Exception:
                attrs = []
            name = tuple([tag] + list(attrs))
            startx = _visual_x(tag, layer)

            idx = i + exclusionoffset
            if idx < 0 or idx >= len(targets):
                continue

            target_x = targets[idx]

            direction = persondex[imageToCharDict[name[0]]]["Direction"]
            #so that characters who move to the middle will face new characters entering the scene
            if (abs(target_x-0.5) < 0.01):
                xzoom = _visual_xzoom(name[0])

                if (direction == "Left" and lastmovein == "Left" and xzoom == -1
                    or direction == "Left" and lastmovein == "Right" and xzoom == 1):
                    direction = "Right"
                elif (direction == "Right" and lastmovein == "Right" and xzoom == -1
                    or direction == "Right" and lastmovein == "Left" and xzoom == 1):
                    direction = "Left"

                # so that characters who *stay* in the middle will still shift position appropriately when made to lineup. 
                # Most likely not be common
                if (startx == 0.5):
                    if (direction == "Left"):
                        startx = 0.49
                    elif (direction == "Right"):
                        startx = 0.51

            renpy.show(
                name,
                layer=layer,
                tag=tag,
                zorder=abs(target_x - 0.5) * 10,
                at_list=atlist + [
                    slide_to(
                        startx,
                        target_x,
                        duration,
                        direction
                    )
                ]
            )

    def SmartShift(tag, pos, duration=0.5, layer="master", atlist=[]):
        """
        Moves a character from one position to another, ensuring that they show up "behind" other characters who are closer to the side of the screen, and flips their facingness, if appropriate, so they are always facing inward.
        """ 
        try:
            attrs = renpy.get_attributes(tag, layer=layer)
        except Exception:
            attrs = []
        name = tuple([tag] + list(attrs))

        renpy.show(name, layer=layer, tag=tag, zorder=abs(pos- 0.5) * 10, at_list=atlist + [slide_to(_visual_x(tag, layer), pos, duration, persondex[imageToCharDict[name[0]]]["Direction"])])

    def ss(tag, pos, duration=0.5, layer="master", atlist=[]):
        """
        Alias for SmartShift.
        """
        SmartShift(tag, pos, duration, layer, atlist)

    def PutRoff(tag, duration=0, behind=[], atlist=[]):
        tag = tag.lower()
        key = tag.split()[0]
        if (isinstance(behind, str)):
            behind = [behind]
        renpy.show(tag, at_list=[Transform(xpos=1.2, xzoom=(-1 if persondex[imageToCharDict[key]]["Direction"] == "Right" else 1))] + atlist, behind=behind)

    def PutLoff(tag, duration=0, behind=[], atlist=[]):
        tag = tag.lower()
        key = tag.split()[0]
        if (isinstance(behind, str)):
            behind = [behind]
        renpy.show(tag, at_list=[Transform(xpos=-0.2, xzoom=(-1 if persondex[imageToCharDict[key]]["Direction"] == "Left" else 1))] + atlist, behind=behind)

    def MoveInRight(tag, duration=0.5):
        tag = tag.lower()
        PutRoff(tag)
        LineUp(duration)

    def MoveInLeft(tag, duration=0.5):
        tag = tag.lower()
        PutLoff(tag)
        LineUp(duration)

    def SmartMoveIn(tag, duration=0.5):
        MoveInSmart(tag, duration)

    def MoveInSmart(tag, duration=0.5, maintain=False, behind=[], atlist = []):
        global lastmovein
        tag = tag.lower()
        if lastmovein == "Right":
            PutLoff(tag, behind, atlist)
            lastmovein = "Left"
        else:
            PutRoff(tag, behind, atlist)
            lastmovein = "Right"
        if maintain:
            lastmovein = "Left" if lastmovein == "Right" else "Right"
        LineUp(duration, atlist=atlist)

    def MoveOutSmart(tag, duration=0.5, layer="master", exclude=None, considerexcludes=False, atlist=[], maintain=False):
        SmartMoveOut(tag, duration, layer, exclude, considerexcludes, atlist, maintain)

    def SmartMoveOut(tag, duration=0.5, layer="master", exclude=None, considerexcludes=False, atlist=[], maintain=False):
        # if maintain is true, it ignores left/right facingness, and will just leave the same direction as the last character to leave

        global lastmoveout
        # Normalize input to a list of tags
        if isinstance(tag, (list, tuple, set)):
            tags = list(tag)
        else:
            tags = [tag]

        entries = []
        for t in tags:
            t = t.lower()
            x = _visual_x(t, layer)

            # Build the current name (tag + attrs) to preserve attributes.
            try:
                attrs = renpy.get_attributes(t, layer=layer)
                if (attrs == None):
                    attrs = []
            except Exception:
                attrs = []
            name = tuple([t] + list(attrs))

            # Base facing from your persondex, using the image->char map.
            try:
                base_dir = persondex[imageToCharDict[name[0]]]["Direction"]
            except Exception:
                base_dir = "Right"

            # Decide which side we're leaving from and where to exit.
            
            if (maintain):
                leaving_left = lastmoveout == "Left" 
            else:
                leaving_left = x < 0.5

            lastmoveout = "Left" if leaving_left else "Right"
            target = -0.2 if leaving_left else 1.2
            facing_left = base_dir == "Left"

            entries.append(dict(
                tag=t, name=name, x=x, target=target, orientation=facing_left, outward=leaving_left
            ))

        for e in entries:
            renpy.show(
                e["name"], layer=layer, tag=e["tag"],
                zorder=abs(e["x"] - 0.5) * 10,
                at_list=atlist + [flip_then_exit(e["x"], e["target"], duration, duration, e["orientation"], e["outward"])]
            )

        renpy.pause(duration * 2)  # total time (turn + move)
        for e in entries:
            renpy.hide(e["tag"])

        # Re-line up whatever remains on-screen
        LineUp(exclude=exclude, considerexcludes=considerexcludes, atlist=atlist)

    def ShiftAlign(tag, pos, atlist=[]):
        """
        Combines functionality of SmartShift and LineUp, allowing a character to move into a position, and then realign everyone around them.
        """
        SmartShift(tag, pos, atlist=atlist)
        LineUp(exclude=tag, prefilled=pos, considerexcludes=False, atlist=atlist)

# ATL transform used by LineUp()
transform slide_to(start_xpos=0.5, _xpos=0.5, _dur=0.5, orientation="Right"):
    # if you're moving from offscreen onto the screen, 
    ease _dur xpos _xpos zoom 1.0 ypos 1.0 xzoom (-1 if (((_xpos if _xpos != 0.5 else start_xpos) < 0.5 and orientation == "Left") or ((_xpos if _xpos != 0.5 else start_xpos) > 0.5 and orientation == "Right")) else 1)

transform flip_then_exit(_xpos, target_x, turn_dur=0.5, move_dur=0.5, orientation_left=True, face_left=True):
    xpos _xpos
    # Phase 1: flip/face change
    # Use xzoom as a "turn in place" stand-in; replace with rotate/matrixtransform if you prefer a true spin.
    ease turn_dur xzoom (-1 if (orientation_left != face_left) else 1)
    # Phase 2: move out
    ease move_dur xpos target_x