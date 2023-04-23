# Training Multiple Faces stored on a DataBase:
# 	==> Each face should have a unique numeric integer ID as 1, 2, 3, etc                       
# 	==> LBPH computed model will be saved on trainer/ directory. (if it does not exist, pls create one)
# 	==> for using PIL, install pillow library with "pip install pillow"
# Based on original code by Anirban Kar: https://github.com/thecodacus/Face-Recognition    
# Developed by Marcelo Rovai - MJRoBot.org @ 21Feb18 

# https://github.com/Mjrovai/OpenCV-Face-Recognition/blob/master/FacialRecognition/02_face_training.py

import numpy as np
import cv2
from webcam import Webcam
import dotenv
from pathlib import Path
import os
from PIL import Image


BASE_DIR = Path(__file__).resolve().parent.parent

dotenv_file = os.path.join(BASE_DIR, ".env")
if os.path.isfile(dotenv_file):
    dotenv.load_dotenv(dotenv_file)

a_uname = os.environ.get('CAMERA_A_USERNAME')
a_passwd = os.environ.get('CAMERA_A_PASSWORD')
a_ip = os.environ.get('CAMERA_A_IP')
a_port = os.environ.get('CAMERA_A_PORT')

# Path for face image database
path = 'dataset'

recognizer = cv2.face.LBPHFaceRecognizer_create()
detector = cv2.CascadeClassifier("cascades/haarcascade_frontalface_default.xml")

# function to get the images and label data
def getImagesAndLabels(path):

    imagePaths = [os.path.join(path,f) for f in os.listdir(path)]     
    faceSamples=[]
    ids = []

    for imagePath in imagePaths:

        PIL_img = Image.open(imagePath).convert('L') # convert it to grayscale
        img_numpy = np.array(PIL_img,'uint8')

        id = int(os.path.split(imagePath)[-1].split(".")[1])
        faces = detector.detectMultiScale(img_numpy)

        for (x,y,w,h) in faces:
            faceSamples.append(img_numpy[y:y+h,x:x+w])
            ids.append(id)

    return faceSamples,ids

print ("\n [INFO] Training faces. It will take a few seconds. Wait ...")
faces,ids = getImagesAndLabels(path)
recognizer.train(faces, np.array(ids))

# Save the model into trainer/trainer.yml
recognizer.write('trainer/trainer.yml') # recognizer.save() worked on Mac, but not on Pi

# Print the numer of faces trained and end program
print("\n [INFO] {0} faces trained. Exiting Program".format(len(np.unique(ids))))
