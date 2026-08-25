from dataclasses import dataclass
from functools import cache

import cv2

from tests.meme_generator.config import RESOURCE_FOLDER


@dataclass(frozen=True)
class ImageSpecs:
    width: int
    height: int

@dataclass(frozen=True)
class VideoSpecs:
    width: int
    height: int
    frames: int
    fps: float
    duration_seconds: float


@cache
def get_video_file_specs(file_path) -> VideoSpecs:
    cap = cv2.VideoCapture(RESOURCE_FOLDER + file_path)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    duration_seconds = (frames / fps) if fps else 0
    cap.release()

    return VideoSpecs(width, height, frames, fps, duration_seconds)

@cache
def get_image_file_specs(file_path) -> ImageSpecs:
    img = cv2.imread(RESOURCE_FOLDER + file_path)
    height, width, channels = img.shape
    return ImageSpecs(width, height)

if __name__ == "__main__":
    specs = get_video_file_specs("videos/green.mp4")
    print(specs.width)
    print(specs.height)
    print(specs.frames)
    print(specs.fps)
    print(specs.duration_seconds)


