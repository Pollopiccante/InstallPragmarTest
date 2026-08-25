from PRAGMAR.decorators import def_run
from PRAGMAR.new_tree import AllParentNode

from tests.meme_generator.gen.nodes import AllParent


def create_image(ap, angle, offset, time):
    img = ap.create_Image("images/red.png")
    scaled = ap.create_Scale(img, 200, 300)
    dur = ap.create_Duration(scaled, time)
    offset = ap.create_MoveTime(dur, offset)
    rotated = ap.create_Rotate(offset, angle)
    return rotated

# create AST
@def_run
def run(ap: AllParentNode):
    ap: AllParent = AllParent.wrap(ap)

    video = ap.create_Video("videos/green.mp4")

    fs = []
    for i in range(24):
        f = ap.create_Position(create_image(ap, int((360/24.0)*i), i*2, 2), 400, 400)
        fs.append(f)


    stack = ap.create_Stack([video, *fs])
    frame_root = ap.create_FrameRoot(stack)

    ap.prag_add_ast(frame_root)


    print(f"time: {stack.time_duration()}")
    print(f"size: {stack.dimension_size()}")
    print(f"inputs: {stack.media_get_inputs()}")
    print(f"command:{frame_root.media_generate_ffmpeg_command()} ")
    print(f"video inp:{video.media_filter_key()} ")