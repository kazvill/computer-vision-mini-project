# Climbing Video Pose Tracking (OpenCV + MediaPipe Pose)

This project applies real-time human pose estimation to a vertical climbing video using MediaPipe’s 33-landmark pose model.  
Each frame is processed with OpenCV, annotated with a skeleton overlay, and saved into a new output video.

---

## 🎯 Project Overview

The goal of this project was to learn fundamental video processing and pose estimation techniques using:

- **OpenCV** for handling video input, resizing frames, colour conversions, and writing outputs.
- **MediaPipe Pose** for detecting 33 human body landmarks and drawing a skeleton.

This demonstrates practical skills relevant to:
- computer vision
- sports movement analysis
- robotics and tracking
- defence applications (e.g., human movement understanding)

---

## 🧗 What the Script Does

- Loads a vertical climbing video (`IMG_2203.mp4`)
- Resizes each frame to **270 × 480** for faster inference
- Converts BGR → RGB for MediaPipe
- Runs **MediaPipe Pose** in lightweight mode (`model_complexity=0`)
- Draws:
  - 33 joints (keypoints)
  - skeletal connections
- Writes the output frames into `climb_pose_output.mp4` with the **same FPS** as the input
- (Optional) Displays a preview window during processing

---

## 📁 Files Included

- `video_track.py` — main pose-tracking script  
- `IMG_2203.mp4` — raw climbing video  
- `climb_pose_output.mp4` — final annotated output video  

---

## 🛠️ Technologies Used

- **Python**
- **OpenCV (cv2)** — video I/O, resizing, colour conversions, display, output writer
- **MediaPipe Pose** — fast 33-point human pose detector
- **NumPy** (optional)

---

## ▶️ How to Run

Make sure `video_track.py` and your climbing video are in the same folder.

Then:

```bash
python video_track.py

