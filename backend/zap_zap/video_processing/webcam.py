from cv2 import VideoCapture

class Webcam:
    def __init__(self, url):
        self.url = url
        self.video = VideoCapture(url)
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if not self.video.isOpened():
            print("stop due to closed")
            raise StopIteration
        
        ret, frame = self.video.read()

        if not ret:
            print("stop due to not ret")
            print(self.url)
            raise StopIteration

        return frame
    
    def close(self):
        self.video.release()

class CamSet:
    def __init__(self, *cams: Webcam):
        self.cams = cams

    def __iter__(self):
        return self
    
    def __next__(self):
        return tuple(next(cam) for cam in self.cams)
