import cv2 as cv

img = cv.imread('ShadowRemoval1.jpg')
img = cv.resize(img, (500, 500), interpolation=cv.INTER_AREA)
cv.imshow('Shadows', img)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(gray, 60, 200, cv.THRESH_BINARY)
cv.imshow('Binary', thresh)

cv.waitKey(0)