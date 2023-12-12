import cv2 as cv
import numpy as np 
import datetime as dt 
import math 

img = cv.imread('imgs/4.jpg')
img = cv.resize(img, (int(img.shape[1]*0.7), int(img.shape[0]*0.7)))
kernel = np.ones((5, 5), np.uint8)

lower = np.array([0, 120, 0])
upper = np.array([179, 255, 255])

while True:
    gray = hsv = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

    mask = cv.inRange(hsv, lower, upper)
    output = cv.bitwise_and(img,img, mask=mask) 

    opening = cv.morphologyEx(mask, cv.MORPH_OPEN, kernel)
    edges = cv.Canny(opening, 50, 100)

    circles = cv.HoughCircles(edges, cv.HOUGH_GRADIENT, 2, minDist=20, param1=50, param2=33, minRadius=0, maxRadius=0)
    circles = np.uint16(np.around(circles))

    # n = 0
    # for i in circles[0, :]: 
    #     cv.circle(img, (i[0], i[1]), i[2], (0, 255, 0), 1)
    #     cv.circle(img, (i[0], i[1]), 2, (0, 0, 255), 1)
    #     print(f'x{n}: {i[0]}, y{n}: {i[1]}')
    #     n += 1

    y0 = 0
    for i in circles[0, :]: 
        cv.circle(img, (i[0], i[1]), i[2], (0, 255, 0), 2)
        cv.circle(img, (i[0], i[1]), 2, (0, 0, 255), 3)
        if y0 < i[1]:
            x0 = i[0]
            y0 = i[1]
    print(x0, y0)
    Ymax1 = img.shape[0]
    Ymax2 = img.shape[0]
    for i in circles[0, :]:
        if i[0] != x0 and i[1] != y0:
            if x0 <= i[0] and Ymax1 > (int(y0) - int(i[1])):
                # cv.line(img, (x0, y0), (i[0], i[1]), (255, 0, 0), 2)
                Ymax1 = int(y0) - int(i[1]) 
            elif x0 > i[0] and Ymax2 > (int(y0) - int(i[1])):
                # cv.line(img, (x0, y0), (i[0], i[1]), (255, 0, 0), 2)
                Ymax2 = int(y0) - int(i[1])
    print(Ymax1, Ymax2)

    cv.imshow('image',img)
    cv.imshow('edges',edges)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cv.destroyAllWindows()    