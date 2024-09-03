import cv2 as cv

img= cv.imread('/home/daniel/Documents/openCV learning material/photos/Capture.PNG')
cv.imshow('Daniel', img)

gray= cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

threshold, thresh = cv.threshold(gray, 225, 255, cv.THRESH_BINARY)
cv.imshow('simple threshold', thresh)

threshold, thresh_inv = cv.threshold(gray, 225, 255, cv.THRESH_BINARY_INV)
cv.imshow('inverse threshold', thresh_inv)

adaptive_thresh= cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 9)
cv.imshow('adaptive threshold', adaptive_thresh)

cv.waitKey(0)