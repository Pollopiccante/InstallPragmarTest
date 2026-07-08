from tests.list_test.gen.classes import Def
from tests.list_test.gen.nodes import Image, ApplicableRange, Window, Video, Filter


@Def.ApplicableRange
def frame_is_in_range(node: ApplicableRange, frame_index: int):
    for window in node.windows:
        if window.start_frame < frame_index < window.end_frame:
            return True
    return False

@Def.Video
def apply_all_filters(node: Video):
    for fil in node.filters:
        fil.attributes_apply_filter_to_frames(fil)

@Def.Video.Filter
def apply_filter_to_frames(node: Video, fil: Filter):
    for i, frame in enumerate(node.frames):
        if fil.range.attributes_frame_is_in_range(i):
            fil.attributes_apply(frame)

@Def.Filter
def apply(node: Filter, image: Image):
    print(f"applied filter: {node.mod.mod_name} to image: {image.image_file_path}")