import cv2 as cv

img= cv.imread('/home/daniel/Documents/openCV learning material/photos/Capture.PNG')
cv.imshow('daniel', img)

average=cv.blur(img, (7,7))
cv.imshow('average', average)

median= cv.medianBlur(img, 7)
cv.imshow('Median Blur', median)

bilateral= cv.bilateralFilter(img, 10, 35, 25)
cv.imshow('Bilateral', bilateral)

cv.waitKey(0)