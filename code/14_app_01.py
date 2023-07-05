# Simple Background Estimation in Videos

import numpy as np
import cv2
from skimage import data,filters

#open video
cap = cv2.VideoCapture('Resources/output_video_from_camera.mp4')

####################################### Background Estimation ####################################################
# Randomly selects 25 frames
frameIds = cap.get(cv2.CAP_PROP_FRAME_COUNT) * np.random.uniform(size=25)

# store selected frames in an array
frames = []
for fid in frameIds:
    cap.set(cv2.CAP_PROP_POS_FRAMES,fid)#reset frame ids as fid
    ret,frame = cap.read()
    frames.append(frame)

# Calculate median along the time axis
medianFrame = np.median(frames,axis=0).astype(dtype=np.uint8)

# Display median filter
cv2.imshow('Frame',medianFrame)
cv2.waitKey(0)

"""
OBSERVATION: As you can see, we randomly select 25 frames and calculate the median of every pixel over the 25 frames. 
This median frame is a good estimate of the background as long as every pixel sees the background at least 50% of the time.
"""

################################################# Frame differencing #####################################################
"""
This is accomplished in the following steps

1.Convert the median frame to grayscale.
2.Loop over all frames in the video. Extract the current frame and convert it to grayscale.
3.Calcualte the absolute difference between the current frame and the median frame.
4.Threshold the above image to remove noise and binarize the output.
"""

cap.set(cv2.CAP_PROP_POS_FRAMES,0)#reset frame number to 0
grayMedianFrame = cv2.cvtColor(medianFrame,cv2.COLOR_BGR2GRAY)

#loop over all frames
ret = True
while(ret):
    ret,frame = cap.read()
    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)#step 2
    dframe = cv2.absdiff(frame,grayMedianFrame)#step 3
    th,dframe = cv2.threshold(dframe,30,255,cv2.THRESH_BINARY)#step 4

    cv2.imshow('frame',dframe)
    cv2.waitKey(20)

cap.release()
cv2.destroyAllWindows()                

