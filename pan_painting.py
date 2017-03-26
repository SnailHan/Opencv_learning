# -*- coding: cp936 -*-
'''
#��Ů��ϲ����С����Ҳϲ������ʻ�Ϳɫ��
#������ű����Ǹ���д�ģ� �������Ŷ���Ƭ��Ļ��ͼ�� �Ϳ����Ƴɼ�ʻ���
#�÷�python pan_painting.py  ���ͼƬ ���� python pan_painting.py  time.jpg
#�˽ű���windows����python 2.7+opencv3.2�汾��
#��Ҫ��ǰ��װspeechģ�飬 ��װ����pip install speech
'''
print (__doc__)
import cv2
#����cv2���moduleģ��
import numpy as np
#����numpy��������õ�ģ��
#import argparse
#�������ģ��
import sys
#import speech
#��������ģ��
def nothing(x):
    pass
#�Զ���һ��nothing��ģ�飬 �����trackbar�������õ�

#speech.say("���ڿ�ʼ")
#˵���� ����ʼ
#ap = argparse.ArgumentParser()
#ap.add_argument("-i", "--image", required=True,help="path to the input image")
#��ʾ��Ҫ����ͼƬ����ʾ
#args = vars(ap.parse_args())
#������ǻ��������ͼƬ���Ʋ���ֵ

# load the image and resize it to a smaller factor so that
# the shapes can be approximated better
im = cv2.imread(sys.argv[1])
#��ȡ�����д����ͼƬ����
kernel = np.ones((5,5),np.uint8)
#im=cv2.imread('time.jpg',0)

cv2.imshow('raw',im)
gray=cv2.cvtColor(im,6)
#��ʾ���ͼƬ
cv2.namedWindow('edge',0)
#����һ�����ֽ�edge���´��ڣ�������ʾ�ӹ����Ч��ͼ�� 0����˼�ǣ� ���ڿ�����
cv2.createTrackbar('thrs1', 'edge', 203, 255, nothing)
#����һ������thrs1�Ļ�������Ĭ��ֵ��127�� ��0-255�ķ�Χ�ڣ� �ֶ�������ֵ��Χ�� ���������nothingģ�飬��ʵ�൱��ʲô��û�������Ǹ�ʽҪ��ġ�
while(True):
#ѭ����ΪʲôҪѭ������Ϊ�ֶ�������ֵ��Ч�����ű䣬��ͣ�ص�������ͣ�ı䣬����Ҫѭ��
    thrs1 = cv2.getTrackbarPos('thrs1', 'edge')
    #print thrs1
    #��ֵthrs1����edge������thrs1��ֵ
    ret, thresh=cv2.threshold(gray,thrs1,255,cv2.THRESH_BINARY_INV)
    #
    #�ڰײ�ֵ��,��׼ȡ�Ի������ϵķ�ֵ
    #cv2.imshow('thresh',thresh)
    #��ʾ�ڰײ�ֵͼ
    edges = cv2.Canny(thresh,0,255,3)
    #����Ǳ�Եͼ���ڵף�����
    edges_INV =cv2.bitwise_not(edges)
    #ȡ���� �׵ף�����
    #erosion = cv2.erode(edges1,kernel,iterations = 1)
    #dilation = cv2.dilate(edges1,kernel,iterations = 1)
    #cv2.imwrite(sys.argv[1]+'.jpg',edges_INV)
    #д��Դ�ļ��� �滻��ԭͼ
    cv2.imshow('edge',edges_INV)

    #��ʾ��ͼ
    cv2.waitKey(50)
#cv2.imshow('erosion',erosion)
#cv2.imshow('dilation',dilation)
#speech.say("ת������")
#������ʾ�� ��ʾ�������
#cv2.waitKey(0)
#��������˳�

