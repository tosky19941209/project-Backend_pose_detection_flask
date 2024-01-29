import cv2
import mediapipe as mp

# Load MediaPipe Pose model
mp_pose = mp.solutions.pose
pose = mp_pose.Pose()

# Open the video file
video = cv2.VideoCapture('input_img/6.avi')

# Create a video writer to save the result
output_video_path = 'output/6.mp4'
frame_width = int(video.get(3))
frame_height = int(video.get(4))
output_video = cv2.VideoWriter(output_video_path, cv2.VideoWriter_fourcc(*'mp4v'), 30, (frame_width, frame_height))

# Process each frame of the video
while video.isOpened():
    ret, frame = video.read()
    if not ret:
        break

    # Convert the frame to RGB
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame and detect the pose
    result = pose.process(frame_rgb)

    # If pose is detected, draw the landmarks and connections
    if result.pose_landmarks:
        # Draw the landmarks on the frame
        mp_drawing = mp.solutions.drawing_utils
        annotated_frame = frame.copy()  # Create a copy of the frame for drawing
        mp_drawing.draw_landmarks(annotated_frame, result.pose_landmarks, mp_pose.POSE_CONNECTIONS)

        # Write the annotated frame to the output video
        output_video.write(annotated_frame)
    else:
        # If no pose is detected, write the original frame to the output video
        output_video.write(frame)

    # Display the frame with pose landmarks
    cv2.imshow('Frame with Pose Landmarks', annotated_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video and close all windows
video.release()
output_video.release()
cv2.destroyAllWindows()

# Release the pose model
pose.close()