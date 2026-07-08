# eternityshader.rpy
#
# Usage:
#
#     show eternity at chroma_glitch()
#
# Strong:
#
#     show eternity at chroma_glitch(strength=0.85, aberration=3.5, jitter=2.0)
#
# Very visible test:
#
#     show eternity at chroma_glitch(strength=1.5, aberration=8.0, jitter=5.0, scanline=0.2, flicker=0.3)


init python:

    renpy.register_shader(
        "game.chromaglitch",

        variables = """
            uniform sampler2D tex0;

            uniform float u_time;
            uniform float u_strength;
            uniform float u_aberration;
            uniform float u_jitter;
            uniform float u_scanline;
            uniform float u_flicker;

            varying vec2 v_tex_coord;
        """,

        fragment_functions = """

            float glitch_rand(vec2 co) {
                return fract(sin(dot(co.xy, vec2(12.9898, 78.233))) * 43758.5453);
            }

            float glitch_band_noise(float y, float t) {
                float band = floor(y * 42.0);
                return glitch_rand(vec2(band, floor(t * 18.0)));
            }

        """,

        fragment_300 = """

            vec2 uv = v_tex_coord;
            float t = u_time;
            float strength = max(u_strength, 0.0);

            // IMPORTANT:
            // gl_FragColor already contains the normal Ren'Py sprite color
            // because renpy.texture has already run.
            vec4 original = gl_FragColor;

            // Never affect fully transparent pixels.
            if (original.a <= 0.0) {
                gl_FragColor = original;
            } else {

                // Texture coordinates are 0.0 to 1.0, so these must be tiny.
                float aberration = u_aberration * 0.0015 * strength;
                float jitter = u_jitter * 0.0010 * strength;

                float band = glitch_band_noise(uv.y, t);
                float band_mask = step(0.84, band);
                float hard_band = step(0.965, band);

                float wave = sin((uv.y * 90.0) + (t * 16.0));

                float shove = 0.0;
                shove += ((band - 0.5) * jitter * 12.0 * band_mask);
                shove += wave * jitter * 0.45;
                shove += ((band - 0.5) * jitter * 24.0 * hard_band);

                vec2 red_uv = uv + vec2(aberration + shove, 0.0);
                vec2 blue_uv = uv - vec2(aberration - shove, 0.0);

                vec4 red_sample = texture2D(tex0, red_uv);
                vec4 blue_sample = texture2D(tex0, blue_uv);

                vec4 color = original;

                // Only borrow color channels where the offset sample actually has sprite.
                color.r = mix(original.r, red_sample.r, red_sample.a);
                color.b = mix(original.b, blue_sample.b, blue_sample.a);

                // Small blue/cyan digital flicker.
                float flick = glitch_rand(vec2(floor(t * 24.0), 17.0));
                color.rgb *= 1.0 + ((flick - 0.5) * u_flicker * strength);

                // Subtle scanline shimmer.
                float lines = sin((uv.y * 900.0) + t * 20.0);
                float scan = 1.0 - ((0.5 + 0.5 * lines) * u_scanline * strength);
                color.rgb *= scan;

                // Rare corrupt flecks.
                float fleck = glitch_rand(vec2(floor(uv.x * 80.0), floor(uv.y * 80.0) + floor(t * 20.0)));
                float fleck_mask = step(0.993, fleck) * original.a * strength;
                color.rgb = mix(color.rgb, vec3(0.75, 0.95, 1.0), fleck_mask * 0.45);

                // Critical: preserve Ren'Py's original alpha.
                color.a = original.a;

                gl_FragColor = color;
            }

        """
    )


transform chroma_glitch(
    strength=0.45,
    aberration=2.0,
    jitter=1.0,
    scanline=0.08,
    flicker=0.10
):
    mesh True

    # A little room for chromatic offset so the sides do not get clipped.
    mesh_pad (24, 0, 24, 0)

    shader "game.chromaglitch"

    u_strength strength
    u_aberration aberration
    u_jitter jitter
    u_scanline scanline
    u_flicker flicker

    # Keeps u_time-based shader animation updating even when nothing else moves.
    pause 0
    repeat