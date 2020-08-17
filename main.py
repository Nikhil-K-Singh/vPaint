"""


"""

import cv2
import numpy as np

framewidth  = 640
frameheight = 480

cap = cv2.VideoCapture(0)
cap.set(3, framewidth)
cap.set(4, frameheight)
cap.set(10, 150)


# you need to set the color values
# for your objects to be tracked
# here the color are sored as HSV values
# with lower and upper limits

#  remember that myColors is in Hmin,Smin,Vmin,Hmax,Smax,Vmax


myColors = [
    [5,107,0,19,255,255],
    [133,56,0,159,156,255],
    [57,76,0,100,255,255]
]

# Can add / remove as many colors to track 

# below list is to mark the drawing pointer
# on the screen with the same color
# below myColorValues is in BGR

myColorValues=[
    [51,153,255],
    [255,0,255],
    [0,255,0],
]

## make sure that myColors and myColorValues should have the same color reference at teh same index
# ex index 0 for both is for orange 



myPoints = []       ## [x,y,colorId]

def drawOnCanvas(myPoints,myColorValues):
    for point in myPoints:
        cv2.circle(img,point[0],point[1],10, myColorValues[point[2]],cv2.FILLED)


def find_color(img,myColors,myColorValues):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    count=0
    for color in myColors:
        lower = np.array(myColors[0][0:3])
        upper = np.array(myColors[0][3:6])
        mask = cv2.inRange(imgHSV,lower,upper)

        x,y = getContours(mask)
        cv2.circle(imgResult,(x,y),10,myColorValues[count],cv2.FILLED)
        if x!=0 and y!=0:
            newPoints.append([x,y,count])
        count+=1
    return newPoints
    
def getContours(img):
    contours, hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    x,y,w,h = 0,0,0,0

    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area >500:
            peri = cv2.arcLength(cnt,True)
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)
            x,y,w,h = cv2.boundingRect(approx)
    return x+w//2,y


while True:
    success,img = cap.read()
    imgResult = img.copy()
    newPoints = find_color(img,myColors,myColorValues)

    if len(newPoints)!=0:
        for newP in newPoints:
            myPoints.append(newP)

    if len(myPoints)!=0:
        drawOnCanvas(myPoints,myColorValues)

    cv2.imshow("Result",imgResult)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break