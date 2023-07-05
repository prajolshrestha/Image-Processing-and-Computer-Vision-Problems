import cv2

# Read image ==> cv2.imread(filename, flags)
img_grayscale = cv2.imread('Resources/Lenna.png',0)  #cv2.IMREAD_UNCHANGED  or -1
img_color = cv2.imread('Resources/Leena.png',1)      #cv2.IMREAD_COLOR  or 1   #OpenCV reads color images in BGR format                                         # cv2.IMREAD_GRAYSCALE  or 0
img_unchanged = cv2.imread('Resources/Leena.png',-1)  #cv2.IMREAD_UNCHANGED  or -1                                         

# Display image ==> cv2.imshow(window_name, image)
cv2.imshow('grayscale image',img_grayscale)

cv2.waitKey(0)# wait for a key press
cv2.destroyAllWindows() #destroys all windows

# Write an Image
cv2.imwrite('Resources/grayscale.jpg',img_grayscale)


"""
Summary
Here, you learned to use the: 

imread(), imshow() and imwrite() functions to read, display, and write images 
waitKey() and destroyAllWindows() functions, along with the display function to 
close the image window on key press
and clear any open image window from the memory.
"""