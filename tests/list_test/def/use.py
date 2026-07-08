
from PRAGMAR.decorators import def_run

from tests.list_test.gen.nodes import Video, Image, Filter, ApplicableRange, Window, Modificator, AllParent


@def_run
def run(ap):
    ap: AllParent = AllParent.wrap(ap)

    frames = [ap.create_Image(100, 200, f"my_image{x}.png") for x in range(100)]
    filters = [
        ap.create_Filter(
            ap.create_ApplicableRange([
                ap.create_Window(0, 10),
                ap.create_Window(90, 100)
            ]),
            ap.create_Modificator("slow_music", 1000)
        ),
    ]
    video = ap.create_Video(frames, filters, "my_video_file.mp4", "My Awesome Video")
    ap.prag_add_ast(video)

    video.attributes_apply_all_filters()