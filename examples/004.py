from graphics_maker import (
    GraphicsMaker,
    Object,
    TEXT_TYPE,
    IMAGE_TYPE,
    AnimationData,
    SCALE_AFFECT,
    EASE_IN_OUT_ELASTIC,
)

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080


def main():
    maker = GraphicsMaker("text&image", SCREEN_WIDTH, SCREEN_HEIGHT)

    maker.add_object(
        Object("text", TEXT_TYPE, text="what is this", font_size=40, location=(0.5, 0.3), scale=0.01)
    )
    maker.add_object(
        Object(
            "image",
            IMAGE_TYPE,
            dimensions=(0.067, 0.119),
            image="godot.png",
            location=(0.5, 0.6),
            scale=0.01,
        )
    )

    maker.add_to_timeline(
        AnimationData("image", EASE_IN_OUT_ELASTIC, 0.2, 0.8, SCALE_AFFECT, scale=1.0)
    )

    maker.add_to_timeline(
        AnimationData("text", EASE_IN_OUT_ELASTIC, 0.4, 1.2, SCALE_AFFECT, scale=1.0)
    )

    maker.generate_animation()


if __name__ == "__main__":
    main()
