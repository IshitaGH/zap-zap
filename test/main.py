#!/usr/bin/env python3

import cv2
import numpy as np

from webcam import Webcam, CamSet
from dotenv import dotenv_values

env = dotenv_values(".env")
uname = env["uname"]
passwd = env["passwd"]

ip1 = env["ip1"]
port1 = env["port1"]
url1 = f"https://{uname}:{passwd}@{ip1}:{port1}/video"

ip2 = env["ip2"]
port2 = env["port2"]
url2 = f"http://{ip2}:{port2}/video"

cam1 = Webcam(url1)
cam2 = Webcam(url2)

camset = CamSet(cam1, cam2)

windows = ("window1", "window2")

for imgs in camset:
    for win, img in zip(windows, imgs):
        cv2.imshow(win, cv2.rotate(img, rotateCode=cv2.ROTATE_90_CLOCKWISE))

    match cv2.pollKey():
        case 0x71:  # q
            for cam in camset.cams:
                cam.close()
            break
