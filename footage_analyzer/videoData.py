from dataclasses import dataclass
from moviepy.editor import VideoFileClip
from pathlib import Path

@dataclass
class VideoData:
    filename: str
    file_extension: str
    runtime_minutes: float
    resolution: str

def get_metadata(file: Path) -> VideoData | None:
    try:
        with VideoFileClip(str(file)) as video:
            filename = file.name.replace(file.suffix, "")
            extension = file.suffix[1:]
            runtime = video.duration
            resolution = f"{video.w}x{video.h}"

        return VideoData(filename, extension, runtime, resolution)
    except:  # noqa: E722
        return None
