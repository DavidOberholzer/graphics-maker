import math

LERP = "linear"
EASE_IN_SINE = "ease_in_sine"
EASE_OUT_SINE = "ease_out_sine"
EASE_IN_OUT_SINE = "ease_in_out_sine"
EASE_IN_CUBIC = "ease_in_cubic"
EASE_OUT_CUBIC = "ease_out_cubic"
EASE_IN_OUT_CUBIC = "ease_in_out_cubic"
EASE_IN_ELASTIC = "ease_in_elastic"
EASE_OUT_ELASTIC = "ease_out_elastic"
EASE_IN_OUT_ELASTIC = "ease_in_out_elastic"

VALID_CURVES = [
    EASE_IN_SINE,
    EASE_OUT_SINE,
    EASE_IN_OUT_SINE,
    EASE_IN_CUBIC,
    EASE_OUT_CUBIC,
    EASE_IN_OUT_CUBIC,
    EASE_IN_ELASTIC,
    EASE_OUT_ELASTIC,
    EASE_IN_OUT_ELASTIC,
]

C4 = (2 * math.pi) / 3
C5 = (2 * math.pi) / 4.5

# Util mathematics functions for interpolation and other generic functions.


def get_time_alpha(s: float, e: float, c: float):
    return (c - s) / (e - s)


def valid_curve(curve: str) -> bool:
    return curve in VALID_CURVES


def interpolate_value(curve: str, v0: float, v1: float, t: float):
    if curve == LERP:
        return lerp(v0, v1, t)
    if curve == EASE_IN_SINE:
        return ease_in_sine(v0, v1, t)
    if curve == EASE_OUT_SINE:
        return ease_out_sine(v0, v1, t)
    if curve == EASE_IN_OUT_SINE:
        return ease_in_out_sine(v0, v1, t)
    if curve == EASE_IN_CUBIC:
        return ease_in_cubic(v0, v1, t)
    if curve == EASE_OUT_CUBIC:
        return ease_out_cubic(v0, v1, t)
    if curve == EASE_IN_OUT_CUBIC:
        return ease_in_out_cubic(v0, v1, t)
    if curve == EASE_IN_ELASTIC:
        return ease_in_elastic(v0, v1, t)
    if curve == EASE_OUT_ELASTIC:
        return ease_out_elastic(v0, v1, t)
    if curve == EASE_IN_OUT_ELASTIC:
        return ease_in_out_elastic(v0, v1, t)

    return lerp(v0, v1, t)


def lerp(v0: float, v1: float, t: float) -> float:
    return (1 - t) * v0 + t * v1


def ease_in_sine(v0: float, v1: float, t: float) -> float:
    change = v1 - v0
    perc = 1 - math.cos((t * math.pi) / 2)
    return v0 + (change * perc)


def ease_out_sine(v0: float, v1: float, t: float) -> float:
    change = v1 - v0
    perc = math.sin((t * math.pi) / 2)
    return v0 + (change * perc)


def ease_in_out_sine(v0: float, v1: float, t: float) -> float:
    change = v1 - v0
    perc = -(math.cos(math.pi * t) - 1) / 2
    return v0 + (change * perc)


def ease_in_cubic(v0: float, v1: float, t: float) -> float:
    change = v1 - v0
    perc = t * t * t
    return v0 + (change * perc)


def ease_out_cubic(v0: float, v1: float, t: float) -> float:
    change = v1 - v0
    perc = 1 - math.pow(1 - t, 3)
    return v0 + (change * perc)


def ease_in_out_cubic(v0: float, v1: float, t: float) -> float:
    change = v1 - v0
    perc = 1 - math.pow(-2 * t + 2, 3) / 2
    if t < 0.5:
        perc = 4 * t * t * t
    return v0 + (change * perc)


def ease_in_elastic(v0: float, v1: float, t: float) -> float:
    if t == 0:
        return v0
    if t == 1:
        return v1

    change = v1 - v0
    perc = -math.pow(2, 10 * t - 10) * math.sin((t * 10 - 10.75) * C4)
    return v0 + (change * perc)


def ease_out_elastic(v0: float, v1: float, t: float) -> float:
    if t == 0:
        return v0
    if t == 1:
        return v1

    change = v1 - v0
    perc = math.pow(2, -10 * t) * math.sin((t * 10 - 0.75) * C4) + 1
    return v0 + (change * perc)


def ease_in_out_elastic(v0: float, v1: float, t: float) -> float:
    if t == 0:
        return v0
    if t == 1:
        return v1

    change = v1 - v0
    perc = (math.pow(2, -20 * t + 10) * math.sin((20 * t - 11.125) * C5)) / 2 + 1
    if t < 0.5:
        perc = -(math.pow(2, 20 * t - 10) * math.sin((20 * t - 11.125) * C5)) / 2
    return v0 + (change * perc)


def validate_animation_data(data: dict) -> str:
    return ""
