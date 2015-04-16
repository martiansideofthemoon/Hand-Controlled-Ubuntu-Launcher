import numpy as np
import cv2

cap = cv2.VideoCapture(0)
areaglobal=0
oldlen=0
permieter=0
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    # Our operations on the frame come her
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    ret,thresh = cv2.threshold(gray,90,255,cv2.THRESH_BINARY_INV)
    ret2,thresh2 = cv2.threshold(gray,90,255,cv2.THRESH_BINARY_INV)
    contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    # Display the resulting frame
    #cnt=contours[0]
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
    approx=cv2.convexHull(cnt,returnPoints=False)
    defects=cv2.convexityDefects(cnt,approx)
    #print defects
    if len(approx)!=oldlen:
        #print len(approx)
        oldlen=len(approx)
    print len(range(defects.shape[0]))
    for i in range(defects.shape[0]):
        s,e,f,d = defects[i,0]
        start = tuple(cnt[s][0])
        end = tuple(cnt[e][0])
        far = tuple(cnt[f][0])
        cv2.line(frame,start,end,[0,255,0],2)
        cv2.circle(frame,far,5,[0,0,255],-1)
    #cv2.polylines(frame,[approx],True,(255,0,0))
    #cv2.imshow('frame',thresh)
    cv2.imshow('image',frame)
    cv2.imshow('thresh',thresh2)

    if cv2.waitKey(1) & 0xFF == ord('q'):
    	
    	break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()