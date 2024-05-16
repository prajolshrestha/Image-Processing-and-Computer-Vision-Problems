import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

# Read Image
img = cv.imread('touching_coins.jpg')
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
assert gray_img is not None, "Unable to read the image"

# 1. Outsu's binary Thresholding 
ret, thresh = cv.threshold(gray_img, 0, 255, cv.THRESH_BINARY_INV+cv.THRESH_OTSU)

# 2. noise removal using Opening (Erosion + Dilation)
kernel = np.ones((3,3), np.uint8)
opening = cv.morphologyEx(thresh, cv.MORPH_OPEN, kernel, iterations = 2)

# 3. Sure background area
sure_bg = cv.dilate(opening, kernel, iterations=3)

# 4. Sure Foreground area 
dist_transform = cv.distanceTransform(opening, cv.DIST_L2, 5)
ret, sure_fg = cv.threshold(dist_transform, 0.7*dist_transform.max(), 255, 0)
sure_fg = np.uint8(sure_fg)

# 5. unknown area
unknown = cv.subtract(sure_bg, sure_fg)

# 6. Marker labelling 
ret, markers = cv.connectedComponents(sure_fg)

# Add 1 to all labels so that sure background is not 0, but 1
markers = markers + 1

# Mark the region of unknown with zero
markers[unknown==255] = 0


# 7. Watershed algo
markers = cv.watershed(image=img, markers=markers)
img[markers == -1] = [255,0,0]


# Visualize
plt.figure(figsize=(10,8))
plots = [(gray_img, "Gray Image"),
         (thresh, "Binary Image"),
         (opening, "Opening"),
         (sure_bg, "Sure Background"),
         (dist_transform, "Distance Transform"),
         (sure_fg, "Sure Foreground"),
         (unknown, "Unknown area"),
         (markers, "markers"),
         (img, "segmentation result")

         ]

for i, (img, title) in enumerate(plots, 1):
    plt.subplot(3,3,i)
    cmap = 'gray'
    if i == 8:
        cmap= 'jet'
    plt.imshow(img, cmap=cmap)
    plt.title(title)
    plt.axis('off')

plt.suptitle("Image segmentation with marker-based watershed algorithm")
plt.show()