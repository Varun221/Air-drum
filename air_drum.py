import cv2
import numpy as np
import time
import pygame

w = 100
h = 200
x1 = 80
y = 250
x2 = 460
x3 = 270
flag = 0
cap = cv2.VideoCapture(0)
cap.set(3, 720)
cap.set(4, 1280)
lower_bound = np.array([80,10,170])
upper_bound = np.array([120, 100, 255])
right_thresh = 7000
left_thresh = 5000
centre_thresh = 6000
tl = 0
tr = 0
tc = 0
bet_time = 0.8

pygame.init()
pygame.mixer.init()
pl= pygame.mixer.Sound("tin.wav")
pr= pygame.mixer.Sound("chsh.wav")
pc= pygame.mixer.Sound("clamp.wav")


while (cap.isOpened()):
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)  # flipping the image
    to_show = np.copy(frame)
    # so that the box will not interfere in masking
    to_show = cv2.rectangle(to_show, (x1,y), (x1+w, y+h), (0,255,0), 2)
    to_show = cv2.rectangle(to_show, (x2, y), (x2 + w, y + h), (0, 255, 0), 2)
    to_show = cv2.rectangle(to_show, (x3, y), (x3+w, y+h), (0,255,0), 2)


    cv2.imshow("video", to_show)


    # creating the mask and the boxes
    kernel = np.ones((5, 5), np.uint8)
    frame = cv2.erode(frame, kernel, iterations=2)
    frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(frame_hsv, lower_bound, upper_bound)
    left_box = mask[y:y + h, x1:x1 + w]
    right_box = mask[y:y + h, x2:x2 + w]
    centre_box = mask[y:y+h, x3:x3+w]

    # checking left box
    left_vals = left_box == 255
    if np.sum(left_vals) > left_thresh:
        if time.time() - tl >= bet_time:
            print('left one')
            pl.play()
            time.sleep(0.1)
            tl = time.time()


    # checking right
    right_vals = right_box == 255
    if np.sum(right_vals) > right_thresh:
        if time.time() - tr >=bet_time:
            print('right one')
            pr.play()
            time.sleep(0.1)
            tr = time.time()

    # checking centre
    centre_vals = centre_box == 255
    if np.sum(centre_vals) > centre_thresh:
        if time.time() - tc >=bet_time:
            print('centre one')
            pc.play()
            time.sleep(0.1)
            tc = time.time()


    #cv2.imshow('left_box', left_box)
    #cv2.imshow('right_box', right_box)
    #cv2.imshow('centre_box', centre_box)
    #cv2.imshow("mask", mask)
    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()
