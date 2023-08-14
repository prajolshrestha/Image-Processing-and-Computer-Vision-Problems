#Object Detection in Videos using OpenCV DNN

import cv2
import numpy as np
import time

#1.load class names
with open('Resources/input_app_02/object_detection_classes_coco.txt','r') as f:
    class_names = f.read().split('\n')

COLORS = np.random.uniform(0,255,size=(len(class_names),3))

#2.load model
model = cv2.dnn.readNet(model='Resources/input_app_02/frozen_inference_graph.pb',
                        config='Resources/input_app_02/ssd_mobilenet_v2_coco_2018_03_29.pbtxt.txt',
                        framework='Tensorflow')
#inference on GPU if avilable else CPU
model.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
model.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA)

#3.load video
#cap = cv2.VideoCapture('Resources/input_app_02/video_1.mp4')
cap = cv2.VideoCapture(0)

frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
out = cv2.VideoWriter('Resources/input_app_02/video_result.mp4',cv2.VideoWriter_fourcc(*'mp4v'),30,(frame_width,frame_height))

########################Looping Over the Video Frames and Detecting Objects in Each Frame ############
while cap.isOpened():
    ret,frame = cap.read()
    if ret:
        image = frame
        image_height,image_width,_ = image.shape
        # create blob
        blob = cv2.dnn.blobFromImage(image=image,size=(300,300),mean=(104,117,123),swapRB=True)
        #inference
        start = time.time()
        model.setInput(blob)
        output = model.forward()
        end = time.time()
        #calculate fps
        fps = 1/(end-start)
        #loop over each of detection
        for detection in output[0,0,:,:]:
            confidence = detection[2] # confidence
            if confidence > .4:
                class_id = detection[1]#class id
                class_name = class_names[int(class_id)-1]
                color = COLORS[int(class_id)-1]
                #bounding box coordinates
                box_x = detection[3] * image_width
                box_y = detection[4] * image_height
                # bounding box width and height
                box_width = detection[5] * image_width
                box_height = detection[6] * image_height
                #draw rectangle
                cv2.rectangle(image,(int(box_x),int(box_y)),(int(box_width),int(box_height)),color,thickness=2)
                #put text
                cv2.putText(image,class_name,(int(box_x),int(box_y - 5)),cv2.FONT_HERSHEY_SIMPLEX,1,color,2)
                cv2.putText(image,f"{fps:.2f} FPS",(20,30),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)


        cv2.imshow('image',image)
        #out.write(image)#save to disk
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
