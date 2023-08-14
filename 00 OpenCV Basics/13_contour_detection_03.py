#CHAIN_APPROX_SIMPLE algorithm.

import cv2

image = cv2.imread('Resources/image_2.jpg')#image read
image_gray1 = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)#gray
ret,thresh1 = cv2.threshold(image_gray1,150,255,type=cv2.THRESH_BINARY)#threshold

contours2, hierarchy = cv2.findContours(thresh1,mode=cv2.RETR_TREE,method=cv2.CHAIN_APPROX_SIMPLE)
image_copy_2 = image.copy()
cv2.drawContours(image_copy_2,contours2,contourIdx=-1,color=(0,255,0),thickness=2,lineType=cv2.LINE_AA)
cv2.imshow('SIMPLE approx contours',image_copy_2)
cv2.waitKey(0)

"""
1.The first for loop cycles over each contour area present in the contours list. 
2.The second loops over each of the coordinates in that area.
3.We then draw a green circle on each coordinate point, using the circle() function from OpenCV.
"""

image_copy_3 = image.copy()
for i, contour in enumerate(contours2): #loop over one contour area
    for j, contour_point in enumerate(contour): #loop over the points
        #Draw a circle on the current contour coordinates
        cv2.circle(image_copy_3,((contour_point[0][0],contour_point[0][1])),2,(0,255,0),thickness=2,lineType=cv2.LINE_AA)

cv2.imshow('CHAIN approx simple point only',image_copy_3)
cv2.waitKey(0)       

"""
OBSERVATION: Observe that there are only four contour dots on the four corners of the book when using CHAIN_APPROX_SIMPLE for contour detection. 
             The vertical and horizontal straight lines of the book are completely ignored.
"""
####################################################################################################################
"""
Let’s now understand the contour hierarchy output in detail.

The contour hierarchy is represented as an array, which in turn contains arrays of four values. 
It is represented as:

[Next, Previous, First_Child, Parent] 
-Next: Denotes the next contour in an image, which is at the same hierarchical level.
-Previous: Denotes the previous contour at the same hierarchical level. This means that contour 1 will always have its Previous value as -1.
-First_Child: Denotes the first child contour of the contour we are currently considering
-Parent: Denotes the parent contour’s index position for the current contour.

The above explanations make sense, but how do we actually visualize these hierarchy arrays? The best way is to:

-Use a simple image with lines and shapes like the previous image
-Detect the contours and hierarchies, using different retrieval modes 
   = RETR_TREE - parent child relationship
   = RETR_LIST - does not create any parent child relationship
   = RETR_EXTERNAL -  It only detects the parent contours, and ignores any child contours
   = RETR_CCOMP. - All the outer contours will have hierarchy level 1
                   All the inner contours will have hierarchy level 2
-Then print the values to visualize them
"""
image2 = cv2.imread('Resources/image_2.jpg')
img_gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
ret, thresh2 = cv2.threshold(img_gray2, 150, 255, cv2.THRESH_BINARY)
contours3, hierarchy3 = cv2.findContours(thresh2, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)#RETR_LIST (Fastest method)
image_copy4 = image2.copy()
cv2.drawContours(image_copy4, contours3, -1, (0, 255, 0), 2, cv2.LINE_AA)
# see the results
cv2.imshow('LIST', image_copy4)
print(f"LIST: {hierarchy3}")
cv2.waitKey(0) 
cv2.destroyAllWindows()