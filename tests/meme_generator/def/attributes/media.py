import math
from typing import List

from tests.meme_generator.config import RESOURCE_FOLDER
from tests.meme_generator.gen.classes import Def
from tests.meme_generator.gen.nodes import Frame, SingleTargetModification, MultiTargetModification, Image, Video, \
    FrameRoot, ResourceInput, Stack, Duration, Scale, Position, Modification, Rotate, MoveTime


# by default all frames have a size of (0, 0)
@Def.FrameRoot
def generate_ffmpeg_command(node: FrameRoot):
    inputs = node.media_get_inputs()
    input_string = " ".join([f"-i {RESOURCE_FOLDER}{inp.path}" for inp in inputs])
    complex_filter = node.root_target.media_get_complex_filter()
    file_ending = ".mp4" if node.root_target.time_duration() > 1 else ".png"

    filter_slot = ""
    if complex_filter:
        filter_slot = f" -filter_complex \"{complex_filter}\""
        filter_slot += f" -map \"[{node.root_target.media_filter_key()}]\""

    return f"ffmpeg {input_string}{filter_slot} {RESOURCE_FOLDER}out/test{file_ending}"

# generate inputs of the whole frame root
@Def.FrameRoot
def get_inputs(node: FrameRoot) -> List[ResourceInput]:
    return node.root_target.media_get_inputs()

@Def.Frame
def get_inputs(node: Frame) -> List[ResourceInput]:
    raise NotImplementedError("get inputs not implemented for generic frame")

@Def.SingleTargetModification
def get_inputs(node: SingleTargetModification) -> List[ResourceInput]:
    return node.target.media_get_inputs()

@Def.MultiTargetModification
def get_inputs(node: MultiTargetModification) -> List[ResourceInput]:
    inputs = []
    for target in node.targets:
        inputs.extend(target.media_get_inputs())
    return inputs

@Def.Image
def get_inputs(node: Image) -> List[ResourceInput]:
    return [node]
@Def.Video
def get_inputs(node: Video) -> List[ResourceInput]:
    return [node]

# get resource index on leave nodes
@Def.FrameRoot.ResourceInput
def filter_key_by_resource_node(node: FrameRoot, resource_node: ResourceInput) -> str:
    present = node.media_get_inputs()
    return str(present.index(resource_node))
@Def.Frame
def filter_key(node: Frame) -> str:
    return node.get_path_identity()
@Def.ResourceInput
def filter_key(node: ResourceInput) -> str:
    return node.media_filter_key_by_resource_node(node)
# duration, position and moveTime forward the input key of their target
@Def.Duration
def filter_key(node: Duration) -> str:
    return node.target.media_filter_key()
@Def.Position
def filter_key(node: Position) -> str:
    return node.target.media_filter_key()
@Def.MoveTime
def filter_key(node: MoveTime) -> str:
    return node.target.media_filter_key()


@Def.Frame
def get_complex_filter(node: Frame) -> str:
    raise NotImplementedError("get complex filter not implemented for generic frame")


@Def.MultiTargetModification
def get_child_complex_filters(node: MultiTargetModification) -> str:
    out = ""
    for target in node.targets:
        filter = target.media_get_complex_filter()
        if filter:
            out += filter
    return out

@Def.SingleTargetModification
def get_child_complex_filters(node: SingleTargetModification) -> str:
    return node.target.media_get_complex_filter()

@Def.Scale
def get_complex_filter(node: Scale) -> str:
    out = node.media_get_child_complex_filters()

    target_filter_key = node.target.media_filter_key()
    own_filter_key = node.media_filter_key()

    return out + f"[{target_filter_key}]scale={int(node.width)}:{int(node.height)}[{own_filter_key}];"

@Def.Rotate
def get_complex_filter(node: Rotate) -> str:
    out = node.media_get_child_complex_filters()
    rotation_exp = f"{node.angle}*PI/180"
    size = node.target.dimension_size()
    original_width, original_height = size.width, size.height
    theta = math.radians(node.angle)
    c = abs(math.cos(theta))
    s = abs(math.sin(theta))
    enclosing_width = original_width * c + original_height * s
    enclosing_height = original_width * s + original_height * c
    return out + f"[{node.target.media_filter_key()}]rotate={rotation_exp}:ow='{int(enclosing_width)}':oh='{int(enclosing_height)}':c=none[{node.media_filter_key()}];"

@Def.Stack
def get_complex_filter(node: Stack) -> str:
    targets = node.targets

    out = node.media_get_child_complex_filters()

    filter_name = node.get_path_identity()

    final_filter_out_key = node.media_filter_key()

    # for the overlay filter to make sense there must be at least two target (one background and one overlay)
    # if there is only one, a dummy filter is used
    if len(targets) == 0:
        raise RuntimeError("Stack had not targets")
    if len(targets) == 1:
        return f"[{targets[0].media_filter_key()}]null[{final_filter_out_key}];"

    # initially set the background key to the first targets key
    background_input_key = targets[0].media_filter_key()
    iterated_targets = targets[1:]
    for i, target in enumerate(iterated_targets):
        # set the output key:
        # on last iteration: the final key of the current node
        # on any other iteration: a unique dummy key (using iteration count)
        if i == len(iterated_targets) - 1:
            output_key = final_filter_out_key
        else:
            output_key = f"{filter_name}_{i}"

        # set the overlay key: the currently iterated target
        overlay_input_key = target.media_filter_key()
        time_start = target.time_start()
        time_end = target.time_end() - 1 # -1 because between is inclusive
        location = target.position_location()

        # add everything to the filter graph
        out += f"[{background_input_key}][{overlay_input_key}]overlay={location.x}:{location.y}:enable='between(n, {time_start}, {time_end})'[{output_key}];"

        # change background key to output key for next iteration
        background_input_key = output_key
    return out


@Def.Image
def get_complex_filter(node: Image) -> str:
    return ""
@Def.Video
def get_complex_filter(node: Video) -> str:
    return ""
@Def.Duration
def get_complex_filter(node: Duration) -> str:
    return node.media_get_child_complex_filters()
@Def.Position
def get_complex_filter(node: Position) -> str:
    return node.media_get_child_complex_filters()
@Def.MoveTime
def get_complex_filter(node: MoveTime) -> str:
    return node.media_get_child_complex_filters()
