# zap-zap

Our product - *Zap-Zap* - is a home security system that alerts against people considered intruders, ie. those not saved within the trusted database connected with the homeowner’s account. It works by ringing an alarm as soon as it detects an intruder. It also aims a laser at the intruder’s eyes to temporarily stun them and give those living within the home to react.

## Features
* Eye Detection
* Laser Aiming
* Alarms
* Adding Trusted People

## Technologies
* Django
* OpenCV
* React
* Raspberry Pi
* Python
* MicroPython
* JavaScript

## Setup:
### Backend:
Make sure you have pipenv installed! In the root of the project, run the following:
```
cd backend
pipenv install
cd zap_zap
python manage.py runserver
```
If you want to start the video processing, open a new terminal, and within the root directory of this project, run the following:
```
cd backend/zap_zap/video_processing
python process_video.py
```
### Frontend:
From the root of the project, run the following:
```
cd frontend
npm install
npm start
```
### Hardware:
Follow the Raspberry Pi documentation to install the necessary environment (eg. Thonny). Use Thonny to upload hardware/main.py to the Raspberry Pi Pico Board.

## Authors
This project was created by Ishita Ghosh, Jason Cheng, Catherine Kang, and Serena Ong for LA Hacks 2023.