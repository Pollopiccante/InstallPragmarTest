from tests.meme_generator.gen.classes import Def
from tests.meme_generator.gen.nodes import Image, Video, Frame, Duration, SingleTargetModification, Stack, MoveTime
from tests.meme_generator.util.resource_util import get_video_file_specs

# SECTION Duration

# by default all frames have a duration of 1
@Def.Frame
def duration(node: Frame) -> int:
    return 1

# videos as a leave frames have the duration of their resource file
@Def.Video
def duration(node: Video) -> int:
    return get_video_file_specs(node.path).frames

# single target modifications have the duration of their target frame, except for the "Duration" modifier
@Def.SingleTargetModification
def duration(node: SingleTargetModification):
    return node.target.time_duration()

@Def.Duration
def duration(node: Duration) -> int:
    return int(node.duration)

# multi target modifications have more complex duration handling

# stack node takes the duration of the background
@Def.Stack
def duration(node: Stack) -> int:
    targets = node.targets
    if not targets:
        return 0
    return targets[0].time_duration()

# SECTION start / end time
# by default all frames have a start time 0
@Def.Frame
def start(node: Frame) -> int:
    return 0
# the time end of a frame is determined by its starting time and its duration
@Def.Frame
def end(node: Frame) -> int:
    return node.time_start() + node.time_duration()

# single target modifications have the start time of their target frame, except for the "MoveTime" modifier
@Def.SingleTargetModification
def start(node: SingleTargetModification):
    return node.target.time_start()

@Def.MoveTime
def start(node: MoveTime) -> int:
    target_start = node.target.time_start()
    new_start = target_start + node.offset
    if new_start < 0:
        raise RuntimeError("Start time can not be lower than 0")
    return new_start

# multi target modifications have more complex start time handling

# stack node takes the start time of the background
@Def.Stack
def start(node: Stack) -> int:
    targets = node.targets
    if not targets:
        return 0
    return targets[0].time_start()

