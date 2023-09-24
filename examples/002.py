from graphics_maker import GraphicsMaker
from object import Object, RECT_TYPE, POLY_TYPE
from animation_data import AnimationData, LINEAR_COLOUR_GRADIENT_AFFECT, LOCATION_AFFECT, SCALE_AFFECT, BASIC_COLOUR_AFFECT, REMOVE_OBJECT
from utils import *

POLYGON_SIDES = 6
RADIUS = 0.1
LOCATIONS = [
    (0.5, 0.3), (0.6, 0.4), (0.4, 0.4), (0.6, 0.6), (0.4, 0.6), (0.5, 0.5), (0.5, 0.7), # Purple
    (0.6, 0.2), (0.7, 0.3), (0.7, 0.5) # White
]
MID_INDEX = 5
NEW_MID_INDEX = 1
END_MID_INDEX = 8
HIDE_HEXES = [2, 4, 6]
SHOW_HEXES = [7,8,9]
NORMAL_COLOUR = (0.87, 0.63, 0.87)
HOVER_COLOUR = (0.73, 0.33, 0.83)

def __main__():
    maker = GraphicsMaker("hexes", 1920, 1080)
    maker.add_object(Object(
        "bg",
        RECT_TYPE,
        dimensions=(1.0, 1.0),
        location=(0.5, 0.5),
        colour=(1.0, 1.0, 1.0)
    ))

    for i, l in enumerate(LOCATIONS):
        name = f"hex_{i}"
        time_offset = i * 0.1
        colour = NORMAL_COLOUR
        if i > 6:
            colour = (1.0, 1.0, 1.0)
        maker.add_object(Object(
            name,
            POLY_TYPE,
            radius=RADIUS,
            points=POLYGON_SIDES,
            location=l,
            scale=0.0,
            colour=colour,
        ))
        maker.add_to_timeline(AnimationData(
            name,
            EASE_OUT_SINE,
            time_offset,
            time_offset + 0.5,
            SCALE_AFFECT,
            scale=1.0,
        ))
    
    maker.add_to_timeline(AnimationData(
        f"hex_{MID_INDEX}",
        EASE_IN_OUT_SINE,
        1.5, 2.0,
        SCALE_AFFECT,
        scale=1.1,
    ))
    maker.add_to_timeline(AnimationData(
        f"hex_{MID_INDEX}",
        EASE_IN_OUT_SINE,
        1.5, 2.0,
        BASIC_COLOUR_AFFECT,
        colour=HOVER_COLOUR,
    ))
    
    maker.add_to_timeline(AnimationData(
        f"hex_{MID_INDEX}",
        EASE_IN_OUT_SINE,
        2.5, 3.0,
        SCALE_AFFECT,
        scale=1.0,
    ))
    maker.add_to_timeline(AnimationData(
        f"hex_{MID_INDEX}",
        EASE_IN_OUT_SINE,
        2.5, 3.0,
        BASIC_COLOUR_AFFECT,
        colour=NORMAL_COLOUR,
    ))
    
    maker.add_to_timeline(AnimationData(
        f"hex_{NEW_MID_INDEX}",
        EASE_IN_OUT_SINE,
        2.75, 3.25,
        SCALE_AFFECT,
        scale=1.1,
    ))
    maker.add_to_timeline(AnimationData(
        f"hex_{NEW_MID_INDEX}",
        EASE_IN_OUT_SINE,
        2.75, 3.25,
        BASIC_COLOUR_AFFECT,
        colour=HOVER_COLOUR,
    ))

    for i, l in enumerate(LOCATIONS):
        maker.add_to_timeline(AnimationData(
            f"hex_{i}",
            EASE_IN_OUT_CUBIC,
            3.5, 4.0,
            LOCATION_AFFECT,
            location=(l[0] - 0.1, l[1] + 0.1)
        ))
        if i in HIDE_HEXES:
            maker.add_to_timeline(AnimationData(
                f"hex_{i}",
                EASE_IN_OUT_CUBIC,
                3.5, 4.0,
                BASIC_COLOUR_AFFECT,
                colour=(1.0, 1.0, 1.0)
            ))
        if i in SHOW_HEXES:
            maker.add_to_timeline(AnimationData(
                f"hex_{i}",
                EASE_IN_OUT_CUBIC,
                3.5, 4.0,
                BASIC_COLOUR_AFFECT,
                colour=NORMAL_COLOUR
            ))
    
    
    maker.add_to_timeline(AnimationData(
        f"hex_{NEW_MID_INDEX}",
        EASE_IN_OUT_SINE,
        4.25, 4.375,
        SCALE_AFFECT,
        scale=0.9,
    ))
    for i, l in enumerate(LOCATIONS):
        if i == NEW_MID_INDEX:
            continue

        maker.add_to_timeline(AnimationData(
            f"hex_{i}",
            LERP,
            4.25, 4.375,
            BASIC_COLOUR_AFFECT,
            colour=(1.0, 1.0, 1.0),
        ))
        maker.add_to_timeline(AnimationData(
            f"hex_{i}",
            LERP,
            4.375, 4.5,
            REMOVE_OBJECT,
        ))
    
    maker.add_to_timeline(AnimationData(
        f"hex_{NEW_MID_INDEX}",
        EASE_IN_OUT_SINE,
        4.375, 6,
        SCALE_AFFECT,
        scale=20.0,
    ))
    
    maker.add_to_timeline(AnimationData(
        f"hex_{NEW_MID_INDEX}",
        EASE_IN_OUT_SINE,
        6.5, 7.0,
        LINEAR_COLOUR_GRADIENT_AFFECT,
        gradient_colours=(HOVER_COLOUR, (0.0, 1.0, 0.2)),
        gradient_start=(0.0, 0.0),
        gradient_end=(1.0, 1.0),
    ))

    maker.generate_animation()

if __name__ == "__main__":
    __main__()
