"""
OpenCV DNN Module Supports:

-Image classification.
-Object Detection.
-Image segmentation.
-Text detection and recognition.
-Pose estimation.
-Depth estimation.
-Person and face verification and detection.
-Person Reid.
"""

# Image Classification
"""
Steps:
1.Load the class names text file from the disk and extract the required labels.
2.Load the pre-trained neural network model from disk.
3.Load the image from the disk and prepare the image to be in the correct input format for the deep learning model.
4.Forward propagate the input image through the model and obtain the outputs.
"""
import cv2
import numpy as np

#1. read imageNet class names
with open('Resources/input_app_02/classification_classes_ILSVRC2012.txt','r') as f:
    image_net_names = f.read().split('\n')

class_names = [name.split(',')[0] for name in image_net_names]#final class name
print(class_names)

#2. load pre-trained weights and configuration file (NN model)
model = cv2.dnn.readNet(model='Resources\input_app_02\DenseNet_121.caffemodel',config='Resources/input_app_02/DenseNet_121.prototxt',framework='caffe')

#3.load image
image = cv2.imread('Resources\input_app_02\image_1.jpg')
#blobFromImage() function prepares the image in the correct format to be fed into the mode
blob = cv2.dnn.blobFromImage(image=image,scalefactor=0.01,size=(224,224),mean=(104,117,123)) #create blob from image

#4.Prediction
model.setInput(blob)
outputs = model.forward()

############### Output ##########################
final_outputs = outputs[0]
final_outputs = final_outputs.reshape(1000,1)#1D banako

label_id = np.argmax(final_outputs)#class label

probs = np.exp(final_outputs) / np.sum(np.exp(final_outputs))# convert the output scores to softmax probabilities
final_prob = np.max(probs) * 100. #final heighest probability

# map the max confidence to the class label names
out_name = class_names[label_id]
out_text = f"{out_name},{final_prob:.3f}"

#put class name text on top of the image
cv2.putText(image,out_text,(25,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
cv2.imshow('image',image)
cv2.waitKey(0)

