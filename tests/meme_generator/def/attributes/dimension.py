from dataclasses import dataclass
from functools import cached_property

from tests.meme_generator.gen.classes import Def
from tests.meme_generator.gen.nodes import Image, Video, Frame, Stack, Scale, Position, SingleTargetModification
from tests.meme_generator.util.resource_util import get_video_file_specs, get_image_file_specs


@dataclass(frozen=True)
class Size:
    width: int
    height: int

# by default all frames have a size of (0, 0)
@Def.Frame
def size(node: Frame):
    return Size(0, 0)

# image and video frames as leave frames have the size of their resource files
@Def.Image
def size(node: Image):
    specs = get_image_file_specs(node.path)
    return Size(specs.width, specs.height)

@Def.Video
def size(node: Video):
    specs = get_video_file_specs(node.path)
    return Size(specs.width, specs.height)

# single target modifications have the size of their target frame, except for the "scale" modifier
@Def.SingleTargetModification
def size(node: SingleTargetModification):
    return node.target.dimension_size()

@Def.Scale
def size(node: Scale):
    # Scale node overrides the width and height
    return Size(int(node.width), int(node.height))

# multi target modifications have complex size handling

# stack node uses the width and height of the background (first target)
@Def.Stack
def size(node: Stack):
    targets = node.targets
    if not targets:
        return Size(0, 0)
    return targets[0].dimension_size()

