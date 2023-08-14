import cv2

cap = cv2.VideoCapture(0)#Video object

#when 'q' key is clicked image is saved 
while (cap.isOpened()):
    ret,frame = cap.read()#read framesq
    cv2.imshow('Captured image',frame )
    
    k = cv2.waitKey(20)
    if k == ord('q'):
        cv2.destroyAllWindows()
        cv2.imwrite('Resources/captured_image.jpg',frame)
        cv2.imshow('Captured image',frame )
        cv2.waitKey(0)
        break