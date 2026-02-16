from flask import Flask, request, jsonify
from fingerprint_module import extract_frames, generate_video_hash
from Hash_matching_module import compare_hashes
from webscrapper_module import search_videos
from Visualization_module import visualize_frames
import os

app = Flask(__name__)

# Configure the upload folder
UPLOAD_FOLDER = os.path.abspath('uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def home():
    return "Backend is working!"

@app.route('/search')
def search():
    query = "deepfake"
    results = search_videos(query)
    print("Search function called")
    return {"results": results}

@app.route('/upload', methods=['GET', 'POST'])
def upload_video():
    if request.method == 'GET':
        return "Upload endpoint is ready. Use POST to upload a video."

    if 'video' not in request.files:
        print("No video file provided. Request files:", request.files)
        return jsonify({"error": "No video file provided", "files": str(request.files)}), 400

    video = request.files['video']
    if video.filename == '':
        return jsonify({"error": "No selected file"}), 400

    # Save the video to the existing uploads folder
    video_path = os.path.join(app.config['UPLOAD_FOLDER'], video.filename)
    video.save(video_path)

    print(f"Video uploaded: {video_path}")

    return jsonify({"message": "Video uploaded successfully!", "path": video_path})

if __name__ == "__main__":
    print("Server is starting...")
    app.run(host="0.0.0.0", port=5001, debug=True)
