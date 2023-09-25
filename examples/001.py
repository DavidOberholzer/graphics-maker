import math

from graphics_maker import (
    GraphicsMaker,
    Object,
    RECT_TYPE,
    POLY_TYPE,
    AnimationData,
    LOCATION_AFFECT,
    ROTATION_AFFECT,
    LERP,
    EASE_OUT_ELASTIC,
)

AMOUNT = 10


def __main__():
    width = 1.2
    height = 1.0 / AMOUNT
    start_x = -0.6
    start_y = height / 2.0
    start_time_offset = 0.05
    colour_offset = -0.1
    maker = GraphicsMaker("blinds", 1920, 1080)
    for i in range(AMOUNT):
        y = start_y + height * i
        time_offset = start_time_offset * i
        name = f"rect_{i}"
        co = colour_offset * i
        maker.add_object(
            Object(
                name,
                RECT_TYPE,
                dimensions=(width, height),
                location=(start_x, y),
                colour=(1 + co, 1, 1),
            )
        )
        maker.add_to_timeline(
            AnimationData(
                name,
                LERP,
                0 + time_offset,
                1 + time_offset,
                LOCATION_AFFECT,
                location=(0.6, y),
            )
        )

    c_rect_name = "center_rect"
    maker.add_object(
        Object(
            c_rect_name,
            POLY_TYPE,
            location=(-0.2, 0.5),
            colour=(0.3, 0.4, 0.7),
        )
    )
    end_blinds_time = start_time_offset * (AMOUNT - 1)
    maker.add_to_timeline(
        AnimationData(
            c_rect_name,
            EASE_OUT_ELASTIC,
            end_blinds_time + 1.0,
            end_blinds_time + 2.0,
            LOCATION_AFFECT,
            location=(0.5, 0.5),
        )
    )
    maker.add_to_timeline(
        AnimationData(
            c_rect_name,
            EASE_OUT_ELASTIC,
            end_blinds_time + 2.2,
            end_blinds_time + 4.0,
            ROTATION_AFFECT,
            rotation=math.pi / 2,
        )
    )
    maker.generate_animation()


if __name__ == "__main__":
    __main__()
