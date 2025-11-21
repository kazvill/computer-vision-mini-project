import cv2
import mediapipe as mp

VIDEO_PATH = "IMG_2203.mp4"          # change if your file has a different name
OUTPUT_PATH = "climb_pose_output.mp4"

# --- Setup video capture ---
cap = cv2.VideoCapture(VIDEO_PATH)

if not cap.isOpened():
    print("❌ Could not open video file:", VIDEO_PATH)
    exit()

# Get FPS from source (fall back to 30 if missing)
fps = cap.get(cv2.CAP_PROP_FPS)
if fps == 0:
    fps = 30.0

# Because it’s a vertical video we keep height > width
OUT_SIZE = (270, 480)   # (width, height)

fourcc = cv2.VideoWriter_fourcc(*"mp4v")
out = cv2.VideoWriter(OUTPUT_PATH, fourcc, fps, OUT_SIZE)

# --- Mediapipe setup ---
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

with mp_pose.Pose(
        static_image_mode=False,
        model_complexity=0,          # 0 = lightest, fastest model
        enable_segmentation=False,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5) as pose:

    frame_count = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            print("✅ Finished processing video.")
            break

        frame_count += 1

        # OPTIONAL: skip frames to speed up processing
        # if frame_count % 2 == 0:
        #     continue

        # Resize to 270 x 480 (vertical)
        frame = cv2.resize(frame, OUT_SIZE)

        # BGR -> RGB for mediapipe
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Pose estimation
        results = pose.process(rgb)

        # Draw skeleton if detected
        if results.pose_landmarks:
            mp_drawing.draw_landmarks(
                frame,
                results.pose_landmarks,
                mp_pose.POSE_CONNECTIONS
            )

        # Write to output video
        out.write(frame)

        # Optional preview (will look slow while processing – that’s normal)
        cv2.imshow("Processing (press q to quit)", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

cap.release()
out.release()
cv2.destroyAllWindows()

print("💾 Saved processed video to:", OUTPUT_PATH)
