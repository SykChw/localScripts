import cv2 as cv

img = cv.imread('BookCount_1.jpeg')

cv.imshow('Books', img)

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

# Converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Blur
blur = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

# Edge Cascade
canny = cv.Canny(blur, 100, 175)
cv.imshow('Edges', canny)

# Dilate the images
dilated = cv.dilate(canny, (7, 7), iterations=1)
##cv.imshow('Dilated', dilated)

# Eroding (inverse of dilating)
eroded = cv.erode(dilated, (7, 7), iterations=1)
##cv.imshow('Eroded', eroded)

# Resize
resize = cv.resize(img, (500, 500), interpolation=cv.INTER_AREA)
# INTER_AREA use this interpolation when shrinking the image
# INTER_LINEAR used when enlarging the image size; INTER_CUBIC gives higher quality (&slower) interpolation than INTER_LINEAR
##cv.imshow('Resized', resize)

# Cropping
cropped = img[20:200, 50:200]
##cv.imshow('Cropped', cropped)



cv.waitKey(0)