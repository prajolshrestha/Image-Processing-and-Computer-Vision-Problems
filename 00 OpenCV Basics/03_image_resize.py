"""
When resizing an image:

1.It is important to keep in mind the original aspect ratio of the image (i.e. width by height), 
  if you want to maintain the same in the resized image too.
2.Reducing the size of an image will require resampling of the pixels. 
3.Increasing the size of an image requires reconstruction of the image. 
  This means you need to interpolate new pixels.
"""

import cv2

# Original Image
image = cv2.imread('Resources/Lenna.png')
cv2.imshow('Original Image',image)
h,w,c = image.shape #Height, width and number of channels.
print('Original Height is %s  and width is %s.And, No. of channels: %s' %(h,w,c))

# Downscale image
down_width = 300
down_height = 200
down_points = (down_width,down_height)
resized_down_image = cv2.resize(image,down_points,interpolation=cv2.INTER_LINEAR)
cv2.imshow('Downsized image', resized_down_image)

# Upscale image
up_width = 600
up_height = 400
up_points = (up_width,up_height)
resized_up_image = cv2.resize(image,up_points,interpolation=cv2.INTER_LINEAR)
cv2.imshow('Upsized image', resized_up_image)

# RESIZE with scaling factor
scale_up_x = 1.2
scale_up_y = 1.2

scale_down = 0.6

scaled_f_down = cv2.resize(image, None,fx = scale_down,fy = scale_down,interpolation=cv2.INTER_LINEAR)
scaled_f_up = cv2.resize(image, None,fx = scale_up_x,fy = scale_up_y,interpolation=cv2.INTER_LINEAR)
cv2.imshow('Upscaled image',scaled_f_up)
cv2.imshow('Downscaled image',scaled_f_down)



cv2.waitKey()
cv2.destroyAllWindows()