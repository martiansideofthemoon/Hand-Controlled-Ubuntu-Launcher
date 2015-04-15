import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    # Our operations on the frame come her
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    ret,thresh = cv2.threshold(gray,127,255,0)
    contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    # Display the resulting frame
    image = cv2.drawContours(gray, contours, -1, (0,255,0), 3)
    cv2.imshow('frame',gray)
    cv2.imshow('image',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
    	break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()