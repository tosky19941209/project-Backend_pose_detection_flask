from flask import Flask, request, send_file
import cv2
import mediapipe as mp
import numpy as np
import base64
from io import BytesIO
import json
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})


def generate_bytes(image):
    while True:
        # Convert image to bytes in chunks and yield them
        ret, frame = cv2.imencode('.jpg', image)
        if not ret:
            break
        yield (b'--frame\r\n'
            b'Content-Type: image/jpeg\r\n\r\n' + frame.tobytes() + b'\r\n')

@app.route('/api/upload', methods=['POST'])
def Img_analysis():
    
    file = request.files['image']
    img = file.save('static/image.jpg')
    # app.logger.info('success')
    mp_pose = mp.solutions.pose
    pose = mp_pose.Pose(static_image_mode=True, min_detection_confidence=0.5)

    input_image = cv2.imread('static/image.jpg')

    input_image_rgb = cv2.cvtColor(input_image, cv2.COLOR_BGR2RGB)
    
    # Process the image and detect the pose landmarks
    result = pose.process(image=input_image_rgb)
    app.logger.info(result)
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

        _, encoded_img = cv2.imencode('.jpg', annotated_image)
        my_string = base64.b64encode(encoded_img.tobytes()).decode("utf-8")
        return json.dumps({"title": 1, "image":my_string})
        # return "success"
    else:
        app.logger.info("No pose detected in the image")

@app.route('/api/test', methods = ['GET'])
def Hello():
    app.logger.info("Hello")
    return 'Hello'


if __name__ == '__main__':
    app.run(debug=True)