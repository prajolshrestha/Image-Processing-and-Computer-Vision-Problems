#Object Detection in Image using OpenCV DNN

import cv2
import numpy as np

#1.load class names
with open('Resources\input_app_02\object_detection_classes_coco.txt','r') as f:
    class_names = f.read().split('\n')

#get different color array for each of the classes
COLORS = np.random.uniform(0,255,size=(len(class_names),3)) # holds tuples of three integer values #helps to draw diff. bounding box for each class

#2.load MobileNet SSD model
model = cv2.dnn.readNet(model="Resources/input_app_02/frozen_inference_graph.pb",config='Resources\input_app_02\ssd_mobilenet_v2_coco_2018_03_29.pbtxt.txt',framework='Tensorflow',)

#3.load image and prepare input blob
image = cv2.imread('Resources\input_app_02\image_2.jpg')
image_height, image_width,_ = image.shape

blob = cv2.dnn.blobFromImage(image = image, size=(300,300),mean=(104,117,123),swapRB=True)

#4. Inference
model.setInput(blob)
output = model.forward()

print(output,output.shape)#(1, 1, 100, 7)
"""
output[1] = [ 0.00000000e+00  3.10000000e+01  4.20008786e-02  6.94068909e-01 6.96970642e-01  7.35175729e-01  8.56598675e-01]
Here, index position 1 contains the class label, which can be from 1 to 80. 
Index position 2 contains the confidence score. This is not a probability score but rather the model’s confidence for the object belonging to the class that it has detected.
Of the final four values, the first two are x, y bounding box coordinates, and the last is the bounding box’s width and height.
"""

############ Looping Over the Detections and Drawing the Bounding Boxes ####################
for detection in output[0,0,:,:]: #loop over detection
    confidence = detection[2]
    #draw bounding box if detection confidence is above´certain threshold
    if confidence > .4:
        #get the class id
        class_id = detection[1]
        # map the class id with the class
        class_name = class_names[int(class_id)-1]
        color = COLORS[int(class_id)]
        #get the bounding box coordinates
        box_x = detection[3] * image_width
        box_y = detection[4] * image_height
        #get the bounding box width and height
        box_width = detection[5] * image_width
        box_height = detection[6] * image_height

        # draw a rectangle around each detected object
        cv2.rectangle(image,(int(box_x),int(box_y)),(int(box_width),int(box_height)),color,thickness=2)
        #put fps text on top of the frame
        cv2.putText(image,class_name,(int(box_x),int(box_y - 5)),cv2.FONT_HERSHEY_SIMPLEX,1,color,1)

cv2.imshow('image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()   
