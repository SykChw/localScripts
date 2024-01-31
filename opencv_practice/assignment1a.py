import cv2 as cv

img = cv.imread('BookCount_1.jpeg')

cv.imshow('Books', img)


# Converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Blur
blur = cv.GaussianBlur(img, (5, 5), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

# Edge Cascade
canny = cv.Canny(blur, 100, 175)
cv.imshow('Edges', canny)


cv.waitKey(0)