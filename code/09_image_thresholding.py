import cv2
import numpy as np

src = cv2.imread('Resources/threshold.png',cv2.IMREAD_GRAYSCALE)
cv2.imshow('Original image',src)
cv2.waitKey(0)

#1. Binary thresholding (thresh_binary)
"""
If src(x,y) > thresh, then dst(x,y)= maxValue
"""
th,dst = cv2.threshold(src,thresh=0,maxval=255,type=cv2.THRESH_BINARY)
cv2.imshow('thresh binary',dst)
cv2.waitKey(0)

#2. Binary_inv
th, dst = cv2.threshold(src,127,255,cv2.THRESH_BINARY_INV)
cv2.imshow('thresh binary_inv',dst)
cv2.waitKey(0)

#3. THRESH_TRUNC
"""
+If src > thresh, then des = thresh
+else, des=src
+MaxValue is ignored.
"""
th,dst = cv2.threshold(src,127,255,cv2.THRESH_TRUNC)
cv2.imshow('thresh_trunc',dst)
cv2.waitKey(0)

#4. TRUNC_TO_ZERO
"""
+If src > thresh, then des = src
+else, des = 0
+The maxValue is ignored
"""
th, dst = cv2.threshold(src,127,255,cv2.THRESH_TOZERO)
cv2.imshow('thresh_tozero',dst)
cv2.waitKey(0)

#5. TRUNC_TO_ZERO_INV
"""
+If src > thresh, then des = 0
+else, des = src
+The maxValue is ignored

-artifacts
"""
th,dst = cv2.threshold(src,127,255,cv2.THRESH_TOZERO_INV)
cv2.imshow('thresh_tozero_inv',dst)
cv2.waitKey(0)