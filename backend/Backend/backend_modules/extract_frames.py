import cv2
import os

def extract_frames(video_path, output_folder, frame_interval=30):
    """
    Extract frames from a video at regular intervals.
    
    :param video_path: Path to the video file
    :param output_folder: Folder to save the extracted frames
    :param frame_interval: Interval between frames (in seconds)
    """
    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Load the video
    cap = cv2.VideoCapture(video_path)
    
    frame_count = 0
    success, frame = cap.read()
    fps = cap.get(cv2.CAP_PROP_FPS)
    interval_frames = int(fps * frame_interval)
    
    while success:
        # Save a frame at the specified interval
        if frame_count % interval_frames == 0:
            frame_filename = os.path.join(output_folder, f"frame_{frame_count}.jpg")
            cv2.imwrite(frame_filename, frame)
            print(f"Saved: {frame_filename}")
        
        # Read the next frame
        success, frame = cap.read()
        frame_count += 1
    
    cap.release()
    print(f"Frames extracted and saved to {output_folder}")

if __name__ == "__main__":
    video_path = "sample_video.mp4"  # Replace with your video file path
    output_folder = "frames"         # Folder to save the frames
    
    extract_frames(video_path, output_folder)
