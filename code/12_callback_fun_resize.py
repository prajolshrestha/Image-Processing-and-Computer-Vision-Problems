import cv2

maxScaleUp = 100
scaleFactor = 1
windowName = "Resize Image"
trackbarValue = "Scale"

# read image
image = cv2.imread('Resources/sample.jpg')

#create window to display results
cv2.namedWindow(windowName,cv2.WINDOW_AUTOSIZE)

# Callback functions
def scaleImage(*args):
    #Get the scale factor from the trackbar
    scaleFactor = 1 + args[0]/100.0 # retrieve the trackbar position from args[0], on a scale of 0 to 100.  
    #Resize the image
    scaledImage = cv2.resize(image,None,fx=scaleFactor,fy=scaleFactor,interpolation=cv2.INTER_LINEAR)
    cv2.imshow(windowName,scaledImage)

#create trackbar and associate a callback function
cv2.createTrackbar(trackbarValue,windowName,scaleFactor,maxScaleUp,scaleImage)

cv2.imshow(windowName,image)
c = cv2.waitKey(0)
cv2.destroyAllWindows()