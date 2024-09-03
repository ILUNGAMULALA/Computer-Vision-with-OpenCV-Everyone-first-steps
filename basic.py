import cv2 as cv

img=cv.imread('/home/daniel/Documents/openCV learning material/photos/Capture.PNG')
cv.imshow('Daniel', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

blur= cv.GaussianBlur(img, (3,3),cv.BORDER_DEFAULT)
cv.imshow('blur', blur)

canny= cv.Canny(img, 125, 175)
cv.imshow('canny', canny)

dilated= cv.dilate(canny, (7,7), iterations=1)
cv.imshow('Dilated image', dilated)

resized= cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('resized',resized)

cv.waitKey(0)