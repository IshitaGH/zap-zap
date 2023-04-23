from turtle import window_width
import numpy as np
import cv2
from webcam import Webcam, CamSet
import dotenv
from pathlib import Path
import os

from detection_recognition import face_detection, face_eye_detection, image_collector_for_database, face_recognition
from servo_formula import get_servo_space_coord, solve_angles
import math
import struct
import socket

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

for w in windows:
    cv2.namedWindow(w, cv2.WINDOW_AUTOSIZE | cv2.WINDOW_KEEPRATIO | cv2.WINDOW_GUI_NORMAL)

ip = os.environ.get('RPI_IP')

sock = socket.create_connection((ip, 8000))

try:
    for frame_a, frame_b in camset:

        match cv2.pollKey():
            case 0x71:  # PRESS 'q' TO STOP!!
                webcam_a.close()
                webcam_b.close()
                break

        frame_a = cv2.rotate(frame_a, cv2.ROTATE_90_CLOCKWISE)
        frame_b = cv2.rotate(frame_b, cv2.ROTATE_90_CLOCKWISE)

        gray_a = cv2.cvtColor(frame_a,cv2.COLOR_BGR2GRAY)
        gray_b = cv2.cvtColor(frame_b,cv2.COLOR_BGR2GRAY)

        cv2.imshow(windows[0],gray_a)
        cv2.imshow(windows[1],gray_b) 

        try:
            j1, i1 = face_eye_detection(gray_a)
            j2, i2 = face_eye_detection(gray_b)
            i1 = int(i1)
            j1 = int(j1)
            i2 = int(i2)
            j2 = int(j2)
        except Exception as e:
            print(e)
            continue

        try:
            x, y, z = get_servo_space_coord(i1, j1, i2, j2)

            theta, phi = solve_angles(x, y, z)

            # Calibration
            theta += 5.5 * math.pi / 180
            phi -= 7.2 * math.pi / 180

        except ZeroDivisionError:
            print("div 0")
            continue

        f1 = theta / math.pi
        f2 = phi / math.pi + 0.5

        msg = struct.pack("!bff", 2, f1, f2)

        sock.sendall(msg)

except Exception as e:
    print(e)

finally:
    cv2.destroyAllWindows()
    sock.close()
