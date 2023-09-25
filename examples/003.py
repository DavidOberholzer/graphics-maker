import gizeh
import math

from graphics_maker import (
    GraphicsMaker,
    Object,
    CUSTOM_TYPE,
    AnimationData,
    ROTATION_AFFECT,
    EASE_IN_OUT_ELASTIC,
)

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080


def cursor_draw(o: Object, s: gizeh.Surface):
    x, y = o.location
    colour = o.colour
    r = o.radius * SCREEN_HEIGHT * o.scale
    poly = gizeh.regular_polygon(
        r,
        3,
        fill=colour,
    )
    poly = poly.rotate(-math.pi / 4)
    handle_xy = [(-0.025) * SCREEN_WIDTH, (0.05) * SCREEN_HEIGHT]
    w, h = (0.05 * SCREEN_WIDTH, 0.05 * SCREEN_HEIGHT)
    handle = gizeh.rectangle(w, h, xy=handle_xy, fill=colour)
    handle = handle.rotate(-math.pi / 4, handle_xy)

    xy = [x * SCREEN_WIDTH, y * SCREEN_HEIGHT]
    group = gizeh.Group([poly, handle])
    group = group.translate(xy)
    group = group.rotate(o.rotation, xy)
    group.draw(s)


def main():
    maker = GraphicsMaker("custom_types", SCREEN_WIDTH, SCREEN_HEIGHT, fps=60)
    maker.add_object(
        Object(
            "cursor",
            CUSTOM_TYPE,
            radius=0.1,
            location=(0.5, 0.5),
            custom_draw=cursor_draw,
        )
    )
    maker.add_to_timeline(
        AnimationData(
            "cursor",
            EASE_IN_OUT_ELASTIC,
            1.0,
            3.0,
            ROTATION_AFFECT,
            rotation=2 * math.pi,
        )
    )
    maker.generate_animation()


if __name__ == "__main__":
    main()
