import numpy as np
import math
import cv2
#Start by checking hand profile
#THink about 1
cap = cv2.VideoCapture(0)
areaglobal=0
oldlen=0
permieter=0
def angle(start,end,apex):
    dotProd=(start[0]-apex[0])*(end[0]-apex[0]) + (start[1]-apex[1])*(end[1]-apex[1])
    len1=math.sqrt((start[0]-apex[0])*(start[0]-apex[0])+(start[1]-apex[1])*(start[1]-apex[1]))
    len2=math.sqrt((end[0]-apex[0])*(end[0]-apex[0])+(end[1]-apex[1])*(end[1]-apex[1]))
    return math.acos(dotProd/(len1*len2))
def distance(start,end):
    return math.sqrt((start[0]-end[0])*(start[0]-end[0])+(start[1]-end[1])*(start[1]-end[1]))

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
    #cv2.drawContours(frame, [cnt], 0, (255,0,0), 2)
    approx=cv2.convexHull(cnt,returnPoints=False)
    defects=cv2.convexityDefects(cnt,approx)
    count=0;
    angles=[]
    depthA=[]
    startA=[]
    endA=[]
    apexA=[]
    for i in range(defects.shape[0]):
        s,e,f,d = defects[i,0]
        if d>10000:
            start = tuple(cnt[s][0])
            end = tuple(cnt[e][0])
            far = tuple(cnt[f][0])
            angleRad=angle(start,end,far)
            if angleRad<(3.14/3):
                count=count+1
                depthA.append(d)
                angles.append(angleRad)
                endA.append(end)
                apexA.append(far)
                startA.append(start)
                cv2.line(frame,start,end,[0,255,0],2)
                cv2.circle(frame,end,5,[0,0,255],-1)
                cv2.circle(frame,start,5,[0,0,255],-1)
                cv2.circle(frame,far,5,[0,0,255],-1)
    #cv2.polylines(frame,[approx],True,(255,0,0))
    #cv2.imshow('frame',thresh)
    cv2.imshow('image',frame)
    #cv2.imshow('thresh',thresh2)
    average=0.0
    if cv2.waitKey(1) & 0xFF == ord('q'):
        for i in range(len(startA)):
            d=distance(startA[i],endA[i])
            #print d
            average+=d
        #d=d/len()
        count=count+1;
        #print defects;
        print count;
    	break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()


