import PIL
import gizeh
import uuid
from moviepy.editor import VideoClip

from .animation_data import *
from .object import (
    Object,
    CIRCLE_TYPE,
    RECT_TYPE,
    POLY_TYPE,
    TEXT_TYPE,
    IMAGE_TYPE,
    CUSTOM_TYPE,
)
from .utils import *


MP4_TYPE = "mp4"
GIF_TYPE = "gif"

VALID_OUTPUT_TYPES = [MP4_TYPE, GIF_TYPE]


class GraphicsMaker:
    animation_name = ""
    screen_width = 0
    screen_height = 0
    fps = 60
    output_dir = "./outputs/"
    output_type = ""
    objects = {}
    timeline = {}

    def __init__(
        self,
        name: str,
        w: int,
        h: int,
        fps: int = 60,
        output_dir: str = "./outputs/",
        output_type: str = MP4_TYPE,
    ) -> None:
        self.animation_name = name
        self.screen_width = w
        self.screen_height = h
        self.fps = fps
        self.output_dir = output_dir
        if not valid_output_type(output_type):
            sys.exit(f"invalid output type must be: {VALID_OUTPUT_TYPES}")
        self.output_type = output_type

    def add_object(self, object: Object) -> None:
        if object.name in self.objects:
            print(f"already existing object ignored... {object.name}")
            return

        self.objects[object.name] = object

    def add_to_timeline(self, data: AnimationData) -> None:
        if data.object_name not in self.objects:
            print(
                f"animation data for non existent object ignored... {data.object_name}"
            )
            return

        id = uuid.uuid4()
        self.timeline[id] = data

    def _remove_object(self, id: uuid.UUID) -> None:
        a = self.timeline[id]
        name = a.object_name
        del self.objects[name]
        animations_to_remove = []
        for in_id in self.timeline:
            if self.timeline[in_id].object_name != name:
                continue
            animations_to_remove.append(in_id)

        for in_id in animations_to_remove:
            del self.timeline[in_id]

    def _transform_object(self, t: float, id: uuid.UUID) -> None:
        a = self.timeline[id]
        if a.affects == ROTATION_AFFECT:
            self._rotate_object(t, id)
        elif a.affects == SCALE_AFFECT:
            self._scale_object(t, id)
        elif a.affects == LOCATION_AFFECT:
            self._translate_object(t, id)
        elif a.affects == BASIC_COLOUR_AFFECT:
            self._change_colour(t, id)
        elif a.affects == LINEAR_COLOUR_GRADIENT_AFFECT:
            self._change_colour_gradient_linear(t, id)
        elif a.affects == RADIAL_COLOUR_GRADIENT_AFFECT:
            self._change_colour_gradient_radial(t, id)

    def _scale_object(self, current_time: float, id: uuid.UUID) -> None:
        a = self.timeline[id]
        o = self.objects[a.object_name]

        if not a.started:
            a.started = True
            o.start_scale = o.scale

        time_lapsed = get_time_alpha(a.start_time, a.end_time, current_time)

        v0 = o.start_scale
        v1 = a.scale

        o.scale = interpolate_value(a.curve, v0, v1, time_lapsed)

    def _rotate_object(self, current_time: float, id: uuid.UUID) -> None:
        a = self.timeline[id]
        o = self.objects[a.object_name]

        if not a.started:
            a.started = True
            o.start_rotation = o.rotation

        time_lapsed = get_time_alpha(a.start_time, a.end_time, current_time)

        v0 = o.start_rotation
        v1 = a.rotation
        o.rotation = interpolate_value(a.curve, v0, v1, time_lapsed)

    def _translate_object(self, current_time: float, id: uuid.UUID) -> None:
        a = self.timeline[id]
        o = self.objects[a.object_name]

        if not a.started:
            a.started = True
            o.start_location = o.location

        time_lapsed = get_time_alpha(a.start_time, a.end_time, current_time)

        vx0, vy0 = o.start_location
        vx1, vy1 = a.location
        o.location = (
            interpolate_value(a.curve, vx0, vx1, time_lapsed),
            interpolate_value(a.curve, vy0, vy1, time_lapsed),
        )

    def _change_colour(self, current_time: float, id: uuid.UUID) -> None:
        a = self.timeline[id]
        o = self.objects[a.object_name]

        if not a.started:
            a.started = True
            o.start_colour = o.colour

        time_lapsed = get_time_alpha(a.start_time, a.end_time, current_time)

        r0, g0, b0 = o.start_colour
        r1, g1, b1 = a.colour
        o.colour = (
            interpolate_value(a.curve, r0, r1, time_lapsed),
            interpolate_value(a.curve, g0, g1, time_lapsed),
            interpolate_value(a.curve, b0, b1, time_lapsed),
        )

    def _change_colour_gradient_linear(
        self, current_time: float, id: uuid.UUID
    ) -> None:
        a = self.timeline[id]
        o = self.objects[a.object_name]

        if not a.started:
            a.started = True
            o.is_gradient_colour = True
            o.gradient_colours = a.gradient_colours
            o.gradient_points = (a.gradient_start, a.gradient_end)

        time_lapsed = get_time_alpha(a.start_time, a.end_time, current_time)

        o.gradient = (
            interpolate_value(a.curve, -1.0, 1.0, time_lapsed),
            interpolate_value(a.curve, 0.0, 2.0, time_lapsed),
        )

    def _change_colour_gradient_radial(
        self, current_time: float, id: uuid.UUID
    ) -> None:
        pass

    def _get_gradient_colour(self, o: Object) -> None:
        x, y = o.gradient
        colour0, colour1 = o.gradient_colours
        p1, p2 = o.gradient_points
        x1, y1 = (p1[0] * self.screen_width, p1[1] * self.screen_height)
        x2, y2 = (p2[0] * self.screen_width, p2[1] * self.screen_height)
        return gizeh.ColorGradient(
            "linear", ((x, colour1), (y, colour0)), xy1=[x1, y1], xy2=[x2, y2]
        )

    def _make_cirle(self, o: Object, surface: gizeh.Surface) -> None:
        x, y = o.location
        xy = [x * self.screen_width, y * self.screen_height]
        colour = o.colour
        if o.is_gradient_colour:
            colour = self._get_gradient_colour(o)
        r = o.radius * self.screen_height * o.scale
        gizeh.circle(r, fill=colour).translate(xy).scale(o.scale, center=xy).rotate(
            o.rotation, xy
        ).draw(surface)

    def _make_rectangle(self, o: Object, surface: gizeh.Surface) -> None:
        x, y = o.location
        xy = [x * self.screen_width, y * self.screen_height]
        colour = o.colour
        if o.is_gradient_colour:
            colour = self._get_gradient_colour(o)
        w, h = o.dimensions
        gizeh.rectangle(
            w * self.screen_width,
            h * self.screen_height,
            fill=colour,
        ).translate(xy).scale(o.scale, center=xy).rotate(o.rotation, xy).draw(surface)

    def _make_polygon(self, o: Object, surface: gizeh.Surface) -> None:
        x, y = o.location
        xy = [x * self.screen_width, y * self.screen_height]
        colour = o.colour
        if o.is_gradient_colour:
            colour = self._get_gradient_colour(o)
        r = o.radius * self.screen_height

        gizeh.regular_polygon(
            r,
            o.points,
            fill=colour,
        ).translate(xy).scale(
            o.scale, center=xy
        ).rotate(o.rotation, xy).draw(surface)

    def _make_text(self, o: Object, surface: gizeh.Surface) -> None:
        x, y = o.location
        xy = [x * self.screen_width, y * self.screen_height]
        colour = o.colour
        if o.is_gradient_colour:
            colour = self._get_gradient_colour(o)
        gizeh.text(
            o.text, fontfamily=o.font_family, fontsize=o.font_size, fill=colour
        ).translate(xy).scale(o.scale, center=xy).rotate(o.rotation, xy).draw(surface)

    def _make_image(self, o: Object, surface: gizeh.Surface) -> None:
        x, y = o.location
        xy = [x * self.screen_width, y * self.screen_height]
        w, h = o.dimensions
        w = w * self.screen_width
        h = h * self.screen_height
        image = gizeh.ImagePattern(o.image_array, pixel_zero=(w / 2, h / 2))
        gizeh.rectangle(
            w,
            h,
            fill=image,
        ).translate(xy).scale(
            o.scale, center=xy
        ).rotate(o.rotation, xy).draw(surface)

    def _make_custom(self, o: Object, surface: gizeh.Surface) -> None:
        o.custom_draw(o, surface)

    def _make_frame_func(self) -> callable:
        def make_frame(t):
            surface = gizeh.Surface(width=self.screen_width, height=self.screen_height)
            remove_animations = []
            for id in self.timeline:
                a = self.timeline[id]
                if t >= a.start_time and t <= a.end_time:
                    self._transform_object(t, id)
                    if a.affects == REMOVE_OBJECT:
                        remove_animations.append(id)

            for a in remove_animations:
                self._remove_object(a)

            for name in self.objects:
                o = self.objects[name]
                if o.objectType == CIRCLE_TYPE:
                    self._make_cirle(o, surface)
                if o.objectType == RECT_TYPE:
                    self._make_rectangle(o, surface)
                if o.objectType == POLY_TYPE:
                    self._make_polygon(o, surface)
                if o.objectType == TEXT_TYPE:
                    self._make_text(o, surface)
                if o.objectType == IMAGE_TYPE:
                    self._make_image(o, surface)
                if o.objectType == CUSTOM_TYPE:
                    self._make_custom(o, surface)
            return surface.get_npimage()

        return make_frame

    def generate_animation(self) -> None:
        duration = 0
        for id in self.timeline:
            a = self.timeline[id]
            if a.end_time > duration:
                duration = a.end_time

        clip = VideoClip(self._make_frame_func(), duration=duration + 1)
        if self.output_type == MP4_TYPE:
            clip.write_videofile(
                f"{self.output_dir}{self.animation_name}.{self.output_type}",
                fps=self.fps,
            )
        if self.output_type == GIF_TYPE:
            clip.write_gif(
                f"{self.output_dir}{self.animation_name}.{self.output_type}",
                fps=self.fps,
            )


def valid_output_type(output_type: str):
    return output_type in VALID_OUTPUT_TYPES
