import sys

REMOVE_OBJECT = "remove"
LOCATION_AFFECT = "location"
SCALE_AFFECT = "scale"
ROTATION_AFFECT = "rotation"
BASIC_COLOUR_AFFECT = "basic_colour"
LINEAR_COLOUR_GRADIENT_AFFECT = "linear_gradient_colour"
RADIAL_COLOUR_GRADIENT_AFFECT = "radial_gradient_colour"

DEFAULT_COLOUR_CHANGE = (1.0, 1.0, 1.0)


VALID_AFFECTS = [
    REMOVE_OBJECT,
    LOCATION_AFFECT,
    SCALE_AFFECT,
    ROTATION_AFFECT,
    BASIC_COLOUR_AFFECT,
    LINEAR_COLOUR_GRADIENT_AFFECT,
    RADIAL_COLOUR_GRADIENT_AFFECT,
]


class AnimationData:
    object_name = ""
    curve = ""
    start_time = 0.0
    end_time = 0.0
    affects = ""
    location = (0.0, 0.0)
    scale = 1.0
    rotation = 0.0
    colour = DEFAULT_COLOUR_CHANGE
    gradient_colours = ((0.0, 0.0, 0.0), (0.0, 0.0, 0.0))
    gradient_start = (-1.0, 0.0)
    gradient_end = (1.0, 0.0)
    started = False

    def __init__(
        self,
        object_name: str,
        curve: str,
        start_time: float,
        end_time: float,
        affects: str,
        location: tuple = (0.0, 0.0),
        scale: float = 1.0,
        rotation: float = 0.0,
        colour: tuple = DEFAULT_COLOUR_CHANGE,
        gradient_colours=((0.0, 0.0, 0.0), (0.0, 0.0, 0.0)),
        gradient_start=(-1.0, 0.0),
        gradient_end=(1.0, 0.0),
    ) -> None:
        self.object_name = object_name
        self.curve = curve
        self.start_time = start_time
        self.end_time = end_time
        if not valid_affect(affects):
            sys.exit(
                f"animation affecting '{object_name}' should affect one of the following: {VALID_AFFECTS}"
            )
        self.affects = affects
        if len(location) == 0 or len(location) > 2:
            sys.exit(
                f"animation affecting '{object_name}' location should be a tuple of (x, y)"
            )
        self.location = location
        self.scale = scale
        self.rotation = rotation
        self.colour = colour
        self.gradient_colours = gradient_colours
        self.gradient_start = gradient_start
        self.gradient_end = gradient_end
        self.started = False


def valid_affect(affects: str) -> bool:
    return affects in VALID_AFFECTS
