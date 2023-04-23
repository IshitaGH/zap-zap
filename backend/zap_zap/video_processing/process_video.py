from turtle import window_width
import numpy as np
import cv2
from webcam import Webcam, CamSet
import dotenv
from pathlib import Path
import os

from detection_recognition import face_detection, face_eye_detection, image_collector_for_database, face_recognition, find_person


BASE_DIR = Path(__file__).resolve().parent.parent

dotenv_file = os.path.join(BASE_DIR, ".env")
if os.path.isfile(dotenv_file):
    dotenv.load_dotenv(dotenv_file)

a_uname = os.environ.get('CAMERA_A_USERNAME')
a_passwd = os.environ.get('CAMERA_A_PASSWORD')
a_ip = os.environ.get('CAMERA_A_IP')
a_port = os.environ.get('CAMERA_A_PORT')

b_ip = os.environ.get('CAMERA_B_IP')
b_port = os.environ.get('CAMERA_B_PORT')

url_a = f"https://{a_uname}:{a_passwd}@{a_ip}:{a_port}/video"
webcam_a = Webcam(url_a)

url_b = f"http://{b_ip}:{b_port}/video"
webcam_b = Webcam(url_b)

camset = CamSet(webcam_a,webcam_b)
windows = ("Camera_A", "Camera_B")

for frame_a in webcam_a:
    frame_b = next(webcam_b)

    frame_a = cv2.rotate(frame_a, cv2.ROTATE_90_CLOCKWISE)
    frame_b = cv2.rotate(frame_b, cv2.ROTATE_90_CLOCKWISE)

    gray_a = cv2.cvtColor(frame_a,cv2.COLOR_BGR2GRAY)
    gray_b = cv2.cvtColor(frame_b,cv2.COLOR_BGR2GRAY)

    print(find_person(frame_a, gray_a))
    print(find_person(frame_b, gray_b))

    cv2.imshow(windows[0],frame_a)
    cv2.imshow(windows[1],frame_b) 

    match cv2.pollKey():
        case 0x71:  # PRESS 'q' TO STOP!!
            webcam_a.close()
            webcam_b.close()
            break

cv2.destroyAllWindows()
