import numpy as np
import cv2

cap = cv2.VideoCapture(0)
areaglobal=0
permieter=0
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    # Our operations on the frame come her
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    ret,thresh = cv2.threshold(gray,130,255,0)
    ret2,thresh2 = cv2.threshold(gray,130,180,0)
    contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    # Display the resulting frame
    #cnt=contours[0]
    global cnt
    for i in contours:
    	area=cv2.contourArea(i)
    	if area>1000:
    		cnt=i
    if abs(areaglobal-cv2.contourArea(cnt))>5500 :
        print cv2.contourArea(cnt)
        print cv2.arcLength(cnt,True)
        areaglobal=cv2.contourArea(cnt)
        perimeter=cv2.arcLength(cnt,True)
    #cv2.drawContours(frame, [cnt], 0, (255,0,0), 2)
    approx=cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True)
    cv2.polylines(frame,[approx],True,(255,0,0))
    #cv2.imshow('frame',thresh)
    cv2.imshow('image',frame)
    #cv2.imshow('thresh',thresh2)

    if cv2.waitKey(1) & 0xFF == ord('q'):
    	
    	break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()