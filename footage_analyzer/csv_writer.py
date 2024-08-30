import csv
import os
from pathlib import Path

from footage_analyzer.videoData import VideoData, get_metadata

def collect_and_write(root_dir: Path, output_csv: Path, allowed_extensions: list[str]):
    with open(output_csv, mode="w", newline="") as csv_file:
        field_names = ["filename", "full path", "type", "runtime (seconds)", "resolution"]
        writer = csv.DictWriter(csv_file, fieldnames=field_names, delimiter=";")
        writer.writeheader()
        total_files = 0
        total_videos = 0

        for subdir, _, files in os.walk(root_dir):
            print(f"found {len(files)} files at {subdir}...")
            curr_folder_file_count = 0
            for file in files:
                total_files += 1
                curr_folder_file_count += 1
                print(f"processing {curr_folder_file_count}/{len(files)}...")
                file_extension = Path(file).suffix.lower().replace(".", "")
                if file_extension in allowed_extensions:
                    file_path: Path = Path(subdir) / file
                    video: VideoData = get_metadata(file_path)
                    if video:
                        print("Found valid video!")
                        total_videos += 1
                        writer.writerow(
                            {
                                "filename": video.filename,
                                "full path": video.path,
                                "type": video.file_extension,
                                "runtime (seconds)": video.runtime_minutes,
                                "resolution": video.resolution,
                            }
                        )

    print("Finished process")
    print(f"Registered {total_videos} out of {total_files} files")
    print(f"csv file created at: {output_csv}")
