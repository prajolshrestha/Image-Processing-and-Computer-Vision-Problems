"""
Demonstrate the use of the mouse pointer and trackbar capabilities in OpenCV.
"""
import cv2

#Annotating Images Using the Mouse

# lists to store bounding box coordinates
top_left_corner = []
bottom_right_corner = []

#  MouseCallback function which will be called on mouse input
# --> You need not specify any input arguments to the function, these will be populated automatically when the user interacts with the mouse.
# The mouse event type and event flags are recorded, along with the mouse x and y coordinates.  
def drawRectange(action,x,y,flags,*userdata):
    #Refrencing global variables
    global top_left_corner,bottom_right_corner
    #Marked the top left corner when left mouse button is pressed
    if action == cv2.EVENT_LBUTTONDOWN:
        top_left_corner = [(x,y)]
    #when left botton is released, mark bottom right corner
    elif action == cv2.EVENT_LBUTTONUP:
        bottom_right_corner = [(x,y)]
        #Draw the rectangle
        cv2.rectangle(image,top_left_corner[0],bottom_right_corner[0],(0,255,0),2,8)
        cv2.imshow('window',image)

image = cv2.imread('Resources/sample.jpg')
temp = image.copy()

cv2.namedWindow("window")
cv2.setMouseCallback("window",drawRectange) # function called when mouse is clicked
#cv2.waitKey(0)

#In the final step, we need to create a display loop that allows the user to interact with the named window.
k = 0
while k != 113:#Enter 'q' to exit
    cv2.imshow("window",image)
    k = cv2.waitKey(0)
    if (k==99):# enter 'c' to clear annotation
        image = temp.copy()
        cv2.imshow("window",image)
cv2.destroyAllWindows()