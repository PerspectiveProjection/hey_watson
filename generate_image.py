import numpy as np
import cv2

def generate_image():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cv2.imwrite("frame.jpg", frame)
    cap.release
    return

generate_image()
