import cv2 as cv
import numpy as np 
import datetime as dt 

cap = cv.VideoCapture('videos/1.mp4')
# ret = cap.set(3, 720) # set frame width
# ret = cap.set(4, 1280) # set frame height
kernel = np.ones((5, 5), np.uint8)

Ymax1 = Ymax2 = 1280

Ym1 = [0]
Ym2 = [0]

if cap.isOpened() is True:
    while True:
        ret, frame = cap.read()

        # dim = (int(frame.shape[1]*0.7), int(frame.shape[0]*0.7))
        # frame = cv.resize(frame, dim)

        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV) 
    
        lower = np.array([0, 120, 0])
        upper = np.array([179, 255, 255])

        mask = cv.inRange(hsv, lower, upper) 
        opening = cv.morphologyEx(mask, cv.MORPH_OPEN, kernel) 
        bila = cv.bilateralFilter(mask, 10, 200, 200) 
        edges = cv.Canny(opening, 50, 100)

        circles = cv.HoughCircles(edges, cv.HOUGH_GRADIENT, 2, minDist=20, param1=50, param2=50, minRadius=0, maxRadius=50)
        circles = np.uint16(np.around(circles))

        x0 = 0
        y0 = 0
        if circles is not None:
            for i in circles[0, :]: 
                cv.circle(frame, (i[0], i[1]), i[2], (0, 255, 0), 2)
                cv.circle(frame, (i[0], i[1]), 2, (0, 0, 255), 3)
                if y0 < i[1]:
                    x0 = i[0]
                    y0 = i[1]
            # print(x0, y0)
            Ymax1 = frame.shape[0]
            Ymax2 = frame.shape[0]
            for i in circles[0, :]:
                if i[0] != x0 and i[1] != y0:
                    if x0 <= i[0] and Ymax1 > (int(y0) - int(i[1])):
                        # cv.line(frame, (x0, y0), (i[0], i[1]), (255, 0, 0), 2)
                        Ymax1 = int(y0) - int(i[1])
                        Ym1.append(int(Ymax1))
                    elif x0 > i[0] and Ymax2 > (int(y0) - int(i[1])):
                        # cv.line(frame, (x0, y0), (i[0], i[1]), (255, 0, 0), 2)
                        Ymax2 = int(y0) - int(i[1])
                        Ym2.append(int(Ymax2))
            print('Начальная высота: ', max(Ym1), ' / ','Высота поднятия: ', max(Ym2))

        cv.imshow('Koper video', frame)
        cv.imshow('Edges', edges)

        cv.waitKey(100)

        if cv.waitKey(1) & 0xFF==ord('q'):
            break

cv.destroyAllWindows()

