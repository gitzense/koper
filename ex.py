import numpy as np
import cv2
 
cap = cv2.VideoCapture('videos/2.mp4')
# ret = cap.set(3, 640) # set frame width
# ret = cap.set(4, 480) # set frame height
font = cv2.FONT_HERSHEY_SIMPLEX # Set font style
kernel = np.ones((5, 5), np.uint8) # Convolution kernel
 
if cap.isOpened() is True: # Check whether the camera is started normally
    while(True):
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # Convert to gray channel
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) # Convert to HSV space
 
        lower = np.array([0, 120, 0])
        upper = np.array([179, 255, 255])

        mask = cv2.inRange(hsv, lower, upper) 
        opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel) 
        bila = cv2.bilateralFilter(mask, 10, 200, 200) 
        edges = cv2.Canny(opening, 50, 100)
                 
        circles = cv2.HoughCircles(edges, cv2.HOUGH_GRADIENT, 1.8, minDist=20, param1=50, param2=45, minRadius=20, maxRadius=35)

        if circles is not None: 
            for circle in circles[0]:   
                x = int(circle[0])
                y = int(circle[1])
                r = int(circle[2])
                cv2.circle(frame, (x, y), r, (0, 0, 255), 3) 
                cv2.circle(frame, (x, y), 3, (255, 255, 0), -1) 
                text = 'x:  '+str(x)+' y:  '+str(y)
                cv2.putText(frame, text, (10, 30), font, 1, (0, 255, 0), 2, cv2.LINE_AA, 0)
        else:
            cv2.putText(frame, 'x: None y: None', (10, 30), font, 1, (0, 255, 0), 2, cv2.LINE_AA, 0)
        cv2.imshow('frame', frame)
        # cv2.imshow('mask', mask)
        cv2.imshow('edges', edges)
        k = cv2.waitKey(5) & 0xFF

        if k == 27:
            break

    cap.release()
    cv2.destroyAllWindows()
else:
    print('cap is not opened!')