import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img= cv.imread('/home/daniel/Documents/openCV learning material/photos/Capture.PNG')
cv.imshow('Daniel', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

gray_hist= cv.calcHist([gray], [0], None, [256], [0,256])

plt.figure()
plt.title('colour Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
colours= ('b', 'g', 'r')

for i, col in enumerate(colours):
    hist = cv.calcHist([img], [i], None, [256], [0,256])
    plt.plot(hist, color=col)
    plt.xlim([0,256])

plt.show()

cv.waitKey(0)