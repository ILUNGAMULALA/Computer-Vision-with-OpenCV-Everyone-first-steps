import cv2 as cv
import matplotlib.pyplot as plt

img= cv.imread('/home/daniel/Documents/openCV learning material/photos/Capture.PNG')
cv.imshow('Daniel', img)

gray= cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

hsv=cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

lab=cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('LAB', lab)

rgb= cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)

plt.imshow(rgb)
plt.show()

cv.waitKey(0)