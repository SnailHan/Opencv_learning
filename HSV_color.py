# -*- coding: cp936 -*-
#���ģ��㶮��
'''
�˽ű���������������HSV��ѧ���ԣ�����ɫ���ȵ���Ϣ

#�˽ű���windows����python 2.7+opencv3.2�汾�ģ� ���ü����������
https://github.com/wjb711/Opencv_learning/blob/master/windows_python2.7_opencv3.2%E5%AE%89%E8%A3%85%E9%85%8D%E7%BD%AE%E6%8C%87%E5%AF%BC.txt
#��Ҫ��ǰ��װspeechģ�飬 ��װ����pip install speech
���У���ֵ1��2����Hɫ�ʣ� 3��4����S���ȣ�5��6����V����     
'''
import cv2
import numpy as np
import sys
def nothing(x):
    pass

cap = cv2.VideoCapture(0)
cv2.namedWindow('��ɫ��׽',0)
cv2.createTrackbar('��ֵ1', '��ɫ��׽', 0, 255, nothing)
cv2.createTrackbar('��ֵ2', '��ɫ��׽', 255, 255, nothing)
cv2.createTrackbar('��ֵ3', '��ɫ��׽', 0, 255, nothing)
cv2.createTrackbar('��ֵ4', '��ɫ��׽', 255, 255, nothing)
cv2.createTrackbar('��ֵ5', '��ɫ��׽', 0, 255, nothing)
cv2.createTrackbar('��ֵ6', '��ɫ��׽', 255, 255, nothing)

while(1):

    # Take each frame
    _, frame = cap.read()

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    thrs1 = cv2.getTrackbarPos('��ֵ1', '��ɫ��׽')
    thrs2 = cv2.getTrackbarPos('��ֵ2', '��ɫ��׽')
    thrs3 = cv2.getTrackbarPos('��ֵ3', '��ɫ��׽')
    thrs4 = cv2.getTrackbarPos('��ֵ4', '��ɫ��׽')
    thrs5 = cv2.getTrackbarPos('��ֵ5', '��ɫ��׽')
    thrs6 = cv2.getTrackbarPos('��ֵ6', '��ɫ��׽')

    # define range of blue color in HSV
    lower_blue = np.array([thrs1,thrs3,thrs5])
    upper_blue = np.array([thrs2,thrs4,thrs6])

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask)

    #cv2.imshow('frame',frame)
    #cv2.imshow('mask',mask)
    cv2.imshow('��ɫ��׽',res)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()


