"""how to read, display and write videos from a file, an image sequence and a webcam?

1. cv2.VideoCapture – Creates a video capture object, which would help stream or display the video.
2. cv2.VideoWriter – Saves the output video to a directory.
3. In addition, we also discuss other needed functions 
   such as cv2.imshow(), cv2.waitKey() and the get() method 
   which is used to read the video metadata such as frame height, width, fps etc.
"""
import cv2

#Video Capture Object
vid_capture = cv2.VideoCapture(0,cv2.CAP_DSHOW)#webcam used

if (vid_capture.isOpened() == False):
    print('Error opening video')

fps = 24
frame_width = int(vid_capture.get(3))
frame_height = int(vid_capture.get(4))
frame_size = (frame_width,frame_height)

#Video Writer Object
output = cv2.VideoWriter('Resources/output_video_from_camera.mp4',cv2.VideoWriter_fourcc(*'XVID'),20,frame_size)

#Main loop
while(vid_capture.isOpened()):
    ret,frame = vid_capture.read() #READ VIDEO

    if ret == True:
        output.write(frame) # WRITE VIDEO
        cv2.imshow('Frames',frame) #Display VIDEO

        key = cv2.waitKey(20)
        if key == ord('q'):
            print('Your Video has been saved.')
            break
    
    else:
        print('Web cam disconnected')
        break

vid_capture.release()
output.release()
cv2.destroyAllWindows()

