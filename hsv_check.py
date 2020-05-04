import cv2
import numpy as np
import time
w = 100
h = 200
x1 = 117
y = 103
lower_bound = np.array([80,10,180])
upper_bound = np.array([120, 100, 255])
values = np.array([])


cap = cv2.VideoCapture(0)

while True:
    """ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    cv2.rectangle(frame, (x1, y), (x1 + w, y + h), (0, 255, 0), 2)
    cv2.imshow("video",frame)
    centre =  frame_hsv[142:192, 153: 253 ]
    avg = np.sum(centre)/ centre.size
    print(avg)
    print("--------")"""

    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    #frame = cv2.GaussianBlur(frame, (5,5),0)
    kernel = np.ones((5, 5), np.uint8)
    frame = cv2.erode(frame, kernel, iterations=2)
    cv2.imshow('feed',frame)
    frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(frame_hsv, lower_bound, upper_bound)
    res = cv2.bitwise_and(frame, frame, mask = mask)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)


    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()