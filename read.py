import cv2 as cv

img= cv.imread('photos/Capture.PNG')

def rescaleFrame(frame, scale=0.20):
    width = int(frame.shape[1]*scale)
    height= int(frame.shape[0]*scale)

    dimensions=(width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

resized_image=rescaleFrame(img)
cv.imshow('Daniel', resized_image)



'''capture= cv.VideoCapture('/home/daniel/Documents/openCV learning material/Videos/Sorry____Halsey_Lyrics(720p).mp4')

while True:
    isTrue, frame=capture.read()
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()'''

cv.waitKey(0)

