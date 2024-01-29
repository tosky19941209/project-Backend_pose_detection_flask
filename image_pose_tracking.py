import cv2
import mediapipe as mp

# Load MediaPipe Pose model
mp_pose = mp.solutions.pose
pose = mp_pose.Pose()

# Read the input image
img = cv2.imread('1.jpg')

# Convert the image to RGB
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Process the image and detect the pose
result = pose.process(img_rgb)

# If pose is detected, draw the landmarks
if result.pose_landmarks:
    # Draw the landmarks on the image


    for landmark in result.pose_landmarks.landmark:
        # Get the pixel coordinates of the landmark
        h, w, c = img.shape
        cx, cy = int(landmark.x * w), int(landmark.y * h)
        # Draw a small circle at the landmark position
        cv2.circle(img, (cx, cy), 3, (255,255,0), -1)


# Display the result
cv2.imshow('Pose Detection Result', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Release the pose model
pose.close()