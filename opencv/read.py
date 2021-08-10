"""(VİDEO OYNATMA)"""
import cv2 as cv

capture = cv.VideoCapture('videolar/dog.mp4')

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video',frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()

"""(FOTOĞRAF GÖRÜNTÜLEME)
import cv2 as cv
img = cv.imread('fotograf/cat.jpg')
cv.imshow('cat',img)
cv.waitKey(0)"""





