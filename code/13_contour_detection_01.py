"""
Q. What are Contours?
==> a specific contour refers to boundary pixels that have the same color and intensity.

Using contour detection, we can detect the borders of objects, and localize them easily in an image. 
It is often the first step for many interesting applications, 
such as image-foreground extraction, simple-image segmentation, detection and recognition. 
- Motion Detection
- Object Detection
- Background/Foreground Segmentation

~Steps for Detecting and Drawing Contours in OpenCV
1. Read image and convert to grayscale 
2. Apply binary thresholding ==> object of interest is highlighted ie, becomes white. and background becomes black.
3. findContours()
4. drawContours()

"""
import cv2

image = cv2.imread('Resources/image_1.jpg')

#Method 1: cv2.CHAIN_APPROX_NONE
#1.Gray
img_gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
#2.Binary threshold
ret,thresh = cv2.threshold(img_gray,150,255,cv2.THRESH_BINARY)
#3.find contours
contours, hierarchy = cv2.findContours(thresh,mode=cv2.RETR_TREE,method=cv2.CHAIN_APPROX_NONE)
#4.draw contours
image_copy1 = image.copy()
cv2.drawContours(image_copy1,contours,contourIdx=-1,color=(0,255,0),thickness=2,lineType=cv2.LINE_AA)

#Method 2: cv2.CHAIN_APPROX_SIMPLE
"""
The CHAIN_APPROX_SIMPLE  algorithm compresses horizontal, vertical, and diagonal segments along the contour and leaves only their end points. 
This means that any of the points along the straight paths will be dismissed, and we will be left with only the end points. 
For example, consider a contour, along a rectangle. All the contour points, except the four corner points will be dismissed. 
This method is faster than the CHAIN_APPROX_NONE because the algorithm does not store all the points, uses less memory, 
and therefore, takes less time to execute.
"""
#1.Gray
img_gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
#2.Binary threshold
ret,thresh = cv2.threshold(img_gray,150,255,cv2.THRESH_BINARY)
#3.find contours
contours, hierarchy = cv2.findContours(thresh,mode=cv2.RETR_TREE,method=cv2.CHAIN_APPROX_SIMPLE)
#4.draw contours
image_copy2 = image.copy()
cv2.drawContours(image_copy2,contours,contourIdx=-1,color=(0,255,0),thickness=2,lineType=cv2.LINE_AA)




cv2.imshow('Original Image',image)
cv2.waitKey(0)
cv2.imshow('Image with contours (None approx)',image_copy1)
cv2.waitKey(0)
cv2.imshow('Image with contours (Simple approx)',image_copy2)
cv2.waitKey(0)