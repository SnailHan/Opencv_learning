# -*- coding: cp936 -*-
import cv2
import numpy as np
def nothing(x):
    pass

cap = cv2.VideoCapture(0)
cv2.namedWindow('��ʻ�',0)
cv2.createTrackbar('��ֵ1', '��ʻ�', 0, 255, nothing)
cv2.createTrackbar('��ֵ2', '��ʻ�', 255, 255, nothing)
cv2.createTrackbar('��ֵ3', '��ʻ�', 0, 255, nothing)
cv2.createTrackbar('��ֵ4', '��ʻ�', 255, 255, nothing)
cv2.createTrackbar('��ֵ5', '��ʻ�', 0, 255, nothing)
cv2.createTrackbar('��ֵ6', '��ʻ�', 255, 255, nothing)

while(1):

    # Take each frame
    _, frame = cap.read()

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    thrs1 = cv2.getTrackbarPos('��ֵ1', '��ʻ�')
    thrs2 = cv2.getTrackbarPos('��ֵ2', '��ʻ�')
    thrs3 = cv2.getTrackbarPos('��ֵ3', '��ʻ�')
    thrs4 = cv2.getTrackbarPos('��ֵ4', '��ʻ�')
    thrs5 = cv2.getTrackbarPos('��ֵ5', '��ʻ�')
    thrs6 = cv2.getTrackbarPos('��ֵ6', '��ʻ�')

    # define range of blue color in HSV
    lower_blue = np.array([thrs1,thrs3,thrs5])
    upper_blue = np.array([thrs2,thrs4,thrs6])

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask)

    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('��ʻ�',res)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()


