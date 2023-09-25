from graphics_maker import (
    GraphicsMaker,
    Object,
    CIRCLE_TYPE,
    RECT_TYPE,
    AnimationData,
    LOCATION_AFFECT,
    SCALE_AFFECT,
    LERP,
    EASE_IN_OUT_ELASTIC,
    EASE_OUT_ELASTIC,
)


def __main__():
    name1 = "circle1"
    name2 = "rect1"
    animation = GraphicsMaker("test", 1280, 720)
    animation.add_object(
        Object(
            name1,
            CIRCLE_TYPE,
            colour=(0.4, 0.2, 0.8),
        )
    )
    animation.add_object(
        Object(
            name2,
            RECT_TYPE,
            dimensions=(0.2, 0.1),
            location=(0.8, 0.6),
            colour=(0.8, 0.3, 0.5),
        )
    )
    animation.add_to_timeline(
        AnimationData(
            name1,
            EASE_IN_OUT_ELASTIC,
            0,
            2,
            LOCATION_AFFECT,
            location=(0.5, 0.5),
        )
    )
    animation.add_to_timeline(
        AnimationData(
            name2,
            EASE_OUT_ELASTIC,
            1,
            3,
            LOCATION_AFFECT,
            location=(0.3, 0.9),
        )
    )
    animation.add_to_timeline(
        AnimationData(
            name1,
            LERP,
            1,
            2.5,
            SCALE_AFFECT,
            scale=1.5,
        )
    )

    animation.generate_animation()


if __name__ == "__main__":
    __main__()
