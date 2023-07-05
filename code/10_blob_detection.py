"""
Q.What is a Blob?
=> A Blob is a group of connected pixels in an image that share some common property ( E.g, grayscale value ). 
   e.g.In the image, the dark connected regions are blobs, and blob detection aims to identify and mark these regions.

Q.How Does Blob Detection Work?
=> 1.Thresholding : Convert the source images to several binary images by thresholding the source image with thresholds starting at minThreshold. 
     These thresholds are incremented  by thresholdStep until maxThreshold. 
     So the first threshold is minThreshold, the second is minThreshold + thresholdStep, the third is minThreshold + 2 x thresholdStep, and so on.
   2.Grouping : In each binary image,  connected white pixels are grouped.  Let’s call these binary blobs.
   3.Merging  : The centers of the binary blobs in the binary images are computed, and blobs located closer than minDistBetweenBlobs are merged.
   4.Center & Radius Calculation:  The centers and radii of the newly merged blobs are computed and returned.
"""
import cv2
import numpy as np

im = cv2.imread('Resources/blob.jpg',cv2.IMREAD_GRAYSCALE)

# #setup detector with default parameters
# detector = cv2.SimpleBlobDetector()

#setup the detector with parameters
params = cv2.SimpleBlobDetector_Params()
#change threshold
params.minThreshold = 10
params.maxThreshold = 200
# Filter by area
params.filterByArea = True
params.minArea = 1500
# Filter by circularity
params.filterByCircularity = True
params.minCircularity = 0.1
# Filter by Convexity
params.filterByConvexity = True
params.minConvexity = 0.87
#Filter by inertia
params.filterByInertia = True
params.minInertiaRatio =0.1

detector = cv2.SimpleBlobDetector_create(params)

#Detect blobs 
keypoints = detector.detect(im)

#Draw red circle  around detected blobs(keypoints)
img_with_keypoints = cv2.drawKeypoints(im,keypoints,np.array([]),(0,0,255),cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

cv2.imshow('Detected blobs',img_with_keypoints)
cv2.waitKey(0)