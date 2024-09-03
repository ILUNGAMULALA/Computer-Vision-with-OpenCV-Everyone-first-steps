import cv2 as cv

img= cv.imread('/home/daniel/Documents/openCV learning material/photos/florence and husband.JPG')

resized= cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('resized',resized)

gray=cv.cvtColor(resized, cv.COLOR_BGR2GRAY)
cv.imshow('Gray Person', gray)

haar_cascade = cv.CascadeClassifier('/home/daniel/Documents/openCV learning material/haar_face.xml')
faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

print(f'Number of faces in the images are = {len(faces_rect)}')

for (x, y, w, h) in faces_rect:
    cv.rectangle(resized, (x,y), (x+w, y+h), (0,255,0), thickness=2)

cv.imshow('Detected Faces', resized)
cv.waitKey(0)