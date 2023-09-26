import sys
import numpy
from PIL import Image

CIRCLE_TYPE = "circle"
RECT_TYPE = "rectangle"
POLY_TYPE = "polygon"
TEXT_TYPE = "text"
IMAGE_TYPE = "image"
CUSTOM_TYPE = "custom"

VALID_TYPES = [CIRCLE_TYPE, RECT_TYPE, POLY_TYPE, TEXT_TYPE, IMAGE_TYPE, CUSTOM_TYPE]

DEFAULT_COLOUR = (1.0, 1.0, 1.0)
DEFAULT_DIMENSIONS = (0.2, 0.1)
DEFAULT_RADIUS = 0.2
DEFAULT_POLYGON_POINTS = 3


class Object:
    name = ""
    objectType = ""
    dimensions = DEFAULT_DIMENSIONS
    radius = DEFAULT_RADIUS
    points = DEFAULT_POLYGON_POINTS
    scale = 1.0
    location = (0.0, 0.0)
    rotation = 0.0
    text = ""
    font_family = "Helvetica"
    font_size = 20
    image = "default.png"
    colour = DEFAULT_COLOUR
    is_gradient_colour = False
    gradient = (-1.0, 0.0)
    gradient_colours = (DEFAULT_COLOUR, DEFAULT_COLOUR)
    gradient_points = ((-1.0, 0.0), (1.0, 0.0))
    start_scale = 1.0
    start_location = (0.0, 0.0)
    start_rotation = 0.0
    start_colour = DEFAULT_COLOUR
    custom_draw = None

    def __init__(
        self,
        name: str,
        objectType: str,
        dimensions: tuple = DEFAULT_DIMENSIONS,
        radius: float = DEFAULT_RADIUS,
        points: float = DEFAULT_POLYGON_POINTS,
        scale: float = 1.0,
        location: float = (0.0, 0.0),
        rotation: float = 0.0,
        text: str = "default text",
        font_family: str = "Helvetica",
        font_size: int = 20,
        image: str = "default.png",
        colour: tuple = DEFAULT_COLOUR,
        custom_draw: callable = None,
    ) -> None:
        self.name = name
        if not valid_type(objectType):
            sys.exit(f"object '{name}' type invalid: valid types are {VALID_TYPES}")
        self.objectType = objectType
        if len(dimensions) > 2 or len(dimensions) == 0:
            sys.exit(f"object '{name}' needs dimensions of (x, y)")
        self.dimensions = dimensions
        self.radius = radius
        self.points = points
        self.scale = scale
        if len(location) > 2 or len(location) == 0:
            sys.exit(f"object '{name}' location should be a tuple of (x, y)")
        self.location = location
        self.rotation = rotation
        self.text = text
        self.font_family = font_family
        self.font_size = font_size
        self.image = image
        if self.objectType == IMAGE_TYPE:
            self.image_array = self.get_image_array()
        if len(colour) > 3 or len(colour) == 0:
            sys.exit(f"object '{name}' colour should be a tuple of (r,g,b)")
        self.colour = colour
        if custom_draw == None and objectType == CUSTOM_TYPE:
            sys.exit(f"object '{name}' custom_draw function required for custom type")
        self.custom_draw = custom_draw

    def get_image_array(self) -> numpy.ndarray:
        image = Image.open(self.image)
        return numpy.asarray(image)


def valid_type(t: str) -> bool:
    return t in VALID_TYPES
