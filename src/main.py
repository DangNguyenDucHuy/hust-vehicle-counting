import os

from dotenv import load_dotenv
load_dotenv()

from preprocess_data import extract_frames


# Env
PROJECT_PATH = os.getenv("PROJECT_PATH")

# Paths
DATA_PATH = os.path.join(PROJECT_PATH, "data")
RAW_DATA_PATH = os.path.join(DATA_PATH, "raw")
PROCESSED_DATA_PATH = os.path.join(DATA_PATH, "processed")
DATASET_DATA_PATH = os.path.join(DATA_PATH, "dataset")

# Config
EXTRACT_FRAMES_INTERVAL_SECONDS = 1



# Run
if __name__ == "__main__":
    for video_filename in os.listdir(RAW_DATA_PATH):
        video_filepath = os.path.join(RAW_DATA_PATH, video_filename)
        
        extract_frames(
            input_video_path=video_filepath,
            output_folder_path=os.path.join(PROCESSED_DATA_PATH, "raw_frames"),
            interval_seconds=EXTRACT_FRAMES_INTERVAL_SECONDS
        )

