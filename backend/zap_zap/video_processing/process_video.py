from turtle import window_width
import numpy as np
import cv2
from webcam import Webcam, CamSet
import dotenv
from pathlib import Path
import os

from detection_recognition import face_detection, face_eye_detection, image_collector_for_database, face_recognition, find_person
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

ip = os.environ.get('RPI_IP')

sock = socket.create_connection((ip, 8000))

try:
    for frame_a, frame_b in camset:

        frame_a = cv2.rotate(frame_a, cv2.ROTATE_90_CLOCKWISE)
        frame_b = cv2.rotate(frame_b, cv2.ROTATE_90_CLOCKWISE)

        gray_a = cv2.cvtColor(frame_a,cv2.COLOR_BGR2GRAY)
        gray_b = cv2.cvtColor(frame_b,cv2.COLOR_BGR2GRAY)

        cv2.imshow(windows[0],frame_a)
        cv2.imshow(windows[1],frame_b) 

        try:
            (i1, j1) = find_person(frame_a, gray_a)
            (i2, j2) = find_person(frame_b, gray_b)
            print("FOUND 2 FACES")
        except Exception:
            print("did not find 2 faces")
            continue

        x, y, z = get_servo_space_coord(i1, j1, i2, j2)
        print(f"servo: {(x, y, z)}")

        theta, phi = solve_angles(x, y, z)

        print(f"theta = {theta} phi = {phi}")

        f1 = theta / math.pi
        f2 = phi / math.pi + 0.5

        msg = struct.pack("!bff", 2, f1, f2)

        sock.sendall(msg)

        match cv2.pollKey():
            case 0x71:  # PRESS 'q' TO STOP!!
                webcam_a.close()
                webcam_b.close()
                break

finally:
    cv2.destroyAllWindows()
    sock.close()
