import cv2
import numpy as np
import time


cap = cv2.VideoCapture(0)

fps = 20.0
width = int(cap.get(3))
height = int(cap.get(4))
fourcc = cv2.cv.FOURCC(*'XVID')
out = cv2.VideoWriter('test.avi',
        fourcc, 
        fps,
        (width,height))

start = time.time()

while True:
        ret, frame = cap.read()
        out.write(frame)
        
        if time.time() - start > 10:
                break

cap.release()
out.release()

