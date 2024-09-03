import cv2 as cv
import numpy as np


img=cv.imread('/home/daniel/Documents/openCV learning material/photos/Capture.PNG')

cv.imshow('daniel', img)

gray= cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

blank= np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank', blank)

canny= cv.Canny(img, 125, 125)
cv.imshow('Canny Edges', canny)

contours, hierarchies= cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contour(s) found')

cv.drawContours(blank, contours,-1, (0,0,255), 1)
cv.imshow('Countours Drawn', blank)
cv.waitKey()
