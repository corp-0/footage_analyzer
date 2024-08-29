from dataclasses import dataclass
from pathlib import Path

from footage_analyzer.csv_writer import collect_and_write


def get_videos_folder() -> Path:
    script_location = Path(__file__).resolve().parent
    videos_folder = script_location.parent

    return videos_folder


@dataclass
class Analyzer:
    videos_folder: Path
    allowed_extensions: list[str]
    output_file: str

    def analyze(self):
        collect_and_write(self.videos_folder, Path(self.output_file), self.allowed_extensions)