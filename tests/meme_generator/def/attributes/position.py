import math
from dataclasses import dataclass

from tests.meme_generator.gen.classes import Def
from tests.meme_generator.gen.nodes import Image, Video, Frame, Stack, Scale, Position, SingleTargetModification, Rotate
from tests.meme_generator.util.resource_util import get_video_file_specs, get_image_file_specs


@dataclass(frozen=True)
class Pos:
    x: int
    y: int

@Def.Frame
def location(node: Frame):
    return Pos(0, 0)

@Def.Position
def location(node: Position):
    target_location = node.target.position_location()
    return Pos(int(node.x + target_location.x), int(node.y  + target_location.y))

@Def.Rotate
def location(node: Rotate):
    target_size = node.target.dimension_size()
    original_width = target_size.width
    original_height = target_size.height

    theta = math.radians(node.angle)
    c = abs(math.cos(theta))
    s = abs(math.sin(theta))
    enclosing_width = original_width * c + original_height * s
    enclosing_height = original_width * s + original_height * c

    top, left = 0, 0
    mod_angle = node.angle % 360
    if 0 < mod_angle <= 90:
        left, top = s * original_height, 0
    elif 90 < mod_angle <= 180:
        left, top = enclosing_width, c * original_height
    elif 180 < mod_angle <= 270:
        left, top = (c * original_width), enclosing_height
    elif 270 < mod_angle <= 360:
        left, top = 0, s * original_width
    return Pos(-left, -top)