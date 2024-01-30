import cv2 as cv

img = cv.imread('BookCount_1.jpeg')

cv.imshow('Books', img)
cv.waitKey(0)
'''
#Reading videos
capture = cv.VideoCapture('/home/sayak/Downloads/KillersOfTheFlowerMoon/Killers.Of.The.Flower.Moon.2023.720p.WEBRip.x264.AAC-[YTS.MX].mp4')

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    if cv.waitKey(20) and 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()
'''

