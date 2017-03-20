# -*- coding: cp936 -*-
#��Ů��ϲ����С����Ҳϲ������ʻ�Ϳɫ��
#������ű����Ǹ���д�ģ� �������Ŷ���Ƭ��Ļ��ͼ�� �Ϳ����Ƴɼ�ʻ���
import cv2
import numpy as np
kernel = np.ones((5,5),np.uint8)
im=cv2.imread('time.jpg',0)

cv2.imshow('1',im)
ret, thresh=cv2.threshold(im,150,255,cv2.THRESH_BINARY_INV)
cv2.imshow('thresh',thresh)
edges = cv2.Canny(im,0,255,3)
edges_INV =cv2.bitwise_not(edges)
#erosion = cv2.erode(edges1,kernel,iterations = 1)
#dilation = cv2.dilate(edges1,kernel,iterations = 1)
cv2.imshow('2',edges_INV)
#cv2.imshow('erosion',erosion)
#cv2.imshow('dilation',dilation)
cv2.waitKey(0)

