import os
import cv2

def extract_frames(
    input_video_path: str, 
    output_folder_path: str,
    interval_seconds: float = 1
):
    os.makedirs(output_folder_path, exist_ok=True)
    
    cap = cv2.VideoCapture(input_video_path)
    
    fps = cap.get(cv2.CAP_PROP_FPS)
    interval = int(fps * interval_seconds)
    
    video_name = os.path.basename(input_video_path).split('.')[0]

    frame_count = 0
    saved_count = 0
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        if frame_count % interval == 0:
            save_path = os.path.join(output_folder_path, f"{video_name}_{saved_count}.jpg")
            cv2.imwrite(save_path, frame)
            saved_count += 1
        
        frame_count += 1
    
    cap.release()
    print(f"[Info] Video '{video_name}' done: Saved {saved_count}/{frame_count} frames to '{output_folder_path}'")
