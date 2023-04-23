# https://www.hackster.io/mjrobot/real-time-face-recognition-an-end-to-end-project-a10826

import numpy as np
import cv2
from webcam import Webcam
import dotenv
from pathlib import Path
import os

def face_detection():
    BASE_DIR = Path(__file__).resolve().parent.parent

    dotenv_file = os.path.join(BASE_DIR, ".env")
    if os.path.isfile(dotenv_file):
        dotenv.load_dotenv(dotenv_file)

    a_uname = os.environ.get('CAMERA_A_USERNAME')
    a_passwd = os.environ.get('CAMERA_A_PASSWORD')
    a_ip = os.environ.get('CAMERA_A_IP')
    a_port = os.environ.get('CAMERA_A_PORT')
    
    url = f"https://{a_uname}:{a_passwd}@{a_ip}:{a_port}/video"
    webcam = Webcam(url)

    # multiple cascades: https://github.com/Itseez/opencv/tree/master/data/haarcascades
    face_cascade = cv2.CascadeClassifier('cascades/haarcascade_frontalface_default.xml')

    for frame in webcam:
        # frame = cv2.flip(frame, 0) # Flip camera vertically
        frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(
            gray,
            
            scaleFactor=1.2,
            minNeighbors=5,     
            minSize=(20, 20)
        )

        for (x,y,w,h) in faces:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = frame[y:y+h, x:x+w]
        
        # cv2.imshow('frame', frame)
        cv2.imshow('video', frame)
        
        match cv2.pollKey():
            case 0x71:  # PRESS 'q' TO STOP!!
                webcam.close()
                break
    
    cv2.destroyAllWindows()
    # DELETE THE LINE FOLLOWING THIS EVENTUALLY!!! in here for now for cam_test.py
    return False

def face_eye_detection(frame, gray):
    # multiple cascades: https://github.com/Itseez/opencv/tree/master/data/haarcascades
    face_cascade = cv2.CascadeClassifier('cascades/haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier('cascades/haarcascade_eye.xml')

    eye_coords = ()

    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5,     
        minSize=(20, 20)
    )

    for (x,y,w,h) in faces:
        # cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

        eyes = eye_cascade.detectMultiScale(
            roi_gray,
            scaleFactor= 1.5,
            minNeighbors=10,
            minSize=(5, 5),
        )

        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
            print("found eyes")
            eye_coords = (ex + (ew/2), ey + (eh/2))

    return eye_coords

def image_collector_for_database():
    BASE_DIR = Path(__file__).resolve().parent.parent

    dotenv_file = os.path.join(BASE_DIR, ".env")
    if os.path.isfile(dotenv_file):
        dotenv.load_dotenv(dotenv_file)

    a_uname = os.environ.get('CAMERA_A_USERNAME')
    a_passwd = os.environ.get('CAMERA_A_PASSWORD')
    a_ip = os.environ.get('CAMERA_A_IP')
    a_port = os.environ.get('CAMERA_A_PORT')
    
    url = f"https://{a_uname}:{a_passwd}@{a_ip}:{a_port}/video"
    webcam = Webcam(url)

    # multiple cascades: https://github.com/Itseez/opencv/tree/master/data/haarcascades
    face_cascade = cv2.CascadeClassifier('cascades/haarcascade_frontalface_default.xml')

    # For each person, enter one numeric face id
    face_id = input('\n enter user id end press <return> ==>  ')

    print("\n [INFO] Initializing face capture. Look the camera and wait ...")
    # Initialize individual sampling face count
    count = 0

    for frame in webcam:
        frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x,y,w,h) in faces:
            cv2.rectangle(frame, (x,y), (x+w,y+h), (255,0,0), 2)     
            count += 1

            # Save the captured image into the datasets folder
            cv2.imwrite("dataset/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])

            cv2.imshow('image', frame)
        
        match cv2.pollKey():
            case 0x71:  # PRESS 'q' TO STOP!!
                webcam.close()
                break
    
    print("\n [INFO] Exiting Program and cleanup stuff")
    cv2.destroyAllWindows()
    # DELETE THE LINE FOLLOWING THIS EVENTUALLY!!! in here for now for cam_test.py
    return False

def face_recognition(frame, gray):
    # Real Time Face Recogition
    #     ==> Each face stored on dataset/ dir, should have a unique numeric integer ID as 1, 2, 3, etc                       
    #     ==> LBPH computed model (trained faces) should be on trainer/ dir
    # Based on original code by Anirban Kar: https://github.com/thecodacus/Face-Recognition    
    # Developed by Marcelo Rovai - MJRoBot.org @ 21Feb18

    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read('trainer/trainer.yml')
    cascade_path = "cascades/haarcascade_frontalface_default.xml"
    face_cascade = cv2.CascadeClassifier(cascade_path)

    font = cv2.FONT_HERSHEY_SIMPLEX

    #iniciate id counter
    id = 0

    # names related to ids: example ==> Marcelo: id=1,  etc
    names = ['Serena', 'Jason', 'Catherine', 'Morgan', 'idk'] 

    # Define min window size to be recognized as a face
    # IDK ABOUT THESE NUMBERS
    minW = 5
    minH = 5

    faces = face_cascade.detectMultiScale( 
        gray,
        scaleFactor = 1.2,
        minNeighbors = 5,
        minSize = (int(minW), int(minH)),
    )

    for(x,y,w,h) in faces:

        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)

        id, confidence = recognizer.predict(gray[y:y+h,x:x+w])

        # Check if confidence is less them 100 ==> "0" is perfect match 
        # confidence = 0: good
        if (confidence < 50):
            id = names[id]
            confidence = "  {0}%".format(round(100 - confidence))
            return True
        else:
            id = "unknown"
            confidence = "  {0}%".format(round(100 - confidence))
            
        
        cv2.putText(frame, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
        cv2.putText(frame, str(confidence), (x+5,y+h-5), font, 1, (255,255,0), 1)
    
    return False

def find_person(frame, gray):
    # if it doesn't recognize a trusted person, and there are other people detected, point laser there
    eye_coords = face_eye_detection(frame, gray)
    # if face_recognition(frame, gray):
    #     print("recognized trusted person")
    #     eye_coords = ()

    return print(eye_coords)