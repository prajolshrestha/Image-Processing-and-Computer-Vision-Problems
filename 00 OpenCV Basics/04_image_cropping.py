"""
There is no specific function for cropping using OpenCV, 
NumPy array slicing is what does the job. 
Every image that is read in, gets stored in a 2D array (for each color channel). 
Simply specify the height and width (in pixels) of the area to be cropped. 
And it’s done!
"""

import cv2

image = cv2.imread('Resources/test.jpg')
cv2.imshow('Original image',image)
print(image.shape)

# CROP
cropped_image = image[80:280, 150:330]
cv2.imshow('Corpped image',cropped_image)
cv2.imwrite('Resources/croped_img.jpg',cropped_image)

# Dividing an Image into small patches Using Cropping
image_copy = image.copy()
imgheight = image.shape[0]
imgwidth = image.shape[1]

# patches with a height and width of 76 pixels and 104 pixels
M = 76
N = 104
x1 = 0
y1 = 0
 
for y in range(0, imgheight, M):
    for x in range(0, imgwidth, N):
        if (imgheight - y) < M or (imgwidth - x) < N:
            break
             
        y1 = y + M
        x1 = x + N
 
        # check whether the patch width or height exceeds the image width or height
        if x1 >= imgwidth and y1 >= imgheight:
            x1 = imgwidth - 1
            y1 = imgheight - 1
            #Crop into patches of size MxN
            tiles = image_copy[y:y+M, x:x+N]
            #Save each patch into file directory
            cv2.imwrite('Resources/saved_patches/'+'tile'+str(x)+'_'+str(y)+'.jpg', tiles)
            cv2.rectangle(image, (x, y), (x1, y1), (0, 255, 0), 1)
        elif y1 >= imgheight: # when patch height exceeds the image height
            y1 = imgheight - 1
            #Crop into patches of size MxN
            tiles = image_copy[y:y+M, x:x+N]
            #Save each patch into file directory
            cv2.imwrite('Resources/saved_patches/'+'tile'+str(x)+'_'+str(y)+'.jpg', tiles)
            cv2.rectangle(image, (x, y), (x1, y1), (0, 255, 0), 1)
        elif x1 >= imgwidth: # when patch width exceeds the image width
            x1 = imgwidth - 1
            #Crop into patches of size MxN
            tiles = image_copy[y:y+M, x:x+N]
            #Save each patch into file directory
            cv2.imwrite('Resources/saved_patches/'+'tile'+str(x)+'_'+str(y)+'.jpg', tiles)
            cv2.rectangle(image, (x, y), (x1, y1), (0, 255, 0), 1)
        else:
            #Crop into patches of size MxN
            tiles = image_copy[y:y+M, x:x+N]
            #Save each patch into file directory
            cv2.imwrite('Resources/saved_patches/'+'tile'+str(x)+'_'+str(y)+'.jpg', tiles)
            cv2.rectangle(image, (x, y), (x1, y1), (0, 255, 0), 1)


#Save full image into file directory
cv2.imshow("Patched Image",image)
cv2.imwrite("Resources/patched.jpg",image)

cv2.waitKey(0)
cv2.destroyAllWindows()


"""
Some Interesting Applications using Cropping
1. You can use cropping to extract a region of interest from an image and discard the other parts you do not need to use.
2. You can extract patches from an image to train a patch-based neural network.
"""