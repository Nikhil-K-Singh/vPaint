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

#  remember it is in BGR
myColors = [
    [5,107,0,19,255,255],
    [133,56,0,159,156,255],
    [57,76,0,100,255,255]
]
# Can add / remove as many colors to track 

# below list is to mark the drawing pointer
# on the screen with the same color

myColorValues=[
    [51,153,255],
    [255,0,255],
    [0,255,0]
]


def find_color(img,myColors,myColorValues):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    count=0
    for color in myColors:
        lower = np.array(myColors[0][0:3])
        upper = np.array(myColors[0][3:6])
        mask = cv2.inRange(imgHSV,lower,upper)

        x,y = getContours(mask)
        cv2.circle(imgResult,(x,y),10,myColorValues[count],cv2.FILLED)
        count+=1

def getContours(img):
    pass


while True:
    success,img = cap.read()
    find_color(img,myColors)
    cv2.imshow("Result",img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break