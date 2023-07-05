"""
we will learn how to:

1. Rotate an image
2. Translate or shift the image content
"""

import cv2
import numpy as np

image = cv2.imread('Resources/Lenna.png')
height, width = image.shape[:2]
center = (width/2,height/2) #center coordinates

#### ROTATION 
rotate_matrix = cv2.getRotationMatrix2D(center=center,angle = 45, scale=1) #Rotation Matrix
rotated_image = cv2.warpAffine(src=image, M=rotate_matrix,dsize=(width,height))

cv2.imshow('Original image', image)
cv2.imshow('Roatated image',rotated_image)
cv2.imwrite('Resources/rotated_image.jpg',rotated_image)

#### Translate / shift
"""while shifting the image by tx and ty values.

1. Providing positive values for tx will shift the image to right and negative values will shift the image to the left.
2. Similarly, positive values of ty will shift the image down while negative values will shift the image up.
"""
tx ,ty = width/4, height/4
translate_matrix = np.array([[1,0,tx],
                             [0,1,ty]],dtype=np.float32) #Translation Matrix
translated_image = cv2.warpAffine(src=image,M =translate_matrix,dsize=(width,height))

cv2.imshow('Translated image',translated_image)
cv2.imwrite('Resources/translated_image.jpg',translated_image)

cv2.waitKey(0)
cv2.destroyAllWindows()