import numpy as np
import math
import cv2
#Start by checking hand profile
#THink about 1
cap = cv2.VideoCapture(0)
points = [(280,220),(300,220),(300,250),(270,300),(300,320),(320,300),(290,410),(310,400),(330,400),(280,350),(305,360),(330,355)]
#points = [(300,300)]
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    images=[]
    # Our operations on the frame come her
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    counter=0
    for i in points:
        cv2.circle(frame,i,5,[0,0,255],-1)
        ret2,thresh2 = cv2.threshold(gray,gray[i]-1,255,cv2.THRESH_BINARY)
        ret2,thresh3 = cv2.threshold(gray,gray[i]+1,255,cv2.THRESH_BINARY_INV)
        final = cv2.bitwise_and(thresh2,thresh3)
        images.append(final)
    final_added=images[0]
    for i in images:
        final_added=cv2.add(final_added,i)
    cv2.imshow('img without blur',final_added)
    final_added2=cv2.medianBlur(final_added,35)
    cv2.imshow('image',frame)
    cv2.imshow('image2',final_added2)
    th2 = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY,11,2)
    cv2.imshow('adaptiveThreshold',th2)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break;
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()


