# -*- coding: cp936 -*-
'''
#��Ů��ϲ����С����Ҳϲ������ʻ�Ϳɫ��
#������ű����Ǹ���д�ģ� �������Ŷ���Ƭ��Ļ��ͼ�� �Ϳ����Ƴɼ�ʻ���
#�÷�python pan_painting.py -i ���ͼƬ ���� python pan_painting.py -y time.jpg
#�˽ű���windows����python 2.7+opencv3.2�汾��
#��Ҫ��ǰ��װspeechģ�飬 ��װ����pip install speech
'''
print (__doc__)
import cv2
#����cv2���moduleģ��
import numpy as np
#����numpy��������õ�ģ��
import argparse
#�������ģ��
import speech
#��������ģ��
speech.say("���ڿ�ʼ")
#˵���� ����ʼ
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="path to the input image")
#��ʾ��Ҫ����ͼƬ����ʾ
args = vars(ap.parse_args())
#������ǻ��������ͼƬ���Ʋ���ֵ

# load the image and resize it to a smaller factor so that
# the shapes can be approximated better
im = cv2.imread(args["image"])
#��ȡ�����д����ͼƬ����
kernel = np.ones((5,5),np.uint8)
#im=cv2.imread('time.jpg',0)

cv2.imshow('1',im)
#��ʾ���ͼƬ
ret, thresh=cv2.threshold(im,150,255,cv2.THRESH_BINARY_INV)
#�ڰײ�ֵ��
cv2.imshow('thresh',thresh)
#��ʾ�ڰײ�ֵͼ
edges = cv2.Canny(im,0,255,3)
#����Ǳ�Եͼ���ڵף�����
edges_INV =cv2.bitwise_not(edges)
#ȡ���� �׵ף�����
#erosion = cv2.erode(edges1,kernel,iterations = 1)
#dilation = cv2.dilate(edges1,kernel,iterations = 1)
cv2.imwrite(args["image"],edges_INV)
#д��Դ�ļ��� �滻��ԭͼ
cv2.imshow('2',edges_INV)

#��ʾ��ͼ
#cv2.imshow('erosion',erosion)
#cv2.imshow('dilation',dilation)
speech.say("ת������")
#������ʾ�� ��ʾ�������
cv2.waitKey(0)
#��������˳�

