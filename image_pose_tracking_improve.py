import cv2
import mediapipe as mp

# Load MediaPipe Pose model
mp_pose = mp.solutions.pose
pose = mp_pose.Pose(static_image_mode=True, min_detection_confidence=0.5)

# Read the input image
img_path = 'input_img'
filename = '5.jpg'
input_image = cv2.imread(img_path + '/' + filename)

# Convert the image to RGB
input_image_rgb = cv2.cvtColor(input_image, cv2.COLOR_BGR2RGB)

# Process the image and detect the pose landmarks
result = pose.process(image=input_image_rgb)

# Draw the landmarks on the image with custom color
if result.pose_landmarks:
    mp_drawing = mp.solutions.drawing_utils
    annotated_image = input_image.copy()  # Create a copy of the input image for drawing
    mp_drawing.draw_landmarks(
        annotated_image, 
        result.pose_landmarks, 
        mp_pose.POSE_CONNECTIONS,
        landmark_drawing_spec=mp_drawing.DrawingSpec(color=(255, 0, 0), thickness=2, circle_radius=2),
        connection_drawing_spec=mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=2, circle_radius=2)
    )

    # Display the image with pose landmarks
    cv2.imshow('Pose Landmarks', annotated_image)
    cv2.imwrite(f'output/{filename}', annotated_image)
    cv2.waitKey(0)
else:
    print("No pose detected in the image")

# Release the pose model
pose.close()


