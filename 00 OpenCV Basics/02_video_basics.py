import cv2

########## READ VIDEO FROM FILE / Image Sequence / WEB CAM
# Create a video capture object 
#vid_capture = cv2.VideoCapture('Resources/Cars.mp4') #video capture object
#vid_capture = cv2.VideoCapture('Resources/Image_sequence/Cars%04d.jpg') #%04d indicates a four-digit sequence
vid_capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)  #CAP_DSHOW =  is short for direct show via video input. (its optional)


# Conform video file is opened # retrive desired metadata
if(vid_capture.isOpened() == False):#conform video file was opened
    print('Error opening the video file')

else:
    fps = vid_capture.get(5) #Frame rate info (5 = CAP_PROP_FPS)
    print('Frames per second:',fps,'FPS')
    frame_count = vid_capture.get(7) #Frame count (7 = CAP_PROP_FRAME_COUNT)
    print('Frame Count:', frame_count)


# MAIN LOOP
while(vid_capture.isOpened()):
    ret, frame = vid_capture.read()   # vCapture.read() methods returns a tuple, first element is a bool 
                                      # and the second is frame
    if ret == True:
        cv2.imshow('Frame',frame)

        k = cv2.waitKey(20)
        if k == 113: # 113 is ASCII code for q key
            break
    else:
        break

# Release the objects
vid_capture.release()
cv2.destroyAllWindows()

