# Graphics Maker (Python)

# What

This is a simple python package that provides a way to generate flat design animation videos.
It allows for simple shapes and transitions of location, rotation and scale.

# Why

I was tired of building animations with other tools and getting choppy/unsatisfactory results. I'm also too cheap and lazy to pay for an expensive tool, and then have to learn all the intricacies. So I just made this for myself.

# Dependencies:

In order to use this package you need to have some libraries installed for libcairo2. Google what you need to install for your distro. Also for images we need PIL.

# How to use:

Install the package in your python environment:

`pip install graphics-maker`

The following steps should be taken to create an animation:

*NOTE: ALL LOCATION/DIMENSION BASED VALUES SHOULD BE GIVEN AS PERCENTAGES OF THE VIDEO DIMENSIONS.*

1. Instantiate an instance of `GraphicsMaker` with the desired settings.

| Argument    | Description                                                |
|-------------|------------------------------------------------------------|
| name        | File name                                                  |
| w           | Video width                                                |
| h           | Video height                                               |
| fps         | FPS `default:60`                                           |
| output_dir  | The directory to output the result to `default:./outputs/` |
| output_type | The video type output (mp4/gif) `default:mp4`              |

2. Create and add Objects to the GraphicsMaker with the desired type, location, rotation, scale and colour.
3. Add AnimationData instances to the GraphicsMaker for objects you'd like to animate within a given timeframe.
4. Run `.generate_animation()` on the GraphicsMaker instance.

# Supported object types

1. Circle
2. Rectangle
3. Polygon
4. Text
5. Image
6. Custom Draw (provide your own draw function)

# TODO:

- More documentation on capabilities.
- Radial gradient transition.
- Fix linear gradient transition of odd angle.

# Examples

Example programs using the lib are in `examples/`. Feel free to run it locally and generate the videos! But here they are as well:

https://github.com/DavidOberholzer/graphics-maker/assets/20847795/72428e27-dd3d-4585-83f6-23776edaae99

https://github.com/DavidOberholzer/graphics-maker/assets/20847795/55603c97-59d8-485c-966c-0ccf743d93c4

https://github.com/DavidOberholzer/graphics-maker/assets/20847795/04dc3927-9b7d-4abd-b37a-3f5f945617f3
