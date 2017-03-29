# -*- coding: cp936 -*-
#���ģ��㶮��
#!/usr/bin/python
'''
���ڼ��У� �������磬 ��������ط羰��ʤ��Ӱ
�÷�����
#�÷�python pan_painting.py  ���ͼƬ ���� python pan_painting.py  time.jpg
#�˽ű���windows����python 2.7+opencv3.2�汾�ģ� ���ü����������
https://github.com/wjb711/Opencv_learning/blob/master/windows_python2.7_opencv3.2%E5%AE%89%E8%A3%85%E9%85%8D%E7%BD%AE%E6%8C%87%E5%AF%BC.txt
#��Ҫ��ǰ��װspeechģ�飬 ��װ����pip install speech
����ʾ���´���
no module named win32com.client������
�����ض�Ӧpywin32���
https://sourceforge.net/projects/pywin32/files/pywin32/
����������΢��tts
http://www.microsoft.com/en-us/download/confirmation.aspx?id=27224
'''


import cv2
import numpy as np
import time
import sys
#import win32com
#import speech

#��������ģ��
def nothing(x):
    pass


print(__doc__)
#��ʾǰ����ɫ������������
print ('��ǰopencv�汾Ϊ'+cv2.__version__)
#��ʾopencv�汾
print ('���python�汾��ϢΪ')
print (sys.version_info)
#speech.say("�Ƽ�ʹ��720p��1080p��������ͷ")

cv2.namedWindow('mix',0)

cap=cv2.VideoCapture(0)
try:
        
    ret = cap.set(3,1280)
    ret = cap.set(3,960)
    y1=1280
    x1=960

except:
    ret = cap.set(3,640)
    ret = cap.set(3,480)
    y1=640
    x1=480
try:
    fn = sys.argv[1]
    #���Ի������ĵ�һ�������� Ҳ����ͼƬ������
except:
    fn = 'images/lufugong.jpg'
    print fn
    #����Ҳ�������ָ����ͼƬ���ƣ� Ĭ������Ϊlufugong.jpg
#������1280x960������ͷ�� ���ʧ�ܣ� ʹ��Ĭ�ϵ�640x480
print ('ʵ�ʷֱ���Ϊ')
print cap.get(3)
print cap.get(4)
#ret = cap.set(3,1280)
#ret = cap.set(4,720)
c=1
d=0
im = cv2.imread(fn)

im_white= cv2.imread('images/white.jpg')
im = cv2.imread(fn)
cv2.namedWindow('��ɫ��׽',0)
cv2.createTrackbar('ɫ�����', '��ɫ��׽', 0, 180, nothing)
cv2.createTrackbar('ɫ�����', '��ɫ��׽', 180, 180, nothing)
cv2.createTrackbar('�������', '��ɫ��׽', 0, 255, nothing)
cv2.createTrackbar('�������', '��ɫ��׽', 255, 255, nothing)
cv2.createTrackbar('�������', '��ɫ��׽', 0, 255, nothing)
cv2.createTrackbar('�������', '��ɫ��׽', 255, 255, nothing)

while (True):

    ret,frame=cap.read()
        
    cv2.imshow('ԭͼ',frame)
    #ԭͼ
    gray = cv2.cvtColor(frame, 6)
    cv2.imshow('ԭͼ�Ҷ�',gray)
    #�Ҷ�ͼ
    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    thrs1 = cv2.getTrackbarPos('ɫ�����', '��ɫ��׽')
    thrs2 = cv2.getTrackbarPos('ɫ�����', '��ɫ��׽')
    thrs3 = cv2.getTrackbarPos('�������', '��ɫ��׽')
    thrs4 = cv2.getTrackbarPos('�������', '��ɫ��׽')
    thrs5 = cv2.getTrackbarPos('�������', '��ɫ��׽')
    thrs6 = cv2.getTrackbarPos('�������', '��ɫ��׽')

    # define range of blue color in HSV
    lower_blue = np.array([thrs1,thrs3,thrs5])
    upper_blue = np.array([thrs2,thrs4,thrs6])

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    cv2.imshow('Video_mask',mask)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_not(frame,frame, mask= mask)
    cv2.imshow('��ɫ��׽',res)

############################################################
    

    if cv2.waitKey(10)==ord('9'):

        d=c+10

        print 'key 9 press'

        #cv2.waitKey(3000)

        #timestr = time.strftime("%Y%m%d-%H%M%S")

        #cv2.waitKey(5000)

        #ret,frame=cap.read()

        #cv2.imshow('222',frame)

        #cv2.imwrite('images\pic'+timestr+'.jpg',frame)

        #cv2.imshow('111',frame)

        #cv2.waitKey(3000)

        #cv2.destroyWindow('111')

    #if c==d:

        #timestr = time.strftime("%Y%m%d-%H%M%S")

        #cv2.imwrite('images\pic'+timestr+'.jpg',frame)

    #    im=frame

    #    cv2.imshow('111',frame)

    #    cv2.waitKey(1000)

    #    cv2.destroyWindow('111')

 


    a,thresh=cv2.threshold(gray,135,255,cv2.THRESH_BINARY)
    cv2.imshow('��ֵͼ',thresh)
    #��ֵͼ
    thresh_INV=cv2.bitwise_not(thresh)
     
    cv2.imshow('��ֵͼȡ��',thresh_INV)
    #��ֵͼȡ��
    dst1=cv2.add(frame,frame,mask=thresh_INV)
    #dst1=cv2.add(frame,frame,mask=mask)
    cv2.imshow('ԭͼ+��ֵȡ��',dst1)
    dst2=cv2.add(frame,frame,mask=thresh)
    cv2.imshow('ԭͼ+��ֵ',dst2)
    #im_dst1=cv2.bitwise_and(im,im,mask=thresh)

    im_dst1=cv2.add(im,im,mask=thresh)

    mixed_clone =cv2.add(im_dst1,dst1)

    #cv2.imshow('mix',mixed_clone)
    cv2.imshow('����',mixed_clone)
    if cv2.waitKey(1)==ord('0'):

        d=c+20

        print 'key 0 press'

    if c==d:

        timestr = time.strftime("%Y%m%d-%H%M%S")

        cv2.imwrite('images\pic'+timestr+'.jpg',mixed_clone)

        cv2.imshow('photo',mixed_clone)

        cv2.waitKey(2000)

        cv2.destroyWindow('photo')

    c=c+1

    print c
