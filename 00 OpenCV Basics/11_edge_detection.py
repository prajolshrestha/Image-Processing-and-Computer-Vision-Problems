"""
Edge detection is an image-processing technique that is used to identify the boundaries (edges) of objects or regions within an image.

Q.How are Edges Detected?
==> Sudden changes in pixel intensity characterize edges. We need to look for such changes in the neighboring pixels to detect edges.
"""
import cv2

image = cv2.imread('Resources/Lenna.png')
cv2.imshow('original image', image)
cv2.waitKey(0)

# Gray and blur image
img_gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
img_blur = cv2.GaussianBlur(img_gray,(3,3),0)

# Sobel edge detection
sobelx = cv2.Sobel(src=img_blur,ddepth=cv2.CV_64F,dx=1,dy=0,ksize=5) # 1st derivative Sobel image in the x-direction (sharp vertical edges)
sobely = cv2.Sobel(src=img_blur,ddepth=cv2.CV_64F,dx=0,dy=1,ksize=5) # detects sharp horizontal edges
sobelxy = cv2.Sobel(src=img_blur,ddepth=cv2.CV_64F,dx=1,dy=1,ksize=5) # 1st derivative Sobel image in both directions

# Canny edge detection
"""
Four-stage process:
1.Noise Reduction 
  - Gaussian blur
2.Calculating the Intensity Gradient of the Image 
  - Filtered with a Sobel kernel, both horizontally and vertically. ==>  gradient direction is then rounded to the nearest 45-degree angle
3.Suppression of False Edges 
  - non-maximum suppression of edges to filter out unwanted pixels (which may not actually constitute an edge). 
    To accomplish this, each pixel is compared to its neighboring pixels in the positive and negative gradient direction. 
    If the gradient magnitude of the current pixel is greater than its neighboring pixels, it is left unchanged. 
    Otherwise, the magnitude of the current pixel is set to zero.
4.Hysteresis Thresholding 
  - gradient magnitudes are compared with two threshold values, one smaller than the other. 
    Gradient mag. value 
          -higher than max. threshold is (strong edge) preserved.
          -betn min. and max threshold are weak edge.
"""
edges = cv2.Canny(image=img_blur, threshold1=100, threshold2=200)



# Display
cv2.imshow('Sobel X',sobelx)
cv2.waitKey(0)
cv2.imshow('Sobel y',sobely)
cv2.waitKey(0)
cv2.imshow('Sobel XY',sobelxy)
cv2.waitKey(0)

cv2.imshow('Canny Edge Detection',edges)
cv2.waitKey(0)

cv2.destroyAllWindows()



