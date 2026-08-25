import subprocess
import unittest

from PRAGMAR.main import load_all_parent

from tests.meme_generator.gen.nodes import AllParent


def run_command():
    pass

class TestAll(unittest.TestCase):

    def run_command(self, command):
        command = command + " -y"
        print("RUNNING COMMAND: " + command)
        result = subprocess.run(command, shell=True, capture_output=True)
        print(f"COMMAND RETURN: {result.returncode}")
        self.assertEqual(result.returncode, 0)

    def setUp(self):
        ap = load_all_parent("tests.meme_generator.def", "tests.meme_generator.gen")
        self.ap = AllParent.wrap(ap)

    def tearDown(self):
        self.ap = None

    def test_simple_image(self):
        img = self.ap.create_Image("images/red.png")
        frame_root = self.ap.create_FrameRoot(img)
        self.ap.prag_add_ast(frame_root)
        self.run_command(frame_root.media_generate_ffmpeg_command())

    def test_simple_video(self):
        vid = self.ap.create_Video("videos/green.mp4")
        frame_root = self.ap.create_FrameRoot(vid)
        self.ap.prag_add_ast(frame_root)
        self.run_command(frame_root.media_generate_ffmpeg_command())


    def test_stack(self):
        video = self.ap.create_Video("videos/green.mp4")
        img = self.ap.create_Image("images/red.png")
        stack = self.ap.create_Stack([video, self.ap.create_Duration(img, 24)])
        frame_root = self.ap.create_FrameRoot(stack)

        self.ap.prag_add_ast(frame_root)
        self.run_command(frame_root.media_generate_ffmpeg_command())

    def test_complex_no_rotation(self):
        video = self.ap.create_Video("videos/green.mp4")
        img = self.ap.create_Image("images/red.png")
        dur = self.ap.create_Duration(img, 24)
        scaled = self.ap.create_Scale(dur, 100, 100)
        moved = self.ap.create_Position(scaled, 200, 400)
        stack = self.ap.create_Stack([video, moved])
        frame_root = self.ap.create_FrameRoot(stack)

        self.ap.prag_add_ast(frame_root)
        self.run_command(frame_root.media_generate_ffmpeg_command())


