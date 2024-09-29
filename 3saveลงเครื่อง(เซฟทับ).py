'''saveลงเครื่อง(เซฟทับ)'''

import numpy as np
import cv2
import datetime


hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

cv2.startWindowThread()
cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()
    frame = cv2.resize(frame, (1280, 720))
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    boxes, weights = hog.detectMultiScale(frame, winStride=(8,8) )


    for(x,y,w,h) in boxes:
        cv2.rectangle(frame, (x,y),(x+w,y+h),(255,0,0),2)
        org = (x+10, y)  
        font = cv2.FONT_HERSHEY_SIMPLEX
        fontScale = 1
        color = (255, 0, 0)  
        thickness = 2
        cv2.putText(frame,"Person", org, font, fontScale, color, thickness, cv2.LINE_AA)
        
    cv2.imwrite(".\\Folder_Result\\result.jpg",frame)
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
cv2.waitKey(1)