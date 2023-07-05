"""
Popular colorspaces used in Computer Vision and use it for color based segmentation.

-Different colours might look similar in some lightning condition. It makes color based segmentation difficult.

-The inherent problems associated with the RGB Color space:
1.significant perceptual non-uniformity.
2.mixing of chrominance ( Color related information ) and luminance ( Intensity related information ) data.

*Images will get loaded in BGR format by default. 
+We can convert between different colorspaces using the OpenCV function cvtColor().



"""
import cv2

# RGB Color-space
bright = cv2.imread('Resources/cube_images/rub00.jpg')# loaded in BGR format by default
dark = cv2.imread('Resources/cube_images/rub09.jpg')
cv2.imshow('bright',bright)
cv2.imshow('dark',dark)
cv2.waitKey(0)

#LAB Color-space
"""
It has the following properties.

Perceptually uniform color space which approximates how we perceive color.
Independent of device ( capturing or displaying ).
Used extensively in Adobe Photoshop.
Is related to the RGB color space by a complex transformation equation.
"""
brightLAB = cv2.cvtColor(bright, cv2.COLOR_BGR2LAB)
darkLAB = cv2.cvtColor(dark, cv2.COLOR_BGR2LAB)
cv2.imshow('bright',brightLAB)
cv2.imshow('dark',darkLAB)
cv2.waitKey(0)

# YCrCb color-space
brightYCB = cv2.cvtColor(bright, cv2.COLOR_BGR2YCrCb)
darkYCB = cv2.cvtColor(dark, cv2.COLOR_BGR2YCrCb)
cv2.imshow('bright',brightYCB)
cv2.imshow('dark',darkYCB)
cv2.waitKey(0)

# HSV color space
"""
The HSV color space has the following three components

H – Hue ( Dominant Wavelength ).
S – Saturation ( Purity / shades of the color ).
V – Value ( Intensity ).

Best thing is that it uses only one channel to describe color (H), making it very intuitive to specify color.
"""
brightHSV = cv2.cvtColor(bright, cv2.COLOR_BGR2HSV)
darkHSV = cv2.cvtColor(dark, cv2.COLOR_BGR2HSV)
cv2.imshow('bright',brightHSV)
cv2.imshow('dark',darkHSV)
cv2.waitKey(0)