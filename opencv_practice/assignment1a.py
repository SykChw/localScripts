import cv2 as cv
import numpy as np

img = cv.imread('BookCount_1.jpeg')

cv.imshow('Books', img)


# Converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Blur
blur = cv.GaussianBlur(gray, (7, 7), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

scratch_mask = gray - blur
cv.imshow('scratch_mask', scratch_mask)

eroded = cv.erode(scratch_mask, (7, 7), iterations=10)
cv.imshow('eroded_scratch_mask', eroded)

# Edge Cascade
canny = cv.Canny(blur, 100, 175)
cv.imshow('Edges', canny)


cv.waitKey(0)