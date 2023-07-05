"""
1.Adding information to your demos
2.Drawing bounding boxes around objects in case of object detection
3.Highlighting pixels with different colors for image segmentation

Once you learn to annotate images, annotating video frames will seem just as easy. 
That’s because each frame in a video is represented as an image. 
We will demonstrate here how to annotate images with geometric shapes and text.
"""

import cv2
image = cv2.imread('Resources/sample.jpg')

cv2.imshow('Original Image',image)
cv2.waitKey(0)

if image is None:
    print('Could not read image')

# 1.Draw line on image
imageLine = image.copy()
pointA = (200,80)
pointB = (450,80)
cv2.line(imageLine,pointA,pointB,(255,255,0),thickness=3,lineType=cv2.LINE_AA)
cv2.imshow('Image Line',imageLine)
cv2.waitKey(0)

# 2.Draw a Circle
imageCircle = image.copy()
circle_center = (415,190)
radius = 100
cv2.circle(imageCircle,center=circle_center, radius=radius,color=(0,0,255),thickness=3,lineType=cv2.LINE_AA)
cv2.imshow('Image Circle',imageCircle)
cv2.waitKey(0)

# 3.Draw a filled Circle
imageCircle = image.copy()
circle_center = (415,190)
radius = 100
cv2.circle(imageCircle,center=circle_center, radius=radius,color=(255,0,0),thickness=-1,lineType=cv2.LINE_AA)#thickness argument to -1
cv2.imshow('Image Circle',imageCircle)
cv2.waitKey(0)

# 4. Draw a rectangle
imageRectangle = image.copy()
start_point =(300,115)
end_point =(475,225)
cv2.rectangle(imageRectangle, start_point, end_point, (0, 0, 255), thickness= 3, lineType=cv2.LINE_8) 
cv2.imshow('imageRectangle', imageRectangle)
cv2.waitKey(0)

# 5. Draw a ellipse
imageEllipse = image.copy()
ellipse_center = (415,190)
axis1 = (100,50)
axis2 = (125,50)
# draw the ellipse
#Horizontal
cv2.ellipse(imageEllipse, ellipse_center, axis1, 0, 0, 360, (255, 0, 0), thickness=3)
#Vertical
cv2.ellipse(imageEllipse, ellipse_center, axis2, 90, 0, 360, (0, 0, 255), thickness=3)
cv2.imshow('ellipse Image',imageEllipse)
cv2.waitKey(0)

# 6. Draw half ellipse (one is transparent, another is filled)
halfEllipse = image.copy()
# define the center of half ellipse
ellipse_center = (415,190)
# define the axis point
axis1 = (100,50)
# draw the Incomplete/Open ellipse, just a outline
cv2.ellipse(halfEllipse, ellipse_center, axis1, 0, 180, 360, (255, 0, 0), thickness=3)
# if you want to draw a Filled ellipse, use this line of code
cv2.ellipse(halfEllipse, ellipse_center, axis1, 0, 0, 90, (0, 0, 255), thickness=-2)
# display the output
cv2.imshow('halfEllipse',halfEllipse)
cv2.waitKey(0)

# 7. Adding TEXT
text_image = image.copy()
text = 'I am a happy dog.'
cv2.putText(text_image,text,org=(50,350),fontFace = cv2.FONT_HERSHEY_COMPLEX,fontScale=1.5,color=(155,155,45))
cv2.imshow('Text added image',text_image)
cv2.waitKey(0)