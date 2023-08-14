import cv2
import numpy as np

image = cv2.imread('Resources/test.jpg')
cv2.imshow('Original Image',image)

if image is None:
    print('Error while reading an image')

# 1.Applying kernel identity : What makes an identity matrix special is that multiplying it with any other matrix will return the original matrix
kernel1 = np.array([[0,0,0],
                    [0,1,0],
                    [0,0,0]])

identity = cv2.filter2D(src=image,ddepth=-1,kernel=kernel1)
cv2.imshow('Identity',identity)
cv2.waitKey(0)


# 2.1.Applying blurring kernel
kernel2 = np.ones((5,5),np.float32) / 25
img = cv2.filter2D(src=image,ddepth=-1,kernel=kernel2)
cv2.imshow('Blur kernel',img)
cv2.waitKey(0)

# 2.2. built-in blur() function (same as 2. blurring kernel)
img_blur = cv2.blur(src=image,ksize=(5,5))
cv2.imshow('Blur built-in',img)
cv2.waitKey(0)

# 3. Apply gaussian blur
gauss_blur = cv2.GaussianBlur(src=image,ksize=(5,5),sigmaX=0,sigmaY=0)
cv2.imshow('Gaussian Blur',gauss_blur)
cv2.waitKey(0)

# 4. Apply Median Blur
mid_blur = cv2.medianBlur(src=image,ksize=5)
cv2.imshow('Median Blur',img)
cv2.waitKey(0)

# 5. Sharpening image using filter2D()
kernel3 = np.array([[0,-1,0],
                    [-1,5,-1],
                    [0,-1,0]])
sharp_img = cv2.filter2D(src=image,ddepth=-1,kernel=kernel3)
cv2.imshow('Sharp image',sharp_img)
cv2.waitKey(0)

# 6. Apply Bilateral Filtering - Blur but preserve edges.
"""
While blurring can be an effective way to reduce noise in an image, 
it is often not desirable to blur the entire image, 
as important details and sharp edges may be lost. 
In such cases, bilateral filtering can make your life easier.

a.]This technique applies the filter selectively to blur similar intensity pixels in a neighborhood. 
Sharp edges are preserved, wherever possible.
b.]It lets you control not only the spatial size of the filter, 
but also the degree to which the neighboring pixels are included in the filtered output. 
This is done, based on variation in their color intensity, and also distance from the filtered pixel.

Thus,

+pixels that are similar and near the filtered pixel will have influence
+pixels that are far away from the filtered pixel will have little influence (due to the spatial Gaussian)
+pixels that have dissimilar intensities will have little influence (due to the color-intensity Gaussian), 
 even if they are close to the center of the kernel.

- Computationally expensive.
"""
bilateral_filt_img = cv2.bilateralFilter(src=image,d=9,sigmaColor=75,sigmaSpace=75)#filtered image is a product of its spatial and intensity weight.
cv2.imshow('Bilateral filtered',bilateral_filt_img)
cv2.waitKey(0)