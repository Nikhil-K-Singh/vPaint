import cv2

framewidth  = 640
frameheight = 480

cap = cv2.VideoCapture(0)
cap.set(3, framewidth)
cap.set(4, frameheight)
cap.set(10, 150)

while True:
    success,img = cap.read()
    cv2.imshow("Result",img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break