import cv2, os, imutils
import numpy as np
# import dlib

capture = cv2.VideoCapture(0)

if not capture.isOpened():
    exit()

ret, old_frame = capture.read()

cv2.namedWindow('Select Window')
cv2.imshow('Select Window', old_frame)

# Select ROI
rect = cv2.selectROI('Select Window', old_frame, fromCenter=False, showCrosshair=True)
cv2.destroyWindow('Select Window')

while capture.isOpened():
    ret, frame = capture.read()
    if not ret:
        exit()

    cv2.imshow('img', frame)

    if cv2.waitKey(1) == ord('q'):
        break