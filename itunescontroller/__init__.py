import os
import random
import sys
import cv2

path = os.path.abspath(os.path.dirname(__file__))

def capture_pic():
    cam = cv2.VideoCapture(0)
    captured, img = cam.read()
    #cam.release()

    if captured:
        return img
    else:
        return None

def detect_face(img):
    cascade_path = path + os.path.sep + "data/haarcascade_frontalface_default.xml"

    face_cascade = cv2.CascadeClassifier(cascade_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor = 1.1,
        minNeighbors = 3,
        flags = cv2.cv.CV_HAAR_SCALE_IMAGE
    )

    # We get a empty tuple, if no face is detected.
    return len(faces) > 0

def main():
    img = capture_pic()

    if img is not None:
        if detect_face(img):
            print("face")
        else:
            print("no face")
